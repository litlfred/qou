#!/usr/bin/env python3
"""Six-term substrate-only predictor on Model B (SDP-canonical) T1.

Per `docs/coordination/six-term-mass-pipeline.md`, the canonical
substrate-only six-term predictor is `paper_six_term_isotope_sweep.py`
which consumes Model A's T1 values (`atomic_braid_word_3A` via
`markov_peel.tr_M_atomic`).  This script runs the same six-term
machinery but with **Model B T1**: SDP-canonical low-strand braid
words from `probe-sdp-canonical-paper-formula.witness.json`.

Outputs a side-by-side table of:
  T1 (Model A) | T1 (Model B) | M_pred_A | M_pred_B | CODATA | err_A | err_B

Status of T2..T6 input formulas (unchanged from paper_six_term_isotope_sweep):
  T2, T3:  Path 1 "r-side-bare" (Markov-invariant, paper preferred)
  T4:      Frobenius co-Casimir per-3A (algebraic form, derived)
  T5:      multiplicative_on_t1 chirality a_K (derived for D, T, 4He)
  T6:      open R&D (Habiro residue witness not yet generated)

Output witness: build-six-term-substrate-model-b.witness.json
"""
from __future__ import annotations

import sys
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp

mp.mp.dps = 50

from paper_six_term_isotope_sweep import (  # noqa: E402
    paper_six_term_mass,
    canonical_t1 as canonical_t1_model_a,
    Q0,
    Z_MARK,
)
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402  # CAL-1


def _load_model_b_t1() -> dict[str, mp.mpf]:
    """Atom-label → |tr_M(canonical-knot)| at q_0 (Wenzl-Schur).

    Reads from `probe-sdp-canonical-paper-formula.witness.json` which
    contains the Model B SDP-canonical low-strand T1 values.
    """
    path = HERE / "probe-sdp-canonical-paper-formula.witness.json"
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


# Mapping from paper_six_term sweep labels to probe-sdp-canonical labels.
_MODEL_B_NAME = {
    "D": "deuteron",
    "T": "tritium",
    "3He": "he3",
}


# CODATA masses (MeV); proton anchor + Q_β-derived neutron for comparison.
_CODATA = {
    "p":   mp.mpf("938.27208816"),
    "n":   mp.mpf("939.56542052"),
    "D":   mp.mpf("1875.61294257"),
    "T":   mp.mpf("2808.92113298"),
    "3He": mp.mpf("2808.39160743"),
    "4He": mp.mpf("3727.37941"),
}

# (Z, N) per isotope label.
_ISOTOPE_ZN = {
    "p":  (1, 0),
    "n":  (0, 1),
    "D":  (1, 1),
    "T":  (1, 2),
    "3He": (2, 1),
    "4He": (2, 2),
}

# Chirality factors a_K per paper (D, T, 4He explicit; 3He via Borromean ≡ 1).
# h = q - q^{-1} at q_0.
_H_VAL = Q0 - mp.mpf(1) / Q0
_A_K = {
    "D":   mp.mpf(1) + _H_VAL,                  # 1 + h
    "T":   mp.mpf(1) - _H_VAL ** 2,             # 1 - h²
    "3He": mp.mpf(1) - _H_VAL ** 2,             # 1 - h² (mirror of T)
    "4He": (mp.mpf(1) - _H_VAL ** 2) ** 2,      # (1 - h²)²
}


def run_six_term(isotope: str, t1: mp.mpf, *, tower_mode: str = "r-side-bare") -> dict:
    """Run the six-term formula with a specific T1 input.

    Returns a dict with all per-term contributions in Hecke units +
    the calibrated MeV prediction (against the proton-anchor E_0).
    """
    Z, N = _ISOTOPE_ZN[isotope]
    chirality_signs = None  # let the helper compute from knot type
    # paper_six_term_mass already loads T1 via its own canonical_t1();
    # to override, we monkey-patch the canonical_t1 lookup via the
    # caller side: run the six-term with a substituted t1 by wrapping
    # the original.  Here, we bypass and just compute Hecke-unit terms
    # using the public terms helpers.
    from paper_six_term_isotope_sweep import (
        term2_single_gen_tower,
        term3_pair_gen_tower,
        term4_frobenius_codim,
        # term5_chirality below uses signs we pass; for now use a_K alone
    )

    # T1
    t1_val = t1  # |tr_M| (input)

    # T2, T3 — r-side-bare: depends only on n_gens, not the braid
    A = Z + N
    n_gens_total = 3 * A - 1  # include_inter=True
    if tower_mode == "r-side-bare":
        t2 = n_gens_total * Z_MARK ** 2
        t3 = (n_gens_total * (n_gens_total - 1) // 2) * Z_MARK ** 4
    elif tower_mode == "drop":
        t2 = mp.mpf(0)
        t3 = mp.mpf(0)
    else:
        raise ValueError(f"unsupported tower_mode={tower_mode}")

    # T4 — Frobenius co-Casimir per-3A (algebraic form)
    t4_raw = term4_frobenius_codim(A)
    t4 = mp.mpf(M_E_MEV) * t4_raw  # in MeV directly

    # T5 — chirality multiplicative on T1
    a_K = _A_K.get(isotope, mp.mpf(1))
    t5_hecke = (a_K - mp.mpf(1)) * t1_val  # additive deviation

    # T6 — open R&D
    t6_MeV = mp.mpf(0)

    # Total Hecke-units (T1 + T2 + T3 + T5)
    total_hecke = t1_val + t2 + t3 + t5_hecke

    return {
        "isotope": isotope,
        "Z": Z, "N": N,
        "t1": t1_val,
        "t2": t2,
        "t3": t3,
        "t4_MeV": t4,
        "t5_hecke": t5_hecke,
        "t6_MeV": t6_MeV,
        "total_hecke": total_hecke,
        "a_K": a_K,
    }


def calibrate_E0(proton_target_MeV: mp.mpf, proton_six_term: dict) -> mp.mpf:
    """Calibrate E_0 so that the proton six-term sum hits the CODATA mass.

    E_0 = (M_p - T4_p - T6_p) / total_hecke_p   [MeV / Hecke-unit]
    """
    return (proton_target_MeV
            - proton_six_term["t4_MeV"]
            - proton_six_term["t6_MeV"]) / proton_six_term["total_hecke"]


def main() -> int:
    print("=" * 96)
    print("Six-term substrate predictor — Model B (SDP-canonical) T1")
    print("=" * 96)
    print(f"  q_0     = {mp.nstr(Q0, 20)}")
    print(f"  m_e     = {mp.nstr(M_E_MEV, 8)} MeV (CAL-1)")
    print()

    t1_model_b = _load_model_b_t1()
    print(f"  Loaded Model B T1 for: {sorted(t1_model_b)}")
    print()

    # Run six-term for each isotope (Model A and Model B side-by-side)
    # Note: Model B only covers D, T, ³He (the SDP-canonical witness).
    # Falls back to Model A for p, n, ⁴He.
    rows: list[dict] = []
    for iso in ["p", "n", "D", "T", "3He", "4He"]:
        # Model A T1
        try:
            t1_A = canonical_t1_model_a(iso)
        except Exception:
            t1_A = None

        # Model B T1 (only D, T, 3He covered)
        b_name = _MODEL_B_NAME.get(iso)
        t1_B = t1_model_b.get(b_name) if b_name else None

        row = {"isotope": iso, "t1_A": t1_A, "t1_B": t1_B}
        if t1_A is not None:
            row["A_six_term"] = run_six_term(iso, t1_A)
        if t1_B is not None:
            row["B_six_term"] = run_six_term(iso, t1_B)
        rows.append(row)

    # Calibrate E_0 from the proton row (Model A — Model B doesn't have proton)
    E0_A = calibrate_E0(_CODATA["p"], rows[0]["A_six_term"])
    print(f"  E_0 (Model A proton-anchor) = {mp.nstr(E0_A, 8)} MeV/Hecke-unit")
    print()

    # Compute MeV predictions
    print(f"  {'iso':>4}  {'T1_A':>12}  {'T1_B':>12}  "
          f"{'M_pred_A (MeV)':>16}  {'M_pred_B (MeV)':>16}  "
          f"{'M_CODATA (MeV)':>16}  {'err_A':>9}  {'err_B':>9}")
    print("  " + "-" * 110)

    results = []
    for row in rows:
        iso = row["isotope"]
        codata = _CODATA.get(iso, mp.mpf(0))

        if "A_six_term" in row:
            tot_A = row["A_six_term"]["total_hecke"]
            t4_A = row["A_six_term"]["t4_MeV"]
            M_A = E0_A * tot_A + t4_A
            err_A = (M_A - codata) / codata * 100 if codata != 0 else mp.mpf(0)
        else:
            M_A = None; err_A = None

        if "B_six_term" in row:
            tot_B = row["B_six_term"]["total_hecke"]
            t4_B = row["B_six_term"]["t4_MeV"]
            M_B = E0_A * tot_B + t4_B  # same E_0 (substrate calibration)
            err_B = (M_B - codata) / codata * 100 if codata != 0 else mp.mpf(0)
        else:
            M_B = None; err_B = None

        ta = mp.nstr(row["t1_A"], 6) if row["t1_A"] else "—"
        tb = mp.nstr(row["t1_B"], 6) if row["t1_B"] else "—"
        ma = f"{float(M_A):>16.4f}" if M_A is not None else " " * 16
        mb = f"{float(M_B):>16.4f}" if M_B is not None else " " * 16
        ea = f"{float(err_A):>+8.3f}%" if err_A is not None else " " * 9
        eb = f"{float(err_B):>+8.3f}%" if err_B is not None else " " * 9
        cm = f"{float(codata):>16.4f}" if codata != 0 else " " * 16

        print(f"  {iso:>4}  {ta:>12}  {tb:>12}  "
              f"{ma}  {mb}  {cm}  {ea}  {eb}")

        results.append({
            "isotope": iso,
            "t1_model_a": str(row["t1_A"]) if row["t1_A"] else None,
            "t1_model_b": str(row["t1_B"]) if row["t1_B"] else None,
            "M_pred_a_MeV": str(M_A) if M_A is not None else None,
            "M_pred_b_MeV": str(M_B) if M_B is not None else None,
            "M_codata_MeV": str(codata),
            "err_a_pct": str(err_A) if err_A is not None else None,
            "err_b_pct": str(err_B) if err_B is not None else None,
        })

    print()
    print("  Mode: r-side-bare (Path 1, Markov-invariant T2/T3)")
    print("  T4 = m_e · Σ_{λ⊢3A} 1/dim_q(λ) (Frobenius co-Casimir per-3A)")
    print("  T5 = (a_K - 1) · T1 (chirality multiplicative on T1)")
    print("  T6 = 0 (open R&D; Habiro residue witness not yet generated)")
    print()

    # Save witness
    w = (
        WitnessBuilder("build-six-term-substrate-model-b", engine="mpmath")
        .set_description(
            "Six-term substrate-only mass predictor on Model B (SDP-canonical) "
            "T1 inputs.  Runs the same R-side-bare tower formula as "
            "paper_six_term_isotope_sweep.py with mode='r-side-bare', but with "
            "Model B T1 values from probe-sdp-canonical-paper-formula.witness.json "
            "instead of Model A's atomic_braid_word_3A.  Side-by-side comparison "
            "of A vs B predictions at q_0, calibrated to proton CODATA via "
            "Model A (Model B doesn't have a free-proton braid)."
        )
        .set_content_block("thm:knot-mass-formula-unified")
        .set_audit_only(
            "docs/coordination/six-term-mass-pipeline.md (audit doc); "
            "docs/audits/2026-05-11-model-b-mass-table.md (Model B T1)"
        )
        .add_parameter("q_0", mp.nstr(Q0, 50))
        .add_parameter("m_e_MeV", mp.nstr(mp.mpf(M_E_MEV), 20))
        .add_parameter("tower_mode", "r-side-bare")
        .add_parameter("E_0_MeV_per_hecke_unit", mp.nstr(E0_A, 20))
        .add_data("results", results)
    )
    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
