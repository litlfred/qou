#!/usr/bin/env python3
"""gg_four_strand_pure_threshold_probe.py — q-threshold of reading 3 on pure γγ words (amendment 3).

Bean qou-a1hh. Convention D, proton q₀. Independent Hoefsmit seminormal representation of H₄(q) at
variable q (mpmath, 40 dps, no float). Pre-registered in preregistration.md (amendment 3).
Nothing fitted or selected; the threshold is a readout. Scope (a).
-- Ref: [manuscript] bean qou-a1hh
"""
from __future__ import annotations

import itertools
import json
import random
import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 40
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_one_rule"))
import h2_one_rule_probe as base  # noqa: E402

from qou_substrate.witness import WitnessBuilder  # noqa: E402

Q0 = base.Q
TYPES = ["V0", "B0", "V1", "B1"]
SHAPES = {1: [(1,)], 2: [(2,), (1, 1)], 3: [(3,), (2, 1)], 4: [(4,), (3, 1), (2, 2)]}


def syts(shape):
    """Standard Young tableaux as lists: pos[e] = (row, col) of entry e = 1..n."""
    n = sum(shape)
    out = []

    def rec(filled, e, pos):
        if e > n:
            out.append(dict(pos))
            return
        for r in range(len(shape)):
            c = filled[r]
            if c < shape[r] and (r == 0 or filled[r - 1] > c):
                filled[r] += 1
                pos[e] = (r, c)
                rec(filled, e + 1, pos)
                filled[r] -= 1
                del pos[e]

    rec([0] * len(shape), 1, {})
    return out


TAB = {lam: syts(lam) for lam in SHAPES[4]}


def gens(lam, q):
    """Seminormal σ_i (i = 1..3), eigenvalues q, −1/q, in the GT basis of λ ⊢ 4."""
    T = TAB[lam]
    d = len(T)
    G = []
    for i in range(1, 4):
        M = mp.zeros(d, d)
        for a, t in enumerate(T):
            (r1, c1), (r2, c2) = t[i], t[i + 1]
            dist = (c2 - r2) - (c1 - r1)
            qa = q ** (2 * dist)
            M[a, a] = (q - 1 / q) * qa / (qa - 1)
            if r1 != r2 and c1 != c2:
                s = dict(t)
                s[i], s[i + 1] = t[i + 1], t[i]
                b = T.index(s)
                qb = q ** (-2 * dist)
                ab = (q - 1 / q) * qb / (qb - 1)
                # off-diagonal: b_{T→sT}·b_{sT→T} = a_T a_{sT} + 1 ; take 1 when T < sT
                M[b, a] = 1 if a < b else M[a, a] * ab + 1
        G.append(M)
    return G


def y(lam, q):
    lam = tuple(lam) + (0,) * (2 - len(lam))
    qi = lambda k: (q ** k - q ** (-k)) / (q - 1 / q)
    return qi(lam[0] - lam[1] + 1) / qi(2) ** (lam[0] + lam[1])


def restricted(t, m):
    r = [0, 0]
    for e in range(1, m + 1):
        r[t[e][0]] += 1
    return (r[0], r[1]) if r[1] else (r[0],)


class Rep:
    def __init__(self, q):
        self.q = q
        self.G = {lam: gens(lam, q) for lam in SHAPES[4]}
        h = q - 1 / q
        self.Gi = {lam: [g - h * mp.eye(len(TAB[lam])) for g in gs] for lam, gs in self.G.items()}
        self.V = {(lam, t): self._vert(lam, t) for lam in SHAPES[4] for t in TYPES}

    def vert(self, lam, t):
        return self.V[(lam, t)]

    def _vert(self, lam, t):
        o, s = t[0], int(t[1])
        G, Gi = self.G[lam], self.Gi[lam]
        return G[s] * Gi[s + 1] if o == "V" else Gi[s] * G[s + 1]

    def chars(self, ts):
        diag = {}
        for lam in SHAPES[4]:
            W = mp.eye(len(TAB[lam]))
            for t in ts:
                W = W * self.vert(lam, t)
            diag[lam] = [W[a, a] for a in range(len(TAB[lam]))]
        out = {}
        for m in range(1, 5):
            for mu in SHAPES[m]:
                acc = mp.mpf(0)
                for lam in SHAPES[4]:
                    s = mp.fsum(v for v, t in zip(diag[lam], TAB[lam]) if restricted(t, m) == mu)
                    acc += y(lam, self.q) / y(mu, self.q) * s
                out[(m, mu)] = acc
        return out


def check_relations(rep):
    err = mp.mpf(0)
    for lam, G in rep.G.items():
        I = mp.eye(len(TAB[lam]))
        for g in G:
            err = max(err, mp.mnorm((g - rep.q * I) * (g + I / rep.q), 1))
        err = max(err, mp.mnorm(G[0] * G[1] * G[0] - G[1] * G[0] * G[1], 1))
        err = max(err, mp.mnorm(G[1] * G[2] * G[1] - G[2] * G[1] * G[2], 1))
        err = max(err, mp.mnorm(G[0] * G[2] - G[2] * G[0], 1))
    return err


def perm(ts):
    p = list(range(4))
    for t in ts:
        s = int(t[1]) + 1
        for g in (s, s + 1):
            p[g - 1], p[g] = p[g], p[g - 1]
    return tuple(p)


def minchar(ts, q):
    c = Rep(q).chars(ts)
    k = min(c, key=c.get)
    return c[k], k


def threshold(ts, lo=mp.mpf(1), hi=mp.mpf(2), step=mp.mpf("0.001")):
    q = lo + step
    while q <= hi:
        v, _ = minchar(ts, q)
        if v < 0:
            a, b = q - step, q
            for _ in range(40):
                mid = (a + b) / 2
                if minchar(ts, mid)[0] < 0:
                    b = mid
                else:
                    a = mid
            return b, minchar(ts, b)[1]
        q += step
    return None, None


def main() -> int:
    rep0 = Rep(Q0)
    rel = check_relations(rep0)
    print("relations err at q0:", mp.nstr(rel, 5))
    ref = json.loads((HERE / "gg-four-strand.witness.json").read_text())["results"]
    t2 = rel < mp.mpf(10) ** -30
    for m in range(1, 7):
        for ts in itertools.product(TYPES, repeat=m):
            c = rep0.chars(ts)
            r = ref[".".join(ts)]
            ok = all(v >= -mp.mpf(10) ** -30 for v in c.values())
            if ok != r["passes_alone"] or abs(min(c.values()) - mp.mpf(r["min_char"])) > mp.mpf(10) ** -6:
                t2 = False
                print("T2 mismatch", ts, mp.nstr(min(c.values()), 10), r)
                break
        if not t2:
            break
    print(f"[{'PASS' if t2 else 'FAIL'}] T2 independent rep reproduces the witness")
    if not t2:
        return 1
    rows = {}
    rng = random.Random(0)
    for m in [int(x) for x in sys.argv[1:]] or (3, 4, 5, 6, 9, 12):
        if m <= 6:
            words = [ts for ts in itertools.product(TYPES, repeat=m) if perm(ts) == (0, 1, 2, 3)]
            mode = "exhaustive"
        else:
            words, seen = [], set()
            while len(words) < 2000:
                ts = tuple(rng.choice(TYPES) for _ in range(m))
                if perm(ts) == (0, 1, 2, 3) and ts not in seen:
                    seen.add(ts)
                    words.append(ts)
            mode = "sample-2000-seed0"
        best = None
        q = mp.mpf(1)
        step = mp.mpf("0.001")
        while best is None and q < 2:
            q += step
            rep = Rep(q)
            failing = [ts for ts in words if min(rep.chars(ts).values()) < 0]
            if failing:
                cands = []
                for ts in failing:
                    a, b = q - step, q
                    for _ in range(40):
                        mid = (a + b) / 2
                        if minchar(ts, mid)[0] < 0:
                            b = mid
                        else:
                            a = mid
                    cands.append((b, minchar(ts, b)[1], ts))
                best = min(cands, key=lambda c: c[0])
        if best is None:
            rows[m] = {"mode": mode, "n_words": len(words), "q_star_min": None}
            print(m, mode, len(words), "no failure on [1,2]")
            continue
        rows[m] = {"mode": mode, "n_words": len(words), "q_star_min": mp.nstr(best[0], 15),
                   "m_times_excess": mp.nstr(m * (best[0] - 1), 10), "first_failing_char": str(best[1]),
                   "minimiser": ".".join(best[2])}
        print(m, rows[m], flush=True)
        print('progress: m done', m, flush=True)
    wb = WitnessBuilder("gg-four-strand-pure-threshold", engine="mpmath", output_dir=HERE)
    wb.add_assertion("T2_independent_rep_reproduces_witness", computed="1", expected="1",
                     source="gg-four-strand.witness.json")
    wb.save({"q0Anchor": "proton", "q0AnchorReason": "via h2_one_rule (cf.Q, proton pin)",
             "description": "PROBE (bean qou-a1hh, amendment 3): q-threshold of reading 3 on pure gg words on "
                            "4 strands; independent seminormal rep at variable q. Scope (a); nothing wired.",
             "weight_family": "markov_y_lambda_convention_D", "relations_err_q0": mp.nstr(rel, 5),
             "results": {str(k): v for k, v in rows.items()}})
    return 0


if __name__ == "__main__":
    sys.exit(main())
