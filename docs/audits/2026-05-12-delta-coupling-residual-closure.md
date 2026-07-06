# Δ_coupling residual closure: H6 / H7 / H8 probe at the (2,2) anchor

**Date:** 2026-05-12
**Branch:** `copilot/feature-coordinate-pr-644` (PR #645)
**Builds on:** [`2026-05-12-delta-coupling-leading-term-followup.md`](2026-05-12-delta-coupling-leading-term-followup.md),
[`probe_delta_coupling_leading_form.py`](../../computations/probe_delta_coupling_leading_form.py)
**Author:** Copilot agent (PR #645 Section C — Phase 3 residual-closure)

This is a **single-finding** follow-up to the Section A leading-term
probe.  Section A established at 50 dps that

$$\Delta_{\mathrm{coupling}}(2,2) \;\approx\; (A-2) \cdot E_0 \cdot \log(1/h(q_0))$$

closes the doubly-magic anchor to **+0.71 %** (~7100 ppm).  This
section probes three structural correction families to see whether
any closes the residual with a clean (rational / quantum-integer)
coefficient.

## TL;DR

> $$\boxed{\;\Delta_{\mathrm{coupling}}(2, 2)\;\approx\;[A-2]_q \cdot E_0 \cdot \log\!\left(1/h(q_0)\right)\;}$$
>
> with $[n]_q := (q^n - q^{-n})/(q - q^{-1})$ the **quantum integer**.
> At $q = q_0$, $[2]_{q_0} = q_0 + q_0^{-1} \approx 2.01090$, and the
> resulting prediction matches the (2,2) anchor with **gap +0.169 %**
> (~1700 ppm) — a **4.2× improvement** over the classical $(A-2)$
> prefactor.

The residual is still **above** the 1 ppb floor by ~6 orders of
magnitude, so this is **not** a closure.  It is a refinement that
suggests the leading form is structurally a *q-deformed* magic-shell
correction, with the residual likely arising from higher-order
$q$-corrections or anchor-class-specific structural terms.

## What was done

A new probe script,
[`computations/probe_delta_coupling_residual_closure.py`](../../computations/probe_delta_coupling_residual_closure.py),
emits witness
[`delta-coupling-residual-closure-probe.witness.json`](../../computations/delta-coupling-residual-closure-probe.witness.json)
recording three hypothesis families at 50 dps for the doubly-magic
(2,2) anchor:

| ID  | Family                                         | Verdict at (2,2)                     |
|-----|------------------------------------------------|--------------------------------------|
| H6  | additive q-dilog / q-trilog correction $c \cdot E_0 \cdot g(q_0)$ for $g \in \{\mathrm{Li}_2^q(\pm h),\,\mathrm{Li}_3^q(-h),\,\log(1+h),\,h,\,h^2,\,(1-h)\log(1/h)\}$ | **none** — no $c$ within $10^{-3}$ of any $p/q$, $q \le 12$ |
| H7a | $[A-2]_q \cdot E_0 \cdot \log(1/h(q_0))$       | **gap +0.169 %** (4.2× better than H1) |
| H7b | $(A-2) \cdot E_0 \cdot \log_q(1/h(q_0))$        | gap +9.6 %, worse than H1            |
| H8  | additive micro-correction $c \cdot s$ for $s \in \{m_e,\,E_0 h,\,E_0 h^2,\,E_0/q_0,\,E_0/q_0^2\}$ | **none** — no $c$ within $10^{-3}$ of any small rational |

### Numeric details (50 dps)

| Quantity                              | Value                            |
|---------------------------------------|----------------------------------|
| anchor $\Delta_{\mathrm{coupling}}(2,2)$ | 13.196873807548 MeV          |
| H1 prediction $2 \cdot E_0 \cdot \log(1/h)$ | 13.103228829437 MeV         |
| H1 residual                            | +0.093644978111 MeV (+0.710 %) |
| $[2]_{q_0} = q_0 + q_0^{-1}$           | 2.010896869118                  |
| H7a prediction $[2]_q \cdot E_0 \cdot \log(1/h)$ | 13.174620914229 MeV     |
| H7a residual                           | +0.022252893319 MeV (+0.169 %) |
| H7b prediction $2 \cdot E_0 \cdot \log_q(1/h)$ | 12.037507287762 MeV     |
| H7b residual                           | +1.159366519786 MeV (+8.785 %) |

## Interpretation

The improvement from H1 to H7a is structurally meaningful:

1. **Quantum integer prefactor is the natural q-deformation** of the
   counting prefactor $(A-2)$, replacing the classical "number of
   bound nucleons beyond the closed pair" by its KLR / quantum-group
   counterpart.

2. **$\log(1/h(q_0))$ remains classical** — H7b's q-deformation of
   the *log* factor (rather than the prefactor) makes things
   significantly worse (+9.6 % vs +0.7 %), so the q-deformation lives
   in the prefactor, not in the radial function.

3. **The remaining 1700 ppm gap** is far above the 1 ppb floor.  The
   residual is now $+0.0223$ MeV $= +0.0339 \cdot E_0$ — small
   enough that further probing should look at higher-order structural
   corrections (KLR canonical-basis dimension counts, or anchor-class
   topology multiplicity) rather than additional q-deformations.

## What is OPEN

- **Cross-anchor consistency** (BLOCKING).  The (2,1) ³He=D+p and
  (1,2) T=D+n anchors require $\Delta_\mathrm{cat}$ for proton and
  neutron, added by PR #644 to
  `magic-shell-empirical-instantiation.witness.json` but not yet on
  `main`.  H7a's quantum-integer prefactor MUST be re-run with all
  three anchors before any substrate-derivation attempt — a
  coefficient that varies across $(Z, N)$ is not a structural
  closure.
- **Substrate derivation** of the $[A-2]_q$ prefactor.  H7a
  identifies a structural near-form, but per AGENTS.md §3b-cond +
  the trivial-skeleton workplan, a numerical near-fit is **not**
  acceptable as a Pattern-A/B Lean instance.  The next agent must
  derive $[A-2]_q$ from KLR / Markov-trace primitives before any
  Lean promotion.
- **Closing the residual 1700 ppm gap** to the 1 ppb floor.  Likely
  candidates for the residual structural term: KLR canonical-basis
  dimension at the magic-shell topology class, or a higher-order
  $h$-expansion correction.  None of the H6/H8 ansatz families
  closed it at the (2,2) single anchor.

## Recommended next steps for the post-#644-merge agent

1. **Re-run** `probe_delta_coupling_residual_closure.py` after
   PR #644 merges and the proton + neutron $\Delta_\mathrm{cat}$
   values are on `main`.  Extend the script to evaluate H1, H7a,
   H7b, H6 and H8 candidates at all three anchors $(2,2)$, $(2,1)$,
   $(1,2)$, and emit a consistency table:
     - For H7a: report $[A-2]_q \cdot E_0 \cdot \log(1/h)$ vs each
       anchor and flag whether the relative gap is consistent across
       $(Z,N)$.
     - If H7a is consistent, report the residual ratio
       $(\text{anchor} - [A-2]_q E_0 \log(1/h)) / E_0$ at each
       anchor and check whether *that* ratio is anchor-independent
       (a shared structural correction) or anchor-class-specific.

2. **If H7a is cross-anchor consistent**, draft a §3b-cond Pattern-B
   class statement for `MagicShellCrossCoupling.canonicalCrossCoupling`
   that names $[A-2]_q \cdot E_0 \cdot \log(1/h(q_0))$ as the
   leading form and axiomatises the residual as a **named** higher-
   order structural correction (not as a free numerical fit term).
   Do NOT commit a Lean discharge that closes only one anchor.

3. **If H7a is NOT cross-anchor consistent**, treat the (2,2)
   improvement as an anchor-class coincidence (doubly-magic) and
   continue exploring substrate-derived corrections.  Update
   [`docs/audits/2026-05-12-1ppb-implementation-plan.md`](2026-05-12-1ppb-implementation-plan.md)
   §Phase 3 with the negative finding.

## Acceptance / non-acceptance

- **Accept** as a structural near-form refinement of H1 — H7a is
  worth recording and re-running cross-anchor.
- **Do NOT accept** as a Lean §3b-cond Pattern-A/B discharge for
  `MagicShellCrossCoupling.canonicalCrossCoupling`.  The 1700 ppm
  gap is ~$10^6\times$ the 1 ppb target, and the substrate
  derivation of $[A-2]_q$ from KLR / Markov-trace structure has not
  been attempted.
- **Do NOT** calibrate H7a's residual to AME — three-cal discipline
  forbids it.

## Files added by this section

- [`computations/probe_delta_coupling_residual_closure.py`](../../computations/probe_delta_coupling_residual_closure.py)
- [`computations/delta-coupling-residual-closure-probe.witness.json`](../../computations/delta-coupling-residual-closure-probe.witness.json)
- This handover document.
