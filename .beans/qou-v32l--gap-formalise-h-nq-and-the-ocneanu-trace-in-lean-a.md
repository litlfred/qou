---
# qou-v32l
title: 'GAP: formalise H_n(q) and the Ocneanu trace in Lean, and prove Wenzl 1988'
status: todo
type: task
priority: low
tags:
    - lean
    - hecke
    - mathlib-gap
    - wenzl
created_at: 2026-08-16T13:04:38Z
updated_at: 2026-08-16T13:04:38Z
---

## What is open

`QOU.QBeta.WenzlWeight.IsOcneanuWeightSystem` (PR #5230) axiomatises Wenzl
(1988) — that the Ocneanu/Markov-trace weights on `H_n(Q)` at
`z = Q^r(1−Q)/(1−Q^r)` are the principal specialisations
`s_λ(1, Q, …, Q^{r−1})`. Three declarations are conditional on it. **No instance
exists, and none should be added except by proving the theorem.**

To discharge it you must first be able to **state** Wenzl's theorem in Lean,
which needs `H_n(q)`, its `T_w` basis, its Markov trace, its partition-indexed
irreducible characters, and the Schur principal specialisation.

## Mathlib coverage — measured, not assumed

Surveyed against the pinned revision `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`
(toolchain v4.24.0), all 6990 modules of the local build.

**Exists and reusable:** Coxeter systems / length / reduced words / descents /
inversions (`Mathlib/GroupTheory/Coxeter/*`), `CoxeterSystem.lift`,
Artin–Wedderburn (strong — `exists_algEquiv_pi_matrix_divisionRing`),
`LinearMap.trace` / `Algebra.trace` / `Algebra.traceForm`, the `e/h/p/m`
symmetric polynomials + fundamental theorem, `YoungDiagram` and `Nat.Partition`.

**Absent:** the Iwahori–Hecke algebra (**entirely** — a grep for `Hecke` over all
6990 modules matches one bibliography line in the FLT docstring; there is not
even a modular-forms Hecke operator), braid groups `B_n` (the `Braid*` modules
are categorical braidings), Temperley–Lieb, Matsumoto's theorem, `S_n` as a
Coxeter group of type A, Specht modules / any `S_n` representation theory,
Schur polynomials, principal specialisation, hook lengths, contents, standard
Young tableaux, `f^λ`, RSK, Frobenius/symmetrising forms.

Two findings that matter more than "not yet ported":

- **The Coxeter files are an island.** `Coxeter` appears only inside the four
  `Coxeter/*` modules. Good foundations, load-bearing nothing.
- **`CoxeterMatrix.Aₙ` exists as a matrix but is never proved to present `S_n`.**
  That bridge is the first thing this build needs and it does not exist.

## The build, in dependency order

1. **`CoxeterSystem (CoxeterMatrix.Aₙ n) (Equiv.Perm (Fin (n+1)))`** — bootstrap
   from `Equiv.Perm.mclosure_swap_castSucc_succ` (generation exists; the
   presentation does not). Smallest item; independently Mathlib-worthy.
2. **`H_n(q)` + the `T_w` basis** — the sharp gap. Standard route needs
   **Matsumoto's theorem** (absent). Either prove Matsumoto for general Coxeter
   systems (`alternatingWord` / `braidWord` / `IsReduced` / the descent lemmas
   are the right substrate) or take the Bourbaki–Iwahori construction of the
   multiplication operators directly. The latter is likely cheaper and yields
   no reusable Mathlib theorem.
3. **Generic semisimplicity of `H_n(q)`** — Wedderburn is a black box, but Tits'
   deformation argument is absent, as is the decomposition of `K[S_n]`.
4. **Irreps indexed by partitions** — Specht modules + `q`-deformation. Not
   optional: without it the indexing set of the weight formula has no home and
   the theorem cannot be written down.
5. **`tr = Σ_λ y_λ χ_λ`** — decomposing a trace on a semisimple algebra into
   irreducible characters with weights is not packaged, and neither are central
   primitive idempotents as a labelled family.
6. **Schur polynomials + principal specialisation** — plus the `q`-hook-content
   formula, hence hook lengths, contents, `q`-integers; and SYT / `f^λ` for the
   `q → 1` checks.
7. **Wenzl's theorem**, on top of all of it.

**Honest size: Mathlib-contribution scale, not a session.** Plausibly several
thousand lines across 1–6 before 7 is stateable; items 2 and 4 are each real
mathematics to formalise, not transcription.

## The cheaper candidate — cost this before committing to the full route

**Prove only the vanishing set, not the weight formula.** Downstream the corpus
consumes the vanishing *set* (the trace annihilates exactly the `≥ 3`-row
blocks), not the weight *values*. That is what gives `radical = ⟨E⁽³⁾⟩`, the
`n! − Catalan(n)` coranks, and the `TL_n` compute quotient (`qou-ondw`).

Route: define `TL_n`, show the Markov trace factors through `H_n ↠ TL_n`,
identify `TL_n`'s blocks with the `≤ 2`-row partitions. **This skips items 5 and
6 entirely** — the whole symmetric-function and hook-content stack.

Not free: still needs 1–4, and `TL_n`'s block structure is its own
representation theory. It also yields something weaker than the class as stated,
so the class would need re-shaping around the vanishing set rather than the
weight identity.

## Two non-routes, named so nobody reaches for them

- **Redefine rather than prove.** Declaring the Ocneanu weight to *be* the
  principal specialisation makes the class vacuous by fiat and destroys the
  content — `radical = ⟨E⁽³⁾⟩` means something only because the weights are the
  *trace's* Wedderburn weights.
- **Fixed-`n` verification.** Tractable at `n = 3` (#5185 did it symbolically),
  but the class quantifies over all Young diagrams with no `n` parameter, so a
  fixed-`n` instance does not fit without reformulation; and `n = 6` is
  720-dimensional, past any kernel decision procedure. Buys confidence, not
  unconditionality.

## Before starting

- [ ] Check whether Hecke algebras are **in flight for Mathlib upstream**. The
      survey covers the pinned build only, not open PRs. If items 1–3 are
      already landing, contribute there instead of duplicating.
- [ ] Cost the `TL_n`-only route against the full route explicitly, and record
      the comparison, before writing item 2.

## Recommendation on record

**Keep the conditional and cite it honestly** (`docs/audits/2026-08-16-ocneanu-weight-axiomatisation.md`).
The dependency is a 39-year-old, widely-used published theorem, not a gap in the
framework's own reasoning; the cost of discharging it is out of proportion to
the risk that Wenzl is wrong.

If this build happens, do it **for its own sake** — items 1–4 are independently
valuable to the corpus and to Mathlib, and the `TL_n` infrastructure is what
`qou-ondw` wants anyway. Discharging this class would be a by-product, not the
motivation.

## Related

- `qou-smtg` — its step 2 (the `ℓ(λ) ≥ 3` vanishing at `z_D`) landed in #5217;
  steps 1, 3, 4 remain open. This bean is the layer *beneath* it: what would
  make #5217's result unconditional rather than Wenzl-conditional.
- `qou-ondw` — the `TL_n` compute quotient; shares the cheaper route's infra.
- `qou-fpjy` — the class-carried-input visibility gap this axiomatisation
  surfaced.
- `qou-7d08` — the Lean level-family residue.
- `qou-5hul` (completed) — a prior assessment of "genericity ⇒ semisimple =
  Hecke radical theory, deep Mathlib gap". Read it before re-deriving item 3.
