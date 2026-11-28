import QOU.BringsSurface.BringTripleSelection
import QOU.BringsSurface.BringReflectionParity

/-!
# The typed spectral sunset on Bring's surface

Bean `qou-u81q`. This is the hyperbolic counterpart of the flat-torus sunset from the two-loop
measure thread (PR #9860). For the Green function `G = Σ_{λ ≠ 0} φ_λ ⊗ φ_λ / λ` of the Laplacian
on `B`, with a real orthonormal eigenbasis, the two-loop sunset is
```
∫∫ G(x,y)³ dx dy = Σ_{a,b,c} w_a w_b w_c C_{abc}² ,   w = 1/λ,   C_{abc} = ∫ φ_a φ_b φ_c .
```
There is no known closed form, and none is claimed. What is proved is the **selection rule**.
Choose the eigenbasis adapted to the fourteen types of `S₅ × C₂` (`BringReflectionParity.lean`).
Then `C_{abc}` restricts an invariant trilinear form to `ρ_a ⊗ ρ_b ⊗ ρ_c`, so it vanishes unless
`N(ρ_a, ρ_b, ρ_c) ≠ 0` (`BringTripleSelection.lean`) and the number of reflection-odd factors is
even. So the sunset is a sum over the **572 allowed** typed triples out of `2744`. On the `S₅`
level it is `143` of `343`, and it never involves three holomorphic-type (`[2,1,1,1]`) modes.

## Form of the statement

Following the owner's rule that observations are energy-bounded cuts, the sum runs over a finite
cut `cut : Finset Λ` of opaque eigenvalue labels. The weights `w` and the triple products `C`
live in an arbitrary commutative ring `K`: no real number, limit or eigenvalue value appears. The
selection rule is the structure field `selection`. Its justification (invariance of the
integral under the isometries, and Schur's lemma) is analytic and cited, not formalised.

* `sunset_eq_allowed`: the cut sunset equals its restriction to allowed typed triples.
* `sunset_forbidden_zero`: the forbidden part is zero.
* `sunset_by_type`: the sunset regroups as a sum over the `S₅ × C₂` type triples
  `(a, b, c, pa, pb, pc)` of the partial sunsets, and only allowed ones contribute.
-/

namespace QOU.Transcendental.Brings.SpectralSunset

open QOU.Brings.TripleSelection

/-- A finite, energy-bounded cut of the typed spectrum, with ring-valued weights and triple
products. -/
structure TypedCut (Λ K : Type*) [CommRing K] where
  /-- The labels inside the cut. -/
  cut : Finset Λ
  /-- `w_a`, standing for `1/λ_a`. It is an element of `K`, never evaluated. -/
  weight : Λ → K
  /-- The `S₅` type of the mode `a`. -/
  type : Λ → Fin 7
  /-- The reflection parity of the mode `a` (`true` = odd under `c`). -/
  parity : Λ → Bool
  /-- `C_{abc} = ∫ φ_a φ_b φ_c`. -/
  C : Λ → Λ → Λ → K
  /-- **Selection rule** (cited: invariance plus Schur). -/
  selection : ∀ a b c,
    allowedParity (type a) (type b) (type c) (parity a) (parity b) (parity c) = false →
      C a b c = 0

variable {Λ K : Type*} [CommRing K]

/-- The summand `w_a w_b w_c C_{abc}²`. -/
def TypedCut.term (D : TypedCut Λ K) (a b c : Λ) : K :=
  D.weight a * D.weight b * D.weight c * D.C a b c ^ 2

/-- Whether the triple `(a, b, c)` is allowed by the selection rule. -/
def TypedCut.allowed (D : TypedCut Λ K) (a b c : Λ) : Bool :=
  allowedParity (D.type a) (D.type b) (D.type c) (D.parity a) (D.parity b) (D.parity c)

/-- The cut sunset `Σ_{a,b,c ∈ cut} w_a w_b w_c C_{abc}²`. -/
def TypedCut.sunset (D : TypedCut Λ K) : K :=
  ∑ a ∈ D.cut, ∑ b ∈ D.cut, ∑ c ∈ D.cut, D.term a b c

theorem TypedCut.term_forbidden (D : TypedCut Λ K) (a b c : Λ) (h : D.allowed a b c = false) :
    D.term a b c = 0 := by
  simp [TypedCut.term, D.selection a b c h]

/-- **The sunset is a sum over allowed typed triples only.** -/
theorem sunset_eq_allowed (D : TypedCut Λ K) :
    D.sunset = ∑ a ∈ D.cut, ∑ b ∈ D.cut, ∑ c ∈ D.cut,
      if D.allowed a b c then D.term a b c else 0 := by
  unfold TypedCut.sunset
  refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ =>
    Finset.sum_congr rfl fun c _ => ?_
  by_cases h : D.allowed a b c
  · simp [h]
  · simp only [Bool.not_eq_true] at h
    simp [h, D.term_forbidden a b c h]

/-- **The forbidden part vanishes.** -/
theorem sunset_forbidden_zero (D : TypedCut Λ K) :
    (∑ a ∈ D.cut, ∑ b ∈ D.cut, ∑ c ∈ D.cut,
      if D.allowed a b c then 0 else D.term a b c) = 0 := by
  refine Finset.sum_eq_zero fun a _ => Finset.sum_eq_zero fun b _ =>
    Finset.sum_eq_zero fun c _ => ?_
  by_cases h : D.allowed a b c
  · simp [h]
  · simp only [Bool.not_eq_true] at h
    simp [h, D.term_forbidden a b c h]

/-- The partial sunset of one typed triple `(ta, tb, tc)` with parities `(pa, pb, pc)`. -/
def TypedCut.partial (D : TypedCut Λ K) (ta tb tc : Fin 7) (pa pb pc : Bool) : K :=
  ∑ a ∈ D.cut.filter (fun a => D.type a = ta ∧ D.parity a = pa),
    ∑ b ∈ D.cut.filter (fun b => D.type b = tb ∧ D.parity b = pb),
      ∑ c ∈ D.cut.filter (fun c => D.type c = tc ∧ D.parity c = pc), D.term a b c

/-- **A forbidden typed triple contributes nothing.** -/
theorem partial_forbidden (D : TypedCut Λ K) (ta tb tc : Fin 7) (pa pb pc : Bool)
    (h : allowedParity ta tb tc pa pb pc = false) : D.partial ta tb tc pa pb pc = 0 := by
  unfold TypedCut.partial
  refine Finset.sum_eq_zero fun a ha => Finset.sum_eq_zero fun b hb =>
    Finset.sum_eq_zero fun c hc => ?_
  simp only [Finset.mem_filter] at ha hb hc
  apply D.term_forbidden
  simp only [TypedCut.allowed, ha.2.1, ha.2.2, hb.2.1, hb.2.2, hc.2.1, hc.2.2, h]

/-- **The sunset by type.** The cut sunset is the sum of the partial sunsets over the
`14³` typed triples. By `partial_forbidden`, only the `572` allowed ones
(`allowed_parity_count`) can be nonzero. -/
theorem sunset_by_type [DecidableEq Λ] (D : TypedCut Λ K) :
    D.sunset = ∑ ta : Fin 7 × Bool, ∑ tb : Fin 7 × Bool, ∑ tc : Fin 7 × Bool,
      D.partial ta.1 tb.1 tc.1 ta.2 tb.2 tc.2 := by
  let tp : Λ → Fin 7 × Bool := fun a => (D.type a, D.parity a)
  have key : ∀ (s : Finset Λ) (f : Λ → K), ∑ a ∈ s, f a =
      ∑ t : Fin 7 × Bool, ∑ a ∈ s.filter (fun a => D.type a = t.1 ∧ D.parity a = t.2), f a := by
    intro s f
    rw [← Finset.sum_fiberwise_of_maps_to (g := tp) (t := Finset.univ)
      (fun _ _ => Finset.mem_univ _)]
    refine Finset.sum_congr rfl fun t _ => Finset.sum_congr ?_ fun _ _ => rfl
    ext a
    simp [tp, Prod.ext_iff]
  unfold TypedCut.sunset TypedCut.partial
  rw [key D.cut]
  refine Finset.sum_congr rfl fun ta _ => ?_
  rw [Finset.sum_congr rfl fun a _ => key D.cut (fun b => ∑ c ∈ D.cut, D.term a b c)]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun tb _ => ?_
  rw [Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ =>
    key D.cut (fun c => D.term a b c)]
  rw [Finset.sum_congr rfl fun a _ => Finset.sum_comm]
  rw [Finset.sum_comm]

end QOU.Transcendental.Brings.SpectralSunset
