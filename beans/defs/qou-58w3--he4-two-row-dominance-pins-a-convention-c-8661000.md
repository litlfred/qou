---
# qou-58w3
title: he4-two-row-dominance pins a convention-C 866/1000 that D makes exactly 1
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T13:41:43Z
updated_at: 2026-11-20T08:32:31Z
parent: qou-cdx1
---

Under convention D the two-row share is exactly 1 (QOU.MassTheory.TwoRowCap.twoRow_share_eq_one_of_wenzl, PR #5242, sorry-free). The block asserts >= 0.80 with an empirical 86.6% pinned into a 3b-cond instance 'ratio := 866/1000'.

866/1000 is NOT a weaker-but-valid bound. A share below 1 records a nonzero >=3-row contribution, which is what D forbids. The witness self-identifies as C-frame: the .md table reports the sign rep (1^12) at 4.7e-10, which under D is exactly 0.

The sibling def:two-row-stratum already withdrew the figure 2026-08-09 ('under the production convention D the restriction is not a dominance but an identity'); he4-two-row-dominance.{md,ts,lean} was never updated. The two blocks have contradicted each other for a week.

Also: dominant_block_positive_share : (1:Q)/77 <= 866/1000 is a norm_num numeral tautology with no 4He content.

FIX: retire class HasHe4TwoRowDominance, restate as a corollary of the cap with share = 1, re-derive or retire the C-frame top-5 table.
NOT done in #5242: needs qa-sweep, and folio-assistant is not set up in that sandbox (disk 1.3G free).

## 2026-11-15 — Convention-D upgrade (`litlfred/qou#7986`)

- Updated `folio/quantum-observable-universe/mass-theory/he4-two-row-dominance.{lean,ts}` per owner ruling `Q-CDX1-1 = 1`:
  - Imported `QOU.MassTheory.TwoRowCap` and specialized `he4_twoRow_share_eq_one_of_wenzl` and `he4_threeRowPart_eq_zero_of_wenzl` directly from `QOU.MassTheory.TwoRowCap.twoRow_share_eq_one_of_wenzl` and `threeRowPart_eq_zero_of_wenzl`.
  - Updated `HasHe4TwoRowDominance` to `ratio := 1` (`ratio_eq_one : ratio = 1`, retiring the Convention-C `866 / 1000` pin and `dominant_block_positive_share`).
  - Kept `HasHe4DominantBlock` (`[9, 3]` vs `[12]`).
  - Verified with `lean -DautoImplicit=false -s 65536` (`EXIT: 0`, `0` warnings, `0` `sorry`).
- PR: [`litlfred/qou#7986`](https://github.com/litlfred/qou/pull/7986) (commit `fd12a6522e45d32a4855f0b4dd0db7ac856c2986`, signed `ready:` comment [`#issuecomment-6900782211`](https://github.com/litlfred/qou/pull/7986#issuecomment-6900782211)).


**2026-11-20T08:32:31Z — owner-approved status change (coordinator session_01VQDpPdnjTBLBcPi6D5gj61, PR #8542 batch A):** in-progress → completed. Work commit fd12a6522e4 is on main.
