# The Q_β ladder phase `α`, derived from the actual Wedderburn weights

Bean [`qou-q2oa`](../../.beans/qou-q2oa--the-ladder-phase-alpha-has-no-derivation-from-the.md)
(high, parent `qou-cdx1`, tranche `qou-cds1`).

**Status: IN PROGRESS — claim stated, derivation and Lean pending.**

## The object

The ladder phase is
[`QOU.QBeta.phaseTwice`](../../content/quantum-observable-universe/lean/QOU/QBeta/LadderPhaseMirrorCovariance.lean):

    2α = (z − 1)·h,     h = q − q⁻¹

with `z` the Markov stabilisation parameter (`tr(x σ_n) = z·tr(x)`).

## The structural claim under test

Under convention D (`z_D = q³/(q²+1)`, owner ruling 2026-08-15), with the
`H₃(q)` Wedderburn weights of PR #5185

    y₍₃₎ = (q⁴+1)/(q²+1)²,   y₍₂,₁₎ = q²/(q²+1)²,   y₍₁³₎ = 0

the claim to be proved or refuted is the **loop-mean identity**

    2·z_D − h  =  y₍₃₎ · [2]_q,      [2]_q = q + q⁻¹

and hence, via `phaseTwice_projected_eq_loopMean`,

    α_D  =  (h/4)·( y₍₃₎·[2]_q + h − 2 ).

Both sides of the loop-mean identity are bar-EVEN, so this is consistent
with — and strictly sharper than — the standing corpus prune in
`MarkovWeightsConventionD.lean` ("no quantity built from the D-frame weights
alone carries a bar-odd part"): the bar-odd part comes from the `h` factor,
which that file already named as a permitted source, and what is new is that
the weights determine its **multiplier**.

## Anti-fit statement

No step below inverts an experimental Q_β. `c₃` in production is
`(Q_codata/Q_N2 − 1)/u³` — an inversion of the CODATA value, a fit in every
convention — and is not used here. If the derived `α` disagrees with
experiment, that is reported as the result.
