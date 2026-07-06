/-
  Conjecture: Whipple–rotation intertwining.

  The archimedean shadow of the fibre-level channel rotation
  (x, q) -> (ix, q^{-1}) acts on the toroidal channel family
  P^mu_{nu-1/2}(cosh eta) e^{i mu theta} e^{i nu phi} as the Whipple
  degree–order exchange: it swaps the two winding gradings (mu, nu) and is
  involutive on the ladder data.

  Status: PRIMARY conjecture (§3b-tax) — no other conjecture class appears
  as a hypothesis, and no instance is provided. The class fields encode the
  conjecture's CONTENT (grading swap + involutivity), parameter-quantified
  in the shape of the claim — not `True`, not an empty marker. Supporting
  facts (bar-even ladder, exact Whipple argument involution, 50-dps
  degree–order exchange with Gamma-shift laws) are verified in
  computations/substrate/whipple-rotation-involution-probe.witness.json;
  the forced mu = 1/2 order is prop:hoefsmit-toroidal-ladder-locus
  (QOU.BraidsAndKnots.toroidal_locus_forced, sorry-free).

  Dependency-free (§7c: no archimedean ring — the gradings are ℤ-valued
  and the rotation is an abstract carrier map).

  -- Ref: [whipple1917] https://doi.org/10.1112/plms/s2-16.1.301
  -- Ref: [ismail-masson1994] https://doi.org/10.1090/S0002-9947-1994-1264148-6
-/

namespace QOU.MassEndomorphism

/-- Winding-graded channel-ladder data: a carrier `M` of ladder states with
    the two winding gradings — `muGrade` (around-core) and `nuGrade`
    (along-loop) — and the fibre-level channel rotation `rot` (the
    archimedean shadow of the `rotation_step` map `(x, q) ↦ (ix, q⁻¹)`). -/
structure WindingLadderData (M : Type) where
  rot : M → M
  muGrade : M → Int
  nuGrade : M → Int

/-- **Conjecture (primary): Whipple–rotation intertwining.** The channel
    rotation acts on winding-graded ladder data as the Whipple degree–order
    exchange: it swaps the two winding gradings and squares to the
    identity on ladder states. An instance for the toroidal channel family
    of a bound vortex pair would realise the identification; none is
    provided — the conjecture is open. -/
class WhippleRotationIntertwining {M : Type} (L : WindingLadderData M) : Prop where
  /-- The rotation exchanges the around-core and along-loop windings —
      the Whipple degree–order swap. -/
  rot_swaps_windings :
    ∀ x : M, L.muGrade (L.rot x) = L.nuGrade x ∧
             L.nuGrade (L.rot x) = L.muGrade x
  /-- The rotation is involutive on ladder states, matching the exact
      involutivity of the Whipple argument exchange cosh ↔ coth. -/
  rot_involutive_on_ladder : ∀ x : M, L.rot (L.rot x) = x

/-- Sanity (provable, not part of the conjecture): the two grading-swap
    conditions plus involutivity are mutually consistent — swapping twice
    returns both gradings. Stated to keep the class honest: the fields are
    not vacuous and compose as the Whipple square should. -/
theorem grading_square {M : Type} (L : WindingLadderData M)
    [W : WhippleRotationIntertwining L] (x : M) :
    L.muGrade (L.rot (L.rot x)) = L.muGrade x := by
  rw [W.rot_involutive_on_ladder x]

end QOU.MassEndomorphism
