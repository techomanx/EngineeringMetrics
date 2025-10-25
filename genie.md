# genie platform review notes

## what's missing / broken

### payments - only UK stuff works
- FPS and Bacs only, no international 
- SWIFT/SEPA in backlog but not live
- examples all show GBP, paymentScheme: FPS
- balance endpoints have currency codes but no FX flows exposed

### cards - debit only, no credit 
- using Paymentology for processing
- Mastercard partnership 
- no native credit card engine
- missing: billing cycles, chargebacks, scheme fees

### not integrated with group payments yet
- "FY-25 plan to explore with Payments Services & Tech CoE Q1"
- can't reuse existing rails

### limited product builder
- current accounts, savings, term loans work fine
- missing credit card specific stuff

## tech issues

### single region risk
- AWS multi-AZ but no active-active cross-region
- S3 + GCP backups but still single point of failure for full region outage

### monitoring migration in progress  
- moving from Honeycomb to OpenTelemetry + Datadog
- gaps during transition

### auth is chatty for server-to-server
- 2-step JWT with 60s tokens = lots of round trips
- they know it's "inefficient for system-system communication"
- mTLS + Istio/OPA planned but not ready

### webhooks = more client work
- at-least-once delivery 
- clients need retry/recovery logic
- 30-day fetch window for missed events

### no performance numbers
- availability stats but no TPS/latency under load
- credit decisions target 10-20s (fine for lending, not card auth)

### vendor risk
- Form3 (payments), Paymentology (cards), FeatureSpace (ARIC) 
- availability depends on external services

### DX still rough
- schema drifts happening
- FAQ needed = not self-serve yet
- sandbox + Bank of APIs but not seamless

## TODO fix list

- [ ] ship mTLS auth, kill JWT token dance
- [ ] multi-region setup + DR drills  
- [ ] SWIFT/SEPA behind same API as FPS
- [ ] publish real perf SLOs (p50/p95/p99, TPS)
- [ ] lock down API schemas, better DX docs