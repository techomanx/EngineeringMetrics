# Mainframe Integration Engineer (CICS/Db2 + IBM DataPower) — Payments
## INTERNAL REVIEW VERSION - Interview Guide & Assessment

**Location:** London (hybrid)
**Team:** Digital Channels / Bankline
**Type:** Contract
**Seniority:** Senior/Lead level (10-15 years experience)

---

## Quick Reference

**Must-Have (Non-Negotiable):**
- 10-12+ years mainframe (CICS, Db2, JCL) - Senior/Lead level
- 5+ years IBM DataPower gateway administration
- 5+ years z/OS Connect EE or similar API gateway
- 2+ years payment systems (ISO 20022, CHAPS, Faster Payments)

**Nice-to-Have (Bonus):**
- Enterprise Java (Spring Boot, Spring Framework) - 4+ years
- CICS Liberty (Java in CICS)
- AWS (Aurora PostgreSQL, API Gateway, cloud databases)
- TYK/Apigee
- Kafka/event streaming
- Multi-region cloud databases
- Infrastructure as Code (Terraform, CloudFormation)

---

## Interview Assessment Framework

### Round 1: Technical Screen (60 min) - Phone/Video

**Focus Areas:** Mainframe fundamentals, DataPower basics, payments knowledge

#### A. Mainframe Core (20 min)

**Q1: Explain the difference between COMMAREA and Channels/Containers in CICS.**

**Expected Answer:**
- COMMAREA: Legacy method, 32KB limit, single contiguous memory block, passed by value
- Channels/Containers: Modern approach, 16MB per container, multiple containers per channel, named data, supports BLOB/CLOB
- Channels allow structured data exchange, better for web services and modern APIs
- Good candidates will mention use cases for each

**Red Flags:**
- Can't explain the 32KB COMMAREA limit
- Doesn't know channels/containers (shows outdated knowledge)
- No practical experience with either

**Q2: You have a batch job running slow with a Db2 SQL step. Walk me through your troubleshooting approach.**

**Expected Answer:**
- Check EXPLAIN plan for the query (access path, index usage)
- Look for tablespace scans instead of index usage
- Review RUNSTATS currency (are statistics up to date?)
- Check for missing indexes on JOIN/WHERE columns
- Examine BIND parameters (ISOLATION level, package options)
- Review bufferpool configuration and hit ratios
- Consider REORG if fragmentation is high
- Check for lock contention (DEADLOCKS, TIMEOUTS)

**Strong candidates will:**
- Mention specific Db2 tools (EXPLAIN, RUNSTATS, REORG)
- Talk about monitoring (Db2 PM, SMF records)
- Discuss preventive measures

**Q3: What's the purpose of GDG (Generation Data Groups) and when would you use them?**

**Expected Answer:**
- Versioned dataset management - automatic rotation of datasets
- Each generation is a version (GDG base + relative generation number)
- Common uses: daily backup files, batch output archives, audit trails
- Example: PAYROLL.OUTPUT.G0001V00 (current), G0002V00 (previous)
- JCL references: (+1) for new, (0) for current, (-1) for previous
- LIMIT parameter controls retention (e.g., LIMIT(7) keeps 7 generations)

**Red Flags:**
- Confuses GDG with PDS
- Can't explain relative generation numbers
- No practical examples

#### B. IBM DataPower (15 min)

**Q4: What's the difference between MPGW and WS-Proxy in DataPower?**

**Expected Answer:**
- **Multi-Protocol Gateway (MPGW):** Protocol-agnostic, handles HTTP, HTTPS, MQ, FTP, etc.; full transformation control; more flexible but complex
- **Web Service Proxy (WS-Proxy):** SOAP/WSDL-specific, auto-generates from WSDL, easier for simple web services, built-in WS-Security
- MPGW is more common for REST APIs and complex mediation
- WS-Proxy better for straightforward SOAP services with WSDL contracts

**Strong candidates will:**
- Mention XML Firewall as another option
- Discuss when to use each
- Reference actual project examples

**Q5: A DataPower service is returning 500 errors intermittently. How do you troubleshoot?**

**Expected Answer:**
- Enable debug logging for the specific service
- Check default log (filter by transaction ID/correlation ID)
- Review error handling rules and catch actions
- Examine backend connectivity (timeouts, connection refused)
- Use DataPower probe to capture request/response
- Check memory/CPU on DataPower appliance
- Review firmware logs for system issues
- Verify certificate validity if MTLS is involved

**Red Flags:**
- Doesn't mention logging or probes
- No systematic approach
- Can't explain correlation ID usage

**Q6: How do you implement rate limiting in DataPower?**

**Expected Answer:**
- Use SLM (Service Level Monitoring) policy
- Configure throttle settings (requests per second/minute)
- Define document weight and threshold
- Implement client identification (IP, header, JWT claim)
- Configure overflow/error handling (429 Too Many Requests)
- Can be applied per-service or globally

**Strong candidates will:**
- Mention tiered rate limits (per client)
- Discuss burst vs sustained rates
- Reference APM integration

#### C. Payments Domain (15 min)

**Q7: Explain the difference between CHAPS and Faster Payments in the UK.**

**Expected Answer:**
- **CHAPS:** High-value (typically £10K+), real-time gross settlement, same-day guaranteed, higher fees, used for property purchases, operates 6am-6pm
- **Faster Payments:** Lower value (up to £1M but typically smaller), near-instant, 24/7/365, lower fees, used for everyday transfers
- Both support ISO 20022 messaging (pacs.008 for payments)
- CHAPS is RTGS (each payment settled individually), FP is deferred net settlement

**Q8: What's ISO 20022 and why is it important for payment systems?**

**Expected Answer:**
- Global standard for financial messaging (XML-based)
- Replacing legacy formats (SWIFT MT messages, proprietary formats)
- Richer data model - more structured information than MT messages
- Key message types: pacs.* (payment clearing/settlement), pain.* (payment initiation), camt.* (cash management)
- UK mandated for CHAPS (2017), other schemes adopting
- Enables better STP (straight-through processing), fraud detection, compliance

**Strong candidates will:**
- Name specific message types (pacs.008, pacs.002, pain.001)
- Discuss migration challenges (MT to MX)
- Mention CBPR+ (cross-border payments)

**Q9: What's a payment "return" vs an "advice"?**

**Expected Answer:**
- **Return (R-Message):** Payment rejected/failed, funds returned to originator (e.g., incorrect account, insufficient funds, beneficiary deceased)
- **Advice:** Notification/confirmation message (e.g., credit advice, debit advice, status update)
- Returns trigger reconciliation and exception handling
- ISO 20022: pacs.004 is payment return, camt.* for advice messages
- Important for operational metrics (return rates indicate data quality issues)

#### D. General Technical (10 min)

**Q10: Describe your experience with z/OS Connect EE.**

**Listen for:**
- SAR (Service Archive) creation for CICS/IMS programs
- AAR (API Archive) with OpenAPI specs
- REST-to-COMMAREA/channel mapping
- API versioning and lifecycle
- Integration with API gateways (TYK, Apigee, AWS)
- Interceptors for logging/transformation
- Performance tuning (connection pooling, thread management)

**Q11: How would you design a payment API that needs to hit both mainframe (CICS) and cloud database (Aurora)?**

**Expected Answer outline:**
- API Gateway (DataPower/TYK) receives request
- Route to z/OS Connect EE → CICS program for account validation
- Call Spring Boot microservice for business rules (Aurora)
- Implement compensating transaction pattern for failures
- Use correlation IDs for distributed tracing
- Consider timeout/circuit breaker patterns
- Event sourcing for audit trail
- Idempotency keys to prevent duplicate payments

**Strong candidates will:**
- Discuss transaction boundaries and consistency models
- Mention eventual consistency challenges
- Talk about error handling and rollback strategies
- Reference specific patterns (Saga, 2PC challenges)

---

### Round 2: Coding Exercise (90 min) - On-site/Virtual

**Part A: COBOL/JCL Review (30 min)**

Provide a COBOL program snippet with issues and ask candidate to:
1. Identify bugs or inefficiencies
2. Explain what the code does
3. Suggest improvements

**What to look for:**
- Can read and understand COBOL structure
- Identifies common issues (hard-coded values, missing error handling)
- Understands VSAM file processing
- Recognizes Db2 cursor handling

**Part B: Java/SQL Problem (60 min)**

**Scenario:** Build a payment validation service

**Requirements:**
- REST endpoint that accepts payment request JSON
- Validate against Db2 database (account exists, sufficient balance)
- Implement rate limiting (max 100 requests/min per account)
- Return structured error responses
- Include unit tests

**Assessment Criteria:**
- Clean code structure (separation of concerns)
- Proper exception handling
- SQL injection prevention (PreparedStatement)
- Use of Spring Boot annotations correctly
- Transaction management
- Test coverage (JUnit, Mockito)
- Error response structure (RFC 7807 Problem Details)

**Bonus points:**
- Implements caching (Redis/Caffeine)
- Uses Spring Security for auth
- Adds correlation ID logging
- Circuit breaker pattern (Resilience4j)

---

### Round 3: System Design (60 min) - On-site/Virtual

**Problem Statement:**

"Design a high-availability payment processing system that:
1. Accepts ISO 20022 payment instructions via REST API
2. Validates against mainframe account data (CICS/Db2)
3. Sends to payment clearing engine
4. Handles returns and advices
5. Supports 10,000 TPS with P95 latency < 200ms
6. Multi-region DR (RPO < 1 min, RTO < 5 min)"

**What to evaluate:**

**Architecture:**
- Component diagram (API Gateway, DataPower, z/OS Connect, CICS, Spring Boot services, databases)
- Data flow and integration points
- Clear separation of concerns

**Scalability:**
- Horizontal scaling strategies
- Database read replicas
- Caching layers
- Async processing (Kafka/MQ)

**Reliability:**
- Circuit breakers, retries, timeouts
- Dead letter queues
- Compensating transactions
- Health checks and monitoring

**Data Management:**
- Database strategy (mainframe vs cloud)
- Data consistency models
- Caching strategy
- Event sourcing for audit

**Security:**
- Authentication/authorization (OAuth2, JWT)
- Encryption in transit/at rest
- PCI DSS compliance considerations
- MTLS between components

**DR/HA:**
- Multi-region deployment
- Database replication (Db2 HADR, Aurora Global)
- Active-active vs active-passive
- Failover testing

**Strong candidates will:**
- Ask clarifying questions before diving in
- Consider trade-offs explicitly (CAP theorem, consistency vs availability)
- Discuss observability (logs, metrics, traces)
- Mention cost implications
- Reference real-world patterns and anti-patterns
- Draw clear diagrams

**Red flags:**
- No consideration of failure scenarios
- Over-engineered or under-engineered solution
- Ignores mainframe constraints
- No monitoring/observability strategy
- Can't explain trade-offs

---

### Round 4: Behavioral (45 min)

**Q1: Tell me about a time you debugged a critical production issue in a payment system.**

**Listen for:**
- Structured approach (gather data, form hypothesis, test, validate)
- Collaboration with teams (DBAs, network, security)
- Use of monitoring tools
- Communication during incident
- Post-mortem and preventive measures
- Ownership and accountability

**Q2: Describe a mainframe modernization project you led or contributed to.**

**Listen for:**
- Strangler fig pattern or similar approach
- Risk mitigation strategies
- Balancing modernization with stability
- Stakeholder management (business, ops, security)
- Metrics for success

**Q3: How do you stay current with both legacy mainframe and modern cloud technologies?**

**Listen for:**
- Active learning (courses, certifications, conferences)
- Hands-on experimentation
- Community involvement
- Reading (blogs, docs, books)
- Balance between depth and breadth

**Q4: Tell me about a time you had to make a technical trade-off between performance and reliability.**

**Listen for:**
- Clear articulation of the trade-off
- Data-driven decision making
- Consideration of business impact
- Monitoring post-decision
- Willingness to revisit decisions

---

## Sample Technical Deep-Dive Questions (Use Selectively)

### Advanced CICS

**Q: Explain CICS task lifecycle and transaction management.**
- Task creation (attach)
- UOW boundaries and syncpoints
- Two-phase commit with Db2
- Rollback handling
- Pseudo-conversational vs conversational
- Task termination and cleanup

**Q: How does CICS Liberty integrate with traditional CICS? What are the performance implications?**
- JVM server within CICS region
- JCICS API for program link, VSAM access
- Thread pooling and resource management
- Garbage collection impact on response time
- When to use vs traditional CICS programs

### Advanced DataPower

**Q: Explain DataPower processing pipeline for MPGW.**
- Request flow: input → policy → transformation → backend
- Response flow: backend → transformation → policy → output
- Processing context (INPUT/OUTPUT/ERROR)
- Match rules and priorities
- GatewayScript vs XSLT performance

**Q: How do you implement dynamic routing in DataPower?**
- Routing based on content (XPath, JSONPath)
- Load balancing algorithms
- Backend service groups
- Health checks and failover
- Circuit breaker implementation

### Advanced Payments

**Q: How do you handle duplicate payment detection?**
- Idempotency keys (client-generated)
- Database constraints (unique index)
- Distributed caching (Redis)
- Time-based deduplication window
- Reconciliation processes

**Q: Explain the payment lifecycle from initiation to settlement.**
- Initiation (pain.001 or API call)
- Validation (account, limits, sanctions)
- Routing (scheme selection)
- Clearing (batch or real-time)
- Settlement (central bank, nostro accounts)
- Confirmation (pacs.002)
- Returns/advices handling

### Advanced AWS/Cloud

**Q: How do you achieve multi-region consistency with Aurora Global Database?**
- Primary region (writer)
- Secondary regions (read replicas)
- Replication lag (typically < 1 second)
- Failover process (promote secondary)
- Application considerations (read after write)
- Conflict resolution strategies

**Q: Design a disaster recovery strategy for a payment system spanning mainframe and AWS.**
- Db2 HADR for mainframe
- Aurora Global Database for cloud
- Application deployment in multiple regions
- DataPower HA pairs
- DNS failover or Global Accelerator
- DR drills and testing
- RPO/RTO targets and validation

---

## Evaluation Rubric

### Technical Skills (70%)

| Area | Weight | Junior | Mid | Senior | Lead |
|------|--------|--------|-----|--------|------|
| Mainframe (CICS/Db2/JCL) | 20% | Basic COBOL reading | Program development | Performance tuning | Architecture decisions |
| DataPower | 15% | Basic configuration | Policy development | Advanced mediation | Platform strategy |
| API Integration | 10% | Simple REST APIs | z/OS Connect | Complex hybrid patterns | Integration architecture |
| Java/Spring | 15% | Spring Boot basics | Enterprise patterns | Microservices design | Platform leadership |
| Payments | 10% | ISO 20022 awareness | Message handling | End-to-end flows | Domain expertise |

### Soft Skills (30%)

| Area | Weight | Assessment Criteria |
|------|--------|-------------------|
| Problem Solving | 10% | Structured thinking, debugging approach, root cause analysis |
| Communication | 10% | Technical explanation, documentation, stakeholder management |
| Leadership | 5% | Mentorship, decision-making, ownership |
| Adaptability | 5% | Learning agility, handling ambiguity, technology breadth |

### Scoring Guide

**Total Score: 100 points**

- **90-100:** Exceptional - Hire immediately, strong senior/lead candidate
- **75-89:** Strong - Hire, solid mid-senior candidate
- **60-74:** Moderate - Consider for mid-level, may need growth areas
- **Below 60:** Weak - Pass or junior role only

---

## Red Flags (Immediate Concerns)

**Technical:**
- Can't explain basic CICS transaction flow
- No hands-on DataPower experience (only theoretical)
- Doesn't understand payment compliance requirements
- Can't read COBOL code (for mainframe role)
- No experience with production debugging
- Unfamiliar with API security (OAuth2, JWT, MTLS)

**Behavioral:**
- Blames others for production incidents
- No ownership or accountability
- Dismissive of legacy technology
- Can't articulate trade-offs
- Poor communication skills
- No interest in learning

**Cultural:**
- Only wants to work on "new tech" (not mainframe)
- Not comfortable with on-call rotation
- Expects 100% remote (role is hybrid)
- Unwilling to mentor others

---

## Ideal Candidate Profile

**Background:**
- 7-10 years total experience
- Started with mainframe, expanded to cloud
- Financial services background (banking, payments, cards)
- Mix of development and operations experience
- Has modernized legacy systems successfully

**Technical:**
- Equally comfortable in COBOL and Java
- Deep DataPower expertise (not just basic config)
- Strong understanding of payment schemes and regulations
- Cloud-native patterns (Kubernetes, microservices, event-driven)
- DevOps mindset (CI/CD, Infrastructure as Code)

**Personal:**
- Pragmatic problem solver
- Strong communicator (can explain to business)
- Mentorship experience
- Passionate about technology evolution
- Resilient under pressure (payments are mission-critical)

---

## Questions to Ask Candidate

**Cultural Fit:**
1. "What excites you about working with mainframe AND cloud technologies?"
2. "How do you feel about on-call rotation for payment systems?"
3. "Tell me about your ideal team structure."

**Technical Direction:**
1. "Where do you see mainframe technology in 5 years?"
2. "What's your view on microservices vs monoliths for payment systems?"
3. "How do you balance technical debt vs new features?"

**Growth:**
1. "What do you want to learn in this role?"
2. "How do you approach mentoring junior developers?"
3. "What's your leadership style?"

---

## Next Steps After Interview

**Strong Hire:**
- Reference checks (focus on technical depth and incident handling)
- Discuss compensation and start date
- Team introduction
- Onboarding plan

**Borderline:**
- Additional technical deep-dive (pair programming session)
- Architecture discussion with team lead
- Reference checks with specific questions

**Pass:**
- Polite rejection with feedback
- Keep in network for future roles
- Offer alternative role if applicable (junior position)

---

## Compensation Guidance (London Market)


**Contract:**
- Day rate: £500 - £750/day (outside IR35)
- Inside IR35: £450 - £650/day

**Factors:**
- DataPower expertise commands premium (+£10-15K)
- Payment systems domain adds value (+£5-10K)
- CICS Liberty experience is rare (+£10K)
- Multi-region cloud experience (+£5-10K)

---

## Common Interview Mistakes to Avoid

**Interviewer Mistakes:**
- Focusing only on theory, not practical experience
- Not testing actual coding ability
- Skipping system design for "senior" candidates
- Not probing on production incident experience
- Ignoring cultural fit
- Not selling the role (candidates are interviewing you too)

**What Makes a Great Interview:**
- Conversational, not interrogational
- Mix of depth and breadth
- Real-world scenarios
- Opportunity for candidate to ask questions
- Clear next steps
- Respectful of candidate's time

---

**Document Owner:** Engineering Hiring Manager
**Last Updated:** 2025-11-06
**Review Cycle:** Quarterly

*This is an internal document. Do NOT share with external recruiters or candidates.*
