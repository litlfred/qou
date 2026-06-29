---
# sy7b
title: 'SYT HLF: close dimAitkenIdentity via branching bijection (numSYTenum_branching + dimHLF_branching)'
status: todo
type: task
priority: normal
created_at: 2026-06-28T17:05:00Z
updated_at: 2026-06-29T00:00:00Z
---

## Progress (2026-06-29)

Merged to main — steps 1 + the 2-row half of step 2 complete, all sorry-free:
- **#2984** — HLF reduced to (A)+(B): `numSYTenum_eq_dimHLF_of_branchings`
  (strong induction + termination `sz_decrementRow_lt` + base `sz=0` +
  `decrementRow_sorted`); plus combinators and decide-pinned n≤5 targets and
  the n≤7 axiom-free regression backstop.
- **#3044** — `dimHLF_pair`: two-row dimension = ballot number
  `C(a+b,b)−C(a+b,b−1)` (integrality infra; dodges floor-division).
- **#3051** — `dimHLF_branching_pair`: **obligation (A) proved on two rows**
  via Pascal + binomial monotonicity/symmetry (4 cases).

Remaining frontier (harder, step up in difficulty):
- **(A) general m-row** — the β-number Lagrange/Vandermonde identity over a
  variable number of rows (no ballot-style closed form; the general hook side
  `prodHooks·betaProdGap = betaFactProd` is already sorry-free in
  `SYTHookFormulaBetaProd`, so the remaining piece is the dimension-side
  Lagrange identity). **KEYSTONE FOUND (2026-06-29, verified m≤4):** the
  manifestly-integer form is the Frobenius/Aitken determinant
  `dimHLF λ = Σ_{σ∈S_m} sgn(σ)·multinomial(n; (λ_i−i+σ(i)))` — generalises the
  2-row ballot number exactly; the remaining work is the `Matrix.det_vandermonde`
  formalization (multi-day, LSP). Full path: the scope doc §"Update (2026-06-29)".
- **(B) `numSYTenum_branching`** — the SYT corner-deletion bijection on the
  brute-force enumerator (the multi-day core).

## CONVERGENCE / coordination (2026-06-29) — DO NOT DUPLICATE

Sibling **PR #2986** (`claude/gnw-corner-recursion-hlf-kk4cnm`) has **discharged
(B) sorry-free** (the GNW corner-deletion bijection on Mathlib `YoungDiagram`/
`StandardYoungTableau`, built on my #2984 composition) and reduced the HLF to the
**same single gap (A)** — `gnwHookIdentity`/`dimHLF_branching`. They are **actively
closing (A)** via a clean ℚ-polynomial **Lagrange-interpolation** route
(`SYTBetaLagrange` node-poly → `G = R + H·Q` → `SYTLagrangeInterp.interp_leadingCoeff`
keystone; 2 sorries left). This is the **same** β-Lagrange identity my
`det_vandermonde`/`frobeniusDim` route targets — so the `det_vandermonde` grind is
**HELD to avoid duplication** (coordination posted on #2986).

Division of labour: **they own (A) via Lagrange**; my merged assets stand as
cross-checks/regression backstops — #3051 (A 2-row, sorry-free), #3067/#3071
(`frobeniusDim` manifestly-integer form + divisor-free keystone, decide-verified
n≤5). When their (A) lands ⇒ (A)+(B) ⇒ fully sorry-free `numSYTenum_eq_dimHLF` and
`dimAitkenIdentity` discharged. Offered to help close their `SYTBetaLagrange`/
`SYTLagrangeInterp` sorries if wanted.


Close the single remaining sorry in the SYT hook-length cone,
`SYTHookFormulaGeneral.dimAitkenIdentity` (general-n Frame–Robinson–Thrall).
Multi-session effort (~1-2 weeks), no owner gate (pure ℕ combinatorics).

Full plan + Lean signatures + effort/risk table:
docs/workplans/2026-06-28-syt-hlf-branching-bijection-scope.md

Sequencing (net-sorry discipline — never commit 3 open sorries):
1. removableCorners / decrementRow defs + characterizing lemmas (sorry-free, low risk).
2. (A) dimHLF_branching — Lagrange/partial-fraction recursion, divisor-free ℕ (sorry-free; biggest tractable win).
3. State (B) numSYTenum_branching with ONE honest sorry + Ref; prove composition conditional on (B).
   Corpus then carries one sharp sorry (the bijection) instead of the opaque determinant identity.
4. (B) the deletion bijection on standard fillings — the multi-day core, high risk.
5. On (B): dimAitkenIdentity + numSYTenum_eq_dimHLF go sorry-free; retire the _of_aitken wrappers.

Regression backstop: decide-verified n≤7 (SYTEnumerationN7.numSYTenum_eq_dimHLF_7,
dimAitkenIdentity_le4/_5/_6) — all axiom-free kernel decide.

Origin: PR #2984, branch claude/lean-proof-sorries-lyxk3h.
