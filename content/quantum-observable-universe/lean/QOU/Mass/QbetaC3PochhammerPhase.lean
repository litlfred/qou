import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.GroupWithZero.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.Mass.QbetaC3PochhammerPhase — the `c_3` bar-odd core as
`S = (q;q)_3 × (resurgent phase)`: the order-3 q-Pochhammer supplies the
ALGEBRAIC magnitude, the phase is the open Δ_ω-sourced resurgent object.

**Scope (read first).** This file welds two facts onto the sorry-free Hopf-cubic
decomposition of `QOU.Mass.QbetaC3HopfResidue` (bean `qou-fk0w`, parallel to
`qou-1dnr`). The bar-odd core of the Q_β precision-ladder coefficient `c_3` is
`S = c_3 + Vol(4₁) = h·D(ũ)` (`h = q − q⁻¹`, `D(ũ)` the open KC22 resurgent
ℚ(√3) ladder — `QbetaC3HopfResidue`, KC21). The owner-steered decomposition:

    S = |(q;q)_3| × (resurgent phase),

where the ALGEBRAIC magnitude is the **order-3 q-Pochhammer**
`(q;q)_3 = (1−q)(1−q²)(1−q³)` (corpus `|(q;q)_3| ≈ 0.0094` at the substrate — the
`|S|_geom` scale, `path_a_extended_light_isotopes.py:197`), and the **phase**
(which carries `S`'s cross-anchor SIGN-swing: proton `S<0`, muon `S>0`) is the
open object sourced by the **alien-calculus `Δ_ω` datum** — Écalle's bridge
equation `Δ_ω f̃ = A_ω ∂f̃`, GGM Stokes constant `−3` for `4₁`, `A_ω = Vol(4₁)/π`
(`qbeta_g3_ggm_stokes_41.py`, `docs/audits/2026-07-20-c3-stokes-route.md`; the
archimedean tail action `A₀ = π²/5` is `QOU.QBeta.HabiroTailAction`).

**Outcome — DERIVED-MODULO-OPEN-PHASE. This NARROWS; it does NOT derive `c_3`.**
The provable content isolates the open piece to the single Δ_ω-sourced bar-even
phase; every theorem below is sorry-free, nothing is wired, `c_3` stays EMPIRICAL.

**The honest findings (the theorems below).**

* **The `h`-factorization of `(q;q)_3` — the KEY provable structural bridge.**
  Since `(1−q²) = −q·h` (`h = q − q⁻¹`), the order-3 q-Pochhammer factors as
  `(q;q)_3 = h · (−q·(1−q)·(1−q³))` (`qPochhammer3_h_factor`, sorry-free,
  generic `CommRing` via the abstract bar-odd relation `1 − q² = −q·h`; the
  literal `q⁻¹` restatement is `qPochhammer3_h_factor_field`). So BOTH `S = h·D`
  and `(q;q)_3 = h·pochCofactor` carry the SAME automatic bar-odd `h`.

* **⟹ the phase `S/(q;q)_3 = D/pochCofactor` is bar-EVEN** — the `h` cancels
  (`pochhammer_normalization_is_barEven`, sorry-free, division-free; literal
  ratio in `normalization_eq_D_over_cofactor`). This is the exact shape of
  `QbetaC3HopfResidue.carrier_to_S_normalization_is_barEven`: the automatic
  bar-odd carrier is bookkeeping; the genuine open content is the bar-even ratio.

* **The magnitude match `|S|_geom = |(q;q)_3|` forces `phase² = 1`**
  (`phase_is_unit_of_magnitude_match`, sorry-free, over a domain), so the phase
  is a genuine ±1 sign object (`phase_sign_dichotomy`) — `+1` at the proton
  anchor, `−1` at the muon anchor. This is why the bar-even phase must carry the
  full cross-anchor SIGN-swing (`flatPhase_cannot_source_swinging_S`), and why a
  flat phase cannot source both anchors.

* **The decomposition theorem** `S = (q;q)_3 · phase`
  (`pochhammer_phase_decomposition`) is PROVED **modulo** the conditional class
  `[ResurgentPhaseFromAlienDatum]` (§3b-cond) — a *genuine composition* of the
  two `h`-factorizations with the class's Δ_ω phase relation, NOT a self-assuming
  projection (the conclusion is not a class field; it is derived from
  `phase·pochCofactor = D`).

**What stays OPEN (the conjecture class).** That the phase is *fixed by the
alien-calculus `Δ_ω` datum* (bridge equation `Δ_ω f̃ = A_ω ∂f̃`, `A_ω = Vol(4₁)/π`,
Stokes constant `−3`) rather than free — recorded as a content-bearing **primary
conjecture class** `ResurgentPhaseFromAlienDatum` with **NO instance**. Per KC22
`D(ũ)` is resurgent / non-holonomic (radius → 0), so `phase = D/pochCofactor` is
not a low-order (q-)holonomic scalar to be read off; supplying an instance would
be a fit.

## Honesty (AGENTS.md §Axiomatization is NOT a Proof, §3b, §3b-tax, ck-dk-registry §8)

* The `h`-factorization, bar-even ratio, magnitude→`phase²=1`, sign-dichotomy,
  and (conditional) decomposition are genuine sorry-free ring/field algebra.
* The conjecture class is content-bearing (parameter-quantified equations +
  nonvanishing, no `True`, no empty marker) and has **NO instance** — the honest
  open state. The exact q-Pochhammer supplies only the (automatic) bar-odd `h`
  and the algebraic magnitude; the Δ_ω-sourced bar-even phase is the open core.
* Nothing inverted from Q_β; nothing wired to production; `c_3` stays EMPIRICAL;
  this file changes no rung's tier.

## Base ring (§7c)

The factorization, bar-even ratio, and decomposition are pure ring/field
identities — generic `{R : Type*} [CommRing R]` (one `Field` restatement for the
literal `q⁻¹` / ratio; `NoZeroDivisors` for the magnitude→sign step). No `ℝ`, no
ordering, no `Real.*`; the archimedean substrate evaluation (`|(q;q)_3| ≈ 0.0094`
at `q₀ ≈ 1.10998`, the sign swing) lives downstream in the probe, past the
substrate→archimedean wall.

## References

- [manuscript] `conj:qdifference-kernel-prolongation-symbol`;
  `QOU.Mass.QbetaC3HopfResidue` (KC20/KC21/KC22 carrier + `S = h·D`);
  `QOU.QBeta.HabiroTailAction` (`A₀ = π²/5`);
  `docs/coordination/ck-dk-canonical-registry.md` §9;
  `docs/audits/2026-07-20-c3-stokes-route.md`;
  `docs/audits/2026-07-20-c3-hopf-cubic-residue-exploration.md`;
  `computations/probes/qbeta_g3_ggm_stokes_41.py`;
  `computations/_deprecated/path_a_extended_light_isotopes.py` (`|(q;q)_3|`).
- [garoufalidis-gu-marino2021] https://arxiv.org/abs/2011.07617 (Stokes constants
  = DT integers; the `4₁` peacock pattern, GGM constant `−3`).
-/

namespace QOU.Mass.QbetaC3PochhammerPhase

/-! ### (1) The order-3 q-Pochhammer and its `h`-factorization (the key bridge)

`(q;q)_3 = (1−q)(1−q²)(1−q³)`; using `(1−q²) = −q·h` (`h = q − q⁻¹`) the bar-odd
carrier `h` factors out, `(q;q)_3 = h·pochCofactor`, so the algebraic magnitude
carries the same automatic bar-odd `h` as the target `S = h·D`. -/

/-- The **order-3 q-Pochhammer** `(q;q)_3 = (1−q)(1−q²)(1−q³)` — a finite product,
purely algebraic; its substrate magnitude `|(q;q)_3| ≈ 0.0094` is the anchor-blind
`|S|_geom` scale (archimedean, in the probe). -/
def qPochhammer3 {R : Type*} [CommRing R] (q : R) : R :=
  (1 - q) * (1 - q ^ 2) * (1 - q ^ 3)

/-- The **bar-even cofactor** left after pulling the bar-odd `h` out of `(q;q)_3`:
`pochCofactor(q) = −q·(1−q)·(1−q³)` (so `(q;q)_3 = h·pochCofactor`). -/
def pochCofactor {R : Type*} [CommRing R] (q : R) : R :=
  -q * (1 - q) * (1 - q ^ 3)

/-- **The `h`-factorization of the order-3 q-Pochhammer (sorry-free, division-free,
generic `CommRing`).** Given the bar-odd relation `1 − q² = −q·h` (i.e.
`h = q − q⁻¹`, the KC bar-odd carrier), the order-3 q-Pochhammer factors through
the SAME automatic bar-odd `h`:

    (q;q)_3 = h · pochCofactor(q),   pochCofactor(q) = −q·(1−q)·(1−q³).

This is the structural bridge: both `S = h·D` (KC21) and `(q;q)_3 = h·pochCofactor`
carry one `h`, so the phase `S/(q;q)_3` is bar-even. -/
theorem qPochhammer3_h_factor {R : Type*} [CommRing R] (q h : R)
    (hRel : 1 - q ^ 2 = -q * h) :
    qPochhammer3 q = h * pochCofactor q := by
  unfold qPochhammer3 pochCofactor
  linear_combination (1 - q) * (1 - q ^ 3) * hRel

/-- **Literal `q⁻¹` form (`Field`, `q ≠ 0`).** With `h = q − q⁻¹` written out,
`(q;q)_3 = (q − q⁻¹) · pochCofactor(q)`. The `Field`/`q ≠ 0` hypothesis only
licenses `q⁻¹`; the content is the division-free `qPochhammer3_h_factor`. -/
theorem qPochhammer3_h_factor_field {F : Type*} [Field F] (q : F) (hq : q ≠ 0) :
    qPochhammer3 q = (q - q⁻¹) * pochCofactor q := by
  have hRel : 1 - q ^ 2 = -q * (q - q⁻¹) := by
    field_simp
    ring
  exact qPochhammer3_h_factor q (q - q⁻¹) hRel

/-! ### (2) The phase `S/(q;q)_3 = D/pochCofactor` is bar-EVEN (the `h` cancels)

Both `S = h·D` (KC21) and `(q;q)_3 = h·pochCofactor` are bar-odd, so both equal
`h·(bar-even)`; the `h` cancels in the phase. Same shape as
`QbetaC3HopfResidue.carrier_to_S_normalization_is_barEven`. -/

/-- **The phase `S/(q;q)_3` is bar-even (sorry-free, division-free).** Given the
KC21 factorization `S = h·D` and the KC/§1 factorization `(q;q)_3 = h·pochCof`,
the bar-odd carrier `h` cancels:

    S · pochCof = D · (q;q)_3,

i.e. `S/(q;q)_3 = D/pochCof` — a purely **bar-even** quantity. The order-3
q-Pochhammer supplies only the automatic bar-odd `h`; the genuine open content is
the bar-even phase `D/pochCof`. -/
theorem pochhammer_normalization_is_barEven {R : Type*} [CommRing R]
    (h pochCof dLadder smoothS poch3 : R)
    (hPoch : poch3 = h * pochCof)
    (hS : smoothS = h * dLadder) :
    smoothS * pochCof = dLadder * poch3 := by
  linear_combination pochCof * hS - dLadder * hPoch

/-- **Literal bar-even ratio form (`Field`).** With `pochCof ≠ 0` and `poch3 ≠ 0`,
the phase is exactly `S/(q;q)_3 = D/pochCof`. The `Field`/nonvanishing hypotheses
only license division; the content is the division-free
`pochhammer_normalization_is_barEven`. -/
theorem normalization_eq_D_over_cofactor {F : Type*} [Field F]
    (h pochCof dLadder smoothS poch3 : F)
    (hPoch : poch3 = h * pochCof)
    (hS : smoothS = h * dLadder)
    (hpoch : poch3 ≠ 0) (hcof : pochCof ≠ 0) :
    smoothS / poch3 = dLadder / pochCof := by
  have key : smoothS * pochCof = dLadder * poch3 :=
    pochhammer_normalization_is_barEven h pochCof dLadder smoothS poch3 hPoch hS
  rw [div_eq_div_iff hpoch hcof]
  linear_combination key

/-! ### (3) The magnitude match `|S|_geom = |(q;q)_3|` forces `phase² = 1`

The corpus anchor-blind magnitude `|S|_geom ≈ 0.0094 = |(q;q)_3|` says the phase
has unit magnitude; algebraically (squared, to avoid `abs`) `S² = (q;q)_3²`
combined with `S = (q;q)_3·phase` gives `phase² = 1` — the phase is a genuine ±1
sign object, carrying the cross-anchor sign-swing. -/

/-- **Magnitude match ⟹ the phase is a unit (`phase² = 1`), sorry-free.** Over any
domain, if `S = (q;q)_3·phase` and the anchor-blind squared magnitudes agree
`S² = (q;q)_3²` (the corpus `|S|_geom = |(q;q)_3|`), then `phase² = 1` — the phase
carries no magnitude, only a sign. -/
theorem phase_is_unit_of_magnitude_match {R : Type*} [CommRing R] [NoZeroDivisors R]
    (poch3 phase smoothS : R)
    (hDecomp : smoothS = poch3 * phase)
    (hMag : smoothS ^ 2 = poch3 ^ 2)
    (hpoch : poch3 ≠ 0) :
    phase ^ 2 = 1 := by
  have h2 : poch3 ^ 2 * (phase ^ 2 - 1) = 0 := by
    linear_combination hMag - hDecomp * (smoothS + poch3 * phase)
  have hpoch2 : poch3 ^ 2 ≠ 0 := pow_ne_zero 2 hpoch
  rcases mul_eq_zero.mp h2 with h | h
  · exact absurd h hpoch2
  · exact sub_eq_zero.mp h

/-- **The unit phase is `±1` (sorry-free).** `phase² = 1` over a domain gives
`phase = 1 ∨ phase = −1` — the phase is the proton (`+1`) / muon (`−1`) sign
selector, the carrier of `S`'s cross-anchor sign-swing. -/
theorem phase_sign_dichotomy {R : Type*} [CommRing R] [NoZeroDivisors R]
    (phase : R) (h : phase ^ 2 = 1) :
    phase = 1 ∨ phase = -1 := by
  have hfac : (phase - 1) * (phase + 1) = 0 := by linear_combination h
  rcases mul_eq_zero.mp hfac with h1 | h1
  · exact Or.inl (sub_eq_zero.mp h1)
  · exact Or.inr (eq_neg_of_add_eq_zero_left h1)

/-- **A flat (anchor-invariant) phase cannot source the sign-swinging `S`
(sorry-free).** `phase` is `+1` at the proton anchor and `−1` at the muon anchor
(`phase_sign_dichotomy`); a single flat value pinned to both would force
`phase_p = phase_m`, contradicting the measured sign-swing (`hSwing`). So the
phase MUST be the anchor-dependent Δ_ω-sourced object — it cannot be a constant. -/
theorem flatPhase_cannot_source_swinging_S {R : Type*} [CommRing R]
    (phaseFlat phase_p phase_m : R)
    (hP : phaseFlat = phase_p) (hM : phaseFlat = phase_m) (hSwing : phase_p ≠ phase_m) :
    False :=
  hSwing (hP ▸ hM)

/-! ### (4) The decomposition `S = (q;q)_3 · phase`, conditional on the alien datum

The decomposition is PROVED modulo the Δ_ω conditional class (§3b-cond): a genuine
composition of the two `h`-factorizations with the class's phase relation
`phase·pochCof = D`, NOT a self-assuming projection. -/

/-- Substrate datum for the Pochhammer-phase `c_3` decomposition. Carries the
decomposition data — the order-3 q-Pochhammer `poch3 = (q;q)_3`, its bar-even
cofactor `pochCof`, the bar-odd carrier `hCarrier = q − q⁻¹`, the smooth bar-odd
object `smoothS = S = h·D`, the open resurgent ladder `dLadder = D(ũ)`, the
resurgent `phase` — and the **alien-calculus `Δ_ω` datum** it must be sourced by:
`aOmega = A_ω = Vol(4₁)/π`, the GGM Stokes constant `stokesConst = −3`, and the
Écalle bridge-equation data `alienDeriv = Δ_ω f̃`, `ordinaryDeriv = ∂f̃`. Data —
asserts nothing. -/
structure PochhammerPhaseDatum (R : Type*) [CommRing R] where
  /-- The order-3 q-Pochhammer `(q;q)_3` (the algebraic magnitude carrier). -/
  poch3 : R
  /-- The bar-even cofactor `−q·(1−q)·(1−q³)` (`(q;q)_3 = h·pochCof`). -/
  pochCof : R
  /-- The bar-odd carrier `h = q − q⁻¹`. -/
  hCarrier : R
  /-- The smooth bar-odd `c_3` object `S = c_3 + Vol(4₁) = h·D(ũ)`. -/
  smoothS : R
  /-- The OPEN bar-even resurgent ℚ(√3) ladder value `D(ũ)` (KC22). -/
  dLadder : R
  /-- The OPEN resurgent phase (unit magnitude; carries the sign-swing). -/
  phase : R
  /-- The alien-calculus action `A_ω = Vol(4₁)/π`. -/
  aOmega : R
  /-- The GGM Stokes constant for `4₁` (DT integer `−3`). -/
  stokesConst : R
  /-- The alien derivative `Δ_ω f̃` (bridge-equation LHS). -/
  alienDeriv : R
  /-- The ordinary derivative `∂f̃` (bridge-equation RHS factor). -/
  ordinaryDeriv : R

/-- **§3b primary conjecture class — the resurgent phase is fixed by the alien
`Δ_ω` datum.**

    `@conjecture: primary`

    The honest OPEN core of the Pochhammer-phase decomposition. It asserts that the
    resurgent `phase` is *sourced by the alien-calculus datum* — Écalle's bridge
    equation `Δ_ω f̃ = A_ω ∂f̃` (`bridge_equation`), the GGM Stokes constant `−3` for
    `4₁` (`stokes_datum`), `A_ω = Vol(4₁)/π ≠ 0` (`aOmega_nonzero`) — via the phase
    relation `phase·pochCof = D` (`phase_from_alien`, the OPEN content: the phase
    ties the algebraic cofactor to the resurgent ladder `D(ũ)`). Together with the
    two `h`-factorizations (`smoothS_factorization`, `poch3_factorization`,
    structural/§1) this DERIVES the decomposition `S = (q;q)_3·phase`
    (`pochhammer_phase_decomposition`) — the conclusion is NOT a field, so the class
    is non-degenerate (not a self-assuming projection). The phase is nontrivial
    (`phase_nontrivial`, `phase ≠ 1`, consistent with its `±1` sign-swing) and the
    bar-odd channel is real (`smoothS_nonzero`). **No instance is supplied** — per
    KC22 `D(ũ)` is resurgent / non-holonomic (radius → 0), so `phase = D/pochCof`
    is not a scalar to be read off; an instance would be a fit. -/
-- Ref: [garoufalidis-gu-marino2021] https://arxiv.org/abs/2011.07617
-- Ref: [manuscript] conj:qdifference-kernel-prolongation-symbol;
--      QOU.Mass.QbetaC3HopfResidue; QOU.QBeta.HabiroTailAction;
--      docs/coordination/ck-dk-canonical-registry.md §9;
--      docs/audits/2026-07-20-c3-stokes-route.md;
--      docs/audits/2026-07-20-c3-hopf-cubic-residue-exploration.md
class ResurgentPhaseFromAlienDatum {R : Type*} [CommRing R]
    (d : PochhammerPhaseDatum R) : Prop where
  /-- KC21 bar-odd factorization of the target: `S = h·D`. -/
  smoothS_factorization : d.smoothS = d.hCarrier * d.dLadder
  /-- §1 `h`-factorization of the magnitude: `(q;q)_3 = h·pochCof`. -/
  poch3_factorization : d.poch3 = d.hCarrier * d.pochCof
  /-- **Écalle bridge equation** `Δ_ω f̃ = A_ω ∂f̃` — the alien derivative of the
      resurgent series is `A_ω` times its ordinary derivative (the source of the
      Stokes / non-perturbative phase datum). -/
  bridge_equation : d.alienDeriv = d.aOmega * d.ordinaryDeriv
  /-- **The OPEN phase relation** `phase·pochCof = D`: the resurgent phase ties the
      algebraic cofactor to the open resurgent ladder `D(ũ)`. The whole open
      content — `phase` fixed by the Δ_ω datum rather than free. -/
  phase_from_alien : d.phase * d.pochCof = d.dLadder
  /-- The GGM Stokes constant for `4₁` is the DT integer `−3`. -/
  stokes_datum : d.stokesConst = -3
  /-- `A_ω = Vol(4₁)/π ≠ 0` — the bridge equation is nontrivial. -/
  aOmega_nonzero : d.aOmega ≠ 0
  /-- The phase is nontrivial (`≠ 1`), consistent with its `±1` sign-swing. -/
  phase_nontrivial : d.phase ≠ 1
  /-- There IS a bar-odd channel to derive — the decay-face object is nonzero. -/
  smoothS_nonzero : d.smoothS ≠ 0

/-- **The decomposition `S = (q;q)_3 · phase` (conditional, sorry-free, §3b-cond).**

    Given the alien-datum class, the smooth bar-odd `c_3` object decomposes as the
    order-3 q-Pochhammer times the resurgent phase:

        S = (q;q)_3 · phase.

    This is a **genuine composition** — it is derived from the two `h`-factorizations
    (`S = h·D`, `(q;q)_3 = h·pochCof`) and the class's OPEN phase relation
    `phase·pochCof = D`, by cancelling `h`. The conclusion is NOT a class field, so
    this is not a self-assuming projection. It is a rigorous conditional result:
    fully verified modulo the single, named, class-axiomatised resurgent-phase
    input. It does **NOT** derive `c_3` — the phase `= D/pochCof` is the open
    resurgent object. -/
theorem pochhammer_phase_decomposition {R : Type*} [CommRing R]
    (d : PochhammerPhaseDatum R) [self : ResurgentPhaseFromAlienDatum d] :
    d.smoothS = d.poch3 * d.phase := by
  linear_combination self.smoothS_factorization
    - d.phase * self.poch3_factorization
    - d.hCarrier * self.phase_from_alien

end QOU.Mass.QbetaC3PochhammerPhase
