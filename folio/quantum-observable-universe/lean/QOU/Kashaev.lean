import QOU.PhiQPiece
import QOU.Knot.FigureEightVolumeLiterature
import QOU.Knot.BorromeanVolume

/-!
# QOU.Kashaev — Kashaev volume conjecture as a typeclass

The **Kashaev volume conjecture (KVC)** is axiomatised here as a Lean
typeclass.  Any downstream theorem that depends on KVC takes
`[VolumeConjecture q]` as a typeclass argument and is then fully
verified by Lean — the only unproved input is the class instance.

**Formal-chain version.**  This file lives under `lean/QOU/` and is
compiled by `lake build`.  The co-located documentation stub at
`folio/quantum-observable-universe/braids-and-knots/kashaev-volume-conjecture.lean`
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
- [leitner2026] Ch 3 §sec:calibration-algebraic-mass /
  kashaev-volume-conjecture
-/

namespace QOU.Kashaev

open QOU.PhiQPiece

/-- Figure-eight braid `4₁` = closure of `(σ₀σ₁⁻¹)²` on 3 strands
    (`Bool = true` marks a negative crossing). -/
def fourOneBraid : Braid :=
  { n := 3, word := [((0 : Fin 2), false), ((1 : Fin 2), true),
                     ((0 : Fin 2), false), ((1 : Fin 2), true)] }

/-- Borromean braid `B₃` = closure of `(σ₀σ₁⁻¹)³` on 3 strands. -/
def borromeanBraid : Braid :=
  { n := 3, word := [((0 : Fin 2), false), ((1 : Fin 2), true),
                     ((0 : Fin 2), false), ((1 : Fin 2), true),
                     ((0 : Fin 2), false), ((1 : Fin 2), true)] }

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
  /-- The Kashaev invariant `⟨K_β⟩_N` (the `N`-coloured Jones polynomial at
      `e^{2πi/N}`, in absolute value) of the closure of `β`.  No general
      braid-to-invariant map exists in this corpus, so it is carried as data —
      but see the two anchors below, which pin it where the corpus defines it. -/
  kashaevInvariant : Braid → ℕ → ℝ
  /-- **`kashaevLimit` is the limit it is named for** (bean `qou-dx7g`):
      `(2π/N) · log ⟨K_β⟩_N → kashaevLimit β`.  Until 2026-11-20 `kashaevLimit`
      was a free function, so `kvc_holds` related two instance-chosen values
      and `hypVolume := 0, kashaevLimit := 0` satisfied the class. -/
  kashaevLimit_spec : ∀ β, Filter.Tendsto
    (fun N : ℕ => (2 * Real.pi / (N : ℝ)) * Real.log (kashaevInvariant β N))
    Filter.atTop (nhds (kashaevLimit β))
  /-- **Anchor (4₁).** On the figure-eight braid the invariant is the corpus's
      root-of-unity Kashaev sum `QOU.Knot.FigureEightVolume.kashaev`. -/
  kashaevInvariant_fourOne :
    kashaevInvariant fourOneBraid = QOU.Knot.FigureEightVolume.kashaev
  /-- **Anchor (𝓑₃).** On the Borromean braid the invariant is
      `QOU.Knot.FigureEightVolume.borromeanKashaev`. -/
  kashaevInvariant_borromean :
    kashaevInvariant borromeanBraid = QOU.Knot.FigureEightVolume.borromeanKashaev
  /-- **Anchor (4₁).** The hyperbolic volume of the figure-eight complement is
      `VOL_4_1 = 2·Cl₂(π/3)` (Thurston; corpus definition). -/
  hypVolume_fourOne : hypVolume fourOneBraid = QOU.Knot.FigureEightVolume.VOL_4_1
  /-- **Anchor (𝓑₃).** The hyperbolic volume of the Borromean complement is
      `Vol_Borromean = 8·Cl₂(π/2)` (corpus definition). -/
  hypVolume_borromean : hypVolume borromeanBraid = QOU.Archimedean.Vol_Borromean
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
-- Ref: [leitner2026] Ch 3 §sec:calibration-algebraic-mass / kashaev-volume-conjecture
-- Ref: [kashaev1997] Kashaev, "The hyperbolic volume of knots from the quantum dilogarithm," Lett. Math. Phys. 39 (1997)
@[simp]
noncomputable def pieceVolume (q : ℝ) [inst : VolumeConjecture q]
    (β : Braid) (S : Finset (Fin (β.n - 1))) : ℝ :=
  inst.pieceVol β S

/-- The piece volume is non-negative — a genuine hyperbolic volume,
    discharged by the instance field `pieceVol_nonneg`. -/
-- Ref: [leitner2026] Ch 3 §sec:calibration-algebraic-mass / kashaev-volume-conjecture
theorem pieceVolume_nonneg (q : ℝ) [inst : VolumeConjecture q]
    (β : Braid) (S : Finset (Fin (β.n - 1))) :
    0 ≤ pieceVolume q β S :=
  inst.pieceVol_nonneg β S


/-! ### The anchors have teeth (bean `qou-dx7g`)

On the two braids where the corpus defines both sides, the limit field and the
anchors alone — **without** `kvc_holds` — force the Kashaev limit to be the volume,
because the corpus proves the volume conjecture for `4₁`
(`tendsto_log_kashaev_vol`) and for `𝓑₃` (`tendsto_log_borromeanKashaev_vol`).
So `kvc_holds` is not an extra input there; it is consistent with, and implied
by, the proved theorems.  Everywhere else `kashaevInvariant` and `hypVolume`
remain data supplied by the instance (residual: no general coloured-Jones map
from `Braid`, no general hyperbolic-volume map). -/

theorem kashaevLimit_fourOne (q : ℝ) [inst : VolumeConjecture q] :
    inst.kashaevLimit fourOneBraid = QOU.Knot.FigureEightVolume.VOL_4_1 := by
  have h := inst.kashaevLimit_spec fourOneBraid
  rw [inst.kashaevInvariant_fourOne] at h
  exact tendsto_nhds_unique h QOU.Knot.FigureEightVolume.tendsto_log_kashaev_vol

theorem kashaevLimit_borromean (q : ℝ) [inst : VolumeConjecture q] :
    inst.kashaevLimit borromeanBraid = QOU.Archimedean.Vol_Borromean := by
  have h := inst.kashaevLimit_spec borromeanBraid
  rw [inst.kashaevInvariant_borromean] at h
  exact tendsto_nhds_unique h QOU.Knot.FigureEightVolume.tendsto_log_borromeanKashaev_vol

/-- The volume conjecture on `4₁` follows from the anchors, not from `kvc_holds`. -/
theorem kvc_fourOne_of_anchors (q : ℝ) [inst : VolumeConjecture q] :
    inst.hypVolume fourOneBraid = inst.kashaevLimit fourOneBraid := by
  rw [inst.hypVolume_fourOne, kashaevLimit_fourOne]

/-- The volume conjecture on `𝓑₃` follows from the anchors, not from `kvc_holds`. -/
theorem kvc_borromean_of_anchors (q : ℝ) [inst : VolumeConjecture q] :
    inst.hypVolume borromeanBraid = inst.kashaevLimit borromeanBraid := by
  rw [inst.hypVolume_borromean, kashaevLimit_borromean]

end QOU.Kashaev
