/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.Hecke.InteriorMarkovOfBraidedTower

/-!
# Interior bond factors for the `σ`, `σ⁻¹` and symmetric letters

Bean `qou-qqm4`. The bond product (`tr_bondWord_of_braided`, and
`Mass.ProductionChainBondProduct` for the production layout) carries an
**arbitrary** scalar `d` per bond. This file pins `d` for three specific
letters, in the **interior** position a bond actually occupies.

## What is proved

`tr_bond_interp` — **the headline.** For the colour superposition
`σ_t := (1−t)·σ + t·σ⁻¹`, the interior bond factor is `z − h·t`, for **every**
`t : R`. Every letter in the corpus is an instance: `t = 0` is `σ` (p-p),
`t = 1` is `σ⁻¹` (n-n), `t = 1/2` is `averaged`, and `t = 1/2 − δ/4` is
`averaged_weighted`, the production p-n letter.

This is the trace-level counterpart of
`MassTheory.DeuteronKernel.interfaceFactor`, which defines `f(q,t) = z_D − h·t`
as a **scalar**. Here it is a theorem about the Markov trace on the tower, with
material on both sides of the bond.

**So the factor law is settled for the production letter as well**, and what
`qou-qqm4` leaves measured about the bond model reduces to the single *value*
`t = 1/2 − δ/4`.

`tr_bond_gen` — the `σ` letter carries `d = 0`: factor `z`. `InteriorMarkov`
restated at the bond; here so the three sit together.

`tr_bond_ginv` — **the content.** The `σ⁻¹` letter carries `d = −h`: factor
`z − h`. The skein relation `σ⁻¹ = σ − h` (`gen_inv_eq_of_quadratic`) fed
through `tr_bond_of_interiorMarkov` at `d = −h`.

`tr_bond_gen_add_ginv` — the unnormalised symmetric letter `σ + σ⁻¹` carries
`2z − h`, i.e. `z − h/2` per letter wherever `2` is invertible. Stated
unnormalised so it needs no `2⁻¹` in `R`.

`bond_factors_of_skein_letters` — the three collected.

All are stated over a `MarkovTrace` carrying `[BraidedTower]`, so
`InteriorMarkov` is **discharged** by `interiorMarkov_of_braided` rather than
assumed: the hypotheses are the tower's defining relations, the Markov axioms,
and the quadratic scalar `h`.

## Why these are not already in the corpus

The corpus has both halves of the `σ⁻¹` fact but never composes them, and it
has the composition only in **right-multiplication** form:

* `MathlibExt.OcneanuTrace.tr_mul_ginv_of_quadratic` — `tr (a * ginv n) =
  (z − h) * tr a`. The `b = 1` case.
* `MathlibExt.DisjointBlockTraceLaw.tr_mul_gen_comb_of_quadratic` — the general
  combination `tr (a * (c • g n + c' • ginv n)) = tr a * ((c+c')·z − c'·h)`.
  Also `b = 1`.
* `mass-theory/interface-knot-markov-z.lean` — over a different structure
  (`MarkovHeckeSkeinAlgebra`), and takes trace-linearity as a *hypothesis*.

A bond carries material on **both** sides, so the bond product needs the
interior form with `b ∈ upper g`. The structural reason it is missing is that
`MarkovInteriorBond` works in `MarkovTower`, which has no `ginv` field at all.

## 🛑 THE `pn` LETTER IS NOT THE SYMMETRIC ONE — corrected before merge

An earlier version of this file, and the first body of its PR, identified the
production `pn` interface with the symmetric letter, i.e. `d_pn = −h/2`. **That
is wrong, and the corpus had already ruled it out on 2026-09-07.** The
production letter is `averaged_weighted`:

    d_pn = −h · (1/2 − δ/4),   δ = (q−1)²(1 − q⁻⁴)/3

carried by `Hecke.ClosedFormInterfaceFactors.bondD`, `MathlibExt.MarkovBondRule.dIface`,
`computations/canonical_braid_crossings.py` and `computations/markov_peel.py`.
`−h/2` is the corpus's **`averaged`** letter — a different `ctype`, and not the
production one.

The two agree through order `ε³` and separate at `ε⁴`:

| | `ε⁰` | `ε¹` | `ε²` | `ε³` | `ε⁴` |
|---|---|---|---|---|---|
| `z − h/2` (symmetric) | `1/2` | `0` | `3/4` | `−3/4` | **`5/8`** |
| `z + d_pn` (production) | `1/2` | `0` | `3/4` | `−3/4` | **`31/24`** |
| measured `pn` bond | `1/2` | `0` | `3/4` | `−3/4` | **`31/24`** |

`computations/probes/bond_pn_kind_order_four_discriminator_probe.py` is the
discriminator, on two objects plus a held-out ³He word. The error is instructive
and is why this block exists: an `ε²` check **passes both**, so agreeing to the
order you happened to expand to is not evidence of identity.

`tr_bond_gen_add_ginv` is therefore a theorem about the `averaged` letter, and
is **not** a statement about the production `pn` interface.

## 🛑 What is NOT proved

1. **The value `t = 1/2 − δ/4` is not derived here.** `tr_bond_interp` settles
   the factor *law* for every letter including the production one, so what
   remains is precisely the colour weight's value — not the form of its
   contribution. `δ = (q−1)²(1−q⁻⁴)/3 = ℏ_q²·h_q·[2]_q/3` is the substrate
   flavour split (`prop:flavor-split-substrate`, i.e. `Δm/M_N`), so it is
   assembled from corpus quantities rather than fitted; why the weight is
   `1/2 − δ/4` specifically is `qou-qqm4`'s live open item.
2. **`h` is a hypothesis, not a value.** That `h = q − q⁻¹` for `H_n(q)`, and
   that the substrate's `z` is `z_D = q³/(q²+1)`, are elsewhere.
   `BraidedTower.quad` is existential (`∀ m, ∃ h, …`) and cannot supply a
   uniform `h`, which is why it is an explicit argument.
3. **No `c_k`, no binding coefficient, no absolute trace.** The bond model is
   about the *ratio* `tr(atom)/tr(free)`.
4. **Nothing here reaches the production Ocneanu trace.** The only
   `MarkovTrace` on the presented tower factors through a rank-2 quotient;
   `qou-0fmb` is the bridge.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [leitner2026] beans qou-qqm4, qou-0fmb; prop:interface-knot-markov-z.
-/

namespace QOU.Hecke.BondLetterIdentification

open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.HeckeSandwichReduces
open QOU.Hecke.MarkovInteriorBond QOU.Hecke.InteriorMarkovOfBraidedTower

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable (S : MarkovTrace R A) [BraidedTower S]

/-- **The whole interpolation family at once.** For the colour superposition
`σ_t := (1−t)·σ + t·σ⁻¹`, the interior bond factor is `z − h·t`, for **every**
`t : R`.

This is the trace-level counterpart of
`MassTheory.DeuteronKernel.interfaceFactor`, which defines `f(q,t) = z_D − h·t`
as a scalar; here it is a theorem about the Markov trace on the tower, with
material on both sides of the bond.

Every letter in the corpus is an instance:

| `t` | letter | factor |
|---|---|---|
| `0` | `σ` (p-p) | `z` |
| `1` | `σ⁻¹` (n-n) | `z − h` |
| `1/2` | `averaged` | `z − h/2` |
| `1/2 − δ/4` | `averaged_weighted` (the production p-n) | `z − h(1/2 − δ/4)` |

So the **factor law** is settled for the production letter too. What is not
settled is the *value* of `t` — and that is now the whole of what `qou-qqm4`
leaves measured about the bond model. -/
theorem tr_bond_interp {g : ℕ} (t h : R)
    (hq : S.g g * S.g g = h • S.g g + 1) {a b : A}
    (ha : a ∈ S.H g) (hb : b ∈ upper (toTowerB S) g) :
    S.tr (a * ((1 - t) • S.g g + t • S.ginv g) * b)
      = (S.z - h * t) * S.tr (a * b) := by
  have hcomb : (1 - t) • S.g g + t • S.ginv g = S.g g + (-(h * t)) • (1 : A) := by
    rw [S.gen_inv_eq_of_quadratic g h hq, smul_sub, sub_smul, one_smul, smul_smul]
    module
  rw [hcomb]
  have := tr_bond_of_interiorMarkov (toTowerB S) (interiorMarkov_of_braided S)
    (g := g) (a := a) (b := b) ha hb (-(h * t))
  simpa [sub_eq_add_neg] using this

/-- **The `σ` letter carries `d = 0`**, so a positive-crossing interface's bond
factor is `z` itself. Immediate from `InteriorMarkov`; stated so the three
letters sit together. -/
theorem tr_bond_gen {g : ℕ} {a b : A}
    (ha : a ∈ S.H g) (hb : b ∈ upper (toTowerB S) g) :
    S.tr (a * S.g g * b) = S.z * S.tr (a * b) :=
  interiorMarkov_of_braided S g a ha b hb

/-- **The `σ⁻¹` letter carries `d = −h`**, so a negative-crossing interface's
bond factor is `z − h`.

This is the **interior** counterpart of
`MathlibExt.OcneanuTrace.tr_mul_ginv_of_quadratic`, which is the `b = 1` case.
A bond has material above it as well as below, and the bond product needs that
form; `MarkovTower` has no `ginv` field, which is why the composition lives
here in the `MarkovTrace` vocabulary. -/
theorem tr_bond_ginv {g : ℕ} (h : R)
    (hq : S.g g * S.g g = h • S.g g + 1) {a b : A}
    (ha : a ∈ S.H g) (hb : b ∈ upper (toTowerB S) g) :
    S.tr (a * S.ginv g * b) = (S.z - h) * S.tr (a * b) := by
  have hgi : S.ginv g = S.g g + (-h) • (1 : A) := by
    rw [S.gen_inv_eq_of_quadratic g h hq, neg_smul, ← sub_eq_add_neg]
  rw [hgi]
  have := tr_bond_of_interiorMarkov (toTowerB S) (interiorMarkov_of_braided S)
    (g := g) (a := a) (b := b) ha hb (-h)
  simpa [sub_eq_add_neg] using this

/-- **The unnormalised symmetric letter `σ + σ⁻¹` carries the factor `2z − h`**,
i.e. `z − h/2` per letter wherever `2` is invertible. Stated unnormalised so the
statement needs no `2⁻¹` in `R`.

🛑 This is the corpus's **`averaged`** letter, **not** the production `pn`
interface, which is `averaged_weighted` with `d = −h(1/2 − δ/4)`. The two agree
through `ε³` and separate at `ε⁴` (`5/8` against the measured `31/24`). See the
module docstring. -/
theorem tr_bond_gen_add_ginv {g : ℕ} (h : R)
    (hq : S.g g * S.g g = h • S.g g + 1) {a b : A}
    (ha : a ∈ S.H g) (hb : b ∈ upper (toTowerB S) g) :
    S.tr (a * (S.g g + S.ginv g) * b) = (2 * S.z - h) * S.tr (a * b) := by
  have hsplit : a * (S.g g + S.ginv g) * b = a * S.g g * b + a * S.ginv g * b := by
    rw [mul_add, add_mul]
  rw [hsplit, map_add, tr_bond_gen S ha hb, tr_bond_ginv S h hq ha hb]
  ring

/-- **The three skein letters' interior bond factors, collected.** Given the
quadratic relation's scalar `h`, the `σ`, `σ⁻¹` and symmetric letters carry
`d = 0`, `d = −h` and (after halving) `d = −h/2`. None is measured.

🛑 The *production* `pn` interface is **not** among these — it is
`averaged_weighted`, `d = −h(1/2 − δ/4)`, and deriving that remains open. The
name says `skein_letters` for exactly this reason. -/
theorem bond_factors_of_skein_letters {g : ℕ} (h : R)
    (hq : S.g g * S.g g = h • S.g g + 1) {a b : A}
    (ha : a ∈ S.H g) (hb : b ∈ upper (toTowerB S) g) :
    S.tr (a * S.g g * b) = (S.z + 0) * S.tr (a * b)
      ∧ S.tr (a * S.ginv g * b) = (S.z + -h) * S.tr (a * b)
      ∧ S.tr (a * (S.g g + S.ginv g) * b) = (2 * S.z - h) * S.tr (a * b) := by
  refine ⟨?_, ?_, tr_bond_gen_add_ginv S h hq ha hb⟩
  · simpa using tr_bond_gen S ha hb
  · simpa [sub_eq_add_neg] using tr_bond_ginv S h hq ha hb

/-! ## What the production weight `t = 1/2 − δ/4` equals, and why that is not
yet a derivation

`observations/flavor-split-substrate` defines the substrate flavour split as

    δ = (m_n − m_p) / M_N,      M_N = (m_p + m_n)/2

— the **mean** nucleon mass in the denominator. Under that normalisation the
production weight is not an opaque offset: it is exactly the proton's share of
the pair's mass. The two theorems below record the identity and the reason it
does **not** promote to a rule. -/

section ProductionWeight

/-- **The production p-n weight is the proton's mass fraction.**

With `δ = (m_n − m_p)/M_N` at `M_N = (m_p + m_n)/2` — the corpus's own
normalisation — the canonical colour weight satisfies

    t = 1/2 − δ/4 = m_p / (m_p + m_n)

identically. Dually `1 − t = m_n/(m_p + m_n)`, so the `σ` branch carries the
neutron's fraction and the `σ⁻¹` branch the proton's: the split is
**cross-weighted**, the shape a barycentric lever arm takes.

🛑 This is an **algebraic identity**, not a derivation. It re-expresses `δ/4`
in the corpus's own quantities and supplies no mechanism; what it buys is that
the open coefficient now has a name and a candidate reading that can be tested.
The test is `massFraction_like_pair`, immediately below, and it fails. -/
theorem tPN_eq_proton_mass_fraction (mp mn : ℝ) (hpos : mp + mn ≠ 0) :
    1 / 2 - ((mn - mp) / ((mp + mn) / 2)) / 4 = mp / (mp + mn) := by
  field_simp
  ring

/-- **…and the mass-fraction reading does not extend to the like pairs**, which
is what stops the identity above from being a derivation.

A mass-fraction rule assigns any *like* pair the weight `m/(m+m) = 1/2`. The
corpus assigns `t = 0` to `pp` (the letter is `σ`) and `t = 1` to `nn`
(`σ⁻¹`) — see `tr_bond_gen` and `tr_bond_ginv`. So the rule contradicts both
like-pair letters, and cannot be the mechanism fixing `t` in general.

A consistent reading survives and is **not** proved here: the like pairs are
fixed by exchange symmetry (identical particles admit no interpolation), and
only the *unlike* pair has a free weight, displaced from the symmetric `1/2`
by the flavour asymmetry. That is a story about why `δ` appears, not a
derivation of the factor `1/4`. Bean `qou-qqm4`. -/
theorem massFraction_like_pair (m : ℝ) (hm : m ≠ 0) : m / (m + m) = 1 / 2 := by
  field_simp
  ring

/-! ### The like-pair bond factors, and where `1 − q⁻⁴` in `δ` comes from

At the canonical `z_D = q³/(q²+1)` and `h = q − q⁻¹` the two like-pair factors
are not independent numbers: the `nn` one is `q⁻⁴` times the `pp` one. That
single identity accounts for the `(1 − q⁻⁴)` factor of the substrate flavour
split, which is otherwise an unexplained substrate expression.

The definitions are inlined as hypotheses rather than imported so this section
costs no new dependency; they are `MassTheory.DeuteronKernel.zD`, `.hq` and
`.flavorDelta` verbatim. -/

/-- **The `nn` bond factor is `q⁻⁴` times the `pp` one.**

`z_D − h = 1/(q(q²+1))` against `z_D = q³/(q²+1)`, so their ratio is exactly
`q⁻⁴`. Each `pp → nn` substitution multiplies a bond product by `q⁻⁴`.

🛑 **This is a FORMALISATION of an identity the corpus already had, not a new
one — credit upstream.** `computations/qbeta/qbeta_bond_factors_derived_probe.py`
records `b_pp/b_nn − q⁴ = 0` as its identity 2, established symbolically, and
`b_pp − z = 0` as its identity 1 under an assertion named
`b_pp_IS_the_markov_parameter`. Both predate this file. What is added here is
that the two are the **same law** at `t = 0` and `t = 1` of `tr_bond_interp`
— identity 2 is `tr_bond_ginv` divided by `tr_bond_gen` — and that it holds for
a bond carrying material on *both* sides, which that probe does not address.

All **three** of that file's bond constants are `b(t) = z − h·t`, exactly, as
rational functions of `q`: `b_pp = q³/(q²+1)` at `t = 0`, its degree-10
`b_pn` at `t = 1/2 − δ/4`, and `b_nn = 1/(q³+q)` at `t = 1`. Checked in
`computations/qbeta/qbeta_bond_factors_are_one_interpolation_probe.py` (4/4).
That also separates the production `pn` ctype from `averaged` **symbolically**
(`b(1/2) − b_pn ≠ 0`), which is a stronger form of this file's correction 1 than
the `ε⁴` discriminator it was resting on. -/
theorem nnFactor_eq_ppFactor_div_q_pow_four (q : ℝ) (hq : 0 < q) :
    q ^ 3 / (q ^ 2 + 1) - (q - q⁻¹) = (q ^ 3 / (q ^ 2 + 1)) / q ^ 4 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  field_simp
  ring

/-- **`1 − q⁻⁴` is the relative gap between the like-pair bond factors**, i.e.
`h / z_D` exactly.

So the substrate flavour split factorises through the bond model's own
quantities:

    δ = (q−1)² · (h / z_D) / 3

🛑 An identity, not a derivation — the same class as
`tPN_eq_proton_mass_fraction`. It says the `(1 − q⁻⁴)` in `δ` is not an
independent substrate expression but the like-pair bond gap; it does not
explain the remaining `(q−1)²/3`, and it says nothing at all about the `1/4`
in `t = 1/2 − δ/4`, which is what `qou-qqm4` leaves open. -/
theorem flavorSplit_eq_bondGap (q : ℝ) (hq : 0 < q) :
    (q - 1) ^ 2 * (1 - (q ^ 4)⁻¹) / 3
      = (q - 1) ^ 2 * ((q - q⁻¹) / (q ^ 3 / (q ^ 2 + 1))) / 3 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  field_simp
  ring

/-- **The like-pair bond product collapses to a power of `z` alone.**

With `a` proton-proton bonds and `b` neutron-neutron bonds, `z^a·(z−h)^b·q^(4b)
= z^(a+b)`: every `nn` bond contributes the same `z` as a `pp` bond, up to one
factor `q⁻⁴`. Division-free, so it needs no nonvanishing side conditions beyond
`0 < q`.

**The mirror-pair law is the immediate corollary.** A mirror pair `(Z,N)` and
`(N,Z)` in canonical `pppnnn` ordering has `(a,b) = (Z−1, N−1)` and
`(N−1, Z−1)`, and one `pn` bond each — common, hence cancelling. So

    tr(Z,N) / tr(N,Z)  =  q^(−4(N−Z))

exactly, **independent of the `pn` convention**: `δ` does not appear. Verified
symbolically at `(Z,N) = (1,2), (2,3), (1,3), (2,4), (3,5), (4,6)` and at the
self-mirror `(1,1), (2,2)`, where it gives `1`.

Swapping the two like-pair letters swaps `a` and `b`, which inverts the ratio.
Nothing else **in the bond model** distinguishes a proton from a neutron — that
scope is exact and load-bearing; see the correction below.

🛑 **The δ-cancellation here is a RE-DERIVATION — the corpus got there first.**
`QOU.QBeta.InterfaceScalar.mirror_split_eq_L_diff` (sorry-free) already proves
it, and its docstring states the reason in the same words: *"³H = `pnn` carries
bonds `{pn, nn}` and ³He = `ppn` carries `{pp, pn}`, so the predicted splitting
is `α(L_nn − L_pp)` regardless of what the p–n bond is."* What is new here is
only the **closed form** `q^(4(Z−N))` for the bare bond-product ratio, and its
generalisation off `A = 3`; the cancellation itself is not.

🛑 **Reconciling that closed form with the corpus's measured split is NOT
done.** `InterfaceScalar` reports `α(L_nn − L_pp) = 2.27077 MeV` under
convention C and `0.76532 MeV` under D with the writhe term wired. The ratio
here is the **bare** bond product, before `α` and before the writhe
normalisation `(1−h)^(Δe/2)`, so the two are not directly comparable and no
arithmetic bridging them is attempted. Anyone quoting both must do that step.

🛑 **The assignment this file's `t = 0` / `t = 1` endpoints encode is reported
FALSIFIED.** Bean `qou-0pzi` (live) concludes from the two-nucleon signs that
*"`pp = sigma`, `nn = sigma^-1` cannot be the right assignment"*: the model
makes the diproton and dineutron **bound** (`+2.5416`, `+3.3069` MeV) where
nature has both unbound. That is a **scope-(a)** negative — this assignment,
alone, gets the two-nucleon signs wrong — with no proved invariant excluding
the ingredient, so do not upgrade it to scope (b). The theorems in this file
are unaffected: they say what a given letter contributes, not that the
production letters are right.

🛑 **The bond letters are NOT the only p/n injection in the framework.**
`appendix-mass-binding-algorithms/mba-sidecar-mirror-cancellation` records a
second one, upstream of this file: the **intra**-nucleon writhe asymmetry,
*"proton `+3` > neutron `+1`"* per nucleon, which fixes the sign of its mirror
split `ζ`. So an unqualified "the p/n asymmetry is injected at the bond
letters" is wrong; the correct statement is that it is injected at the bond
letters **and** in the per-nucleon blocks, and this file only sees the first.

That block also states the total writhe `w = σ − σ⁻¹ = 4Z`, hence
`w(Z,N) − w(N,Z) = 4(Z−N)` — numerically **the same exponent** this theorem
produces, so the mirror ratio here is `q` raised to the writhe difference.
🛑 Whether that is structural or a coincidence of two different counts is
**NOT established**: the writhe there is over the whole word, intra letters
included, while `a` and `b` here count only the `A−1` inter-nucleon bonds.
Do not cite the agreement as a derivation.

And that block already declares the mirror-split **magnitude** *"open and
unfitted"*, so the open item this file points at is in part one the corpus had
already named. Bean `qou-qqm4`. -/
theorem likePairBondProduct_eq_z_pow {R : Type*} [CommRing R]
    (zpp znn c : R) (hrel : znn * c = zpp) (a b : ℕ) :
    zpp ^ a * znn ^ b * c ^ b = zpp ^ (a + b) := by
  rw [pow_add, ← hrel, mul_pow]
  ring

/-- The multiplicative form of `nnFactor_eq_ppFactor_div_q_pow_four`, which is
what feeds `likePairBondProduct_eq_z_pow`: `(z_D − h)·q⁴ = z_D`. -/
theorem nnFactor_mul_q_pow_four (q : ℝ) (hq : 0 < q) :
    (q ^ 3 / (q ^ 2 + 1) - (q - q⁻¹)) * q ^ 4 = q ^ 3 / (q ^ 2 + 1) := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  field_simp
  ring

/-- **The mirror-pair law, at the canonical `z_D`.** With `a` proton-proton and
`b` neutron-neutron bonds, the like-pair product is `z_D^(a+b)` once the `b`
factors of `q⁴` are restored — so a mirror pair, which swaps `a` and `b`,
differs by exactly `q^(4(a−b))`. -/
theorem likePairBondProduct_zD (q : ℝ) (hq : 0 < q) (a b : ℕ) :
    (q ^ 3 / (q ^ 2 + 1)) ^ a * (q ^ 3 / (q ^ 2 + 1) - (q - q⁻¹)) ^ b * (q ^ 4) ^ b
      = (q ^ 3 / (q ^ 2 + 1)) ^ (a + b) :=
  likePairBondProduct_eq_z_pow _ _ _ (nnFactor_mul_q_pow_four q hq) a b

end ProductionWeight

/-- The difference of interior bond traces at two colour-mixing weights `t₁` and `t₂`
is proportional to `h * (t₂ - t₁)`, isolating the weight difference from `S.z`. -/
theorem tr_bond_interp_sub {g : ℕ} (t₁ t₂ h : R)
    (hq : S.g g * S.g g = h • S.g g + 1) {a b : A}
    (ha : a ∈ S.H g) (hb : b ∈ upper (toTowerB S) g) :
    S.tr (a * ((1 - t₁) • S.g g + t₁ • S.ginv g) * b) -
      S.tr (a * ((1 - t₂) • S.g g + t₂ • S.ginv g) * b)
      = h * (t₂ - t₁) * S.tr (a * b) := by
  have h1 := tr_bond_interp S t₁ h hq ha hb
  have h2 := tr_bond_interp S t₂ h hq ha hb
  rw [h1, h2]
  ring

end QOU.Hecke.BondLetterIdentification
