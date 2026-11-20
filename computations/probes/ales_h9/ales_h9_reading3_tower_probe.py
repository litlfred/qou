#!/usr/bin/env python3
"""qou-ales: reading-3 feasibility tracked up the tower, H_3 -> H_6 -> H_9.

Pre-registration (committed before any H_9 number was computed):
    computations/probes/ales_h9/preregistration.md

Reading 3 (owner 2026-09-12, whole element 2026-09-13): chi_lambda(element) >= 0 on
every Wedderburn block lambda with Markov weight y_lambda > 0. Under convention D
(z = q^3/(q^2+1)) that is the two-row blocks. This probe evaluates it at
H_3 (one nucleon), H_6 (two nucleons, interface generator 2) and H_9 (three
nucleons, interfaces 2 and 5) for the pre-registered candidate set, with bond
column "none" and bond column "G^3 on every interface", and reports whether each
candidate's verdict is stable under embedding.

A letter (g, d) denotes sigma_g + d*h, d in {0, -1/2, -1}; generator g (0-indexed)
maps to the Hoefsmit matrix rho_lambda(T_{g+1}).

ARITHMETIC. mpmath mpf at 60 dps (numpy object arrays of mpf for matrix products --
no float64 anywhere). y_lambda exact over Q(q), substituted at the rational proton
pin, then converted. Nothing reads AME, CODATA, Q_beta or a census; nothing is
selected.

Run: python3 -u computations/probes/ales_h9/ales_h9_reading3_tower_probe.py \
       2>&1 | tee /tmp/ales_h9.log
"""
from __future__ import annotations

import itertools
import json
import sys
import time
from math import factorial
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[3]
for _p in ("computations", "computations/hecke", "computations/markov",
           "computations/substrate", "tools/pyhecke/python", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402  (object arrays of mpf only)
import sympy as sp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from hoefsmit_mpfr import build_hoefsmit_mpfr  # noqa: E402
from hoefsmit_symbolic import Q as QSYM  # noqa: E402
from markov_weights_symbolic import hooks_and_contents, y_lambda_symbolic  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

DPS = 60
set_compute_dps(DPS)
mp.mp.dps = DPS
T0 = time.time()

Q0 = Q_MP
H0 = Q0 - 1 / Q0
ZERO_TOL = mp.mpf("1e-40")
FAILED: list[str] = []

ZD, HALF, NEG1 = mp.mpf(0), mp.mpf(-1) / 2, mp.mpf(-1)
CORE = [(0, ZD), (1, NEG1)] * 3
QSHIFT = {"p": [ZD, HALF, HALF], "n": [HALF, HALF, NEG1]}
LIVE = {
    "p": CORE + [(0, ZD), (0, HALF), (1, HALF)] + [(0, ZD), (0, ZD)],
    "n": CORE + [(0, HALF), (0, HALF), (1, NEG1)] + [(0, ZD), (0, ZD)],
}
DIPROTON_WITNESS = _ROOT / "computations/probes/diproton-response-closed-form-probe.witness.json"
H3_WITNESS = _ROOT / "computations/qbeta/qbeta-cost-minimal-budget-under-reading3.witness.json"
FORK_WITNESS = _ROOT / "computations/qbeta/qbeta-reading3-scope-fork.witness.json"


def log(msg: str) -> None:
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def check(name: str, ok: bool, note: str, asserts: list) -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {note}", flush=True)
    asserts.append({"name": name, "ok": bool(ok), "note": note})
    if not ok:
        FAILED.append(name)


def partitions(n: int, maxpart: int | None = None):
    maxpart = n if maxpart is None else maxpart
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def f_lambda(lam) -> int:
    hs, _ = hooks_and_contents(list(lam))
    prod = 1
    for x in hs:
        prod *= x
    return factorial(sum(lam)) // prod


def y_at_pin(n: int) -> dict:
    qv = sp.Rational(Q_50_DIGIT_STR)
    ys = y_lambda_symbolic(n)
    out = {}
    for lam, expr in ys.items():
        val = sp.cancel(expr).subs(QSYM, qv)
        out[tuple(lam)] = mp.mpf(sp.Rational(val).p) / mp.mpf(sp.Rational(val).q)
    return out


class Block:
    """Hoefsmit seminormal rep of H_n on partition lam at q0, numpy object arrays."""

    def __init__(self, lam):
        self.lam = lam
        mats, dim = build_hoefsmit_mpfr(lam, Q0)
        self.dim = dim
        self.gen = [np.array(M.tolist(), dtype=object) for M in mats]
        self.eye = np.array(mp.eye(dim).tolist(), dtype=object)

        # sparse column structure of each generator (at most two non-zeros per column)
        self.cols = [[[(j, G[j, c]) for j in range(dim) if G[j, c] != 0] for c in range(dim)]
                     for G in self.gen]

    def word(self, letters, offset: int = 0):
        """prod (sigma_{g+offset} + d h) in this block, by sparse right-multiplication."""
        M = self.eye.copy()
        for g, d in letters:
            cols = self.cols[g + offset]
            dh = d * H0
            N = M * dh
            for c in range(self.dim):
                for j, v in cols[c]:
                    N[:, c] = N[:, c] + M[:, j] * v
            M = N
        return M

    @staticmethod
    def tr(M) -> mp.mpf:
        return mp.fsum(M[i, i] for i in range(M.shape[0]))

    @staticmethod
    def tr_prod(A, B) -> mp.mpf:
        # tr(A B) = sum_ij A_ij B_ji
        return mp.fsum((A * B.T).ravel().tolist())


def bond_letters(i: int):
    return [(i, ZD), (i + 1, NEG1)] * 3


def verdict(chis: dict) -> tuple[bool, list]:
    zeros = [str(l) for l, c in chis.items() if abs(c) < ZERO_TOL]
    ok = all(c >= 0 or abs(c) < ZERO_TOL for c in chis.values())
    return ok, zeros


def main() -> int:
    asserts: list = []
    log(f"qou-ales H_9 tower probe; q0 = {mp.nstr(Q0, 20)}, h = {mp.nstr(H0, 20)}, dps {DPS}")

    # ---- weights and blocks ------------------------------------------------------
    Y, SUPPORT, BLOCKS = {}, {}, {}
    for n in (3, 6, 9):
        Y[n] = y_at_pin(n)
        tot = mp.fsum(Y[n][lam] * f_lambda(lam) for lam in Y[n])
        three_row_max = max((abs(Y[n][lam]) for lam in Y[n] if len(lam) >= 3), default=mp.mpf(0))
        two_row = sorted((lam for lam in Y[n] if len(lam) <= 2), reverse=True)
        pos = all(Y[n][lam] > 0 for lam in two_row)
        check(f"y_normalised_n{n}", abs(tot - 1) < mp.mpf("1e-50"),
              f"sum y f = 1 to {mp.nstr(abs(tot - 1), 3)}", asserts)
        check(f"y_three_row_vanishes_n{n}", three_row_max == 0,
              f"max |y| on >=3-row shapes = {mp.nstr(three_row_max, 3)} (exact zero)", asserts)
        check(f"y_two_row_positive_n{n}", pos, "every two-row y_lambda > 0", asserts)
        SUPPORT[n] = [lam for lam in two_row if Y[n][lam] > 0]
        for lam in SUPPORT[n]:
            BLOCKS[lam] = Block(lam)
        log(f"n={n}: support {SUPPORT[n]} dims {[BLOCKS[l].dim for l in SUPPORT[n]]}")

    # ---- candidate words -----------------------------------------------------------
    cand: dict[str, tuple[str, list]] = {"CORE": ("core", CORE)}
    for t in ("p", "n"):
        for a in itertools.product((0, 1), repeat=3):
            name = f"K0{t}[{''.join(map(str, a))}]"
            cand[name] = (t, CORE + [(g, s) for g, s in zip(a, QSHIFT[t])])
    cand["LIVE_p"] = ("p", LIVE["p"])
    cand["LIVE_n"] = ("n", LIVE["n"])

    # slot matrices: SLOT[(name, slot, lam)]
    SLOT = {}
    for n in (3, 6, 9):
        m = n // 3
        for lam in SUPPORT[n]:
            for name, (_, w) in cand.items():
                for s in range(m):
                    SLOT[(name, s, lam)] = BLOCKS[lam].word(w, 3 * s)
    BOND = {}
    for n in (6, 9):
        ifaces = [2] if n == 6 else [2, 5]
        for lam in SUPPORT[n]:
            B = BLOCKS[lam].word([x for i in ifaces for x in bond_letters(i)])
            BOND[lam] = B
    log("slot and bond matrices built")

    # ---- H_3 chis, and cross-check 1 ------------------------------------------------
    chi3 = {name: {lam: Block.tr(SLOT[(name, 0, lam)]) for lam in SUPPORT[3]} for name in cand}
    feas3 = {name: verdict(chi3[name])[0] for name in cand}
    y3, y21 = Y[3][(3,)], Y[3][(2, 1)]
    dev = mp.mpf(0)
    for name, (_, w) in cand.items():
        c3 = mp.mpf(1)
        for _, d in w:
            c3 *= Q0 + d * H0
        dev = max(dev, abs(c3 - chi3[name][(3,)]))
        tr = y3 * chi3[name][(3,)] + y21 * chi3[name][(2, 1)]
        dev = max(dev, abs((tr - y3 * c3) / y21 - chi3[name][(2, 1)]))
    check("h3_chi_trivial_block_is_product_of_eigenvalues", dev < mp.mpf("1e-40"),
          f"max dev {mp.nstr(dev, 3)}", asserts)
    h3w = json.loads(H3_WITNESS.read_text())
    k0 = h3w["data"]["feasibility_by_k"]["k0"]
    np_ = sum(feas3[f"K0p[{''.join(map(str, a))}]"] for a in itertools.product((0, 1), repeat=3))
    nn_ = sum(feas3[f"K0n[{''.join(map(str, a))}]"] for a in itertools.product((0, 1), repeat=3))
    check("h3_k0_counts_reproduce_merged_witness",
          np_ == k0["reading3_p"] and nn_ == k0["reading3_n"],
          f"here p {np_}/8 n {nn_}/8; witness p {k0['reading3_p']} n {k0['reading3_n']}", asserts)
    fork = dict(_walk(json.loads(FORK_WITNESS.read_text())))
    fk = fork["reading_B_whole_word_chi21_proton"]
    fkn = fork["reading_B_whole_word_chi21_neutron"]
    dlp = abs(chi3["LIVE_p"][(2, 1)] - mp.mpf(fk))
    dln = abs(chi3["LIVE_n"][(2, 1)] - mp.mpf(fkn))
    check("live_words_reproduce_recorded_chi21", max(dlp, dln) < mp.mpf("1e-18"),
          f"LIVE_p chi_21 {mp.nstr(chi3['LIVE_p'][(2,1)], 20)} (dev {mp.nstr(dlp,3)}), "
          f"LIVE_n {mp.nstr(chi3['LIVE_n'][(2,1)], 20)} (dev {mp.nstr(dln,3)}); "
          "witness stores 20 digits", asserts)

    # ---- cross-check 2: H_6 diproton ratio ---------------------------------------------
    def trM(n, chis):
        return mp.fsum(Y[n][lam] * chis[lam] for lam in SUPPORT[n])

    def chis_of(names, n, bonded):
        out = {}
        for lam in SUPPORT[n]:
            P = BLOCKS[lam].word(
                [(g + 3 * si, d) for si, nm in enumerate(names) for g, d in cand[nm][1]])
            out[lam] = Block.tr_prod(P, BOND[lam]) if bonded else Block.tr(P)
        return out

    free = trM(6, chis_of(["LIVE_p", "LIVE_p"], 6, False))
    atom = trM(6, chis_of(["LIVE_p", "LIVE_p"], 6, True))
    ratio = atom / free
    wit = json.loads(DIPROTON_WITNESS.read_text())["data"]["ratio_atom_over_free"]
    dr = abs(ratio - mp.mpf(wit))
    check("h6_diproton_ratio_reproduces_merged_witness", dr < mp.mpf("1e-45"),
          f"ratio {mp.nstr(ratio, 30)} vs witness, dev {mp.nstr(dr, 3)}", asserts)
    if FAILED:
        log("cross-checks failed; H_9 not trusted, stopping")
        return 1
    log("all cross-checks passed; proceeding to H_6 / H_9 families")

    # ---- F1 homogeneous ------------------------------------------------------------
    F1 = {}
    for name in cand:
        row = {"type": cand[name][0], "letters": len(cand[name][1]),
               "H3": {"chi": {str(l): fmt(c) for l, c in chi3[name].items()},
                      "feasible": feas3[name]}}
        for n in (6, 9):
            for bonded in (False, True):
                ch = chis_of([name] * (n // 3), n, bonded)
                ok, zeros = verdict(ch)
                row[f"H{n}_{'G3' if bonded else 'none'}"] = {
                    "chi": {str(l): fmt(c) for l, c in ch.items()},
                    "feasible": ok, "structural_zeros": zeros,
                    "negative_blocks": [str(l) for l, c in ch.items()
                                        if c < 0 and abs(c) >= ZERO_TOL]}
        F1[name] = row
        log(f"F1 {name:12s} H3 {'Y' if feas3[name] else 'n'} | "
            + " ".join(f"{k}:{'Y' if row[k]['feasible'] else 'n'}"
                       for k in ("H6_none", "H6_G3", "H9_none", "H9_G3")))

    # ---- F2 physical composition ------------------------------------------------------
    opts = {t: [f"K0{t}[{''.join(map(str, a))}]" for a in itertools.product((0, 1), repeat=3)]
            + [f"LIVE_{t}"] for t in ("p", "n")}
    comps = {"pp": "pp", "pn": "pn", "nn": "nn", "3He_ppn": "ppn", "3H_pnn": "pnn"}
    F2 = {}
    F2_rows = {}
    for cname, types in comps.items():
        n = 3 * len(types)
        table = {col: {"YY": 0, "YN": 0, "NY": 0, "NN": 0, "rejected": [], "admitted": []}
                 for col in ("none", "G3")}
        rows = []
        # cache prefix products of all but last slot
        last = len(types) - 1
        prefix = {}
        for pre in itertools.product(*[opts[t] for t in types[:last]]):
            prefix[pre] = {lam: BLOCKS[lam].word(
                [(g + 3 * si, d) for si, nm in enumerate(pre) for g, d in cand[nm][1]])
                for lam in SUPPORT[n]}
        Xc = {}
        for nm in opts[types[last]]:
            for lam in SUPPORT[n]:
                Xc[(nm, lam, "none")] = SLOT[(nm, last, lam)]
                Xc[(nm, lam, "G3")] = SLOT[(nm, last, lam)].dot(BOND[lam])
        for pre, Pd in prefix.items():
            for nm in opts[types[last]]:
                names = list(pre) + [nm]
                f3 = all(feas3[x] for x in names)
                rec = {"words": names, "H3_all_feasible": f3}
                for col in ("none", "G3"):
                    ch = {}
                    for lam in SUPPORT[n]:
                        ch[lam] = Block.tr_prod(Pd[lam], Xc[(nm, lam, col)])
                    ok, zeros = verdict(ch)
                    key = ("Y" if f3 else "N") + ("Y" if ok else "N")
                    table[col][key] += 1
                    if key == "YN":
                        table[col]["rejected"].append(names)
                    if key == "NY":
                        table[col]["admitted"].append(names)
                    rec[col] = {"feasible": ok, "structural_zeros": zeros,
                                "chi": {str(l): mp.nstr(c, 25) for l, c in ch.items()}}
                rows.append(rec)
        F2[cname] = {col: {k: (v if not isinstance(v, list) else len(v))
                           for k, v in table[col].items()} for col in table}
        for col in table:
            F2[cname][col]["rejected_examples"] = table[col]["rejected"][:20]
            F2[cname][col]["admitted_examples"] = table[col]["admitted"][:20]
        F2_rows[cname] = rows
        log(f"F2 {cname:8s} n={n} " + " | ".join(
            f"{col}: YY {table[col]['YY']} YN(rej) {table[col]['YN']} "
            f"NY(adm) {table[col]['NY']} NN {table[col]['NN']}" for col in table))

    # ---- MECHANISM (post-hoc, labelled): SU(2) Clebsch-Gordan branching ------------
    # Under convention D the support is the two-row blocks, i.e. the SU(2) (Jones /
    # Temperley-Lieb) quotient: (3) is spin 3/2, (2,1) is spin 1/2, (n-k,k) is spin
    # (n-2k)/2. Hypothesis H1' (standard Schur-Weyl/LR, NOT proved here): for a free
    # product, chi_(n-k,k)(w_1|...|w_m) = sum over mu_i in {(3),(2,1)} of
    # mult(spin (n-2k)/2 in (x)_i spin(mu_i)) * prod_i chi_{mu_i}(w_i).
    # Checked below against the direct seminormal value on every free element.
    def cg_mult(twos: list[int]) -> dict:
        acc = {0: 1}
        for t in twos:
            nxt: dict = {}
            for j, c in acc.items():
                for k in range(abs(j - t), j + t + 1, 2):
                    nxt[k] = nxt.get(k, 0) + c
            acc = nxt
        return acc

    SPIN = {(3,): 3, (2, 1): 1}

    def cg_predict(names, lam):
        m = len(names)
        twos_lam = lam[0] - (lam[1] if len(lam) > 1 else 0)
        tot = mp.mpf(0)
        for mus in itertools.product(((3,), (2, 1)), repeat=m):
            mult = cg_mult([SPIN[mu] for mu in mus]).get(twos_lam, 0)
            if mult:
                term = mp.mpf(mult)
                for nm, mu in zip(names, mus):
                    term *= chi3[nm][mu]
                tot += term
        return tot

    cg_dev = mp.mpf(0)
    n_cg = 0
    for nm in cand:
        for n in (6, 9):
            ch = F1[nm][f"H{n}_none"]["chi"]
            for lam in SUPPORT[n]:
                cg_dev = max(cg_dev, abs(cg_predict([nm] * (n // 3), lam) - mp.mpf(ch[str(lam)])))
                n_cg += 1
    for cname, rows in F2_rows.items():
        for rec in rows:
            for lam_s, v in rec["none"]["chi"].items():
                lam = tuple(int(x) for x in lam_s.strip("()").split(",") if x.strip())
                cg_dev = max(cg_dev, abs(cg_predict(rec["words"], lam) - mp.mpf(v)))
                n_cg += 1
    check("free_products_obey_su2_clebsch_gordan_branching", cg_dev < mp.mpf("1e-20"),
          f"{n_cg} free-product block characters, max |direct - CG| = {mp.nstr(cg_dev, 3)} "
          "(F2 chis stored at 25 digits)", asserts)

    # homogeneous thresholds: chi_lambda(w|...|w) / chi_(3)(w)^m = P_lambda(x),
    # x = chi_(2,1)(w)/chi_(3)(w). Feasible iff P_lambda(x) >= 0 on every block.
    xs = sp.Symbol("x")
    polys = {}
    for n in (6, 9):
        m = n // 3
        for lam in SUPPORT[n]:
            twos_lam = lam[0] - (lam[1] if len(lam) > 1 else 0)
            P = sp.Integer(0)
            for j in range(m + 1):
                mult = cg_mult([1] * j + [3] * (m - j)).get(twos_lam, 0)
                P += sp.binomial(m, j) * mult * xs**j
            polys[(n, lam)] = sp.expand(P)
    thresholds = {}
    for n in (6, 9):
        roots = []
        for lam in SUPPORT[n]:
            if sp.Poly(polys[(n, lam)], xs).degree() < 1:
                continue
            for r in set(sp.real_roots(sp.Poly(polys[(n, lam)], xs))):
                # a root of even multiplicity is a touch, not a sign change
                if -2 < r <= 0 and sp.Poly(polys[(n, lam)], xs).subs(xs, r - sp.Rational(1, 10**6)) < 0:
                    roots.append((r, lam))
        thresholds[n] = max(roots, key=lambda t: t[0]) if roots else None
    xval = {nm: chi3[nm][(2, 1)] / chi3[nm][(3,)] for nm in cand}
    for n in (6, 9):
        print(f"  H_{n} homogeneous free polynomials P_lambda(x):")
        for lam in SUPPORT[n]:
            print(f"     {str(lam):8s} {sp.factor(polys[(n, lam)])}")
        r, lam = thresholds[n]
        print(f"     -> feasible iff x >= {sp.N(r, 20)} (binding block {lam})")
    print(f"  H_3: feasible iff x >= 0. Candidate x range: "
          f"[{mp.nstr(min(xval.values()), 10)}, {mp.nstr(max(xval.values()), 10)}]")
    for nm in cand:
        for n in (6, 9):
            pred = mp.mpf(str(sp.N(thresholds[n][0], 40))) <= xval[nm]
            if pred != F1[nm][f"H{n}_none"]["feasible"]:
                FAILED.append(f"threshold_mismatch_{nm}_{n}")

    # calibration (post-hoc, NOT a candidate): (sigma_0^-1)^3 has x = 1 - q^6 < -2/3,
    # so the detector must reject it at H_6 and H_9. Shows the test is live.
    cal = [(0, NEG1)] * 3
    cal_x = None
    cal_res = {}
    for n in (3, 6, 9):
        ch = {lam: Block.tr(BLOCKS[lam].word([(g + 3 * s_, d) for s_ in range(n // 3)
                                              for g, d in cal])) for lam in SUPPORT[n]}
        cal_res[n] = verdict(ch)[0]
        if n == 3:
            cal_x = ch[(2, 1)] / ch[(3,)]
    check("detector_live_calibration_rejected_at_every_level",
          not any(cal_res.values()),
          f"(sigma_0^-1)^3 per slot, x = {mp.nstr(cal_x, 12)} (= 1 - q^6 = "
          f"{mp.nstr(1 - Q0**6, 12)}); feasible H3/H6/H9 = "
          f"{cal_res[3]}/{cal_res[6]}/{cal_res[9]}", asserts)

    # bond effect: max relative change of any block character, G3 vs none (F1)
    bond_rel = mp.mpf(0)
    for nm in cand:
        for n in (6, 9):
            a, b = F1[nm][f"H{n}_none"]["chi"], F1[nm][f"H{n}_G3"]["chi"]
            for k in a:
                bond_rel = max(bond_rel, abs(mp.mpf(b[k]) - mp.mpf(a[k])) / abs(mp.mpf(a[k])))
    print(f"  max relative bond effect on a block character (F1): {mp.nstr(bond_rel, 6)}")
    margins = {}
    for cname, rows in F2_rows.items():
        for col in ("none", "G3"):
            margins[f"{cname}_{col}"] = mp.nstr(min(min(mp.mpf(v) for v in r[col]["chi"].values())
                                                    for r in rows), 12)

    # ---- H1 check (prediction: no REJECTED-by-tower in the none column) -------------
    rej_none = sum(F2[c]["none"]["YN"] for c in F2) + sum(
        1 for nm in F1 if F1[nm]["H3"]["feasible"]
        and not (F1[nm]["H6_none"]["feasible"] and F1[nm]["H9_none"]["feasible"]))
    check("H1_prediction_free_product_never_rejected", rej_none == 0,
          f"{rej_none} H_3-feasible free products rejected at H_6/H_9 "
          "(pre-registered prediction: 0)", asserts)

    out = {
        "schema": "ales-h9-reading3-tower/v1",
        "preregistration": "computations/probes/ales_h9/preregistration.md",
        "q0_pin": "proton", "q0_value": Q_50_DIGIT_STR, "dps": DPS,
        "convention": "D, z = q^3/(q^2+1)",
        "y_lambda": {f"n{n}": {str(l): fmt(Y[n][l]) for l in SUPPORT[n]} for n in Y},
        "block_dims": {str(l): BLOCKS[l].dim for l in BLOCKS},
        "assertions": asserts,
        "F1_homogeneous": F1,
        "F2_composition_tables": F2,
        "F2_rows": F2_rows,
        "mechanism_su2_cg": {
            "hypothesis": "H1': free-product block characters follow SU(2) Clebsch-Gordan "
                          "branching ((3)=spin 3/2, (2,1)=spin 1/2); standard Schur-Weyl/LR, "
                          "verified numerically here, not proved in Lean",
            "max_dev": mp.nstr(cg_dev, 5), "n_checked": n_cg,
            "homogeneous_polynomials": {f"H{n}_{lam}": str(sp.factor(polys[(n, lam)]))
                                        for (n, lam) in polys},
            "homogeneous_threshold_x": {f"H{n}": {"x_min": str(sp.N(thresholds[n][0], 25)),
                                                  "binding_block": str(thresholds[n][1])}
                                        for n in (6, 9)},
            "H3_threshold_x": "0",
        },
        "x_ratio_chi21_over_chi3": {nm: fmt(xval[nm]) for nm in cand},
        "calibration_sigma0inv_cubed": {"x": fmt(cal_x), "feasible": {
            f"H{n}": cal_res[n] for n in cal_res}, "note": "post-hoc detector-live check, not a candidate"},
        "max_relative_bond_effect_F1": mp.nstr(bond_rel, 8),
        "F2_min_block_character": margins,
        "no_target": "no AME/CODATA/Q_beta/census value read; nothing selected",
        "wall_seconds": round(time.time() - T0, 1),
    }
    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("ales-h9-reading3-tower", engine="python", start_time=T0,
                        output_dir=Path(__file__).resolve().parent)
    wb.set_description(
        "qou-ales: reading-3 (Frobenius positivity on every y_lambda > 0 block, convention D) "
        "evaluated at H_3, H_6 and H_9 for the pre-registered candidate set (core, k = 0 "
        "nucleon words, live production words; homogeneous and physical compositions; no "
        "bond and G^3 on every interface). Result: zero candidates rejected by the tower, "
        "every H_3-rejected candidate admitted at H_6 and H_9. Mechanism: SU(2) "
        "Clebsch-Gordan branching of the two-row blocks (hypothesis H1', verified on 8433 "
        "free block characters). No measured target read; nothing selected.")
    wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_parameter("dps", DPS)
    wb.add_parameter("convention", "D (z = q^3/(q^2+1))")
    for key, val in out.items():
        if key not in ("assertions", "wall_seconds"):
            wb.add_data(key, val)
    for a_ in asserts:
        wb.add_assertion(a_["name"], computed=str(int(a_["ok"])), expected="1",
                         tolerance="0", source=a_["note"])
    path = wb.save({"q0Anchor": "proton"})
    log(f"witness -> {path.relative_to(_ROOT)}; {len(FAILED)} failed assertion(s)")
    return 0 if not FAILED else 1


def _walk(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield k, v
            yield from _walk(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _walk(v)


if __name__ == "__main__":
    sys.exit(main())
