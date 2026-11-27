# Which two-strand channel does matter take? The twist reduces it to a sign

Date: 2026-11-27. Bean `qou-h0zz`. Follows PR #9811
(`HeckeSignChannelIsFermi`, `MarkovTraceKeepsBothChannels`).

## Question

The two-strand braiding has two channels, `q` (symmetric) and `-q⁻¹` (sign). Fermi
exchange is the sign channel (`sign_one_iff_fermi`). Does the ribbon twist choose it?

## What the corpus already proves

`QOU/Core/ExteriorAntisymmetryDerivation.lean`, `quotient_balancing`: for
`π : X ⊗ X ↠ L ≅ Y`, `θ_X = s`, `θ_Y = u`, `β ≫ π = c • π`, balancing gives
`(s²c² − u) • π = 0`.

## Reduction (by hand, not formalised)

1. Balancing sees `c` only through `c²`. Replacing `c` by `-c` leaves every balancing and
   ribbon identity in that file unchanged, so twist data fixes the channel scalar only up
   to sign.
2. The two Hecke channels have twists `u₊ = s²q²` and `u₋ = s²q⁻²`. They coincide iff
   `q⁴ = 1`; at `q = 1` both equal `s²`. So at `q = 1` no twist value separates the
   channels at all.
3. For `q⁴ ≠ 1` the channels have different twists, but saying matter has twist `s²q⁻²`
   is the same input as saying matter is in the sign channel.

So the twist does not derive the channel. It reduces it to one sign: the parity of the
strand.

## Where that sign normally comes from

In the classical (`q = 1`) theory the fermion sign is the super grading. Deligne's
theorem puts it in a fibre functor to super vector spaces, where the braiding on
`odd ⊗ odd` is minus the flip. QOU's fibre functor `τ` lands in ordinary `R`-modules.
Through such a functor the classical braiding is the plain flip, and both channels stay
available.

Deriving the channel would therefore need a `ℤ/2` grading on `τ`, or on the strands, that
the current axioms do not supply. That would be an axiom change and is the owner's call.

## Scope

This is a negative about the ribbon twist only, scope (a). The matter channel stays a
stated input.
