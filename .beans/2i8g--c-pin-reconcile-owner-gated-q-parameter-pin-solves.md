---
# 2i8g
title: 'c₄ pin reconcile (owner-gated): q_parameter pin solves with 46·u⁴, producer uses 4143/90·u⁴ — 0.18 ppb on m_p; aligning means a re-pin of Q_50_DIGIT_STR (touches ~840 witnesses). Needs owner ruling; do NOT change unilaterally.'
status: completed
type: task
created_at: 2026-07-04T00:13:54Z
updated_at: 2026-07-04T14:20:00Z
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


## RESOLVED (2026-07-04, PR #3280 + local-shim fix) — re-pin moot, all sites tower-free

The pin-vs-producer consistency question is closed: every site that carried
the fitted `(1 + 46u⁴)(1 + 4u⁵)(1 − 29u⁶)` tower is now tower-free and mutually
consistent, so the owner-gated ~840-witness re-pin is **not needed**.

- **Producer** `m_p_substrate_identity_50dps.py` — tower dropped (#3280, merged).
- **Canonical pin solver** `qou_substrate.constants._solve_q_proton_f64` — tower
  stripped (owner ruling 2026-07-03, commit 7b95577a); `Q` derives from it.
- **Local back-compat shim** `computations/substrate/q_parameter.py` — dead
  duplicate `_solve_q_proton_f64` (still carried the tower) removed 2026-07-04.
- **`Q_50_DIGIT_STR`** = `1.10997858275138080759…` is the raw proton pin and
  matches the tower-free f64 `Q` to truncation — i.e. it does **not** embed the
  fitted value. The "0.008 ppb in q₀" drift the bean feared was already absorbed
  by the 2026-07-03 raw-pin restore; nothing left to re-pin.

Verified: `q_parameter` imports clean, `Q = 1.1099785827513808`, no `46·u` tower
anywhere in the pin path.
