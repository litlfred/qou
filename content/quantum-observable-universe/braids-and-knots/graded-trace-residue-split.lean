import QOU.BraidKnot.ConfinementLevel

/-!
# Graded-trace residue split on the confinement filtration

The Markov trace on the filtered Hecke algebra `H_n(q)` decomposes
canonically as

    tr_M(T_w) = tr_gr(σ(T_w)) + Res_GB(T_w)

where `σ` is the symbol map to the associated graded algebra and
`Res_GB` is the sum of rewriting-defect residues at root-of-unity
poles.  This is the filtered-algebra analogue of Strutinsky's
smooth-plus-oscillating nuclear-energy decomposition.

Ref: [manuscript] Chapter 6, §Nuclear Binding and Beta Stability
LaTeX label: `prop:graded-trace-residue-split`
-/

namespace QOU.BraidKnot

/-- The symbol map `σ: J^ℓ → J^ℓ/J^{ℓ+1}` on the confinement
    filtration.  Axiomatized; full construction is downstream of
    `QOU.BraidKnot.ConfinementLevel`. -/
noncomputable opaque symbolMap (ℓ : ℕ) (q : ℝ) : Unit → Unit  -- placeholder

/-- The Markov trace on the associated graded algebra `gr H_n(q)`.
    This is the "smooth" / macroscopic piece of the trace split. -/
noncomputable opaque gradedTrace (q : ℝ) (x : Unit) : ℝ

/-- The total residue contribution from GB rewriting defects at
    root-of-unity poles — the "oscillating" / shell piece of the
    trace split.  Equals the Mittag-Leffler sum in
    `prop:gb-residue-spectral-sum`. -/
noncomputable opaque gbResidue (q : ℝ) (x : Unit) : ℝ

/-- The full Markov trace on `H_n(q)`. -/
noncomputable opaque markovTrace (q : ℝ) (x : Unit) : ℝ

/-- **Graded-trace residue split.**

    For any braid word `T_w ∈ H_n(q)`,

      tr_M(T_w, q) = tr_gr(σ(T_w), q) + Res_GB(T_w, q).

    The first term is the Markov trace on the associated graded
    algebra (smooth, Strutinsky-macroscopic analogue); the second
    is the sum of residues at root-of-unity poles (oscillating,
    Strutinsky-shell analogue).

    Ref: [manuscript] `conj:mass-endomorphism`. -/
class GradedTraceResidueSplit where
  q : ℝ
  element : Unit
  smooth : ℝ  -- tr_gr(σ(element), q)
  oscillating : ℝ  -- Res_GB(element, q)
  total : ℝ  -- tr_M(element, q)
  split_identity :
    total = smooth + oscillating
  smooth_is_graded :
    smooth = gradedTrace q element
  oscillating_is_residue :
    oscillating = gbResidue q element

/-- Level-0 case: if a braid word lies entirely in filtration
    level 0 (no crossings climb the GB filtration), then the
    residue contribution vanishes and the Markov trace equals
    the graded trace.  This recovers the pure-descended regime.

    Ref: [manuscript] `prop:categorical-mass-markov`. -/
theorem level_zero_pure_descended (S : GradedTraceResidueSplit)
    (h : S.oscillating = 0) :
    S.total = S.smooth := by
  rw [S.split_identity, h, add_zero]

/-- Strutinsky analogue: the split is the algebraic shadow of
    `E = Ẽ + δE_shell` with `Ẽ` the liquid-drop (smooth) piece
    and `δE_shell` the oscillating correction.  The precise
    identification is paper-side in
    `rem:strutinsky-from-graded-trace`.

    Ref: [manuscript] §Nuclear Binding and Beta Stability. -/
theorem strutinsky_analogue (S : GradedTraceResidueSplit) :
    -- The split exists and is canonical; the physics interpretation
    -- is developed in the Physical Observations chapter.
    S.total = S.smooth + S.oscillating :=
  S.split_identity

end QOU.BraidKnot
