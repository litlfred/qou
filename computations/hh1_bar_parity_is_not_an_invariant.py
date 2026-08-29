#!/usr/bin/env python3
"""PROBE A part 4 (bean `qou-jcmw`) — the bar-parity gate is VACUOUS on a
one-dimensional HH^1. Exact arithmetic over a cyclotomic field.

THE QUESTION THIS SETTLES
    Parts 1-3 found dim HH^1(H_5(zeta_5)) = 1 with the outer class acting
    nontrivially (rank 1) on the 7-dimensional cocenter, and left bar parity as
    "the decisive gate". Part 3 could only measure a sign-twisted shadow, because
    bar is semilinear and does not act on a single finite-field specialization.

    Done properly over Q(zeta), bar DOES act -- and the gate dissolves.

THE STRUCTURAL ARGUMENT (proved here, verified below)
    Over K = Q(zeta) the map  bar : T_i -> T_i - a,  a = zeta - zeta^{-1},
    together with sigma : zeta -> zeta^{-1}, is a sigma-SEMILINEAR algebra
    automorphism of A = H_n(zeta) -- it maps A to itself, unlike over F_p.
    Verified directly: applying bar to  T_i^2 - a T_i - 1  gives
    (T_i-a)^2 - sigma(a)(T_i-a) - 1 = T_i^2 - a T_i - 1 = 0, using sigma(a) = -a.

    bar preserves Der and Inn, hence acts on HH^1 sigma-semilinearly. When
    dim_K HH^1 = 1, write  [D^bar] = mu.[D].  Applying bar twice forces

        mu . sigma(mu) = 1                                    (norm one)

    and Hilbert 90 for the quadratic extension K/K^sigma gives mu = nu/sigma(nu).
    Then:
        nu.D    is bar-EVEN         (B (nu D_0) B^-1 =  nu D_0)
        a.nu.D  is bar-ODD          (B (a nu D_0) B^-1 = -a nu D_0)
    because sigma(a) = -a. BOTH parities are realised by generators of the SAME
    line.

    => Bar parity is a property of a CHOSEN GENERATOR, not of the class. On a
       one-dimensional HH^1 it carries no information and cannot prune anything.

    Two scale-invariant facts survive and are free: since B D_0 B^-1 = mu D_0 is
    a scalar multiple, im(D_0) and ker(D_0) are automatically bar-STABLE. So even
    the refined "does the outer class respect the bar-decomposition" question is
    answered yes, with no computation.

WHY H_3 IS THE VERIFICATION VEHICLE
    The argument is uniform in n -- it uses only dim HH^1 = 1, sigma(a) = -a and
    Hilbert 90. H_3 at a root of unity has dim HH^1 = 1 (merged producer) and is
    6-dimensional, so every step can be verified in EXACT Q(i) arithmetic rather
    than asserted. H_5(zeta_5) satisfies the same three hypotheses: dim HH^1 = 1
    (part 1), sigma(a) = -a (immediate, asserted below for zeta_5 too), and
    Q(zeta_5)/Q(sqrt 5) is quadratic with sigma : zeta -> zeta^{-1}.

Nothing wired, no fit. This does NOT advance c_3; it removes a proposed gate.
"""
import json
import os

import sympy as sp

# --------------------------------------------------------------------------
# H_3 over Q(i):  q = i,  a = q - q^{-1} = 2i,  sigma = complex conjugation.
# Basis [e, s1, s2, s1s2, s2s1, s1s2s1]; tables reused verbatim from the merged
# hh1_hecke_outer_derivations.py so this is a check of the ARGUMENT, not a
# re-derivation of the algebra.
# --------------------------------------------------------------------------

Q = sp.I
A_PARAM = Q - 1 / Q          # 2i
N = 6


def sigma(expr):
    """The nontrivial element of Gal(Q(i)/Q): complex conjugation."""
    return sp.conjugate(sp.expand(expr))


def sigma_mat(M):
    return M.applyfunc(sigma)


def col(*pairs):
    v = [sp.Integer(0)] * N
    for idx, coeff in pairs:
        v[idx] += coeff
    return v


a = A_PARAM
L1cols = [col((1, 1)), col((1, a), (0, 1)), col((3, 1)),
          col((3, a), (2, 1)), col((5, 1)), col((5, a), (4, 1))]
L2cols = [col((2, 1)), col((4, 1)), col((2, a), (0, 1)),
          col((5, 1)), col((4, a), (1, 1)), col((5, a), (3, 1))]
L1 = sp.Matrix.hstack(*[sp.Matrix(N, 1, c) for c in L1cols])
L2 = sp.Matrix.hstack(*[sp.Matrix(N, 1, c) for c in L2cols])
I6 = sp.eye(N)
WORDS = {0: [], 1: [1], 2: [2], 3: [1, 2], 4: [2, 1], 5: [1, 2, 1]}


def left_mult_matrix(word):
    M = I6
    for g in reversed(word):
        M = (L1 if g == 1 else L2) * M
    return sp.simplify(M)


Lmat = {i: left_mult_matrix(WORDS[i]) for i in range(N)}
Rmat = {}
for j in range(N):
    cols = []
    for i in range(N):
        ej = sp.Matrix(N, 1, [1 if k == j else 0 for k in range(N)])
        cols.append(Lmat[i] * ej)
    Rmat[j] = sp.Matrix.hstack(*cols)


def derivation_space():
    """Basis of Der(A) as 6x6 matrices (columns = D(basis element))."""
    D = sp.Matrix(N, N, lambda r, c: sp.Symbol(f'd_{r}_{c}'))
    unknowns = list(D)
    eqs = []
    for i in range(N):
        for j in range(N):
            BiBj = Rmat[j][:, i]
            lhs = D * BiBj
            rhs = Rmat[j] * D[:, i] + Lmat[i] * D[:, j]
            eqs.extend(sp.expand(x) for x in (lhs - rhs))
    Msys, _ = sp.linear_eq_to_matrix(eqs, unknowns)
    ns = sp.Matrix(Msys).nullspace()
    return [sp.Matrix(N, N, list(v)) for v in ns]


def inner_space():
    return [sp.simplify(Rmat[k] - Lmat[k]) for k in range(N)]


def flat(M):
    return sp.Matrix(N * N, 1, list(M))


def in_span(target, basis):
    """Solve target = sum c_i basis_i over Q(i); return coeffs or None."""
    if not basis:
        return None
    Amat = sp.Matrix.hstack(*[flat(b) for b in basis])
    sol = sp.linsolve((Amat, flat(target)))
    if not sol:
        return None
    return list(sol)[0]


def main():
    out = {}
    print("PROBE A part 4 — bar parity on a 1-dimensional HH^1\n")
    print(f"H_3 at q = {Q},  a = q - 1/q = {A_PARAM},  "
          f"sigma(a) = {sigma(A_PARAM)}")
    assert sp.simplify(sigma(A_PARAM) + A_PARAM) == 0
    print("  check sigma(a) = -a                                  ✓\n")

    der = derivation_space()
    inn = inner_space()
    rank_inn = sp.Matrix.hstack(*[flat(x) for x in inn]).rank()
    rank_all = sp.Matrix.hstack(*[flat(x) for x in der + inn]).rank()
    hh1 = rank_all - rank_inn
    print(f"dim Der = {len(der)}   dim Inn = {rank_inn}   dim HH^1 = {hh1}")
    assert hh1 == 1, "expected a 1-dimensional HH^1 at this root of unity"
    out["dim_Der"], out["dim_Inn"], out["dim_HH1"] = len(der), rank_inn, hh1

    # an outer derivation
    Dout = None
    for cand in der:
        r = sp.Matrix.hstack(*[flat(x) for x in inn + [cand]]).rank()
        if r > rank_inn:
            Dout = cand
            break
    assert Dout is not None
    print("outer derivation found                                 ✓")

    # ---- bar as a sigma-semilinear algebra automorphism --------------------
    # bar(T_w) = prod over the reduced word of (T_{i_j} - a); linear part M.
    Mcols = []
    for c in range(N):
        vec = sp.Matrix(N, 1, [1 if k == 0 else 0 for k in range(N)])
        # build (T_{g0}-a)(T_{g1}-a)...(T_{gk}-a) by left-multiplying from the
        # RIGHT end of the word outwards -- iterating forwards would reverse it
        for g in reversed(WORDS[c]):
            Lg = L1 if g == 1 else L2
            vec = sp.expand((Lg - a * I6) * vec)
        Mcols.append(vec)
    M = sp.Matrix.hstack(*Mcols)

    # bar = M o sigma ; involution  <=>  M . sigma(M) = I
    inv_check = sp.simplify(M * sigma_mat(M))
    print(f"bar is an involution (M.sigma(M) = I)                  "
          f"{'✓' if inv_check == I6 else '✗'}")
    assert inv_check == I6
    out["bar_is_involution"] = True

    # bar is an algebra automorphism: bar(xy) = bar(x)bar(y) on basis pairs
    ok = True
    for i in range(N):
        for j in range(N):
            lhs = M * sigma_mat(Rmat[j])[:, i]          # bar(B_i B_j)
            barBi = M[:, i]
            rhs = sum((barBi[k] * (Lmat[k] * M[:, j]) for k in range(N)),
                      sp.zeros(N, 1))
            if sp.simplify(lhs - rhs) != sp.zeros(N, 1):
                ok = False
    print(f"bar is an algebra automorphism                         "
          f"{'✓' if ok else '✗'}")
    assert ok
    out["bar_is_algebra_automorphism"] = True

    # ---- D^bar = M . sigma(D) . sigma(M) ----------------------------------
    Dbar = sp.simplify(M * sigma_mat(Dout) * sigma_mat(M))
    is_der = True
    for i in range(N):
        for j in range(N):
            BiBj = Rmat[j][:, i]
            if sp.simplify(Dbar * BiBj
                           - (Rmat[j] * Dbar[:, i] + Lmat[i] * Dbar[:, j])) \
                    != sp.zeros(N, 1):
                is_der = False
    print(f"D^bar is again a derivation                            "
          f"{'✓' if is_der else '✗'}")
    assert is_der

    # ---- solve [D^bar] = mu.[D] in HH^1 -----------------------------------
    # Solve  D^bar = mu.D + sum_k c_k . ad_{B_k}  for (mu, c_0..c_5) at once:
    # one linear system in 7 unknowns over Q(i).
    mu = sp.Symbol('mu')
    cs = sp.symbols('c0:6')
    combo = mu * Dout + sum((cs[k] * inn[k] for k in range(N)), sp.zeros(N, N))
    eqs = [sp.expand(e) for e in sp.Matrix(Dbar - combo)]
    sol = sp.solve(eqs, (mu,) + cs, dict=True)
    assert sol, "D^bar must be congruent to a multiple of D modulo Inn"
    mu_val = sp.simplify(sol[0][mu])
    print(f"\n[D^bar] = mu.[D]   with   mu = {mu_val}")
    out["mu"] = str(mu_val)

    norm = sp.simplify(mu_val * sigma(mu_val))
    print(f"norm  mu.sigma(mu) = {norm}                            "
          f"{'✓' if norm == 1 else '✗'}")
    assert norm == 1, "involution forces norm 1"
    out["norm_mu_sigma_mu"] = str(norm)

    # ---- Hilbert 90: find nu with mu = nu/sigma(nu) ------------------------
    nu = None
    for cand in (1 + mu_val, sp.I * (1 + mu_val), mu_val, sp.I):
        cand = sp.simplify(cand)
        if cand != 0 and sp.simplify(cand / sigma(cand) - mu_val) == 0:
            nu = cand
            break
    assert nu is not None, "Hilbert 90 guarantees such a nu exists"
    print(f"Hilbert 90:  mu = nu/sigma(nu)  with nu = {nu}          ✓")
    out["nu"] = str(nu)

    # ---- both parities are realised on the SAME line ----------------------
    def parity_of(scale):
        Dm = sp.expand(scale * Dout)
        Dmb = sp.simplify(M * sigma_mat(Dm) * sigma_mat(M))
        even = in_span(sp.expand(Dmb - Dm), inn) is not None
        odd = in_span(sp.expand(Dmb + Dm), inn) is not None
        return even, odd

    e1, o1 = parity_of(nu)
    e2, o2 = parity_of(sp.expand(A_PARAM * nu))
    print(f"\n  generator  nu.D      : bar-even={e1}  bar-odd={o1}")
    print(f"  generator  a.nu.D    : bar-even={e2}  bar-odd={o2}")
    out["nu_D_parity"] = {"even": bool(e1), "odd": bool(o1)}
    out["a_nu_D_parity"] = {"even": bool(e2), "odd": bool(o2)}

    both = e1 and o2
    print("\n" + "=" * 72)
    if both:
        print("VERDICT: BOTH parities are realised by generators of the SAME")
        print("one-dimensional class. Scaling by a = zeta - zeta^{-1} flips the")
        print("parity, because sigma(a) = -a. Bar parity is therefore a property")
        print("of a CHOSEN GENERATOR, not of the class -- on a 1-dimensional")
        print("HH^1 it carries no information and CANNOT prune anything.")
        print()
        print("Applied to H_5(zeta_5): dim HH^1 = 1 (part 1), sigma(a) = -a, and")
        print("Q(zeta_5)/Q(sqrt 5) is quadratic -- the same three hypotheses. So")
        print("the bar-parity gate proposed for the c_3 route is VACUOUS.")
        print()
        print("Free corollary: since B.D_0.B^-1 = mu.D_0 is a scalar multiple,")
        print("im(D_0) and ker(D_0) are automatically bar-STABLE. The refined")
        print("question is answered too, with no computation.")
    else:
        print("VERDICT: parities did NOT both appear -- the structural argument")
        print("fails somewhere; do not cite it. Investigate before using.")
    print("=" * 72)

    # ---- the hypotheses, checked for zeta_5 itself -------------------------
    # Done ALGEBRAICALLY in Q[x]/Phi_5(x) with sigma : x -> x^4 = x^{-1}.
    # (Going through exp(2*pi*I/5) leaves sympy holding an unreduced
    # conjugate(sin(2*pi/5)) and reports a spurious failure.)
    x = sp.Symbol('x')
    phi5 = sp.cyclotomic_poly(5, x)

    def red(p):
        return sp.rem(sp.expand(p), phi5, x)

    def sigma5(p):
        """sigma : zeta -> zeta^{-1} = zeta^4, then reduce mod Phi_5."""
        return red(sp.expand(p.subs(x, x ** 4)))

    a5 = x - x ** 4                       # zeta - zeta^{-1}
    holds = red(a5 + sigma5(a5)) == 0
    # and confirm sigma is an involution of order 2 on the field
    invol = red(sigma5(sigma5(x)) - x) == 0
    print(f"\nhypothesis check at zeta_5 (algebraic, in Q[x]/Phi_5):")
    print(f"    sigma(a) = -a           ->  {'holds' if holds else 'FAILS'}")
    print(f"    sigma^2 = id            ->  {'holds' if invol else 'FAILS'}")
    print(f"    Q(zeta_5)/Q(sqrt 5) quadratic, Gal = {{1, sigma}}  (standard)")
    assert holds and invol
    out["zeta5_sigma_a_eq_minus_a"] = bool(holds)
    out["zeta5_sigma_is_involution"] = bool(invol)

    witness = {
        "schema": "qou-probe/v1",
        "probe": "PROBE-A part 4: bar parity is not an invariant of a 1-dim HH^1",
        "bean": "qou-jcmw",
        "description": (
            "Exact Q(i) verification that the bar involution is a sigma-"
            "semilinear algebra automorphism, that [D^bar] = mu.[D] with "
            "mu.sigma(mu) = 1, and that Hilbert 90 plus sigma(a) = -a realise "
            "BOTH parities on generators of the same one-dimensional class. "
            "Hence the bar-parity gate cannot prune a 1-dimensional HH^1."),
        "verification_vehicle": (
            "H_3 at q = i, chosen because the argument is uniform in n (it uses "
            "only dim HH^1 = 1, sigma(a) = -a, and Hilbert 90 for a quadratic "
            "cyclotomic extension) and H_3 is small enough for exact arithmetic. "
            "All three hypotheses hold for H_5(zeta_5): dim HH^1 = 1 was computed "
            "in part 1, sigma(a) = -a is checked here for zeta_5 directly, and "
            "Q(zeta_5)/Q(sqrt 5) is quadratic."),
        "results": out,
        "verdict": (
            "The bar-parity sub-test of bean qou-jcmw is VACUOUS as posed: parity "
            "is a property of a chosen generator, not of a one-dimensional class, "
            "and both parities are realised. Scope-(b) for the GATE (invariant "
            "cited: Hilbert 90 for K/K^sigma together with sigma(a) = -a). This "
            "neither advances nor refutes the c_3 route -- it removes a proposed "
            "filter, so the route must be advanced or pruned on other grounds."),
        "wired_to_production": False,
        "fit_performed": False,
    }
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "hh1-bar-parity-not-an-invariant.witness.json")
    with open(path, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        import os as _os  # noqa: E402 -- provenance stamp
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    print(f"\nwitness -> {path}")


if __name__ == "__main__":
    main()
