  
**Bakuten Data Pipeline – Student Report**

Use this to align with the Bakuten case study. Phase 1 (design) is mandatory. Phase 2 (execution) is optional if you can ;)

**Header**  
- Case Study Title  
- Student Name(s) / Group  
 - Date

**Executive Summary (≤150 words)**  
- Problem in one sentence.  
- Your proposed approach (tools + flow) in 2–3 bullets.  
- Biggest risk and how you’d mitigate it.

**Phase 1 – Design (must do)**  
1) **Architecture & Flow (5–8 bullets)**  
   - Describe how data moves: CSV (comma-separated values) files → raw/bronze → modeled tables (dim_customers, fact_transactions, fact_clickstream) → consumers.  
   - Call out tools you picked (or DuckDB) and why (simplicity/cost/reliability).  
2) **Data Model**  
   - List tables, keys, and main joins.  
   - Note any partitioning/filtering (by date, channel, etc.).  
3) **Quality & SLAs (service-level agreements)**  
   - 5–7 checks you’ll enforce first (nulls, uniqueness, valid values, referential integrity).  
   - Freshness/latency targets and what triggers an alert/block.  
4) **Security**  
   - Sensitive fields and how you’d restrict/mask them.  
5) **Assumptions & Gaps**  
   - Unknowns you’d validate later; stretch ideas if time remains.

**Phase 2 – Execute (optional)**  
- What you ran (tool used), and whether it succeeded.  
- Row counts per table; note duplicates removed or blocked.  
- Quality check results: which checks passed/failed.  
- One or two sample metrics (e.g., daily revenue, return rate by channel, avg session depth).

**Conclusion (3–4 bullets)**  
- Why your approach fits the requirements.  
- Top risk and mitigation.  
- Next step you’d take with more time.

**Appendix (optional)**  
- SQL (Structured Query Language) snippets or pseudocode for key steps (e.g., `event_rank`, `is_return`).  
- Any diagrams or quick sketches.
