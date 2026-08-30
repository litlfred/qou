#!/usr/bin/env python3
"""
binding_fewbody_bondcount.py — few-body truncation tames the tower overshoot; the
residual is the geometric BOND-COUNT M_n(K), not an algebraic weight kernel.

Owner steer (2026-07-11): try the few-body truncated form
  B(K) = m_e · Σ_{n=2}^{n_max} a_D^(n) · w_n · M_n(K),
then: "but scaling / normalization issue?"

Two findings:
  (1) Truncating the na-Stokes jet tower at n_max=3 with a linear-chain cluster
      count drops the Part-5 overshoot from ~2e6 % (sum-to-A) to ~50 % — few-body
      truncation is the right structure.
  (2) The residual IS a normalization: the bond-count M_n(K). Anchoring the
      per-bond energy on the deuteron (1 bond = B_strong(D) = 2.22 MeV), the
      implied #bonds/A (coordination number) plateaus at ~2.6–3.8 for A≥6 — the
      nuclear saturation curve. ⁴He (coordination 3.28 > its 6 pairwise bonds) is
      the magic-shell outlier needing the n=3 term.

Synthesis: a_D^(n) supplies the per-cluster energy (deuteron-anchored); the knot
topology supplies the cluster count M_n(K) (crossing/coordination structure of
𝓑_K). The missing piece is GEOMETRIC (bond-count / hyperbolic-link, 2026-07-03
Option 1), NOT an algebraic weight kernel R(q,x).

EXPLORATORY — no production wiring, no fitted constant (weights anchored on D, T;
one Coulomb model). No tier change.
Audit: docs/audits/2026-07-11-eigenfunction-weight-kernel-link-and-wn-derive-or-refute.md §Part 6
"""
from __future__ import annotations
import sys
from math import comb
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps
set_compute_dps()  # canonical COMPUTE_DPS (=70) — matches WitnessBuilder precisionMetadata
# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

try:
    from q_parameter import Q_MP as Q0
    q = mp.mpf(str(Q0))
except Exception:
    q = mp.mpf("1.10997859555733471")

from experimental_constants import M_E_MEV as _M_E_MEV  # noqa: E402 — CAL-1 registry (single source)
M_E = mp.mpf(str(_M_E_MEV))  # CODATA-2022 m_e (full precision; prior literal was 8 sig figs)
ISO = {"D": (2.224566, 1, 2), "T": (8.481821, 1, 3), "3He": (7.718058, 2, 3),
       "4He": (28.295661, 2, 4), "6Li": (31.99464, 3, 6), "7Li": (39.24454, 3, 7),
       "9Be": (58.16497, 4, 9), "12C": (92.16172, 6, 12)}


def qint(k):
    return (q ** k - q ** (-k)) / (q - q ** (-1))


def qfac(n):
    p = mp.mpf(1)
    for k in range(1, n + 1):
        p *= qint(k)
    return p


def parts(n, m=None):
    m = n if m is None else m
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for r in parts(n - k, k):
            yield (k,) + r


def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(lam[i] - j - 1) + (conj[j] - i - 1) + 1
            for i in range(len(lam)) for j in range(lam[i])]


def dimq(lam):
    d = qfac(sum(lam))
    for h in hooks(lam):
        d /= qint(h)
    return d


def a_D(n):
    return mp.fsum(dimq(l) for l in parts(n)) / n


def b_strong(B, Z, A):
    R = mp.mpf("1.2") * mp.mpf(A) ** (mp.mpf(1) / 3)
    return mp.mpf(str(B)) + mp.mpf("0.6") * Z * (Z - 1) * mp.mpf("1.44") / R


def main() -> int:
    # weights anchored (no free fit) on deuteron (M2=1) and triton (chain M2=2,M3=1)
    w2 = b_strong(*ISO["D"]) / (M_E * a_D(2))
    w3 = (b_strong(*ISO["T"]) / M_E - a_D(2) * w2 * 2) / (a_D(3) * 1)

    print("=== few-body truncation + bond-count normalization ===")
    print(f"anchored: w2={float(w2):.3f} (deuteron), w3={float(w3):.3f} (triton chain)\n")

    print("(1) n_max=3, linear-chain cluster count M_n=A-n+1 (vs full-tower ~2e6%):")
    print(f"  {'iso':<5}{'A':>3}{'B_str':>9}{'B_pred':>10}{'err%':>9}")
    mx = mp.mpf(0)
    for K, (B, Z, A) in ISO.items():
        bs = b_strong(B, Z, A)
        bp = M_E * (a_D(2) * w2 * max(A - 1, 0) + a_D(3) * w3 * max(A - 2, 0))
        e = (bp - bs) / bs
        mx = max(mx, abs(e))
        print(f"  {K:<5}{A:>3}{float(bs):>9.2f}{float(bp):>10.2f}{float(e) * 100:>8.1f}%")
    print(f"  worst |err| = {float(mx) * 100:.0f}%  (vs full-tower ~2e6%)\n")

    print("(2) residual = bond-count normalization: implied #bonds/A (coordination):")
    coord = {}
    print(f"  {'iso':>5}{'A':>3}{'#bonds':>9}{'#bonds/A':>10}{'C(A,2)':>8}")
    for K, (B, Z, A) in ISO.items():
        nb = b_strong(B, Z, A) / (M_E * a_D(2) * w2)
        coord[K] = float(nb / A)
        print(f"  {K:>5}{A:>3}{float(nb):>9.2f}{float(nb / A):>10.2f}{comb(A, 2):>8}")
    print("  → #bonds/A rises 0.5 (D) → plateau ~2.6-3.8 (A≥6): the saturation curve.")
    print("    ⁴He 3.28 (magic α; > 6 pairwise bonds ÷ 4 → needs n=3 term).\n")

    print("SYNTHESIS: a_D^(n) = per-cluster energy (deuteron-anchored); knot topology")
    print("  = cluster count M_n(K). Missing piece is GEOMETRIC (bond-count/hyperbolic")
    print("  link), NOT an algebraic weight kernel R(q,x).")

    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("binding-fewbody-bondcount", engine="mpmath")
        wb.set_description(
            "EXPLORATORY: few-body truncation (n_max=3) of the na-Stokes jet-filtration "
            "binding drops the sum-to-A overshoot from ~2e6% to ~50%; the residual is the "
            "geometric bond-count M_n(K) (implied #bonds/A = nuclear coordination, plateau "
            "~2.6-3.8 for A≥6). Synthesis: a_D=per-cluster energy, knot topology=cluster "
            "count; missing piece is geometric (bond-count), not an algebraic weight kernel. "
            "Weights anchored on D,T; no free fit.")
        wb.add_data("w2_w3_anchored", {"w2": float(w2), "w3": float(w3)})
        wb.add_data("coordination_bonds_per_A", coord)
        wb.add_data("chain_worst_err_pct", float(mx) * 100)
        wb.add_assertion(
            name="fewbody_truncation_tames_overshoot",
            computed=str(int(float(mx) * 100 < 100)), expected="1", tolerance=0,
            source=(f"n_max=3 chain truncation worst |err| = {float(mx) * 100:.0f}% "
                    "(vs full-tower ~2e6%); residual is the geometric bond-count M_n(K)."))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness emit skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
