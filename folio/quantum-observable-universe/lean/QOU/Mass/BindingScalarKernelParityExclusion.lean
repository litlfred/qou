/-
# QOU.Mass.BindingScalarKernelParityExclusion — no SCALAR q-difference kernel
  on the surviving (q-Borel / Gevrey-normalized) binding carrier

`prop:binding-genfun-qdifference` posits the **rank-1** relation

    G(qx;q) = R(q,x)·G(x;q),      R ∈ ℚ(q)[x,x⁻¹] of bounded depth d,

and `conj:qdifference-kernel-prolongation-symbol` names its carrier: the rank-2
q-difference module `𝒦` of the binding q-lift recurrence
`[m+2]_q·b_{m+2} = b_{m+1} + b_m`, i.e. (with `x = q^m`, `σ : x ↦ qx`)

    L_𝒦 = (q²x − 1)·σ² − (q−1)·σ − (q−1).

Two carriers have been proposed for `G`, and the first is already closed:

* **raw** — the OGF of the raw body terms `B_n = I(n)/n`. Excluded sorry-free by
  the confluent/Gevrey growth argument
  `QOU.Mass.QDifferenceConfluentObstruction.no_bounded_depth_first_order_kernel`
  (audit `2026-07-20-qdifference-kernel-confluent-narrowing.md` §4).
* **normalized** — the q-Borel carrier `b_n = f_n/[n]_q!`, to which §5 of that
  audit explicitly RE-TARGETED the conjecture ("the obstruction vanishes"),
  predicting depth `d = 2`. It provably satisfies `L_𝒦` (sorry-free,
  `QOU.Mass.QDifferenceConfluentObstruction.qlift_normalized_kernel_exists`).

This file closes the second. A scalar kernel is a first-order right factor
`σ − a` of `L_𝒦`, i.e. a solution `a ∈ K(x)` of the **q-Riccati** equation
`(q²x − 1)·a(qx)·a(x) − (q−1)·a(x) − (q−1) = 0`. Writing `a = P/Q` and clearing
denominators gives `riccatiResidual q P Q = 0`, whose three terms have degrees

    T₁ = 1 + 2p,      T₂ = p + u,      T₃ = 2u        (p = deg P, u = deg Q).

`T₁` is **odd-shaped** and `T₃` is **even**, so `T₁ = T₃` is impossible over ℤ
(`riccati_top_degrees_ne`); a two-line case split then gives that the maximum of
the three is attained **exactly once** (`riccati_degree_unique_max`). A lone
top-degree term cannot cancel, so the residual is nonzero and no such `a` exists
(`no_rational_riccati_solution`). Consequently `𝒦` has no rank-1 sub- or
quotient module and **no nonzero solution of `L_𝒦` obeys any scalar relation**
(`no_scalar_kernel_on_carrier`).

**This parity IS the Newton-slope invariant.** `L_𝒦` is pure isoclinic of slope
`1/2` at infinity; every rank-1 q-difference module has INTEGER slope, and
Newton slopes are additive on sub- and quotient modules. Independently corroborated
by the van der Put–Reversat classification of pure modules: a pure module of
non-integral slope `d/r` (`gcd(d,r) = 1`) and rank `r` is the restriction of a
rank-one module over the ramified field — `E(c z^{d/r})` in van der Put–Reversat's
notation, `E(r,d,b)` in Bugeaud's — and it is irreducible. Held in this corpus
three times over: the theorem itself at `library/afst-2007-6-16-3-665-0/`
([vanderput-reversat2007] Prop. 1.3, over the formal field), its English survey
form at `library/arxiv-math-0612592v1/` ([vanderput2006] Thm 3.4–3.5, over the
convergent field, with uniqueness of the triple `(d/r, c^r, m)`), and the
`E(r,d,b)` notation at `library/crmath-2011-349-19-20-1037-0/` ([bugeaud2011],
a *use* of the theorem in the two-slope non-integral classification, not its
source — this docstring previously pointed only there, and attributed it to
van der Put–Reversat). Slope `1/2` has `r = 2 = rank 𝒦`. Measured corroboration (second differences of `log_q|b_m|`
→ `−1/2`, with the period-2 ramification amplitude directly observed) in
`computations/probes/binding_qdiff_scalar_kernel_parity_exclusion_probe.py`.

## SCOPE (AGENTS.md "refuted"/"ruled out" discipline)

**Scope (b), structural exclusion, invariant cited** — the degree parity
`2u − 2p = 1` being unsolvable over ℤ, equivalently the non-integrality of the
Newton slope. It holds for every field `K` and every `q ∈ K` with `q ≠ 0, 1`.

**What is NOT excluded, and must not be read as excluded.** The carrier `𝒦`
stands; the audit's depth-`d = 2` prediction stands; the prolongation-symbol
identification is untouched. Only the **scalar** form dies. "Depth 2" means
**rank 2**: the kernel is a `2×2` matrix `A(q,x)` on `(G, σG)`, whose τ-image is
a first-order 2-component (Dirac-type) system — the shape
`prop:binding-genfun-qdifference` already asks for. The exclusion is over `K(x)`:
after a degree-2 **ramified** base change (adjoining `q^{1/2}`, `x^{1/2}`) the
slope becomes the integer `1` and a scalar kernel does exist on the double cover,
relating half-shifts — i.e. even and odd body orders separately. That
ramification is the missing structure, not a gap in the proof.

**One downstream claim is falsified.** Consequence 2 of
`conj:qdifference-kernel-prolongation-symbol` — that the recurrence "determines
every body term from the deuteron base case" — is wrong by exactly one initial
condition: a rank-2 module needs TWO. The genuine three-body `n = 3` term is
independently required (bean `qou-hh9q`).

`§7c`: generic `[Field K]` throughout (the Riccati needs `x⁻¹`; no ordering, no
`Real`, no archimedean structure — this is fibre-level algebra). Sorry-free.

-- Ref: [leitner2026] mass-theory, prop:binding-genfun-qdifference;
--      conj:qdifference-kernel-prolongation-symbol
-- Ref: [leitner2026] docs/audits/2026-07-20-qdifference-kernel-confluent-narrowing.md §§4–5
-- Ref: [vanderput-reversat2007] library/afst-2007-6-16-3-665-0/ (Prop. 1.3: E(c z^{t/n}) is irreducible of rank n and slope t/n)
-- Ref: [vanderput2006] https://arxiv.org/abs/math/0612592 (Thm 3.4–3.5: the same over C({z}), triple (t/n, c^n, m) unique)
-- Ref: [bugeaud2011] library/crmath-2011-349-19-20-1037-0/ (the E(r,d,b) notation, non-integral slopes)
-/

import Mathlib.Tactic

namespace QOU.Mass.BindingScalarKernelParityExclusion

open Polynomial

/-! ## Tier 0 — the invariant, as pure arithmetic

The whole exclusion rests on two facts about ℕ. They are isolated here so that
the obstruction is visible without any polynomial algebra. -/

/-- **The parity.** The `PP` term of the cleared q-Riccati has degree `1 + 2p`
and the `QQ` term has degree `2u`; the first is odd-shaped and the second even,
so they can never coincide. Equivalently `2u − 2p = 1` has no solution over ℤ.
This single fact is the Newton slope's denominator `2`. -/
theorem riccati_top_degrees_ne (p u : ℕ) : 1 + 2 * p ≠ 2 * u := by omega

/-- **Unique strict maximum.** For every pair of degrees, exactly one of the
three cleared-Riccati terms attains the top degree: `T₁ = 1 + 2p` when `u ≤ p`,
and `T₃ = 2u` when `p < u`. The middle term `T₂ = p + u` never wins. A lone
top-degree term has nothing to cancel against. -/
theorem riccati_degree_unique_max (p u : ℕ) :
    (p + u < 1 + 2 * p ∧ 2 * u < 1 + 2 * p) ∨ (p + u < 2 * u ∧ 1 + 2 * p < 2 * u) := by
  omega

/-! ## Tier 1 — a lone top-degree term cannot cancel -/

/-- If `A` has degree exactly `M` and is nonzero while `B` and `C` sit strictly
below `M`, then `A − B − C ≠ 0`: read off the coefficient at `M`. -/
theorem sub_sub_ne_zero_of_top_unique {K : Type*} [CommRing K] {A B C : K[X]} {M : ℕ}
    (hA : A.natDegree = M) (hA0 : A ≠ 0)
    (hB : B.natDegree < M) (hC : C.natDegree < M) :
    A - B - C ≠ 0 := by
  intro hzero
  have hcoeff : (A - B - C).coeff M = 0 := by rw [hzero]; simp
  rw [coeff_sub, coeff_sub, coeff_eq_zero_of_natDegree_lt hB,
    coeff_eq_zero_of_natDegree_lt hC] at hcoeff
  have hAc : A.coeff M = 0 := by linear_combination hcoeff
  exact leadingCoeff_ne_zero.mpr hA0 (by rw [leadingCoeff, hA]; exact hAc)

/-- Mirror of `sub_sub_ne_zero_of_top_unique` for the case where the SUBTRACTED
tail term `C` carries the top degree: its coefficient survives with a sign. -/
theorem sub_sub_ne_zero_of_top_unique' {K : Type*} [CommRing K] {A B C : K[X]} {M : ℕ}
    (hC : C.natDegree = M) (hC0 : C ≠ 0)
    (hA : A.natDegree < M) (hB : B.natDegree < M) :
    A - B - C ≠ 0 := by
  intro hzero
  have hcoeff : (A - B - C).coeff M = 0 := by rw [hzero]; simp
  rw [coeff_sub, coeff_sub, coeff_eq_zero_of_natDegree_lt hA,
    coeff_eq_zero_of_natDegree_lt hB] at hcoeff
  have hCc : C.coeff M = 0 := by linear_combination -hcoeff
  exact leadingCoeff_ne_zero.mpr hC0 (by rw [leadingCoeff, hC]; exact hCc)

/-! ## Tier 2 — the q-dilation `P(x) ↦ P(qx)` -/

/-- The q-dilation `(dil q P)(x) = P(qx)`, the substitution the shift `σ`
performs on a polynomial coefficient-wise. -/
noncomputable def dil {K : Type*} [Field K] (q : K) (P : K[X]) : K[X] :=
  P.comp (C q * X)

@[simp] theorem natDegree_dil {K : Type*} [Field K] {q : K} (hq : q ≠ 0) (P : K[X]) :
    (dil q P).natDegree = P.natDegree := by
  rw [dil, natDegree_comp]; simp [natDegree_C_mul_X _ hq]

theorem dil_ne_zero {K : Type*} [Field K] {q : K} (hq : q ≠ 0) {P : K[X]} (hP : P ≠ 0) :
    dil q P ≠ 0 := by
  rw [dil]
  refine leadingCoeff_ne_zero.mp ?_
  rw [leadingCoeff_comp (by simp [natDegree_C_mul_X _ hq])]
  exact mul_ne_zero (leadingCoeff_ne_zero.mpr hP) (pow_ne_zero _ (by simpa using hq))

/-! ## Tier 3 — the cleared q-Riccati residual, and the exclusion -/

/-- The cleared q-Riccati residual of `L_𝒦 = (q²x−1)σ² − (q−1)σ − (q−1)`.
Substituting `σy = a·y` with `a = P/Q` into `L_𝒦 y = 0` and multiplying through
by `Q(qx)Q(x)` gives exactly this polynomial; `a` solves the Riccati iff the
residual vanishes. No coprimality of `P, Q` is needed anywhere below. -/
noncomputable def riccatiResidual {K : Type*} [Field K] (q : K) (P Q : K[X]) : K[X] :=
  (C (q ^ 2) * X - 1) * dil q P * P
    - C (q - 1) * (P * dil q Q)
    - C (q - 1) * (dil q Q * Q)

/-- **THE EXCLUSION.** For any field `K` and any `q ≠ 0, 1`, the cleared
q-Riccati residual of `L_𝒦` is nonzero for every pair of nonzero polynomials.
Hence the q-Riccati has **no solution `a ∈ K(x)`**, so `L_𝒦` has no first-order
right factor and the rank-2 module `𝒦` is irreducible.

The proof is the parity: by `riccati_degree_unique_max` exactly one of the three
terms attains the top degree — the `PP` term (degree `1 + 2p`) when `u ≤ p`, the
`QQ` term (degree `2u`) when `p < u` — and by `sub_sub_ne_zero_of_top_unique` a
lone top-degree term cannot cancel. -/
theorem no_rational_riccati_solution {K : Type*} [Field K] {q : K}
    (hq0 : q ≠ 0) (hq1 : q ≠ 1) {P Q : K[X]} (hP : P ≠ 0) (hQ : Q ≠ 0) :
    riccatiResidual q P Q ≠ 0 := by
  set p := P.natDegree with hp
  set u := Q.natDegree with hu
  have hqq : (q - 1) ≠ 0 := sub_ne_zero_of_ne hq1
  have hCq : (C (q - 1) : K[X]) ≠ 0 := Polynomial.C_ne_zero.mpr hqq
  have hdeg2 : (C (q ^ 2) * X : K[X]).natDegree = 1 :=
    natDegree_C_mul_X _ (pow_ne_zero 2 hq0)
  have hlin : (C (q ^ 2) * X - 1 : K[X]).natDegree = 1 := by
    have h1 : ((1 : K[X])).natDegree < (C (q ^ 2) * X : K[X]).natDegree := by
      rw [hdeg2, natDegree_one]; norm_num
    rw [natDegree_sub_eq_left_of_natDegree_lt h1, hdeg2]
  have hlin0 : (C (q ^ 2) * X - 1 : K[X]) ≠ 0 := by
    intro h; rw [h, natDegree_zero] at hlin; exact absurd hlin (by norm_num)
  have hdP := dil_ne_zero hq0 hP
  have hdQ := dil_ne_zero hq0 hQ
  -- the three term degrees
  have hT1 : ((C (q ^ 2) * X - 1) * dil q P * P).natDegree = 1 + 2 * p := by
    rw [natDegree_mul (mul_ne_zero hlin0 hdP) hP, natDegree_mul hlin0 hdP, hlin,
      natDegree_dil hq0]
    omega
  have hT2 : (C (q - 1) * (P * dil q Q)).natDegree = p + u := by
    rw [natDegree_mul hCq (mul_ne_zero hP hdQ), natDegree_mul hP hdQ,
      natDegree_dil hq0, natDegree_C]
    omega
  have hT3 : (C (q - 1) * (dil q Q * Q)).natDegree = 2 * u := by
    rw [natDegree_mul hCq (mul_ne_zero hdQ hQ), natDegree_mul hdQ hQ,
      natDegree_dil hq0, natDegree_C]
    omega
  have hT10 : ((C (q ^ 2) * X - 1) * dil q P * P) ≠ 0 :=
    mul_ne_zero (mul_ne_zero hlin0 hdP) hP
  have hT30 : (C (q - 1) * (dil q Q * Q)) ≠ 0 :=
    mul_ne_zero hCq (mul_ne_zero hdQ hQ)
  rw [riccatiResidual]
  rcases riccati_degree_unique_max p u with ⟨h2, h3⟩ | ⟨h2, h3⟩
  · -- the PP term is the strict top
    exact sub_sub_ne_zero_of_top_unique hT1 hT10 (by omega) (by omega)
  · -- the QQ term is the strict top
    exact sub_sub_ne_zero_of_top_unique' hT3 hT30 (by omega) (by omega)

/-- **No scalar kernel on the carrier**, in the form the conjecture uses.
A scalar kernel `R = P/Q` for a nonzero solution of `L_𝒦` is exactly a solution
of the cleared q-Riccati identity below; that identity is unsatisfiable. So the
rank-1 form of `prop:binding-genfun-qdifference` cannot hold on the carrier `𝒦`
of `conj:qdifference-kernel-prolongation-symbol`, for ANY depth `d` — the depth
never enters the argument, only the degrees do. -/
theorem no_scalar_kernel_on_carrier {K : Type*} [Field K] {q : K}
    (hq0 : q ≠ 0) (hq1 : q ≠ 1) {P Q : K[X]} (hP : P ≠ 0) (hQ : Q ≠ 0) :
    (C (q ^ 2) * X - 1) * dil q P * P
      ≠ C (q - 1) * (P * dil q Q) + C (q - 1) * (dil q Q * Q) := by
  intro h
  refine no_rational_riccati_solution hq0 hq1 hP hQ ?_
  rw [riccatiResidual, h]
  ring

/-! ## Tier 4 — how much an UNCONSTRAINED kernel would leave undetermined

Logically independent of the exclusion, and it sharpens
`conj:binding-manybody-eq-jet-filtration`'s "supplies a derived target for
`R(q,x)` but does not determine it" into an exact count. -/

/-- **Exactly one new kernel coefficient per body order.** Matching the
coefficient of `x^{k+1}` in `G(qx) = R(q,x)·G(x)` expresses `(q^{k+1} − 1)·h_{k+1}`
as `r_{k+1}·h_0` plus a tail involving only kernel coefficients of order `≤ k`.
For ANY body sequence with `h_0 ≠ 0` that equation has exactly one solution
`r_{k+1}` — whatever the body terms are.

So kernel coefficients and body terms are in bijection, one for one: an
unconstrained scalar ansatz is a **reparametrisation of the unknowns, not a
determination of them**, and "`ρ·A` is an output of the recursion" is false as
stated — the recursion transfers the unknown, it does not remove it. Every bit
of the ansatz's content therefore lives in the FINITENESS of the Laurent window,
which is precisely what `no_rational_riccati_solution` shows is unattainable in
the scalar form. -/
theorem kernel_coeff_existsUnique {K : Type*} [Field K] {q : K} (h : ℕ → K)
    (h0 : h 0 ≠ 0) (r : ℕ → K) (k : ℕ) :
    ∃! rk : K, (q ^ (k + 1) - 1) * h (k + 1)
      = rk * h 0 + ∑ j ∈ Finset.range k, r (j + 1) * h (k - j) := by
  set S := ∑ j ∈ Finset.range k, r (j + 1) * h (k - j) with hS
  set T := (q ^ (k + 1) - 1) * h (k + 1) with hT
  refine ⟨(T - S) / h 0, ?_, ?_⟩
  · field_simp; ring
  · intro y hy
    rw [eq_div_iff h0]
    linear_combination -hy

end QOU.Mass.BindingScalarKernelParityExclusion
