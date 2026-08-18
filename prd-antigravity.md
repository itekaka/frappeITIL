# Product Requirement Document (PRD)
# ITIL 4 Master Control Panel ("ITIL Master Control")

---

| Document Metadata | Details |
| :--- | :--- |
| **Project Name** | ITIL 4 Master Control Panel |
| **Document Version** | 1.0.0-draft |
| **Author** | Senior Product Manager & Tech Lead |
| **Target Release Date**| September 2026 |
| **Platform / Stack** | Frappe Framework (Python Backend, MariaDB/PostgreSQL, Frappe Desk UI) |
| **Document Status** | Under Review / Draft |

---

## 1. Executive Summary & Vision

### 1.1 Executive Summary
**ITIL 4 Master Control Panel** ("ITIL Master Control") is a next-generation Enterprise IT Service Management (ITSM) application built on top of the open-source **Frappe Framework**. Designed from the ground up around **ITIL 4** core principles, the system moves beyond traditional ticket-centric ITSM by unifying **24 ITIL 4 practices** grouped across the **Four Dimensions of Service Management**.

The cornerstone differentiator of ITIL Master Control is the **Service Value Stream Mapper**—an interactive visual engine for mapping, tracking, and measuring end-to-end value stream efficiency. By auto-correlating cross-practice artifacts (e.g., Incident $\rightarrow$ Problem $\rightarrow$ Change Enablement $\rightarrow$ Software Development $\rightarrow$ Deployment Management), the system identifies operational bottlenecks, lead time latency, and wasteful activities (Lean IT).

### 1.2 Product Vision Statement
*"To deliver an intelligent, lean, and holistically integrated ITSM control plane that empowers IT organizations to transform practices into flow, measure true value creation across all 4 ITIL dimensions, and operate continuous service improvement with zero waste."*

---

## 2. Objectives & Key Results (OKRs)

### 2.1 Strategic Business Objectives
1. **Holistic Governance**: Single-pane dashboard governing 24 ITIL 4 practices across 4 dimensions by Q3 2026.
2. **End-to-End Visibility**: Eliminate departmental silos by automatically linking practice transactions across the entire Service Value Stream.
3. **Lean Optimization**: Reduce Mean Time to Resolution (MTTR) and Change Lead Time by 35% through visual waste detection (Lean IT principles).
4. **Frappe Ecosystem Advantage**: Provide a clean, low-overhead enterprise ITSM suite natively extensible via custom Frappe apps, DocTypes, Server Scripts, and Client Scripts.

### 2.2 Key Performance Indicators (KPIs)
* **Value Stream Flow Efficiency**: Ratio of active work time to total lead time across value streams ($> 40\%$).
* **Cross-Practice Auto-Correlation Rate**: $\ge 85\%$ of Incidents leading to structural changes automatically linked to Problem and Change DocTypes.
* **Practice Health Index Accuracy**: Real-time health score calculation (0–100%) calculated dynamically for all 24 practices.
* **System Performance**: Page load time under 1.2s for Frappe Desk Workspace dashboards with full widget metrics rendering.

---

## 3. Target Audience & User Personas

| Persona Role | Primary Goal | Key Pain Points | Core Feature Interactions |
| :--- | :--- | :--- | :--- |
| **VP of IT / CIO** | Executive overview of IT health, alignment with business value stream, risk mitigation. | Lack of high-level visibility across practices, siloed tools, unquantified IT ROI. | 4-Dimension Health Summary, Executive Value Stream Reports, Risk Matrix. |
| **IT Service Manager / Process Owner** | Monitor compliance, SLA adherence, and operational metrics for assigned ITIL practices. | Manual correlation of incidents to changes, fragmented reporting across spreadsheets. | Practice Widgets, Service Level Management, Incident & Change Control dashboards. |
| **Lead DevOps / SysAdmin** | Fast pipeline updates, clear change audit trails, automated event-to-incident mapping. | Slow CAB approvals, disconnected CI/CD deployments and ITSM change logs. | Value Stream Mapper, Deployment & Release Management, Event Auto-triggering. |
| **Service Desk Agent / Tech Support** | Rapid incident logging, knowledge retrieval, clear escalation paths to Problem Mgmt. | Context switching between multiple disconnected tools during triage. | Incident Management, Knowledge Base lookup, Incident-to-Problem linking workflow. |
| **IT Asset & Vendor Manager** | Lifecycle asset tracking, vendor SLA compliance, financial cost distribution. | Blind spots in license compliance, unmonitored supplier performance. | IT Asset Management, Supplier Management, Service Financial Management. |

---

## 4. Key Unique Feature: Service Value Stream Mapper

### 4.1 Concept & Functional Description
The **Service Value Stream Mapper** is an interactive, visual canvas integrated directly into Frappe Desk. It represents how value flows from **Demand/Trigger** (e.g. User Incident, Business Feature Request, Infrastructure Alert) to **Value Delivered** (e.g. Resolved Incident, Deployed Feature, Patched System).

```
[ Demand / Event ] 
       │
       ▼
 [ Incident Management ] ──(Auto-Link)──► [ Problem Management ]
                                                 │
                                              (Auto-Link)
                                                 ▼
 [ Deployment Management ] ◄──(Auto-Link)── [ Change Enablement ]
       │
       ▼
[ Value Realized / Metric Recorded ]
```

### 4.2 Core Requirements for Value Stream Mapper
1. **Interactive Visual Canvas**: Built using custom HTML5 Canvas / SVG library (e.g., Cytoscape.js / D3.js wrapped in Frappe Page UI) displaying practice nodes and directional workflow edges.
2. **Automated Cross-Practice Correlation Engine**:
   - Creating a **Problem** from an **Incident** copies reference IDs and auto-draws dependency edges.
   - Linking a **Change Request** to a **Problem** auto-updates node statuses on the VSM canvas.
   - Associating a **Software Release / Deployment Log** updates lead time metrics from request to deployment.
3. **Lean Metrics & Waste Identification (Lean IT)**:
   - **Lead Time (LT)**: Elapsed time from initial trigger to value delivery.
   - **Process Time (PT)**: Actual active touch time spent working on tasks.
   - **Wait Time (WT / Waste)**: Idle queue time between practice handoffs.
   - **Flow Efficiency**: $\text{FE} = \left(\frac{\sum PT}{\sum LT}\right) \times 100\%$.
   - **Visual Alerts**: Red/Yellow highlighted nodes on nodes where wait times exceed SLA thresholds.
4. **Drill-down Capability**: Clicking any node or connector edge opens the underlying Frappe DocType record or filtered list view in a slide-out modal or context drawer.

---

## 5. Scope: 24 ITIL 4 Practices Across 4 Dimensions

The system governs **24 ITIL 4 Practices** structured under the **Four Dimensions of Service Management**.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        THE FOUR DIMENSIONS                             │
├───────────────────────────────┬────────────────────────────────────────┤
│ 1. Organizations & People     │ 2. Information & Technology            │
│  - Organizational Change Mgmt │  - Information Security Management     │
│  - Knowledge Management       │  - Architecture Management             │
│                               │  - IT Asset Management (ITAM)          │
│                               │  - Software Development & Management   │
│                               │  - Monitoring & Event Management       │
│                               │  - Infrastructure & Platform Management│
├───────────────────────────────┼────────────────────────────────────────┤
│ 3. Partners & Suppliers       │ 4. Value Streams & Processes           │
│  - Supplier Management        │  - Incident Management                 │
│  - Service Financial Mgmt     │  - Problem Management                  │
│                               │  - Service Request Management          │
│                               │  - Change Enablement                   │
│                               │  - Service Level Management (SLA)      │
│                               │  - Service Continuity Management       │
│                               │  - Service Design                      │
│                               │  - Service Desk                        │
│                               │  - Service Validation & Testing        │
│                               │  - Deployment Management               │
│                               │  - Release Management                  │
│                               │  - Measurement & Reporting             │
│                               │  - Risk Management                     │
│                               │  - Project Management                  │
└───────────────────────────────┴────────────────────────────────────────┘
```

### 5.1 Detailed Practice Functional Matrix

#### Dimension A: Organizations & People
1. **Organizational Change Management (OCM)**: Track stakeholder engagement, change readiness assessments, training plans, and cultural impact scores for major IT transformations.
2. **Knowledge Management**: Articles, KEDB (Known Error Database), solution templates, auto-suggestion during Incident/Service Request creation, markdown format, versioning.

#### Dimension B: Information & Technology
3. **Information Security Management**: Security incident logging, vulnerability register, access request approvals, compliance audit trails (ISO 27001 mapping).
4. **Architecture Management**: EA (Enterprise Architecture) component mapping, technology stack registry, lifecycle tracking (Active, Deprecated, End-of-Life).
5. **IT Asset Management (ITAM)**: Hardware/Software asset inventory, lifecycle management, license compliance tracking, software metering, depreciation records.
6. **Software Development & Management**: Code repository integration (Git/GitHub/GitLab webhooks), build/PR tracking linked to change requests.
7. **Monitoring & Event Management**: Alert ingestion engine (REST API / Webhooks for Prometheus, Zabbix, Datadog), rule-based event deduplication and auto-creation of Incidents.
8. **Infrastructure & Platform Management**: Server/Cloud instance inventory, environment definitions (Dev, Staging, Prod), capacity monitoring metrics.

#### Dimension C: Partners & Suppliers
9. **Supplier Management**: Vendor registry, contract lifecycle management, Underpinning Contracts (UC), vendor performance rating, SLA compliance per vendor.
10. **Service Financial Management**: IT service cost modeling, TCO calculation, budget vs actual tracking, chargeback/showback reports per business unit.

#### Dimension D: Value Streams & Processes
11. **Incident Management**: Incident lifecycle, priority matrix (Impact x Urgency), first contact resolution (FCR), auto-assignment rules, SLA timers, major incident protocols.
12. **Problem Management**: RCA (Root Cause Analysis) workflows (5-Whys, Fishbone), Known Error creation, Workaround publication, linking to Change Enablement.
13. **Service Request Management**: Service Catalog, self-service portal integration, multi-stage approval workflows, task fulfillment routing.
14. **Change Enablement**: Change Models (Standard, Normal, Emergency), CAB (Change Advisory Board) voting workspace, risk assessment scoring, conflict calendar.
15. **Service Level Management**: SLA policies, Operational Level Agreements (OLA), Service Level Targets (SLT), automated SLA breach notifications, penalty calculation.
16. **Service Continuity Management**: Business Impact Analysis (BIA), Disaster Recovery (DR) plans, failover drill testing logs, RTO/RPO targets monitoring.
17. **Service Design**: SDP (Service Design Package) management, utility & warranty definition, service transition criteria checklist.
18. **Service Desk**: Omnichannel ticket ingestion, agent dispatch board, CTI/email integration, ticket queue routing.
19. **Service Validation & Testing**: Test suites, UAT sign-off logs, quality gate checks prior to Release Management approval.
20. **Deployment Management**: Deployment execution logs, CI/CD pipeline triggers (Jenkins, GitHub Actions, GitLab CI), rollback tracking.
21. **Release Management**: Release package aggregation, deployment window scheduling, release note generator, version tag tracking.
22. **Measurement & Reporting**: Customizable metrics engine, KPI scorecards, dynamic Frappe charts, automated scheduled report generation.
23. **Risk Management**: IT Risk Register, Risk Assessment Matrix (Likelihood x Impact), mitigation action plans, risk score recalculation.
24. **Project Management**: IT Project tracking, Gantt charts, sprint/milestone execution, resource allocation linked to ITSM changes.

---

## 6. UI/UX Architecture & Widget System in Frappe Desk

### 6.1 Desk Card / Widget Specification
Each of the 24 practices is assigned a customized **Frappe Dashboard Widget Card** placed inside the main **ITIL 4 Master Workspace**.

```
┌─────────────────────────────────────────────────────────┐
│ [Icon] Incident Management                [Health: 92%] │
├─────────────────────────────────────────────────────────┤
│ Open Incidents: 14      │ SLA Compliance: 96.4%         │
│ MTTR: 1.8 hrs           │ Major Incidents: 0            │
├─────────────────────────────────────────────────────────┤
│ Trend: 📈 -12% Incidents (vs last week)                 │
├─────────────────────────────────────────────────────────┤
│ [ View Value Stream ]           [ Quick Action + New ]  │
└─────────────────────────────────────────────────────────┘
```

### 6.2 Widget Core Components
1. **Health Score Indicator (0–100%)**: Color-coded badge (Green $\ge 85\%$, Yellow $70-84\%$, Red $<70\%$).
2. **Key Metric Counter Grid**: 2–4 critical metrics per practice (e.g. MTTR, SLA %, Open Items).
3. **Trend Indicator**: Sparkline chart or percentage delta compared to previous period ($W-1 / M-1$).
4. **Action Buttons**:
   - `Open Practice Workspace`: Deep-link to practice-specific list/kanban view.
   - `View in Value Stream`: Filters the visual VSM canvas to highlight active nodes for this practice.
   - `Quick Action`: Modal to create a new transaction record (e.g., + Incident, + Risk).

### 6.3 Health Score Calculation Engine Formula
$$\text{Health Score} = \left( w_1 \times S_{\text{SLA}} \right) + \left( w_2 \times S_{\text{Backlog}} \right) + \left( w_3 \times S_{\text{Quality}} \right)$$
Where:
* $S_{\text{SLA}}$: Percentage of records within SLA target.
* $S_{\text{Backlog}}$: Metric reflecting queue growth/staleness.
* $S_{\text{Quality}}$: Metric reflecting re-open rate / error rate / SLA breach rate.
* Weights ($w_1, w_2, w_3$) configured via **ITIL Practice Config** DocType.

---

## 7. Frappe DocType Architecture Design

To achieve maximum efficiency, modularity, and native Frappe framework integration without redundant code, the system utilizes a **Hierarchical DocType Matrix**.

```
                               ┌───────────────────────────┐
                               │   ITIL Practice Master    │ (Configuration & Health)
                               └─────────────┬─────────────┘
                                             │
             ┌───────────────────────────────┼───────────────────────────────┐
             ▼                               ▼                               ▼
┌──────────────────────────┐    ┌──────────────────────────┐    ┌──────────────────────────┐
│ ITIL Value Stream Node   │    │  ITIL Practice Transaction│    │   ITIL Practice Metric   │
│  (Canvas Coordinates &   │    │  (Base Link DocType)     │    │   (Log / Snapshot Data)  │
│   Connection Edges)      │    └────────────┬─────────────┘    └──────────────────────────┘
└──────────────────────────┘                 │
                                ┌────────────┴────────────┐
                                ▼                         ▼
                     [ Standard ITIL DocTypes ]   [ Child Table DocTypes ]
                     - ITIL Incident              - ITIL Practice KPI Line
                     - ITIL Problem               - ITIL Waste Log
                     - ITIL Change Request        - ITIL Value Stream Edge
                     - ITIL Asset                 - ITIL CAB Member
                     - ITIL Risk Register
```

### 7.1 Key Standard DocTypes & Schemas

#### 1. Core Config & Governance DocTypes
* `ITIL Practice`: Master configuration DocType containing practice name, dimension category, practice owner, weight configs, health score logic formula, icon, and desk dashboard route.
* `ITIL Practice Health Snapshot`: Periodic historical log of calculated health scores and KPI values for trend analysis.
* `ITIL Practice Link`: Relational bridge storing cross-practice associations (Source DocType, Source Name $\rightarrow$ Target DocType, Target Name, Link Type e.g., "Caused By", "Resolved By", "Mitigated By").

#### 2. Service Value Stream Mapper DocTypes
* `ITIL Value Stream Definition`: Master DocType defining value stream name, trigger condition, target outcome, target lead time, baseline cost.
* `ITIL Value Stream Node`: Child table / linked DocType defining individual step nodes in the value stream (Practice reference, Step name, Target Process Time, Target Wait Time, Auto-trigger rules).
* `ITIL Value Stream Edge`: Defines connections between nodes (Source Node, Target Node, Transition Condition, Automated Action trigger).
* `ITIL Value Stream Transaction`: Instance execution log of a single item flowing through a Value Stream. Stores total Lead Time, total Wait Time, active step, and computed Flow Efficiency.

#### 3. Practice Core Transactional DocTypes (Sample Breakdown across Dimensions)

##### Dimension A: Organizations & People
* `ITIL Org Change Record`: Organizational change planning, readiness checklist, communication log.
* `ITIL Knowledge Article`: Knowledge base entry, category, draft/published state, view count, helpfulness score.

##### Dimension B: Information & Technology
* `ITIL Security Event`: Security incident ticket, severity level, threat vector, ISO 27001 mapping.
* `ITIL Architecture Asset`: Enterprise architecture node, tech stack category, lifecycle phase.
* `ITIL Asset Item`: ITAM hardware/software item, serial number, owner, maintenance contract, status.
* `ITIL Software Commit Link`: Bridges Git commits/PRs to Change Requests and Incidents.
* `ITIL Monitoring Event`: Ingested alert payload, deduplication hash, triggered incident link.
* `ITIL Infrastructure Node`: Server/Cloud instance profile, health status, connected IT Assets.

##### Dimension C: Partners & Suppliers
* `ITIL Supplier`: Vendor profile, rating score, underpinning contract link, contact person.
* `ITIL Service Cost Center`: Cost tracking per service, direct/indirect allocation lines.

##### Dimension D: Value Streams & Processes
* `ITIL Incident`: Core incident ticket, priority matrix, SLA link, resolution details, FCR flag.
* `ITIL Problem`: RCA details, 5-Whys analysis table, workaround markdown, Known Error flag.
* `ITIL Service Request`: Request item from service catalog, customer details, fulfillment workflow.
* `ITIL Change Request`: Change classification (Standard, Normal, Emergency), CAB approval table, risk score, rollout plan, backout plan.
* `ITIL SLA Policy`: Response/Resolution SLA definitions, priority rules, business hours schedule.
* `ITIL Service Continuity Plan`: DR plan definition, RTO/RPO metrics, drill schedule, drill execution logs.
* `ITIL Service Design Package`: Specifications for new/modified IT services.
* `ITIL Service Desk Queue`: Dispatch board queue rules and routing criteria.
* `ITIL Validation Test Suite`: Test cases, test run results, pass/fail status before release.
* `ITIL Deployment Log`: Deployment execution details, target environment, execution status.
* `ITIL Release Package`: Release version tag, bundled Change Requests, rollout schedule.
* `ITIL Metric Log`: Metric data points for custom KPI reporting.
* `ITIL Risk Register`: Identified risk, likelihood rating, impact rating, risk score, mitigation plan.
* `ITIL Project`: IT Project container, milestones, linked ITSM Change Requests.

---

## 8. Technical Architecture & Tech Stack

### 8.1 Architecture Layer Diagram
```
┌────────────────────────────────────────────────────────────────────────┐
│                        FRAAPPE DESK FRONTEND                           │
│  - Custom Workspaces (ITIL 4 Master Control)                           │
│  - 24 Practice Widget Cards (HTML/JS + Vue/Frappe Controls)            │
│  - Visual Service Value Stream Mapper (D3.js / Canvas Custom Page)     │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ REST / Frappe Call (RPC API)
┌───────────────────────────────────▼────────────────────────────────────┐
│                        FRAPPE BACKEND (PYTHON)                         │
│  - Custom Frappe App: `itil_master_control`                            │
│  - Controllers: Practice Health Calculator Engine                      │
│  - Value Stream Flow Engine (Lead Time, PT, WT, Flow Efficiency)       │
│  - Event Ingestion Webhooks API (Prometheus/Zabbix/GitLab)             │
│  - SLA & Auto-Correlation Background Jobs (RQ Workers)                │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ ORM / Query Builder
┌───────────────────────────────────▼────────────────────────────────────┐
│                        PERSISTENCE & INFRASTRUCTURE                    │
│  - MariaDB / PostgreSQL (DocTypes Data)                                │
│  - Redis (Caching & Job Queue management)                              │
└────────────────────────────────────────────────────────────────────────┘
```

### 8.2 Technology Specifications
* **Backend Framework**: Frappe Framework (v15+)
* **Programming Language**: Python 3.10+
* **Database**: MariaDB 10.6+ or PostgreSQL 14+
* **Cache & Queues**: Redis & Frappe Background Workers (RQ)
* **Frontend Components**: Frappe Desk UI, JavaScript (ES6+), HTML5 Canvas / D3.js (for VSM canvas rendering)
* **Integrations**: Webhooks REST Endpoints for Monitoring Systems (Zabbix/Prometheus) and Version Control (GitHub/GitLab).

---

## 9. Non-Functional Requirements (NFRs)

### 9.1 Performance & Scalability
* **API Response Time**: REST endpoints for event ingestion response time $< 150\text{ ms}$.
* **Dashboard Load Time**: Workspace rendering time $< 1.2\text{ s}$ for 24 widgets.
* **Concurrent Capacity**: Minimum 500 concurrent active users without degradation on standard 4 vCPU / 8 GB RAM deployment.

### 9.2 Security & Governance
* **Role-Based Access Control (RBAC)**: Custom Frappe Roles (ITIL Executive, Service Desk Agent, Process Owner, CAB Member, Risk Manager).
* **Audit Trail**: Native Frappe Audit Trail enabled on all critical DocTypes (Change Request, Security Event, Risk Register).
* **Data Security**: Field-level permissions for sensitive security & financial data.

### 9.3 Quality & Standards Compliance
* **ITIL 4 Alignment**: Strict adherence to ITIL 4 terminology, concepts, and Service Value System (SVS) guidelines.
* **ISO/IEC 20000 Compliance Ready**: Data structures mapped to facilitate ISO 20000 audit readiness.

---

## 10. Release & Implementation Roadmap

Target Release: **September 2026**

```
 2026 Q1                  2026 Q2                  2026 Q3 (Release Sept)
┌───────────────────────┐ ┌───────────────────────┐ ┌─────────────────────────┐
│ Phase 1: Core & Setup │ │ Phase 2: 24 Practices │ │ Phase 3: VSM Engine     │
│ - Frappe App Setup    │ │ - Build 24 DocTypes   │ │ - Visual Canvas UI      │
│ - Master DocTypes     │ │ - Workflows & SLAs    │ │ - Lean Analytics        │
│ - Base Widgets        │ │ - Health Score Logic  │ │ - Final QA & Pilot      │
└───────────────────────┘ └───────────────────────┘ └─────────────────────────┘
```

### Milestone Breakdown
1. **Phase 1: Architecture & Foundation (Feb 2026 – Apr 2026)**
   - Initialize `itil_master_control` Frappe App structure.
   - Implement `ITIL Practice`, `ITIL Practice Link`, and Health Score Calculation engine.
   - Build base Frappe Desk Workspace layout.
2. **Phase 2: 24 Practice DocTypes & Workflows (May 2026 – Jul 2026)**
   - Develop DocTypes across 4 Dimensions.
   - Configure SLA rules, Workflows, CAB voting module, and KEDB.
   - Populate Practice Widget cards with real-time KPI data.
3. **Phase 3: Service Value Stream Mapper & Integration (Aug 2026 – Sept 2026)**
   - Build visual VSM Frappe Page canvas using D3.js/Canvas.
   - Connect cross-practice auto-correlation triggers.
   - Conduct end-to-end performance testing, security audit, and final September 2026 release.

---

## 11. Document Sign-off & Next Steps

* [x] **Product Manager Approval**: Detailed functional requirements established.
* [x] **Tech Lead Approval**: Frappe DocType architecture & API specification defined.
* [ ] **User / Stakeholder Review**: Pending user feedback on initial PRD draft.
