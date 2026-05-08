#!/usr/bin/env python3
"""Six-term mass-formula consumer for Family 1 (D, T, ³He).

Sprint A v4 — canonical-only enumeration audit (T4 wired).

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
  T4      : wired via `term_T4()` partition-sum helper below
            (Σ_λ 1/dim_q(λ) over λ⊢n=3·A; Frobenius co-Casimir per
            `frobenius-codim-universal.lean`).  Memoised per n.
  T5      : `ribbon_content_average.content_average(Z, N, include_inter)`
            returns ⟨c(λ)⟩_β (the chirality content average).
  T6      : `habiro_residue_symbolic.eval_schur_weyl_exact_at_q0(A_values=)`
            returns a dict keyed `"A=<n>"`; we extract the per-A entry.
            Memoized across particles that share an A (T and ³He both A=3).

The output witness records the canonical per-term contribution where
available, marks pending terms explicitly, and DOES NOT emit a
calibrated AME-comparable binding-energy prediction yet — that
requires the calibration + (Z·m_p + N·m_n - M) conversion pipeline,
which is queued as Sprint A v5.

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

    Memoised per n for the dimensionless partition sum only (so D(n=6),
    T(n=9), ³He(n=9) share work).  `T4_MeV` is derived per call from
    the current `m_e_MeV` so a stale electron-mass argument cannot
    poison the cached scaled value (per Copilot review)."""
    n = 3 * (Z + N)
    if n not in _T4_CACHE:
        from hecke_characters import partitions_of, dim_q
        total = mp.mpf(0)
        parts = list(partitions_of(n))
        for p in parts:
            d = dim_q(p)
            total += mp.mpf(1) / mp.mpf(str(d))
        # Per Gemini review: preserve full mpmath precision in the
        # witness JSON via mp.nstr(..., _DPS) rather than float().
        # The numerical bounds-check tests use float(s) at consumption
        # time; downstream high-precision consumers can re-parse the
        # mpmath string at any precision they like.
        _T4_CACHE[n] = {
            "n_strands": n,
            "n_partitions": len(parts),
            "sum_inv_dim_q": mp.nstr(total, _DPS),
            "source": "Σ_λ 1/dim_q(λ) over λ⊢n  (Frobenius co-Casimir, frobenius-codim-universal.lean)",
        }
    cached = _T4_CACHE[n]
    total = mp.mpf(cached["sum_inv_dim_q"])
    t4_mev = mp.mpf(str(m_e_MeV)) * total
    return {
        **cached,
        "T4_MeV": mp.nstr(t4_mev, _DPS),
    }


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


def assemble_ame_comparison(per_particle, m_e_MeV, m_p_AME, m_n_AME):
    """Sprint A v5 — naïve six-term assembly into a binding-energy
    prediction, reported with explicit caveats about the combination
    convention (which is open theoretical work).

    For each Family 1 atom (Z, N, A):
      * T1+T2+T3 mass-tower (MeV) is taken as-is from compute_isotope_tower.
      * T4 (Frobenius co-Casimir, MeV) is added.
      * T5 (chirality, MeV) is added as `m_e · ⟨c(λ)⟩_β · h` with
        h = q − q⁻¹.
      * T6 (Habiro residue) is currently a symbolic / per-A object;
        its MeV translation requires nailing down whether it is
        ALREADY counted inside T1 (per the Mittag-Leffler decomposition
        of the full Markov trace) or is a separate additive correction.
        Round-2 probe established that the full tr_M (= T1+T6 in the
        decomposition `tr_M = tr_M^entire + Σ residues`) gives the
        −25 % neutron residual; so naïvely *adding* T6 to an already-
        full-tower-mass result would double-count.  Hence the v5
        assembly here treats T6 as ALREADY-INCLUDED in T1+T2+T3 and
        does not re-add it; this is one of the open convention choices
        (flagged in the witness `assembly_convention` field).

    Binding-energy comparison:
        M_atom_pred = (T1+T2+T3) + T4 + T5
        B_pred      = Z·m_p_AME + N·m_n_AME + Z·m_e − M_atom_pred
        B_AME       = b_ame_mev (from input witness)
        ppb_residual = (B_pred − B_AME) / B_AME · 1e9

    Returns a dict keyed by particle name with per-atom term-MeV
    breakdown + the assembled binding-energy prediction + ppb residual."""
    out = {}
    for name, atom in per_particle.items():
        Z, N, A = atom["Z"], atom["N"], atom["A"]
        b_ame = atom["b_ame_mev"]
        terms = atom["terms"]

        t123 = terms.get("T1_T2_T3_brane_tower", {})
        t4 = terms.get("T4_frobenius_co_casimir", {})
        t5 = terms.get("T5_chirality_content_average", {})
        t6 = terms.get("T6_habiro_residue", {})

        # Extract numeric MeV contributions (None if pending).
        # Per Gemini review: M_MeV_raw is an mpmath nstr string (50 dps);
        # tolerate trailing unit suffixes (e.g. " MeV") via split().
        M_t123 = None
        if not t123.get("pending"):
            raw_val = t123.get("M_MeV_raw")
            if raw_val is not None:
                try:
                    M_t123 = float(str(raw_val).split()[0])
                except (ValueError, IndexError):
                    M_t123 = None

        M_t4 = None
        if not t4.get("pending"):
            try:
                M_t4 = float(t4.get("T4_MeV"))
            except (TypeError, ValueError):
                M_t4 = None

        # T5 in MeV: m_e · ⟨c(λ)⟩_β · h, where h = q − q⁻¹.
        # ⟨c(λ)⟩_β is dimensionless; the canonical Term-5 mass
        # contribution scales it by m_e and h (per six-term-mass-formula
        # §Term 5).  The c_avg from ribbon_content_average is float64
        # (deferred from #453 review); h is computed from q_0.
        M_t5 = None
        if not t5.get("pending"):
            try:
                from q_parameter import Q as Q0_FLOAT
                c_avg = float(t5["c_avg"])
                h = Q0_FLOAT - 1.0 / Q0_FLOAT
                M_t5 = m_e_MeV * c_avg * h
            except (KeyError, TypeError, ValueError):
                M_t5 = None

        # T6: per the round-2 finding, treat as ALREADY-IN T1 (full
        # Markov-trace decomposition); not a separate additive term.
        # Recorded in the witness for traceability but not summed.
        M_t6_separate_addition = 0.0  # by convention

        # Assembly
        if M_t123 is not None:
            M_atom_pred = M_t123
            if M_t4 is not None:
                M_atom_pred += M_t4
            if M_t5 is not None:
                M_atom_pred += M_t5
            # M_atom_AME includes Z electrons bound to the nucleus
            # (atomic mass, not nuclear): atomic_mass = Z·m_p + N·m_n + Z·m_e − B.
            constituent_sum = Z * m_p_AME + N * m_n_AME + Z * m_e_MeV
            B_pred = constituent_sum - M_atom_pred
            B_pct = (B_pred - b_ame) / b_ame * 100 if b_ame else None
            B_ppb = B_pct * 1e7 if B_pct is not None else None
        else:
            M_atom_pred = None
            B_pred = None
            B_pct = None
            B_ppb = None

        out[name] = {
            "Z": Z, "N": N, "A": A,
            "term_MeV_contributions": {
                "T1_T2_T3_brane_tower_MeV": M_t123,
                "T4_frobenius_co_casimir_MeV": M_t4,
                "T5_chirality_MeV": M_t5,
                "T6_habiro_residue_MeV_separate": M_t6_separate_addition,
            },
            "M_atom_pred_MeV": M_atom_pred,
            "constituent_sum_MeV": Z * m_p_AME + N * m_n_AME + Z * m_e_MeV,
            "B_AME_MeV": b_ame,
            "B_pred_MeV": B_pred,
            "B_err_pct": B_pct,
            "B_err_ppb": B_ppb,
            "assembly_convention": (
                "M_atom_pred = T1+T2+T3 + T4 + T5; T6 treated as "
                "already-in T1 per round-2 finding (full Markov trace = "
                "T1^entire + cyclotomic residues = T1 + T6 in the "
                "decomposition). The right combination convention is "
                "open theoretical work — round-2 probe established that "
                "full tr_M alone gives −25 % neutron residual, so the "
                "remaining gap is in T2/T3 brane-tower assembly, T4/T5 "
                "additive contributions, or normalisation/sign convention. "
                "Reported ppb_residual is a baseline for further probing, "
                "not a canonical accuracy claim."
            ),
        }
    return out


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
                # sum_inv_dim_q and T4_MeV are 50-dps strings (mp.nstr);
                # cast to float only at the print boundary.
                print(f"  T4 (Frobenius co-Casimir): n={t4['n_strands']}, "
                      f"|partitions|={t4['n_partitions']}, "
                      f"Σ 1/dim_q(λ) = {float(t4['sum_inv_dim_q']):.6f}, "
                      f"T4 = {float(t4['T4_MeV']):.6f} MeV")
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

    # Sprint A v5 — naïve six-term assembly into a binding-energy
    # prediction (with explicit caveats; combination convention is
    # open theoretical work, see assemble_ame_comparison docstring).
    from experimental_constants import M_P_MEV, M_N_MEV
    ame_assembly = assemble_ame_comparison(
        out_per_atom, m_e_MeV=M_E_MEV, m_p_AME=M_P_MEV, m_n_AME=M_N_MEV,
    )

    print("\n  AME comparison (Sprint A v5 — naïve assembly):")
    print(f"    {'particle':<14} {'B_AME':>9} {'B_pred':>11} {'err [%]':>9} {'err [ppb]':>14}")
    print(f"    {'-' * 14} {'-' * 9} {'-' * 11} {'-' * 9} {'-' * 14}")
    for name, a in ame_assembly.items():
        b_a = f"{a['B_AME_MeV']:>9.4f}" if a['B_AME_MeV'] is not None else f"{'—':>9}"
        b_p = f"{a['B_pred_MeV']:>11.4f}" if a['B_pred_MeV'] is not None else f"{'—':>11}"
        e_pct = f"{a['B_err_pct']:>+9.2f}" if a['B_err_pct'] is not None else f"{'—':>9}"
        e_ppb = f"{a['B_err_ppb']:>+14.4e}" if a['B_err_ppb'] is not None else f"{'—':>14}"
        print(f"    {name:<14} {b_a} {b_p} {e_pct} {e_ppb}")
    print()

    out = {
        "computation": "six-term-mass-pred",
        "description": (
            "Per-particle six-term mass-formula enumeration for Family 1 "
            "(D, T, ³He) consuming canonical GB-NF data from "
            "joint-tower-sdp-rust.witness.json. Reads each existing per-term "
            "script's helper (no SnapPy, no hp_volume, no fitted constants). "
            "All six terms wired (Sprint A v4); naïve AME-comparable "
            "binding-energy assembly added (Sprint A v5) with explicit "
            "caveats about the open combination convention — round-2 "
            "neutron-gap probe established that full tr_M alone gives "
            "−25 % residual, so the assembly here is a baseline for "
            "further probing, not a canonical accuracy claim."
        ),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "source_witness": str(WITNESS_IN.relative_to(HERE.parent.parent)),
        "precision_dps": _DPS,
        "per_particle": out_per_atom,
        "ame_assembly_v5": ame_assembly,
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
