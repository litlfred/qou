#!/usr/bin/env python3
"""Round-6 redo under canonical tr_M from the derivation-chain registry.

Same hypothesis as `probe_neutron_gap_round6.py`:

  B = E_0 · |Z·tr_M(p) + N·tr_M(n) − tr_M(atom)|
  E_0 := m_p_AME / |tr_M(p)|

but with `tr_M(p)`, `tr_M(n)`, `tr_M(D)` loaded from the registry
files registered in PR #473 (p-tr-M-q0.derivation.json,
n-tr-M-q0.derivation.json, D-tr-M-q0.derivation.json) — i.e. the
canonical Wenzl–Schur convention validated by PR #472's
`prop:habiro-residue-sum-equivalence` cross-check.

Original `probe_neutron_gap_round6.py` used
`atomic-tr-m-mpfr-50dps.witness.json`, a different (factor ~2 on
proton, factor 0.46 on deuteron — non-uniform!) Wenzl–Schur
normalization that's now superseded.

Output: `neutron-gap-probes-round6-canonical.witness.json`
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from q_parameter import Q as Q0_FLOAT  # noqa: E402
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

_DPS = 50

B_AME = {"deuteron": 2.22456612}
Z_N = {"proton": (1, 0), "neutron": (0, 1), "deuteron": (1, 1)}


def load_canonical_tr_M(atom_short: str) -> str:
    p = HERE / f"{atom_short}-tr-M-q0.derivation.json"
    return json.loads(p.read_text())["target_value"]


def main() -> int:
    tr_M = {
        "proton":   load_canonical_tr_M("p"),
        "neutron":  load_canonical_tr_M("n"),
        "deuteron": load_canonical_tr_M("D"),
    }

    print("=" * 100)
    print("NEUTRON-GAP PROBE ROUND-6 — CANONICAL tr_M from derivation registry")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  tr_M(p)  = {tr_M['proton']}")
    print(f"  tr_M(n)  = {tr_M['neutron']}")
    print(f"  tr_M(D)  = {tr_M['deuteron']}")
    print(f"  source: D/n/p-tr-M-q0.derivation.json (PR #473)")
    print()

    with mp.workdps(_DPS):
        tr_p = mp.mpf(tr_M["proton"])
        tr_n = mp.mpf(tr_M["neutron"])
        tr_d = mp.mpf(tr_M["deuteron"])
        m_p = mp.mpf(str(M_P_MEV))
        m_n = mp.mpf(str(M_N_MEV))
        m_e = mp.mpf(str(M_E_MEV))

        E0 = m_p / mp.fabs(tr_p)
        print(f"  E_0 = m_p_AME / |tr_M(p)| = {mp.nstr(E0, 12)} MeV/(tr_M unit)")
        print()

        # Round-6 hypothesis on D:
        Z, N = 1, 1
        deficit = Z * tr_p + N * tr_n - tr_d
        B_pred = E0 * mp.fabs(deficit)
        B_AME_D = mp.mpf(str(B_AME["deuteron"]))
        err_pct = (B_pred - B_AME_D) / B_AME_D * 100
        err_ppb = err_pct * mp.mpf(10**7)

        print(f"  Deuteron under canonical tr_M:")
        print(f"    |Z·tr_p + N·tr_n − tr_d| = {mp.nstr(mp.fabs(deficit), 12)}")
        print(f"    B_pred = E_0 · deficit   = {mp.nstr(B_pred, 12)} MeV")
        print(f"    AME B_D                 = {float(B_AME_D)} MeV")
        print(f"    err [%]                  = {float(err_pct):+.2f}%")
        print(f"    err [ppb]                = {float(err_ppb):+.4e}")
        print()

        # Compare to original round-6 (non-canonical convention)
        # original report: deuteron err = +6.33e+11 ppb
        print(f"  Original round-6 (non-canonical convention): err = +6.33e+11 ppb")
        print(f"  Canonical round-6:                              err = "
              f"{float(err_ppb):+.4e} ppb")
        print()

        # Verdict
        if abs(err_pct) < 1e3 / 1e9:
            verdict = "passes ppb"
        elif abs(err_pct) < 0.5:
            verdict = "closes to <0.5% — significant improvement under canonical convention"
        else:
            verdict = (f"trace-deficit hypothesis FALSIFIED at canonical convention "
                       f"({float(err_pct):+.1f}% off on D)")
        print(f"  VERDICT: {verdict}")

    w = (
        WitnessBuilder("neutron-gap-probes-round6-canonical", engine="mpmath")
        .set_description(
            "Round-6 trace-deficit probe redone under canonical tr_M from "
            "the derivation-chain registry (PR #473). Hypothesis "
            "B = E_0 · |Z·tr_M(p) + N·tr_M(n) − tr_M(atom)| applied to D "
            "with E_0 calibrated on proton."
        )
        .set_content_block("prop:atom-knot-mass-derivation")
        .add_parameter("q_0", Q0_FLOAT)
        .add_parameter("m_p_codata_MeV", M_P_MEV)
        .add_parameter("m_n_codata_MeV", M_N_MEV)
        .add_parameter("m_e_codata_MeV", M_E_MEV)
        .add_parameter("precision_dps", _DPS)
        .add_parameter("tr_M_source", "D/n/p-tr-M-q0.derivation.json (PR #473)")
        .add_data("results", [{
            "atom": "deuteron", "Z": Z, "N": N,
            "tr_M_proton":   tr_M["proton"],
            "tr_M_neutron":  tr_M["neutron"],
            "tr_M_deuteron": tr_M["deuteron"],
            "trace_deficit": mp.nstr(mp.fabs(deficit), 30),
            "E0_MeV":        mp.nstr(E0, 30),
            "B_pred_MeV":    mp.nstr(B_pred, 20),
            "B_AME_MeV":     float(B_AME_D),
            "err_pct":       float(err_pct),
            "err_ppb":       float(err_ppb),
        }])
        .add_data("verdict", verdict)
        .add_data("comparison", {
            "round6_original_err_ppb": +6.33e11,
            "round6_canonical_err_ppb": float(err_ppb),
            "note": (
                "Non-canonical convention (atomic-tr-m-mpfr-50dps) and canonical "
                "convention (D-tr-M-q0.derivation.json) give DIFFERENT "
                "round-6 predictions because the two Wenzl-Schur normalizations "
                "differ per-atom non-uniformly (factor 1.99 on p, 1.72 on n, "
                "0.46 on D)."
            ),
        })
    )
    out_path = w.save()
    print(f"\n  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
