#!/usr/bin/env python3
"""qou-99qc task W, parts 2-3: can candidates A-D be EXCLUDED by proved invariants?

Pre-registered: PREREGISTRATION-exclusions.md (f816f993c8) and PREREGISTRATION-part3.md (3e36b55843),
both before any number here was computed. Lean companion: QOU/QBeta/PairCreationExclusions.lean.

Candidates: A V1^3 = (s1 s2^-1)^3; B passage s0 s1 s2; C s2; D mirror vertices Vb_i = s_i^-1 s_{i+1}.
Process word W = X . beta_Bor, rho(W) = rho(X) rho(beta) (as in part 1).

Per candidate, exact in Q(q):
* chirality: CC block n(x)nu -> p(x)e- and reverse block p(x)e- -> n(x)nu [premise L];
* closure components: lepton cycle of the permutation of W, its size, and for a 2-strand component
  the signed crossing number k (closure T(2,k));
* nucleon sensitivity in the ONE-TERM trace: C1 = tr_D(X beta) - tr_D(beta) tr_D(X);
* the TWO-TERM functional F_c = tr_D + c conn (PREREGISTRATION-part3 §1) in both readings
  T2cov (scored form extended verbatim: quark charge on every strand; covariant) and
  T2lep (labelled comparison, NOT covariant: lepton charge (0,-1) on position 3 [L]):
  conn(W), C2 = conn(Xb) - conn(b) tr(X) - tr(b) conn(X), C22 = -conn(b) conn(X);
* reading 3 at the proton q0 (70 dps), and for B the exact sign of chi_(3,1) on all of (1, inf).
Five strands: separate nu-bar strand, pair created by the U_q singlet cup [L5], gamma-gamma words with
V0, V1, V2 up to length 8 (and mirrors to length 6).

Numbers only at q0 for signs; CODATA is not read; nothing is selected.

Run:  python3 -u beta_pair_exclusions_probe.py 2>&1 | tee /tmp/beta_pair_exclusions_probe.log
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
from sympy import Poly, Symbol, factor, real_roots  # noqa: E402

import beta_pair_creation_word_probe as P1  # noqa: E402  (part-1 engine; its main() is not run)
from hecke_exact import H, KF, ONE, ZERO, reduced_word  # noqa: E402
from jimbo import apply_gen  # noqa: E402
from qou_substrate.precision import fmt  # noqa: E402

mp.mp.dps = P1.DPS
Q0 = P1.Q0
T0 = time.time()
ASSERTS: list = []
QK, HK, TWO = P1.QK, P1.HK, P1.TWO
_X = Symbol("q")


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def check(name, ok, note=""):
    ASSERTS.append({"name": name, "ok": bool(ok), "note": note})
    log(f"{'PASS' if ok else 'FAIL'} {name} {note}")


gk, ev, fx, order1 = P1.gk, P1.ev_frac, P1.fx, P1.order_at_one
word_el, el_mul, el_add, el_scale = P1.word_el, P1.el_mul, P1.el_add, P1.el_scale
BETA, V, Vbar, PASS, PL = P1.BETA, P1.V, P1.Vbar, P1.PASS, P1.PL


# ---------------------------------------------------------------- generic-N helpers
def rho_on(vec, w):
    for g in reversed(w):
        vec = apply_gen(vec, g, inv=False) if g >= 0 else apply_gen(vec, -g - 1, inv=True)
    return vec


def strand_track(w, N):
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


def components(w, N, lep):
    """Lepton closure component of the word w: strands of the cycle containing `lep`, signed
    crossings between each pair inside it."""
    final, crossings = strand_track(w, N)
    cyc, s = [], lep
    while True:
        cyc.append(s)
        s = final[s]
        if s == lep:
            break
    k = 0
    for a, b, sg in crossings:
        if a in cyc and b in cyc:
            k += sg
    out = {"lepton_component_strands": sorted(cyc), "size": len(cyc),
           "self_crossings_signed": k}
    if len(cyc) == 1:
        out["knot"] = "unknot (one-strand closure)"
    elif len(cyc) == 2:
        out["knot"] = f"T(2,{k})" + (" = unknot" if abs(k) == 1 else
                                     " = trefoil" if abs(k) == 3 else "")
    else:
        out["knot"] = f"{len(cyc)}-strand component (not identified, pre-registered)"
    return out


def diag_entries(el, N):
    """<b|rho(el)|b> for every basis state b of V^{(x)N} (KF)."""
    out = {}
    for b in itertools.product((0, 1), repeat=N):
        tot = KF.zero
        for c, w in el:
            img = rho_on({b: ONE}, w)
            tot += c * gk(img.get(b, ZERO))
        out[b] = tot
    return out


def Kw(b):
    return QK ** (len(b) - 2 * sum(b))


def ch3(lep, x):
    return (-3 if x else 0) if lep else (-1 if x else 2)


def allpairs(b, species):
    s = KF.zero
    for i in range(len(b)):
        for j in range(i + 1, len(b)):
            s += KF(ch3(species[i], b[i]) * ch3(species[j], b[j])) / 9
    return s


def traces(el, N, species):
    """one-term tr_D (as the quantum trace) and the connected two-term insertion conn."""
    d = diag_entries(el, N)
    norm = TWO ** N
    tr1 = sum((Kw(b) * v for b, v in d.items()), KF.zero) / norm
    conn = KF.zero
    for k in range(N + 1):
        sect = [b for b in d if sum(b) == k]
        qa = {b: allpairs(b, species) for b in sect}
        mean = sum(qa.values(), KF.zero) / len(sect)
        conn += sum((Kw(b) * (qa[b] - mean) * d[b] for b in sect), KF.zero)
    return tr1, conn / norm


SPECIES = {"T2cov": (False,) * 4, "T2lep": (False, False, False, True)}


# ---------------------------------------------------------------- four strands: candidates
def candidates():
    A = (V(1)) * 3
    c = {
        "A  V1^3": word_el(A),
        "B  passage s0s1s2": word_el(PASS),
        "C  s2": word_el((2,)),
        "C' one-sided weak vertex s2 - h P_L(s2)": P1.weakvertex(2),
        "C'' P_L(s2)": PL(2),
        "Pbar s2^-1 s1^-1 s0^-1": word_el(P1.PASSBAR),
        "A.P_L(s2)": el_mul(word_el(A), PL(2)),
        "P_L(s2).A": el_mul(PL(2), word_el(A)),
        "A.passage": word_el(A + PASS),
        "passage.A": word_el(PASS + A),
        "A.passage.P_L-vertex": el_mul(word_el(A), el_mul(el_mul(P1.weakvertex(0), P1.weakvertex(1)),
                                                         P1.weakvertex(2))),
        "V0V1V0V1": word_el(V(0) + V(1) + V(0) + V(1)),
        "V1V0V1V0": word_el(V(1) + V(0) + V(1) + V(0)),
    }
    return c


def full_record(name, el, y, beta_chi, beta_tr):
    r = P1.record(name, el, y, beta_chi, "word" if len(el) == 1 else "element")
    W = el_mul(el, word_el(BETA))
    out = P1.public(r, full=True)
    if len(el) == 1:
        out["closure"] = components(el[0][1] + BETA, 4, P1.LEP)
    else:
        out["closure"] = "element (sum of words): no single closure"
    out["chiral"] = r["cc_nonzero"] and not r["reverse_block_nonzero"]
    # one-term via the quantum trace (must equal the Markov route of part 1)
    trX, _ = traces(el, 4, SPECIES["T2cov"])
    trW, _ = traces(W, 4, SPECIES["T2cov"])
    C1 = trW - beta_tr["tr"] * trX
    out["one_term_cross_term_exact"] = fx(C1) if C1 != 0 else "0"
    out["one_term_cross_term_order_q_to_1"] = order1(C1)
    out["_C1"] = C1
    out["_r"] = r
    for lab, sp in SPECIES.items():
        trX, cX = traces(el, 4, sp)
        trW, cW = traces(W, 4, sp)
        C2 = cW - beta_tr[lab] * trX - beta_tr["tr"] * cX
        C22 = -beta_tr[lab] * cX
        out[lab] = {
            "conn_W_exact": fx(cW) if cW != 0 else "0",
            "C2_exact": fx(C2) if C2 != 0 else "0",
            "C2_order_q_to_1": order1(C2),
            "C2_at_q0": fmt(ev(C2)) if C2 != 0 else "0",
            "C22_exact": fx(C22) if C22 != 0 else "0",
            "_C2": C2,
        }
    return out


def mixed_sign_roots(f):
    """Exact real roots of numerator and denominator of f in (1, inf)."""
    num = Poly(f.numer.as_expr(), _X)
    den = Poly(f.denom.as_expr(), _X)
    roots = sorted({r for r in real_roots(num) if r > 1} | {r for r in real_roots(den) if r > 1})
    return roots


def five_strands():
    N = 5
    y_words = [reduced_word(p) for p in itertools.permutations(range(N))]
    log(f"H5: validating Markov weights on {len(y_words)} T_w")

    def chis(el):
        d = diag_entries(el, N)
        tr = [sum((v for b, v in d.items() if sum(b) == k), KF.zero) for k in range(3)]
        return {"5": tr[0], "41": tr[1] - tr[0], "32": tr[2] - tr[1]}

    data = []
    for k, w in enumerate(y_words):
        data.append((w, chis(word_el(w)), P1.gk(H.one(N).rmul_word(list(w)).trace())))
        if k % 30 == 0:
            log(f"  H5 T_w {k}/120")
    from sympy import Matrix
    for trip in itertools.combinations(range(len(data)), 3):
        M = Matrix([[data[t][1][l].as_expr() for l in ("5", "41", "32")] for t in trip])
        if M.det().simplify() != 0:
            ysol = M.LUsolve(Matrix([data[t][2].as_expr() for t in trip]))
            break
    y = {l: KF.from_expr(factor(ysol[i])) for i, l in enumerate(("5", "41", "32"))}
    yok = all(sum(y[l] * c[l] for l in y) == t for _, c, t in data)
    check("H5: tr_D = y5 chi5 + y41 chi41 + y32 chi32 on all 120 T_w", yok)
    yq0 = {l: ev(v) for l, v in y.items()}
    check("H5: y_lambda > 0 at q0 for (5),(4,1),(3,2)", all(v > 0 for v in yq0.values()))

    NUC_IN = [(0, 1, 1), (1, 0, 1), (1, 1, 0)]
    NUC_OUT = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    QI = 1 / QK

    def cc5(w):
        final, _ = strand_track(w, N)
        cc = [[KF.zero] * 3 for _ in range(3)]
        rev = [[KF.zero] * 6 for _ in range(3)]
        for j, nb in enumerate(NUC_IN):
            vec = {nb + (0, 1): ONE, nb + (1, 0): ONE * (-QI)}  # n (x) cup
            img = rho_on(vec, w)
            for i, pb in enumerate(NUC_OUT):
                st = pb + (1, 1)
                posv = [0] * N
                for s in range(N):
                    posv[final[s]] = st[s]
                cc[i][j] += gk(img.get(tuple(posv), ZERO))
        for j, pb in enumerate(NUC_OUT):
            img = rho_on({pb + (1, 1): ONE}, w)
            for i, nb in enumerate(NUC_IN):
                for m, lep in enumerate(((0, 1), (1, 0))):
                    st = nb + lep
                    posv = [0] * N
                    for s in range(N):
                        posv[final[s]] = st[s]
                    rev[j][2 * i + m] += gk(img.get(tuple(posv), ZERO))
        return any(e != 0 for r in cc for e in r), any(e != 0 for r in rev for e in r), cc

    def vtx(i):
        return (i, -(i + 1) - 1)

    def vbar(i):
        return (-i - 1, i + 1)

    blocks = [("V0", vtx(0)), ("V1", vtx(1)), ("V2", vtx(2))]
    mblocks = blocks + [("Vb0", vbar(0)), ("Vb1", vbar(1)), ("Vb2", vbar(2))]
    fams = {"G5_len_le_8": [], "Gbar5_len_le_6": []}
    for fam, bl, kmax in (("G5_len_le_8", blocks, 4), ("Gbar5_len_le_6", mblocks, 3)):
        for k in range(1, kmax + 1):
            for combo in itertools.product(bl, repeat=k):
                fams[fam].append(("".join(n for n, _ in combo), sum((w for _, w in combo), ())))
    out = {"markov_weights_q0": {l: fmt(v) for l, v in yq0.items()},
           "pair_state": "U_q singlet cup ud - q^-1 du on strands 3,4 [L5]; e- = d, nu-bar = d"}
    for fam, words in fams.items():
        recs = []
        for k, (n, w) in enumerate(words):
            W = w + BETA
            ccnz, revnz, _ = cc5(W)
            c = chis(word_el(W))
            r3 = all(ev(v) >= 0 for v in c.values())
            final, _ = strand_track(W, N)
            recs.append({"word": n, "length": len(w), "cc5": ccnz, "reverse_nonzero": revnz,
                         "r3": r3, "pure": final == list(range(N)),
                         "lepton_component": components(W, N, 3)["knot"]})
            if k % 40 == 0:
                log(f"  {fam}: {k}/{len(words)}")
        surv = [r for r in recs if r["cc5"] and r["r3"]]
        lmin = min((r["length"] for r in surv), default=None)
        out[fam] = {"n_words": len(recs), "cc5": sum(r["cc5"] for r in recs),
                    "cc5_and_r3": len(surv),
                    "cheapest_cc5_r3": [r for r in surv if r["length"] == lmin],
                    "chiral_among_cc5_r3": [r["word"] for r in surv if not r["reverse_nonzero"]],
                    "cc5_r3_words": [r["word"] for r in surv],
                    "cc5_r3_records": surv}
        log(f"{fam}: cc5={out[fam]['cc5']}, cc5&r3={len(surv)}, cheapest="
            f"{[r['word'] for r in out[fam]['cheapest_cc5_r3']]}")
    return out


def main():
    out: dict = {}
    y, yok, _ = P1.solve_y()
    check("V4 (part 1): tr_D = sum y chi on all 24 T_w of H_4", yok)
    beta_el = word_el(BETA)
    beta_chi, _, _ = P1.analyse_element(beta_el)
    trB, _ = traces(beta_el, 4, SPECIES["T2cov"])
    check("V7: quantum trace Tr(K^4 rho)/[2]^4 of beta equals tr_D(beta) (sum y chi)",
          trB == sum(y[l] * beta_chi[l] for l in y))
    for w in [(), (0,), (0, 1), (2, 1, 0), (0, -2, 1), (1, 2) * 2]:
        tq, _ = traces(word_el(w), 4, SPECIES["T2cov"])
        if tq != P1.hecke_trace_word(w):
            check(f"V8: quantum trace = Hecke Markov trace on {w}", False)
            break
    else:
        check("V8: quantum trace = Hecke Markov trace on 6 test words", True)
    beta_tr = {"tr": trB}
    for lab, sp in SPECIES.items():
        _, cb = traces(beta_el, 4, sp)
        beta_tr[lab] = cb
        out[f"conn_beta_{lab}"] = fx(cb) if cb != 0 else "0"
    check("P-T1: covariant all-pairs conn(beta) = 0 on four strands", beta_tr["T2cov"] == 0)
    log(f"conn(beta) T2lep = {out['conn_beta_T2lep']}")

    recs = {}
    for name, el in candidates().items():
        recs[name] = full_record(name, el, y, beta_chi, beta_tr)
        r = recs[name]
        log(f"{name}: chiral={r['chiral']} cc={r['cc_nonzero']} rev={r['reverse_block_nonzero']} "
            f"R3={r['r3_feasible_at_q0']} C1={r['one_term_cross_term_exact'][:40]} "
            f"T2cov.C2={r['T2cov']['C2_exact']} T2lep.C2ord={r['T2lep']['C2_order_q_to_1']} "
            f"closure={r['closure'] if isinstance(r['closure'], str) else r['closure']['knot']}")
    # cross-checks against part 1 / Lean
    for name, r in recs.items():
        if r["_C1"] != r["_r"]["_Cx"]:
            check(f"V9: one-term cross term via quantum trace = part-1 Markov route ({name})", False)
            break
    else:
        check("V9: one-term cross term via quantum trace = part-1 Markov route (all candidates)", True)
    check("Lean twoTerm_allPairs_scalar: T2cov C2 = 0 for every candidate",
          all(r["T2cov"]["_C2"] == 0 for r in recs.values()))
    check("Lean crossTerm_lastLetter_eq_zero: C1 = 0 for s2, the one-sided weak vertex and P_L(s2)",
          all(recs[n]["_C1"] == 0 for n in ("C  s2", "C' one-sided weak vertex s2 - h P_L(s2)",
                                            "C'' P_L(s2)")))
    check("Lean trackA: A's lepton closes on itself",
          recs["A  V1^3"]["closure"]["size"] == 1)

    # ---------- mirror ties (D): the eight length-6 Gbar words that pass CC and R3 in part 1
    fam2b = P1.gg_words(6, mirrors=True)
    ties = []
    for n, w in fam2b:
        if len(w) != 6 or P1.is_gg(w):
            continue
        rr = P1.record(n, word_el(w), y, beta_chi, "word")
        if rr["cc_nonzero"] and rr["r3_feasible_at_q0"]:
            ties.append(full_record(n, word_el(w), y, beta_chi, beta_tr))
    out["mirror_ties_len6"] = [{k: v for k, v in t.items() if not k.startswith("_")} | {
        "T2cov": {k: v for k, v in t["T2cov"].items() if not k.startswith("_")},
        "T2lep": {k: v for k, v in t["T2lep"].items() if not k.startswith("_")}} for t in ties]
    log(f"mirror ties: {[(t['name'], t['chiral'], t['closure']['knot']) for t in ties]}")
    check("D: part-1 tie set reproduced: 7 mirror-containing length-6 words (+ V1^3 = the 8 of part 1)",
          len(ties) == 7, f"n={len(ties)}")

    # ---------- B: sign of chi_(3,1)(W_B) on all of (1, inf)
    rB = recs["B  passage s0s1s2"]["_r"]
    bsign = {}
    for lab in ("4", "31", "22"):
        f = rB["_chiW"][lab]
        roots = mixed_sign_roots(f)
        pts = [mp.mpf("1.0001")] + [mp.mpf(str(r.evalf(80))) + mp.mpf("1e-6") for r in roots]
        bsign[lab] = {"exact": fx(f), "real_roots_gt_1": [str(r) for r in roots],
                      "sign_on_intervals_from_1": [int(mp.sign(ev(f, p))) for p in pts]}
    out["B_characters_sign_map"] = bsign
    chB = rB["_chiW"]
    check("B: chi_4(W_B) = q^3, chi_(3,1)(W_B) = -(q^6 - q^4 + 1)/q, chi_(2,2)(W_B) = 0 (exact)",
          chB["4"] == QK ** 3 and chB["31"] == -(QK ** 6 - QK ** 4 + 1) / QK and chB["22"] == 0)
    log(f"B characters: { {k: (v['real_roots_gt_1'], v['sign_on_intervals_from_1']) for k, v in bsign.items()} }")

    # ---------- five strands
    out["five_strands"] = five_strands()

    out["candidates"] = {n: {k: v for k, v in r.items() if not k.startswith("_")} | {
        "T2cov": {k: v for k, v in r["T2cov"].items() if not k.startswith("_")},
        "T2lep": {k: v for k, v in r["T2lep"].items() if not k.startswith("_")}}
        for n, r in recs.items()}

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("beta-pair-exclusions", engine="python", start_time=T0, output_dir=_HERE)
    wb.set_description("qou-99qc task W parts 2-3: exclusion tests for the beta-minus pair-creation "
                       "candidates A (V1^3), B (passage), C (s2), D (mirror vertices): chirality, "
                       "closure component, one-term and two-term (covariant / lepton-labelled) cross "
                       "terms, reading 3, five strands. Pre-registered f816f993c8 + 3e36b55843. "
                       "Selects nothing; not wired to any scorecard.")
    wb.add_parameter("q0", fmt(Q0))
    wb.add_parameter("dps", P1.DPS)
    wb.add_parameter("trace_one_term", "Ocneanu convention D = Tr(K^n rho)/[2]^n")
    wb.add_parameter("trace_two_term", "PREREGISTRATION-part3 §1; c not chosen (#8524)")
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
