#!/usr/bin/env python3
"""Structure of the q-Collatz backward tree at a primitive cube root of unity.

Supplies the computational half of the argument in
content/quantum-observable-universe/lean/QOU/AppendixSurreals/collatz_block_descent.lean
(section "The unit obstruction"), which explains — rather than merely records —
why no two chained odd-preimages appear in the backward tree, i.e. why no v = 0
block occurs there.

The Lean side proves the ENGINE, over a generic CommRing:
  * an odd-preimage forces P(w) = -w, which is a UNIT;
  * the even branch-inverse multiplies P(w) by the unit (w+1);
  * hence a non-unit evaluation blocks odd-preimages through the whole
    even-subtree, permanently.

This probe supplies the three ARITHMETIC inputs that engine is applied to, none
of which is proved in Lean:

  A. (w+1) has multiplicative ORDER 6 -- the source of the "6" in the observed
     congruence. Along the main even chain the evaluation returns to -w exactly
     at n = 0 (mod 6).
  B. The coupled recursion (u,v) -> ((w+1)u, u + (w+1)v) has closed form
     v_n = a^n v_0 + n a^(n-1) u_0   with a = w+1,
     checked against the real chain, and it produces exactly the observed
     P'(w) = (-6k, -6k-1).
  C. The odd-preimage taken at the n = 6k node lands on an evaluation of NORM
     1 + 6k + 12k^2, which is 1 only for k = 0 (k = 0 returns q^-1, already on
     the chain). So every k >= 1 branch is non-unit, and the Lean engine applies.

Exact arithmetic: Laurent polynomials over Z, and Z[w] as pairs (x,y) = x + y*w
with w^2 = -1 - w. No float.

SCOPE. This does not prove the tree-level conclusion. A and B are verified over
the stated finite ranges; C is verified for k = 0..10. And even a full proof
would settle v = 0 for the backward TREE only -- the step to all of D_inf is the
convergence conjecture itself (qcz7 A1).

Exploratory research probe (NOT canonical production).
"""
import sys, json, importlib.util
from pathlib import Path  # witness path must be FILE-relative, not cwd-relative

try:  # P30 provenance stamp; optional so a bare container still runs
    from qou_substrate.witness import WitnessBuilder as _WitnessBuilder
except ImportError:  # pragma: no cover
    from witness_base import WitnessBuilder as _WitnessBuilder

_spec = importlib.util.spec_from_file_location(
    "_vz", __file__.replace("backward_tree_structure_probe", "vzero_block_probe"))
_vz = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_vz)

ALPHA = (1, 1)      # w + 1
NEG_W = (0, -1)


def norm(a):
    x, y = a
    return x * x - x * y + y * y


def wpow_alpha(n):
    r = (1, 0)
    for _ in range(n):
        r = _vz.wmul(r, ALPHA)
    return r


def order_of_alpha(limit=24):
    r = (1, 0)
    for i in range(1, limit + 1):
        r = _vz.wmul(r, ALPHA)
        if r == (1, 0):
            return i
    return None


def closed_form_v(n, u0, v0):
    """v_n = alpha^n v0 + n alpha^(n-1) u0."""
    an = wpow_alpha(n)
    t1 = _vz.wmul(an, v0)
    if n == 0:
        return t1
    anm1 = wpow_alpha(n - 1)
    t2 = _vz.wmul(anm1, u0)
    return (t1[0] + n * t2[0], t1[1] + n * t2[1])


def run(chain_len=25, kmax=10, branch_depth=30):
    # A. order of alpha
    order = order_of_alpha()

    # B. closed form against the real even chain from 1+q^-1
    u0, v0 = _vz.at_omega(_vz.ATTR_B), _vz.deriv_at_omega(_vz.ATTR_B)
    P = dict(_vz.ATTR_B)
    closed_ok, odd_positions, odd_vs = True, [], []
    for n in range(chain_len):
        u, v = _vz.at_omega(P), _vz.deriv_at_omega(P)
        if v != closed_form_v(n, u0, v0):
            closed_ok = False
        if u == NEG_W:
            odd_positions.append(n)
            odd_vs.append(list(v))
        P = _vz.even_preimage(P)

    # C. norm of the odd-preimage taken at n = 6k, and the branch induction
    norms, branch_ok = [], True
    P = dict(_vz.ATTR_B)
    for n in range(6 * kmax + 1):
        if n % 6 == 0:
            k = n // 6
            Q = _vz.odd_preimage(P)
            if Q is None:
                branch_ok = False
                break
            nq = norm(_vz.at_omega(Q))
            norms.append(dict(k=k, norm=nq, predicted=1 + 6 * k + 12 * k * k,
                              matches=(nq == 1 + 6 * k + 12 * k * k)))
            if k >= 1:
                R = dict(Q)
                for _ in range(branch_depth):
                    if norm(_vz.at_omega(R)) != nq:
                        branch_ok = False
                    if _vz.at_omega(R) == NEG_W:
                        branch_ok = False
                    if _vz.odd_preimage(R) is not None:
                        branch_ok = False
                    R = _vz.even_preimage(R)
        P = _vz.even_preimage(P)

    return dict(
        A_order_of_w_plus_1=order,
        A_odd_preimage_positions_on_main_chain=odd_positions,
        A_all_positions_divisible_by_6=all(n % 6 == 0 for n in odd_positions),
        B_closed_form_matches_chain=closed_ok,
        B_observed_v_at_those_positions=odd_vs,
        C_branch_norms=norms,
        C_norm_formula_holds=all(r['matches'] for r in norms),
        C_norm_one_only_at=[r['k'] for r in norms if r['norm'] == 1],
        C_k_ge_1_branches_never_admit_a_further_odd_preimage=branch_ok,
    )


if __name__ == '__main__':
    r = run()
    print(json.dumps(r, indent=2))
    assert r['A_order_of_w_plus_1'] == 6
    assert r['A_all_positions_divisible_by_6']
    assert r['B_closed_form_matches_chain']
    assert r['C_norm_formula_holds']
    assert r['C_norm_one_only_at'] == [0]
    assert r['C_k_ge_1_branches_never_admit_a_further_odd_preimage']
    print("\nall structural assertions hold")
    w = {
        'schema': 'qou-probe/v0',
        'description': ('Backward-tree structure of the q-Collatz map at a '
                        'primitive cube root of unity: order of w+1, the closed '
                        'form for the coupled (P(w), P\'(w)) recursion, and the '
                        'norm 1+6k+12k^2 of the odd-preimage branches. Supplies '
                        'the arithmetic inputs to the unit obstruction proved in '
                        'collatz_block_descent.lean. Exact Z and Z[w] arithmetic. '
                        'Exploratory research probe (NOT canonical production).'),
        'result': r,
    }
    with open(Path(__file__).with_name('qcollatz_backward_tree_structure_probe.witness.json'), 'w') as f:
        w["q0Anchor"] = "independent"
        # P30: add the staleness provenance (scriptHash / commitSha /
        # engine) that a hand-rolled dump cannot get from build().
        # The q0Anchor lines just below own the anchor decision and run
        # after this, so their value stands.
        _WitnessBuilder.stamp_staleness_metadata(
            w, script_path=__file__, engine="python")
        w["q0AnchorReason"] = "No substrate pin enters this computation: neither the producer nor its transitive import cone inside computations/ references q_at, q_muon_at, Q_50_DIGIT_STR, q_parameter or resolve_q0_anchor outside comments (AST import-cone walk, 2026-09-03). The probe computes: Structure of the q-Collatz backward tree at a primitive cube root of unity."
        json.dump(w, f, indent=2)
    print("wrote qcollatz_backward_tree_structure_probe.witness.json")
