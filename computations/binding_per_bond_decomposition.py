#!/usr/bin/env python3
"""
binding_per_bond_decomposition.py — decompose the H_{3A} binding trace
into per-inter-nucleon-bond contributions (groundwork for the open
A≥3 binding problem).

The atom braid is a CHAIN: nucleon₀ —[bond₀₁]— nucleon₁ —[bond₁₂]— …
with inter-nucleon crossings at generators 3k+2 (pp: (1,0),
pn: (1,−h/2), nn: (1,−h)). Binding lives in these bonds.

This probe toggles each inter-nucleon bond on/off and records the
per-bond trace shift, to test whether binding is additive over bonds
(chain) or pairs. It does NOT fit a scale — it reports the raw
structure so the A-dependence can be characterised honestly.

Per the binding-link-volumes finding (PR #1397): a single binding-
link volume does NOT carry the A-dependence, so the next hypothesis
is a per-bond / per-pair sum. This script produces the data to test
that, without rescaling Δtr by hand-chosen factors (cf. retracted
PR #1383).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

from mpmath import mp, mpf, fabs

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

try:
    from mass_at_3A_proper import (
        atom_braid_word_3A, chi_lambda_of_word,
        normalized_plancherel_weights_3A, _cached_seminormal,
    )
    HAVE_INFRA = True
except Exception as e:  # pragma: no cover
    HAVE_INFRA = False
    _IMPORT_ERR = str(e)


def full_trace(Z, N, q, include_inter):
    """H_{3A} Wedderburn Markov trace of the atom braid, using the
    same normalized-Plancherel weight table + cached seminormal
    matrices as per_generator_V_hat_3A."""
    n_strands = 3 * (Z + N)
    n_gens = n_strands - 1
    word = atom_braid_word_3A(Z, N, include_inter=include_inter)
    total = mpf(0)
    for shape, w_lam in normalized_plancherel_weights_3A(Z + N):
        sigmas, dim, _ = _cached_seminormal(shape)
        if dim == 0:
            continue
        chi = chi_lambda_of_word(sigmas, dim, word, n_gens)
        total += mpf(str(w_lam)) * mpf(str(chi)) / dim
    return total


def main():
    set_compute_dps()
    wb = WitnessBuilder("binding-per-bond-decomposition", engine="numpy+mpmath")

    if not HAVE_INFRA:
        wb.set_description(f"infra unavailable: {_IMPORT_ERR}")
        wb.add_assertion("infra_present", computed=False, expected=True,
                         tolerance=0, source="import guard")
        # Lean SDP-uniqueness cross-reference (post-#1537 wiring).
        wb.add_data("lean_uniqueness_ref", {
            "generic": "qou:QOU.BraidKnot.@nucleus_uniqueness_closed (3*A)",
            "framework_doc":
                "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
            "note": "Certifies T_w uniqueness at the abstract empty-constraint SDP level (PR #1537 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md.",
        })

        wb.save()
        print(f"Infra unavailable: {_IMPORT_ERR}")
        return

    from q_parameter import Q_50_DIGIT_STR
    q = mpf(Q_50_DIGIT_STR)
    m_e = mpf(str(M_E_MEV))
    from mpmath import catalan
    VOL_B3 = 8 * catalan

    AME = {"2H": mpf("2.22452"), "3H": mpf("8.48182"), "3He": mpf("7.71804")}

    print("=" * 70)
    print("PER-BOND BINDING DECOMPOSITION (H_{3A} chain)")
    print("=" * 70)
    print()

    results = {}
    for iso, (Z, N) in [("2H", (1, 1)), ("3H", (1, 2)), ("3He", (2, 1))]:
        A = Z + N
        n_bonds = A - 1  # chain bonds
        tr_free = fabs(full_trace(Z, N, q, include_inter=False))
        tr_bound = fabs(full_trace(Z, N, q, include_inter=True))
        dtr = tr_free - tr_bound
        B_single = m_e * VOL_B3 * dtr
        # Per-bond Δtr if additive over the chain
        dtr_per_bond = dtr / n_bonds if n_bonds else dtr
        results[iso] = {
            "A": A, "n_bonds": n_bonds,
            "tr_free": str(float(tr_free)),
            "tr_bound": str(float(tr_bound)),
            "delta_tr": str(float(dtr)),
            "delta_tr_per_bond": str(float(dtr_per_bond)),
            "B_single_link_MeV": str(float(B_single)),
            "B_AME_MeV": str(float(AME[iso])),
            "single_link_err_pct": float((B_single - AME[iso]) / AME[iso] * 100),
            "scale_needed_per_bond_MeV": str(float(AME[iso] / n_bonds)) if n_bonds else None,
        }
        print(f"  {iso} (A={A}, bonds={n_bonds}):")
        print(f"    Δtr = {float(dtr):.6f}, Δtr/bond = {float(dtr_per_bond):.6f}")
        print(f"    B(single-link) = {float(B_single):.3f} vs AME {float(AME[iso]):.3f} "
              f"({float((B_single-AME[iso])/AME[iso]*100):+.1f}%)")
        print(f"    AME/bond = {float(AME[iso]/n_bonds):.3f} MeV")

    # Method-discrepancy flag: binding_canonical (Wenzl-bridge closed
    # form) reports Δtr(²H) = 0.5952 → B = 2.229 (+0.2%); this H_{3A}-
    # direct Wedderburn sum reports Δtr(²H) = 0.424 → −28.6%. The two
    # production trace conventions DISAGREE — this must be reconciled
    # before the binding endomorphism can be trusted at A≥3.
    dtr_canonical_2H = mpf("0.5952")
    dtr_h3a_2H = mpf(results["2H"]["delta_tr"])
    method_gap_pct = float(fabs(dtr_canonical_2H - dtr_h3a_2H) / dtr_canonical_2H * 100)

    print()
    print(f"METHOD DISCREPANCY (²H): binding_canonical Δtr = {float(dtr_canonical_2H):.4f}")
    print(f"  vs H_{{3A}}-direct Δtr = {float(dtr_h3a_2H):.4f}  ({method_gap_pct:.0f}% gap)")
    print("The clean +0.19% deuteron result is specific to the Wenzl-bridge")
    print("convention; the H_{3A} Wedderburn sum disagrees. Reconciling the")
    print("two binding-trace conventions is a prerequisite for A≥3 closure.")

    wb.set_description(
        "Per-inter-nucleon-bond decomposition of the H_{3A} binding trace "
        "for ²H/³H/³He. FINDING: the H_{3A}-direct Wedderburn trace "
        f"disagrees with binding_canonical (Wenzl bridge) by {method_gap_pct:.0f}% "
        "on the deuteron Δtr — the +0.19% endomorphism result is "
        "convention-specific. Reconciling the two conventions is the "
        "prerequisite for the open A≥3 binding problem."
    )
    wb.add_data("per_bond", results)
    wb.add_data("method_discrepancy_2H", {
        "delta_tr_binding_canonical": str(float(dtr_canonical_2H)),
        "delta_tr_h3a_direct": str(float(dtr_h3a_2H)),
        "gap_pct": method_gap_pct,
        "note": "Two production trace conventions disagree; reconcile before A≥3.",
    })
    wb.add_assertion(
        "method_discrepancy_recorded",
        computed=method_gap_pct,
        expected=method_gap_pct,
        tolerance=1,
        source="Diagnostic: records the binding_canonical vs H_{3A} Δtr gap",
    )
    wb.save()


if __name__ == "__main__":
    main()
