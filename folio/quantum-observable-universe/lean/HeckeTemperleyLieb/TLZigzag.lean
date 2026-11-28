import HeckeTemperleyLieb.TLCupCapCorner
import HeckeTemperleyLieb.TLQuotientBraiding

/-!
# Zigzag words in the Temperley–Lieb algebra

Bean `hkmt`. The word `zig p k = e_p e_{p+1} ⋯ e_{p+k-1}` is the planar isotopy that slides a
cup across `k − 1` strands; `zag p k` is the same word read backwards. These are the explicit
cup-moving maps used to put a tensor product of two standard corners into standard form
(`TLTensorCorner`), chosen once and for all so that coherence can be checked by computation.

* `zig_mul_zag`: `zig p (k+1) · zag p k = e_p`.
* `zig_mul_zag_succ`: `zig p (k+1) · zag p (k+1) = δ e_p`.
* `zag_mul_zig`: `zag p (k+1) · zig p (k+1) = δ e_{p+k}`.
* `gen_mul_zig`, `zig_mul_gen`: the cup at either end is absorbed, `e_p · zig = δ zig`,
  `zig · e_{p+k} = δ zig` (and the same for `zag`).
* `commute_zig`, `commute_zag`: a zigzag commutes with every generator two or more steps away.
* `mvn_slide`: **sliding a cup across `m` strands** is an isomorphism of corners, with the
  explicit partial isometries `Y · zig p (m+1)` and `δ⁻² Y · zag p (m+1)`.

Everything holds over any commutative ring; only the Temperley–Lieb relations are used.

-- Ref: [kauffman1987] State models and the Jones polynomial, §3 (zigzag isotopy).
-- Ref: [leitner2026] the Temperley–Lieb chapter (bean `hkmt`).
-/

namespace QOU.HeckeTemperleyLieb.TLZigzag

open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov QOU.HeckeTemperleyLieb.TLCupCap

variable {K : Type*} [Field K] {δ : K}

variable (δ) in
/-- The generator `e_i` indexed by a natural number (zero out of range). -/
noncomputable def gen (n i : ℕ) : TLFin K δ n :=
  if h : i < n then e K δ adjFin ⟨i, h⟩ else 0

theorem gen_of_lt {n i : ℕ} (h : i < n) : gen δ n i = e K δ adjFin ⟨i, h⟩ := dif_pos h

theorem gen_fin {n : ℕ} (i : Fin n) : e K δ adjFin i = gen δ n i := by
  rw [gen_of_lt i.isLt]

theorem gen_sq {n i : ℕ} (h : i < n) : gen δ n i * gen δ n i = δ • gen δ n i := by
  rw [gen_of_lt h]; exact e_sq' δ _

theorem gen_adj_up {n i : ℕ} (h : i + 1 < n) :
    gen δ n i * gen δ n (i + 1) * gen δ n i = gen δ n i := by
  rw [gen_of_lt (by omega : i < n), gen_of_lt h]
  exact e_adjacent_fin (by simp)

theorem gen_adj_down {n i : ℕ} (h : i + 1 < n) :
    gen δ n (i + 1) * gen δ n i * gen δ n (i + 1) = gen δ n (i + 1) := by
  rw [gen_of_lt (by omega : i < n), gen_of_lt h]
  exact e_adjacent_fin (by simp)

theorem commute_gen {n i j : ℕ} (h : i + 2 ≤ j ∨ j + 2 ≤ i) : Commute (gen δ n i) (gen δ n j) := by
  unfold gen
  split_ifs with hi hj
  · exact e_commute_fin (by simpa using h)
  all_goals simp

variable (δ) in
/-- `zig p k = e_p e_{p+1} ⋯ e_{p+k-1}`. -/
noncomputable def zig (n p : ℕ) : ℕ → TLFin K δ n
  | 0 => 1
  | k + 1 => zig n p k * gen δ n (p + k)

variable (δ) in
/-- `zag p k = e_{p+k-1} ⋯ e_{p+1} e_p`, the reverse word. -/
noncomputable def zag (n p : ℕ) : ℕ → TLFin K δ n
  | 0 => 1
  | k + 1 => gen δ n (p + k) * zag n p k

theorem zig_succ (n p k : ℕ) : zig δ n p (k + 1) = zig δ n p k * gen δ n (p + k) := rfl
theorem zag_succ (n p k : ℕ) : zag δ n p (k + 1) = gen δ n (p + k) * zag δ n p k := rfl

theorem zig_one (n p : ℕ) : zig δ n p 1 = gen δ n p := by simp [zig]
theorem zag_one (n p : ℕ) : zag δ n p 1 = gen δ n p := by simp [zag]

/-- A zigzag commutes with every generator two or more steps away from its support. -/
theorem commute_zig {n p i : ℕ} : ∀ k, (i + 2 ≤ p ∨ p + k + 1 ≤ i) → Commute (gen δ n i) (zig δ n p k)
  | 0, _ => Commute.one_right _
  | k + 1, h => (commute_zig k (by omega)).mul_right (commute_gen (by omega))

theorem commute_zag {n p i : ℕ} : ∀ k, (i + 2 ≤ p ∨ p + k + 1 ≤ i) → Commute (gen δ n i) (zag δ n p k)
  | 0, _ => Commute.one_right _
  | k + 1, h => (commute_gen (by omega)).mul_right (commute_zag k (by omega))

/-- `zig p (k+1) · zag p k = e_p`. -/
theorem zig_mul_zag {n p : ℕ} : ∀ k, p + k < n → zig δ n p (k + 1) * zag δ n p k = gen δ n p
  | 0, _ => by rw [zig_one, zag, mul_one]
  | k + 1, h => by
    have IH : zig δ n p (k + 1) * zag δ n p k = gen δ n p := zig_mul_zag k (by omega)
    calc zig δ n p (k + 1 + 1) * zag δ n p (k + 1)
        = zig δ n p k * (gen δ n (p + k) * gen δ n (p + k + 1) * gen δ n (p + k)) *
            zag δ n p k := by
          simp only [zig_succ, zag_succ, ← add_assoc, mul_assoc]
      _ = gen δ n p := by
          rw [gen_adj_up (by omega), ← zig_succ, IH]

/-- `zig p (k+1) · zag p (k+1) = δ e_p`. -/
theorem zig_mul_zag_succ {n p k : ℕ} (h : p + k < n) :
    zig δ n p (k + 1) * zag δ n p (k + 1) = δ • gen δ n p := by
  rw [zig_succ, zag_succ, mul_assoc, ← mul_assoc (gen δ n (p + k)), gen_sq h, smul_mul_assoc,
    mul_smul_comm, ← mul_assoc, ← zig_succ, zig_mul_zag k h]

/-- `zag p (k+1) · zig p (k+1) = δ e_{p+k}`. -/
theorem zag_mul_zig {n p : ℕ} : ∀ k, p + k < n →
    zag δ n p (k + 1) * zig δ n p (k + 1) = δ • gen δ n (p + k)
  | 0, h => by rw [zag_one, zig_one, gen_sq (by omega), add_zero]
  | k + 1, h => by
    have IH : zag δ n p (k + 1) * zig δ n p (k + 1) = δ • gen δ n (p + k) :=
      zag_mul_zig k (by omega)
    calc zag δ n p (k + 1 + 1) * zig δ n p (k + 1 + 1)
        = gen δ n (p + (k + 1)) * (zag δ n p (k + 1) * zig δ n p (k + 1)) *
            gen δ n (p + (k + 1)) := by
          simp only [zag_succ (k := k + 1), zig_succ (k := k + 1), mul_assoc]
      _ = δ • gen δ n (p + (k + 1)) := by
          rw [IH, mul_smul_comm, smul_mul_assoc, show p + (k + 1) = p + k + 1 by omega,
            gen_adj_down (by omega)]

/-- The cup at the left end is absorbed: `e_p · zig p (k+1) = δ zig p (k+1)`. -/
theorem gen_mul_zig {n p : ℕ} (hp : p < n) : ∀ k, gen δ n p * zig δ n p (k + 1) = δ • zig δ n p (k + 1)
  | 0 => by rw [zig_one, gen_sq hp]
  | k + 1 => by
    rw [zig_succ, ← mul_assoc, gen_mul_zig hp k, smul_mul_assoc]

/-- The cup at the right end is absorbed: `zig p (k+1) · e_{p+k} = δ zig p (k+1)`. -/
theorem zig_mul_gen {n p k : ℕ} (h : p + k < n) :
    zig δ n p (k + 1) * gen δ n (p + k) = δ • zig δ n p (k + 1) := by
  rw [zig_succ, mul_assoc, gen_sq h, mul_smul_comm]

theorem gen_mul_zag {n p k : ℕ} (h : p + k < n) :
    gen δ n (p + k) * zag δ n p (k + 1) = δ • zag δ n p (k + 1) := by
  rw [zag_succ, ← mul_assoc, gen_sq h, smul_mul_assoc]

theorem zag_mul_gen {n p : ℕ} (hp : p < n) : ∀ k, zag δ n p (k + 1) * gen δ n p = δ • zag δ n p (k + 1)
  | 0 => by rw [zag_one, gen_sq hp]
  | k + 1 => by
    rw [zag_succ, mul_assoc, zag_mul_gen hp k, mul_smul_comm]

/-! ## Sliding one cup -/

theorem commute_zig_of {n p : ℕ} {Y : TLFin K δ n} :
    ∀ k, (∀ i, p ≤ i → i < p + k → Commute Y (gen δ n i)) → Commute Y (zig δ n p k)
  | 0, _ => Commute.one_right _
  | k + 1, h => (commute_zig_of k (fun i h1 h2 => h i h1 (by omega))).mul_right
      (h (p + k) (by omega) (by omega))

theorem commute_zag_of {n p : ℕ} {Y : TLFin K δ n} :
    ∀ k, (∀ i, p ≤ i → i < p + k → Commute Y (gen δ n i)) → Commute Y (zag δ n p k)
  | 0, _ => Commute.one_right _
  | k + 1, h => (h (p + k) (by omega) (by omega)).mul_right
      (commute_zag_of k (fun i h1 h2 => h i h1 (by omega)))

/-- **Sliding a cup across `m` strands.** If `Y` is an idempotent commuting with the generators
`e_p, …, e_{p+m}`, the cup at `p` and the cup at `p + m` give isomorphic corners of `Y`, with the
explicit partial isometries `Y · zig p (m+1)` and `δ⁻² Y · zag p (m+1)`. -/
theorem mvn_slide (hδ : δ ≠ 0) {n p m : ℕ} (h : p + m < n) {Y : TLFin K δ n} (hY : Y * Y = Y)
    (hc : ∀ i, p ≤ i → i ≤ p + m → Commute Y (gen δ n i)) :
    MvN (δ⁻¹ • (Y * gen δ n p)) (δ⁻¹ • (Y * gen δ n (p + m))) := by
  have cp : Commute Y (gen δ n p) := hc p le_rfl (by omega)
  have cq : Commute Y (gen δ n (p + m)) := hc _ (by omega) le_rfl
  have cz : Commute Y (zig δ n p (m + 1)) := commute_zig_of _ (fun i h1 h2 => hc i h1 (by omega))
  have cw : Commute Y (zag δ n p (m + 1)) := commute_zag_of _ (fun i h1 h2 => hc i h1 (by omega))
  have hm : ∀ u v : TLFin K δ n, Commute Y u → Y * u * (Y * v) = Y * (u * v) := by
    intro u v hu
    rw [mul_assoc, ← mul_assoc u, ← hu.eq, mul_assoc, ← mul_assoc Y, hY]
  have hp : p < n := by omega
  have one : ∀ (c : K) (x : TLFin K δ n), c = 1 → c • x = x := by rintro c x rfl; exact one_smul _ _
  refine ⟨?_, ?_, Y * zig δ n p (m + 1), δ⁻¹ ^ 2 • (Y * zag δ n p (m + 1)), ?_, ?_, ?_, ?_⟩
  · simp only [smul_mul_assoc, mul_smul_comm, smul_smul]
    rw [hm _ _ cp, gen_sq hp, mul_smul_comm, smul_smul]
    congr 1; field_simp
  · simp only [smul_mul_assoc, mul_smul_comm, smul_smul]
    rw [hm _ _ cq, gen_sq h, mul_smul_comm, smul_smul]
    congr 1; field_simp
  · simp only [smul_mul_assoc, mul_smul_comm, smul_smul]
    rw [hm _ _ cp, hm _ _ (cp.mul_right cz), gen_mul_zig hp, smul_mul_assoc, zig_mul_gen h,
      mul_smul_comm, mul_smul_comm, smul_smul, smul_smul]
    exact one _ _ (by field_simp)
  · simp only [smul_mul_assoc, mul_smul_comm, smul_smul]
    rw [hm _ _ cq, hm _ _ (cq.mul_right cw), gen_mul_zag h, smul_mul_assoc, zag_mul_gen hp,
      mul_smul_comm, mul_smul_comm, smul_smul, smul_smul]
    congr 1; field_simp
  · simp only [mul_smul_comm]
    rw [hm _ _ cz, zig_mul_zag_succ h, mul_smul_comm, smul_smul]
    congr 1; field_simp
  · simp only [smul_mul_assoc]
    rw [hm _ _ cw, zag_mul_zig _ h, mul_smul_comm, smul_smul]
    congr 1; field_simp

/-! ## Splitting and the shift-by-two intertwining -/

theorem zig_add (n p a : ℕ) : ∀ b, zig δ n p (a + b) = zig δ n p a * zig δ n (p + a) b
  | 0 => by rw [add_zero, zig, mul_one]
  | b + 1 => by rw [← add_assoc, zig_succ, zig_add n p a b, zig_succ, mul_assoc, add_assoc]

theorem zag_add (n p a : ℕ) : ∀ b, zag δ n p (a + b) = zag δ n (p + a) b * zag δ n p a
  | 0 => by rw [add_zero, zag, one_mul]
  | b + 1 => by rw [← add_assoc, zag_succ, zag_add n p a b, zag_succ, mul_assoc, add_assoc]

/-- **A full slide intertwines the shift by two strands.** Inside the support of
`zig p (k+1) = e_p ⋯ e_{p+k}`, `e_{i+2} · zig = zig · e_i`. -/
theorem gen_shift_zig {n p k i : ℕ} (hpi : p ≤ i) (hik : i + 2 ≤ p + k) (hn : p + k < n) :
    gen δ n (i + 2) * zig δ n p (k + 1) = zig δ n p (k + 1) * gen δ n i := by
  have hk : k + 1 = (i - p) + 3 + (k + 1 - (i - p) - 3) := by omega
  set r := k + 1 - (i - p) - 3
  rw [hk, zig_add, zig_add n p (i - p) 3, show p + (i - p) = i by omega,
    show p + (i - p + 3) = i + 3 by omega]
  have hz : zig δ n i 3 = gen δ n i * (gen δ n (i + 1) * gen δ n (i + 2)) := by
    simp [zig, one_mul, mul_assoc]
  have hA : Commute (gen δ n (i + 2)) (zig δ n p (i - p)) := commute_zig _ (by omega)
  have hB : Commute (gen δ n i) (zig δ n (i + 3) r) := commute_zig _ (by omega)
  have hC : Commute (gen δ n i) (gen δ n (i + 2)) := commute_gen (by omega)
  have h1 : gen δ n (i + 2) * gen δ n (i + 1) * gen δ n (i + 2) = gen δ n (i + 2) :=
    gen_adj_down (δ := δ) (show i + 1 + 1 < n by omega)
  have h2 := gen_adj_up (δ := δ) (show i + 1 < n by omega)
  have key : gen δ n (i + 2) * gen δ n i * gen δ n (i + 1) * gen δ n (i + 2) =
      gen δ n i * gen δ n (i + 1) * gen δ n (i + 2) * gen δ n i := by
    rw [← hC.eq, mul_assoc, mul_assoc, ← mul_assoc (gen δ n (i + 2)), h1, mul_assoc _ _ (gen δ n i),
      ← hC.eq, ← mul_assoc, h2]
  rw [hz]
  simp only [mul_assoc]
  rw [← mul_assoc (gen δ n (i + 2)) (zig δ n p (i - p)), hA.eq, mul_assoc, ← hB.eq]
  congr 1
  simp only [← mul_assoc]
  rw [key]

/-- The same for the reversed word: `zag · e_{i+2} = e_i · zag`. -/
theorem zag_shift_gen {n p k i : ℕ} (hpi : p ≤ i) (hik : i + 2 ≤ p + k) (hn : p + k < n) :
    zag δ n p (k + 1) * gen δ n (i + 2) = gen δ n i * zag δ n p (k + 1) := by
  have hk : k + 1 = (i - p) + 3 + (k + 1 - (i - p) - 3) := by omega
  set r := k + 1 - (i - p) - 3
  rw [hk, zag_add, zag_add n p (i - p) 3, show p + (i - p) = i by omega,
    show p + (i - p + 3) = i + 3 by omega]
  have hz : zag δ n i 3 = gen δ n (i + 2) * (gen δ n (i + 1) * gen δ n i) := by
    simp [zag, mul_one]
  have hA : Commute (gen δ n (i + 2)) (zag δ n p (i - p)) := commute_zag _ (by omega)
  have hB : Commute (gen δ n i) (zag δ n (i + 3) r) := commute_zag _ (by omega)
  have hC : Commute (gen δ n i) (gen δ n (i + 2)) := commute_gen (by omega)
  have h1 : gen δ n (i + 2) * gen δ n (i + 1) * gen δ n (i + 2) = gen δ n (i + 2) :=
    gen_adj_down (δ := δ) (show i + 1 + 1 < n by omega)
  have h2 := gen_adj_up (δ := δ) (show i + 1 < n by omega)
  have kL : gen δ n (i + 2) * gen δ n (i + 1) * gen δ n i * gen δ n (i + 2) =
      gen δ n i * gen δ n (i + 2) := by
    rw [mul_assoc _ (gen δ n i), hC.eq, ← mul_assoc, h1]
  have kR : gen δ n i * gen δ n (i + 2) * gen δ n (i + 1) * gen δ n i =
      gen δ n i * gen δ n (i + 2) := by
    rw [hC.eq, mul_assoc (gen δ n (i + 2)) (gen δ n i), mul_assoc (gen δ n (i + 2)), h2]
  rw [hz]
  simp only [mul_assoc]
  rw [hA.symm.eq, ← mul_assoc (gen δ n i) (zag δ n (i + 3) r), hB.eq]
  simp only [mul_assoc]
  congr 1
  simp only [← mul_assoc]
  rw [kL, kR]

/-! ## Sliding a placed block through a zigzag -/

section Place

open QOU.HeckeTemperleyLieb.TLCableBraiding

theorem gen_eq_E (n i : ℕ) : gen δ n i = E δ n i := rfl

/-- Two algebra maps out of `TL_m` intertwine with `Z` once they do so on generators. -/
theorem intertwine {m N : ℕ} (f g : TLFin K δ m →ₐ[K] TLFin K δ N) (Z : TLFin K δ N)
    (h : ∀ i, f (e K δ adjFin i) * Z = Z * g (e K δ adjFin i)) (x : TLFin K δ m) :
    f x * Z = Z * g x := by
  induction mem_adjoin_e x using Algebra.adjoin_induction with
  | mem y hy => obtain ⟨j, rfl⟩ := hy; exact h j
  | algebraMap r =>
    rw [AlgHom.commutes, AlgHom.commutes, Algebra.algebraMap_eq_smul_one, smul_mul_assoc,
      one_mul, mul_smul_comm, mul_one]
  | add y z _ _ hy hz => rw [map_add, map_add, add_mul, mul_add, hy, hz]
  | mul y z _ _ hy hz => rw [map_mul, map_mul, mul_assoc, hz, ← mul_assoc, hy, mul_assoc]

/-- **Full slide.** A block placed on strands `[t+2, t+2+M]`, pushed through the zigzag
`zig p (k+1)` that spans it, lands on `[t, t+M]`. -/
theorem pl_shift_zig {N t M p k : ℕ} (h2 : t + 2 + M ≤ N) (h0 : t + M ≤ N) (hp : p ≤ t)
    (hk : t + M + 1 ≤ p + k) (hn : p + k < N) (x : TLFin K δ M) :
    pl δ (t + 2) M h2 x * zig δ N p (k + 1) = zig δ N p (k + 1) * pl δ t M h0 x := by
  refine intertwine _ _ _ (fun j => ?_) x
  rw [pl_e, pl_e, ← gen_eq_E, ← gen_eq_E, show t + 2 + (j : ℕ) = t + j + 2 by omega]
  exact gen_shift_zig (by omega) (by omega) hn

/-- The same slide read backwards, through `zag`. -/
theorem pl_shift_zag {N t M p k : ℕ} (h2 : t + 2 + M ≤ N) (h0 : t + M ≤ N) (hp : p ≤ t)
    (hk : t + M + 1 ≤ p + k) (hn : p + k < N) (x : TLFin K δ M) :
    zag δ N p (k + 1) * pl δ (t + 2) M h2 x = pl δ t M h0 x * zag δ N p (k + 1) := by
  refine (intertwine _ _ _ (fun j => ?_) x).symm
  rw [pl_e, pl_e, ← gen_eq_E, ← gen_eq_E, show t + 2 + (j : ℕ) = t + j + 2 by omega]
  exact (zag_shift_gen (by omega) (by omega) hn).symm

/-- A placed block commutes with a zigzag on strands two or more steps away. -/
theorem commute_pl_zig {N t M p k : ℕ} (h0 : t + M ≤ N) (h : t + M + 1 ≤ p ∨ p + k + 1 ≤ t)
    (x : TLFin K δ M) : Commute (pl δ t M h0 x) (zig δ N p k) :=
  intertwine _ _ _ (fun j => by
    rw [pl_e, ← gen_eq_E]; exact (commute_zig k (by omega)).eq) x

theorem commute_pl_zag {N t M p k : ℕ} (h0 : t + M ≤ N) (h : t + M + 1 ≤ p ∨ p + k + 1 ≤ t)
    (x : TLFin K δ M) : Commute (pl δ t M h0 x) (zag δ N p k) :=
  intertwine _ _ _ (fun j => by
    rw [pl_e, ← gen_eq_E]; exact (commute_zag k (by omega)).eq) x

/-- Two algebra maps out of `TL_m` that agree on generators agree. -/
theorem algHom_eq_of_gen {m N : ℕ} (f g : TLFin K δ m →ₐ[K] TLFin K δ N)
    (h : ∀ i, f (e K δ adjFin i) = g (e K δ adjFin i)) (x : TLFin K δ m) : f x = g x := by
  simpa using intertwine f g 1 (fun i => by rw [mul_one, one_mul, h i]) x

theorem pl_incl {N t M : ℕ} (h : t + (M + 1) ≤ N) (x : TLFin K δ M) :
    pl δ t (M + 1) h (incl δ M x) = pl δ t M (by omega) x :=
  algHom_eq_of_gen ((pl δ t (M + 1) h).comp (incl δ M)) (pl δ t M (by omega)) (fun i => by
    rw [AlgHom.comp_apply, incl_e, pl_e, pl_e]; rfl) x

/-- **A cup slides through a placed block.** In `TL_N` with `N = n + m + 3`: the cup that
`capEmb` puts after `x`, followed by the block `y`, pushed through `zig (n+1) (m+2)`, comes out as
the block `y` moved two strands left, with no cup between `x` and `y`. -/
theorem cup_slide_block (hδ : δ ≠ 0) {N n m : ℕ} (hN : n + m + 3 = N) (x : TLFin K δ n) (y : TLFin K δ m) :
    pl δ 0 (n + 1 + 1) (by omega) (capEmb δ n x) * pl δ (n + 3) m (by omega) y *
        zig δ N (n + 1) (m + 2) =
      zig δ N (n + 1) (m + 2) * (pl δ 0 n (by omega) x * pl δ (n + 1) m (by omega) y) := by
  have hE : pl δ 0 (n + 1 + 1) (N := N) (by omega) (e K δ adjFin (Fin.last (n + 1))) = gen δ N (n + 1) := by
    rw [pl_e, gen_eq_E]; simp
  have hx : pl δ 0 (n + 1 + 1) (N := N) (by omega) (incl δ (n + 1) (incl δ n x)) = pl δ 0 n (N := N) (by omega) x := by
    rw [pl_incl, pl_incl]
  have hs := pl_shift_zig (δ := δ) (N := N) (t := n + 1) (M := m) (p := n + 1) (k := m + 1)
    (by omega) (by omega) le_rfl (by omega) (by omega) y
  have hc := commute_pl_zig (δ := δ) (N := N) (t := 0) (M := n) (p := n + 1) (k := m + 2)
    (by omega) (Or.inl (by omega)) x
  rw [capEmb, map_smul, map_mul, hx, hE, smul_mul_assoc, smul_mul_assoc, mul_assoc, mul_assoc,
    hs, ← mul_assoc (gen δ N (n + 1)), gen_mul_zig (by omega), smul_mul_assoc, mul_smul_comm,
    smul_smul, inv_mul_cancel₀ hδ, one_smul, ← mul_assoc, hc.eq, mul_assoc]

end Place

end QOU.HeckeTemperleyLieb.TLZigzag
