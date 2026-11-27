import QOU.Core.LawvereCut

/-!
# QOU.Core.QuantaleCut — one cut core, indexed by a resolution quantale

Bean `qou-dk7p` (constructive turn), owner choice 2026-11-27: one core for Dedekind,
surreal, `p`-adic, characteristic-`p` and Habiro cuts. Each setting supplies:

* a **resolution** type `V` with a preorder (`ε ≤ δ` means `δ` is the coarser resolution)
  and a combination `comb`, monotone in both arguments (Lawvere's quantale tensor);
* a **near system** on the carrier `X`: `near ε x y` means "`x` and `y` agree to
  resolution `ε`", monotone in `ε`, symmetric, and satisfying the triangle law
  `near ε x y → near δ y z → near (comb ε δ) x z`.

`near` is a `Prop`, not a distance value, so no setting is asked to compute an exact
distance (an `ord` or an `|x − y|`). This is the relational form of a `V`-enriched
category in Lawvere's sense.

A **cut** `LCut N` is a family of approximants `approx ε a` with Lawvere `ev`
(any two approximants are near at the combined resolution). Lawvere `coev`
(locatedness) is the separate predicate `LCut.LocatedAt`.

Instances in this file:

* `ordNear K`: any linearly ordered additive group `K`, `V = K`, `comb = +`,
  `near ε x y ↔ |x − y| ≤ ε`. This covers `ℚ`, any ordered field, and the surreals
  (Mathlib's `Surreal` is a linearly ordered additive group). `Cut.toLCut` sends a
  two-sided Dedekind `Cut` here, and `Cut.Located` gives `LocatedAt (0 < ·)`.
* `adicNear I`: any commutative ring with an antitone ideal tower `I`, `V = AdicLevel`
  (`ℕ`, reversed), `comb = min`, `near n x y ↔ x − y ∈ I n`. This covers `p`-adic
  (`I n = (pⁿ)`), characteristic-`p` `t`-adic (`I n = (tⁿ)`) and Habiro
  (`I n = ((q;q)_n)`) towers. `AdicCut.toLCut` is located at every level with no axiom.

No empirical value enters this file.
-/

namespace QOU.Core.LawvereCut

/-- A resolution quantale: a preorder with a combination monotone in both arguments. -/
class Resolution (V : Type*) [Preorder V] where
  comb : V → V → V
  comb_mono : ∀ {a a' b b' : V}, a ≤ a' → b ≤ b' → comb a b ≤ comb a' b'

/-- A near system on `X` over the resolution quantale `V`. -/
structure NearSystem (V X : Type*) [Preorder V] [Resolution V] where
  near : V → X → X → Prop
  mono : ∀ {ε δ : V} {x y : X}, ε ≤ δ → near ε x y → near δ x y
  symm : ∀ {ε : V} {x y : X}, near ε x y → near ε y x
  tri : ∀ {ε δ : V} {x y z : X}, near ε x y → near δ y z →
    near (Resolution.comb ε δ) x z

variable {V X : Type*} [Preorder V] [Resolution V]

/-- A Lawvere cut: approximants at each resolution, with `ev`. -/
structure LCut (N : NearSystem V X) where
  approx : V → X → Prop
  /-- Lawvere `ev`: any two approximants are near at the combined resolution. -/
  ev : ∀ {ε δ : V} {a b : X}, approx ε a → approx δ b →
    N.near (Resolution.comb ε δ) a b

namespace LCut

variable {N : NearSystem V X}

/-- Lawvere `coev` on a set `pos` of admissible resolutions: an approximant exists at each. -/
def LocatedAt (c : LCut N) (pos : V → Prop) : Prop :=
  ∀ ε, pos ε → ∃ a, c.approx ε a

/-- The cut of a point `x`: its approximants are the points near `x`. -/
def ofPoint (N : NearSystem V X) (x : X) : LCut N where
  approx ε a := N.near ε a x
  ev ha hb := N.tri ha (N.symm hb)

/-- A point's cut is located wherever `x` is near itself. -/
theorem ofPoint_locatedAt (N : NearSystem V X) (x : X) {pos : V → Prop}
    (h : ∀ ε, pos ε → N.near ε x x) : (ofPoint N x).LocatedAt pos :=
  fun ε hε => ⟨x, h ε hε⟩

/-- Two approximants at the same resolution are near at `comb ε ε`. -/
theorem approx_near (c : LCut N) {ε : V} {a b : X} (ha : c.approx ε a) (hb : c.approx ε b) :
    N.near (Resolution.comb ε ε) a b :=
  c.ev ha hb

end LCut

/-! ### The ordered (Dedekind / surreal) instance -/

section Ordered

variable (K : Type*) [AddCommGroup K] [LinearOrder K] [IsOrderedAddMonoid K]

/-- On an ordered additive group, resolutions combine by addition. -/
instance (priority := low) ordResolution : Resolution K where
  comb a b := a + b
  comb_mono h1 h2 := add_le_add h1 h2

/-- `near ε x y ↔ |x − y| ≤ ε`. -/
def ordNear : NearSystem K K where
  near ε x y := |x - y| ≤ ε
  mono h hxy := hxy.trans h
  symm h := by rwa [abs_sub_comm]
  tri h1 h2 := (abs_sub_le _ _ _).trans (add_le_add h1 h2)

end Ordered

section Dedekind

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- A two-sided Dedekind cut as a Lawvere cut: `a` approximates at resolution `ε` when
`a` is a lower probe and `a + ε` an upper probe. -/
def Cut.toLCut (c : Cut K) : LCut (ordNear K) where
  approx ε a := c.lower a ∧ c.upper (a + ε)
  ev := by
    intro ε δ a b ha hb
    have h1 := c.ev a (b + δ) ha.1 hb.2
    have h2 := c.ev b (a + ε) hb.1 ha.2
    have h3 := c.ev a (a + ε) ha.1 ha.2
    have h4 := c.ev b (b + δ) hb.1 hb.2
    show |a - b| ≤ ε + δ
    rw [abs_sub_le_iff]
    constructor <;> linarith

/-- Dedekind locatedness gives Lawvere `coev` at every positive resolution. -/
theorem Cut.toLCut_locatedAt {c : Cut K} (hc : c.Located) :
    c.toLCut.LocatedAt (fun ε => 0 < ε) := by
  intro ε hε
  obtain ⟨a, b, ha, hb, hab⟩ := hc ε hε
  exact ⟨a, ha, c.upper_up b (a + ε) (by linarith) hb⟩

end Dedekind

/-! ### The adic (p-adic / char p / Habiro) instance -/

/-- Adic resolution levels: `ℕ` with the reversed order (a larger level is finer). -/
structure AdicLevel where
  n : ℕ

instance : Preorder AdicLevel where
  le a b := b.n ≤ a.n
  le_refl a := le_refl a.n
  le_trans _ _ _ h1 h2 := le_trans h2 h1

instance : Resolution AdicLevel where
  comb a b := ⟨min a.n b.n⟩
  comb_mono {a a' b b'} h1 h2 :=
    show min a'.n b'.n ≤ min a.n b.n from
      min_le_min (show a'.n ≤ a.n from h1) (show b'.n ≤ b.n from h2)

section Adic

variable {R : Type*} [CommRing R]

/-- `near n x y ↔ x − y ∈ I n` for an antitone ideal tower. -/
def adicNear (I : ℕ → Ideal R) (hI : Antitone I) : NearSystem AdicLevel R where
  near ε x y := x - y ∈ I ε.n
  mono {ε δ x y} h hxy := hI (show δ.n ≤ ε.n from h) hxy
  symm {ε x y} h := by
    have := neg_mem h
    rwa [neg_sub] at this
  tri {ε δ x y z} h1 h2 := by
    show x - z ∈ I (min ε.n δ.n)
    have := Ideal.add_mem _ (hI (min_le_left ε.n δ.n) h1) (hI (min_le_right ε.n δ.n) h2)
    rwa [sub_add_sub_cancel] at this

/-- An adic cut as a Lawvere cut: `a` approximates at level `n` when `a ≡ stage n` mod `I n`. -/
def AdicCut.toLCut (c : AdicCut R) : LCut (adicNear c.ideal c.ideal_anti) where
  approx ε a := a - c.stage ε.n ∈ c.ideal ε.n
  ev := by
    intro ε δ a b ha hb
    show a - b ∈ c.ideal (min ε.n δ.n)
    have e : a - b = (a - c.stage ε.n) - (b - c.stage δ.n) + (c.stage ε.n - c.stage δ.n) := by
      ring
    have hA := c.ideal_anti (min_le_left ε.n δ.n) ha
    have hB := c.ideal_anti (min_le_right ε.n δ.n) hb
    have hS : c.stage ε.n - c.stage δ.n ∈ c.ideal (min ε.n δ.n) := by
      rcases le_total ε.n δ.n with h | h
      · have := c.ideal_anti (min_le_left ε.n δ.n) (c.stage_sub_mem h)
        rw [← neg_sub]
        exact neg_mem this
      · exact c.ideal_anti (min_le_right ε.n δ.n) (c.stage_sub_mem h)
    rw [e]
    exact Ideal.add_mem _ (Ideal.sub_mem _ hA hB) hS

/-- Adic `coev` is free: every level has an approximant, namely its own stage. -/
theorem AdicCut.toLCut_locatedAt (c : AdicCut R) : c.toLCut.LocatedAt (fun _ => True) := by
  intro ε _
  refine ⟨c.stage ε.n, ?_⟩
  show c.stage ε.n - c.stage ε.n ∈ c.ideal ε.n
  rw [sub_self]
  exact zero_mem _

end Adic

end QOU.Core.LawvereCut
