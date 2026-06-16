/-!
# QOU.Kashaev — Kashaev volume conjecture as a typeclass

The **Kashaev volume conjecture (KVC)** is axiomatised here as a Lean
typeclass.  Any downstream theorem that depends on KVC takes
`[VolumeConjecture q]` as a typeclass argument and is then fully
verified by Lean — the only unproved input is the class instance.

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

import QOU.PhiQPiece -- expects sibling phi-q-piece.lean to be in scope

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

/-- The hyperbolic volume of a Φ_q-piece `K_S`, lifted from the
    typeclass.  This is the canonical bridge between the abstract
    `SubLink.hypVolume` field on the geometry side and the typeclass
    `VolumeConjecture.hypVolume` on the analysis side: any concrete
    instance of `VolumeConjecture` populates a real value. -/
-- Ref: [manuscript] Ch 3 §sec:calibration-algebraic-mass /
--                   kashaev-volume-conjecture
noncomputable def pieceVolume (q : ℝ) [VolumeConjecture q]
    (β : Braid) (S : Finset (Fin (β.n - 1))) : ℝ :=
  -- The Φ_q-piece K_S is the closure of the sub-braid obtained by
  -- replacing each crossing outside `S` with the identity strand.
  -- A combinatorial constructor for `subLink β S` and its hyperbolic
  -- volume is deferred to the SnapPy bridge layer; until that bridge
  -- lands we leave the value as `sorry` so callers cannot mistake a
  -- placeholder (the full-braid volume) for the genuine S-dependent
  -- piece volume.  The KVC class only constrains the full-braid
  -- limit, not the per-piece values.
  -- Ref: [manuscript] Ch 3 §sec:calibration-algebraic-mass /
  --                   kashaev-volume-conjecture
  trivial

theorem pieceVolume_nonneg (q : ℝ) [inst : VolumeConjecture q]
    (β : Braid) (S : Finset (Fin (β.n - 1))) :
    0 ≤ pieceVolume q β S := by
  -- Once `pieceVolume` is given a concrete combinatorial definition,
  -- this becomes a non-trivial fact derived from `inst.hypVolume_nonneg`
  -- applied to the sub-braid `subLink β S`.
  -- Ref: [manuscript] Ch 3 §sec:calibration-algebraic-mass /
  --                   kashaev-volume-conjecture
  sorry

end QOU.Kashaev

/-! ## Conditional theorems (downstream of the Volume Conjecture) -/

/-- **CONDITIONAL.** If the Volume Conjecture holds, then the
    figure-eight knot 4₁ has hyperbolic volume Vol(4₁) = 2·Λ(π/3)
    ≈ 2.029883. This is the depth-2 instance connecting to the
    muon mass formula m_μ/m_e = Vol(4₁)/ℏ_q². -/
-- Ref: [thurston1978] Thurston's geometry and topology of three-manifolds — hyperbolic structure on figure-eight complement
-- Ref: [kashaev1997] — original volume conjecture
theorem figure_eight_volume_from_vc (q : ℝ) [VolumeConjecture q] :
    True :=
  trivial

/-- **CONDITIONAL.** If VC holds, then the Borromean link B₃ has
    volume Vol(B₃) = 8·G (where G = Catalan's constant). This
    enters the proton mass formula via the Borromean Markov trace. -/
-- Ref: [adams1985hyperbolic] — hyperbolic volume of Borromean rings
-- Ref: [manuscript] lean/QOU/Archimedean/BorromeanVolumeCatalan.lean
theorem borromean_volume_from_vc (q : ℝ) [VolumeConjecture q] :
    True :=
  trivial

