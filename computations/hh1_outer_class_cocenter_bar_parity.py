#!/usr/bin/env python3
"""PROBE — bar-parity of the OUTER derivation class acting on the cocenter.

The decisive cheap prune for the surviving fibre-level c_3 route (bean
`qou-qb8b`; companion to PROBE A `hh1_hecke_outer_derivations.py`).

WHY THIS TEST DECIDES SOMETHING
-------------------------------
The invariant that closed every *real* c_3 route is BAR-PARITY: the swing S
is bar-ODD, while a real, trace-built Gram resolvent is bar-EVEN
(`fig8Trace_im_odd`; docs/audits/2026-07-19-c3-q0-real-routes-closed-fibre-
phase-survives.md).  The surviving carrier must therefore be bar-ODD.

Two merged sorry-free facts put the outer derivation class in the frame:
  * `CocenterTraceFactor.lean`   — the Markov trace factors through the
    cocenter HH_0 = A/[A,A];
  * `OuterDerivationResidue.lean` — every INNER derivation is trace-blind.

So the question "can the HH^1 outer class carry the bar-odd swing?" reduces
to a finite computation: read the bar-parity of the outer class's induced
action on HH_0.  Bar-EVEN kills the route to the same invariant that killed
the real resolvent.  Bar-ODD and it is the first object to clear it.

WHY THE TEST IS CANONICAL (not representative-dependent)
--------------------------------------------------------
A derivation descends to the cocenter:
    D(ab - ba) = [D(a), b] + [a, D(b)]  in  [A,A].
And an INNER derivation descends to ZERO, since ad_x(y) = xy - yx is itself
a commutator.  Hence the induced map on HH_0 depends only on the HH^1 CLASS
-- the map HH^1 -> End(HH_0) is well defined.  This is asserted below, not
assumed (assertion `inner_acts_as_zero_on_cocenter`).

CONVENTIONS (inherited from PROBE A / AGENTS.md §7a)
----------------------------------------------------
H_3(q), dim 6, basis [e, s1, s2, s1s2, s2s1, s1s2s1];
relation s_i^2 = a s_i + 1 with a = q - q^{-1}, i.e. (s-q)(s+q^{-1}) = 0;
braid s1s2s1 = s2s1s2.

Bar involution: the ring involution with bar(q) = q^{-1}, bar(s_i) = s_i^{-1}.
From s^2 = a s + 1 we get s^{-1} = s - a, and bar(a) = -a, so bar is
involutive on the generators -- checked below (`bar_is_involutive`).
Bar is SEMILINEAR: bar(lambda x) = bar(lambda) bar(x).  At a root of unity
q^{-1} = conj(q), so bar conjugates coefficients as well as moving the basis.
Getting this wrong silently produces a meaningless parity, so the semilinear
conjugation is applied explicitly and `bar_is_involutive` guards it.

HONEST SCOPE
------------
n = 3 is the MECHANISM check (its non-semisimple points are [2]_q = 0 and
[3]_q = 0, NOT the Bring [5]).  The Bring fibre is H_5 at a 5th root of
unity (bean qou-jcmw).  A clean parity here is evidence about the mechanism,
not yet the Bring-specific statement -- reported as such in the verdict.

No fit, no free parameter: an exact computation over a cyclotomic field.
"""
import json
import os

import sympy as sp

q = sp.symbols('q')
a = q - 1 / q                      # (q - q^{-1})
DIM = 6
BASIS = ['e', 's1', 's2', 's1s2', 's2s1', 's1s2s1']
WORDS = {0: [], 1: [1], 2: [2], 3: [1, 2], 4: [2, 1], 5: [1, 2, 1]}


def col(*pairs):
    v = [sp.Integer(0)] * DIM
    for idx, coeff in pairs:
        v[idx] += coeff
    return v


# Left-multiplication by the generators (columns = s_i * B_j), from PROBE A.
L1cols = [
    col((1, 1)),                # s1*e        = s1
    col((1, a), (0, 1)),        # s1*s1       = a s1 + 1
    col((3, 1)),                # s1*s2       = s1s2
    col((3, a), (2, 1)),        # s1*s1s2     = a s1s2 + s2
    col((5, 1)),                # s1*s2s1     = s1s2s1
    col((5, a), (4, 1)),        # s1*s1s2s1   = a s1s2s1 + s2s1
]
L2cols = [
    col((2, 1)),                # s2*e        = s2
    col((4, 1)),                # s2*s1       = s2s1
    col((2, a), (0, 1)),        # s2*s2       = a s2 + 1
    col((5, 1)),                # s2*s1s2     = s2s1s2 = s1s2s1
    col((4, a), (1, 1)),        # s2*s2s1     = a s2s1 + s1
    col((5, a), (3, 1)),        # s2*s1s2s1   = a s1s2s1 + s1s2
]
LGEN = {
    1: sp.Matrix.hstack(*[sp.Matrix(DIM, 1, c) for c in L1cols]),
    2: sp.Matrix.hstack(*[sp.Matrix(DIM, 1, c) for c in L2cols]),
}
I6 = sp.eye(DIM)


def left_mult_matrix(word):
    """Matrix of x -> B_word * x."""
    M = I6
    for g in reversed(word):
        M = LGEN[g] * M
    return M


LMAT = {i: left_mult_matrix(WORDS[i]) for i in range(DIM)}


def mul(u, v):
    """Product of two coordinate vectors, via bilinear extension."""
    out = sp.zeros(DIM, 1)
    for i in range(DIM):
        if u[i] == 0:
            continue
        out += u[i] * (LMAT[i] * v)
    return sp.expand(out)


def evec(i):
    return sp.Matrix(DIM, 1, [1 if k == i else 0 for k in range(DIM)])


# ── Bar involution on A ───────────────────────────────────────────────
# bar(s_i) = s_i^{-1} = s_i - a ; bar(word) = product of bar(letters).
def bar_of_basis(i):
    v = evec(0)
    for g in WORDS[i]:
        gen_inv = evec(g) - a * evec(0)     # s_g - a
        v = mul(v, gen_inv)
    return sp.expand(v)


BAR_A = sp.Matrix.hstack(*[bar_of_basis(i) for i in range(DIM)])


def bar_scalar(expr):
    """Apply q -> q^{-1} to coefficients (the semilinear part), SYMBOLICALLY.

    Only valid while the expression still carries the symbol `q`.  Once a
    matrix has been specialized to a root of unity its entries are numbers
    in Q(zeta) and this substitution is a NO-OP -- use `bar_scalar_at`.
    """
    return sp.expand(sp.simplify(expr.subs(q, 1 / q)))


def bar_scalar_at(expr):
    """Bar on Q(zeta): the Galois automorphism zeta -> zeta^{-1}.

    For |zeta| = 1 that automorphism is complex conjugation restricted to
    Q(zeta).  This is the branch that applies AFTER specialization -- the
    symbolic `q -> 1/q` substitution is a no-op on a number and silently
    returns the wrong (identity) answer, which is the bug this splits out.
    """
    return sp.expand(sp.simplify(sp.conjugate(expr)))


def bar_entries_at(M):
    return M.applyfunc(bar_scalar_at)


def bar_matrix_entries(M):
    return M.applyfunc(bar_scalar)


def bar_apply(vec):
    """Semilinear bar on a coordinate vector: BAR_A * bar(coeffs)."""
    return sp.expand(BAR_A * vec.applyfunc(bar_scalar))


# ── Cocenter HH_0 = A / [A,A] ─────────────────────────────────────────
def commutator_span(subs):
    """Column space of all [B_i, B_j], evaluated at `subs`."""
    cols = []
    for i in range(DIM):
        for j in range(DIM):
            c = LMAT[i][:, j] - LMAT[j][:, i]
            cols.append(sp.Matrix(DIM, 1, [sp.simplify(x.subs(subs)) for x in c]))
    return sp.Matrix.hstack(*cols)


def quotient_data(subs):
    """Return (P, S, dim) where P: A -> HH_0 projection, S: section HH_0 -> A.

    Complementary-coordinate construction: pick pivot rows of the commutator
    span to identify a complement, so P is projection onto the remaining
    coordinates modulo [A,A].
    """
    C = commutator_span(subs)
    # Column space basis of [A,A]
    cs = C.columnspace()
    K = sp.Matrix.hstack(*cs) if cs else sp.zeros(DIM, 0)
    k = K.shape[1]
    m = DIM - k                                   # dim HH_0
    # Choose m coordinates complementary to the row-pivots of K^T.
    rref, pivots = K.T.rref()
    comp = [i for i in range(DIM) if i not in pivots]
    assert len(comp) == m, (len(comp), m)
    # P: read off the complementary coords AFTER reducing mod [A,A].
    # Build the reduction: any v = v_K + v_comp; solve for the comp part.
    # Concretely, extend K by the complementary unit vectors to a basis of A,
    # invert, and keep the last m coordinates.
    E = sp.Matrix.hstack(K, *[evec(i) for i in comp]) if k else sp.Matrix.hstack(
        *[evec(i) for i in comp])
    Einv = E.inv()
    P = Einv[k:, :]                               # m x DIM
    S = sp.Matrix.hstack(*[evec(i) for i in comp])  # DIM x m
    return P, S, m


# ── Derivations ───────────────────────────────────────────────────────
def leibniz_equations():
    D = sp.Matrix(DIM, DIM, lambda r, c: sp.Symbol(f'd_{r}_{c}'))
    unknowns = list(D)
    eqs = []
    for i in range(DIM):
        for j in range(DIM):
            BiBj = LMAT[i][:, j]
            lhs = D * BiBj
            rhs = sp.Matrix.hstack(*[LMAT[k][:, j] for k in range(DIM)]) * D[:, i] \
                + LMAT[i] * D[:, j]
            for comp in (lhs - rhs):
                eqs.append(sp.expand(comp))
    return D, unknowns, eqs


D_SYM, UNKNOWNS, EQS = leibniz_equations()


def derivation_space(subs):
    Msys, _ = sp.linear_eq_to_matrix([sp.expand(e.subs(subs)) for e in EQS],
                                     UNKNOWNS)
    ns = sp.Matrix(Msys).nullspace()
    return ns


def inner_derivations(subs):
    """ad_x for x ranging over the basis, as DIM x DIM matrices."""
    out = []
    for i in range(DIM):
        M = sp.zeros(DIM, DIM)
        for j in range(DIM):
            c = LMAT[i][:, j] - LMAT[j][:, i]
            M[:, j] = sp.Matrix(DIM, 1, [sp.simplify(x.subs(subs)) for x in c])
        out.append(M)
    return out


def vec_to_matrix(v):
    """Nullspace vector (36 entries, ordered as list(D)) -> 6x6 matrix."""
    M = sp.zeros(DIM, DIM)
    for idx, sym in enumerate(UNKNOWNS):
        r, c = int(str(sym).split('_')[1]), int(str(sym).split('_')[2])
        M[r, c] = v[idx]
    return M


def flatten(M):
    return sp.Matrix(DIM * DIM, 1, [M[r, c] for r in range(DIM) for c in range(DIM)])


def run_point(qval, label, assertions):
    subs = {q: qval}
    print(f"\n{'=' * 68}\n{label}   (q = {qval})\n{'=' * 68}")

    P, S, mdim = quotient_data(subs)
    print(f"dim HH_0 (cocenter) = {mdim}")

    ders = derivation_space(subs)
    inns = inner_derivations(subs)
    inn_flat = [flatten(M) for M in inns]
    inn_space = sp.Matrix.hstack(*inn_flat)
    dim_inn = inn_space.rank()
    dim_der = len(ders)
    dim_hh1 = dim_der - dim_inn
    print(f"dim Der = {dim_der}   dim Inn = {dim_inn}   dim HH^1 = {dim_hh1}")

    # --- structural assertion: inner derivations act as ZERO on HH_0 ---
    for idx, M in enumerate(inns):
        induced = sp.simplify(P * M * S)
        assert induced.is_zero_matrix, (
            f"inner derivation ad_B{idx} does NOT vanish on the cocenter -- "
            "the HH^1 -> End(HH_0) map would be ill defined")
    assertions.append({
        "name": f"inner_acts_as_zero_on_cocenter[{label}]",
        "passed": True,
        "detail": ("every ad_x induces the zero map on HH_0, so the induced "
                   "action depends only on the HH^1 class (test is canonical)"),
    })
    print("assert  inner derivations act as 0 on HH_0            OK "
          "(=> induced action is class-canonical)")

    # --- bar involution sanity: bar^2 = id on A ---
    bar2 = sp.simplify(BAR_A.subs(subs) * bar_matrix_entries(BAR_A).subs(subs))
    assert sp.simplify(bar2 - I6).is_zero_matrix, "bar is not involutive on A"
    assertions.append({
        "name": f"bar_is_involutive[{label}]", "passed": True,
        "detail": "BAR_A * bar(BAR_A) = I on A (semilinear involution verified)",
    })
    print("assert  bar^2 = id on A                               OK")

    if dim_hh1 == 0:
        print("HH^1 = 0 -> no outer class here; nothing to read.")
        return {"label": label, "dim_HH0": int(mdim), "dim_HH1": 0,
                "outer_action_on_cocenter": None, "bar_parity": "n/a (no outer class)"}

    # --- pick an outer representative: a derivation not in the inner span ---
    outer = None
    for v in ders:
        M = vec_to_matrix(v)
        test = sp.Matrix.hstack(inn_space, flatten(M))
        if test.rank() > dim_inn:
            outer = M
            break
    assert outer is not None, "dim HH^1 > 0 but no outer representative found"

    # --- induced action on the cocenter ---
    Delta = sp.simplify(P * outer * S)
    print(f"\ninduced action of the outer class on HH_0 (Delta):")
    sp.pprint(Delta)

    if Delta.is_zero_matrix:
        print("\nDelta = 0: the outer class acts TRIVIALLY on the cocenter.")
        return {"label": label, "dim_HH0": int(mdim), "dim_HH1": int(dim_hh1),
                "outer_action_on_cocenter": "zero",
                "bar_parity": "n/a (trivial action)"}

    # --- bar on HH_0, with an involutivity GUARD ------------------------
    # bar descends because it is an algebra automorphism (preserves [A,A]).
    Mbar = sp.simplify(P * BAR_A.subs(subs) * S)
    # beta(v) = Mbar * bar(v)  is semilinear; beta^2 = id  <=>  Mbar*bar(Mbar)=I.
    invol = sp.simplify(Mbar * bar_entries_at(Mbar))
    assert sp.simplify(invol - sp.eye(mdim)).is_zero_matrix, (
        "bar does NOT descend to an involution on HH_0 -- the parity readout "
        f"would be meaningless. Mbar*bar(Mbar) =\n{invol}")
    assertions.append({
        "name": f"bar_involutive_on_cocenter[{label}]", "passed": True,
        "detail": "Mbar * bar(Mbar) = I on HH_0 (guards the semilinear branch)",
    })
    print("assert  bar^2 = id on HH_0                            OK")

    def conjugate_action(Dl):
        """Delta^bar = Mbar * bar(Delta) * bar(Mbar)  (semilinear conjugation)."""
        return sp.simplify(Mbar * bar_entries_at(Dl) * bar_entries_at(Mbar))

    Delta_bar = conjugate_action(Delta)
    even = sp.simplify(Delta_bar - Delta).is_zero_matrix
    odd = sp.simplify(Delta_bar + Delta).is_zero_matrix
    raw_parity = "bar-EVEN" if even else ("bar-ODD" if odd else "neither")
    print(f"\nbar-conjugated action (Delta^bar):")
    sp.pprint(Delta_bar)
    print(f"\nraw parity of THIS representative: {raw_parity}")

    # --- is Delta^bar PROPORTIONAL to Delta?  (the scale-invariant question) --
    lam = None
    for r in range(mdim):
        for c in range(mdim):
            if sp.simplify(Delta[r, c]) != 0:
                lam = sp.simplify(Delta_bar[r, c] / Delta[r, c])
                break
        if lam is not None:
            break
    proportional = sp.simplify(Delta_bar - lam * Delta).is_zero_matrix
    print(f"Delta^bar proportional to Delta? {proportional}"
          + (f"   (lambda = {sp.simplify(lam)})" if proportional else ""))

    if proportional:
        # beta^2 = id forces the norm condition lambda*bar(lambda) = 1.  That is
        # exactly the Hilbert-90 hypothesis for the quadratic extension
        # Q(zeta)/Q(zeta)^+ (the bar-fixed field), whose H^1 vanishes -- so
        # lambda = bar(c)/c is ALWAYS solvable and the parity is always
        # normalizable away.  Checked, not asserted from theory.
        norm = sp.simplify(lam * bar_scalar_at(lam))
        assert sp.simplify(norm - 1) == 0, f"lambda*bar(lambda) = {norm} != 1"
        assertions.append({
            "name": f"lambda_has_norm_one[{label}]", "passed": True,
            "detail": ("lambda*bar(lambda) = 1 -- the Hilbert-90 hypothesis for "
                       "Q(zeta)/Q(zeta)^+, so lambda = bar(c)/c is solvable and "
                       "the parity is a choice of normalization, not an invariant"),
        })
        print(f"assert  lambda*bar(lambda) = 1 (Hilbert-90 hypothesis)  OK")

    # --- self-check: Delta is well defined up to a scalar --------------------
    # dim HH^1 = 1, so any two outer representatives differ by (scalar)*outer
    # + inner; inner dies on HH_0, so every outer rep must give a Delta
    # PROPORTIONAL to this one.  Verified against a genuinely different rep.
    # Build genuinely different representatives of the SAME class by adding
    # each inner derivation; every one must reproduce Delta EXACTLY.  (An
    # earlier version searched the nullspace basis for a second outer vector
    # and silently found none -- dim HH^1 = 1 -- making the check vacuous.)
    n_alt = 0
    for idx, Minn in enumerate(inns):
        cand = sp.simplify(P * (outer + Minn) * S)
        assert sp.simplify(cand - Delta).is_zero_matrix, (
            f"outer + ad_B{idx} gave a DIFFERENT action on HH_0 -- the "
            "class-canonicity argument would be broken")
        n_alt += 1
    assert n_alt > 0, "class-canonicity self-check did not run"
    assertions.append({
        "name": f"delta_is_class_canonical[{label}]", "passed": True,
        "detail": (f"{n_alt} alternative representatives (outer + ad_x for each "
                   "basis x) all reproduce Delta exactly"),
    })
    print(f"assert  {n_alt} alt. representatives reproduce Delta      OK")

    # --- NORMALIZATION-DEPENDENCE: rescale D by a bar-ODD scalar -------------
    # The outer class is defined only up to a nonzero scalar c.  Under D -> cD,
    # Delta -> c*Delta and Delta^bar -> bar(c)*Delta^bar, so the parity is
    # multiplied by bar(c)/c.  Choosing c bar-ODD (bar(c) = -c) FLIPS it.
    # zeta - zeta^{-1} is bar-odd by construction; verified, not assumed.
    c_odd = sp.simplify(qval - 1 / qval)
    c_odd_is_bar_odd = sp.simplify(bar_scalar_at(c_odd) + c_odd) == 0
    flip_note = None
    if c_odd != 0 and c_odd_is_bar_odd:
        Delta_scaled = sp.simplify(c_odd * Delta)
        Delta_scaled_bar = conjugate_action(Delta_scaled)
        s_even = sp.simplify(Delta_scaled_bar - Delta_scaled).is_zero_matrix
        s_odd = sp.simplify(Delta_scaled_bar + Delta_scaled).is_zero_matrix
        scaled_parity = "bar-EVEN" if s_even else ("bar-ODD" if s_odd else "neither")
        flipped = (raw_parity in ("bar-EVEN", "bar-ODD")
                   and scaled_parity in ("bar-EVEN", "bar-ODD")
                   and scaled_parity != raw_parity)
        flip_note = {"scaling_scalar": sp.sstr(c_odd),
                     "scalar_is_bar_odd": True,
                     "parity_after_rescale": scaled_parity,
                     "parity_flipped_by_rescaling": bool(flipped)}
        print(f"rescale by bar-ODD c = {c_odd}: parity becomes {scaled_parity}"
              f"   -> flipped: {flipped}")

    return {"label": label, "dim_HH0": int(mdim), "dim_HH1": int(dim_hh1),
            "outer_action_on_cocenter": sp.sstr(Delta),
            "bar_conjugated": sp.sstr(Delta_bar),
            "raw_parity_of_representative": raw_parity,
            "bar_conjugate_proportional_to_delta": bool(proportional),
            "proportionality_lambda": sp.sstr(sp.simplify(lam)) if proportional else None,
            "normalization_dependence": flip_note,
            "bar_parity": raw_parity}


def main():
    print("bar-parity of the OUTER derivation class acting on the cocenter")
    print("H_3(q) mechanism check -- bean qou-qb8b\n")
    assertions = []
    results = []
    # Exact rectangular forms: `conjugate` (the zeta -> zeta^{-1} Galois map at
    # |zeta| = 1) must evaluate cleanly, which exp(I*pi/3) does not always do.
    z6 = sp.Rational(1, 2) + sp.sqrt(3) / 2 * sp.I          # primitive 6th root
    for zz, nm in ((sp.I, "q = i"), (z6, "q = zeta_6")):
        assert sp.simplify(sp.Abs(zz) - 1) == 0, f"{nm} is not on the unit circle"
        assert sp.simplify(sp.conjugate(zz) - 1 / zz) == 0, \
            f"{nm}: conjugation != zeta -> zeta^-1 (bar branch invalid)"
    assert sp.simplify(sp.I + 1 / sp.I) == 0, "[2]_q != 0 at q = i"
    assert sp.simplify(z6**2 + 1 + z6**-2) == 0, "[3]_q != 0 at q = zeta_6"
    assertions.append({
        "name": "root_of_unity_points_valid", "passed": True,
        "detail": ("q=i has [2]_q=0, q=zeta_6 has [3]_q=0; both on the unit "
                   "circle with conjugate(z) = z^{-1}, so the bar branch is valid"),
    })
    print("assert  root-of-unity points valid, bar branch sound   OK")

    results.append(run_point(sp.I, "q = i        ([2]_q = 0)", assertions))
    results.append(run_point(z6, "q = zeta_6   ([3]_q = 0)", assertions))
    results.append(run_point(sp.Integer(2), "q = 2        (semisimple control)",
                             assertions))

    parities = {r["label"]: r["bar_parity"] for r in results}
    print(f"\n{'=' * 68}\nSUMMARY\n{'=' * 68}")
    for k, v in parities.items():
        print(f"  {k:32s} {v}")

    witness = {
        "schema": "qou-probe/v1",
        "probe": "bar-parity of the HH^1 outer class acting on the cocenter",
        "bean": "qou-qb8b",
        "algebra": "H_3(q) Iwahori-Hecke, dim 6",
        "description": (
            "Reads the bar-parity of the induced action of the HH^1 outer "
            "derivation class on the cocenter HH_0 = A/[A,A]. The action is "
            "class-canonical because inner derivations induce zero on HH_0 "
            "(asserted). Bar-EVEN kills the fibre-level c_3 carrier route to "
            "the same bar-parity invariant that closed the real Gram-resolvent "
            "route; bar-ODD would clear that obstruction."),
        "method": ("exact cyclotomic linear algebra; Der = nullspace of Leibniz "
                   "constraints, Inn = span of ad_x, cocenter by complementary "
                   "coordinates; bar applied SEMILINEARLY "
                   "(Delta^bar = M bar(Delta) bar(M)). No fit."),
        "assertions": assertions,
        "allPassed": all(x["passed"] for x in assertions),
        "results": results,
        "verdict": (
            "THE PROPOSED PRUNE DOES NOT EXIST. The bar-parity of the HH^1 "
            "outer class acting on HH_0 is NOT an invariant of the class: it "
            "is a choice of normalization. Delta^bar is proportional to Delta "
            "at both root-of-unity points (lambda = +1 at q=i, lambda = -1 at "
            "q=zeta_6), and lambda*bar(lambda) = 1 -- the Hilbert-90 hypothesis "
            "for Q(zeta)/Q(zeta)^+ -- so lambda = bar(c)/c is always solvable. "
            "Demonstrated constructively rather than argued: rescaling the "
            "representative by a bar-ODD scalar FLIPS the parity at both "
            "points (bar-EVEN -> bar-ODD at q=i; bar-ODD -> bar-EVEN at "
            "q=zeta_6). CONSEQUENCE: bar-parity cannot prune the fibre-level "
            "c_3 carrier the way it pruned the real Gram resolvent. The route "
            "is NOT killed -- and NOT confirmed either. A finer invariant, or "
            "a construction that PINS the normalization, is required."),
        "scope": (
            "scope-(a). This is a negative result about the TEST, not about the "
            "route: it shows the bar-parity readout carries no information for "
            "an un-normalized class. It does NOT exclude the HH^1 carrier. "
            "n=3 is the MECHANISM check: its non-semisimple points are [2]_q=0 "
            "and [3]_q=0, NOT the Bring [5]. The Bring fibre is H_5 at a 5th "
            "root of unity (bean qou-jcmw). The normalization-dependence "
            "argument is field-theoretic (Hilbert 90 over Q(zeta)/Q(zeta)^+) "
            "and does not depend on n, so it is expected to carry to H_5 -- "
            "which is why the expensive dim-120 H_5 parity computation should "
            "NOT be run expecting a prune."),
        "why_the_real_route_pruned_but_this_does_not": (
            "The real Gram resolvent lived over R, where bar acts trivially, so "
            "its parity was rigid and the bar-odd target S was genuinely "
            "unreachable. At a root of unity bar acts as the nontrivial Galois "
            "map zeta -> zeta^{-1}, and Q(zeta) CONTAINS bar-odd scalars (e.g. "
            "zeta - zeta^{-1}), so both parities are always available. That is "
            "precisely why the fibre-level route survived the real-route "
            "exclusion chain in the first place."),
    }
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "hh1-outer-class-cocenter-bar-parity.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    print(f"\nwitness -> {out}")


if __name__ == "__main__":
    main()
