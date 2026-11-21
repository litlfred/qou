import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.Algebra.Algebra.Operations
import Mathlib.Tactic

/-!
# QOU.MassCore.CellularDepth — the provable algebraic core of
`conj:two-filtration-bridge-general`

Standalone, Mathlib-only, sorry-free, no new axioms.

The old Lean (`QOU.AlgebraicSubstrate.TwoFiltrationBridgeGeneral.bridge_map_general`)
projected a class field equal to its own conclusion. This file proves what is
actually provable and carries every unproved input as a *named hypothesis*.

## §1 The partition-cellular depth filtration on a split semisimple centre

`Z` is a commutative `R`-algebra (the centre `Z(H_n(K,q))` in the split
semisimple case) and `e : ι → Z` a family of pairwise-orthogonal idempotents
(the central primitive idempotents `e_λ`, `ι` = partitions of `n`). For any
depth function `δ : ι → ℕ` (GB-depth = the `a`-function `aDepth`, owner ruling
2026-11-16; or the maximal hook length `maxHookDepth`),

    F δ k := span_R { e i | δ i ≤ k }.

Proved: `F` is monotone; `F j * F k ⊆ F (min j k)` (so each `F k` is closed
under multiplication by `F j`, and `F` is a multiplicative filtration);
`1 ∈ F k ↔ ∀ i, δ i ≤ k` (so `F` is **never** a unital algebra filtration
when `δ > 0` somewhere — it is a filtration by ideals, not a GB/PBW filtration).

## §2 The transposing automorphism `#`

If an `R`-algebra map `φ` permutes the `e i` by `τ` and `δ ∘ τ = δ`, then
`φ (F k) ⊆ F k`; in general `φ (F δ k) ⊆ F (δ ∘ τ) k` (`map_mem_F_comp`).
For `δ = maxHookDepth`, `δ ∘ transpose = δ` (`maxHookDepth_transpose`); for the
`a`-function, `a ∘ transpose = n` (`aDepth_transpose`), so `#` does NOT
preserve the `a`-filtration: it carries it to the `n`-filtration. `e i` is `φ`-fixed iff `τ i = i`, and `e i - e (τ i)`
is a `(-1)`-eigenvector.

The input `φ (e_λ) = e_{λ'}` for `φ = #` (`σ_i ↦ -σ_i⁻¹`) is the standard
twist `(S^λ)^# ≅ (S^{λ'})^⊛` [Mathas 1999, Ch. 3; Dipper–James 1986]; it is a
hypothesis here (`hφ`), checked exactly by the probe recorded on issue #8094
for `n ≤ 4` (and 5) at three rational `q`.

## §3 Combinatorics on Mathlib `YoungDiagram`

`maxHookDepth μ.transpose = maxHookDepth μ`, `aDepth μ.transpose = nStat μ`; the number-of-rows and number-of-columns
statistics are swapped by transposition (`rows_transpose`), so a rows
filtration is not `#`-stable.

## §4 The conditional transfer (`…_of_intertwines`)

Given a linear "period realisation" `Φ : Z → P`, an involution `ι'` on `P`
(orientation reversal), and the **unproved** matching hypothesis
`Φ ∘ φ = ι' ∘ Φ`, together with the **unproved** parity hypothesis that `ι'`
acts on the depth-`d` component by `(-1)^d`: for a self-conjugate cell every
odd-depth component of `Φ (e i)` vanishes; for a chiral pair the odd-depth
components are opposite, and an odd-depth component of `Φ (e i)` is nonzero
**iff** it differs from that of `Φ (e (τ i))`. The nonvanishing itself (the
"`d_II = 3`" / "`d_II = 2`" values) is **not** derivable and remains the
conjecture.
-/

namespace QOU.MassCore.CellularDepth

/-! ## §1 -/

section Filtration

variable {R Z ι : Type*} [CommRing R] [CommRing Z] [Algebra R Z]

/-- A family of pairwise-orthogonal idempotents. -/
structure OrthIdem (e : ι → Z) : Prop where
  idem : ∀ i, e i * e i = e i
  orth : ∀ i j, i ≠ j → e i * e j = 0

variable (R) in
/-- The cellular depth filtration `F δ k = span {e i | δ i ≤ k}`. -/
def F (e : ι → Z) (δ : ι → ℕ) (k : ℕ) : Submodule R Z :=
  Submodule.span R (e '' {i | δ i ≤ k})

variable {e : ι → Z} {δ : ι → ℕ}

theorem F_mono : Monotone (F R e δ) := fun _ _ hjk =>
  Submodule.span_mono (Set.image_mono fun _ hi => le_trans hi hjk)

theorem gen_mem_F {i : ι} {k : ℕ} (hi : δ i ≤ k) : e i ∈ F R e δ k :=
  Submodule.subset_span ⟨i, hi, rfl⟩

theorem gen_mul_gen_mem (he : OrthIdem e) {j k : ℕ} {a b : ι}
    (ha : δ a ≤ j) (hb : δ b ≤ k) : e a * e b ∈ F R e δ (min j k) := by
  by_cases hab : a = b
  · subst hab
    rw [he.idem]
    exact gen_mem_F (le_min ha hb)
  · rw [he.orth a b hab]
    exact Submodule.zero_mem _

/-- **Multiplicativity.** `F j * F k ⊆ F (min j k)`. -/
theorem mul_mem_F (he : OrthIdem e) {j k : ℕ} {x y : Z}
    (hx : x ∈ F R e δ j) (hy : y ∈ F R e δ k) : x * y ∈ F R e δ (min j k) := by
  have hxy : x * y ∈ F R e δ j * F R e δ k := Submodule.mul_mem_mul hx hy
  rw [F, F, Submodule.span_mul_span] at hxy
  refine (Submodule.span_le.mpr ?_) hxy
  rintro _ ⟨_, ⟨a, ha, rfl⟩, _, ⟨b, hb, rfl⟩, rfl⟩
  exact gen_mul_gen_mem he ha hb

/-- In particular `F` is a multiplicative filtration in the usual sense. -/
theorem mul_mem_F_add (he : OrthIdem e) {j k : ℕ} {x y : Z}
    (hx : x ∈ F R e δ j) (hy : y ∈ F R e δ k) : x * y ∈ F R e δ (j + k) :=
  F_mono (min_le_left j k |>.trans (Nat.le_add_right j k)) (mul_mem_F he hx hy)

/-- An idempotent of depth `> k` annihilates `F k`. -/
theorem gen_mul_eq_zero_of_lt (he : OrthIdem e) {i : ι} {k : ℕ} (hi : k < δ i)
    {x : Z} (hx : x ∈ F R e δ k) : e i * x = 0 := by
  induction hx using Submodule.span_induction with
  | mem y hy =>
      obtain ⟨j, hj, rfl⟩ := hy
      have hne : i ≠ j := by
        rintro rfl
        exact absurd (hj : δ i ≤ k) (not_le.mpr hi)
      exact he.orth i j hne
  | zero => exact mul_zero _
  | add y z _ _ hy hz => rw [mul_add, hy, hz, add_zero]
  | smul a y _ hy => rw [mul_smul_comm, hy, smul_zero]

/-- **The unit sits at the top.** With a complete family of nonzero
orthogonal idempotents, `1 ∈ F k` iff every depth is `≤ k`. -/
theorem one_mem_F_iff [Fintype ι] (he : OrthIdem e) (hsum : ∑ i, e i = 1)
    (hne : ∀ i, e i ≠ 0) (k : ℕ) : (1 : Z) ∈ F R e δ k ↔ ∀ i, δ i ≤ k := by
  constructor
  · intro h1 i
    by_contra hlt
    have := gen_mul_eq_zero_of_lt (R := R) he (not_le.mp hlt) h1
    rw [mul_one] at this
    exact hne i this
  · intro hall
    rw [← hsum]
    exact Submodule.sum_mem _ fun i _ => gen_mem_F (hall i)

/-- Corollary: if some depth is positive, `1 ∉ F 0`; the filtration is not a
unital algebra filtration. -/
theorem one_not_mem_F_zero [Fintype ι] (he : OrthIdem e) (hsum : ∑ i, e i = 1)
    (hne : ∀ i, e i ≠ 0) {i : ι} (hi : 0 < δ i) : (1 : Z) ∉ F R e δ 0 := by
  rw [one_mem_F_iff he hsum hne]
  intro h
  exact absurd (h i) (not_le.mpr hi)

end Filtration

/-! ## §2 -/

section Hash

variable {R Z ι : Type*} [CommRing R] [CommRing Z] [Algebra R Z]
variable {e : ι → Z} {δ : ι → ℕ}

/-- **`#` preserves the filtration** when it permutes the idempotents by a
depth-preserving `τ`. -/
theorem map_mem_F_of_perm (φ : Z →ₐ[R] Z) (τ : ι → ι)
    (hφ : ∀ i, φ (e i) = e (τ i)) (hδ : ∀ i, δ (τ i) = δ i) {k : ℕ} {x : Z}
    (hx : x ∈ F R e δ k) : φ x ∈ F R e δ k := by
  have hle : F R e δ k ≤ (F R e δ k).comap φ.toLinearMap := by
    refine Submodule.span_le.mpr ?_
    rintro _ ⟨i, hi, rfl⟩
    show φ (e i) ∈ F R e δ k
    rw [hφ]
    exact gen_mem_F (by rw [hδ]; exact hi)
  exact hle hx

/-- **`#` transports the filtration.** If `φ` permutes the idempotents by an
involution `τ`, then `φ (F δ k) ⊆ F (δ ∘ τ) k` for every depth `δ`. For the
`a`-function this is the statement that `#` carries the `a`-filtration to the
filtration by `a ∘ transpose = n` (`aDepth_transpose`). -/
theorem map_mem_F_comp (φ : Z →ₐ[R] Z) (τ : ι → ι) (hτ : ∀ i, τ (τ i) = i)
    (hφ : ∀ i, φ (e i) = e (τ i)) {k : ℕ} {x : Z}
    (hx : x ∈ F R e δ k) : φ x ∈ F R e (δ ∘ τ) k := by
  have hle : F R e δ k ≤ (F R e (δ ∘ τ) k).comap φ.toLinearMap := by
    refine Submodule.span_le.mpr ?_
    rintro _ ⟨i, hi, rfl⟩
    show φ (e i) ∈ F R e (δ ∘ τ) k
    rw [hφ]
    exact gen_mem_F (by simp only [Function.comp, hτ]; exact hi)
  exact hle hx

/-- **`#` transports the filtration, as an equality.** Under the hypotheses of
`map_mem_F_comp`, the image of `F δ k` is exactly `F (δ ∘ τ) k`: the reverse
inclusion holds because `e i = φ (e (τ i))`. -/
theorem map_F_eq (φ : Z →ₐ[R] Z) (τ : ι → ι) (hτ : ∀ i, τ (τ i) = i)
    (hφ : ∀ i, φ (e i) = e (τ i)) (k : ℕ) :
    (F R e δ k).map φ.toLinearMap = F R e (δ ∘ τ) k := by
  refine le_antisymm ?_ ?_
  · rw [Submodule.map_le_iff_le_comap]
    intro x hx
    exact map_mem_F_comp φ τ hτ hφ hx
  · refine Submodule.span_le.mpr ?_
    rintro _ ⟨i, hi, rfl⟩
    refine ⟨e (τ i), gen_mem_F (show δ (τ i) ≤ k from hi), ?_⟩
    show φ (e (τ i)) = e i
    rw [hφ, hτ]

/-- With nonzero orthogonal idempotents, a generator lies in `F k` exactly when
its depth is at most `k`: the filtration determines the depth function. -/
theorem gen_mem_F_iff (he : OrthIdem e) (hne : ∀ i, e i ≠ 0) {i : ι} {k : ℕ} :
    e i ∈ F R e δ k ↔ δ i ≤ k := by
  refine ⟨fun h => ?_, gen_mem_F⟩
  by_contra hlt
  have := gen_mul_eq_zero_of_lt (R := R) he (not_le.mp hlt) h
  rw [he.idem] at this
  exact hne i this

/-- **`#`-stability criterion.** For a `φ` permuting nonzero orthogonal
idempotents by an involution `τ`, the filtration is `φ`-stable at every level
if and only if the depth is `τ`-invariant. -/
theorem map_F_stable_iff (he : OrthIdem e) (hne : ∀ i, e i ≠ 0)
    (φ : Z →ₐ[R] Z) (τ : ι → ι) (hτ : ∀ i, τ (τ i) = i)
    (hφ : ∀ i, φ (e i) = e (τ i)) :
    (∀ k, (F R e δ k).map φ.toLinearMap = F R e δ k) ↔ ∀ i, δ (τ i) = δ i := by
  constructor
  · intro h i
    have h1 : e i ∈ F R e δ (δ (τ i)) := by
      rw [← h, map_F_eq φ τ hτ hφ]
      exact gen_mem_F (show δ (τ i) ≤ δ (τ i) from le_refl _)
    have h2 : e (τ i) ∈ F R e δ (δ i) := by
      rw [← h, map_F_eq φ τ hτ hφ]
      exact gen_mem_F (show δ (τ (τ i)) ≤ δ i by rw [hτ])
    exact le_antisymm ((gen_mem_F_iff he hne).mp h2) ((gen_mem_F_iff he hne).mp h1)
  · intro h k
    rw [map_F_eq φ τ hτ hφ]
    have : δ ∘ τ = δ := funext h
    rw [this]

/-- Orthogonal nonzero idempotents are pairwise distinct. -/
theorem OrthIdem.injective (he : OrthIdem e) (hne : ∀ i, e i ≠ 0) :
    Function.Injective e := by
  intro i j hij
  by_contra h
  apply hne i
  rw [← he.idem i]
  nth_rewrite 2 [hij]
  exact he.orth i j h

/-- `e i` is `φ`-fixed iff its cell is self-conjugate. -/
theorem map_gen_eq_self_iff (he : OrthIdem e) (hne : ∀ i, e i ≠ 0)
    (φ : Z →ₐ[R] Z) (τ : ι → ι) (hφ : ∀ i, φ (e i) = e (τ i)) (i : ι) :
    φ (e i) = e i ↔ τ i = i := by
  rw [hφ]
  exact (he.injective hne).eq_iff

/-- For a chiral pair, `e i - e (τ i)` is a `(-1)`-eigenvector of `φ`. -/
theorem map_gen_sub (φ : Z →ₐ[R] Z) (τ : ι → ι) (hτ : ∀ i, τ (τ i) = i)
    (hφ : ∀ i, φ (e i) = e (τ i)) (i : ι) :
    φ (e i - e (τ i)) = -(e i - e (τ i)) := by
  rw [map_sub, hφ, hφ, hτ]; abel

/-- …and `e i + e (τ i)` is a `(+1)`-eigenvector. -/
theorem map_gen_add (φ : Z →ₐ[R] Z) (τ : ι → ι) (hτ : ∀ i, τ (τ i) = i)
    (hφ : ∀ i, φ (e i) = e (τ i)) (i : ι) :
    φ (e i + e (τ i)) = e i + e (τ i) := by
  rw [map_add, hφ, hφ, hτ, add_comm]

end Hash

/-! ## §3 -/

section Young

open YoungDiagram

/-- Hook length of cell `c = (i, j)` (same definition as the corpus's
`TwoFiltrationBridge.hookLength`). -/
def hookLength (μ : YoungDiagram) (c : ℕ × ℕ) : ℕ :=
  (μ.rowLen c.1 - c.2) + (μ.colLen c.2 - c.1) - 1

/-- Maximal hook length. This is the statistic the corpus formerly called
"GB-depth" (`gbDepth`); since the owner ruling of 2026-11-16 GB-depth is
Lusztig's `a`-function (`aDepth` below), so this one is renamed. -/
def maxHookDepth (μ : YoungDiagram) : ℕ :=
  μ.cells.sup fun c => hookLength μ c

theorem hookLength_transpose (μ : YoungDiagram) (c : ℕ × ℕ) :
    hookLength μ.transpose c.swap = hookLength μ c := by
  simp only [hookLength, Prod.fst_swap, Prod.snd_swap, rowLen_transpose,
    colLen_transpose]
  rw [Nat.add_comm (μ.colLen c.2 - c.1)]

/-- **Max-hook depth is transpose-invariant.** -/
theorem maxHookDepth_transpose (μ : YoungDiagram) :
    maxHookDepth μ.transpose = maxHookDepth μ := by
  have hcells : μ.transpose.cells = μ.cells.map (Equiv.prodComm ℕ ℕ).toEmbedding := rfl
  unfold maxHookDepth
  rw [hcells, Finset.sup_map]
  congr 1
  funext c
  exact hookLength_transpose μ c

/-- **Cell depth (GB-depth, owner ruling 2026-11-16): Lusztig's `a`-function**
of the two-sided Kazhdan–Lusztig cell of shape `μ`, in the labelling where the
one-row shape `(n)` is the index representation: `a(μ) = Σ_i C(μ_i, 2)`.
Written as a sum over cells: the cell `(i, j)` contributes its column index
`j`, because row `i` contributes `0 + 1 + ⋯ + (μ_i - 1) = C(μ_i, 2)`.
The identification with the `a`-function is cited (Lusztig; Kazhdan–Lusztig
1979) and checked exactly for `n ≤ 5`; here `aDepth` is the combinatorial
statistic. -/
def aDepth (μ : YoungDiagram) : ℕ :=
  ∑ c ∈ μ.cells, c.2

/-- The statistic `n(μ) = Σ_i (i-1) μ_i`, written as a sum over cells of the
row index. -/
def nStat (μ : YoungDiagram) : ℕ :=
  ∑ c ∈ μ.cells, c.1

/-- **Transposition exchanges `a` and `n`:** `a(μ') = n(μ)`. So `#`, which
sends `e_μ` to `e_{μ'}`, sends the `a`-depth to the `n`-statistic. -/
theorem aDepth_transpose (μ : YoungDiagram) : aDepth μ.transpose = nStat μ := by
  have hcells : μ.transpose.cells = μ.cells.map (Equiv.prodComm ℕ ℕ).toEmbedding := rfl
  unfold aDepth nStat
  rw [hcells, Finset.sum_map]
  rfl

/-- The `#`-symmetrised depth `a(μ) + a(μ')` is transpose-invariant. -/
theorem aDepth_add_transpose (μ : YoungDiagram) :
    aDepth μ.transpose + aDepth μ.transpose.transpose = aDepth μ + aDepth μ.transpose := by
  rw [YoungDiagram.transpose_transpose, Nat.add_comm]

/-- Number of rows. -/
def rows (μ : YoungDiagram) : ℕ := μ.colLen 0

/-- Transposition swaps the number of rows and the length of the first row,
so a "number of rows" filtration is not `#`-stable. -/
theorem rows_transpose (μ : YoungDiagram) : rows μ.transpose = μ.rowLen 0 :=
  colLen_transpose μ 0

end Young

/-! ## §4 -/

section Transfer

variable {R Z ι P : Type*} [CommRing R] [CommRing Z] [Algebra R Z]
  [AddCommGroup P] [Module R P]
variable {e : ι → Z}

/-- Self-conjugate cell ⇒ its realisation is orientation-even —
conditional on the matching hypothesis `hmatch`. -/
theorem realisation_even_of_intertwines (φ : Z →ₐ[R] Z) (τ : ι → ι)
    (hφ : ∀ i, φ (e i) = e (τ i)) (ι' : P →ₗ[R] P) (Φ : Z →ₗ[R] P)
    (hmatch : ∀ x, Φ (φ x) = ι' (Φ x)) {i : ι} (hi : τ i = i) :
    ι' (Φ (e i)) = Φ (e i) := by
  rw [← hmatch, hφ, hi]

/-- Chiral pair ⇒ orientation reversal swaps the two realisations. -/
theorem realisation_swap_of_intertwines (φ : Z →ₐ[R] Z) (τ : ι → ι)
    (hφ : ∀ i, φ (e i) = e (τ i)) (ι' : P →ₗ[R] P) (Φ : Z →ₗ[R] P)
    (hmatch : ∀ x, Φ (φ x) = ι' (Φ x)) (i : ι) :
    ι' (Φ (e i)) = Φ (e (τ i)) := by
  rw [← hmatch, hφ]

/-- **Odd-depth vanishing for self-conjugate cells**, conditional on the
matching hypothesis `hmatch` and the parity hypothesis `hpar` (orientation
reversal acts on the depth-`d` component by `(-1)^d`), with no 2-torsion. -/
theorem odd_component_eq_zero_of_intertwines_of_parity
    (φ : Z →ₐ[R] Z) (τ : ι → ι) (hφ : ∀ i, φ (e i) = e (τ i))
    (ι' : P →ₗ[R] P) (Φ : Z →ₗ[R] P) (hmatch : ∀ x, Φ (φ x) = ι' (Φ x))
    (π : P →ₗ[R] P) (d : ℕ) (hd : Odd d)
    (hpar : ∀ p, π (ι' p) = ((-1 : R) ^ d) • π p)
    (htwo : ∀ p : P, p + p = 0 → p = 0) {i : ι} (hi : τ i = i) :
    π (Φ (e i)) = 0 := by
  have h1 := realisation_even_of_intertwines φ τ hφ ι' Φ hmatch hi
  have h2 : π (Φ (e i)) = -π (Φ (e i)) := by
    conv_lhs => rw [← h1]
    rw [hpar, hd.neg_one_pow, neg_one_smul]
  apply htwo
  nth_rewrite 1 [h2]
  exact neg_add_cancel _

/-- For a chiral pair, the depth-`d` components are related by `(-1)^d`. -/
theorem component_swap_of_intertwines_of_parity
    (φ : Z →ₐ[R] Z) (τ : ι → ι) (hφ : ∀ i, φ (e i) = e (τ i))
    (ι' : P →ₗ[R] P) (Φ : Z →ₗ[R] P) (hmatch : ∀ x, Φ (φ x) = ι' (Φ x))
    (π : P →ₗ[R] P) (d : ℕ) (hpar : ∀ p, π (ι' p) = ((-1 : R) ^ d) • π p)
    (i : ι) : π (Φ (e (τ i))) = ((-1 : R) ^ d) • π (Φ (e i)) := by
  rw [← realisation_swap_of_intertwines φ τ hφ ι' Φ hmatch i, hpar]

/-- **What "`d_II = 3` on a chiral pair" reduces to.** For odd `d`, the
depth-`d` component of `Φ (e i)` is nonzero iff it differs from that of
`Φ (e (τ i))`. The right-hand side is a non-degeneracy condition that no
hypothesis here supplies: it is the residual conjecture. -/
theorem odd_component_ne_zero_iff_of_intertwines_of_parity
    (φ : Z →ₐ[R] Z) (τ : ι → ι) (hφ : ∀ i, φ (e i) = e (τ i))
    (ι' : P →ₗ[R] P) (Φ : Z →ₗ[R] P) (hmatch : ∀ x, Φ (φ x) = ι' (Φ x))
    (π : P →ₗ[R] P) (d : ℕ) (hd : Odd d)
    (hpar : ∀ p, π (ι' p) = ((-1 : R) ^ d) • π p)
    (htwo : ∀ p : P, p + p = 0 → p = 0) (i : ι) :
    π (Φ (e i)) ≠ 0 ↔ π (Φ (e i)) ≠ π (Φ (e (τ i))) := by
  have hs := component_swap_of_intertwines_of_parity φ τ hφ ι' Φ hmatch π d hpar i
  rw [hd.neg_one_pow, neg_one_smul] at hs
  rw [hs]
  constructor
  · intro h heq
    apply h
    apply htwo
    nth_rewrite 2 [heq]
    exact add_neg_cancel _
  · intro h h0
    apply h
    rw [h0, neg_zero]

end Transfer

end QOU.MassCore.CellularDepth

