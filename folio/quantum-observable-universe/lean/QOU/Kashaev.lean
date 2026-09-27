import QOU.PhiQPiece

/-!
# QOU.Kashaev — Kashaev volume conjecture as a typeclass

The **Kashaev volume conjecture (KVC)** is axiomatised here as a Lean
typeclass.  Any downstream theorem that depends on KVC takes
`[VolumeConjecture q]` as a typeclass argument and is then fully
verified by Lean — the only unproved input is the class instance.

**Formal-chain version.**  This file lives under `lean/QOU/` and is
compiled by `lake build`.  The co-located documentation stub at
`content/quantum-observable-universe/braids-and-knots/kashaev-volume-conjecture.lean`
mirrors this content for `.md`-rendering / sibling-resolution purposes
(per `QOU.GroundRingAnnotations`).

LaTeX label: `conj:kashaev-volume-conjecture`

The conjecture remains **open in general**; instances are constructed
by hand for specific knot families (figure-eight knot, torus knots,
etc.) where the conjecture is actually proved.

## References

- [kashaev1997] Modular dilogarithm, q-deformed knot invariants and the
  asymptotics of the colored Jones polynomial. Lett. Math. Phys. 39 (1997).
  https://doi.org/10.1023/A:1007364912784
- [murakami-murakami2001] The colored Jones polynomial and the simplicial
  volume of a knot. Acta Math. 186 (2001).
  https://doi.org/10.1007/BF02392716
- [manuscript] Ch 3 §sec:calibration-algebraic-mass /
  kashaev-volume-conjecture
-/

namespace QOU.Kashaev

open QOU.PhiQPiece

/-- **Kashaev Volume Conjecture (axiomatised).**

    Encodes the assertion that the hyperbolic volume of `S³ \ K`
    equals the Kashaev limit `2π · lim_N log|J_N(K)| / N` of the
    colored Jones polynomial.

    Any instance of this class supplies:
    - `hypVolume β` — the hyperbolic volume of the complement of the
      closure of `β` (zero when the complement is not hyperbolic).
    - `kashaevLimit β` — the asymptotic limit of the colored Jones
      polynomial.
    - `kvc_holds β` — the conjecture itself, identifying the two.

    The `kvc_holds` field is the **conjectural input**: providing it
    is the role of mathematicians (not Lean).  Downstream theorems
    consuming `[VolumeConjecture q]` are conditional on it. -/
-- Ref: [kashaev1997] Kashaev, "The hyperbolic volume of knots from the quantum dilogarithm," Lett. Math. Phys. 39 (1997)
-- Ref: [murakami-murakami2001] Murakami & Murakami, "The colored Jones polynomials and the simplicial volume of a knot," Acta Math. 186 (2001), arXiv:math/9905075
class VolumeConjecture (q : ℝ) where
  -- Witness: computations/none
  /-- Hyperbolic volume of `S³ \ K_β`, with the convention that
      non-hyperbolic complements contribute zero. -/
  hypVolume : Braid → ℝ
  /-- The Kashaev asymptotic limit `2π · lim_N log|J_N(K)| / N`. -/
  kashaevLimit : Braid → ℝ
  /-- Hyperbolic volume is non-negative. -/
  hypVolume_nonneg : ∀ β, 0 ≤ hypVolume β
  /-- **The conjecture itself**: the Kashaev limit equals the
      hyperbolic volume.  This is the field that plays the role
      of `sorry` for KVC. -/
  kvc_holds : ∀ β, hypVolume β = kashaevLimit β
  /-- The hyperbolic volume of a Φ_q-piece `K_S` (the sub-link selected
      by the smoothing set `S`).  Supplied by the instance (the SnapPy
      bridge layer for concrete knot families); abstract here so callers
      never see a placeholder masquerading as a genuine S-dependent value. -/
  pieceVol : (β : Braid) → Finset (Fin (β.n - 1)) → ℝ
  /-- Piece volumes are non-negative (each is a genuine hyperbolic volume). -/
  pieceVol_nonneg : ∀ β S, 0 ≤ pieceVol β S

/-- The hyperbolic volume of a Φ_q-piece `K_S`, lifted from the
    typeclass.  This is the canonical bridge between the abstract
    `SubLink.hypVolume` field on the geometry side and the typeclass
    `VolumeConjecture.hypVolume` on the analysis side: any concrete
    instance of `VolumeConjecture` populates a real value.

    The per-piece value is now supplied by the `VolumeConjecture`
    instance via the `pieceVol` field (populated by the SnapPy bridge
    layer for concrete knot families); this definition is the thin
    accessor.  Callers never see a placeholder masquerading as a genuine
    S-dependent piece volume — an instance must provide a real value. -/
-- Ref: [manuscript] Ch 3 §sec:calibration-algebraic-mass / kashaev-volume-conjecture
-- Ref: [kashaev1997] Kashaev, "The hyperbolic volume of knots from the quantum dilogarithm," Lett. Math. Phys. 39 (1997)
@[simp]
noncomputable def pieceVolume (q : ℝ) [inst : VolumeConjecture q]
    (β : Braid) (S : Finset (Fin (β.n - 1))) : ℝ :=
  inst.pieceVol β S

/-- The piece volume is non-negative — a genuine hyperbolic volume,
    discharged by the instance field `pieceVol_nonneg`. -/
-- Ref: [manuscript] Ch 3 §sec:calibration-algebraic-mass / kashaev-volume-conjecture
theorem pieceVolume_nonneg (q : ℝ) [inst : VolumeConjecture q]
    (β : Braid) (S : Finset (Fin (β.n - 1))) :
    0 ≤ pieceVolume q β S :=
  inst.pieceVol_nonneg β S

end QOU.Kashaev
