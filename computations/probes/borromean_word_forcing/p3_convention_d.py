#!/usr/bin/env python3
"""P3-D (Addendum 3): writhe != 0 trace fibre of beta_Bor under true convention-D
weights y(1^3)=0, y(2,1)=1/[2]^2, y(3)=1-2/[2]^2. Exact sympy, no float."""
import json, sys
from pathlib import Path
import sympy as sp
sys.path.insert(0, str(Path(__file__).parent))
from borromean_word_forcing_probe import (char, reduced_words, writhe, lkey, show,
                                          BOR, orbit, self_check)

def main():
    self_check()
    q = sp.symbols("q", positive=True)
    br2 = q + 1/q
    y21 = 1/br2**2
    y3 = 1 - 2*y21
    def sym(d): return sum(sp.Integer(v)*q**k for k, v in d.items())
    def trD(w): return y3*q**writhe(w) + y21*sym(char(w))
    tb = sp.factor(sp.together(trD(BOR)))
    h = sp.symbols("h")
    corpus = ((4 + h**2 - 3*h**4 - h**6)/(h**2 + 4)).subs(h, q - 1/q)
    out = {"trD_bor": str(tb), "trD_bor_minus_corpus": str(sp.factor(sp.together(trD(BOR) - corpus))),
           "weights": "y111=0, y21=1/[2]^2, y3=1-2/[2]^2"}
    print("tr_M^D(Bor) =", tb)
    print("tr_M^D(Bor) - corpus =", out["trD_bor_minus_corpus"])
    borb = orbit(BOR)
    res = {}
    for n in range(1, 9):
        seen, hits = {}, []
        for w in reduced_words(n):
            e = writhe(w)
            if e == 0 or abs(e) > 4:
                continue
            key = (e, lkey(char(w)))
            if key not in seen:
                t = trD(w)
                seen[key] = (sp.simplify(sp.together(t - trD(BOR))) == 0
                             or sp.simplify(sp.together(t + trD(BOR))) == 0)
            if seen[key]:
                hits.append(show(w))
        res[n] = {"distinct_(writhe,chi)": len(seen), "n_hits": len(hits), "hits": hits[:10]}
        print(f"P3-D len {n}: distinct (writhe,chi) {len(seen)}, hits {len(hits)}")
    out["P3D"] = res
    Path(__file__).with_name("p3-convention-d.result.json").write_text(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
