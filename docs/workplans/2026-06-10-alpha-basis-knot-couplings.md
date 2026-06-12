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
| 1 | **Compute foundation** — 6 δ_q + bare α_EM, no π | ✅ `alpha_basis_knot_couplings.py` (PR #2100) |
| 2 | **3-strand δ_q** — `T_{3,4}` (and `T_{3,5}` check) via Rosso–Jones | ✅ `rosso_jones_three_strand_delta_q.py` (PR #2107) — writhe rule `δ_q(T_{m,p}) = h[(m-1)p]_q`; `T_{3,4} → h[8]_q` resolved, `T_{3,5} → h[10]_q` derived |
| 3 | **Per-force α_K assembly** — which carriers mediate which force (EM uses `T_{2,9},T_{3,5}`; strong/weak/gen need their carrier sets) | ✅ carrier-role table, `alpha_k_per_force_assembly.py` (PR #2107); per-force *selection* stays conditional on `conj:e-hartree-categorical-derivation` (anti-fishing — no pair-vs-coupling enumeration) |
| 4 | **Lean** — `δ_q(T_{2,k}) = h[k]_q` and the per-knot α_K = trace, sorry-free (generic ring, no π) | ✅ `alpha-basis-knot-delta-q.lean` (PR #2100) + `torus_deltaQ_eq_h_qbracket` (PR #2107), sorry-free |
| 5 | **Paper** — `def:alpha-basis-knot-coupling` (the family) + `prop` (α_EM = α_{T_{2,3}}), pre-archimedean | ✅ `prop:alpha-basis-knot-delta-q` (PR #2100) + `prop:torus-knot-delta-q-writhe` (PR #2107) |
| 6 | **Optimize (no π)** — the pre-archimedean sinh/q source of `2/(3π)`+`α/(4π)` (the Hopf S¹→S³→S² / e₋ channel); reduce the residual to ≤ CODATA σ without π | **partial** — π = archimedean image of Hopf periods, corrected `1/α` resid −2.2e-8 (`alpha_em_no_pi_correction_probe.py`, PR #2107); n=1 `2/(3π) = b₁/Area` **proven** sorry-free (`PhotonIRZeroMode`, PR #2114); n=2 regrouped `α·H(q)/(π·b₁)`, resid −3.65e-10 (PR #2114). Open remainder: Habiro↔Bloch `τ_arch` bridge + `−h²α` fermion loop (PR #1495 RT 2-loop track) |

## Status addendum (2026-06-12) — where the work lives

The roadmap above was executed across three merged PRs by one session
(2026-06-10 → 06-11): **#2100** (foundation + step-4 Lean),
**#2107** (steps 2/3/5 + step-6 probe), **#2114** (step-6 n=1 proof
`b₁/Area` + n=2 Habiro regroup). The **carrier-role table for the 6
cohomological force-knots** (the "α_EM is the trefoil — what are the
other 5?" question) is in
`folio-assistant/computations/alpha_k_per_force_assembly.py` +
witness: `T_{2,3}` EM (trefoil) · `T_{2,5}` 2nd generation ·
`T_{2,7}` charm/3rd generation · `T_{2,9}` strong (force-carrier,
`(2,1,1)`, `h[9]_q`) · `T_{3,4}` Hopf-squared/top · `T_{3,5}`
weak/β-decay (force-carrier, `(3,1)`, `h[10]_q`). Open continuation
threads: PR #1495 (n=2 RT 2-loop; fermion loop `−h²α`), PR #1523
(`[2]_q(1−h²α)` = `J_2(unknot)`·Hecke 2-vertex categorical ID), and
the step-3 per-force coupling *values* (α_s, α_W) gated on
`conj:e-hartree-categorical-derivation`.

## Discipline

- **No π in the derivation** (pre-archimedean R); π only as the `τ_arch` image.
- **No fitting** — each α_K and each correction must be a q-rational/sinh
  expression forced by the cohomological force structure, reported tiered.
- Coordinate with the stalled `alpha-em-4pi-*` family (`todos/research-queue.json`
  `triage-alpha-em-4pi-sibling-family`) — they are the (π-carrying) α/(4π)
  attempts; this program reframes them pre-archimedean.
