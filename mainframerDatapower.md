# Mainframe Integration Engineer (CICS/Db2 + IBM DataPower) — Payments

## Role Overview

**Location:** London (hybrid)
**Team:** Digital Channels / Bankline
**Type:** Permanent/Contract

### Technology Stack

**Mainframe:**
- z/OS (CICS, Db2, MQ, CA7)
- IBM DataPower
- z/OS Connect EE
- CICS Liberty

**Modern Stack:**
- Java/Spring Boot
- Python
- AWS (Aurora PostgreSQL Global)
- CockroachDB

---

## The Mission

Own and evolve high-volume payment APIs and batch flows sitting at the seam of mainframe and cloud. You'll modernise CICS/Db2 services, harden SOAP/REST mediation on IBM DataPower, and expose core capabilities to Java/Spring microservices hitting Aurora Postgres—without breaking bank-grade resilience.

---

## What You'll Do

### 1. Engineer Mainframe Services

Design, build, and support mission-critical mainframe components:

- **CICS Programming:** Transaction processing, channels/containers, pipelines, COMMAREA structures
- **Db2 for z/OS:** Stored procedures, SQL optimization, BIND strategies, package management, bufferpool tuning
- **File I/O:** VSAM (KSDS/ESDS/RRDS), QSAM, Generation Data Groups (GDGs)
- **Job Control:** JCL scripting, job scheduling with CA7, REXX utilities
- **Data Structures:** Copybooks, DAM (Data Access Method) modules
- **Performance Tuning:** Explain plans, index strategies, cursor management
- **Change Management:** Migration strategies, backout procedures, version control

### 2. Harden API Edge (IBM DataPower)

Own the DataPower gateway layer that fronts BL/OAI CICS web services:

- **Gateway Configuration:**
  - Multi-Protocol Gateway (MPGW)
  - Web Service Proxy (WS-Proxy)
  - XML/JSON mediation

- **Security Policies:**
  - AAA (Authentication, Authorization, Audit) policies
  - LDAP integration
  - JWT/OAuth2 token validation
  - Mutual TLS (MTLS) certificate authentication
  - WS-Security envelope validation

- **API Management:**
  - Rate limiting and throttling
  - Schema validation (WSDL/XSD/JSON Schema)
  - Threat protection rules
  - Header/body transformations using XSLT/GatewayScript
  - API versioning strategies

- **Observability:**
  - Structured logging
  - Metrics collection
  - Distributed tracing
  - Health checks and monitoring

- **Operations:**
  - High availability configuration
  - Firmware lifecycle management
  - Configuration versioning
  - Disaster recovery procedures

### 3. Bridge to Cloud

Expose mainframe capabilities through modern APIs and integrate with cloud services:

- **z/OS Connect EE:**
  - Create Service Archives (SAR) for CICS programs
  - Build API Archives (AAR) with OpenAPI specs
  - REST ↔ CICS/Db2 mapping and transformation
  - Correlation ID propagation for distributed tracing

- **API Gateway Integration:**
  - AWS API Gateway integration
  - TYK API management
  - Kong/Apigee patterns

- **Microservices Integration:**
  - Java/Spring Boot service mesh
  - JDBC connection pooling strategies
  - Stored procedure invocation patterns
  - Idempotency key handling
  - Circuit breakers and timeout management
  - Back-pressure and flow control
  - Asynchronous messaging patterns

### 4. Data Platform Work

Lead data modernization efforts from mainframe to cloud:

- **Database Migration:**
  - Model and migrate domain tables from Db2 to Aurora PostgreSQL Global
  - Schema design and DDL management
  - Data type mapping and conversion
  - Migration scripts and validation procedures

- **Aurora PostgreSQL Global:**
  - Multi-region writer/reader configuration
  - RDS Proxy setup and connection management
  - Failover testing and DR drills
  - Performance baselines and optimization
  - Backup and restore strategies
  - Version upgrade planning

- **Distributed SQL:**
  - CockroachDB deployment patterns
  - Query plan analysis and optimization
  - Transaction boundaries and consistency models
  - Geo-partitioning strategies

- **Data Synchronization:**
  - Change Data Capture (CDC) patterns
  - ETL/ELT pipeline design
  - Data quality validation
  - Reconciliation procedures

### 5. Payments Change

Build and validate payment flows in compliance with industry standards:

- **ISO 20022 Implementation:**
  - CHAPS (Clearing House Automated Payment System)
  - Faster Payments (FT)
  - CBPR+ (Cross-Border Payments and Reporting Plus)
  - Message types: pacs.008, pacs.002, pacs.004, pain.001, etc.

- **Payment Processing:**
  - Payment validation rules
  - Returns and advices handling
  - Routing rules engine
  - Duplicate detection
  - Reconciliation workflows

- **Integration:**
  - Partner with PIMS (Payment Instruction Management System)
  - XCT/Propay/CPS engine integration
  - Cutover planning and execution
  - Proving and certification activities

- **Compliance:**
  - AML/KYC checks
  - Sanctions screening
  - Audit trail requirements
  - PSD2/Open Banking standards

### 6. Reliability & Operations

Implement SRE principles for mission-critical payment systems:

- **Operational Excellence:**
  - SRE-style runbooks and playbooks
  - Incident response procedures
  - Post-mortem analysis
  - RCA (Root Cause Analysis) documentation

- **Deployment Strategies:**
  - Canary releases
  - Blue/green deployments
  - Rolling updates
  - Feature flags/toggles

- **Performance Management:**
  - Capacity planning and forecasting
  - TPS (Transactions Per Second) targets
  - P95/P99 latency monitoring
  - Resource utilization tracking
  - Load testing and stress testing

- **Security Operations:**
  - TLS/SSL certificate lifecycle management
  - Certificate rotation across DataPower/z/OS/Cloud
  - Vulnerability patching
  - Security scanning and compliance

- **Monitoring & Alerting:**
  - Real-time dashboards
  - Proactive alerting
  - SLA/SLO tracking
  - On-call rotation management

### 7. Secure by Default

Implement defense-in-depth security across all layers:

- **Mainframe Security:**
  - RACF (Resource Access Control Facility) administration
  - Dataset security and permissions
  - User access management
  - Security audit logging

- **Cloud Security:**
  - AWS Secrets Manager / KMS integration
  - IAM roles and policies
  - Security groups and NACLs
  - Encryption at rest and in transit

- **API Security:**
  - Token exchange at the edge
  - OAuth2/OIDC flows
  - API key rotation
  - Rate limiting per client

- **Data Protection:**
  - Data minimization principles
  - PII handling and masking
  - Data retention policies
  - Audit trail and compliance logging
  - GDPR/data sovereignty requirements

---

## Must-Have Skills (Hands-On)

### Mainframe Core

**Required:**
- **CICS:** Channels/containers, pipelines, COMMAREA, ECI/EPI, web services, CICS Liberty
- **Db2 for z/OS:** SQL, stored procedures, BIND strategies, package management, performance tuning
- **Job Control:** JCL, REXX scripting, IEFBR14, IDCAMS, utilities
- **File Systems:** VSAM (KSDS/ESDS/RRDS), QSAM, GDG, catalog management
- **Messaging:** IBM MQ (queue managers, channels, triggers), NDM/Connect:Direct
- **Tools:** 3270 emulation, ISPF, File Manager
- **Languages:** COBOL/PLI (reading), Assembler (reading & light modifications)
- **Data:** Copybooks, DAM modules, SPDEFS
- **Automation:** CA7 scheduling, batch dependencies

**Expected Experience Level:** 5+ years hands-on mainframe development

#### What is CICS Liberty? (Developer Perspective)

**CICS Liberty** is IBM's strategic technology for mainframe modernization that embeds WebSphere Liberty (a lightweight Java EE application server) directly into CICS Transaction Server. This is a game-changer for developers because it bridges traditional mainframe and modern cloud-native development.

**What it means for you as a developer:**

**1. Run Modern Java in CICS**
- Deploy Java EE / Jakarta EE applications directly in CICS regions
- Use Spring Boot, JAX-RS, JPA, CDI, and other modern frameworks
- Write RESTful APIs that run natively in CICS with full transaction support
- Leverage modern IDEs (IntelliJ, VS Code, Eclipse) instead of green-screen editors

**2. Hybrid Programming Model**
- **From Liberty, call CICS:** Your Java/Spring Boot code can invoke traditional CICS programs (COBOL, PLI) using JCICS API
- **From CICS, call Liberty:** Traditional programs can call your Java services via ECI (External Call Interface)
- Link transactions across both worlds with coordinated transaction management

**3. Modernization Path**
- Gradually replace COBOL logic with Java microservices without a full rewrite
- Expose legacy CICS programs as REST APIs using Liberty JAX-RS
- Implement new business logic in Java while keeping core transaction processing in CICS
- Use the "Strangler Fig" pattern: wrap legacy functions with modern APIs

**4. Development Workflow**
```
Local Dev → Build WAR/EAR → Deploy to CICS Liberty JVM Server → Access via HTTP/REST
```
- Develop and test Java code locally on your laptop
- Package as standard WAR/EAR files
- Deploy to CICS Liberty JVM server (similar to deploying to WebSphere/Tomcat)
- No need for mainframe access during early development

**5. Practical Example - Payment Validation Service**
```java
@Path("/payments")
@ApplicationScoped
public class PaymentValidationResource {

    @Inject
    private CICSProgramInvoker cicsInvoker;  // Calls legacy COBOL program

    @POST
    @Path("/validate")
    @Produces(MediaType.APPLICATION_JSON)
    public Response validatePayment(PaymentRequest request) {
        // Modern Java code in CICS Liberty

        // Call legacy CICS COBOL program for account validation
        AccountStatus status = cicsInvoker.call("ACCTVALD", request.getAccountId());

        // Modern business logic in Java
        if (status.isValid() && request.getAmount() < status.getLimit()) {
            return Response.ok(new ValidationResponse("APPROVED")).build();
        }

        return Response.status(400)
                      .entity(new ValidationResponse("REJECTED"))
                      .build();
    }
}
```

**6. Key Developer Skills Needed**
- **Java EE/Jakarta EE:** Servlets, JAX-RS, CDI, EJB Lite
- **JCICS API:** Java API for invoking CICS services (channels, containers, programs, queues)
- **Liberty Configuration:** server.xml, feature configuration, JDBC datasources
- **Transaction Management:** Understanding CICS UOW (Unit of Work) boundaries
- **Deployment:** Bundle creation, CICS BUNDLE resources, DFHDPLOY utility
- **Debugging:** Liberty trace, CICS messages (DFHPI, DFHAP), remote debugging

**7. Integration Points**
- **Access Db2:** Use JDBC or JPA from Liberty to query Db2 on z/OS
- **MQ Integration:** Send/receive messages to/from IBM MQ queues
- **CICS Resources:** Access VSAM files, temporary storage, transient data queues
- **Security:** Integrate with RACF, use Liberty's built-in OAuth2/JWT support
- **Monitoring:** Liberty metrics, Performance Monitoring Infrastructure (PMI)

**8. Why This Matters for This Role**
In this payment systems role, CICS Liberty lets you:
- Build ISO 20022 payment validation APIs in Spring Boot running in CICS
- Call existing CICS payment engine programs (written in COBOL) from your Java code
- Expose mainframe payment functions to cloud services via REST APIs
- Maintain bank-grade transaction integrity and security while using modern languages
- Deploy once to CICS and handle millions of TPS with proven scalability

**9. Development Environment**
- **Local:** Liberty Developer Tools, VS Code, Maven/Gradle
- **Remote:** SSH to z/OS, CICS Explorer, IBM Developer for z/OS
- **CI/CD:** Jenkins pipeline → build WAR → DFHDPLOY to CICS → automated testing
- **Version Control:** Git for Java code, Endevor/DBB for CICS artifacts

**Real-World Scenario:**
You're tasked with adding a new CHAPS payment validation rule. Instead of modifying 20-year-old COBOL code, you:
1. Write a Spring Boot REST service in CICS Liberty
2. Call the existing COBOL payment program to get account data
3. Apply your new validation logic in Java (easier to test, maintain, extend)
4. Return the result via REST API to DataPower gateway
5. The COBOL program continues to handle the actual payment posting (proven, stable)

This hybrid approach is the future of mainframe development—keeping what works, modernizing what needs to change.

### IBM DataPower

**Required:**
- **Gateway Types:** Multi-Protocol Gateway (MPGW), Web Service Proxy (WS-Proxy), XML Firewall
- **Security:** AAA policies, LDAP/RADIUS, JWT/OAuth2, MTLS, WS-Security, SAML
- **Transformation:** XSLT 1.0/2.0, GatewayScript (JavaScript), JSONiq
- **Protocols:** WSDL/SOAP, REST/JSON, XML validation (XSD)
- **Operations:** Error handling, logging patterns, HA configuration, firmware management
- **Monitoring:** DataPower probe integration, SNMP, syslog

**Expected Experience Level:** 3+ years DataPower gateway administration

### API Mediation on Host

**Required:**
- **CICS Web Services:** PIPELINE configuration, web services assistant
- **z/OS Connect EE:**
  - Service Archive (SAR) creation
  - API Archive (AAR) development
  - OpenAPI/Swagger spec authoring
  - REST ↔ CICS/Db2 mapping
  - Interceptor patterns
- **Integration Patterns:** Correlation IDs, request/response transformation, error mapping
- **Protocol Handling:** HTTP/HTTPS, content negotiation, header propagation

**Expected Experience Level:** 2+ years z/OS Connect or similar mainframe API gateway

### Modern Application & Data

**Required:**

**Java Ecosystem:**
- Java 17+ (modern language features, records, pattern matching)
- Spring Boot 3.x / Spring Framework 6.x
- Spring Data JPA / JDBC
- Spring Security (OAuth2, JWT)
- Spring Cloud (config, discovery, gateway)
- Maven/Gradle build tools
- JUnit 5, Mockito, Testcontainers

**Python:**
- Python 3.10+ for automation and tooling
- pytest, requests, pandas
- Scripting for DevOps tasks

**Database:**
- JDBC/R2DBC connection patterns
- SQL tuning and query optimization
- Transaction management (ACID properties)
- Connection pooling (HikariCP)

**Aurora PostgreSQL:**
- Global Database setup (multi-region)
- RDS Proxy configuration
- Read replica strategies
- Failover testing procedures
- Performance Insights analysis
- Parameter group tuning
- Backup/restore operations

**CockroachDB:**
- Query plan analysis
- Transaction retry logic
- Geo-partitioning concepts
- Distributed consistency models

**Expected Experience Level:** 4+ years enterprise Java, 2+ years cloud databases

### Payments Domain

**Required:**
- **UK Payments:** CHAPS, Faster Payments, BACS
- **International:** SWIFT, SEPA, TARGET2
- **Standards:**
  - ISO 20022 message types (pacs.*, pain.*, camt.*)
  - MT message formats (transitional knowledge)
  - CBPR+ implementation
- **Processing:** Returns, advices (R-Messages), routing rules, cut-over strategies
- **Compliance:** Payment validation rules, sanctions screening, AML/CTF

**Expected Experience Level:** 2+ years in payment systems development

### Additional Technical Skills

**Version Control & CI/CD:**
- Git workflows (branching strategies, PR reviews)
- Jenkins/GitLab CI/CircleCI
- Infrastructure as Code (Terraform/CloudFormation)
- Ansible/Chef for configuration management

**Observability:**
- Logging frameworks (Log4j2, SLF4J)
- Metrics (Prometheus, CloudWatch)
- Distributed tracing (Jaeger, X-Ray)
- APM tools (New Relic, Dynatrace, AppDynamics)

**Containerization:**
- Docker fundamentals
- Container orchestration concepts (Kubernetes/ECS)
- Service mesh patterns (Istio/Linkerd)

---

## Nice-to-Have

### Extended Technology Experience

- **API Management Platforms:** TYK, Apigee, Kong, AWS API Gateway advanced features
- **Mainframe Data Integration:** zDIH (z/OS Data Integration Hub), CDC solutions
- **Observability Tools:** Grafana dashboards, Kibana/Elasticsearch, Splunk
- **Event Streaming:** Apache Kafka, AWS MSK, event-driven architecture patterns
- **Mainframe Tools:**
  - CA Endevor (SCM for mainframe)
  - CA7 advanced scheduling
  - Blu Age runtime and modernization patterns
- **Legacy Modernization:** Refactoring strategies, strangler fig pattern, API-first approaches

### Cloud Platform Knowledge

**AWS Services:**
- Aurora vs RDS shared-cluster trade-offs
- Security groups, VPC design
- DR strategies (multi-region, backup, snapshots)
- Upgrade planning and blast radius mitigation
- Cost optimization and performance modeling
- Well-Architected Framework principles

**Additional AWS:**
- Lambda serverless patterns
- Step Functions orchestration
- SQS/SNS messaging
- EventBridge event routing
- Secrets Manager, KMS, IAM
- CloudWatch Logs Insights

### Soft Skills & Practices

- **Agile/DevOps:** Scrum/Kanban, continuous improvement mindset
- **Documentation:** Technical writing, architecture diagrams (C4, UML)
- **Collaboration:** Cross-functional team coordination, stakeholder management
- **Problem Solving:** Analytical thinking, root cause analysis, debugging complex distributed systems
- **Communication:** Ability to explain technical concepts to non-technical audiences

---

## Success Metrics

After 6 months in role, you should have:

- **Technical Delivery:**
  - Delivered 3+ DataPower MPGW/WS-Proxy services in production
  - Migrated 2+ CICS programs to modern API exposure
  - Completed 1+ Db2 to Aurora data migration
  - Implemented 5+ ISO 20022 payment message handlers

- **Operational Excellence:**
  - Reduced API P95 latency by 20%
  - Achieved 99.95%+ uptime for payment APIs
  - Zero critical production incidents related to your changes
  - Documented runbooks for all new services

- **Team Impact:**
  - Mentored 2+ team members on mainframe or DataPower
  - Led 1+ architectural design review
  - Contributed to team knowledge base and documentation

---

## Interview Process

1. **Technical Screen (60 min):** Mainframe + DataPower + payments concepts
2. **Coding Exercise (90 min):** CICS/COBOL review + Java/SQL problem solving
3. **System Design (60 min):** Design payment API with mainframe/cloud integration
4. **Behavioral (45 min):** Past projects, incident handling, team collaboration
5. **Final Round (30 min):** Meet the team, culture fit, Q&A

---

## Why This Role?

- Work on mission-critical payment infrastructure processing billions in transactions
- Unique blend of legacy mainframe and cutting-edge cloud technologies
- Hands-on with both the historical foundation and future direction of banking systems
- Strong emphasis on SRE practices and operational excellence
- Collaborative environment with opportunities for mentorship and growth

---

**Apply:** [Contact details or application URL would go here]

*This role offers a rare opportunity to work across the full stack of enterprise banking—from COBOL on CICS to Kotlin on Kubernetes—while ensuring rock-solid reliability for payment systems that power the economy.*
