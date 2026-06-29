import QOU.Basic


/-!
# QOU.BraidKnot.ShadowPriceContinuity — continuity of shadow prices

Each shadow price u_λ(q) = w_λ(q)/d_λ(q) − 1/[k]_q! is a rational
function of q over the base ring, continuous on the generic locus
{q : [k]_q! · d_λ(q) ≠ 0}.

LaTeX: `\label{prop:shadow-price-continuity}`
-/

namespace QOU.BraidKnot

open Topology

/-- **Continuity of shadow prices on the generic locus.**

    Model the shadow price as `u_λ(q) = w_λ(q)/d_λ(q) − cℓ(q)` where
    `w_λ` is the partition weight, `d_λ` the q-dimension, and
    `cℓ(q) = 1/[k]_q!` the common normaliser — all continuous in `q`.
    On the generic locus where `d_λ(q₀) ≠ 0`, the rational function
    `u_λ` is continuous at `q₀`: the quotient is continuous where its
    denominator is nonzero, and subtracting the continuous `cℓ`
    preserves continuity. -/
theorem ShadowPriceContinuity
    (w d cℓ : ℝ → ℝ) (q₀ : ℝ)
    (hw : ContinuousAt w q₀) (hd : ContinuousAt d q₀)
    (hc : ContinuousAt cℓ q₀) (hne : d q₀ ≠ 0) :
    ContinuousAt (fun q => w q / d q - cℓ q) q₀ :=
  (hw.div hd hne).sub hc

end QOU.BraidKnot
