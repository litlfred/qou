---
# qou-dw5q
title: Measure closeability of the 4 analysis axioms (Lobachevsky-Catalan, Weierstrass, 2x parallelogram contour)
status: completed
type: task
priority: normal
created_at: 2026-08-25T21:26:14Z
updated_at: 2026-08-25T22:19:50Z
---

## RESULT 2026-08-25 — one theorem PROVED; the axiom itself stays External

**Closeability measured, not guessed.** The Lobachevsky-Catalan axiom
`lobachevsky (π/4) = catalan_G / 2` is NOT closeable here, and the 2026-06-03
tractability triage that classifies it **External** is correct. I did not
contradict it.

**But its recorded reason is half stale.** The docstring says a proof "would
require ... Clausen function `Cl_2`, dilogarithm `Li_2` — none of which is
currently upstream". `Cl_2` is no longer missing: `ClausenFunctionMathlibFiller`
defines it in-repo. The real residual obstruction is exactly ONE thing — the
Clausen **integral representation** `Cl_2' θ = -log|2 sin(θ/2)|`, converting the
log-sine integral into the series. That is genuine analysis over an improper
integrand. Narrower and better-named than "the machinery is absent".

## What was actually proved (sorry-free, by proof term)

`QOU.Archimedean.CatalanClausenBridge.catalan_G_eq_Cl_2_pi_div_two`:

    catalan_G = Cl_2 (π/2)

The repo defined Catalan's constant **twice**, in files that do not import each
other, with **no** cross-reference anywhere in the tree (corpus-grepped). The
filler's `catalan_constant_eq_cl_2_pi_over_2` is `rfl` over a DEFINITION and
carries no content. Two unbridged definitions of one constant is a live hazard.

Proof is elementary: at `θ = π/2` the Clausen series IS the alternating series
with its zero terms dropped — `sin((2k+2)π/2) = 0`, `sin((2k+1)π/2) = (-1)^k` —
then `tsum_even_add_odd`. `Real.cos_nat_mul_pi` is absent at this toolchain, so
`cos_nat_mul_pi'` proves it by induction.

All three declarations: `[propext, Classical.choice, Quot.sound]`, zero sorryAx.
Pinned in the axiom guard; full gate rc=0 on 37 entries.

**Axiom count unchanged at 24** — this proves a theorem that was missing, it does
not discharge an axiom. Saying otherwise would be the over-claim this repo warns
about.


## FOLLOW-UP — gap isolated; still External, now for three NAMED reasons

Pushed further toward the axiom. It is still **not closeable**, and the External
classification stands — but the gap is now one identity with three named missing
prerequisites, all measured against the pinned olean tree (401,418 constants
visible, positive controls pass).

**New theorem** `QOU.Archimedean.lobachevsky_catalan_iff_clausen`:

    Λ(π/4) = catalan_G / 2   <->   Λ(π/4) = Cl_2 (π/2) / 2

One rewrite off the bridge. Catalan is now **eliminated** from the statement of
the gap: what remains is exactly the θ = π/4 instance of the Clausen integral
representation `Λ(θ) = Cl_2 (2θ)/2`.

**The three missing Mathlib pieces (measured, not assumed):**
1. `∫₀^{π/2} log(sin x) dx = -(π/2) log 2` — no `integral`+`log` lemma of this
   kind exists at this toolchain at all.
2. Abel's limit theorem / boundary log series. Mathlib has
   `Real.hasSum_pow_div_log_of_abs_lt_one` (strictly inside the disc) and nothing
   carrying it to |z| = 1, z ≠ 1 — exactly where
   `∑ cos(kθ)/k = -log|2 sin(θ/2)|` lives.
3. Term-by-term integration of a conditionally-convergent Fourier series against
   an integrand improper at t = 0.

**Both classical routes hit the same wall.** The Fourier route needs (2)+(3). The
`∫₀^{π/4} log(cot t) dt = G` route (u = tan t, geometric expansion — which
sidesteps the boundary) still needs (1) to convert ∫log sin / ∫log cos into Λ.

Verified `[propext, Classical.choice, Quot.sound]`. Pinned. Full gate rc=0 on 38.
**Axiom count unchanged at 24** — this reduces what must be shown; it does not
show it.
