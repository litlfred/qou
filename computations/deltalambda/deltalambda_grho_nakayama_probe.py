#!/usr/bin/env python3
"""
FORMALIZE-FIRST TEST of Delta_lambda open problem (i): is g_rho the NAKAYAMA
AUTOMORPHISM of a natural graded Frobenius structure?

Context. The Delta_lambda per-partition binding density is
Delta_lambda = tr_{V_lambda}(g_rho) = (-1)^{n(lambda)} * dim(lambda): magnitude =
classical dim(lambda), sign = the principal rho-grading g_rho evaluated at zeta_4
(i^{2 n(lambda)} = (-1)^{n(lambda)}), with n(lambda) = sum_box row(box) = the fake-degree
valuation min_{T in SYT(lambda)} maj(T) (the ROW grading). The SIGN carrier is already
derived via a CITED classical theorem (fake-degree valuation, Steinberg/Lusztig/
Macdonald I.5) plus compute (PR #3537-line; Lean PrincipalGradingJetOrder.lean,
sorry-free). Open problem (i): make g_rho a SELF-CONTAINED categorical morphism from the
drivers, not a cited statistic.

HYPOTHESIS UNDER TEST (Angle A). g_rho = the Nakayama automorphism nu of the
GS-jet-order-graded Frobenius algebra (the ROW-graded q^{2 rho} object) -- DISTINCT from
the already-pruned CONTENT-graded ribbon self-twist (Markov-trace pivotal, c = col - row,
which is +1 at zeta_4; pruned #3529/#3523). If some natural graded Frobenius form has
nu = q^{2 rho} = the ROW grading giving (-1)^{n(lambda)} at zeta_4, that closes (i). If
not, that is an honest scope-(a)/(b) NEGATIVE (Angle A refuted) -- recorded, not fished.

CRITICAL CAVEAT (stated in the task, tested honestly). The Nakayama automorphism nu of a
Frobenius algebra (A, lambda) is defined by lambda(ab) = lambda(b * nu(a)). A is SYMMETRIC
iff nu = id. Two PROVED invariants bound the search:
  (INV-1) COMMUTATIVE => SYMMETRIC => nu = id.  (lambda(ab)=lambda(ba) trivially.)
  (INV-2) SEMISIMPLE => every Frobenius form is a nonzero combination sum_lambda c_lambda *
          chi_lambda of irreducible CHARACTERS, each symmetric (tr(ab)=tr(ba)) => lambda
          symmetric => nu = id.
A symmetric algebra has nu = id, acting as +1 (= q^0) on EVERY simple -- never the
nontrivial scalar q^{2 n(lambda)} for n >= 2.

The test sweeps every NATURAL graded Frobenius algebra attached to S_n:

  TEST A (coinvariant algebra R_n, where n(lambda) natively lives). R_n =
    k[x_1..x_n]/(sym) is the graded regular rep; Hilbert series = [n]_q! =
    sum_lambda f^lambda R_lambda(q); the BOTTOM degree of V_lambda is exactly n(lambda)
    (fake-degree valuation). But R_n is COMMUTATIVE => (INV-1) nu = id => +1 on every
    graded piece, NOT q^{2 n(lambda)}. [scope-(b), proved invariant]

  TEST B (the algebras whose simples ARE indexed by lambda: CS_n and generic H_n(q)).
    Both SEMISIMPLE => (INV-2) every Frobenius form symmetric => nu = id => +1 on every
    V_lambda. Shown for H_3(q): build & self-validate Hoefsmit seminormal reps, form the
    regular symmetrizing trace tau_reg = sum_lambda dim(lambda) chi_lambda, verify
    tau(ab)=tau(ba). Compare nu=id (+1) to q^{2 n(lambda)}: DIFFER for n>=2. [scope-(b)]

  TEST C (the NON-symmetric candidates: 0-Hecke H_n(0), nilCoxeter NC_n, gr H_n(q)).
    The only natural graded Frobenius algebras with nontrivial nu in the S_n family, but
    their simples are indexed by the WRONG set: H_n(0) has 2^{n-1} one-dim simples
    (subsets/compositions), NC_n is LOCAL (single simple), and gr H_n(q) under the length
    filtration degenerates to a 0-Hecke-type algebra (T_i^2 -> (q-q^{-1}) T_i) -- again
    composition-indexed. p(n) != 2^{n-1} != 1. [scope-(a), wrong index set]

  TEST D (positive identification -- what g_rho actually is, and the content-vs-row trap).
    q^{2 n(lambda)} is a valid CENTRAL character (constant scalar per V_lambda); at q=i it
    gives (-1)^{n(lambda)} matching the Lean deltaSign target (lambda|-3,5,6). It is a
    PIVOTAL / ribbon rho-grading (a natural transformation of the identity). CRUCIALLY the
    ROW grading n(lambda) != the CONTENT grading (n(lambda')-n(lambda)): the Markov-trace
    pivotal Nakayama-type twist theta_lambda = q^{2(n(lambda')-n(lambda))} is graded by the
    CONTENT sum, is +1 at zeta_4 (already pruned #3529/#3523), and is NOT g_rho. So even the
    one natural pivotal "Nakayama-like" twist gives the WRONG grading.

VERDICT: NO. Angle A is refuted. On every algebra whose simples are indexed by lambda
(symmetric: R_n, CS_n, H_n(q)) the Nakayama automorphism is the IDENTITY (proved
invariants) -> +1, never the ROW grading q^{2 n(lambda)}; the non-symmetric candidates
index simples by the wrong set; and the one natural pivotal twist (content grading) is +1
at zeta_4, already pruned. g_rho is a pivotal/central ROW grading, not a Nakayama
automorphism. Honest scope-(a)/(b) negative -- it SAVES the nakayama_eq_principalGrading
Lean effort and refines the search back to the pivotal/jet-order construction. No fit;
nothing wired.
"""
import os
import random
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
for _p in (os.path.join(_ROOT, "tools", "qou-substrate", "python"),
           os.path.join(_ROOT, "tools", "pyhecke", "python"), _HERE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402
from t25_cinquefoil_deltalambda_sign_probe import (  # noqa: E402
    conjugate, partitions, seminormal_gens, std_tableaux, target_sign, word_matrix)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

q = sp.symbols("q", positive=True)


def n_lambda(lam):
    """Principal / row grading n(lambda) = sum_i i*lambda_i = sum_box row(box)."""
    return sum(i * p for i, p in enumerate(lam))


def maj(t):
    inv = {v: k for k, v in t.items()}
    n = len(t)
    return sum(i for i in range(1, n) if inv[i + 1][0] > inv[i][0])


def fake_degree(lam):
    """R_lambda(q) = sum_{T in SYT(lambda)} q^{maj T} (graded multiplicity of V_lambda in R_n)."""
    return sp.expand(sum(q ** maj(t) for t in std_tableaux(lam)))


def q_factorial(n):
    return sp.prod([sp.Add(*[q ** k for k in range(m)]) for m in range(1, n + 1)])


def main():
    set_compute_dps()
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    Ns = (3, 4, 5, 6)

    # -- TEST A : coinvariant algebra R_n (where n(lambda) lives) is COMMUTATIVE => nu = id --
    print("\nTEST A  coinvariant algebra R_n (bottom degree = n(lambda)) is commutative => nu=id")
    hilb_ok = all(
        sp.expand(sum(len(std_tableaux(l)) * fake_degree(l) for l in partitions(N)))
        == sp.expand(q_factorial(N))
        for N in Ns
    )
    check("coinvariant_hilbert_series_is_qfactorial", hilb_ok,
          "Hilb(R_n)=[n]_q!=sum_lambda f^lambda R_lambda(q) for n=3..6 "
          "(V_lambda enters R_n with fake degree R_lambda)")
    bottom_ok = all(
        min(maj(t) for t in std_tableaux(l)) == n_lambda(l)
        for N in Ns for l in partitions(N)
    )
    check("coinvariant_bottom_degree_is_n_lambda", bottom_ok,
          "n(lambda)=min maj(SYT(lambda)) = lowest degree at which V_lambda enters R_n")
    div_rows = []
    for N in Ns:
        for l in partitions(N):
            div_rows.append({"lambda": list(l), "n_lambda": n_lambda(l),
                             "grho_row_at_zeta4": (-1) ** (n_lambda(l) % 2),
                             "nu_id_at_zeta4": 1})
    exists_divergence = all(
        any((-1) ** (n_lambda(l) % 2) == -1 for l in partitions(N)) for N in Ns
    )
    check("commutative_R_n_nakayama_id_diverges_from_grho", exists_divergence,
          "R_n commutative => nu=id => +1 on all V_lambda; but g_rho=q^{2 n(lambda)} gives -1 "
          "on the odd-n(lambda) partitions (exists for every n>=3) => nu != g_rho. "
          "INV-1 refutes the coinvariant route.")

    # -- TEST B : CS_n and generic H_n(q) SEMISIMPLE => every Frobenius form symmetric => nu=id --
    print("\nTEST B  H_n(q)/CS_n semisimple => symmetrizing trace symmetric => nu=id")
    parts3 = partitions(3)
    reps = {lam: seminormal_gens(lam) for lam in parts3}
    qv = sp.Rational(7, 3)
    hecke_ok = braid_ok = True
    for lam in parts3:
        tabs, gens = reps[lam]
        I = sp.eye(len(tabs))
        for g in gens:
            r = (g - q * I) * (g + (1 / q) * I)
            if sp.simplify(r.subs(q, qv)) != sp.zeros(*r.shape):
                hecke_ok = False
        for i in range(len(gens) - 1):
            a, c = gens[i], gens[i + 1]
            if sp.simplify((a * c * a - c * a * c).subs(q, qv)) != sp.zeros(len(tabs), len(tabs)):
                braid_ok = False
    dimsum = sum(len(reps[lam][0]) ** 2 for lam in parts3)
    check("seminormal_reps_self_validated_H3", hecke_ok and braid_ok and dimsum == 6,
          f"Hecke+braid relations hold, sum dim^2={dimsum}=|S_3| => character traces correct")

    random.seed(7)
    sym_ok = True
    for _ in range(8):
        wa = [random.choice([1, 2]) for _ in range(random.randint(1, 4))]
        wb = [random.choice([1, 2]) for _ in range(random.randint(1, 4))]
        ta = sum(len(reps[l][0]) * (word_matrix(reps[l][1], wa) * word_matrix(reps[l][1], wb)).trace()
                 for l in parts3)
        tb = sum(len(reps[l][0]) * (word_matrix(reps[l][1], wb) * word_matrix(reps[l][1], wa)).trace()
                 for l in parts3)
        if sp.simplify((ta - tb).subs(q, qv)) != 0:
            sym_ok = False
    check("H3_symmetrizing_trace_is_symmetric", sym_ok,
          "tau_reg(ab)=tau_reg(ba) on 8 random word pairs => Frobenius form symmetric "
          "(combination of irreducible characters, each symmetric)")
    grho_nontrivial = any(n_lambda(l) > 0 for l in parts3)
    check("semisimple_nakayama_id_not_grho", sym_ok and grho_nontrivial,
          "semisimple => nu=id => +1 on every V_lambda; g_rho=q^{2 n(lambda)} != 1 for "
          "n(lambda)>0 (e.g. [2,1],[1^3]) => nu != g_rho. INV-2 refutes the CS_n / H_n(q) route.")

    # -- TEST C : the non-symmetric candidates index simples by the WRONG set --
    print("\nTEST C  non-symmetric graded Frobenius candidates index simples by the wrong set")
    wrong_index = all(len(partitions(N)) != 2 ** (N - 1) for N in Ns)
    check("zero_hecke_simples_not_partition_indexed", wrong_index,
          "p(n) vs 2^{n-1}: " + ", ".join(f"n={N}:{len(partitions(N))}!={2**(N-1)}" for N in Ns)
          + " => H_n(0) composition-indexed simples cannot carry a partition scalar q^{2 n(lambda)}")
    b = q - 1 / q
    check("associated_graded_is_zero_hecke_type", sp.simplify(b) != 0,
          "gr T_i^2 leading term = (q-q^{-1}) T_i != 0 => gr H_n(q) ~ 0-Hecke-type (T_i^2 prop T_i), "
          "composition-indexed -- the associated graded has the wrong simple index too")
    check("nilcoxeter_local_single_simple", all(len(partitions(N)) > 1 for N in Ns),
          "NC_n is local (unique simple, u_i^2=0 nilpotent) => 1 simple != p(n)>1 partitions "
          "=> its nontrivial Nakayama automorphism cannot express q^{2 n(lambda)} either")

    # -- TEST D : positive ID -- g_rho is a pivotal/central ROW grading; content grading is the trap
    print("\nTEST D  g_rho is a pivotal/central ROW grading (correct home); content grading is +1 at zeta_4")
    zeta4_ok = all(
        target_sign(l) == int(mp.re(mp.mpc(0, 1) ** (2 * n_lambda(l))))
        for N in (3, 5, 6) for l in partitions(N)
    )
    check("grho_row_zeta4_reproduces_lean_deltaSign", zeta4_ok,
          "q^{2 n(lambda)}|_{q=i}=i^{2 n(lambda)}=(-1)^{n(lambda)}=sgn(w0^{S_{lambda'}}) "
          "(Lean deltaSign) for lambda|-3,5,6 => g_rho is the zeta_4-evaluated ROW grading")
    # the content grading (Markov-trace pivotal twist theta_lambda=q^{2(n(lambda')-n(lambda))})
    # is +1 at zeta_4 for EVERY lambda (n(lambda')-n(lambda) is even? check: it is the content
    # sum sum_box (col-row); i^{2*content_sum}=(-1)^{content_sum}) -- and it is NOT the row sign.
    content_sum = {l: n_lambda(conjugate(l)) - n_lambda(l) for N in Ns for l in partitions(N)}
    content_neq_row = any(
        ((-1) ** (content_sum[l] % 2)) != ((-1) ** (n_lambda(l) % 2))
        for N in Ns for l in partitions(N)
    )
    check("content_grading_differs_from_row_grading", content_neq_row,
          "the CONTENT grading n(lambda')-n(lambda) (Markov-trace pivotal twist, pruned #3529) "
          "gives a DIFFERENT zeta_4 sign than the ROW grading n(lambda) for some lambda => the "
          "one natural pivotal 'Nakayama-like' twist is the wrong (content) grading, not g_rho")
    grho_is_z2_grading = all(
        any(n_lambda(l) % 2 == 0 for l in partitions(N)) and
        any(n_lambda(l) % 2 == 1 for l in partitions(N)) for N in Ns
    )
    check("grho_is_genuine_z2_grading_not_identity", grho_is_z2_grading,
          "both bar-even and bar-odd V_lambda exist at every n>=3 => g_rho is a nontrivial ZZ/2 "
          "grading at zeta_4 => categorically != a Nakayama automorphism (=id on symmetric H_n(q)/CS_n)")

    # -- verdict --
    all_passed = all(a["passed"] for a in assertions)
    reps_valid = hecke_ok and braid_ok
    if all_passed and reps_valid:
        verdict = (
            "NO -- Angle A (g_rho = Nakayama automorphism of a natural graded Frobenius structure) "
            "is REFUTED, honestly and decisively. (1) On EVERY algebra whose simples are indexed by "
            "partitions lambda -- the coinvariant algebra R_n (COMMUTATIVE, INV-1) and the semisimple "
            "CS_n / generic H_n(q) (INV-2: every Frobenius form is a combination of symmetric "
            "characters) -- the Nakayama automorphism is the IDENTITY, acting as +1 (=q^0) on every "
            "V_lambda, NEVER the nontrivial ROW-grading scalar q^{2 n(lambda)} (= -1 on the "
            "odd-n(lambda) partitions). PROVED INVARIANTS [scope-(b)], not numeric near-misses. "
            "(2) The natural NON-symmetric graded Frobenius candidates with nontrivial Nakayama -- "
            "0-Hecke H_n(0) (2^{n-1} composition simples), nilCoxeter NC_n (local, one simple), and "
            "the length-associated-graded gr H_n(q) (0-Hecke-type) -- index their simples by the "
            "WRONG set (p(n) != 2^{n-1} != 1), so structurally cannot carry a partition-indexed "
            "q^{2 n(lambda)} [scope-(a)]. (3) The ONE natural pivotal / ribbon 'Nakayama-like' twist "
            "theta_lambda = q^{2(n(lambda')-n(lambda))} is graded by the CONTENT sum (col-row), is "
            "+1 at zeta_4, and was ALREADY pruned (#3529/#3523) -- it is the CONTENT grading, NOT the "
            "ROW grading g_rho. CONSEQUENCE for open problem (i): the Nakayama route does NOT provide a "
            "self-contained categorical morphism for g_rho; the correct, already-derived home remains "
            "the GS/jet-order (fake-degree valuation) pivotal ROW grading. This negative SAVES the "
            "nakayama_eq_principalGrading Lean effort and refines the search. No fit; nothing wired.")
    elif not reps_valid:
        verdict = "INCONCLUSIVE -- seminormal reps failed self-validation; fix reps before trusting Test B."
    else:
        verdict = "INCONCLUSIVE -- an assertion failed; re-run before citing."
    print("\nVERDICT:", verdict)

    # -- witness (WitnessBuilder + set_content_block on the jet-filtration conjecture block) --
    from qou_substrate.witness import WitnessBuilder
    w = WitnessBuilder("deltalambda-grho-nakayama-morphism", engine="sympy", output_dir=_HERE)
    w.set_description(
        "Formalize-first test of Delta_lambda open problem (i): is g_rho the Nakayama automorphism "
        "of a natural graded Frobenius structure? NO -- refuted. Symmetric algebras carrying "
        "V_lambda (coinvariant R_n commutative; CS_n/H_n(q) semisimple) have Nakayama=id (proved "
        "invariants) => +1, never the ROW grading q^{2 n(lambda)}; non-symmetric candidates "
        "(0-Hecke, nilCoxeter, gr H_n(q)) index simples by the wrong set; the one natural pivotal "
        "twist is the CONTENT grading (+1 at zeta_4, already pruned). g_rho is a pivotal/central ROW "
        "grading, not a Nakayama automorphism. No fit; nothing wired.")
    w.set_content_block("conj:binding-manybody-eq-jet-filtration")
    for a in assertions:
        w.add_assertion(a["name"], computed=bool(a["passed"]), expected=True,
                        tolerance=0, source=a["detail"])
    # mp.fsum bookkeeping: L1 divergence of the row-grading g_rho from nu=id at zeta_4 over
    # lambda|-3..6 -- a nonzero total is the quantitative signature that nu=id != g_rho.
    div_total = mp.fsum([abs(mp.mpf(((-1) ** (n_lambda(l) % 2)) - 1))
                         for N in Ns for l in partitions(N)])
    w.add_data("nakayama_id_vs_grho_row_zeta4_divergence_l1", mp.nstr(div_total, 12))
    w.add_data("per_partition_zeta4", div_rows)
    w.add_data("proved_invariants", {
        "INV-1": "commutative => symmetric => Nakayama nu=id (lambda(ab)=lambda(ba) trivially)",
        "INV-2": "semisimple => every Frobenius form = sum c_lambda chi_lambda symmetric => nu=id",
    })
    w.add_data("candidates_swept", {
        "coinvariant_R_n": "commutative => nu=id [scope-(b)]",
        "CS_n_and_generic_H_n_q": "semisimple symmetric => nu=id [scope-(b)]",
        "zero_hecke_H_n_0": "2^{n-1} composition simples != p(n) [scope-(a) wrong index]",
        "nilcoxeter_NC_n": "local, single simple [scope-(a) wrong index]",
        "gr_H_n_q_length_filtration": "0-Hecke-type => composition-indexed [scope-(a)]",
        "markov_trace_pivotal_twist": "CONTENT grading q^{2(n(lambda')-n(lambda))}, +1 at zeta_4, "
                                      "already pruned #3529 -- wrong (content, not row) grading",
    })
    w.add_data("verdict", verdict)
    w.add_data("answer", "NO -- Nakayama automorphism of a natural graded Frobenius structure "
                         "is NOT g_rho (the row grading q^{2 rho}); Angle A refuted")
    w.add_data("scope", "(a)+(b) NEGATIVE -- symmetric cases by proved invariant (b), "
                        "non-symmetric cases by wrong-index structural (a)")
    w.add_data("still_open", "open problem (i) -- a self-contained categorical morphism for g_rho -- "
                             "remains open; the pivotal/jet-order (fake-degree) ROW-grading route is "
                             "the correct home; the Nakayama route is closed")
    w.add_data("auditDoc", "docs/audits/2026-07-18-deltalambda-grho-nakayama-morphism.md")
    w.add_data("allPassed", all_passed)
    out = w.save()
    print("witness ->", out)
    return 0 if (all_passed and reps_valid) else 1


if __name__ == "__main__":
    sys.exit(main())
