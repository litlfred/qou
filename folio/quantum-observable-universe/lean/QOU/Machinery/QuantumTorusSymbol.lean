import QOU.Machinery.QuantumTorus

/-!
# QOU.Machinery.QuantumTorusSymbol — principal symbol calculus (QDM-1 / QDM-2)

Bricks QDM-1 and QDM-2 of the q-D-module symbol-calculus epic (`qou-dap4`).
This is the **algebraic, verifiable-here** core, built directly on the existing
`QOU.Machinery.QuantumTorus` q-Weyl ring (NT-T2).  The deep geometric
application (QDM-3/QDM-4 — a characteristic-variety / holonomicity statement)
is out of scope: see `docs/audits/2026-07-20-qdm-symbol-calculus.md`.

## The order filtration and the principal symbol

The quantum torus `T = A[L^±; σ]` (`SkewMonoidAlgebra A (Multiplicative ℤ)`)
carries the **order filtration** by top `L`-degree `topDeg : T → WithBot ℤ`
(defined in `QuantumTorus.lean`).  The **principal symbol** of `P` is its
leading `L`-monomial:

  `symbol P = L^(leadDeg P) · leadCoeff P = monomial (leadDeg P) (leadCoeff P)`,

where `leadDeg P = (topDeg P).unbotD 0 ∈ ℤ` (junk `0` for `P = 0`, which is
harmless because `leadCoeff 0 = 0`) and `leadCoeff P = coeffAt P (leadDeg P)`.

## What is proved here (sorry-free)

* **QDM-1** — `symbol`, `leadDeg`, `leadCoeff` and their values on the
  generators: `symbol_monomial`, `symbol_emb`, `symbol_Lgen`, `topDeg_emb`,
  `topDeg_Lgen`, plus `leadCoeff_ne_zero` (a nonzero element has a nonzero
  leading coefficient).
* **QDM-2** — the *leading-coefficient product law*
  `coeffAt_mul_add : coeffAt (P·Q) (m+n) = coeffAt P m · (σᵐ (coeffAt Q n))`
  (proved over **any** `CommRing`, no domain hypothesis — the twist `σᵐ`
  survives here as the *graded structure constant*), the vanishing lemma
  `coeffAt_mul_eq_zero_of_lt`, and hence, **over a domain**,
  `topDeg_mul : topDeg (P·Q) = topDeg P + topDeg Q` and
  `symbol_mul : symbol (P·Q) = symbol P · symbol Q`.

## The associated graded — what commutes in `gr` vs the ambient twist

The quantum torus is *already* `ℤ`-graded by `L`-degree, so its associated
graded ring `gr T` for the order filtration is `T` itself.  The symbol map is
therefore multiplicative into `gr T = T` with the **twisted** product law
`L^m a · L^n b = L^{m+n}(a · σᵐ b)` (`monomial_mul_monomial`).  In particular
the classical-Weyl "symbols commute" phenomenon **does not hold here**: the
commutator `[L, M] = (σ − id)(M)·L = (q²−1) M L` has the *same* order as `ML`
(the q-Weyl twist is a same-order deformation, not a lower-order one), so the
principal symbol of a commutator is **not** forced to vanish.  What `symbol_mul`
records is the honest statement — the leading term of a product is the twisted
product of the leading terms — and the twist `σ^{leadDeg P}` is exactly the
graded structure constant that survives into `gr`.

## Base ring (§7c)

Generic `{A : Type*} [CommRing A] [MulSemiringAction Ldeg A]` throughout, plus
`[IsDomain A]` for the two multiplicativity results that genuinely need the
leading coefficient to stay nonzero.  No `ℝ`, no ordering, no archimedean
construct: the whole file is generic-ring algebra and `lean`-direct-verifies
against the package oleans.
-/

noncomputable section

namespace QOU.Machinery.QuantumTorus

open SkewMonoidAlgebra

variable {A : Type*} [CommRing A] [MulSemiringAction Ldeg A]

/-! ### QDM-1 — the principal symbol map -/

/-- **Leading `L`-degree** of `P` as an integer (`0` for `P = 0`, which is
    harmless: the leading coefficient there is `0` as well). -/
def leadDeg (P : QuantumTorus A) : ℤ := (topDeg P).unbotD 0

/-- **Leading coefficient** of `P`: its coefficient at the top `L`-degree. -/
def leadCoeff (P : QuantumTorus A) : A := coeffAt P (leadDeg P)

/-- **Principal symbol** of `P`: the leading `L`-monomial
    `L^(leadDeg P) · leadCoeff P`.  For the order filtration by top `L`-degree,
    this is the image of `P` in the associated graded ring. -/
def symbol (P : QuantumTorus A) : QuantumTorus A := monomial (leadDeg P) (leadCoeff P)

@[simp] theorem leadDeg_zero : leadDeg (0 : QuantumTorus A) = 0 := by
  rw [leadDeg, topDeg_zero]; rfl

@[simp] theorem leadCoeff_zero : leadCoeff (0 : QuantumTorus A) = 0 := by
  rw [leadCoeff, coeffAt]; simp

@[simp] theorem symbol_zero : symbol (0 : QuantumTorus A) = 0 := by
  rw [symbol, leadCoeff_zero, monomial]; simp

/-- If `topDeg P = m` (an integer, not `⊥`) then `leadDeg P = m`. -/
theorem leadDeg_of_topDeg {P : QuantumTorus A} {m : ℤ} (h : topDeg P = (m : ℤ)) :
    leadDeg P = m := by
  rw [leadDeg, h]; rfl

theorem leadDeg_monomial {n : ℤ} {a : A} (ha : a ≠ 0) : leadDeg (monomial n a) = n :=
  leadDeg_of_topDeg (topDeg_monomial n ha)

theorem leadCoeff_monomial {n : ℤ} {a : A} (ha : a ≠ 0) :
    leadCoeff (monomial n a) = a := by
  rw [leadCoeff, leadDeg_monomial ha, coeffAt_monomial]; simp

/-- **QDM-1 core:** the symbol of a monomial is itself. -/
theorem symbol_monomial {n : ℤ} {a : A} (ha : a ≠ 0) :
    symbol (monomial n a) = monomial n a := by
  rw [symbol, leadDeg_monomial ha, leadCoeff_monomial ha]

/-- The symbol of the order-`0` coefficient embedding `emb a` is itself. -/
theorem symbol_emb {a : A} (ha : a ≠ 0) : symbol (emb a) = emb a := by
  have h : (emb a : QuantumTorus A) = monomial 0 a := (monomial_zero_left a).symm
  rw [h, symbol_monomial ha]

/-- The symbol of `L` is `L` (order `1`). -/
theorem symbol_Lgen [Nontrivial A] : symbol (Lgen : QuantumTorus A) = Lgen := by
  rw [Lgen_eq_monomial]; exact symbol_monomial one_ne_zero

/-- `emb a` has order `0`. -/
theorem topDeg_emb {a : A} (ha : a ≠ 0) : topDeg (emb a) = (0 : ℤ) := by
  have h : (emb a : QuantumTorus A) = monomial 0 a := (monomial_zero_left a).symm
  rw [h]; exact_mod_cast topDeg_monomial 0 ha

/-- `L` has order `1`. -/
theorem topDeg_Lgen [Nontrivial A] : topDeg (Lgen : QuantumTorus A) = (1 : ℤ) := by
  rw [Lgen_eq_monomial]; exact topDeg_monomial 1 (one_ne_zero : (1 : A) ≠ 0)

/-! ### Nonzero elements have a nonzero leading coefficient (and `topDeg = leadDeg`) -/

theorem support_nonempty_of_ne_zero {P : QuantumTorus A} (hP : P ≠ 0) :
    (expSupport P).Nonempty := by
  rw [expSupport, Finset.image_nonempty, Finset.nonempty_iff_ne_empty]
  intro h
  exact hP (toFinsupp_eq_zero.mp (Finsupp.support_eq_empty.mp h))

/-- For a **nonzero** `P`, the order filtration degree is genuinely an integer,
    equal to `leadDeg P`. -/
theorem topDeg_eq_leadDeg {P : QuantumTorus A} (hP : P ≠ 0) :
    topDeg P = ((leadDeg P : ℤ) : WithBot ℤ) := by
  have hne := support_nonempty_of_ne_zero hP
  have hmax : topDeg P = ((expSupport P).max' hne : WithBot ℤ) := by
    rw [topDeg, ← Finset.coe_max' hne]
  have hld : leadDeg P = (expSupport P).max' hne := by
    rw [leadDeg, hmax]; rfl
  rw [hmax, hld]

/-- A nonzero element has a nonzero leading coefficient. -/
theorem leadCoeff_ne_zero {P : QuantumTorus A} (hP : P ≠ 0) : leadCoeff P ≠ 0 := by
  have hne := support_nonempty_of_ne_zero hP
  have hmem : (expSupport P).max' hne ∈ expSupport P := Finset.max'_mem _ hne
  have hld : leadDeg P = (expSupport P).max' hne := by
    have h : ((leadDeg P : ℤ) : WithBot ℤ) = ((expSupport P).max' hne : WithBot ℤ) := by
      rw [← topDeg_eq_leadDeg hP, topDeg, ← Finset.coe_max' hne]
    exact_mod_cast h
  rw [leadCoeff, hld]
  exact (mem_expSupport_iff P _).mp hmem

/-! ### QDM-2 — the leading-coefficient product law and multiplicativity -/

/-- A support exponent is bounded by any upper bound on `topDeg`. -/
theorem toAdd_le_of_mem_support {P : QuantumTorus A} {m : ℤ}
    (hP : topDeg P ≤ (m : WithBot ℤ)) {x : Ldeg} (hx : x ∈ P.support) :
    Multiplicative.toAdd x ≤ m := by
  have hmem : Multiplicative.toAdd x ∈ expSupport P := by
    rw [expSupport]; exact Finset.mem_image_of_mem _ hx
  have h1 : ((Multiplicative.toAdd x : ℤ) : WithBot ℤ) ≤ topDeg P := Finset.le_max hmem
  exact_mod_cast le_trans h1 hP

/-- **QDM-2 leading-coefficient product law (holds over any `CommRing`).**
    The coefficient of `P·Q` at the sum of top degrees is the *twisted* product
    of the leading coefficients: `coeffAt (P·Q) (m+n) = coeffAt P m · σᵐ(coeffAt Q n)`.
    The twist `σᵐ = ofAdd m • ·` is the graded structure constant that survives
    into the associated graded ring. -/
theorem coeffAt_mul_add {P Q : QuantumTorus A} {m n : ℤ}
    (hP : topDeg P ≤ (m : WithBot ℤ)) (hQ : topDeg Q ≤ (n : WithBot ℤ)) :
    coeffAt (P * Q) (m + n)
      = coeffAt P m * (Multiplicative.ofAdd m • coeffAt Q n) := by
  have key : (Multiplicative.ofAdd (m + n) : Ldeg)
      = Multiplicative.ofAdd m * Multiplicative.ofAdd n := by rw [ofAdd_add]
  rw [coeffAt, key, coeff_mul]
  simp only [sum_def]
  -- Outer sum: only `a₁ = ofAdd m` survives.
  have outerVanish : ∀ b : Ldeg, P.toFinsupp b ≠ 0 → b ≠ Multiplicative.ofAdd m →
      (Q.toFinsupp.sum fun a₂ b₂ =>
        if b * a₂ = Multiplicative.ofAdd m * Multiplicative.ofAdd n
        then P.toFinsupp b * b • b₂ else 0) = 0 := by
    intro b hb hbne
    have hble : Multiplicative.toAdd b ≤ m :=
      toAdd_le_of_mem_support hP (mem_support_iff.mpr hb)
    have hbne' : Multiplicative.toAdd b ≠ m := by
      intro h; apply hbne; apply Multiplicative.toAdd.injective
      rw [toAdd_ofAdd]; exact h
    have hblt : Multiplicative.toAdd b < m := lt_of_le_of_ne hble hbne'
    refine (Finsupp.sum_congr (g2 := fun _ _ => 0) ?_).trans Finsupp.sum_zero
    intro a₂ ha₂
    have ha2le : Multiplicative.toAdd a₂ ≤ n :=
      toAdd_le_of_mem_support hQ (by exact ha₂)
    rw [if_neg]
    intro hcond
    have hda := congrArg Multiplicative.toAdd hcond
    simp only [toAdd_mul, toAdd_ofAdd] at hda
    omega
  have outerZero : P.toFinsupp (Multiplicative.ofAdd m) = 0 →
      (Q.toFinsupp.sum fun a₂ b₂ =>
        if Multiplicative.ofAdd m * a₂ = Multiplicative.ofAdd m * Multiplicative.ofAdd n
        then (0 : A) * Multiplicative.ofAdd m • b₂ else 0) = 0 := by
    intro _
    refine (Finsupp.sum_congr (g2 := fun _ _ => 0) ?_).trans Finsupp.sum_zero
    intro a₂ _; simp
  rw [Finsupp.sum_eq_single (Multiplicative.ofAdd m) outerVanish outerZero]
  -- Inner sum: only `a₂ = ofAdd n` survives.
  have innerVanish : ∀ b : Ldeg, Q.toFinsupp b ≠ 0 → b ≠ Multiplicative.ofAdd n →
      (if Multiplicative.ofAdd m * b = Multiplicative.ofAdd m * Multiplicative.ofAdd n
       then P.toFinsupp (Multiplicative.ofAdd m) * Multiplicative.ofAdd m • Q.toFinsupp b
       else 0) = 0 := by
    intro b _ hbne
    rw [if_neg]
    intro hcond
    exact hbne (mul_left_cancel hcond)
  have innerZero : Q.toFinsupp (Multiplicative.ofAdd n) = 0 →
      (if Multiplicative.ofAdd m * Multiplicative.ofAdd n
          = Multiplicative.ofAdd m * Multiplicative.ofAdd n
       then P.toFinsupp (Multiplicative.ofAdd m) * Multiplicative.ofAdd m • (0 : A)
       else 0) = 0 := by
    intro _; simp
  rw [Finsupp.sum_eq_single (Multiplicative.ofAdd n) innerVanish innerZero, if_pos rfl]
  rfl

/-- **QDM-2 vanishing lemma:** above the sum of top degrees the product's
    coefficients vanish (holds over any `CommRing`). -/
theorem coeffAt_mul_eq_zero_of_lt {P Q : QuantumTorus A} {m n k : ℤ}
    (hP : topDeg P ≤ (m : WithBot ℤ)) (hQ : topDeg Q ≤ (n : WithBot ℤ))
    (hk : m + n < k) : coeffAt (P * Q) k = 0 := by
  rw [coeffAt, coeff_mul]
  simp only [sum_def]
  refine (Finsupp.sum_congr (g2 := fun _ _ => 0) ?_).trans Finsupp.sum_zero
  intro a₁ ha₁
  have h1le : Multiplicative.toAdd a₁ ≤ m := toAdd_le_of_mem_support hP (by exact ha₁)
  refine (Finsupp.sum_congr (g2 := fun _ _ => 0) ?_).trans Finsupp.sum_zero
  intro a₂ ha₂
  have h2le : Multiplicative.toAdd a₂ ≤ n := toAdd_le_of_mem_support hQ (by exact ha₂)
  rw [if_neg]
  intro hcond
  have hda := congrArg Multiplicative.toAdd hcond
  simp only [toAdd_mul, toAdd_ofAdd] at hda
  omega

/-- **QDM-2 order additivity (over a domain).**  `topDeg (P·Q) = topDeg P + topDeg Q`
    for nonzero `P`, `Q`: the leading coefficients do not annihilate. -/
theorem topDeg_mul [IsDomain A] {P Q : QuantumTorus A} (hP : P ≠ 0) (hQ : Q ≠ 0) :
    topDeg (P * Q) = ((leadDeg P + leadDeg Q : ℤ) : WithBot ℤ) := by
  set m := leadDeg P with hm
  set n := leadDeg Q with hn
  have htP : topDeg P = (m : WithBot ℤ) := topDeg_eq_leadDeg hP
  have htQ : topDeg Q = (n : WithBot ℤ) := topDeg_eq_leadDeg hQ
  have hlead : coeffAt (P * Q) (m + n)
      = leadCoeff P * (Multiplicative.ofAdd m • leadCoeff Q) :=
    coeffAt_mul_add (le_of_eq htP) (le_of_eq htQ)
  have hne : coeffAt (P * Q) (m + n) ≠ 0 := by
    rw [hlead]
    refine mul_ne_zero (leadCoeff_ne_zero hP) ?_
    intro h
    apply leadCoeff_ne_zero hQ
    have hz : (Multiplicative.ofAdd (-m)) • (Multiplicative.ofAdd m • leadCoeff Q) = 0 := by
      rw [h]; simp
    rwa [← mul_smul, ← ofAdd_add, neg_add_cancel, ofAdd_zero, one_smul] at hz
  have hmem : (m + n) ∈ expSupport (P * Q) := (mem_expSupport_iff _ _).mpr hne
  have hge : ((m + n : ℤ) : WithBot ℤ) ≤ topDeg (P * Q) := Finset.le_max hmem
  have hle : topDeg (P * Q) ≤ ((m + n : ℤ) : WithBot ℤ) := by
    rw [topDeg]
    apply Finset.max_le
    intro k hk
    by_contra hcon
    rw [not_le] at hcon
    have hkk : m + n < k := by exact_mod_cast hcon
    have : coeffAt (P * Q) k = 0 :=
      coeffAt_mul_eq_zero_of_lt (le_of_eq htP) (le_of_eq htQ) hkk
    exact ((mem_expSupport_iff _ _).mp hk) this
  exact le_antisymm hle hge

/-- **QDM-2 principal symbol is multiplicative (over a domain).**
    `symbol (P·Q) = symbol P · symbol Q`.  This is the associated-graded
    ring-hom property of the principal-symbol map — the leading term of a
    product is the (twisted) product of the leading terms.  The `[IsDomain A]`
    hypothesis is exactly what keeps the leading coefficient nonzero (so the
    top degree is `leadDeg P + leadDeg Q`, not lower). -/
theorem symbol_mul [IsDomain A] {P Q : QuantumTorus A} (hP : P ≠ 0) (hQ : Q ≠ 0) :
    symbol (P * Q) = symbol P * symbol Q := by
  have hld : leadDeg (P * Q) = leadDeg P + leadDeg Q :=
    leadDeg_of_topDeg (by exact_mod_cast topDeg_mul hP hQ)
  have hlc : leadCoeff (P * Q)
      = leadCoeff P * (Multiplicative.ofAdd (leadDeg P) • leadCoeff Q) := by
    rw [leadCoeff, hld]
    exact coeffAt_mul_add (le_of_eq (topDeg_eq_leadDeg hP)) (le_of_eq (topDeg_eq_leadDeg hQ))
  rw [symbol, symbol, symbol, hld, hlc, monomial_mul_monomial]

end QOU.Machinery.QuantumTorus
