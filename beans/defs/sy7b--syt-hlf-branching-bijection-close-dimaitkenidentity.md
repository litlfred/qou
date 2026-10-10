---
# sy7b
title: 'SYT HLF: close dimAitkenIdentity via branching bijection (numSYTenum_branching + dimHLF_branching)'
status: completed
type: task
priority: normal
created_at: 2026-06-28T17:05:00Z
updated_at: 2026-07-02T17:12:10Z
---

## FINAL WIRING DONE (2026-07-02, PR #3219)

The last sorry in the SYT hook-length cone is closed:
`IdentityIHLFBridge.dimSYT_eq_dimHLF` (`#SYT(λ) = n!/∏h_c` on the genuine
`Nat.card` count) proved by composing `SYTEnum.dimSYT_eq_numSYTenum`
(counting bridge) with `SYTEnum.numSYTenum_eq_dimHLF` (GNW general HLF).
Adds `rskBurnsideHolds_iff_dimHLF`: `RSKBurnsideHolds n` is now equivalent
to a computable `dimHLF` sum. Verified lean-direct exit 0 (24-module dep
cone, no errors, no sorry warnings). Stale "open/deferred" doc comments in
`RSKBurnsideTarget`/`SYTEnumerationBridge`/`SYTHookFormula` refreshed.

PR #3219 MERGED 2026-07-02 (rebase-merge, 59fc4abc).

Follow-up DONE same day (PR #3225, `claude/rskburnside-partitionsof-bridge-2026-07-02`):
`PartitionsOfBridge.lean` proves the `Nat.Partition n ↔ partitionsOf n`
enumeration bridge (partsFuel soundness/completeness/nodup by fuel induction,
`toFinset_partitionsOf`, `sum_map_partitionsOf`) and discharges
**`RSKBurnsideHolds n` sorry-free for all n ≤ 12** on the genuine SYT count —
no RSK correspondence. Direct kernel `decide` over `Fintype (Nat.Partition n)`
probed and refuted (instance does not kernel-reduce; recorded in docstring).

Bean is CLOSEABLE once PR #3225 merges.

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

## CONVERGENCE / coordination (2026-06-29) — KEYSTONE DONE (det route)

Sibling **PR #2986** (`claude/gnw-corner-recursion-hlf-kk4cnm`) has **discharged
(B) sorry-free** (the GNW corner-deletion bijection on Mathlib `YoungDiagram`/
`StandardYoungTableau`, built on my #2984 composition) and reduced the HLF to the
**same single gap (A)** — `gnwHookIdentity`/`dimHLF_branching`, which it attacked via
a hand-rolled ℚ-polynomial **Lagrange-interpolation** keystone
`SYTLagrangeInterp.interp_leadingCoeff`.

**Owner ruling (2026-06-29): drop the interpolation keystone; use the determinant
route.** Owner dislikes interpolation over ℝ/ℚ (conditioning baggage) and prefers
exact determinant algebra. **PR #3079** (`claude/syt-hlf-vandermonde-keystone`) now
provides the drop-in replacement, **SORRY-FREE + AXIOM-FREE**, lean-direct verified
(`QOU/Mathlib/SYTVandermondeKeystone.lean`):

- `cof_mul_vWeight` — the Vandermonde cofactor product-split `cofᵢ·vWeightᵢ = det V`,
  proved by splitting `det_vandermonde`'s pair product at the pivot row via
  `Fin.prod_univ_succAbove` (helpers: `succAbove_image_Ioi`, `inner_split`,
  `pivot_contribution`, `det_vandermonde_pivot_split`).
- `powSum` — `∑ᵢ (βᵢ)ᵈ/vWeightᵢ = [d=k]` for `d ≤ k`.
- `interp_leadingCoeff` — `∑ᵢ f.eval(βᵢ)/vWeightᵢ = f.coeff k` for `f.natDegree ≤ k`
  (over `Fin (k+1)`).  **Same statement** as the sibling's keystone under `k ↦ k−1`
  (`Fin k`, `<k`, `coeff (k−1)`); `vWeight` defs are identical.  No interpolation, no ℝ.

Bridge for #2986: import `QOU.Mathlib.SYTVandermondeKeystone` and adapt
`interp_leadingCoeff` with `k := k−1` (their `0 < k` supplies `k−1+1 = k`).  Coordination
posted on #2986.  Other merged assets stand as cross-checks/regression backstops —
#3051 (A 2-row), #3067/#3071 (`frobeniusDim` manifestly-integer form, decide-verified
n≤5).  When (A) closes on this keystone ⇒ (A)+(B) ⇒ fully sorry-free
`numSYTenum_eq_dimHLF` and `dimAitkenIdentity` discharged.


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

## (A) CLOSED — gnwHookIdentity sorry-free (2026-06-29, PR #3115)

`claude/gnw-hookid-removecorner-2026-06-29` (#3115) discharges the **sole remaining
GNW gap** `SYTHookGNW.gnwHookIdentity` SORRY-FREE (lean-direct exit 0), closing
obligation (A) on the GNW route. The per-corner hook ratio + assembly:
- R1 `betaProdGap_ratio`, R2 `prodHooks_ratio` (per-corner hook ratio, non-row-drop),
  R3 `prodHooks_removeCorner` (filter-zero invariance ⇒ row-drop corner), all in
  `SYTHookGNWRatio.lean`.
- R4 assembly `gnwHookIdentity_proof`: sum over corners (non-corners vanish via
  `β_c−1=β_{c+1}`) ⇒ `betaLagrange_range` ⇒ `sz l`, bridging the corner list-sum to
  the `det_vandermonde`-keystone β-Lagrange identity.

So the GNW route is fully sorry-free end-to-end: `cornerRecursion` +
`gnwHookIdentity` ⟹ `numSYTenum_eq_dimHLF_gnw` (general Frame–Robinson–Thrall HLF)
⟹ `dimAitkenIdentity_of_gnw` — discharging the Mathlib-blocked `dimAitkenIdentity`
with no Specht/RSK/determinant infra. Remaining to fully retire the
`SYTHookFormulaGeneral.dimAitkenIdentity` sorry itself: route it through
`dimAitkenIdentity_of_gnw` (a follow-up wiring edit).

## PR #2986 status (2026-06-29, rebased + keystone-swapped)

Honoring the owner determinant ruling: SYTBetaLagrange now rests on
SYTVandermonde.interp_leadingCoeff (Matrix.det_vandermonde, merged #3079); the
branch's hand-rolled SYTLagrangeInterp interpolation keystone is DELETED.

Sorry-free on this branch: betaLagrange (the β-Lagrange identity), obligation (B)
numSYTenum_branching, cornerRecursion, and the full gnwHookIdentity→betaLagrange
Vandermonde wiring (SYTHookGNWWiring: betaVec/betaNat, sum_betaVec_sub, betaGapProd
_cast/_row_cast, betaProdGap_cast = ∏_{i<j}(βᵢ−βⱼ), betaFactProd_cast = ∏βᵢ!).

Single remaining cited sorry: gnwHookIdentity, reduced to the per-corner ratio
prodHooks(l)/prodHooks(l∖c) = β_c·∏_{j≠c}(β_c−1−β_j)/(β_c−β_j) — the betaProdGap/
betaFactProd ratio under removeCorner (incl. row-drop). Vandermonde+factorial infra
for it is all proved; the ratio surgery is the remaining work.
