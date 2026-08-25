---
# qou-4dq1
title: Resolve the 6 conflicting open PRs and land them
status: in-progress
type: task
priority: normal
created_at: 2026-08-25T10:08:52Z
updated_at: 2026-08-25T11:26:16Z
---

## Map (measured 2026-08-25 by git merge-tree against origin/main)

| PR | conflicts | shape | state |
|---|---|---|---|
| #4673 | (was) 0, but rebase-red | convention C→D shift, see below | **MERGED** |
| #4766 | 1 | docs/coordination/trace-convention-registry.json | resolved, verifying |
| #4619 | 1 | .beans/qou-3q7t bean, append-only | trivial |
| #5249 | 2 | rho_k_h3a_refinement.py + its witness | producer re-run needed |
| #4868 | 2 | delta_lambda_k_star_variance_phase5d_5b.py + witness | producer re-run needed |
| #4718 | 4 | 2 lepton producers + 2 witnesses | producer re-run needed |
| #4925 | 8 | 4 add/add content blocks + references.ts + mass-theory.ts | main has later edited copies |
| #5500 | 2 | SKIP — its own body says "DO NOT MERGE YET, knowingly red" |
| #5352, #5402 | — | SKIP — author said do not merge |

## The finding that came out of #4673

Rebasing moved two probes' numbers 22 % / 26 % and turned the convention audit's
own gate red. Attributed by running the UNMODIFIED producer in a worktree at the
pre-rebase merge-base: it reproduces the old numbers there and the new ones on
main. Not a regression — `_wenzl_constants` moved C -> D, and under D the Wenzl
level collapses to r = 2, so y_lambda = 0 exactly for every partition with three
or more rows (25 of 30 at n = 9). Already Lean-proved on main
(`wenzlLevel_conventionD`, `schurPrincipal_eq_zero_iff`) and measured by
`two_row_support_recount.py`; nothing re-derived.

Two consequences that were live in #4673 and are now fixed there:

1. Its headline "7.7 % undeclared systematic from the |chi|-vs-signed choice" was
   ALL of the measured spread and is a convention-C artifact — the ten negative-
   weight partitions under C all have ell >= 3, so under D |chi| is a no-op.
   Measured under D: 0.0146 %, all of it the p-n crossing.
2. `mu3_door_budget_probe` printed "the negative blocks supply ~1/7.6e39 of what
   the door needs". There are no negative blocks; sum|y_neg| = 1.04e-42 is
   round-off at 40 dps. Round-off reported as a measurement.

GENERALISATION NOT YET SWEPT: 32 producers import `y_lambda_at_q0_mpmath`, and
several reason explicitly about three-row or negative-weight structure
(`threerow_sign_crossing_decomp`, `threerow_sign_crossing_probe`,
`threerow_4he_completion_probe`, `threerow_qcross_trend_probe`,
`ylambda_sign_content_threshold_probe`, `mirror_split_milnor_one_third_probe`).
Any of them written pre-2026-08-09 may be measuring an object D sets to zero, or
dividing by round-off. Not swept here — separate bean when someone picks it up.


## Progress 2026-08-25

MERGED: #4673, #4766, #4619, #5249, #4868, #4718. Remaining: #4925 (8 conflicts).
SKIPPED, deliberately: #5500 (its own body says DO NOT MERGE, knowingly red),
#5352 and #5402 (author said do not merge).

All six used a merge-of-main rather than a rebase, because the resolution has to
live in a commit and GitHub then refuses `rebase`. Merge method `merge`, never
squash. Each merge commit records which side each hunk went to and why.

Resolutions worth remembering, because three of them went AGAINST the branch:

* #4868, both hunks -> MAIN. The branch's `K_atom_chis.get(..., mp.mpf(0))`
  raised TypeError on the first atom (the witnesses store chi_lambda as
  strings), and its `M_E_MEV = 0.51099895` was a hand-typed truncated m_e whose
  binary64 expansion was being serialized as 50 digits.
* #5249 -> BRANCH, but only for the named constant; main had already converged
  on the fix independently. What the branch still contributes is the root-cause
  record and the retraction of bean qou-8x1l.
* #4718 -> BRANCH on both, but carrying main's precision fix INTO the branch's
  shared module rather than dropping it. See below.

## Two defects found by re-running, both fixed at the producer

1. `wlambda_covariance_epic_A3_transfer_bound_extension` (#4868) emitted three
   raw float64 fields into a witness the branch ADDS — so not in the baseline,
   so a genuine NEW dirty witness. `mp.nstr`, baseline untouched.
2. `lepton_tower_core` (#4718) binds M_E / M_MU / M_TAU as module-scope
   `mpf("...")` while its docstring says precision is the caller's business.
   True of the functions, false of the constants: they bind at IMPORT time at
   mpmath's default dps 15. Measured, `mpf("0.51099895000")` ->
   `0.5109989499999999518209393`. I expected this to be a non-issue on the
   grounds that an 11-digit literal fits in binary64, and that was wrong --
   measure, do not reason about it.

## Two findings handed on rather than fixed

* `qbeta-habiro-integrality-kill-test.witness.json`: recomputing it gives
  `4.703e-4` against a committed `-8.657e-52`. Forty-eight orders of magnitude,
  in a producer whose name is a kill test. Found incidentally, because #4718
  makes 59 previously-uncollected test files collectible and one of them runs
  that producer at IMPORT time -- so `pytest --collect-only` now writes a
  witness. Both halves want an owner: the staleness, and the side-effecting
  import.
* #4925 is the last conflicted PR and the only hard one. Its four content
  blocks landed on main separately (commit a1fcca562d) and main has since
  edited both -- the \operatorname drain and the nq_01 trap-drain -- so the
  add/add conflicts must resolve toward main. Its `references.ts` predates
  main's `LibraryRef` interface, so a naive resolution DELETES that interface
  and re-breaks 712 TS2353 errors. It still carries four genuinely new blocks
  (birthday-axioms-underdetermine, ideal-tetrahedron-law-of-sines,
  ideal-tetrahedron-volume-well-defined, kummer-identity-radial-reduction) plus
  a new probe, so it is worth landing rather than closing.


## Closed out 2026-08-25

SEVEN merged: #4673, #4766, #4619, #5249, #4868, #4718, #4925. Zero conflicting
PRs remain that are mine to touch.

Two left alone, both deliberately:

* **#5500** — its own body says "DO NOT MERGE YET, knowingly red" (Q0_FLIP 53).
* **#5746** — conflicts, but ALL 15 of its non-bean files are byte-identical to
  main; only the bean differs, and main's version is the LATER one (closed the
  item, opened qou-t1kv). Merging would revert a bean. Its last commit is ~2 h
  old, inside the 3 h stall window, so not a takeover target. Commented on the
  PR with the measurement and two dispositions rather than pushing to it.

## #4925 — the resolution worth remembering

Two of its four new content blocks were DUPLICATES of blocks main already
carries under different labels, and the Lean is what proved it rather than my
reading of the prose: `kummer-identity-radial-reduction` and
`ideal-tetrahedron-volume-well-defined` point at `QOU.Knot.KummerRadial.kummer`
and `QOU.MathlibExt.IdealTetrahedron.volume_rotate` — the exact declarations
main's `kummer-bloch-wigner-identity` and `ideal-tetrahedron-relabelling-
invariance` already point at. Registering both would have put two content blocks
on one Lean decl. Dropped the two, retargeted
`birthday-axioms-underdetermine`'s dangling `uses[]` edge, run-validate exit 0.

**When two blocks might be duplicates, compare their `lean.ref`, not their
prose.** Prose comparison said "these look like the same theorem"; the shared
declaration said so without judgement.

Its `references.ts` looked like it added 13 references. It did not — all 13 were
present at the merge-base, so main DELETED them. Resolving toward main gives an
id set byte-identical to main's. A stale branch's apparent additions can be
someone else's deletions.
