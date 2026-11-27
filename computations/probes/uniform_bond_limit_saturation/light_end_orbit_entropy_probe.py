#!/usr/bin/env python3
"""
light_end_orbit_entropy_probe.py -- why the uniform bond limit over-binds light nuclei.

QUESTION (coordinator relay of the owner, 2026-11-27): find a derived reason for the light-end
over-binding of rule (3inf) (2H 4.1x, 3H 1.9x) and say which bond carries a non-vanishing exponent.

DERIVATION (q = 1, exact). At q = 1 the vertex V(s) = s_s s_{s+1}^-1 is the 3-cycle on strands
s, s+1, s+2, the free word x = prod_a V(3a)^3 is the identity, and the normalised Markov trace on
(C^2)^n is Tr/2^n. The uniform average over words in a vertex set W converges to the projector onto
the vectors fixed by the group G_W the 3-cycles generate, so
        r_cl = #orbits(G_W on {0,1}^n) / 2^n,     B_cl = E0 ln(2^n / #orbits).
This is a count of states, with no interaction strength in it. Two vertex sets:
  all       W = every vertex (rule 3inf as recorded):      G = Alt(n),      #orbits = n + 1
  junction  W = the junction vertices only (bonds between nucleons): G = Alt on strands 1..n-2,
            strands 0 and n-1 free,                          #orbits = 4 (n - 1)
The orbit counts are computed here by closing the group and counting orbits, not assumed (K1, K2).

So B_cl grows like E0 n ln 2 for both: about 2.93 MeV per strand, minus a log. At A = 2 that is already
9.36 MeV (all) and 4.92 MeV (junction), against AME 2.22. The q-deformation changes it by only 2-3 %
(K3, K4). The over-binding is the state-count entropy of the projection, not a bond.

WHICH BOND CARRIES A NON-VANISHING EXPONENT. By QOU.MassTheory.ClassicalLogBindingCycleCount the q = 1
log binding of a single bond word is E0 ln 2 (c_free - c_atom), with c the cycle count. V^3 = id at q = 1,
so the ruled gamma-gamma bond has exponent 0 (and binds only at O(y^4), audit 2026-11-27-gg-binding-
mass-chart). A bond word has a non-zero exponent iff its q = 1 permutation merges cycles; the quantum is
E0 ln 2 = 2.930 MeV, and one 3-cycle across a junction merges three cycles (2 quanta, 5.86 MeV). AME 2H
is 0.759 quanta (comparison only), so no single bond word gives 2H at q = 1.

Scope (a). Nothing fitted; AME only in comparison columns. Decays are not re-scored: no derived binding
comes out of this.
"""
import sys
from itertools import product
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
COMP = HERE.parents[1]
sys.path[:0] = [str(COMP / "substrate"), str(COMP)]
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
except ImportError:  # pragma: no cover
    WitnessBuilder = None

mp.mp.dps = 50
q = mp.mpf(Q_50_DIGIT_STR)
E0 = mp.mpf("4.2274833556")
LT1 = mp.mpf("-0.0014388708415464")  # ln tr(x) per nucleon, from uniform_bond_limit_saturation witness
AME = {2: mp.mpf("2.224566"), 3: mp.mpf("8.481798")}  # comparison only
# junction-only uniform limit at q0, power average to L = 1024, produced by junction_uniform_limit_q0.py
# (same directory; A = 2 about 1 min, A = 3 about 10 min) on the bond_rules_length_bound representation
JUNC_Q0 = {2: mp.mpf("4.822697666"), 3: mp.mpf("11.39945146")}


def three_cycle(n, s):
    p = list(range(n))
    p[s], p[s + 1], p[s + 2] = s + 1, s + 2, s
    return tuple(p)


def orbits(n, gens):
    seen, count = set(), 0
    for v in product((0, 1), repeat=n):
        if v in seen:
            continue
        count += 1
        stack = [v]
        seen.add(v)
        while stack:
            u = stack.pop()
            for g in gens:
                w = tuple(u[g[i]] for i in range(n))
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
    return count


def vertex_sets(A):
    n = 3 * A
    allv = list(range(n - 2))
    junc = sorted({s for j in range(1, A) for s in (3 * j - 2, 3 * j - 1)})
    return n, allv, junc


def qi(n):
    return (q**n - q**-n) / (q - 1 / q)


def main() -> int:
    checks, rows = {}, {}
    for A in (2, 3, 4, 5):
        n, allv, junc = vertex_sets(A)
        oa = orbits(n, [three_cycle(n, s) for s in allv])
        oj = orbits(n, [three_cycle(n, s) for s in junc])
        checks[f"K1_all_orbits_eq_n_plus_1_A{A}"] = oa == n + 1
        checks[f"K2_junction_orbits_eq_4(n-1)_A{A}"] = oj == 4 * (n - 1)
        b_all = E0 * mp.log(mp.mpf(2) ** n / oa)
        b_junc = E0 * mp.log(mp.mpf(2) ** n / oj)
        b_all_q0 = E0 * (A * LT1 - mp.log(qi(n + 1)) + n * mp.log(qi(2)))
        row = {"n": n, "orbits_all": oa, "orbits_junction": oj,
               "B_cl_all_MeV": mp.nstr(b_all, 10), "B_q0_all_MeV": mp.nstr(b_all_q0, 10),
               "q0_over_cl_all": mp.nstr(b_all_q0 / b_all, 8), "B_cl_junction_MeV": mp.nstr(b_junc, 10)}
        if A in JUNC_Q0:
            row["B_q0_junction_MeV"] = mp.nstr(JUNC_Q0[A], 10)
            row["q0_over_cl_junction"] = mp.nstr(JUNC_Q0[A] / b_junc, 8)
            checks[f"K4_junction_deformation_under_5pct_A{A}"] = abs(JUNC_Q0[A] / b_junc - 1) < mp.mpf("0.05")
        if A in AME:
            row["AME_MeV"] = mp.nstr(AME[A], 10)
        checks[f"K3_all_deformation_under_5pct_A{A}"] = abs(b_all_q0 / b_all - 1) < mp.mpf("0.05")
        rows[str(A)] = row
        print(A, row)
    quantum = E0 * mp.log(2)
    checks["K5_gg_vertex_cubed_is_identity_at_q1"] = all(
        tuple(three_cycle(6, s)[three_cycle(6, s)[three_cycle(6, s)[i]]] for i in range(6)) == tuple(range(6))
        for s in range(4))
    print("E0 ln2 =", mp.nstr(quantum, 10), " 2H AME / quantum =", mp.nstr(AME[2] / quantum, 6))
    for k, v in checks.items():
        print(("PASS " if v else "FAIL ") + k)
    if WitnessBuilder is not None:
        wb = WitnessBuilder("light-end-orbit-entropy", engine="mpmath")
        wb.set_description("Uniform bond limits are q=1 orbit-count entropy E0 ln(2^n/#orbits); the q-deformation "
                           "moves them 2-3 %. Classical exponent quantum E0 ln2 per merged cycle. AME comparison only.")
        for k, v in checks.items():
            wb.add_assertion(k, computed=str(bool(v)), expected="True", tolerance="0")
        wb.add_data("rows", rows)
        wb.add_data("classical_quantum_E0_ln2_MeV", mp.nstr(quantum, 15))
        wb.add_data("AME_2H_in_quanta_comparison_only", mp.nstr(AME[2] / quantum, 10))
        wb.save()
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
