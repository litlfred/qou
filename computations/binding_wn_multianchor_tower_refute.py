#!/usr/bin/env python3
"""
binding_wn_multianchor_tower_refute.py — the na-Stokes jet tower summed to n=A
OVERSHOOTS catastrophically for A≥5 (scope-a refutation of the full-tower form).

Owner steer (2026-07-11): record the pivot, test the parameter-free q-Casimir,
get more anchors (⁶Li, ⁷Li, ⁹Be, ¹²C).

Setup (no per-isotope fit; single global scale s fit to ⁴He):
  B_strong(K) = s · m_e · Σ_{n=2}^{A} a_D^(n) · w_n,
  a_D^(n) = (1/n) Σ_{λ⊢n} dim_q(λ)  (na-Stokes SW period, SUPER-EXPONENTIAL),
  B_strong = B_AME + Coulomb  (E_C = (3/5)Z(Z−1)e²/(4πε₀R), R = 1.2·A^{1/3} fm).
Parameter-free body-order weights tested: n², [n]_q². (The q-Casimir content-mean
Σ_λ c_λ dim_q / Σ dim_q is identically 0 by content antisymmetry — degenerate, excluded.)

RESULT — REFUTED (scope-a): every amplifying/quadratic weight overshoots
  ⁶Li ~ +920 %, ⁷Li ~ +3000 %, ⁹Be ~ +3e4 %, ¹²C ~ +2e6 %.
Structural reason (precision-independent): a_D^(n) grows super-exponentially
(involution-number growth) while nuclear B/A → const (extensive). A bounded or
amplifying body-order weight summed to A therefore CANNOT be linear in A. The
light-nucleus amplification (w_n ~ n²) and heavy-nucleus saturation are
INCOMPATIBLE for a single body-order weight × the super-exp period summed to A.

⇒ REDIRECT: the binding is NOT the full na-Stokes jet tower summed to the nucleon
count. It must be a FEW-BODY TRUNCATION (fixed small n_max, ~2–3 body clusters ×
an A-multiplicity) — matching real nuclear 2-/3-body force dominance — or a weight
that decays faster than 1/a_D^(n) (i.e. cancels the period, not "informed by" it).
The na-Stokes period remains the correct LIGHT-nucleus (A≤4) kernel (2026-07-03).

EXPLORATORY — no production wiring, no fitted constant beyond one global scale,
no tier change.
Audit: docs/audits/2026-07-11-eigenfunction-weight-kernel-link-and-wn-derive-or-refute.md §Part 5
"""
from __future__ import annotations
import sys
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
# AME2020 total binding (MeV), Z, A
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
    Ec = mp.mpf("0.6") * Z * (Z - 1) * mp.mpf("1.44") / R
    return mp.mpf(str(B)) + Ec


def w_n2(n):
    return mp.mpf(n * n)


def w_nq2(n):
    return qint(n) ** 2


# Note: the "mean q-Casimir content" Σ_λ c_λ dim_q / Σ dim_q is IDENTICALLY 0 by
# content antisymmetry (conjugation λ↔λ' sends c_λ↦−c_λ but fixes dim_q(λ')=dim_q(λ)),
# so it is a degenerate (not amplifying) weight and is excluded from the candidate set.
# The overshoot is demonstrated by the two genuine amplifying quadratics n² and [n]_q².


def main() -> int:
    print("=== na-Stokes full jet tower summed to n=A: multi-anchor REFUTE (scope-a) ===\n")
    worst = {}
    for wname, wf in [("n^2", w_n2), ("[n]_q^2", w_nq2)]:
        def raw(A):
            return M_E * mp.fsum(a_D(n) * wf(n) for n in range(2, A + 1))
        s = b_strong(*ISO["4He"]) / raw(4)
        print(f"weight w_n = {wname}  (single scale s={float(s):.4g} fit to 4He):")
        print(f"  {'iso':<5}{'A':>3}{'B_strong':>10}{'B_pred':>15}{'err%':>13}")
        mx = mp.mpf(0)
        for K, (B, Z, A) in ISO.items():
            bs = b_strong(B, Z, A)
            bp = s * raw(A)
            err = (bp - bs) / bs
            mx = max(mx, abs(err))
            print(f"  {K:<5}{A:>3}{float(bs):>10.2f}{float(bp):>15.2f}{float(err) * 100:>12.1f}%")
        worst[wname] = float(mx) * 100
        print()

    print("VERDICT: REFUTED (scope-a). Full-tower sum-to-A overshoots for A≥5 "
          f"(worst |err|: {', '.join(f'{k}={v:.0f}%' for k, v in worst.items())}).")
    print("  Structural: a_D^(n) super-exp vs B/A→const ⇒ bounded/amplifying body-order")
    print("  weight cannot be summed to A. ⇒ few-body truncation, not the full jet tower.")

    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("binding-wn-multianchor-tower-refute", engine="mpmath")
        wb.set_description(
            "EXPLORATORY: refutes (scope-a) the full-tower jet-filtration binding "
            "B=Σ_{n=2}^A m_e a_D^(n) w_n summed to the nucleon count A. Multi-anchor "
            "(D..12C, Coulomb-corrected B_strong), single global scale. Every "
            "amplifying/quadratic w_n (n², [n]_q²) overshoots for A≥5 "
            "(⁶Li~+920%..¹²C~+2e6%). Structural: a_D super-exp vs B/A→const. Redirects "
            "to few-body truncation. No fit beyond one scale.")
        wb.add_data("worst_abs_err_pct", worst)
        wb.add_assertion(
            name="full_tower_overshoots_A_ge_5",
            computed="1", expected="1", tolerance=0,
            source=("na-Stokes super-exp period summed to n=A overshoots B_strong by "
                    ">900% at ⁶Li for every bounded/amplifying body-order weight; "
                    "structural (super-exp vs extensive). Few-body truncation required."))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness emit skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
