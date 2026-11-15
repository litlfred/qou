#!/usr/bin/env python3
"""ρ_binding constancy test — is α_M a forced single calibration?

Path-3 (Habiro) binding model: B = α_M · |tr_M(T_w)|, with α_M calibrated from
the deuteron. The formalize-first question (PR #2849, synthesis doc §Item 3):
is α_M = m_e · ρ_binding a FORCED single constant, or a per-atom fit?

The scale-free (derivable) content is the RATIO B_obs / |tr_M| — α_M cancels.
If α_M is genuinely one universal calibration, this ratio is CONSTANT across
atoms. The decisive discriminator is the T / ³He mirror pair (same n=9, same
|tr_M| up to the p/n braid asymmetry) against their different B_obs.

tr_M(β_atomic(Z,N)) = Σ_{λ⊢3A} y_λ(q0)·χ^λ_q(β) via the canonical Markov-axiom
reducer (global_wedderburn_sum_q_hecke_seminormal). No fit; scale cancels.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "substrate"))

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()  # raise dps BEFORE Q0 and the constants below are built
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

from wedderburn_jones_markov import global_wedderburn_sum_q_hecke_seminormal  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION

# q0 read BY NAME (bean qou-9ugp, 2026-09-03) and carried as mpf, not float.
# It was the bare float64 literal 1.10997859555733471 -- the RETIRED
# self-certified muon pin A, superseded 2026-08-22. No comparison leg here,
# so the 2026-08-30 owner ruling puts it on the proton default (11.54 ppb).
# The old comment said the scale cancels in the ratio; that is an argument
# about the RATIO, not a licence to feed a float64 into the Wedderburn sum.
Q0 = mp.mpf(Q_50_DIGIT_STR)

# AME2020 binding energies (MeV).
B_OBS = {
    "D":   (1, 1, AME_B_DEUTERON_MEV_VALIDATION),
    "T":   (1, 2, 8.481821),
    "He3": (2, 1, 7.718058),
}


def main() -> int:
    print(f"ρ_binding constancy test  (q0 = {Q0})")
    print(f"{'atom':6s} {'Z,N':6s} {'|tr_M|':>14s} {'B_obs':>12s} "
          f"{'B_obs/|tr_M|':>16s}")
    print("-" * 60)
    ratios = {}
    for atom, (Z, N, B) in B_OBS.items():
        trM, _rows = global_wedderburn_sum_q_hecke_seminormal(
            Z, N, q_val=Q0, include_inter=True)
        r = B / abs(trM)
        ratios[atom] = r
        print(f"{atom:6s} ({Z},{N})  {abs(trM):14.6f} {B:12.6f} {r:16.4f}")
    print("-" * 60)
    vals = list(ratios.values())
    spread = (max(vals) - min(vals)) / (sum(vals) / len(vals))
    print(f"B_obs/|tr_M| relative spread = {spread*100:.2f}%  "
          f"(0% ⇒ α_M is one forced constant; large ⇒ per-atom fit)")
    # mirror discriminator
    mr = None
    if "T" in ratios and "He3" in ratios:
        mr = abs(ratios["T"] - ratios["He3"]) / (
            (ratios["T"] + ratios["He3"]) / 2)
        print(f"T vs ³He mirror ratio mismatch = {mr*100:.2f}%")
    _emit_witness(ratios, spread, mr)
    return 0


def _emit_witness(ratios, spread, mr):
    import hashlib
    import os as _os
    import subprocess
    import sys as _sys
    _sys.path.insert(0, _os.path.join(HERE, ".."))
    _sys.path.insert(0, _os.path.join(HERE, "..", "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    script = os.path.abspath(__file__)
    try:
        sha = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", script],
            cwd=HERE, text=True).strip()
    except Exception:
        sha = None
    with open(script, "rb") as f:
        script_hash = hashlib.sha256(f.read()).hexdigest()[:12]
    description = ("B_obs/|tr_M| across D,T,³He under the canonical Markov "
                  "trace (include_inter=True). Tests whether the Path-3 "
                  "single-prefactor binding model B=α_M·|tr_M| has a FORCED "
                  "universal α_M (= m_e·ρ_binding, constant). Finding: the "
                  "ratio varies ~182% (D 5.73, T 81.5, ³He 37.4), so α_M is "
                  "NOT a forced constant — the model is a deuteron-anchored "
                  "approximation that fails at A=3. Scope (a): tr_M as an "
                  "ingredient is NOT excluded; only the constant-prefactor "
                  "assumption is refuted. The D ratio 5.728 reproduces the "
                  "published α_M 5.729 (cross-validates the pipeline).")
    data_payload = {
        "name": "rho-binding-constancy",
        "probe": True,
        "substrate": {"q0": Q0, "q0_pin": "muon (computations-layer canonical)"},
        "ratios_B_over_trM": {k: float(v) for k, v in ratios.items()},
        "relative_spread": float(spread),
        "t_he3_mirror_mismatch": (float(mr) if mr is not None else None),
        "witness": {"scriptCommitSha": sha, "scriptHash": script_hash,
                    "producer": "computations/probes/rho_binding_constancy_probe.py"},
    }
    wb = WitnessBuilder.wrap_legacy(
        "rho-binding-constancy", data_payload,
        script_path=__file__, engine="python",
        output_dir=os.path.join(HERE, ".."))
    wb.set_description(description)
    wb.add_assertion("ratios computed for all 3 atoms",
                     computed=int(len(ratios)), expected=3)
    # auditOnly was a bare boolean in the legacy witness; preserve it
    # verbatim (set_audit_only expects a report-path string instead).
    out = wb.save(extra={"auditOnly": True})
    print(f"[witness] wrote {os.path.normpath(str(out))}")


if __name__ == "__main__":
    raise SystemExit(main())
