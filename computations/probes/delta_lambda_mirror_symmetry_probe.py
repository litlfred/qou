#!/usr/bin/env python3
# polynomial_q_not_applicable: exact rational arithmetic at the rational q0, then mpmath at 60 dps.
"""Is there a DERIVED reason Phi = sum_lam y_lam chi^lam Delta_lam sees mirror-symmetric words (pn = np)?

Owner pick (2026-10-11, "2"). EXPLORE / DERIVE ONLY: no producer, dashboard or content block is
touched; nothing is selected by agreement with nature (AME is not used anywhere in this file).

Setting (predecessor: delta_lambda_binding_reading_probe.py, commit 0217fa155e3). H_6, convention D,
proton pin. A two-nucleon word is X_xy = x(0) (x) y(3) (the 11-letter nucleon element on generators
(0,1) and (3,4)); the interface letter is s = sigma_2. Phi is a trace, so it is invariant under
  F   sigma_i -> sigma_{4-i}         (conjugation by the H_6 half twist; F(s) = s)
  rho word reversal                   (anti-automorphism; every chi^lam is rho-invariant)
and F maps x(0) (x) y(3) to mu(y)(0) (x) mu(x)(3), mu = in-block generator swap.

Symmetry-transport criterion (Lean: QOU/Mass/DeltaLambdaMirrorTransport.lean). The only Phi-symmetries
that fix s and EXCHANGE the blocks are F and F.rho (the sign automorphism # and the bar involution
fix the block order; # also moves the support onto shapes with three or more rows, where y = 0
under convention D). Hence Phi(X_pn s) = Phi(X_np s) is FORCED by symmetry exactly when each
nucleon N satisfies, up to conjugation by an element commuting with s,
    (M)  mu(N) = N            or         (P)  rho(mu(N)) = N .
Conjugation by Delta_3 realises mu on every word, so "N is conjugate to its mirror" is true of
EVERY element of H_3 and decides nothing; (M)/(P) are the non-vacuous forms.

Measured here:
  H3  For N in {proton, neutron, gamma-gamma core beta_Bor = (sigma_a sigma_b^-1)^3}: test (M) and (P)
      in the 2-dim irrep (2,1) with sigma_a diagonal. The centraliser-of-s test is: some invertible
      DIAGONAL D with rho(mu N) D = D rho(N) (necessary: equal diagonals and equal off-diagonal
      products).
  H6  Three placements of the right-hand nucleon: T (translation, the corpus) x (x) y; R x (x) mu(y);
      L mu(x) (x) y. R and L are exchange-covariant under F, so pn = np by construction; L != R
      unless (M) holds — the choice "which end of the nucleon faces the interface" remains.
  B   For each placement: B = -m_e Phi(atom) (corpus direct reading) and the difference reading, on
      the isospin projector channels P_T on the interface, for pp, nn, pn, np, T = 1, 0.
"""
from __future__ import annotations

import json
import sys
import time
from math import factorial
from multiprocessing import Pool
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("computations", "computations/hecke", "computations/markov",
           "computations/substrate", "tools/pyhecke/python", "tools/qou-substrate/python",
           "computations/probes"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from hoefsmit_symbolic import Q  # noqa: E402
from hecke_character_symbolic import hoefsmit_matrices_symbolic, q_character_on_braid_word  # noqa: E402
from canonical_braid_crossings import d_for_ctype  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from markov_weights_symbolic import solve_y_lambda  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from gamma_gamma_isospin_channel_probe import nucleon  # noqa: E402

DPS = 60
set_compute_dps(DPS)
QV = sp.Rational(Q_50_DIGIT_STR)
NGEN = 5
S2 = [(2, "sigma")]
PAIRS = ("pp", "pn", "np", "nn")


def to_mp(x) -> mp.mpf:
    num, den = sp.fraction(sp.Rational(x))
    return mp.mpf(int(num)) / mp.mpf(int(den))


def hook_dim(lam) -> int:
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    prod = 1
    for i, r in enumerate(lam):
        for j in range(r):
            prod *= (r - j - 1) + (conj[j] - i - 1) + 1
    return factorial(n) // prod


def delta(lam) -> int:
    return (-1) ** sum(i * r for i, r in enumerate(lam)) * hook_dim(lam)


def shift(word, k):
    return [(g + k, t) for (g, t) in word]


def mu(word, g0):
    """In-block generator swap on (g0, g0+1)."""
    return [((g0 + 1 if g == g0 else g0), t) for (g, t) in word]


def rev(word):
    return list(reversed(word))


def core(g0):
    return [(g0, "sigma"), (g0 + 1, "sigma_inv")] * 3


def element3(kind):
    return core(0) if kind == "core" else nucleon(kind, 0)


# ---------------------------------------------------------------- H_3 matrix tests
def h3_matrix(word, shape):
    mats, dim, _ = hoefsmit_matrices_symbolic(list(shape), QV)
    h = QV - 1 / QV
    M = sp.eye(dim)
    for g, t in word:
        d = d_for_ctype(t, h, delta=flavor_split_leading(QV))
        M = (M * (mats[g] + d * sp.eye(dim))).applyfunc(sp.expand)
    return M


def diag_conj_test(A, B):
    """Is there an invertible diagonal D with A D = D B (2x2)? Returns (bool, data)."""
    A = A.applyfunc(sp.radsimp)
    B = B.applyfunc(sp.radsimp)
    diag_eq = bool(sp.simplify(A[0, 0] - B[0, 0]) == 0 and sp.simplify(A[1, 1] - B[1, 1]) == 0)
    pa, pb = sp.simplify(A[0, 1] * A[1, 0]), sp.simplify(B[0, 1] * B[1, 0])
    prod_eq = bool(sp.simplify(pa - pb) == 0)
    zero_pattern = (A[0, 1] == 0) == (B[0, 1] == 0) and (A[1, 0] == 0) == (B[1, 0] == 0)
    data = {"A_diag": [fmt(to_mp_alg(A[0, 0])), fmt(to_mp_alg(A[1, 1]))],
            "B_diag": [fmt(to_mp_alg(B[0, 0])), fmt(to_mp_alg(B[1, 1]))],
            "A_offdiag_product": fmt(to_mp_alg(pa)), "B_offdiag_product": fmt(to_mp_alg(pb))}
    return bool(diag_eq and prod_eq and zero_pattern), data


def to_mp_alg(x) -> mp.mpf:
    """Exact algebraic sympy number -> mpf at the working precision (no float path)."""
    return mp.mpf(sp.N(x, DPS + 10).__str__()) if not x.is_Rational else to_mp(x)


# ---------------------------------------------------------------- H_6 words
def two_nucleon(x, y, placement):
    X, Y = nucleon(x, 0), nucleon(y, 3)
    if placement == "R":
        Y = mu(Y, 3)
    elif placement == "L":
        X = mu(X, 0)
    return X + Y


def _job(args):
    tag, word, lam = args
    return tag, lam, sp.Rational(q_character_on_braid_word(lam, tuple(word), QV))


def main() -> int:
    t0 = time.time()
    q = Q_MP
    from qou_substrate.constants import M_E_MEV  # noqa: PLC0415
    me = mp.mpf(str(M_E_MEV))
    s = 1 / (q + 1 / q)
    tol = mp.mpf(10) ** (-50)
    print(f"Delta_lambda mirror-symmetry probe (proton pin, convention D, {DPS} dps)")
    results: dict = {}
    checks: dict = {}

    # ---------- H_3: (M) and (P) for each nucleon element ----------
    sig_a = h3_matrix([(0, "sigma")], (2, 1))
    checks["H3_sigma_a_diagonal_in_basis"] = bool(sig_a[0, 1] == 0 and sig_a[1, 0] == 0)
    # positive/negative CONTROLS, so the tests cannot certify themselves:
    #   Delta = s_a s_b s_a is exactly mu-fixed;  s_a s_b is exactly rho.mu-fixed;
    #   s_b s_a is mu-fixed only up to conjugation by s_a (diagonal), s_a alone is neither.
    ctl = {"Delta": [(0, "sigma"), (1, "sigma"), (0, "sigma")], "ab": [(0, "sigma"), (1, "sigma")],
           "ba": [(1, "sigma"), (0, "sigma")], "a": [(0, "sigma")]}
    cm = {k: (h3_matrix(w, (2, 1)), h3_matrix(mu(w, 0), (2, 1)), h3_matrix(rev(mu(w, 0)), (2, 1)))
          for k, w in ctl.items()}
    checks["control_Delta_exact_M"] = bool((cm["Delta"][1] - cm["Delta"][0]).applyfunc(sp.simplify) == sp.zeros(2, 2))
    checks["control_ab_exact_P"] = bool((cm["ab"][2] - cm["ab"][0]).applyfunc(sp.simplify) == sp.zeros(2, 2))
    checks["control_ba_M_not_exact"] = bool((cm["ba"][1] - cm["ba"][0]).applyfunc(sp.simplify) != sp.zeros(2, 2))
    checks["control_ba_M_up_to_centraliser"] = diag_conj_test(cm["ba"][1], cm["ba"][0])[0]
    checks["control_a_M_fails"] = not diag_conj_test(cm["a"][1], cm["a"][0])[0]
    h3 = {}
    for kind in ("core", "p", "n"):
        N = element3(kind)
        mats = {k: h3_matrix(w, (2, 1)) for k, w in
                (("N", N), ("muN", mu(N, 0)), ("rhoN", rev(N)), ("rhomuN", rev(mu(N, 0))))}
        exact_M = bool((mats["muN"] - mats["N"]).applyfunc(sp.simplify) == sp.zeros(2, 2))
        exact_P = bool((mats["rhomuN"] - mats["N"]).applyfunc(sp.simplify) == sp.zeros(2, 2))
        dM, dataM = diag_conj_test(mats["muN"], mats["N"])
        dP, dataP = diag_conj_test(mats["rhomuN"], mats["N"])
        # 1-dim irreps: every element agrees with its mirror there (both letters act by the same scalar)
        one_dim = {}
        for sh in ((3,), (1, 1, 1)):
            a = h3_matrix(N, sh)[0, 0]
            b = h3_matrix(mu(N, 0), sh)[0, 0]
            one_dim[str(sh)] = bool(sp.simplify(a - b) == 0)
        h3[kind] = {"exact_mu_fixed_(M)": exact_M, "exact_rhomu_fixed_(P)": exact_P,
                    "diag_conj_mu_(M_up_to_centraliser)": dM, "diag_conj_rhomu_(P_up_to_centraliser)": dP,
                    "one_dim_irreps_agree": one_dim, "data_M": dataM, "data_P": dataP}
        print(f"  H3 {kind:<4}: (M) exact={exact_M} up-to-centraliser={dM};  "
              f"(P) exact={exact_P} up-to-centraliser={dP}", flush=True)
    results["H3_mirror_tests"] = h3

    # ---------- H_6 placements ----------
    Y6s = solve_y_lambda(6)
    support = sorted((lam for lam in Y6s if sp.cancel(Y6s[lam]) != 0), key=len)
    y6 = {lam: sp.Rational(sp.cancel(Y6s[lam]).subs(Q, QV)) for lam in support}
    words = {}
    for pl in ("T", "R", "L"):
        for pair in PAIRS:
            W = two_nucleon(pair[0], pair[1], pl)
            words[(pl, pair, "W")] = W
            words[(pl, pair, "W.s")] = W + S2
    # reversal invariance of Phi (on the bonded corpus words)
    for pair in ("pn", "np"):
        words[("T", pair, "rev(W.s)")] = rev(words[("T", pair, "W.s")])
    jobs = [(tag, w, lam) for tag, w in words.items() for lam in support]
    print(f"  {len(words)} words x {len(support)} blocks = {len(jobs)} characters", flush=True)
    chi: dict = {}
    with Pool(4) as pool:
        for i, (tag, lam, val) in enumerate(pool.imap_unordered(_job, jobs), 1):
            chi.setdefault(tag, {})[lam] = val
            if i % 16 == 0:
                print(f"    {i}/{len(jobs)}  {time.time() - t0:.0f} s", flush=True)
    ph = {tag: to_mp(sum(y6[l] * c[l] * delta(l) for l in support)) for tag, c in chi.items()}
    results["Phi"] = {f"{a}|{b}|{c}": fmt(v) for (a, b, c), v in ph.items()}

    checks["rho_invariance_Phi"] = bool(all(abs(ph[("T", p, "rev(W.s)")] - ph[("T", p, "W.s")]) < tol
                                            for p in ("pn", "np")))
    # The predecessor's values are READ from its witness, not typed, so this check
    # tracks the predecessor if it is ever re-run (witness-value copy ratchet).
    _pred = json.loads((Path(__file__).resolve().parent
                        / "delta-lambda-binding-reading-probe.witness.json").read_text(encoding="utf-8"))
    _pred_phi = _pred["data"]["results"]["Phi"]
    checks["T_reproduces_predecessor_pn"] = bool(abs(ph[("T", "pn", "W.s")] - mp.mpf(
        _pred_phi["pn"]["W.s"])) < tol)
    checks["T_reproduces_predecessor_np"] = bool(abs(ph[("T", "np", "W.s")] - mp.mpf(
        _pred_phi["np"]["W.s"])) < tol)
    checks["T_bond_pn_ne_np"] = bool(abs(ph[("T", "pn", "W.s")] - ph[("T", "np", "W.s")]) > mp.mpf(10) ** -20)
    for pl in ("R", "L"):
        checks[f"{pl}_bond_pn_eq_np_by_F"] = bool(abs(ph[(pl, "pn", "W.s")] - ph[(pl, "np", "W.s")]) < tol)
        checks[f"{pl}_free_pn_eq_np"] = bool(abs(ph[(pl, "pn", "W")] - ph[(pl, "np", "W")]) < tol)
    checks["L_ne_R_bond_pn"] = bool(abs(ph[("L", "pn", "W.s")] - ph[("R", "pn", "W.s")]) > mp.mpf(10) ** -20)

    # ---------- B on the projector channels ----------
    def proj(T):
        return (s / q, s) if T == 1 else (s * q, -s)

    B = {}
    for pl in ("T", "R", "L"):
        for p in PAIRS:
            for T in (1, 0):
                if p in ("pp", "nn") and T == 0:
                    continue
                a, b = proj(T)
                free = ph[(pl, p, "W")]
                atom = a * free + b * ph[(pl, p, "W.s")]
                B[f"{pl}|{p}|T{T}"] = {"R_dir_corpus": fmt(-me * atom), "R_diff": fmt(me * (free - atom))}
    results["B_MeV"] = B
    results["charge_independence_pp_minus_nn_R_dir_corpus"] = {
        pl: fmt(mp.mpf(B[f"{pl}|pp|T1"]["R_dir_corpus"]) - mp.mpf(B[f"{pl}|nn|T1"]["R_dir_corpus"]))
        for pl in ("T", "R", "L")}

    print("\n  Phi(W), Phi(W.s)")
    for pl in ("T", "R", "L"):
        for p in PAIRS:
            print(f"    {pl} {p}: {mp.nstr(ph[(pl, p, 'W')], 12)}  {mp.nstr(ph[(pl, p, 'W.s')], 12)}")
    print("\n  B [MeV]  (R_dir_corpus = -m_e Phi(atom);  R_diff = m_e (Phi(free) - Phi(atom)))")
    for k, r in B.items():
        print(f"    {k:<10} dir={mp.nstr(mp.mpf(r['R_dir_corpus']), 10):>14}  diff={mp.nstr(mp.mpf(r['R_diff']), 10):>14}")
    print(f"  pp - nn: {results['charge_independence_pp_minus_nn_R_dir_corpus']}")
    print(f"  checks: {checks}")
    print(f"  wall {time.time() - t0:.1f} s")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    w = WitnessBuilder("delta-lambda-mirror-symmetry-probe", engine="python", start_time=t0)
    w.set_description(
        "Owner pick '2': is there a derived reason the Delta_lambda functional Phi sees mirror-symmetric "
        "words so that pn = np? Tests the non-vacuous mirror conditions (M) mu(N)=N and (P) rho mu(N)=N "
        "on the proton, neutron and gamma-gamma core in the H_3 irrep (2,1), and three placements of "
        "the right-hand nucleon in H_6 (translation T = corpus; reflected R, L). Convention D, proton "
        "pin. Nothing is selected by agreement with nature; AME is not used.")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("convention", "D (z = q^3/(q^2+1))")
    w.add_parameter("dps", DPS)
    w.add_parameter("m_e_MeV", fmt(me))
    w.add_data("results", json.loads(json.dumps(results, default=str)))
    w.add_data("checks", {k: bool(v) for k, v in checks.items()})
    for k, v in checks.items():
        w.add_assertion(name=k, computed=str(int(bool(v))), expected="1", tolerance="0",
                        source="exact recomputation at the rational q0")
    out = w.save()
    print(f"  witness -> {out}")
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
