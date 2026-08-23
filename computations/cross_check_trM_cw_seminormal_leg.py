#!/usr/bin/env python3
"""L1 defense-in-depth: a genuinely-independent THIRD method for the
color-weighted atomic Markov trace tr_M(β_atom) at q_0.

Motivation.  The L1 1ppQ certification (docs/audits/2026-07-13-l1-4he-
certification-complete.md) rests on `markov_peel` (Markov-axiom recursive
ascent) and the chi-cache combiner.  This adds a third path built on a
different decomposition — the **Wedderburn/seminormal** one:

    tr_M(β_atom) = | Σ_λ  y_λ(q_0) · χ_λ(β_atom) |

with χ_λ from the Hoefsmit **seminormal** engine
(`pyhecke_native.chi_lambda_all_partitions_mpfr`) and the color-weighted
p-n seam handled by the exact two-branch identity

    σ − h(½ − δ/4)·𝟙  =  a_cw·σ + b_cw·σ⁻¹,   a_cw,b_cw = ½ ± δ/4,

so χ_λ(color-weighted word) = a_cw·χ_λ(σ-branch) + b_cw·χ_λ(σ⁻¹-branch)
by linearity.  Agreement with the peel reference at 1ppQ is a genuinely
independent confirmation of the χ engine + the color-weighting.

CRITICAL — exact δ.  The color split MUST use the **exact** symbolic
δ = (q−1)²(1−q⁻⁴)/3 evaluated at q_0 (the form used by
`markov_peel._color_delta`), NOT `canonical_braid_crossings._avg_color_delta`
which is `flavor_split_leading` — a LEADING-order approximation that differs
from the exact δ by ~3.2e-7 and would cap agreement at ~5.86e-11 (well above
1ppQ).  See docs/audits/2026-07-18-l1-third-method-cw-seminormal.md.

Scope-(a); audit-only; no fit; nothing wired to an observable.  The peel
reference is loaded from `markov/markov-peel-atomic-tr-m.witness.json` so
this cross-check tracks it automatically.
"""
from __future__ import annotations

import datetime
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("QOU_Q0_ANCHOR", "ideal")

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE.parent / "tools" / "qou-substrate" / "python"))
sys.path.insert(0, str(HERE.parent / "tools" / "pyhecke" / "python"))

import mpmath as mp  # noqa: E402

import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

import pyhecke_native as pn  # noqa: E402
import hecke_core  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402

TOLERANCE_PPQ = mp.mpf("1e-15")
# (Z, N) → canonical atom name (matches the peel witness rows).
ATOMS = [("proton", 1, 0), ("neutron", 0, 1), ("deuteron", 1, 1),
         ("triton", 1, 2), ("helium-3", 2, 1), ("helium-4", 2, 2)]


def load_q() -> str:
    d = json.loads((HERE / "q-pinning-50-digit.witness.json").read_text())
    q = d["derived_50_digit"]["q"]
    assert q.startswith("1.109978595557"), q
    return q


def load_peel_reference() -> dict[tuple, mp.mpf]:
    """|tr_M(β_atom)| per (Z, N) from the canonical peel witness."""
    w = json.loads((HERE / "markov" / "markov-peel-atomic-tr-m.witness.json").read_text())
    rows = w.get("data", {}).get("results") or w.get("results")
    out = {}
    for r in rows:
        v = r["tr_M_at_q0"]
        vs = v if isinstance(v, str) else (v.get("value") if isinstance(v, dict) else str(v))
        out[(r["Z"], r["N"])] = abs(mp.mpf(vs))
    return out


def classify(triples, h_num: float):
    """(c, d, gen) → seminormal factor kind. Loose tol (peel convention)."""
    out = []
    for (c, d, g0) in triples:
        df = float(d)
        if abs(df) < 1e-6:
            out.append(("s", g0))
        elif abs(df + h_num) < 1e-6:
            out.append(("i", g0))
        elif abs(df + h_num / 2) < 1e-6:
            out.append(("a", g0))
        else:
            out.append(("cw", g0))          # color-weighted p-n seam
    return out


def cw_trM(Z: int, N: int, q_str: str, q0: "mp.mpf", a_cw, b_cw) -> "mp.mpf":
    n = 3 * (Z + N)
    kinds = classify(atom_braid_word_3A(Z, N, include_inter=True),
                     float(hecke_core.h))

    def signed(br):
        return [{"s": (1, g + 1), "i": (-1, g + 1), "a": (0, g + 1),
                 "cw": (br, g + 1)}[k] for (k, g) in kinds]

    y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, q0).items()}
    branch = {br: {tuple(l): mp.mpf(c) for l, c in
                   pn.chi_lambda_all_partitions_mpfr(n, signed(br), q_str, 50)}
              for br in (1, -1)}
    chi = {l: a_cw * branch[1][l] + b_cw * branch[-1][l] for l in branch[1]}
    # mp.fsum (not built-in sum): tr_M = Σ y_λ χ_λ has sign cancellation
    # (χ_λ can be negative), so accurate summation matters at 1ppQ.
    return abs(mp.fsum(y[l] * chi[l] for l in chi))


def main() -> int:
    t0 = time.time()
    q_str = load_q()
    q0 = mp.mpf(q_str)
    # EXACT symbolic color split at q_0 (markov_peel convention).
    delta = (q0 - 1) ** 2 * (1 - q0 ** (-4)) / 3
    a_cw, b_cw = mp.mpf(1) / 2 + delta / 4, mp.mpf(1) / 2 - delta / 4
    peel = load_peel_reference()

    rows, worst = [], mp.mpf(0)
    for name, Z, N in ATOMS:
        ta = time.time()
        trM = cw_trM(Z, N, q_str, q0, a_cw, b_cw)
        ref = peel[(Z, N)]
        rel = abs(trM - ref) / ref
        worst = max(worst, rel)
        rows.append({"atom": name, "Z": Z, "N": N, "A": Z + N,
                     "trM_cw_seminormal": mp.nstr(trM, 40),
                     "peel_reference": mp.nstr(ref, 40),
                     "rel_diff": mp.nstr(rel, 4),
                     "within_1ppQ": bool(rel < TOLERANCE_PPQ)})
        print(f"  {name:9} A={Z+N}  |Δ|/ref={float(rel):.2e}  "
              f"{'OK' if rel < TOLERANCE_PPQ else 'FAIL'}  [{time.time()-ta:.0f}s]",
              flush=True)

    all_ok = all(r["within_1ppQ"] for r in rows)
    wit = {
        "computation": "cross-check-trM-cw-seminormal",
        "description": "L1 defense-in-depth THIRD method: color-weighted "
                       "Wedderburn/seminormal tr_M(beta_atom) with exact "
                       "delta=(q-1)^2(1-q^-4)/3, cross-checked vs the "
                       "markov_peel reference at 1ppQ. Genuinely independent "
                       "decomposition (Sigma y_lambda chi_lambda) from peel's "
                       "Markov-axiom recursion.",
        "audit_only": True,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "pyhecke_native seminormal-mpfr 50dps (chi_lambda_all_"
                  "partitions_mpfr); two-branch color-weighting with exact "
                  "symbolic delta.",
        "dps": 50,
        "q_pin": {"used": "canonical muon (QOU_Q0_ANCHOR=ideal)", "value": q_str},
        "exact_delta_at_q0": mp.nstr(delta, 40),
        "tolerance_1ppQ": mp.nstr(TOLERANCE_PPQ, 2),
        "worst_rel_diff": mp.nstr(worst, 6),
        "results": rows,
        "scope": "(a) — independent third method for the L1 color-weighted "
                 "atomic trace; no AME input; no fit; nothing wired.",
        "assertions": [
            {"label": "all 6 atoms agree with peel at 1ppQ (rel < 1e-15)",
             "passed": all_ok},
            {"label": "exact symbolic delta used (not flavor_split_leading)",
             "passed": True},
        ],
    }
    wit["allPassed"] = all(a["passed"] for a in wit["assertions"])
    out = HERE / "cross-check-trM-cw-seminormal.witness.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(wit, f, indent=1)
    print(f"\nworst |Δ|/ref = {float(worst):.2e}  ({'ALL 1ppQ' if all_ok else 'FAIL'})")
    print(f"witness -> {out.name}  allPassed: {wit['allPassed']}  "
          f"({time.time()-t0:.0f}s)")
    return 0 if wit["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
