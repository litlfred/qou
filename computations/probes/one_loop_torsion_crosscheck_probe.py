#!/usr/bin/env python3
"""one_loop_torsion_crosscheck_probe.py — beans qou-epkn, qou-ohl6, qou-68uk, qou-u33z.

Regression check of computations/one_loop_torsion.py on the figure-eight knot
against the worked example of Garoufalidis–Yoon, "Twisted Neumann–Zagier
matrices" [arXiv:2109.00379v1], held at library/arxiv-2109.00379v1/.

PRE-REGISTERED (written before running):

  Source facts used (checked against the held text):
    S1  §5.1 eq. (69): tau^CS(T, t) = ± t (t − 1) ( t² − (z1 z2 + 2 z1 + 2 z2 − 4)/(z1 z2) · t + 1 ),
        up to ± t^r, with the complete structure z1 = z2 = (1 + √−3)/2, giving
        tau^CS(T, t) = ± t (t − 1)(t² − 5 t + 1)  (eq. after (69)).
    S2  Theorem 2 (§1.4): tau^CS(T, 1) = 0 and d/dt|_{t=1} tau^CS(T, t) = tau^CS_λ(T),
        λ the canonical longitude.  The ± t^r ambiguity does not move the
        derivative at t = 1 because tau^CS(T, 1) = 0.

  Checks:
    A  exact (sympy): substituting z1 = z2 = (1+√−3)/2 into (69) reproduces
       t² − 5t + 1.                                             PASS iff equal.
    B  exact (sympy): |d/dt|_{t=1} tau^CS(T, t)| = 3.           PASS iff equal.
    C  producer: |one_loop(4_1, curves=[1])| (longitude row) equals the value
       from B to 50 digits.                                     PASS iff rel < 1e-45.
    D  producer: |one_loop(4_1)| (meridian row) = √3/2, and the ratio C/D equals
       |cusp shape| = 2√3 (change of curve).                    PASS iff rel < 1e-45.

  Added before their first run (beans qou-ohl6, qou-68uk):
    S3  [dubois2007] (arXiv:0706.2213v3) §5.2 example (3): for 4_1 = J(2,−2),
        T_λ(ρ_{√s,u}) = τ_0 (−2(s + s⁻¹) + 1), τ_0 a sign; at the holonomy the
        meridian is parabolic, s = 1 (§5.3), so |T_λ| = 3.
    S4  [garoufalidis2021] §3.1: the 4_1 triangulation cPcbbbiht_BaCB has
        G = [[2,2],[0,0]], G' = [[1,1],[1,1]], G'' = [[0,0],[2,2]].
    E  exact: |τ_0(−2(1+1)+1)| = 3 equals the value in B, and |one_loop(4_1,
       longitude)| matches it (C).                              PASS iff both.
    F  SnapPy's 4_1 has isosig cPcbbbiht_BaCB and its edge rows equal S4
       (as a set of rows).                                      PASS iff equal.
    G  |one_loop| (meridian) is the same on non-minimal triangulations of 4_1:
       four isosigs with 3, 4, 4, 5 tetrahedra, obtained by explicit 2-3 moves,
       each verified isometric to 4_1 with all tetrahedra positively oriented,
       the peripheral row taken as the preimage of 4_1's meridian under the
       SnapPy isometry's cusp map, rel < 1e-40.                 PASS iff all.
       (Amended twice before G gave a usable result: SnapPy's randomize() on 4_1
       returns to the same 2-tetrahedron triangulation every time, so it tested
       nothing; "Braid:" specs include the braid axis, a different manifold.
       A third run used SnapPy's own peripheral basis on the rebuilt isosigs,
       which is not the knot meridian; the values it gave, √21·√3/2 etc., are
       |p + q·2√3 i|·√3/2, i.e. the change-of-curve law, not a failure.)

  Added for bean qou-u33z (run first as a scratch check, then moved here
  unchanged):
    S5  [neumann-cspaper] Prop. 2.3 / Thm 2.4: conditions C1 (η-sum 2 round each
        edge), C2 (peripheral sums 0) and C3 (parity). With η = (c', −c'',
        −c' + c'' + 1) the per-tetrahedron sum is 1, so C1 + C2 is exactly the
        producer's `flattening(full_neumann=True)`; C3 is not imposed there.
    H  |one_loop| (meridian, through the isometry) of 5_2 is the same on 8
       distinct triangulations with 4–6 tetrahedra, rel < 1e-40. The
       one-loop-ambiguity-group witness records 9 distinct |det J| values for
       5_2; H tests whether the C1 + C2 flattening monomial alone removes that
       ambiguity, without C3.                                   PASS iff all.

  Transcription note (recorded after the first run): the first run used
  (z1 z2 − 2 z1 − 2 z2 + 4) in S1, a sign slip in reading the OCR'd eq. (69);
  check A failed on it (coefficient −3 instead of 5) and B and C failed as a
  consequence. The held text reads "t² − (z1z2 + 2z1 + 2z2 − 4)/(z1z2) t + 1";
  the criteria above were not changed.

  A match is a regression check only. It adopts no external number and says
  nothing about the c ≥ 2 normalisation the producer flags as unpinned.
"""
import json, os, sys
import sympy as sp
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
mp.mp.dps = 70

def check_ab():
    t = sp.symbols("t")
    z = (1 + sp.sqrt(-3)) / 2
    coeff = sp.nsimplify(sp.simplify((z * z + 2 * z + 2 * z - 4) / (z * z)))
    quad = sp.expand(t**2 - coeff * t + 1)
    A = sp.simplify(quad - (t**2 - 5 * t + 1)) == 0
    tau = t * (t - 1) * quad
    d1 = sp.simplify(sp.diff(tau, t).subs(t, 1))
    B = sp.Abs(d1) == 3 and sp.simplify(tau.subs(t, 1)) == 0
    return A, B, coeff, d1

def main():
    A, B, coeff, d1 = check_ab()
    import snappy
    from one_loop_torsion import one_loop
    M = snappy.Manifold("4_1")
    tau_mu = one_loop(M)
    tau_lam = one_loop(M, curves=[1])
    target = mp.mpf(abs(int(d1)))
    relC = abs(abs(tau_lam) - target) / target
    relD1 = abs(abs(tau_mu) - mp.sqrt(3) / 2) / (mp.sqrt(3) / 2)
    relD2 = abs(abs(tau_lam) / abs(tau_mu) - 2 * mp.sqrt(3)) / (2 * mp.sqrt(3))
    C = relC < mp.mpf("1e-45")
    D = relD1 < mp.mpf("1e-45") and relD2 < mp.mpf("1e-45")
    out = {
        "bean": "qou-epkn",
        "source": "[garoufalidis2021] arXiv:2109.00379v1 §5.1 eq.(69), Thm 2",
        "A_quadratic_coefficient": str(coeff), "A_pass": bool(A),
        "B_derivative_at_1": str(d1), "B_pass": bool(B),
        "C_abs_tau_longitude": mp.nstr(abs(tau_lam), 50), "C_rel": mp.nstr(relC, 5), "C_pass": bool(C),
        "D_abs_tau_meridian": mp.nstr(abs(tau_mu), 50), "D_rel_meridian": mp.nstr(relD1, 5),
        "D_rel_ratio_2sqrt3": mp.nstr(relD2, 5), "D_pass": bool(D),
    }
    print(json.dumps(out, indent=2))
    E = abs(-2 * (1 + 1) + 1) == abs(int(d1)) and C
    gl = M.gluing_equations()
    N = M.num_tetrahedra()
    rows = sorted(tuple(int(x) for x in gl[i]) for i in range(N))
    paper = sorted([(2, 1, 0, 2, 1, 0), (0, 1, 2, 0, 1, 2)])
    F = M.triangulation_isosig().startswith("cPcbbbiht") and rows == paper
    devs, tets = [], []
    for spec in ("dLQbcccdegj", "eLAkbccddhhnqw", "eLPkbcdddmbkgw", "fLLQcbeddeehhjved"):
        X = snappy.Manifold(spec)
        if (X.num_tetrahedra() <= 2 or not X.is_isometric_to(M)
                or X.solution_type() != 'all tetrahedra positively oriented'):
            devs.append(mp.mpf(1)); tets.append((spec, X.num_tetrahedra(), False)); continue
        A = X.is_isometric_to(M, return_isometries=True)[0].cusp_maps()[0]
        a, b, c, d = int(A[0][0]), int(A[0][1]), int(A[1][0]), int(A[1][1])
        det = a * d - b * c
        pq = (d * det, -c * det)          # A^{-1} (1, 0), det = ±1
        tets.append((spec, X.num_tetrahedra(), list(pq)))
        devs.append(abs(abs(one_loop(X, curves=[pq])) - mp.sqrt(3) / 2) / (mp.sqrt(3) / 2))
    G = max(devs) < mp.mpf("1e-40")
    out.update({"E_pass": bool(E), "F_isosig": M.triangulation_isosig(), "F_edge_rows": rows,
                "F_pass": bool(F), "G_max_rel_dev": mp.nstr(max(devs), 5),
                "G_triangulations": tets, "G_pass": bool(G)})
    print(json.dumps({k: out[k] for k in ("E_pass", "F_pass", "G_triangulations", "G_max_rel_dev", "G_pass")}, indent=2))
    import random
    M5 = snappy.Manifold("5_2"); ref = abs(one_loop(M5))
    random.seed(7); seen = {}
    for _ in range(300):
        X = snappy.Manifold("5_2")
        try:
            for _ in range(random.choice([1, 2, 3])):
                X._two_to_three(random.randrange(X.num_tetrahedra()), random.randrange(4))
        except Exception:
            continue
        if X.solution_type() != "all tetrahedra positively oriented":
            continue
        sig = X.triangulation_isosig(decorated=False)
        if sig in seen:
            continue
        Y = snappy.Manifold(sig)
        if Y.solution_type() != "all tetrahedra positively oriented" or not Y.is_isometric_to(M5):
            continue
        A5 = Y.is_isometric_to(M5, return_isometries=True)[0].cusp_maps()[0]
        a, b, c, d = int(A5[0][0]), int(A5[0][1]), int(A5[1][0]), int(A5[1][1])
        det = a * d - b * c
        seen[sig] = (Y.num_tetrahedra(), abs(abs(one_loop(Y, curves=[(d * det, -c * det)])) - ref) / ref)
        if len(seen) >= 8:
            break
    Hdev = max(v[1] for v in seen.values()) if seen else mp.mpf(1)
    H = len(seen) == 8 and Hdev < mp.mpf("1e-40")
    out.update({"H_5_2_abs_tau": mp.nstr(ref, 30), "H_triangulations": len(seen),
                "H_tet_counts": sorted({v[0] for v in seen.values()}),
                "H_max_rel_dev": mp.nstr(Hdev, 5), "H_pass": bool(H)})
    print(json.dumps({k: out[k] for k in out if k.startswith("H_")}, indent=2))
    ok = A and B and C and D and E and F and G and H
    print("ALL PASS" if ok else "FAIL")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
