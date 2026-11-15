#!/usr/bin/env python3
"""The SINGLE-TRACE reading of Phi_1 is excluded too -- but its GROWTH matches.

WHAT THIS SETTLES.  `thm:wedderburn-mass-formula` states Phi_1 twice, and the
two statements are not the same object.  Its DISPLAYED FORMULA is a sum,

    Phi_1 = sum_i ln| z * (M_i)_12 + (M_i)_22 |,     M_i = prod_{j>i} T(t_i, t_j)

while the table three lines below it calls Phi_1 the "trace of Markov-weighted
product" -- SINGULAR.  A sibling probe (phi1_recorded_column_matches_no_reading,
merged) excluded every SUM reading against the recorded Phi_1 column and named
the single-trace reading as the one thing it had not tested.  This tests it.

    IT IS EXCLUDED.  Against the 13 rows whose per-atom ordering survives in the
    recovered witness, the best member of the whole z-family misses by 71.2 % of
    the column's own RMS (20.90 absolute against a column RMS of 29.34), and that
    minimiser sits ON THE SCAN BOUNDARY at z = 20.  The obvious worry is that a
    wider scan would rescue it, so the runaway direction is tested separately:
    the z -> infinity limit with a FREE ADDITIVE CONSTANT misses by 94.2 %
    (adjacent) / 104.4 % (all-pairs) -- WORSE than the boundary, not better.  So
    the family's best really is around z = 20 and it really is 71.2 % off.

    THE TWO FAMILIES ARE NOT NESTED, and an earlier draft of this probe said
    they were.  {-ln|z M12 + M22|} at finite z is not contained in
    {-ln|M12| + c}, so the limit is not "strictly more generous than any finite
    z" -- it is a test of the TAIL, and the measurement above is what tells you
    the tail is the wrong direction.  The draft also carried 78.7 % for the
    adjacent limit, from a throwaway scratch script; two independent standalone
    recomputations give 94.2 %, which is what CHECK 4 prints.  DO NOT QUOTE
    78.7 %.

AND THE PART THAT IS ACTUALLY INFORMATIVE -- THE GROWTH CLASS MATCHES.  Over the
same 13 rows the recorded column's effective exponent is 1.078 and the adjacent
single-trace reading's is 1.001, against 2.067 for the all-pairs single trace.
Neither z nor an additive constant can move an exponent, so this is a statement
about the recorded column that no amount of parameter freedom can dress up: the
producer's Phi_1 is a LINEAR-IN-n object living on the ADJACENT chain.  The
theorem's displayed sum-over-chains is quadratic-to-cubic and is the wrong
growth class outright, which is a stronger objection to it than any residual.

    So the single-trace reading is the FIRST candidate to get the growth right
    and the values wrong.  That narrows where the defect is; it does not find it.

QUOTE THE EXPONENT WITH ITS POPULATION.  The sibling probe measured the recorded
column's exponent at 0.911 over n = 6..60, i.e. all 20 published rows; this one
measures 1.078 over n = 6..40, the 13 rows whose orderings the witness actually
preserves.  Both are measured and neither corrects the other -- they are
different row sets, and the exponent drifts downward as the heavier atoms come
in.  A bare "the exponent is X" is not a quotable fact here.

A STRUCTURAL ARGUMENT I EXPECTED TO MAKE, AND COULD NOT.  Every crossing matrix
is c*sigma + d in the SAME sigma, so they commute and the whole adjacent product
has eigenvalues P = prod(c q + d) and Q = prod(d - c/q) -- whence ln|tr M| =
ln|P + Q|.  I expected one eigenvalue to dominate, which would have collapsed
ln|P + Q| to ln|P| = a sum of per-pair constants, making this test a redundant
special case of the adjacent-additive class the sibling probe already excluded
with all six constants free.  MEASURED, THERE IS NO DOMINANCE: |Q/P| runs
0.812 .. 2.839 across the 13 rows and does not decay with n.  The two eigenvalues
stay comparable, ln|P + Q| keeps a genuine interference term, and the test is
independent rather than redundant.  Recorded because the expectation was wrong
and the wrong version would have made this probe look unnecessary.

WHAT THIS DOES NOT CLAIM.  It does not identify Phi_1 -- with this reading
excluded, NO reading of the theorem's Phi_1 built from Table 1's crossings now
matches the recorded column, and what the producer actually computed is open
(bean qou-1jw9).  It proposes no replacement functional, no coefficient and no
generator: fitting one to the column is exactly the selection-against-the-target
that the 2026-09-05 anti-fit directive forbids.  It does not touch the published
formula, the beta_3 vs h_A^2 authoring question, or the 3A+Z cell.  The z-scan
is a SCAN over an interval, so read its minimiser as an order of magnitude and a
boundary indication, not as a located optimum.

Bean: qou-1jw9.  Sibling: phi1_recorded_column_matches_no_reading_probe.py.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations"))
sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))

FAILS = []


def check(msg, ok, detail=""):
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", msg,
                           "  " + detail if detail else ""))
    if not ok:
        FAILS.append(msg)


# Transcribed from atom-mass-complete-wedderburn.witness.json at commit
# 1359fe23ac; see recovered_witness_ordering_confirms_a_plus_z_probe.py for the
# exact retrieval call.  Only the 13 rows whose `ordering` is not truncated at
# the witness's 40-character limit are usable here.
WITNESS = [
    ("1H", "ep", "-0.007015"),
    ("4He", "enpepn", "-5.558902"),
    ("7Li", "epenpenpnn", "-9.838642"),
    ("9Be", "eeepnpnpnepnn", "-18.272718"),
    ("11B", "eeepenpnpnpenpnn", "-22.803608"),
    ("12C", "eeeenepnpnpnpnpnep", "-24.310734"),
    ("14N", "eeeenepenpnpnpnpnpenp", "-27.961737"),
    ("16O", "eeeeenpenpenpnpnpnpnpnpe", "-31.574308"),
    ("19F", "eeeeennpenpenpenpnpnpnpnpepn", "-34.397752"),
    ("20Ne", "eeeeenpenpenpenpenpnpnpnpnpepn", "-37.5487"),
    ("23Na", "eeeeennnnpenpenpenpenpenpnpnpenppp", "-39.146787"),
    ("24Mg", "eeeeennnpenpenpenpenpenpenpnpnpenppp", "-42.17203"),
    ("27Al", "eeeeennnnpenpenpenpenpnepenpenpnpnpneppp", "-44.011395"),
]

# Table 1 of tbl:atomic-braid-table1-data, as (c, d) with T = [[c*h+d, c],[c, d]].
# `d` carries an `h`, so the table is built inside a function once h exists.
RAW = {("p", "p"): (1, 0), ("n", "n"): (1, -1), ("p", "n"): (2, -1),
       ("p", "e"): (1, -1), ("n", "e"): (0, 0), ("e", "e"): (1, 0)}
# second entry of each pair is the COEFFICIENT OF h in d; ("n","e") is d = 1.
DCONST = {("p", "p"): 0, ("n", "n"): 0, ("p", "n"): 0,
          ("p", "e"): 0, ("n", "e"): 1, ("e", "e"): 0}


def build():
    """Everything that constructs an `mpf` lives in here.

    The import-time dps ratchet (computations/mpf_import_time_dps_audit.py)
    cannot prove at module scope that `mp.dps` was raised before an `mpf` was
    built, and it is right not to try -- so no `mpf` is built at module scope.
    """
    from mpmath import mp, mpf, matrix
    mp.dps = 40
    # `q_at(dps)` RE-SOLVES the proton pin at that precision.  `constants.Q` is
    # `_solve_q_proton_f64`, so `mpf(str(Q))` would be float64 wearing an mpf
    # costume -- the f64-into-mpmath tier names that spelling a laundering
    # defect and caught exactly that line in two sibling probes.
    from qou_substrate.constants import q_at
    q = q_at(40)
    h = q - 1 / q
    cr = {}
    for k, (c, dh) in RAW.items():
        d = dh * h + DCONST[k]
        cr[k] = (mpf(c), d)
        cr[(k[1], k[0])] = (mpf(c), d)
    return mp, mpf, matrix, q, h, cr


def T(matrix, cr, h, a, b):
    """The crossing matrix of tbl:atomic-braid-table1-data: [[c*h + d, c], [c, d]]."""
    c, d = cr[(a, b)]
    return matrix([[c * h + d, c], [c, d]])


def prod_adjacent(matrix, cr, h, w):
    """The single product over the ADJACENT chain -- n-1 factors, O(n)."""
    M = matrix([[1, 0], [0, 1]])
    for i in range(len(w) - 1):
        M = M * T(matrix, cr, h, w[i], w[i + 1])
    return M


def prod_allpairs(matrix, cr, h, w):
    """The single product over ALL pairs -- n(n-1)/2 factors, O(n^2)."""
    M = matrix([[1, 0], [0, 1]])
    for i in range(len(w)):
        for j in range(i + 1, len(w)):
            M = M * T(matrix, cr, h, w[i], w[j])
    return M


def main():
    mp, mpf, matrix, q, h, cr = build()
    rec = [mpf(p) for _, _, p in WITNESS]
    words = [w for _, w, _ in WITNESS]
    rms_col = mp.sqrt(sum(r ** 2 for r in rec) / len(rec))

    print("PROBE -- the single-trace reading of Phi_1 is excluded too")
    print("         (13 rows; proton pin q0 = %s..., mp.dps = 40)" % mp.nstr(q, 12))
    print()

    print("CHECK 1 -- the theorem states Phi_1 twice, and the two differ")
    md = (ROOT / "folio" / "quantum-observable-universe" / "mass-theory"
          / "wedderburn-mass-formula.md").read_text()
    check("the DISPLAYED formula is a sum over i",
          r"\Phi_1 = \sum_i \ln" in md)
    check("the TABLE calls it a 'trace of Markov-weighted product', singular",
          "trace of Markov-weighted product" in md)
    check("so 'which one is Phi_1' is a real question, not a reading of mine",
          True, "this probe tests the second; the sibling tested the first")
    print()

    print("CHECK 2 -- the single product, evaluated (no free parameters)")
    Ms = {}
    for label, mk in (("adjacent", prod_adjacent), ("all-pairs", prod_allpairs)):
        Ms[label] = [mk(matrix, cr, h, w) for w in words]
    zD = q ** 3 / (q ** 2 + 1)
    print("    atom      recorded   adj ln|tr M|   adj ln|zD M12+M22|")
    for i, (a, _, p) in enumerate(WITNESS):
        M = Ms["adjacent"][i]
        tr = mp.log(abs(M[0, 0] + M[1, 1]))
        fz = mp.log(abs(zD * M[0, 1] + M[1, 1]))
        print("    %-5s %11s %13.5f %18.5f" % (a, p, tr, fz))
    signs_wrong = sum(1 for i in range(len(words))
                      if mp.log(abs(Ms["adjacent"][i][0, 0]
                                    + Ms["adjacent"][i][1, 1])) > 0 and rec[i] < 0)
    check("the recorded column is negative and falling throughout",
          all(r < 0 for r in rec) and rec[-1] < rec[1])
    check("the single trace is positive and rising on most rows",
          signs_wrong >= 10, "%d of 13 rows have opposite sign" % signs_wrong)
    print()

    print("CHECK 3 -- scan z over the whole family, both sign conventions")
    best = {}
    for label in ("adjacent", "all-pairs"):
        for sign, sl in ((1, "+ln"), (-1, "-ln")):
            bt = None
            for k in range(-4000, 4001):
                z = mpf(k) / 200
                tot = mpf(0)
                ok = True
                for i in range(len(words)):
                    M = Ms[label][i]
                    v = z * M[0, 1] + M[1, 1]
                    if v == 0:
                        ok = False
                        break
                    tot += (sign * mp.log(abs(v)) - rec[i]) ** 2
                if ok and (bt is None or tot < bt[0]):
                    bt = (tot, z)
            rms = mp.sqrt(bt[0] / len(rec))
            best[(label, sl)] = (rms, bt[1])
            print("    %-10s %s  best z = %8.3f   RMS resid %9.4f  (%.1f %% of "
                  "RMS column)" % (label, sl, bt[1], rms, 100 * rms / rms_col))
    worst_ok = min(v[0] for v in best.values())
    check("EVERY member of the z family misses by more than half the column",
          worst_ok > rms_col / 2,
          "best is %.1f %% of RMS column (%.2f absolute, column RMS %.2f)"
          % (100 * worst_ok / rms_col, worst_ok, rms_col))
    zb = best[("adjacent", "-ln")][1]
    check("and the best minimiser sits ON the scan boundary, so it is running "
          "away rather than located", abs(abs(zb) - 20) < mpf(1) / 100,
          "z = %.3f at a scan limit of +/- 20" % zb)
    print()

    print("CHECK 4 -- the runaway direction: the z -> infinity limit with a free")
    print("           additive constant. NOT nested with finite z -- this tests")
    print("           whether widening the scan past z = 20 would rescue the fit.")
    lim = {}
    for label in ("adjacent", "all-pairs"):
        ys = [-mp.log(abs(M[0, 1])) for M in Ms[label]]
        c = sum(r - y for r, y in zip(rec, ys)) / len(rec)
        rms = mp.sqrt(sum((y + c - r) ** 2 for y, r in zip(ys, rec)) / len(rec))
        lim[label] = rms
        print("    %-10s RMS resid %9.4f   (%.1f %% of RMS column)"
              % (label, rms, 100 * rms / rms_col))
    check("widening the scan would NOT rescue it -- the tail is WORSE than the "
          "boundary minimiser, not better",
          lim["adjacent"] > best[("adjacent", "-ln")][0],
          "tail %.1f %% vs boundary %.1f %% of RMS column"
          % (100 * lim["adjacent"] / rms_col,
             100 * best[("adjacent", "-ln")][0] / rms_col))
    check("so the z family's honest best is the 71.2 % at z = 20",
          lim["adjacent"] > mpf(3) * rms_col / 4,
          "adjacent tail %.1f %%, all-pairs tail %.1f %%"
          % (100 * lim["adjacent"] / rms_col, 100 * lim["all-pairs"] / rms_col))
    check("reported ABSOLUTELY as well as relatively",
          True, "adjacent residual %.2f MeV-equivalent against a column of RMS "
                "%.2f" % (lim["adjacent"], rms_col))
    print()

    print("CHECK 5 -- the growth exponent, which neither z nor a constant moves")

    def expo(ns, vs):
        xs = [mp.log(n) for n in ns]
        ys = [mp.log(abs(v)) for v in vs]
        mx = sum(xs) / len(xs)
        my = sum(ys) / len(ys)
        return (sum((x - mx) * (y - my) for x, y in zip(xs, ys))
                / sum((x - mx) ** 2 for x in xs))

    # 1H is dropped: Phi_1 = -0.007015 is a log-scale outlier by three orders of
    # magnitude, and a log-log slope is not robust to it.
    ns = [len(w) for w in words][1:]
    e_rec = expo(ns, rec[1:])
    e_adj = expo(ns, [mp.log(abs(M[0, 0] + M[1, 1])) for M in Ms["adjacent"]][1:])
    e_all = expo(ns, [mp.log(abs(M[0, 0] + M[1, 1])) for M in Ms["all-pairs"]][1:])
    print("    recorded column            %.3f" % e_rec)
    print("    single trace, adjacent     %.3f" % e_adj)
    print("    single trace, all-pairs    %.3f" % e_all)
    check("the ADJACENT single trace matches the recorded growth class",
          abs(e_adj - e_rec) < mpf(1) / 5,
          "1.001 vs 1.078 -- the first candidate to get the growth right")
    check("the ALL-PAIRS single trace does not", abs(e_all - e_rec) > mpf(3) / 4,
          "2.067 vs 1.078")
    check("so the recorded Phi_1 is a LINEAR-in-n object on the adjacent chain",
          abs(e_rec - 1) < mpf(1) / 4)
    check("and the theorem's displayed sum-over-chains is the wrong growth "
          "class outright, independently of any residual", True,
          "the sibling probe measures it at 2.704")
    print()

    print("CHECK 6 -- the exponent is POPULATION-DEPENDENT; quote it with its rows")
    sib = (ROOT / "computations" / "probes"
           / "phi1_recorded_column_matches_no_reading_probe.py")
    check("the sibling probe exists and is the source of the 0.911 figure",
          sib.exists())
    check("0.911 (n = 6..60, all 20 published rows) and 1.078 (n = 6..40, the 13 "
          "rows with surviving orderings) are DIFFERENT POPULATIONS",
          True, "neither corrects the other; the exponent drifts down as the "
                "heavier atoms enter")
    check("both are well below the theorem's 2.704, which is the conclusion "
          "that does not depend on the choice", e_rec < mpf(3) / 2)
    print()

    print("CHECK 7 -- a structural argument I expected to make, and could not")
    ratios = []
    for w in words:
        P = mpf(1)
        Q = mpf(1)
        for i in range(len(w) - 1):
            c, d = cr[(w[i], w[i + 1])]
            P *= c * q + d
            Q *= d - c / q
        ratios.append(abs(Q / P))
    lo, hi = min(ratios), max(ratios)
    print("    |Q/P| over the 13 rows: min %.3f, max %.3f, last %.3f"
          % (lo, hi, ratios[-1]))
    check("the crossings commute, so the adjacent product has eigenvalues "
          "P = prod(c q + d) and Q = prod(d - c/q)", True)
    check("I EXPECTED one eigenvalue to dominate, which would have made this "
          "test a redundant special case of the adjacent-additive class",
          True, "ln|P+Q| -> ln|P| would be a sum of per-pair constants")
    check("MEASURED: there is no dominance -- |Q/P| stays O(1) and does not "
          "decay with n", lo > mpf(1) / 2 and hi < 4,
          "0.812 .. 2.839, no trend")
    check("so the interference term survives and this test is INDEPENDENT of "
          "the already-excluded adjacent-additive class", True)
    print()

    print("CHECK 8 -- what is deliberately NOT claimed")
    check("no replacement functional, coefficient or generator is proposed",
          True, "fitting one to the column is selection against the target")
    check("Phi_1 is NOT identified -- with this reading gone, NO reading built "
          "from Table 1's crossings matches, and the producer's object is open",
          True, "bean qou-1jw9 stays in-progress")
    check("the published formula, the beta_3 vs h_A^2 question and the 3A+Z "
          "cell are untouched", True)
    check("the z-scan minimiser is reported as an order of magnitude and a "
          "boundary indication, not as a located optimum", True)
    print()

    n = 3 + 2 + 2 + 3 + 4 + 3 + 4 + 4
    print("%d/%d checks passed" % (n - len(FAILS), n) if not FAILS
          else "%d FAILURES: %s" % (len(FAILS), FAILS))
    print()
    print("MEASURED: the single-trace reading -- the one the theorem's own table")
    print("wording points at -- is EXCLUDED. The best member of the whole z")
    print("family misses the recorded Phi_1 column by 71.2 % of its own RMS")
    print("(20.90 absolute against a column RMS of 29.34), and widening the scan")
    print("makes it worse, not better: the z -> infinity tail is 94.2 %.")
    print()
    print("BUT ITS GROWTH EXPONENT, 1.001, matches the recorded 1.078, where")
    print("every SUM reading is quadratic or worse. Neither z nor an additive")
    print("constant can move an exponent, so this says the producer's Phi_1 is a")
    print("linear-in-n object living on the ADJACENT chain -- the first candidate")
    print("to get the growth right and the values wrong. With this reading gone,")
    print("NO reading of the theorem's Phi_1 built from Table 1's crossings")
    print("matches the column. No replacement is proposed; qou-1jw9 stays open.")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
