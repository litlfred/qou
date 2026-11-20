#!/usr/bin/env python3
"""qou-99qc P1 + P4: β decay as ONE Gröbner–Shirshov reduction in H_6(q).

Pre-registered: PREREGISTRATION.md (commit c59f09c7fb), before any number.

P1  (Hecke-trace reading). Nucleon β_Bor = (σ₀σ₁⁻¹)³ on strands 0-2, photon pair
    Γ = γ(φ)γ(ψ), γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹, on strands 3-5, joined by bridge letters.
    Reduce to the T_w normal form; cross term C(W) = tr(W) − tr(β)tr(Γ)tr(bridge alone).
P4  (strand-colour reading). Jimbo Ř on V^{⊗6}; sector traces on n⊗ν (nucleon T³ = −½, strand 3 = u)
    and p⊗e⁻ (nucleon T³ = +½, strand 3 = d); K-weighted (sums to the convention-D trace) and plain.

Exact over ℚ(q)[φ, ψ]; numbers at the proton q₀, mpmath 70 dps. CODATA only in the last block.
Run:  python3 -u beta_gs_reduction_probe.py 2>&1 | tee /tmp/beta_gs_reduction_probe.log
"""
from __future__ import annotations

import itertools
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "tools/qou-substrate/python", str(_HERE)):
    sys.path.insert(0, str(_ROOT / _p) if not _p.startswith("/") else _p)

import mpmath as mp  # noqa: E402
from sympy import factor  # noqa: E402

import qou_substrate.constants as C  # noqa: E402
from qou_substrate.precision import fmt  # noqa: E402
from hecke_exact import (H, KF, RING, ONE, ZERO, embed, h, q, zD,  # noqa: E402
                         p0, p1, p2, s0, s1, s2)
from jimbo import apply_H, apply_word  # noqa: E402

DPS = 70
mp.mp.dps = DPS
T0 = time.time()
ASSERTS: list = []


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def check(name, ok, note=""):
    ASSERTS.append({"name": name, "ok": bool(ok), "note": note})
    log(f"{'PASS' if ok else 'FAIL'} {name} {note}")


# ---------------------------------------------------------------- exact objects
def photon(a0, a1, a2):
    return (H.one(3) + H.gen(3, 0).scale(a0) + H.gen(3, 1).scale(a1)
            + H.one(3).rmul_word([0, -2]).scale(a2))


I3, S0, S1, S01, S10, E3 = (0, 1, 2), (1, 0, 2), (0, 2, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0)
BASIS3 = [I3, S0, S1, S01, S10, E3]          # 1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀
BASIS3_NAMES = ["1", "s0", "s1", "s0s1", "s1s0", "s0s1s0(e-_BW)"]
BETA = H.one(3).rmul_word([0, -2] * 3)
GAMMA = photon(p0, p1, p2) * photon(s0, s1, s2)
TR_B = BETA.trace()
TR_G = GAMMA.trace()
PHI = (p0, p1, p2, s0, s1, s2)

# Words on six strands: (pre-bridge letters after β, post letters after Γ'). Negative g = σ_{-g-1}⁻¹.
WORDS = {
    "W0_split": ([], []),
    "W1_one_bridge": ([2], []),
    "W1sq_clasp": ([2, 2], []),
    "W2_two_same": ([2], [2]),
    "W2b_two_opposite": ([2], [-3]),
    "W3_loop_around_2": ([2, 1, 1, 2], []),
    "W4_loop_around_3": ([2, 1, 0, 0, 1, 2], []),
    "W4b_two_pair_strands_loop": ([3, 2, 2, 3], []),
    "W6_passage_and_return": ([2, 1, 0], [0, 1, 2]),
    "W7_passage_after_pair": ([], [0, 1, 2]),
}


def build(pre, post, N=6, shift=3):
    return (embed(BETA, N, 0).rmul_word(pre) * embed(GAMMA, N, shift)).rmul_word(post)


def bridge_trace(pre, post, N=6):
    return H.one(N).rmul_word(pre + post).trace()


# ---------------------------------------------------------------- numerics
Q0 = C.q_at(DPS)
ME = mp.mpf(C.M_E_MEV_STR)
VOL41 = 2 * mp.clsin(2, mp.pi / 3)
HBAR = 1 - 1 / Q0
M_MU = ME * VOL41 / HBAR ** 2


def ev_frac(f, qv=Q0):
    num = sum(mp.mpf(int(c)) * qv ** e[0] for e, c in f.numer.terms())
    den = sum(mp.mpf(int(c)) * qv ** e[0] for e, c in f.denom.terms())
    return num / den


def ev(x, point, qv=Q0):
    """Evaluate a RING element at q = qv and photon weights `point` (6 mpf)."""
    tot = mp.mpf(0)
    for mon, cf in x.terms():
        t = ev_frac(cf, qv)
        for e, v in zip(mon, point):
            t *= v ** e
        tot += t
    return tot


def qint(n, qv=Q0):
    return (qv ** n - qv ** (-n)) / (qv - 1 / qv)


def scale(N, qv=Q0):
    f = mp.mpf(1)
    for k in range(1, N + 1):
        f *= qint(k, qv)
    return M_MU * f / qv ** N


hq = Q0 - 1 / Q0
POINTS = {
    "bare (phi=psi=0, Gamma=1)": [mp.mpf(0)] * 6,
    "Borromean (0,0,qh)(0,0,-h/q): Gamma=beta_Bor, e- channel 0": [0, 0, Q0 * hq, 0, 0, -hq / Q0],
}


def linear_in_gamma(fn):
    """fn(Γ-element) -> RING value, linear in Γ; return its 6 coefficients on BASIS3."""
    out = []
    for w in BASIS3:
        out.append(fn(H(3, {w: ONE})))
    return out


def low_order(f):
    """Lowest power of (q − 1) dividing an exact rational function (0 if none)."""
    k, num = 0, f.numer
    one = mp.mpf(1)
    while k < 40 and ev_frac(KF(num) / KF(f.denom), one) == 0 if False else False:
        k += 1
    # exact: count roots at q = 1 of the numerator
    from sympy import Poly, Symbol
    x = Symbol("q")
    P = Poly(num.as_expr(), x)
    while P.eval(1) == 0:
        P = P.quo(Poly(x - 1, x))
        k += 1
    return k


def fx(f):
    return str(factor(f.as_expr()))


def main():
    out: dict = {"validation": {}, "P1": {}, "P4": {}, "energies": {}}
    log(f"q0 (proton) = {mp.nstr(Q0, 30)}; m_mu = {mp.nstr(M_MU, 20)} MeV")

    # ---------------- validation against the corpus
    hh = h
    trB_closed = (4 + hh ** 2 - 3 * hh ** 4 - hh ** 6) / (hh ** 2 + 4)
    check("tr(beta_Bor) = BorromeanMarkovTrace closed form", TR_B.coeff(1) == trB_closed)
    c = {w: BETA.c.get(w, ZERO).coeff(1) for w in BASIS3}
    check("NF(beta_Bor) = #8634 [1-h^4,-h^3-h^5,h^3,{h^2+h^4,-h^2},0]",
          c[I3] == 1 - hh ** 4 and c[S0] == -hh ** 3 - hh ** 5 and c[S1] == hh ** 3
          and c[S01] == hh ** 2 + hh ** 4 and c[S10] == -hh ** 2 and c[E3] == 0)
    check("e- coordinate of gamma(phi)gamma(psi) = phi01 psi0 + phi1 psi01 (pairNFChiral_eq)",
          GAMMA.c.get(E3) == p2 * s0 + p1 * s2)
    check("tr(e-_BW = s0 s1 s0) = z(hz+1): closes to a 2-component link, permutation (0 2)",
          H.one(3).rmul_word([0, 1, 0]).trace().coeff(1) == zD * (h * zD + 1))
    # quantum-trace calibration: Tr(q^{2T3} rho(X))/[2]^N = Ocneanu at z_D
    ok = True
    for word in ([0], [0, 1, 0], [0, -2] * 3, [0, 0, 0]):
        X = H.one(3).rmul_word(word)
        tot = ZERO
        for b in itertools.product((0, 1), repeat=3):
            img = apply_H({b: ONE}, X)
            tot += img.get(b, ZERO) * RING(q ** sum(1 if x == 0 else -1 for x in b))
        ok &= tot.coeff(1) / (q + 1 / q) ** 3 == X.trace().coeff(1)
    check("K-weighted Jimbo trace / [2]^N = Ocneanu trace at z_D (fixes the K normalisation)", ok)

    # ---------------- P1
    n_hom = 0
    for name, (pre, post) in WORDS.items():
        t = time.time()
        W = build(pre, post)
        # homomorphism check: rho(raw word product) == rho(NF) on two basis vectors
        for b in ((1, 0, 1, 0, 1, 1), (0, 1, 1, 1, 0, 0)):
            raw = apply_H(apply_word({b: ONE}, post), embed(GAMMA, 6, 3))
            raw = apply_word(raw, pre)
            raw = apply_H(raw, embed(BETA, 6, 0))
            n_hom += int(raw == apply_H({b: ONE}, W))
        trW = W.trace()
        Cw = trW - TR_B * TR_G * bridge_trace(pre, post)
        outside = sum(1 for w in W.c if sorted(w[:3]) != [0, 1, 2])
        # e-_BW channel block: terms with w in S3 x S3 and pair part = (2,1,0) on 3-5
        Xe = H(3, {w[:3]: v for w, v in W.c.items()
                   if sorted(w[:3]) == [0, 1, 2] and tuple(x - 3 for x in w[3:]) == E3})
        Xe_fact = BETA.scale(GAMMA.c.get(E3, ZERO))
        rec = {"normal_form_terms": len(W.c), "terms_outside_S3xS3": outside,
               "cross_term_zero": Cw == 0,
               "eminus_channel_block_equals_beta_times_eminus_coord": (Xe - Xe_fact).c == {}}
        if Cw != 0:
            kap = linear_in_gamma(lambda G: (build_with(G, pre, post).trace()
                                             - TR_B * G.trace() * bridge_trace(pre, post)))
            rec["cross_term_as_functional_on_pair_NF"] = {
                n_: fx(k.coeff(1)) for n_, k in zip(BASIS3_NAMES, kap)}
            rec["lowest_order_in_(q-1)"] = min(low_order(k.coeff(1)) for k in kap if k != 0)
            rec["cross_term_at_q0"] = {k: fmt(ev(Cw, v)) for k, v in POINTS.items()}
            C1 = (build_with(H.one(3), pre, post).trace()
                  - TR_B * bridge_trace(pre, post))
            rec["cross_term_equals_kappa_times_tr_pair"] = (Cw - C1 * TR_G) == 0
            rec["kappa_exact (cross term at Gamma=1)"] = fx(C1.coeff(1)) if C1 != 0 else "0"
        out["P1"][name] = rec
        log(f"P1 {name}: terms={len(W.c)} outside={outside} C==0:{Cw == 0} "
            f"e-block factorised:{rec['eminus_channel_block_equals_beta_times_eminus_coord']} "
            f"({time.time() - t:.1f}s)")
    check("GS normal form is the element: rho(word) == rho(NF) on 2 vectors x 10 words", n_hom == 20)
    # shared-strand (five-strand connected sum)
    W5 = embed(BETA, 5, 0) * embed(GAMMA, 5, 2)
    C5 = W5.trace() - TR_B * TR_G
    out["P1"]["W5_shared_strand_H5"] = {"normal_form_terms": len(W5.c), "cross_term_zero": C5 == 0}
    for nm in ("W0_split", "W1_one_bridge", "W1sq_clasp", "W2_two_same", "W2b_two_opposite"):
        check(f"PR1/PR2: cross term of {nm} vanishes (connected sum)", out["P1"][nm]["cross_term_zero"])
    check("PR1: cross term of W5 (shared strand) vanishes", C5 == 0)
    for nm in ("W3_loop_around_2", "W4_loop_around_3", "W4b_two_pair_strands_loop",
               "W6_passage_and_return", "W7_passage_after_pair"):
        check(f"cross term of {nm} is non-zero", not out["P1"][nm]["cross_term_zero"])

    # ---------------- energies (P1, principal and alternates)
    E = {}
    sig3 = H.one(2).rmul_word([0, 0, 0]).trace()
    eBW = H.one(3).rmul_word([0, 1, 0]).trace()
    E["E3(beta_Bor) = m_mu F_Bor"] = scale(3) * abs(ev(TR_B, [0] * 6))
    E["E3(e-_BW)"] = scale(3) * abs(ev(eBW, [0] * 6))
    E["E2(e-_K = s^3, trefoil)"] = scale(2) * abs(ev(sig3, [0] * 6))
    E["E1(nubar)"] = scale(1)
    E["m_e (CAL-1)"] = ME
    E["S6 = m_mu [6]!/q^6"] = scale(6)
    out["energies"]["self"] = {k: fmt(v) for k, v in E.items()}
    for nm in ("W3_loop_around_2", "W4_loop_around_3", "W6_passage_and_return", "W7_passage_after_pair"):
        check(f"{nm}: cross term = kappa(q) * tr(pair) (pair joins at ONE strand, so it still factorises)",
              out["P1"][nm]["cross_term_equals_kappa_times_tr_pair"])
    check("W4b (two pair strands wrap the nucleon strand): cross term NOT proportional to tr(pair)",
          not out["P1"]["W4b_two_pair_strands_loop"]["cross_term_equals_kappa_times_tr_pair"])
    check("PR4: E(e-) >> m_e for both electron words",
          E["E3(e-_BW)"] > 10 * ME and E["E2(e-_K = s^3, trefoil)"] > 10 * ME)
    trFinK = TR_B * sig3            # beta (x) s3^3 (x) 1 on six strands
    trFinBW = TR_B * eBW
    qrows = {}
    for name, (pre, post) in WORDS.items():
        W = build(pre, post)
        trW = W.trace()
        Cw = trW - TR_B * TR_G * bridge_trace(pre, post)
        for pk, pv in POINTS.items():
            ti = ev(trW, pv)
            qrows[f"{name} | {pk}"] = {
                "tr_initial": fmt(ti),
                "cross_term": fmt(ev(Cw, pv)),
                "S6_times_cross_term_MeV": fmt(scale(6) * ev(Cw, pv)),
                "Q_principal_MeV (e-_K)": fmt(scale(6) * (abs(ti) - abs(ev(trFinK, pv)))),
                "Q_A1_MeV (e-_BW)": fmt(scale(6) * (abs(ti) - abs(ev(trFinBW, pv)))),
            }
    out["energies"]["Q_rows"] = qrows
    for pk, pv in POINTS.items():
        out["energies"][f"Q_A2_additive | {pk}"] = fmt(
            scale(3) * abs(ev(TR_G, pv)) - E["E2(e-_K = s^3, trefoil)"] - E["E1(nubar)"])

    # ---------------- P4 strand colour
    def sector(b, nucT, lep):
        return sum(1 if x == 0 else -1 for x in b[:3]) == nucT and b[3] == lep

    def sectr(X, nucT, lep, K):
        tot = ZERO
        for b in itertools.product((0, 1), repeat=6):
            if not sector(b, nucT, lep):
                continue
            img = apply_H({b: ONE}, X)
            wt = sum(1 if x == 0 else -1 for x in b)
            tot += img.get(b, ZERO) * (RING(q ** wt) if K else ONE)
        return tot

    for name, (pre, post) in WORDS.items():
        t = time.time()
        W = build(pre, post)
        rec = {}
        for K in (True, False):
            tag = "K" if K else "plain"
            Dl = (sectr(W, -1, 0, K) - sectr(W, +1, 1, K)) * RING(KF(1) / 12)
            rec[f"{tag}_dimnorm_sector_difference_zero"] = Dl == 0
            if Dl != 0:
                rec[f"{tag}_Q4_MeV"] = {pk: fmt(scale(6) * ev(Dl, pv)) for pk, pv in POINTS.items()}
                rec[f"{tag}_Delta_hat_at_q0"] = {pk: fmt(ev(Dl, pv)) for pk, pv in POINTS.items()}
                if name in ("W1_one_bridge", "W7_passage_after_pair") and K:
                    rec[f"{tag}_Delta_hat_bare_exact"] = fx(Dl.coeff(1)) if Dl.coeff(1) != 0 else "0"
        out["P4"][name] = rec
        log(f"P4 {name}: K-zero={rec['K_dimnorm_sector_difference_zero']} "
            f"plain-zero={rec['plain_dimnorm_sector_difference_zero']} ({time.time() - t:.1f}s)")
    check("P4 null: factorised W0 has zero K-weighted sector difference",
          out["P4"]["W0_split"]["K_dimnorm_sector_difference_zero"])
    check("PR5: an entangled word separates n(x)nu from p(x)e- (K-weighted)",
          not out["P4"]["W1_one_bridge"]["K_dimnorm_sector_difference_zero"])

    # amplitude <e- (x) p | rho(passage) | n (x) nu> for W7 (lepton ends on strand 0)
    amp = {}
    for nb in ((0, 1, 1), (1, 0, 1), (1, 1, 0)):
        img = apply_H({nb + (0, 0, 0): ONE}, build([], [0, 1, 2]))
        for pb in ((0, 0, 1), (0, 1, 0), (1, 0, 0)):
            v = img.get((1,) + pb + (0, 0), ZERO)
            amp[f"{''.join('ud'[x] for x in nb)}nu -> e-{''.join('ud'[x] for x in pb)}"] = \
                {pk: fmt(ev(v, pv)) for pk, pv in POINTS.items()}
    out["P4"]["W7_amplitude_spectators_uu"] = amp

    # ---------------- comparison only
    Qcod = mp.mpf(C.M_N_MEV_STR) - mp.mpf(C.M_P_MEV_STR) - ME
    out["comparison"] = {"Q_beta_codata_MeV": fmt(Qcod)}
    log(f"CODATA Q_beta = {mp.nstr(Qcod, 12)} MeV (comparison only)")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("beta-gs-reduction-n-gammagamma", engine="python", start_time=T0, output_dir=_HERE)
    wb.set_description("qou-99qc P1/P4: beta decay as one GS reduction in H_6(q): nucleon beta_Bor (x) "
                       "photon pair with bridge letters; Markov cross term; strand-colour sector traces. "
                       "Pre-registered at c59f09c7fb. Not wired to any scorecard.")
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


def build_with(G, pre, post, N=6, shift=3):
    return (embed(BETA, N, 0).rmul_word(pre) * embed(G, N, shift)).rmul_word(post)


if __name__ == "__main__":
    sys.exit(main())
