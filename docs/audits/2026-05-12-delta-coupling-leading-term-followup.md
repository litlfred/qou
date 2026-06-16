# Δ_coupling closed-form: leading-term lead at the (2,2) doubly-magic anchor

**Date:** 2026-05-12
**Branch:** `copilot/phase3-delta-coupling-leading-form`
**Builds on:** PR #644 P3.A initial probe ([`delta_coupling_closed_form_probe.py`](../../computations/probes/delta_coupling_closed_form_probe.py)),
[`2026-05-12-1ppb-implementation-plan.md` §Phase 3](2026-05-12-1ppb-implementation-plan.md),
[`2026-05-11-1ppb-gap-narrowing-plan.md` §Path A](2026-05-11-1ppb-gap-narrowing-plan.md)
**Author:** Copilot agent (Phase 3 follow-up handover)

This is a **single-finding** follow-up to PR #644's initial Phase 3
probe. PR #644's float64 probe surfaced one cross-anchor consistent
candidate (C1 = log(1/t) at t = h(q₀)). This document records its
verification at mpmath 50 dps and gives the next agent a precise
hand-off for the structural derivation.

## TL;DR

At the doubly-magic (2,2) anchor, with all inputs at 50 dps:

> $$\boxed{\;\Delta_{\mathrm{coupling}}(2, 2)\;\approx\;2\cdot E_0 \cdot \log\!\left(1 / h(q_0)\right)\;}$$
>
> with $E_0 = m_e / (q_0(q_0-1))$, $h(q_0) = q_0 - q_0^{-1}$, and a
> relative gap of **+0.71 % (~7100 ppm)**.

The factor of 2 is consistent with $(A - 2) = 2$ for ⁴He ($A = 4$).
**Whether $(A-2)$ generalises to the (2,1) ³He=D+p and (1,2) T=D+n
anchors is deferred to the post-#644-merge re-run** — those anchors
need $\Delta_\mathrm{cat}$ values for proton and neutron, which PR
#644 added to `magic-shell-empirical-instantiation.witness.json` but
have not yet landed on `main`.

## What was done

A new probe script,
[`computations/probe_delta_coupling_leading_form.py`](../../computations/probe_delta_coupling_leading_form.py),
emits witness
[`delta-coupling-leading-form-probe.witness.json`](../../computations/delta-coupling-leading-form-probe.witness.json)
recording five hypotheses at 50 dps:

| ID | Ansatz | Verdict at (2,2) |
|---|---|---|
| **H1** | $\Delta = (A-2) \cdot E_0 \cdot \log(1/h(q_0))$ | **+0.71 %** gap |
| H2 | residual = $c \cdot (Z-N)$ chirality term | *deferred* (needs PR #644 merge) |
| H3 | alternative factor ∈ $\{Z+N, Z\cdot N, Z^2+N^2, (A-2)^2, \min(Z,N), Z\cdot N - 1\}$ | only $(A-2)$ and $\min(Z,N)$ within 1 % of unity (degenerate at $(2,2)$) |
| H4 | $f(t) = \mathrm{Li}_2^q(-h(q_0))$ (q-dilogarithm) | no integer factor |
| H5 | same factors at $t = q_0 - 1$ (β-decay normalisation) | no integer factor |

The float64 prior in PR #644 reported the same C1 lead at +0.71 %
gap; this probe confirms it is not a precision artefact.

## Numerical context

At $q_0 = :val[q_0]{precision=6}\ldots$ and $m_e = :val[m_e_MeV]{precision=6}$ MeV:

| Quantity | Value (50 dps) |
|---|---|
| $E_0 = m_e / (q_0(q_0-1))$ | $4.18598082771483857\ldots$ MeV |
| $h(q_0) = q_0 - q_0^{-1}$ | $0.20906032198987945\ldots$ |
| $\log(1/h(q_0))$ | $1.56513244669948601\ldots$ |
| $E_0 \cdot \log(1/h(q_0))$ | $6.55161441471846489\ldots$ MeV |
| $\Delta_\mathrm{coupling}(2,2) = \Delta_\mathrm{cat}(\mathrm{^4He}) - 2\,\Delta_\mathrm{cat}(\mathrm{^3He})$ | $13.19687380754797\ldots$ MeV |
| $\Delta / (2 E_0 \log(1/h))$ | $1.00714671012\ldots$ |
| relative gap | **+0.7096 %** |

## What this is NOT

- **Not a fit.** No coefficient was tuned. The "2" came from
  evaluating $(A-2)$ at $A=4$, not from a regression.
- **Not a 1 ppb closure.** The 7100 ppm gap is ~10⁴× the 780 ppb hard
  floor from CAL-2 propagation. This is a leading-order *near-form*.
- **Not a Lean §3b-cond Pattern-A/B instance.** Per CLAUDE.md
  §3b-cond and the [`2026-05-08-trivial-skeleton-workplan.md`](2026-05-08-trivial-skeleton-workplan.md),
  a numerical near-fit cannot discharge the
  `MagicShellCrossCoupling.canonicalCrossCoupling` `sorry` — it must
  be derived from substrate primitives (Markov-trace structure or
  KLR canonical-basis count). The witness is empirical input that a
  future Pattern-B *data instance* could consume; it does not
  constitute the structural derivation.

## Next steps for the next agent

1. **Re-run post-#644 merge** with proton and neutron $\Delta_\mathrm{cat}$
   values to populate the H2 chirality-residual test and the (2,1)/(1,2)
   anchors. The float64 prior in PR #644 strongly suggests:
   - $(A-2)$ remains the leading factor (factors {2, 1, 1} match
     $(A-2)$ at A=4, A=3, A=3 respectively),
   - relative gaps spread to **+0.71 %, −8.74 %, +3.95 %** at (2,2),
     (2,1), (1,2),
   - the residual is **NOT** a pure $(Z-N)$ chirality term
     (`res(2,1) + res(1,2) = −0.257 MeV ≠ 0`).

2. **Test higher-order corrections** to close the 7100 ppm residual
   at (2,2). The most natural candidates (in priority order):
   - q-dilog *additive* correction:
     $\Delta = (A-2) E_0 \log(1/h(q_0)) + c \cdot E_0 \cdot \mathrm{Li}_2^q(-h(q_0))$
     for some integer $c$ derived from the magic-shell topology.
   - KLR canonical-basis dim count at the magic-shell partition
     (per Path A.4 of the gap-narrowing plan).
   - Multiplicative q-deformation: $\log(1/h(q_0)) \to \log_q(1/h(q_0))$.

3. **Substrate derivation.** Before any Lean instance promotion,
   show that the $(A-2) \cdot \log(1/h(q_0))$ form arises from the
   substrate-derived Markov-trace formula (not just empirically). This
   is the genuinely-mathematical Phase 3 work that the
   gap-narrowing plan flags as "new math, not plumbing".

## Files touched (this PR)

- `computations/probe_delta_coupling_leading_form.py` — new probe script (mpmath 50 dps)
- `computations/delta-coupling-leading-form-probe.witness.json` — generated witness
- `docs/audits/2026-05-12-delta-coupling-leading-term-followup.md` — this document

## Cross-references

- PR #644 — Phase 1+2 wiring + initial Phase 3 probe (open)
- PR #645 — Lean Phase 4 review (`docs/audits/2026-05-12-lean-gap-closeability-audit.md`)
- `conj:magic-shell-stabilization` — the conjecture being narrowed
- `prop:t-3he-mirror-asymmetry` — documented mechanism for the
  (2,1)/(1,2) anchor split
