#!/usr/bin/env python3
"""The LEGACY-MARSHALLED frame, in one named place — bean `qou-iu3m`.

`canonical_braid_marshalling.marshal_to_chi_lambda_braid` "emits signs and
drops `d` entirely" (its own docstring) and maps `averaged -> sign=+1`. For a
nucleon chain that is lossy in a specific, measurable way: each chain carries
TWO `averaged` crossings — intra-nucleon, nothing to do with a p-n interface —
so the flattening replaces that crossing's Markov factor `z - h/2` by `z`, at
two sites per nucleon. The result differs from the true trace of the stated
Hecke element by 15.3 % (proton) and 27.3 % (neutron):

    legacy (this module)   tau_p 1.3215929842373445   tau_n 1.2575579046963118
    canonical helper       tau_p 1.1457596924573009   tau_n 0.9877436881158096

## This module is NOT a deprecation shim, and its callers are NOT broken

`closed_form_tau_M.compute_tau_M_nucleon_H3` was fixed on 2026-08-26 to stop
dropping `d` (bean `qou-qu2w`). The scripts that call THIS module were
deliberately left alone, and must stay that way: each compares a closed form
against an *empirical slow path* that is itself bound to `chi_lambda_braid`
via the same marshaller. Both sides of such a comparison must sit in ONE
frame or the comparison means nothing. The 2026-06-03 colour-averaging audit
says exactly this — "leave validation-only callers on `chi_lambda_braid`
(they match the empirical pipeline by design)".

So: **do not re-point these callers at the canonical helper.** Doing so would
silently re-frame one side of each comparison, and the checks would go on
passing while testing nothing.

## Why it exists as a module at all

Before this, the legacy frame lived as THREE anonymous local copies —
`marshal_intra` duplicated verbatim in `closed_form_tau_M_verification_phase5q`
and `rho_constit_equals_tau_M_proton_phase5l`, each wrapped in its own
near-identical trace function, plus a third full-word usage in
`constit_factor_varying_q_phase5k2`. Two of those copies were named
`compute_tau_M_nucleon_H3` / `compute_tau_M_proton_H3` — colliding with the
canonical helper's name while returning different numbers, with nothing
saying so.

That invisibility is what let the `qou-qu2w` defect survive: the canonical
helper had the same bug, and there was no single place where "this is the
lossy frame" was written down, so fixing one copy told you nothing about the
others. A named module makes the frame greppable, gives the divergence one
documented home, and means a fourth copy is a visible choice rather than an
accident. `test_legacy_frame_no_new_copies.py` enforces that.

Ref: closed_form_tau_M.py (compute_tau_M_nucleon_H3 — the CANONICAL helper)
Ref: canonical_braid_marshalling.py (marshal_to_chi_lambda_braid)
Ref: docs/audits/2026-06-03-color-averaging-wiring-audit.md
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402

import mpmath as mp  # noqa: E402

from canonical_braid_marshalling import marshal_to_chi_lambda_braid  # noqa: E402


def legacy_h_val() -> float:
    """`h = q - 1/q` at the substrate point, as a float.

    Sign-classification parameter for `marshal_to_chi_lambda_braid` (matched
    against `d` within eps=1e-10), NOT a precision coefficient — which is why
    a float is correct here and does not put f64 into any computed value.
    """
    from q_parameter import Q as Q0
    return float(Q0 - 1 / Q0)


def legacy_marshal_intra(chain_g0, chain_g1, h_val: float | None = None):
    """Marshal an H_3 nucleon intra word to `[(sign, gen)]` for chi_lambda_braid.

    Was duplicated verbatim as `marshal_intra` in two scripts. LOSSY by
    construction — see the module docstring.

    LOSSY IN A SECOND WAY THE MODULE DOCSTRING DID NOT NAME: the assembly below
    is the GROUPED intra ordering, all of g0 then all of g1. It used to be
    written out inline here, which made it indistinguishable from the dozen
    other unnamed transcriptions of that line the corpus grew (bean
    `qou-t29k`). It now says so, by calling the one definition. That is the
    right call *for this module*, which exists to be the legacy frame and
    documents its own legacy values two functions down — it is NOT the right
    call for a site that wanted the canonical word, and the audit counts these
    calls (check E) precisely so the difference stays visible.

    Nothing moves numerically: `grouped_word_from_chains` is the same
    concatenation, hoisted.
    """
    from pyhecke.atom import grouped_word_from_chains
    if h_val is None:
        h_val = legacy_h_val()
    chain_with_gens = grouped_word_from_chains(chain_g0, chain_g1)
    return marshal_to_chi_lambda_braid(chain_with_gens, h_val)


def legacy_nucleon_tau_M_H3(g0, g1, q_val: mp.mpf, dps: int = 50) -> mp.mpf:
    """tr_M^3(nucleon, q) IN THE LEGACY FRAME — `d` dropped on averaged crossings.

    ⚠ This is NOT `closed_form_tau_M.compute_tau_M_nucleon_H3`. The name is
    deliberately different now; two of the copies this replaces shared that
    name while returning different numbers. Use the canonical helper for
    anything that is not comparing against the legacy empirical slow path.

    Returns 1.3215929842373445 (proton) / 1.2575579046963118 (neutron) at the
    substrate q_0, against the canonical 1.1457596924573009 / 0.9877436881158096.
    """
    from hecke_characters import chi_lambda_braid, partitions_of
    from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric

    word = legacy_marshal_intra(g0, g1)
    q_str = mp.nstr(q_val, dps, strip_zeros=False)
    total = mp.mpf(0)
    for lam in partitions_of(3):
        y = y_lambda_wenzl_bridge_numeric(lam, q_val, dps=dps)
        chi = chi_lambda_braid(lam, word, q_value=q_str,
                               precision=f"mpfr_{dps}dps")
        total += y * mp.mpf(str(chi))
    return total
