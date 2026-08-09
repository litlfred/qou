---
# kmmr
title: "Kummer's identity (Λ-sum = dilogarithm form) — now UNBLOCKED by cLiTwoExt"
status: todo
type: task
priority: high
tags:
    - lean
    - dilogarithm
    - hyperbolic-volume
    - stale-claim-corrected
created_at: 2026-08-09T20:30:00Z
updated_at: 2026-08-09T20:30:00Z
---

## The claim that was stale

`QOU/Archimedean/BlochWignerLobachevsky.lean` defines

    BlochWigner_lob z := Λ(arg z) + Λ(arg(1/(1−z))) + Λ(arg(1 − 1/z))

and said of the dilogarithm form `D(z) = Im Li₂(z) + log|z|·arg(1−z)` that the
two agreeing is **Kummer's identity**, "a theorem, not a definitional
unfolding" — and that it "**cannot currently be proved in this corpus**: Mathlib
has no polylogarithm or dilogarithm at all (checked 2026-08-08)".

The Mathlib half remains true. The conclusion does not: **the corpus has its own
dilogarithm**, `QOU.MathlibExt.cLiTwoExt`, with reflection, inversion and the
five-term identity all proved this session. Corrected in place 2026-08-09.

## Why it matters

That file spells out the factorisation: the target `Vol = Λ-sum` splits as
(geometric) `Vol = D` ∘ (analytic) `D = Λ-sum`. **Kummer is the analytic
factor**, and it is the bridge between the two halves of this whole lane:

* the Λ-sum side — angles, `Cl₂`, Rivin concavity, `qou-rvnc`/`qou-mlgp`;
* the dilogarithm side — `cLiTwoExt`, the pentagon, the proved 5₂ sum rule.

Proving it would let dilogarithm facts be transported onto `BlochWigner_lob`,
which the file currently and correctly **forbids** ("do not transport
dilogarithm facts onto this symbol … the name is shared; the objects are so far
only numerically observed to agree").

## Numerical status — exact, checked 2026-08-09 at 40 dps

Against this file's own `Lob`/`tetAngle` definitions, `Λ-sum` vs
`Im Li₂(z) + log|z|·arg(1−z)`, residual `≤ 1.1e-41` (the precision floor) at
`0.3+0.7i`, `1.5+0.8i`, `−0.4+1.2i`, `0.2+2.5i`, and at the **5₂ shape**
`y₁ = 0.78492+1.30714i`. The three `tetAngle`s sum to `π` to `4.6e-41` at each.

And at `y₁`: `3·BlochWigner_lob(y₁) = 2.828122088330783162763899…`, which is
`Vol(5₂)` to every digit the corpus records. So the Λ-sum route *does* reach the
volume — the gap is a proof, not a fact.

## Suggested attack

Both sides are real-valued on the upper half-plane, so the holomorphic
"derivative vanishes on a preconnected open set" trick used all through
`FiveTwoComplexPentagon` does **not** apply directly. Options:

1. Differentiate along the two real directions and match, then pin the constant
   on a ray where both sides are computable (`Lob_zero`/`Lob_pi` and
   `cLiTwoExt` on `(0,1)` give candidate basepoints).
2. Go through `Cl₂`'s Fourier series and `Im Li₂(e^{iθ}) = Cl₂(θ)` — the corpus
   already has `hasDerivAt_Cl_2_series` and `clausen_eq_series`, and
   `QOU/Knot/Clausen.lean` notes `Cl₂′` is *simultaneously* the derivative of
   the dilog-saddle potential `V(θ) = Im Li₂(e^{iθ})`. That coincidence is
   probably the cheapest entry point.

⚠ Do not assume the identity extends off the upper half-plane; `BlochWigner_lob`
is built from `arg`s and the corpus already proves it vanishes on real shapes in
`(0,1)`, which is a branch statement.

## Not this bean

The **geometric** factor `Vol = D` — that a specific triangulation's Λ-sum is
the hyperbolic volume of a specific knot complement. That is `qou-m015` +
`qou-krvm` territory and is not closed by Kummer.
