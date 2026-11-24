import Mathlib.Tactic

/-!
# QOU.TopologicalMass.cat_transient_localises_blowup

**Lemma** ([`lem:topological-mass-cat-transient`](../../../quantum-observable-universe/mass-endomorphism/topological-mass-cat-transient.md)).

*The transient component `α − τ̂ₙ(α) ∈ 𝓐_{n+1}^{trans}` has support
contained in the union of the kernels of `𝔡_{n+1}` at the blow-up
centres `p₁, …, p_N`, and the transient trace decomposes as a sum of
disjoint local contributions:*

    tr(α − τ̂ₙ(α)) = Σ_{i=1}^{N} tr_trans(ϱ, p_i).

## Structure (hypothesis vs. derivation)

Everything is a **parameter**; nothing is a named constant.

* The observation algebra `𝓐_{n+1}` is an arbitrary `R`-module `A` over a
  generic commutative ring `R` (§7c: the statement is linear algebra, so
  no archimedean structure is needed).  The descent projector `τ̂ₙ` is an
  arbitrary map `A → A`, the Frobenius trace an arbitrary `R`-linear
  functional `A →ₗ[R] R`, and the jet differential at the `i`-th centre
  an arbitrary `R`-linear map `𝔡ᵢ : A →ₗ[R] B`.
* **Hypothesis (the .md's first clause, the open geometric input).**
  `hsupp`: the transient component lies in the span of the local kernels,
  `α − τ̂ₙ(α) ∈ ⨆_{i<N} ker 𝔡ᵢ`.  This is the jet-filtration support
  statement, which is *not* derived here; it is carried as an explicit
  hypothesis of the theorem rather than as a class field projected back.
* **Hypothesis (disjointness).** `hindep`: the local kernels are
  independent (`iSupIndep`), the formal content of the proof block's
  "mutually disjoint submodules".
* **Derived.**  From `hsupp` the transient component splits into local
  pieces `cᵢ ∈ ker 𝔡ᵢ` (`Submodule.mem_iSup_finset_iff_exists_sum`), the
  linear trace distributes over the split (`map_sum`), and under `hindep`
  the local pieces — hence the local traces `tr_trans(ϱ, pᵢ) := tr(cᵢ)` —
  are **unique**, so `tr_trans(ϱ, pᵢ)` is well defined
  (`localPiece_unique`).

The conclusion is not assumed anywhere: no hypothesis mentions the trace.

An earlier revision modelled every input as a named `opaque` real and
carried the decomposition itself as a `Prop`-class field projected back
by `transient_decomposition` (a self-assuming projection); an earlier
one still defined the inputs as `0` / the identity.  Bean `tmvac`.
-/

namespace QOU.TopologicalMass

namespace CatTransient

variable {R A B : Type*} [CommRing R] [AddCommGroup A] [Module R A]
  [AddCommGroup B] [Module R B]

/-- The local kernel `ker 𝔡_{n+1}|_{pᵢ}` at the `i`-th blow-up centre. -/
def localKer (d : ℕ → A →ₗ[R] B) (i : ℕ) : Submodule R A := LinearMap.ker (d i)

/-- **Existence of the local split.**  If the transient component lies in
the span of the local kernels at the first `N` centres, it is a sum of
pieces `cᵢ ∈ ker 𝔡ᵢ`. -/
theorem exists_localPieces (d : ℕ → A →ₗ[R] B) (N : ℕ) (x : A)
    (hsupp : x ∈ ⨆ i ∈ Finset.range N, localKer d i) :
    ∃ c : ℕ → A, (∀ i, c i ∈ localKer d i) ∧
      ∑ i ∈ Finset.range N, c i = x := by
  obtain ⟨μ, hμ⟩ := (Submodule.mem_iSup_finset_iff_exists_sum _ x).1 hsupp
  exact ⟨fun i => (μ i : A), fun i => (μ i).2, hμ⟩

/-- **Uniqueness of the local split under disjointness.**  If the local
kernels are independent, two splits of the same element over the first
`N` centres agree piece by piece. -/
theorem localPiece_unique (d : ℕ → A →ₗ[R] B) (N : ℕ)
    (hindep : iSupIndep (localKer d))
    (c c' : ℕ → A) (hc : ∀ i, c i ∈ localKer d i) (hc' : ∀ i, c' i ∈ localKer d i)
    (hsum : ∑ i ∈ Finset.range N, c i = ∑ i ∈ Finset.range N, c' i) :
    ∀ i ∈ Finset.range N, c i = c' i := by
  intro i hi
  have hsplit : c i - c' i = ∑ j ∈ (Finset.range N).erase i, (c' j - c j) := by
    have h1 := Finset.add_sum_erase (Finset.range N) c hi
    have h2 := Finset.add_sum_erase (Finset.range N) c' hi
    rw [Finset.sum_sub_distrib]
    have : c i + ∑ j ∈ (Finset.range N).erase i, c j
        = c' i + ∑ j ∈ (Finset.range N).erase i, c' j := by rw [h1, h2, hsum]
    linear_combination (norm := abel_nf) this
  have hmemI : c i - c' i ∈ localKer d i := Submodule.sub_mem _ (hc i) (hc' i)
  have hmemO : c i - c' i ∈ ⨆ (j : ℕ) (_ : j ≠ i), localKer d j := by
    rw [hsplit]
    refine Submodule.sum_mem _ fun j hj => ?_
    have hji : j ≠ i := Finset.ne_of_mem_erase hj
    have hmem : c' j - c j ∈ localKer d j := Submodule.sub_mem _ (hc' j) (hc j)
    exact (le_iSup₂_of_le j hji le_rfl :
      localKer d j ≤ ⨆ (j : ℕ) (_ : j ≠ i), localKer d j) hmem
  have h0 : c i - c' i = 0 :=
    (Submodule.disjoint_def.1 (hindep i)) _ hmemI hmemO
  exact sub_eq_zero.1 h0

end CatTransient

open CatTransient in
/-- **Transient trace localises to the blow-up centres**
    ([`lem:topological-mass-cat-transient`]).

Given the support hypothesis `hsupp` (the transient component
`α − τ̂ₙ(α)` lies in the span of the local kernels `ker 𝔡ᵢ`, `i < N`),
there are local pieces `cᵢ ∈ ker 𝔡ᵢ` such that
`tr(α − τ̂ₙ(α)) = Σ_{i<N} tr(cᵢ)`, i.e. the trace is a sum of local
contributions `tr_trans(ϱ, pᵢ) := tr(cᵢ)`.  *Derived*: split by the
support hypothesis, then distribute the linear trace (`map_sum`).  When
the kernels are disjoint (`hindep`), the pieces are unique
(`CatTransient.localPiece_unique`), so the local contributions are well
defined. -/
theorem cat_transient_localises_blowup
    {R A B : Type*} [CommRing R] [AddCommGroup A] [Module R A]
    [AddCommGroup B] [Module R B]
    (alpha : A) (tauHat : A → A) (trFrob : A →ₗ[R] R)
    (d : ℕ → A →ₗ[R] B) (N : ℕ)
    (hsupp : alpha - tauHat alpha ∈ ⨆ i ∈ Finset.range N, localKer d i) :
    ∃ c : ℕ → A, (∀ i, c i ∈ localKer d i) ∧
      ∑ i ∈ Finset.range N, c i = alpha - tauHat alpha ∧
      trFrob (alpha - tauHat alpha) = ∑ i ∈ Finset.range N, trFrob (c i) := by
  obtain ⟨c, hc, hsum⟩ := exists_localPieces d N _ hsupp
  refine ⟨c, hc, hsum, ?_⟩
  rw [← hsum, map_sum]

end QOU.TopologicalMass
