#!/usr/bin/env python3
"""he4_crossing_remainder_probe.py: exact closed form of the 4He all-pairs crossing
remainder (issue #8960). PROBE, adopts nothing.

The all-pairs ratio of ../he4_gg_all_pairs splits (../he4_closed_form) as
    tr_atom / tr_free = mu(N1) * rho_2(N2) * rho_3(N3) * X_route,
and X_route (the "crossing remainder") had no closed form. Here:

  * the trace is computed exactly in Q(q) through the Temperley-Lieb quotient
    (tl_exact.py: at z_D the three-row Ocneanu weights vanish, so the Markov trace is the
    Jones trace d^(loops - n), d = q + 1/q; checked letter-for-letter against
    ../he4_closed_form/hecke_exact.py);
  * X_route is returned as a rational function of q for every route x {over, under}
    x bond chirality {(s s^-1)^3, mirror (s^-1 s)^3} x labels {ppnn, nnpp};
  * it is checked against the witness ratios (30 stored digits) and evaluated at q = 1;
  * the q0 value is split by inclusion-exclusion over the two crossed nucleon blocks,
    and by which transported bond is present (term by term).

Block 0 is factored out exactly (towerTr_disjoint). The transport is the probe's T_ij.
Exact arithmetic only (sympy QQ(q) field, fractions.Fraction); mpmath only to print.
"""
from __future__ import annotations

import json
import sys
import time
from fractions import Fraction
from multiprocessing import Pool
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "he4_closed_form"))
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))

import _path_bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402  (proton pin)
from witness_base import WitnessBuilder  # noqa: E402
import tl_exact as T  # noqa: E402
from tl_int import TLInt, tr_poly  # noqa: E402
from assembly import ROUTES_HE4, build, rest_after_N0, conv_word  # noqa: E402

mp.mp.dps = 80
T0 = time.time()
GG = COMP / "probes" / "he4_gg_all_pairs" / "he4-gg-all-pairs.witness.json"
CF = COMP / "probes" / "he4_closed_form" / "he4-closed-form.witness.json"
LABELS = {"ppnn": "pn", "nnpp": "np"}   # (type of N1, type of N2 = N3); N0 = other type


def log(m):
    print(f"[{time.time() - T0:7.1f}s] {m}", flush=True)


def to_mp(x):
    return mp.mpf(x.numerator) / x.denominator


def feval(f, q):
    """Evaluate an element of Q(q) at a Fraction."""
    from hecke_exact import qs  # noqa: F401
    num, den = f.numer, f.denom
    nv = sum((Fraction(int(c.numerator), int(c.denominator)) * Fraction(q) ** m[0]
              for m, c in num.terms()), Fraction(0))
    dv = sum((Fraction(int(c.numerator), int(c.denominator)) * Fraction(q) ** m[0]
              for m, c in den.terms()), Fraction(0))
    return nv / dv


def poly_to_field(cl, n):
    """num(q) / ((2q)^len (q^2+1)^n) as an element of Q(q)."""
    from hecke_exact import K, qs
    c, length = cl
    num = K.zero
    for k, v in c.items():
        num += K(v) * qs ** k
    return num / ((2 * qs) ** length * (qs ** 2 + 1) ** n)


def blocks_of(R, label):
    a, b = (R.proton, R.neutron) if label == "ppnn" else (R.neutron, R.proton)
    return [a(), a(), b(), b()]


def sym_row(args):
    route, variant, mirror, label = args
    R = TLInt(2)  # letters only; tr_poly evaluates at q = 2^512 and decodes
    w = build(R, blocks_of(R, label), ROUTES_HE4[route], variant, mirror)
    return args, tr_poly(10, rest_after_N0(w, 11))


def single_factors(mirror):
    R = T.SymLetters
    out = {}
    for nm, blk in (("p", T.proton()), ("n", T.neutron())):
        t = T.tr_field(3, blk)
        out[f"tr_{nm}"] = t
        out[f"mu_{nm}"] = T.tr_field(4, R.V3(0, mirror) + [(a, b, g + 1) for a, b, g in blk]) / t
        for k in (2, 3):
            vals = {v: T.tr_field(k + 3, conv_word(R, blk, k, v, mirror)) / t for v in ("over", "under")}
            assert vals["over"] == vals["under"], (nm, k, mirror)
            out[f"rho{k}_{nm}"] = vals["over"]
    return out


# ---------------------------------------------------------------- q0 attribution (exact, Fraction)
def q0_attribution(route, variant, mirror, label):
    R = TLInt(Q_50_DIGIT_STR)
    bl = blocks_of(R, label)

    def tr3(b):
        return R.tr(3, b) if b else Fraction(1)

    def rho(b, k):
        return R.tr(k + 3, conv_word(R, b, k, "over", mirror)) / tr3(b)

    def X(blocks, bonds):
        w = build(R, blocks, bonds, variant, mirror)
        t = R.tr(10, rest_after_N0(w, len(blocks[0])))
        incoming = {j: sum(1 for _, jj in bonds if jj == j) for j in (1, 2, 3)}
        f = Fraction(1)
        for j in (1, 2, 3):
            f *= tr3(blocks[j]) * (rho(blocks[j], incoming[j]) if incoming[j] >= 2 else
                                    (R.tr(4, R.V3(0, mirror) + [(a, b, g + 1) for a, b, g in blocks[j]])
                                     / tr3(blocks[j]) if incoming[j] == 1 else 1))
        return t / f - 1

    full = ROUTES_HE4[route]
    out = {"full": X(bl, full),
           "skeleton_N1_N2_trivial": X([bl[0], [], [], bl[3]], full),
           "N1_trivial": X([bl[0], [], bl[2], bl[3]], full),
           "N2_trivial": X([bl[0], bl[1], [], bl[3]], full)}
    near = [b for b in full if b[1] - b[0] == 1]
    for far in ((0, 2), (1, 3), (0, 3)):
        out[f"only_transported_{far[0]}{far[1]}"] = X(bl, [b for b in full if b in near or b == far])
    return out


def main():
    gg = json.loads(GG.read_text())["data"]
    E0 = mp.mpf(gg["E0_MeV"])
    cf = json.loads(CF.read_text())["data"]
    keys = [(r, v, m, l) for m in (False, True) for l in ("ppnn", "nnpp")
            for r in ROUTES_HE4 for v in ("over", "under")]
    with Pool(4) as pool:
        facs = {m: single_factors(m) for m in (False, True)}
        log("single-nucleon factors done (rho_2, rho_3 over = under, both chiralities)")
        res = {}
        for args, t in pool.imap_unordered(sym_row, keys):
            res[args] = poly_to_field(t, 10)
            log(f"symbolic {args} done")
        att = dict(zip(keys, pool.starmap(q0_attribution, keys)))
    log("q0 attribution done")

    q0 = Fraction(Q_50_DIGIT_STR)
    rows, checks = [], {}
    for args in keys:
        route, variant, mirror, label = args
        F = facs[mirror]
        a, b = LABELS[label]
        free = F[f"tr_{a}"] * F[f"tr_{b}"] ** 2
        conv = F[f"mu_{a}"] * F[f"rho2_{b}"] * F[f"rho3_{b}"]
        ratio = res[args] / free
        X = ratio / conv
        Xq0, ratio_q0, conv_q0 = feval(X, q0), feval(ratio, q0), feval(conv, q0)
        tf4 = to_mp(feval(F["tr_p"] ** 2 * F["tr_n"] ** 2, q0))
        B_cross = -E0 * tf4 * (to_mp(ratio_q0) - to_mp(conv_q0))
        num, den = X.numer.as_expr(), X.denom.as_expr()
        X1 = num.subs("q", 1) / den.subs("q", 1)
        row = {"route": route, "variant": variant, "bond": "mirror (s^-1 s)^3" if mirror else "(s s^-1)^3",
               "labels": label, "X_minus_1_at_q0": mp.nstr(to_mp(Xq0 - 1), 40),
               "ratio_at_q0": mp.nstr(to_mp(ratio_q0), 40),
               "B_crossing_keV": mp.nstr(B_cross * 1000, 25),
               "X_at_q1": str(X1),
               "X_minus_1_rational_function": str((X - 1).as_expr()),
               "X_num_degree": X.numer.degree(), "X_den_degree": X.denom.degree(),
               "attribution_q0_X_minus_1": {k: mp.nstr(to_mp(v), 20) for k, v in att[args].items()}}
        assert abs(to_mp(att[args]["full"]) - to_mp(Xq0 - 1)) < mp.mpf(10) ** -60
        if not mirror and label == "ppnn":
            wr = next(r for r in gg["rows"] if r["atom"] == "4He" and r["route"] == route and r["variant"] == variant)
            gap = abs(to_mp(ratio_q0) - mp.mpf(wr["ratio_atom_over_free"]))
            cr = next(r for r in cf["he4_all_pairs_split"] if r["route"] == route and r["variant"] == variant)
            row["witness_ratio"] = wr["ratio_atom_over_free"]
            row["ratio_gap_vs_witness"] = mp.nstr(gap, 5)
            row["B_crossing_gap_vs_closed_form_witness_keV"] = mp.nstr(abs(B_cross * 1000 - mp.mpf(cr["B_crossing_keV"])), 5)
            checks[f"{route}_{variant}_ratio_gap"] = gap
        rows.append(row)
        log(f"{label} {'mirror' if mirror else 'normal'} {route:14s} {variant:5s} X-1 = {mp.nstr(to_mp(Xq0 - 1), 12)} "
            f"B_cross = {mp.nstr(B_cross * 1000, 10)} keV  X(1) = {X1}")

    wb = WitnessBuilder("he4-crossing-remainder", engine="Temperley-Lieb quotient over Q(q) (tl_exact.py)",
                        output_dir=HERE)
    wb.set_description(
        "PROBE, adopts nothing (issue #8960). Exact closed form, as a rational function of q, of the 4He "
        "all-pairs crossing remainder X = (tr_atom/tr_free)/(mu(N1) rho2(N2) rho3(N3)), for 4 routes x over/under x "
        "bond chirality x labels. Trace through the TL quotient at z_D (Jones trace), checked against hecke_exact.")
    wb.add_data("E0_MeV_source", "he4-gg-all-pairs.witness.json E0_MeV")
    wb.add_data("single_factors_at_q0", {("mirror_" if m else "") + k: mp.nstr(to_mp(feval(v, q0)), 40)
                                        for m, F in facs.items() for k, v in F.items()})
    wb.add_data("rows", rows)
    for k, v in checks.items():
        wb.add_assertion(k, computed=v, expected=0, tolerance=mp.mpf("1e-28"),
                         source="witness ratios stored to 30 significant digits")
    wb.save({"q0Anchor": "proton"})
    log("witness written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
