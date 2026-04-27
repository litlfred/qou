#!/usr/bin/env python3
"""Six-term mass-formula consumer for Family 1 (D, T, ³He).

Sprint A v3 — canonical-only enumeration audit.

Per `content/quantum-observable-universe/braids-and-knots/six-term-mass-formula-complete.md`,
the canonical mass is

    𝔪(ρ) = |tr_M(T_w)|                            (T1)
         + Σ_i Φ_q(|V̂_i^full|)                   (T2)
         + z² Σ_{i<j} Φ_q(|V̂_i^full V̂_j^full|)  (T3)
         + m_e · τ(C_{dim_q})                       (T4)
         + a_K · 𝒞_K                               (T5)
         + Σ_{ℓ≥2} Res_{q=ζ_ℓ}[·] / (q_0 - ζ_ℓ).   (T6)

This consumer reads the joint-tower SDP witness
(`joint-tower-sdp-rust.witness.json`) for the canonical GB-NF data on
D / T / ³He, then enumerates which terms have a per-atom value
available from the existing per-term scripts and which still require a
per-atom helper to be added.  **It does not invoke SnapPy or any
hp_volume helper anywhere.**

Terms reused from existing scripts (no reimplementation):
  T1   : `crt_markov.tr_M_at_q0_via_crt(Z, N, ...)`
  T2+T3: `tower_isotope_absolute.compute_isotope_tower(Z, N, m_e_H)`
         (returns the brane-tower mass in MeV, single-point electron
         calibration; this IS T1+T2+T3 evaluated at q_0).
  T4   : pending per-atom helper (Frobenius co-Casimir is partition-
         indexed; `frobenius_partition_sum.py` lacks a clean per-atom
         caller).
  T5   : `ribbon_content_average.content_average(Z, N, include_inter)`
         returns ⟨c(λ)⟩_β (the chirality content average).
  T6   : `habiro_residue_symbolic.eval_schur_weyl_exact_at_q0(A_values=)`
         returns per-A residue values.

The output witness records the canonical per-term contribution where
available, marks pending terms explicitly, and DOES NOT emit a
calibrated AME-comparable binding-energy prediction yet — that
requires the calibration + (Z·m_p + N·m_n - M) conversion pipeline,
which is queued as Sprint A v4.

Usage:
  python folio-assistant/computations/six_term_consumer.py
"""
from __future__ import annotations

import json
import sys
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import mpmath as mp
mp.mp.dps = 50

WITNESS_IN = HERE / "joint-tower-sdp-rust.witness.json"
WITNESS_OUT = HERE / "six-term-mass-pred.witness.json"

# Family 1 atoms — name in joint-tower-sdp registry → (Z, N, A)
FAMILY_1 = {
    "deuteron-2H":  (1, 1, 2),
    "tritium-3H":   (1, 2, 3),
    "helium3-3He":  (2, 1, 3),
}


def _safe(fn, label):
    """Call `fn` and return (value, error_or_None).  Never raises."""
    try:
        return fn(), None
    except Exception as e:  # noqa: BLE001 — boundary; we report all failures
        return None, f"{type(e).__name__}: {e}"


def term_T1_T2_T3(Z, N):
    """Brane-tower mass (T1+T2+T3 combined) in MeV via electron
    calibration.  Returns the canonical mass that the existing
    `compute_isotope_tower` produces — no SnapPy, no fitted constants."""
    import tower_isotope_absolute as tia
    m_e_H, _ = tia.compute_electron_tower()
    r = tia.compute_isotope_tower(Z, N, m_e_H)
    return {
        "M_MeV_raw": r["M_MeV_raw"],
        "M_MeV_corrected": r["M_MeV_corrected"],
        "n_strands": r["n_strands"],
        "source": "tower_isotope_absolute.compute_isotope_tower",
    }


def term_T5(Z, N):
    """Chirality content average ⟨c(λ)⟩_β (per-crossing dual-space form).
    Returns the dimensionless average; the canonical Term 5 mass
    contribution is m_e · ⟨c(λ)⟩_β · h with h = q − q⁻¹."""
    import ribbon_content_average as rca
    c_avg, num, den, _per_lam = rca.content_average(Z, N, include_inter=True)
    return {
        "c_avg": float(c_avg),
        "numerator": float(num),
        "denominator": float(den),
        "source": "ribbon_content_average.content_average",
    }


def term_T6(A):
    """Habiro / Schur-Weyl exact residue at q_0.  The helper takes
    A_values; we extract just the entry for our A."""
    import habiro_residue_symbolic as hrs
    out = hrs.eval_schur_weyl_exact_at_q0(A_values=(A,))
    # The helper returns a dict keyed by A (or list of dicts);
    # normalise to the per-A entry.
    if isinstance(out, dict):
        return {"per_A": {str(A): out.get(A, out)}, "source": "habiro_residue_symbolic.eval_schur_weyl_exact_at_q0"}
    if isinstance(out, list):
        per_A = {str(A): out[0] if out else None}
        return {"per_A": per_A, "source": "habiro_residue_symbolic.eval_schur_weyl_exact_at_q0"}
    return {"raw": str(out), "source": "habiro_residue_symbolic.eval_schur_weyl_exact_at_q0"}


def main() -> int:
    if not WITNESS_IN.exists():
        print(f"[ERROR] missing input witness: {WITNESS_IN}")
        return 1

    in_data = json.loads(WITNESS_IN.read_text())
    certs_by_name = {c["name"]: c for c in in_data.get("per_atom_certificates", [])}

    print("=" * 100)
    print("SIX-TERM MASS-FORMULA CONSUMER — Family 1 (D, T, ³He)")
    print("Canonical-only: no SnapPy, no hp_volume, no fitted constants.")
    print("=" * 100)

    out_per_atom = {}
    for name, (Z, N, A) in FAMILY_1.items():
        cert = certs_by_name.get(name)
        if cert is None:
            print(f"  [WARN] {name}: not found in joint-tower-sdp witness; skipping")
            continue

        print(f"\n── {name} (Z={Z}, N={N}, A={A}) ──")
        b_ame = cert.get("b_ame_mev")
        braid_word = cert.get("braid_word")
        native_n = cert.get("native_strand_count")
        print(f"  braid_word = {braid_word}")
        print(f"  native_strand_count = {native_n}")
        print(f"  b_ame_mev = {b_ame}")

        t1_t2_t3, e1 = _safe(lambda: term_T1_T2_T3(Z, N), "T1+T2+T3")
        t5, e5 = _safe(lambda: term_T5(Z, N), "T5")
        t6, e6 = _safe(lambda: term_T6(A), "T6")

        per_atom = {
            "Z": Z, "N": N, "A": A,
            "braid_word": braid_word,
            "native_strand_count": native_n,
            "b_ame_mev": b_ame,
            "terms": {
                "T1_T2_T3_brane_tower":
                    t1_t2_t3 if t1_t2_t3 is not None else {"error": e1, "pending": True},
                "T4_frobenius_co_casimir":
                    {"pending": True,
                     "reason": "frobenius_partition_sum.py lacks per-atom helper; "
                               "Term 4 contribution is partition-indexed and requires "
                               "summing the central-idempotent basis weighted by "
                               "[n]_q!/(dim_q(λ)²·dim(λ)) — to be added in Sprint A v4."},
                "T5_chirality_content_average":
                    t5 if t5 is not None else {"error": e5, "pending": True},
                "T6_habiro_residue":
                    t6 if t6 is not None else {"error": e6, "pending": True},
            },
        }
        out_per_atom[name] = per_atom

        # Diagnostic print
        if t1_t2_t3:
            print(f"  T1+T2+T3 (brane tower): M_MeV_raw = {t1_t2_t3['M_MeV_raw']}")
        else:
            print(f"  T1+T2+T3: PENDING — {e1}")
        print(f"  T4 (Frobenius co-Casimir): PENDING — needs per-atom helper")
        if t5:
            print(f"  T5 (chirality ⟨c(λ)⟩_β): c_avg = {t5['c_avg']:.10f}")
        else:
            print(f"  T5: PENDING — {e5}")
        if t6:
            print(f"  T6 (Habiro residue): emitted")
        else:
            print(f"  T6: PENDING — {e6}")

    out = {
        "computation": "six-term-mass-pred",
        "description": (
            "Per-particle six-term mass-formula enumeration for Family 1 "
            "(D, T, ³He) consuming canonical GB-NF data from "
            "joint-tower-sdp-rust.witness.json. Reads each existing per-term "
            "script's helper (no SnapPy, no hp_volume, no fitted constants). "
            "T4 (Frobenius co-Casimir) is marked pending because "
            "frobenius_partition_sum.py lacks a per-atom helper; the AME-"
            "comparable binding-energy assembly is queued as Sprint A v4."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source_witness": str(WITNESS_IN.relative_to(HERE.parent.parent)),
        "precision_dps": 50,
        "per_particle": out_per_atom,
        "attestation": {
            "used_snappy": False,
            "used_hp_volume": False,
            "used_volume_match": False,
            "used_fitted_constants": False,
            "term_status": {
                "T1_T2_T3": "wired (compute_isotope_tower)",
                "T4": "pending — needs per-atom Frobenius co-Casimir helper",
                "T5": "wired (ribbon_content_average.content_average)",
                "T6": "wired (habiro_residue_symbolic.eval_schur_weyl_exact_at_q0)",
            },
            "ame_comparison_pending": True,
            "ame_comparison_reason": (
                "Four-of-six terms wired but the consumer does not yet "
                "calibrate to MeV via electron and convert tower mass to "
                "binding energy via B = Z·m_p + N·m_n − M_total. "
                "Sprint A v4 will land that conversion."
            ),
        },
    }
    WITNESS_OUT.write_text(json.dumps(out, indent=2, default=str) + "\n")
    print()
    print(f"  Witness: {WITNESS_OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
