import QOU.SchurWeyl.JMProjector

/-!
# Explicit central idempotents `e_λ` of `H_{n+1}(q)` for every `n` (bean `qou-2150`, owner ruling D2)

`conj:explicit-central-idempotent` claims that the Murphy–Lagrange element

    e_λ = Σ_{T ∈ SYT(λ)} ∏_{k} ∏_{c ≠ c(T(k))} (J_k − c)/(c(T(k)) − c)

is the central primitive idempotent of the `λ`-block of `H_n(q)`, with four cross-checks:
sum to identity, orthogonality, self-adjointness, bar-pairing. Its Lean carrier
(`ExplicitCentralIdempotentConjecture`) states this about an opaque scalar, so it cannot be proved
as written. This module re-states it on the real Iwahori–Hecke algebra `QOU.SchurWeyl.Hecke` and
**proves cross-checks 1 and 2, and centrality, for every `n`**, at generic `q`.

## How, and what it rests on

Nothing new is assumed. The corpus already proves (`QOU.SchurWeyl.JMProjector`):

* `heckeWedderburn q : H_{n+1}(q) ≃ₐ ∏_λ M_{f^λ}(K)`, from faithfulness and surjectivity of the
  seminormal representations (`HeckeProductInjective`, `HeckeProductSurjective`);
* `heckeWedderburn_symm_single`: the Lagrange product in the **additive** Jucys–Murphy elements
  `Y_k` maps to the matrix unit `E^λ_{TT}`.

So `π_T = W⁻¹(E^λ_{TT})` and `e_λ = W⁻¹(1_λ)`, and the cross-checks are matrix-unit identities
transported through the algebra isomorphism. `mulProj_eq_proj` shows that the `.md` formula
in the **multiplicative** Murphy elements `J_k = L_k` (`qJM`, eigenvalue `q^{2c}`) is the same
element, using `L_k = 1 + (q² − 1) Y_k`. The spectrum is `{q^{2d} : |d| ≤ n}`, which is the set of
contents of all partitions of `n + 1`, as in the `.md`.

## Scope

* Generic `q`: `q ≠ 0`, `NotRootOfUnity q`, over a field of characteristic zero — inherited from
  `heckeWedderburn`. At a root of unity the algebra is not semisimple and the statement changes.
* **Proved:** each `π_T` is idempotent, distinct `π_T` are orthogonal, `e_λ` is central,
  idempotent, nonzero, pairwise orthogonal, and `Σ_λ e_λ = 1`.
* **Not proved here:** primitivity of `e_λ` in the centre (true, since its image is the unit of a
  simple block, but not stated), and cross-checks 3–4 (self-adjointness and bar-pairing under the
  bar involution), which need the bar involution on `H_{n+1}(q)`.
-/

namespace QOU.BraidKnot.ExplicitCentralIdempotentGeneral

open QOU.SchurWeyl QOU.SchurWeyl.JMProjector

variable {K : Type*} [Field K] [CharZero K] (q : K) (hq0 : q ≠ 0)
  (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ)

/-- Shorthand for the Wedderburn blocks of `H_{n+1}(q)`. -/
abbrev Blocks (K : Type*) [Field K] (n : ℕ) :=
  ∀ lam : Nat.Partition (n + 1),
    Matrix (QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam))
      (QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam)) K


omit [CharZero K] in
theorem sum_single_diag_one {ι : Type*} [Fintype ι] [DecidableEq ι] :
    ∑ i : ι, Matrix.single i i (1 : K) = 1 := by
  ext a b
  simp only [Matrix.sum_apply, Matrix.single, Matrix.of_apply, Matrix.one_apply]
  by_cases h : a = b
  · subst h; simp
  · simp only [h, if_false]
    exact Finset.sum_eq_zero (fun c _ => if_neg (fun hc => h (hc.1.symm.trans hc.2)))

theorem pi_single_sum {ι α : Type*} [Fintype α] [DecidableEq ι] {M : ι → Type*}
    [∀ i, AddCommMonoid (M i)] (i : ι) (f : α → M i) :
    ∑ a, Pi.single i (f a) = Pi.single (M := M) i (∑ a, f a) := by
  funext j
  by_cases h : j = i
  · subst h; simp [Finset.sum_apply]
  · simp [Finset.sum_apply, h]

/-- The Murphy–Lagrange projector of a standard Young tableau `T` of shape `λ ⊢ n+1`. -/
noncomputable def proj {lam : Nat.Partition (n + 1)}
    (T : QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam)) : Hecke K q q⁻¹ n :=
  jmProjIn q (Hecke.σ K q q⁻¹ n) (contentVec T)

/-- The Murphy–Lagrange central idempotent `e_λ = Σ_{T ∈ SYT(λ)} π_T`. -/
noncomputable def centralIdem (lam : Nat.Partition (n + 1)) : Hecke K q q⁻¹ n :=
  ∑ T : QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam), proj q n T

theorem proj_eq_symm {lam : Nat.Partition (n + 1)}
    (T : QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam)) :
    proj q n T = (heckeWedderburn q hq0 hq2 n).symm (Pi.single lam (Matrix.single T T 1)) :=
  (heckeWedderburn_symm_single q hq0 hq2 n lam T).symm

theorem centralIdem_eq_symm (lam : Nat.Partition (n + 1)) :
    centralIdem q n lam = (heckeWedderburn q hq0 hq2 n).symm (Pi.single lam 1) := by
  classical
  simp only [centralIdem, proj_eq_symm q hq0 hq2 n, ← map_sum]
  congr 1
  rw [pi_single_sum, sum_single_diag_one]

local notation "W" => heckeWedderburn q hq0 hq2 n

include hq0 hq2 in
/-- **Idempotency** of each Murphy–Lagrange projector. -/
theorem proj_idem {lam : Nat.Partition (n + 1)}
    (T : QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam)) :
    proj q n T * proj q n T = proj q n T := by
  classical
  rw [proj_eq_symm q hq0 hq2 n, ← map_mul, ← Pi.single_mul, Matrix.single_mul_single_same,
    one_mul]

include hq0 hq2 in
/-- **Orthogonality** within one shape: distinct tableaux give orthogonal projectors. -/
theorem proj_orth_same {lam : Nat.Partition (n + 1)}
    {T U : QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam)} (h : T ≠ U) :
    proj q n T * proj q n U = 0 := by
  classical
  have show_zero : Matrix.single T T (1 : K) * Matrix.single U U 1 = 0 := by
    ext a b
    simp only [Matrix.mul_apply, Matrix.single, Matrix.of_apply, Matrix.zero_apply]
    refine Finset.sum_eq_zero (fun c _ => ?_)
    by_cases h1 : T = a ∧ T = c
    · rw [if_pos h1, if_neg (fun h2 => h (h1.2.trans h2.1.symm)), mul_zero]
    · rw [if_neg h1, zero_mul]
  rw [proj_eq_symm q hq0 hq2 n, proj_eq_symm q hq0 hq2 n, ← map_mul, ← Pi.single_mul,
    show_zero, Pi.single_zero, map_zero]

omit [CharZero K] in
theorem pi_single_mul_of_ne {lam mu : Nat.Partition (n + 1)} (h : lam ≠ mu) (a : Matrix
    (QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam))
    (QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam)) K) (b : Matrix
    (QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape mu))
    (QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape mu)) K) :
    (Pi.single lam a : Blocks K n) * Pi.single mu b = 0 := by
  classical
  funext nu
  simp only [Pi.mul_apply, Pi.zero_apply]
  by_cases h1 : nu = lam
  · subst h1; rw [Pi.single_eq_of_ne h, mul_zero]
  · rw [Pi.single_eq_of_ne h1, zero_mul]

include hq0 hq2 in
/-- **Orthogonality** across shapes. -/
theorem proj_orth_ne {lam mu : Nat.Partition (n + 1)} (h : lam ≠ mu)
    (T : QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam))
    (U : QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape mu)) :
    proj q n T * proj q n U = 0 := by
  rw [proj_eq_symm q hq0 hq2 n, proj_eq_symm q hq0 hq2 n, ← map_mul,
    pi_single_mul_of_ne n h, map_zero]

include hq0 hq2 in
/-- **`e_λ` is idempotent.** -/
theorem centralIdem_idem (lam : Nat.Partition (n + 1)) :
    centralIdem q n lam * centralIdem q n lam = centralIdem q n lam := by
  classical
  rw [centralIdem_eq_symm q hq0 hq2 n, ← map_mul, ← Pi.single_mul, one_mul]

include hq0 hq2 in
/-- **`e_λ e_μ = 0` for `λ ≠ μ`.** -/
theorem centralIdem_orth {lam mu : Nat.Partition (n + 1)} (h : lam ≠ mu) :
    centralIdem q n lam * centralIdem q n mu = 0 := by
  rw [centralIdem_eq_symm q hq0 hq2 n, centralIdem_eq_symm q hq0 hq2 n, ← map_mul,
    pi_single_mul_of_ne n h, map_zero]

include hq0 hq2 in
/-- **Sum to identity:** `Σ_λ e_λ = 1`, equivalently `Σ_{λ, T} π_T = 1`. -/
theorem sum_centralIdem : ∑ lam, centralIdem q n lam = 1 := by
  classical
  simp only [centralIdem_eq_symm q hq0 hq2 n, ← map_sum]
  rw [show (∑ lam, (Pi.single lam 1 : Blocks K n)) = 1 from Finset.univ_sum_single 1, map_one]

include hq0 hq2 in
/-- **`e_λ` is central.** -/
theorem centralIdem_central (lam : Nat.Partition (n + 1)) (x : Hecke K q q⁻¹ n) :
    centralIdem q n lam * x = x * centralIdem q n lam := by
  classical
  apply (W).injective
  rw [map_mul, map_mul, centralIdem_eq_symm q hq0 hq2 n, AlgEquiv.apply_symm_apply]
  funext nu
  simp only [Pi.mul_apply]
  by_cases h : nu = lam
  · subst h; simp
  · simp [Pi.single_eq_of_ne h]

include hq0 hq2 in
/-- **`e_λ ≠ 0`.** -/
theorem centralIdem_ne_zero (lam : Nat.Partition (n + 1)) [Nonempty
    (QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam))] :
    centralIdem q n lam ≠ 0 := by
  classical
  rw [centralIdem_eq_symm q hq0 hq2 n]
  intro h0
  have := congrArg (fun y => (W y) lam) h0
  simp only [AlgEquiv.apply_symm_apply, Pi.single_eq_same, map_zero, Pi.zero_apply] at this
  exact one_ne_zero this

/-! ## The formula in the multiplicative Murphy elements `L_k`

The `.md` writes the projector with the multiplicative Jucys–Murphy elements `J_k = L_k`
(`qJM`, eigenvalue `q^{2c}`). The corpus' `jmProjIn` uses the additive `Y_k`. They agree factor
by factor: `L_k = 1 + (q² − 1) Y_k` and `q^{2c} = 1 + (q² − 1)[c]_{q²}`. -/

/-- The `k`-th Lagrange factor in `L_k`: `∏_{d ≠ c, |d| ≤ n} (L_k − q^{2d})/(q^{2c} − q^{2d})`. -/
noncomputable def mulFactor (k : ℕ) (c : ℤ) : Hecke K q q⁻¹ n :=
  (((contentRange n).filter (fun d => d ≠ c)).map
    (fun d => (q ^ (2 * c) - q ^ (2 * d))⁻¹ •
      (qJM K q q⁻¹ n k - algebraMap K (Hecke K q q⁻¹ n) (q ^ (2 * d))))).prod

/-- The projector of the `.md` boxed formula, in the multiplicative Murphy elements. -/
noncomputable def mulProj {lam : Nat.Partition (n + 1)}
    (T : QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam)) : Hecke K q q⁻¹ n :=
  ((List.range (n + 1)).map (fun k => mulFactor q n k (contentVec T k))).prod

omit [CharZero K] in
include hq0 hq2 in
/-- **The multiplicative and additive forms agree.** -/
theorem mulProj_eq_proj {lam : Nat.Partition (n + 1)}
    (T : QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam)) :
    mulProj q n T = proj q n T := by
  have hs : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr (hq2 2 (by norm_num))
  unfold mulProj proj jmProjIn
  congr 1
  refine List.map_congr_left (fun k _ => ?_)
  unfold mulFactor jmFactorIn
  congr 1
  refine List.map_congr_left (fun d _ => ?_)
  set c := contentVec T k
  have hL : qJM K q q⁻¹ n k = 1 + (q ^ 2 - 1) • jmAdd q n k := by
    rw [sq_sub_one_smul_jmAdd q hq0 n k]; abel
  have hc : q ^ (2 * c) = 1 + (q ^ 2 - 1) * qInt2 q c := by
    rw [sq_sub_one_mul_qInt2 q hq0 c]; ring
  have hd : q ^ (2 * d) = 1 + (q ^ 2 - 1) * qInt2 q d := by
    rw [sq_sub_one_mul_qInt2 q hq0 d]; ring
  rw [hL, hc, hd]
  have e1 : (1 + (q ^ 2 - 1) * qInt2 q c - (1 + (q ^ 2 - 1) * qInt2 q d))⁻¹
      = (q ^ 2 - 1)⁻¹ * (qInt2 q c - qInt2 q d)⁻¹ := by
    rw [show 1 + (q ^ 2 - 1) * qInt2 q c - (1 + (q ^ 2 - 1) * qInt2 q d)
        = (q ^ 2 - 1) * (qInt2 q c - qInt2 q d) by ring, mul_inv]
  have e2 : (1 : Hecke K q q⁻¹ n) + (q ^ 2 - 1) • jmAdd q n k
      - algebraMap K (Hecke K q q⁻¹ n) (1 + (q ^ 2 - 1) * qInt2 q d)
      = (q ^ 2 - 1) • (jmAdd q n k - algebraMap K (Hecke K q q⁻¹ n) (qInt2 q d)) := by
    rw [map_add, map_one, map_mul, smul_sub, Algebra.smul_def (q ^ 2 - 1)
      (algebraMap K _ (qInt2 q d))]
    abel
  rw [e1, e2, smul_smul]
  congr 1
  field_simp

include hq0 hq2 in
/-- The `.md` boxed formula, in `L_k`, is the Wedderburn matrix unit `E^λ_{TT}`. -/
theorem mulProj_eq_symm {lam : Nat.Partition (n + 1)}
    (T : QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape lam)) :
    mulProj q n T = (heckeWedderburn q hq0 hq2 n).symm (Pi.single lam (Matrix.single T T 1)) := by
  rw [mulProj_eq_proj q hq0 hq2 n, proj_eq_symm q hq0 hq2 n]

include hq0 hq2 in
/-- **Cross-checks 1 and 2 of `conj:explicit-central-idempotent`, and centrality, for every `n`.**
At generic `q` (`q ≠ 0`, not a root of unity) over a characteristic-zero field, the elements
`e_λ = Σ_{T ∈ SYT(λ)} π_T`, with `π_T` the Murphy–Lagrange product of the `.md` boxed formula,
are central, idempotent, pairwise orthogonal, and sum to `1` in `H_{n+1}(q)`. -/
theorem explicit_central_idempotent_cross_checks :
    (∀ lam, ∀ x : Hecke K q q⁻¹ n, centralIdem q n lam * x = x * centralIdem q n lam) ∧
    (∀ lam, centralIdem q n lam * centralIdem q n lam = centralIdem q n lam) ∧
    (∀ lam mu, lam ≠ mu → centralIdem q n lam * centralIdem q n mu = 0) ∧
    (∑ lam, centralIdem q n lam = 1) :=
  ⟨centralIdem_central q hq0 hq2 n, centralIdem_idem q hq0 hq2 n,
    fun _ _ h => centralIdem_orth q hq0 hq2 n h, sum_centralIdem q hq0 hq2 n⟩

end QOU.BraidKnot.ExplicitCentralIdempotentGeneral

