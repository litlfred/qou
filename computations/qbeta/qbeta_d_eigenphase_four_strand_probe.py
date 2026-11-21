#!/usr/bin/env python3
"""qbeta_d_eigenphase_four_strand_probe — the eigenphase test on the four-strand process words.

Issue #8833, PR #8836 (owner 2026-11-21: "keep trying different routes"). The three-strand
base V^3 is elliptic on every block (PhotonVertexEigenphase.lean), so no cosh lever exists
there. This probe asks the same question one strand up, on the process words that
`docs/audits/2026-11-21-beta-pair-creation-word-proposal.md` lists as admitted by the
gamma-gamma grammar, the charged-current block and reading 3 (G ^ CC ^ R3):

    W = X * beta_Bor,   beta_Bor = (s0 s1^-1)^3,   X in {V1^3, V0V1V0V1, V1V0V1V0}

with V_i = s_i s_{i+1}^-1 on four strands. The candidate list is THAT document's, not chosen
here, and no word is selected or ruled here. It is a diagnostic: for each word and each
H_4 block with y_lambda > 0 under convention D ((4), (3,1), (2,2)), is the spectrum on the
unit circle (real phase, cos <= 1) or real positive (imaginary phase, cosh >= 1)?

Exact sympy over Q(q) on (C^2)^{x4} with the Jimbo braiding (eigenvalues q, -1/q), the same
matrices as the flavour-split probe. Blocks are read off weight spaces:
  #d = 1 (dim 4) = (4) + (3,1);  #d = 2 (dim 6) = (4) + (3,1) + (2,2).
Characteristic polynomials are exact; roots are evaluated at the proton q0 at 60 dps.
CODATA enters one comparison ratio only. Nothing is wired or scored.
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
for _p in (_HERE.parent, _HERE, _HERE.parent.parent / "tools/qou-substrate/python"):
    sys.path.insert(0, str(_p))

import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

import qbeta_e0  # noqa: E402
from codata_2022_source import Q_BETA_MEV_AME  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = 60
mp.mp.dps = DPS
q = sp.Symbol("q", positive=True)
lam = sp.Symbol("lam")
h = q - 1 / q
Q0 = sp.Rational(Q_50_DIGIT_STR)

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {detail}\n")


R2 = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])


def sigma(i: int, n: int = 4) -> sp.Matrix:
    mats, k = [], 0
    while k < n:
        if k == i:
            mats.append(R2)
            k += 2
        else:
            mats.append(sp.eye(2))
            k += 1
    M = sp.eye(1)
    for m in mats:
        M = sp.kronecker_product(M, m)
    return M


def block(W: sp.Matrix, nd: int) -> sp.Matrix:
    idx = [i for i in range(16) if bin(i).count("1") == nd]
    return W.extract(idx, idx)


def roots_at_q0(poly):
    p = sp.Poly(sp.expand(poly), lam)
    coeffs = [mp.mpf(str(sp.N(c.subs(q, Q0), DPS + 10))) for c in p.all_coeffs()]
    return mp.polyroots(coeffs, maxsteps=200, extraprec=200)


def classify(roots):
    """Unit circle first: a root equal to 1 is phase 0, not an imaginary phase."""
    if all(abs(abs(r) - 1) < mp.mpf(10) ** -40 for r in roots):
        return "REAL phase (unit circle)"
    if all(abs(mp.im(r)) < mp.mpf(10) ** -40 for r in roots):
        if all(mp.re(r) > 0 for r in roots):
            return "IMAGINARY phase (real positive spectrum)"
        return "real spectrum with a negative eigenvalue"
    return "mixed"


def main() -> int:
    S0, S1, S2 = sigma(0), sigma(1), sigma(2)
    hecke = all(sp.simplify(S * S - (h * S + sp.eye(16))) == sp.zeros(16, 16)
                for S in (S0, S1, S2))
    braid = sp.simplify(S0 * S1 * S0 - S1 * S0 * S1) == sp.zeros(16, 16) and \
        sp.simplify(S1 * S2 * S1 - S2 * S1 * S2) == sp.zeros(16, 16)
    check("jimbo_rep_is_H4", hecke and braid,
          "sigma^2 = h sigma + 1 for all three generators and both braid relations hold "
          "exactly on (C^2)^{x4}.")

    V0 = sp.simplify(S0 * S1.inv())
    V1 = sp.simplify(S1 * S2.inv())
    beta = V0 ** 3
    words = {"V1^3": V1 ** 3, "V0V1V0V1": V0 * V1 * V0 * V1, "V1V0V1V0": V1 * V0 * V1 * V0}
    rows = []
    imag_words = []
    a_max = mp.mpf(0)
    for nm, X in words.items():
        W = X * beta
        b1, b2 = block(W, 1), block(W, 2)
        cp1 = sp.factor(b1.charpoly(lam).as_expr())
        cp2 = sp.factor(b2.charpoly(lam).as_expr())
        # (4) is the factor (lam - 1) (gamma-gamma words have writhe 0, chi_(4) = q^0 = 1)
        q31, rem31 = sp.div(sp.Poly(cp1, lam), sp.Poly(lam - 1, lam))
        q22, rem22 = sp.div(sp.Poly(cp2, lam), sp.Poly(sp.expand(cp1), lam))
        ok_split = rem31.is_zero and rem22.is_zero
        r31, r22 = roots_at_q0(q31.as_expr()), roots_at_q0(q22.as_expr())
        k31, k22 = classify(r31), classify(r22)
        if k31.startswith("IMAGINARY") or k22.startswith("IMAGINARY"):
            imag_words.append(nm)
            for r in list(r31) + list(r22):
                if abs(mp.im(r)) < mp.mpf(10) ** -40 and mp.re(r) > 0:
                    a_max = max(a_max, abs(mp.log(mp.re(r))))
        rows.append({
            "word": f"{nm} * beta_Bor", "split_exact": ok_split,
            "charpoly_31": str(sp.factor(q31.as_expr())),
            "charpoly_22": str(sp.factor(q22.as_expr())),
            "roots_31": [mp.nstr(r, 30) for r in r31], "type_31": k31,
            "roots_22": [mp.nstr(r, 30) for r in r22], "type_22": k22,
        })
        print(f"  {nm:<10} (3,1): {k31}\n             roots {[mp.nstr(r, 10) for r in r31]}")
        print(f"             (2,2): {k22}\n             roots {[mp.nstr(r, 10) for r in r22]}\n")

    check("block_split_exact",
          all(r["split_exact"] for r in rows),
          "for every word, charpoly on #d=1 is (lam-1) x cubic (3,1), and charpoly on #d=2 "
          "is charpoly(#d=1) x quadratic (2,2), exactly in Q(q).")
    check("minimal_word_V1cubed_is_elliptic",
          rows[0]["type_31"].startswith("REAL") and rows[0]["type_22"].startswith("REAL"),
          "the minimal G^CC^R3 word V1^3 * beta_Bor has unit-circle spectrum on (3,1) and "
          "(2,2): real phase, no cosh lever (as on three strands).")
    check("non_minimal_words_have_an_imaginary_phase_on_31",
          imag_words == ["V0V1V0V1", "V1V0V1V0"],
          f"{imag_words} have REAL POSITIVE spectrum on the (3,1) block: the first imaginary "
          "eigenphase found on any gamma-gamma-admitted word. Their (2,2) block stays on the "
          "unit circle.")

    E0 = mp.mpf(qbeta_e0.canonical())
    QB = mp.mpf(str(Q_BETA_MEV_AME))
    # the scored base (flavour split of V^3), used only to size the lever
    epsV3 = abs(mp.mpf(str(sp.N(((q ** 2 - 1) * (q ** 12 - 3 * q ** 10 + 3 * q ** 8 - 5 * q ** 6
                                               + 3 * q ** 4 - 3 * q ** 2 + 1)
                                 / (q ** 4 * (q ** 2 + 1) ** 3)).subs(q, Q0), DPS + 10))))
    F_req = QB / (epsV3 * E0)
    a_need = mp.acosh(F_req)
    check("imaginary_phase_still_too_small",
          a_max > 0 and a_max < a_need,
          f"largest |a| = |log lambda| on those blocks = {mp.nstr(a_max, 15)} "
          f"(cosh a = {mp.nstr(mp.cosh(a_max), 12)}); the scored cell needs a = "
          f"{mp.nstr(a_need, 12)} (F = {mp.nstr(F_req, 10)}): {mp.nstr(a_need / a_max, 6)}x "
          "short. And these words are not the minimal one, so G^CC^R3 + minimality does not "
          "admit them. Diagnostic only.")

    # ---- all 30 gamma-gamma words X (V0, V1 blocks, length <= 8), W = X * beta_Bor ------
    # Same family as gg_words(8, mirrors=False) in beta_pair_creation_word_probe.py.
    # Numeric at q0 (60 dps); classification tolerance 1e-40. Nothing is selected.
    import itertools

    def numm(M):
        return mp.matrix([[mp.mpf(str(sp.N(M[i, j].subs(q, Q0), DPS + 10)))
                           for j in range(M.cols)] for i in range(M.rows)])
    nV0, nV1, nB = numm(V0), numm(V1), numm(beta)
    idx1 = [i for i in range(16) if bin(i).count("1") == 1]
    idx2 = [i for i in range(16) if bin(i).count("1") == 2]

    def sub(M, idx):
        return mp.matrix([[M[i, j] for j in idx] for i in idx])

    scan = []
    scan_amax, scan_arg = mp.mpf(0), None
    for k in range(1, 5):
        for combo in itertools.product(("V0", "V1"), repeat=k):
            Xn = mp.eye(16)
            for c in combo:
                Xn = Xn * (nV0 if c == "V0" else nV1)
            Wn = Xn * nB
            ev = list(mp.eig(sub(Wn, idx1), left=False, right=False)) + \
                list(mp.eig(sub(Wn, idx2), left=False, right=False))
            real_pos = [mp.re(e) for e in ev
                        if abs(mp.im(e)) < mp.mpf(10) ** -40 and mp.re(e) > 0
                        and abs(mp.re(e) - 1) > mp.mpf(10) ** -40]
            amax = max((abs(mp.log(r)) for r in real_pos), default=mp.mpf(0))
            nm = "".join(combo)
            scan.append({"X": nm, "has_imaginary_phase": bool(real_pos),
                         "a_max": mp.nstr(amax, 20)})
            if amax > scan_amax:
                scan_amax, scan_arg = amax, nm
    n_imag = sum(1 for r in scan if r["has_imaginary_phase"])
    print(f"  scan: {n_imag}/{len(scan)} gamma-gamma words have an imaginary phase; "
          f"max |a| = {mp.nstr(scan_amax, 12)} at {scan_arg}\n")
    check("all_30_gamma_gamma_words_stay_below_the_needed_phase",
          len(scan) == 30 and scan_amax < a_need,
          f"{n_imag} of 30 gamma-gamma words X give X * beta_Bor a real positive "
          f"eigenvalue (imaginary phase) on an H_4 block; the largest |a| is "
          f"{mp.nstr(scan_amax, 12)} (word {scan_arg}), against the needed "
          f"{mp.nstr(a_need, 10)}: {mp.nstr(a_need / scan_amax, 5)}x short. Scope (a): "
          "words of length <= 8.")

    allp = all(ok for _, ok, _ in RESULTS)
    print(f"  {sum(ok for _, ok, _ in RESULTS)}/{len(RESULTS)} checks passed")
    wb = WitnessBuilder("qbeta-d-eigenphase-four-strand", engine="mpmath")
    for nm, ok, det in RESULTS:
        wb.add_assertion(nm, computed="PASS" if ok else "FAIL", expected="PASS",
                         tolerance="exact", source=det)
    wb.save({
        "description": ("Eigenphase type (real vs imaginary) of the G^CC^R3 four-strand "
                        "process words X * beta_Bor on the H_4 blocks (3,1) and (2,2). "
                        "Candidate list from docs/audits/2026-11-21-beta-pair-creation-word-"
                        "proposal.md; nothing selected or scored."),
        "beans": ["qou-cds1", "qou-pdix", "qou-99qc"],
        "q0Anchor": "proton",
        "q0Value": Q_50_DIGIT_STR,
        "words": rows,
        "a_max": mp.nstr(a_max, 30),
        "gamma_gamma_scan": scan,
        "scan_a_max": mp.nstr(scan_amax, 30),
        "scan_a_max_word": scan_arg,
        "a_needed": mp.nstr(a_need, 30),
        "F_required": mp.nstr(F_req, 20),
        "scope": "(a): these three words; no claim about other four-strand words.",
    })
    return 0 if allp else 1


if __name__ == "__main__":
    raise SystemExit(main())
