/-
Copyright (c) 2026 Frederick Carl Leitner. All rights reserved.
-/
import Mathlib.Tactic

/-!
# QOU.ParticleInteractions.WeakIsospinT3Grading

## A weak-isospin (up/down-type) grading `T₃` orthogonal to the generation winding

**Reading of `κ` (owner rulings 2026-11-20 and 2026-11-21).** A quark is an
**unknot strand** of the pure braid `B₃`, carrying one crossing letter (`σ` or
`σ⁻¹`); it is **not** a torus knot `T(2,n)`. The torus knot `T(2,n)` is the
quark's **lepton partner** (`T(2,3)` the electron, `T(2,5)` the muon, `T(2,7)`
the tau). So the integer `κ` below is read as follows:

* `|κ| = n` is the **lepton partner's crossing count** — a generation label,
  not a crossing count carried by the quark strand;
* `sign κ` is the **quark strand's own crossing orientation** (`σ` positive,
  `σ⁻¹` negative), which is a property of the quark.

Every definition and theorem in this file is unchanged; only this reading of
the data is. Where older prose below says "winding" or "writhe", read "the
generation label `|κ|`" for the magnitude and "the quark strand's crossing
orientation" for the sign. The identifier `signedWrithe` is kept as a name.

Serves bean `qou-tdrd` (root of the convergence epic `qou-20sx`) and the
honest negative of
`docs/audits/2026-08-02-meson-fluxtube-junction-reduction.md`
(bean `qou-qpj9`, PR #4614).  That audit proved (`MesonFluxTubeReduction.lean`,
`winding_content_not_injective`) that the framework's generation winding
`n ∈ {3,5,7}` is a **symmetric** function of the quark content and therefore
**cannot** separate up-type from down-type at a fixed generation: charm and
strange both carry `n = 5`, so the `T(2,n)` dictionary collides the D-meson
`{5,3}` with the kaon `{3,5}`.  The precise missing datum it named is a
*weak-isospin `T₃` grading orthogonal to `n`*.

### The derivation (what is proved below, sorry-free)

The framework already carries **two** independent facts about a quark:

* a **generation label** `n` — the crossing number of the quark's lepton
  partner `T(2,n)` (`lepton-meson-torus-knot-dictionary.lean`,
  `leptonTorusKnotIndex`); the quark strand itself does not carry `n`
  crossings;
* the **crossing SIGN** of the quark strand — already a *physical* grading in
  the corpus: the
  strong-isospin interface uses `σ_g` (positive) for the `pp` channel and
  `σ_g⁻¹` (negative) for the `nn` channel
  (`crystal-isospin-degeneracy.md`, `isotope_record_schema.py:176-178`;
  audit `docs/audits/2026-05-24-isospin-categorical-source.md`), and the
  weak generator `T(3,5)` maximises the `q≠1` Skein sign-asymmetry that
  drives parity violation and up↔down transmutation
  (`force-knot-identification.md`).

The signed integer `κ = ±n` (historically called the *signed writhe*; it
combines the partner's crossing count with the strand's orientation) therefore
factors *canonically* as
```
      κ  =  sign(κ) · |κ|
           └──┬───┘  └┬┘
            T₃ grading  generation label
```
The magnitude `|κ| = n` is the generation label (the lepton partner's crossing
count); the **sign** `sign(κ) ∈ {+1,−1}`
is an intrinsic `ℤ/2` grading **orthogonal to the magnitude by construction**
(the sign and magnitude of an integer are independent data).  Normalised as a
fundamental SU(2)_weak weight, `T₃ = sign(κ)/2 ∈ {+½, −½}`.

With the sign convention **up-type = positive crossing** inherited from the
strong-isospin `⋈_K` orientation (`pp = σ_g` positive; the proton is the
more-up nucleon), charm (positive strand, partner `T(2,5)`) gets `T₃ = +½` and strange
(negative strand, partner `T(2,5)`) gets `T₃ = −½`: **same generation `n = 5`, opposite `T₃`** — the degeneracy
`winding_content_not_injective` is resolved by refining the *unsigned* winding
to the *signed* writhe.

**Derive-then-check (not fit).** `T₃` is defined from the topology
(`signedWrithe`), and the Gell-Mann–Nishijima relation `Q = T₃ + Y/2` is then
**checked** against the independently-known electric charges `Q` and the
left-doublet hypercharge `Y = 1/3`.  It is a theorem that could have failed
(a wrong sign, or a wrong `½`, breaks it); it does not
(`gellMannNishijima`).  No continuous parameter was tuned — the grading is a
discrete `ℤ/2`.

**But report its WIDTH honestly.**  The relation is quantified over six quarks
and collapses to **two** distinct arithmetic rows: `Y` is constant and both `Q`
and `T₃` are functions of the up/down-type bit alone
(`gmn_data_factors_through_weakType`, `gmn_check_has_two_distinct_rows`).  So
the check is one sign correlation plus one normalisation, verified twice — not
six independent confirmations.  The generation index never enters it
(`genWinding_finer_than_gmn_data`).

### What is NOT proved (the honest open remainder)

`signedWrithe` is *entered as data* over a finite toy `Quark` type, so every
statement below is decidable; the arithmetic being provable does **not** make
the *physics* closed.  Two things remain genuinely open, packaged as the
content-bearing conjecture class `CanonicalWeakIsospinFromBowtie` with **no
instance** (§3b-tax honest open state):

1. that the up-type ↔ positive-writhe identification is *forced* by the `⋈_K`
   framework orientation rather than *chosen* consistently with it; and
2. that this `ℤ/2` lifts to the full SU(2)_L gauge action on the `H_n(q)`
   representations and, combined with the generation tower, reproduces the
   quark masses / CKM mixing.

Both reduce to the open SU(3)-flavour / CKM sector; this file derives the
orthogonal grading and its GMN closure, not that sector.

Refs:
  - docs/audits/2026-08-02-meson-fluxtube-junction-reduction.md (the gate)
  - docs/audits/2026-05-24-isospin-categorical-source.md (⋈_K sign law)
  - content/.../predicted-spectra/force-knot-identification.md (T(3,5) weak)
  - content/.../particle-interactions/lepton-meson-torus-knot-dictionary.lean
  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [leitner2026] Ch. "Predicted Spectra" §force-knot-identification
-/

namespace QOU.ParticleInteractions.WeakIsospinT3

/-! ### The six Standard-Model quarks and their canonical signed writhe -/

/-- The six SM quark flavours. -/
inductive Quark
  | up | charm | top          -- up-type
  | down | strange | bottom   -- down-type
deriving DecidableEq, Fintype

/-- The `ℤ/2` weak-isospin sector: up-type vs down-type. -/
inductive WeakType
  | upType | downType
deriving DecidableEq

/-- **The one derived datum.** The signed integer `κ = ±n` attached to a
    quark.  Magnitude `|κ| = n` is the **crossing count of the quark's lepton
    partner** `T(2,n)` — a generation label (`u,d = 3`, `s,c = 5`, `b,t = 7`,
    matching `lepton-meson-torus-knot-dictionary`); the quark itself is an
    unknot strand of `B₃` (owner rulings 2026-11-20 / 2026-11-21).  The sign
    is the quark strand's crossing orientation, `⋈_K`-inherited,
    **up-type positive, down-type negative**.  Everything
    below is read off this single map — `genWinding`, `weakType`, and `T₃`
    are all functions of it, so the grading is not a second postulate but
    the sign-half of the object whose magnitude is already the generation. -/
def signedWrithe : Quark → ℤ
  | .up      => 3   | .charm   => 5   | .top     => 7
  | .down    => -3  | .strange => -5  | .bottom  => -7

/-- **Generation label = magnitude of `κ`.** Derived from `signedWrithe`,
    not an independent datum. Reproduces the lepton-partner indices `{3,5,7}`
    of the corpus `T(2,n)` dictionary (the partner's crossing count, not the
    quark strand's). -/
def genWinding (q : Quark) : ℕ := (signedWrithe q).natAbs

/-- **Weak-isospin sector = sign of the writhe.** -/
def weakType (q : Quark) : WeakType :=
  if 0 < signedWrithe q then WeakType.upType else WeakType.downType

/-- **Weak isospin `T₃ = sign(κ)/2 ∈ {+½,−½}`** — the fundamental
    SU(2)_weak weight read off the quark strand's crossing orientation. -/
def T3 (q : Quark) : ℚ := ((signedWrithe q).sign : ℚ) / 2

/-! ### ℤ-level sign/type values (kernel-decidable helpers)

These discharge the `ℚ`-valued `T₃` facts below: `Int.sign` of a concrete
numeral is decidable at `ℤ` (`decide`), whereas `decide` on the `ℚ`
arithmetic itself gets stuck on `Rat` kernel reduction.  Each is a genuine
finite numeric check (allowed `decide`, not laundering). -/

theorem writheSign_up      : (signedWrithe .up).sign = 1       := by decide
theorem writheSign_charm   : (signedWrithe .charm).sign = 1    := by decide
theorem writheSign_top     : (signedWrithe .top).sign = 1      := by decide
theorem writheSign_down    : (signedWrithe .down).sign = -1    := by decide
theorem writheSign_strange : (signedWrithe .strange).sign = -1 := by decide
theorem writheSign_bottom  : (signedWrithe .bottom).sign = -1  := by decide

/-- Bundled `simp` set for the six writhe-sign values. -/
theorem writheType_up      : weakType .up = WeakType.upType        := by decide
theorem writheType_charm   : weakType .charm = WeakType.upType     := by decide
theorem writheType_top     : weakType .top = WeakType.upType       := by decide
theorem writheType_down    : weakType .down = WeakType.downType    := by decide
theorem writheType_strange : weakType .strange = WeakType.downType := by decide
theorem writheType_bottom  : weakType .bottom = WeakType.downType  := by decide

/-! ### Orthogonality to the generation winding (the load-bearing content) -/

/-- The generation label reproduces the lepton-partner `T(2,n)` dictionary
    values. -/
theorem genWinding_values :
    genWinding .up = 3 ∧ genWinding .charm = 5 ∧ genWinding .top = 7 ∧
    genWinding .down = 3 ∧ genWinding .strange = 5 ∧ genWinding .bottom = 7 := by
  refine ⟨rfl, rfl, rfl, rfl, rfl, rfl⟩

/-- **Charm and strange share the generation winding** (both `n = 5`) — the
    exact collision `winding_content_not_injective` records. -/
theorem charm_strange_same_generation :
    genWinding .charm = genWinding .strange := rfl

/-- **…yet carry opposite `T₃`.** The signed-writhe refinement separates
    them: charm `+½`, strange `−½`.  This is the datum the unsigned winding
    lacked. -/
theorem charm_strange_differ_T3 : T3 .charm ≠ T3 .strange := by
  simp only [T3, writheSign_charm, writheSign_strange]; norm_num

/-- Charm is up-type, strange is down-type — at the same generation. -/
theorem charm_up_strange_down :
    weakType .charm = WeakType.upType ∧ weakType .strange = WeakType.downType := by
  decide

/-- **`T₃` is orthogonal to generation, in general.** Whenever two quarks
    share the generation winding but sit in different weak sectors, their
    `T₃` differ. So `T₃` is a nontrivial grading transverse to `genWinding`. -/
theorem T3_orthogonal_to_generation :
    ∀ q q' : Quark, genWinding q = genWinding q' → weakType q ≠ weakType q' →
      T3 q ≠ T3 q' := by
  intro q q' _ hsec
  cases q <;> cases q' <;>
    simp only [T3, writheSign_up, writheSign_charm, writheSign_top,
      writheSign_down, writheSign_strange, writheSign_bottom,
      writheType_up, writheType_charm, writheType_top,
      writheType_down, writheType_strange, writheType_bottom] at hsec ⊢ <;>
    first
      | exact absurd rfl hsec
      | norm_num

/-! ### `T₃` is `ℤ/2`-valued `±½` (fundamental SU(2) weights) -/

/-- Every quark's `T₃` is exactly `+½` or `−½`. -/
theorem T3_mem (q : Quark) : T3 q = 1/2 ∨ T3 q = -1/2 := by
  cases q <;>
    simp only [T3, writheSign_up, writheSign_charm, writheSign_top,
      writheSign_down, writheSign_strange, writheSign_bottom] <;> norm_num

/-- The sign of the writhe is the up/down type (definitional bridge). -/
theorem writhe_pos_iff_upType (q : Quark) :
    0 < signedWrithe q ↔ weakType q = WeakType.upType := by
  cases q <;> decide

/-! ### Gell-Mann–Nishijima closure (derive-then-CHECK) -/

/-- The measured electric charges of the six quarks (SM data, in units of
    `e`). Up-type `+2/3`, down-type `−1/3`. -/
def emCharge : Quark → ℚ
  | .up | .charm | .top       => 2/3
  | .down | .strange | .bottom => -1/3

/-- The weak hypercharge of the **left-handed** quark doublet, `Y = 1/3`
    (the same for both members of a doublet). Entered as SM data here; its
    topological derivation is the sibling hypercharge-twist attack (#4561).
    In the GMN normalisation `Q = T₃ + Y/2`, `Y = 2(Q − T₃)` gives `1/3`
    for every left quark. -/
def hyperchargeLeft : Quark → ℚ := fun _ => 1/3

/-- **Gell-Mann–Nishijima holds for the topologically-derived `T₃`.**
    `Q = T₃ + Y/2` for every quark, with `T₃ = sign(κ)/2` (the quark strand's
    crossing orientation) and the SM `Q`, `Y`.  This is the check, not a definition:
    had the sign convention or the `½` normalisation been wrong, it would
    fail.  It does not. -/
theorem gellMannNishijima (q : Quark) :
    emCharge q = T3 q + hyperchargeLeft q / 2 := by
  cases q <;>
    simp only [emCharge, T3, hyperchargeLeft, writheSign_up, writheSign_charm,
      writheSign_top, writheSign_down, writheSign_strange, writheSign_bottom] <;>
    norm_num

/-- **GMN inverted: the derived `T₃` equals the SM value `Q − Y/2`.** Makes
    the check explicit — the topological grading recovers exactly the weak
    isospin the SM assigns, for all six quarks. -/
theorem T3_eq_charge_minus_halfY (q : Quark) :
    T3 q = emCharge q - hyperchargeLeft q / 2 := by
  have := gellMannNishijima q; linarith

/-! ### How WIDE the GMN check actually is — two rows, not six

`gellMannNishijima` is quantified over all six quarks, and it is tempting to
report it as six independent confirmations.  It is not, and the theorems here
make the collapse machine-checked so that no summary can widen it by accident.

`hyperchargeLeft` is a **constant** function, and both `emCharge` and `T3` are
functions of `weakType` alone.  Every one of the three quantities entering
`Q = T₃ + Y/2` therefore depends only on the up/down-type bit, so the six cases
supply exactly **two** distinct arithmetic rows:

    up-type:    2/3 = +1/2 + 1/6
    down-type: −1/3 = −1/2 + 1/6

That is one sign correlation plus one normalisation, checked twice — a genuine
derive-then-check (a wrong sign or a wrong `½` still breaks it), but a
*two-row* one.  The generation index `n ∈ {3,5,7}` never enters GMN at all;
it is exactly the datum the relation is blind to. -/

/-- The left-doublet hypercharge is constant across all six quarks — it carries
no per-quark information into the GMN check. -/
theorem hyperchargeLeft_constant (q q' : Quark) :
    hyperchargeLeft q = hyperchargeLeft q' := rfl

/-- **Every GMN ingredient factors through the up/down-type bit.**  Two quarks
of the same `weakType` are indistinguishable to `Q`, `T₃` and `Y` alike, however
different their generation. -/
theorem gmn_data_factors_through_weakType (q q' : Quark)
    (h : weakType q = weakType q') :
    emCharge q = emCharge q' ∧ T3 q = T3 q' ∧
      hyperchargeLeft q = hyperchargeLeft q' := by
  cases q <;> cases q' <;>
    simp_all [emCharge, T3, hyperchargeLeft,
      writheType_up, writheType_charm, writheType_top,
      writheType_down, writheType_strange, writheType_bottom,
      writheSign_up, writheSign_charm, writheSign_top,
      writheSign_down, writheSign_strange, writheSign_bottom]

/-- The up-type GMN row. -/
def gmnRowUp : ℚ × ℚ × ℚ := (2/3, 1/2, 1/3)

/-- The down-type GMN row. -/
def gmnRowDown : ℚ × ℚ × ℚ := (-1/3, -1/2, 1/3)

/-- **The GMN check has exactly two distinct rows.**  Every one of the six
quarks maps onto one of `gmnRowUp` / `gmnRowDown`, and those two are distinct.
So `gellMannNishijima` is two independent equations restated six times — not
six confirmations.

Stated by exhibiting the rows rather than as a `Finset.card`, because `Rat`
decidable equality does not reduce in the kernel inside `Finset.image`. -/
theorem gmn_check_has_two_distinct_rows :
    gmnRowUp ≠ gmnRowDown ∧
    ∀ q : Quark, (emCharge q, T3 q, hyperchargeLeft q) = gmnRowUp ∨
                 (emCharge q, T3 q, hyperchargeLeft q) = gmnRowDown := by
  refine ⟨by simp [gmnRowUp, gmnRowDown, Prod.ext_iff]; norm_num, fun q => ?_⟩
  cases q <;>
    simp only [emCharge, T3, hyperchargeLeft, gmnRowUp, gmnRowDown,
      writheSign_up, writheSign_charm, writheSign_top,
      writheSign_down, writheSign_strange, writheSign_bottom,
      Prod.mk.injEq] <;> norm_num

/-- **The generation is strictly finer than the GMN data.**  `u`, `c`, `t` carry
three different windings but land on the *same* GMN row — the precise sense in
which the relation is blind to the generation index. -/
theorem genWinding_finer_than_gmn_data :
    genWinding .up ≠ genWinding .charm ∧
    genWinding .charm ≠ genWinding .top ∧
    (emCharge .up, T3 .up, hyperchargeLeft .up)
      = (emCharge .charm, T3 .charm, hyperchargeLeft .charm) ∧
    (emCharge .charm, T3 .charm, hyperchargeLeft .charm)
      = (emCharge .top, T3 .top, hyperchargeLeft .top) := by
  refine ⟨by decide, by decide, ?_, ?_⟩ <;>
    simp only [emCharge, T3, writheSign_up, writheSign_charm, writheSign_top,
      hyperchargeLeft]

/-! ### Doublet (charged-current W±) structure -/

/-- The `SU(2)_L` doublet partner (up-type ↔ down-type within a generation)
    — the `W±` charged-current transition `u ↔ d`, `c ↔ s`, `t ↔ b`. -/
def partner : Quark → Quark
  | .up => .down       | .down => .up
  | .charm => .strange | .strange => .charm
  | .top => .bottom    | .bottom => .top

/-- **The partner map raises/lowers `T₃` by one unit at fixed generation** —
    the `ΔT₃ = ±1` selection rule of the charged current, and a second
    witness that `T₃` is transverse to `genWinding`. -/
theorem partner_flips_T3_same_generation (q : Quark) :
    genWinding (partner q) = genWinding q ∧ T3 (partner q) = - T3 q := by
  cases q <;>
    refine ⟨rfl, ?_⟩ <;>
    simp only [partner, T3, writheSign_up, writheSign_charm, writheSign_top,
      writheSign_down, writheSign_strange, writheSign_bottom] <;> norm_num

/-! ### The honest open remainder — conjecture class, NO instance (§3b-tax) -/

/-- **Primary conjecture (open — deliberately NO instance).**

    The arithmetic above is proved unconditionally.  What is *conjectural* is
    that the writhe-sign grading `T₃` is the **canonical** weak isospin — i.e.
    that there is a framework-intrinsic net-signed-crossing map
    `κ : Quark → ℤ`, arising from the *actual* canonical meson/`⋈_K` braids
    (not entered as data), such that:

    * `writhe_magnitude_is_generation` — its magnitude is the generation
      winding (so the split is genuinely into (generation)×(sign));
    * `sign_forced_by_bowtie` — its sign is *forced* by the strong-isospin
      `⋈_K` orientation (`pp = σ_g` positive ⇒ up-type positive), not merely
      consistent with it;
    * `gmn_with_derived_hypercharge` — GMN closes with a *framework-derived*
      hypercharge `Y` (the #4561 twist invariant), not the SM input used in
      `gellMannNishijima`.

    Content-bearing (each field is a `∀`-quantified constraint in the shape of
    the claim), and **no instance is provided**: constructing the canonical
    `κ` from the braid category and the derived `Y` is the open step, which
    reduces to the SU(3)-flavour / CKM sector.  A trivial `κ := signedWrithe`,
    `Y := hyperchargeLeft` would *fabricate* closure over this finite toy and
    is forbidden (§3b-tax: do not fabricate an instance to close an open
    primary; the openness is physical, not formal).

    **Note (2026-11-21, owner rulings 2026-11-20 / 2026-11-21).** Under the
    ruling that a quark is an unknot strand carrying one crossing letter, the
    net signed crossing of the quark strand in `B₃` has magnitude `1`, not
    `n`.  So `writhe_magnitude_is_generation` can no longer be met by reading
    `κ` off the quark strand's own crossings; its magnitude has to come from
    the lepton partner `T(2,n)`.  The field's statement is unchanged; what
    changes is that "net-signed-crossing map from the canonical braids" above
    now means "orientation of the quark strand times its partner's crossing
    count".  Whether a framework-intrinsic map of that composite kind exists
    is the open question this class records. -/
class CanonicalWeakIsospinFromBowtie
    (κ : Quark → ℤ) (Y : Quark → ℚ) : Prop where
  /-- |κ| recovers the generation winding: κ splits as (generation)×(sign). -/
  writhe_magnitude_is_generation : ∀ q, (κ q).natAbs = genWinding q
  /-- the sign is the `⋈_K`-forced up/down orientation. -/
  sign_forced_by_bowtie : ∀ q, (0 < κ q ↔ weakType q = WeakType.upType)
  /-- GMN closes with the framework-derived hypercharge `Y`. -/
  gmn_with_derived_hypercharge :
    ∀ q, emCharge q = ((κ q).sign : ℚ) / 2 + Y q / 2

end QOU.ParticleInteractions.WeakIsospinT3
