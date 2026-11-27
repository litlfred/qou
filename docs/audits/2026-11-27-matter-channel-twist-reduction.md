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

## Follow-up: does the photon's chiral vertex fix the sign? (2026-11-27)

The photon is `γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹ ∈ H₃(q)`. By hand:

1. On a one-dimensional channel every `σᵢ` acts by the same scalar `λ ∈ {q, -q⁻¹}`. So
   `σ₀σ₁⁻¹` acts by `λλ⁻¹ = 1` on both the fully symmetric and the fully antisymmetric
   channel. The chiral vertex cannot tell them apart. It acts non-trivially only on the
   mixed `(2,1)` channel.
2. The terms that do separate the channels are `φ₀σ₀ + φ₁σ₁`, through `q` versus `-q⁻¹`.
   They are not chiral, and their coefficients are free. On the Borromean factor
   `γ(0,0,qh)`, where `φ₀ = φ₁ = 0`, `γ` acts by the same scalar `1 + φ₀₁` on both channels.
3. The vertex's handedness is a mirror datum: `σᵢ ↦ σᵢ⁻¹` sends `σ₀σ₁⁻¹` to `σ₀⁻¹σ₁`. The
   even/odd choice is a charge-conjugation datum: `S ↦ Sᶜ` negates the charge. Fixing one
   does not fix the other. The Standard Model's choice, "the even part is left-handed",
   links the two. A link between mirror and complement would be needed, and neither the
   photon nor the strand grading supplies one.

So the photon's chiral vertex does not fix the sign. This is a scope-(a) negative about
the photon only. What remains is a P–C link: a statement that the mirror of the braid
acts on strand states as complementation.

## Follow-up: is the mirror a Hodge star? No (2026-11-27)

`HeckeSignChannelIsFermi.sign_mirror_iff_rev` (Lean, sorry-free): a pair state is in the
`-q⁻¹` channel iff its index-reversed state is in the sign channel at `q⁻¹`. The mirror
`q ↦ q⁻¹` is therefore the longest permutation `w₀` acting on labels. It keeps the strand
count. It cannot send degree `k` to degree `5 − k`, so it cannot exchange the even and odd
parts.

Complementation, the Hodge star, is the duality `Λ^k ≅ (Λ^{5−k})* ⊗ Λ^5`, i.e. charge
conjugation. So P (the mirror) and C (the complement) are independent on strand states. The
chirality sign is the choice of which relative orientation of P and C matter takes. The
braid–Hecke structure examined here does not supply it. Scope (a).
