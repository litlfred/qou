#!/usr/bin/env python3
"""The three gauge ansaetze of #7092 are NESTED, and the nesting is an exact integer
identity -- so the three verdicts are one chain, not three independent measurements.

WHAT #7092 AND ITS ANSWER LEFT AS THREE SEPARATE FACTS.  The merged verdict
(main f7fee734c3) reports, on the exact L6a4 class-1 point:

    scalar ansatz  lambda_v^{t_i}   (the issue as written)   NOT a coboundary, either sigma
    PGL(3) torus   snappy's 128 x 6 decoration action        sigma_b YES, sigma_a NO
    SL(3) lift     diagonal matrix over K                    NO  (r(3e_0) is not a cube in K)

Three computations, three verdicts.  They are not independent, and this file proves it.

THE IDENTITY.  Write the gauge exponent matrices as snappy and the probe build them:

    A_TORUS [nm][(lev, k)] = #{ v : cusp(v) = k, t_v >= lev+1 },  lev in {0, 1}
    A_SCALAR[nm][k]        = sum_{v : cusp(v) = k} t_v

On the 128 NON-VERTEX coordinates every t_v <= 2 (t_v = 3 occurs only on the 32 vertex
coordinates, which snappy's action matrix excludes), and for t_v <= 2

    #{lev in {0,1} : t_v >= lev+1}  =  min(t_v, 2)  =  t_v.

Summing the two torus columns of one cusp therefore reproduces the scalar column
EXACTLY, over Z, with no remainder:

    A_SCALAR[:, k]  =  A_TORUS[:, (0,k)] + A_TORUS[:, (1,k)]        (*)

So the scalar ansatz is the SUB-TORUS z_{k,0} = z_{k,1} -- the diagonal-scalar subgroup --
and the column lattice of A_SCALAR sits inside that of A_TORUS.

WHY THAT MATTERS.  A coboundary for a SUBGROUP is a coboundary for the group, so (*)
forces the implication

    scalar coboundary  ==>  torus coboundary

and contrapositively, a torus NO would have forced a scalar NO.  The observed pattern
(torus yes for sigma_b, scalar no) is the only one that is informative: the ratio lies in
the full torus and NOT in the scalar sub-torus.  Had the scalar ansatz come back YES with
the torus NO, that would have been a contradiction and a bug in one of the two.

So #7092 as the owner wrote it -- with the scalar ansatz lambda_v^{t_i} -- asks a
STRICTLY STRONGER question than the one that admits the affirmative answer.  Its "no"
and the torus "yes" are consistent, and neither is evidence against the other.

This file establishes (*) by exact integer comparison on all 128 rows, and separately
checks that it FAILS on the 32 vertex coordinates (where t_v = 3), which is why the
restriction to non-vertex rows is load-bearing rather than incidental.

Integer arithmetic only.  No floats, no field arithmetic, nothing to tolerance.
"""
import sys
import re
import warnings

warnings.filterwarnings('ignore')
import snappy

NAME = 'L6a4'
KCLS = 1
N = 3


def parse(nm):
    m = re.match(r'^c_(\d)(\d)(\d)(\d)_(\d+)$', nm)
    return tuple(int(m.group(i)) for i in range(1, 5)), int(m.group(5))


def main():
    M = snappy.Manifold(NAME)
    ntet = M.num_tetrahedra()
    ncusp = M.num_cusps()
    cusp_of = M._get_cusp_indices_and_peripheral_curve_data()[0]
    rows, names, cols = M._ptolemy_equations_action_by_decoration_change(N)
    A_TORUS = [[int(v) for v in r] for r in rows]
    print(f"{NAME}: {ntet} tets, {ncusp} cusps; action matrix {len(A_TORUS)} x "
          f"{len(cols)}", flush=True)
    assert len(names) == 16 * ntet == 128

    # column (lev, cusp) -> index
    col_of = {}
    for ci, cn in enumerate(cols):
        parts = cn.split('_')
        col_of[(int(parts[2]), int(parts[-1]))] = ci

    def scalar_row(t, tet):
        r = [0] * ncusp
        for v in range(4):
            r[cusp_of[tet][v]] += t[v]
        return r

    # ---- (*) on the 128 non-vertex rows --------------------------------------
    bad, maxt = [], 0
    for nm, trow in zip(names, A_TORUS):
        t, tet = parse(nm)
        maxt = max(maxt, max(t))
        want = scalar_row(t, tet)
        got = [trow[col_of[(0, k)]] + trow[col_of[(1, k)]] for k in range(ncusp)]
        if want != got:
            bad.append((nm, want, got))
    print(f"max t_v over the 128 non-vertex rows: {maxt}  (must be <= 2 for (*))",
          flush=True)
    print(f"rows where A_SCALAR[:,k] == A_TORUS[:,(0,k)] + A_TORUS[:,(1,k)]: "
          f"{len(names) - len(bad)} / {len(names)}", flush=True)
    if bad:
        print("IDENTITY FAILS -- the ansaetze are NOT nested.  First 3:")
        for nm, w, g in bad[:3]:
            print(f"   {nm}: scalar {w} vs torus-sum {g}")
        return 1

    # ---- and it must FAIL on the vertex coordinates, where t_v = 3 ------------
    vbad = 0
    for tet in range(ntet):
        for v in range(4):
            t = tuple(3 if w == v else 0 for w in range(4))
            want = scalar_row(t, tet)
            got = [0] * ncusp
            got[cusp_of[tet][v]] = 2          # min(3,2) = 2, what a 2-level torus sees
            if want != got:
                vbad += 1
    print(f"vertex coordinates (t_v = 3) where the identity FAILS: {vbad} / {4 * ntet}"
          f"  (expected all -- min(3,2) = 2 != 3)", flush=True)
    if vbad != 4 * ntet:
        print("UNEXPECTED: the identity should fail on every vertex coordinate.")
        return 1

    print("\n(*) HOLDS on all 128 non-vertex rows, exactly over Z.")
    print("So the scalar ansatz is the sub-torus z_{k,0} = z_{k,1}, and")
    print("    scalar coboundary  ==>  torus coboundary.")
    print("The merged #7092 verdicts (scalar NO, torus YES for sigma_b) are therefore")
    print("ONE chain, not two independent results: the ratio lies in the full torus and")
    print("not in the scalar sub-torus.  The reverse pattern -- scalar YES, torus NO --")
    print("is excluded by (*), so it would have been a bug in one of the two solves.")
    print("\n#7092 as written asks the STRICTLY STRONGER question; its 'no' is not")
    print("evidence against the torus 'yes'.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
