# Proton-mass substrate-identity work plan (PR #1272)

**Branch:** `claude/brave-mendel-FPxFl`
**Status:** in flight (this commit + follow-ups)
**Goal:** advance the m_p substrate identity from "empirical 0.24 ppm
near-match" toward fuller categorical proof + production wiring.

## The identity (current state)

$$y_{(3)}(q_0) \cdot (m_p + 12 \cdot m_e) \;=\; 2 \cdot m_\mu \cdot |\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q_0)|$$

(equivalently: `m_p = 2·m_μ·F_Bor(q_0) − 12·m_e` where `F_Bor := |tr_M|/y_(3)`).

Matches CODATA to **0.24 ppm**.

## Work items in this PR

| # | Item | Status | Commit |
|---:|---|---|---|
| 1 | Add substrate identity content trio (`.ts`+`.md`+`.lean`) | ✅ done | f8f42df2 |
| 2 | Add production compute script `m_p_substrate_identity_50dps.py` | ✅ done | f8f42df2 |
| 3 | Identify F_Bor categorically as `|tr_M|/y_(3)` | ✅ done | f7096221 |
| 4 | Refine "2" as `dim V_(2,1)` (per sibling PR #1288 trace-dominance) | ✅ done | c2d7f8e3 |
| 5 | Correct "12 = Ocneanu reciprocal" claim (WRONG — different braid) | ✅ done | 801b69db |
| 6 | Lean cleared-form Prop + numerical-witness theorem | this commit | — |
| 7 | Test identity extension to neutron + ⁴He | this commit | — |
| 8 | Polish `proton-mass-substrate-identity.md` for paper-readiness | this commit | — |
| 9 | Factor-2 categorical bridge (class hypothesis per AGENTS.md §3b-cond) | this commit | — |
| 10 | Coordinate sweep on siblings (#1276, #1287, #1288, #1289) | ✅ done | (comments) |
| 11 | Final prepare-merge-auto pipeline | follow-up | — |

## Open structural pieces (after this PR)

These can NOT be closed in-PR; flagged for follow-ups:

| Piece | Why open | Where to attack |
|---|---|---|
| "12" categorical origin (NOT Ocneanu) | Numerical near-integer; structural rep-theory interpretation unknown | Investigate β_Bor representation theory at H_3; search for invariant equal to 12 |
| Factor 2 = `dim V_(2,1)` full proof | Why does dim of trace-dominant rep enter linearly in mass formula? | Formal categorical statement of mass formula via Wedderburn block expansion |
| Hoefsmit symbolic for genuine Ocneanu −1/12 | PR #546's 2×2 block bug pending | Continue PR #546 (sibling work) |
| Lean LSP verification of 30+ theorems | No lake in this remote env | Verify in lake-enabled session |

## Calibration discipline status

- CAL-1 (m_e): unchanged
- CAL-2 (m_μ/m_e or equivalently q_0): unchanged
- CAL-3 (𝔇_π): unchanged (already derived to 6 ppb via N=3 ladder; my session does NOT improve this)

Session's contribution: m_p direct from CAL-1 + CAL-2 + q_0 at 0.24 ppm, with the structural integers 2 and 12 partially identified (2 = dim V_(2,1); 12 = empirical near-integer pending categorical origin).

## After this PR

Prepare-merge-auto pipeline:
1. Final rebase onto main (already done)
2. Push all commits (rolling)
3. Address final review-thread triage (per coordinate skill §5)
4. Merge via rebase (per AGENTS.md §rule 7 default merge method)
