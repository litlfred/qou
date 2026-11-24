import Mathlib.Tactic

/-!
# QOU.BraidsAndKnots.MilnorTripleLinkingMagnus — a computable `μ̄₁₂₃`, nonzero on Borromean

Bean `qou-bhfg` (front 4-B). Companion to
`QOU.BraidsAndKnots.BorromeanPairwiseLinking` and to
`docs/audits/2026-08-25-4b-pairwise-linking-prune.md`.

## Why this file exists

The pairwise prune next door shows every pairwise linking number vanishes on the
proton braid, so an `E_EM` ansatz built from pairwise data cannot separate it
from the unlink. The unique first-order candidate left is the **Milnor triple
linking number** `μ̄₁₂₃`.

The corpus did **not** have one. It has
`electroweak-triplet-charge-spin-from-involution.lean`'s
`evenTwistTripleLinking (_k : ℕ) : ℤ := 0` — correct, but defined only on the
**two**-component carrier `T(2,2k)`, where a triple linking number is `0` by
definition — and `KnotTheory/Vassiliev/MilnorVassilievBridge.lean`, which is
honest conjecture classes. Neither computes anything for three components. This
file supplies the computation **in Lean**.

> **Correction (same day).** This paragraph first said the file supplies "the
> corpus's first **nonzero** triple linking value". **It does not, and that is
> withdrawn.** `computations/binding_mn_milnor_linking.py` already computes
> `μ̄₁₂₃ = +1` on the Borromean link by this same Magnus method, and validates
> it against a Hopf and a 3-chain control. This file is a **Lean port** of
> committed Python, not a discovery. It was written without grepping
> `computations/` — AGENTS.md corpus-grep path 3, whose stated purpose is
> exactly that. See
> `docs/audits/2026-08-25-4b-corrections-duplication-and-two-fronts.md`.

## What is computed

Milnor's `μ̄₁₂₃` is the coefficient of `X₁X₂` in the Magnus expansion of the
longitude of the third component, read in the free group on the meridians
`x₁, x₂`. Degree 2 suffices, so the whole thing is a finite computation:

    x₁ ↦ 1 + X₁       x₁⁻¹ ↦ 1 − X₁ + X₁²
    x₂ ↦ 1 + X₂       x₂⁻¹ ↦ 1 − X₂ + X₂²

`Deg2` carries the seven coefficients of `1, X₁, X₂, X₁X₁, X₁X₂, X₂X₁, X₂X₂`,
and `Deg2.mul` is the truncated product. Everything below is `decide`.

## The coherence check worth noticing

The **degree-1** coefficients of a Magnus expansion are the linking numbers. So
`magnus_commutator`'s `c1 = c2 = 0` is the Magnus-side shadow of
`BorromeanPairwiseLinking.borromean_crossSum_zero`, computed by a completely
different route — a braid-word crossing simulation there, a free-group series
here. That they agree is a real consistency check on both files, not a
restatement.

It also matters mathematically: `μ̄₁₂₃` is only well-defined (indeterminacy-free)
when the pairwise linking numbers vanish. The vanishing degree-1 part is
*precisely* that hypothesis, verified rather than assumed.

## Scope — two topological inputs are CONSUMED, not proved

1. **Milnor's identification** of `μ̄₁₂₃` with the `X₁X₂` coefficient of the
   longitude. That is Milnor's theorem, cited, not re-derived here.
2. **That the Borromean longitude is the commutator `[x₁, x₂]`.** This is the
   standard presentation and is consumed exactly as the braid word
   `(σ₀σ₁⁻¹)³` is consumed next door.

What this file adds is the *computation* those inputs feed, which the corpus
lacked. It does **not** derive `E_EM`, and it does not supply the map from a
triple linking number to an energy — that gap is untouched and is the second of
the two objects 4-B still needs.

-- Ref: [milnor1957] (link groups; `μ̄` invariants as Magnus coefficients);
-- [kawauchi1996] (Borromean longitude as a commutator of meridians).
-/

namespace QOU.BraidsAndKnots.MilnorTripleLinkingMagnus

/-- A Magnus series truncated at degree 2, in two noncommuting variables:
coefficients of `1, X₁, X₂, X₁X₁, X₁X₂, X₂X₁, X₂X₂`. -/
structure Deg2 where
  c : ℤ
  c1 : ℤ
  c2 : ℤ
  c11 : ℤ
  c12 : ℤ
  c21 : ℤ
  c22 : ℤ
deriving DecidableEq, Repr

namespace Deg2

def one : Deg2 := ⟨1, 0, 0, 0, 0, 0, 0⟩

/-- Truncated product. `X₁X₂ ≠ X₂X₁`, so `c12` and `c21` are tracked separately —
which is the whole point: `μ̄₁₂₃` lives in the difference. -/
def mul (a b : Deg2) : Deg2 :=
  { c   := a.c * b.c
    c1  := a.c * b.c1 + a.c1 * b.c
    c2  := a.c * b.c2 + a.c2 * b.c
    c11 := a.c * b.c11 + a.c1 * b.c1 + a.c11 * b.c
    c12 := a.c * b.c12 + a.c1 * b.c2 + a.c12 * b.c
    c21 := a.c * b.c21 + a.c2 * b.c1 + a.c21 * b.c
    c22 := a.c * b.c22 + a.c2 * b.c2 + a.c22 * b.c }

end Deg2

/-- A free-group letter: generator index (`1` or `2`) and whether it is inverted. -/
abbrev Gen := ℕ × Bool

/-- Magnus image of a single letter. -/
def genImage : Gen → Deg2
  | (1, false) => ⟨1, 1, 0, 0, 0, 0, 0⟩
  | (1, true)  => ⟨1, -1, 0, 1, 0, 0, 0⟩
  | (2, false) => ⟨1, 0, 1, 0, 0, 0, 0⟩
  | (2, true)  => ⟨1, 0, -1, 0, 0, 0, 1⟩
  | _          => Deg2.one

/-- Magnus expansion of a word, truncated at degree 2. -/
def magnus : List Gen → Deg2
  | [] => Deg2.one
  | g :: w => Deg2.mul (genImage g) (magnus w)

/-- Milnor's `μ̄₁₂₃`: the coefficient of `X₁X₂` in the longitude's expansion. -/
def mubar123 (longitude : List Gen) : ℤ := (magnus longitude).c12

/-- The Borromean longitude `[x₁, x₂] = x₁x₂x₁⁻¹x₂⁻¹`. -/
def borromeanLongitude : List Gen := [(1, false), (2, false), (1, true), (2, true)]

/-- The unlink: trivial longitude. -/
def unlinkLongitude : List Gen := []

/-- The full degree-2 expansion of the commutator is `1 + X₁X₂ − X₂X₁`.

Note `c1 = c2 = 0`: the degree-1 part vanishes. Those coefficients are the
linking numbers, so this reproduces `BorromeanPairwiseLinking.borromean_crossSum_zero`
by an entirely different route — and it is exactly the hypothesis under which
`μ̄₁₂₃` is indeterminacy-free. -/
theorem magnus_commutator :
    magnus borromeanLongitude = ⟨1, 0, 0, 0, 1, -1, 0⟩ := by decide

/-- **`μ̄₁₂₃ = 1` on the Borromean braid** — the invariant the pairwise prune
leaves standing. (Not a new value: `binding_mn_milnor_linking.py` already
computes it. This is the Lean port.) -/
theorem mubar_borromean_eq_one : mubar123 borromeanLongitude = 1 := by decide

/-- `μ̄₁₂₃ = 0` on the unlink, so the invariant separates the two links that
pairwise linking could not. -/
theorem mubar_unlink_eq_zero : mubar123 unlinkLongitude = 0 := by decide

/-- **The separation the prune asked for.** Pairwise linking assigns the
Borromean braid and the unlink the same data;
`μ̄₁₂₃` does not. -/
theorem mubar_separates_borromean_from_unlink :
    mubar123 borromeanLongitude ≠ mubar123 unlinkLongitude := by decide

/-- **Control on the hypothesis.** The non-commutator word `x₁x₂` also has
`X₁X₂`-coefficient `1`, but its degree-1 part is nonzero — so it does *not*
satisfy the vanishing-linking condition, and reading a `μ̄₁₂₃` off it would be
reading an indeterminate quantity.

This is here so the `= 1` above is not mistaken for "any word gives 1": the
value is meaningful for the commutator *because* its degree-1 part vanishes. -/
theorem noncommutator_degree_one_nonzero :
    (magnus [(1, false), (2, false)]).c1 ≠ 0 ∧
    (magnus [(1, false), (2, false)]).c2 ≠ 0 := by decide

/-! ## The exchange antisymmetry, and what it forbids

`μ̄₁₂₃` reverses sign under an odd permutation of the three components. For 4-B
that is a constraint on the *map to an energy*, not just a curiosity: the two
like-charged strands of the proton are components `1` and `2` (the two up
quarks, with the down as component `3`), and a Coulomb self-energy between two
identical charges must be **symmetric** under exchanging them.

So an `E_EM` that is odd in `μ̄₁₂₃` is forced to vanish. The map has to be
**even** — `|μ̄₁₂₃|`, `μ̄₁₂₃²`, and so on. -/

/-- The longitude with components `1` and `2` exchanged: `[x₂, x₁]`. -/
def swappedLongitude : List Gen := [(2, false), (1, false), (2, true), (1, true)]

/-- `μ̄₁₂₃ = −1` after exchanging the two like-charged components. -/
theorem mubar_swapped_eq_neg_one : mubar123 swappedLongitude = -1 := by decide

/-- **Exchange antisymmetry**, computed rather than quoted. -/
theorem mubar_swap_eq_neg :
    mubar123 swappedLongitude = - mubar123 borromeanLongitude := by decide

/-- **The second prune for 4-B.** Any functional of `μ̄₁₂₃` that is *odd* and
*symmetric under exchanging the two like-charged components* vanishes.

A two-like-charge Coulomb self-energy is symmetric under that exchange, so this
forbids every `E_EM` odd in `μ̄₁₂₃` — in particular every `E_EM` **linear** in
it, which is the obvious first ansatz. The map must be even.

The physics input consumed here is only that the self-energy is exchange-
symmetric; the antisymmetry of `μ̄₁₂₃` is computed above. -/
theorem odd_symmetric_functional_vanishes (F : ℤ → ℤ)
    (hodd : ∀ m, F (-m) = - F m)
    (hsym : F (mubar123 borromeanLongitude) = F (mubar123 swappedLongitude)) :
    F (mubar123 borromeanLongitude) = 0 := by
  rw [mubar_borromean_eq_one, mubar_swapped_eq_neg_one] at hsym
  rw [mubar_borromean_eq_one]
  have h := hodd 1
  omega

/-- The linear case spelled out, since it is the ansatz anyone writes first:
an exchange-symmetric `E_EM = c · μ̄₁₂₃` forces `c = 0`. -/
theorem linear_coefficient_must_vanish (c : ℤ)
    (hsym : c * mubar123 borromeanLongitude = c * mubar123 swappedLongitude) :
    c = 0 := by
  rw [mubar_borromean_eq_one, mubar_swapped_eq_neg_one] at hsym
  omega

/-! ## What the prune leaves open — the positive half

The two theorems above say what an `E_EM` may *not* be.  Route (2) of bean
`qou-o6ml` (the Möbius / knot-energy class) needs the complementary statement:
that an *even* functional is not merely un-excluded but compatible by
construction, and can be nonzero.  Without it, "the map must be even" is only
half an instruction. -/

/-- An **even** functional satisfies the exchange-symmetry hypothesis
automatically — it does not have to be imposed.

So evenness is not a constraint the route must additionally satisfy; it is the
condition under which the exchange symmetry is free. -/
theorem even_functional_is_symmetric (F : ℤ → ℤ) (heven : ∀ m, F (-m) = F m) :
    F (mubar123 borromeanLongitude) = F (mubar123 swappedLongitude) := by
  rw [mubar_borromean_eq_one, mubar_swapped_eq_neg_one]
  exact (heven 1).symm

/-- **The prune is not vacuous in the even direction**: an even, exchange-
symmetric functional can be nonzero at the Borromean configuration.  Witness
`F m = m ^ 2`.

Without this the pair of theorems above would be consistent with *every*
admissible functional vanishing, which would kill route (2) rather than
narrow it. -/
theorem even_symmetric_functional_can_be_nonzero :
    ∃ F : ℤ → ℤ, (∀ m, F (-m) = F m) ∧
      F (mubar123 borromeanLongitude) = F (mubar123 swappedLongitude) ∧
      F (mubar123 borromeanLongitude) ≠ 0 :=
  ⟨fun m => m ^ 2, fun m => by ring, by decide, by decide⟩

/-- **The sharper reading, and the one that constrains route (2).**  Exchange
symmetry *alone* — with no parity assumption at all — forces any admissible
functional to take the **same value** on the Borromean longitude and on its
component-swapped partner.

Since those two are separated by `μ̄₁₂₃ = 1` against `μ̄₁₂₃ = -1`
(`mubar_separates_borromean_from_unlink` gives the analogous separation from
the unlink), the consequence is that **the sign of `μ̄₁₂₃` is invisible to any
exchange-symmetric `E_EM`**: on this pair such a functional sees at most
`|μ̄₁₂₃|`.

That is strictly stronger than "odd functionals vanish", which is the special
case `F (-m) = - F m`.  For route (2) it says the triple-linking channel can
supply a *magnitude* to the EM weight but never a *chirality*, so any
construction whose EM content is carried by the sign of `μ̄₁₂₃` is excluded
before it is built. -/
theorem exchange_symmetry_forces_agreement_on_pm_one (F : ℤ → ℤ)
    (hsym : F (mubar123 borromeanLongitude) = F (mubar123 swappedLongitude)) :
    F 1 = F (-1) := by
  rwa [mubar_borromean_eq_one, mubar_swapped_eq_neg_one] at hsym

/-! ## The third prune: the carrier's own μ̄ is ZERO, which closes the even branch

The two prunes above are about the *shape* of `E_EM` as a function of `μ̄₁₂₃`:
odd is forbidden (`odd_symmetric_functional_vanishes`), and the sign is
invisible (`exchange_symmetry_forces_agreement_on_pm_one`). What survived was
the **even** branch — `|μ̄₁₂₃|`, `μ̄₁₂₃²` — kept alive by
`even_symmetric_functional_can_be_nonzero`, whose witness `F m = m²` is nonzero
precisely because the Borromean sits at `μ̄₁₂₃ = ±1`.

**The derived carrier does not sit at ±1. It sits at 0.**
[`computations/probes/milnor_mubar_vanishes_on_every_triple_probe.py`](../../../../../computations/probes/milnor_mubar_vanishes_on_every_triple_probe.py)
computes `μ̄` on **every** triple of the canonical atom word's closure and gets
**zero** — for ²H, ³H, ³He, ⁴He, ⁶Li, ⁸Be, ¹⁰B, in both crossing-resolution
branches, across all three indeterminacy classes. Its positive controls run the
same code path: the Borromean is asserted **nonzero** and the Hopf link at
`μ = 2, lk = 1`, so the zeros are a result and not a broken implementation.

**The mathematical content below is that hypothesis, not the proofs.** The
proofs are a rewrite and a `funext`; they are short because the work was the
computation. What the statements buy is that the prune is written down in a form
a reader can check against the probe, and — the part that matters — that it
closes the escape an author would actually reach for.

**The escape it closes.** Faced with "μ̄ vanishes on my triple", the natural move
is *use a different triple*, or *use a symmetric function of all of them*. The
second theorem covers that: a functional of the **whole family** of triple
invariants is equally constant, because the family is pointwise zero. So the
even branch is closed on the derived carrier, not merely inconvenienced.

**Scope.** This is scope (a) **on the derived carrier as computed**, inherited
verbatim from the probe. It says nothing about Milnor invariants of length > 3 —
which is what this route's own title ("higher-order Milnor") names, and which the
probe explicitly does not touch — and nothing about a future carrier. The
Borromean control in that same probe is a standing counterexample to any reading
of this as "μ̄ vanishes on every link".

**Not claimed:** that a length-4 or higher Milnor invariant vanishes, or that
this route is dead. Its length-3 rung is. -/

/-- **A functional of an invariant that vanishes across a family is constant on
    it** — so it supplies neither a difference between two members nor an
    A-dependent profile.

    Instantiate `ι` at the isotopes and `μ` at `μ̄₁₂₃` of a chosen triple: with
    the probe's measured `hμ`, every `E_EM` built from `μ̄₁₂₃` — **including every
    even one** — takes the same value at ³H and ³He. -/
theorem constant_of_vanishing_invariant {ι : Type*} (F : ℤ → ℤ) (μ : ι → ℤ)
    (hμ : ∀ i, μ i = 0) (i j : ι) : F (μ i) = F (μ j) := by
  rw [hμ i, hμ j]

/-- **The same, for a functional of the WHOLE family of triples** — which is the
    escape a reader reaches for when told one triple vanishes.

    `κ` indexes the triples; `μ i` is the isotope's full vector of triple
    invariants. The probe's result is `∀ i t, μ i t = 0`, so the vectors are
    equal and any `F` whatever — symmetric function, norm, maximum — is constant
    across isotopes. -/
theorem constant_of_all_triples_vanishing {ι κ : Type*} (F : (κ → ℤ) → ℤ)
    (μ : ι → κ → ℤ) (hμ : ∀ i t, μ i t = 0) (i j : ι) : F (μ i) = F (μ j) := by
  have h : μ i = μ j := funext fun t => by rw [hμ i t, hμ j t]
  rw [h]

/-- **Hence no charge-antisymmetric content**: the mirror difference this route
    would have to supply is zero. -/
theorem no_asymmetry_of_all_triples_vanishing {ι κ : Type*} (F : (κ → ℤ) → ℤ)
    (μ : ι → κ → ℤ) (hμ : ∀ i t, μ i t = 0) (i j : ι) : F (μ i) - F (μ j) = 0 :=
  sub_eq_zero_of_eq (constant_of_all_triples_vanishing F μ hμ i j)

/-! ## The fourth prune: a link invariant of a NON-LINK — the ladder is unaskable

The prune above closes the length-3 rung on the derived carrier, and leaves the
obvious question: *what about length 4?* **Do not answer it by computing length
4.** Walking up the Milnor ladder until a rung is nonzero is selection of a
discrete parameter against the target — the anti-fit directive names exactly
that. This section derives, instead, that the ladder is asking for something the
object does not have.

**The atom element is not a braid, and the corpus established this before this
section — cite it, do not re-derive it.**
[`braids-and-knots/markov-disambiguation.md`](../../../braids-and-knots/markov-disambiguation.md)
(PR #5765, 2026-08-25) states the category fact directly:

> `tr_M` is defined on ALL of `H_n(q)` … no braid, no closure, and no topology
> are needed for the number to exist. What the closure supplies is the
> INTERPRETATION. … for `W` in `H_n(q)` that is NOT in the image of
> `ρ : B_n → H_n(q)`, `tr_M(W)` is a well-defined number **WITH NO LINK BEHIND
> IT**.

and `computations/binding_is_not_a_link_invariant_probe.py` (bean `qou-brng`)
measures **which** letters leave the image. Its result is sharper than "the
averaged ones are the `d ≠ 0` ones", which is the reading to avoid: under this
module's convention `σ⁻¹ = σ - h`, a `d = -h` letter **is** a braid generator.
Per bond type —

    pp   d = 0                    σ_g        IS a braid generator
    nn   d = -h                   σ_g - h    IS one too (= σ_g⁻¹)
    pn   d = -h(1/2 - δ/4)                   is NOT — the only bond letter that isn't

Milnor invariants are invariants of **links** — closures of braids. A
superposition is not a link, so it has none; to get one you must **resolve** the
averaged letters, and each resolution is a different link.

**One tension, flagged rather than resolved.** That probe concludes the word
*"leaves the braid image exactly at the p-n bond"*, while `atom_braid_word_3A`'s
own docstring describes the per-**nucleon** block as eleven letters *"two of them
averaged (`σ - (h/2)·1`)"* — and `-h/2` is in the outside set. Those are
statements about different letters (inter-nucleon bonds vs intra-nucleon core),
and whether a `Z ≥ 1, N = 0` word would be inside the image turns on it. **It
does not affect anything below**: every nucleus this arc targets has both a
proton and a neutron, so the element is outside `ρ` on either reading. Recorded
so the next reader does not have to notice it twice.

**And the family's LOWEST rung is already branch-dependent.** Measured in
`milnor-mubar-vanishes-on-every-triple.witness.json`: the indeterminacy classes,
which are determined by the pairwise linking numbers, differ between the two
recorded resolutions at **every** isotope —

    isotope   delta_1 (sigma -> sigma^-1)   delta_2 (sigma -> sigma^-1)
    2H            1 -> 0                        0 -> 1
    3H            2 -> 0                        2 -> 4
    3He           3 -> 0                        1 -> 4
    4He           5 -> 0                        4 -> 9
    6Li          13 -> 0                       12 -> 25
    8Be          25 -> 0                       24 -> 49
    10B          41 -> 0                       40 -> 81

— 14 of 14 compared fields differ, and the producer states the cause directly:
*"lk is branch-dependent, so the Delta classes differ per branch."* So `lk`, the
length-2 member, is **not a function of the element**.

**Therefore `μ̄₁₂₃ = 0` on both branches is VANISHING, not well-definedness.** It
agrees across resolutions because it is zero, and the theorem below says that
carries no information about any other member: the family was already broken at
length 2. A *nonzero* higher rung would be branch-dependent like `lk`, and
consuming it would require **choosing a resolution** — a free parameter selected
against the target, which is the fit this section exists to refuse.

**Where this leaves the three routes.** Route (1) is not blocked by a missing
computation; it is asking for a **link invariant of a non-link**, and the only
way to make its question well-posed is a choice that is itself a fit. The Hecke
trace channel asks in the **right category** — `tr_M` is defined on `H_n(q)`,
which is where the element actually lives — and is blocked on infrastructure
rather than on a category error.

**Not claimed:** that no invariant of the element exists (`tr_M` is one); that
some Milnor invariant could not turn out constant across *all* `2^(2A+1)`
resolutions (only two are recorded, and constancy of one member is not the
family's); that route (1) is refuted for a future carrier that IS a braid. What
is derived is that on the carrier as built, the family is not well-defined. -/

/-- An invariant is **well-defined on a superposed element** exactly when it is
    constant across the element's resolutions. `R` indexes resolutions, `res`
    sends each to the link it resolves to. -/
def WellDefinedOnResolutions {R I : Type*} (res : R → I) (inv : I → ℤ) : Prop :=
  ∀ r r', inv (res r) = inv (res r')

/-- A **family** of invariants is well-defined on the element when every member
    is. This is the right object: a route does not consume one invariant, it
    consumes a ladder. -/
def FamilyWellDefinedOnResolutions {R I κ : Type*} (res : R → I)
    (fam : κ → I → ℤ) : Prop :=
  ∀ k, WellDefinedOnResolutions res (fam k)

/-- **Two resolutions with different values refute well-definedness.** This is
    the shape of the `lk` measurement: exhibit the σ and σ⁻¹ branches. -/
theorem not_wellDefinedOnResolutions_of_ne {R I : Type*} (res : R → I)
    (inv : I → ℤ) {r r' : R} (h : inv (res r) ≠ inv (res r')) :
    ¬ WellDefinedOnResolutions res inv :=
  fun hw => h (hw r r')

/-- **ONE branch-dependent member refutes the whole family.**

    This is the load-bearing statement. `lk` is measured branch-dependent, so the
    Milnor family is not well-defined on the atom element — and that is settled
    *before* any higher rung is computed. Walking the ladder cannot repair it. -/
theorem not_familyWellDefined_of_one_member_ne {R I κ : Type*} (res : R → I)
    (fam : κ → I → ℤ) {k : κ} {r r' : R} (h : fam k (res r) ≠ fam k (res r')) :
    ¬ FamilyWellDefinedOnResolutions res fam :=
  fun hf => h (hf k r r')

/-- **A member that vanishes everywhere is constant VACUOUSLY.**

    `μ̄₁₂₃ = 0` on both recorded branches, so it *is* well-defined on its own —
    and this says so, to make precise that the agreement is the zero, not a
    structural property. Composed with the theorem above, it is the whole point:
    a vanishing member is well-defined while the family is not. -/
theorem wellDefined_of_const_zero {R I : Type*} (res : R → I) (inv : I → ℤ)
    (h : ∀ r, inv (res r) = 0) : WellDefinedOnResolutions res inv :=
  fun r r' => by rw [h r, h r']

/-- **The definitions are not vacuous, in both directions.** A constant family is
    well-defined; the identity family on `ℤ` with two distinct resolutions is
    not. Without this pair, everything above would be consistent with the
    predicates being unsatisfiable or trivially satisfiable. -/
theorem familyWellDefined_nondegenerate :
    FamilyWellDefinedOnResolutions (R := Bool) (κ := Unit) (fun _ => (0 : ℤ))
        (fun _ n => n)
      ∧ ¬ FamilyWellDefinedOnResolutions (R := Bool) (κ := Unit)
          (fun b => if b then (1 : ℤ) else 0) (fun _ n => n) := by
  constructor
  · intro _ _ _; rfl
  · intro hf
    have := hf () true false
    simp at this

end QOU.BraidsAndKnots.MilnorTripleLinkingMagnus
