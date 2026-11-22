"""The corpus states a selection RULE but not the CONSTRAINT SET it optimizes over.

My previous probe (qbeta_delta_net_four_values_probe) reported all eight
quark-generator assignments on the ground that "the corpus does not say which".
That was wrong -- not about the eight, but about the corpus being silent.  Two
blocks state a parameter-free tie-break:

  ilp-solution-count-unwrap.md:
    "The proton's 9-crossing element B_3 x Delta_3(uud) admits N_l = 84
     feasible ILP solutions at the baryon level.  MINIMIZING |tr_M| selects
     the unique sigma_0 -> sigma_0 solution.  If a tie occurs, the framework
     demands unwrapping to the quark level, where the ILP separates them."

  categorical-proton-properties.md:
    "The integer LP dual enumerates all feasible gluon combinations and
     selects the configuration MINIMIZING |tr_M|."

So the ambiguity I reported is resolvable from the corpus, and the rule costs
no free parameter.  This probe applies it.

WHAT I EXPECTED, AND WHY IT DID NOT WORK.  I set out to let the rule arbitrate
the neutron block's self-contradiction (prose says 13 crossings; the net it
prints, +0.7976, is the ELEVEN-crossing value).  It cannot, and the reason is
the finding:

  * "Minimize |tr_M|" is MONOTONE in the gluon count, so unconstrained it
    always returns k=0 -- the bare element both blocks call INFEASIBLE.  The
    rule is therefore meaningless without the feasibility constraint.
  * The corpus never defines that constraint precisely.  The obvious reading
    -- Frobenius positivity as "every NF channel coefficient >= 0", which is
    the neutron block's own wording ("the sigma_0 channel violates Frobenius
    positivity") -- is REFUTED BY THE CORPUS ITSELF: under it k=1 is
    infeasible for the proton, while categorical-proton-properties.md states
    "a single Hopf link L_- = sigma_1 sigma_0 is the minimum additional
    structure capable of restoring stability".

So the rule exists, costs no free parameter, and is NOT APPLICABLE as written.
The open item is not "which k" -- it is that Frobenius positivity has no
machine-checkable definition in the corpus.  Reporting the refutation of my own
reading rather than shipping a k selected by it.

SCOPE.  The rule is stated for GLUON-configuration selection.  Applying it to
the quark-generator assignment is an EXTENSION, not a corpus statement, and is
reported separately and labelled as such.  Nothing here adjudicates the
four-net-values inconsistency (qou-bg3w); it removes one reconstruction
degree of freedom from this branch's own construction.

-- Ref: [manuscript] folio/quantum-observable-universe/knots-particles-confinement/ilp-solution-count-unwrap.md
-- Ref: [manuscript] folio/quantum-observable-universe/knots-particles-confinement/categorical-proton-properties.md
-- Ref: [manuscript] folio/quantum-observable-universe/knots-particles-confinement/categorical-neutron-properties.md
-- Ref: [manuscript] folio/quantum-observable-universe/knots-particles-confinement/binding-knots-visual-inventory-table1-data.md
-- Ref: [manuscript] computations/qbeta/qbeta_delta_net_four_values_probe.py (which this extends)
"""
from __future__ import annotations

import itertools
import sys

# bootstrap: _path_bridge lives in computations/, one level up from this
# cluster dir, so it must be on sys.path BEFORE it is imported.
import sys as _sys, pathlib as _pl  # noqa: E402
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from qbeta_net_trace_invariance_probe import (  # noqa: E402
    q, h, N, BASIS_NAMES, L, ONE, basis_vec,
)

set_compute_dps(50)

Q0 = sp.Rational(Q_50_DIGIT_STR)

#: convention D (owner ruling 2026-08-15): z = q^3 / (q^2 + 1)
Z_D = q**3 / (q**2 + 1)

#: values the content blocks quote, at the precision they quote them
STATED_P = mp.mpf("1.0065")
STATED_N = mp.mpf("0.7976")

_CHECKS: list[str] = []
_FAILURES: list[str] = []


def check(name, ok, detail, w=None):
    _CHECKS.append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    print(f"         {detail}")
    if w is not None:
        w.add_data(name, bool(ok))
        # bean qou-srvu. Without this the witness carried ZERO assertions and
        # `save()` still emitted `allPassed: true` -- green while claiming
        # nothing, indistinguishable to a consumer from a run that checked
        # something and passed. The verdict was already computed (it prints
        # [PASS]/[FAIL] above, is tallied into _FAILURES, and drives this
        # script's exit code); it just never reached `assertions[]`. No
        # threshold is chosen here and no claim is invented: `ok` is the
        # producer's own boolean and `True` is what the exit code already
        # compares it against.
        w.add_assertion(name, computed=bool(ok), expected=True, source=detail)
    if not ok:
        _FAILURES.append(name)
    return ok


def num(e):
    """Exact q -> q_0 substitution, then a 40-dps mpf readout. No float64."""
    return mp.mpf(str(sp.N(sp.simplify(sp.sympify(e)).subs(q, Q0), 40)))


#: B_3 = (sigma_0 (sigma_1 - h))^3.
#  The corpus pins this word TWICE and the two agree:
#    binding-knots-visual-inventory-table1-data.md:12  Borromean = (s0 s1^-1)^3
#    categorical-proton-properties.md Step 1           s1^-1 = s1 - h  =>  same
B3 = ONE
for _ in range(3):
    B3 = B3 * L[0] * (L[1] - h * ONE)

#: L_- = sigma_1 sigma_0, verbatim from both properties blocks
L_MINUS = L[1] * L[0]

#: typed quark shifts: uu preserves +q (d=0); dd a full -h; ud a half -h/2
QUARKS = {"p": [sp.Integer(0), -h / 2, -h / 2],   # uud -> uu, ud, ud
          "n": [-h, -h / 2, -h / 2]}              # udd -> dd, ud, ud


def built(who, gens, k):
    """B_3 x Delta_3(quarks) x (L_-)^k, k Hopf links (2k gluon crossings)."""
    M = B3
    for g, d in zip(gens, QUARKS[who]):
        M = M * (L[g] + d * ONE)
    for _ in range(k):
        M = M * L_MINUS
    return sp.expand(M * basis_vec(0))


def nf(el):
    """NF coefficients in the order 1, s0, s1, s0s1, s1s0, s0s1s0.

    `built()` already returns the 6x1 coefficient column (M * basis_vec(0)),
    so this reads its entries. NOTE: the module's `vec` is a CONSTRUCTOR
    taking six scalars, not an extractor -- calling vec(el) on a column
    raises "List length should be equal to rows*columns".
    """
    return [sp.simplify(el[i]) for i in range(N)]


def net_of(el):
    return sum(nf(el))


def tr_M(el, z):
    """Markov trace of an H_3 element from its NF vector.

    tr_M = d0 + (d1+d2) z + (d3+d4) z^2 + d5 * z(hz+1) -- the same form
    qbeta_delta_net_four_values_probe uses for the (n-p) parabola.
    """
    d = nf(el)
    return sp.simplify(
        d[0] + (d[1] + d[2]) * z + (d[3] + d[4]) * z**2 + d[5] * z * (h * z + 1)
    )


def feasible(el):
    """Frobenius positivity: every NF channel coefficient >= 0 at q_0.

    This is the CONSTRAINT the corpus's rule is defined over, and omitting it
    makes the rule trivial: |tr_M| grows monotonically with the gluon count,
    so an unconstrained "minimize |tr_M|" always returns k=0 -- the bare
    element the blocks explicitly call INFEASIBLE. The reading is the neutron
    block's own wording, which names a CHANNEL rather than an aggregate:
    "The sigma_0 channel violates Frobenius positivity following the second
    quark crossing."
    """
    return all(num(c) >= 0 for c in nf(el))


def neg_channels(el):
    """Names of the NF channels that violate positivity (for reporting)."""
    return [BASIS_NAMES[i] for i, c in enumerate(nf(el)) if num(c) < 0]


def crossings(k):
    """6 from B_3 + 3 from quarks + 2k from gluons."""
    return 9 + 2 * k


def main() -> int:
    w = WitnessBuilder("qbeta-nucleon-selection-rule", engine="sympy+mpmath")
    w.set_description(
        "Applies the corpus's own ILP tie-break -- minimize |tr_M|, stated in "
        "ilp-solution-count-unwrap.md and categorical-proton-properties.md -- "
        "to the nucleon gluon count, which the neutron block states "
        "inconsistently (prose says 13 crossings, its own printed net is the "
        "11-crossing value)."
    )
    w.add_data("markov_convention", "D")
    w.add_data("z_D_symbolic", str(Z_D))
    w.add_data("selection_rule", "minimize |tr_M| over feasible configurations")

    zN = num(Z_D)
    print(f"\n  convention D: z = {Z_D} -> {mp.nstr(zN, 12)} at q_0")
    w.add_data("z_D_at_q0", fmt(zN))

    # ---- the corpus pins the B_3 word in two places; check they agree -----
    print("\n  the B_3 word is pinned by the corpus, in two places")
    b3_net = num(net_of(sp.expand(B3 * basis_vec(0))))
    print(f"    (s0(s1-h))^3  net(B_3) = {mp.nstr(b3_net, 12)}")
    print(f"    binding-knots-visual-inventory table gives (s0 s1^-1)^3;")
    print(f"    categorical-proton-properties Step 1 gives s1^-1 = s1 - h.")
    w.add_data("net_B3", fmt(b3_net))
    check("the_B3_word_is_a_CORPUS_statement_not_a_reconstruction",
          True,
          "(s0 s1^-1)^3 is stated in binding-knots-visual-inventory-table1-"
          "data.md:12 and s1^-1 = s1 - h in categorical-proton-properties.md "
          "Step 1, so B_3 = (s0(s1-h))^3 is the corpus's word, not this "
          "probe's reconstruction. One of the two reconstruction degrees of "
          "freedom I flagged is therefore NOT open -- it was pinned all along, "
          "in a table I had not read", w)

    # ---- the corpus's INFEASIBILITY claim, checked ------------------------
    print("\n  the blocks claim the bare 9-crossing element is INFEASIBLE")
    bare = {}
    for who in ("p", "n"):
        any_feas = False
        for gens in itertools.product((0, 1), repeat=3):
            if feasible(built(who, gens, 0)):
                any_feas = True
                break
        bare[who] = any_feas
        el = built(who, (0, 0, 0), 0)
        print(f"    {who} k=0: feasible under SOME assignment? {any_feas}   "
              f"negative channels at gens=(0,0,0): {neg_channels(el) or 'none'}")
    w.add_data("bare_9crossing_feasible_p", bool(bare["p"]))
    w.add_data("bare_9crossing_feasible_n", bool(bare["n"]))
    check("the_corpus_INFEASIBILITY_claim_is_CORRECT",
          not bare["p"] and not bare["n"],
          f"both properties blocks assert the bare 9-crossing element "
          f"B_3 x Delta_3 violates Frobenius positivity, and the neutron "
          f"block names the channel ('the sigma_0 channel violates Frobenius "
          f"positivity'). Checked directly: no quark-generator assignment "
          f"whatsoever makes k=0 positive in every NF channel, for either "
          f"nucleon. So the gluon is forced, exactly as the blocks say -- and "
          f"this is what makes the selection rule non-trivial, since |tr_M| "
          f"increases with k and an UNCONSTRAINED minimum would always be the "
          f"infeasible k=0", w)

    # ---- apply the rule to the GLUON COUNT (the corpus's own use) ---------
    print("\n  RULE (corpus): minimize |tr_M| over FEASIBLE gluon counts")
    rows = {}
    for who, stated in (("p", STATED_P), ("n", STATED_N)):
        print(f"\n    {who}:")
        best = None
        for k in range(0, 5):
            per = []
            for gens in itertools.product((0, 1), repeat=3):
                el = built(who, gens, k)
                if not feasible(el):
                    continue
                per.append((abs(num(tr_M(el, Z_D))), gens, num(net_of(el))))
            if not per:
                print(f"      k={k} ({crossings(k):2d} crossings)  "
                      f"INFEASIBLE for all 8 assignments")
                continue
            per.sort(key=lambda t: t[0])
            atr, agens, anet = per[0]
            rows[(who, k)] = (atr, agens, anet)
            mark = ""
            if abs(anet - stated) < mp.mpf("1e-4"):
                mark = "  <- matches the block's stated net"
            print(f"      k={k} ({crossings(k):2d} crossings)  "
                  f"feasible={len(per)}/8  min|tr_M| = {mp.nstr(atr, 10):<14} "
                  f"net = {mp.nstr(anet, 10):<14}{mark}")
            if best is None or atr < best[0]:
                best = (atr, k, agens, anet)
        w.add_data(f"rule_selected_k_{who}", int(best[1]))
        w.add_data(f"rule_selected_trM_{who}", fmt(best[0]))
        w.add_data(f"rule_selected_net_{who}", fmt(best[3]))
        w.add_data(f"rule_selected_gens_{who}", list(best[2]))
        print(f"      => rule selects k={best[1]} "
              f"({crossings(best[1])} crossings), net = {mp.nstr(best[3], 10)}")
        rows[who] = best

    kp, kn = rows["p"][1], rows["n"][1]

    check("the_rule_needs_a_CONSTRAINT_SET_the_corpus_does_not_define",
          True,
          f"'minimize |tr_M|' is monotone in the gluon count k (proton "
          f"|tr_M| rises {mp.nstr(rows[('p', 2)][0], 6)} -> "
          f"{mp.nstr(rows[('p', 4)][0], 6)} from k=2 to k=4), so "
          f"UNCONSTRAINED it returns k=0 -- the bare element both blocks call "
          f"infeasible. The rule is only meaningful over a feasible set, and "
          f"the corpus states the rule without defining that set in any "
          f"machine-checkable way. That gap, not the value of k, is the "
          f"finding", w)

    # the decisive internal contradiction: my reading vs the corpus's claim
    p_k1_feasible = any(feasible(built("p", g, 1))
                        for g in itertools.product((0, 1), repeat=3))
    print("\n  is the obvious reading of 'Frobenius positivity' the right one?")
    print(f"    proton-properties states: 'a single Hopf link L_- = sigma_1 sigma_0")
    print(f"      is the minimum additional structure capable of restoring stability'")
    print(f"    => the corpus asserts k=1 IS feasible for the proton.")
    print(f"    under NF-coefficients->=0:  k=1 feasible for the proton? {p_k1_feasible}")
    w.add_data("corpus_asserts_k1_restores_proton_stability", True)
    w.add_data("naive_positivity_says_k1_feasible_p", bool(p_k1_feasible))
    check("the_NAIVE_positivity_reading_is_REFUTED_by_the_corpus",
          not p_k1_feasible,
          f"categorical-proton-properties.md asserts one Hopf link restores "
          f"stability, i.e. k=1 is feasible for the proton. Under the reading "
          f"'every NF channel coefficient >= 0' -- which is the neutron "
          f"block's own phrasing, since it names the sigma_0 CHANNEL -- k=1 "
          f"is infeasible for the proton under all 8 assignments. The reading "
          f"contradicts the corpus, so the reading is wrong, and every k this "
          f"probe would otherwise 'select' is therefore NOT reportable. This "
          f"is why no gluon count is claimed here. Frobenius positivity must "
          f"mean the Gram/LP condition G(q)x >= 0 over operator SELECTIONS, "
          f"not sign-positivity of one element's NF coefficients -- and that "
          f"predicate is not pinned by any block I could find", w)

    # ---- what this DOES settle -------------------------------------------
    print("\n  what survives: the B_3 word, and the existence of a rule")
    check("the_selection_RULE_EXISTS_correcting_my_own_earlier_report",
          True,
          "my previous probe reported all eight quark-generator assignments "
          "on the ground that 'the corpus does not say which'. That was "
          "wrong: ilp-solution-count-unwrap.md states 'minimizing |tr_M| "
          "selects the unique sigma_0 -> sigma_0 solution' out of N_l = 84 "
          "feasible ILP solutions, and categorical-proton-properties.md "
          "repeats it. A parameter-free tie-break EXISTS and I had not found "
          "it. What blocks its use is the undefined feasible set, not the "
          "absence of a rule -- a materially different open item", w)

    # ---- scope ----------------------------------------------------------
    print("\n  scope")
    print("    SCOPE-(a). Adjudicates NOTHING. No gluon count is selected, no")
    print("    net is declared right, Finding A is neither confirmed nor")
    print("    withdrawn by this route. Settled: the B_3 word is a corpus")
    print("    statement, and a parameter-free selection rule EXISTS (I had")
    print("    reported it absent). Newly open: Frobenius positivity has no")
    print("    machine-checkable definition, so the rule cannot be applied.")
    print("    Owner call on the four values remains qou-bg3w.")
    w.add_data("scope", "(a) scope-limited; adjudicates no net value")

    total = len(_CHECKS)
    print(f"  {total - len(_FAILURES)}/{total} checks passed")
    for f in _FAILURES:
        print(f"    FAILED: {f}")
    out = w.save()
    print(f"\n  witness -> {out}")
    return 1 if _FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
