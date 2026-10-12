import QOU.Archimedean.RossoJonesGeneral

/-!
# Middle weight traces of `γ^p`, for `gcd(n + 1, p) = 1`

This file proves `MiddleWeightTraces q n p` (from `RossoJonesGeneral`) whenever
`Nat.Coprime (n + 1) p` and `q ≠ 0`. That discharges the hypothesis of `rossoJones_of_middle` and
`markov_rossoJones_of_middle`, so the Rosso–Jones formula holds unconditionally for the torus
knots `T(r, s)` with `gcd(r, s) = 1` (`r = n + 1`, `s = p`).

The route has three steps, all over a generic field `R`:

1. **An explicit matrix for `γ`** (`gam_eq_G`). The letter on the last site is carried to the
   front. A carried `1` may instead be set down at a zero, which is then carried on.
2. **Three identities.** Write `E` for the `U_q(sl₂)` raising operator `Em`, `ρ, ρ'` for two
   weighted rotations, and `K` for `Km`. Then
   `γ = ρ + E K` (`gam_eq_rho_add`), `ρ E = E ρ'` (`rho_mul_Em`) and `K E = γ − ρ'`
   (`Km_mul_Em`).
3. **Telescoping.** In any ring these give `γ^p = ρ^p + E K_p` with `K_p E = γ^p − ρ'^p`
   (`pow_decomp`). `E` raises the weight by one, so
   `T_{m+1}(γ^p) = T_{m+1}(ρ^p) + T_m(γ^p) − T_m(ρ'^p)` (`T_gam_succ`). A weighted rotation's
   `p`-th power has a nonzero diagonal entry only on states fixed by `rot^p`. When `gcd(n+1, p) = 1`
   those states are constant, so they have weight `0` or `n + 1`. Hence every middle trace of
   `ρ^p, ρ'^p` vanishes, and induction from `T_0` gives `T_m(γ^p) = q^{np} − q^{(n−2)p}`
   (`T_gam_mid`).

The non-coprime case `gcd(n + 1, p) > 1` (torus *links*) is not covered here.
-/

namespace QOU.Archimedean.RossoJonesGeneral

open QOU.IwahoriHecke.TensorMarkovModel QOU.IwahoriHecke.JonesNormalForm
open QOU.IwahoriHecke.TensorEmbed QOU.IwahoriHecke.RMatrix QOU.IwahoriHecke.MarkovPeel

variable {R : Type*} [Field R]

/-! ## Letter weights -/

/-- `q` on a zero, `1` on a one. -/
def qz (q : R) (x : Fin 2) : R := if x = 0 then q else 1

/-- `q` on a one, `1` on a zero. -/
def qo (q : R) (x : Fin 2) : R := if x = 1 then q else 1

/-- The `K⁻¹` weight: `q⁻¹` on a zero, `q` on a one. -/
noncomputable def ki (q : R) (x : Fin 2) : R := if x = 0 then q⁻¹ else q

/-- The weight of the split term of `γ`: ones to the right of `j` and zeros to its left. -/
def cJ {n : ℕ} (q : R) (j : Fin n) (c : Fin n → Fin 2) (i : Fin n) : R :=
  if j < i then qo q (c i) else if i < j then qz q (c i) else 1

/-! ## The explicit column of `γ` -/

/-- **The explicit matrix of `γ` on `V^{⊗(n+1)}`.** Writing a column state as `c · x` (`x` the
last site), `γ` carries the letter `x` from the last site to the first. A carried `0` passes every
letter, picking up `q` per zero it passes. A carried `1` either passes every letter (`q` per one
passed) or is set down at the first zero `c j` it meets and that zero is carried on instead,
with weight `(q − q⁻¹) · q^{#ones right of j + #zeros left of j}`. -/
noncomputable def G (q : R) (n : ℕ) : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R :=
  Matrix.of fun a b =>
    if b (Fin.last n) = 0 then
      (if a = (Fin.cons 0 (Fin.init b) : Fin (n + 1) → Fin 2) then
        ∏ i, qz q (Fin.init b i) else 0)
    else
      (if a = (Fin.cons 1 (Fin.init b) : Fin (n + 1) → Fin 2) then
        ∏ i, qo q (Fin.init b i) else 0)
        + ∑ j : Fin n, if Fin.init b j = 0 then
            (if a = (Fin.cons 0 (Function.update (Fin.init b) j 1) : Fin (n + 1) → Fin 2) then
              (q - q⁻¹) * ∏ i, cJ q j (Fin.init b) i else 0) else 0

theorem G_snoc0 (q : R) {n : ℕ} (a : Fin (n + 1) → Fin 2) (c : Fin n → Fin 2) :
    G q n a (Fin.snoc c 0) =
      if a = (Fin.cons 0 c : Fin (n + 1) → Fin 2) then ∏ i, qz q (c i) else 0 := by
  simp [G, Fin.init_snoc, Fin.snoc_last]

theorem G_snoc1 (q : R) {n : ℕ} (a : Fin (n + 1) → Fin 2) (c : Fin n → Fin 2) :
    G q n a (Fin.snoc c 1) =
      (if a = (Fin.cons 1 c : Fin (n + 1) → Fin 2) then ∏ i, qo q (c i) else 0)
        + ∑ j : Fin n, if c j = 0 then
            (if a = (Fin.cons 0 (Function.update c j 1) : Fin (n + 1) → Fin 2) then
              (q - q⁻¹) * ∏ i, cJ q j c i else 0) else 0 := by
  simp [G, Fin.init_snoc, Fin.snoc_last]

/-! ## The recursion `γ_{n+1} = (γ_n ⊗ 1) · σ_n` -/

theorem gam_succ (q : R) (n : ℕ) :
    gam q (n + 1) = extendSiteHom (R := R) (m := n) (gam q n) * S q (n + 1) n := by
  rw [gam, cox, gam, extend_cox q n le_rfl]

/-- The diagonal coefficient of `Ř` on `(y, x)`. -/
noncomputable def dg (q : R) (y x : Fin 2) : R :=
  if y = x then q else if y < x then q - q⁻¹ else 0

theorem S_last_apply (q : R) {n : ℕ} (v : Fin (n + 2) → Fin 2) (c : Fin n → Fin 2)
    (y x : Fin 2) :
    S q (n + 1) n v (Fin.snoc (Fin.snoc c y) x)
      = (if v = Fin.snoc (Fin.snoc c y) x then dg q y x else 0)
        + (if y ≠ x ∧ v = Fin.snoc (Fin.snoc c x) y then 1 else 0) := by
  classical
  obtain ⟨c', y', x', rfl⟩ : ∃ c' y' x', v = Fin.snoc (Fin.snoc c' y') x' :=
    ⟨Fin.init (Fin.init v), Fin.init v (Fin.last n), v (Fin.last (n + 1)), by
      rw [Fin.snoc_init_self, Fin.snoc_init_self]⟩
  rw [S_of_lt q (Nat.lt_succ_self n), strandBraid, braidAt, embedPair_apply]
  have hI : ((⟨n, Nat.lt_succ_self n⟩ : Fin (n + 1)).castSucc : Fin (n + 2))
      = (Fin.last n).castSucc := rfl
  have hJ : ((⟨n, Nat.lt_succ_self n⟩ : Fin (n + 1)).succ : Fin (n + 2)) = Fin.last (n + 1) := by
    ext; simp
  rw [hI, hJ]
  simp only [Fin.snoc_last, Fin.snoc_castSucc]
  have hoff : (∀ k : Fin (n + 2), k ≠ (Fin.last n).castSucc → k ≠ Fin.last (n + 1) →
      (Fin.snoc (Fin.snoc c' y') x' : Fin (n + 2) → Fin 2) k
        = (Fin.snoc (Fin.snoc c y) x : Fin (n + 2) → Fin 2) k) ↔ c' = c := by
    constructor
    · intro h
      funext i
      have := h (i.castSucc.castSucc) (by simp [Fin.ext_iff]; omega)
        (by simp [Fin.ext_iff]; omega)
      simpa only [Fin.snoc_castSucc] using this
    · rintro rfl k hk1 hk2
      induction k using Fin.lastCases with
      | last => exact absurd rfl hk2
      | cast k =>
        induction k using Fin.lastCases with
        | last => exact absurd rfl hk1
        | cast i => simp only [Fin.snoc_castSucc]
  by_cases hc : c' = c
  · subst hc
    rw [if_pos (hoff.mpr rfl)]
    fin_cases y <;> fin_cases x <;> fin_cases y' <;> fin_cases x' <;> simp [dg, rCheck_apply]
  · rw [if_neg (fun h => hc (hoff.mp h))]
    simp [hc]

theorem extS_apply (q : R) {n : ℕ} (X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R)
    (a : Fin (n + 2) → Fin 2) (c : Fin n → Fin 2) (y x : Fin 2) :
    (extendSiteHom (R := R) (m := n) X * S q (n + 1) n) a (Fin.snoc (Fin.snoc c y) x)
      = (if a (Fin.last (n + 1)) = x then dg q y x * X (Fin.init a) (Fin.snoc c y) else 0)
        + (if y ≠ x ∧ a (Fin.last (n + 1)) = y then X (Fin.init a) (Fin.snoc c x) else 0) := by
  classical
  rw [Matrix.mul_apply]
  simp_rw [S_last_apply, mul_add, Finset.sum_add_distrib, mul_ite, mul_zero, mul_one]
  rw [Finset.sum_ite_eq' Finset.univ _ (fun v => extendSiteHom (R := R) (m := n) X a v * dg q y x)]
  simp only [ite_and]
  rw [Finset.sum_ite_irrel, Finset.sum_ite_eq' Finset.univ, Finset.sum_const_zero]
  simp only [Finset.mem_univ, if_true, extendSiteHom_apply, Fin.snoc_last]
  have h1 : (fun k : Fin (n + 1) => (Fin.snoc (Fin.snoc c y) x : Fin (n + 2) → Fin 2) k.castSucc)
      = Fin.snoc c y := by funext k; simp
  have h2 : (fun k : Fin (n + 1) => (Fin.snoc (Fin.snoc c x) y : Fin (n + 2) → Fin 2) k.castSucc)
      = Fin.snoc c x := by funext k; simp
  rw [h1, h2]
  congr 1
  · split_ifs <;> simp only [one_mul, zero_mul] <;> first | rfl | exact mul_comm _ _
  · split_ifs <;> simp only [one_mul, zero_mul] <;> rfl

theorem cJ_castSucc_prod (q : R) {n : ℕ} (j : Fin n) (c : Fin n → Fin 2) (y : Fin 2) :
    ∏ i : Fin (n + 1), cJ q j.castSucc (Fin.snoc c y) i = (∏ i, cJ q j c i) * qo q y := by
  rw [Fin.prod_univ_castSucc]
  congr 1
  · refine Finset.prod_congr rfl fun i _ => ?_
    simp [cJ, Fin.snoc_castSucc]
  · simp [cJ, Fin.snoc_last, Fin.castSucc_lt_last]

theorem cJ_last_prod (q : R) {n : ℕ} (c : Fin n → Fin 2) (y : Fin 2) :
    ∏ i : Fin (n + 1), cJ q (Fin.last n) (Fin.snoc c y) i = ∏ i, qz q (c i) := by
  rw [Fin.prod_univ_castSucc]
  simp only [cJ, Fin.snoc_castSucc, lt_self_iff_false, if_false, mul_one]
  refine Finset.prod_congr rfl fun i _ => ?_
  rw [if_neg (not_lt.mpr (Fin.le_last _)), if_pos (Fin.castSucc_lt_last i)]

theorem snoc_eq_cons_one (c : Fin 0 → Fin 2) (x : Fin 2) :
    (Fin.snoc c x : Fin 1 → Fin 2) = Fin.cons x c := by
  funext i; fin_cases i; rfl

theorem prod_snoc (f : Fin 2 → R) {n : ℕ} (c : Fin n → Fin 2) (y : Fin 2) :
    ∏ i : Fin (n + 1), f ((Fin.snoc c y : Fin (n + 1) → Fin 2) i) = (∏ i, f (c i)) * f y := by
  rw [Fin.prod_univ_castSucc]; simp

theorem cons_snoc' {n : ℕ} (b : Fin 2) (c : Fin n → Fin 2) (y : Fin 2) :
    (Fin.cons b (Fin.snoc c y : Fin (n + 1) → Fin 2) : Fin (n + 2) → Fin 2)
      = Fin.snoc (Fin.cons b c : Fin (n + 1) → Fin 2) y :=
  Fin.cons_snoc_eq_snoc_cons b c y

/-- **`γ` is the explicit carry matrix `G`**, for every number of sites. -/
theorem gam_eq_G (q : R) : ∀ n, gam q n = G q n
  | 0 => by
    ext a b
    obtain ⟨c, x, rfl⟩ : ∃ (c : Fin 0 → Fin 2) (x : Fin 2), b = Fin.snoc c x :=
      ⟨Fin.init b, b (Fin.last 0), (Fin.snoc_init_self b).symm⟩
    rw [gam, cox, snoc_eq_cons_one, Matrix.one_apply]
    fin_cases x
    · rw [show ((⟨0, by decide⟩ : Fin 2)) = 0 from rfl, ← snoc_eq_cons_one, G_snoc0,
        snoc_eq_cons_one]
      simp
    · rw [show ((⟨1, by decide⟩ : Fin 2)) = 1 from rfl, ← snoc_eq_cons_one, G_snoc1,
        snoc_eq_cons_one]
      simp
  | n + 1 => by
    classical
    ext a b
    obtain ⟨c, y, x, rfl⟩ : ∃ (c : Fin n → Fin 2) (y x : Fin 2),
        b = Fin.snoc (Fin.snoc c y) x :=
      ⟨Fin.init (Fin.init b), Fin.init b (Fin.last n), b (Fin.last (n + 1)), by
        rw [Fin.snoc_init_self, Fin.snoc_init_self]⟩
    obtain ⟨a', z, rfl⟩ : ∃ (a' : Fin (n + 1) → Fin 2) (z : Fin 2), a = Fin.snoc a' z :=
      ⟨Fin.init a, a (Fin.last (n + 1)), (Fin.snoc_init_self a).symm⟩
    rw [gam_succ, extS_apply, gam_eq_G q n]
    simp only [Fin.init_snoc, Fin.snoc_last]
    fin_cases y <;> fin_cases x <;> fin_cases z <;>
      simp only [show ((⟨0, by decide⟩ : Fin 2)) = 0 from rfl,
        show ((⟨1, by decide⟩ : Fin 2)) = 1 from rfl, G_snoc0, G_snoc1,
        Fin.sum_univ_castSucc, Fin.snoc_castSucc, Fin.snoc_last, ← Fin.snoc_update,
        Fin.update_snoc_last, cons_snoc', Fin.snoc_inj, cJ_castSucc_prod, cJ_last_prod,
        prod_snoc] <;>
      simp [dg, qz, qo, mul_add, Finset.mul_sum, mul_ite] <;> ring_nf

/-! ## Product identities for the letter weights -/

variable {q : R}

theorem prod_qz_mul_ki (hq : q ≠ 0) {n : ℕ} (c : Fin n → Fin 2) :
    (∏ i, qz q (c i)) * ∏ i, ki q (c i) = ∏ i, qo q (c i) := by
  rw [← Finset.prod_mul_distrib]
  refine Finset.prod_congr rfl fun i _ => ?_
  rcases Fin.exists_fin_two.mp ⟨c i, rfl⟩ with h | h <;> rw [h] <;> simp [qz, ki, qo, hq]

theorem prod_qz_mul_phi (hq : q ≠ 0) {n : ℕ} (c : Fin n → Fin 2) (j : Fin n) (hj : c j = 0) :
    (∏ i, qz q (c i)) * ∏ i, (if j < i then ki q (c i) else 1) = q * ∏ i, cJ q j c i := by
  classical
  rw [← Finset.prod_mul_distrib,
    ← Finset.mul_prod_erase Finset.univ
      (fun i => qz q (c i) * (if j < i then ki q (c i) else 1)) (Finset.mem_univ j),
    ← Finset.mul_prod_erase Finset.univ (cJ q j c) (Finset.mem_univ j)]
  have h1 : qz q (c j) * (if j < j then ki q (c j) else 1) = q := by simp [hj, qz]
  have h2 : cJ q j c j = 1 := by simp [cJ]
  rw [h1, h2, one_mul]
  refine congrArg (q * ·) (Finset.prod_congr rfl fun i hi => ?_)
  have hij : i ≠ j := Finset.ne_of_mem_erase hi
  rcases lt_trichotomy j i with h | h | h
  · simp only [cJ, if_pos h]
    rcases Fin.exists_fin_two.mp ⟨c i, rfl⟩ with h' | h' <;> rw [h'] <;> simp [qo, ki, qz, hq]
  · exact absurd h.symm hij
  · simp only [cJ, if_neg (not_lt.mpr h.le), if_pos h, mul_one]

theorem prod_update_one (f : Fin 2 → R) {n : ℕ} (c : Fin n → Fin 2) (j : Fin n) (hj : c j = 0) :
    (∏ i, f (Function.update c j 1 i)) * f 0 = (∏ i, f (c i)) * f 1 := by
  classical
  rw [← Finset.mul_prod_erase Finset.univ (fun i => f (Function.update c j 1 i))
      (Finset.mem_univ j),
    ← Finset.mul_prod_erase Finset.univ (fun i => f (c i)) (Finset.mem_univ j)]
  simp only [Function.update_self, hj]
  have : ∏ x ∈ Finset.univ.erase j, f (Function.update c j 1 x)
      = ∏ x ∈ Finset.univ.erase j, f (c x) :=
    Finset.prod_congr rfl fun i hi => by
      rw [Function.update_of_ne (Finset.ne_of_mem_erase hi)]
  rw [this]; ring

theorem prod_qz_update (hq : q ≠ 0) {n : ℕ} (c : Fin n → Fin 2) (j : Fin n) (hj : c j = 0) :
    ∏ i, qz q (Function.update c j 1 i) = (∏ i, qz q (c i)) * q⁻¹ := by
  have h := prod_update_one (qz q) c j hj
  rw [show qz q 0 = q by simp [qz], show qz q 1 = 1 by simp [qz], mul_one] at h
  rw [← h]; field_simp

theorem prod_qo_update {n : ℕ} (c : Fin n → Fin 2) (j : Fin n) (hj : c j = 0) :
    ∏ i, qo q (Function.update c j 1 i) = (∏ i, qo q (c i)) * q := by
  have h := prod_update_one (qo q) c j hj
  simpa [qo] using h

/-! ## The raising operator `E`, the lowering operator `K` and the two rotations -/

/-- The `K⁻¹`-string to the right of site `k`. -/
noncomputable def phi (q : R) {n : ℕ} (k : Fin (n + 1)) (b : Fin (n + 1) → Fin 2) : R :=
  ∏ l, if k < l then ki q (b l) else 1

/-- **The raising operator** `E = Σ_k e_k ⊗ K⁻¹ ⊗ ⋯ ⊗ K⁻¹` of `U_q(sl₂)` on `V^{⊗(n+1)}`. -/
noncomputable def Em (q : R) (n : ℕ) : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R :=
  Matrix.of fun a b => ∑ k, if b k = 0 then
    (if a = Function.update b k 1 then phi q k b else 0) else 0

/-- The weight of `K`: `(q − q⁻¹) q⁻¹ q^{#zeros}`. -/
noncomputable def lam (q : R) {n : ℕ} (c : Fin n → Fin 2) : R :=
  (q - q⁻¹) * q⁻¹ * ∏ i, qz q (c i)

/-- **The lowering operator `K`**: delete a final `1`, insert a `0` in front. -/
noncomputable def Km (q : R) (n : ℕ) : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R :=
  Matrix.of fun a b => if b (Fin.last n) = 1 then
    (if a = (Fin.cons 0 (Fin.init b) : Fin (n + 1) → Fin 2) then lam q (Fin.init b) else 0)
    else 0

/-- The cyclic rotation of a state: the last letter moves to the front. -/
def rot {n : ℕ} (b : Fin (n + 1) → Fin 2) : Fin (n + 1) → Fin 2 :=
  Fin.cons (b (Fin.last n)) (Fin.init b)

/-- The coefficient of the rotation `ρ`. -/
noncomputable def cRho (q : R) {n : ℕ} (c : Fin n → Fin 2) (x : Fin 2) : R :=
  if x = 0 then ∏ i, qz q (c i) else (∏ i, qo q (c i)) * q⁻¹ ^ 2

/-- The coefficient of the rotation `ρ'`. -/
noncomputable def cRho' (q : R) {n : ℕ} (c : Fin n → Fin 2) (x : Fin 2) : R :=
  if x = 0 then (∏ i, qz q (c i)) * q⁻¹ ^ 2 else ∏ i, qo q (c i)

/-- A weighted rotation: `M e_b = f(b) e_{rot b}`. -/
noncomputable def rotMat {n : ℕ} (f : (Fin (n + 1) → Fin 2) → R) :
    Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R :=
  Matrix.of fun a b => if a = rot b then f b else 0

/-- `ρ`: the weighted rotation with which `γ − ρ = E K`. -/
noncomputable def rho (q : R) (n : ℕ) : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R :=
  rotMat fun b => cRho q (Fin.init b) (b (Fin.last n))

/-- `ρ'`: the weighted rotation with which `ρ E = E ρ'` and `K E = γ − ρ'`. -/
noncomputable def rho' (q : R) (n : ℕ) : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R :=
  rotMat fun b => cRho' q (Fin.init b) (b (Fin.last n))

theorem rot_snoc {n : ℕ} (c : Fin n → Fin 2) (x : Fin 2) :
    rot (Fin.snoc c x : Fin (n + 1) → Fin 2) = Fin.cons x c := by
  simp [rot, Fin.init_snoc, Fin.snoc_last]

theorem phi_castSucc (q : R) {n : ℕ} (j : Fin n) (c : Fin n → Fin 2) (x : Fin 2) :
    phi q j.castSucc (Fin.snoc c x : Fin (n + 1) → Fin 2)
      = (∏ i, if j < i then ki q (c i) else 1) * ki q x := by
  rw [phi, Fin.prod_univ_castSucc]
  simp [Fin.snoc_castSucc, Fin.snoc_last, Fin.castSucc_lt_last]

theorem phi_last (q : R) {n : ℕ} (b : Fin (n + 1) → Fin 2) : phi q (Fin.last n) b = 1 := by
  rw [phi]
  exact Finset.prod_eq_one fun l _ => if_neg (not_lt.mpr (Fin.le_last l))

theorem phi_zero (q : R) {n : ℕ} (c : Fin n → Fin 2) (x : Fin 2) :
    phi q 0 (Fin.cons x c : Fin (n + 1) → Fin 2) = ∏ i, ki q (c i) := by
  rw [phi, Fin.prod_univ_succ]
  simp [Fin.succ_pos]

theorem phi_succ (q : R) {n : ℕ} (j : Fin n) (c : Fin n → Fin 2) (x : Fin 2) :
    phi q j.succ (Fin.cons x c : Fin (n + 1) → Fin 2)
      = ∏ i, if j < i then ki q (c i) else 1 := by
  rw [phi, Fin.prod_univ_succ]
  simp [Fin.succ_lt_succ_iff]

theorem Em_cons (q : R) {n : ℕ} (a : Fin (n + 1) → Fin 2) (c : Fin n → Fin 2) (x : Fin 2) :
    Em q n a (Fin.cons x c)
      = (if x = 0 then (if a = (Fin.cons 1 c : Fin (n + 1) → Fin 2) then ∏ i, ki q (c i) else 0)
          else 0)
        + ∑ j : Fin n, if c j = 0 then
            (if a = (Fin.cons x (Function.update c j 1) : Fin (n + 1) → Fin 2) then
              ∏ i, (if j < i then ki q (c i) else 1) else 0) else 0 := by
  simp only [Em, Matrix.of_apply]
  rw [Fin.sum_univ_succ]
  simp only [Fin.cons_zero, Fin.cons_succ, Fin.update_cons_zero, ← Fin.cons_update, phi_zero,
    phi_succ]

/-- `(X · E)` column by column: `E` raises one zero of the column state. -/
theorem mul_Em_apply (q : R) {n : ℕ} (X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R)
    (a b : Fin (n + 1) → Fin 2) :
    (X * Em q n) a b = ∑ k, if b k = 0 then X a (Function.update b k 1) * phi q k b else 0 := by
  classical
  rw [Matrix.mul_apply]
  simp only [Em, Matrix.of_apply, Finset.mul_sum]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun k _ => ?_
  by_cases hk : b k = 0
  · simp only [hk, if_true, mul_ite, mul_zero]
    rw [Finset.sum_ite_eq' Finset.univ, if_pos (Finset.mem_univ _)]
  · simp [hk]

theorem mul_Em_snoc (q : R) {n : ℕ} (X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R)
    (a : Fin (n + 1) → Fin 2) (c : Fin n → Fin 2) (x : Fin 2) :
    (X * Em q n) a (Fin.snoc c x)
      = (∑ j : Fin n, if c j = 0 then
            X a (Fin.snoc (Function.update c j 1) x)
              * ((∏ i, if j < i then ki q (c i) else 1) * ki q x) else 0)
        + (if x = 0 then X a (Fin.snoc c 1) else 0) := by
  rw [mul_Em_apply, Fin.sum_univ_castSucc]
  simp only [Fin.snoc_castSucc, Fin.snoc_last, ← Fin.snoc_update, Fin.update_snoc_last,
    phi_castSucc, phi_last, mul_one]

/-- A product with a weighted rotation on the right collapses. -/
theorem mul_rotMat_apply {n : ℕ} (X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R)
    (f : (Fin (n + 1) → Fin 2) → R) (a b : Fin (n + 1) → Fin 2) :
    (X * rotMat f) a b = X a (rot b) * f b := by
  classical
  rw [Matrix.mul_apply]
  simp only [rotMat, Matrix.of_apply, mul_ite, mul_zero]
  rw [Finset.sum_ite_eq' Finset.univ, if_pos (Finset.mem_univ _)]

theorem rotMat_apply {n : ℕ} (f : (Fin (n + 1) → Fin 2) → R) (a b : Fin (n + 1) → Fin 2) :
    rotMat f a b = if a = rot b then f b else 0 := rfl

/-! ## The three identities -/

/-- **`γ = ρ + E K`.** -/
theorem gam_eq_rho_add (hq : q ≠ 0) (n : ℕ) : gam q n = rho q n + Em q n * Km q n := by
  classical
  rw [gam_eq_G]
  ext a b
  obtain ⟨c, x, rfl⟩ : ∃ (c : Fin n → Fin 2) (x : Fin 2), b = Fin.snoc c x :=
    ⟨Fin.init b, b (Fin.last n), (Fin.snoc_init_self b).symm⟩
  have hK : (Em q n * Km q n) a (Fin.snoc c x)
      = if x = 1 then Em q n a (Fin.cons 0 c) * lam q c else 0 := by
    rw [Matrix.mul_apply]
    simp only [Km, Matrix.of_apply, Fin.snoc_last, Fin.init_snoc]
    split_ifs
    · simp only [mul_ite, mul_zero]
      rw [Finset.sum_ite_eq' Finset.univ, if_pos (Finset.mem_univ _)]
    · simp
  rw [Matrix.add_apply, hK]
  simp only [rho, rotMat_apply, rot_snoc, Fin.init_snoc, Fin.snoc_last]
  rcases Fin.exists_fin_two.mp ⟨x, rfl⟩ with rfl | rfl
  · simp [G_snoc0, cRho]
  · rw [G_snoc1, Em_cons]
    simp only [cRho, show (1 : Fin 2) ≠ 0 by decide, if_false, if_true, add_mul,
      Finset.sum_mul]
    rw [← add_assoc]
    congr 1
    · split_ifs
      · rw [lam, show ∏ i, qo q (c i) = (∏ i, qz q (c i)) * ∏ i, ki q (c i) from
          (prod_qz_mul_ki hq c).symm]
        field_simp; ring
      · simp
    · refine Finset.sum_congr rfl fun j _ => ?_
      split_ifs with h1 h2
      · rw [lam]
        have := prod_qz_mul_phi hq c j h1
        calc (q - q⁻¹) * ∏ i, cJ q j c i
            = (q - q⁻¹) * q⁻¹ * (q * ∏ i, cJ q j c i) := by field_simp
          _ = _ := by rw [← this]; ring
      · simp
      · simp

theorem rho_apply_snoc (q : R) {n : ℕ} (a : Fin (n + 1) → Fin 2) (c : Fin n → Fin 2) (x : Fin 2) :
    rho q n a (Fin.snoc c x)
      = if a = (Fin.cons x c : Fin (n + 1) → Fin 2) then cRho q c x else 0 := by
  simp [rho, rotMat_apply, rot_snoc, Fin.init_snoc, Fin.snoc_last]

theorem rho'_apply_snoc (q : R) {n : ℕ} (a : Fin (n + 1) → Fin 2) (c : Fin n → Fin 2)
    (x : Fin 2) :
    rho' q n a (Fin.snoc c x)
      = if a = (Fin.cons x c : Fin (n + 1) → Fin 2) then cRho' q c x else 0 := by
  simp [rho', rotMat_apply, rot_snoc, Fin.init_snoc, Fin.snoc_last]

theorem Km_apply_snoc (q : R) {n : ℕ} (a : Fin (n + 1) → Fin 2) (c : Fin n → Fin 2)
    (x : Fin 2) :
    Km q n a (Fin.snoc c x)
      = if x = 1 then (if a = (Fin.cons 0 c : Fin (n + 1) → Fin 2) then lam q c else 0)
        else 0 := by
  simp [Km, Fin.init_snoc, Fin.snoc_last]

/-- **`ρ E = E ρ'`.** -/
theorem rho_mul_Em (hq : q ≠ 0) (n : ℕ) : rho q n * Em q n = Em q n * rho' q n := by
  classical
  ext a b
  obtain ⟨c, x, rfl⟩ : ∃ (c : Fin n → Fin 2) (x : Fin 2), b = Fin.snoc c x :=
    ⟨Fin.init b, b (Fin.last n), (Fin.snoc_init_self b).symm⟩
  rw [mul_Em_snoc, rho', mul_rotMat_apply, rot_snoc, Fin.init_snoc, Fin.snoc_last, Em_cons,
    add_mul, Finset.sum_mul, add_comm (∑ j : Fin n, _)]
  simp only [rho_apply_snoc]
  rcases Fin.exists_fin_two.mp ⟨x, rfl⟩ with rfl | rfl
  · simp only [if_true]
    congr 1
    · split_ifs
      · rw [cRho, cRho', if_neg (by decide), if_pos rfl, ← prod_qz_mul_ki hq c]; ring
      · simp
    · refine Finset.sum_congr rfl fun j _ => ?_
      split_ifs with h1 h2
      · rw [cRho, cRho', if_pos rfl, if_pos rfl, prod_qz_update hq c j h1, ki, if_pos rfl]
        ring
      · simp
      · simp
  · simp only [show (1 : Fin 2) ≠ 0 by decide, if_false, zero_mul, add_zero, zero_add]
    refine Finset.sum_congr rfl fun j _ => ?_
    split_ifs with h1 h2
    · rw [cRho, cRho', if_neg (by decide), if_neg (by decide), prod_qo_update c j h1, ki,
        if_neg (by decide)]
      field_simp
    · simp
    · simp

/-- **`K E = γ − ρ'`.** -/
theorem Km_mul_Em (hq : q ≠ 0) (n : ℕ) : Km q n * Em q n = gam q n - rho' q n := by
  classical
  rw [gam_eq_G]
  ext a b
  obtain ⟨c, x, rfl⟩ : ∃ (c : Fin n → Fin 2) (x : Fin 2), b = Fin.snoc c x :=
    ⟨Fin.init b, b (Fin.last n), (Fin.snoc_init_self b).symm⟩
  rw [mul_Em_snoc, Matrix.sub_apply, rho'_apply_snoc]
  simp only [Km_apply_snoc]
  rcases Fin.exists_fin_two.mp ⟨x, rfl⟩ with rfl | rfl
  · simp only [show (0 : Fin 2) ≠ 1 by decide, if_false, zero_mul, if_true,
      Finset.sum_const_zero, ite_self, zero_add, G_snoc0]
    split_ifs
    · rw [lam, cRho', if_pos rfl]; field_simp
    · simp
  · simp only [if_true, show (1 : Fin 2) ≠ 0 by decide, if_false, add_zero, G_snoc1, cRho']
    rw [add_sub_cancel_left]
    refine Finset.sum_congr rfl fun j _ => ?_
    split_ifs with h1 h2
    · rw [lam, prod_qz_update hq c j h1, ki, if_neg (by decide)]
      have := prod_qz_mul_phi hq c j h1
      calc (q - q⁻¹) * q⁻¹ * ((∏ i, qz q (c i)) * q⁻¹)
            * ((∏ i, if j < i then ki q (c i) else 1) * q)
          = (q - q⁻¹) * q⁻¹ * ((∏ i, qz q (c i)) * ∏ i, (if j < i then ki q (c i) else 1)) := by
            field_simp
        _ = _ := by rw [this]; field_simp
    · simp
    · simp

/-! ## From the three identities to the weight-space recursion -/

/-- **The ring-level telescoping.** If `g = r + e k`, `r e = e r'` and `k e = g − r'` in any
ring, then for every `p` there is `k_p` with `g^p = r^p + e k_p` and `k_p e = g^p − r'^p`. -/
theorem pow_decomp {A : Type*} [Ring A] (g r r' e k : A) (h1 : g = r + e * k)
    (h3 : r * e = e * r') (h4 : k * e = g - r') :
    ∀ p : ℕ, ∃ kp : A, g ^ p = r ^ p + e * kp ∧ kp * e = g ^ p - r' ^ p := by
  have hge : g * e = e * g :=
    calc g * e = r * e + e * (k * e) := by rw [h1, add_mul, mul_assoc]
      _ = e * r' + e * (g - r') := by rw [h3, h4]
      _ = e * g := by noncomm_ring
  have hpe : ∀ p : ℕ, r ^ p * e = e * r' ^ p := by
    intro p
    induction p with
    | zero => simp
    | succ p ih => rw [pow_succ, mul_assoc, h3, ← mul_assoc, ih, mul_assoc, ← pow_succ]
  intro p
  induction p with
  | zero => exact ⟨0, by simp, by simp⟩
  | succ p ih =>
    obtain ⟨kp, hA, hB⟩ := ih
    refine ⟨k * r ^ p + g * kp, ?_, ?_⟩
    · rw [pow_succ', hA, mul_add, ← mul_assoc g e kp, hge, h1, pow_succ']
      noncomm_ring
    · rw [add_mul, mul_assoc, hpe, mul_assoc, hB, ← mul_assoc, h4, pow_succ', pow_succ']
      noncomm_ring

theorem T_add {n : ℕ} (X Y : Matrix (Fin n → Fin 2) (Fin n → Fin 2) R) (m : ℕ) :
    T (X + Y) m = T X m + T Y m := by
  simp [T, Finset.sum_add_distrib]

theorem T_sub {n : ℕ} (X Y : Matrix (Fin n → Fin 2) (Fin n → Fin 2) R) (m : ℕ) :
    T (X - Y) m = T X m - T Y m := by
  simp [T, Finset.sum_sub_distrib]

theorem ones_update {n : ℕ} (b : Fin n → Fin 2) (k : Fin n) (hk : b k = 0) :
    ones (Function.update b k 1) = ones b + 1 := by
  classical
  unfold ones
  have : Finset.univ.filter (fun l => Function.update b k 1 l = 1)
      = insert k (Finset.univ.filter (fun l => b l = 1)) := by
    ext l
    by_cases hl : l = k
    · subst hl; simp
    · simp [Function.update_of_ne hl, hl]
  rw [this, Finset.card_insert_of_notMem]
  simp [hk]

/-- `E` raises the weight by one. -/
theorem Em_weight (q : R) {n : ℕ} (a b : Fin (n + 1) → Fin 2) (h : Em q n a b ≠ 0) :
    ones a = ones b + 1 := by
  classical
  simp only [Em, Matrix.of_apply] at h
  obtain ⟨k, -, hk⟩ := Finset.exists_ne_zero_of_sum_ne_zero h
  by_cases hb : b k = 0
  · rw [if_pos hb] at hk
    by_cases ha : a = Function.update b k 1
    · rw [ha, ones_update b k hb]
    · rw [if_neg ha] at hk; exact absurd rfl hk
  · rw [if_neg hb] at hk; exact absurd rfl hk

/-- **The weight-space trace moves across `E`.** -/
theorem T_Em_mul (q : R) {n : ℕ} (X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R)
    (m : ℕ) : T (Em q n * X) (m + 1) = T (X * Em q n) m := by
  classical
  have key : ∀ a v : Fin (n + 1) → Fin 2,
      (if ones a = m + 1 then Em q n a v * X v a else 0)
        = (if ones v = m then Em q n a v * X v a else 0) := by
    intro a v
    by_cases hE : Em q n a v = 0
    · simp [hE]
    · have hw := Em_weight q a v hE
      by_cases hv : ones v = m
      · rw [if_pos hv, if_pos (by omega)]
      · rw [if_neg hv, if_neg (by omega)]
  unfold T
  rw [Finset.sum_filter, Finset.sum_filter]
  simp only [Matrix.mul_apply]
  have hL : ∀ a : Fin (n + 1) → Fin 2,
      (if ones a = m + 1 then ∑ v, Em q n a v * X v a else 0)
        = ∑ v, (if ones a = m + 1 then Em q n a v * X v a else 0) := by
    intro a; split_ifs <;> simp
  have hR : ∀ v : Fin (n + 1) → Fin 2,
      (if ones v = m then ∑ a, X v a * Em q n a v else 0)
        = ∑ a, (if ones v = m then Em q n a v * X v a else 0) := by
    intro v; split_ifs <;> simp [mul_comm]
  simp only [hL, hR, key]
  exact Finset.sum_comm

/-! ## Weighted rotations -/

theorem rot_apply {n : ℕ} (b : Fin (n + 1) → Fin 2) (i : Fin (n + 1)) : rot b i = b (i - 1) := by
  induction i using Fin.cases with
  | zero =>
    have h : (0 : Fin (n + 1)) - 1 = Fin.last n := by
      ext; rw [Fin.coe_sub_one, if_pos rfl]; simp
    rw [h]; rfl
  | succ j =>
    have h : j.succ - 1 = j.castSucc := by
      ext; rw [Fin.coe_sub_one, if_neg (Fin.succ_ne_zero j)]; simp
    rw [h]; rfl

theorem val_nsmul_one {n : ℕ} (k : ℕ) : ((k • (1 : Fin (n + 1)) : Fin (n + 1)) : ℕ) = k % (n + 1) := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [succ_nsmul, Fin.val_add, ih, Fin.val_one', Nat.add_mod_mod, Nat.mod_add_mod]

theorem rot_iterate {n : ℕ} (b : Fin (n + 1) → Fin 2) (k : ℕ) :
    rot^[k] b = fun i => b (i - k • (1 : Fin (n + 1))) := by
  induction k with
  | zero => funext i; simp
  | succ k ih =>
    funext i
    rw [Function.iterate_succ_apply', rot_apply, ih]
    show b (i - 1 - k • (1 : Fin (n + 1))) = _
    rw [succ_nsmul, sub_sub, add_comm (1 : Fin (n + 1))]

theorem const_of_rot_fixed {n : ℕ} {p : ℕ} (hcop : Nat.Coprime (n + 1) p) (hn : 0 < n)
    (b : Fin (n + 1) → Fin 2) (hb : rot^[p] b = b) : ∀ i, b i = b 0 := by
  have hp : ∀ i, b (i - p • (1 : Fin (n + 1))) = b i := fun i => by
    have := congrFun hb i; rwa [rot_iterate] at this
  obtain ⟨m, hm⟩ := Nat.exists_mul_emod_eq_one_of_coprime hcop.symm (by omega : 1 < n + 1)
  have hpm : ∀ t : ℕ, ∀ i, b (i - (p * t) • (1 : Fin (n + 1))) = b i := by
    intro t
    induction t with
    | zero => intro i; simp
    | succ t ih =>
      intro i
      rw [mul_add, mul_one, add_nsmul, ← sub_sub, hp, ih]
  have h1 : (p * m) • (1 : Fin (n + 1)) = 1 := by
    apply Fin.ext
    rw [val_nsmul_one, hm, Fin.val_one', Nat.mod_eq_of_lt (by omega)]
  have hstep : ∀ i, b (i - 1) = b i := fun i => by
    have := hpm m i; rwa [h1] at this
  have hnat : ∀ t : ℕ, b (t • (1 : Fin (n + 1))) = b 0 := by
    intro t
    induction t with
    | zero => simp
    | succ t ih =>
      rw [← hstep, ← ih, succ_nsmul, add_sub_cancel_right]
  intro i
  have hi : (i : ℕ) • (1 : Fin (n + 1)) = i := by
    apply Fin.ext; rw [val_nsmul_one, Nat.mod_eq_of_lt i.isLt]
  rw [← hi]
  exact hnat _

theorem ones_mid_not_rot_fixed {n p m : ℕ} (hcop : Nat.Coprime (n + 1) p)
    (hm0 : 0 < m) (hm : m < n + 1) (b : Fin (n + 1) → Fin 2) (hbm : ones b = m) :
    rot^[p] b ≠ b := by
  intro hb
  have hn : 0 < n := by omega
  have hc := const_of_rot_fixed hcop hn b hb
  rcases Fin.exists_fin_two.mp ⟨b 0, rfl⟩ with h0 | h0
  · have : b = fun _ => 0 := funext fun i => by rw [hc i, h0]
    have := (ones_eq_zero_iff b).mpr this
    omega
  · have : b = fun _ => 1 := funext fun i => by rw [hc i, h0]
    have := (ones_eq_top_iff b).mpr this
    omega

theorem rotMat_pow_apply {n : ℕ} (f : (Fin (n + 1) → Fin 2) → R) (p : ℕ)
    (a b : Fin (n + 1) → Fin 2) :
    (rotMat f ^ p) a b
      = if a = rot^[p] b then ∏ k ∈ Finset.range p, f (rot^[k] b) else 0 := by
  induction p generalizing b with
  | zero => simp [Matrix.one_apply]
  | succ p ih =>
    rw [pow_succ, mul_rotMat_apply, ih, Function.iterate_succ_apply, Finset.prod_range_succ']
    simp only [Function.iterate_succ_apply, Function.iterate_zero, id]
    split_ifs <;> ring

theorem T_rotMat_pow_mid {n p m : ℕ} (f : (Fin (n + 1) → Fin 2) → R)
    (hcop : Nat.Coprime (n + 1) p) (hm0 : 0 < m) (hm : m < n + 1) :
    T (rotMat f ^ p) m = 0 := by
  unfold T
  refine Finset.sum_eq_zero fun b hb => ?_
  rw [rotMat_pow_apply, if_neg]
  intro h
  exact ones_mid_not_rot_fixed hcop hm0 hm b (Finset.mem_filter.mp hb).2 h.symm

theorem rot_const {n : ℕ} (c : Fin 2) : rot (fun _ : Fin (n + 1) => c) = fun _ => c := by
  funext i; rw [rot_apply]

theorem T_rotMat_pow_zero {n : ℕ} (f : (Fin (n + 1) → Fin 2) → R) (p : ℕ) :
    T (rotMat f ^ p) 0 = f (fun _ => 0) ^ p := by
  classical
  have hfix : ∀ k, rot^[k] (fun _ : Fin (n + 1) => (0 : Fin 2)) = fun _ => 0 :=
    fun k => Function.iterate_fixed (rot_const 0) k
  rw [T, Finset.sum_eq_single (fun _ => 0)]
  · rw [rotMat_pow_apply, if_pos (hfix p).symm]
    simp [hfix]
  · intro u hu hne
    exact absurd ((ones_eq_zero_iff u).mp (Finset.mem_filter.mp hu).2) hne
  · intro h; exact absurd (Finset.mem_filter.mpr ⟨Finset.mem_univ _, by
      rw [ones_eq_zero_iff]⟩) h

/-! ## The weight-space traces -/

/-- **The weight-space recursion**, for every `p`:
`T_{m+1}(γ^p) = T_{m+1}(ρ^p) + T_m(γ^p) − T_m(ρ'^p)`. -/
theorem T_gam_succ (hq : q ≠ 0) (n p m : ℕ) :
    T (gam q n ^ p) (m + 1)
      = T (rho q n ^ p) (m + 1) + T (gam q n ^ p) m - T (rho' q n ^ p) m := by
  obtain ⟨kp, hA, hB⟩ := pow_decomp (gam q n) (rho q n) (rho' q n) (Em q n) (Km q n)
    (gam_eq_rho_add hq n) (rho_mul_Em hq n) (Km_mul_Em hq n) p
  conv_lhs => rw [hA]
  rw [T_add, T_Em_mul, hB, T_sub]
  ring

/-- **Every middle weight space carries the same trace**, for `p` coprime to `n + 1`. -/
theorem T_gam_mid (hq : q ≠ 0) (n p : ℕ) (hcop : Nat.Coprime (n + 1) p) :
    ∀ m, 0 < m → m < n + 1 → T (gam q n ^ p) m = q ^ (n * p) - (q ^ n * q⁻¹ ^ 2) ^ p := by
  have hρ' : ∀ m, 0 < m → m < n + 1 → T (rho' q n ^ p) m = 0 :=
    fun m h0 h1 => T_rotMat_pow_mid _ hcop h0 h1
  have hρ : ∀ m, 0 < m → m < n + 1 → T (rho q n ^ p) m = 0 :=
    fun m h0 h1 => T_rotMat_pow_mid _ hcop h0 h1
  intro m hm0 hm1
  induction m with
  | zero => omega
  | succ m ih =>
    rw [T_gam_succ hq, hρ _ (by omega) hm1]
    rcases Nat.eq_zero_or_pos m with rfl | hm
    · rw [T_zero, rho', T_rotMat_pow_zero]
      simp [cRho', Fin.init, qz]
    · rw [ih hm (by omega), hρ' m hm (by omega)]
      ring

/-- **`MiddleWeightTraces` holds whenever `gcd(n + 1, p) = 1`** (`q ≠ 0`). -/
theorem middleWeightTraces_of_coprime (hq : q ≠ 0) (n p : ℕ) (hcop : Nat.Coprime (n + 1) p) :
    MiddleWeightTraces q n p := by
  intro m hm0 hm1
  rw [T_gam_mid hq n p hcop m hm0 hm1, mul_pow, ← pow_mul, ← pow_mul]
  have h2 : q ^ (2 * p) * q⁻¹ ^ (2 * p) = 1 := by
    rw [← mul_pow, mul_inv_cancel₀ hq, one_pow]
  calc q ^ (2 * p) * (q ^ (n * p) - q ^ (n * p) * q⁻¹ ^ (2 * p))
      = q ^ (2 * p) * q ^ (n * p) - q ^ (n * p) * (q ^ (2 * p) * q⁻¹ ^ (2 * p)) := by ring
    _ = q ^ (p * (n + 2)) - q ^ (p * n) := by
      rw [h2, mul_one, ← pow_add, mul_comm n p, show 2 * p + p * n = p * (n + 2) by ring]

/-- **Rosso–Jones on `V^{⊗(n+1)}`, unconditionally, for `gcd(n + 1, p) = 1`.** -/
theorem rossoJones_of_coprime (hq : q ≠ 0) (n p : ℕ) (hcop : Nat.Coprime (n + 1) p) :
    q ^ (2 * p) * Matrix.trace (W q (n + 1) * gam q n ^ p)
      = (∑ m ∈ Finset.range (n + 2), (q ^ 2) ^ m) * q ^ (p * (n + 2))
        - (∑ m ∈ Finset.Ioo 0 (n + 1), (q ^ 2) ^ m) * q ^ (p * n) :=
  rossoJones_of_middle q n p (middleWeightTraces_of_coprime hq n p hcop)

/-- **Rosso–Jones for every Markov trace with `z_D`, for `gcd(r, s) = 1`** (`r = n + 1`
strands, `s = p`). -/
theorem markov_rossoJones (hq : q ≠ 0) (hq1 : q ^ 2 + 1 ≠ 0)
    {B : Type*} [Ring B] [Algebra R B] {N : ℕ} {s : ℕ → B}
    (hs : HeckeFamily N (q - q⁻¹) 1 s) (t : B →ₗ[R] R) (ht1 : t 1 = 1)
    (hcyc : ∀ x y : B, t (x * y) = t (y * x))
    (hmark : ∀ k, k < N → ∀ x ∈ Algebra.adjoin R (s '' Set.Iio k), t (x * s k) = zD q * t x)
    {n : ℕ} (hn : n ≤ N) (p : ℕ) (hcop : Nat.Coprime (n + 1) p) :
    q ^ (2 * p) * (q ^ 2 + 1) ^ (n + 1) * t (cox s n ^ p)
      = (∑ m ∈ Finset.range (n + 2), (q ^ 2) ^ m) * q ^ (p * (n + 2))
        - (∑ m ∈ Finset.Ioo 0 (n + 1), (q ^ 2) ^ m) * q ^ (p * n) :=
  markov_rossoJones_of_middle hq hq1 hs t ht1 hcyc hmark hn p
    (middleWeightTraces_of_coprime hq n p hcop)

end QOU.Archimedean.RossoJonesGeneral
