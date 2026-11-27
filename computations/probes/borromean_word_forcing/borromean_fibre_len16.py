#!/usr/bin/env python3
"""Addendum 4 (E5) of PREREGISTRATION.md: same-character fibre and Brunnian
characters at lengths 12 and 14. Depth-first over reduced words, carrying the
(2,1) matrix, strand state and writhe along the prefix. Exact Laurent arithmetic."""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from borromean_word_forcing_probe import (  # noqa: E402
    BOR, IDM, LETTERS, T, char, inverse, ladd, lkey, mmul, orbit, reduced_words,
    self_check, show, components, perm_and_linking)

LENGTHS = (16,)
MAXLEN = max(LENGTHS)


def mat(word):
    M = IDM
    for c in word:
        M = mmul(M, T[c])
    return tuple(lkey(M[i][j]) for i in range(2) for j in range(2))


def main():
    self_check()
    t0 = time.time()
    chi_bor, chi_id = lkey(char(BOR)), lkey(char(()))
    two_sq = {2: 1, 0: 2, -2: 1}
    cb = dict(chi_bor)
    chi_neg = lkey(ladd(ladd({0: 4}, {k: -v for k, v in cb.items()}),
                        {k: -2 * v for k, v in two_sq.items()}))
    orb = orbit(BOR)
    conj = set()
    for L in range(0, 8):
        for c in reduced_words(L):
            ci = inverse(c)
            for b in orb:
                conj.add(mat(c + b + ci))
    print(f"conjugate matrices |c|<=7: {len(conj)}  ({time.time()-t0:.0f}s)", flush=True)

    res = {n: {"same": [], "neg": [], "brunnian_chars": {}} for n in LENGTHS}
    nodes = [0]
    last = [time.time()]

    def dfs(word, M, pos, lk, wr):
        n = len(word)
        nodes[0] += 1
        if nodes[0] % 500000 == 0:
            el = time.time() - t0
            print(f"  nodes {nodes[0]:,}  elapsed {el:.0f}s", flush=True)
        if n in res:
            tr = lkey(ladd(M[0][0], M[1][1]))
            if wr == 0:
                if tr == chi_bor:
                    res[n]["same"].append(word)
                elif tr == chi_neg:
                    res[n]["neg"].append(word)
            if pos == (0, 1, 2) and lk == (0, 0, 0) and tr != chi_id:
                d = res[n]["brunnian_chars"]
                if tr not in d:
                    d[tr] = [0, word]
                d[tr][0] += 1
        if n == MAXLEN:
            return
        # prune: writhe 0 needed at the end only for fibre; keep all for E4 (pure+lk0 also forces writhe 0)
        if abs(wr) > MAXLEN - n:
            return
        for c in LETTERS:
            if word and word[-1][0] == c[0] and word[-1][1] == -c[1]:
                continue
            g, s = c
            p = list(pos)
            a, b = p[g], p[g + 1]
            p[g], p[g + 1] = b, a
            pair = tuple(sorted((a, b)))
            idx = {(0, 1): 0, (0, 2): 1, (1, 2): 2}[pair]
            l2 = list(lk)
            l2[idx] += s
            dfs(word + (c,), mmul(M, T[c]), tuple(p), tuple(l2), wr + s)

    dfs((), IDM, (0, 1, 2), (0, 0, 0), 0)
    out = {}
    for n in LENGTHS:
        same = res[n]["same"]
        miss = [w for w in same if mat(w) not in conj]
        miss_data = {}
        for w in miss:
            _, l2 = perm_and_linking(w)
            k = str((components(w), sorted(l2.values())))
            miss_data.setdefault(k, []).append(show(w))
        bc = res[n]["brunnian_chars"]
        out[n] = {"same_chi": len(same), "minus_tr": len(res[n]["neg"]),
                  "conjugate_found": len(same) - len(miss), "not_found": len(miss),
                  "not_found_by_closure": {k: {"count": len(v), "examples": v[:5]}
                                           for k, v in miss_data.items()},
                  "brunnian_distinct_chars": len(bc),
                  "brunnian_chars": [{"count": v[0], "example": show(v[1]),
                                      "is_bor": k == chi_bor,
                                      "chi": [list(t) for t in k]} for k, v in bc.items()]}
        print(f"E3 len {n}: same chi {len(same)}, -tr {len(res[n]['neg'])}, "
              f"conjugate found {len(same)-len(miss)}, not found {len(miss)} {list(miss_data)}")
        print(f"E4 len {n}: distinct Brunnian chars {len(bc)}: "
              + "; ".join(f"{v[0]}x {show(v[1])}{' (BOR)' if k == chi_bor else ''}" for k, v in bc.items()))
    print(f"nodes {nodes[0]:,}, wall {time.time()-t0:.0f}s")
    Path(__file__).with_name("borromean-fibre-len16.result.json").write_text(
        json.dumps(out, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
