#!/usr/bin/env python3
"""knot_convoluted_tensor_h2_probe.py — the corpus LP for the bond operator K in A ⊗_K B, on H2.

Bean `qou-a1hh`. Owner 2026-10-13: the bond is "a knot-convoluted tensor product that acts on braids, part of dual
space". Corpus carrier: prop:ilp-covalent-bond — the bond is a knot operator K acting by x ↦ NF(x·K), selected by

    min cr(K)  s.t.  K a knot (single-component closure),  G·NF(x·K) ≥ 0,  tr_M(x·K) < tr_M(x)   (strict: binding)

Companion Lean: QOU/Molecular/KnotConvolutedTensor.lean (kct, kct_mul: operators at one site compose, so a bond
operator never adds strands).

HOW EACH CORPUS CLAUSE IS READ HERE (stated, not chosen to get a result)
  x            A1 ⊗ A2 on 3A + 3Z = 12 strands (owner ruling 2026-10-12): each H atom = proton block (production
               nucleon word) + electron (corpus electron sigma0 sigma1 sigma0) on its own 3 strands.
  G·NF ≥ 0     reading 3 (owner ruling 2026-09-12): chi_lambda(x·K) ≥ 0 on every convention-D block with y_lambda > 0
               (two-row only: convention D kills three-row y).
  knot         the closure of K on its 3 strands is one component, i.e. its permutation is a 3-cycle.
  site         K acts on 3 consecutive strands that straddle the junction cut (between strand 5 and 6): s = 4 or 5.
  cr(K)        word length of a freely reduced 3-strand word (lengths 2..4 enumerated; the LP stops at the first length
               with a feasible word).

UNFIXED, ALL VALUES RUN (nothing selected):
  atom2        orientation of the second atom: 'pe' (junction faces e|p) or 'ep' (junction faces e|e).
  pe_letter    the intra-atom p–e letter sigma^-1 (molecular-crossing-table p_i e_j) present or absent.
  cmol         the inter-atomic crossing-table letter at the junction cut present or absent.

ELECTRON WORD (owner 2026-10-13, "try both"): both run.
  Tw0_s0s1s0        the corpus H_3 electron T_{w0} (particle-nf-table, covalent-bond-shared-trefoil); closes to a Hopf link.
  trefoil_s0s0s0s1  a true trefoil on 3 strands (sigma_1^3 in B_2, ChiralFermionBraidWords, stabilised once).

GAMMA-GAMMA RESTRICTION (owner ruling 2026-09-08, bean qou-ales: select words by gamma-gamma + SDP, not census):
  K restricted to products of the vertex sigma_s sigma_{s+1}^-1 that close to a knot: the vertex itself (unknot) and its
  square (figure-eight 4_1); the cube is the Borromean link (3 components). Reported as gg_lp_selected beside the full LP.

ALSO RECORDED: the corpus "trefoil" sigma0 sigma1 sigma0 has permutation (0 2), i.e. its closure is a 2-component
link, not a knot. Checked mechanically below.

Precision: mpmath 40 dps throughout; no float. TOL 1e-25.

-- Ref: [manuscript] prop:ilp-covalent-bond; def:covalent-bond-shared-trefoil; def:molecular-braid; bean qou-a1hh
"""
from __future__ import annotations

import itertools
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import composition_feasibility_a2_probe as cf  # noqa: E402
import molecular_junction_window_probe as mjw  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 40
Q = cf.Q
H = cf.H
ZD = cf.Z_D
ONE, ZERO = mp.mpf(1), mp.mpf(0)
TOL = mp.mpf("1e-25")
T0 = time.time()
N = 12
JCUT = 5


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def cols(shape):
    mjw.chi(shape, [])
    return mjw._COLS[tuple(shape)]


def right_apply(M, word, shape):
    cg_all, dim = cols(shape)
    for c, d, g in word:
        cg = cg_all[g]
        M = [[c * mp.fsum(row[k] * v for k, v in cg[j]) + d * row[j] for j in range(dim)] for row in M]
    return M


def sparse_word(word, shape):
    """Columns of the matrix of `word` (sparse dicts)."""
    cg_all, dim = cols(shape)
    K = [{j: ONE} for j in range(dim)]
    for c, d, g in word:
        cg = cg_all[g]
        new = []
        for j in range(dim):
            col = {}
            for k, v in cg[j]:
                for i, w in K[k].items():
                    col[i] = col.get(i, ZERO) + c * v * w
            if d != 0:
                for i, w in K[j].items():
                    col[i] = col.get(i, ZERO) + d * w
            new.append(col)
        K = new
    return K


def tr_prod(M, K):
    """tr(M K). K[i] is column i of K, i.e. {j: K_ji}, so tr(MK) = sum_ij M_ij K_ji.
    (Until 2026-10-13 this read M[j][i], i.e. tr(M^T K); the identity-M cross-check could not see it.)"""
    return mp.fsum(M[i][j] * w for i in range(len(K)) for j, w in K[i].items())


def proton_block():
    _, blocks, _ = mjw.tokens(1, 0)
    return [(c, d, off) for c, d, off in blocks[0]]


ELECTRONS = {
    # corpus particle-nf-table / covalent-bond-shared-trefoil: the Hecke basis element T_{w0}; closes to a Hopf link
    "Tw0_s0s1s0": lambda b: [(ONE, ZERO, b), (ONE, ZERO, b + 1), (ONE, ZERO, b)],
    # a true trefoil on 3 strands: sigma_1^3 in B_2 (ChiralFermionBraidWords) stabilised once
    "trefoil_s0s0s0s1": lambda b: [(ONE, ZERO, b), (ONE, ZERO, b), (ONE, ZERO, b), (ONE, ZERO, b + 1)],
}
ELECTRON = "Tw0_s0s1s0"


def electron(base):
    return ELECTRONS[ELECTRON](base)


GG_WORDS = {"s0+s1-", "s0+s1-s0+s1-"}   # gamma-gamma: products of the vertex sigma_i sigma_{i+1}^-1 that close to knots


def sinv(g):
    return [(ONE, -H, g)]


def shift(word, s):
    return [(c, d, g + s) for c, d, g in word]


def atom(order, pe_letter):
    p = proton_block()
    if order == "pe":
        w = p + (sinv(2) if pe_letter else []) + electron(3)
        return w, ["p", "p", "p", "e", "e", "e"]
    w = electron(0) + (sinv(2) if pe_letter else []) + shift(p, 3)
    return w, ["e", "e", "e", "p", "p", "p"]


def perm_cycles(word, k=3):
    p = list(range(k))
    for _, _, g in word:
        p[g], p[g + 1] = p[g + 1], p[g]
    seen, cyc = set(), 0
    for i in range(k):
        if i not in seen:
            cyc += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = p[j]
    return cyc


def candidates(max_len=4):
    letters = [(0, 1), (0, -1), (1, 1), (1, -1)]
    out = {}
    for L in range(1, max_len + 1):
        out[L] = []
        for w in itertools.product(letters, repeat=L):
            if any(w[i][0] == w[i + 1][0] and w[i][1] == -w[i + 1][1] for i in range(L - 1)):
                continue
            word = [(ONE, ZERO if e == 1 else -H, g) for g, e in w]
            if perm_cycles(word) == 1:
                out[L].append(("".join(f"s{g}{'+' if e == 1 else '-'}" for g, e in w), word))
    return out


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        log(f"[{'PASS' if ok else 'FAIL'}] {name}")

    y = {n: cf.load_y(n) for n in (3, 12)}
    shapes = [l for l in mjw.two_row(N) if y[N][l] != 0]
    log(f"n={N}: two-row blocks with y>0: {shapes}")

    corpus_trefoil = ELECTRONS["Tw0_s0s1s0"](0)
    check("true_trefoil_electron_is_one_component", perm_cycles(ELECTRONS["trefoil_s0s0s0s1"](0)) == 1, "(0 1)^3(1 2)")
    check("corpus_trefoil_s0s1s0_closure_is_two_component", perm_cycles(corpus_trefoil) == 2, "permutation (0 2)")
    check("s0s1s0s1_closure_is_one_component", perm_cycles(ELECTRONS["Tw0_s0s1s0"](0)[:2] * 2) == 1, "permutation (0 1 2)^2")

    # cross-check sparse product against mjw.chi on a small case
    w6 = shift(electron(0), 1) + sinv(0) + [(ONE, ZERO, 4)]
    ok = True
    for l in mjw.two_row(6):
        M = [[ONE if i == j else ZERO for j in range(cols(l)[1])] for i in range(cols(l)[1])]
        if abs(tr_prod(M, sparse_word(w6, l)) - mjw.chi(l, w6)) > TOL:
            ok = False
    check("sparse_trace_matches_mjw_chi_n6", ok, "two independent products")

    # the cross-check that matters: a NON-identity prefix M, tr(M K) against chi of the concatenated word.
    # (The identity-M check above cannot distinguish tr(MK) from tr(M^T K).)
    pre6 = electron(0) + sinv(2) + [(ONE, ZERO, 3), (ONE, -H, 4), (ONE, ZERO, 3)]
    k6 = [(ONE, -H, 1), (ONE, ZERO, 2), (ONE, -H, 1), (ONE, ZERO, 2)]
    ok = True
    for l in mjw.two_row(6):
        dim = cols(l)[1]
        I = [[ONE if i == j else ZERO for j in range(dim)] for i in range(dim)]
        Mp = right_apply(I, pre6, l)
        if abs(tr_prod(Mp, sparse_word(k6, l)) - mjw.chi(l, pre6 + k6)) > TOL:
            ok = False
    check("prefix_times_operator_trace_matches_chi_of_concatenation_n6", ok, "non-identity prefix")

    cand = candidates(4)
    log("single-component reduced 3-strand words per length: " + str({L: len(v) for L, v in cand.items()}))
    check("no_single_component_word_of_length_1", len(cand[1]) == 0, "transposition")

    global ELECTRON
    results = {}
    for ELECTRON in ELECTRONS:
     for atom2 in ("pe", "ep"):
         for pe_letter in (True, False):
             for cmol in (True, False):
                 tag = f"electron={ELECTRON},atom2={atom2},pe_letter={int(pe_letter)},cmol={int(cmol)}"
                 w1, lab1 = atom("pe", pe_letter)
                 w2, lab2 = atom(atom2, pe_letter)
                 pair = (lab1[-1], lab2[0])
                 x = w1 + shift(w2, 6)
                 if cmol:
                     x += sinv(JCUT) if set(pair) == {"p", "e"} else ([(ONE, ZERO, JCUT)] if pair == ("e", "e") else [])
                 prefix = {}
                 for l in shapes:
                     dim = cols(l)[1]
                     I = [[ONE if i == j else ZERO for j in range(dim)] for i in range(dim)]
                     prefix[l] = right_apply(I, x, l)
                 log(f"{tag}: prefix built (junction pair {pair})")
                 chi_x = {l: mp.fsum(prefix[l][i][i] for i in range(cols(l)[1])) for l in shapes}
                 tr_x = mp.fsum(y[N][l] * chi_x[l] for l in shapes)
                 r3_x = all(chi_x[l] >= -TOL for l in shapes)
                 rows, feasible_by_len, decreasing_by_len = [], {}, {}
                 for L in (2, 3, 4):
                     for name, kw in cand[L]:
                         for s in (4, 5):
                             kws = shift(kw, s)
                             chis = {l: tr_prod(prefix[l], sparse_word(kws, l)) for l in shapes}
                             tr = mp.fsum(y[N][l] * chis[l] for l in shapes)
                             r3 = all(chis[l] >= -TOL for l in shapes)
                             dec = tr < tr_x - TOL
                             neg = [str(l) for l in shapes if chis[l] < -TOL]
                             rows.append({"word": name, "site": s, "len": L, "ratio": mp.nstr(tr / tr_x, 25),
                                          "reading3": r3, "trace_decreases": bool(dec), "negative_blocks": neg})
                             if r3 and dec:
                                 feasible_by_len.setdefault(L, []).append(f"{name}@{s}")
                             if dec:
                                 decreasing_by_len.setdefault(L, []).append(f"{name}@{s}")
                 gg_feasible = [f"{r['word']}@{r['site']}" for r in rows if r["word"] in GG_WORDS and r["reading3"] and r["trace_decreases"]]
                 gg_rows = [r for r in rows if r["word"] in GG_WORDS]
                 gg_len = min((len(w.split("@")[0]) // 3 for w in gg_feasible), default=None)
                 lp_len = min(feasible_by_len) if feasible_by_len else None
                 results[tag] = {
                     "junction_pair": list(pair), "tr_x": mp.nstr(tr_x, 30), "reading3_x": r3_x,
                     "chi_x_negative_blocks": [str(l) for l in shapes if chi_x[l] < -TOL],
                     "lp_selected_length": lp_len,
                     "lp_selected": feasible_by_len.get(lp_len, []) if lp_len else [],
                     "trace_decreasing_by_length": decreasing_by_len,
                     "gg_lp_selected": [w for w in gg_feasible if len(w.split("@")[0]) // 3 == gg_len] if gg_len else [],
                     "gg_rows": gg_rows, "rows": rows}
                 log(f"{tag}: reading3(x)={r3_x}; LP length={lp_len}; selected={results[tag]['lp_selected']}; "
                     f"gg selected={results[tag]['gg_lp_selected']}; "
                     f"gg ratios={[(r['word'], r['site'], r['ratio'][:10], r['reading3']) for r in gg_rows]}")

    ok_all = all(ok for _, ok, _ in checks)
    wb = WitnessBuilder("knot-convoluted-tensor-h2", engine="mpmath")
    for name, ok, src in checks:
        wb.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = wb.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "q0 enters only through the committed y-lambda-at-q0 witness (proton pin) and the production "
                          "nucleon word",
        "description": "PROBE (bean qou-a1hh): the corpus ILP for the bond operator K of A ⊗_K B (prop:ilp-covalent-"
                       "bond), on H2 with 3A + 3Z strands, K on the two 3-strand sites straddling the junction, "
                       "reading-3 positivity and strict trace decrease. Unfixed choices all run. Nothing fitted, "
                       "selected against data, or wired.",
        "weight_family": "markov_y_lambda_convention_D",
        "constants": {"q0": mp.nstr(Q, 40), "h": mp.nstr(H, 40), "z_D": mp.nstr(ZD, 40)},
        "results": results,
    })
    log(f"witness: {out}")
    log(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
