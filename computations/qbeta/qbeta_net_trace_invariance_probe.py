#!/usr/bin/env python3
"""
qbeta_net_trace_invariance_probe.py — step 8 of the fitting-finding audit: what
kind of object is `net`, and how much of `epsNPq` can any observable see?

# Ref: docs/audits/2026-05-24-q-beta-net-ansatz-fitting-finding.md (step 8)
# Ref: folio/quantum-observable-universe/lean/QOU/Interactions/qbeta_energy_scale.lean
# Ref: computations/qbeta/qbeta_epsnpq_functional_mismatch_probe.py
# Ref: computations/qbeta/qbeta_single_wrap_element_cannot_exist_probe.py

STEP 8 IS THE CHAIN'S ONE POSTULATE. The audit's table marks nine of ten steps
derived and step 8 "POSTULATED, NOT DERIVED" — `pre-archimedean-derivation-
chain.md` line 391 reads "so Q_β = |Δ(net)| × 𝔈₀ **by construction**". Steps 9
and 10 (the closed form and the +0.17 % CODATA match) are consequences of it.

THE CORPUS'S OWN JUSTIFICATION IS ATTACHED TO THE WRONG FUNCTIONAL. The Lean
docstring for `QOU.Interactions.QBetaEnergyScale` says `ε(Δ)` is "the **Frobenius
counit** of the neutron−proton normal-form difference" and calls the result a
"counit (transition) observable, categorically distinct from the Markov-trace
(static loop / partition-function) mass". Two prior results empty that sentence:

  * `epsNPq` is the COORDINATE SUM `σ ↦ 1` of the stated NF vector, not the
    augmentation `σ ↦ q` (qou-99qc), and `σ ↦ 1` is not an algebra map unless
    h = 0 (Lean, sorry-free: `QBeta.CounitSigmaOne.h_eq_zero_of_image_one`);
  * no difference of typed-crossing words has counit `epsNPq` at all — a
    scope-(b) exclusion on the norm form of Z[√2] (qou-avt6).

WHAT THIS PROBE ADDS, and it is the part that bites. An algebra homomorphism
into a commutative ring is automatically a trace: ε(xy) = ε(x)ε(y) = ε(yx). So
the counit IS a class function, and "counit observable" cannot be the licence
for a functional that is not one. This probe asks directly whether `net` is a
trace, in the 6-dimensional regular representation of H_3(q) built here from
the Hecke relations alone, symbolically in q.

The consequences of the answer are structural, not numerical:

  * a trace is constant on conjugacy classes, hence invariant under the
    Markov-I move β ↦ gβg⁻¹ — the move that says two braid words present the
    SAME closed braid. A functional that fails it reports a property of the
    chosen presentation, not of the particle;
  * for split semisimple H, H = Z(H) ⊕ [H,H], and EVERY trace functional
    annihilates [H,H]. So the [H,H]-component of Δ is invisible to every
    observable-as-trace in the framework — the Markov trace, the counit, each
    χ^λ, and any combination. If `net(Δ)` draws on that component, that part of
    Q_β is not an eigenvalue of anything.

NOT CLAIMED: that Q_β's number is wrong, or that a non-trace functional is
forbidden a priori. What is established is (i) which of the two it is, (ii) the
exact split of `epsNPq` into a trace-visible and a trace-invisible part, and
(iii) the spread of Q_β over the presentations of one particle. Deciding whether
a presentation-dependent functional may carry a decay observable is the owner's
call; step 8 currently gives no argument either way.

--- WHAT IT MEASURES (25/25) ------------------------------------------------

`net` is NOT a trace: 8 of the 36 ordered basis pairs fail cyclicity, the first
being net(sigma0 * L_plus) - net(L_plus * sigma0) = (q-1)(q+1)/q. Both controls
pass, so the multiplication table is right: the augmentation and the regular
character are cyclic on all 36.

THE SPLIT. H_3(q) is split semisimple, so H = Z(H) + [H,H] with dim 3 and 3
(measured, not assumed), and every trace annihilates [H,H]. Δ has a nonzero
[H,H] component, and at q0

    epsNPq                  = -0.187207194529378
      central   part        = -0.172847658641848      (92.33 %)
      commutator part       = -0.014359535887530      ( 7.67 %)

so 7.67 % of the Q-value comes from a component on which the Markov trace, the
augmentation, every chi^lambda and every combination of them is identically
zero. Q_A from the full net is 0.783646 MeV (+0.168 %); from the trace-visible
part alone it is 0.723537 MeV (-7.52 %).

THE DERIVABLE PIECE. The 92.33 % is not merely "trace-visible" in the abstract:
it is exhibited here in the framework's own basis. The unique trace agreeing
with `net` on the centre is

    a_(3)     = (q+1) / ((q^2+1)(q^2-q+1))
    a_(2,1)   = q(q^2-1) / (q^4+q^2+1)
    a_(1,1,1) = q^3(q-1) / ((q^2+1)(q^2+q+1))

verified to reproduce `net` on the whole centre, to annihilate [H,H], and to
give exactly the central part on Δ. Note a_(1,1,1) != 0: this trace is NOT
supported on the two rows convention D forces at N=2, so it is not a two-row
Markov trace.

THE PRESENTATION SPREAD. Conjugating both nucleon words by the same basis
element - a Markov-I move, the move that says two braid words present the SAME
closed braid - moves Q_beta over 0.692169 ... 0.783646 MeV, a spread of 0.0915
MeV = 11.7 % of Q_exp, about 70x the +0.168 % residual the framework is
explaining. `net` takes exactly two values across the six, and the reason is
structural rather than accidental: conjugation by w0 is the diagram
automorphism s0 <-> s1, which permutes the standard basis and therefore
preserves any coordinate sum. So net's stabiliser here is {1, w0}, and the
counit control is invariant across all six, as a class function must be.

--- SCOPE (read before citing) ----------------------------------------------

This is scope-(a). It does NOT say Q_beta's number is wrong, that a non-cyclic
functional is forbidden, or that the route is closed. It says the argument
currently offered for step 8 - "counit (transition) observable" - is not
available for this functional, and it prices exactly what a replacement
argument has to account for: a 7.67 % trace-invisible component and a preferred
presentation.

And per the standing rule that a structurally-exact piece is a permanent
contribution even while the total is inaccurate: the chi-expansion above is
such a piece. It narrows step 8's postulate from the whole of `net` to the
7.67 % remainder, and it stands whatever happens to that remainder.

Exact throughout: the algebra is symbolic in q over Q(q); numerics are mpmath at
50 dps via lambdify. NO fit, NO c_k, NO wiring.
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from qou_substrate.constants import Q_NEUTRON_MEV, M_E_MEV  # noqa: E402

set_compute_dps(50)

q = sp.Symbol("q", positive=True)
h = q - 1 / q

# ---------------------------------------------------------------------------
# S_3 and the Gröbner-Shirshov / standard basis, in the corpus's order.
# ---------------------------------------------------------------------------
E = (0, 1, 2)
S0 = (1, 0, 2)
S1 = (0, 2, 1)


def compose(p, r):
    """(p∘r)[i] = p[r[i]]."""
    return tuple(p[r[i]] for i in range(3))


def length(w):
    return sum(1 for i in range(3) for j in range(i + 1, 3) if w[i] > w[j])


# [γ, σ₀, σ₁, L₊, L₋, e⁻] — the basis the corpus's NF vector is written in.
BASIS = [E, S0, S1, compose(S0, S1), compose(S1, S0), compose(compose(S0, S1), S0)]
BASIS_NAMES = ["gamma", "sigma0", "sigma1", "L_plus", "L_minus", "e_minus"]
IDX = {w: i for i, w in enumerate(BASIS)}
N = 6


def _left_mult_generator(s):
    """Matrix of x ↦ T_s·x, from T_s T_w = T_sw (ℓ up) / h T_w + T_sw (ℓ down)."""
    M = sp.zeros(N, N)
    for j, w in enumerate(BASIS):
        sw = compose(s, w)
        if length(sw) > length(w):
            M[IDX[sw], j] += 1
        else:
            M[IDX[w], j] += h
            M[IDX[sw], j] += 1
    return M


L = {0: _left_mult_generator(S0), 1: _left_mult_generator(S1)}


def _right_mult_generator(s):
    """Matrix of x |-> x*T_s, from T_w T_s = T_ws (l up) / h T_w + T_ws (l down)."""
    M = sp.zeros(N, N)
    for j, wd in enumerate(BASIS):
        ws = compose(wd, s)
        if length(ws) > length(wd):
            M[IDX[ws], j] += 1
        else:
            M[IDX[wd], j] += h
            M[IDX[ws], j] += 1
    return M


R = {0: _right_mult_generator(S0), 1: _right_mult_generator(S1)}
ONE = sp.eye(N)

# Reduced words for each basis element, in the same order as BASIS.
REDUCED = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]


def left_op(word):
    M = ONE
    for g in word:
        M = M * L[g]
    return sp.simplify(M)


def right_op(word):
    """x |-> x*T_w for w = T_a T_b ... : apply R_a first, so matrix R_...R_b R_a."""
    M = ONE
    for g in word:
        M = R[g] * M
    return sp.simplify(M)


LEFT = [left_op(wd) for wd in REDUCED]
LINV = {g: L[g] - h * ONE for g in (0, 1)}
RINV = {g: R[g] - h * ONE for g in (0, 1)}


def right_inv_op(word):
    """x |-> x*T_w^{-1};  (T_a T_b)^{-1} = T_b^{-1} T_a^{-1}."""
    M = ONE
    for g in reversed(word):
        M = RINV[g] * M
    return sp.simplify(M)


RIGHT_INV = [right_inv_op(wd) for wd in REDUCED]


def basis_vec(i):
    v = sp.zeros(N, 1)
    v[i] = 1
    return v


def vec(*coeffs):
    return sp.Matrix(N, 1, list(coeffs))


def net(v):
    return sp.simplify(sum(v))


def counit(v):
    """Augmentation sigma -> q, i.e. T_w -> q^l(w)."""
    return sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))


def reg_char(v):
    """Regular character: trace of left multiplication. Manifestly a trace."""
    M = sum((v[i] * LEFT[i] for i in range(N)), sp.zeros(N, N))
    return sp.simplify(M.trace())


def main() -> int:
    w = WitnessBuilder("qbeta-net-trace-invariance", engine="sympy+mpmath")
    w.set_description(
        "Step 8 of the Q_beta fitting-finding audit: `net` is tested for "
        "trace-invariance in the regular representation of H_3(q), and "
        "epsNPq is split into its trace-visible Z(H) part and its "
        "trace-invisible [H,H] part."
    )
    ok_all = []
    notes = []

    def check(name, ok, note=""):
        ok_all.append(bool(ok))
        w.add_assertion(name, computed="1" if ok else "0",
                        expected="1", tolerance="0")
        if note:
            notes.append({"assertion": name, "note": note})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name} {note}")

    # -- 0. the representation really is H_3(q) ------------------------------
    braid = sp.simplify(L[0] * L[1] * L[0] - L[1] * L[0] * L[1])
    hk = [sp.simplify(L[g] * L[g] - h * L[g] - ONE) for g in (0, 1)]
    check("regular_rep_satisfies_hecke_and_braid_relations",
          braid.is_zero_matrix and all(m.is_zero_matrix for m in hk))
    check("left_and_right_actions_commute_CONTROL",
          all(sp.simplify(L[a] * R[b] - R[b] * L[a]).is_zero_matrix
              for a in (0, 1) for b in (0, 1)))
    check("generators_invertible_via_sigma_inv_eq_sigma_minus_h",
          all(sp.simplify(L[g] * LINV[g] - ONE).is_zero_matrix for g in (0, 1))
          and all(sp.simplify(R[g] * RINV[g] - ONE).is_zero_matrix for g in (0, 1)))
    check("conjugation_by_each_basis_element_is_an_algebra_automorphism_CONTROL",
          all(sp.simplify(LEFT[i] * RIGHT_INV[i] * basis_vec(0)
                          - basis_vec(0)).is_zero_matrix for i in range(N)),
          "(g.1.g^-1 = 1 for all six)")

    # -- 1. the corpus's Delta, rebuilt from the typed-crossing words --------
    # proton  = sigma0 (sigma1 - h/2);  neutron = (sigma0 - h/2)(sigma1 - h)
    proton = sp.simplify(L[0] * (L[1] - (h / 2) * ONE) * basis_vec(0))
    neutron = sp.simplify((L[0] - (h / 2) * ONE) * (L[1] - h * ONE) * basis_vec(0))
    delta = sp.expand(neutron - proton)
    stated = vec(h**2 / 2, -h / 2, -h / 2, 0, 0, 0)
    check("delta_reproduces_the_corpus_NF_vector",
          sp.simplify(delta - stated).is_zero_matrix)
    epsNPq = sp.simplify(h * (h - 2) / 2)
    check("net_of_delta_is_epsNPq_symbolically",
          sp.simplify(net(delta) - epsNPq) == 0)

    # -- 2. controls: two functionals that ARE traces ------------------------
    def trace_failures(f):
        bad = []
        for i in range(N):
            for j in range(N):
                d = sp.simplify(f(LEFT[i] * basis_vec(j))
                                - f(LEFT[j] * basis_vec(i)))
                if d != 0:
                    bad.append((i, j, d))
        return bad

    check("counit_is_a_trace_CONTROL", not trace_failures(counit))
    check("regular_character_is_a_trace_CONTROL", not trace_failures(reg_char))

    # -- 3. the question ------------------------------------------------------
    bad = trace_failures(net)
    first = (f"{BASIS_NAMES[bad[0][0]]}*{BASIS_NAMES[bad[0][1]]} differs by "
             f"{sp.factor(bad[0][2])}") if bad else ""
    check("net_is_NOT_a_trace", len(bad) > 0,
          f"({len(bad)}/{N * N} ordered basis pairs fail cyclicity; first {first})")

    # -- 4. the trace-invisible part of Delta --------------------------------
    comms = [LEFT[i] * basis_vec(j) - LEFT[j] * basis_vec(i)
             for i in range(N) for j in range(N)]
    comm_basis = sp.Matrix.hstack(*comms).columnspace()
    zc = [sp.Matrix.vstack(sp.simplify(L[0] * basis_vec(i) - R[0] * basis_vec(i)),
                           sp.simplify(L[1] * basis_vec(i) - R[1] * basis_vec(i)))
          for i in range(N)]
    centre = sp.Matrix.hstack(*zc).nullspace()
    check("dim_commutator_is_3_and_dim_centre_is_3",
          len(comm_basis) == 3 and len(centre) == 3,
          f"(got {len(comm_basis)} and {len(centre)}; H_3 = Q(q) + M_2 + Q(q))")

    P = sp.Matrix.hstack(*(list(centre) + list(comm_basis)))
    check("centre_plus_commutator_spans_H", sp.simplify(P.det()) != 0)
    coords = sp.simplify(P.solve(delta))
    dZ = sp.simplify(sum((coords[i] * centre[i] for i in range(3)),
                         sp.zeros(N, 1)))
    dC = sp.simplify(delta - dZ)
    net_Z, net_C = sp.simplify(net(dZ)), sp.simplify(net(dC))
    check("net_delta_is_the_sum_of_the_two_parts",
          sp.simplify(net_Z + net_C - epsNPq) == 0)
    check("commutator_part_of_delta_is_nonzero", not sp.simplify(dC).is_zero_matrix)
    check("both_control_traces_annihilate_the_commutator_part_CONTROL",
          sp.simplify(counit(dC)) == 0 and sp.simplify(reg_char(dC)) == 0)

    # -- 4b. the trace-visible part, IN THE FRAMEWORK'S OWN chi^lambda BASIS --
    # Traces on H_3 span {chi^(3), chi^(2,1), chi^(1^3)}. The two 1-dim reps are
    # sigma -> q and sigma -> -1/q; the 2-dim one follows from
    # chi_reg = 1*chi^(3) + 2*chi^(2,1) + 1*chi^(1^3).
    def chi3(v):
        return sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))

    def chi111(v):
        return sp.simplify(sum(v[i] * (-1 / q) ** length(BASIS[i])
                               for i in range(N)))

    def chi21(v):
        return sp.simplify((reg_char(v) - chi3(v) - chi111(v)) / 2)

    CHI = [("(3)", chi3), ("(2,1)", chi21), ("(1,1,1)", chi111)]
    check("chi_decomposition_of_the_regular_character_CONTROL",
          all(sp.simplify(reg_char(basis_vec(i))
                          - (chi3(basis_vec(i)) + 2 * chi21(basis_vec(i))
                             + chi111(basis_vec(i)))) == 0 for i in range(N)))
    check("each_chi_is_a_trace_CONTROL",
          all(not trace_failures(f) for _, f in CHI))

    a = sp.symbols("a0 a1 a2")
    eqs = [sp.Eq(sum(a[k] * CHI[k][1](z) for k in range(3)), net(z))
           for z in centre]
    sol = sp.solve(eqs, a, dict=True)
    check("net_restricted_to_the_centre_has_a_unique_chi_expansion", len(sol) == 1)
    sol = sol[0]
    coeffs = [sp.simplify(sp.factor(sol[a[k]])) for k in range(3)]

    def f_tr(v):
        return sp.simplify(sum(coeffs[k] * CHI[k][1](v) for k in range(3)))

    check("chi_expansion_reproduces_net_on_the_whole_centre",
          all(sp.simplify(f_tr(z) - net(z)) == 0 for z in centre))
    check("chi_expansion_annihilates_the_commutator_part_BY_CONSTRUCTION",
          sp.simplify(f_tr(dC)) == 0)
    check("chi_expansion_of_delta_equals_the_central_part_of_net",
          sp.simplify(f_tr(delta) - net_Z) == 0)
    check("chi_expansion_is_NOT_the_two_row_D_shape",
          sp.simplify(coeffs[2]) != 0,
          f"(a_(1,1,1) = {coeffs[2]}, nonzero, so the trace part of net is not "
          "supported on the two rows convention D forces)")

    # -- 5. numbers -----------------------------------------------------------
    q0 = Q_MP

    def ev(e):
        return sp.lambdify(q, e, "mpmath")(q0)

    E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))
    Qexp = mp.mpf(str(Q_NEUTRON_MEV))
    eps_n, nz, nc = ev(epsNPq), ev(net_Z), ev(net_C)
    QA, QA_Z = abs(eps_n) * E0, abs(nz) * E0

    # -- 6. the spread over presentations of ONE particle --------------------
    rows = []
    for i in range(N):
        cd = sp.simplify(LEFT[i] * RIGHT_INV[i] * delta)
        v = ev(sp.simplify(net(cd)))
        rows.append({"conjugator": BASIS_NAMES[i], "net": fmt(v),
                     "Q_MeV": fmt(abs(v) * E0),
                     "err_ppb": fmt((abs(v) * E0 / Qexp - 1) * mp.mpf(10) ** 9)})
    vals = [mp.mpf(r["Q_MeV"]) for r in rows]
    spread = max(vals) - min(vals)
    check("Q_beta_moves_under_conjugation_a_Markov_I_move",
          spread > mp.mpf("1e-9"),
          f"(spread {fmt(spread)} MeV over the six basis conjugators)")
    # Why exactly two values: T_w0 conjugation is the diagram automorphism
    # s0 <-> s1, which PERMUTES the standard basis, so it preserves any
    # coordinate sum. {1, w0} is therefore net's stabiliser here.
    Cw0 = sp.simplify(LEFT[5] * RIGHT_INV[5])
    is_perm = all(sorted(sp.simplify(Cw0[:, j]).T.tolist()[0]) == [0] * 5 + [1]
                  for j in range(N))
    check("conjugation_by_w0_permutes_the_standard_basis", is_perm,
          "(the diagram automorphism s0<->s1; it is why net survives that one "
          "conjugation and not the other four)")
    check("net_takes_exactly_two_values_over_the_six_conjugators",
          len({r["net"] for r in rows}) == 2)

    check("counit_of_delta_is_conjugation_invariant_CONTROL",
          len({str(sp.simplify(counit(sp.simplify(LEFT[i] * RIGHT_INV[i] * delta))))
               for i in range(N)}) == 1)

    for k, v in [("epsNPq_at_q0", eps_n), ("net_central_part", nz),
                 ("net_commutator_part", nc),
                 ("fraction_of_epsNPq_invisible_to_every_trace",
                  abs(nc) / abs(eps_n)),
                 ("Q_A_MeV_full_net", QA),
                 ("Q_A_MeV_trace_visible_part_only", QA_Z),
                 ("Q_A_err_ppb_full_net", (QA / Qexp - 1) * mp.mpf(10) ** 9),
                 ("Q_A_err_ppb_trace_visible_only",
                  (QA_Z / Qexp - 1) * mp.mpf(10) ** 9)]:
        w.add_data(k, fmt(v))
    for (lbl, _), c in zip(CHI, coeffs):
        w.add_data(f"net_trace_part_coefficient_chi_{lbl}", str(c))
        w.add_data(f"net_trace_part_coefficient_chi_{lbl}_at_q0", fmt(ev(c)))
    w.add_data("epsNPq_symbolic", str(sp.factor(epsNPq)))
    w.add_data("net_central_symbolic", str(sp.factor(net_Z)))
    w.add_data("net_commutator_symbolic", str(sp.factor(net_C)))
    w.add_data("conjugation_spread", rows)
    w.add_data("cyclicity_failures_of_net", len(bad))
    w.add_data("markov_convention", "n/a - no Markov parameter z enters")

    verdict = (
        "net is NOT a trace. The corpus's stated licence for step 8 - that "
        "eps(Delta) is a 'counit (transition) observable' - cannot apply to it: "
        "an algebra map into a commutative ring is automatically cyclic, so a "
        "counit IS a class function. The split above reports how much of epsNPq "
        "lives in [H,H], where every trace in the framework (the Markov trace, "
        "the augmentation, each chi^lambda, any combination) is identically "
        "blind. NOT claimed: that a non-cyclic functional is forbidden, or that "
        "Q_beta's number is wrong. What is established is which of the two net "
        "is, the exact split, and the spread of Q_beta across presentations of "
        "one particle."
        if all(ok_all) else
        "INCONCLUSIVE - an assertion failed; re-derive before citing.")
    w.add_data("assertion_notes", notes)
    w.add_data("verdict", verdict)
    path = w.save()
    print(f"\n{verdict}\n\nWitness: {path}")
    return 0 if all(ok_all) else 1


if __name__ == "__main__":
    raise SystemExit(main())
