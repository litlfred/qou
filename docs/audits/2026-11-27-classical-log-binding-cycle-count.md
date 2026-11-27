# The classical part of the ruled log binding law is a merge count

**Date** 2026-11-27 · **Brief** C2 (compute-accuracy epic `qou-myts`) · **Beans** `qou-brng`, `qou-v2om`, `qou-rf43`
**Lean** [`QOU/MassTheory/ClassicalLogBindingCycleCount.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/ClassicalLogBindingCycleCount.lean): sorry-free, lean-direct exit 0, `#print axioms` = `[propext, Classical.choice, Quot.sound]`
**Probe** [`computations/probes/classical_log_binding_cycle_count/`](../../computations/probes/classical_log_binding_cycle_count/): 4/4 checks, mpmath 50 dps at the proton pin, exact `Fraction` at `q = 1`, exact `ℚ(q)` for `z_D`, no float64
**Scope** (a) for the physics; the Lean statements are exact. Nothing fitted, selected, or wired.

## 0. Result in one paragraph

Under the ruled law `B = E₀·log(tr_free/tr_atom)`, the `q = 1` part of the convention-D trace turns the
binding into a whole number times `E₀·ln 2`: the number of closure components the bonds merge
(`classicalLogBinding_eq`). Three consequences are proved. (i) The γγ-cheapest bond `V³` is a
3-cycle cubed, so it is the identity at `q = 1` and merges nothing: the selected deuteron's whole
binding is a `q`-deformation correction, which is why it is keV and not MeV
(`selected_deuteron_classical_binding_zero`). (ii) With three strands per nucleon, at most `3A − 1`
merges are possible, so the classical binding per nucleon is strictly below `E₀·ln 8`
(`classicalLogBinding_le_ceiling`, `ceiling_lt_per_nucleon`). (iii) The Cayley length is
subadditive, so if a three-nucleon atom permutation is the product of its three pair bonds, the
classical `b₃` is `≤ 0` (`classicalB3_nonpos_of_product`). A positive classical `b₃` needs a
genuinely three-body permutation.

## 1. What was already on main (corpus grep)

| fact | where | relation to this note |
|---|---|---|
| `q = 1` trace is `2^{c(σ)−n}` | `ClassicalTraceFloor` (hypothesis), `MathlibExt/TensorTraceCharacter.trace_permMatrixOf_two` (proved) | used as step 1 |
| orbit count, defect, ±1 swap lemmas | `MathlibExt/OrbitCount` (`qou-qro1`) | used for subadditivity |
| the classical **linear** floor `2^{−A} − 2^{1−2A}` | `ClassicalTraceFloor` | retired functional; this note does the **log** one |
| "S2: the classical part of route-C `b₃` is quantised" | `docs/audits/2026-09-07-route-c-step3-and-kz-level-plans.md` §2 | planned, never formalised; done here (`classicalB3_quantised`) |
| pair-factorised `I(S)` gives `b₃ = 0` under log | `InteractionFactorNotPairwise.pairFactorised_b3_eq_zero` | consistent; (iii) is the classical-permutation analogue with an inequality |
| Boolean `b₃ < 0` on `(0,1)³` | `UrsellPartitionFunctionB3.b3corpus_neg` | about the Boolean assembly `W = 1 − Z`, not the ruled log law |

## 2. The theorems

`B_cl(σ_free, σ_atom) := E₀·log(tr₁(σ_free)/tr₁(σ_atom))`, `tr₁(σ) = 2^{c(σ)}/2^n`.

1. `classicalLogBinding_eq`: `B_cl = E₀·log 2·(c(σ_free) − c(σ_atom))`.
2. `classicalLogBinding_of_trivial_free`: with `σ_free = 1`, `B_cl = E₀·log 2·orbitDefect(σ_atom)`, the
   transposition length of the atom permutation.
3. `orbitDefect_le_card_sub_one`, `classicalLogBinding_le_ceiling`, `ceiling_lt_per_nucleon`,
   `ceiling_attained`: `B_cl ≤ E₀·log 2·(kA − 1) < A·E₀·log 2^k`, equality iff the closure is one
   component. `log_eight`: for `k = 3` the per-nucleon bound is `E₀·log 8`.
4. `orbitDefect_mul_le` (from `exists_swapProd`: every permutation is a product of exactly
   `orbitDefect` transpositions) and `classicalB3_nonpos_of_product`.
5. `classicalB3_quantised`: for any four words, `b₃^cl ∈ E₀·log 2·ℤ`.
6. Concrete words by `decide`: `nucleon_V3_classically_trivial`, `freeDeuteron_eq_one`,
   `selected_bond_merges_none` (`V(2)³`), `selected_bond_V1_merges_none` (`V(1)³`),
   `single_vertex_bond_merges_two` (`V(1)`, `V(2)`), and `merges_even_of_sign_one` with
   `vertex_sign`: every pure-junction bond is an even permutation, so it merges 0 or 2
   components on the deuteron, never 1.

No empirical number appears in any statement.

## 3. The probe

- **K0** `tr(σ₁) = q³/(q²+1) = z_D`, exact in `ℚ(q)`: the trace here is the corpus's convention-D trace.
- **K1** it reproduces the six rows of the γγ deuteron table (PR #9426 `results.md`) to the printed
  digits, including `V(2)³` ratio `0.998497160633`.
- **K2** at `q = 1`, exact: all 126 pure-junction bond words of 1–6 vertices on `V³ ⊗ V³` have trace
  `2^{c−n}`.
- **K3** their merge counts are exactly `{0, 2}` (parity, item 6).

**The `q₀` departure from the classical count** (`−ln r` at the proton pin, all 126 words):

| merges | words | classical `ln 2·m` | `−ln r(q₀)` range |
|---|---|---|---|
| 0 | 12 | 0 | −0.0352 … +0.0059 |
| 2 | 114 | 1.3863 | 0.7895 … 2.1923 |

So the classical count is the right order of magnitude for merging bonds, but the deformation moves a
6-vertex word by −43 % to +58 %. The ceiling of item 3 is a theorem at `q = 1` only.

## 4. Comparison with AME (scorecard only, not a derivation)

The merge unit at the ruled tower scale is `E₀·ln 2 = 2.930268` MeV (`E₀ = 4.2274834` MeV,
proton pin). AME 2020 in that unit:

| | B (MeV) | merges `B/(E₀ ln 2)` | finite-`A` classical ceiling `3A − 1` |
|---|---|---|---|
| ²H | 2.224566 | 0.759 | 5 |
| ³H | 8.481796 | 2.895 | 8 |
| ³He | 7.718041 | 2.634 | 8 |
| ⁴He | 28.295662 | 9.656 | 11 |
| ⁵⁶Fe | 492.25995 | 167.991 | 167 |
| ⁶²Ni | 545.26244 | 186.079 | 185 |
| `b₃` (sym) | 1.426220 | 0.487 | — |

Reading, with the hazards stated:

- Peak `B/A` sits at the asymptotic per-nucleon bound `E₀ ln 8 = 8.790805` MeV: ⁵⁶Fe −0.005 %,
  ⁶²Ni +0.043 %. **I saw `ln 8` in these numbers before I found the structural reason**, so this
  is a post-hoc match. With the order-zero `E₀` it is off by 0.99 %. And the heavy nuclei sit
  **above** the finite-`A` ceiling by about one merge (⁵⁶Fe 167.99 against 167), so the classical
  law cannot be the whole story there. The match is recorded, not used.
- `b₃` is 0.487 of a merge unit, so no classical word reproduces it (item 5). This agrees with the
  2026-09-07 S2 diagnostic.
- The light nuclei sit far below their ceilings, as a surface term would require, but nothing here
  derives a surface term.

## 5. What this changes

- The −99.7 % deuteron (budget row 1) now has a one-line structural cause: the selection rule
  `FrobeniusSelected` picks the cheapest γγ bond, and the cheapest γγ bond is classically
  trivial. MeV-scale binding needs a bond that merges closure components. Every merging
  pure-junction bond merges exactly two.
- The `b₃` sign question is restated classically: a positive `b₃` needs either an atom permutation
  that is not the product of its pair bonds, or a `q`-deformation contribution of order one merge
  unit (`0.49·E₀ ln 2`).
- Budget row 2 ("no pairwise assembly can make `b₃` positive") now has a classical-permutation
  version under the **ruled log law**, with an equality case. The earlier Lean result
  (`b3corpus_neg`) was about the Boolean assembly.

## 6. Open, with options (owner decision pending in the thread)

1. **Ceiling at `q₀`.** Is `−ln r(q₀) ≤ ln 2·(n − 1)` for one-component closures of bounded length?
   The table above shows the deformation can exceed the classical count by 58 % at fixed merges,
   so the answer is not obvious. This needs exact `ℚ(q)` traces on 9–12 strands (coordinate with
   B1, binding compute scaling).
2. **Bond selection.** The cheapest γγ bond merges nothing, so under the current rule the deuteron
   cannot bind at MeV scale. Whether some derived rule other than "cheapest" picks a merging bond
   is an owner question. Selecting a bond because it binds would be fitting.
3. **Three-body permutations.** Classify the three-nucleon γγ words whose permutation is not a
   product of pair-bond permutations, and measure their merge count against `3·m(²H)`.
