#!/usr/bin/env python3
"""gg_four_strand_pure_long_q0_probe.py — does pure ⟺ pass persist at q₀ for long γγ words? (amendment 4)

Bean qou-a1hh. Convention D, proton q₀. Reuses the amendment-3 independent seminormal representation
(mpmath, 40 dps, no float). Readouts R1 (exhaustive m = 7, 8), R2 (powers u^k of pure u, |u| = 3..6,
k = 1..10), R3 (seeded samples, m = 10..30), as pre-registered in preregistration.md (amendment 4).
Nothing fitted or selected. Scope (a).
-- Ref: [manuscript] bean qou-a1hh
"""
from __future__ import annotations

import itertools
import random
import sys
import time
from pathlib import Path

import mpmath as mp

mp.mp.dps = 40
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import gg_four_strand_pure_threshold_probe as a3  # noqa: E402

from qou_substrate.witness import WitnessBuilder  # noqa: E402

TOL = mp.mpf(10) ** -30
TYPES = a3.TYPES
SHAPES = a3.SHAPES
LAMS = SHAPES[4]


class Eval:
    """Level characters from a per-irrep product, at fixed q = q₀."""

    def __init__(self, q):
        self.q = q
        self.rep = a3.Rep(q)
        self.idx = {}
        for m in range(1, 5):
            for mu in SHAPES[m]:
                self.idx[(m, mu)] = {lam: [a for a, t in enumerate(a3.TAB[lam]) if a3.restricted(t, m) == mu]
                                     for lam in LAMS}
        self.w = {(m, mu): {lam: a3.y(lam, q) / a3.y(mu, q) for lam in LAMS} for (m, mu) in self.idx}

    def chars_from(self, W):
        out = {}
        for key, sel in self.idx.items():
            out[key] = mp.fsum(self.w[key][lam] * mp.fsum(W[lam][a, a] for a in sel[lam]) for lam in LAMS)
        return out

    def product(self, ts):
        W = {lam: mp.eye(len(a3.TAB[lam])) for lam in LAMS}
        for t in ts:
            for lam in LAMS:
                W[lam] = W[lam] * self.rep.vert(lam, t)
        return W

    def minchar(self, ts):
        c = self.chars_from(self.product(ts))
        k = min(c, key=c.get)
        return c[k], k


def is_pure(ts):
    return a3.perm(ts) == (0, 1, 2, 3)


def r1(ev, m):
    """Exhaustive over 4^m words by DFS with shared prefix products."""
    counts = {"pure_pass": 0, "pure_fail": 0, "nonpure_pass": 0, "nonpure_fail": 0}
    worst_pure = (mp.inf, None)
    nonpure_passers = []
    I = {lam: mp.eye(len(a3.TAB[lam])) for lam in LAMS}

    def rec(prefix, W):
        nonlocal worst_pure
        if len(prefix) == m:
            c = ev.chars_from(W)
            v = min(c.values())
            ok = v >= -TOL
            p = is_pure(prefix)
            counts[("pure_" if p else "nonpure_") + ("pass" if ok else "fail")] += 1
            if p and v < worst_pure[0]:
                worst_pure = (v, ".".join(prefix))
            if ok and not p:
                nonpure_passers.append(".".join(prefix))
            return
        for t in TYPES:
            rec(prefix + (t,), {lam: W[lam] * ev.rep.vert(lam, t) for lam in LAMS})

    rec((), I)
    return {"counts": counts, "min_char_over_pure": mp.nstr(worst_pure[0], 15), "argmin_pure": worst_pure[1],
            "nonpure_passers": nonpure_passers}


def charpoly_roots(A):
    """Eigenvalues via the characteristic polynomial (QR in mp.eig fails on near-identity matrices)."""
    n = A.rows
    if n == 2:
        c = [1, -(A[0, 0] + A[1, 1]), mp.det(A)]
    else:
        t = A[0, 0] + A[1, 1] + A[2, 2]
        s2 = (A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0] + A[0, 0] * A[2, 2] - A[0, 2] * A[2, 0]
              + A[1, 1] * A[2, 2] - A[1, 2] * A[2, 1])
        c = [1, -t, s2, -mp.det(A)]
    try:
        return mp.polyroots(c, maxsteps=2000, extraprec=400)
    except mp.NoConvergence:
        # repeated roots: report the characteristic-polynomial coefficients instead
        return ["charpoly"] + [mp.mpf(x) if not isinstance(x, int) else x for x in c]


def r2(ev):
    rows = []
    for L in range(3, 7):
        for u in itertools.product(TYPES, repeat=L):
            if not is_pure(u):
                continue
            U = ev.product(u)
            P = {lam: mp.eye(len(a3.TAB[lam])) for lam in LAMS}
            first_fail, mins = None, []
            for k in range(1, 11):
                P = {lam: P[lam] * U[lam] for lam in LAMS}
                v = min(ev.chars_from(P).values())
                mins.append(v)
                if v < -TOL and first_fail is None:
                    first_fail = k
            eig = {}
            for lam in [(3, 1), (2, 2)]:
                eig[str(lam)] = [e if isinstance(e, str) else mp.nstr(e, 8) for e in charpoly_roots(U[lam])]
            rows.append({"u": ".".join(u), "first_fail_k": first_fail, "min_char_k10": mp.nstr(mins[-1], 10),
                         "min_over_k": mp.nstr(min(mins), 10), "eig": eig})
    return rows


def sample(rng, m, n, pure):
    out, seen = [], set()
    while len(out) < n:
        ts = tuple(rng.choice(TYPES) for _ in range(m))
        if is_pure(ts) == pure and ts not in seen:
            seen.add(ts)
            out.append(ts)
    return out


def r3(ev):
    rows = {}
    for m in (10, 12, 16, 20, 24, 30):
        row = {}
        for pure, seed in ((True, 0), (False, 1)):
            words = sample(random.Random(seed * 1000 + m), m, 2000, pure)
            fails, vmin, arg = 0, mp.inf, None
            for ts in words:
                v, _ = ev.minchar(ts)
                if v < -TOL:
                    fails += 1
                if v < vmin:
                    vmin, arg = v, ".".join(ts)
            row["pure" if pure else "nonpure"] = {"n": len(words), "fail": fails, "pass": len(words) - fails,
                                                   "min_char": mp.nstr(vmin, 12), "argmin": arg}
        rows[str(m)] = row
        print("R3", m, row["pure"]["fail"], row["nonpure"]["pass"], flush=True)
    return rows


def main() -> int:
    t0 = time.time()
    ev = Eval(a3.Q0)
    rel = a3.check_relations(ev.rep)
    print("relations err at q0:", mp.nstr(rel, 5), flush=True)
    if rel > mp.mpf(10) ** -30:
        return 1
    out = {"R1": {}}
    for m in (7, 8):
        out["R1"][str(m)] = r1(ev, m)
        c = out["R1"][str(m)]
        print("R1", m, c["counts"], "minpure", c["min_char_over_pure"], f"{time.time()-t0:.0f}s", flush=True)
    out["R2"] = r2(ev)
    nf = sum(1 for r in out["R2"] if r["first_fail_k"] is not None)
    print("R2 pure u with a failing power:", nf, "of", len(out["R2"]), f"{time.time()-t0:.0f}s", flush=True)
    out["R3"] = r3(ev)
    wb = WitnessBuilder("gg-four-strand-pure-long-q0", engine="mpmath", output_dir=HERE)
    wb.add_assertion("H4_relations_at_q0_below_1e-30", computed="1" if rel < mp.mpf(10) ** -30 else "0",
                     expected="1", source="a3.check_relations")
    wb.save({"q0Anchor": "proton", "q0AnchorReason": "via h2_one_rule (cf.Q, proton pin)",
             "description": "PROBE (bean qou-a1hh, amendment 4): pure <=> pass at q0 for long gg words on 4 strands. "
                            "Scope (a); nothing wired.",
             "weight_family": "markov_y_lambda_convention_D", "relations_err_q0": mp.nstr(rel, 5),
             "results": out})
    print(f"done {time.time()-t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
