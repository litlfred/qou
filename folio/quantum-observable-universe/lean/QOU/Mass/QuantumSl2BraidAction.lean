import QOU.Mass.QuantumSl2Hexagon
import QOU.IwahoriHecke.BraidGroup

/-!
# The braid group action of `Ř` on `V_{d+1}^{⊗(m+1)}`

Stage 2 of issue #8894. `QuantumSl2Hexagon.rCheck_braid` gives the braid relation for the
`U_q(sl₂)` braiding `Ř` on `V ⊗ V ⊗ V` with `V = V_{d+1}`, for every `d`. Here that is turned
into a homomorphism from the braid group on `m+1` strands,

    braidRep : B_{m+1} → GL(V^{⊗(m+1)}),   σ_a ↦ Ř acting on factors a, a+1,

for every `m` and every `d`.

`V^{⊗(m+1)}` is modelled by its monomial basis `Fin (m+1) → ι` with `ι = Fin (d+1)`, as in
`QOU.IwahoriHecke.TensorEmbed` (which does the same for `d = 1` and the Hecke algebra). The
site calculus there is written for `ι = Fin 2`; it is restated here for an arbitrary finite
local index `ι` (`pembed`, `tembed`), with the same proofs.

The construction is generic: any invertible `M` on `ι × ι` satisfying the braid relation on
`ι × ι × ι` gives `braidRep M`. The `U_q(sl₂)` instance is `rCheckRep`; its two inputs are
`isUnit_rCheckMat` (new here: `Θ` is an invertible diagonal and the polynomial part is
unipotent) and `rCheck_braid`.

-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. X.6 (braid group representations from
-- an R-matrix); [turaev1988] Turaev, "The Yang–Baxter equation and invariants of links".
-/

namespace QOU.Mass.QuantumSl2.BraidAction

open Matrix
open scoped Kronecker
open QOU.MathlibExt.IwahoriHecke (altProd altProd_two altProd_three map_altProd)
open QOU.IwahoriHecke.TensorEmbed (coxA coxA_symm)
open QOU.IwahoriHecke.BraidGroup (BraidGroupN braidGen artinRels val_altProd)

set_option linter.unusedSectionVars false

/-! ## Operators at sites of `ι^{⊗n}` -/

section Sites

variable {R : Type*} [CommRing R] {ι : Type*} [Fintype ι] [DecidableEq ι] {n : ℕ}

/-- A two-site operator acting at sites `i` and `j` of `V^{⊗n}` and trivially elsewhere. -/
def pembed (i j : Fin n) (M : Matrix (ι × ι) (ι × ι) R) :
    Matrix (Fin n → ι) (Fin n → ι) R :=
  Matrix.of fun a b =>
    if (∀ k, k ≠ i → k ≠ j → a k = b k) then M (a i, a j) (b i, b j) else 0

theorem pembed_apply (i j : Fin n) (M : Matrix (ι × ι) (ι × ι) R) (a b : Fin n → ι) :
    pembed i j M a b
      = if (∀ k, k ≠ i → k ≠ j → a k = b k) then M (a i, a j) (b i, b j) else 0 := rfl

/-- The assignments to sites `i ≠ j` biject with the states agreeing with `a` elsewhere. -/
def pairEquiv {i j : Fin n} (hij : i ≠ j) (a : Fin n → ι) :
    (ι × ι) ≃ {c : Fin n → ι // ∀ k, k ≠ i → k ≠ j → a k = c k} where
  toFun x := ⟨Function.update (Function.update a i x.1) j x.2, by
    intro k hki hkj
    rw [Function.update_of_ne hkj, Function.update_of_ne hki]⟩
  invFun c := (c.1 i, c.1 j)
  left_inv x := by
    have hi : Function.update (Function.update a i x.1) j x.2 i = x.1 := by
      rw [Function.update_of_ne hij, Function.update_self]
    simp [hi, Function.update_self]
  right_inv c := by
    refine Subtype.ext (funext fun k => ?_)
    dsimp only
    by_cases hkj : k = j
    · subst hkj; rw [Function.update_self]
    · rw [Function.update_of_ne hkj]
      by_cases hki : k = i
      · subst hki; rw [Function.update_self]
      · rw [Function.update_of_ne hki]
        exact c.2 k hki hkj

theorem sum_collapse {i j : Fin n} (hij : i ≠ j) (a : Fin n → ι)
    (F : (Fin n → ι) → R)
    (hF : ∀ c, ¬(∀ k, k ≠ i → k ≠ j → a k = c k) → F c = 0) :
    ∑ c, F c = ∑ x : ι × ι, F (Function.update (Function.update a i x.1) j x.2) := by
  classical
  rw [← Finset.sum_filter_of_ne (p := fun c => ∀ k, k ≠ i → k ≠ j → a k = c k)
        (fun c _ hc => by by_contra h; exact hc (hF c h))]
  rw [Finset.sum_subtype _ (fun c => by simp)
        (f := F) (p := fun c => ∀ k, k ≠ i → k ≠ j → a k = c k)]
  exact (Fintype.sum_equiv (pairEquiv hij a) _ _ (fun _ => rfl)).symm

variable {i j : Fin n}

private theorem update_left (hij : i ≠ j) (a : Fin n → ι) (x : ι × ι) :
    Function.update (Function.update a i x.1) j x.2 i = x.1 := by
  rw [Function.update_of_ne hij, Function.update_self]

private theorem update_right (a : Fin n → ι) (x : ι × ι) :
    Function.update (Function.update a i x.1) j x.2 j = x.2 := Function.update_self ..

private theorem update_agrees (a : Fin n → ι) (x : ι × ι) :
    ∀ k, k ≠ i → k ≠ j → a k = Function.update (Function.update a i x.1) j x.2 k := by
  intro k hki hkj
  rw [Function.update_of_ne hkj, Function.update_of_ne hki]

theorem pembed_apply_update (hij : i ≠ j) (M : Matrix (ι × ι) (ι × ι) R)
    (a : Fin n → ι) (x : ι × ι) :
    pembed i j M a (Function.update (Function.update a i x.1) j x.2) = M (a i, a j) x := by
  rw [pembed_apply, if_pos (update_agrees a x), update_left hij, update_right]

theorem pembed_update_apply (hij : i ≠ j) (N : Matrix (ι × ι) (ι × ι) R)
    (a b : Fin n → ι) (x : ι × ι) :
    pembed i j N (Function.update (Function.update a i x.1) j x.2) b
      = if (∀ k, k ≠ i → k ≠ j → a k = b k) then N x (b i, b j) else 0 := by
  rw [pembed_apply, update_left hij, update_right]
  congr 1
  refine propext ⟨fun h k hki hkj => ?_, fun h k hki hkj => ?_⟩
  · rw [update_agrees a x k hki hkj]; exact h k hki hkj
  · rw [← update_agrees a x k hki hkj]; exact h k hki hkj

theorem pembed_mul (hij : i ≠ j) (M N : Matrix (ι × ι) (ι × ι) R) :
    pembed i j M * pembed i j N = pembed i j (M * N) := by
  classical
  ext a b
  rw [Matrix.mul_apply]
  rw [sum_collapse hij a (fun c => pembed i j M a c * pembed i j N c b)
    (fun c hc => by dsimp only; rw [pembed_apply, if_neg hc, zero_mul])]
  simp only [pembed_apply_update hij, pembed_update_apply hij]
  by_cases hab : ∀ k, k ≠ i → k ≠ j → a k = b k
  · simp only [if_pos hab]
    rw [pembed_apply, if_pos hab, Matrix.mul_apply]
  · simp [hab, pembed_apply]

theorem pembed_one (hij : i ≠ j) : pembed i j (1 : Matrix (ι × ι) (ι × ι) R) = 1 := by
  classical
  ext a b
  rw [pembed_apply, Matrix.one_apply, Matrix.one_apply]
  by_cases hab : ∀ k, k ≠ i → k ≠ j → a k = b k
  · rw [if_pos hab]
    by_cases h : a = b
    · subst h; simp
    · rw [if_neg h]
      refine if_neg (fun hx => h (funext fun k => ?_))
      by_cases hki : k = i
      · subst hki; exact congrArg Prod.fst hx
      · by_cases hkj : k = j
        · subst hkj; exact congrArg Prod.snd hx
        · exact hab k hki hkj
  · rw [if_neg hab, if_neg (fun h => hab (fun k _ _ => by rw [h]))]

/-- `M ↦ M` at sites `i ≠ j` is a monoid map `End(V ⊗ V) → End(V^{⊗n})`. -/
def pembedHom (hij : i ≠ j) :
    Matrix (ι × ι) (ι × ι) R →* Matrix (Fin n → ι) (Fin n → ι) R where
  toFun := pembed i j
  map_one' := pembed_one hij
  map_mul' _ _ := (pembed_mul hij _ _).symm

theorem isUnit_pembed (hij : i ≠ j) {M : Matrix (ι × ι) (ι × ι) R} (hM : IsUnit M) :
    IsUnit (pembed (n := n) i j M) :=
  hM.map (pembedHom hij)

/-! ### Far commutation -/

variable {k l : Fin n}

private theorem agree_update_iff (hij : i ≠ j) (hki : k ≠ i) (hkj : k ≠ j)
    (hli : l ≠ i) (hlj : l ≠ j) (a b : Fin n → ι) (x : ι × ι) :
    (∀ m, m ≠ k → m ≠ l → Function.update (Function.update a i x.1) j x.2 m = b m)
      ↔ (x = (b i, b j) ∧ ∀ m, m ≠ i → m ≠ j → m ≠ k → m ≠ l → a m = b m) := by
  constructor
  · intro h
    refine ⟨Prod.ext ?_ ?_, fun m hmi hmj hmk hml => ?_⟩
    · rw [← update_left hij a x]; exact h i (Ne.symm hki) (Ne.symm hli)
    · rw [← update_right a x]; exact h j (Ne.symm hkj) (Ne.symm hlj)
    · rw [update_agrees a x m hmi hmj]; exact h m hmk hml
  · rintro ⟨rfl, h3⟩ m hmk hml
    by_cases hmi : m = i
    · subst hmi; exact update_left hij a _
    · by_cases hmj : m = j
      · subst hmj; exact update_right a _
      · rw [← update_agrees a _ m hmi hmj]; exact h3 m hmi hmj hmk hml

private theorem pembed_mul_apply_of_disjoint (hij : i ≠ j) (hki : k ≠ i) (hkj : k ≠ j)
    (hli : l ≠ i) (hlj : l ≠ j) (M N : Matrix (ι × ι) (ι × ι) R) (a b : Fin n → ι) :
    (pembed i j M * pembed k l N) a b
      = if (∀ m, m ≠ i → m ≠ j → m ≠ k → m ≠ l → a m = b m)
        then M (a i, a j) (b i, b j) * N (a k, a l) (b k, b l) else 0 := by
  classical
  rw [Matrix.mul_apply,
    sum_collapse hij a (fun c => pembed i j M a c * pembed k l N c b)
      (fun c hc => by dsimp only; rw [pembed_apply, if_neg hc, zero_mul])]
  have hval : ∀ x : ι × ι,
      pembed i j M a (Function.update (Function.update a i x.1) j x.2)
          * pembed k l N (Function.update (Function.update a i x.1) j x.2) b
        = M (a i, a j) x
          * (if (x = (b i, b j) ∧ ∀ m, m ≠ i → m ≠ j → m ≠ k → m ≠ l → a m = b m)
             then N (a k, a l) (b k, b l) else 0) := by
    intro x
    rw [pembed_apply_update hij, pembed_apply,
      ← update_agrees a x k hki hkj, ← update_agrees a x l hli hlj]
    simp only [agree_update_iff hij hki hkj hli hlj]
  rw [Finset.sum_congr rfl (fun x _ => hval x)]
  by_cases hP : ∀ m, m ≠ i → m ≠ j → m ≠ k → m ≠ l → a m = b m
  · rw [if_pos hP]
    simp only [eq_true hP, and_true, mul_ite, mul_zero]
    simp
  · rw [if_neg hP]
    simp [hP]

/-- **Far commutation**: operators at disjoint pairs of sites commute. -/
theorem pembed_commute (hij : i ≠ j) (hkl : k ≠ l) (hki : k ≠ i) (hkj : k ≠ j)
    (hli : l ≠ i) (hlj : l ≠ j) (M N : Matrix (ι × ι) (ι × ι) R) :
    pembed i j M * pembed k l N = pembed k l N * pembed i j M := by
  ext a b
  rw [pembed_mul_apply_of_disjoint hij hki hkj hli hlj,
    pembed_mul_apply_of_disjoint hkl (Ne.symm hki) (Ne.symm hli)
      (Ne.symm hkj) (Ne.symm hlj)]
  by_cases h : ∀ m, m ≠ i → m ≠ j → m ≠ k → m ≠ l → a m = b m
  · rw [if_pos h, if_pos (fun m h1 h2 h3 h4 => h m h3 h4 h1 h2), mul_comm]
  · rw [if_neg h, if_neg (fun hc => h (fun m h1 h2 h3 h4 => hc m h3 h4 h1 h2))]

/-! ### Three sites, and the braid relation -/

/-- A three-site operator on `(ι × ι) × ι`, acting at `i`, `j`, `k` and trivially elsewhere. -/
def tembed (i j k : Fin n) (M : Matrix ((ι × ι) × ι) ((ι × ι) × ι) R) :
    Matrix (Fin n → ι) (Fin n → ι) R :=
  Matrix.of fun a b =>
    if (∀ m, m ≠ i → m ≠ j → m ≠ k → a m = b m)
    then M ((a i, a j), a k) ((b i, b j), b k) else 0

theorem tembed_apply (i j k : Fin n) (M : Matrix ((ι × ι) × ι) ((ι × ι) × ι) R)
    (a b : Fin n → ι) :
    tembed i j k M a b
      = if (∀ m, m ≠ i → m ≠ j → m ≠ k → a m = b m)
        then M ((a i, a j), a k) ((b i, b j), b k) else 0 := rfl

/-- The update of `a` at three sites. -/
def upd3 (i j k : Fin n) (a : Fin n → ι) (x : (ι × ι) × ι) : Fin n → ι :=
  Function.update (Function.update (Function.update a i x.1.1) j x.1.2) k x.2

private theorem upd3_i (hij : i ≠ j) (hik : i ≠ k) (a : Fin n → ι) (x : (ι × ι) × ι) :
    upd3 i j k a x i = x.1.1 := by
  rw [upd3, Function.update_of_ne hik, Function.update_of_ne hij, Function.update_self]

private theorem upd3_j (hjk : j ≠ k) (a : Fin n → ι) (x : (ι × ι) × ι) :
    upd3 i j k a x j = x.1.2 := by
  rw [upd3, Function.update_of_ne hjk, Function.update_self]

private theorem upd3_k (a : Fin n → ι) (x : (ι × ι) × ι) : upd3 i j k a x k = x.2 :=
  Function.update_self ..

private theorem upd3_agrees (a : Fin n → ι) (x : (ι × ι) × ι) :
    ∀ m, m ≠ i → m ≠ j → m ≠ k → a m = upd3 i j k a x m := by
  intro m hmi hmj hmk
  rw [upd3, Function.update_of_ne hmk, Function.update_of_ne hmj, Function.update_of_ne hmi]

/-- The three free sites parametrise the states agreeing with `a` elsewhere. -/
def tripleEquiv (hij : i ≠ j) (hik : i ≠ k) (hjk : j ≠ k) (a : Fin n → ι) :
    ((ι × ι) × ι) ≃ {c : Fin n → ι // ∀ m, m ≠ i → m ≠ j → m ≠ k → a m = c m} where
  toFun x := ⟨upd3 i j k a x, upd3_agrees a x⟩
  invFun c := ((c.1 i, c.1 j), c.1 k)
  left_inv x := by
    simp only [upd3_i hij hik, upd3_j hjk, upd3_k]
  right_inv c := by
    refine Subtype.ext (funext fun m => ?_)
    simp only [upd3]
    by_cases hmk : m = k
    · subst hmk; rw [Function.update_self]
    · rw [Function.update_of_ne hmk]
      by_cases hmj : m = j
      · subst hmj; rw [Function.update_self]
      · rw [Function.update_of_ne hmj]
        by_cases hmi : m = i
        · subst hmi; rw [Function.update_self]
        · rw [Function.update_of_ne hmi]; exact c.2 m hmi hmj hmk

theorem sum_collapse3 (hij : i ≠ j) (hik : i ≠ k) (hjk : j ≠ k) (a : Fin n → ι)
    (F : (Fin n → ι) → R)
    (hF : ∀ c, ¬(∀ m, m ≠ i → m ≠ j → m ≠ k → a m = c m) → F c = 0) :
    ∑ c, F c = ∑ x : (ι × ι) × ι, F (upd3 i j k a x) := by
  classical
  rw [← Finset.sum_filter_of_ne (p := fun c => ∀ m, m ≠ i → m ≠ j → m ≠ k → a m = c m)
        (fun c _ hc => by by_contra h; exact hc (hF c h))]
  rw [Finset.sum_subtype _ (fun c => by simp)
        (f := F) (p := fun c => ∀ m, m ≠ i → m ≠ j → m ≠ k → a m = c m)]
  exact (Fintype.sum_equiv (tripleEquiv hij hik hjk a) _ _ (fun _ => rfl)).symm

theorem tembed_apply_update (hij : i ≠ j) (hik : i ≠ k) (hjk : j ≠ k)
    (M : Matrix ((ι × ι) × ι) ((ι × ι) × ι) R) (a : Fin n → ι) (x : (ι × ι) × ι) :
    tembed i j k M a (upd3 i j k a x) = M ((a i, a j), a k) x := by
  rw [tembed_apply, if_pos (upd3_agrees a x), upd3_i hij hik, upd3_j hjk, upd3_k]

theorem tembed_update_apply (hij : i ≠ j) (hik : i ≠ k) (hjk : j ≠ k)
    (N : Matrix ((ι × ι) × ι) ((ι × ι) × ι) R) (a b : Fin n → ι) (x : (ι × ι) × ι) :
    tembed i j k N (upd3 i j k a x) b
      = if (∀ m, m ≠ i → m ≠ j → m ≠ k → a m = b m)
        then N x ((b i, b j), b k) else 0 := by
  rw [tembed_apply, upd3_i hij hik, upd3_j hjk, upd3_k]
  congr 1
  refine propext ⟨fun h m hmi hmj hmk => ?_, fun h m hmi hmj hmk => ?_⟩
  · rw [upd3_agrees a x m hmi hmj hmk]; exact h m hmi hmj hmk
  · rw [← upd3_agrees a x m hmi hmj hmk]; exact h m hmi hmj hmk

theorem tembed_mul (hij : i ≠ j) (hik : i ≠ k) (hjk : j ≠ k)
    (M N : Matrix ((ι × ι) × ι) ((ι × ι) × ι) R) :
    tembed i j k M * tembed i j k N = tembed i j k (M * N) := by
  classical
  ext a b
  rw [Matrix.mul_apply,
    sum_collapse3 hij hik hjk a (fun c => tembed i j k M a c * tembed i j k N c b)
      (fun c hc => by dsimp only; rw [tembed_apply, if_neg hc, zero_mul])]
  simp only [tembed_apply_update hij hik hjk, tembed_update_apply hij hik hjk]
  by_cases hab : ∀ m, m ≠ i → m ≠ j → m ≠ k → a m = b m
  · simp only [if_pos hab]
    rw [tembed_apply, if_pos hab, Matrix.mul_apply]
  · simp [hab, tembed_apply]

/-- `A ⊗ 1` on `(ι × ι) × ι` (the `leg12` of `QuantumSl2Hexagon`, over any commutative ring). -/
def left2 (M : Matrix (ι × ι) (ι × ι) R) : Matrix ((ι × ι) × ι) ((ι × ι) × ι) R :=
  M ⊗ₖ (1 : Matrix ι ι R)

/-- `1 ⊗ A` on `(ι × ι) × ι` (the `leg23` of `QuantumSl2Hexagon`, over any commutative ring). -/
def right2 (M : Matrix (ι × ι) (ι × ι) R) : Matrix ((ι × ι) × ι) ((ι × ι) × ι) R :=
  Matrix.of fun u v => M (u.1.2, u.2) (v.1.2, v.2) * (1 : Matrix ι ι R) u.1.1 v.1.1

/-- At sites `i, j` the operator is `M ⊗ 1` at sites `i, j, k`. -/
theorem pembed_eq_tembed_left (hik : i ≠ k) (hjk : j ≠ k) (M : Matrix (ι × ι) (ι × ι) R) :
    pembed i j M = tembed i j k (left2 M) := by
  classical
  ext a b
  rw [pembed_apply, tembed_apply]
  by_cases hk : a k = b k
  · by_cases h3 : ∀ m, m ≠ i → m ≠ j → m ≠ k → a m = b m
    · rw [if_pos h3, if_pos (fun m hmi hmj => by
        by_cases hmk : m = k
        · subst hmk; exact hk
        · exact h3 m hmi hmj hmk)]
      simp [left2, kroneckerMap_apply, hk]
    · rw [if_neg h3, if_neg (fun h2 => h3 (fun m hmi hmj _ => h2 m hmi hmj))]
  · rw [if_neg (fun h2 => hk (h2 k (Ne.symm hik) (Ne.symm hjk)))]
    by_cases h3 : ∀ m, m ≠ i → m ≠ j → m ≠ k → a m = b m
    · rw [if_pos h3]; simp [left2, kroneckerMap_apply, hk]
    · rw [if_neg h3]

/-- At sites `j, k` the operator is `1 ⊗ M` at sites `i, j, k`. -/
theorem pembed_eq_tembed_right (hij : i ≠ j) (hik : i ≠ k) (N : Matrix (ι × ι) (ι × ι) R) :
    pembed j k N = tembed i j k (right2 N) := by
  classical
  ext a b
  rw [pembed_apply, tembed_apply]
  by_cases hi : a i = b i
  · by_cases h3 : ∀ m, m ≠ i → m ≠ j → m ≠ k → a m = b m
    · rw [if_pos h3, if_pos (fun m hmj hmk => by
        by_cases hmi : m = i
        · subst hmi; exact hi
        · exact h3 m hmi hmj hmk)]
      simp [right2, hi]
    · rw [if_neg h3, if_neg (fun h2 => h3 (fun m _ hmj hmk => h2 m hmj hmk))]
  · rw [if_neg (fun h2 => hi (h2 i hij hik))]
    by_cases h3 : ∀ m, m ≠ i → m ≠ j → m ≠ k → a m = b m
    · rw [if_pos h3]; simp [right2, hi]
    · rw [if_neg h3]

/-- **The braid relation at three distinct sites**, from the braid relation on
`(ι × ι) × ι`. No new matrix computation: both sides factor through `tembed`. -/
theorem pembed_braid (hij : i ≠ j) (hik : i ≠ k) (hjk : j ≠ k) (M : Matrix (ι × ι) (ι × ι) R)
    (hYB : left2 M * right2 M * left2 M = right2 M * left2 M * right2 M) :
    pembed i j M * pembed j k M * pembed i j M = pembed j k M * pembed i j M * pembed j k M := by
  rw [pembed_eq_tembed_left hik hjk, pembed_eq_tembed_right hij hik,
    tembed_mul hij hik hjk, tembed_mul hij hik hjk, tembed_mul hij hik hjk,
    tembed_mul hij hik hjk, hYB]

end Sites

/-! ## The braid group action -/

section Action

variable {R : Type*} [CommRing R] {ι : Type*} [Fintype ι] [DecidableEq ι] {m : ℕ}

/-- `M` acting on strands `a`, `a+1` of `ι^{⊗(m+1)}`. -/
def strandMat (M : Matrix (ι × ι) (ι × ι) R) (a : Fin m) :
    Matrix (Fin (m + 1) → ι) (Fin (m + 1) → ι) R :=
  pembed a.castSucc a.succ M

private theorem cs_ne_succ (a : Fin m) : a.castSucc ≠ a.succ := by
  simp [Fin.ext_iff]

/-- The strand operator as a unit. -/
noncomputable def strandUnit (M : Matrix (ι × ι) (ι × ι) R) (hM : IsUnit M) (a : Fin m) :
    (Matrix (Fin (m + 1) → ι) (Fin (m + 1) → ι) R)ˣ :=
  (isUnit_pembed (cs_ne_succ a) hM).unit

theorem strandUnit_val (M : Matrix (ι × ι) (ι × ι) R) (hM : IsUnit M) (a : Fin m) :
    ((strandUnit M hM a : (Matrix (Fin (m + 1) → ι) (Fin (m + 1) → ι) R)ˣ) :
      Matrix (Fin (m + 1) → ι) (Fin (m + 1) → ι) R) = strandMat M a :=
  IsUnit.unit_spec _

/-- The Artin relations of type `A` hold among the strand operators. -/
theorem strandMat_artin (M : Matrix (ι × ι) (ι × ι) R)
    (hYB : left2 M * right2 M * left2 M = right2 M * left2 M * right2 M) (a b : Fin m) :
    altProd (strandMat M a) (strandMat M b) (coxA m a b)
      = altProd (strandMat M b) (strandMat M a) (coxA m b a) := by
  by_cases hab : a = b
  · subst hab; rfl
  · have hba : b ≠ a := Ne.symm hab
    by_cases hadj : (a : ℕ) + 1 = (b : ℕ) ∨ (b : ℕ) + 1 = (a : ℕ)
    · rw [show coxA m a b = 3 from by simp [coxA, hab, hadj],
        show coxA m b a = 3 from by simp [coxA, hba, hadj.symm],
        altProd_three, altProd_three]
      rcases hadj with h | h
      · have hjk : a.succ = b.castSucc := by simp [Fin.ext_iff, h]
        have e := pembed_braid (R := R) (i := a.castSucc) (j := a.succ)
          (k := b.succ) (by simp [Fin.ext_iff])
          (by simp [Fin.ext_iff]; omega) (by simp [Fin.ext_iff]; omega) M hYB
        simp only [strandMat, ← hjk]
        rw [← mul_assoc, ← mul_assoc]
        exact e
      · have hjk : b.succ = a.castSucc := by simp [Fin.ext_iff, h]
        have e := pembed_braid (R := R) (i := b.castSucc) (j := b.succ)
          (k := a.succ) (by simp [Fin.ext_iff])
          (by simp [Fin.ext_iff]; omega) (by simp [Fin.ext_iff]; omega) M hYB
        simp only [strandMat, ← hjk]
        rw [← mul_assoc, ← mul_assoc]
        exact e.symm
    · have hadj' : ¬((b : ℕ) + 1 = (a : ℕ) ∨ (a : ℕ) + 1 = (b : ℕ)) :=
        fun hc => hadj hc.symm
      rw [show coxA m a b = 2 from by simp [coxA, hab, hadj],
        show coxA m b a = 2 from by simp [coxA, hba, hadj'],
        altProd_two, altProd_two]
      exact pembed_commute (cs_ne_succ a) (cs_ne_succ b)
        (by simp [Fin.ext_iff]; omega) (by simp [Fin.ext_iff]; omega)
        (by simp [Fin.ext_iff]; omega) (by simp [Fin.ext_iff]; omega) M M

/-- **The braid group action** `B_{m+1} → GL(ι^{⊗(m+1)})`, `σ_a ↦ M` on strands `a, a+1`,
for any invertible `M` satisfying the braid relation. -/
noncomputable def braidRep (M : Matrix (ι × ι) (ι × ι) R) (hM : IsUnit M)
    (hYB : left2 M * right2 M * left2 M = right2 M * left2 M * right2 M) :
    BraidGroupN m →* (Matrix (Fin (m + 1) → ι) (Fin (m + 1) → ι) R)ˣ :=
  PresentedGroup.toGroup (f := strandUnit M hM) (by
    rintro r ⟨a, b, rfl⟩
    rw [map_mul, map_inv, map_altProd, map_altProd]
    simp only [FreeGroup.lift_apply_of]
    have h : altProd (strandUnit M hM a) (strandUnit M hM b) (coxA m a b)
        = altProd (strandUnit M hM b) (strandUnit M hM a) (coxA m b a) := by
      refine Units.ext ?_
      rw [val_altProd, val_altProd, strandUnit_val, strandUnit_val]
      exact strandMat_artin M hYB a b
    rw [h, mul_inv_cancel])

@[simp] theorem braidRep_braidGen (M : Matrix (ι × ι) (ι × ι) R) (hM : IsUnit M)
    (hYB : left2 M * right2 M * left2 M = right2 M * left2 M * right2 M) (a : Fin m) :
    braidRep M hM hYB (braidGen (coxA m) a) = strandUnit M hM a :=
  PresentedGroup.toGroup.of _

theorem braidRep_braidGen_val (M : Matrix (ι × ι) (ι × ι) R) (hM : IsUnit M)
    (hYB : left2 M * right2 M * left2 M = right2 M * left2 M * right2 M) (a : Fin m) :
    ((braidRep M hM hYB (braidGen (coxA m) a) :
        (Matrix (Fin (m + 1) → ι) (Fin (m + 1) → ι) R)ˣ) :
      Matrix (Fin (m + 1) → ι) (Fin (m + 1) → ι) R) = strandMat M a := by
  rw [braidRep_braidGen, strandUnit_val]

end Action

/-! ## The `U_q(sl₂)` instance -/

section Rsl2

variable {𝕜 : Type*} [Field 𝕜] (s : 𝕜) (hs : s ≠ 0) (d : ℕ)

private theorem isUnit_of_mul_eq_one' {κ : Type*} [Fintype κ] [DecidableEq κ]
    {A B : Matrix κ κ 𝕜} (h : A * B = 1) : IsUnit A :=
  ⟨⟨A, B, h, Matrix.mul_eq_one_comm.mp h⟩, rfl⟩

/-- The polynomial part `Σ_{n ≤ d} c_n Eⁿ ⊗ Fⁿ` is unipotent, hence invertible. -/
theorem isUnit_rSum :
    IsUnit (Rep.rSum s (irrep (pow_ne_zero 2 hs) d) (irrep (pow_ne_zero 2 hs) d) (rOrder d d)) := by
  rw [rSum_irrep s hs d]
  set X : Matrix (Fin (d + 1) × Fin (d + 1)) (Fin (d + 1) × Fin (d + 1)) 𝕜 :=
    irrepE (s ^ 2) d ⊗ₖ irrepF (s ^ 2) d with hX
  have hterm : ∀ n, rcoef s n • ((irrepE (s ^ 2) d ^ n) ⊗ₖ (irrepF (s ^ 2) d ^ n))
      = rcoef s n • X ^ n := fun n => by rw [hX, kron_pow]
  simp only [hterm]
  set P := ∑ n ∈ Finset.range d, rcoef s (n + 1) • X ^ n with hP
  have hsplit : ∑ n ∈ Finset.range (d + 1), rcoef s n • X ^ n = 1 + X * P := by
    rw [Finset.sum_range_succ', pow_zero, rcoef_zero, one_smul, hP, Finset.mul_sum,
      add_comm _ (1 : Matrix (Fin (d + 1) × Fin (d + 1)) (Fin (d + 1) × Fin (d + 1)) 𝕜)]
    congr 1
    refine Finset.sum_congr rfl fun n _ => ?_
    rw [mul_smul_comm, pow_succ']
  rw [hsplit]
  refine IsNilpotent.isUnit_one_add ⟨d + 1, ?_⟩
  have hc : Commute X P := by
    rw [hP]
    exact Commute.sum_right _ _ _ fun n _ => (Commute.pow_right (Commute.refl X) n).smul_right _
  rw [hc.mul_pow, hX, kron_pow, irrepE_pow_nil, zero_kronecker, zero_mul]

/-- The `U_q(sl₂)` R-matrix on `V_{d+1} ⊗ V_{d+1}` is invertible. -/
theorem isUnit_rMat : IsUnit (rMat s hs d d) := by
  refine IsUnit.mul ?_ (isUnit_rSum s hs d)
  refine isUnit_of_mul_eq_one' (B := diagonal fun x => (s ^ (wt d x.1 * wt d x.2))⁻¹) ?_
  rw [cartanTheta, diagonal_mul_diagonal]
  conv_rhs => rw [← diagonal_one]
  congr 1
  funext x
  exact mul_inv_cancel₀ (zpow_ne_zero _ hs)

/-- The braiding `Ř = P R` on `V_{d+1} ⊗ V_{d+1}` is invertible. -/
theorem isUnit_rCheckMat : IsUnit (rCheckMat s hs d d) := by
  obtain ⟨u, hu⟩ := isUnit_rMat s hs d
  refine isUnit_of_mul_eq_one'
    (B := ((u⁻¹ : (Matrix _ _ 𝕜)ˣ) : Matrix _ _ 𝕜).submatrix id Prod.swap) ?_
  rw [rCheckMat, ← hu, ← submatrix_mul _ _ _ _ _ Function.bijective_id, Units.mul_inv]
  exact submatrix_one_equiv (Equiv.prodComm _ _)

/-- The braid relation for `Ř` in the form `braidRep` consumes. -/
theorem rCheck_braid_left2 (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)
    (hint : ∀ k, 0 < k → k ≤ 2 * d → qint (s ^ 2) k ≠ 0) :
    left2 (rCheckMat s hs d d) * right2 (rCheckMat s hs d d) * left2 (rCheckMat s hs d d)
      = right2 (rCheckMat s hs d d) * left2 (rCheckMat s hs d d) * right2 (rCheckMat s hs d d) := by
  have h12 : left2 (rCheckMat s hs d d) = leg12 (rCheckMat s hs d d) := rfl
  have h23 : right2 (rCheckMat s hs d d) = leg23 (rCheckMat s hs d d) := by ext x y; rfl
  rw [h12, h23]
  exact rCheck_braid s hs hq2 d hint

/-- **The `U_q(sl₂)` braid group action** `B_{m+1} → GL(V_{d+1}^{⊗(m+1)})`, `σ_a ↦ Ř` on
strands `a, a+1`, for every number of strands and every spin. -/
noncomputable def rCheckRep (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)
    (hint : ∀ k, 0 < k → k ≤ 2 * d → qint (s ^ 2) k ≠ 0) (m : ℕ) :
    BraidGroupN m →* (Matrix (Fin (m + 1) → Fin (d + 1)) (Fin (m + 1) → Fin (d + 1)) 𝕜)ˣ :=
  braidRep (rCheckMat s hs d d) (isUnit_rCheckMat s hs d) (rCheck_braid_left2 s hs d hq2 hint)

theorem rCheckRep_braidGen (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)
    (hint : ∀ k, 0 < k → k ≤ 2 * d → qint (s ^ 2) k ≠ 0) (m : ℕ) (a : Fin m) :
    ((rCheckRep s hs d hq2 hint m (braidGen (coxA m) a) :
        (Matrix (Fin (m + 1) → Fin (d + 1)) (Fin (m + 1) → Fin (d + 1)) 𝕜)ˣ) :
      Matrix (Fin (m + 1) → Fin (d + 1)) (Fin (m + 1) → Fin (d + 1)) 𝕜)
      = strandMat (rCheckMat s hs d d) a :=
  braidRep_braidGen_val _ _ _ a

end Rsl2

end QOU.Mass.QuantumSl2.BraidAction
