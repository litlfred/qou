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

## χ(A) = −6 — is it forced by the QOU axioms? YES (2026-07-25)

Recurrent question: *is χ(A) = −6 implied by the QOU axioms?* The corpus is
decisive — **yes, it is derived, via Bring's terminality.** (An earlier draft of
this ledger recorded an over-correction — "bare axioms don't force it"; that was
wrong. It missed that the 3-colour / Reeb / Frobenius–Hopf structure *is* part of
the axioms and forces g = 4. Corrected here per the corpus-grep discipline.)

- **Derivation chain** (`brings-surface/chi-minus-six-chain.md`): 3 colours + a
  Reeb flow + the Frobenius–Hopf structure ⟹ the `S₃ ⊂ S₅` orbits on the 6
  Weierstrass points ⟹ exactly 6 branch points ⟹ `|χ(A)| = 6` ⟹ (from
  `χ = 2 − 2g`) **g = 4**. `brings-surface-qou-intro.md`: *"three colours, a Reeb
  flow, and a χ = −6 ledger force a unique surface."*
- **Bring is the terminal object** (`brings-surface-example.md`): among all
  genus-4 curves Bring's surface `Σ₄` realises the maximal automorphism group
  `Aut(Σ₄) ≅ S₅` (order 120) and **any other genus-4 QOU maps to it — "this
  establishes the Descartes theorem."** So a non-Bring genus-4 fibre *factors
  through* `Σ₄`; the χ = −6 / `H₁(Σ₄)` structure is universal, not chosen.
- **Consequence for C9 (#4252):** the `χ(A) = −6` hypothesis is not an arbitrary
  stipulation — it is the numerical shadow of the forced genus-4 Bring terminal
  fibre. (It may still be carried as an explicit Lean hypothesis for a decl that
  is stated *before* the chi-minus-six-chain is available, but semantically it is
  a theorem of the framework, not a free input.)
- **Consequence for the P-vs-NP gate (strengthened):** the non-algebraic residue
  the algebrization obstruction (#4264) demands is a class in
  `H₁(Σ₄) / HH²(U_q)` — and since `Σ₄` is the **terminal** object, that residue
  is **canonical / universal**, not universe-dependent. Genuinely topological,
  exactly what polynomial Jones data cannot recover. This is the honest, canonical
  home of the separating residue.

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

## Consolidation pass — 2026-08-09 (PR #4861, corrected)

Rigor audit of the P≠NP leg + alignment of the three problems onto the shared
`SkeinObservationSystem`.

**Rigor verdict (P≠NP): not a proof, and honestly so.** `qou-p-neq-np` is a
`conjecture` (`validation: stub`); the Lean carrier `class QouPNeqNp : Prop` has
an un-instantiated `faithful` field (the open counting→decision transfer); the
cone is sorry-free and axiom-free. What is *proved* is strictly weaker
(`qou_physical_intractability_unconditional` → `geometry_of_incompleteness`).

**R1 RETRACTED (honest correction).** An earlier revision of this PR "fixed
dangling `QOU.PvsNPBoundary.*` refs" by creating three sibling `.lean` over
`SkeinObservationSystem`. That was a **regression based on a false premise**: the
three siblings
(`p-vs-np-boundary.lean` / `computational-boundary.lean` /
`polynomial-observable-subcategory.lean`) have existed on `main` since
`2e7abbd47` (2026-07-18), are **sorry-free**, and already define
`boundary_dichotomy` / `computationalBoundary` /
`polynomialObservableSubcategory` (a resolution-tree Set model). The refs were
**never dangling** — a mapping sub-agent reported them missing (it grepped the
library tree and missed the content-block siblings), and the overwrite deleted
~290 lines of landed sorry-free Lean. The overwrite is reverted; `main`'s
versions stand. Lesson: verify sibling-file existence directly before declaring
a `lean.ref` dangling.

**What actually landed this pass:**
- **R2** — fix the stale "single `sorry` on the Lean carrier" prose in
  `qou-p-neq-np.md` → accurate sorry-free class-hypothesis description.
- **Tier 2** — "Shared substrate" cross-refs on `q-collatz-conjecture.md`
  (descent leg), `q-bkm-criterion.md` (regularity leg), `qou-p-neq-np.md`
  (poly-rate leg), naming the one `len` filtration and `SkeinObservationSystem`.

**Tier 3 — no Lean tie-through added; it is already on `main`**
(`regular_and_halts_of_len_orbit_descent`, `vortexReductionSystem`,
`PNeqNpWallUnification`). The two remaining ties are conjecture-adjacent, beaned
`qou-gh14`, not laundered.

**Separately:** the #P→P≠NP robustness (PR #4866) — the transfer is named,
the Toda / algebrization / natural-proofs barriers recorded — and a sorry-free
Toda-consistency barrier lemma (PR TBD).
