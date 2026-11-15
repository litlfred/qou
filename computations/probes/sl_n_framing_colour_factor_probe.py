#!/usr/bin/env python3
"""The factor of 2 in the level-3 colour test is the U(1) part of gl_N. The
SU(N) framing q^(-1/N) removes it, and the colour singlet forces that factor.

WHAT THIS TESTS
---------------
`level_three_colour_channel_probe.py` (bean `qou-ezhi`) compares the
substrate's two-strand exchange channels with the QCD one-gluon-exchange colour
factors of `3 (x) 3 = 3bar + 6`:

    C(3bar) = -2/3  (attractive)      C(6) = +1/3  (repulsive)      ratio -2

The Hecke generator has eigenvalues `q` (Sym^2) and `-1/q` (Lambda^2), so
`L = -log|eigenvalue|` gives `-log q` and `+log q`. The signs are right and the
ratio is 1. That probe attributes the missing 2 to `det T = -1`.

This probe checks a sharper reading, proposed by the coordinator of bean
`qou-qs4c` as a candidate and not taken as a finding:

1. The Hecke generator in this normalisation is the **gl_N** braiding
   (Jimbo's R-matrix). `gl_N = sl_N (+) u_1`, and the gl_N braiding carries the
   u_1 part. Colour is SU(N), whose braiding is `R_sl = q^(-1/N) R_gl`.
2. By the ribbon (Drinfeld) formula, the braiding on an irreducible summand
   `R` of `V (x) V` is `+/- q^(c_R)`, where `c_R = C_2(R) - 2 C_2(V)` with the
   Casimir in the trace-form normalisation `T_F = 1/2` times 2. Equivalently,
   the exponent is `2 c_R`, where `c_R = (C_2(R) - 2 C_F)/2` is exactly the
   QCD one-gluon colour factor `<lambda_i . lambda_j>/4`.
3. The gl_N exponents are `2 c_R + 1/N`: the u_1 part adds the same `1/N` to
   both channels. That uniform shift is what makes `L_sym + L_anti = 0`
   (`|det T| = 1`). Removing it gives the ratio `(N+1)/(N-1)`, which is 2 at N=3.

WHAT IS CHECKED HERE
--------------------
- **B1. Symbolic in N.** The sl_N eigenvalue exponents equal 2 c_R for both
  channels. The gl_N exponents equal 2 c_R + 1/N. The ratio is (N+1)/(N-1),
  and it equals 2 iff N = 3. Exact arithmetic over Q(N) in sympy.
- **B2. The forcing, on explicit matrices.** Jimbo's gl_N R-matrix is built on
  `V^(x)(N+1)` for N = 2 and N = 3, with exact rational q. The q-antisymmetric
  line `Lambda^N_q` on strands 2..N+1 is located, and the monodromy of strand 1
  around it is measured. It is the scalar `q^2`, not 1, so in gl_N the
  "colour singlet" `Lambda^N V` braids nontrivially. That is the u_1 charge.
  Rescaling `sigma -> c sigma` multiplies the monodromy (2N crossings) by
  `c^(2N)`. Requiring the singlet to braid trivially, which is what makes it
  the trivial object of Rep SU(N) rather than the determinant character of
  GL(N), forces `c^(2N) q^2 = 1`. So `c = q^(-1/N)` is the unique positive
  solution. The general-N statement also comes from Young contents and is
  checked symbolically.
- **B3. The corpus already had the number.** The framing probe
  `the_hull_exit_is_a_fractional_twist_probe.py` (bean `qou-vlrq`) writes a
  framing scalar as `u = -log c`, with `ratio(u) = (log q + u)/(log q - u)`.
  `u = log q / N` gives `(N+1)/(N-1)`, and `e/e_max = u/log q = 1/N`. At N=3
  this is the `e = e_max/3 EXACTLY` that `level_three_colour_channel_probe` A6
  reports as a "clean closed form" without identifying it. It is the sl_3
  framing.
- **B4. Both arms at the proton q_0, at 40 dps.** gl_3 gives ratio 1. sl_3
  gives ratio 2 exactly, and each L equals -2 log q_0 times the QCD colour
  factor.
- **B5. The nuclear sector is NOT repaired.** At level 2, sl_2 framing gives
  ratio 3 against the probe's nuclear target of 33.7. This is a scope-(a)
  negative: the sl_N framing is forced by N and fixes the colour ratio, but it
  is not the missing nuclear mechanism.

DISCIPLINE
----------
Nothing is fitted. The scalar is fixed by the singlet-transparency condition
(B2), which never mentions the colour-factor ratio. The ratio 2 is then a
consequence, checked after the fact. The QCD factors are standard SU(N) group
theory, quoted as the external target. What is NOT established here: whether
the corpus's colour observables SHOULD be read in the SU(N) frame rather than
the Hecke/gl frame. That is a modelling ruling, and it is the owner's (bean
`qou-sl3f`).

-- Ref: [kassel1995] Kassel, Quantum Groups, ch. VIII (Jimbo R-matrix) and
   ch. XIV (ribbon element, theta_V = q^{C_2(V)})
-- Ref: [manuscript] computations/probes/level_three_colour_channel_probe.py A4-A6
-- Ref: [manuscript] computations/probes/the_hull_exit_is_a_fractional_twist_probe.py
"""
from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
sys.path.insert(0, str(ROOT / "tools" / "pyhecke" / "python"))
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from q_parameter import q_at  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False


# ── B1: symbolic in N ───────────────────────────────────────────────────
def b1():
    N = sp.symbols("N", positive=True)
    CF = (N**2 - 1) / (2 * N)                       # T_F = 1/2
    C2_sym = (N - 1) * (N + 2) / N                  # Sym^2 V
    C2_anti = (N + 1) * (N - 2) / N                 # Lambda^2 V
    c_sym = sp.simplify((C2_sym - 2 * CF) / 2)      # QCD colour factor
    c_anti = sp.simplify((C2_anti - 2 * CF) / 2)
    # sl_N eigenvalue exponents (eigenvalue = +q^a_sym, -q^a_anti)
    a_sym_sl, a_anti_sl = 1 - 1 / N, -(1 + 1 / N)
    # gl_N (= Hecke) exponents
    a_sym_gl, a_anti_gl = sp.Integer(1), sp.Integer(-1)
    r = {
        "c_sym": sp.factor(c_sym), "c_anti": sp.factor(c_anti),
        "sl_sym_eq_2c": sp.simplify(a_sym_sl - 2 * c_sym) == 0,
        "sl_anti_eq_2c": sp.simplify(a_anti_sl - 2 * c_anti) == 0,
        "gl_sym_eq_2c_plus_1/N": sp.simplify(a_sym_gl - 2 * c_sym - 1 / N) == 0,
        "gl_anti_eq_2c_plus_1/N": sp.simplify(a_anti_gl - 2 * c_anti - 1 / N) == 0,
        "ratio": sp.factor(sp.simplify(a_anti_sl / a_sym_sl)),
        "sl_L_sum_over_logq": sp.simplify(-(a_sym_sl + a_anti_sl)),
    }
    sols = sp.solve(sp.Eq(-a_anti_sl / a_sym_sl, 2), N)
    r["ratio_2_iff_N"] = sols
    # QCD values at N=3
    r["c_sym_N3"] = c_sym.subs(N, 3)
    r["c_anti_N3"] = c_anti.subs(N, 3)
    return r


# ── B2: forcing, on explicit Jimbo R-matrices ───────────────────────────
def jimbo_R(N, q):
    """gl_N braiding on V(x)V, eigenvalues q (Sym) and -1/q (Lambda)."""
    d = N * N
    M = sp.zeros(d, d)
    h = q - 1 / q
    idx = lambda i, j: i * N + j  # noqa: E731
    for i in range(N):
        for j in range(N):
            if i == j:
                M[idx(i, i), idx(i, i)] = q
            elif i < j:
                M[idx(j, i), idx(i, j)] = 1
            else:
                M[idx(j, i), idx(i, j)] = 1
                M[idx(i, j), idx(i, j)] = h
    return M


def on_strands(R, N, k, n):
    """R acting on strands k,k+1 (0-based) of V^(x)n."""
    left = sp.eye(N ** k)
    right = sp.eye(N ** (n - k - 2))
    return sp.kronecker_product(left, R, right)


def b2(N, q):
    R = jimbo_R(N, q)
    I2 = sp.eye(N * N)
    hecke = sp.simplify((R - q * I2) * (R + I2 / q)) == sp.zeros(N * N, N * N)
    n = N + 1
    S = [on_strands(R, N, k, n) for k in range(n - 1)]
    braid = all(S[k] * S[k + 1] * S[k] == S[k + 1] * S[k] * S[k + 1]
                for k in range(n - 2))
    # q-antisymmetric line on strands 1..N (0-based): common -1/q eigenspace
    # of sigma_2..sigma_N
    stack = sp.Matrix.vstack(*[S[k] + sp.eye(N ** n) / q for k in range(1, n - 1)])
    ker = stack.nullspace()
    # ker = V (x) Lambda^N_q, dimension N
    # monodromy of strand 0 around the block: (s1 s2 .. sN)(sN .. s1)
    A = sp.eye(N ** n)
    for k in range(n - 1):
        A = A * S[k]
    B = sp.eye(N ** n)
    for k in reversed(range(n - 1)):
        B = B * S[k]
    Mono = A * B
    scal = []
    for v in ker:
        w = Mono * v
        # find ratio
        nz = [i for i in range(len(v)) if v[i] != 0][0]
        lam = w[nz] / v[nz]
        scal.append(sp.simplify(lam))
        assert sp.simplify(w - lam * v) == sp.zeros(len(v), 1)
    return {"hecke": hecke, "braid": braid, "dim_ker": len(ker),
            "monodromy": scal, "q_squared": q ** 2}


def b2_contents():
    """Monodromy of V around Lambda^N V from Young contents, general N.

    Full twist acts on S^lambda by q^(2 * sum of contents). V (x) Lambda^N in
    gl_N is lambda = (2, 1^(N-1)) (the (1^(N+1)) summand vanishes).
    """
    N = sp.symbols("N", positive=True, integer=True)
    cont_big = 1 + sum_neg(N)           # (2,1^(N-1)): contents 0,1,-1..-(N-1)
    cont_small = sum_neg(N)             # (1^N): contents 0,-1,..,-(N-1)
    expo = sp.simplify(2 * cont_big - 2 * cont_small)
    c = sp.symbols("c", positive=True)
    q = sp.symbols("q", positive=True)
    # rescaled monodromy c^(2N) q^expo = 1
    sol = sp.solve(sp.Eq(c ** (2 * N) * q ** expo, 1), c)
    return {"exponent": expo, "forced_c": sol}


def sum_neg(N):
    k = sp.symbols("k", integer=True)
    return sp.summation(-k, (k, 0, N - 1))


# ── B3-B5: numbers at q_0 ───────────────────────────────────────────────
def numbers():
    mp.mp.dps = 40
    q = q_at(mp.mp.dps)
    lq = mp.log(q)
    out = {}
    for N in (2, 3):
        Ls_gl, La_gl = -lq, lq
        Ls_sl = -(1 - mp.mpf(1) / N) * lq
        La_sl = (1 + mp.mpf(1) / N) * lq
        out[N] = {"gl": (Ls_gl, La_gl, abs(La_gl / Ls_gl)),
                  "sl": (Ls_sl, La_sl, abs(La_sl / Ls_sl))}
    # framing-probe parametrisation: ratio(u) = (lq+u)/(lq-u), u = lq/N
    u3 = lq / 3
    ratio_u3 = (lq + u3) / (lq - u3)
    # colour factors times -2 log q
    cs, ca = mp.mpf(1) / 3, -mp.mpf(2) / 3
    resid_s = out[3]["sl"][0] - (-2 * lq * cs)
    resid_a = out[3]["sl"][1] - (-2 * lq * ca)
    return q, lq, out, ratio_u3, resid_s, resid_a


def main() -> int:
    A = []
    print("sl_N framing and the colour-factor ratio")

    r1 = b1()
    print("\n  B1 symbolic in N")
    for k, v in r1.items():
        print(f"     {k}: {v}")
    ok = (r1["sl_sym_eq_2c"] and r1["sl_anti_eq_2c"]
          and r1["gl_sym_eq_2c_plus_1/N"] and r1["gl_anti_eq_2c_plus_1/N"]
          and r1["ratio_2_iff_N"] == [3]
          and r1["c_sym_N3"] == sp.Rational(1, 3)
          and r1["c_anti_N3"] == sp.Rational(-2, 3))
    A.append(("B1_sl_exponent_is_twice_colour_factor_all_N", ok,
              f"sl exponents = 2c_R, gl = 2c_R + 1/N, ratio "
              f"{r1['ratio']}, =2 iff N in {r1['ratio_2_iff_N']}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    print("\n  B2 forcing: monodromy of V around Lambda^N_q (Jimbo gl_N)")
    b2res = {}
    ok = True
    for N, qv in ((2, sp.Rational(3, 2)), (2, sp.Rational(7, 5)),
                  (3, sp.Rational(3, 2))):
        r = b2(N, qv)
        b2res[f"N={N},q={qv}"] = r
        good = (r["hecke"] and r["braid"] and r["dim_ker"] == N
                and all(m == r["q_squared"] for m in r["monodromy"]))
        ok = ok and good
        print(f"     N={N} q={qv}: hecke {r['hecke']} braid {r['braid']} "
              f"dim(V(x)Lambda^N_q)={r['dim_ker']} monodromy={r['monodromy'][0]}"
              f" (q^2={r['q_squared']})  {'ok' if good else 'BAD'}")
    rc = b2_contents()
    print(f"     general N from contents: monodromy = q^{rc['exponent']}; "
          f"c^(2N) q^2 = 1 forces c = {rc['forced_c']}")
    ok = ok and rc["exponent"] == 2
    A.append(("B2_singlet_transparency_forces_q_minus_1_over_N", ok,
              f"gl_N monodromy of V around Lambda^N_q is q^2 (explicit N=2,3; "
              f"contents for all N); trivial singlet forces c = "
              f"{rc['forced_c']}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    q, lq, nums, ratio_u3, rs, ra = numbers()
    print(f"\n  B3 framing-probe link: u = log q / 3 gives ratio "
          f"{mp.nstr(ratio_u3, 20)} (e/e_max = 1/3)")
    ok = abs(ratio_u3 - 2) < mp.mpf("1e-35")
    A.append(("B3_e_max_over_3_is_the_sl3_framing", ok,
              f"ratio(u=log q/3) = {mp.nstr(ratio_u3, 12)}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    print(f"\n  B4 both arms at proton q_0 = {mp.nstr(q, 16)}")
    for arm in ("gl", "sl"):
        Ls, La, rr = nums[3][arm]
        print(f"     {arm}_3: L_sym = {mp.nstr(Ls, 15)}  L_anti = "
              f"{mp.nstr(La, 15)}  |ratio| = {mp.nstr(rr, 15)}")
    print(f"     sl_3 residual vs -2 log q * C_R: sym {mp.nstr(rs, 3)}, "
          f"anti {mp.nstr(ra, 3)}")
    ok = (abs(nums[3]["gl"][2] - 1) < mp.mpf("1e-35")
          and abs(nums[3]["sl"][2] - 2) < mp.mpf("1e-35")
          and abs(rs) < mp.mpf("1e-35") and abs(ra) < mp.mpf("1e-35")
          and nums[3]["sl"][0] < 0 < nums[3]["sl"][1])
    A.append(("B4_both_arms_gl_ratio_1_sl_ratio_2", ok,
              f"gl_3 ratio {mp.nstr(nums[3]['gl'][2], 10)}, sl_3 ratio "
              f"{mp.nstr(nums[3]['sl'][2], 10)}, signs preserved"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    print("\n  B5 nuclear sector (level 2): sl_2 framing ratio")
    r2 = nums[2]["sl"][2]
    print(f"     sl_2 ratio = {mp.nstr(r2, 15)} vs nuclear target ~33.7 — "
          f"NOT repaired (scope (a))")
    ok = abs(r2 - 3) < mp.mpf("1e-35")
    A.append(("B5_sl2_framing_gives_3_not_nuclear_33p7", ok,
              f"sl_2 ratio {mp.nstr(r2, 10)}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in A)
    print("\n  " + "-" * 60)
    for n, p, _ in A:
        print(f"  {'PASS' if p else 'FAIL'}  {n}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    if _HAVE_WB:
        try:
            wb = WitnessBuilder(Path(__file__).stem, engine="sympy+mpmath")
            wb.set_description(
                "The factor 2 in the level-3 colour-factor test "
                "(level_three_colour_channel_probe A4) is the u_1 part of "
                "gl_N = sl_N + u_1. The Hecke generator is the gl_N braiding; "
                "its exponents are 2c_R + 1/N where c_R = (C_2(R) - 2C_F)/2 is "
                "the QCD one-gluon colour factor. The SU(N) braiding "
                "q^(-1/N) sigma has exponents exactly 2c_R, giving ratio "
                "(N+1)/(N-1) = 2 at N = 3 with correct signs. The factor "
                "q^(-1/N) is forced, not fitted: in gl_N the monodromy of V "
                "around the q-antisymmetric line Lambda^N_q is q^2 (explicit "
                "Jimbo matrices N=2,3; Young contents all N), and requiring "
                "the colour singlet to braid trivially gives c^(2N) q^2 = 1, "
                "c = q^(-1/N). This is also the e = e_max/3 value already "
                "recorded by the level-3 probe A6. It does not repair the "
                "nuclear ratio (sl_2 gives 3, not 33.7).")
            wb.add_data("symbolic", {k: str(v) for k, v in r1.items()})
            wb.add_data("forcing", {k: {kk: str(vv) for kk, vv in v.items()}
                                    for k, v in b2res.items()})
            wb.add_data("forcing_general_N", {k: str(v) for k, v in rc.items()})
            wb.add_data("arms_at_q0", {
                f"{arm}_{N}": {"L_sym": mp.nstr(nums[N][arm][0], 20),
                               "L_anti": mp.nstr(nums[N][arm][1], 20),
                               "ratio": mp.nstr(nums[N][arm][2], 20)}
                for N in (2, 3) for arm in ("gl", "sl")})
            for n, p, d in A:
                wb.add_assertion(name=n, computed=str(int(bool(p))),
                                 expected="1", tolerance=0, source=str(d))
            wb.add_caveat(
                "Applying the SU(N) frame to colour observables is a "
                "modelling ruling (bean qou-sl3f), not established here. "
                "Rescaling sigma multiplies an unnormalised Markov trace of a "
                "word by c^writhe and shifts the Markov parameter z -> c z; "
                "it must not be applied to already-ruled gl/convention-D "
                "observables without an owner decision.")
            wb.add_caveat(
                "The identification of the two-strand Wedderburn blocks with "
                "3bar and 6 is inherited from level_three_colour_channel_probe "
                "and is not constructed here.")
            print(f"\nWitness: {wb.save()}")
        except Exception as e:  # pragma: no cover
            print(f"\n(witness emit skipped: {e})")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
