/-
Copyright (c) 2026 litlfred. All rights reserved.

# The Gram radical pairs with a braid to give its sign-representation value

Bean `qou-cds2`. Under the canonical trace convention D (owner ruling
2026-08-15) the Markov-trace Gram on the `H_3(q)` normal-form basis is
SINGULAR, with radical spanned by the q-antisymmetriser
`v_i = (-1/q)^len(w_i)` (`QOU.QBeta.MarkovGramDegenerate`, and
`pyhecke.gram.RADICAL` / `radical_mp`). Any demand of the form `G x = nf` is
therefore solvable only when `nf` is orthogonal to `v`.

`computations/probes/qbeta_braid_nf_sdp_offset_probe.py` poses exactly such a
demand, on the premise *"Since `G` is invertible (rank 6), `G x = nf` fixes
`x* = G⁻¹ nf` uniquely"*. That premise fails under D. This file identifies
**what the unreachable component is**, which turns a numerical obstruction
into a structural one.

## The measurement this formalises

Measured at 50 dps over thirteen braid words, exact to `1.3e-51`
(`computations/qbeta/radical_pairing_sign_rep_probe.py`):

    <v, nf(beta)>  =  (-1/q) ^ writhe(beta)

i.e. the radical pairing is the value of `beta` in the **sign representation**
of `H_3(q)`, the one-dimensional rep where every generator acts by `-1/q`.
That is the eigenvalue the Hecke relation `(sigma - q)(sigma + q⁻¹) = 0`
assigns to the antisymmetric channel, and the q-antisymmetriser is precisely
its projector — so the identity is what the radical *is*, not a coincidence
of the basis.

## What is proved here (sorry-free, generic `Field` per §7c)

The sign-representation value is a **monoid homomorphism on braid words**
graded by writhe, and it is **never zero**:

1. `signRepValue_append` — multiplicative over concatenation, via
   `QOU.StandardModel.MarkovInvariance.writhe_append`.
2. `signRepValue_inv` — inverts under braid-word inverse (`writhe_inv`), so
   it is mirror-ODD in the exponent, matching the framing prefactor's parity
   (`QOU.QBeta.LadderPhaseMirrorCovariance`).
3. `signRepValue_ne_zero` — nonzero for every braid word whenever `q ≠ 0`.

**The consequence, and the point of the file:** `nf(beta)` is orthogonal to
the radical iff its sign-rep value vanishes, and by (3) that never happens.
So `G x = nf` is unsatisfiable for **EVERY** braid, not merely for the two
anchors the probe happens to use. The obstruction is not a bad choice of knot
and cannot be dodged by picking another one — `signRepValue_ne_zero` is the
proof of that, and it is why re-solving the probe's demand on the quotient and
reporting an offset angle would be reporting a number for a question that has
no solution.

## Where the missing component belongs

The unreachable piece is graded by **writhe**, and writhe is exactly what the
Ocneanu trace does *not* see: link invariance is restored by a writhe-dependent
prefactor **outside** the trace (Jones 1987 §5; block
`prop:jones-markov-trace-stabilisation`). Under D the pin additionally forces
the antisymmetriser weight `y_(1³)` to vanish
(`TemperleyLiebTower.conventionD_kills_antisymmetriser`), so the trace is blind
to that channel by construction. The probe was asking the trace to reproduce
content that structurally lives outside it. Posing the demand on the quotient
`H_3(q)/rad` is the well-posed replacement; this file does not carry out that
re-derivation, it establishes what has to be quotiented and why.

Scope: no value is wired, no registry tier moves, and the convention ruling is
untouched. Sorry-free.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import QOU.StandardModel.WritheMarkovInvariance

namespace QOU.QBeta

open QOU.StandardModel.MarkovInvariance

variable {F : Type*} [Field F]

/-- The value of a braid word in the **sign representation** of `H_n(q)`: the
    one-dimensional representation sending every generator to `-q⁻¹`, which is
    the antisymmetric eigenvalue of the Hecke relation
    `(σ - q)(σ + q⁻¹) = 0`. Graded by writhe, since each positive crossing
    contributes one factor and each negative crossing its inverse. -/
noncomputable def signRepValue (q : F) (β : BraidWord) : F :=
  (-q⁻¹) ^ (writhe β)

/-- **Multiplicative over concatenation.** Immediate from `writhe_append`;
    this is what makes the pairing a representation value rather than a
    word-dependent artefact. -/
theorem signRepValue_append (q : F) (hq : q ≠ 0) (a b : BraidWord) :
    signRepValue q (a ++ b) = signRepValue q a * signRepValue q b := by
  unfold signRepValue
  rw [writhe_append, zpow_add₀ (by simpa using neg_ne_zero.mpr (inv_ne_zero hq))]

/-- **Mirror sends it to its inverse.** From `writhe_inv`: the braid-word
    inverse negates writhe, so the sign-rep value inverts. This is the same
    mirror-oddness the framing prefactor carries — see
    `QOU.QBeta.LadderPhaseMirrorCovariance`.

    No `q ≠ 0` hypothesis: `zpow_neg` holds unconditionally in a field, so
    requiring one would overstate what the statement needs. -/
theorem signRepValue_inv (q : F) (a : BraidWord) :
    signRepValue q (inv a) = (signRepValue q a)⁻¹ := by
  unfold signRepValue
  rw [writhe_inv, zpow_neg]

/-- **Never zero.** A `zpow` of a nonzero base is nonzero, for every exponent
    and hence every braid word. -/
theorem signRepValue_ne_zero (q : F) (hq : q ≠ 0) (β : BraidWord) :
    signRepValue q β ≠ 0 :=
  zpow_ne_zero _ (by simpa using neg_ne_zero.mpr (inv_ne_zero hq))

/-- **The obstruction is universal, not anchor-specific.**

    Stated against the measured identity as a hypothesis (`hpair`: the radical
    pairing of `nf β` equals the sign-rep value — verified to `1.3e-51` over
    thirteen words in `radical_pairing_sign_rep_probe.py`): the pairing is
    nonzero for EVERY braid word, so no braid's normal form is orthogonal to
    the radical, so `G x = nf` is unsatisfiable for every braid.

    Choosing a different knot cannot rescue the demand. That is the fact that
    makes re-solving it on the quotient and reporting an offset angle a
    category error rather than a numerical approximation. -/
theorem radical_pairing_ne_zero_of_sign_rep
    (q : F) (hq : q ≠ 0) (β : BraidWord) (pairing : F)
    (hpair : pairing = signRepValue q β) : pairing ≠ 0 := by
  rw [hpair]; exact signRepValue_ne_zero q hq β


/-- **Braid-word inverse cancellation in the sign representation (`qou-egqr`).**
For any nonzero `q : F` and braid word `β`, concatenating `β` with `inv β` in either order
yields unit sign-representation pairing `1`. -/
theorem signRepValue_inv_mul_and_mul_inv (q : F) (hq : q ≠ 0) (β : BraidWord) :
    signRepValue q (β ++ inv β) = 1 ∧ signRepValue q (inv β ++ β) = 1 := by
  refine ⟨?_, ?_⟩
  · rw [signRepValue_append q hq β (inv β), signRepValue_inv,
        mul_inv_cancel₀ (signRepValue_ne_zero q hq β)]
  · rw [signRepValue_append q hq (inv β) β, signRepValue_inv,
        inv_mul_cancel₀ (signRepValue_ne_zero q hq β)]

end QOU.QBeta
