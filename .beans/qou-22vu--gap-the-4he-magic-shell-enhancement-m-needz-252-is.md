---
# qou-22vu
title: 'GAP: the 4He magic-shell enhancement M_need/z ~ 2.52 is not derivable-and-checkable -- only one magic point exists'
status: completed
type: task
priority: normal
created_at: 2026-08-30T19:42:23Z
updated_at: 2026-08-30T19:43:09Z
---

## Result (2026-08-30) — not derivable-and-checkable, and the blocker is countable

PR #6315, branch `claude/magic-shell-enhancement-2026-08-30`. Full write-up:
[`docs/audits/2026-08-30-he4-magic-shell-enhancement-not-derived.md`](../docs/audits/2026-08-30-he4-magic-shell-enhancement-not-derived.md).

### 1. `a_D^(4)` IS derived — `bk-coordination-multiplicity.md` mislabels it

The block says the 2.52 factor "is likewise **an AME read rather than a derived
Schur-Weyl period**". Half of that is backwards, and it is the damaging half.

`a_D^(n) = lw(n-1) = sum_{lam|-n} dim_q(lam)/n`
(`theta_wn_kernel_derive_or_refute.py:86`, PR #3270) is a Schur-Weyl q-dimension
sum at the substrate q0 — no AME, no anchor, no free parameter. Exact q=1 limit
`I(n)/n`, I = A000085 (`QOU.Mass.sum_numSYT_eq_involutionNumber`).

    a_D^(2) = 1.0                  q=1: 1
    a_D^(3) = 1.3369656222357074   q=1: 4/3
    a_D^(4) = 2.5327796563993915   q=1: 5/2
    a_D^(5) = 5.3761377296793154   q=1: 26/5

`M_need/z = 2.5188914618` is the AME read; `a_D^(4)` is derived. The
IDENTIFICATION is what is unsupported. The comparison was already committed on
main as `candidates_z_aD` in `bk-crossing-coordination.witness.json` — it needed
reading as a test, not discovering.

### 2. Being a-priori, `z*a_D^(A)` can be tested — and it fails

    3H    M_need 2.00311688   z*a_D 2.67393124   +33.49 %
    3He   M_need 2.06118960   z*a_D 2.67393124   +29.73 %
    4He   M_need 7.55667439   z*a_D 7.59833897   + 0.5514 %

    B(4He) pred 28.4516737527 MeV vs AME2020 28.2956624 MeV -- miss +0.156 MeV.

The block's own "~30 % overshoot at A=3" IS this: `a_D^(3) = 1.3370` against the
A=3 pair's `M_need/z ~ 1.00`. Not a separate caveat — the same law refuted one A
down.

0.55 % is a DISCREPANCY, not agreement within errors: every input to
`M_need(4He)` is known to <~1e-7 relative (AME2020 B, CODATA m_e, an exact
hyperbolic volume). No experimental slack for 5.5e-3.

So the block SELECTS between two parameter-free candidates (`z` if non-magic,
`z*a_D^(A)` if magic) and 4He is the only datum selecting it. One fitted bit,
one point, zero residual constraint — the `qou-ebs6` shape with the denominator
reduced by one.

### 3. Genericity — the offset is IN RANGE, not FORCED

Window `M_need/z*(1 +- 0.005514)` = `[2.505003, 2.532780]`, width 0.0278.
Pre-registered parameter-free family of 3996 (q-brackets, rationals, `q0^k*p/r`)
→ 7 hits, and ALL SEVEN are closer to the AME read than `a_D^(4)` is:

    q0^5*(3/2)  = 2.52734339537   0.336 %   <- beats a_D^(4) by 1.6x
    q0^4*(5/3)  = 2.52992208303   0.438 %
    q0^3*(11/6) = 2.50717836774   0.465 %
    a_D^(4)     = 2.53277965640   0.551 %

The near-match carries no information favouring `a_D^(4)` specifically. Same
failure mode the `S_leak` offset-window check found for `c3 + Vol(4_1)`.

### 4. Scope-(b) EXCLUSION — the Wigner-SU(4) route cannot SIZE it

`QOU.Mass.WignerSU4RowBoundInactive` (new, sorry-free, lean-direct exit 0,
`#print axioms` = propext / Quot.sound / Classical.choice on all 8 decls).

Invariant `rows_le`: a partition of n has at most n parts, since every part >= 1.
Hence for every n <= 4 the SU(4) "at most 4 rows" constraint holds for EVERY
partition (`su4_inactive_of_le_four`), so the admissible set IS the full set, and
for EVERY weight into EVERY AddCommMonoid the restricted Schur-Weyl sum equals
the unrestricted one (`su4_restricted_sum_eq`). `su4_no_magic_enhancement` says
it at n=3 and n=4 at once: the restriction does the same nothing at both, so no
functional built from it can carry a factor present at 4He and absent at A=3.

`su4_active_at_five`: the bound is genuine and first bites at n=5 (all-ones
partition) — exactly the `dim[1^5] = 0` fact used to LOCATE the turnover. So
SU(4) is a real constraint that is inactive PRECISELY on the range where the
enhancement lives.

Non-vacuity checked, not assumed: an `example` resolves the
`[Fintype (Nat.Partition 4)]` binder by instance search.

Narrow by construction — excludes the SU(4)-row-restriction route to sizing and
nothing else. Not other Schur-Weyl functionals, not non-representation-theoretic
consequences of the closed shell, not the A=3 `z = A-1` match.

### The blockers, precisely

**(B1) `Vol_A` stops at A=4, so there is exactly ONE magic point.**
`binding_link_volumes.py` assigns links for 2H (Hopf), 3H (8_11), 3He (L6a4) and
the 4He L6a4 base; no nucleus->knot accessor for A >= 5 (the knot-periodic-table
appendix is knot-indexed, not nucleus-indexed). 2H is degenerate (Vol(Hopf) = 0
exactly). Three usable points, one magic. A magic/non-magic selector fitted on
one point cannot be validated now, and cannot be validated by more work on this
axis — only by extending `Vol_A` past A=4, which is a different problem (the
block already says 16O/40Ca are alpha-conjugate clusters, not single hyperbolic
links).

**(B2) The 30 % A=3 overshoot consumes the rest of the dataset.** With three
usable points, an explanation costing one further free parameter has spent
everything.

### Recommendation (judgement, not a finding)

Correct the block's label; do not chase a seventh candidate. Not because the
space is exhausted but because THE DATASET CANNOT DISTINGUISH CANDIDATES — the
window already holds parameter-free expressions closer than the named one, and
there is no second magic point to break the tie.

### What would change it

1. Extend `Vol_A` to a second magic nucleus (16O — already named in the corpus
   and in `qou-o16k` for the independent kappa question). One more magic point
   turns the selector from unfalsifiable into testable.
2. Derive the multiplicity from the jet-filtration SUM
   `B(K) = m_e sum_n a_D^(n) w_n(K)` rather than from its collapse to
   `M_need*Vol_A`. That is the open `w_n(K)` residue-weight question — input (3)
   of the `prop:jet-filtration-binding-extensive` scope note — not this one.

### Follow-ups opened

- `qou-sh62` — correct the mislabel in `bk-coordination-multiplicity.md`.
