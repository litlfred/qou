/-
# Bond counting on a coloured graph: the cut identity, and why no interface
# weight can supply the symmetry energy

The adopted binding law (owner ruling 2026-09-04, Option B) is a **pair-additive
bond count**: `B = E₀ · (e_pp·n_pp + e_pn·n_pn + e_nn·n_nn)` with the per-bond
energies `e = -ln b` derived from the closed-form Markov factors and the pair
counts `n_t` read off a bond graph on the `Z + N` nucleons. The residual is
shape, not scale (arc synthesis 2026-09-05 §6), and its dominant shape is the
SEMF symmetry term `-a_A (N-Z)²/A` — which the framework's own isospin
weighting produces with the **wrong sign**.

This file states the hypothesis class precisely and proves the invariants the
whole class satisfies, so that no numeric scan over edge sets is needed to know
what a bond count can and cannot do. Nothing here fits anything: every SEMF
number appears only as a *target* the derived quantities are checked against.

## The cut identity

For any graph and any proton/neutron colouring, the degree-sum formula on each
colour class reads `2 n_pp + n_pn = d_P` and `2 n_nn + n_pn = d_N`, where `d_P`
is the total degree of the protons. Substituting,

```
2 B = e_pp·d_P + e_nn·d_N + (2 e_pn - e_pp - e_nn)·n_pn          (two_mul_bondSum)
  B = (e_pp·d_P + e_nn·d_N)/2 + δ·n_pn,   δ = e_pn - (e_pp+e_nn)/2   (bondSum_eq_cut)
```

**The entire dependence of a bond count on the layout runs through one number,
the p–n cut `n_pn`, with one coefficient, `δ`.** This is
`SymmetrySignAmGm`'s decomposition with the graph put back in: for a `k`-regular
graph `d_P = kZ`, `d_N = kN`, so the like-species part is *linear* in `(Z, N)`
and the symmetry energy — whatever curvature in `N - Z` the law has — is
`δ · n_pn(Z, N)`. Two consequences fall out at once:

* **Segregated layouts carry no symmetry term.** If the cut is a constant
  (the canonical `A-1` chain has `n_pn = 1`), the law is affine in `(Z, N)`
  for every choice of the three energies (`bondSum_segregated_sub`).
* **Well-mixed layouts carry exactly one.** With the mean-field cut
  `n_pn = μ·Z·N` and `4ZN = A² - (N-Z)²`, the `A²` and `(N-Z)²` terms have
  equal and opposite coefficients `± δμ/4` (`bondSum_wellMixed`). The SEMF
  sign is `δ > 0`, i.e. `e_pn > (e_pp+e_nn)/2` (`symmetryCoeff_pos_iff`) —
  the AM-vs-GM statement, now with the power attached under a labelled
  mean-field hypothesis.

## The two invariants that exclude the class

**(1) The convex interface bounds `δ` by `2 ln q`.** The corpus's p–n bond is a
convex combination `b_pn = w·b_pp + (1-w)·b_nn` (`SymmetrySignAmGm`,
`weight_of_convention`). For any `w ∈ [0,1]` the interface lies between the two
like-species bonds, so `δ ≤ (e_nn - e_pp)/2`, and with the pinned
`b_pp = q²/[2]_q`, `b_nn = q⁻²/[2]_q` that is **exactly `2 ln q`**
(`energySlope_convex_le`, `energySlope_convex_le_two_log`). At `q₀` this is
`0.2087`; the corpus's actual `δ` is `-0.0218`. So the *whole* convex family —
every interface weight, including those that flip the sign — has a symmetry
coefficient at most `(μ/2)·ln q`. In MeV, on a degree-`k` graph, at most
`(k/2)·E₀·ln q ≈ 2.6 MeV` at `k = 12`, against the SEMF `a_A ≈ 23 MeV`.
Flipping the sign is cheap; supplying the magnitude is not available to any
interface weight.

**(2) Positivity forbids the SEMF magnitude outright, layout-free.** Every bond
energy is `-ln b` with `0 < b < 1`, so positive; every pair count is a count.
A bond sum is therefore **non-negative at every composition, including pure
neutron matter** (`bondSum_nonneg`). The SEMF symmetry term is larger than its
volume term (`a_A/a_V ≈ 1.5`, AME2020 — a measured target), which is precisely
the statement that neutron matter is *unbound*: `a_V·A - a_A·A < 0`
(`semf_neutronMatter_neg`). No pair-additive bond count with non-negative
energies agrees with that, on any graph, with any interface
(`bondSum_ne_semf_neutronMatter`). This is the synthesis's "unbound systems
are outside it by construction" (§6 item 3) recognised as the *same* fact as
the missing symmetry energy.

## The `O(ℏ_q²)` question, answered by sign

Could a second-order correction to `b_pn` flip `δ`? The miss of the convex
weight against the crossing `1/(q²+1)` is `(q²-1)/(2(q²+1)) + δ_f/4`
(`SymmetrySignAmGm.weight_miss`). Its first part is **at least `ℏ_q/2`** with
`ℏ_q = (q-1)/q` (`weight_miss_ge_half_hbar`) — first order, not second — and its
second part, the flavour tilt, has the derived sign `δ_f > 0` (the neutron is
heavier) and pushes the weight *up*, away from the crossing
(`flavour_tilt_wrong_direction`). So an `O(ℏ_q²)` correction cannot flip the
sign unless its coefficient exceeds `1/(2ℏ_q) ≈ 5`, and the one derived
sub-leading ingredient in `w` has the wrong sign anyway. And by invariant (1),
even a flipped sign is an order of magnitude short.

## What is and is not proved

Everything in this file is proved for arbitrary energies and counts over a
generic ring or ordered field (§7c); the substrate enters only through the
*hypotheses* `0 < b < 1`, `1 < q`, `0 < δ_f`, which are measurement. The
archimedean specialisation — the `e = -ln b` letters, the convex interface
and the `2 ln q` bound of invariant (1) — lives in the sibling
`QOU/Hecke/BondCutSymmetryLogBound.lean`, which consumes this file. The mean-field cut
`n_pn = μZN` is a **labelled model**, used only in `bondSum_wellMixed` and
`symmetryCoeff_pos_iff`; invariants (1) and (2) do not use it. Nothing here
touches the closed-form Markov factors, `RowCap`, or the Wigner-term route in
the mass channel (bean `qou-a5jk`), which is a different functional.

Producer: `computations/qbeta/qbeta_bond_cut_symmetry_shape_probe.py`.
Builds on `QOU/Hecke/SymmetrySignAmGm.lean` (bean `qou-i01a`),
`QOU/Hecke/BoundedDegreeCoulomb.lean` (`qou-556v`),
`QOU/Mass/CoordinationSaturation.lean`. Bean `qou-qve5`.
-/

import Mathlib.Tactic

namespace QOU.Hecke.BondCutSymmetry

/-! ## The bond count and the cut identity (generic commutative ring) -/

section Ring

variable {R : Type*} [CommRing R]

/-- A pair-additive bond-counting law: three per-bond energies against three
pair counts. Under Option B the energies are `e_t = -ln b_t` and the counts
are read off a bond graph; nothing below depends on either reading. -/
def bondSum (epp epn enn npp npn nnn : R) : R :=
  epp * npp + epn * npn + enn * nnn

/-- **The cut identity, ring form.** If the proton and neutron colour classes
have total degrees `d_P` and `d_N` — the degree-sum formula on each class,
`2 n_pp + n_pn = d_P`, `2 n_nn + n_pn = d_N` — then twice the bond sum is the
like-species degree sum plus the cut weighted by `2 e_pn - e_pp - e_nn`. No
graph structure beyond the two degree sums is used. -/
theorem two_mul_bondSum (epp epn enn npp npn nnn dP dN : R)
    (hP : 2 * npp + npn = dP) (hN : 2 * nnn + npn = dN) :
    2 * bondSum epp epn enn npp npn nnn
      = epp * dP + enn * dN + (2 * epn - epp - enn) * npn := by
  subst hP hN
  unfold bondSum
  ring

/-- `4ZN = (Z+N)² - (N-Z)²`: the mean-field cut is a difference of the volume
square and the asymmetry square, with equal and opposite coefficients. -/
theorem four_mul_ZN (Z N : R) : 4 * (Z * N) = (Z + N) ^ 2 - (N - Z) ^ 2 := by
  ring

/-- **Isobaric mirror difference of `bondSum` on `k`-regular colour classes (`qou-qve5`).**
When the proton and neutron colour classes have degrees `k * Z` and `k * N` and both mirror
nuclei `(Z, N)` and `(N, Z)` share the same cut `2 * npn`, the mirror difference
`bondSum epp epn enn (k * Z - npn) (2 * npn) (k * N - npn) - bondSum epp epn enn (k * N - npn) (2 * npn) (k * Z - npn)`
equals `k * (epp - enn) * (Z - N)`, independent of `epn` and `npn`. -/
theorem bondSum_mirror_diff_cut_invariant (epp epn enn k Z N npn : R) :
    bondSum epp epn enn (k * Z - npn) (2 * npn) (k * N - npn) -
      bondSum epp epn enn (k * N - npn) (2 * npn) (k * Z - npn) =
      k * (epp - enn) * (Z - N) := by
  unfold bondSum
  ring

end Ring

/-! ## Layouts: what the cut does to the composition dependence (field) -/

section Field

variable {K : Type*} [Field K] [CharZero K]

/-- The p–n slope: the change in the bond sum when one like-species pair of
half-bonds is traded for a p–n bond. In the corpus's letters this is
`SymmetrySignAmGm.delta` with `e = -ln b` (`BondCutSymmetryLogBound.energySlope_eq_log_form`).
Needs division by `2`, hence a field. -/
def energySlope (epp epn enn : K) : K :=
  epn - (epp + enn) / 2

/-- **The cut identity.** The bond sum is the like-species degree sum, halved,
plus the p–n cut times the slope `δ`. The whole layout dependence is `δ · n_pn`. -/
theorem bondSum_eq_cut (epp epn enn npp npn nnn dP dN : K)
    (hP : 2 * npp + npn = dP) (hN : 2 * nnn + npn = dN) :
    bondSum epp epn enn npp npn nnn
      = (epp * dP + enn * dN) / 2 + energySlope epp epn enn * npn := by
  subst hP hN
  unfold bondSum energySlope
  ring

/-- **The canonical `A-1` chain, as an instance.** Segregated `p…p n…n` with
`Z-1` p–p edges, one p–n edge and `N-1` n–n edges is the corpus's law
`(Z-1)e_pp + e_pn + (N-1)e_nn`; its endpoint degrees are `2Z-1` and `2N-1`
and its cut is `1`. -/
theorem bondSum_chain (epp epn enn Z N : K) :
    bondSum epp epn enn (Z - 1) 1 (N - 1)
      = (epp * (2 * Z - 1) + enn * (2 * N - 1)) / 2 + energySlope epp epn enn * 1 := by
  unfold bondSum energySlope
  ring

/-- **A constant cut carries no symmetry term.** On a `k`-regular graph whose
p–n cut is a constant `c` (every segregated layout; the chain has `c = 1`),
the difference of the bond sums at two compositions is *linear* in the
composition difference, with only the like-species energies — for every
`e_pp, e_pn, e_nn`. There is no `(N-Z)²` to have a sign. -/
theorem bondSum_segregated_sub (epp epn enn k c Z N Z' N' : K) :
    bondSum epp epn enn ((k * Z - c) / 2) c ((k * N - c) / 2)
      - bondSum epp epn enn ((k * Z' - c) / 2) c ((k * N' - c) / 2)
      = k / 2 * (epp * (Z - Z') + enn * (N - N')) := by
  unfold bondSum
  ring

/-- **The well-mixed (mean-field) layout carries exactly one symmetry term.**
With cut `n_pn = μ·Z·N` on a `k`-regular graph, the bond sum is the like-species
line plus `δμ/4` times `(A² - (N-Z)²)`: the mixing contribution to the volume
term and the symmetry term have the *same* coefficient, opposite signs.

This is the only place the mean-field model enters. It is a model, not a
theorem about the braid: it is what "well-mixed" means. -/
theorem bondSum_wellMixed (epp epn enn k μ Z N : K) :
    bondSum epp epn enn ((k * Z - μ * Z * N) / 2) (μ * Z * N) ((k * N - μ * Z * N) / 2)
      = k / 2 * (epp * Z + enn * N)
        + energySlope epp epn enn * μ / 4 * ((Z + N) ^ 2 - (N - Z) ^ 2) := by
  unfold bondSum energySlope
  ring

/-- The coefficient of `-(N-Z)²` in the well-mixed law: `a_A`-like, positive
means the SEMF sign. -/
def symmetryCoeff (epp epn enn μ : K) : K :=
  energySlope epp epn enn * μ / 4

theorem bondSum_wellMixed_symmetry (epp epn enn k μ Z N : K) :
    bondSum epp epn enn ((k * Z - μ * Z * N) / 2) (μ * Z * N) ((k * N - μ * Z * N) / 2)
      = k / 2 * (epp * Z + enn * N) + symmetryCoeff epp epn enn μ * (Z + N) ^ 2
        - symmetryCoeff epp epn enn μ * (N - Z) ^ 2 := by
  rw [bondSum_wellMixed]
  unfold symmetryCoeff
  ring

end Field

/-! ## Signs and bounds (ordered field) -/

section OrderedField

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **The SEMF sign is `δ > 0`.** The symmetry coefficient is positive — the
law binds symmetric nuclei more — exactly when the p–n energy exceeds the
arithmetic mean of the like-species energies. With `e = -ln b` that is
`b_pn < √(b_pp b_nn)`: `SymmetrySignAmGm.delta_nonpos_iff`, with the power
attached. -/
theorem symmetryCoeff_pos_iff {epp epn enn μ : K} (hμ : 0 < μ) :
    0 < symmetryCoeff epp epn enn μ ↔ (epp + enn) / 2 < epn := by
  unfold symmetryCoeff energySlope
  constructor
  · intro h
    by_contra hc
    push_neg at hc
    have : (epn - (epp + enn) / 2) * μ / 4 ≤ 0 := by
      have h1 : epn - (epp + enn) / 2 ≤ 0 := by linarith
      have h2 : (epn - (epp + enn) / 2) * μ ≤ 0 :=
        mul_nonpos_of_nonpos_of_nonneg h1 hμ.le
      linarith
    linarith
  · intro h
    have h1 : 0 < epn - (epp + enn) / 2 := by linarith
    have : 0 < (epn - (epp + enn) / 2) * μ := mul_pos h1 hμ
    linarith

/-- **The cut is bounded by the smaller colour class times the degree bound.**
From the degree-sum identities with non-negative like-species counts and a
degree bound `d`, `n_pn ≤ d·Z` and `n_pn ≤ d·N`. So on any bounded-degree
graph the layout-dependent part `δ·n_pn` is at most `|δ|·d·min(Z, N)` — a
chain (`d = 2`) can move the law by at most `2|δ|·min(Z,N)`, which is linear
in `|N-Z|` at fixed `A`, never quadratic. -/
theorem cut_le_degree_bound {npp npn nnn dP dN d Z N : K}
    (hP : 2 * npp + npn = dP) (hN : 2 * nnn + npn = dN)
    (hpp : 0 ≤ npp) (hnn : 0 ≤ nnn)
    (hdP : dP ≤ d * Z) (hdN : dN ≤ d * N) :
    npn ≤ d * Z ∧ npn ≤ d * N := by
  constructor <;> linarith

/-- **A bond sum is non-negative at every composition.** Non-negative energies
against non-negative counts. Pure neutron matter (`Z = 0`, `n_pp = n_pn = 0`)
is a composition like any other, so the law binds it. -/
theorem bondSum_nonneg {epp epn enn npp npn nnn : K}
    (hepp : 0 ≤ epp) (hepn : 0 ≤ epn) (henn : 0 ≤ enn)
    (hpp : 0 ≤ npp) (hpn : 0 ≤ npn) (hnn : 0 ≤ nnn) :
    0 ≤ bondSum epp epn enn npp npn nnn := by
  unfold bondSum
  have := mul_nonneg hepp hpp
  have := mul_nonneg hepn hpn
  have := mul_nonneg henn hnn
  linarith

/-- **The SEMF with `a_A > a_V` unbinds neutron matter.** At `Z = 0` the
asymmetry `(N-Z)²/A` equals `A`, so the volume and symmetry terms combine to
`(a_V - a_A)·A < 0`. The surface and pairing terms only lower it further.
`a_A > a_V` is what AME2020 measures (`≈ 23` against `≈ 16` MeV); it enters
here as a hypothesis, never as a fit. -/
theorem semf_neutronMatter_neg {aV aA A : K} (hA : 0 < A) (h : aV < aA) :
    aV * A - aA * (A * A / A) < 0 := by
  have hA0 : A ≠ 0 := ne_of_gt hA
  have : A * A / A = A := by field_simp
  rw [this]
  nlinarith

/-- **No pair-additive bond count with non-negative energies agrees with the
SEMF at pure neutron matter** — on any graph, with any interface, at any
scale `E₀ > 0`. The left side is `≥ 0` and the right side is `< 0`. This is the
layout-free form of "the bond count cannot supply the symmetry energy": the
magnitude the data demands is the magnitude that makes neutron matter unbound,
and positive bond energies cannot unbind anything. -/
theorem bondSum_ne_semf_neutronMatter {epp epn enn npp npn nnn E0 aV aA A : K}
    (hepp : 0 ≤ epp) (hepn : 0 ≤ epn) (henn : 0 ≤ enn)
    (hpp : 0 ≤ npp) (hpn : 0 ≤ npn) (hnn : 0 ≤ nnn)
    (hE0 : 0 ≤ E0) (hA : 0 < A) (h : aV < aA) :
    E0 * bondSum epp epn enn npp npn nnn ≠ aV * A - aA * (A * A / A) := by
  intro heq
  have hl : 0 ≤ E0 * bondSum epp epn enn npp npn nnn :=
    mul_nonneg hE0 (bondSum_nonneg hepp hepn henn hpp hpn hnn)
  have hr := semf_neutronMatter_neg hA h
  linarith

/-! ### The interface weight: first-order miss, and the flavour tilt's sign -/

/-- **The miss against the crossing is first order in `ℏ_q`.** With
`ℏ_q = (q-1)/q`, the deformation part of `SymmetrySignAmGm.weight_miss`
satisfies `(q²-1)/(2(q²+1)) ≥ ℏ_q/2` for every `q ≥ 1` — the difference is
`(q-1)²/(2q(q²+1)) ≥ 0`. So a correction of order `ℏ_q²` cannot close it unless
its coefficient is at least `1/(2ℏ_q)`, which at `q₀` is about `5`. -/
theorem weight_miss_ge_half_hbar {q : K} (hq : 1 ≤ q) :
    (q - 1) / (2 * q) ≤ (q ^ 2 - 1) / (2 * (q ^ 2 + 1)) := by
  have hq0 : 0 < q := by linarith
  have h1 : 0 < q ^ 2 + 1 := by positivity
  rw [div_le_div_iff₀ (by positivity) (by positivity)]
  nlinarith [sq_nonneg (q - 1), hq0, h1, mul_pos hq0 h1]

/-- **The flavour tilt pushes the weight the wrong way.** The one derived
sub-leading ingredient in `w = 1/2 + δ_f/4` is the p–n flavour split
`δ_f = Δm_pn/M_N`, whose sign is fixed by the neutron being heavier:
`δ_f > 0`. It moves `w` *up*, while the crossing `1/(q²+1)` sits *below* `1/2`
(`SymmetrySignAmGm.crossing_lt_half`). So the miss is larger with the derived
correction than without it. -/
theorem flavour_tilt_wrong_direction {q d : K} (hq : 1 < q) (hd : 0 < d) :
    1 / (q ^ 2 + 1) < 1 / 2 ∧ 1 / 2 < 1 / 2 + d / 4 := by
  constructor
  · have hq2 : (1 : K) < q ^ 2 := by nlinarith
    have hpos : (0 : K) < q ^ 2 + 1 := by linarith
    rw [div_lt_div_iff₀ hpos (by norm_num : (0 : K) < 2)]
    linarith
  · linarith

end OrderedField

end QOU.Hecke.BondCutSymmetry
