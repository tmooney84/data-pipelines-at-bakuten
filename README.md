![Bakuten data pipeline animation](ascii-animation.gif)

**Data Pipelines for Bakuten**  
*Peak-season data ops: fast campaign insights, hourly revenue you can trust.*
You are a Data Engineer at Bakuten (5M customers, multi-category e-commerce). Leadership wants a reliable ELT (Extract-Load-Transform) pipeline to feed analytics and machine learning (ML) uses such as recommendations, return on investment (ROI) prediction, and fraud detection. Work in two phases: Phase 1 is design (required), Phase 2 is execution (optional).

**Objectives**
- Propose a scalable ELT (Extract-Load-Transform) architecture and data model for customers, transactions, and clickstream.  
- Define enforceable quality rules and service-level agreements (SLAs).  
- (Optional) Run a starter pipeline using the provided CSV (comma-separated values) files in `/data`.

**Sample Data**
- `data/customers.csv`: synthetic customer profiles.  
- `data/transactions.csv`: synthetic orders, returns, payments.  
- `data/clickstream.csv`: synthetic web/app events.

**Scenario (story + constraints)**
Bakuten just launched a loyalty push ahead of peak season. Marketing needs clickstream rollups for campaigns within minutes, and Finance needs trusted transactional numbers each hour to manage cash and fraud risk. Data Engineering must land raw feeds quickly, model them reliably, and keep personally identifiable information (PII) safe while costs stay predictable.
- Speed: clickstream summaries in ~15 minutes; transactions within 1 hour.  
- Reliability: ~99.5% of daily loads succeed; stop/alert if checks fail.  
- Cost: prefer simple/managed services; keep storage and compute separate.  
- Privacy: mask/tokenize personally identifiable information (PII) and keep audit logs for changes.

**Phase 1 – Design**  
- **Flow & Tools**: Describe how data moves from CSV files → raw/bronze → modeled tables (dim_customers, fact_transactions, fact_clickstream) → consumers. Pick tools (or stick with DuckDB) and justify briefly.  
- **Data Model**: Tables, keys, main joins; any partitioning/filtering.  
- **Quality & SLAs**: 5–7 checks (nulls, uniqueness, valid values, referential integrity), freshness/latency targets, and what blocks/alerts.  
- **Security**: Sensitive fields and masking/access rules.  
- **Assumptions & Risks**: Unknowns and top risks with mitigations.

**Phase 2 – Execute (optional)**  
- Load CSV files; build the three models; run starter queries (daily revenue, return rate by channel, active customers, session depth).  
- Show quality check results and row counts; note any duplicates removed/blocked.  
- Optional stretch: add one extra check or metric (e.g., conversion by campaign).

**Deliverables**  
- 1-page architecture + data model sketch with a brief text diagram.  
- Quality-check and observability checklist and alert/block plan.  
- Short validation summary (row counts, duplicates, any failed checks).  
- Optional: SQL or Python notebook or pseudocode for key steps (event_rank, is_return).

**Guiding Questions**  
- What are the raw → modeled layers and their purposes?  
- Which tools will you use (or keep it simple) and why?  
- How will you ensure `customer_id` consistency across tables?  
- Which 5–7 quality-check rules will you enforce first, and what happens on failure?  
- How will you measure freshness and alert on delays?  
- What are the key joins (customers ↔ transactions ↔ clickstream) and any partitioning/filtering you’d use?  
- How will you handle personally identifiable information (PII) and other sensitive fields (access, masking, logging)?
