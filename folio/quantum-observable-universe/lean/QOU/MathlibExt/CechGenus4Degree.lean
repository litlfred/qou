import QOU.MathlibExt.CechGenus4Nerve
import QOU.MathlibExt.CechNerveNormalize

/-!
# The degree on the genus-4 nerve (route R3, step S2b, combinatorial half)

For a function `V` on ordered triples of vertices of the genus-4 triangulation
(`CechGenus4Nerve`), satisfying the cocycle identity on every quadruple that lies
in one face (`IsCocycle Q4 V`), define

  `deg V = Σ_f V2 V (fA f) (fB f) (fC f)`,

the sum over the 50 oriented faces of the normalised cochain `V2`
(`CechNerveNormalize`). Values on triples outside a face play no role.

## Results, all sorry-free

* `deg_congr`: `deg` depends only on the values on simplices.
* `deg_cob`, `deg_eq_of_rel`: coboundaries have degree `0`, so cohomologous
  cochains have equal degree.
* `exists_cob_of_deg_eq_zero`: a cocycle of degree `0` is a coboundary on the
  simplices.
* `Vg_cocycle`, `deg_Vg`: for every `g` there is a cocycle of degree `g`.

Together: `deg` is an isomorphism from the nerve `H²` onto the coefficient
group. The step that passes this to the open-star cover of the realised
surface is `CechGenus4Cover`.

## What this does NOT do

No topology here. Bean `qou-skn4`.

-- Ref: [manuscript] lifting-and-descent, route R3, surface step S2
-/

namespace QOU.CentralExtension.Cech.Genus4

open NerveNormalize (V1 V2 w1 w2 u2 IsCocycle Simplicial)

/-- The three vertices of face `f`. -/
def face4 (f : Fin 50) : Finset (Fin 19) := {fA f, fB f, fC f}

/-- The simplices of the triangulation: vertex sets inside one face. -/
def Q4 (s : Finset (Fin 19)) : Prop := ∃ f, s ⊆ face4 f

theorem simplicial_Q4 : Simplicial Q4 := ⟨fun hts ⟨f, hf⟩ => ⟨f, hts.trans hf⟩⟩

theorem face_distinct : ∀ f : Fin 50, fA f ≠ fB f ∧ fB f ≠ fC f ∧ fA f ≠ fC f := by
  decide +kernel

theorem inc_self (x : Fin 19) (e : Fin 75) : inc x x e = 0 := by
  have he := edge_ne e
  unfold inc
  rw [if_neg, if_neg] <;> rintro ⟨h1, h2⟩ <;> exact he (h1.symm.trans h2)

variable {A : Type} [AddCommGroup A]

theorem prim_diag (φ : Fin 50 → A) (x : Fin 19) : prim φ x x = 0 := by
  simp [prim, inc_self]

/-- **Exactness on one triangle.** On three distinct points, an antisymmetric
pair function with zero diagonal whose coboundary vanishes on `(x,y,z)` has
vanishing coboundary on every triple of the three points. -/
theorem cob_eq_zero_of_cob_xyz {ι : Type} [LinearOrder ι] {x y z : ι}
    (hxy : x ≠ y) (hyz : y ≠ z) (hxz : x ≠ z) (d : ι → ι → A)
    (hs : ∀ a ∈ ({x, y, z} : Finset ι), ∀ b ∈ ({x, y, z} : Finset ι), d b a = - d a b)
    (hd : ∀ a ∈ ({x, y, z} : Finset ι), d a a = 0)
    (h0 : NerveNormalize.cob d x y z = 0) :
    ∀ a ∈ ({x, y, z} : Finset ι), ∀ b ∈ ({x, y, z} : Finset ι), ∀ c ∈ ({x, y, z} : Finset ι),
      NerveNormalize.cob d a b c = 0 := by
  classical
  let t : ι → A := fun a => if a = x then 0 else if a = y then d x y else d x z
  have hx : x ∈ ({x, y, z} : Finset ι) := by simp
  have hy : y ∈ ({x, y, z} : Finset ι) := by simp
  have hz : z ∈ ({x, y, z} : Finset ι) := by simp
  have hyx := hs x hx y hy
  have hzx := hs x hx z hz
  have hzy := hs y hy z hz
  have h0' : d x y + d y z - d x z = 0 := h0
  have key : ∀ a ∈ ({x, y, z} : Finset ι), ∀ b ∈ ({x, y, z} : Finset ι), d a b = t b - t a := by
    intro a ha b hb
    simp only [Finset.mem_insert, Finset.mem_singleton] at ha hb
    obtain h | h | h := ha <;> obtain h' | h' | h' := hb <;> rw [h, h'] <;>
      simp only [t, if_true, hxy, hxy.symm, hyz.symm, hxz.symm, if_false] <;>
      first
      | exact hyx | exact hzx | exact hzy
      | (simp [hd _ hx, hd _ hy, hd _ hz]; done)
      | (simp only [zero_sub]; first | exact hyx | exact hzx)
      | (linear_combination (norm := abel) h0'; done)
      | (linear_combination (norm := abel) hzy - h0'; done)
  intro a ha b hb c hc
  simp only [NerveNormalize.cob, key a ha b hb, key b hb c hc, key a ha c hc]
  abel

/-! ### The degree of a cochain on the nerve -/

local notation "NC" => NerveNormalize.cob

theorem prim_face (φ : Fin 50 → A) (h : ∑ f, φ f = 0) (f : Fin 50) :
    φ f = cob (prim φ) (fA f) (fB f) (fC f) := by
  rw [cob_prim, sum_D_smul_W]
  simp only [cert, sub_smul, ite_smul, one_smul, zero_smul, Finset.sum_sub_distrib,
    Finset.sum_ite_eq, Finset.mem_univ, if_true]
  by_cases hf : f = 0
  · subst hf; simp [h]
  · simp [hf]

theorem mem_face (f : Fin 50) : fA f ∈ face4 f ∧ fB f ∈ face4 f ∧ fC f ∈ face4 f := by
  simp [face4]

theorem Q4_of_mem {f : Fin 50} {p q r : Fin 19} (hp : p ∈ face4 f) (hq : q ∈ face4 f)
    (hr : r ∈ face4 f) : Q4 {p, q, r} :=
  ⟨f, by simp [Finset.insert_subset_iff, hp, hq, hr]⟩

theorem V2_add (V V' : Fin 19 → Fin 19 → Fin 19 → A) (a b c : Fin 19) :
    V2 (fun i j k => V i j k + V' i j k) a b c = V2 V a b c + V2 V' a b c := by
  simp only [V2, V1, w1, w2, NerveNormalize.cob]; split_ifs <;> abel

theorem V2_congr {s : Finset (Fin 19)} {V V' : Fin 19 → Fin 19 → Fin 19 → A}
    (h : ∀ p q r, p ∈ s → q ∈ s → r ∈ s → V p q r = V' p q r) {a b c : Fin 19}
    (ha : a ∈ s) (hb : b ∈ s) (hc : c ∈ s) : V2 V a b c = V2 V' a b c := by
  simp (disch := assumption) only [V2, V1, w1, w2, NerveNormalize.cob, h]

theorem V2_zero (a b c : Fin 19) : V2 (fun _ _ _ => (0 : A)) a b c = 0 := by
  simp only [V2, V1, w1, w2, NerveNormalize.cob]; split_ifs <;> simp

theorem V2_cob_alt (u : Fin 19 → Fin 19 → A) (hu : ∀ x y, u y x = - u x y)
    (hd : ∀ x, u x x = 0) (a b c : Fin 19) : V2 (NC u) a b c = NC u a b c := by
  simp only [V2, V1, w1, w2, NerveNormalize.cob, hd]
  split_ifs <;> (try simp only [hu a b, hu b c, hu a c]) <;> abel

/-- The degree: sum over the oriented faces of the normalised cochain. -/
def deg (V : Fin 19 → Fin 19 → Fin 19 → A) : A := ∑ f, V2 V (fA f) (fB f) (fC f)

theorem deg_add (V V' : Fin 19 → Fin 19 → Fin 19 → A) :
    deg (fun i j k => V i j k + V' i j k) = deg V + deg V' := by
  simp only [deg, V2_add, Finset.sum_add_distrib]

/-- The degree depends only on the values on simplices. -/
theorem deg_congr {V V' : Fin 19 → Fin 19 → Fin 19 → A}
    (h : ∀ a b c, Q4 {a, b, c} → V a b c = V' a b c) : deg V = deg V' :=
  Finset.sum_congr rfl fun f _ =>
    V2_congr (s := face4 f) (fun p q r hp hq hr => h p q r (Q4_of_mem hp hq hr))
      (mem_face f).1 (mem_face f).2.1 (mem_face f).2.2

/-- Antisymmetrisation of a pair function using the order. -/
def asym (W : Fin 19 → Fin 19 → A) (a b : Fin 19) : A :=
  if a < b then W a b else if b < a then - W b a else 0

theorem asym_antisymm (W : Fin 19 → Fin 19 → A) (a b : Fin 19) :
    asym W b a = - asym W a b := by
  unfold asym
  rcases lt_trichotomy a b with h | rfl | h
  · simp [h, not_lt.mpr h.le]
  · simp
  · simp [h, not_lt.mpr h.le]

theorem asym_eq {W : Fin 19 → Fin 19 → A} {a b : Fin 19} (hd : W a a = 0)
    (hs : W b a = - W a b) : asym W a b = W a b := by
  unfold asym
  rcases lt_trichotomy a b with h | rfl | h
  · simp [h]
  · simp [hd]
  · simp [h, not_lt.mpr h.le, hs]

/-- **The degree of a coboundary is zero.** -/
theorem deg_cob (w : Fin 19 → Fin 19 → A) : deg (NC w) = 0 := by
  set V : Fin 19 → Fin 19 → Fin 19 → A := NC w
  have hV : IsCocycle Q4 V := fun i j k l _ => by simp only [V, NerveNormalize.cob]; abel
  set W : Fin 19 → Fin 19 → A := fun a b => w a b - (w1 V a b + w2 V a b)
  have hW : ∀ a b c, V2 V a b c = NC W a b c := fun a b c => by
    rw [NerveNormalize.V2_eq_sub_cob]; simp only [V, W, NerveNormalize.cob]; abel
  have hface : ∀ f, ∀ a ∈ face4 f, ∀ b ∈ face4 f, W a a = 0 ∧ W b a = - W a b := by
    intro f a ha b hb
    have hs : Q4 {fA f, fB f, fC f} := ⟨f, subset_rfl⟩
    obtain ⟨h1, -, -, -, -⟩ := NerveNormalize.V2_alt simplicial_Q4 hV hs ha ha ha
    obtain ⟨-, -, h3, -, -⟩ := NerveNormalize.V2_alt simplicial_Q4 hV hs ha hb hb
    rw [hW] at h1 h3
    simp only [NerveNormalize.cob] at h1 h3
    refine ⟨by simpa using h1, ?_⟩
    have : W a a = 0 := by simpa using h1
    rw [this, sub_zero] at h3
    exact eq_neg_of_add_eq_zero_right h3
  have key : ∀ f, V2 V (fA f) (fB f) (fC f) = cob (asym W) (fA f) (fB f) (fC f) := by
    intro f
    obtain ⟨ma, mb, mc⟩ := mem_face f
    rw [hW]; simp only [NerveNormalize.cob, cob]
    rw [asym_eq (hface f _ ma _ mb).1 (hface f _ ma _ mb).2,
      asym_eq (hface f _ mb _ mc).1 (hface f _ mb _ mc).2,
      asym_eq (hface f _ ma _ mc).1 (hface f _ ma _ mc).2]
  simp only [deg, key]
  exact sum_cob_eq_zero _ (fun x y => asym_antisymm W x y)

/-- Cohomologous on the simplices ⇒ same degree. -/
theorem deg_eq_of_rel {V V' : Fin 19 → Fin 19 → Fin 19 → A} (w : Fin 19 → Fin 19 → A)
    (h : ∀ a b c, Q4 {a, b, c} → V' a b c = V a b c + NC w a b c) : deg V' = deg V := by
  rw [deg_congr (V' := fun i j k => V i j k + NC w i j k) h, deg_add, deg_cob, add_zero]

/-- **Injectivity.** A cocycle on the simplices with degree zero is a coboundary
there. -/
theorem exists_cob_of_deg_eq_zero {V : Fin 19 → Fin 19 → Fin 19 → A} (hV : IsCocycle Q4 V)
    (h : deg V = 0) : ∃ w : Fin 19 → Fin 19 → A, ∀ a b c, Q4 {a, b, c} → V a b c = NC w a b c := by
  set φ : Fin 50 → A := fun f => V2 V (fA f) (fB f) (fC f)
  set u := prim φ
  have hface : ∀ f, ∀ a ∈ face4 f, ∀ b ∈ face4 f, ∀ c ∈ face4 f, V2 V a b c = NC u a b c := by
    intro f
    obtain ⟨d1, d2, d3⟩ := face_distinct f
    have hs : Q4 {fA f, fB f, fC f} := ⟨f, subset_rfl⟩
    set d : Fin 19 → Fin 19 → A := fun a b => u2 V (fA f) a b - u a b
    have hd0 : NC d (fA f) (fB f) (fC f) = 0 := by
      have e1 := NerveNormalize.V2_local simplicial_Q4 hV hs (mem_face f).1 (mem_face f).2.1
        (mem_face f).2.2
      have e2 := prim_face φ h f
      simp only [φ] at e2
      simp only [d, NerveNormalize.cob] at e1 ⊢
      simp only [cob] at e2
      rw [e1] at e2
      simp only [u]
      linear_combination (norm := abel) e2
    have hzero := cob_eq_zero_of_cob_xyz d1 d2 d3 d
      (fun a ha b hb => by
        simp only [d, NerveNormalize.u2_antisymm simplicial_Q4 hV hs ha hb, u,
          prim_antisymm φ a b]; abel)
      (fun a _ => by simp [d, NerveNormalize.u2_diag, u, prim_diag]) hd0
    intro a ha b hb c hc
    have e := NerveNormalize.V2_local simplicial_Q4 hV hs ha hb hc
    have z := hzero a ha b hb c hc
    simp only [d, NerveNormalize.cob] at z e ⊢
    rw [e]; linear_combination (norm := abel) z
  refine ⟨fun a b => u a b + (w1 V a b + w2 V a b), fun a b c ⟨f, hf⟩ => ?_⟩
  simp only [Finset.insert_subset_iff, Finset.singleton_subset_iff] at hf
  have e := NerveNormalize.V2_eq_sub_cob (V := V) a b c
  rw [hface f a hf.1 b hf.2.1 c hf.2.2] at e
  simp only [NerveNormalize.cob] at e ⊢
  linear_combination (norm := abel) -e

/-! ### A cocycle of every degree -/

/-- The pair function supported on the first side of face `0`. -/
def u0 (g : A) (x y : Fin 19) : A :=
  if x = fA 0 ∧ y = fB 0 then g else if x = fB 0 ∧ y = fA 0 then - g else 0

theorem u0_antisymm (g : A) (x y : Fin 19) : u0 g y x = - u0 g x y := by
  have hne := (face_distinct 0).1
  unfold u0
  by_cases h1 : x = fA 0 ∧ y = fB 0
  · obtain ⟨rfl, rfl⟩ := h1; simp [hne, Ne.symm hne]
  · by_cases h2 : x = fB 0 ∧ y = fA 0
    · obtain ⟨rfl, rfl⟩ := h2; simp [hne, Ne.symm hne]
    · rw [if_neg h1, if_neg h2, if_neg (fun h => h2 ⟨h.2, h.1⟩),
        if_neg (fun h => h1 ⟨h.2, h.1⟩), neg_zero]

theorem u0_diag (g : A) (x : Fin 19) : u0 g x x = 0 := by
  have hne := (face_distinct 0).1
  unfold u0
  rw [if_neg, if_neg]
  · rintro ⟨rfl, h⟩; exact hne h.symm
  · rintro ⟨rfl, h⟩; exact hne h

theorem face0_unique : ∀ h : Fin 50, h ≠ 0 →
    ¬ (fA 0 ∈ face4 h ∧ fB 0 ∈ face4 h ∧ fC 0 ∈ face4 h) := by
  decide +kernel

/-- The cocycle: the coboundary of `u0 g` on the triples of face `0`, zero
elsewhere. -/
def Vg (g : A) (a b c : Fin 19) : A :=
  if a ∈ face4 0 ∧ b ∈ face4 0 ∧ c ∈ face4 0 then NC (u0 g) a b c else 0

theorem cob_u0_degenerate (g : A) {a b c : Fin 19} (h : a = b ∨ b = c ∨ a = c) :
    NC (u0 g) a b c = 0 := by
  simp only [NerveNormalize.cob]
  rcases h with rfl | rfl | rfl
  · simp [u0_diag]
  · simp [u0_diag]
  · rw [u0_antisymm g a b, u0_diag]; abel

theorem Vg_zero (g : A) {h : Fin 50} (hh : h ≠ 0) {a b c : Fin 19} (ha : a ∈ face4 h)
    (hb : b ∈ face4 h) (hc : c ∈ face4 h) : Vg g a b c = 0 := by
  unfold Vg
  split_ifs with h0
  · by_cases hdeg : a = b ∨ b = c ∨ a = c
    · exact cob_u0_degenerate g hdeg
    · exfalso
      push_neg at hdeg
      obtain ⟨hab, hbc, hac⟩ := hdeg
      obtain ⟨a0, b0, c0⟩ := h0
      simp only [face4, Finset.mem_insert, Finset.mem_singleton] at a0 b0 c0
      apply face0_unique h hh
      rcases a0 with rfl | rfl | rfl <;> rcases b0 with rfl | rfl | rfl <;>
        rcases c0 with rfl | rfl | rfl <;>
        first
        | exact absurd rfl hab | exact absurd rfl hbc | exact absurd rfl hac
        | exact ⟨by assumption, by assumption, by assumption⟩
  · rfl

theorem Vg_cocycle (g : A) : IsCocycle Q4 (Vg g) := by
  rintro i j k l ⟨h, hsub⟩
  simp only [Finset.insert_subset_iff, Finset.singleton_subset_iff] at hsub
  obtain ⟨hi, hj, hk, hl⟩ := hsub
  by_cases hh : h = 0
  · subst hh
    simp only [Vg, hi, hj, hk, hl, and_self, if_true, NerveNormalize.cob]; abel
  · rw [Vg_zero g hh hi hj hk, Vg_zero g hh hi hk hl, Vg_zero g hh hj hk hl,
      Vg_zero g hh hi hj hl]

/-- **Surjectivity.** `Vg g` has degree `g`. -/
theorem deg_Vg (g : A) : deg (Vg g) = g := by
  unfold deg
  rw [Finset.sum_eq_single (0 : Fin 50)]
  · obtain ⟨ma, mb, mc⟩ := mem_face 0
    rw [V2_congr (s := face4 0) (V' := NC (u0 g)) (fun p q r hp hq hr => by
        simp [Vg, hp, hq, hr]) ma mb mc,
      V2_cob_alt _ (u0_antisymm g) (u0_diag g)]
    obtain ⟨d1, d2, d3⟩ := face_distinct 0
    simp only [NerveNormalize.cob, u0]
    simp [d1, Ne.symm d1, Ne.symm d2, Ne.symm d3]
  · intro h _ hh
    obtain ⟨ma, mb, mc⟩ := mem_face h
    rw [V2_congr (s := face4 h) (V' := fun _ _ _ => (0 : A)) (fun p q r hp hq hr =>
        Vg_zero g hh hp hq hr) ma mb mc, V2_zero]
  · simp

end QOU.CentralExtension.Cech.Genus4
