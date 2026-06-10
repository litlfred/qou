# The α_{basis-knot} coupling family — pre-archimedean (no π)

**Date:** 2026-06-10. **Owner directive:** "take up and finish the
α_{basis-knot} work (α_EM := α_{T_{2,3}}); write up in paper, prove in Lean,
use in compute to optimize/reduce error. I don't like to see π… should be
pre-archimedean."

## Goal

A coupling constant **α_K for each of the 6 cohomological force-knots** on
Bring's Σ₄ (`prop:cohomological-embedding`: `{T_{2,3}, T_{2,5}, T_{2,7},
T_{2,9}, T_{3,4}, T_{3,5}}`), with **α_EM := α_{T_{2,3}}** (the trefoil,
electromagnetic). Everything **pre-archimedean** — in
`R = ℤ[q^{±1/2}, h^{-1}]` (`h = q − q⁻¹`), **no π** in the derivation; π appears
only as the archimedean image under `τ_arch`.

## Pre-archimedean building block (foundation — DONE)

The q-dimension decoration, in q-data, no π:
$$\delta_q(T_{2,k}) = q^k - q^{-k} = h\,[k]_q, \qquad [k]_q = \frac{\sinh(k\lambda)}{\sinh\lambda},\ \lambda=\ln q.$$
α_EM, pre-archimedean (`prop:alpha-em-categorical-trace-ratio`):
$$\alpha_{EM} = \frac{h^2}{q\,\delta_q(T_{2,9})\,\delta_q(T_{3,5})} = \frac{1}{q\,[9]_q\,[10]_q}$$
— the antisymmetric **e₋ (sinh)** coupling of the Hopf 2-strand operation
(`thm:em-spectral-completeness`, `cor:gauge-coupling-uniqueness`). Bare residual
−1.55×10⁻³ vs CODATA. Compute: `alpha_basis_knot_couplings.py` (witness, 2/2;
the 6 δ_q + the bare FSC, no π).

## The π problem → push pre-archimedean via the Hopf/sinh channel

The corrections `2/(3π)` and `α/(4π)` (`prop:em-coupling-bring-zero-mode`) are
the **archimedean** pieces. The block itself suggests they come from a **Hopf
fibration S¹→S³→S²** — i.e. the **same Hopf / e₋ / sinh channel** as van der
Waals (`prop:vdw-pskew-isolation`, the bar-odd `sinh(2λ)(e₊−e₋)` residual) and
the FSC e₋ coupling. So `2/(3π)` is the `τ_arch`-image of a **pre-archimedean
sinh/q quantity**; finding that source is the no-π optimization that reduces the
residual without writing π.

## Deliverables / roadmap

| # | step | status |
|---|---|---|
| 1 | **Compute foundation** — 6 δ_q + bare α_EM, no π | ✅ `alpha_basis_knot_couplings.py` |
| 2 | **3-strand δ_q** — `T_{3,4}` (and `T_{3,5}` check) via Rosso–Jones | open |
| 3 | **Per-force α_K assembly** — which carriers mediate which force (EM uses `T_{2,9},T_{3,5}`; strong/weak/gen need their carrier sets) | open (research) |
| 4 | **Lean** — `δ_q(T_{2,k}) = h[k]_q` and the per-knot α_K = trace, sorry-free (generic ring, no π) | open |
| 5 | **Paper** — `def:alpha-basis-knot-coupling` (the family) + `prop` (α_EM = α_{T_{2,3}}), pre-archimedean | open |
| 6 | **Optimize (no π)** — the pre-archimedean sinh/q source of `2/(3π)`+`α/(4π)` (the Hopf S¹→S³→S² / e₋ channel); reduce the residual to ≤ CODATA σ without π | open (the prize) |

## Discipline

- **No π in the derivation** (pre-archimedean R); π only as the `τ_arch` image.
- **No fitting** — each α_K and each correction must be a q-rational/sinh
  expression forced by the cohomological force structure, reported tiered.
- Coordinate with the stalled `alpha-em-4pi-*` family (`todos/research-queue.json`
  `triage-alpha-em-4pi-sibling-family`) — they are the (π-carrying) α/(4π)
  attempts; this program reframes them pre-archimedean.
