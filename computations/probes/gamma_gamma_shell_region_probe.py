#!/usr/bin/env python3
"""Binding region in photon-colour space, Z = 1..10 (bean qou-mgg1).

Owner choices 2026-11-21: A1 per-atom SDP value = positivity margin
    m(W) = min over λ ⊢ k+1 with at most two rows of χ_λ(W) / dim λ
(positive exactly when reading-3 Frobenius positivity holds); B1 map the
binding region over a φ grid for every Z, to see whether it vanishes and
reopens near Z = 10.

Model, operators and seminormal representations are imported from
gamma_gamma_shell_probe.py. Certified arb arithmetic at the proton q0; a
margin whose interval contains 0 is 'undecided'. φ is a grid variable,
never tuned. No float64.
"""
from __future__ import annotations

import itertools
import json
import sys
import time
from multiprocessing import Pool
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from flint import arb, ctx  # noqa: E402

import gamma_gamma_shell_probe as G  # noqa: E402

ctx.prec = 256
OUT = Path(__file__).with_name("gamma-gamma-shell-region.result.json")
T0 = time.time()
_REPS = {}


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def reps_for(k):
    if k not in _REPS:
        q = arb(G.Q0_STR)
        _REPS[k] = {sh: G.seminormal(sh, q) for sh in G.two_row_partitions(k + 1)}
    return _REPS[k]


def point(args):
    k, phi = args
    ctx.prec = 256
    q = arb(G.Q0_STR)
    ph = tuple(arb(x) for x in phi)
    vals = {}
    for sh, g in reps_for(k).items():
        if not g:
            continue
        vals[str(sh)] = G.trace(G.atom_matrix(g, k, ph, q)) / g[0].nrows()
    m = min(vals.values(), key=lambda v: v.mid())
    # certified sign of the minimum: binds iff every normalised character >= 0
    signs = [G.sign(v) for v in vals.values()]
    if any(s is None for s in signs) and not any(s == -1 for s in signs):
        binds = None
    else:
        binds = all(s is not None and s >= 0 for s in signs)
    argmin = min(vals, key=lambda s: vals[s].mid())
    scale = max((abs(v) for v in vals.values()), key=lambda v: v.mid())
    rel = m / scale
    return {"phi": list(phi), "binds": binds, "margin": m.mid().str(12, radius=False),
            "rel_margin": rel.mid().str(12, radius=False), "argmin_block": argmin}


def main():
    kmax = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    fine = ["-1", "-0.6666666666666666666666666666666666666667", "-0.3333333333333333333333333333333333333333",
            "0", "0.3333333333333333333333333333333333333333", "0.6666666666666666666666666666666666666667", "1"]
    coarse = ["-1", "-0.5", "0", "0.5", "1"]
    rows = []
    with Pool(2) as pool:
        for k in range(1, kmax + 1):
            vals = fine if k <= 8 else coarse
            grid = list(itertools.product(vals, repeat=3))
            res = pool.map(point, [(k, p) for p in grid])
            nb = sum(1 for r in res if r["binds"])
            nu = sum(1 for r in res if r["binds"] is None)
            best = max(res, key=lambda r: float_free_key(r["rel_margin"]))
            bare = next(r for r in res if r["phi"] == ["0", "0", "0"])
            rows.append({"k": k, "grid": len(res), "binding_points": nb, "undecided": nu,
                         "bare_margin": bare["margin"], "bare_binds": bare["binds"],
                         "bare_rel_margin": bare["rel_margin"],
                         "best_rel_margin": best["rel_margin"], "best_phi": best["phi"], "points": res})
            log(f"k={k}: binds {nb}/{len(res)} (undecided {nu}); bare margin {bare['margin'][:10]}; "
                f"bare rel {bare['rel_margin'][:9]}; best rel margin {best['rel_margin'][:9]} at {[p[:5] for p in best['phi']]}")
            OUT.write_text(json.dumps({"model": "docs/audits/2026-11-21-magic-shells-gamma-gamma-model.md",
                                       "margin": "min over <=2-row lambda of chi_lambda(W)/dim lambda",
                                       "q0": G.Q0_STR, "rows": rows}, indent=1))
    log(f"wrote {OUT}")


def float_free_key(s):
    """Sort key from a decimal string without converting through float."""
    from fractions import Fraction
    return Fraction(s)


if __name__ == "__main__":
    main()
