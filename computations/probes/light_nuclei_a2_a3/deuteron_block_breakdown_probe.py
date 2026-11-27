"""Deuteron convention-D trace split by Temperley–Lieb cell module (two-row partition) (bean qou-sv7h).

PROBE, adopts nothing. tr(x) = Σ_j [j+1] / [2]⁶ · χ_j(x), χ_j the trace on the cell module of TL_6
with j through-strands (partition ((6+j)/2, (6−j)/2)). Computed exactly in ℚ at rational q for the
free word (proton ⊗ neutron) and the γγ-bonded deuteron word, with the sum checked to equal the
sweep trace exactly. Reports each block's contribution to (tr_atom − tr_free)/tr_free.

Result: the trivial block (6) is untouched by the bond; near q₀ (q = 111/100) the one-box block
(5,1) raises the trace (+0.00488 of tr_free) and (4,2), (3,3) lower it (−0.00377, −0.00050), net
+0.00061 — a small residue of larger cancelling pieces. At q = 3/2 and 2 the pattern changes.

Run: python3 -u deuteron_block_breakdown_probe.py
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import flint  # noqa: E402
import mpmath as mp  # noqa: E402

import hecke_flint as F  # noqa: E402
import hecke_tl as T  # noqa: E402

mp.mp.dps = 40
n = 6


def link_states(n, j):
    """Planar link states on n points with j defects: tuple s, s[p] = partner or -1 (defect)."""
    out = []

    def rec(p, s, stack):
        if p == n:
            if not stack and s.count(-1) == j:
                out.append(tuple(s))
            return
        # defect: only if no open arc
        if not stack:
            rec(p + 1, s + [-1], stack)
        # open
        rec(p + 1, s + [None], stack + [p])
        # close
        if stack:
            o = stack[-1]
            s2 = s + [o]
            s2[o] = p
            rec(p + 1, s2, stack[:-1])
    rec(0, [], [])
    return out


def act(t, s, n):
    """D (tuple t: top 0..n-1, bottom n..2n-1) applied to link state s glued at its bottom.
    Returns (new state, closed loops) or None if a through-strand is lost."""
    res = [None] * n
    vis = set()  # visited bottom points
    for p in range(n):
        if res[p] is not None:
            continue
        cur = t[p]
        while True:
            if cur < n:
                res[p], res[cur] = cur, p
                break
            b = cur - n
            vis.add(b)
            if s[b] == -1:
                res[p] = -1
                break
            vis.add(s[b])
            cur = t[n + s[b]]
    loops = 0
    for b in range(n):
        if b in vis:
            continue
        if s[b] == -1:
            return None  # this defect is joined to another defect through D: lost
        # walk the component; it can only be a loop or end at a defect (both ends then defects)
        cur, closed = b, True
        while True:
            vis.add(cur)
            o = s[cur]
            if o == -1:
                closed = False
                break
            vis.add(o)
            nxt = t[n + o]
            assert nxt >= n
            cur = nxt - n
            if cur == b:
                break
            if cur in vis and s[cur] != -1:
                break
        if not closed:
            return None
        loops += 1
    if res.count(-1) != s.count(-1):
        return None
    return tuple(res), loops


def chars(x, n, R):
    out = {}
    for j in range(n % 2, n + 1, 2):
        sts = link_states(n, j)
        tot = R.zero
        for t, c in x.items():
            k = 0
            for s in sts:
                r = act(t, s, n)
                if r is not None and r[0] == s:
                    f = R.one
                    for _ in range(r[1]):
                        f = f * R.d
                    tot = tot + c * f
        out[j] = tot
    return out


def final_elem(letters, n, R):
    x = {T.identity(n): R.one}
    m = n
    for kind, i in letters:
        a = R.coef[kind]
        y = {}
        for t, c in x.items():
            y[t] = y.get(t, R.zero) + a * c
            u, loop = T._mul_e(t, m, i)
            c2 = -c * R.d if loop else -c
            y[u] = y.get(u, R.zero) + c2
        x = y
    return x


def dec(x):
    return mp.nstr(mp.mpf(int(x.p)) / mp.mpf(int(x.q)), 15)


def main():
    words = {"free": F.atom_word("pn", [], "over"), "atom": F.atom_word("pn", [(0, 1)], "over")}
    rows = []
    for qv in (flint.fmpq(111, 100), flint.fmpq(3, 2), flint.fmpq(2)):
        R = T.Ring(qv, flint.fmpq)
        d = qv + 1 / qv
        out = {}
        for name, w in words.items():
            ch = chars(final_elem(w, n, R), n, R)
            ref = T.sweep_trace(T.word_program(n, w), R)[0]
            terms = {j: sum(qv ** (j - 2 * i) for i in range(j + 1)) / d ** n * c for j, c in ch.items()}
            assert sum(terms.values()) == ref, name  # exact
            out[name] = terms
        trf = sum(out["free"].values())
        row = {"q": str(qv), "atom_minus_free_over_trfree": dec((sum(out["atom"].values()) - trf) / trf),
               "blocks": {f"({(n + j) // 2},{(n - j) // 2})": {
                   "free": dec(out["free"][j] / trf), "atom": dec(out["atom"][j] / trf),
                   "diff": dec((out["atom"][j] - out["free"][j]) / trf)} for j in sorted(out["free"])}}
        rows.append(row)
        print(json.dumps(row, ensure_ascii=False))
    w = {"bean": "qou-sv7h", "q0Anchor": "independent",
         "q0AnchorReason": "exact rational q; q = 111/100 is a stand-in near the pin, not the pin",
         "rows": rows, "checks": {"block_sum_equals_sweep_trace_exact": True},
         "note": "PROBE. Block contributions are fractions of tr_free; exact rationals shown to 15 digits."}
    with open(os.path.join(HERE, "deuteron-block-breakdown.witness.json"), "w") as fh:
        json.dump(w, fh, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
