import Mathlib.Tactic

/-
  Routing the binding ISOVECTOR coefficient into the W_λ keystone residual-(i).

  Follow-up to `DeltaLambdaWritheConstantB.lean` (#3114) and the keystone
  residual-(i) reduction (#3106, merged): residual-(i) is now ONE open
  conjecture `BWVacuumRowIsHecke` (`bwS0 λ = d_q(λ)/D`), from which the W_λ
  Plancherel/Verlinde measure `μ(λ) = d_q(λ)²/D²` is derived.

  The Δ_λ binding residual's bar-ODD (isovector) part `b·T₃` is the **chiral
  residue** of the categorical mass (`QOU.WedderburnMass.chirality_residue_mass_term`'s
  `mass_chiral`), homed on the Bring surface via the Reeb involution `ξ ↦ −ξ`
  (`brings-surface/archimedean-chirality.md`) and the A₅ Galois `√5 ↦ −√5` twist.
  This file formalizes that the binding isovector closure is **downstream of the
  SAME keystone chiral datum** — the per-writhe weight `κ` IS the chiral-residue
  weight of the W_λ measure, whose value routes to `BWVacuumRowIsHecke`.

  Discipline: §3b-cond conditional; the chiral identification is the (single,
  keystone-shared) conjectural hypothesis; the binding consequence is DERIVED.
  NO fit: `κ` is the keystone chiral weight (an output of CAL-1/2/3 + the gated
  identification), never tuned to `−0.437`/`−√3`. The test stays `residual b → 0`.

  All `ring` over a generic `[CommRing R]` (§7c).

  -- Ref: [leitner2026] docs/audits/2026-06-29-kappa-framing-route-refuted.md;
  --      QOU.BraidKnot keystone residual-(i) `BWVacuumRowIsHecke` (PR #3106);
  --      QOU.WedderburnMass.chirality_residue_mass_term (mass_chiral).
-/

namespace QOU.BraidKnot

/-- **§3b-cond conditional class — the keystone-shared chiral identification.**
The Δ_λ binding residual's isovector (bar-odd) part is the chiral residue of the
W_λ Plancherel measure, carried by the writhe's isovector part `2(Z−N)` with an
**A-independent** chiral weight `κ`.

The conjectural content is `bindingOdd_eq_chiral` — a parameter-quantified
identification (not `True`, not the downstream conclusion): the binding's odd
part equals `κ·2(Z−N)`, with `κ` the chiral-residue weight of `μ(λ)=d_q²/D²`. Its
open value routes to the keystone's single open conjecture `BWVacuumRowIsHecke`;
no instance is fabricated (the value stays open, gated, unfit). -/
class WLambdaChiralBinding (R : Type*) [CommRing R] where
  /-- The chiral-residue weight from the keystone W_λ Plancherel measure
  `μ(λ)=d_q²/D²` (chiral part). Open value ⟶ `BWVacuumRowIsHecke`; never a fit. -/
  kappa : R
  /-- The binding residual's isovector (bar-odd) part, as a function of `(Z, N)`. -/
  bindingOdd : Int → Int → R
  /-- **Identification (conjectural content).** The binding odd part is the chiral
  residue carried by the writhe's isovector part `2(Z−N)` (`writhe = 4Z = 2A +
  2(Z−N)`, the A-independent isovector slope), weight `κ`. -/
  bindingOdd_eq_chiral : ∀ Z N : Int, bindingOdd Z N = kappa * (2 * (Z - N))

/-- **Conditional (proved; the chiral identification is the hypothesis).** Given
the keystone chiral identification, the binding isovector mirror difference is
`4·κ·(Z−N)` — **A-independent**, with the per-`T₃` coefficient `b = 4κ` fixed by
the keystone chiral weight `κ`. This routes the binding isovector closure into the
SAME single open conjecture as the W_λ keystone (`BWVacuumRowIsHecke`): once `κ`
is derived there, the binding `b` follows, and the test `residual b → 0` becomes
a binding-side check on the keystone. -/
theorem binding_isovector_mirror_from_chiral {R : Type*} [CommRing R]
    [c : WLambdaChiralBinding R] (Z N : Int) :
    c.bindingOdd Z N - c.bindingOdd N Z = 4 * c.kappa * (Z - N) := by
  rw [c.bindingOdd_eq_chiral, c.bindingOdd_eq_chiral]; ring

/-- **Corollary (A-independence of `b`).** The binding isovector coefficient does
not depend on `A`: for any two mass numbers, the same chiral weight `κ` governs
the mirror difference. Concretely, the per-`(Z−N)` slope is `2κ` at every `A`
(here shown as the mirror difference depending only on `κ` and `Z−N`, not on
`Z+N`). -/
theorem binding_isovector_A_independent {R : Type*} [CommRing R]
    [c : WLambdaChiralBinding R] (Z N Z' N' : Int) (h : Z - N = Z' - N') :
    c.bindingOdd Z N - c.bindingOdd N Z
      = c.bindingOdd Z' N' - c.bindingOdd N' Z' := by
  rw [binding_isovector_mirror_from_chiral, binding_isovector_mirror_from_chiral]
  have hR : ((Z : R) - N) = ((Z' : R) - N') := by
    rw [← Int.cast_sub, ← Int.cast_sub, h]
  rw [hR]

end QOU.BraidKnot
