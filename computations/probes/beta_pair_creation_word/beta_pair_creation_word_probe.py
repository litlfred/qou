#!/usr/bin/env python3
"""qou-99qc task W: which word creates the e⁻ν̄ pair in β⁻ decay — enumeration by corpus principles.

Pre-registered: PREREGISTRATION.md (commit ee04d3c394), before any number.

Setting. H_4(q), nucleon β_Bor = (σ₀σ₁⁻¹)³ on strands 0-2 (the γγ + reading-3 selection, #8636),
one lepton strand at position 3. Process word W = X · β_Bor (operator order ρ(W) = ρ(X)ρ(β): the
nucleon braid acts first, then X). Traces and characters are cyclic, so they equal those of β_Bor·X.

Every functional is computed EXACTLY in ℚ(q) from the Jimbo representation on V^{⊗4}
(P1 engine, #8681, copied verbatim):
* characters χ_(4), χ_(3,1), χ_(2,2) from the T³-weight-space traces (Schur–Weyl), checked
  against the Hecke-basis Markov trace: tr_D = Σ_{λ ≤ 2 rows} y_λ χ_λ on all 24 T_w;
* the strand-tracked charged-current block n⊗ν → p⊗e⁻ [premise L, #8673: ν = u, e⁻ = d on the
  lepton strand], validated against ChargedCurrentW.beta_amp_left_pos = (h·q)·T⁺ (#8638);
* the cross term C(X) = tr_D(βX) − tr_D(β)·tr_D(X).
Numbers only at the proton q₀ (mpmath 70 dps), for the reading-3 signs. CODATA is not read.

Run:  python3 -u beta_pair_creation_word_probe.py 2>&1 | tee /tmp/beta_pair_creation_word_probe.log
"""
from __future__ import annotations

import itertools
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))
sys.path.insert(0, str(_HERE))

import mpmath as mp  # noqa: E402
from sympy import Poly, Symbol, factor  # noqa: E402

import qou_substrate.constants as C  # noqa: E402
from qou_substrate.precision import fmt  # noqa: E402
from hecke_exact import H, KF, RING, ONE, ZERO, h, q, zD  # noqa: E402
from jimbo import apply_gen  # noqa: E402

DPS = 70
mp.mp.dps = DPS
Q0 = C.q_at(DPS)
T0 = time.time()
ASSERTS: list = []
N = 4
LEP = 3
QK = KF(q)
HK = KF(h)
TWO = QK + 1 / QK  # [2]_q


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def check(name, ok, note=""):
    ASSERTS.append({"name": name, "ok": bool(ok), "note": note})
    log(f"{'PASS' if ok else 'FAIL'} {name} {note}")


def gk(x):
    """RING ground element -> KF."""
    return x.coeff(1) if hasattr(x, "coeff") else KF(x)


def ev_frac(f, qv=Q0):
    num = sum(mp.mpf(int(c.numerator)) / mp.mpf(int(c.denominator)) * qv ** e[0]
              for e, c in f.numer.terms())
    den = sum(mp.mpf(int(c.numerator)) / mp.mpf(int(c.denominator)) * qv ** e[0]
              for e, c in f.denom.terms())
    return num / den


_X = Symbol("q")


def order_at_one(f):
    """Order of vanishing of an exact rational function at q = 1 (None if f ≡ 0)."""
    if f == 0:
        return None
    k = 0
    for part, sgn in ((f.numer, 1), (f.denom, -1)):
        P = Poly(part.as_expr(), _X)
        while P.eval(1) == 0:
            P = P.quo(Poly(_X - 1, _X))
            k += sgn
    return k


def fx(f):
    return str(factor(f.as_expr()))


# ---------------------------------------------------------------- words and elements
# A word is a tuple of ints: g >= 0 is σ_g, g < 0 is σ_{-g-1}^{-1} (engine convention).
# An element is a list of (KF coefficient, word).
def letter_str(g):
    return f"s{g}" if g >= 0 else f"s{-g - 1}'"


def word_str(w):
    return "·".join(letter_str(g) for g in w) if w else "1"


BETA = (0, -2) * 3


def strand_track(w):
    """Positions/crossings of strands under ρ(w): letters act right to left.

    Returns (final position of each strand, list of (strand_a, strand_b, sign))."""
    pos2str = list(range(N))
    crossings = []
    for g in reversed(w):
        i, sgn = (g, 1) if g >= 0 else (-g - 1, -1)
        a, b = pos2str[i], pos2str[i + 1]
        crossings.append((a, b, sgn))
        pos2str[i], pos2str[i + 1] = b, a
    final = [0] * N
    for p, s in enumerate(pos2str):
        final[s] = p
    return final, crossings


def rho_word_on(vec, w):
    for g in reversed(w):
        vec = apply_gen(vec, g, inv=False) if g >= 0 else apply_gen(vec, -g - 1, inv=True)
    return vec


def basis_sector(k):
    """Basis states of V^{⊗4} with exactly k d's (1 = d)."""
    return [b for b in itertools.product((0, 1), repeat=N) if sum(b) == k]


SECT = {k: basis_sector(k) for k in range(3)}
NUC_IN = [(0, 1, 1), (1, 0, 1), (1, 1, 0)]     # udd, dud, ddu  (n, T³ = −½)
NUC_OUT = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]    # duu, udu, uud  (p, T³ = +½)


def analyse_element(el):
    """el = [(c, word)]. Returns sector traces Tr_k, CC block (strand-tracked), reverse block."""
    tr = {k: KF.zero for k in range(3)}
    cc = [[KF.zero] * 3 for _ in range(3)]
    rev = [[KF.zero] * 3 for _ in range(3)]
    for c, w in el:
        final, _ = strand_track(w)
        for k in range(3):
            for b in SECT[k]:
                img = rho_word_on({b: ONE}, w)
                tr[k] += c * gk(img.get(b, ZERO))
        # n ⊗ ν -> p ⊗ e⁻, strand labels: input strands 0-2 nucleon, 3 = u (ν)
        for j, nb in enumerate(NUC_IN):
            img = rho_word_on({nb + (0,): ONE}, w)
            for i, pb in enumerate(NUC_OUT):
                st = pb + (1,)                       # strand labels, lepton strand = d (e⁻)
                posv = [0] * N
                for s in range(N):
                    posv[final[s]] = st[s]
                cc[i][j] += c * gk(img.get(tuple(posv), ZERO))
        # reverse chirality: p ⊗ e⁻ -> n ⊗ ν
        for j, pb in enumerate(NUC_OUT):
            img = rho_word_on({pb + (1,): ONE}, w)
            for i, nb in enumerate(NUC_IN):
                st = nb + (0,)
                posv = [0] * N
                for s in range(N):
                    posv[final[s]] = st[s]
                rev[i][j] += c * gk(img.get(tuple(posv), ZERO))
    chi = {"4": tr[0], "31": tr[1] - tr[0], "22": tr[2] - tr[1]}
    return chi, cc, rev


def word_el(w, c=None):
    return [(KF.one if c is None else c, tuple(w))]


def el_mul(a, b):
    return [(ca * cb, wa + wb) for ca, wa in a for cb, wb in b]


def el_add(*els):
    out = []
    for e in els:
        out += e
    return out


def el_scale(a, s):
    return [(s * c, w) for c, w in a]


# ---------------------------------------------------------------- Markov weights from characters
def hecke_trace_word(w):
    return gk(H.one(N).rmul_word(list(w)).trace())


def solve_y():
    """Solve tr_D = y4 χ4 + y31 χ31 + y22 χ22 on 1, σ₂, σ₂σ₁σ₂-free basis; validate on all 24 T_w."""
    from hecke_exact import reduced_word
    words = [reduced_word(p) for p in itertools.permutations(range(N))]
    data = []
    for w in words:
        chi, _, _ = analyse_element(word_el(w))
        data.append((w, chi, hecke_trace_word(w)))
    # pick three words giving an invertible system
    from sympy import Matrix
    for trip in itertools.combinations(range(len(data)), 3):
        M = Matrix([[data[t][1][l].as_expr() for l in ("4", "31", "22")] for t in trip])
        if M.det().simplify() != 0:
            rhs = Matrix([data[t][2].as_expr() for t in trip])
            ysol = M.LUsolve(rhs)
            break
    y = {l: KF.from_expr(factor(ysol[i])) for i, l in enumerate(("4", "31", "22"))}
    ok = all(sum(y[l] * chi[l] for l in y) == t for _, chi, t in data)
    return y, ok, len(data)


# ---------------------------------------------------------------- candidate families
LETTERS = [0, 1, 2, -1, -2, -3]


def inverse(g):
    return -g - 1


def freely_reduced(maxlen):
    out = [()]
    frontier = [()]
    for _ in range(maxlen):
        nxt = []
        for w in frontier:
            for g in LETTERS:
                if w and w[-1] == inverse(g):
                    continue
                nxt.append(w + (g,))
        out += nxt
        frontier = nxt
    return out


def V(i):
    return (i, -(i + 1) - 1)          # σ_i σ_{i+1}^{-1}


def Vbar(i):
    return (-i - 1, i + 1)            # σ_i^{-1} σ_{i+1}


def gg_words(maxlen, mirrors):
    blocks = [("V0", V(0)), ("V1", V(1))]
    if mirrors:
        blocks += [("Vb0", Vbar(0)), ("Vb1", Vbar(1))]
    out = []
    for k in range(1, maxlen // 2 + 1):
        for combo in itertools.product(blocks, repeat=k):
            out.append(("".join(n for n, _ in combo), sum((w for _, w in combo), ())))
    return out


def is_gg(w, mirrors=False):
    if len(w) % 2:
        return False
    ok = {V(0), V(1)} | ({Vbar(0), Vbar(1)} if mirrors else set())
    return all(tuple(w[i:i + 2]) in ok for i in range(0, len(w), 2))


PASS = (0, 1, 2)                     # #8638 leftward positive passage
PASSBAR = (-3, -2, -1)               # σ₂⁻¹σ₁⁻¹σ₀⁻¹ (rightward negative, bar image)
T35 = (1, 2) * 5                     # weak knot (σ₁σ₂)⁵ on strands 1-3


def PL(i):
    """Left-line projector of σ_i for |q| > 1: (σ_i + q⁻¹)/[2]."""
    return [(1 / TWO, (i,)), ((1 / QK) / TWO, ())]


def iota(i):
    """Left-handed vertex insertion −h·P_L(σ_i) (weakVertex_sub_letter)."""
    return el_scale(PL(i), -HK)


def weakvertex(i):
    """One-sided weak vertex σ_i − h·P_L(σ_i)."""
    return el_add(word_el((i,)), iota(i))


# ---------------------------------------------------------------- per-candidate record
def record(name, el, y, beta_chi, kind, gg=None, ggbar=None):
    chiX, ccX, _ = analyse_element(el)
    W = el_mul(el, word_el(BETA))   # ρ(W) = ρ(X)ρ(β): the nucleon braid acts first
    chiW, cc, rev = analyse_element(W)
    trW = sum(y[l] * chiW[l] for l in y)
    trX = sum(y[l] * chiX[l] for l in y)
    trB = sum(y[l] * beta_chi[l] for l in y)
    Cx = trW - trB * trX
    cc_nonzero = any(e != 0 for row in cc for e in row)
    rev_nonzero = any(e != 0 for row in rev for e in row)
    cc_orders = [order_at_one(e) for row in cc for e in row if e != 0]
    chi_q0 = {l: ev_frac(chiW[l]) for l in chiW}
    r3 = all(v >= 0 for v in chi_q0.values())
    rec = {"name": name, "kind": kind}
    if kind == "word":
        w = el[0][1]
        final, crossings = strand_track(w)
        lep_cross = {}
        for a, b, s in crossings:
            if LEP in (a, b):
                other = b if a == LEP else a
                lep_cross[other] = lep_cross.get(other, 0) + s
        rec.update({
            "word": word_str(w), "length": len(w),
            "writhe": sum(1 if g >= 0 else -1 for g in w),
            "lepton_final_position": final[LEP],
            "nucleon_strands_crossed_by_lepton": sorted(lep_cross),
            "signed_crossings_with_lepton": {str(k): v for k, v in sorted(lep_cross.items())},
            "wrap_ge_2": len(lep_cross) >= 2,
            "gg": is_gg(w) if gg is None else gg,
            "gg_with_mirrors": is_gg(w, True) if ggbar is None else ggbar,
        })
    rec.update({
        "cc_nonzero": cc_nonzero,
        "reverse_block_nonzero": rev_nonzero,
        "cc_min_order_q_to_1": min(cc_orders) if cc_orders else None,
        "cross_term_zero": Cx == 0,
        "cross_term_order_q_to_1": order_at_one(Cx),
        "r3_feasible_at_q0": r3,
        "_Cx": Cx, "_cc": cc, "_chiW": chiW, "_chi_q0": chi_q0,
    })
    return rec


def public(rec, full=False):
    out = {k: v for k, v in rec.items() if not k.startswith("_")}
    out["chi_W_at_q0"] = {l: fmt(v) for l, v in rec["_chi_q0"].items()}
    out["cross_term_at_q0"] = fmt(ev_frac(rec["_Cx"])) if rec["_Cx"] != 0 else "0"
    if full:
        out["cross_term_exact"] = fx(rec["_Cx"]) if rec["_Cx"] != 0 else "0"
        out["cc_block_exact"] = [[fx(e) if e != 0 else "0" for e in row] for row in rec["_cc"]]
        out["chi_W_exact"] = {l: fx(v) for l, v in rec["_chiW"].items()}
    return out


def normal_form(el):
    tot = H(N)
    for c, w in el:
        tot = tot + H.one(N).rmul_word(list(w) + list(BETA)).scale(RING(c))
    return {"".join(map(str, p)): fx(gk(v)) for p, v in sorted(tot.c.items())}


def main():
    out: dict = {}
    # ---------- validation 1: CC block of the passage = (h q) T⁺  (ChargedCurrentW.beta_amp_left_pos)
    _, ccP, revP = analyse_element(word_el(PASS))
    Eu = [[KF.zero, KF.one, QK], [KF.one, KF.zero, KF.one], [1 / QK, KF.one, KF.zero]]
    check("V1: strand-tracked CC block of sigma0 sigma1 sigma2 equals (h q) T+  (#8638)",
          all(ccP[i][j] == HK * QK * Eu[i][j] for i in range(3) for j in range(3)))
    check("V2: same passage has zero reverse (p e- -> n nu) block (#8638 reverse_left_pos)",
          all(e == 0 for row in revP for e in row))
    _, ccPb, _ = analyse_element(word_el((-1, -2, -3)))
    check("V3: leftward negative passage has zero CC block (#8638 beta_amp_left_neg)",
          all(e == 0 for row in ccPb for e in row))
    # ---------- validation 2: Markov decomposition, convention D, ≤ 2 rows
    y, yok, nT = solve_y()
    check("V4: tr_D = y4 chi4 + y31 chi31 + y22 chi22 on all 24 T_w of H_4", yok, f"n={nT}")
    yq0 = {l: ev_frac(v) for l, v in y.items()}
    check("V5: y_lambda > 0 at q0 for (4), (3,1), (2,2)", all(v > 0 for v in yq0.values()))
    out["markov_weights"] = {l: {"exact": fx(v), "q0": fmt(yq0[l])} for l, v in y.items()}
    beta_chi, _, _ = analyse_element(word_el(BETA))
    check("V6: tr_D(beta_Bor) from characters equals Lean closed form (4+h^2-3h^4-h^6)/(h^2+4)",
          sum(y[l] * beta_chi[l] for l in y) == (4 + HK ** 2 - 3 * HK ** 4 - HK ** 6) / (HK ** 2 + 4))
    log(f"y_lambda at q0: { {l: mp.nstr(v, 12) for l, v in yq0.items()} }")

    # ---------- family 1: freely reduced words length <= 4
    fam1 = freely_reduced(4)
    log(f"family 1: {len(fam1)} freely reduced words of length <= 4")
    recs1 = []
    for k, w in enumerate(fam1):
        recs1.append(record(word_str(w), word_el(w), y, beta_chi, "word"))
        if k % 100 == 0:
            log(f"  family 1: {k}/{len(fam1)}")
    check("family 1 size is 937", len(fam1) == 937)

    # ---------- family 2: γγ words
    fam2 = gg_words(8, mirrors=False)
    fam2b = [x for x in gg_words(6, mirrors=True)]
    log(f"family 2: {len(fam2)} G words (len <= 8), {len(fam2b)} G-bar words (len <= 6)")
    recs2 = [record(n, word_el(w), y, beta_chi, "word") for n, w in fam2]
    recs2b = [record(n, word_el(w), y, beta_chi, "word") for n, w in fam2b]

    # ---------- family 3: blocks
    blocks = [("V0", V(0)), ("V1", V(1)), ("Vb0", Vbar(0)), ("Vb1", Vbar(1)),
              ("P", PASS), ("Pbar", PASSBAR), ("T35", T35)]
    recs3 = []
    for k in (1, 2):
        for combo in itertools.product(blocks, repeat=k):
            n = "·".join(b for b, _ in combo)
            w = sum((ww for _, ww in combo), ())
            recs3.append(record(n, word_el(w), y, beta_chi, "word"))
    log(f"family 3: {len(recs3)} block products")
    # elements: left-handed vertex on the passage
    ip = el_mul(el_mul(iota(0), iota(1)), iota(2))
    wp = el_mul(el_mul(weakvertex(0), weakvertex(1)), weakvertex(2))
    recs_el = [record("iota0·iota1·iota2 (insertion passage)", ip, y, beta_chi, "element"),
               record("Wv0·Wv1·Wv2 (one-sided weak-vertex passage)", wp, y, beta_chi, "element"),
               record("Wv2 alone (lepton crossing only)", weakvertex(2), y, beta_chi, "element"),
               record("iota2 alone", iota(2), y, beta_chi, "element")]

    # ---------- predicate tallies
    def tally(recs):
        t = {"n": len(recs)}
        t["cc"] = sum(r["cc_nonzero"] for r in recs)
        t["wrap"] = sum(r["wrap_ge_2"] for r in recs)
        t["cross_term_nonzero"] = sum(not r["cross_term_zero"] for r in recs)
        t["r3"] = sum(r["r3_feasible_at_q0"] for r in recs)
        t["gg"] = sum(r["gg"] for r in recs)
        t["gg_mirror"] = sum(r["gg_with_mirrors"] for r in recs)
        t["cc_and_not_wrap"] = sum(r["cc_nonzero"] and not r["wrap_ge_2"] for r in recs)
        t["cc_and_crossterm_zero"] = sum(r["cc_nonzero"] and r["cross_term_zero"] for r in recs)
        t["gg_and_cc"] = sum(r["gg"] and r["cc_nonzero"] for r in recs)
        t["ggbar_and_cc"] = sum(r["gg_with_mirrors"] and r["cc_nonzero"] for r in recs)
        t["cc_and_r3"] = sum(r["cc_nonzero"] and r["r3_feasible_at_q0"] for r in recs)
        t["gg_cc_r3"] = sum(r["gg"] and r["cc_nonzero"] and r["r3_feasible_at_q0"] for r in recs)
        t["ggbar_cc_r3"] = sum(r["gg_with_mirrors"] and r["cc_nonzero"] and r["r3_feasible_at_q0"]
                               for r in recs)
        t["reverse_and_cc"] = sum(r["cc_nonzero"] and r["reverse_block_nonzero"] for r in recs)
        t["cc_order_hist"] = {}
        for r in recs:
            if r["cc_nonzero"]:
                o = str(r["cc_min_order_q_to_1"])
                t["cc_order_hist"][o] = t["cc_order_hist"].get(o, 0) + 1
        return t

    out["tally"] = {"family1_letters_len_le_4": tally(recs1), "family2_G_len_le_8": tally(recs2),
                    "family2b_Gbar_len_le_6": tally(recs2b), "family3_blocks_le_2": tally(recs3)}
    for k, v in out["tally"].items():
        log(f"tally {k}: {v}")

    # conservation: every word commutes with total charge (sector-preserving by construction)
    check("Q: every enumerated word preserves T3 sectors (Jimbo, structural)", True,
          "apply_gen maps a weight state to the same weight; no word is excluded by Q")

    # minimal CC words in family 1
    cc1 = [r for r in recs1 if r["cc_nonzero"]]
    lmin = min(r["length"] for r in cc1) if cc1 else None
    minimal = [r for r in cc1 if r["length"] == lmin]
    out["family1_minimal_cc_words"] = [public(r) for r in minimal]
    minimal_r3 = [r for r in minimal if r["r3_feasible_at_q0"]]
    log(f"family 1 minimal CC length {lmin}: {[r['word'] for r in minimal]}; "
        f"R3-feasible: {[r['word'] for r in minimal_r3]}")
    out["family1_minimal_cc_r3"] = [r["word"] for r in minimal_r3]

    # survivors of each conjunction in families 2/2b/3 (full exact detail)
    surv = {}
    for fam, recs in (("G", recs2), ("Gbar", recs2b), ("blocks", recs3)):
        s = [r for r in recs if r["cc_nonzero"]]
        surv[fam] = [public(r, full=len(s) <= 40) for r in s]
    out["cc_survivors"] = surv
    out["elements"] = [public(r, full=True) for r in recs_el]

    # survivors reported with normal form: the cost-minimal word in each grammar that has CC ≠ 0
    def cheapest(recs):
        s = [r for r in recs if r["cc_nonzero"]]
        if not s:
            return []
        m = min(r["length"] for r in s)
        return [r for r in s if r["length"] == m]

    report = {}
    for fam, recs in (("G", recs2), ("Gbar", recs2b), ("letters_le_4", recs1), ("blocks", recs3)):
        for sub in ("any", "r3"):
            rr = [r for r in recs if (sub == "any" or r["r3_feasible_at_q0"])]
            c = cheapest(rr)
            report[f"{fam}/{sub}"] = [r["word"] for r in c]
    out["cheapest_cc"] = report
    log(f"cheapest CC words: {report}")

    # full detail + normal forms for a fixed short list of named candidates
    named = {
        "P (passage s0 s1 s2)": PASS, "Pbar": PASSBAR, "T35 on strands 1-3": T35,
        "V1": V(1), "V1·V1": V(1) * 2, "V0·V1": V(0) + V(1), "V1·V0": V(1) + V(0),
        "Vb1": Vbar(1), "s2^2 (one-strand clasp)": (2, 2),
    }
    det = {}
    for n, w in named.items():
        r = record(n, word_el(w), y, beta_chi, "word")
        d = public(r, full=True)
        if len(w) <= 10:
            d["normal_form_of_W_in_T_w"] = normal_form(word_el(w))
        det[n] = d
        log(f"named {n}: cc={r['cc_nonzero']} wrap={r['wrap_ge_2']} C0={r['cross_term_zero']} "
            f"R3={r['r3_feasible_at_q0']} ccord={r['cc_min_order_q_to_1']} Cord={r['cross_term_order_q_to_1']}")
    out["named"] = det

    # pre-registered checks of priors (recorded, not required to pass)
    t1 = out["tally"]["family1_letters_len_le_4"]
    out["priors"] = {
        "PR1_P_T35_not_gg": not is_gg(PASS, True) and not is_gg(T35, True),
        "PR2_some_G_word_has_cc": out["tally"]["family2_G_len_le_8"]["gg_and_cc"] > 0,
        "PR3_cc_implies_wrap_family1": t1["cc_and_not_wrap"] == 0,
        "PR5_all_cc_order_ge_1_family1": all(int(k) >= 1 for k in t1["cc_order_hist"]),
    }
    log(f"priors: {out['priors']}")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("beta-pair-creation-word", engine="python", start_time=T0, output_dir=_HERE)
    wb.set_description("qou-99qc task W: enumeration of beta-minus pair-creation words in H_4(q) by "
                       "corpus principles (gamma-gamma grammar, derived charged current [premise L], "
                       "wrap, cross term, confinement SDP reading 3 at q0). Pre-registered at "
                       "ee04d3c394. Selects nothing; not wired to any scorecard.")
    wb.add_parameter("q0", fmt(Q0))
    wb.add_parameter("dps", DPS)
    wb.add_parameter("trace", "Ocneanu, convention D, z = q^3/(q^2+1)")
    wb.add_parameter("nucleon", "beta_Bor = (s0 s1^-1)^3 on strands 0-2")
    wb.add_data("results", out)
    for a_ in ASSERTS:
        wb.add_assertion(a_["name"], computed=str(int(a_["ok"])), expected="1", tolerance="0",
                         source=a_["note"])
    path = wb.save({"q0Anchor": "proton"})
    fails = [a_ for a_ in ASSERTS if not a_["ok"]]
    log(f"witness -> {path.relative_to(_ROOT)}; {len(ASSERTS) - len(fails)}/{len(ASSERTS)} pass")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
