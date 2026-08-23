#!/usr/bin/env python3
"""
Option E — is the KL left-cell Betti sum CONTRIBUTIVE to deuteron binding?

The deuteron (H_6 / S_6) is the one nucleus whose Kazhdan-Lusztig left-cell
Betti sums B_λ = Σ_{w∈Γ_λ} P_{e,w}(1) are *exactly* computable (no S_12 wall,
no proxy).  This script answers, with a reproducible number, the question:

    "Can KL-Betti be contributive (move B(D) toward AME) even if it does not
     fully close the deuteron?"

It evaluates the Δ_λ binding sum with the SAME primitives as the canonical
producer `delta_lambda_binding_full_evaluation.py` (y_λ Wenzl weights, χ^λ
Hoefsmit+interface character, sgn(w_0^{S_{λ'}}) Macdonald sign), changing ONLY
the per-partition magnitude:

    Σ_f = Σ_λ y_λ · χ^λ(β_D) · sgn(w_0^{S_{λ'}}) · f^λ      (canonical ansatz)
    Σ_b = Σ_λ y_λ · χ^λ(β_D) · sgn(w_0^{S_{λ'}}) · B_λ      (KL-Betti magnitude)

B(D) = m_e · |Σ|.  AME 2020: B(D) = 2.22452 MeV.

Discipline note (AGENTS.md §"Before declaring refuted"): this is a
SCOPE-LIMITED measurement of the size of a candidate contribution, not a
refutation of any ingredient.  B_λ = f^λ on hook partitions (Lean-anchorable
identity); the bulk partitions are where B_λ > f^λ.  We report how much the
deuteron sum actually moves — the honest "contributive vs closing" verdict.

The B_λ computation is identical to the on-main probe
`probe_option_e_probe4_kl_batch.py` (PR #2658): RSK left-cell grouping +
P_{e,w}(1) over the canonical left cell of each shape.
"""
from __future__ import annotations

import json
import math
import time
from pathlib import Path

from mpmath import mp, mpf, fabs

from kazhdan_lusztig import permutations_S_n, kl_polynomial
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
HERE = Path(__file__).resolve().parent

m_e = mpf("0.51099895069")          # CAL-1, matches the canonical producer
B_AME_D = mpf("2.22452")            # AME 2020 deuteron binding (MeV)
N = 6                               # deuteron = H_6 / S_6

# ── KL-Betti helpers (verbatim from probe_option_e_probe4_kl_batch.py) ──────
def rsk(w):
    P, Q = [], []
    for i, x in enumerate(w):
        r = 0
        while r < len(P):
            idx = -1
            for c in range(len(P[r])):
                if P[r][c] > x:
                    idx = c
                    break
            if idx == -1:
                P[r].append(x); Q[r].append(i + 1); break
            else:
                x, P[r][idx] = P[r][idx], x; r += 1
        if r == len(P):
            P.append([x]); Q.append([i + 1])
    return P, Q

def get_shape(P):
    return tuple(len(row) for row in P)

def syt_to_tuple(T):
    return tuple(tuple(row) for row in T)

def canonical_Q(lam):
    Q, counter = [], 1
    for r in lam:
        Q.append(tuple(range(counter, counter + r))); counter += r
    return tuple(Q)

def kl_betti_left_cell_sums(n):
    """B_λ = Σ_{w in canonical left cell Γ_λ} P_{e,w}(1).  Exact for S_n."""
    perms = permutations_S_n(n)
    left_cells = {}
    for w in perms:
        P, Q = rsk(w)
        lam = get_shape(P)
        Q_tup = syt_to_tuple(Q)
        left_cells.setdefault(lam, {}).setdefault(Q_tup, []).append(w)
    e = tuple(range(1, n + 1))
    betti = {}
    for lam, cells in left_cells.items():
        Q_can = canonical_Q(lam)
        if Q_can not in cells:
            Q_can = list(cells.keys())[0]
        s = 0
        for w in cells[Q_can]:
            p = kl_polynomial(e, w)
            s += int(p.subs({sym: 1 for sym in p.free_symbols}))
        betti[lam] = s
    return betti

# ── Δ_λ primitives (verbatim from delta_lambda_binding_full_evaluation.py) ──
def conjugate(lam):
    if not lam:
        return ()
    return tuple(sum(1 for p in lam if p > i) for i in range(lam[0]))

def sgn_conjugate_parabolic(lam):
    """(-1)^{n(λ)} = sgn(w_0^{S_{λ'}}) via Macdonald I.1.5."""
    return math.prod((-1) ** (p * (p - 1) // 2) for p in conjugate(lam))

def dim_sn(lam):
    """f^λ = dim(V_λ) via hook-length formula."""
    n = sum(lam)
    den = 1
    for i in range(len(lam)):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
            den *= arm + leg + 1
    return math.factorial(n) // den

def load_chi(fname):
    d = json.loads((HERE / fname).read_text(encoding="utf-8"))
    atom = d["data"]["atom"]
    return [(tuple(e["partition"]), mpf(str(e["chi_lambda"])))
            for e in atom["by_partition"]]

def load_y(fname):
    d = json.loads((HERE / fname).read_text(encoding="utf-8"))
    return {tuple(e["partition"]): mpf(str(e["y_lambda_at_q0"]))
            for e in d["data"]["per_lambda"]}


def main():
    t0 = time.perf_counter()
    print("=" * 72)
    print("Option E — KL-Betti CONTRIBUTIVE test on the deuteron (S_6, exact)")
    print("=" * 72)

    chi = dict(load_chi("atom-chi-rust-d.witness.json"))
    y = load_y("rho-k-h3a-lp-dual.witness.json")
    print(f"Loaded χ^λ ({len(chi)} partitions), y_λ ({len(y)} partitions)")

    print(f"Computing exact KL left-cell Betti sums for S_{N} ...")
    betti = kl_betti_left_cell_sums(N)

    rows = []
    sum_f = mpf(0)
    sum_b = mpf(0)
    for lam in sorted(chi.keys(), key=lambda t: (-len(t), t)):
        c = chi[lam]
        yl = y.get(lam, mpf(0))
        sgn = sgn_conjugate_parabolic(lam)
        f = dim_sn(lam)
        b = betti.get(lam, f)
        term_f = yl * c * sgn * f
        term_b = yl * c * sgn * b
        sum_f += term_f
        sum_b += term_b
        rows.append((lam, f, b, sgn, float(c), float(yl),
                     float(term_f), float(term_b)))

    B_f = m_e * fabs(sum_f)
    B_b = m_e * fabs(sum_b)

    print()
    hdr = f"{'λ':>14} {'f^λ':>4} {'B_λ':>4} {'sgn':>4} {'χ^λ':>9} " \
          f"{'term(f)':>11} {'term(B)':>11}"
    print(hdr); print("-" * len(hdr))
    for lam, f, b, sgn, c, yl, tf, tb in rows:
        mark = "" if b == f else "  <-bulk"
        print(f"{str(lam):>14} {f:>4} {b:>4} {sgn:>+4} {c:>9.4f} "
              f"{tf:>+11.5f} {tb:>+11.5f}{mark}")

    print()
    print(f"  Σ_f  (f^λ)   = {float(sum_f):>+12.6f}   "
          f"[canonical witness: -0.743901]")
    print(f"  Σ_b  (Betti) = {float(sum_b):>+12.6f}")
    print()
    print(f"  B(D) f^λ     = m_e·|Σ_f| = {float(B_f):>9.5f} MeV  "
          f"({float((B_f-B_AME_D)/B_AME_D*100):+.2f}%)")
    print(f"  B(D) Betti   = m_e·|Σ_b| = {float(B_b):>9.5f} MeV  "
          f"({float((B_b-B_AME_D)/B_AME_D*100):+.2f}%)")
    print(f"  B(D) AME2020 = {float(B_AME_D):>9.5f} MeV")
    print()
    need = B_AME_D / B_f if B_f > 0 else mpf("nan")
    got = B_b / B_f if B_f > 0 else mpf("nan")
    print(f"  factor needed to CLOSE (×):     {float(need):>7.3f}")
    print(f"  factor KL-Betti DELIVERS (×):   {float(got):>7.3f}")
    verdict = ("CONTRIBUTIVE (moves toward AME) but does NOT close"
               if 1.0 < float(got) < float(need) * 0.98
               else "moves AWAY from AME (anti-contributive)"
               if float(got) < 1.0
               else "CLOSES (within ~2%)"
               if abs(float(B_b) - float(B_AME_D)) / float(B_AME_D) < 0.02
               else "overshoots / non-monotone")
    print(f"  VERDICT: KL-Betti is {verdict}.")

    # Sanity: does the f^λ path reproduce the canonical producer's -0.7439?
    repro = abs(float(sum_f) - (-0.7439005054492055)) < 5e-4
    print(f"  [reconstruction check] Σ_f matches canonical -0.743901: {repro}")

    witness = {
        "engine": "python3/mpmath", "engineVersion": "50dps",
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "computation": "option-e-kl-betti-contributive-deuteron",
        "scriptFile": "option_e_kl_betti_contributive_deuteron.py",
        "description": (
            "Scope-limited measurement (AGENTS.md §before-declaring-refuted): "
            "size of the KL left-cell Betti-sum contribution to deuteron "
            "binding vs the canonical f^λ ansatz. NOT a refutation. "
            "B_λ = f^λ on hooks; bulk partitions carry B_λ > f^λ."
        ),
        "data": {
            "nucleus": "D (H_6/S_6)",
            "sum_f_lambda": str(sum_f),
            "sum_betti": str(sum_b),
            "B_D_f_lambda_MeV": str(B_f),
            "B_D_betti_MeV": str(B_b),
            "B_D_AME_MeV": str(B_AME_D),
            "factor_needed_to_close": str(need),
            "factor_betti_delivers": str(got),
            "verdict": verdict,
            "reconstruction_matches_canonical": repro,
            "per_partition": [
                {"partition": list(lam), "f_lambda": f, "betti": b,
                 "sgn": sgn, "chi": c, "y": yl,
                 "term_f": tf, "term_betti": tb}
                for lam, f, b, sgn, c, yl, tf, tb in rows
            ],
        },
        "assertions": [
            {"label": "f^λ path reproduces canonical -0.7439",
             "passed": bool(repro)},
        ],
        "allPassed": bool(repro),
        "wallSeconds": round(time.perf_counter() - t0, 2),
    }
    out = HERE / "option-e-kl-betti-contributive-deuteron.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
    witness["scriptFile"] = _os.path.basename(__file__)
    out.write_text(json.dumps(witness, indent=2, default=str), encoding="utf-8")
    print(f"\nWitness: {out.name}  ({witness['wallSeconds']}s)")


if __name__ == "__main__":
    main()
