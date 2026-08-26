---
# qou-qu2w
title: H3 constituents disagree between the two canonical tr_M(4He) producers by 2.157x
status: completed
type: task
priority: normal
created_at: 2026-08-25T22:10:20Z
updated_at: 2026-08-26T13:20:06Z
---

Found 2026-08-25 while flipping `_habiro_coefficient_extract.py` to the
canonical `bring_color_weighted` p-n interface (bean `qou-cds4`, PR #5801).
**NOT caused by that flip** — both producers disagreed by this factor before it.

Two producers compute tr_M(⁴He) at q₀, both now in the canonical frame:

    habiro-coefficients-helium-4.witness.json      0.16097414544240738
    atomic-tr-m-helium4-canonical.witness.json     0.34716181818783578
    ratio                                          2.1567

The difference is entirely in the **H₃ constituent traces**, not in the
interface convention (both now price p-n as `z - h(1/2 - delta/4)`):

    habiro chain, from habiro-coefficients-atomic.witness.json
        tau_p = 1.1457596924573008697   tau_n = 0.98774368811580957163
    compute_tau_M_nucleon_H3 (closed_form_tau_M)
        tau_p = 1.321592984237344535    tau_n = 1.257557904696311813

    (1.321592984 * 1.257557905)^2 / (1.145759692 * 0.987743688)^2 = 2.1567

which is the whole ratio, exactly.

So one of the two H₃ baselines is not canonical, or the two are computing
different objects under one name. Worth settling: the habiro chain feeds 25
committed mass-table witnesses and ~72 consumers, and `compute_tau_M_nucleon_H3`
feeds the closed-form path.

Not in scope for PR #5801, which changes only the interface convention.
Recorded in docs/audits/2026-08-23-habiro-mass-table-convention-c-attribution.md.


## ROOT-CAUSED AND FIXED 2026-08-26 (owner: "fix all issues found")

**Not a convention difference.** Both producers are convention D — the habiro
atomic `tr_M_in_q` is rational in q with no half-powers and its proton
denominator factors as `4q^9(q^2+1)^2`, the D fingerprint — and A=1 has no p-n
interface, so no `pn_convention` argument reaches the site at all. That is
exactly why it survived every convention audit: anything keyed on
`pn_convention` is structurally blind here. The ratio also DIFFERS between
proton (1.15346) and neutron (1.27316), so it did not look like a common
normalisation factor either.

### Root cause

`closed_form_tau_M.compute_tau_M_nucleon_H3` marshalled the nucleon chain
through `canonical_braid_marshalling.marshal_to_chi_lambda_braid`, which by its
own docstring "emits signs and drops `d` entirely" and maps `averaged ->
sign=+1`. Each nucleon chain carries TWO `averaged` crossings — INTRA-nucleon,
nothing to do with a p-n interface:

    proton   {sigma: 6, averaged: 2, sigma_inv: 3}
    neutron  {sigma: 5, averaged: 2, sigma_inv: 4}

so the flattening replaced that crossing's Markov factor `z - h/2` by `z`, at
two sites per nucleon. That marshaller's defence — "equally lossy for both
variants, which is why the collapse is correct *here*" — is about `averaged` vs
`averaged_weighted`, and does not license `averaged -> sigma`.

### Fix

Re-pointed to `chi_monotone_transfer.chi_all_lambda`, which preserves `d` and is
independently validated (its own self-test checks it against `char_fast` at n=6
and four cached oracles to n=12, all at 1e-50). Also passes `q=q_val`
explicitly, removing a second, latent straddle: the old code classified
crossing signs against the module-level `q_parameter.Q` while tracing at the
caller's `q_val`.

    tau_p  1.32159298423734454 -> 1.14575969245730087
    tau_n  1.25755790469631181 -> 0.987743688115809572

Both now reproduce `habiro-coefficients-atomic.witness.json` to ~1e-50, and
`atomic-tr-m-helium4-canonical` gives 0.16097414544240738 against the habiro
table's 0.16097414544240737. **The 2.157x is closed.**

Convention axes verified explicitly, not assumed:
  D              markov_z = q^3/(q^2+1) = 0.61268803714646525 (C would be 0.49932)
  proton pin     Q_50_DIGIT_STR = 1.109978582751380807... (muon is ...9955573347)
  colour-weighted  4He kinds = [positive, averaged_weighted, negative],
                   f_pn = 0.50822978937673896 (blind z-h/2 = 0.50815788774864559)

### Not affected, and why

`closed_form_tau_M_verification_phase5q.py` defines its OWN local
`compute_tau_M_nucleon_H3` using the legacy marshalling and passes those taus
into `closed_form_tau_M` as arguments, so it is entirely self-contained in the
legacy frame. It therefore still validates what it is meant to validate — the
closed-form machinery against the empirical slow path within one frame, which
is what the 2026-06-03 audit says to preserve. NOTE the name collision: a local
function shares the canonical helper's name and now computes something
different. Flagged in-file.

Measured by `probes/nucleon_h3_marshalling_divergence_probe.py`.


## CLOSED 2026-08-26 — landed on main (PR #5821 cone, merge 0bc2794da9)

`closed_form_tau_M.compute_tau_M_nucleon_H3` now routes through the
d-preserving `chi_monotone_transfer.chi_all_lambda` instead of
`marshal_to_chi_lambda_braid`, which flattened each nucleon's two
INTRA-nucleon averaged crossings to plain sigma. Verified present on
origin/main. tau_p 1.32159298 -> 1.14575969, tau_n 1.25755790 -> 0.98774369;
the 2.157x 4He constituent disagreement is closed. Root cause was NOT a
convention issue — both producers were convention D throughout.
