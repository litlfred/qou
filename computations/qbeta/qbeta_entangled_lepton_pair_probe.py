#!/usr/bin/env python3
"""P2: beta-minus with the e- nubar pair as ONE non-factorising braid word.

Bean qou-99qc.  Pre-registration (committed BEFORE this script was run):
docs/audits/2026-11-20-beta-entangled-lepton-pair.md  section 0.

What this computes, exactly over Q(q) (sympy QQ.frac_field, no float):

* Markov trace, convention D (z = q^3/(q^2+1), tr 1 = 1), of
    - the nucleons  p, n = nuc11_interleaved (pyhecke.atom.build_atom_nf_exact,
      transcribed from qbeta_delta_candidate_census_probe.py) on 3 strands,
      and the bare Borromean core beta_Bor = (s0 s1^-1)^3 (the word inside F_Bor);
    - e-  = trefoil T(2,3) = s^3 on 2 strands      (def:electron-knot);
    - nubar = identity on 1 strand                    (def:antineutrino-knot);
    - pair words P_k = s0^3 s1^{2k} on 3 strands, k in {-1,0,1};
    - final-state words W_{j,k} = p(s0,s1) . s2^{2j} . s3^3 . s4^{2k} on 6 strands.
* the trace channel F(b) = |tr_D(b)| [N]_q! / q^N on N strands, E_T = m_mu F,
  m_mu = m_e Vol(4_1)/hbar_q^2 (the linear part of the canonical m_p identity);
* X(j,k) = E(W) - E(p) - E(e-) - E(nubar), DeltaX = X(j,k) - X(0,0),
  Q(j,k) = E(n) - E(W);
* q -> 1 limits and values at the proton pin q0 (70 dps).

Volume channel: trefoil and unknot are non-hyperbolic (Vol = 0, #8659); the
entangled closures' volumes are NOT computed here (no SnapPy) and are reported
as unevaluated, never as 0.

Two independent Hecke engines are used and must agree on every 3-strand word:
(A) the permutation-basis engine + Ocneanu recursion of pyhecke.tl (general N);
(B) the six-coordinate NF engine that mirrors QOU/Machinery/MarkovTraceOnHecke.lean
    (mulsigma0 / mulsigma1 / TRM), 3 strands only.
"""
from __future__ import annotations

import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations", "computations/substrate", "tools/qou-substrate/python",
           "tools/pyhecke/python"):
    _s = os.path.join(ROOT, _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from pyhecke import tl  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from qou_substrate.constants import q_at, M_E_MEV_STR, Q_NEUTRON_MEV_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = 70
mp.mp.dps = DPS
T0 = time.time()

qs = sp.Symbol("q")
K = sp.QQ.frac_field(qs)
q = K.convert(qs)
ONE = K.one
ZERO = K.zero
H = q - ONE / q
Z = q ** 3 / (q ** 2 + ONE)
HALF = K.convert(sp.Rational(1, 2))


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


# ------------------------------------------------------------------ engine A
# A word is a list of factors (g, c, d) meaning (c*sigma_g + d), 0-based g.
def letter(g, c=None, d=None):
    return (g, ONE if c is None else c, ZERO if d is None else d)


def inv(g):            # sigma^-1 = sigma - h
    return (g, ONE, -H)


def mul_factor(elem, fac):
    g, c, d = fac
    out = {}
    if c != ZERO:
        for p, v in tl._mul_gen(elem, g, H).items():
            out[p] = out.get(p, ZERO) + c * v
    if d != ZERO:
        for p, v in elem.items():
            out[p] = out.get(p, ZERO) + d * v
    return {p: v for p, v in out.items() if v != ZERO}


def element(word, n):
    e = {tuple(range(1, n + 1)): ONE}
    for fac in word:
        assert fac[0] <= n - 2, (fac, n)
        e = mul_factor(e, fac)
    return e


def trace_A(word, n):
    e = element(word, n)
    cache = {}
    tot = ZERO
    for p, v in e.items():
        tot = tot + v * tl.markov_trace_basis(p, n, H, Z, ONE, cache)
    return tot


# ------------------------------------------------------------------ engine B
# Mirror of QOU/Machinery/MarkovTraceOnHecke.lean (namespace H3).
def mulB(v, g):
    if g == 0:
        return [v[1], v[0] + H * v[1], v[3], v[2] + H * v[3], v[5], v[4] + H * v[5]]
    return [v[2], v[4], v[0] + H * v[2], v[5], v[1] + H * v[4], v[3] + H * v[5]]


TRM = [ONE, Z, Z, Z ** 2, Z ** 2, H * Z ** 2 + Z]


def trace_B(word):
    v = [ONE] + [ZERO] * 5
    for g, c, d in word:
        m = mulB(v, g)
        v = [c * m[i] + d * v[i] for i in range(6)]
    return sum((v[i] * TRM[i] for i in range(6)), ZERO)


# ------------------------------------------------------------------ words
def shift(word, s):
    return [(g + s, c, d) for g, c, d in word]


B3 = [letter(0), inv(1)] * 3                       # (s0 s1^-1)^3 = beta_Bor


def nuc11(kind):
    w = list(B3)
    if kind == "p":
        w += [letter(0), letter(0, d=-H * HALF), letter(1, d=-H * HALF)]
    else:
        w += [letter(0, d=-H * HALF), letter(0, d=-H * HALF), letter(1, d=-H)]
    w += [letter(0), letter(0)]                    # gluon s0 s0
    return w


def power(g, k):
    return [letter(g)] * k if k >= 0 else [inv(g)] * (-k)


TREFOIL = power(0, 3)


def pair(k):          # e- on strands 1-2, nubar on strand 3, 2k crossings between
    return TREFOIL + power(1, 2 * k)


def final(pw, j, k):  # proton 1-3, e- 4-5, nubar 6
    return list(pw) + power(2, 2 * j) + shift(TREFOIL, 3) + power(4, 2 * k)


def interleaved(pw, ab, de):
    """Family B (amendment, see audit section 0.5): the trefoil s3^3 on strands
    4-5 with proton clasps s2^{2a} and nubar clasps s4^{2d} inserted BETWEEN its
    crossings, so the top generators recur and the Markov peel cannot strip them."""
    w = list(pw)
    for (a, d) in zip(ab, de):
        w += [letter(3)] + power(2, 2 * a) + power(4, 2 * d)
    return w


def clasp2(a):
    """A^a with A = s2 s1^2 s2^-1: strand 4 (the electron) loops proton strand 2,
    passing proton strand 3, so the lepton word touches TWO proton strands and the
    one-strand connected-sum factorisation no longer applies (family C)."""
    if a == 0:
        return []
    return [letter(2)] + power(1, 2 * a) + [inv(2)]


def interleaved2(pw, ab):
    w = list(pw)
    for a in ab:
        w += [letter(3)] + clasp2(a)
    return w


def full_twist(gens, t):
    """Delta^{2t} on the strands spanned by consecutive generators `gens`:
    (s_a ... s_b)^{(b-a+2) t}. Central in that braid subgroup, so it is the one
    entangler that prefers no strand order (family D)."""
    m = len(gens) + 1
    if t >= 0:
        return [letter(g) for g in gens] * (m * t)
    return [inv(g) for g in reversed(gens)] * (m * (-t))


def family_d_word(pw, span, t, k):
    return list(pw) + full_twist(span, t) + shift(TREFOIL, 3) + power(4, 2 * k)


def qfact(n):
    r = ONE
    for m in range(1, n + 1):
        r = r * (q ** m - q ** (-m)) / (q - ONE / q)
    return r


def to_expr(x):
    return sp.factor(K.to_sympy(x))


def ev(x, qv):
    num, den = sp.fraction(sp.together(K.to_sympy(x)))
    pn = sp.Poly(num, qs)
    pd = sp.Poly(den, qs)

    def peval(P):
        acc = mp.mpf(0)
        for c in P.all_coeffs():
            acc = acc * qv + mp.mpf(sp.Rational(c).p) / mp.mpf(sp.Rational(c).q)
        return acc
    return peval(pn) / peval(pd)


def at_one(x):
    return sp.limit(K.to_sympy(x), qs, 1)


def fmt(x):
    return mp.nstr(x, 50)


def main():
    q0 = q_at(DPS)
    assert mp.nstr(q0, 49)[:40] == Q_50_DIGIT_STR[:40]
    m_e = mp.mpf(M_E_MEV_STR)
    vol41 = 2 * mp.clsin(2, mp.pi / 3)
    hbar = (q0 - 1) / q0
    m_mu = m_e * vol41 / hbar ** 2
    q_codata = mp.mpf(Q_NEUTRON_MEV_STR)
    checks = []

    def check(name, ok, note=""):
        checks.append((name, bool(ok), note))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name} {note}")

    # ---- traces
    log("traces on 1-3 strands (two engines)")
    tr = {}
    for name, w in [("beta_Bor", B3), ("p", nuc11("p")), ("n", nuc11("n")),
                    ("e", TREFOIL), ("pair_m1", pair(-1)), ("pair_0", pair(0)),
                    ("pair_p1", pair(1))]:
        a = trace_A(w, 3)
        b = trace_B(w)
        check(f"engineA==engineB {name}", a == b)
        tr[name] = a
    tr["nu"] = ONE
    hb = H
    closed = (4 + hb ** 2 - 3 * hb ** 4 - hb ** 6) / (hb ** 2 + 4)
    check("tr(beta_Bor) == Lean closed form (BorromeanMarkovTrace)", tr["beta_Bor"] == closed)
    check("tr(e) == (h^2+1) z + h", tr["e"] == (H ** 2 + ONE) * Z + H)
    check("tr(pair_0) == tr(e)  (nubar unlinked: Markov restriction)", tr["pair_0"] == tr["e"])
    lam_p = ONE + H * Z
    lam_m = ONE - H * Z + H ** 2
    check("lam_+ = 1 + h z = (q^4+1)/(q^2+1)", lam_p == (q ** 4 + 1) / (q ** 2 + 1))
    check("lam_- = 1 - h z + h^2 = (q^4+1)/(q^2 (q^2+1))", lam_m == (q ** 4 + 1) / (q ** 2 * (q ** 2 + 1)))
    check("tr(pair_+-1) == tr(e) lam_+-", tr["pair_p1"] == tr["e"] * lam_p and tr["pair_m1"] == tr["e"] * lam_m)

    log("final-state words on 6 strands")
    for pk in ("p", "beta_Bor"):
        pw = nuc11("p") if pk == "p" else B3
        for j in (-1, 0, 1):
            for k in (-1, 0, 1):
                tr[f"W_{pk}_{j}_{k}"] = trace_A(final(pw, j, k), 6)
                log(f"  W[{pk}] j={j} k={k} done")
        check(f"multiplicativity tr(W_{pk}_0_0) == tr({pk}) tr(e)",
              tr[f"W_{pk}_0_0"] == tr[pk] * tr["e"])
        lam = {1: ONE + H * Z, 0: ONE, -1: ONE - H * Z + H ** 2}
        check(f"clasp factorisation tr(W_{pk}_j_k) == tr({pk}) tr(e) lam_j lam_k, all j,k",
              all(tr[f"W_{pk}_{j}_{k}"] == tr[pk] * tr["e"] * lam[j] * lam[k]
                  for j in (-1, 0, 1) for k in (-1, 0, 1)))
        check(f"tr(W_{pk}_0_k) == tr({pk}) tr(pair_k), k=+-1",
              all(tr[f"W_{pk}_0_{k}"] == tr[pk] * tr[{-1: 'pair_m1', 1: 'pair_p1'}[k]]
                  for k in (-1, 1)))

    # ---- Family B: genuinely interleaved entanglement
    import itertools
    if os.environ.get("P2_SKIP_B"):
        famB_iter = []
    else:
        famB_iter = None
    log("family B: 729 interleaved words x 3 nucleon words on 6 strands")
    famB = []
    trs3 = {"p": tr["p"], "n": tr["n"], "beta_Bor": tr["beta_Bor"]}
    blind = 0
    for idx, (ab, de) in enumerate(famB_iter if famB_iter is not None else itertools.product(
            itertools.product((-1, 0, 1), repeat=3), itertools.product((-1, 0, 1), repeat=3))):
        R = {}
        for pk, pw in (("p", nuc11("p")), ("n", nuc11("n")), ("beta_Bor", B3)):
            R[pk] = trace_A(interleaved(pw, ab, de), 6)
        is_blind = all(R[pk] * trs3["p"] == R["p"] * trs3[pk] for pk in ("n", "beta_Bor"))
        blind += is_blind
        famB.append((ab, de, R, is_blind))
        if idx % 81 == 0:
            log(f"  family B {idx}/729, proton-blind so far {blind}")
    tr["_famB"] = famB

    log("family C: 27 two-proton-strand clasp words x 3 nucleon words")
    famC = []
    for ab in itertools.product((-1, 0, 1), repeat=3):
        R = {pk: trace_A(interleaved2(pw, ab), 6)
             for pk, pw in (("p", nuc11("p")), ("n", nuc11("n")), ("beta_Bor", B3))}
        is_blind = all(R[pk] * trs3["p"] == R["p"] * trs3[pk] for pk in ("n", "beta_Bor"))
        famC.append((ab, R, is_blind))
    log(f"  family C proton-blind: {sum(b for _, _, b in famC)}/27")

    log("family D: full twist on (proton strands 2-3 + e-) or (proton 1-3 + e-)")
    famD = []
    for span_name, span in (("D3_strands_2_4", [1, 2]), ("D4_strands_1_4", [0, 1, 2])):
        for t in (-1, 1):
            for k in (-1, 0, 1):
                R = {pk: trace_A(family_d_word(pw, span, t, k), 6)
                     for pk, pw in (("p", nuc11("p")), ("n", nuc11("n")), ("beta_Bor", B3))}
                is_blind = all(R[pk] * trs3["p"] == R["p"] * trs3[pk] for pk in ("n", "beta_Bor"))
                famD.append((span_name, t, k, R, is_blind))
                log(f"  D {span_name} t={t} k={k} blind={is_blind}")

    # ---- energies at q0 (trace channel)
    def F(x, n):
        return abs(ev(x, q0)) * ev(qfact(n), q0) / q0 ** n

    nstr = {"beta_Bor": 3, "p": 3, "n": 3, "e": 2, "nu": 1}
    E = {k: m_mu * F(tr[k], nstr[k]) for k in nstr}
    rows = []
    for pk in ("p", "beta_Bor"):
        for j in (-1, 0, 1):
            for k in (-1, 0, 1):
                key = f"W_{pk}_{j}_{k}"
                EW = m_mu * F(tr[key], 6)
                X = EW - E[pk] - E["e"] - E["nu"]
                row = {"proton_word": pk, "j": j, "k": k,
                       "tr_exact": str(to_expr(tr[key])),
                       "tr_q0": fmt(ev(tr[key], q0)),
                       "tr_q_to_1": str(at_one(tr[key])),
                       "E_W_MeV": fmt(EW), "X_MeV": fmt(X)}
                if pk == "p":
                    Qv = E["n"] - EW
                    row["Q_MeV"] = fmt(Qv)
                    row["Q_over_Qbeta_codata"] = fmt(Qv / q_codata)
                rows.append(row)
    c6 = ev(qfact(6), q0) / q0 ** 6
    famB_rows = []
    for ab, de, R, is_blind in famB:
        EWp = m_mu * abs(ev(R["p"], q0)) * c6
        EWn = m_mu * abs(ev(R["n"], q0)) * c6
        famB_rows.append({"proton_clasps": list(ab), "nubar_clasps": list(de),
                          "tr_p_q0": fmt(ev(R["p"], q0)), "tr_q_to_1": str(at_one(R["p"])),
                          "X_MeV": fmt(EWp - E["p"] - E["e"] - E["nu"]),
                          "Q_MeV": fmt(E["n"] - EWp),
                          "Q_cross_n_minus_p_final_MeV": fmt(EWn - EWp),
                          "proton_blind": is_blind})
    nblind = sum(r["proton_blind"] for r in famB_rows)
    Qs = [mp.mpf(r["Q_MeV"]) for r in famB_rows]
    Xs = [mp.mpf(r["X_MeV"]) for r in famB_rows]
    trB = [mp.mpf(r["tr_p_q0"]) for r in famB_rows]
    zero_tr = sum(1 for _, _, R, _ in famB if R["p"] == ZERO)
    print(f"\n=== family B: {len(famB_rows)} words; proton-blind (tr(W)/tr(nucleon) same for p, n, beta_Bor): {nblind}")
    print(f"  exact tr_W == 0 : {zero_tr}")
    if famB_rows:
        print(f"  tr_W(q0) range [{mp.nstr(min(trB), 12)}, {mp.nstr(max(trB), 12)}]")
        print(f"  X range  [{mp.nstr(min(Xs), 12)}, {mp.nstr(max(Xs), 12)}] MeV")
        print(f"  Q range  [{mp.nstr(min(Qs), 12)}, {mp.nstr(max(Qs), 12)}] MeV")
    famD_rows = []
    for span_name, t, k, R, is_blind in famD:
        EWp = m_mu * abs(ev(R["p"], q0)) * c6
        EWn = m_mu * abs(ev(R["n"], q0)) * c6
        Xex = (R["p"] - tr["p"] * tr["e"])
        famD_rows.append({"span": span_name, "twist": t, "nubar_clasp": k,
                          "tr_p_exact": str(to_expr(R["p"])),
                          "tr_p_q0": fmt(ev(R["p"], q0)), "tr_p_q_to_1": str(at_one(R["p"])),
                          "tr_n_q0": fmt(ev(R["n"], q0)),
                          "trace_cross_term_exact": str(to_expr(Xex)),
                          "trace_cross_term_q_to_1": str(at_one(Xex)),
                          "X_MeV": fmt(EWp - E["p"] - E["e"] - E["nu"]),
                          "Q_MeV": fmt(E["n"] - EWp),
                          "final_state_n_minus_p_MeV": fmt(EWn - EWp),
                          "proton_blind": is_blind})
    print("\n=== family D")
    for r in famD_rows:
        print(f"  {r['span']} t={r['twist']:+d} k={r['nubar_clasp']:+d} blind={r['proton_blind']}  "
              f"trW(q0)={mp.nstr(mp.mpf(r['tr_p_q0']), 15)}  X={mp.nstr(mp.mpf(r['X_MeV']), 10)}  "
              f"Q={mp.nstr(mp.mpf(r['Q_MeV']), 10)}  q->1 tr={r['tr_p_q_to_1']}")
    famC_rows = []
    for ab, R, is_blind in famC:
        EWp = m_mu * abs(ev(R["p"], q0)) * c6
        famC_rows.append({"proton_two_strand_clasps": list(ab),
                          "tr_p_exact": str(to_expr(R["p"])),
                          "tr_p_q0": fmt(ev(R["p"], q0)), "tr_q_to_1": str(at_one(R["p"])),
                          "ratio_n_over_p_final_trace_q0": fmt(ev(R["n"], q0) / ev(R["p"], q0)),
                          "X_MeV": fmt(EWp - E["p"] - E["e"] - E["nu"]),
                          "Q_MeV": fmt(E["n"] - EWp), "proton_blind": is_blind})
    print(f"\n=== family C: proton-blind {sum(r['proton_blind'] for r in famC_rows)}/27")
    for r in famC_rows:
        print(f"  {r['proton_two_strand_clasps']}  trW(q0)={mp.nstr(mp.mpf(r['tr_p_q0']), 15)}  "
              f"X={mp.nstr(mp.mpf(r['X_MeV']), 10)}  Q={mp.nstr(mp.mpf(r['Q_MeV']), 10)}  blind={r['proton_blind']}")
    for r in rows:
        base = next(s for s in rows if s["proton_word"] == r["proton_word"]
                    and s["j"] == 0 and s["k"] == 0)
        r["DeltaX_MeV"] = fmt(mp.mpf(r["X_MeV"]) - mp.mpf(base["X_MeV"]))

    # exact X(0,0) structure: F is multiplicative in tr, strand factor is not
    print("\n=== exact traces")
    for k in ("beta_Bor", "p", "n", "e", "pair_m1", "pair_0", "pair_p1"):  # noqa
        print(f"  tr({k}) = {to_expr(tr[k])}   q->1: {at_one(tr[k])}   q0: {mp.nstr(ev(tr[k], q0), 25)}")
    print("\n=== energies at q0 (trace channel, MeV)")
    for k, v in E.items():
        print(f"  E({k}) = {mp.nstr(v, 25)}")
    print("\n=== final-state rows")
    for r in rows:
        print(f"  {r['proton_word']:8s} j={r['j']:+d} k={r['k']:+d}  trW(q0)={mp.nstr(mp.mpf(r['tr_q0']), 15):>22s}"
              f"  X={mp.nstr(mp.mpf(r['X_MeV']), 12):>18s}  dX={mp.nstr(mp.mpf(r['DeltaX_MeV']), 12):>18s}"
              + (f"  Q={mp.nstr(mp.mpf(r['Q_MeV']), 12)}" if "Q_MeV" in r else ""))
    print(f"\n  Q_beta CODATA (comparison only) = {mp.nstr(q_codata, 15)} MeV; m_mu(q0) = {mp.nstr(m_mu, 20)}")
    assert all(ok for _, ok, _ in checks), "a check failed"

    if os.environ.get("P2_SKIP_B"):
        log("P2_SKIP_B set: preview only, no witness written")
        return
    w = WitnessBuilder("qbeta-entangled-lepton-pair")
    w.set_description(
        "P2 (qou-99qc): beta-minus with the e- nubar pair as one braid word. Exact "
        "convention-D Markov traces over Q(q) of nucleon (nuc11_interleaved, beta_Bor), "
        "trefoil, unknot, linked pair words s0^3 s1^{2k} and six-strand final states "
        "p.s2^{2j}.s3^3.s4^{2k}; trace-channel energies E = m_mu |tr| [N]!/q^N, cross "
        "term X, Q = E(n) - E(W). Enumeration over j,k; nothing selected by CODATA.")
    w.add_data("q0_anchor", "proton")
    w.add_data("q0_value", Q_50_DIGIT_STR)
    w.add_data("dps", DPS)
    w.add_data("m_mu_MeV", fmt(m_mu))
    base_keys = [k for k in tr if not k.startswith(("W_", "_"))]
    w.add_data("exact_traces", {k: str(to_expr(tr[k])) for k in base_keys})
    w.add_data("traces_q_to_1", {k: str(at_one(tr[k])) for k in base_keys})
    w.add_data("energies_trace_channel_MeV", {k: fmt(v) for k, v in E.items()})
    w.add_data("final_state_rows", rows)
    w.add_data("family_D_full_twist", {"count": len(famD_rows),
        "proton_blind_count": sum(r["proton_blind"] for r in famD_rows), "rows": famD_rows})
    w.add_data("family_C_two_strand_clasp", {"count": len(famC_rows),
        "proton_blind_count": sum(r["proton_blind"] for r in famC_rows), "rows": famC_rows})
    w.add_data("family_B_interleaved", {"count": len(famB_rows), "proton_blind_count": nblind,
                                        "exact_zero_trace_count": zero_tr,
                                        "X_MeV_min": fmt(min(Xs)), "X_MeV_max": fmt(max(Xs)),
                                        "Q_MeV_min": fmt(min(Qs)), "Q_MeV_max": fmt(max(Qs)),
                                        "rows": famB_rows})
    w.add_data("clasp_factor", {"lam_plus": "(q^4+1)/(q^2+1)", "lam_minus": "(q^4+1)/(q^2 (q^2+1))",
                                "lam_plus_q0": fmt(ev(ONE + H * Z, q0)),
                                "lam_minus_q0": fmt(ev(ONE - H * Z + H ** 2, q0))})
    c = {n_: ev(qfact(n_), q0) / q0 ** n_ for n_ in (1, 2, 3, 6)}
    w.add_data("strand_factor_q0", {str(n_): fmt(v) for n_, v in c.items()})
    w.add_data("E_n_minus_E_p_MeV", fmt(E["n"] - E["p"]))
    x00_units = {"q_to_1_X00_over_m_mu": "175 = (1/2)(1/2)720 - (1/2)6 - (1/2)2 - 1"}
    w.add_data("X00_q_to_1", x00_units)
    w.add_data("Q_beta_CODATA_MeV_comparison_only", fmt(q_codata))
    w.add_data("volume_channel", "e- and nubar: Vol = 0 (non-hyperbolic). Entangled closures: "
               "NOT computed (no SnapPy); unevaluated, not zero.")
    w.add_caveat("Trace channel strand factor [N]_q!/q^N is defined by the corpus only at N=3 "
                 "(F_Bor); its use at N=1,2,6 is this probe's extension. The -12 m_e offset of "
                 "the m_p identity (a recorded FIT) is excluded. Linking letters are a choice "
                 "(the corpus only ever writes the pair as a disjoint union) and are enumerated.")
    for name, ok, note in checks:
        w.add_assertion(name, "1" if ok else "0", "1", "0", source=note or name)
    log(f"wrote {w.save({'q0Anchor': 'proton', 'q0Value': Q_50_DIGIT_STR})}")


if __name__ == "__main__":
    main()
