---
# t2vq
title: 'Pre-existing: delta_lambda_empirical_tabulation.py ImportError on main — m_n_derived_3input not exported by experimental_constants'
status: completed
type: task
created_at: 2026-06-29T17:35:28Z
updated_at: 2026-06-29T20:30:00Z
---

> **CLOSED 2026-06-29** — verified resolved on `main`: `experimental_constants.py:88` exports `m_n_derived_3input`; the consumer `delta_lambda_empirical_tabulation.py:100` imports it and the file parses cleanly (commit `6e233cf0`, "fix(t2vq): export m_n_derived_3input"). Audit: `docs/audits/2026-06-29-bean-hygiene-data-integrity-verified-resolved.md`.

