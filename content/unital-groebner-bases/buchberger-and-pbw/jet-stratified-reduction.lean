import Mathlib.Data.Nat.Basic

/-!
# Jet-Stratified Gröbner–Shirshov Reduction

Content-block Lean sibling for `def:jet-stratified-reduction`.

The full formalization lives in the `UGB` library module
`UGB/GrobnerShirshov/JetOrder.lean`, which the content pipeline
resolves via the Lake package (candidate-2 resolution under the
package's Lake root). It declares:

- `jet_stratified_gs_criterion`, `descended_gs_inherited`,
  `degree_filtered_reduction_correct` — axiomatised GS-criterion
  results (each carries a `-- Ref:` to [fred2005] §3 / [bergman1978]);
- `jet_stratified_correct` — the conditional main theorem, proved
  from `jet_stratified_gs_criterion`;
- `DegreeBucket`, `bucketize` — degree-bucketed reduction data;
- `spolyCountNaive`, `spolyCountStratified`, `spolySavings` — the
  S-polynomial complexity counts.

This sibling does **not** re-`export` those declarations: the
`UGB` library is not on the standalone `lean`-direct path, and the
structural results depend on the full `UGB.GrobnerShirshov`
dependency cone. Re-stating them here would either fail to resolve
(`unknown module prefix 'UGB'`) or shadow the genuine library
declarations. Instead the self-contained complexity counts are
restated faithfully below (pure `ℕ` arithmetic, identical to the
library definitions), so the headline `O(m²)` → `O(mk + k²)`
S-polynomial savings is checkable standalone.

LaTeX label: `def:jet-stratified-reduction`

## References
- [fred2005] §3, Proposition 3.8
- [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5
-/

namespace UGB.GrobnerShirshov.ContentBlock

/-- **S-polynomial count** at level `n+1` under jet stratification.

    Let `m = |Σₙ|` (descended rules) and `k = |Σ^trans|` (transient).
    Naive Buchberger checks `(m + k) choose 2 ≈ O((m+k)²)` pairs.
    Faithful to `UGB.GrobnerShirshov.spolyCountNaive`. -/
def spolyCountNaive (m k : ℕ) : ℕ := (m + k) * (m + k - 1) / 2

/-- Jet-stratified S-polynomial count: `m·k + k choose 2 ≈ O(mk + k²)`
    pairs. Faithful to `UGB.GrobnerShirshov.spolyCountStratified`. -/
def spolyCountStratified (m k : ℕ) : ℕ := m * k + k * (k - 1) / 2

/-- Pairs skipped by jet stratification: `m choose 2 ≈ O(m²)`.
    Faithful to `UGB.GrobnerShirshov.spolySavings`. -/
def spolySavings (m k : ℕ) : ℕ := m * (m - 1) / 2

/-- The three counts partition the naive pair count: the stratified
    work plus the skipped descended×descended pairs recover the naive
    total, `binom(m+k,2) = m·k + binom(k,2) + binom(m,2)`. Checked
    here at the SU(2) Hecke level (`m = 2` descended Hecke/far-comm
    rules, `k = 2` transient rules), the standalone-verifiable
    instance of the headline `O(m²) → O(mk + k²)` savings. -/
theorem spoly_count_decomposition_su2 :
    spolyCountStratified 2 2 + spolySavings 2 2 = spolyCountNaive 2 2 := by
  rfl

/-- Jet stratification strictly skips work whenever there are ≥ 2
    descended rules: at the SU(2) level it skips one descended×descended
    pair (`spolyCountStratified 2 2 = 5 < 6 = spolyCountNaive 2 2`). -/
theorem spoly_stratified_lt_naive_su2 :
    spolyCountStratified 2 2 < spolyCountNaive 2 2 := by
  decide

end UGB.GrobnerShirshov.ContentBlock
