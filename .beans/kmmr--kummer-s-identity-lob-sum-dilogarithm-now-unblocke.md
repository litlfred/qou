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

---
**2026-08-09 — first increment landed: Kummer on `|z| = 1`.**

`QOU/Knot/KummerUnitCircle.lean`, sorry-free, standard axioms, `lake build`
exit 0 / 3091 jobs. Probe `qbeta_5two_route72_kummer_unit_circle_probe.py`
(60 dps, 4 gates, all passing); float64 guard clean, run in place.

`blochWigner_lob_exp` — for `θ ∈ (0, π)`,
`BlochWigner_lob(e^{iθ}) = Cl₂(θ)`.

**Why the unit circle is the cheap case, and it is a real reason not an
accident.** There the ideal tetrahedron is **isosceles**: the three angles of
`e^{iθ}` are `(θ, (π−θ)/2, (π−θ)/2)`. So the Λ-sum is `Λ(θ) + 2Λ((π−θ)/2)`,
which is `Cl₂(θ)` by the **duplication formula the corpus already had**
(`Cl_2_duplication`). On `|z| = 1`, Kummer *is* Clausen duplication — three
lines once the angles are computed.

The work was the angle computation, not the identity: `one_sub_exp_mul_I`
factors `1 − e^{iθ} = 2 sin(θ/2)·e^{i(θ−π)/2}`, which pins
`arg(1−e^{iθ}) = (θ−π)/2` with no branch ambiguity, and the other two angles
follow by `Complex.arg_inv` / `Complex.arg_conj` (both need `arg ≠ π`, supplied).

**Two boundaries, both gated so they cannot be blurred:**

* **G3** — the *dilogarithm half* (`Im Li₂(e^{iθ}) = Cl₂(θ)`, hence Λ-sum = the
  Bloch–Wigner dilogarithm form) is numerically true to `1e-45` but is **NOT
  proved** for `cLiTwoExt`. The Lean theorem deliberately states its conclusion
  in terms of `Cl₂` alone and makes **no** dilogarithm claim. Until that half
  lands, `BlochWignerLobachevsky`'s prohibition on transporting dilogarithm
  facts onto the symbol still stands — this increment does not lift it.
* **G4** — this does **not** reach `Vol(5₂)`. `|y₁| = 1.5236`, off the unit
  circle; its tetrahedron is not isosceles and `log|z| ≠ 0`.

**Still open, in order:** (a) `Im Li₂(e^{iθ}) = Cl₂(θ)` for `cLiTwoExt` — the
cheaper of the two, and `QOU/Knot/Clausen.lean` already notes `Cl₂′` is
*simultaneously* the derivative of `V(θ) = Im Li₂(e^{iθ})`, which is the entry
point; (b) general `z`, which needs the two-variable argument
`dD = log|z| d arg(1−z) − log|1−z| d arg z` against `dΛ(θ) = −log|2 sin θ| dθ`.
Only (b) reaches the 5₂ shape.
