#!/usr/bin/env python3
"""Keystone Step-1 gate: does WRT(S3/2I) (SU(2)-side modular data) reproduce the
S_n-side q-Plancherel weight  W_lambda = d_q(lambda)^2 / [n]_q!  ?

This is the "cheap and decisive" Step-1 gate of the DG attack plan (#2503), run
systematically across n = 3, 4, 5 (it had not been run as a systematic gate; #2608
only spot-checked n = 5). EXPLORATORY, zero free parameters, no production rewire.

Frame (respecting the #2608 Schur-Weyl category-error trap)
-----------------------------------------------------------
WRT(S3/2I) is a Chern-Simons / RT invariant whose colour data is the *SU(2)-side*
modular data: a block lambda |- n with at most two rows corresponds, under classical
Schur-Weyl (C^2)^{x n} = (+)_{lambda: <=2 rows} S^lambda (x) V_lambda, to the SU(2)
irrep of spin  j = (lambda_1 - lambda_2)/2,  whose balanced quantum dimension is
[2j+1]_q = [lambda_1 - lambda_2 + 1]_q.  W_lambda lives on the *Hecke S_n side*: its
numerator is the S_n q-dimension d_q(lambda) (q-hook-length formula). The gate asks,
per block, whether the SU(2)-side q-dim equals the S_n-side q-dim d_q(lambda).

Two ways the SU(2)/WRT(S3/2I) route can FAIL to reproduce W_lambda:
  (COVERAGE) blocks with >= 3 rows (e.g. the electron (3,1,1) at n=5) are OUTSIDE the
             GL_2 Schur-Weyl image -- the SU(2) side assigns them no weight at all.
  (VALUE)    even on <=2-row blocks, [2j+1]_q can differ from d_q(lambda).

Also reports the normalization analysis the owner asked about: W_lambda in the
[n]_q! normalization vs the D^2 = sum d_q^2 (Plancherel-probability) normalization,
and the defect 1 - Z(n) with Z(n) = sum_lambda d_q^2/[n]_q!. Per-block *ratios*
within fixed n are normalization-invariant; only the total Z(n) (the defect) is
normalization-sensitive.

Balanced quantum integer  [m]_q = (q^m - q^-m)/(q - q^-1)  (symmetric q -> 1/q).
q-dimension  d_q(lambda) = [n]_q! / prod_cells [hook]_q  (q-hook-length).
No fit: every number is computed; q_0 and the 210 ppb target never tune anything.
"""
import json
import sys
import mpmath as mp

mp.mp.dps = 50


def q0_value():
    """Canonical q_0 if qou_substrate is importable, else the pinned literal."""
    try:
        from qou_substrate.constants import q_at  # noqa
        return mp.mpf(str(q_at("proton")))
    except Exception:
        return mp.mpf("1.1099785900594")


Q0 = q0_value()


def qint(m, q):
    """Balanced quantum integer [m]_q = (q^m - q^-m)/(q - q^-1)."""
    return (q ** m - q ** (-m)) / (q - q ** (-1))


def q_factorial(m, q):
    r = mp.mpf(1)
    for k in range(1, m + 1):
        r *= qint(k, q)
    return r


def partitions(n, _max=None):
    """All partitions of n as weakly-decreasing tuples (rows)."""
    if _max is None:
        _max = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, _max), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def hooks(lam):
    """Hook lengths of every cell of the Young diagram of lam."""
    lam = list(lam)
    cols = [0] * (lam[0] if lam else 0)
    for r in lam:
        for j in range(r):
            cols[j] += 1
    hs = []
    for i, r in enumerate(lam):
        for j in range(r):
            arm = r - 1 - j
            leg = cols[j] - 1 - i
            hs.append(arm + leg + 1)
    return hs


def d_q(lam, q):
    """S_n-side q-dimension via the q-hook-length formula."""
    n = sum(lam)
    den = mp.mpf(1)
    for h in hooks(lam):
        den *= qint(h, q)
    return q_factorial(n, q) / den


def su2_dim_q(lam, q):
    """SU(2)-side balanced q-dimension [2j+1]_q for a <=2-row block (spin
    j=(lam_1-lam_2)/2), i.e. the WRT(S3/2I) modular datum. None if >2 rows
    (outside the GL_2 Schur-Weyl image)."""
    if len(lam) > 2:
        return None
    l1 = lam[0]
    l2 = lam[1] if len(lam) > 1 else 0
    return qint(l1 - l2 + 1, q)


def analyse(n):
    parts = list(partitions(n))
    nf = q_factorial(n, Q0)
    rows = []
    D2 = mp.mpf(0)
    for lam in parts:
        dq = d_q(lam, Q0)
        D2 += dq ** 2
    Z = mp.mpf(0)
    for lam in parts:
        dq = d_q(lam, Q0)
        w_fac = dq ** 2 / nf          # W_lambda = d_q^2 / [n]_q!
        Z += w_fac
        su2 = su2_dim_q(lam, Q0)
        # the VALUE test compares the two q-dimensions d_q (S_n) vs [2j+1]_q (SU(2))
        if su2 is None:
            match = None
        else:
            match = abs(dq - su2) < mp.mpf(10) ** (-12)
        rows.append({
            "lambda": list(lam),
            "rows": len(lam),
            "in_su2_image": su2 is not None,
            "d_q_Sn": mp.nstr(dq, 8),
            "su2_dim_q": (mp.nstr(su2, 8) if su2 is not None else None),
            "d_q_eq_su2": match,
            "W_lambda_nfac": mp.nstr(w_fac, 8),
            "W_lambda_D2": mp.nstr(dq ** 2 / D2, 8),
        })
    return parts, nf, D2, Z, rows


def main():
    print(f"q_0 = {mp.nstr(Q0, 12)}  (>1, growth regime; SU(2) Schur-Weyl <=2 rows)")
    out = {
        "description": ("Keystone Step-1 gate: WRT(S3/2I) SU(2)-side [2j+1]_q vs the "
                        "S_n-side W_lambda numerator d_q(lambda), n=3,4,5 at q_0. "
                        "Tests coverage (>=3-row blocks outside the GL_2 Schur-Weyl "
                        "image) and value (d_q vs [2j+1]_q). No fit."),
        "q0": mp.nstr(Q0, 16),
        "dps": mp.mp.dps,
        "by_n": {},
    }
    total_coverage_gap = 0
    total_value_match = 0
    total_le2 = 0
    coincidences = []
    for n in (3, 4, 5):
        parts, nf, D2, Z, rows = analyse(n)
        gap = sum(1 for r in rows if not r["in_su2_image"])
        le2 = [r for r in rows if r["in_su2_image"]]
        matches = [r for r in le2 if r["d_q_eq_su2"]]
        total_coverage_gap += gap
        total_le2 += len(le2)
        total_value_match += len(matches)
        for r in matches:
            coincidences.append({"n": n, "lambda": r["lambda"]})
        print(f"\n=== n = {n}  ({len(parts)} blocks; Z(n)=sum d_q^2/[n]_q! = "
              f"{mp.nstr(Z, 10)}; 1-Z(n) = {mp.nstr(1 - Z, 10)}) ===")
        print(f"{'lambda':<16}{'rows':>5}{'d_q (S_n)':>14}{'[2j+1]_q (SU2)':>16}"
              f"{'eq?':>6}{'W_l/[n]!':>12}{'W_l/D^2':>12}")
        for r in rows:
            su2s = r["su2_dim_q"] if r["su2_dim_q"] is not None else "-- (>=3 row)"
            eqs = "" if r["d_q_eq_su2"] is None else ("YES" if r["d_q_eq_su2"] else "no")
            print(f"{str(r['lambda']):<16}{r['rows']:>5}{r['d_q_Sn']:>14}{su2s:>16}"
                  f"{eqs:>6}{r['W_lambda_nfac']:>12}{r['W_lambda_D2']:>12}")
        out["by_n"][str(n)] = {
            "num_blocks": len(parts),
            "Z_n": mp.nstr(Z, 12),
            "defect_1_minus_Z": mp.nstr(1 - Z, 12),
            "coverage_gap_blocks": gap,
            "le2_row_blocks": len(le2),
            "value_matches": len(matches),
            "blocks": rows,
        }

    verdict = (
        "REFUTE the naive SU(2)/WRT(S3/2I) route as a reproduction of the full "
        f"W_lambda family. COVERAGE: {total_coverage_gap} blocks across n=3,4,5 have "
        ">=3 rows and lie OUTSIDE the GL_2 (spinor C^2) Schur-Weyl image -- the "
        "SU(2) side assigns them no weight (incl. the electron (3,1,1) at n=5). "
        f"VALUE: of {total_le2} <=2-row blocks, only {total_value_match} have "
        f"d_q(lambda) == [2j+1]_q exactly ({coincidences}); the rest differ (e.g. "
        "muon (3,2): d_q=[5]_q vs [2]_q). Consistent with #2608's Schur-Weyl duality "
        "(WRT SU(2)-side != W_lambda S_n-side, coincide only at (4,1)-type) and "
        "#2406's 'no finite colour-SU(N) arena'. The geometric W_lambda index MUST "
        "live on the full-Hecke (infinite-dim) side, not the SU(2)/WRT(S3/2I) "
        "modular data. NORMALIZATION: per-block ratios within fixed n are identical "
        "in the [n]_q! and D^2 conventions (global factor cancels); only the total "
        "Z(n) -- the defect 1-Z(n) -- is normalization-sensitive, so the defect "
        "(not the absolute per-block value) is the fixed falsifiable content."
    )
    out["verdict"] = verdict
    out["coincidences_d_q_eq_su2"] = coincidences
    print("\nVERDICT:\n" + verdict)

    wpath = "computations/keystone-step1-gate-wrt-vs-wlambda.witness.json"
    with open(wpath, "w") as fh:
        json.dump(out, fh, indent=2)
    print(f"\nwitness -> {wpath}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
