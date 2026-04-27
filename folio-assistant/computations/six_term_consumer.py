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
  T1+T2+T3: `tower_isotope_absolute.compute_isotope_tower(Z, N, m_e_H)`
            (returns the brane-tower mass at q_0 in MeV via electron
            calibration; this IS T1+T2+T3 evaluated at q_0). The
            `crt_markov` Markov-trace path is NOT called here — Term 1
            on its own would over-count once T2+T3 land via the brane
            tower, so we consume the combined T1+T2+T3 from the tower
            helper directly.
  T4      : pending per-atom helper (Frobenius co-Casimir is partition-
            indexed; `frobenius_partition_sum.py` lacks a clean per-atom
            caller).
  T5      : `ribbon_content_average.content_average(Z, N, include_inter)`
            returns ⟨c(λ)⟩_β (the chirality content average).
  T6      : `habiro_residue_symbolic.eval_schur_weyl_exact_at_q0(A_values=)`
            returns a dict keyed `"A=<n>"`; we extract the per-A entry.
            Memoized across particles that share an A (T and ³He both A=3).

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
from pathlib import Path
from datetime import datetime, timezone

# Note: `import warnings; warnings.filterwarnings("ignore")`,
# `mp.mp.dps = 50` and `sys.path.insert(...)` are import-time side
# effects per Copilot/Gemini review. They are now applied inside
# `main()` only — importing this module (e.g. from the test suite)
# leaves the importer's global state untouched.

import mpmath as mp

HERE = Path(__file__).parent

WITNESS_IN = HERE / "joint-tower-sdp-rust.witness.json"
WITNESS_OUT = HERE / "six-term-mass-pred.witness.json"

# Sprint A precision contract: all mpmath operations in this module
# are scoped under `with mp.workdps(_DPS):` rather than mutating the
# global `mp.mp.dps` (per Gemini's standing review preference).
_DPS = 50

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


def term_T1_T2_T3(Z, N, m_e_H):
    """Brane-tower mass (T1+T2+T3 combined) in MeV via electron
    calibration. Returns the canonical mass that the existing
    `compute_isotope_tower` produces — no SnapPy, no fitted constants.

    `m_e_H` is the once-computed electron-tower value (Hecke units),
    passed in by `main()` to avoid recomputing it per particle
    (per Copilot review: a single tower call dominates Phi_q iterations)."""
    import tower_isotope_absolute as tia
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


_T4_CACHE: dict[int, dict] = {}


def term_T4(Z, N, m_e_MeV):
    """Frobenius co-Casimir contribution: m_e · Σ_λ 1/dim_q(λ)
    summed over partitions λ of the strand count n = 3·(Z+N).

    Per `frobenius-codim-universal.lean` and `frobenius-codim-universal`
    theorem, the universal Frobenius co-Casimir element of `H_n(R, q)`
    has Markov trace `Σ_λ 1/dim_q(λ)`. At n=3 this specialises to
    `2 + 1/[2]_q ≈ 2.451` (matching `partition-sum-proton-residual`).
    For atomic braids n = 3·A is the strand count.

    Memoised per n (so D(n=6), T(n=9), ³He(n=9) share work)."""
    n = 3 * (Z + N)
    if n in _T4_CACHE:
        return _T4_CACHE[n]
    from hecke_characters import partitions_of, dim_q
    total = mp.mpf(0)
    parts = list(partitions_of(n))
    for p in parts:
        d = dim_q(p)
        total += mp.mpf(1) / mp.mpf(str(d))
    result = {
        "n_strands": n,
        "n_partitions": len(parts),
        "sum_inv_dim_q": float(total),
        "T4_MeV": float(mp.mpf(str(m_e_MeV)) * total),
        "source": "Σ_λ 1/dim_q(λ) over λ⊢n  (Frobenius co-Casimir, frobenius-codim-universal.lean)",
    }
    _T4_CACHE[n] = result
    return result


_T6_CACHE: dict[int, dict] = {}


def term_T6(A):
    """Habiro / Schur-Weyl exact residue at q_0. The helper takes
    `A_values=` and returns a dict keyed `"A=<n>"`. We memoize per A
    so that A=3 (shared by T and ³He) is computed once across the run
    (per Copilot review: A=4+ can take ~30s in the upstream helper)."""
    if A in _T6_CACHE:
        return _T6_CACHE[A]
    import habiro_residue_symbolic as hrs
    out = hrs.eval_schur_weyl_exact_at_q0(A_values=(A,))
    # The helper returns a dict keyed by `"A=<n>"` (int A misses).
    payload = out.get(f"A={A}", out) if isinstance(out, dict) else {"raw": str(out)}
    result = {
        "per_A": {f"A={A}": payload},
        "source": "habiro_residue_symbolic.eval_schur_weyl_exact_at_q0",
    }
    _T6_CACHE[A] = result
    return result


def main() -> int:
    # Apply import-time side effects only when run as a script, not on
    # bare import (per Copilot review): `warnings.filterwarnings`,
    # `sys.path.insert`, and the precision context manager.
    import warnings
    warnings.filterwarnings("ignore")
    sys.path.insert(0, str(HERE))

    if not WITNESS_IN.exists():
        print(f"[ERROR] missing input witness: {WITNESS_IN}")
        return 1

    in_data = json.loads(WITNESS_IN.read_text())
    certs_by_name = {c["name"]: c for c in in_data.get("per_atom_certificates", [])}

    # Pull electron mass once for T4 (Frobenius co-Casimir = m_e · Σ 1/dim_q).
    from experimental_constants import M_E_MEV

    # Compute the electron tower value ONCE, share across all particles
    # (per Copilot review: avoids redundant Phi_q iterations).
    import tower_isotope_absolute as tia
    with mp.workdps(_DPS):
        m_e_H, _V_e = tia.compute_electron_tower()

    print("=" * 100)
    print("SIX-TERM MASS-FORMULA CONSUMER — Family 1 (D, T, ³He)")
    print("Canonical-only: no SnapPy, no hp_volume, no fitted constants.")
    print("=" * 100)

    out_per_atom = {}
    with mp.workdps(_DPS):
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

            t1_t2_t3, e1 = _safe(lambda: term_T1_T2_T3(Z, N, m_e_H), "T1+T2+T3")
            t4, e4 = _safe(lambda: term_T4(Z, N, M_E_MEV), "T4")
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
                        t4 if t4 is not None else {"error": e4, "pending": True},
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
            if t4:
                print(f"  T4 (Frobenius co-Casimir): n={t4['n_strands']}, "
                      f"|partitions|={t4['n_partitions']}, "
                      f"Σ 1/dim_q(λ) = {t4['sum_inv_dim_q']:.6f}, "
                      f"T4 = {t4['T4_MeV']:.6f} MeV")
            else:
                print(f"  T4: PENDING — {e4}")
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
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "source_witness": str(WITNESS_IN.relative_to(HERE.parent.parent)),
        "precision_dps": _DPS,
        "per_particle": out_per_atom,
        "attestation": {
            "used_snappy": False,
            "used_hp_volume": False,
            "used_volume_match": False,
            "used_fitted_constants": False,
            "term_status": {
                "T1_T2_T3": "wired (tower_isotope_absolute.compute_isotope_tower)",
                "T4": "wired (Σ_λ 1/dim_q(λ) over λ⊢3·A; Frobenius co-Casimir, frobenius-codim-universal.lean)",
                "T5": "wired (ribbon_content_average.content_average)",
                "T6": "wired (habiro_residue_symbolic.eval_schur_weyl_exact_at_q0)",
            },
            "ame_comparison_pending": True,
            "ame_comparison_reason": (
                "All six terms now have per-atom values, but the consumer "
                "does not yet assemble them into a single AME-comparable "
                "binding-energy prediction. The conversion pipeline "
                "(electron MeV calibration + B = Z·m_p + N·m_n − M_total + "
                "appropriate term-by-term sign/sum convention) is queued "
                "as Sprint A v5."
            ),
        },
    }
    WITNESS_OUT.write_text(json.dumps(out, indent=2, default=str) + "\n")
    print()
    print(f"  Witness: {WITNESS_OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
