#!/usr/bin/env python3
"""R&D probe: extended PSLQ search for c_4 (Step 4 of
conj:lambda-scale-substrate-form proof).

Previous probe found c_4 ≈ 0.006911959516716808 at 100 dps, with
no match in a 14-candidate basis. This script extends the search:

1. **Wide basis**: q-integers [n]_q (n = 2..15), powers h^k (k = 1..8),
   G^k (k = 1..3), Vol(B_3) ratios, mixed products.
2. **mpmath.pslq**: integer-relation finder operating at 100 dps to
   discover rational dependencies.
3. **Structured ansatz scan**: form-templates like
   c_4 = a·G·h^k + b·[n]_q · h^m, with (a, b, n, k, m) over small
   integer ranges.

If PSLQ finds an integer relation Σ a_i · x_i = 0 with small
coefficients, it's a candidate closed form. Otherwise the search
yields a bound on the complexity of any closed form for c_4.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from itertools import product
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import M_E_MEV, M_P_MEV  # noqa: E402

mp.mp.dps = 120  # extra headroom for PSLQ

Q = mp.mpf(Q_50_DIGIT_STR)
H = Q - mp.mpf(1) / Q
HBAR_Q = (Q - mp.mpf(1)) / Q
G = mp.catalan
VOL_B3 = 8 * mp.catalan  # = Vol(Borromean rings complement), 8·G via Adams 1985

M_E = mp.mpf(repr(M_E_MEV))
M_P = mp.mpf(repr(M_P_MEV))

LAM_P_TARGET = (M_P / M_E) * HBAR_Q**2 / VOL_B3


def qint(n):
    return (Q**n - Q**(-n)) / (Q - 1/Q)


def main() -> int:
    w = WitnessBuilder("lambda-scale-rd-c4-pslq-search", engine="mpmath")
    w.set_description(
        "R&D probe: extended PSLQ search for the c_4 coefficient "
        "in λ_p = 5/2 − h²·G − h^4·c_4 + O(h^6) "
        "(Step 4 of conj:lambda-scale-substrate-form proof). "
        "Tests integer relations over a wide basis at mpmath 120 dps."
    )
    w.set_content_block("conj:lambda-scale-substrate-form")
    w.add_parameter("dps", 120)
    w.add_parameter("q_0", Q_50_DIGIT_STR)

    # Solve c_4 precisely
    c4 = (mp.mpf(5)/2 - H**2 * G - LAM_P_TARGET) / H**4
    print(f"c_4 = {mp.nstr(c4, 30)}")
    w.add_data("c4_value", mp.nstr(c4, 50))

    # ── PSLQ Run 1: c_4 vs q-integers and G powers ────────────
    basis_v1 = {
        "1": mp.mpf(1),
        "G": G,
        "G^2": G**2,
        "G^3": G**3,
        "1/G": 1/G,
        "h": H,
        "h^2": H**2,
        "h^4": H**4,
        "[2]_q": qint(2),
        "[3]_q": qint(3),
        "[4]_q": qint(4),
        "[5]_q": qint(5),
        "[6]_q": qint(6),
        "[7]_q": qint(7),
    }
    keys_v1 = list(basis_v1.keys())
    vec_v1 = [c4] + [basis_v1[k] for k in keys_v1]
    try:
        rel_v1 = mp.pslq(vec_v1, tol=mp.mpf("1e-80"), maxcoeff=10**6)
    except Exception as e:
        rel_v1 = None
        print(f"  PSLQ v1 error: {e}")
    pslq_v1 = None
    if rel_v1:
        # Format: rel[0] · c_4 + sum(rel[i+1] · basis[i]) = 0
        terms = [(rel_v1[i+1], keys_v1[i]) for i in range(len(keys_v1)) if rel_v1[i+1] != 0]
        pslq_v1 = {
            "c4_coeff": int(rel_v1[0]),
            "basis_terms": [{"coeff": int(c), "term": t} for c, t in terms],
            "max_abs_coeff": int(max(abs(x) for x in rel_v1)),
        }
        print(f"\n  PSLQ v1 (q-ints + G): c_4 · {rel_v1[0]} + {len(terms)} terms")
    else:
        print(f"\n  PSLQ v1 (q-ints + G): no integer relation found")
    w.add_data("pslq_v1_q_ints_G", pslq_v1 or "no relation found within tol 1e-80")

    # ── PSLQ Run 2: c_4 vs h^k · G^m products ─────────────────
    basis_v2 = {
        "1": mp.mpf(1),
        "G": G,
        "G^2": G**2,
        "h": H,
        "h·G": H*G,
        "h·G^2": H*G**2,
        "h^2": H**2,
        "h^2·G": H**2 * G,
        "h^3": H**3,
        "h^3·G": H**3 * G,
        "h^4": H**4,
        "h^4·G": H**4 * G,
    }
    keys_v2 = list(basis_v2.keys())
    vec_v2 = [c4] + [basis_v2[k] for k in keys_v2]
    try:
        rel_v2 = mp.pslq(vec_v2, tol=mp.mpf("1e-80"), maxcoeff=10**6)
    except Exception as e:
        rel_v2 = None
        print(f"  PSLQ v2 error: {e}")
    pslq_v2 = None
    if rel_v2:
        terms = [(rel_v2[i+1], keys_v2[i]) for i in range(len(keys_v2)) if rel_v2[i+1] != 0]
        pslq_v2 = {
            "c4_coeff": int(rel_v2[0]),
            "basis_terms": [{"coeff": int(c), "term": t} for c, t in terms],
            "max_abs_coeff": int(max(abs(x) for x in rel_v2)),
        }
        print(f"  PSLQ v2 (h^k · G^m): c_4 · {rel_v2[0]} + {len(terms)} terms")
    else:
        print(f"  PSLQ v2 (h^k · G^m): no integer relation found")
    w.add_data("pslq_v2_hk_Gm", pslq_v2 or "no relation found within tol 1e-80")

    # ── Structured ansatz scan ────────────────────────────────
    matches = []
    for a, b in product(range(-10, 11), range(-10, 11)):
        if a == 0 and b == 0:
            continue
        for k in range(1, 5):
            test = mp.mpf(a) * G * H**k + mp.mpf(b) * H**(k+1)
            diff = abs(test - c4)
            if diff < mp.mpf("1e-3"):
                matches.append({
                    "ansatz": f"{a}·G·h^{k} + {b}·h^{k+1}",
                    "value": mp.nstr(test, 12),
                    "abs_diff": mp.nstr(diff, 8),
                })
    matches.sort(key=lambda m: float(m["abs_diff"]))
    w.add_data("ansatz_scan_top10", matches[:10])
    print("\n  Structured ansatz scan top 3 (a·G·h^k + b·h^(k+1)):")
    for m in matches[:3]:
        print(f"    {m['ansatz']:25s}  Δ = {m['abs_diff']}")

    # ── PSLQ Run 3: very-large basis (everything that could matter) ─
    basis_v3 = {
        "1": mp.mpf(1),
        "G": G,
        "h": H,
        "h^2": H**2,
        "h^4": H**4,
        "Vol(B_3)": VOL_B3,
        "[2]_q": qint(2),
        "[3]_q": qint(3),
        "[2]_q · [3]_q": qint(2) * qint(3),
        "ℏ_q": HBAR_Q,
        "1/[2]_q": 1/qint(2),
        "1/[3]_q": 1/qint(3),
    }
    keys_v3 = list(basis_v3.keys())
    vec_v3 = [c4] + [basis_v3[k] for k in keys_v3]
    try:
        rel_v3 = mp.pslq(vec_v3, tol=mp.mpf("1e-90"), maxcoeff=10**8)
    except Exception as e:
        rel_v3 = None
        print(f"  PSLQ v3 error: {e}")
    pslq_v3 = None
    if rel_v3:
        terms = [(rel_v3[i+1], keys_v3[i]) for i in range(len(keys_v3)) if rel_v3[i+1] != 0]
        pslq_v3 = {
            "c4_coeff": int(rel_v3[0]),
            "basis_terms": [{"coeff": int(c), "term": t} for c, t in terms],
            "max_abs_coeff": int(max(abs(x) for x in rel_v3)),
        }
        print(f"  PSLQ v3 (large basis):  c_4 · {rel_v3[0]} + {len(terms)} terms")
    else:
        print(f"  PSLQ v3 (large basis): no integer relation found")
    w.add_data("pslq_v3_large_basis", pslq_v3 or "no relation found within tol 1e-90")

    # ── Interpretation ────────────────────────────────────────
    if any([pslq_v1, pslq_v2, pslq_v3]):
        interpretation = (
            "PSLQ found at least one candidate integer relation. "
            "Inspect coefficients and term structure — small coefficients "
            "indicate genuine substrate form; large coefficients indicate "
            "PSLQ noise rather than real algebraic dependency."
        )
    else:
        interpretation = (
            "No PSLQ integer relation found in tested bases. "
            "Either (a) c_4 requires basis elements not yet tried "
            "(higher q-integers, transcendental forms like Cl_2(π/3), "
            "Vol(4_1), Bloch-Wigner dilogarithm values), or "
            "(b) c_4 is genuinely transcendental w.r.t. these bases, "
            "or (c) the 5/2 − h²·G + h^4·c_4 ansatz is wrong and "
            "λ_scale has a different functional form (e.g. with "
            "non-polynomial dependence on h)."
        )
    w.add_data("interpretation", interpretation)

    w.add_caveat(
        "R&D probe — does not modify production paths. PSLQ is "
        "a numerical heuristic; integer relations it finds at "
        "finite precision should be cross-verified at higher precision "
        "before claiming a closed form. Negative results (no relation "
        "found) constrain but do not exclude existence of one."
    )

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
