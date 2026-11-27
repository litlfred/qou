import QOU.EightfoldWay.FermiPairWedge

/-!
# QOU.EightfoldWay.HeckeSignChannelIsFermi — the Hecke sign channel is Fermi exchange

`FermiPairWedge` takes **Fermi exchange** `f j i = -f i j` on a strand pair as an input. This
module replaces that input by a statement about the braiding.

Two strands labelled by `Fin n` carry a pair state `f : Fin n → Fin n → K`, the coefficients
of `Σ f k l · e_k ⊗ e_l`. The standard (Jimbo) braiding `braid q` acts by
`e_i ⊗ e_i ↦ q e_i ⊗ e_i`, `e_i ⊗ e_j ↦ e_j ⊗ e_i` and
`e_j ⊗ e_i ↦ e_i ⊗ e_j + (q - q⁻¹) e_j ⊗ e_i` for `i < j`.

* `braid_hecke` — `braid q` satisfies the Hecke relation `σ² = (q - q⁻¹) σ + 1`, so its
  eigenvalues are `q` and `-q⁻¹` (AGENTS.md §7a: symmetric and antisymmetric channels).
* `sign_iff` — for `q² + 1 ≠ 0`, a pair state is in the `-q⁻¹` channel iff it vanishes on
  equal labels and `f l k = -q⁻¹ f k l` for `k < l`. Equal labels are excluded for every such
  `q`, not only at `q = 1` (a `q`-Pauli exclusion).
* `sym_iff` — the `q` channel is `f l k = q f k l` for `k < l`, with the diagonal free.
* `sign_ext` — a sign-channel state is fixed by its values on `k < l` (the `q`-wedges).
* `sign_one_iff_fermi` — at `q = 1`, on `Fin 5` over `ℚ`, the sign channel is exactly
  `FermiPairWedge.IsFermi`. So every Fermi-pair result there is a result about the
  `-q⁻¹` eigenspace of the braiding.

## What stays an input

That a matter strand pair lives in the `-q⁻¹` channel and not the `q` channel. The braiding
supplies the two channels and their content; it does not choose between them. Spin–statistics
is still not derived.

Base ring: a generic field `K` (§7c); the specialisation is over `ℚ`. No empirical input.
-/

namespace QOU.EightfoldWay.HeckeSignChannelIsFermi

variable {K : Type*} [Field K] {n : ℕ}

/-- The Jimbo braiding on pair coefficients: `(braid q f) k l` is the coefficient of
`e_k ⊗ e_l` in `σ (Σ f i j e_i ⊗ e_j)`. -/
def braid (q : K) (f : Fin n → Fin n → K) (k l : Fin n) : K :=
  if k = l then q * f k k
  else if k < l then f l k
  else f l k + (q - q⁻¹) * f k l

/-- Pair state in the `-q⁻¹` (sign) channel. -/
def IsSignState (q : K) (f : Fin n → Fin n → K) : Prop :=
  ∀ k l, braid q f k l = -q⁻¹ * f k l

/-- Pair state in the `q` (symmetric) channel. -/
def IsSymState (q : K) (f : Fin n → Fin n → K) : Prop :=
  ∀ k l, braid q f k l = q * f k l

/-- The braiding satisfies the Hecke relation `σ² = (q - q⁻¹) σ + 1`. -/
theorem braid_hecke {q : K} (hq : q ≠ 0) (f : Fin n → Fin n → K) (k l : Fin n) :
    braid q (braid q f) k l = (q - q⁻¹) * braid q f k l + f k l := by
  rcases lt_trichotomy k l with hkl | rfl | hkl
  · have h1 : k ≠ l := ne_of_lt hkl
    have h2 : l ≠ k := (ne_of_lt hkl).symm
    have h3 : ¬ l < k := not_lt.mpr hkl.le
    simp only [braid, h1, h2, h3, hkl, if_false, if_true]
    ring
  · simp only [braid, if_true]
    field_simp
    ring
  · have h1 : k ≠ l := (ne_of_lt hkl).symm
    have h2 : l ≠ k := ne_of_lt hkl
    have h3 : ¬ k < l := not_lt.mpr hkl.le
    simp only [braid, h1, h2, h3, hkl, if_false, if_true]
    ring

private theorem two_ne {q : K} (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) : q + q⁻¹ ≠ 0 := by
  intro h
  apply h2
  have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
  rw [← this, h, mul_zero]

/-- The sign channel: zero on equal labels, `f l k = -q⁻¹ f k l` above the diagonal. -/
theorem sign_iff {q : K} (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (f : Fin n → Fin n → K) :
    IsSignState q f ↔ (∀ k, f k k = 0) ∧ ∀ k l, k < l → f l k = -q⁻¹ * f k l := by
  constructor
  · intro h
    refine ⟨fun k => ?_, fun k l hkl => ?_⟩
    · have hk := h k k
      simp only [braid, if_true] at hk
      have : (q + q⁻¹) * f k k = 0 := by linear_combination hk
      exact (mul_eq_zero.mp this).resolve_left (two_ne hq h2)
    · have hk := h k l
      simp only [braid, ne_of_lt hkl, hkl, if_false, if_true] at hk
      exact hk
  · rintro ⟨hd, ho⟩ k l
    rcases lt_trichotomy k l with hkl | rfl | hkl
    · simp only [braid, ne_of_lt hkl, hkl, if_false, if_true]
      exact ho k l hkl
    · simp only [braid, if_true, hd k, mul_zero]
    · have h1 : k ≠ l := (ne_of_lt hkl).symm
      have h3 : ¬ k < l := not_lt.mpr hkl.le
      simp only [braid, h1, h3, if_false]
      rw [ho l k hkl]
      field_simp
      ring

/-- The symmetric channel: `f l k = q f k l` above the diagonal, diagonal free. -/
theorem sym_iff {q : K} (hq : q ≠ 0) (f : Fin n → Fin n → K) :
    IsSymState q f ↔ ∀ k l, k < l → f l k = q * f k l := by
  constructor
  · intro h k l hkl
    have hk := h k l
    simp only [braid, ne_of_lt hkl, hkl, if_false, if_true] at hk
    exact hk
  · intro ho k l
    rcases lt_trichotomy k l with hkl | rfl | hkl
    · simp only [braid, ne_of_lt hkl, hkl, if_false, if_true]
      exact ho k l hkl
    · simp only [braid, if_true]
    · have h1 : k ≠ l := (ne_of_lt hkl).symm
      have h3 : ¬ k < l := not_lt.mpr hkl.le
      simp only [braid, h1, h3, if_false]
      rw [ho l k hkl]
      field_simp
      ring

/-- Every diagonal state `e_i ⊗ e_i` lies in the symmetric channel, for every `q`. -/
theorem diag_isSym (q : K) (i : Fin n) :
    IsSymState q (fun k l => if k = i ∧ l = i then (1 : K) else 0) := by
  intro k l
  rcases lt_trichotomy k l with hkl | rfl | hkl
  · have h1 : k ≠ l := ne_of_lt hkl
    simp only [braid, h1, hkl, if_false, if_true]
    by_cases hk : k = i
    · subst hk; simp [h1.symm]
    · simp [hk]
  · simp [braid]
  · have h1 : k ≠ l := (ne_of_lt hkl).symm
    have h3 : ¬ k < l := not_lt.mpr hkl.le
    simp only [braid, h1, h3, if_false]
    by_cases hk : k = i
    · subst hk; simp [h1.symm]
    · simp [hk]

/-- A sign-channel state is determined by its values on `k < l`. -/
theorem sign_ext {q : K} (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) {f g : Fin n → Fin n → K}
    (hf : IsSignState q f) (hg : IsSignState q g) (h : ∀ k l, k < l → f k l = g k l) :
    f = g := by
  obtain ⟨fd, fo⟩ := (sign_iff hq h2 f).mp hf
  obtain ⟨gd, go⟩ := (sign_iff hq h2 g).mp hg
  funext k l
  rcases lt_trichotomy k l with hkl | rfl | hkl
  · exact h k l hkl
  · rw [fd, gd]
  · rw [fo l k hkl, go l k hkl, h l k hkl]

/-- At `q = 1`, on `Fin 5` over `ℚ`, the Hecke sign channel is exactly Fermi exchange. -/
theorem sign_one_iff_fermi (f : Fin 5 → Fin 5 → ℚ) :
    IsSignState (1 : ℚ) f ↔ FermiPairWedge.IsFermi f := by
  rw [sign_iff one_ne_zero (by norm_num) f]
  constructor
  · rintro ⟨hd, ho⟩ i j
    rcases lt_trichotomy i j with hij | rfl | hij
    · rw [ho i j hij]; simp
    · rw [hd]; simp
    · rw [ho j i hij]; simp
  · intro hf
    refine ⟨FermiPairWedge.fermi_diag_zero hf, fun k l _ => ?_⟩
    rw [hf k l]; simp

/-- At `q = 1` the symmetric channel is `f j i = f i j`. -/
theorem sym_one_iff (f : Fin n → Fin n → ℚ) :
    IsSymState (1 : ℚ) f ↔ ∀ i j, f j i = f i j := by
  rw [sym_iff one_ne_zero f]
  constructor
  · intro ho i j
    rcases lt_trichotomy i j with hij | rfl | hij
    · rw [ho i j hij, one_mul]
    · rfl
    · rw [ho j i hij, one_mul]
  · intro hs k l _
    rw [hs k l, one_mul]

end QOU.EightfoldWay.HeckeSignChannelIsFermi
