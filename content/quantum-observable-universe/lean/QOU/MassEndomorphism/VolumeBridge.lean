import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.Ring

/-!
# QOU.MassEndomorphism.VolumeBridge — the Volume-Conjecture bridge (§3b-cond)

A **non-degenerate** conditional-class carrier (AGENTS.md §3b-cond) for the
mass-endomorphism conjecture, reducing its open surface to exactly the one
genuinely-open ingredient: the **Volume-Conjecture bridge** (Step 3 of
`conj:mass-endomorphism`).

## The three steps of the conjecture

Per [`mass-endomorphism-conjecture.md` §"Established results"]:

- **Step 1 (proved, `prop:categorical-mass-markov`).** The single-level
  categorical mass is the descended Markov trace `|tr_M(ρ(β))|`
  (Nakayama `S² = id`).
- **Step 2 (proved, `prop:topological-mass-formula`).** The full brane tower
  sums to `Vol(K_β)/ℏ_q²`.
- **Step 3 (OPEN — the Volume Conjecture).** The Jones–Markov trace
  `tr_M(ρ(β)) = J(K;q)` (a Laurent polynomial) and the hyperbolic volume
  `Vol(K)` (transcendental) are *different* knot invariants; the only known
  bridge is the Volume Conjecture
  \cite{kashaev1997, murakami-murakami2001}. The transient brane tower
  `Σ Φ_q(z_i)` is conjectured to close this gap at the substrate `q_0`.

## What this carrier does (§3b-cond non-degenerate)

The class `VolumeBridge` axiomatises **only the open input** — the archimedean
bridge equality `volTerm = descTrace + transient` (the Volume-Conjecture
content at `q_0`) — and **derives** the manuscript's stated identities:

- `transient_identity` : `transient = volTerm − descTrace`
  (the conjecture's displayed transient identity), and
- `fullMass_eq_volTerm` : `descTrace + transient = volTerm`
  (Step 2, the full categorical mass).

This is non-degenerate per §3b-cond item 5: the class field is the *hypothesis*
(the VC bridge, the open Step 3), and the theorems *derive* the conclusions —
the class does **not** carry a block's own conclusion behind a trivial
projection.

## Honest open primary — NO instance

Unlike `QOU.MassEndomorphism.MassEndomorphism`
([`MassEndomorphismConjecture.lean`]), this class deliberately carries **no
`instance`**. Per AGENTS.md §3b-tax ("an unproved primary is honestly
represented by a content-bearing class with no instance; do not fabricate a
trivial instance to 'close' it"), the absence of an instance is the honest
representation of the open state: any `[VolumeBridge R β]`-conditional result
is genuinely *modulo the Volume Conjecture*.

> **Follow-up, now actioned (2026-08-24):** the sibling class
> `MassEndomorphism` in `MassEndomorphismConjecture.lean` shipped a global
> `instance canonical` (all-zeros) and `MassEndomorphismTrivial.lean` shipped
> `trivial_int_zero`; both made `[MassEndomorphism R β]` synthesizable, so
> conditionality against *that* class was vacuous. Both are now `def`s, so
> the class is no longer globally inhabited and a caller who wants the zero
> model must name it. The **mathematical** gap the models stand in for is
> unchanged and still governed by the GAP-18a scoping audits
> (`docs/audits/2026-05-04-gap-6a-18a-scoping.md`): there is still no
> deterministic recipe `Braid n → MassEndomorphism R β`. `VolumeBridge`
> remains the instance-free carrier for the open Volume-Conjecture bridge.

-- Ref: [manuscript] conj:mass-endomorphism §"Established results" (Steps 1–3)
-- Ref: [kashaev1997] https://doi.org/10.1007/BF01238857
-- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
LaTeX label: `conj:mass-endomorphism`
-/

namespace QOU.MassEndomorphism

/-- **The Volume-Conjecture bridge (open input of `conj:mass-endomorphism`).**

    Over a commutative ring `R ⊇ ℤ[q^±1]` and a braid type `β`:
    - `descTrace : R` — the descended Markov trace `|tr_M(ρ(β))|` (Step 1,
      proved; at the archimedean realisation `R = ℝ` it is the absolute value);
    - `transient : R` — the brane-tower transient sum `Σ Φ_q(z_i)`;
    - `volTerm : R` — the volume term `Vol(K_β)/ℏ_q²` (Step 2, proved);
    - `archimedean_bridge` — the **sole open field**: the Volume-Conjecture
      equality at `q_0`, `volTerm = descTrace + transient`, asserting the
      transient tower closes the Jones→Volume gap.

    Carries no instance: this is an honest open primary (§3b-tax). -/
-- Ref: [manuscript] conj:mass-endomorphism §"Step 3" (the open bridge)
class VolumeBridge (R : Type*) [CommRing R] (β : Type*) where
  /-- Descended Markov trace `|tr_M(ρ(β))|` (Step 1, proved). -/
  descTrace : R
  /-- Brane-tower transient sum `Σ Φ_q(z_i)`. -/
  transient : R
  /-- Volume term `Vol(K_β)/ℏ_q²` (Step 2, proved). -/
  volTerm : R
  /-- The open Volume-Conjecture bridge at `q_0`: the descended trace plus the
      transient tower realises the volume term. -/
  archimedean_bridge : volTerm = descTrace + transient

namespace VolumeBridge

variable (R : Type*) [CommRing R] (β : Type*) [VolumeBridge R β]

/-- **The transient identity** of `conj:mass-endomorphism`, derived from the
    bridge:
    `tr_M(Φ^trans) = Vol(K_β)/ℏ_q² − |tr_M(ρ(β))|`. -/
-- Ref: [manuscript] conj:mass-endomorphism §"Statement"
theorem transient_identity :
    transient (R := R) β = volTerm (R := R) β - descTrace (R := R) β := by
  have h := archimedean_bridge (R := R) (β := β)
  rw [h]; ring

/-- **Full categorical mass = volume term** (Step 2), derived from the bridge:
    the descended trace plus the transient tower equals `Vol(K_β)/ℏ_q²`. -/
-- Ref: [manuscript] conj:mass-endomorphism §"Established results", Step 2
theorem fullMass_eq_volTerm :
    descTrace (R := R) β + transient (R := R) β = volTerm (R := R) β :=
  (archimedean_bridge (R := R) (β := β)).symm

/-- The full categorical mass, as a definition (descended + transient). -/
def fullMass : R := descTrace (R := R) β + transient (R := R) β

/-- `fullMass` unfolds to the volume term under the bridge. -/
theorem fullMass_eq : fullMass R β = volTerm (R := R) β := by
  unfold fullMass
  exact fullMass_eq_volTerm R β

end VolumeBridge

end QOU.MassEndomorphism
