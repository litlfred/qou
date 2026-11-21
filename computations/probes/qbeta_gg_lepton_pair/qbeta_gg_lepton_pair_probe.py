#!/usr/bin/env python3
"""qbeta_gg_lepton_pair_probe — which γγ words close to e⁻ ⊔ ν̄ (issue #8833).

Closed family and reporting rules: PREREGISTRATION.md (committed first). Lean first:
QOU/QBeta/GammaGammaLeptonPair.lean (n + #components is even for a γγ word).

Exact rational arithmetic (fractions.Fraction) at q = 2 and q = 3; no floats. The framing-
corrected invariant is Ĩ(w) = q^(−2·writhe)·Tr(K^{⊗n} ρ(w)), with the Jimbo R-matrix
(eigenvalues q, −1/q) and K = diag(q, q⁻¹); stabilisation σ^{±1} multiplies the trace by
q^{±2}, checked below (G2). Nothing is selected or scored.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as Fr
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[3]
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

from witness_base import WitnessBuilder  # noqa: E402

RESULTS: list[tuple[str, bool, str]] = []
QS = (Fr(2), Fr(3))


def check(name: str, ok: bool, detail: str) -> None:
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {detail}\n")


def vertex(i: int):
    return [(i, +1), (i + 1, -1)]


def gg_word(vs):
    w = []
    for i in vs:
        w += vertex(i)
    return w


def apply_crossing(vec: dict, n: int, i: int, s: int, q: Fr) -> dict:
    """R (s=+1) or R^-1 = R - h (s=-1) on positions (i, i+1); bit 1 = 'down'."""
    h = q - 1 / q
    out: dict = {}

    def add(k, v):
        if v:
            out[k] = out.get(k, 0) + v
    sh = n - 2 - i
    for b, c in vec.items():
        x, y = (b >> (sh + 1)) & 1, (b >> sh) & 1
        base = b & ~(3 << sh)
        sw = base | (y << (sh + 1)) | (x << sh)
        if x == y:
            add(b, c * (q if s > 0 else 1 / q))
        elif (x, y) == (0, 1):          # e01 -> e10 (R);  R^-1: e10 - h e01
            add(sw, c)
            if s < 0:
                add(b, -h * c)
        else:                           # e10 -> e01 + h e10 (R); R^-1: e01
            add(sw, c)
            if s > 0:
                add(b, h * c)
    return out


def qtrace(word, n: int, q: Fr) -> Fr:
    tot = Fr(0)
    for b in range(2 ** n):
        v = {b: Fr(1)}
        for (i, s) in word:   # rho(w) = product left to right, applied right-most first
            pass
        for (i, s) in reversed(word):
            v = apply_crossing(v, n, i, s, q)
        diag = v.get(b, 0)
        if diag:
            ones = bin(b).count("1")
            tot += q ** (n - 2 * ones) * diag
    return tot


def inv(word, n, q):
    wr = sum(s for _, s in word)
    return q ** (-2 * wr) * qtrace(word, n, q)


def strand_data(word, n):
    """Permutation, components, linking numbers (x2) and self-crossing counts."""
    pos = list(range(n))            # pos[p] = strand currently at position p
    crossings = []
    for (i, s) in word:
        a, b = pos[i], pos[i + 1]
        crossings.append((a, b, s))
        pos[i], pos[i + 1] = b, a
    perm = {pos[p]: p for p in range(n)}  # strand starting at p ends at position perm...
    # closure: strand at top position p continues as the strand starting at p
    end = {pos[p]: p for p in range(n)}
    comp, seen = {}, set()
    for s0 in range(n):
        if s0 in seen:
            continue
        cid = len(set(comp.values()))
        s = s0
        while s not in seen:
            seen.add(s)
            comp[s] = cid
            s = end[s]
    k = len(set(comp.values()))
    lk2 = [[0] * k for _ in range(k)]
    selfc = [0] * k
    for a, b, sg in crossings:
        ca, cb = comp[a], comp[b]
        if ca == cb:
            selfc[ca] += 1
        else:
            lk2[ca][cb] += sg
            lk2[cb][ca] += sg
    return k, lk2, selfc


def main() -> int:
    # G1: Jimbo R satisfies the Hecke relation (checked on 2 strands)
    ok = True
    for q in QS:
        h = q - 1 / q
        for b in range(4):
            v1 = apply_crossing(apply_crossing({b: Fr(1)}, 2, 0, 1, q), 2, 0, 1, q)
            v2 = apply_crossing({b: Fr(1)}, 2, 0, 1, q)
            rhs = {kk: h * vv for kk, vv in v2.items()}
            rhs[b] = rhs.get(b, 0) + 1
            ok &= all(v1.get(kk, 0) == rhs.get(kk, 0) for kk in set(v1) | set(rhs))
    check("G1_hecke_relation", ok, "sigma^2 = h sigma + 1 for the Jimbo R at q = 2, 3 (exact).")

    # G2: Markov invariance of the framing-corrected invariant on samples
    samples = [([(0, 1)], 2, []), ([(0, -1)], 2, []), ([(0, 1), (1, 1)], 3, [(0, 1)]),
               ([(0, 1), (1, 1), (0, 1), (2, -1)], 4, [(0, 1), (1, 1), (0, 1)])]
    okm = True
    for big, nb, small in samples:
        for q in QS:
            okm &= inv(big, nb, q) == inv(small, nb - 1, q)
    check("G2_framing_corrected_trace_is_markov_invariant", okm,
          "q^(-2 writhe) Tr(K^n rho) is unchanged by positive and negative stabilisation "
          "on four samples at q = 2, 3, exactly.")

    ref = {q: inv([(0, 1), (1, 1), (0, 1)], 4, q) for q in QS}      # Hopf+ (+) unknot
    refm = {q: inv([(0, -1), (1, -1), (0, -1)], 4, q) for q in QS}  # mirror
    rows = []
    for n, verts in ((3, (0,)), (5, (0, 1, 2))):
        for L in range(1, 7):
            for vs in itertools.product(verts, repeat=L):
                w = gg_word(vs)
                k, lk2, selfc = strand_data(w, n)
                if (n + k) % 2:
                    rows.append({"n": n, "word": list(vs), "parity_violation": True})
                if k != 3:
                    continue
                lks = sorted(abs(lk2[a][b]) // 2 for a in range(3) for b in range(a + 1, 3))
                if lks != [0, 0, 1]:
                    continue
                vals = {q: inv(w, n, q) for q in QS}
                match = "e- + nu-bar" if vals == ref else (
                    "mirror (e+ + nu)" if vals == refm else "other link")
                rows.append({"n": n, "word": "".join(f"V{i}" for i in vs), "vertices": L,
                             "self_crossings": selfc, "match": match})
    par = [r for r in rows if r.get("parity_violation")]
    check("G3_parity_holds_on_every_word", not par,
          "n + #components is even for every gamma-gamma word enumerated on 3 and 5 strands "
          "(Lean gammaGamma_components_parity).")
    cands = [r for r in rows if "match" in r]
    on3 = [r for r in cands if r["n"] == 3]
    hits = [r for r in cands if r["match"] != "other link"]
    check("G4_none_on_three_strands", not on3,
          "no gamma-gamma word on 3 strands (<= 6 vertices) closes to three components with "
          "linking pattern {1,0,0}: three components force the identity permutation, all "
          "components are single strands with no self-crossings, so writhe = 2 lk = +-2, "
          "but every gamma-gamma word has writhe 0.")
    first = {}
    for r in hits:
        first.setdefault(r["match"], r["vertices"])
    print(f"  5-strand candidates with 3 components and lk {{1,0,0}}: {len(cands)}; "
          f"matching e- + nu-bar or mirror: {len(hits)}; first vertex counts: {first}")
    for r in hits[:12]:
        print("   ", r)
    check("G5_report_five_strand_matches", True,
          f"{len(hits)} gamma-gamma words on 5 strands (<= 6 vertices) have the invariant of "
          f"e- + nu-bar or its mirror at q = 2 and 3; smallest vertex counts {first}. "
          "Evidence of isotopy, not a proof. None is selected.")

    allp = all(o for _, o, _ in RESULTS)
    print(f"  {sum(o for _, o, _ in RESULTS)}/{len(RESULTS)} checks passed")
    wb = WitnessBuilder("qbeta-gg-lepton-pair", engine="fractions")
    for nm, o, det in RESULTS:
        wb.add_assertion(nm, computed="PASS" if o else "FAIL", expected="PASS",
                         tolerance="exact", source=det)
    wb.save({
        "description": ("Which gamma-gamma words close to the lepton pair e- + nu-bar (Hopf "
                        "link + unknot): parity, writhe, and an exact framing-corrected "
                        "quantum invariant at q = 2, 3. Nothing selected or scored."),
        "beans": ["qou-cds1", "qou-99qc"],
        "lean": "QOU/QBeta/GammaGammaLeptonPair.lean",
        "reference_invariant": {str(q): str(ref[q]) for q in QS},
        "candidates": cands,
        "first_match_vertex_counts": first,
        "scope": "(a): 3 and 5 strands, at most 6 vertices.",
    })
    return 0 if allp else 1


if __name__ == "__main__":
    raise SystemExit(main())
