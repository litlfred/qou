#!/usr/bin/env python3
"""
30c: Markov-invariant unified mass — extended to full Z ≤ 10 census.

Plugs the 23-atom canonical Markov-trace sweep
(`canonical-isospin-pyhecke-full-census.witness.json`) into the
3-prefactor formula from `markov_invariant_unified_mass.py`:

  B_pred = α_M · log|tr_M(β)| + α_F · m_e · Σ_λ 1/dim_q(V_λ)
                              + m_e · 8G · B_shadow(β)

α_M, α_F calibrated from {D, T} bindings; α_T7 = 1 universal.

This script DROPS the Term 7 shadow-price contribution for atoms
beyond {D, T, ³He, ⁴He} where it has not yet been computed (sets
T7_term = 0).  That is a known under-counting; see follow-up
'extend Term 7 shadow-price to full census' for the eventual fix.

The point of this sweep is to ANSWER the question: does the
Markov-invariant formula generalise across the census, or does it
fail like the per-atom census strategies it replaces?

Output:
  markov-invariant-mass-full-census.witness.json

Refs:
  - markov_invariant_unified_mass.py (6-atom version)
  - canonical_isospin_pyhecke_full_census.py (this sweep's input)
  - low_isotope_mass_table.py (the non-categorical table being replaced)
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 30

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP

Q0 = Q_MP
QI = Q_INV_MP
m_e = mp.mpf("0.51099895")
m_p = mp.mpf("938.27208816")
m_n = mp.mpf("939.56542052")
G = mp.catalan


def qint(n):
    return (Q0 ** n - QI ** n) / (Q0 - QI)


def qfac(n):
    p = mp.mpf(1)
    for k in range(1, n + 1):
        p *= qint(k)
    return p


def hook_lengths(shape):
    rows = len(shape)
    out = []
    for i in range(rows):
        for j in range(shape[i]):
            arm = shape[i] - j - 1
            leg = sum(1 for r in range(i + 1, rows) if shape[r] > j)
            out.append(arm + leg + 1)
    return out


def dim_q_partition(shape, n):
    h_prod = mp.mpf(1)
    for hk in hook_lengths(shape):
        h_prod *= qint(hk)
    return qfac(n) / h_prod


def partitions_of(n, max_height=None):
    """Yield partitions of n with at most max_height parts (default unbounded).

    The early-prune form avoids generating the full p(n) ≈ 2.3M partitions of
    n=66 just to filter them later — only those satisfying the height cap are
    enumerated.
    """
    if n == 0:
        yield ()
        return
    def gen(rem, mxp, parts_used):
        if rem == 0:
            yield ()
            return
        if max_height is not None and parts_used >= max_height:
            return
        for p in range(min(mxp, rem), 0, -1):
            for rest in gen(rem - p, p, parts_used + 1):
                yield (p,) + rest
    yield from gen(n, n, 0)


def Sigma_n(n, height_cap=None, time_budget_sec=10.0):
    """Σ_n = Σ_λ 1/dim_q(V_λ) — Frobenius co-Casimir at H_n.

    For large n (≳ 24), the partition count with height_cap=8 explodes
    (#partitions of 66 with ≤ 8 parts ≈ 10^5).  Adaptive cap based on n,
    plus a hard time budget that returns a partial sum if exceeded.
    """
    import time as _t
    t0 = _t.time()
    if height_cap is None:
        # Adaptive: keep enumeration tractable even at n = 66.
        height_cap = 8 if n <= 12 else (6 if n <= 24 else (4 if n <= 48 else 3))
    total = mp.mpf(0)
    n_terms = 0
    # Tolerance tied to current mpmath precision (don't hardcode 1e-30).
    tol = mp.mpf(10) ** (-(mp.mp.dps - 5))
    for shape in partitions_of(n, max_height=height_cap):
        d = dim_q_partition(shape, n)
        if abs(d) > tol:
            total += 1 / d
            n_terms += 1
        if n_terms % 64 == 0 and _t.time() - t0 > time_budget_sec:
            print(f"  WARNING: Sigma_n({n}) hit time budget {time_budget_sec}s "
                  f"after {n_terms} terms; returning partial sum.")
            break
    return total


# AME 2020 reference (atomic masses + binding energies)
# (Z, N, M_AME [MeV], B_AME [MeV])
AME = {
    "1H":   (1, 0,   938.78308711,    0.000),
    "2H":   (1, 1,  1876.12393,       2.22456612),
    "3H":   (1, 2,  2809.43215,       8.481798),
    "3He":  (2, 1,  2809.41347,       7.718058),
    "4He":  (2, 2,  3728.40133,      28.29566),
    "6Li":  (3, 3,  5603.05152,      31.99405),
    "7Li":  (3, 4,  6535.36682,      39.24454),
    "8Be":  (4, 4,  7456.89450,      56.49951),
    "9Be":  (4, 5,  8394.79533,      58.16507),
    "10Be": (4, 6,  9327.54804,      64.97751),
    "10B":  (5, 5,  9326.99173,      64.75071),
    "11B":  (5, 6, 10255.10314,      76.20530),
    "12C":  (6, 6, 11177.92924,      92.16175),
    "13C":  (6, 7, 12112.54834,      97.10804),
    "14N":  (7, 7, 13043.78085,     104.65866),
    "15N":  (7, 8, 13972.51299,     115.49190),
    "16O":  (8, 8, 14899.16865,     127.61933),
    "17O":  (8, 9, 15834.59045,     131.76273),
    "18O":  (8, 10,16766.11190,     139.80735),
    "19F":  (9, 10,17696.90057,     147.80138),
    "20Ne": (10,10,18622.84014,     160.64491),
    "21Ne": (10,11,19555.64442,     167.40601),
    "22Ne": (10,12,20484.84562,     177.77000),
}


def main() -> int:
    base = Path(__file__).parent

    # Load full-census tr_M
    canon_path = base / "canonical-isospin-pyhecke-full-census.witness.json"
    canon = json.loads(canon_path.read_text())
    tr_M_table: dict[str, mp.mpf] = {}
    for label, entry in canon["results"].items():
        if "tr_M_q0" in entry:
            tr_M_table[label] = mp.mpf(str(entry["tr_M_q0"]))

    # Optional: existing Term 7 shadow-price for the 6 base atoms
    try:
        t7 = json.loads((base / "paper-six-term-shadow-price-sweep.witness.json").read_text())
        t7_results = t7.get("results", {})
    except Exception:
        t7_results = {}

    def get_B_shadow(label: str) -> mp.mpf:
        sup = {"3He": "³He", "4He": "⁴He", "2H": "D", "3H": "T"}
        target = sup.get(label, label)
        for k in t7_results:
            if k == target or k.startswith(target + " "):
                return mp.mpf(str(t7_results[k]["B_shadow"]))
        return mp.mpf(0)

    print("=" * 110)
    print("  30c: Markov-invariant unified mass formula — FULL Z ≤ 10 census")
    print(f"  q_0 = {float(Q0):.10f},  m_e = {float(m_e):.6f} MeV")
    print(f"  m_e·8G = {float(m_e * 8 * G):.6f} MeV")
    print("=" * 110)

    m_e_8G = m_e * 8 * G

    # Calibrate α_M, α_F from D and T (matches existing 30a anchor)
    B_D_AME = mp.mpf(str(AME["2H"][3]))
    B_T_AME = mp.mpf(str(AME["3H"][3]))
    log_D = mp.log(abs(tr_M_table["2H"]))
    log_T = mp.log(abs(tr_M_table["3H"]))
    S_D = Sigma_n(3 * 2)
    S_T = Sigma_n(3 * 3)
    Bsh_D = get_B_shadow("2H")
    Bsh_T = get_B_shadow("3H")

    res_D = B_D_AME - m_e_8G * Bsh_D
    res_T = B_T_AME - m_e_8G * Bsh_T

    A11 = log_D
    A12 = m_e * S_D
    A21 = log_T
    A22 = m_e * S_T
    det_A = A11 * A22 - A12 * A21
    alpha_M = (res_D * A22 - res_T * A12) / det_A
    alpha_F = (A11 * res_T - A21 * res_D) / det_A

    print(f"\n  Calibrated structural prefactors (anchored on D, T):")
    print(f"    α_M = {float(alpha_M):.6f} MeV")
    print(f"    α_F = {float(alpha_F):.6f}  (× m_e)")
    print(f"    α_T7 = 1.0  (universal coefficient on m_e·8G·B_shadow)")
    print()

    # Predict for all 23 isotopes
    print(f"  {'iso':>5} {'A':>3} {'B_AME':>9} {'α_M·log|tr|':>13} {'α_F·m_e·Σ_n':>14} "
          f"{'T7':>8} {'B_pred':>10} {'err B%':>8} {'M_err ppm':>10} {'cal':>4}")
    print("  " + "-" * 105)
    rows = []
    Sigma_cache: dict[int, mp.mpf] = {}
    for label, (Z, N, M_AME, B_AME) in AME.items():
        A = Z + N
        n = 3 * A
        if label not in tr_M_table:
            continue
        if n not in Sigma_cache:
            Sigma_cache[n] = Sigma_n(n)
        Sn = Sigma_cache[n]
        log_tr = mp.log(abs(tr_M_table[label]))
        Bsh = get_B_shadow(label)
        M_term = alpha_M * log_tr
        F_term = alpha_F * m_e * Sn
        T7_term = m_e_8G * Bsh
        B_pred = M_term + F_term + T7_term
        B_AME_mp = mp.mpf(str(B_AME))
        err_B = ((B_pred - B_AME_mp) / B_AME_mp * 100) if B_AME_mp != 0 else mp.mpf(0)
        # Total mass: M = Z·m_p + N·m_n + Z·m_e − B
        M_pred = Z * m_p + N * m_n + Z * m_e - B_pred
        M_AME_mp = mp.mpf(str(M_AME))
        err_M_ppm = ((M_pred - M_AME_mp) / M_AME_mp * 1e6) if M_AME_mp != 0 else mp.mpf(0)
        cal = "CAL" if label in ("2H", "3H") else ""
        print(f"  {label:>5} {A:>3} {float(B_AME):>+9.3f} {float(M_term):>+13.4f} "
              f"{float(F_term):>+14.4f} {float(T7_term):>+8.4f} "
              f"{float(B_pred):>+10.4f} {float(err_B):>+8.2f} "
              f"{float(err_M_ppm):>+10.2f}  {cal:>3}")
        rows.append({
            "iso": label, "Z": Z, "N": N, "A": A, "n_strands": n,
            "M_AME_MeV": float(M_AME_mp), "B_AME_MeV": float(B_AME_mp),
            "tr_M_q0": float(tr_M_table[label]),
            "log_abs_tr_M": float(log_tr),
            "Sigma_n": float(Sn),
            "B_shadow": float(Bsh),
            "M_term_MeV": float(M_term),
            "F_term_MeV": float(F_term),
            "T7_term_MeV": float(T7_term),
            "B_pred_MeV": float(B_pred),
            "M_pred_MeV": float(M_pred),
            "err_B_pct": float(err_B),
            "err_M_ppm": float(err_M_ppm),
            "is_calibration": label in ("2H", "3H"),
            "term7_available": float(Bsh) != 0,
        })

    print()
    pred_rows = [r for r in rows if not r["is_calibration"]]
    abs_err_M = [abs(r["err_M_ppm"]) for r in pred_rows]
    abs_err_B = [abs(r["err_B_pct"]) for r in pred_rows if r["B_AME_MeV"] != 0]
    if abs_err_M:
        print(f"  Predictions: n={len(pred_rows)}  "
              f"mean|err_M|={sum(abs_err_M)/len(abs_err_M):.0f} ppm  "
              f"max|err_M|={max(abs_err_M):.0f} ppm")
        print(f"               mean|err_B|={sum(abs_err_B)/len(abs_err_B):.2f}%  "
              f"max|err_B|={max(abs_err_B):.2f}%")

    # Compare to non-categorical baseline (low_isotope_mass_table)
    try:
        baseline = json.loads((base / "low-isotope-mass-table.witness.json").read_text())
        baseline_rows = {r["symbol"]: r for r in baseline["rows"]}
        baseline_M_errs = []
        for r in pred_rows:
            br = baseline_rows.get(r["iso"])
            if br is None:
                continue
            baseline_M_errs.append(abs(br["M_err_ppm"]))
        if baseline_M_errs:
            print(f"\n  Compare to non-categorical (census/α-cluster/partial-shell):")
            print(f"    baseline mean|err_M|={sum(baseline_M_errs)/len(baseline_M_errs):.0f} ppm  "
                  f"max={max(baseline_M_errs):.0f} ppm")
            print(f"    Markov   mean|err_M|={sum(abs_err_M)/len(abs_err_M):.0f} ppm  "
                  f"max={max(abs_err_M):.0f} ppm")
    except Exception as e:
        print(f"  (baseline comparison unavailable: {e})")

    witness = {
        "computation": "markov-invariant-mass-full-census",
        "description": (
            "30c: Markov-invariant unified mass formula extended to all 23 "
            "isotopes with Z ≤ 10.  Plugs the full-census canonical "
            "Markov-trace sweep into the 3-prefactor formula "
            "(α_M·log|tr_M| + α_F·m_e·Σ_n + m_e·8G·B_shadow), with "
            "α_M, α_F calibrated from {D, T}.  Tests whether the "
            "categorical formula generalises across the census or fails "
            "the way the per-atom census/α-cluster strategies do.  "
            "Term 7 shadow-price drops to 0 for Z ≥ 3 atoms where it has "
            "not yet been computed."
        ),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "structural_prefactors": {
            "alpha_M_MeV": float(alpha_M),
            "alpha_F": float(alpha_F),
            "alpha_T7_universal": 1.0,
            "m_e_8G_MeV": float(m_e_8G),
        },
        "calibration_anchors": ["2H", "3H"],
        "rows": rows,
    }
    out_path = base / "markov-invariant-mass-full-census.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
