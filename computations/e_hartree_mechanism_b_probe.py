#!/usr/bin/env python3
# polynomial_q_not_applicable: this is an archimedean numerical probe of the LP
# binding functional Phi_1(epsilon) at substrate q_0 (mpmath, 60 dps); the
# leading-order extraction is a finite-difference / log-log fit, intrinsically
# real-q.
"""
conj:e-hartree-categorical-derivation — MECHANISM B probe (item 1 of the owner
queue).  Tests the SINGLE remaining gap left after round 20.

THE QUESTION (block Mechanism B).  The molecular binding LP/SDP dual y_cov is
claimed to expand as y_cov(alpha) = c_2 alpha^2 + O(alpha^4) — NO linear term —
which is what makes the Hartree energy scale as alpha^2.  The gap: this needs
the separated-atom point to be a SMOOTH interior facet of the LP (dual
quadratic in the turning-on parameter), NOT a KINK (constraint activating,
generic nonzero linear term).  "This has not been verified" (block).

THE TEST (faithful to h2-molecular-binding.py, prop:h2-lp-dual-binding).
The covalent channel is the INTER-atomic EM crossing (absent in separated
atoms, present in the molecule).  Interpolate every inter-atomic crossing
toward the identity by a parameter eps in [0,1]:
    (c, d)  ->  (eps * c,  1 + eps*(d - 1)),
so eps = 0 makes all inter-atomic crossings identity (the H2 braid factorises
into the two intra-atomic dressed crossings = TWO SEPARATED ATOMS), and eps = 1
is the full molecule.  The binding functional is
    B(eps) = Phi_1(H2 ; eps)  -  Phi_1(2H separated),     B(0) = 0.
eps plays the role of the turning-on parameter (~ alpha_EM in the block).  We
extract the leading power p in B(eps) ~ A * eps^p:
    p ~ 1  =>  LINEAR term present  =>  KINK  =>  Mechanism B FAILS as stated
              (binding has an O(alpha) piece; alpha^2 leading order is not the
               LP-dual's natural scaling at the separated-atom point).
    p ~ 2  =>  no linear term       =>  SMOOTH facet  =>  Mechanism B HOLDS
              (y_cov ~ eps^2, the alpha^2 Hartree scaling is structural).

We also test ACTIVE-SET STABILITY: does the LP-optimal strand ordering at small
eps coincide with the eps = 1 optimum?  A change of optimal ordering as eps -> 0
is the combinatorial signature of a kink.

HONEST SCOPE.  This is the archimedean LP functional at q_0, not a symbolic
proof; it answers the structural question (linear vs quadratic) numerically to
high precision.  It does NOT supply the m_e c^2 unit (the other standing
transport).  No experimental comparison.

Refs: conj:e-hartree-categorical-derivation (Mechanism B); prop:h2-lp-dual-
binding; prop:operator-selection-lp; h2-molecular-binding.py (the binding
functional); e_hartree_round20_trace_ratio.py (the alpha^2 algebraic shape this
gap gates).
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE / "substrate"))
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder

import itertools
from mpmath import mp

mp.dps = 60

try:
    from q_parameter import Q as q0, Q_INV as qi, HA
except Exception:
    q0 = mp.mpf("1.1099785955573347198997632204832250266562084087802")
    qi = 1 / q0
    HA = q0 - qi

z = 1 / (mp.sqrt(q0) + mp.sqrt(qi))
HA_d = q0 ** 5 - qi ** 5          # dressed intra-atomic pe sum (eigenvalues q^5,-q^-5)

STRANDS = [('p', 1), ('e', 1), ('p', 2), ('e', 2)]


def crossing_cd(ti, tj, same_atom):
    """(c, d) for a molecular crossing; mirrors h2-molecular-binding.py."""
    a, b = ti[0], tj[0]
    if same_atom:
        if (a, b) in (('p', 'e'), ('e', 'p')):
            return mp.mpf(1), -(HA_d - HA)        # intra-atomic dressed pe
        return mp.mpf(0), mp.mpf(1)               # identity
    else:
        if (a, b) in (('p', 'p'), ('e', 'e')):
            return mp.mpf(1), mp.mpf(0)           # inter pp/ee EM repulsion
        if (a, b) in (('p', 'e'), ('e', 'p')):
            return mp.mpf(1), -HA                 # inter pe EM attraction (covalent)
        return mp.mpf(0), mp.mpf(1)


def phi1(ordering, eps):
    """Phi_1 = sum ln|V_i| with inter-atomic crossings scaled toward identity
    by eps: (c,d) -> (eps*c, 1+eps*(d-1)). Intra-atomic crossings untouched."""
    n = len(ordering)
    Phi = mp.mpf(0)
    for gen in range(n - 1):
        aa, bb = mp.mpf(0), mp.mpf(1)
        si = STRANDS[ordering[gen]]
        for j in range(gen + 1, n):
            sj = STRANDS[ordering[j]]
            same = (si[1] == sj[1])
            c, d = crossing_cd(si, sj, same)
            if c == 0 and d == 1:
                continue
            if not same:                          # turn-on knob on inter-atomic
                c = eps * c
                d = 1 + eps * (d - 1)
            aa, bb = aa * (c * HA + d) + bb * c, aa * c + bb * d
        V = z * aa + bb
        if abs(V) < mp.mpf(10) ** -290:
            return mp.inf
        Phi += mp.log(abs(V))
    return Phi


def best_ordering(eps):
    """LP-optimal (max binding ⇒ here min Phi, ground state) ordering at eps.
    Enumerate the 4!/2 = 12 distinct orderings (reversal-equivalent)."""
    seen, best, bestperm = set(), mp.inf, None
    for perm in itertools.permutations(range(4)):
        key = min(perm, tuple(reversed(perm)))
        if key in seen:
            continue
        seen.add(key)
        val = phi1(list(perm), eps)
        if val < best:
            best, bestperm = val, perm
    return bestperm, best


def main() -> None:
    w = WitnessBuilder("e-hartree-mechanism-b-probe", engine="python")

    # separated-atom reference = optimal ordering at eps -> 0 limit (eps=0 exactly)
    perm0, phi_sep = best_ordering(mp.mpf(0))
    # full molecule optimum
    perm1, phi_full = best_ordering(mp.mpf(1))
    binding_full = phi_full - phi_sep

    # B(eps) along the FULL-molecule optimal ordering (fixed active set)
    eps_grid = [mp.mpf(10) ** (-k) for k in range(1, 8)]
    rows = []
    for e in eps_grid:
        Be = phi1(list(perm1), e) - phi_sep
        rows.append((e, Be, Be / e, Be / e ** 2))

    # leading power p from log-log slope between the two smallest eps
    e1, B1 = rows[-2][0], rows[-2][1]
    e2, B2 = rows[-1][0], rows[-1][1]
    p_est = mp.log(abs(B2) / abs(B1)) / mp.log(e2 / e1)

    # ratios B/eps and B/eps^2 at the smallest eps (which stabilises?)
    B_over_eps = rows[-1][2]
    B_over_eps2 = rows[-1][3]
    # quadratic if B/eps -> 0 and B/eps^2 -> const; linear if B/eps -> const
    is_quadratic = abs(B_over_eps) < mp.mpf("1e-3") and abs(B_over_eps2) > mp.mpf("1e-6")
    is_linear = abs(B_over_eps) > mp.mpf("1e-3")

    # active-set stability: optimal ordering at small eps vs eps=1
    perm_small, _ = best_ordering(mp.mpf(10) ** -4)
    key_small = min(perm_small, tuple(reversed(perm_small)))
    key_full = min(perm1, tuple(reversed(perm1)))
    active_set_stable = (key_small == key_full)

    print("=" * 74)
    print("conj:e-hartree MECHANISM B — smooth facet vs kink at separated-atom pt")
    print("=" * 74)
    print(f"  q0 = {mp.nstr(q0, 12)}")
    print(f"  separated-atom Phi_sep (eps=0) = {mp.nstr(phi_sep, 12)}  ordering {perm0}")
    print(f"  full molecule  Phi_full (eps=1) = {mp.nstr(phi_full, 12)}  ordering {perm1}")
    print(f"  full binding B(1) = {mp.nstr(binding_full, 8)}")
    print()
    print(f"  {'eps':>10} {'B(eps)':>16} {'B/eps':>14} {'B/eps^2':>14}")
    for e, Be, r1, r2 in rows:
        print(f"  {mp.nstr(e,1):>10} {mp.nstr(Be,8):>16} {mp.nstr(r1,6):>14} {mp.nstr(r2,6):>14}")
    print()
    print(f"  leading power p (log-log, two smallest eps) = {mp.nstr(p_est, 6)}")
    print(f"  B/eps   at eps=1e-7 = {mp.nstr(B_over_eps,6)}  (-> const ⇒ LINEAR/kink)")
    print(f"  B/eps^2 at eps=1e-7 = {mp.nstr(B_over_eps2,6)}  (-> const ⇒ QUADRATIC/smooth)")
    print(f"  active-set (optimal ordering) stable as eps->0: {active_set_stable}")
    print()
    verdict = ("QUADRATIC — Mechanism B HOLDS (smooth facet; y_cov ~ eps^2, "
               "alpha^2 scaling structural)" if is_quadratic else
               "LINEAR — Mechanism B FAILS as stated (kink; binding has an "
               "O(alpha) term)" if is_linear else "INCONCLUSIVE")
    print(f"  VERDICT: {verdict}")

    w.set_description(
        "conj:e-hartree Mechanism B probe (item 1): tests the single remaining "
        "gap — is the separated-atom point a SMOOTH facet of the binding LP "
        "(dual y_cov ~ eps^2, no linear term, alpha^2 Hartree scaling "
        "structural) or a KINK (constraint activation, generic O(eps) term)?  "
        "Faithful to h2-molecular-binding.py: interpolate every inter-atomic "
        "(covalent-channel) crossing toward identity by eps in [0,1] "
        "((c,d)->(eps*c, 1+eps(d-1))), so eps=0 = two separated atoms, eps=1 = "
        "molecule; B(eps)=Phi_1(H2;eps)-Phi_1(2H).  Extract the leading power p "
        "in B~A*eps^p via log-log slope + B/eps, B/eps^2 ratios at q_0 (60 dps); "
        "also test whether the LP-optimal strand ordering is stable as eps->0 "
        "(ordering change = kink signature).  p~2 ⇒ Mechanism B holds; p~1 ⇒ "
        "fails as stated.  Archimedean numerical answer, not a symbolic proof; "
        "does not supply the m_e c^2 transport; no experimental comparison."
    )
    w.set_content_block("conj:e-hartree-categorical-derivation")
    w.add_data("q0", str(q0))
    w.add_data("phi_separated", str(phi_sep))
    w.add_data("phi_full", str(phi_full))
    w.add_data("binding_full", str(binding_full))
    w.add_data("ordering_separated", list(perm0))
    w.add_data("ordering_full", list(perm1))
    w.add_data("leading_power_p", str(p_est))
    w.add_data("B_over_eps_1e7", str(B_over_eps))
    w.add_data("B_over_eps2_1e7", str(B_over_eps2))
    w.add_data("active_set_stable", bool(active_set_stable))
    w.add_data("grid", [{"eps": str(e), "B": str(Be)} for e, Be, _, _ in rows])
    w.add_assertion(
        "binding vanishes at eps=0 (decoupled = separated atoms): |B(0)| ~ 0",
        computed=bool(abs(phi1(list(perm1), mp.mpf(0)) - phi_sep) < mp.mpf("1e-40")),
        expected=True, source="inter-atomic crossings -> identity at eps=0",
    )
    w.add_assertion(
        "leading power p is well-defined and in (0.5, 2.5)",
        computed=bool(mp.mpf("0.5") < p_est < mp.mpf("2.5")),
        expected=True, source="log-log slope of B(eps)",
    )
    w.add_assertion(
        "verdict is decisive (linear XOR quadratic, not inconclusive)",
        computed=bool(is_linear != is_quadratic and (is_linear or is_quadratic)),
        expected=True, source="B/eps vs B/eps^2 stabilisation",
    )
    w.add_data(
        "finding",
        f"Mechanism B verdict: {verdict}.  Leading power p={mp.nstr(p_est,6)}; "
        f"B/eps={mp.nstr(B_over_eps,4)}, B/eps^2={mp.nstr(B_over_eps2,4)} at "
        f"eps=1e-7; active-set stable as eps->0: {active_set_stable}.  This is "
        "the archimedean LP-functional answer to the single remaining "
        "e-hartree gap; the m_e c^2 unit transport is unaffected."
    )
    w.save()
    print("\nDone. Witness saved (e-hartree-mechanism-b-probe).")


if __name__ == "__main__":
    main()
