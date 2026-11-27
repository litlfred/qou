#!/usr/bin/env python3
"""merge_cap_census.py — per-word census for the q0 merge cap (bean qou-brng, brief C2 front B).

For every gamma-gamma bond word of the binding-ceiling population (A = 2: lengths 1..L, A = 3:
lengths 1..L), records: reading 3 at the proton-pin q0 (corpus seminormal helpers, convention D),
the failing (level m, two-row mu) cells with their values, classical reading 3 (q = 1, every level,
Young's rule), merges, atom cycle type, and the support-overlap components of the bond word.
Writes a .jsonl census; no selection, no ratio, AME not read. mpmath only.

-- Ref: [leitner2026] bean qou-brng; computations/probes/binding_ceiling_q0/binding_ceiling_q0_probe.py
"""
from __future__ import annotations
import itertools, json, sys, time
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
L = int(sys.argv[1]); A = int(sys.argv[2])
sys.argv = [sys.argv[0], str(L), str(A)]
sys.path.insert(0, str(HERE.parent / "binding_ceiling_q0"))
import binding_ceiling_q0_probe as b  # noqa: E402

N = 3 * A
JUNCTIONS = [{3 * j - 2, 3 * j - 1} for j in range(1, A)]
OUT = HERE / f"merge-cap-census-A{A}-L{L}.jsonl"


def cyc_lengths(p):
    seen, out = [False] * len(p), []
    for i in range(len(p)):
        if not seen[i]:
            ln, j = 0, i
            while not seen[j]:
                seen[j], j, ln = True, p[j], ln + 1
            out.append(ln)
    return sorted(out, reverse=True)


def a_seq(lengths, n):
    a = [1] + [0] * n
    for ln in lengths:
        bb = a[:]
        for k in range(n + 1 - ln):
            bb[k + ln] += a[k]
        a = bb
    return a


def restrict(p, m):
    out = []
    for i in range(m):
        j = p[i]
        while j >= m:
            j = p[j]
        out.append(j)
    return out


def classical_fail_levels(p):
    bad = []
    for m in range(1, N + 1):
        a = a_seq(cyc_lengths(restrict(p, m)), m)
        if not all(a[k] <= a[k + 1] for k in range(m // 2)):
            bad.append(m)
    return bad


def components(w):
    sets = [set(range(s, s + 3)) for s in set(w)]
    comps = []
    for s in sets:
        merged = [c for c in comps if c & s]
        for c in merged:
            comps.remove(c); s |= c
        comps.append(s)
    return sorted(sorted(c) for c in comps)


def main():
    x = [(s + 3 * a, i) for a in range(A) for (s, i) in b.V(0) * 3]
    words = [w for n in range(1, L + 1) for w in itertools.product(range(N - 2), repeat=n)
             if all(J & set(w) for J in JUNCTIONS)]
    t0 = time.time()
    with OUT.open("w") as fh:
        for k, w in enumerate(words, 1):
            K = [lt for s in w for lt in b.V(s)]
            d = b.base.diag_of(b.corpus_letters(x + K), N)
            lc = b.gga.level_chars(d, N, 1)
            fails = {f"{m}:{','.join(map(str, mu))}": mp.nstr(v, 12)
                     for (m, mu), v in lc.items() if v < -b.TOL}
            p = b.perm(x + K)
            rec = {"word": "".join(f"V{s}" for s in w), "gens": list(w),
                   "pass_q0": not fails, "fails_q0": fails,
                   "classical_fail_levels": classical_fail_levels(p),
                   "merges": N - len(cyc_lengths(p)), "cycle_type": cyc_lengths(p),
                   "components": components(w)}
            fh.write(json.dumps(rec) + "\n")
            if k % 200 == 0:
                el = time.time() - t0
                print(f"{k}/{len(words)} {el:.0f}s ETA {el / k * (len(words) - k):.0f}s", flush=True)
    print("done", OUT, flush=True)


if __name__ == "__main__":
    main()
