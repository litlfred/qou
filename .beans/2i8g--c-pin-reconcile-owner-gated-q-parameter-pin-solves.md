---
# 2i8g
title: 'c₄ pin reconcile (owner-gated): q_parameter pin solves with 46·u⁴, producer uses 4143/90·u⁴ — 0.18 ppb on m_p; aligning means a re-pin of Q_50_DIGIT_STR (touches ~840 witnesses). Needs owner ruling; do NOT change unilaterally.'
status: todo
type: task
created_at: 2026-07-04T00:13:54Z
updated_at: 2026-07-04T00:13:54Z
---


## Investigation verdict (2026-07-04, PR #3266, owner-directed)

- `d27b002745` (2026-06-15) introduced `46·u⁴` into the q_parameter pin solver — the then-current **fitted** c₄.
- `58ba1c6800` (2026-06-28, bean `ovud`): "**replace fitted c_4 with exact geometric index 4143/90**" — upgraded the PRODUCER (`m_p_substrate_identity_50dps.py`) only; touched no q_parameter file.
- ⇒ the pin's 46 is a stale fitted leftover; the committed `Q_50_DIGIT_STR` embeds the fitted value (0.008 ppb in q₀, 0.18 ppb on m_p).
- **Direction when a re-pin window opens: align the pin to the derived 4143/90** (option "Re-pin to 4143/90"). Deferred per owner ruling 2026-07-04 (document + defer); the re-pin itself remains owner-gated (≈840-witness staleness class).
