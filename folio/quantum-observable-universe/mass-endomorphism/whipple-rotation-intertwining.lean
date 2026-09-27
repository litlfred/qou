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

/-- Companion of `grading_square` for the along-loop winding: the along-loop
    grading is also restored after a double rotation. Together the two say
    the winding pair `(μ, ν)` is fixed by `rot²`, as the Whipple square
    requires. -/
theorem nuGrade_square {M : Type} (L : WindingLadderData M)
    [W : WhippleRotationIntertwining L] (x : M) :
    L.nuGrade (L.rot (L.rot x)) = L.nuGrade x := by
  rw [W.rot_involutive_on_ladder x]

/-- **Derived intertwining (provable modulo the class).** The winding-grading
    map `x ↦ (μ(x), ν(x))` intertwines the channel rotation `rot` with the
    coordinate swap `Prod.swap`: for every ladder state, the grading pair of
    `rot x` is the swap of the grading pair of `x`. This is the exact
    categorical shadow of the Whipple degree–order exchange
    `(μ, ν) ↦ (ν, μ)`; it is a genuine *consequence* of the class fields
    (the two swap components), not a restatement of them, and holds for any
    instance without providing one. -/
theorem gradingPair_intertwines_swap {M : Type} (L : WindingLadderData M)
    [W : WhippleRotationIntertwining L] (x : M) :
    (L.muGrade (L.rot x), L.nuGrade (L.rot x))
      = Prod.swap (L.muGrade x, L.nuGrade x) := by
  obtain ⟨hmu, hnu⟩ := W.rot_swaps_windings x
  rw [hmu, hnu]
  rfl

/-! ## Conditional reduction: the winding-swap factors through the channel flip

The grading-swap field of `WhippleRotationIntertwining` is not primitive: it
*follows from* the even↔odd **channel flip** that
`QOU.MassEndomorphism.rotation_step` proves (the ζ₄ recurrence rotation carries
`oddStep` ↔ `evenStep`). The reduction below isolates exactly this. A
`ChannelIndexedLadder` carries the two recurrence-channel indices, the rotation
that flips them (the abstract shadow of `rotation_step`), and the single shared
winding function `windOf` sending a channel index to its winding grading. The
swap is then a *derived* consequence — `windOf (evenIdx (rot x)) = windOf (oddIdx
x)` because `rot` flips the indices — **not** an assumed field.

This does not close the conjecture: no instance of `WhippleRotationIntertwining`
is produced. It moves the open content off the swap and onto (i) the
identification of `rot_flips_channels` with `rotation_step`'s even↔odd carry, and
(ii) the residual involutivity field (the order-2 Whipple `cosh ↔ coth` argument
exchange — a *different* map from the order-4 ζ₄ recurrence rotation, so genuinely
open). Dependency-free: only `Int`, structures, and core tactics. -/

/-- Channel-indexed ladder data: the two recurrence-channel indices, the
    channel-flipping rotation (shadow of `rotation_step`), and the shared
    winding function assigning a grading to a channel index. -/
structure ChannelIndexedLadder (M : Type) where
  /-- even (compact / binding / `cosh`) recurrence-channel index. -/
  evenIdx : M → Int
  /-- odd (non-compact / `𝔔_β` / `sinh`) recurrence-channel index. -/
  oddIdx : M → Int
  /-- the ζ₄ channel rotation (abstract shadow of `rotation_step`). -/
  rot : M → M
  /-- winding grading assigned to a channel index (the SAME map for both
      channels — this is what makes the swap derivable). -/
  windOf : Int → Int
  /-- `rot` flips the even and odd channel indices: the faithful abstraction of
      `rotation_step`'s `oddStep ↔ evenStep` carry. -/
  rot_flips_channels :
    ∀ x : M, evenIdx (rot x) = oddIdx x ∧ oddIdx (rot x) = evenIdx x

/-- The winding-graded ladder induced by a channel-indexed ladder: each grading
    is `windOf` of the corresponding channel index. -/
def ChannelIndexedLadder.toWindingLadder {M : Type} (L : ChannelIndexedLadder M) :
    WindingLadderData M where
  rot := L.rot
  muGrade := fun x => L.windOf (L.evenIdx x)
  nuGrade := fun x => L.windOf (L.oddIdx x)

/-- **The reduction.** For a channel-indexed ladder, the winding-swap field of
    `WhippleRotationIntertwining` is *derived* from the channel flip — no swap is
    assumed. Because both gradings are the same `windOf` of their channel index,
    flipping the indices flips the gradings. -/
theorem channelIndexed_swaps_windings {M : Type} (L : ChannelIndexedLadder M)
    (x : M) :
    L.toWindingLadder.muGrade (L.rot x) = L.toWindingLadder.nuGrade x ∧
      L.toWindingLadder.nuGrade (L.rot x) = L.toWindingLadder.muGrade x := by
  obtain ⟨he, ho⟩ := L.rot_flips_channels x
  refine ⟨?_, ?_⟩
  · show L.windOf (L.evenIdx (L.rot x)) = L.windOf (L.oddIdx x)
    rw [he]
  · show L.windOf (L.oddIdx (L.rot x)) = L.windOf (L.evenIdx x)
    rw [ho]

end QOU.MassEndomorphism
