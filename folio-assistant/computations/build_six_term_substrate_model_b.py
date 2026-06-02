#!/usr/bin/env python3
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

Six-term substrate-only predictor on Model B (SDP-canonical) T1.

Per `docs/coordination/six-term-mass-pipeline.md`, migrating the
canonical mass-formula pipeline to **default Model B**.

Calibration discipline (STRICT):
  - CAL-1: m_e (input)
  - CAL-2: q_0 (input via m_μ/m_e)
  - CAL-3: Q_β(n) (input)
  - E_0:   = m_e / (q_0 · (q_0 - 1)) ≈ 4.186 MeV (Convention A,
           pure CAL-1 + CAL-2; NO proton-anchor back-fit)

T1 source: Model B SDP-canonical low-strand braid words from
  `probe-sdp-canonical-paper-formula.witness.json`.

Strand count `n_canon` for each isotope comes from Model B's canonical
braid (not Model A's `3A`).  This drives:
  - T2 = (n_canon - 1) · z²    (R-side bare, Path 1)
  - T3 = C(n_canon - 1, 2) · z⁴
  - T4 = m_e · Σ_{λ ⊢ n_canon} 1/dim_q(λ)

T5 chirality factor a_K from knot type (D, T, ⁴He explicit; p, n via
free-baryon proxy β_Bor with a_K = 1; ³He inherits T's a_K).

T6 = 0 (open R&D — Habiro residue witness not yet generated).

Output: build-six-term-substrate-model-b.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import sys
import json
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
import mpmath as mp

set_compute_dps()

from paper_six_term_isotope_sweep import (  # noqa: E402
    Q0,
    Z_MARK,
)
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402  # CAL-1


# Substrate E_0 (Convention A: pure CAL-1 + CAL-2; NO calibration)
E0_SUBSTRATE_MEV = mp.mpf(M_E_MEV) / (Q0 * (Q0 - mp.mpf(1)))


# Model B canonical-braid registry (extends the SDP witness with
# proxy free-baryon entries via β_Bor on B_3 = canonical Borromean).
# n_canon = strand count of the canonical braid (NOT 3A).
# ρ = topological prefactor from joint-tower-sdp-h6-h9.witness.json
#     (where defined) or 1 for the free-baryon proxy.
#
# Tentative: p and n share the bare β_Bor as a free-baryon proxy.
# Orientation-partition distinction (uud vs udd) is in the Skein
# corrections (T5/T6), not the topological |τ_M|.
MODEL_B_BRAID_REGISTRY = {
    # (Z, N) → (n_canon, ρ, knot_name, t1 source)
    # At A=1, Model A and Model B converge (both use B_3 with 11 typed
    # crossings); use Model A registry value via t1_atom_a.
    (1, 0): {"n_canon": 3, "rho": 1,
             "knot": "11-cross typed B_3 (uud)", "t1_atom_a": "proton"},
    (0, 1): {"n_canon": 3, "rho": 1,
             "knot": "11-cross typed B_3 (udd)", "t1_atom_a": "neutron"},
    (1, 1): {"n_canon": 3, "rho": 1, "knot": "6_2",  "t1_atom": "deuteron"},
    (1, 2): {"n_canon": 5, "rho": 2, "knot": "8_11", "t1_atom": "tritium"},
    (2, 1): {"n_canon": 3, "rho": 2, "knot": "L6a4", "t1_atom": "he3"},
    (2, 2): {"n_canon": None, "rho": None,
             "knot": "open (no Model B low-strand)", "t1": None},
}


def _load_model_b_t1() -> dict[str, mp.mpf]:
    """Atom-name → |τ_M(canonical-knot)| at q_0 (Wenzl-Schur) from
    `probe-sdp-canonical-paper-formula.witness.json`."""
    path = _pb.witness_path("probe-sdp-canonical-paper-formula.witness.json", HERE)
    if not path.exists():
        raise FileNotFoundError(
            f"Model B T1 witness missing: {path}.  Run "
            f"probe_sdp_canonical_paper_formula.py first."
        )
    d = json.loads(path.read_text())
    out: dict[str, mp.mpf] = {}
    for atom_name, atom_data in d.get("data", {}).get("results", {}).items():
        out[atom_name] = mp.mpf(str(atom_data["tr_M_wenzl_schur"]))
    return out


# CODATA masses (MeV) for the comparison column.
_CODATA = {
    (1, 0):   mp.mpf("938.27208816"),    # proton
    (0, 1):   mp.mpf("939.56542052"),    # neutron
    (1, 1):   mp.mpf("1875.61294257"),   # deuteron
    (1, 2):   mp.mpf("2808.92113298"),   # tritium
    (2, 1):   mp.mpf("2808.39160743"),   # he3
    (2, 2):   mp.mpf("3727.37941"),      # he4
}
_LABEL = {
    (1, 0): "p", (0, 1): "n",
    (1, 1): "D", (1, 2): "T",
    (2, 1): "³He", (2, 2): "⁴He",
}

# Chirality factors a_K per paper figure-eight BW coefficients.
# h = q - q^{-1} at q_0.
_H = Q0 - mp.mpf(1) / Q0
_A_K = {
    (1, 0):  mp.mpf(1),                          # free baryon (proxy)
    (0, 1):  mp.mpf(1),                          # free baryon (proxy)
    (1, 1):  mp.mpf(1) + _H,                     # D: 1 + h
    (1, 2):  mp.mpf(1) - _H ** 2,                # T: 1 - h²
    (2, 1):  mp.mpf(1) - _H ** 2,                # ³He: mirror of T
    (2, 2):  (mp.mpf(1) - _H ** 2) ** 2,         # ⁴He: (1 - h²)²
}


def six_term_model_b(Z: int, N: int, t1: mp.mpf, *,
                     n_canon: int, rho: int) -> dict:
    """Compute the six-term mass formula on Model B braids.

    All term-by-term outputs in Hecke units (multiplied by m_e for T4
    and by E_0 for T1, T2, T3 to get MeV at the final assembly).
    """
    # T1 — descended |τ_M|
    t1_val = mp.fabs(t1)

    # T2, T3 — R-side bare (Markov-invariant; uses n_canon)
    n_gens = n_canon - 1
    t2 = n_gens * Z_MARK ** 2
    t3 = comb(n_gens, 2) * Z_MARK ** 4

    # T4 — Frobenius co-Casimir per-n_canon (algebraic form)
    #   Σ_{λ ⊢ n_canon} 1/dim_q(λ)
    # term4_frobenius_codim expects atom-A (= n/3); pass the
    # equivalent for n_canon.  For non-multiple-of-3 n_canon we
    # compute directly using hecke_characters helpers.
    from hecke_characters import partitions_of, dim_q  # noqa: E402
    t4_raw = sum(mp.mpf(1) / mp.mpf(str(dim_q(lam)))
                 for lam in partitions_of(n_canon))
    t4 = mp.mpf(M_E_MEV) * t4_raw

    # T5 — chirality multiplicative on T1
    a_K = _A_K.get((Z, N), mp.mpf(1))
    t5_hecke = (a_K - mp.mpf(1)) * t1_val

    # T6 — open R&D
    t6_MeV = mp.mpf(0)

    # Total Hecke-units (T1 + T2 + T3 + T5); ρ multiplies T1 piece
    # per paper convention.  Apply ρ to t1_val only.
    total_hecke = rho * t1_val + t2 + t3 + t5_hecke

    return {
        "t1": t1_val,
        "t2": t2,
        "t3": t3,
        "t4_MeV": t4,
        "t5_hecke": t5_hecke,
        "t6_MeV": t6_MeV,
        "rho": rho,
        "total_hecke": total_hecke,
        "a_K": a_K,
    }


def main() -> int:
    print("=" * 100)
    print("Six-term substrate predictor — Default Model B (SDP-canonical)")
    print("=" * 100)
    print(f"  q_0     = {mp.nstr(Q0, 20)}")
    print(f"  m_e     = {mp.nstr(M_E_MEV, 8)} MeV (CAL-1)")
    print(f"  E_0     = m_e / (q_0 · (q_0 - 1)) = "
          f"{mp.nstr(E0_SUBSTRATE_MEV, 8)} MeV (Convention A, substrate)")
    print()

    t1_atoms = _load_model_b_t1()

    print(f"  {'iso':>4}  {'(Z,N)':>6}  {'n_can':>5}  {'ρ':>2}  "
          f"{'knot':>14}  {'|τ_M|':>12}  "
          f"{'M_pred_B (MeV)':>16}  {'M_CODATA (MeV)':>16}  {'err':>10}")
    print("  " + "-" * 116)

    results = []
    for (Z, N), info in MODEL_B_BRAID_REGISTRY.items():
        iso = _LABEL[(Z, N)]
        codata = _CODATA[(Z, N)]
        knot = info["knot"]
        n_canon = info.get("n_canon")
        rho = info.get("rho")

        if rho is None or n_canon is None:
            # No Model B braid yet (e.g., ⁴He)
            print(f"  {iso:>4}  {f'({Z},{N})':>6}  {'—':>5}  "
                  f"{'—':>2}  {knot:>26}  "
                  f"{'—':>12}  "
                  f"{'—':>16}  {float(codata):>16.4f}  {'(open)':>10}")
            results.append({
                "isotope": iso, "Z": Z, "N": N,
                "knot": knot, "M_codata_MeV": str(codata),
                "status": "model_b_braid_open",
            })
            continue

        # T1: from probe witness OR Model A registry (for p, n)
        if "t1_atom" in info:
            t1 = t1_atoms[info["t1_atom"]]
        elif "t1_atom_a" in info:
            # At A=1, Model A == Model B (both use B_3 with 11 typed
            # crossings).  Use Model A 50-dps registry.
            # Explicit label → key map (per Copilot review on PR #640,
            # line 220: avoid the brittle [0] slice).
            _A_TO_REGISTRY_KEY = {"proton": "p", "neutron": "n"}
            from derivation_chain import TR_M_AT_Q0_50DPS
            t1 = mp.mpf(TR_M_AT_Q0_50DPS[_A_TO_REGISTRY_KEY[info["t1_atom_a"]]])
        else:
            t1 = None
        if t1 is None:
            # No Model B braid (e.g., ⁴He)
            print(f"  {iso:>4}  {f'({Z},{N})':>6}  {'—':>5}  "
                  f"{'—':>2}  {knot:>26}  "
                  f"{'—':>12}  "
                  f"{'—':>16}  {float(codata):>16.4f}  {'(open)':>10}")
            results.append({
                "isotope": iso, "Z": Z, "N": N,
                "knot": knot, "M_codata_MeV": str(codata),
                "status": "model_b_braid_open",
            })
            continue

        six = six_term_model_b(Z, N, t1, n_canon=n_canon, rho=rho)

        # Total MeV: E_0 · (T1 + T2 + T3 + T5) + T4 + T6
        M_pred = E0_SUBSTRATE_MEV * six["total_hecke"] + six["t4_MeV"] + six["t6_MeV"]
        err = (M_pred - codata) / codata * 100

        print(f"  {iso:>4}  {f'({Z},{N})':>6}  {n_canon:>5}  {rho:>2}  "
              f"{knot:>14}  {mp.nstr(t1, 8):>12}  "
              f"{float(M_pred):>16.4f}  {float(codata):>16.4f}  "
              f"{float(err):>+9.3f}%")

        results.append({
            "isotope": iso, "Z": Z, "N": N,
            "n_canon": n_canon, "knot": knot, "rho": rho,
            "t1": mp.nstr(t1, 20),
            "t2_hecke": mp.nstr(six["t2"], 20),
            "t3_hecke": mp.nstr(six["t3"], 20),
            "t4_MeV": mp.nstr(six["t4_MeV"], 20),
            "t5_hecke": mp.nstr(six["t5_hecke"], 20),
            "t6_MeV": mp.nstr(six["t6_MeV"], 20),
            "a_K": mp.nstr(six["a_K"], 20),
            "total_hecke": mp.nstr(six["total_hecke"], 20),
            "M_pred_MeV": mp.nstr(M_pred, 20),
            "M_codata_MeV": mp.nstr(codata, 20),
            "err_pct": mp.nstr(err, 12),
        })

    print()
    print("  Mode: r-side-bare (Path 1; Markov-invariant T2, T3)")
    print("  E_0:  substrate Convention A (CAL-1 + CAL-2 only; no proton anchor)")
    print("  T4:   Frobenius co-Casimir per n_canon (Model B canonical braid)")
    print("  T5:   (a_K - 1) · T1, chirality multiplicative on T1")
    print("  T6:   0 (open R&D; Habiro residue witness not yet generated)")
    print()
    print("  Notes:")
    print("    - p, n use the 11-crossing typed B_3 braid (Wenzl-bridge τ_M);")
    print("      at A=1 Model A and Model B converge.")
    print("    - ⁴He Model B canonical low-strand knot is open (the existing")
    print("      12-strand atomic-braid-recipe-4he is Model A 3A-encoding).")
    print("    - NO calibration to CODATA m_p (substrate E_0 only).")
    print()

    w = (
        WitnessBuilder("build-six-term-substrate-model-b", engine="mpmath")
        .set_description(
            "Six-term substrate-only mass predictor on Model B (SDP-canonical "
            "low-strand) braids with substrate E_0 (Convention A: CAL-1 + CAL-2 "
            "only, NO proton-anchor back-fit). Per-term breakdown for "
            "p, n, D, T, ³He, ⁴He using Model B's canonical-knot strand count "
            "n_canon (not Model A's 3A) for T2, T3, T4."
        )
        .set_content_block("thm:knot-mass-formula-unified")
        .set_audit_only(
            "docs/coordination/six-term-mass-pipeline.md (migration to default "
            "Model B); docs/audits/2026-05-11-model-b-mass-table.md"
        )
        .add_parameter("q_0", mp.nstr(Q0, 50))
        .add_parameter("m_e_MeV", mp.nstr(mp.mpf(M_E_MEV), 20))
        .add_parameter("E_0_MeV_substrate", mp.nstr(E0_SUBSTRATE_MEV, 20))
        .add_parameter("tower_mode", "r-side-bare")
        .add_parameter("calibration", "substrate Convention A (no CODATA back-fit)")
        .add_data("results", results)
    )
    # Lean SDP-uniqueness cross-reference (post-#1537 wiring).
    w.add_data("lean_uniqueness_ref", {
        "generic": "qou:QOU.BraidKnot.@nucleus_uniqueness_closed (3*A)",
        "framework_doc":
            "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
        "note": "Certifies T_w uniqueness at the abstract empty-constraint SDP level (PR #1537 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md.",
    })

    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
