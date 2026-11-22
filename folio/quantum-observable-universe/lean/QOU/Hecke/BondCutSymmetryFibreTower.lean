/-
# Class D: the fibre-level tower, and why changing the coefficient ring is not
# an escape

`QOU/Hecke/BondCutSymmetry.lean` (#7165, bean `qou-qve5`) excludes **positive
pair-additive bond counts** from supplying the SEMF symmetry energy. Its
enumeration of escapes (#7181) names four classes, of which A and C are blocked
and B is priced (#7204). **Class D is the last untouched row:** *"fibre-level /
higher order in `q` — a Habiro element whose order-zero rendering is the
observable"*, escaping on the ground that *"every #7165 statement is at order
zero"*.

That ground is the thing this file tests. The owner ruling of 2026-09-03 makes
the full tower mandatory rather than optional — *"should make use of the full
tower even though what is observable is only order zero"*, settled the same day
to mean **both** senses, all `n` of the Hecke tower and all orders in `q`. Class
D is the `q`-order sense. (The `n` sense of the same ruling is bean `qou-hu1f` /
`qou-tower`, a different measurement on a different surface; do not conflate
them.)

## What "order zero" can mean, and both readings are handled

**(D-ev) the evaluation reading** — the law is formed over a fibre coefficient
ring `R` (the Habiro ring, `ℤ[q^{±1}]`, `ℚ(q)`, a ring of functions analytic at
`q₀`) and the observable is `τ(x)` for an archimedean rendering `τ : R → K`.
"Order zero" is then the single evaluation.

**(D-co) the coefficient reading** — the fibre object is a series
`Σ_k c_k · e^{(k)}` in some expansion parameter and "order zero" is the `k = 0`
term.

The two need different arguments: `τ` is multiplicative, coefficient extraction
is not.

## The three invariants

**(1) `bondSum` commutes with any ring homomorphism** (`bondSum_map`). So the
*rendering of a fibre-level bond count is a bond count* — with rendered
energies and rendered counts, and with every #7165 theorem applying to it,
hypotheses read on the rendered quantities. `map_bondSum_nonneg` and
`map_bondSum_ne_semf_neutronMatter` are invariant (2) of #7165, transferred.
Class D does not escape the *shape* by changing the coefficient ring.

**(2) `bondSum` is linear in the energy triple with the counts as coefficients**
(`bondSum_add_energies`, `bondSum_mul_energies`, `bondSum_tower`). Linearity is
what coefficient extraction preserves, and it gives the (D-co) statement:
**every order of the tower is separately a bond count, and the tower's bond sum
is the coefficient-weighted sum of the orders' bond sums.** The same holds for
the p–n slope (`energySlope_tower`), so `δ_tower = Σ_k c_k · δ^{(k)}`. Higher
orders in `q` add terms to `δ`; they cannot change that `δ` is the *only*
coupling to the layout, because the cut identity `bondSum = (like-species)/2 +
δ·n_pn` is a ring identity and holds verbatim in the fibre ring.

**(3) Convexity of the interface is a ring identity, not an order-zero
accident** (`interface_affine`). The three canonical letters are the *same*
generator with three *offsets* — `pp = σ`, `nn = σ - h`, `pn = σ - h·u` — and
the two-strand Markov trace is affine in the offset, `tr(σ + d) = z + d`. Hence

```
b_pn = (1 - u)·b_pp + u·b_nn         for every z, every h, every u
```

identically, in any commutative ring. `z` is where the Markov convention lives
and `h = q - q⁻¹` is where the deformation lives, and the identity does not see
either. So a tower that changes `z` or `h` to any order whatsoever leaves the
interface inside the convex hull of the like-species bonds — which is exactly
the hypothesis of `BondCutSymmetryLogBound.energySlope_convex_le`, i.e. of the
`δ ≤ 2 ln q` cap.

**The only door left open** is the offset ratio `u` itself. For the corpus's
letters `u = 1/2 - δ_f/4` with `δ_f = Δm_pn/M_N` the flavour split
(`SymmetrySignAmGm.weight_of_convention`), and `offsetRatio_mem_iff` reduces the
whole question to a two-sided bound on one rendered scalar:

```
0 ≤ u ≤ 1   ⟺   -2 ≤ δ_f ≤ 2
```

The measured `δ_f` is `≈ 1.4e-3`. A tower correction would have to move it by
three orders of magnitude to leave the hull, and `flavour_factor_to_leave_hull`
states that requirement as a lower bound on the correction factor rather than as
a remark.

## Scope

This is a **scope-(b) structural exclusion** of class D *as an independent
escape class*, in the sense of AGENTS.md §"Before declaring refuted": the
invariants cited are a ring homomorphism's compatibility with a polynomial, the
linearity of `bondSum` in its energy arguments, and an affine identity — none of
them numerical estimates. What is excluded is that **changing the coefficient
ring from `ℝ`-at-`q₀` to a fibre ring, by itself, buys nothing**: the rendered
law is still a bond count, its interface is still convex, and it is therefore
still inside #7165's caps. It is **not** an exclusion of every conceivable
fibre-level construction: a law that is not of the `bondSum` shape is class A or
C, a rendered energy that is negative is class B, and both are governed
elsewhere.

Two hypotheses are carried explicitly rather than assumed, in the `_of_` style
of AGENTS.md §"Conditional-proved ≠ premise-established":

* **that the rendering is a ring homomorphism.** Evaluation of an analytic
  function at `q₀` is; evaluation of a general Habiro element at a
  non-root-of-unity point is not defined at all (bean `qou-ix0x` item 4). Where
  the rendering fails to be a ring map, `bondSum_map` says nothing.
* **that the crossing multiplicity is the canonical `m = 1`.** The trace of
  `(σ + d)^m` is affine in `d` only at `m = 1`, so `interface_affine` applies at
  the canonical multiplicity and not to the `m`-sweep. That sweep is a discrete
  parameter, is separately measured (bean `qou-ib3g`; #7204 R9 reaches
  `5.963 MeV` against a `23.7 MeV` target), and choosing an `m` for its residual
  is the fit AGENTS.md §NO FITTING forbids.

Producer: `computations/qbeta/qbeta_class_d_fibre_tower_probe.py`.
Archimedean sibling (§7c): `QOU/Hecke/BondCutSymmetryFibreTowerBound.lean`.
Builds on `QOU/Hecke/BondCutSymmetry.lean` (`qou-qve5`),
`QOU/Hecke/BondCutSymmetryNoSignDefinite.lean` (class B, #7204),
`QOU/Mass/MultiplicityNotExtensive.lean` (class C, #7181). Bean `qou-brng`.
-/

import QOU.Hecke.BondCutSymmetry

namespace QOU.Hecke.BondCutSymmetryFibreTower

open QOU.Hecke.BondCutSymmetry

/-! ## Part 1 — (D-ev): the rendering of a fibre bond count is a bond count -/

section Ring

variable {R S : Type*} [CommRing R] [CommRing S]

/-- **`bondSum` commutes with every ring homomorphism.** The bond sum is a
polynomial in its six arguments with integer coefficients, so any ring map
carries it to the bond sum of the images. Read right to left this is the whole
of the (D-ev) reading of class D: forming the law in a fibre ring and rendering
at the end gives exactly the same thing as rendering the ingredients and forming
the law at order zero. -/
theorem bondSum_map (τ : R →+* S) (epp epn enn npp npn nnn : R) :
    τ (bondSum epp epn enn npp npn nnn)
      = bondSum (τ epp) (τ epn) (τ enn) (τ npp) (τ npn) (τ nnn) := by
  unfold bondSum
  simp only [map_add, map_mul]

/-- The cut identity survives the rendering, since both sides are ring
expressions: if the degree-sum hypotheses hold in the fibre ring they hold in
the image, so the rendered law has the same one-parameter layout dependence. -/
theorem two_mul_bondSum_map (τ : R →+* S) (epp epn enn npp npn nnn dP dN : R)
    (hP : 2 * npp + npn = dP) (hN : 2 * nnn + npn = dN) :
    2 * τ (bondSum epp epn enn npp npn nnn)
      = τ epp * τ dP + τ enn * τ dN + (2 * τ epn - τ epp - τ enn) * τ npn := by
  have h := congrArg τ (two_mul_bondSum epp epn enn npp npn nnn dP dN hP hN)
  simpa only [map_add, map_mul, map_sub, map_ofNat] using h

/-! ## Part 2 — (D-co): `bondSum` is linear in the energies, so the tower
splits order by order -/

/-- **The bond sum is additive in the energy triple.** The counts are fixed, so
adding two energy triples adds the bond sums. This is the property coefficient
extraction preserves and a ring map's multiplicativity is irrelevant to. -/
theorem bondSum_add_energies (epp epn enn epp' epn' enn' npp npn nnn : R) :
    bondSum (epp + epp') (epn + epn') (enn + enn') npp npn nnn
      = bondSum epp epn enn npp npn nnn + bondSum epp' epn' enn' npp npn nnn := by
  unfold bondSum
  ring

/-- **The bond sum is homogeneous in the energy triple.** Scaling all three
energies by a common factor scales the bond sum. Together with additivity this
is linearity. -/
theorem bondSum_mul_energies (c epp epn enn npp npn nnn : R) :
    bondSum (c * epp) (c * epn) (c * enn) npp npn nnn
      = c * bondSum epp epn enn npp npn nnn := by
  unfold bondSum
  ring

/-- A zero energy triple gives a zero bond sum, whatever the counts. The base
case of the tower, recorded so `bondSum_tower` is visibly a decomposition
rather than an approximation. -/
theorem bondSum_zero_energies (npp npn nnn : R) :
    bondSum (0 : R) 0 0 npp npn nnn = 0 := by
  unfold bondSum
  ring

/-- **The tower decomposition: every order is separately a bond count.** If each
energy is a finite combination `Σ_k c_k · e_t^{(k)}` — a truncated fibre-level
expansion in any parameter, with the *same* coefficients `c_k` for the three
species because they are orders of one expansion — then the bond sum is the
coefficient-weighted sum of the per-order bond sums.

This is the (D-co) reading of class D, and it is the reason the class buys no
new functional form: "all orders in `q`" produces a *sum of bond counts*, and a
sum of bond counts is a bond count. -/
theorem bondSum_tower {ι : Type*} (s : Finset ι) (c epp epn enn : ι → R)
    (npp npn nnn : R) :
    bondSum (∑ k ∈ s, c k * epp k) (∑ k ∈ s, c k * epn k) (∑ k ∈ s, c k * enn k)
        npp npn nnn
      = ∑ k ∈ s, c k * bondSum (epp k) (epn k) (enn k) npp npn nnn := by
  classical
  refine Finset.induction_on s ?_ ?_
  · simp [bondSum]
  · intro a t ha ih
    rw [Finset.sum_insert ha, Finset.sum_insert ha, Finset.sum_insert ha,
      Finset.sum_insert ha, bondSum_add_energies, bondSum_mul_energies, ih]

/-! ## Part 3 — the affine-offset identity: convexity is a ring identity -/

/-- **The two-strand Markov trace of the letter `σ + d`.** The trace is affine
in the offset — `tr(c·σ + d) = c·z + d` for the Markov parameter `z` — and the
canonical letters all have `c = 1`, so the trace is `z + d`. This is the form
`atom_braid_word_3A` emits: `pp = σ` (`d = 0`), `nn = σ - h` (`d = -h`),
`pn = σ - h·u` (`d = -h·u`), with `h = q - q⁻¹`. -/
def letterTrace (z d : R) : R := z + d

/-- **The interface bond is a convex combination of the like-species bonds, by a
ring identity.** For every Markov parameter `z`, every deformation `h` and every
offset ratio `u`,

```
b_pn = (1 - u)·b_pp + u·b_nn
```

exactly. The identity does not mention `z` or `h` except through the three
traces themselves, so it is insensitive to the Markov convention, to the value
of `q`, and to *every order of any fibre-level expansion of either*. Convexity
of the corpus's interface is therefore not a numerical fact about `q₀` that a
higher-order term could spoil; it is an algebraic consequence of the three
letters being one generator with three offsets. -/
theorem interface_affine (z h u : R) :
    letterTrace z (-(h * u))
      = (1 - u) * letterTrace z 0 + u * letterTrace z (-h) := by
  unfold letterTrace
  ring

/-- The same identity in the `w = 1 - u` letters of
`BondCutSymmetryLogBound.interface`, which weights `b_pp` rather than `b_nn`. -/
theorem interface_affine_weight (z h w : R) :
    letterTrace z (-(h * (1 - w)))
      = w * letterTrace z 0 + (1 - w) * letterTrace z (-h) := by
  unfold letterTrace
  ring

/-- The identity is carried by any ring map, so the *rendered* interface is the
convex combination of the *rendered* like-species bonds with the *rendered*
ratio. Nothing about the hull is created or destroyed by the rendering. -/
theorem interface_affine_map (τ : R →+* S) (z h u : R) :
    τ (letterTrace z (-(h * u)))
      = (1 - τ u) * τ (letterTrace z 0) + τ u * τ (letterTrace z (-h)) := by
  have hmap := congrArg τ (interface_affine z h u)
  simpa only [letterTrace, map_add, map_mul, map_sub, map_neg, map_one] using hmap

/-! ### The same argument reaches the dominant-summand channel

`QOU/Mass/OneRowBlockLetterProduct.lean` (#7200, bean `qou-m8f3`) proves that a
one-dimensional block's character of a word of letters `c·σ_g + d·1` is the
**product over the letters** of `c·q + d` — an algebra-homomorphism identity,
stated there over a generic `[CommRing R]`. Its consequence is that the dominant
summand's log-weight `L = log|y_λ χ^λ(β_A)|` is a **sum over letters**, hence
chain-edge additive with no connected many-body term.

`bondSum_tower` does not reach that channel directly, because `Real.log` is not
linear in the bond factors, so the per-order decomposition has to be taken on
the *letter contributions* rather than on the factors. The statement below is
what carries it: a sum over letters whose summands are each expanded in the
tower is, at every order, **again a sum over the same letters**.

The algebra is elementary — it is `Finset.sum_comm` plus distributivity. What is
not elementary is *which index set survives*, and the answer is: the letters. So
"all orders in `q`" leaves the dominant-summand channel pair-additive on exactly
the bond set it was pair-additive on at order zero, and #7200's scope-(b)
negative is inherited by every order rather than being an order-zero artefact.
It says nothing about the *size* of any order's coefficient. -/
theorem letterSum_tower {ι κ : Type*} (s : Finset ι) (t : Finset κ)
    (c : κ → R) (f : ι → κ → R) :
    ∑ i ∈ s, ∑ k ∈ t, c k * f i k = ∑ k ∈ t, c k * ∑ i ∈ s, f i k := by
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [Finset.mul_sum]

end Ring

/-! ## Part 4 — the slope splits order by order (field) -/

section Field

variable {K L : Type*} [Field K] [Field L]

/-- **The p–n slope commutes with a field homomorphism.** `δ` is a second
difference divided by two, and a ring map between fields carries both. -/
theorem energySlope_map (τ : K →+* L) (epp epn enn : K) :
    τ (energySlope epp epn enn) = energySlope (τ epp) (τ epn) (τ enn) := by
  unfold energySlope
  rw [map_sub, map_div₀, map_add, map_ofNat]

/-- The slope is additive in the energy triple. -/
theorem energySlope_add (epp epn enn epp' epn' enn' : K) :
    energySlope (epp + epp') (epn + epn') (enn + enn')
      = energySlope epp epn enn + energySlope epp' epn' enn' := by
  unfold energySlope
  ring

/-- The slope is homogeneous in the energy triple. -/
theorem energySlope_mul (c epp epn enn : K) :
    energySlope (c * epp) (c * epn) (c * enn) = c * energySlope epp epn enn := by
  unfold energySlope
  ring

/-- **`δ_tower = Σ_k c_k · δ^{(k)}`.** The tower's p–n slope is the
coefficient-weighted sum of the per-order slopes — so "all orders in `q`" is a
statement about the *value* of `δ`, never about the *form* of the law. Through
`BondCutSymmetry.bondSum_wellMixed_symmetry` the same holds of the symmetry
coefficient, whose only ingredient is `δ`. -/
theorem energySlope_tower {ι : Type*} (s : Finset ι) (c epp epn enn : ι → K) :
    energySlope (∑ k ∈ s, c k * epp k) (∑ k ∈ s, c k * epn k)
        (∑ k ∈ s, c k * enn k)
      = ∑ k ∈ s, c k * energySlope (epp k) (epn k) (enn k) := by
  classical
  refine Finset.induction_on s ?_ ?_
  · simp [energySlope]
  · intro a t ha ih
    rw [Finset.sum_insert ha, Finset.sum_insert ha, Finset.sum_insert ha,
      Finset.sum_insert ha, energySlope_add, energySlope_mul, ih]

/-- **The corpus's offset ratio.** `SymmetrySignAmGm.weight_of_convention`
derives the p–n interface letter as `σ - h·(1/2 - δ_f/4)` with `δ_f =
Δm_pn/M_N`, so the offset ratio of `interface_affine` is `u = 1/2 - δ_f/4` and
the `BondCutSymmetryLogBound` weight is `w = 1 - u = 1/2 + δ_f/4`. -/
def offsetRatio (df : K) : K := 1 / 2 - df / 4

/-- The corpus's interface, as an instance of `interface_affine`. -/
theorem interface_flavour (z h df : K) :
    letterTrace z (-(h * offsetRatio df))
      = (1 - offsetRatio df) * letterTrace z 0
        + offsetRatio df * letterTrace z (-h) :=
  interface_affine z h (offsetRatio df)

end Field

/-! ## Part 5 — where the last door is, and how wide (ordered field) -/

section OrderedField

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **The whole of class D's remaining freedom, reduced to one scalar bound.**
The offset ratio lies in `[0, 1]` — the hypothesis of the `δ ≤ 2 ln q` cap —
exactly when the rendered flavour split lies in `[-2, 2]`. Everything else about
the tower has already been absorbed by `interface_affine`, which does not see
`z`, `h`, or any order of either. -/
theorem offsetRatio_mem_iff {df : K} :
    (0 ≤ offsetRatio df ∧ offsetRatio df ≤ 1) ↔ (-2 ≤ df ∧ df ≤ 2) := by
  unfold offsetRatio
  constructor
  · rintro ⟨h1, h2⟩
    constructor <;> linarith
  · rintro ⟨h1, h2⟩
    constructor <;> linarith

/-- The convenient direction: a small positive flavour split keeps the interface
inside the hull. The corpus's `δ_f ≈ 1.4e-3` satisfies this with three orders of
magnitude to spare. -/
theorem offsetRatio_mem_of_small {df : K} (h0 : 0 < df) (h2 : df ≤ 2) :
    0 ≤ offsetRatio df ∧ offsetRatio df ≤ 1 :=
  offsetRatio_mem_iff.mpr ⟨by linarith, h2⟩

/-- **The price of leaving the hull, as a factor on the flavour split.** If the
fibre-level tower renders the flavour split as `c · df₀` for a positive leading
value `df₀`, then leaving the convex hull requires `c > 2/df₀`. With the
measured `df₀ ≈ 1.4e-3` that is a correction factor above `1.4e3`: not a
higher-order term but a replacement of the leading one. -/
theorem flavour_factor_to_leave_hull {c df₀ : K} (hdf : 0 < df₀)
    (hout : ¬(0 ≤ offsetRatio (c * df₀) ∧ offsetRatio (c * df₀) ≤ 1)) :
    c < -2 / df₀ ∨ 2 / df₀ < c := by
  rw [offsetRatio_mem_iff] at hout
  push_neg at hout
  rcases lt_or_ge (c * df₀) (-2) with hlt | hge
  · left
    rw [lt_div_iff₀ hdf]
    linarith
  · right
    have h2 : 2 < c * df₀ := hout hge
    rw [div_lt_iff₀ hdf]
    linarith

/-! ### Invariant (2) of #7165, transferred through the rendering -/

variable {R : Type*} [CommRing R]

/-- **A fibre-level bond count with non-negative rendered ingredients renders
non-negative.** `BondCutSymmetry.bondSum_nonneg` applied to the image, which is
legitimate precisely because `bondSum_map` says the image *is* a bond sum. -/
theorem map_bondSum_nonneg (τ : R →+* K) {epp epn enn npp npn nnn : R}
    (hepp : 0 ≤ τ epp) (hepn : 0 ≤ τ epn) (henn : 0 ≤ τ enn)
    (hpp : 0 ≤ τ npp) (hpn : 0 ≤ τ npn) (hnn : 0 ≤ τ nnn) :
    0 ≤ τ (bondSum epp epn enn npp npn nnn) := by
  rw [bondSum_map]
  exact bondSum_nonneg hepp hepn henn hpp hpn hnn

/-- **Class D does not escape invariant (2).** A fibre-level pair-additive bond
count whose rendered energies and counts are non-negative cannot reproduce the
SEMF at pure neutron matter — for every coefficient ring, every ring-map
rendering, every graph and every interface.

The escape hypothesis of class D was that #7165's statements are "at order
zero"; this says that being at order zero was never what they used. What they
use is the shape and the sign of the *rendered* quantities, and a ring map
delivers the shape unchanged. A tower therefore reaches invariant (2) only by
rendering some energy negative — which is class B, with class B's price
(`BondCutSymmetryNoSignDefinite.enn_neg_of_semf_neutronMatter`) and class B's
unchanged `δ ≤ 2 ln q` cap. -/
theorem map_bondSum_ne_semf_neutronMatter (τ : R →+* K)
    {epp epn enn npp npn nnn : R} {E0 aV aA A : K}
    (hepp : 0 ≤ τ epp) (hepn : 0 ≤ τ epn) (henn : 0 ≤ τ enn)
    (hpp : 0 ≤ τ npp) (hpn : 0 ≤ τ npn) (hnn : 0 ≤ τ nnn)
    (hE0 : 0 ≤ E0) (hA : 0 < A) (h : aV < aA) :
    E0 * τ (bondSum epp epn enn npp npn nnn) ≠ aV * A - aA * (A * A / A) := by
  rw [bondSum_map]
  exact bondSum_ne_semf_neutronMatter hepp hepn henn hpp hpn hnn hE0 hA h

end OrderedField

/-! ## Non-vacuity

The transfer theorems are conditionals over an abstract rendering, so they are
checked here against a rendering that exists. Guards against the failure mode of
AGENTS.md §"No trivial trues": the hypotheses are satisfiable and the conclusion
is a genuine disequality. -/

example : (1 : ℚ) * (RingHom.id ℚ) (bondSum 1 1 1 1 1 1) ≠ 1 * 1 - 2 * (1 * 1 / 1) :=
  map_bondSum_ne_semf_neutronMatter (RingHom.id ℚ) (by norm_num) (by norm_num)
    (by norm_num) (by norm_num) (by norm_num) (by norm_num) (by norm_num)
    (by norm_num) (by norm_num)

/-- The affine identity is not vacuous either: at `u = 1/2` it says the
interface is the arithmetic mean of the like-species bonds, which is where the
corpus sits to within `δ_f/4 ≈ 3.5e-4`. -/
example (z h : ℚ) :
    letterTrace z (-(h * (1 / 2))) = (1 / 2) * letterTrace z 0 + (1 / 2) * letterTrace z (-h) := by
  have := interface_affine z h (1 / 2 : ℚ)
  norm_num at this ⊢
  linarith [this]

end QOU.Hecke.BondCutSymmetryFibreTower
