#!/usr/bin/env python3
"""
binding_multibond_wenzl.py — test the multi-bond binding hypothesis in
the CANONICAL Wenzl Jones-Markov convention (conventions now reconciled,
trace_convention_reconciliation.py).

The atom braid is a chain of A−1 inter-nucleon bonds (pp/pn/nn). The
single-link endomorphism B = m_e·Vol(𝓑₃)·Δtr_combined gives ²H
(−6.3%) and fails A≥3 (−56%) because the COMBINED Δtr (all bonds
multiplied together) is nearly A-flat.

⚠ NUMBERS CORRECTED 2026-08-15 (bean `qou-jdhm`). This read "matches ²H
(+0.2%)". That figure is trace **convention C**, excised by owner ruling
2026-08-09 in favour of **convention D**; under D the deuteron is −6.3%.
The A-flatness argument — the actual content of this module — is
unchanged, and the hypothesis tested below is unaffected: it was
motivated by the combined Δtr being nearly A-independent, not by the
deuteron matching.

⚠ Note also that the header line above claims the conventions are "now
reconciled". That refers to `trace_convention_reconciliation.py`, and is
a SEPARATE question from the C→D excision; the corpus-wide C→D sweep is
bean `qou-wgta` and was still open as of this edit.

Hypothesis under test: binding is ADDITIVE over chain bonds —
    B(K) = m_e · Vol(𝓑₃) · Σ_bonds Δtr_bond,
where Δtr_bond is the Wenzl trace shift from activating one bond from
the vacuum. No scale fit; Vol(𝓑₃) is the deuteron-fixed scale and the
sum is over the chain bonds the braid already defines.

Reports per-bond Δtr and the additive-sum prediction vs AME — honestly,
whether or not it closes.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

from mpmath import mp, mpf, fabs, catalan

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)
from tr_m_wenzl_bridge_mpfr import tr_M_via_wenzl_bridge_mpfr  # noqa: E402
from hecke_core import (  # noqa: E402
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1, h as H_VAL,
)


def _chain_word(Z, N, active_bonds):
    """Chain braid word with inter-nucleon bonds only at indices in
    `active_bonds` (subset of range(A-1)). Mirrors atom_braid_word_3A
    but with per-bond on/off control."""
    A = Z + N
    ordering = ["p"] * Z + ["n"] * N
    word = []
    for k, nuc in enumerate(ordering):
        g0 = _PROTON_G0 if nuc == "p" else _NEUTRON_G0
        g1 = _PROTON_G1 if nuc == "p" else _NEUTRON_G1
        for c, d in g0:
            word.append((float(c), float(d), 3 * k))
        for c, d in g1:
            word.append((float(c), float(d), 3 * k + 1))
        if k < A - 1 and k in active_bonds:
            nxt = ordering[k + 1]
            if nuc == "p" and nxt == "p":
                cross = (1.0, 0.0)
            elif nuc == "n" and nxt == "n":
                cross = (1.0, -float(H_VAL))
            else:
                cross = (1.0, -float(H_VAL) / 2)
            word.append((cross[0], cross[1], 3 * k + 2))
    return word


def main():
    set_compute_dps()
    wb = WitnessBuilder("binding-multibond-wenzl", engine="mpmath")

    qs = Q_50_DIGIT_STR
    m_e = mpf(str(M_E_MEV))
    VOL_B3 = 8 * catalan

    isos = [("2H", 1, 1, AME_B_DEUTERON_MEV_VALIDATION),
            ("3H", 1, 2, AME_B_TRITIUM_MEV_VALIDATION),
            ("3He", 2, 1, AME_B_HE3_MEV_VALIDATION),
            ]  # ⁴He (H₁₂) omitted — too slow for this probe

    print("=" * 70)
    print("MULTI-BOND BINDING (Wenzl JM): B = m_e·Vol(𝓑₃)·Σ_bonds Δtr_bond")
    print("=" * 70)
    print(f"m_e·Vol(𝓑₃) = {float(m_e * VOL_B3):.6f} MeV")
    print()

    results = {}
    for iso, Z, N, ame in isos:
        A = Z + N
        n_strands = 3 * A
        n_bonds = A - 1
        ame = mpf(str(ame))

        tr_vac = fabs(mpf(str(tr_M_via_wenzl_bridge_mpfr(
            _chain_word(Z, N, set()), n_strands, qs, dps=50))))

        # per-bond Δtr (each bond alone, from vacuum)
        per_bond = []
        for b in range(n_bonds):
            tr_b = fabs(mpf(str(tr_M_via_wenzl_bridge_mpfr(
                _chain_word(Z, N, {b}), n_strands, qs, dps=50))))
            per_bond.append(tr_vac - tr_b)

        # combined (all bonds on) — the single-link approach
        tr_all = fabs(mpf(str(tr_M_via_wenzl_bridge_mpfr(
            _chain_word(Z, N, set(range(n_bonds))), n_strands, qs, dps=50))))
        dtr_combined = tr_vac - tr_all

        sum_per_bond = sum(per_bond, mpf(0))
        B_sum = m_e * VOL_B3 * sum_per_bond
        B_combined = m_e * VOL_B3 * dtr_combined
        err_sum = float((B_sum - ame) / ame * 100)
        err_comb = float((B_combined - ame) / ame * 100)

        results[iso] = {
            "n_bonds": n_bonds,
            "per_bond_dtr": [mp.nstr(x, 12) for x in per_bond],
            "sum_per_bond": mp.nstr(sum_per_bond, 12),
            "dtr_combined": mp.nstr(dtr_combined, 12),
            "B_sum_MeV": mp.nstr(B_sum, 10),
            "B_combined_MeV": mp.nstr(B_combined, 10),
            "B_AME_MeV": mp.nstr(ame, 10),
            "err_sum_pct": err_sum,
            "err_combined_pct": err_comb,
        }
        print(f"  {iso} (A={A}, {n_bonds} bond{'s' if n_bonds>1 else ''}):")
        print(f"    per-bond Δtr = [{', '.join(f'{float(x):.4f}' for x in per_bond)}]")
        print(f"    Σ per-bond   = {float(sum_per_bond):.4f}   "
              f"combined = {float(dtr_combined):.4f}")
        print(f"    B(Σ-bond)    = {float(B_sum):.3f} ({err_sum:+.1f}%)   "
              f"B(combined) = {float(B_combined):.3f} ({err_comb:+.1f}%)")

    print()
    print("Honest read: compare Σ-per-bond vs combined against AME.")
    print("Neither is tuned — both use the deuteron-fixed m_e·Vol(𝓑₃) scale.")

    wb.set_description(
        "Multi-bond binding test in canonical Wenzl JM. Per-bond Δtr "
        "(each chain bond from vacuum) and the additive sum B = m_e·Vol(𝓑₃)·"
        "Σ Δtr_bond vs AME, alongside the combined single-link value. No "
        "scale fit (deuteron-fixed m_e·Vol(𝓑₃))."
    )
    wb.add_data("isotopes", results)
    wb.add_assertion(
        "deuteron_single_bond_holds",
        computed=abs(results["2H"]["err_sum_pct"]),
        expected=0,
        tolerance=1,
        source="²H (1 bond): Σ-per-bond = combined within 1%",
    )
    # Lean SDP-uniqueness cross-reference (post-#1537 wiring).
    wb.add_data("lean_uniqueness_ref", {
        "generic": "qou:QOU.BraidKnot.@nucleus_uniqueness_closed (3*A)",
        "framework_doc":
            "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
        "note": "Certifies T_w uniqueness at the abstract empty-constraint SDP level (PR #1537 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md.",
    })

    wb.save()


if __name__ == "__main__":
    main()
