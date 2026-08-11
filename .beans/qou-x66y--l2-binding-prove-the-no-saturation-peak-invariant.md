---
# qou-x66y
title: 'L2 binding: prove the no-saturation-peak invariant for the additive per-bond chain (upgrade probe_collective_binding_residual''s near-proof to Lean)'
status: completed
type: task
priority: normal
created_at: 2026-08-11T10:10:00Z
updated_at: 2026-08-11T10:10:45Z
---


## DONE (2026-08-11) — proved, and the exclusion bites

`computations/probe_collective_binding_residual.py` argued at "near-proof level"
that the additive per-bond chain has "no mechanism to produce a saturation PEAK".
That argument narrows the whole collective-binding search, but AGENTS.md
§"Before declaring refuted" allows a scope-(b) exclusion only on a **proved**
invariant. It was not proved. Now it is.

`QOU/MassTheory/ChainBindingNoSaturationPeak.lean` (sorry-free, 3 theorems):

* `chainPerNucleon_eq_hyperbola` — along any isobaric chain (`d = N − Z` fixed),
  `B_sym(A)/A = c₁ + c₂/A` **exactly**, with
  `c₁ = α(L_pp+L_nn)/2` **independent of `d`** and all the `d`-dependence in `c₂`.
  An identity, discharged by `ring`.
* `hyperbola_no_interior_max` — `c₁ + c₂/A` is monotone on `A > 0`, so never
  exceeds both neighbours.
* `chain_no_saturation_peak` — hence no saturation peak, for **any** `α`,
  per-bond constants, or isospin excess.

The `d`-independence of `c₁` is what makes it a real exclusion rather than an
artifact of looking along `N = Z`: every isobaric chain is a hyperbola with the
*same* asymptote.

### Measured, not asserted (`chain_binding_hyperbola_no_peak_probe.py`, exit 0)

* Production `B_sym` **is** the hyperbola: worst |diff| **4.44e-16** over
  2H/4He/6Li/12C/16O/24Mg/40Ca. So the theorem is about the right object, not an
  idealization of it.
* Measured `B_AME/A` peaks at **⁵⁶Fe, 8.7904 MeV** — interior, as required.
* Chain asymptote **c₁ = 2.9242 MeV/nucleon**: the chain is **3.01× low even at
  its own A→∞ limit**.

That last number sharpens the standing framing. The missing collective term is
not only responsible for the *shape* (the peak) but for ~2/3 of the *magnitude* —
the chain cannot reach the plateau even asymptotically.

### Scope

Scope-(b), narrow. Excludes additive per-bond-type sums with constants fixed
along an isobaric chain **as the source of the peak**. Does NOT exclude the chain
as an additive contribution (AGENTS.md permanence principle 1 — an inaccurate
total does not invalidate a proved per-bond factor), nor `A`-dependent per-bond
constants, nor say anything about the magnitude of the missing term. Nothing
fitted; the Δ_λ "no seventh ansatz" gate untouched.
