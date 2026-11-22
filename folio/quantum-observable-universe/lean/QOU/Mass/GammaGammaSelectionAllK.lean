import QOU.Mass.GammaGammaFrobeniusSelection

/-!
# Reading 3 selects `β_Bor` among ALL γγ words of `H₃`, with no bound on the vertex count

Bean `qou-ales`. Owner 2026-11-21 ("Ok" to option 1: make "`β_Bor` is derived" unconditional in
the number of vertices).

Earlier steps proved the selection on candidates with at most 5 (`frobeniusSelected_borromean`)
and at most 10 (`GammaGammaSelectionTen.frobeniusSelected_borromean_ten`) vertices. Those
proofs worked through the sign of `χ_k = tr V^k` for each `k`, and their docstrings left
"does `3 ∣ k` persist for all `k`" open.

## The bounded question was never needed

The cost is the crossing count, and `V^k` has `2k` crossings. Once `V¹` and `V²` are infeasible
and `V³` is feasible, every other feasible candidate costs at least `6`. So the selection holds
on the full candidate set, every non-empty γγ word inside `H₃`, without knowing a single sign
beyond `k = 3`.

## What is proved (sorry-free)

* `gammaGammaH3Cands`: the candidate set, every non-empty γγ-produced word that uses only the
  `H₃` generators.
* `frobeniusSelected_borromean_all`: on `1 < q ≤ 23/20` and any weight with `y_std > 0`,
  reading 3 selects `β_Bor = V³` among all of them.
* `frobeniusSelected_all_eq_borromean`: it is the only selected word.

## What is NOT true, and so not claimed

"`V^k` is feasible iff `3 ∣ k`" for all `k`. It fails at the proton pin: `χ_k = 2 cos kθ` with
`2 cos θ = −1 − h²`, so `θ = 2π/3 + δ` with `δ = 0.025423` at `q₀`. The first `k` that breaks the
pattern is `k = 23` (`k ≡ 2 mod 3`, feasible). This is measured with mpmath at 60 digits in
`computations/qbeta/qbeta_gg_all_k_pattern_probe.py`, not proved here. It does not affect the
selection, because `V²³` costs 46.
-/

namespace QOU.Mass.GammaGammaSelectionAllK

open QOU.Mass.GammaGammaWordSelection
open QOU.Mass.GammaGammaSelectorH3
open QOU.Mass.GammaGammaFrobeniusSelection

/-- Every non-empty γγ-produced word that uses only the `H₃` generators. -/
def gammaGammaH3Cands : Set Word := {w | GammaGammaWord w ∧ InH3 w ∧ w ≠ []}

theorem mem_cands_iff_vertexPow {w : Word} :
    w ∈ gammaGammaH3Cands ↔ ∃ k, 1 ≤ k ∧ w = vertexPow k := by
  constructor
  · rintro ⟨hg, h3, hne⟩
    obtain ⟨k, rfl⟩ := gammaGamma_inH3_eq_vertexPow hg h3
    refine ⟨k, ?_, rfl⟩
    rcases Nat.eq_zero_or_pos k with h0 | h0
    · subst h0; exact absurd rfl hne
    · exact h0
  · rintro ⟨k, hk, rfl⟩
    refine ⟨vertexPow_gammaGamma k, inH3_vertexPow k, ?_⟩
    intro h
    have := congrArg List.length h
    rw [vertexPow_length] at this
    simp at this
    omega

theorem frobeniusSelected_borromean_all {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (y : H3Block → ℝ) (hy : 0 < y .std) :
    FrobeniusSelected (hoefsmitH3 q) y gammaGammaH3Cands (fun w => (w.length : ℝ)) borromean := by
  obtain ⟨n1, n2, f3, _, _⟩ := hoefsmit_vertexPow_frobenius_table hq1 hq2 y hy
  refine ⟨mem_cands_iff_vertexPow.2 ⟨3, by norm_num, vertexPow_three.symm⟩, ?_, ?_⟩
  · rw [← vertexPow_three]; exact f3
  · intro w' hw' hf
    obtain ⟨k, hk, rfl⟩ := mem_cands_iff_vertexPow.1 hw'
    rw [← vertexPow_three, vertexPow_length, vertexPow_length]
    by_cases h1 : k = 1
    · subst h1; exact absurd hf n1
    by_cases h2 : k = 2
    · subst h2; exact absurd hf n2
    have : 3 ≤ k := by omega
    exact_mod_cast (by omega : 2 * 3 ≤ 2 * k)

theorem frobeniusSelected_all_eq_borromean {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (y : H3Block → ℝ) (hy : 0 < y .std) {w : Word}
    (hw : FrobeniusSelected (hoefsmitH3 q) y gammaGammaH3Cands (fun w => (w.length : ℝ)) w) :
    w = borromean := by
  have hc := hw.cost_eq (frobeniusSelected_borromean_all hq1 hq2 y hy)
  obtain ⟨k, _, rfl⟩ := mem_cands_iff_vertexPow.1 hw.mem
  rw [← vertexPow_three, vertexPow_length, vertexPow_length] at hc
  have : k = 3 := by
    have : ((2 * k : ℕ) : ℝ) = ((2 * 3 : ℕ) : ℝ) := by exact_mod_cast hc
    have := Nat.cast_injective this
    omega
  rw [this, vertexPow_three]

end QOU.Mass.GammaGammaSelectionAllK
