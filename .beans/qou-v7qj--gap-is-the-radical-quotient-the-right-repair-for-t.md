---
# qou-v7qj
title: 'GAP: is the radical quotient the right repair for the convention-D operator-selection LP?'
status: todo
type: task
priority: normal
created_at: 2026-08-24T21:23:19Z
updated_at: 2026-08-24T21:24:00Z
---

## Where this comes from

`qou-pb1w` is closed. Its last result: the convention-D operator-selection LP,
run on the `H₃(q)/rad` quotient, selects a canonical parameter-free direction
`Φ*` — and **no element of the coset `Φ* + span(v)` is a nonzero scalar
multiple of a braid image.** Proved symbolically over `ℚ(q)`, not searched.
Probe: `computations/meson/operator_selection_lattice_symbolic.py`; audit:
`docs/audits/2026-08-24-meson-braid-obstruction-a-measured.md`.

The exclusion is scope (b) with the invariant named — every braid word of
exponent sum `e` sits at `χ_sym = qᵉ`, `det ρ_std = (−1)ᵉ`, `χ_alt = (−1/q)ᵉ`
in the Wedderburn decomposition `H₃(q) ≅ ℚ(q) ⊕ M₂(ℚ(q)) ⊕ ℚ(q)`, hence
satisfies `χ_sym·χ_alt = det ρ_std` identically, and `Φ*`'s coset does not.

## The open question, stated sharply

**The two facts are the same fact, and that is what needs explaining.**

- The radical `v` (`vᵢ = (−1/q)^{ℓ(wᵢ)}`, the q-antisymmetriser) is what makes
  the convention-D Gram singular. Quotienting by it is the repair that turns a
  degenerate LP — unbounded in a direction neither the constraints (`Gv = 0`)
  nor the objective (`t·v ≈ −4.4e-16`) can see — into a finite optimum with a
  non-degenerate active set.
- `χ_alt(x) = v·x` **exactly**. So the quotient condition `v·x = 0` **is** the
  vanishing of the alternating character.

So the repair for LP degeneracy is, verbatim, the condition that forbids the
answer from being a braid. That is not a coincidence to note and move past —
it is the whole content of Obstruction A under convention D.

## What would count as progress

Any one of these, in rough order of how cheap it is to settle:

1. **Is the quotient the right repair at all?** It is one way to fix an
   unbounded polyhedron. Alternatives that do not annihilate `χ_alt`: a
   different normalisation in place of `Σx = 1`; bounding via a norm rather
   than a linear condition; keeping the full space and regularising the
   objective. Each gives a different `Φ*` with, in general, `χ_alt ≠ 0`.
2. **Is the objective right?** `primal_obj = 0` and `y₀* = 0` at every target
   — the minimum-action operator is trace-free and the dual certificate is
   trivial, so `n_target` is a pure scale rather than a selector. A program
   whose dual carries no information is weak evidence that the program is the
   intended one.
3. **Should the LP select a braid at all?** Possibly the honest reading is
   that it selects an algebra element and the braid is recovered downstream by
   a different map. If so, say it explicitly in `prop:operator-selection-lp`,
   because the current framing invites the braid reading.
4. **Does convention C behave differently here?** Under C the Gram is
   non-singular (`det = −0.1892`, cond 34), so there is no radical, no
   quotient, and no forced `χ_alt = 0`. That does **not** reopen C — the owner
   ruling of 2026-08-15 is not up for renegotiation — but the contrast
   localises exactly what D's singularity costs, and is cheap to measure.

## What is NOT open

- **Integrality.** `Ψ = D·Φ* = (−q³, −q⁴, N, −q⁵, qN, −q⁶)` with
  `N = q⁶+q²+1` and `D(q) = (q+1)(q⁶−q⁵−q³+q²+1)`: every entry a polynomial
  with integer coefficients. `Φ*` **is** in the `ℤ[q,q⁻¹]`-lattice up to one
  scale, so no integrality argument forbids it. That candidate obstruction was
  tested and does not fire.
- **Whether `G⁻¹` blocks this.** It does not, twice over: the LP uses `G` only
  as `Gx ≥ 0`, and `G_PINV` exists and is owner-approved. Both of my earlier
  "blocked" claims were wrong and are retracted in the audit.

## Discipline note

The exclusion above is a **structural** (b) result, resting on a proved
invariant, not on a search coming back empty. Do not weaken it to "we could
not find a braid". Equally, do not read it as refuting the framework: it says
the convention-D LP on the quotient selects an algebra element that no braid
realises, which relocates Obstruction A rather than closing off the program.
