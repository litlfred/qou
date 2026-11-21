#!/usr/bin/env python3
"""qou-99qc route L: the additive log-trace energy E_kappa = kappa * log|tr| on the P1/P2/P3 words.

Pre-registered in PREREGISTRATION.md (commit 9ce0a5fef8) before anything here was computed.
Lean companion: QOU/QBeta/LogTraceAdditiveEnergy.lean.

Everything is exact in Q(q) (sympy fraction field, vendored P1 engine `hecke_exact.py`) until the
final read-out at the proton pin q0 with mpmath at 70 dps. No float anywhere.

Outputs, per word W built from pieces X_i:
  R(W)      = tr W / prod tr X_i            (exact rational function of q)
  C_log(W)  = log|R(W)|                     (the cross term of E_kappa, divided by kappa)
and the decay balance Q/kappa = log|tr(initial)| - log|tr(final)|.

kappa is NOT chosen here. The corpus offers alpha = E0 = m_e/(q0(q0-1)) (B_sym binding
normalisation, docs/audits/2026-06-16-b-sym-linear-chain-closed-form.md) and its tower-summed
form E0/(1 - hbar_q^2) (owner ruling 2026-09-05 for the Q_beta scale). Both are reported, with
both signs, plus the kappa each row would need for CODATA Q_beta (comparison only).
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))
sys.path.insert(0, str(_HERE))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

import qou_substrate.constants as C  # noqa: E402
from qou_substrate.precision import fmt  # noqa: E402
from hecke_exact import H, KF, embed, h, q  # noqa: E402

DPS = 70
mp.mp.dps = DPS
T0 = time.time()
ASSERTS: list = []
QS = sp.Symbol("q")


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def check(name, ok, note=""):
    ASSERTS.append({"name": name, "ok": bool(ok), "note": note})
    log(("PASS " if ok else "FAIL ") + name + (f" -- {note}" if note else ""))


# ------------------------------------------------------------------ exact helpers
def ground(x):
    """RING element with no photon variables -> KF element."""
    return x.coeff(1)


def tr(x: H):
    return ground(x.trace())


def to_expr(f):
    return sp.sympify(f.as_expr()).subs(sp.Symbol("q"), QS)


def ev(f, qv):
    """Exact KF element evaluated at an mpf q (rational coefficients kept exact)."""
    def pe(P):
        tot = mp.mpf(0)
        for (e,), c in P.terms():
            tot += mp.mpf(int(c.numerator)) / mp.mpf(int(c.denominator)) * qv ** e
        return tot
    return pe(f.numer) / pe(f.denom)


def at_one(f):
    return sp.nsimplify(sp.limit(to_expr(f), QS, 1))


def affine(x: H, g, c, d):
    """x * (c sigma_g + d)."""
    out = H(x.N)
    if c != 0:
        out = out + x.rmul_gen(g).scale(c)
    if d != 0:
        out = out + x.scale(d)
    return out


def word_elem(N, letters, start=None):
    x = H.one(N) if start is None else start
    for g, c, d in letters:
        x = affine(x, g, c, d)
    return x


ONEK = KF.one
HK = KF(h)
HALF = KF.one / 2


def L(g, d=None):
    return (g, ONEK, KF.zero if d is None else d)


def INV(g):
    return (g, ONEK, -HK)


def power(g, k):
    return [L(g)] * k if k >= 0 else [INV(g)] * (-k)


# ------------------------------------------------------------------ numerics
Q0 = C.q_at(DPS)
ME = mp.mpf(C.M_E_MEV_STR)
HBAR = 1 - 1 / Q0
E0 = ME / (Q0 * (Q0 - 1))
E0_TOWER = E0 / (1 - HBAR ** 2)
QCOD = mp.mpf(C.Q_NEUTRON_MEV_STR)
VOL41 = 2 * mp.clsin(2, mp.pi / 3)


def kappa_rows(x):
    """Q = kappa * x for the corpus kappas (both signs) + the kappa CODATA would need."""
    return {
        "Q_over_kappa": fmt(x),
        "Q_MeV_kappa_+E0": fmt(E0 * x),
        "Q_MeV_kappa_-E0": fmt(-E0 * x),
        "Q_MeV_kappa_+E0_tower": fmt(E0_TOWER * x),
        "Q_MeV_kappa_-E0_tower": fmt(-E0_TOWER * x),
        "kappa_needed_MeV (comparison only)": fmt(QCOD / x) if x != 0 else "undefined (x = 0)",
        "kappa_needed_over_m_e": fmt(QCOD / x / ME) if x != 0 else "undefined",
        "kappa_needed_over_E0": fmt(QCOD / x / E0) if x != 0 else "undefined",
    }


def main():
    out: dict = {"constants": {"q0": fmt(Q0), "E0 = m_e/(q0(q0-1))": fmt(E0),
                               "E0_tower = E0/(1-hbar_q^2)": fmt(E0_TOWER),
                               "Q_beta_CODATA_MeV (comparison only)": fmt(QCOD), "ln q0": fmt(mp.log(Q0))}}

    # ---------------------------------------------------------- validation
    BETA = H.one(3).rmul_word([0, -2] * 3)
    tB = tr(BETA)
    hh = q - 1 / q
    lean_closed = (4 + hh ** 2 - 3 * hh ** 4 - hh ** 6) / (hh ** 2 + 4)
    check("tr(beta_Bor) = Lean closed form (4+h^2-3h^4-h^6)/(h^2+4)", tB == lean_closed,
          "BorromeanMarkovTrace.lean")
    E = H.one(2).rmul_word([0, 0, 0])
    tE = tr(E)
    check("tr(sigma0^3) = (q^6+q^2-1)/(q(q^2+1))  (P2 table)", tE == (q ** 6 + q ** 2 - 1) / (q * (q ** 2 + 1)))

    # ---------------------------------------------------------- strand factor is not additive
    def qfac(n, qv):
        f = mp.mpf(1)
        for k in range(1, n + 1):
            f *= (qv ** k - qv ** (-k)) / (qv - 1 / qv)
        return f / qv ** n
    sf = {n: qfac(n, Q0) for n in (1, 2, 3, 6)}
    out["strand_factor_[N]!/q^N"] = {
        **{str(n): fmt(v) for n, v in sf.items()},
        "log([6]!/q^6) - log([3]!/q^3) - log([2]!/q^2) - log([1]!/q)":
            fmt(mp.log(sf[6]) - mp.log(sf[3]) - mp.log(sf[2]) - mp.log(sf[1])),
    }
    check("strand factor breaks additivity on 3+2+1 strands",
          abs(mp.log(sf[6]) - mp.log(sf[3]) - mp.log(sf[2]) - mp.log(sf[1])) > mp.mpf(1),
          "so route L uses bare log|tr| (stated in the pre-registration)")

    # ---------------------------------------------------------- P3: index character
    lq = mp.log(Q0)
    out["P3_index_character"] = {
        "log chi(p)/chi(n) = 2 ln q (exact)": fmt(2 * lq),
        "log chi(e-) = 3 ln q (trefoil writhe 3)": fmt(3 * lq),
        "q->1": "both -> 0",
        "decay balance Q/kappa = log chi(n) - log chi(p) - log chi(e) = -5 ln q": fmt(-5 * lq),
        "rows": kappa_rows(-5 * lq),
        "sign": "Lean no_kappa_for_index_character: no kappa makes p lighter than n and E(e-) > 0",
    }

    # ---------------------------------------------------------- P1 words (H_6)
    log("P1: H_6 words ...")
    WORDS = {
        "W0_split": ([], []), "W1_one_bridge": ([2], []), "W1sq_clasp": ([2, 2], []),
        "W2_two_same": ([2], [2]), "W2b_two_opposite": ([2], [-3]),
        "W3_loop_around_2": ([2, 1, 1, 2], []), "W4_loop_around_3": ([2, 1, 0, 0, 1, 2], []),
        "W4b_two_pair_strands_loop": ([3, 2, 2, 3], []),
        "W6_passage_and_return": ([2, 1, 0], [0, 1, 2]), "W7_passage_after_pair": ([], [0, 1, 2]),
    }
    PAIRS = {"Gamma=1 (bare photons)": H.one(3), "Gamma=beta_Bor (V^3 = photon product)": BETA}
    p1: dict = {}
    for gname, G in PAIRS.items():
        tG = tr(G)
        bE = embed(BETA, 6, 0)
        gE = embed(G, 6, 3)
        rows = {}
        for nm, (pre, post) in WORDS.items():
            W = (bE.rmul_word(pre) * gE).rmul_word(post)
            tW = tr(W)
            tbridge = tr(H.one(6).rmul_word(pre + post))
            R = tW / (tB * tG * tbridge)
            Rq = ev(R, Q0)
            Cl = mp.log(abs(Rq))
            rows[nm] = {"R_exact": str(sp.factor(to_expr(R))), "R_at_q0": fmt(Rq),
                        "C_log = log|R|": fmt(Cl), "R_at_q1": str(at_one(R)),
                        "kappa*C_log_MeV at +E0": fmt(E0 * Cl),
                        "kappa*C_log_MeV at +E0_tower": fmt(E0_TOWER * Cl)}
            log(f"  {gname[:12]} {nm}: R(q0) = {mp.nstr(Rq, 15)}  C_log = {mp.nstr(Cl, 12)}")
        p1[gname] = rows
        for nm in ("W0_split", "W1_one_bridge", "W1sq_clasp", "W2_two_same", "W2b_two_opposite"):
            check(f"P1 {gname}: {nm} has R = 1 exactly (log cross term 0)", rows[nm]["R_exact"] == "1")
    out["P1"] = p1

    # ---------------------------------------------------------- P2 words
    log("P2: nucleons, lepton, family D ...")
    B3 = [L(0), INV(1)] * 3

    def nuc11(kind):
        w = list(B3)
        if kind == "p":
            w += [L(0), L(0, -HK * HALF), L(1, -HK * HALF)]
        else:
            w += [L(0, -HK * HALF), L(0, -HK * HALF), L(1, -HK)]
        w += [L(0), L(0)]
        return w

    tP = tr(word_elem(3, nuc11("p")))
    tN = tr(word_elem(3, nuc11("n")))
    p_, n_, e_ = ev(tP, Q0), ev(tN, Q0), ev(tE, Q0)
    out["P2_traces"] = {
        "tr_p_nuc11": {"exact": str(sp.factor(to_expr(tP))), "q0": fmt(p_), "q1": str(at_one(tP))},
        "tr_n_nuc11": {"exact": str(sp.factor(to_expr(tN))), "q0": fmt(n_), "q1": str(at_one(tN))},
        "tr_e_sigma0^3": {"exact": str(sp.factor(to_expr(tE))), "q0": fmt(e_), "q1": str(at_one(tE))},
        "tr_nubar_identity": "1 (log-energy 0 for every kappa: Lean logEnergy_one)",
    }
    check("P2 hypotheses of markov_log_signs hold at q0: 0<te<1, tn>0, tp>0, tn < tp*te",
          0 < e_ < 1 and n_ > 0 and p_ > 0 and n_ < p_ * e_,
          f"tn = {mp.nstr(n_, 12)}, tp*te = {mp.nstr(p_ * e_, 12)}")
    xsplit = mp.log(n_) - mp.log(p_) - mp.log(e_)
    # exact q->1 of the split balance
    x1 = sp.log(at_one(tN)) - sp.log(at_one(tP)) - sp.log(at_one(tE))
    out["P2_split_decay"] = {
        "Q/kappa = log tr n - log tr p - log tr e - log tr nubar": fmt(xsplit),
        "exact log argument tr n / (tr p tr e)": str(sp.factor(to_expr(tN / (tP * tE)))),
        "q->1 value of Q/kappa": str(sp.simplify(x1)),
        "E(e-)/kappa = log tr e": fmt(mp.log(e_)),
        "rows": kappa_rows(xsplit),
        "nucleon-only (E(n)-E(p))/kappa = log tr n - log tr p": fmt(mp.log(n_) - mp.log(p_)),
        "nucleon-only at kappa = -E0 (comparison: CODATA m_n - m_p)": fmt(-E0 * (mp.log(n_) - mp.log(p_))),
        "CODATA m_n - m_p MeV (comparison only)": fmt(mp.mpf(C.M_N_MEV_STR) - mp.mpf(C.M_P_MEV_STR)),
    }
    log(f"  split Q/kappa = {mp.nstr(xsplit, 15)}; log tr e = {mp.nstr(mp.log(e_), 12)}")

    def full_twist(gens, t):
        m = len(gens) + 1
        if t >= 0:
            return [L(g) for g in gens] * (m * t)
        return [INV(g) for g in reversed(gens)] * (m * (-t))

    TRE6 = [L(3)] * 3
    pE = embed(word_elem(3, nuc11("p")), 6, 0)
    famD = {}
    for span in ((1, 2), (0, 1, 2)):
        for t in (1, -1):
            for k in (-1, 0, 1):
                W = word_elem(6, full_twist(span, t) + TRE6 + power(4, 2 * k), start=pE)
                tW = tr(W)
                R = tW / (tP * tE)
                w_ = ev(tW, Q0)
                Rq = ev(R, Q0)
                nm = f"span{''.join(map(str, span))}_t{t:+d}_k{k:+d}"
                xent = mp.log(n_) - mp.log(abs(w_))
                famD[nm] = {"tr_W_q0": fmt(w_), "R = trW/(tr p tr e) at q0": fmt(Rq),
                            "C_log = log|R|": fmt(mp.log(abs(Rq))),
                            "R_at_q1": str(at_one(R)),
                            "q^6-1 divides R-1": bool(sp.rem(sp.numer(sp.together(to_expr(R) - 1)),
                                                             QS ** 6 - 1, QS) == 0),
                            "entangled decay Q/kappa = log tr n - log|tr W|": fmt(xent),
                            "rows": kappa_rows(xent)}
                log(f"  {nm}: C_log = {mp.nstr(mp.log(abs(Rq)), 12)}, Q/kappa = {mp.nstr(xent, 12)}")
    out["P2_family_D"] = famD

    # ---------------------------------------------------------- volume comparison
    F8 = H.one(3).rmul_word([0, -2, 0, -2])          # figure-eight (s1 s2^-1)^2
    t8 = ev(tr(F8), Q0)
    out["volume_conjecture_check"] = {
        "log|tr(4_1)| at q0": fmt(mp.log(abs(t8))),
        "log|tr(3_1)| at q0": fmt(mp.log(e_)),
        "Vol(4_1)": fmt(VOL41), "Vol(3_1)": "0",
        "reading": ("Vol(3_1) = Vol(unknot) = 0 but log|tr(3_1)| != 0 = log|tr(unknot)|, so no kappa "
                    "makes kappa*log|tr_M(q0)| proportional to Vol across these knots. The volume "
                    "conjecture concerns coloured Jones at e^{2 pi i/N}, N -> infinity, not the "
                    "fundamental Markov trace at real q0."),
    }
    check("log|tr(trefoil)| != 0 at q0 while Vol(trefoil) = 0", abs(mp.log(e_)) > mp.mpf("1e-3"))

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("beta-additive-logtrace", engine="python", start_time=T0, output_dir=_HERE)
    wb.set_description("qou-99qc route L: additive log-trace energy kappa*log|tr| on the P1 (H_6 "
                       "nucleon x photon pair), P2 (nuc11 + trefoil + nubar, family D) and P3 (index "
                       "character) words. Exact in Q(q), read out at the proton q0. kappa is not "
                       "derived: corpus alpha = E0 (B_sym) reported with both signs. Not wired.")
    wb.add_parameter("q0", fmt(Q0))
    wb.add_parameter("dps", DPS)
    wb.add_parameter("trace", "Ocneanu, convention D, z = q^3/(q^2+1)")
    wb.add_data("results", out)
    for a_ in ASSERTS:
        wb.add_assertion(a_["name"], computed=str(int(a_["ok"])), expected="1", tolerance="0", source=a_["note"])
    path = wb.save({"q0Anchor": "proton"})
    fails = [a_ for a_ in ASSERTS if not a_["ok"]]
    log(f"witness -> {path.relative_to(_ROOT)}; {len(ASSERTS) - len(fails)}/{len(ASSERTS)} pass")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
