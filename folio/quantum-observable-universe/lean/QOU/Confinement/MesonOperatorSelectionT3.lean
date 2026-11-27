/-
Copyright (c) 2026 Frederick Carl Leitner. All rights reserved.
-/
import Mathlib.Tactic
import Mathlib.Data.Multiset.Basic

/-!
# QOU.ParticleInteractions.MesonOperatorSelectionT3

## Wiring the derived weak-isospin `T₃` into the meson operator-selection

**Reading of the quark data (owner rulings 2026-11-20 and 2026-11-21).** A
quark is an **unknot strand** of `B₃` carrying one crossing letter; it is not a
torus knot. The integers `3, 5, 7` attached to quarks below are the **crossing
counts of their lepton partners** `T(2,3), T(2,5), T(2,7)` — generation labels.
The sign of `κ` is the quark strand's own crossing orientation (`σ` vs `σ⁻¹`).
So "winding" below means *generation label*, "signed writhe" means
*orientation × generation label*, and a meson's "content" is a multiset of
labels, not of crossings on the quark strands. Every definition and theorem is
unchanged; only this reading is. The identifiers `genWinding` and
`signedWrithe` are kept as names.

Serves bean `qou-2udt` (child of the convergence epic `qou-20sx`).  Resolves
the *selection* half of the honest negative in
`docs/audits/2026-08-02-meson-fluxtube-junction-reduction.md` (bean
`qou-qpj9`, PR #4614): the meson operator-selection was **degenerate** because
its input — the generation winding `n ∈ {3,5,7}` — is a *symmetric* function
of the quark content (`MesonFluxTubeReduction.lean`,
`winding_content_not_injective`): the D̄⁰ meson `c̄u = {5,3}` and the kaon
`K⁻ = ūs = {3,5}` map to the **same** unsigned winding multiset, so the
`gg → c̄c` operator-selection cannot pick a charm-specific channel.

The missing datum that audit named — a weak-isospin `T₃` grading orthogonal
to `n` — was **derived** in `WeakIsospinT3Grading.lean` (PR #4618, bean
`qou-tdrd`) as the *sign of the signed writhe*:
`κ = sign(κ)·|κ| = T₃ · genWinding`, with charm (positive strand, partner
`T(2,5)`, `T₃ = +½`) and strange (negative strand, partner `T(2,5)`,
`T₃ = −½`) — same generation `n = 5`, opposite `T₃`.

This file **refines the meson operator-selection input** from the unsigned
label multiset to the **signed** multiset (an antiquark reverses the strand
orientation, so it contributes `−κ` — a topological fact about the sign, not a
fitted choice; the magnitude it carries is still the partner's label), and checks what the refinement fixes.

### What is proved (sorry-free, `lean`-direct)

1. **The selection input is now injective on quarks.**  `signedWrithe`
   (equivalently the pair `(genWinding, sign) = (n, 2T₃)`) separates all six
   quarks; in particular the charm block `(n=5, T₃=+½)` is *distinctly
   selectable* from the strange block `(n=5, T₃=−½)`
   (`selectionInput_injective`, `charmBlock_ne_strangeBlock`).

2. **The specific blocker degeneracy is resolved.**  The unsigned content
   still collides D̄⁰ with the kaon (`unsigned_D_kaon_collide`, reproducing
   `winding_content_not_injective`), but the **signed** content separates
   them (`graded_D_kaon_distinct`), and is injective on the four-meson
   dictionary of `lepton-meson-torus-knot-dictionary`
   (`gradedContent_injective_on_dictionary`).  The operator-selection is no
   longer degenerate on the pair the audit named.

### What is NOT fixed — the honest remainder (two distinct gaps)

3. **A residual content collision survives** once the neutral kaon
   `K⁰ = d̄s` is admitted: `T₃` grades by *(generation, weak-sign)*, and the
   charm-antiquark `c̄` (`κ = −5`) shares that grade with the strange quark
   `s` (`κ = −5`), while `u` (`κ = +3`) shares it with `d̄` (`κ = +3`).  So
   the **signed multiset** collides D̄⁰ `{−5,+3}` with K⁰ `{+3,−5}`
   (`graded_D_K0_collide`, `gradedContentExt_not_injective`).  It is broken
   only by keeping the **quark/antiquark orientation** (the "bar") as
   *ordered* data — itself topological (strand orientation), giving
   `orderedContent_injective` — a datum the audit's *symmetric-multiset*
   content model does not carry.  The full separation therefore needs a third
   flavour grading (charm number `C` vs strangeness `S`), beyond `(n, T₃)`.

4. **The tube GEOMETRY is untouched (Obstruction A / `qou-qpj9`).**  Even a
   fully-fixed graded content only pins the *carrier quantum numbers* — the
   `Vol = 0` torus data (`MesonFluxTubeReduction.twoStrand_winding_bijective`).
   The *hyperbolic* braid word at `H₃(q)` whose closure volume gives the
   **mass** is a separate, still-open construction.  This is packaged as the
   content-bearing conjecture class `CanonicalHyperbolicMesonBraid` with **no
   instance** (§3b-tax honest open state).  Consequently **no a-priori
   D-meson mass check is run** here: `T₃` resolves the *selection*, not the
   *geometry* (anti-fit discipline — no braid was hand-picked to hit
   1864.84 MeV).

This file re-states the minimal `signedWrithe` / `T₃` scaffold of PR #4618
locally so it verifies standalone off `main` (neither #4618 nor #4614 is on
`main` yet); at merge time the two consolidate into one import.

Refs:
  - docs/audits/2026-08-02-meson-fluxtube-junction-reduction.md (the gate, #4614)
  - content/.../lean/QOU/ParticleInteractions/WeakIsospinT3Grading.lean (#4618)
  - content/.../lean/QOU/ParticleInteractions/MesonFluxTubeReduction.lean (#4614)
  - content/.../particle-interactions/lepton-meson-torus-knot-dictionary.lean
  - content/.../predicted-spectra/knot-operator-selection.md
  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [leitner2026] Ch. "Predicted Spectra" §knot-operator-selection
-/

namespace QOU.ParticleInteractions.MesonOperatorSelectionT3

/-! ### Minimal `signedWrithe` / `T₃` scaffold (mirrors PR #4618) -/

/-- The six SM quark flavours. -/
inductive Quark
  | up | charm | top          -- up-type
  | down | strange | bottom   -- down-type
deriving DecidableEq, Fintype

/-- The signed integer `κ = ±n` attached to a quark.  Magnitude `|κ| = n` is
    the crossing count of the quark's lepton partner `T(2,n)` — a generation
    label (`u,d = 3`, `s,c = 5`, `b,t = 7`); the quark itself is an unknot
    strand.  The sign is the quark strand's crossing orientation,
    `⋈_K`-inherited (up-type positive, down-type negative).  Mirrors
    PR #4618. -/
def signedWrithe : Quark → ℤ
  | .up      => 3   | .charm   => 5   | .top     => 7
  | .down    => -3  | .strange => -5  | .bottom  => -7

/-- Generation label `n = |κ| ∈ {3,5,7}` (the lepton partner's crossing
    count). -/
def genWinding (q : Quark) : ℕ := (signedWrithe q).natAbs

/-- Weak isospin `T₃ = sign(κ)/2 ∈ {+½,−½}`. -/
def T3 (q : Quark) : ℚ := ((signedWrithe q).sign : ℚ) / 2

/-! ### The selection input is now injective on quarks -/

/-- **The refined operator-selection demand input** for a single quark: the
    pair `(generation winding, weak sign) = (n, 2·T₃)`.  The unsigned input
    used by `winding_content_not_injective` is only its first coordinate. -/
def selectionInput (q : Quark) : ℕ × ℤ := (genWinding q, (signedWrithe q).sign)

/-- **`signedWrithe` separates all six quarks.**  The generation-plus-sign
    datum is a complete label — the collision that made the unsigned winding
    non-injective is gone at the quark level. -/
theorem signedWrithe_injective : Function.Injective signedWrithe := by
  decide

/-- **The refined selection input is injective.**  `(n, 2T₃)` distinguishes
    every quark, so each Wedderburn/knot block is individually selectable. -/
theorem selectionInput_injective : Function.Injective selectionInput := by
  decide

/-- **Charm and strange share the generation winding** (both `n = 5`) — the
    degeneracy `winding_content_not_injective` records. -/
theorem charm_strange_same_generation : genWinding .charm = genWinding .strange :=
  rfl

/-- **…but their selection inputs differ** — the sign (`+` vs `−`) breaks the
    tie: the charm block `(5, +1)` is distinctly selectable from the strange
    block `(5, −1)`.  This is the datum the unsigned winding lacked. -/
theorem charmBlock_ne_strangeBlock : selectionInput .charm ≠ selectionInput .strange := by
  decide

/-- Charm's `T₃` is `+½`, strange's is `−½` (the `ℚ`-level statement). -/
theorem T3_charm_ne_strange : T3 .charm ≠ T3 .strange := by
  simp only [T3, signedWrithe, show (5 : ℤ).sign = 1 from rfl,
    show (-5 : ℤ).sign = -1 from rfl]
  norm_num

/-! ### Mesons and their content: unsigned (blocker) vs signed (refined) -/

/-- The four-meson dictionary of `lepton-meson-torus-knot-dictionary`, plus
    the neutral kaon `K⁰ = d̄s` (used below to expose the residual collision).
    A meson is recorded as its `(antiquark, quark)` pair. -/
inductive Meson
  | pion    -- ū d
  | kaon    -- ū s   (K⁻)
  | etaPhi  -- s̄ s
  | Dmeson  -- c̄ u   (D̄⁰, open charm)
  | K0      -- d̄ s   (K⁰)
deriving DecidableEq, Fintype

/-- The `(antiquark, quark)` constituent pair of each meson. -/
def constituents : Meson → Quark × Quark
  | .pion   => (.up,      .down)
  | .kaon   => (.up,      .strange)
  | .etaPhi => (.strange, .strange)
  | .Dmeson => (.charm,   .up)
  | .K0     => (.down,    .strange)

/-- Is this meson in the four-meson dictionary of `lepton-meson-torus-knot-
    dictionary` (i.e. not the extension `K⁰`)? -/
def inDictionary : Meson → Prop
  | .K0 => False
  | _   => True

instance : DecidablePred inDictionary := by
  intro m; cases m <;> unfold inDictionary <;> infer_instance

/-- **Unsigned winding content** `{|κ₁|, |κ₂|}` — the input of
    `MesonFluxTubeReduction.windingContent` (a symmetric function of the two
    generations). -/
def unsignedContent (m : Meson) : Multiset ℕ :=
  {genWinding (constituents m).1, genWinding (constituents m).2}

/-- **Signed content** `{−κ(antiquark), +κ(quark)}` — the *refined*
    input.  The antiquark reverses the strand orientation, hence contributes
    `−κ` (topological, not fitted). -/
def gradedContent (m : Meson) : Multiset ℤ :=
  {- signedWrithe (constituents m).1, signedWrithe (constituents m).2}

/-- **Ordered signed content** `(−κ(antiquark), +κ(quark))` — keeps the
    quark/antiquark orientation (the "bar") as ordered data. -/
def orderedContent (m : Meson) : ℤ × ℤ :=
  (- signedWrithe (constituents m).1, signedWrithe (constituents m).2)

/-! ### The blocker, reproduced; and its resolution -/

/-- **The blocker.** The unsigned content collides D̄⁰ `{5,3}` with the kaon
    `{3,5}` — exactly `MesonFluxTubeReduction.D_kaon_same_winding`. -/
theorem unsigned_D_kaon_collide : unsignedContent .Dmeson = unsignedContent .kaon := by
  decide

/-- **The unsigned selection is degenerate** (reproduces
    `winding_content_not_injective`). -/
theorem unsignedContent_not_injective : ¬ Function.Injective unsignedContent := by
  intro hinj
  have : Meson.Dmeson = Meson.kaon := hinj unsigned_D_kaon_collide
  exact absurd this (by decide)

/-- **THE RESULT.** The signed content **separates** D̄⁰ from the kaon: the
    charm-antiquark `c̄` (`−κ = −5`) vs the up-antiquark `ū` (`−κ = −3`)
    breaks the tie the magnitude hid.  The specific degeneracy the audit
    named is resolved. -/
theorem graded_D_kaon_distinct : gradedContent .Dmeson ≠ gradedContent .kaon := by
  decide

/-- **The refined selection is injective on the four-meson dictionary.**  On
    `{pion, kaon, etaPhi, Dmeson}` the signed content distinguishes every
    meson — the operator-selection is no longer degenerate on the domain the
    blocker lived in. -/
theorem gradedContent_injective_on_dictionary :
    ∀ m m' : Meson, inDictionary m → inDictionary m' →
      gradedContent m = gradedContent m' → m = m' := by
  decide

/-! ### The honest remainder — residual content collision (needs a 3rd grade) -/

/-- **Residual collision.**  With the neutral kaon `K⁰ = d̄s` admitted, the
    signed *multiset* still collides D̄⁰ `{−5,+3}` with K⁰ `{+3,−5}`: `(n,T₃)`
    grades by *(generation, weak-sign)*, and `c̄` shares `(5, −)` with `s`,
    `u` shares `(3, +)` with `d̄`.  So `T₃` does not *globally* separate all
    mesons — a further flavour grading (charm number vs strangeness) is the
    remaining missing datum. -/
theorem graded_D_K0_collide : gradedContent .Dmeson = gradedContent .K0 := by
  decide

/-- Hence the signed content is **not** injective on the full meson set. -/
theorem gradedContentExt_not_injective : ¬ Function.Injective gradedContent := by
  intro hinj
  have : Meson.Dmeson = Meson.K0 := hinj graded_D_K0_collide
  exact absurd this (by decide)

/-- **…but the ordered content IS injective.**  Keeping the quark/antiquark
    orientation (the "bar" — itself topological strand-orientation data, not
    a fit) separates D̄⁰ `(−5,+3)` from K⁰ `(+3,−5)`.  The residual collision
    is an artefact of the *symmetric-multiset* content model of #4614, not of
    the physics; the bar resolves it. -/
theorem orderedContent_injective : Function.Injective orderedContent := by
  decide

/-! ### The tube GEOMETRY gap — conjecture class, NO instance (§3b-tax) -/

/-- **Primary conjecture (open — deliberately NO instance).**

    Refining the operator-selection input to `(n, T₃)` fixes *which* meson
    content is selected (proved above), but **not** the hyperbolic braid word
    that carries the mass.  The graded content is `Vol = 0` torus-carrier data
    (`MesonFluxTubeReduction.twoStrand_winding_bijective`); the mass needs a
    genuinely *hyperbolic* braid at `H₃(q)` (Obstruction A, `qou-qpj9`).

    A canonical realization would provide volume/mass maps such that:

    * `hyperbolic` — every meson's canonical braid has *positive* volume (not
      the `Vol = 0` carrier the `(n,T₃)` content alone gives);
    * `mass_positive` — the mass law reads off that volume;
    * `breaks_graded_collision` — the geometry supplies data *beyond*
      `(n,T₃)`: though `gradedContent .Dmeson = gradedContent .K0`
      (`graded_D_K0_collide`), the physical masses differ sharply
      (`m_D ≈ 1865 ≫ m_K ≈ 498`), so the braid word must carry the residual
      flavour datum the content lacks.

    Content-bearing (each field is a genuine constraint), and **no instance is
    provided** — constructing the canonical hyperbolic meson braid from the
    graded content is the open step `qou-qpj9`.  A fabricated instance over
    this finite toy would be forbidden laundering (§3b-tax). -/
class CanonicalHyperbolicMesonBraid (vol mass : Meson → ℚ) : Prop where
  /-- Every meson's canonical braid is genuinely hyperbolic (positive volume),
      not the `Vol = 0` torus carrier the `(n,T₃)` content provides. -/
  hyperbolic : ∀ m, 0 < vol m
  /-- The mass law reads the hyperbolic volume (volume–density mass form). -/
  mass_positive : ∀ m, 0 < mass m
  /-- The geometry must separate the residual graded-content collision
      D̄⁰ ≡ K⁰: same `(n,T₃)` content, sharply different mass. -/
  breaks_graded_collision : mass .Dmeson ≠ mass .K0

/-- **The `(n,T₃)` content alone cannot witness `breaks_graded_collision`.**
    Any mass map that is a *function of the graded content* assigns D̄⁰ and K⁰
    the *same* mass — so it fails the conjecture's separation field.  This is
    the precise sense in which `T₃` resolves the *selection* but not the
    *geometry*: the mass datum is provably not a function of `(n,T₃)`. -/
theorem mass_from_graded_content_cannot_separate
    (f : Multiset ℤ → ℚ) :
    (fun m => f (gradedContent m)) .Dmeson = (fun m => f (gradedContent m)) .K0 := by
  simp only [graded_D_K0_collide]

end QOU.ParticleInteractions.MesonOperatorSelectionT3
