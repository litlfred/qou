# Pre-registration: flavour-typed letters and a second flavour factor

**Date:** 2026-11-27 · **Beans:** `qou-myts`, `qou-99qc` · **Thread:** "Derive the nucleon flavour factor"

**Disclosure.** Written after exploratory scratch runs in the same session (not committed). The
scratch runs showed the typed γγ word gives `q²` exactly and that hand-placed extra letters move
with their placement. Nothing below is chosen by closeness to data; there is no selection step.

## Question

Owner ruling A (2026-11-27): the mass split uses the framing-corrected trace of
`def:mass-identity`; curls contribute 0; *"the flavour split must come from the flavour letters
themselves"*. Does a second flavour-letter contribution derive a factor of about 2 on top of the
`K`-weight cell `τ_p/τ_n = q²`?

## Model (fixed before the probe)

* Typing rule: `NucleonFlavourIsDetermined` (uu crossing = the crossing, dd = reversed, mixed =
  average). On `V⊗V`, typed `σ^ε` = `P_uu σ^ε + P_dd σ^{−ε} + P_mix (σ + σ⁻¹)/2`.
* Raw trace: letters as above. Corrected trace: every signed group letter `σ^{±1}` weighted
  `q^{∓2}` (`NucleonCurlFramingCancels.writheFactor`), extended linearly on `ℂ[B_n]`.
* `τ_c = Σ_{colourings of W_c} K(s)·⟨s|X|s⟩`, `K = diag(q, q⁻¹)` per strand
  (`NucleonSplitFullTower.markov_forces_K`).

## Observables (all reported, none selected)

1. Typed γγ words `Vᵏ`, `k = 1..6`, on `H₃`: is `τ_p/τ_n = q²` exactly (raw, corrected)?
2. Tower `n = 6`, leftmost block tagged, other block summed over colourings: typed `V³ ⊗ V³`
   (disjoint), plus three interface words (`σ₂`, `σ₂⁻¹`, γγ vertex on strands 2–4). Exact at
   `q = 11/10, 3/2`.
3. Hand-placed extra typed letters on `V³`: one letter (each generator), and the census
   recipe's three typed quark letters (`[uu|dd, ud, ud]`) over all 8 generator assignments × all
   orders. Report the range.

## Pass / fail

A "derived factor 2" requires an observable that (i) is fixed by the corpus (no unruled
placement), and (ii) gives exponent ≈ 4 under the corrected trace. Anything else is reported as
not deriving it.
