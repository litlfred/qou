#!/usr/bin/env python3
"""carbon_ring_stage5_probe.py — stage 5: coarse-grained 6-node cyclic ring vs chain.

Pre-registered in preregistration.md §Stage 5 before this file. One strand per carbon (a stated
coarse-graining). Bonds are Birman-Ko-Lee band generators a_i = sigma_i (i = 0..4) and the closing
bond a_5 = rho sigma_4 rho^-1, rho = sigma_0 ... sigma_4, which crosses strands 0 and 5.
Reading 3 at every level 1..6 (convention D, proton pin, mpmath 40 dps), components, writhe, and the
exact Jones connected part on every 3-component sublink of a pure word. Nothing fitted or selected.
-- Ref: [leitner2026] def:virtual-subword; bean qou-a1hh
"""
from __future__ import annotations

import itertools
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

mp.mp.dps = 40
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_gg_atom"))
sys.path.insert(0, str(HERE))
import h2_gg_atom_probe as ga  # noqa: E402
import borromean_jones_cumulant_probe as bj  # noqa: E402  (exact Kauffman state sum)

base = ga.base
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

ONE, ZERO, H = mp.mpf(1), mp.mpf(0), base.H
N = 6
RHO = [(g, 1) for g in range(5)]


def inv(w):
    return [(g, -s) for g, s in reversed(w)]


def bond(i, e):
    core = [(min(i, 4), 1 if e > 0 else -1)] * abs(e)
    return RHO + core + inv(RHO) if i == 5 else core


def word(pattern, ring):
    w = []
    for i, e in enumerate(pattern):
        if i == 5 and not ring:
            continue
        w += bond(i, e)
    return w


def hecke(w):
    return [(ONE, ZERO, g) if s > 0 else (ONE, -H, g) for g, s in w]


def perm(w):
    p = list(range(N))
    for g, _ in w:
        p[g], p[g + 1] = p[g + 1], p[g]
    return p


def ncycles(p):
    seen, c = set(), 0
    for i in range(N):
        if i not in seen:
            c += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = p[j]
    return c


def phi3(w, q0):
    """Jones connected part on every 3-strand sublink (pure words only)."""
    t = bj.t
    delta = -(sp.sqrt(t) + 1 / sp.sqrt(t))
    J = {}

    def V(T):
        if T not in J:
            sw, k = bj.restrict(w, N, set(T))
            J[T] = sp.simplify(bj.jones(sw, k)) if sw else delta ** (k - 1)
        return J[T]

    def F(T):  # log(delta V / delta^|T|), as a sympy ratio inside the log
        return sp.simplify(V(T) / delta ** (len(T) - 1)) if T else sp.Integer(1)

    out = {}
    for T in itertools.combinations(range(N), 3):
        num, den = sp.Integer(1), sp.Integer(1)  # phi = log(prod F(U)^{sign})
        for r in range(4):
            for U in itertools.combinations(T, r):
                sgn = (-1) ** (3 - r)
                if sgn > 0:
                    num *= F(U)
                else:
                    den *= F(U)
        ratio = sp.factor(sp.simplify(num / den))
        f = sp.lambdify(t, ratio, "mpmath")
        vals = {lab: f(tv) for lab, tv in (("t=q0", q0), ("t=q0^2", q0 ** 2))}
        out[",".join(map(str, T))] = {
            "ratio": str(ratio),
            "exactly_one": bool(sp.simplify(ratio - 1) == 0),
            **{lab: mp.nstr(mp.log(v), 20) if v > 0 else "ratio<=0" for lab, v in vals.items()},
        }
    return out


def main() -> int:
    t0 = time.time()
    q0 = mp.mpf(q_at())
    pats = {}
    for e in (1, 2, -1, -2):
        pats[f"sym({e})"] = (e,) * 6
    pats["alt(2,1)"] = (2, 1) * 3
    pats["alt(1,2)"] = (1, 2) * 3
    pats["alt(-2,-1)"] = (-2, -1) * 3
    pats["alt(-1,-2)"] = (-1, -2) * 3
    rows = {}
    for name, pat in pats.items():
        for ring in (True, False):
            w = word(pat, ring)
            lc = ga.level_chars(base.diag_of(hecke(w), N), N, 1)
            mn = min(lc.values())
            p = perm(w)
            r = {
                "letters": len(w), "writhe": sum(s for _, s in w), "components": ncycles(p),
                "pure": p == list(range(N)), "reading3_every_level": bool(mn > 0),
                "min_level_char": mp.nstr(mn, 20),
                "failing_levels": [f"{m}:{mu}" for (m, mu), v in lc.items() if v <= 0],
                "chi_6": mp.nstr(mp.mpf(q0) ** sum(s for _, s in w), 20),
            }
            if r["pure"]:
                r["phi3"] = phi3(w, q0)
            tag = f"{name},{'ring' if ring else 'chain'}"
            rows[tag] = r
            print(f"{tag}: pass={r['reading3_every_level']} comp={r['components']} wr={r['writhe']} "
                  f"fails={r['failing_levels'][:6]} [{time.time()-t0:.0f}s]", flush=True)
    q1 = {n: (rows[f"{n},ring"]["reading3_every_level"], rows[f"{n},chain"]["reading3_every_level"]) for n in pats}
    print("Q1 ring vs chain pass:", q1)
    nz = {tag: [T for T, v in r["phi3"].items() if not v["exactly_one"]] for tag, r in rows.items() if "phi3" in r}
    print("Q3 nonzero 3-party connected parts:", nz)
    wb = WitnessBuilder("carbon-ring-stage5", engine="mpmath", output_dir=HERE)
    wb.add_assertion("ran_all_patterns", computed=str(len(rows)), expected=str(2 * len(pats)),
                     source="8 exponent patterns x (ring, chain)")
    wb.save({
        "q0Anchor": "proton", "q0AnchorReason": "q_at() (proton pin)",
        "description": "PROBE stage 5 (bean qou-a1hh): coarse-grained 6-node ring (one strand per carbon) "
                       "with BKL band generators vs open chain; reading 3, components, exact Jones 3-party "
                       "connected parts on pure words. Pre-registered.",
        "weight_family": "markov_y_lambda_convention_D",
        "rows": rows, "q1_ring_vs_chain": {k: list(v) for k, v in q1.items()}, "q3_nonzero_phi3": nz,
    })
    return 0


if __name__ == "__main__":
    sys.exit(main())
