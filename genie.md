# Genie Platform Analysis

## Functional Gaps

### Cross-border payments & multi-currency (not live)

What's shipped today is UK domestic FPS and Bacs; API payloads and examples show paymentScheme: FPS and GBP amounts, and the "Make FPS payment" endpoints only.

The backlog explicitly calls out SWIFT and SEPA (i.e., planned, not available).

Balances carry a currency code (examples are GBP; doc notes "cent for EUR"), but there's no exposed SEPA/SWIFT or FX workflow in the API guide.

### Cards scope (debit issuing, not credit)

Genie advertises debit cards with Mastercard sponsorship and card processing via Paymentology; there's no evidence of a native credit card product engine or scheme settlement for credit issuing.

### Group payments connectivity

The deck notes "Not yet integrated… to Group Payments; FY-25 plan to explore with Payments Services & Tech CoE Q1", so broader rails reuse is still in flight.

### API journeys cover core deposits/lending, not complex issuing

The Product Definition "builder" cleanly composes current accounts, savings, term loans (features like UK interbank address, credit interest, statements). Nothing in scope for credit-card-specific constructs (cycles, statementing, chargebacks, scheme fees).

## Technical Gaps

### Regional resiliency posture

The platform is cloud-native on AWS with resiliency across Availability Zones, real-time backups to S3, and even GCP backups — but the material emphasizes AZ-level resilience; there's no evidence of active-active multi-region operations. That leaves a residual risk for a full-region event.

### Observability consolidation still in transition

Monitoring is standardizing on OpenTelemetry + Datadog with Honeycomb being deprecated; good direction, but it's an ongoing migration, which can create gaps during change.

### Auth/DX friction for server-to-server

Current auth uses a two-step JWT flow with 60-second resource tokens (fine-grained and secure), which the guide itself labels "inefficient for system-system communication." A planned move to mTLS + Istio/OPA is documented, but until that's live, integrators pay extra latency/chattiness cost.

### Asynchronous model puts more on the client

Webhook notifications are first-class (with retries, long-backoff, and 30-day fetch for missed events). That's solid, but it also implies at-least-once delivery semantics and recovery logic that clients must build/operate.

### Performance evidence is qualitative, not benchmarked

The deep-dive shows healthy availability and monthly volumes, but no published TPS/latency under load for payments/cards. The credit decisioning PRD targets 10–20s for the decisioning response and sets availability/NFRs for that micro-journey, which is fine for lending but not indicative of real-time card auth workloads.

### Third-party critical dependencies

Payments (Form3), card processing (Paymentology), and ARIC (FeatureSpace) are foundational. That's pragmatic, but it concentrates availability/capability risk outside Genie's direct control (and complicates change management and incident coordination).

### Developer experience still split across surfaces

Practical onboarding and testing leverage Bank of APIs + sandbox. Good signs (customers testing mTLS + private-key JWT + signatures; event notifications working), but the existence of schema drifts and the need for FAQs indicate the DX is improving but not seamless/self-serve yet.

## Targeted Remediations (Evidence-based)

1. **Ship the auth re-platform** - (mTLS + Istio/OPA) and deprecate short-lived resource JWTs for S2S paths to cut round-trips and reduce token-management overhead.

2. **Stand up multi-region active-active** - For the core ledger/payments edge and rehearse cross-region failover (DR drills), aligning NFRs with card-auth style expectations.

3. **Deliver SWIFT/SEPA rails + FX** - Behind the same product abstraction and UPV (Unified Payment View), keeping eventing and reconciliation consistent across schemes.

4. **Publish performance SLOs** - (p50/p95/p99 latency and TPS) for the main APIs under load; complement the availability stat with hard throughput numbers.

5. **DX hardening** - Lock API schemas (idempotency guidance, retry/backoff recipes, webhook signing), expand the sandbox regression packs, and finish the self-serve onboarding improvements already being tracked.