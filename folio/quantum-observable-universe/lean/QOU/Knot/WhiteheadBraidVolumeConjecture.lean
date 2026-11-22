import QOU.Knot.WhiteheadMarkovClosure
import QOU.Knot.WhiteheadVolumeConjectureUnconditional

/-!
# The volume conjecture for the coloured Jones of the Whitehead braid closure

`WhiteheadVolumeConjectureUnconditional` proves the volume limit for van der Veen's closed
formula `whiteheadLinkKashaev N`, the value of `vdvWhiteheadLinkJones` at `s = e^{πi/N}`.
`WhiteheadMarkovClosure` proves that the same formula, at a generic `σ` with `q = σ²`, is
`[N]⁻¹ J(β)`. Here `J` is the writhe-normalised quantum-trace functional of
`jonesSl2_isMarkovInvariant`, and `β = σ₁⁻² σ₂ σ₁⁻¹ σ₂ ∈ B₃` is the Whitehead braid.

These two statements do not compose directly. At the Kashaev point `q = e^{πi/N}` the quantum
integer `[N]` vanishes: the irreducible `V_N` of the braid-closure construction is not defined
there, and `[N]⁻¹ J(β)` is a `0/0`. This file closes that gap with a limit.

* `tendsto_vdvWhiteheadLinkJones`: van der Veen's formula is continuous at every `s₀ ≠ 0` with
  `s₀^{2i} ≠ 1` for `1 ≤ i < N`, which holds at `e^{πi/N}`.
* `eventually_braidGeneric`: the hypotheses of the braid-closure construction hold at every `σ`
  in a punctured neighbourhood of `σ₀ = e^{πi/(2N)}`. Each one fails only on a finite set of
  roots of unity.
* `tendsto_braidJonesRT_whitehead`: for every braid `p` Markov-equivalent to `β`, the normalised
  invariant `[N]⁻¹ J(p)(σ)` tends to `whiteheadLinkKashaev N` as `σ → σ₀`, `σ ≠ σ₀`.
* `whiteheadBraid_volume_conjecture`: with the limit above as the value at the Kashaev point,
  `(2π/N) log ‖·‖ → Vol(W) = Vol(Borromean)/2`.

**Scope.** `J` is an invariant of the braid up to Markov moves. Reading it as an invariant of the
closed link, so that any braid with the Whitehead link as closure gives the same value, is
Markov's theorem, which is not formalised here (issue #8902).

The value at the Kashaev point is defined here as a punctured limit of the generic invariant.
That is the standard meaning of `J_N(K; e^{2πi/N})` for the normalised coloured Jones, whose
generic value is a Laurent polynomial in `q`. This file does not prove that polynomiality; it
proves the limit exists and computes it.

-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, Lemma 1 and Theorem 1
-- Ref: [kashaev1997] Kashaev, "The hyperbolic volume of knots from the quantum dilogarithm"
-- Ref: [murakami-murakami2001] Murakami–Murakami, "The colored Jones polynomials and the simplicial
   volume of a knot"
-/

namespace QOU.Knot.FigureEightVolume

open Filter Topology Complex
open QOU.Mass.QuantumSl2
open QOU.Mass.QuantumSl2.MarkovTrace
open QOU.IwahoriHecke.BraidGroup (BraidGroupN)
open QOU.Torsion.MassTraceMarkovClass (artinTower)
open QOU.MathlibExt.MarkovMoves

/-! ### Continuity of van der Veen's formula -/

theorem tendsto_zpow_at {s₀ : ℂ} (h0 : s₀ ≠ 0) (m : ℤ) :
    Tendsto (fun s : ℂ => s ^ m) (𝓝 s₀) (𝓝 (s₀ ^ m)) :=
  (continuousAt_id.zpow₀ m (Or.inl h0)).tendsto

/-- **van der Veen's formula is continuous** at every `s₀ ≠ 0` at which no denominator
`1 − s^{2i}`, `1 ≤ i < N`, of the clasp function vanishes. -/
theorem tendsto_vdvWhiteheadLinkJones {N : ℕ} {s₀ : ℂ} (h0 : s₀ ≠ 0)
    (hroot : ∀ i : ℕ, 1 ≤ i → i < N → 1 - s₀ ^ (2 * (i : ℤ)) ≠ 0) :
    Tendsto (fun s => vdvWhiteheadLinkJones s N) (𝓝 s₀) (𝓝 (vdvWhiteheadLinkJones s₀ N)) := by
  have hz := tendsto_zpow_at h0
  unfold vdvWhiteheadLinkJones
  refine tendsto_finset_sum _ fun n hn => ?_
  have hn := Finset.mem_range.mp hn
  unfold vdvBeltFused vdvClasp
  refine (tendsto_finset_sum _ fun j _ => hz _).mul ?_
  refine (hz _).mul (tendsto_finset_sum _ fun k _ => ?_)
  refine (hz _).mul (tendsto_finset_prod _ fun j hj => ?_)
  have hj := Finset.mem_range.mp hj
  refine Tendsto.div ((tendsto_const_nhds.sub (hz _)).mul (tendsto_const_nhds.sub (hz _)))
    (tendsto_const_nhds.sub (hz _)) ?_
  have h := hroot (j + 1) (by omega) (by omega)
  push_cast at h
  exact h

/-- The Kashaev point `s₀ = e^{πi/N}` satisfies `s₀^{2i} ≠ 1` for `1 ≤ i < N`. -/
theorem kashaev_pow_ne_one {N i : ℕ} (hi1 : 1 ≤ i) (hiN : i < N) :
    1 - Complex.exp (((Real.pi / N : ℝ) : ℂ) * I) ^ (2 * (i : ℤ)) ≠ 0 := by
  intro h
  have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
  rw [← Complex.exp_int_mul, sub_eq_zero, eq_comm, Complex.exp_eq_one_iff] at h
  obtain ⟨n, hn⟩ := h
  have him := congrArg Complex.im hn
  simp at him
  -- `2 i π / N = 2 π n`, so `i = n N`
  have hre : (i : ℝ) = n * N := by
    field_simp at him
    nlinarith [Real.pi_pos]
  have hz : (i : ℤ) = n * N := by exact_mod_cast hre
  have hi1' : (1 : ℤ) ≤ i := by exact_mod_cast hi1
  have hiN' : (i : ℤ) < N := by exact_mod_cast hiN
  rcases le_or_gt n 0 with hn0 | hn0
  · nlinarith
  · nlinarith

/-! ### The generic hypotheses hold near the Kashaev point -/

/-- The hypotheses of the braid-closure construction at `σ`, `q = σ²`, colour `N = m + 1`. -/
def BraidGeneric (m : ℕ) (σ : ℂ) : Prop :=
  σ ≠ 0 ∧ σ ^ 2 - (σ ^ 2)⁻¹ ≠ 0 ∧ ∀ i, 0 < i → i ≤ 2 * m + 1 → qint (σ ^ 2) i ≠ 0

/-- A point avoids a finite set on a punctured neighbourhood of any point. -/
theorem eventually_not_mem_of_finite {S : Set ℂ} (hS : S.Finite) (a : ℂ) :
    ∀ᶠ x in 𝓝[≠] a, x ∉ S := by
  have hopen : (S \ {a})ᶜ ∈ 𝓝 a :=
    (hS.diff).isClosed.isOpen_compl.mem_nhds (by simp)
  filter_upwards [mem_nhdsWithin_of_mem_nhds hopen, self_mem_nhdsWithin] with x hx hxa
  intro hxS
  exact hx ⟨hxS, hxa⟩

/-- The finite set where the generic hypotheses can fail: `0` and the roots of unity of order
dividing `4i`, `1 ≤ i ≤ 2m + 1`. -/
def braidBadSet (m : ℕ) : Set ℂ :=
  {0} ∪ ⋃ i ∈ Finset.Icc 1 (2 * m + 1), {σ : ℂ | σ ^ (4 * i) = 1}

theorem braidBadSet_finite (m : ℕ) : (braidBadSet m).Finite := by
  refine (Set.finite_singleton 0).union (Set.Finite.biUnion (Finset.finite_toSet _) ?_)
  intro i hi
  have hi : 0 < 4 * i := by
    have := (Finset.mem_Icc.mp hi).1
    omega
  refine (Polynomial.nthRoots (4 * i) (1 : ℂ)).toFinset.finite_toSet.subset ?_
  intro x hx
  simpa [Polynomial.mem_nthRoots hi] using hx

theorem braidGeneric_of_not_mem {m : ℕ} {σ : ℂ} (h : σ ∉ braidBadSet m) :
    BraidGeneric m σ := by
  have h0 : σ ≠ 0 := fun h' => h (Or.inl h')
  have hroot : ∀ i, 1 ≤ i → i ≤ 2 * m + 1 → σ ^ (4 * i) ≠ 1 := fun i h1 h2 h' =>
    h (Or.inr (Set.mem_biUnion (Finset.mem_Icc.mpr ⟨h1, h2⟩) h'))
  have hq0 : σ ^ 2 ≠ 0 := pow_ne_zero 2 h0
  -- `q^k − q^{−k} = 0` forces `σ^{4k} = 1`
  have hnum : ∀ k, 1 ≤ k → k ≤ 2 * m + 1 → (σ ^ 2) ^ k - (σ ^ 2)⁻¹ ^ k ≠ 0 := by
    intro k h1 h2 hk
    apply hroot k h1 h2
    have hk' : (σ ^ 2) ^ k = ((σ ^ 2) ^ k)⁻¹ := by
      rw [inv_pow] at hk
      exact sub_eq_zero.mp hk
    have hk0 : (σ ^ 2) ^ k ≠ 0 := pow_ne_zero k hq0
    have := congrArg (· * (σ ^ 2) ^ k) hk'
    simp only [inv_mul_cancel₀ hk0] at this
    rw [show 4 * k = 2 * k + 2 * k by ring, pow_add, pow_mul]
    simpa using this
  have hden : σ ^ 2 - (σ ^ 2)⁻¹ ≠ 0 := by
    have := hnum 1 le_rfl (by omega)
    simpa using this
  refine ⟨h0, hden, fun i hi1 hi2 => ?_⟩
  exact div_ne_zero (hnum i hi1 hi2) hden

/-- **The generic hypotheses hold on a punctured neighbourhood** of every point. -/
theorem eventually_braidGeneric (m : ℕ) (σ₀ : ℂ) : ∀ᶠ σ in 𝓝[≠] σ₀, BraidGeneric m σ :=
  (eventually_not_mem_of_finite (braidBadSet_finite m) σ₀).mono fun _ h =>
    braidGeneric_of_not_mem h

/-! ### The normalised RT invariant and its limit at the Kashaev point -/

open Classical in
/-- `[N]⁻¹ J(p)` at `σ` (`q = σ²`, `N = m + 1`): the writhe-normalised quantum trace of the braid
`p`, divided by `[N]`, the value on the one-strand unknot. Defined as `0` where the construction
is not available. -/
noncomputable def braidJonesRT (m : ℕ) (p : Tot BraidGroupN) (σ : ℂ) : ℂ :=
  if h : BraidGeneric m σ then
    (qint (σ ^ 2) (m + 1))⁻¹ * normalise artinFraming (thetaU σ h.1 m)⁻¹ 1
      (qtrace σ h.1 m h.2.1 (hint_le σ m h.2.2)) p
  else 0

theorem braidJonesRT_eq_vdv {m : ℕ} {p : Tot BraidGroupN}
    (hp : MarkovEquiv artinTower ⟨2, whiteheadWord⟩ p) {σ : ℂ} (h : BraidGeneric m σ) :
    braidJonesRT m p σ = vdvWhiteheadLinkJones (σ ^ 2) (m + 1) := by
  rw [braidJonesRT, dif_pos h,
    vdvWhiteheadLinkJones_eq_jones_of_markovEquiv σ h.1 m h.2.1 h.2.2 hp]

/-- The Kashaev point in the braid variable: `σ₀ = e^{πi/(2N)}`, so `q = σ₀² = e^{πi/N}`. -/
noncomputable def kashaevSigma (N : ℕ) : ℂ := Complex.exp (((Real.pi / (2 * N) : ℝ) : ℂ) * I)

theorem kashaevSigma_sq {N : ℕ} (hN : 1 ≤ N) :
    kashaevSigma N ^ 2 = Complex.exp (((Real.pi / N : ℝ) : ℂ) * I) := by
  have hN' : (N : ℂ) ≠ 0 := by exact_mod_cast (by omega : N ≠ 0)
  rw [kashaevSigma, ← Complex.exp_nat_mul]
  congr 1
  push_cast
  field_simp

/-- **The normalised coloured Jones of the Whitehead braid at the Kashaev point.** For every braid
`p` Markov-equivalent to `β = σ₁⁻² σ₂ σ₁⁻¹ σ₂`, `[N]⁻¹ J(p)(σ) → whiteheadLinkKashaev N` as `σ`
tends to `e^{πi/(2N)}` through the points where the construction is defined. -/
theorem tendsto_braidJonesRT_whitehead {N : ℕ} (hN : 1 ≤ N) {p : Tot BraidGroupN}
    (hp : MarkovEquiv artinTower ⟨2, whiteheadWord⟩ p) :
    Tendsto (braidJonesRT (N - 1) p) (𝓝[≠] kashaevSigma N) (𝓝 (whiteheadLinkKashaev N)) := by
  have hm : N - 1 + 1 = N := by omega
  have hs0 : Complex.exp (((Real.pi / N : ℝ) : ℂ) * I) ≠ 0 := Complex.exp_ne_zero _
  have hvdv := tendsto_vdvWhiteheadLinkJones (N := N) hs0 fun i h1 h2 => kashaev_pow_ne_one h1 h2
  rw [vdvWhiteheadLinkJones_at_kashaev_point hN, ← kashaevSigma_sq hN] at hvdv
  have hsq : Tendsto (fun σ : ℂ => σ ^ 2) (𝓝 (kashaevSigma N)) (𝓝 (kashaevSigma N ^ 2)) :=
    (continuous_pow 2).tendsto _
  have hcomp := (hvdv.comp hsq).mono_left (nhdsWithin_le_nhds (s := {kashaevSigma N}ᶜ))
  refine hcomp.congr' ?_
  filter_upwards [eventually_braidGeneric (N - 1) (kashaevSigma N)] with σ hσ
  rw [Function.comp_apply, braidJonesRT_eq_vdv hp hσ, hm]

/-- **The volume conjecture for the coloured Jones of the Whitehead braid closure.** For every
braid `p` Markov-equivalent to the Whitehead braid, the normalised invariant `[N]⁻¹ J_N(p)` has
a limit `K N` at the Kashaev point, and `(2π/N) log ‖K N‖ → Vol(W) = Vol(Borromean)/2`. -/
theorem whiteheadBraid_volume_conjecture {p : Tot BraidGroupN}
    (hp : MarkovEquiv artinTower ⟨2, whiteheadWord⟩ p) :
    ∃ K : ℕ → ℂ,
      (∀ N, 1 ≤ N →
        Tendsto (braidJonesRT (N - 1) p) (𝓝[≠] kashaevSigma N) (𝓝 (K N))) ∧
      Tendsto (fun N : ℕ => (2 * Real.pi / N) * Real.log ‖K N‖) atTop
        (𝓝 (QOU.Archimedean.Vol_Borromean / 2)) :=
  ⟨whiteheadLinkKashaev, fun _ hN => tendsto_braidJonesRT_whitehead hN hp,
    whiteheadLink_volume_conjecture⟩

/-- The punctured neighbourhood is non-trivial, so the limit is not vacuous. -/
example (N : ℕ) : (𝓝[≠] kashaevSigma N).NeBot := NormedField.nhdsNE_neBot _

end QOU.Knot.FigureEightVolume
