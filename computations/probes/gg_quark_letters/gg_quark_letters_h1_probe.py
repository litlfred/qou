#!/usr/bin/env python3
"""gamma-gamma words in H_3 to first order in h: single-letter content.

Recipe: preregistration.md (bca743c8b98), committed before this was run.
Issue #7754, bean qou-ales. Measures only; adopts nothing; no data compared.

H_3 over Z[h] in the standard basis T_w (w in S_3), sigma_i^{-1} = sigma_i - h.
Characters via the exact Young seminormal reps of
computations/probes/gg_ntower/gg_ntower_probe.py. No floats.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
h = sp.Symbol("h")
q = sp.Symbol("q", positive=True)
HQ = q - 1 / q


def _a(r):
    return sp.cancel(HQ / (1 - q ** (-2 * r)))


# Young seminormal reps of H_3: (3) is sigma -> q; (2,1) on tableaux
# T1 = [12/3] (contents 0,1,-1), T2 = [13/2] (contents 0,-1,1).
REP = {
    (3, 0): [sp.Matrix([[q]]), sp.Matrix([[q]])],
    (2, 1): [
        sp.Matrix([[q, 0], [0, -1 / q]]),
        sp.Matrix([[_a(-2), 1], [sp.cancel(_a(-2) * _a(2) + 1), _a(2)]]),
    ],
}

# --- S_3 as image tuples on {0,1,2}; s_i swaps i, i+1 (acting on positions)
E = (0, 1, 2)
S = [(1, 0, 2), (0, 2, 1)]


def comp(a, b):          # (a*b)(x) = a(b(x)): product of transpositions
    return tuple(a[b[x]] for x in range(3))


def length(w):
    return sum(1 for i in range(3) for j in range(i + 1, 3) if w[i] > w[j])


NAME = {}
for word in [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]:
    w = E
    for i in word:
        w = comp(w, S[i])
    NAME[w] = "e" if not word else "s" + "".join(map(str, word))
REDUCED = {w: [int(c) for c in n[1:]] if n != "e" else [] for w, n in NAME.items()}


def rmul_gen(x, i, e):
    """x * sigma_i^e, e = +1 or -1, x: dict w -> poly in h."""
    out = {}
    for w, c in x.items():
        ws = comp(w, S[i])
        if length(ws) > length(w):
            terms = [(ws, 1)]
        else:
            terms = [(ws, 1), (w, h)]
        if e == -1:
            terms = terms + [(w, -h)]
        for v, a in terms:
            out[v] = sp.expand(out.get(v, 0) + a * c)
    return {w: c for w, c in out.items() if c != 0}


def word_elt(letters):
    x = {E: sp.Integer(1)}
    for i, e in letters:
        x = rmul_gen(x, i, e)
    return x


def flip_elt(x):
    def fw(w):
        return tuple(2 - w[2 - k] for k in range(3))
    return {fw(w): c for w, c in x.items()}


def chars(x):
    out = {}
    for lam in [(3, 0), (2, 1)]:
        G = REP[lam]
        tot = sp.Integer(0)
        for w, c in x.items():
            M = sp.eye(G[0].shape[0])
            for i in REDUCED[w]:
                M = M * G[i]
            tot += c.subs(h, HQ) * M.trace()
        out[lam] = sp.factor(sp.cancel(tot))
    return out


def first_single_letter_order(x):
    c0 = sp.Poly(x.get(S[0], 0), h)
    c1 = sp.Poly(x.get(S[1], 0), h)
    degs = [m[0] for P in (c0, c1) for m in P.monoms() if not P.is_zero]
    if not degs:
        return None, None, None
    n = min(degs)
    return n, c0.as_expr().coeff(h, n), c1.as_expr().coeff(h, n)


def main():
    checks = {}
    # K1 relations
    s0s0 = word_elt([(0, 1), (0, 1)])
    ok = s0s0 == {E: 1, S[0]: h}
    ok &= word_elt([(0, 1), (1, 1), (0, 1)]) == word_elt([(1, 1), (0, 1), (1, 1)])
    ok &= word_elt([(0, 1), (0, -1)]) == {E: 1}
    for lam, G in REP.items():
        I = sp.eye(G[0].shape[0])
        for X in G:
            ok &= sp.simplify(X * X - HQ * X - I) == sp.zeros(*I.shape)
        ok &= sp.simplify(G[0] * G[1] * G[0] - G[1] * G[0] * G[1]) == sp.zeros(*I.shape)
    checks["K1_hecke_braid_relations"] = bool(ok)

    fam = {
        "V": lambda k: [(0, 1), (1, -1)] * k,
        "U": lambda k: [(0, 1), (1, 1)] * k,
        "Vinv": lambda k: [(1, 1), (0, -1)] * k,
    }
    rows = {}
    k2 = k3 = k4 = True
    for nm, f in fam.items():
        for k in range(1, 7):
            x = word_elt(f(k))
            # K2: h=0 is a single permutation with coefficient 1
            at0 = {w: c.subs(h, 0) for w, c in x.items() if c.subs(h, 0) != 0}
            k2 &= len(at0) == 1 and list(at0.values())[0] == 1
            n, a0, a1 = first_single_letter_order(x)
            ch = chars(x)
            row = {
                "coefficients": {NAME[w]: str(sp.factor(c)) for w, c in sorted(x.items(), key=lambda t: NAME[t[0]])},
                "h0_permutation": NAME[list(at0)[0]],
                "first_single_letter_order": n,
                "c_s0_at_that_order": str(a0), "c_s1_at_that_order": str(a1),
                "flip_symmetric_single_letters": bool(sp.expand(x.get(S[0], 0) - x.get(S[1], 0)) == 0),
                "chi_3": str(ch[(3, 0)]), "chi_21": str(ch[(2, 1)]),
                "chi_21_at_q1": str(sp.cancel(ch[(2, 1)]).subs(q, 1)),
            }
            if nm == "V":
                if k == 3:
                    k3 &= sp.simplify(ch[(2, 1)] - 2 + HQ**4 * (3 + HQ**2)) == 0
                k4 &= flip_elt(x) == word_elt(fam["Vinv"](k))
            rows[f"{nm}^{k}"] = row
            print(f"{nm}^{k}: h0={row['h0_permutation']} first single-letter order={n} "
                  f"(c_s0={a0}, c_s1={a1}) flip-sym={row['flip_symmetric_single_letters']} "
                  f"chi21(q=1)={row['chi_21_at_q1']}", flush=True)
    checks["K2_h0_is_permutation"] = bool(k2)
    checks["K3_V3_identity"] = bool(k3)
    checks["K4_flip_V_is_Vinv"] = bool(k4)
    out = {"q0Anchor": "independent", "q0AnchorReason": "q0_independence_checker: the fully-resolved import cone reads no q0 and the source carries no q0-shaped literal", "recipe": "computations/probes/gg_quark_letters/preregistration.md (bca743c8b98)",
           "issue": 7754, "checks": checks, "rows": rows}
    (HERE / "gg-quark-letters-h1.witness.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(checks)
    sys.exit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
