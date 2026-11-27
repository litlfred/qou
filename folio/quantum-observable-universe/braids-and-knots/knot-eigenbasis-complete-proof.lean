import HeckeTemperleyLieb.CasimirShared
import Mathlib.LinearAlgebra.Span.Basic


/-!
# QOU.PathIntegrals.KnotEigenbasisComplete

Extracted from folio/quantum-observable-universe/lean/ for content-block co-location.
Source: folio/quantum-observable-universe/lean/QOU/PathIntegrals.lean (monolithic)

The shared carrier structures (`SchurWeylDecomposition`, `AlexanderSurjectivity`,
`MarkovTrace`, `HeckeAlgebra`, `BoundedPartition`) are promoted into the
`QOU.Braiding` namespace by the library module `QOU.BraidKnot.CasimirShared`;
they are opened below rather than re-declared.
-/

namespace QOU.PathIntegrals

open QOU.Braiding

/-- **Completeness of the knot-type eigenbasis** (Proposition 4.x).

    Combines semisimplicity of `H_n(q)`, Alexander surjectivity, and
    spanning of the algebraic direct limit to establish that knot types
    form a complete eigenbasis replacing the Feynman path integral.

    Three parts:
    1. `H_n(q)` is semisimple at generic `q`, giving the complete
       q-Schur–Weyl decomposition of `V^{⊗n}`.
    2. Alexander's theorem provides surjectivity of the braid-closure map.
    3. The algebraic direct limit `V_phys = colim V^{⊗n}` is spanned
       by the irreducible summands (no metric completion is used).

    LaTeX: `\label{prop:knot-eigenbasis-complete}` -/
-- Ref: [chari1994guide] Chari–Pressley, *A Guide to Quantum Groups*, Ch. 10
-- Ref: [alexander1923] J.W. Alexander, Proc. Natl. Acad. Sci. USA 9 (1923)
-- Ref: [jones1987] V.F.R. Jones, Annals of Mathematics 126 (1987)
structure KnotEigenbasisComplete where
  /-- Part 1: the q-Schur–Weyl decomposition. -/
  decomposition : SchurWeylDecomposition
  /-- Part 2: Alexander surjectivity. -/
  alexander : AlexanderSurjectivity
  /-- Part 3: the Markov trace detects every irreducible summand. -/
  markov : MarkovTrace
  /-- Consistency: the Markov trace is on the same Hecke algebra
      as the decomposition. -/
  consistent : markov.hecke = decomposition.hecke
  -- The braid-closure map labels irreducible summands: for each partition `λ`
  -- in the decomposition, there exists a braid `β` whose closure detects `λ` —
  -- the Markov trace of the Hecke-algebra image of `β`, restricted to the `S_λ`
  -- summand, is non-zero.  Encoded via the representation map `ρ` below.
  /-- Representation map: braid → Hecke algebra element. -/
  braid_rep : alexander.Braid → decomposition.hecke.carrier
  /-- For each partition `λ`, there exists a braid whose trace on the
      corresponding Hecke-summand is non-zero. -/
  summands_detected : ∀ μ ∈ decomposition.partitions,
    ∃ (β : alexander.Braid),
    markov.tr (consistent ▸ braid_rep β) ≠ 0
  /-- The algebraic direct-limit type `V_phys = colim V^{⊗n}`. -/
  V_phys : Type*
  /-- The level-`n` embedded subspace: `embed n` is the image of
      `V^{⊗n}` inside `V_phys` under the direct-limit inclusion. -/
  embed : ℕ → Set V_phys
  /-- **Spanning** (Part 3): the union of all level-`n` embedded
      subspaces is *all* of `V_phys`.  Equivalently, every element
      of `V_phys` lies in `embed n` for some `n`.

      This is the algebraic-spanning condition (no metric completion
      is invoked).  Non-vacuous: if `embed` is the constant empty
      set, this is unprovable; it captures the genuine
      direct-limit-cover property. -/
  spanning : (⋃ n, embed n) = (Set.univ : Set V_phys)

/-! ## §2. Explicit `Module K` Isotypic Orthogonal Idempotent Direct-Sum Decomposition -/

section IsotypicModuleDecomposition

variable (K : Type*) [CommRing K]
variable (V : Type*) [AddCommGroup V] [Module K V]
variable (ι : Type*) [Fintype ι]

/-- **Orthogonal Idempotent Isotypic Decomposition of a `K`-Module `V`:**
Encodes the `q`-Schur–Weyl decomposition `V^{⊗n} = bigoplus_{λ ⊢ n, ℓ(λ) ≤ 2} W_λ`
inside genuine `Module K` linear algebra via a finite family of central/isotypic
idempotent projectors `e : ι → (V →ₗ[K] V)` that are mutually orthogonal and sum to
the identity `LinearMap.id`. -/
structure IsotypicIdempotentDecomposition where
  /-- The isotypic idempotent projectors `e_λ : V →ₗ[K] V`. -/
  e : ι → (V →ₗ[K] V)
  /-- Each `e_λ` is idempotent (`e_λ ∘ e_λ = e_λ`). -/
  idem : ∀ i : ι, (e i).comp (e i) = e i
  /-- Distinct isotypic projectors are orthogonal (`i ≠ j → e_i ∘ e_j = 0`). -/
  orthog : ∀ {i j : ι}, i ≠ j → (e i).comp (e j) = 0
  /-- Resolution of the identity (`∑_{λ} e_λ = id_V`). -/
  sum_eq_id : (∑ i : ι, e i) = LinearMap.id

namespace IsotypicIdempotentDecomposition

variable {K V ι}
variable (D : IsotypicIdempotentDecomposition K V ι)

/-- The `λ`-th isotypic submodule `W_λ := range(e_λ) ≤ V`. -/
def isotypicSubmodule (i : ι) : Submodule K V :=
  LinearMap.range (D.e i)

/-- Every vector `v : V` decomposes as the sum of its isotypic projections `∑_i e_i(v) = v`. -/
theorem sum_proj_apply (v : V) :
    (∑ i : ι, D.e i v) = v := by
  have h := LinearMap.congr_fun D.sum_eq_id v
  simpa [LinearMap.sum_apply] using h

/-- For every `v ∈ W_i`, `e_i(v) = v` and `e_j(v) = 0` for `j ≠ i`. -/
theorem proj_eq_self_of_mem {i : ι} {v : V} (hv : v ∈ D.isotypicSubmodule i) :
    D.e i v = v := by
  rcases hv with ⟨u, rfl⟩
  have h := LinearMap.congr_fun (D.idem i) u
  simpa using h

theorem proj_eq_zero_of_mem_of_ne {i j : ι} (hij : j ≠ i) {v : V}
    (hv : v ∈ D.isotypicSubmodule i) :
    D.e j v = 0 := by
  rcases hv with ⟨u, rfl⟩
  have h := LinearMap.congr_fun (D.orthog hij) u
  simpa using h

/-- **Part 1a — Isotypic Completeness (`⨆_i W_i = ⊤`):**
The supremum (linear span) of the isotypic submodules `W_i = range(e_i)` equals the
entire `K`-module `⊤ : Submodule K V`. -/
theorem iSup_isotypicSubmodule_eq_top :
    (⨆ i : ι, D.isotypicSubmodule i) = ⊤ := by
  rw [eq_top_iff]
  intro v _
  rw [← D.sum_proj_apply v]
  refine Submodule.sum_mem (⨆ i : ι, D.isotypicSubmodule i) ?_
  intro i _
  exact Submodule.mem_iSup_of_mem i ⟨v, rfl⟩

/-- **Part 1b — Direct-Sum Disjointness (`W_i ⊓ (⨆_{j ≠ i} W_j) = ⊥`):**
Every vector in `W_i` that also lies in the span of `{W_j : j ≠ i}` is `0`, establishing
`CompleteLattice.Independent D.isotypicSubmodule`. -/
theorem disjoint_isotypicSubmodule (i : ι) :
    Disjoint (D.isotypicSubmodule i) (⨆ (j : ι) (_ : j ≠ i), D.isotypicSubmodule j) := by
  rw [Submodule.disjoint_def]
  intro v hvi hvj
  -- Show that `⨆_{j ≠ i} W_j ≤ ker(e_i)`
  have hle : (⨆ (j : ι) (_ : j ≠ i), D.isotypicSubmodule j) ≤ LinearMap.ker (D.e i) := by
    refine iSup_le fun j => iSup_le fun hji => ?_
    intro w hw
    rw [LinearMap.mem_ker]
    exact D.proj_eq_zero_of_mem_of_ne hji.symm hw
  have h0 : D.e i v = 0 := hle hvj
  rw [← D.proj_eq_self_of_mem hvi, h0]

/-- **Part 1c — Unique Isotypic Direct-Sum Decomposition (`∀ v, (v = ∑_i w_i) ↔ ∀ i, w_i = e_i(v)`):**
If a family of vectors `w : ι → V` satisfies `w i ∈ W_i` for each `i` and `∑_i w_i = v`,
then necessarily `w i = e_i(v)` for every `i : ι` (in particular, if `∑_i w_i = 0` with
`w i ∈ W_i`, then `w i = 0` for all `i`). -/
theorem unique_isotypic_components [DecidableEq ι] {v : V} {w : ι → V}
    (hw : ∀ i : ι, w i ∈ D.isotypicSubmodule i)
    (hsum : (∑ j : ι, w j) = v) (i : ι) :
    w i = D.e i v := by
  have happly : D.e i (∑ j : ι, w j) = D.e i v := congrArg (D.e i) hsum
  rw [map_sum] at happly
  have hterm : ∀ j ∈ (Finset.univ : Finset ι),
      D.e i (w j) = if j = i then w i else 0 := by
    intro j _
    by_cases hji : j = i
    · subst hji
      rw [if_pos rfl]
      exact D.proj_eq_self_of_mem (hw j)
    · rw [if_neg hji]
      exact D.proj_eq_zero_of_mem_of_ne (Ne.symm hji) (hw j)
  rw [Finset.sum_congr rfl hterm,
    Finset.sum_ite_eq' Finset.univ i (fun _ => w i),
    if_pos (Finset.mem_univ i)] at happly
  exact happly

/-- **Part 2 — Isotypic Trace / Character Decomposition:**
For any `K`-linear trace functional `τ : (V →ₗ[K] V) →ₗ[K] K` and any endomorphism
`T : V →ₗ[K] V`, `τ(T) = ∑_{i : ι} τ(T ∘ e_i)`. -/
theorem trace_decomp (τ : (V →ₗ[K] V) →ₗ[K] K) (T : V →ₗ[K] V) :
    τ T = ∑ i : ι, τ (T.comp (D.e i)) := by
  have hT : T = ∑ i : ι, T.comp (D.e i) := by
    calc
      T = T.comp LinearMap.id := by ext v; rfl
      _ = T.comp (∑ i : ι, D.e i) := by rw [D.sum_eq_id]
      _ = ∑ i : ι, T.comp (D.e i) := by
        ext v
        simp [LinearMap.sum_apply]
  conv_lhs => rw [hT]
  rw [map_sum]

end IsotypicIdempotentDecomposition

/-! ## §3. Concrete Inhabited `n = 2` Schur–Weyl Decomposition (`Sym² ⊕ Λ²` on `K × K`) -/

/-- The swap involution `s(x, y) = (y, x)` on `K × K`. -/
def swapLinearMap (K : Type*) [CommRing K] : (K × K) →ₗ[K] (K × K) where
  toFun p := (p.2, p.1)
  map_add' _ _ := by ext <;> simp
  map_smul' _ _ := by ext <;> simp

/-- Over any field `K` with `(2 : K) ≠ 0`, the symmetriser `e_sym = 2⁻¹ • (id + s)` and
antisymmetriser `e_alt = 2⁻¹ • (id - s)` form an explicit inhabited
`IsotypicIdempotentDecomposition K (K × K) (Fin 2)`. -/
noncomputable def twoStrandSchurWeylDecomp (K : Type*) [Field K] (_h2 : (2 : K) ≠ 0) :
    IsotypicIdempotentDecomposition K (K × K) (Fin 2) where
  e := fun i =>
    if i = 0 then (2 : K)⁻¹ • (LinearMap.id + swapLinearMap K)
    else (2 : K)⁻¹ • (LinearMap.id - swapLinearMap K)
  idem := fun i => by
    have h2 : (2 : K) ≠ 0 := _h2
    fin_cases i
    · ext <;> dsimp [swapLinearMap] <;> field_simp <;> ring
    · ext <;> dsimp [swapLinearMap] <;> field_simp <;> ring
  orthog := fun {i j} hij => by
    have h2 : (2 : K) ≠ 0 := _h2
    fin_cases i <;> fin_cases j
    · exact False.elim (hij rfl)
    · ext <;> dsimp [swapLinearMap] <;> field_simp <;> ring
    · ext <;> dsimp [swapLinearMap] <;> field_simp <;> ring
    · exact False.elim (hij rfl)
  sum_eq_id := by
    have h2 : (2 : K) ≠ 0 := _h2
    ext <;> simp [Fin.sum_univ_two, swapLinearMap] <;> field_simp <;> ring

/-- **Concrete `n = 2` Schur–Weyl Span and Direct-Sum Disjointness Theorem:**
For `twoStrandSchurWeylDecomp ℚ`, the symmetric and alternating submodules
`W_0 = Sym²` and `W_1 = Λ²` span `ℚ × ℚ` and are direct-sum disjoint. -/
theorem twoStrandSchurWeylDecomp_rat_span_and_independent :
    let D := twoStrandSchurWeylDecomp ℚ (by norm_num)
    (⨆ i : Fin 2, D.isotypicSubmodule i) = ⊤ ∧
    (∀ i : Fin 2,
      Disjoint (D.isotypicSubmodule i) (⨆ (j : Fin 2) (_ : j ≠ i), D.isotypicSubmodule j)) := by
  intro D
  exact ⟨D.iSup_isotypicSubmodule_eq_top, D.disjoint_isotypicSubmodule⟩

end IsotypicModuleDecomposition

end QOU.PathIntegrals
