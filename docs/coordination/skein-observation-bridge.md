# Coordination ledger — the Skein-observation bridge

**Goal.** Formalize the shared Skein substrate on which three QOU-internal
reformulations of hard open problems live — **q-Collatz halting**, the
**P-vs-NP** computational horizon, and **q-Navier–Stokes** regularity — as one
`SkeinObservationSystem` graded by a single length filtration `len`, read through
the Markov-trace observation.

**Owner session.** `session_018pe73GaKJwUHjVf98sWSpB` (2026-07-25).

## Landed on `main` this session

| PR | SHA | Content |
|----|-----|---------|
| #4239 | `8b52daab` | `SkeinObservationSystem` (step/obs/len/normalForm); `haltsObserved_of_halts` (C12); `halts_of_len_descent`; `PolyObservable`/`PolyCollapse`; `separation_of_residue_nonzero` (the residue proof-by-contradiction skeleton); `Regular`/`BlowsUp` + `regular_of_len_nonincreasing` (q-NS); q-Collatz instantiation; `vortexReductionSystem` + `regular_iff_bkm`; the `rem:skein-filtration-trichotomy` content block |
| #4205 | `1a591543` | content-bearing `QuantumComputationalUniversality` carrier (resolves a dangling `lean.ref`); classical Cardona Reeb-Turing proposition split |
| #4252 | `508a89b3` | C9 — `qcollatz_kummer_removable_iff_two_dvd_chi` (the even-branch `[2]_q` divisor ⟷ the universal χ(A) obstruction) |
| #4256 | `a096aec0` | `regular_and_halts_of_len_orbit_descent` (cross-pollination: one descent ⇒ q-NS regularity **and** q-Collatz halting); `vortexReductionSystem_regular_and_halts`; P-vs-NP rate leg `not_polyObservable_of_horizon_cost` + `lt_three_pow` |
| #4264 | `3e38faef` | `treeSearch` — the `3^c` lower bound proved in the decision-tree model (`treeSearch_hcost`); `no_horizon_cost_of_polyObservable` + `not_polyObservable_or_not_horizon_cost` — the algebrization-obstruction core |

All `lean`-direct exit 0, sorry-free. Every hard leg is an honest hypothesis or
a clearly-scoped model result — nothing fabricated, nothing wired to production.

## The three walls (open, honest)

1. **q-Collatz descent measure `μ`** on `ℤ[q^{±1}]` — the `[2]_q`-adic valuation
   descends on even steps, is uncontrolled on odd steps (the natural `v_[2]`
   candidate provably fails). Degree-balance also fails (the odd `+1` cancels the
   top term at the fixed point `−q⁻²`). No elementary `μ` known.
2. **q-NS regularity in the `q→1` infinite-dimensional limit** — #4258 shows no
   finite unforced truncation blows up in-model; the hard core is the infinite
   limit (= the `BlowsUp` / unbounded-filtration regime the `Regular` predicate
   does not cover).
3. **P-vs-NP faithfulness leg** — `res ≠ 0 ⇒ P ≠ NP` with `P`/`NP` opaque
   (#4141's `PNeqNpEquivalence`, still `sorry`). The separating residue must be
   **non-algebraic** (the algebrization obstruction, #4264).

**Cross-pollination map** (partly machine-checked): a single controlled descent
on `len` settles q-Collatz halting **and** q-NS non-blow-up (`regular_and_halts_
of_len_orbit_descent`); P-vs-NP is that descent plus a polynomial-rate bound.

## χ(A) = −6 — the corrected reading (2026-07-25)

Recurrent question: *is χ(A) = −6 implied by the QOU axioms?* Corpus-grounded
answer:

- **χ(A) = −6 is *equivalent* to a cohomological condition**, not a free numeric
  input: it is the genus-4 Bring fiber `Σ₄` via `χ = 2 − 2g`, whose cohomology is
  `H₁(Σ₄)` (rank `2g = 8`). Fixing the genus-4 fiber cohomology **implies**
  χ = −6 (`brings-surface/embeddability-closure.md`,
  `genus-ideal-characterisation.md`).
- **Bare `(𝐂, A, τ)` axioms with an arbitrary fiber do *not* force χ = −6** — a
  different-genus fiber gives a different χ(A) (the framework keeps
  `other-euler-intro` variants). So the genus-4 fiber is the *Descartes-selecting*
  cohomological condition, and χ = −6 is its numerical shadow.
- **Consequence for C9 (#4252):** the `χ(A) = −6` hypothesis is correctly scoped
  (a general QOU need not be genus-4); it is shorthand for "the fiber is the
  genus-4 Bring surface", a cohomological condition — not an arbitrary number.
- **Consequence for the P-vs-NP gate:** the non-algebraic residue the
  algebrization obstruction demands is naturally a class in `H₁(Σ₄) / HH²(U_q)` —
  genuinely topological, exactly what is *not* recoverable from polynomial Jones
  data. This is the honest home of the separating residue.

## Sibling coordination

| Sibling | Relationship | Action |
|---------|--------------|--------|
| #4141 (P-vs-NP, `claude/p-not-equal-np-status-dfdq41`) | this cluster is **downstream** of its faithfulness leg; `separation_of_residue_nonzero` consumes its `res≠0 ⇒ P≠NP` as `hequiv` | posted update — infra now on main; stalled/`dirty`, needs rebase |
| #4258 (q-NS, `claude/q-ns-classical-gaps-9l9mj9`) | **structural ↔ numerical** counterpart: `regular_of_len_nonincreasing` (no blow-up from non-increasing filtration) vs its "no finite unforced blow-up" probe | posted intent — no file overlap; results partition the problem (finite `Regular` vs infinite `BlowsUp`) |

## Next non-overlapping task

The honest terminal gate: **whether the χ(A) / `H₁(Σ₄)` residue is genuinely
non-algebraic** (the actual route to P≠NP, per the #4264 obstruction). This is
P≠NP-hard and cannot be closed; the productive move is to *state it precisely* as
a cohomological non-algebraicity condition tied to the genus-4 surface, and let
the corpus's Bring-surface machinery (`genus-ideal-characterisation`,
`embeddability-closure`) supply the candidate class — coordinating with #4141
(which owns the P≠NP carrier) rather than proliferating a competing one.
