#!/usr/bin/env python3
"""Δ_I at A = 2 (deuteron): the coupling factor of the bound trace over the
disjoint product, on the canonical functional.

    Δ_I(D) := |tr_M(β_D)| / (|tr_M(β_p)| · |tr_M(β_n)|)

All three traces are the convention-D Markov trace (z_D = q³/(q²+1)) on the
ruled borromean words (owner ruling qou-hu1f) at the proton pin, read at
50 dps from `atomic-tr-m-mpfr-50dps-proton.witness.json` through
`canonical_trm_reference.tr_m_nucleon`, which refuses a pin or ordering
mismatch.

Closed form, checked here rather than assumed.  The deuteron word is the
proton word, the shifted neutron word, and one inter-nucleon letter
`(1, d_pn, σ₃)`, i.e. `σ₃ + d_pn·1`, joining the two blocks.  By the Markov
property tr(x·(σ_k + d)) = (z + d)·tr(x) for x in the subalgebra below
strand k+1, so

    Δ_I(D) = z_D + d_pn .

`d_pn` is read from the word builder's own inter letter
(`atom_braid_word_3A(1, 1)`), not typed.  Measured 2026-11-15: the two sides
agree to 9.3e-51, and Δ_I(D) = 0.5082297893767389625779957976...

The fallback Δ_I(A ≤ 2) = 1 of the retired six-term "Strategy-3"
(`jones_quotient_factor_fallback`) is therefore off by a factor 1/0.5082 ≈ 1.968.

HISTORY.  Until 2026-11-15 this script used three cached traces in an
undocumented normalisation (p 1.6332, n 1.2482, D 0.3883 — grouped word,
convention C), obtained Δ_I(D) = 0.1904, and then re-scored the six-term
deuteron mass from `atomic-braid-mass-table.witness.json`.  That input was
deleted 2026-05-19 (7f30a57924d) by owner directive (it carried the six-term
formula at 24-54 % error), so the script could not run.  The six-term mass
re-scoring is not reproduced here: its inputs no longer exist and the formula
is retired.  Rewritten as this probe on owner instruction (option C,
2026-11-15).

Output: deuteron-delta-i-audit.witness.json
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from pathlib import Path

import mpmath as mp
from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import q_at  # noqa: E402
from canonical_trm_reference import tr_m_nucleon  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402

COMPUTATIONS = Path(__file__).resolve().parent.parent
TOL = mp.mpf(10) ** -40


def inter_letter_d_pn(q: mp.mpf) -> mp.mpf:
    """The `d` of the single inter-nucleon letter of the deuteron word."""
    atom = atom_braid_word_3A(1, 1, include_inter=True, q=q)
    free = atom_braid_word_3A(1, 1, include_inter=False, q=q)
    extra = list(atom)
    for letter in free:
        extra.remove(letter)
    if len(extra) != 1:
        raise SystemExit(f"refusing: expected exactly one inter letter, got {extra}")
    c, d, _g = extra[0]
    if mp.mpf(c) != 1:
        raise SystemExit(f"refusing: inter letter coefficient c = {c}, expected 1")
    return mp.mpf(d)


def main() -> int:
    q = mp.mpf(q_at(70))
    z_D = q ** 3 / (q ** 2 + 1)

    p = tr_m_nucleon("proton")
    n = tr_m_nucleon("neutron")
    D = tr_m_nucleon("deuteron")
    disjoint = p * n
    delta_I = D / disjoint

    d_pn = inter_letter_d_pn(q)
    closed = z_D + d_pn
    gap = mp.fabs(delta_I - closed)

    bc = json.loads((COMPUTATIONS / "binding-canonical.witness.json").read_text(),
                    parse_float=str)
    rows = {r["atom"]: r for r in bc["data"]["results"]}
    d_free_bc = mp.mpf(rows["D"]["tr_M_free"])
    free_gap = mp.fabs(d_free_bc - disjoint)

    print("Δ_I at A = 2 (deuteron), convention D, borromean word, proton pin")
    print(f"  |tr_M(p)|         = {mp.nstr(p, 30)}")
    print(f"  |tr_M(n)|         = {mp.nstr(n, 30)}")
    print(f"  |tr_M(D)|         = {mp.nstr(D, 30)}")
    print(f"  disjoint p·n      = {mp.nstr(disjoint, 30)}")
    print(f"  Δ_I(D)            = {mp.nstr(delta_I, 30)}")
    print(f"  z_D               = {mp.nstr(z_D, 30)}")
    print(f"  d_pn (inter)      = {mp.nstr(d_pn, 30)}")
    print(f"  z_D + d_pn        = {mp.nstr(closed, 30)}")
    print(f"  |Δ_I − (z_D+d_pn)| = {mp.nstr(gap, 5)}")
    print(f"  binding-canonical D_free vs p·n: {mp.nstr(free_gap, 5)}")
    print(f"  fallback Δ_I = 1 is off by a factor {mp.nstr(1 / delta_I, 8)}")

    w = WitnessBuilder("deuteron-delta-i-audit", engine="mpmath")
    w.set_description(
        "Δ_I(D) = |tr_M(β_D)|/(|tr_M(p)|·|tr_M(n)|) on the canonical functional "
        "(convention-D Markov trace, borromean word, proton pin) = "
        f"{mp.nstr(delta_I, 15)}, equal to z_D + d_pn (Markov property on the "
        "single inter-nucleon letter σ₃ + d_pn) to 1e-40. The retired six-term "
        "fallback Δ_I = 1 is off by a factor ≈ 1.968. Rewritten 2026-11-15 "
        "(owner option C); the earlier Δ_I = 0.1904 used grouped/convention-C "
        "traces in an undocumented normalisation, and its six-term mass "
        "re-scoring depended on a witness deleted by owner directive."
    )
    w.set_content_block("prop:mass-coefficient-shadow-price")
    w.add_parameter("q_0", fmt(q))
    w.add_parameter("z_D", fmt(z_D))
    w.add_data("tr_M", {"proton": fmt(p), "neutron": fmt(n), "deuteron": fmt(D)})
    w.add_data("tr_M_source", "atomic-tr-m-mpfr-50dps-proton.witness.json via "
               "canonical_trm_reference.tr_m_nucleon (convention D, borromean, proton)")
    w.add_data("disjoint_product", fmt(disjoint))
    w.add_data("delta_I_deuteron", fmt(delta_I))
    w.add_data("d_pn_inter_letter", fmt(d_pn))
    w.add_data("z_D_plus_d_pn", fmt(closed))
    w.add_data("abs_gap_delta_I_vs_closed_form", fmt(gap))
    w.add_data("fallback_over_true_factor", fmt(1 / delta_I))
    w.add_data("superseded", {
        "delta_I": "0.1904",
        "inputs": "p 1.6332, n 1.2482, D 0.3883 (grouped word, convention C, "
                  "undocumented normalisation)",
        "six_term_mass_rescoring": "not reproduced: input witness deleted "
                                   "2026-05-19 (7f30a57924d) by owner directive",
    })
    w.add_assertion("delta_I_equals_zD_plus_d_pn", computed=bool(gap < TOL),
                    expected=True,
                    source="Markov property on the inter letter σ₃ + d_pn; tol 1e-40")
    w.add_assertion("binding_canonical_free_trace_is_disjoint_product",
                    computed=bool(free_gap < TOL), expected=True,
                    source="binding-canonical D tr_M_free vs |tr_M(p)|·|tr_M(n)|; tol 1e-40")
    w.add_assertion("fallback_delta_I_one_is_wrong", computed=bool(delta_I < 1),
                    expected=True,
                    source="Δ_I(D) < 1, so the six-term fallback Δ_I = 1 overstates it")
    w.save()
    print("\n✓ Witness: deuteron-delta-i-audit.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
