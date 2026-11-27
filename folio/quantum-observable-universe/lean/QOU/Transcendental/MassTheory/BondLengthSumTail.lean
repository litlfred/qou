import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.RingTheory.PowerSeries.Basic

/-!
# The sum over all γγ bond lengths: why it needs a weight, and its tail

Brief C2 (compute-accuracy epic `qou-myts`), front E, towards the open kernel `qou-brng`.
Audit: `docs/audits/2026-11-27-bond-rules-and-length-cutoff.md`.

## Setting

Let `V_s = σ_s σ_{s+1}⁻¹` be the chiral vertex of the ruled photon, acting on a module `M`, and
`S = ∑_s V_s` over the `n − 2` vertices of `n` strands. The sum over all bond words of every length,
each vertex carrying a weight `t`, is `∑_L (t • S)^L`. Two facts settle whether a length cutoff is
needed.

* **A fixed vector forces the radius.** In the Schur–Weyl module the top state `|0…0⟩` is an
  eigenvector of `σ_s` with eigenvalue `q` and of `σ_s⁻¹` with `q⁻¹`, so every vertex fixes it and
  `S` acts on it by `n − 2`. The weighted partial sums act on it by `∑_{L<K} (t(n−2))^L`, which is
  at least `K` once `t(n−2) ≥ 1`. So the series cannot converge for `t ≥ 1/(n−2)`; at the corpus
  scale `t ≈ h(q₀) ≈ 0.209` that already happens at `n = 9` (A = 3).
* **Below the radius the tail is geometric.** In a complete normed ring, `‖a‖ < 1` gives
  `‖∑_{L > L₀} a^L‖ ≤ ‖a‖^{L₀+1}/(1 − ‖a‖)`.

The formal (surreal) reading: as a power series in the weight, the remainder after truncation at
`L₀` is divisible by `X^{L₀+1}`, with order exactly `L₀ + 1` when its first coefficient is
nonzero. That is bookkeeping in `R⟦X⟧`; it says nothing about the size of the remainder at a real
weight, which is what the archimedean lemma is for.

## What is proved

Generic (`[CommRing R]`, any module):
1. `vertex_fixes` — `σ v = q • v`, `τ v = q' • v`, `q * q' = 1` ⇒ `(σ * τ) v = v`.
2. `sum_fixes` — vertices all fixing `v` ⇒ `(∑_{s ∈ F} V s) v = (#F : R) • v`.
3. `pow_apply_of_eigen` — `S v = c • v` ⇒ `(S ^ L) v = c ^ L • v`.
4. `geom_partial_apply_of_eigen` — `(∑_{L<K} (t • S)^L) v = (∑_{L<K} (t*c)^L) • v`.
5. `X_pow_dvd_remainder`, `not_X_pow_succ_dvd_remainder` — the truncation remainder has `X`-adic
   order exactly `L₀ + 1` when `c (L₀+1) ≠ 0`.

Archimedean, after the wall (`ℝ`, normed rings):
6. `card_le_geom_partial` — `1 ≤ r` ⇒ `K ≤ ∑_{L<K} r^L` (no convergence at or beyond the radius).
7. `norm_tail_le` — `‖a‖ < 1` ⇒ `‖∑' n, a^(n + (L₀+1))‖ ≤ ‖a‖^(L₀+1) / (1 − ‖a‖)`.

The bridge `|tr Y| ≤ ‖Y‖₂` for the normalised quantum trace (the weight `K = diag(q, q⁻¹)` is positive
with `Tr K = [2]`) is used by the probe and cited, not formalised:
-- Ref: [kassel1995] Ch. XIV (quantum trace); [horn-johnson-2013] von Neumann trace inequality (|Tr(KY)| ≤ ‖Y‖ Tr K for K ⪰ 0).
No empirical number appears in any statement.
-/

namespace QOU.MassTheory.BondLengthSumTail

open PowerSeries

section Generic

variable {R : Type*} [CommRing R] {M : Type*} [AddCommGroup M] [Module R M]

/-- A chiral vertex `σ τ` fixes a common eigenvector whose eigenvalues multiply to `1`
(in the Schur–Weyl module: `|0…0⟩`, eigenvalues `q` of `σ_s` and `q⁻¹` of `σ_{s+1}⁻¹`). -/
theorem vertex_fixes (σ τ : Module.End R M) (v : M) (q q' : R)
    (hσ : σ v = q • v) (hτ : τ v = q' • v) (hq : q * q' = 1) : (σ * τ) v = v := by
  rw [Module.End.mul_apply, hτ, map_smul, hσ, smul_smul, mul_comm, hq, one_smul]

/-- If every vertex fixes `v`, their sum acts on `v` by the number of vertices. -/
theorem sum_fixes {ι : Type*} (F : Finset ι) (V : ι → Module.End R M) (v : M)
    (h : ∀ i ∈ F, V i v = v) : (∑ i ∈ F, V i) v = (F.card : R) • v := by
  rw [LinearMap.sum_apply, Finset.sum_congr rfl h, Finset.sum_const, Nat.cast_smul_eq_nsmul]

theorem pow_apply_of_eigen (S : Module.End R M) (v : M) (c : R) (h : S v = c • v) (L : ℕ) :
    (S ^ L) v = c ^ L • v := by
  induction L with
  | zero => simp
  | succ L ih => rw [pow_succ', Module.End.mul_apply, ih, map_smul, h, smul_smul, pow_succ]

/-- The weighted sum over word lengths `< K` acts on an eigenvector by the scalar geometric sum. -/
theorem geom_partial_apply_of_eigen (S : Module.End R M) (v : M) (c t : R) (h : S v = c • v)
    (K : ℕ) : (∑ L ∈ Finset.range K, (t • S) ^ L) v = (∑ L ∈ Finset.range K, (t * c) ^ L) • v := by
  have h' : (t • S) v = (t * c) • v := by
    rw [LinearMap.smul_apply, h, smul_smul]
  rw [LinearMap.sum_apply, Finset.sum_smul]
  exact Finset.sum_congr rfl fun L _ => pow_apply_of_eigen _ v _ h' L

/-- Formal (surreal-bookkeeping) reading: the remainder after truncation at length `L₀` is
divisible by `X^(L₀+1)`. -/
theorem X_pow_dvd_remainder (c : ℕ → R) (L₀ : ℕ) :
    (X : R⟦X⟧) ^ (L₀ + 1) ∣ mk (fun L => if L ≤ L₀ then 0 else c L) := by
  rw [X_pow_dvd_iff]
  intro m hm
  rw [coeff_mk, if_pos (Nat.lt_succ_iff.mp hm)]

/-- ... and its order is exactly `L₀ + 1` when the first omitted coefficient is nonzero. -/
theorem not_X_pow_succ_dvd_remainder (c : ℕ → R) (L₀ : ℕ) (hc : c (L₀ + 1) ≠ 0) :
    ¬ (X : R⟦X⟧) ^ (L₀ + 2) ∣ mk (fun L => if L ≤ L₀ then 0 else c L) := by
  rw [X_pow_dvd_iff]
  intro h
  have := h (L₀ + 1) (by omega)
  rw [coeff_mk, if_neg (by omega)] at this
  exact hc this

end Generic

section Archimedean

/-- At or beyond the radius the geometric partial sums are unbounded: `1 ≤ r ⇒ K ≤ ∑_{L<K} r^L`.
With `r = t(n−2)` this is the bond series on the fixed vector `|0…0⟩`. -/
theorem card_le_geom_partial (r : ℝ) (hr : 1 ≤ r) (K : ℕ) :
    (K : ℝ) ≤ ∑ L ∈ Finset.range K, r ^ L := by
  have : ∑ L ∈ Finset.range K, (1 : ℝ) ≤ ∑ L ∈ Finset.range K, r ^ L :=
    Finset.sum_le_sum fun L _ => one_le_pow₀ hr
  simpa using this

/-- Geometric tail bound below the radius, in any complete normed ring. -/
theorem norm_tail_le {A : Type*} [NormedRing A] [CompleteSpace A] (a : A) (ha : ‖a‖ < 1)
    (L₀ : ℕ) : ‖∑' n, a ^ (n + (L₀ + 1))‖ ≤ ‖a‖ ^ (L₀ + 1) / (1 - ‖a‖) := by
  have h0 : 0 ≤ ‖a‖ := norm_nonneg a
  have hg : Summable fun n : ℕ => ‖a‖ ^ (L₀ + 1) * ‖a‖ ^ n :=
    (summable_geometric_of_lt_one h0 ha).mul_left _
  have hle : ∀ n : ℕ, ‖a ^ (n + (L₀ + 1))‖ ≤ ‖a‖ ^ (L₀ + 1) * ‖a‖ ^ n := by
    intro n
    calc ‖a ^ (n + (L₀ + 1))‖ ≤ ‖a‖ ^ (n + (L₀ + 1)) := norm_pow_le' a (by omega)
      _ = ‖a‖ ^ (L₀ + 1) * ‖a‖ ^ n := by rw [pow_add, mul_comm]
  have hn : Summable fun n : ℕ => ‖a ^ (n + (L₀ + 1))‖ :=
    Summable.of_nonneg_of_le (fun _ => norm_nonneg _) hle hg
  calc ‖∑' n, a ^ (n + (L₀ + 1))‖ ≤ ∑' n, ‖a ^ (n + (L₀ + 1))‖ := norm_tsum_le_tsum_norm hn
    _ ≤ ∑' n, ‖a‖ ^ (L₀ + 1) * ‖a‖ ^ n := Summable.tsum_le_tsum hle hn hg
    _ = ‖a‖ ^ (L₀ + 1) * (1 - ‖a‖)⁻¹ := by rw [tsum_mul_left, tsum_geometric_of_lt_one h0 ha]
    _ = ‖a‖ ^ (L₀ + 1) / (1 - ‖a‖) := by rw [div_eq_mul_inv]

end Archimedean

end QOU.MassTheory.BondLengthSumTail
