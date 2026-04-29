#!/usr/bin/env python3
"""Round-6 trace-deficit hypothesis under canonical τ_M (Wenzl-bridge).

The "trace-deficit" hypothesis (round-6, originally tested with
the τ_SW-mislabeled registry values) is:

    B_atom = E_0 · |Z · τ(p) + N · τ(n) − τ(atom)|
    E_0    := m_p_AME / |τ(p)|     (proton calibration)

Originally evaluated in `probe_neutron_gap_round6_canonical.py` using
`*-tr-M-q0.derivation.json` registry values (= τ_SW per pr-442's
selection theorem). This probe re-evaluates the same hypothesis
under the canonical τ_M (Wenzl-bridge / Markov-axiom-derived)
loaded from `atomic-tr-m-wenzl-bridge.witness.json`.

Two prefactor variants:
  E_0 = m_p_AME / τ_M(p)     (proton calibration — "binding from mass")
  E_0 = m_e                  (mass-derivation natural scale)

Output: `round6-tau-M-canonical.witness.json`
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from q_parameter import Q as Q0_FLOAT  # noqa: E402
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

_DPS = 50

B_AME = {"deuteron": 2.22456612, "tritium": 8.4817984, "helium-3": 7.7180375}
ZN = {"deuteron": (1, 1), "tritium": (1, 2), "helium-3": (2, 1)}


def load_wenzl_bridge_tau_M():
    """Canonical τ_M values from atomic-tr-m-wenzl-bridge.witness.json
    (Wenzl-bridge / Markov-axiom-derived, non-degenerate per pr-442).

    NOTE: per `probe_wenzl_bridge_witness_audit.py`, the witness's
    proton, neutron, and ³He entries all share bit-exact 0.998366751
    — a witness-generation bug (per-atom Tr(ρ_λ) shows the same
    (1, 1.994, 1) breakdown for all three, suggesting the
    dump-block-matrices Rust binary used a single-nucleon trivial
    braid for all three atoms). The deuteron and tritium entries
    are correct.

    For the round-6 hypothesis (which needs τ_M(p), τ_M(n), τ_M(atom)),
    we OVERRIDE the buggy proton/neutron entries with direct-
    computation values from the audit:
      τ_M(p free, 3-strand)  = +1.733851
      τ_M(n free, 3-strand)  = +1.405980
    """
    w = json.loads((HERE / "atomic-tr-m-wenzl-bridge.witness.json").read_text())
    label_map = {
        "proton": "proton",
        "neutron": "neutron",
        "deuteron-2H": "deuteron",
        "tritium-3H": "tritium",
        "helium3-3He": "helium-3",
    }
    out = {}
    for r in w["results"]:
        if r["atom"] in label_map:
            out[label_map[r["atom"]]] = r["tr_M_mixed_precision"]

    # Override buggy entries with audit-corrected values
    audit_path = HERE / "wenzl-bridge-witness-audit.witness.json"
    if audit_path.exists():
        audit = json.loads(audit_path.read_text())
        findings = audit.get("data", {}).get("findings", {})
        if "tau_M_p_direct" in findings:
            out["proton"]  = str(findings["tau_M_p_direct"])
        if "tau_M_n_direct" in findings:
            out["neutron"] = str(findings["tau_M_n_direct"])
    return out


def load_tau_SW_registry():
    out = {}
    for s, lbl in [("p", "proton"), ("n", "neutron"), ("D", "deuteron")]:
        out[lbl] = json.loads((HERE / f"{s}-tr-M-q0.derivation.json").read_text())["target_value"]
    return out


def main() -> int:
    tau_M  = load_wenzl_bridge_tau_M()
    tau_SW = load_tau_SW_registry()

    print("=" * 100)
    print("ROUND-6 TRACE-DEFICIT — CANONICAL τ_M (Wenzl-bridge)")
    print("=" * 100)
    print()
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  τ_M source: atomic-tr-m-wenzl-bridge.witness.json (Wenzl-bridge y_λ)")
    print(f"  Canonical τ_M values:")
    for lbl in ["proton", "neutron", "deuteron", "tritium", "helium-3"]:
        v = tau_M.get(lbl)
        print(f"    {lbl:<10} = {v}")
    print()

    with mp.workdps(_DPS):
        tau = {k: mp.mpf(str(v)) for k, v in tau_M.items()}
        m_p = mp.mpf(str(M_P_MEV))
        m_e = mp.mpf(str(M_E_MEV))

        E0_proton_cal  = m_p / mp.fabs(tau["proton"])
        E0_electron    = m_e

        print(f"  E_0 (proton calibration) = m_p / |τ_M(p)| = "
              f"{mp.nstr(E0_proton_cal, 10)} MeV/(τ-unit)")
        print(f"  E_0 (electron natural)   = m_e             = "
              f"{mp.nstr(E0_electron, 10)} MeV/(τ-unit)")
        print()

        results = []
        print(f"  {'atom':<10} {'Z':>2} {'N':>2} {'deficit':>10} "
              f"{'B(prot.cal)':>13} {'err %':>10} "
              f"{'B(m_e)':>10} {'err %':>10} {'AME':>8}")
        print("  " + "-" * 90)

        # Atoms whose τ_M(atom) is verified (D and T match the from-scratch
        # chain bit-exactly). ³He's witness entry shares the buggy 0.998…
        # value with the buggy proton/neutron entries and would require an
        # H_8 Wenzl-bridge computation to verify; skip until that lands.
        VERIFIED_ATOMS = {"deuteron", "tritium"}
        UNVERIFIED_ATOMS = {"helium-3"}

        for label in ["deuteron", "tritium", "helium-3"]:
            Z, N = ZN[label]
            verified = label in VERIFIED_ATOMS
            if not verified:
                print(f"  {label:<10} {Z:>2} {N:>2} "
                      f"  SKIPPED — τ_M({label}) entry in the wenzl-bridge "
                      f"witness is suspect (audit) and no verified value "
                      f"available (needs H_8).")
                results.append({
                    "atom": label, "Z": Z, "N": N,
                    "skipped": True,
                    "reason": ("τ_M(atom) entry in wenzl-bridge witness is "
                               "suspect per probe_wenzl_bridge_witness_audit "
                               "(shares bit-exact value with buggy p, n "
                               "entries); needs H_8 Wenzl-bridge computation "
                               "to verify."),
                    "B_AME_MeV": B_AME[label],
                })
                continue
            deficit = mp.fabs(Z * tau["proton"] + N * tau["neutron"] - tau[label])
            B_proton_cal = E0_proton_cal * deficit
            B_electron   = E0_electron * deficit
            ame = B_AME[label]
            err_p = (float(B_proton_cal) - ame) / ame * 100
            err_e = (float(B_electron)   - ame) / ame * 100
            print(f"  {label:<10} {Z:>2} {N:>2} {float(deficit):>10.6f} "
                  f"{float(B_proton_cal):>13.4f} {err_p:>+10.2f} "
                  f"{float(B_electron):>10.6f} {err_e:>+10.2f} "
                  f"{ame:>8.4f}")
            results.append({
                "atom": label, "Z": Z, "N": N,
                "tau_M_p": str(tau["proton"]),
                "tau_M_n": str(tau["neutron"]),
                "tau_M_atom": str(tau[label]),
                "deficit_canonical": mp.nstr(deficit, 30),
                "E0_proton_calibration_MeV": mp.nstr(E0_proton_cal, 30),
                "B_pred_proton_calibration_MeV": mp.nstr(B_proton_cal, 20),
                "B_pred_electron_MeV": mp.nstr(B_electron, 20),
                "B_AME_MeV": ame,
                "err_pct_proton_calibration": err_p,
                "err_pct_electron": err_e,
            })
        print()

        # Side-by-side with τ_SW for D
        Z, N = ZN["deuteron"]
        tau_p_SW = mp.mpf(str(tau_SW["proton"]))
        tau_n_SW = mp.mpf(str(tau_SW["neutron"]))
        tau_D_SW = mp.mpf(str(tau_SW["deuteron"]))
        deficit_SW = mp.fabs(Z * tau_p_SW + N * tau_n_SW - tau_D_SW)
        E0_p_SW = m_p / mp.fabs(tau_p_SW)
        B_SW = E0_p_SW * deficit_SW
        err_SW = (float(B_SW) - B_AME["deuteron"]) / B_AME["deuteron"] * 100
        print(f"  Side-by-side comparison for D:")
        print(f"    τ_M (canonical) deficit  = {float(results[0]['deficit_canonical']):.6f}, "
              f"B(prot.cal) = {float(results[0]['B_pred_proton_calibration_MeV']):.2f}, "
              f"err = {results[0]['err_pct_proton_calibration']:+.2f}%")
        print(f"    τ_SW (registry)  deficit = {float(deficit_SW):.6f}, "
              f"B(prot.cal) = {float(B_SW):.2f}, "
              f"err = {err_SW:+.2f}%")
        print()

        # Verdict
        verified_results = [r for r in results if not r.get("skipped")]
        best_pct = min(abs(r["err_pct_proton_calibration"]) for r in verified_results)
        if best_pct < 1.0:
            verdict = f"trace-deficit hypothesis CLOSES under τ_M ({best_pct:.2f}%)"
        elif best_pct < 50.0:
            verdict = f"trace-deficit hypothesis closes to {best_pct:.1f}% — significant"
        else:
            verdict = (f"trace-deficit hypothesis FAILS at canonical τ_M "
                       f"(best residual {best_pct:.0f}% — same scale as the τ_SW failure)")
        print(f"  VERDICT: {verdict}")

    w = (
        WitnessBuilder("round6-tau-M-canonical", engine="mpmath")
        .set_description(
            "Round-6 trace-deficit hypothesis B = E_0·|Z·τ(p)+N·τ(n)−τ(atom)| "
            "evaluated under canonical τ_M (Wenzl-bridge / Markov-axiom) per "
            "pr-442's selection theorem. Predecessor `probe_neutron_gap_"
            "round6_canonical.py` used τ_SW from the mislabeled registry. "
            "Two prefactor variants: E_0 = m_p_AME/|τ_M(p)| (proton "
            "calibration) and E_0 = m_e (electron natural scale)."
        )
        .add_parameter("q_0", Q0_FLOAT)
        .add_parameter("m_p_AME_MeV", M_P_MEV)
        .add_parameter("m_n_AME_MeV", M_N_MEV)
        .add_parameter("m_e_codata_MeV", M_E_MEV)
        .add_parameter("precision_dps", _DPS)
        .add_parameter("tau_M_source", "atomic-tr-m-wenzl-bridge.witness.json")
        .add_parameter("selection_theorem_ref", "prop:markov-trace-frobenius-selection (commit 25a204e)")
        .add_data("results", results)
        .add_data("D_comparison_tau_SW", {
            "tau_p_SW": str(tau_p_SW),
            "tau_n_SW": str(tau_n_SW),
            "tau_D_SW": str(tau_D_SW),
            "deficit_SW": mp.nstr(deficit_SW, 30),
            "B_pred_proton_calibration_SW": mp.nstr(B_SW, 20),
            "err_pct_SW": err_SW,
            "note": "τ_SW (registry) values were mislabeled as 'tr_M' — see "
                    "prop:markov-trace-frobenius-selection. The QOU mass formula's "
                    "Frobenius co-Casimir requires non-degeneracy, ruling out τ_SW.",
        })
        .add_data("verdict", verdict)
    )
    out_path = w.save()
    print(f"\n  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
