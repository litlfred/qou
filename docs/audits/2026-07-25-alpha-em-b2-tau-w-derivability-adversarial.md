# B2 τ = W — adversarial assessment: is the identification derivable or definitional?

**Date:** 2026-07-25 · **Axis:** α_EM per-loop measure (`1/(8π)`) · **Tier:** red-team
critical-distance assessment (standing license) · **Discipline:** `1/(8π)` stays a
phase-4 identification; no `TauRhoHodgeLift`/`W` instance is registered; this is an
*interpretation constraint*, not a new claim.

## What was closed, and what this attacks

PRs #4160/#4199/#4209 established, rigorously, the **representation-theory** side of
the B2 τ-identification:

- `H^{1,0}(Bring) = std = (4,1)` is the irreducible S₅-rep; by Schur the invariant
  symmetric form on it is **unique up to scalar** — so the Hodge Gram (`∝ M_S`) and
  the (τ-image of the) Markov Gram are **proportional**. **Form: forced.**
- An explicit map `W = T·U⁻¹` (seminormal deformation `T` + S₅ period alignment `U`)
  transports the Hecke Markov Gram at `q₀` onto `M_S`: `Wᵀ·G_Markov(q₀)·W = c·M_S`
  (exact, residual `3e-39`). **The identification is structurally realisable.**

The **open** claim is `τ = W`: that the archimedean functor realises this map — i.e.
the α_EM loop weight *is* the Markov Gram. The question this audit answers: does that
identification force the **magnitude** (hence `1/(8π)`), or only the shape?

## Method — is the scalar `c` convention-free?

The magnitude lives entirely in the scalar `c`. A convention-free `c` would be a
prediction; a convention-dependent `c` means `τ = W` fixes only the shape and leaves
the magnitude to a free choice. `alpha_em_b2_tau_w_freedom_probe.py` computes `c`
under five natural normalisations of the two forms:

| normalisation | `c` |
|---|---|
| Markov-trace scaled (`×w_(4,1) = 0.1286`) | **0.0921** |
| sibling route C (merged `603d1f3`, intrinsic-spectrum) | **~1.47·α_EM = 0.0107** |
| raw (eigsy-normalised `G`, integer `M_S`) | **0.7158** |
| det-normalised / trace-normalised (the `*`-isometry frame) | **1.0** |
| vs Hodge physical `Im(τ₀)·M_S` | **3.834** |

**Spread `max/min = 357`.** The transport lands `∝ M_S` in every case (Schur), but
the constant ranges over more than two orders of magnitude.

## Verdict — `τ = W` forces the FORM, not the MAGNITUDE

`c` is **convention-dependent**. The two forms carry intrinsic scales — the Markov
trace `w_(4,1)` on the Hecke side, the principal polarisation `Im(τ₀)` on the Hodge
side — but these live in **different unit systems** (algebra-trace units vs
geometric-period units), and **nothing in the representation theory bridges them**.
Two independent routes already give different `c` (this probe's `0.7158`; the merged
sibling's `~1.47·α_EM`), empirically confirming the freedom.

Consequences, stated plainly:

1. **The #4209 end-to-end closure is a form-consistency result, not a magnitude
   derivation.** It proves the Markov and Hodge Grams *can* be identified; it does
   not derive the value `1/(8π)`.
2. **`1/(8π)` is not derived by the rep-theory closure.** The magnitude is carried
   by a free scalar; the still-open `1/π` per-mode weight (the genuine physics, per
   [`alpha_em_permode_weight_probe.py`](../../computations/alpha_em_permode_weight_probe.py))
   is untouched.
3. **The anti-laundering risk is live.** If a future `τ` is *defined* so that the
   Markov-trace scale maps to the polarisation scale giving `c = 1` (the
   `*`-isometry frame, `canonical_frame_c_eq_one`), that is **consistent by
   construction, not derived** — the identity would be laundered. `c = 1` is the
   *trivial* frame, not a prediction.

## What a genuine derivation would require

A convention-free `c` — hence a real `1/(8π)` derivation via this route — needs the
**physical functor `τ` with dimensional content**: an independent construction (the
photon spectral-zeta / path-integral measure on `H^{1,0}(Bring)`, or the categorical
archimedean functor, Option D) that assigns the Markov Gram a *physical* scale
commensurable with the polarisation. Only then is `c` a number to be checked (and it
could equally **refute** the identification if it misses). Absent that, `τ = W` is,
at the scalar level, a **free choice**.

## Scope

The FORM identification (`τ(Markov) ∝ Hodge`, Schur) is rigorous and stands. This
audit narrows what it buys: the shape of the loop weight, not its magnitude. No
instance registered; `1/(8π)` phase-4; nothing wired. Witness:
`alpha-em-b2-tau-w-freedom.witness.json`.
