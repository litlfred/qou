---
# 2i8g
title: 'c₄ pin reconcile (owner-gated): q_parameter pin solves with 46·u⁴, producer uses 4143/90·u⁴ — 0.18 ppb on m_p; aligning means a re-pin of Q_50_DIGIT_STR (touches ~840 witnesses). Needs owner ruling; do NOT change unilaterally.'
status: in-progress
type: task
priority: normal
created_at: 2026-07-04T00:13:54Z
updated_at: 2026-07-04T10:42:17Z
---


## Investigation verdict (2026-07-04, PR #3266, owner-directed)

- `d27b002745` (2026-06-15) introduced `46·u⁴` into the q_parameter pin solver — the then-current **fitted** c₄.
- `58ba1c6800` (2026-06-28, bean `ovud`): "**replace fitted c_4 with exact geometric index 4143/90**" — upgraded the PRODUCER (`m_p_substrate_identity_50dps.py`) only; touched no q_parameter file.
- ⇒ the pin's 46 is a stale fitted leftover; the committed `Q_50_DIGIT_STR` embeds the fitted value (0.008 ppb in q₀, 0.18 ppb on m_p).
- **Direction when a re-pin window opens: align the pin to the derived 4143/90** (option "Re-pin to 4143/90"). Deferred per owner ruling 2026-07-04 (document + defer); the re-pin itself remains owner-gated (≈840-witness staleness class).

## Coordination update (2026-07-04, PR #3280 cross-evidence)

PR #3280 (`claude/mu-p-tension-closure-uua4os`) proves the exact c₄ is
LINEAR in the q₀ pin offset (≈3.99/ppb): c₄=46 is the muon-calibration
convention — the μ–p tension reparametrized, not a constant. It also
flags `4143/90` as having no derivation trail (cited s5bb Reeb route is
an honest-negative) and overshooting vs naked 46. **The "re-pin to
4143/90" direction above is WITHDRAWN** — both values are fit-tier; the
reconcile is among #3280's owner options (relabel honestly with fit
banner / revert to 46 / drop the u⁴ tower to the 240 ppb floor / keep
as-is). This bean now tracks only the pin-vs-producer *consistency*
question, subordinate to the #3280 ruling.
