#!/usr/bin/env python3
"""Addendum 1 of PREREGISTRATION.md: E1 (conjugacy of the same-chi fibre) and
E2 (P1 extended to length 12). Exact Laurent-polynomial arithmetic only."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from borromean_word_forcing_probe import (  # noqa: E402
    BOR, IDM, T, char, inverse, is_pure, lk_zero, lkey, mmul, orbit,
    reduced_words, show, writhe, self_check)


def mat(word):
    M = IDM
    for c in word:
        M = mmul(M, T[c])
    return tuple(lkey(M[i][j]) for i in range(2) for j in range(2))


def main():
    self_check()
    chi_bor, chi_id = lkey(char(BOR)), lkey(char(()))
    orb = orbit(BOR)
    # all conjugates c beta c^-1, |c| <= 5, beta in orbit -> matrix set
    conj = {}
    for L in range(0, 6):
        for c in reduced_words(L):
            ci = inverse(c)
            for b in orb:
                m = mat(c + b + ci)
                conj.setdefault(m, L)
    out = {"E1": {}, "E2": {}}
    for n in (8, 10):
        same = [w for w in reduced_words(n) if writhe(w) == 0 and lkey(char(w)) == chi_bor]
        found = [conj.get(mat(w)) for w in same]
        miss = [show(w) for w, f in zip(same, found) if f is None]
        hist = {}
        for f in found:
            if f is not None:
                hist[f] = hist.get(f, 0) + 1
        out["E1"][n] = {"same_chi": len(same), "conjugate_found": len(same) - len(miss),
                        "conjugator_length_hist": hist, "not_found": miss[:20],
                        "n_not_found": len(miss)}
        print(f"E1 len {n}: {len(same)} same-chi words, conjugate to beta_Bor found for "
              f"{len(same) - len(miss)}; conjugator lengths {hist}; not found {len(miss)}")
    for n in (10, 12):
        surv, chars = 0, {}
        for w in reduced_words(n):
            if not is_pure(w) or not lk_zero(w):
                continue
            k = lkey(char(w))
            if k == chi_id:
                continue
            surv += 1
            chars.setdefault(k, []).append(w)
        rows = []
        for k, ws in chars.items():
            in_conj = sum(1 for w in ws if mat(w) in conj)
            rows.append({"chi": [list(t) for t in k], "count": len(ws),
                         "is_bor_chi": k == chi_bor, "conjugate_to_bor_found": in_conj,
                         "examples": [show(w) for w in ws[:4]]})
        out["E2"][n] = {"survivors": surv, "distinct_chars": len(chars), "by_char": rows}
        print(f"E2 len {n}: survivors {surv}, distinct chars {len(chars)}")
        for r in rows:
            print("   ", "BOR" if r["is_bor_chi"] else "other", r["count"],
                  "conj-found", r["conjugate_to_bor_found"], r["examples"][:2])
    Path(__file__).with_name("borromean-conjugacy-extension.result.json").write_text(
        json.dumps(out, indent=1, sort_keys=True, default=str))


if __name__ == "__main__":
    main()
