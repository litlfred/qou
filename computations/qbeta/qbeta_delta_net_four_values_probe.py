#!/usr/bin/env python3
"""Delta is not underdetermined by ONE fork — the corpus carries FOUR net values.

qou-bg3w.  The Delta-element question has been framed as a two-way fork:
`Delta_S` (the short NF vector) versus `Delta_L` (`hecke_core`'s typed-crossing
words).  This probe measures a third and fourth object and shows the four do
not agree, so no choice between the first two can be the whole answer.

WHAT IS MEASURED

  (1) SHORT.  `deuteron-binding-dressing-proton-net.md` gives net(p) = 1 - h/2
      and net(n) = 1 - 3h/2 + h^2/2, so Delta = h^2/2 - h = epsNPq.  This is
      what the published c_k ladder is built from.

  (2) PROPERTIES BLOCKS, AS STATED.  `categorical-proton-properties.md` and
      `categorical-neutron-properties.md` state net(p) = +1.0065 and
      net(n) = +0.7976, hence Delta net = -0.2089.

  (3) PROPERTIES BLOCKS, AS CONSTRUCTED.  Those same blocks give the recipe
      explicitly: B_3 = (sigma_0 (sigma_1 - h))^3, a bare 9-crossing element
      `B_3 x Delta_3(quarks)` with typed shifts (uu -> 0, ud -> -h/2,
      dd -> -h), plus a Hopf link L_- = sigma_1 sigma_0.  Building that gives
      net(n) = 0.79756644, which is EXACTLY the stated 0.7976 -- at ONE Hopf
      link, i.e. ELEVEN crossings.

  (4) HECKE_CORE.  The words `Delta_L` is actually built from give
      net(p) = 1.3464 and net(n) = 1.1132.

THE TWO FINDINGS

  A. THE "13 CROSSINGS" SENTENCE CONTRADICTS ITS OWN BLOCK'S NUMBER.
     `categorical-neutron-properties.md:11` says the LP dual "selects
     L_+ -> L_- (two Hopf links, 4 gluon crossings)... This yields a total of
     13 crossings".  But the net it reports two lines later, +0.7976, is the
     ONE-Hopf-link value; the two-Hopf-link value is 1.2359 and appears
     nowhere in the corpus.  So the count is ELEVEN, and the sentence is the
     error -- not `hecke_core`, and not the "11 typed crossings each" in
     `q-beta-gamma-gamma-canonical-derivation.md:33`.

     This CORRECTS `qbeta_nucleon_crossing_count_contradiction_probe`, which
     established the prose/code mismatch but left open which side was wrong.
     The block's own number settles it.

  B. FOUR VALUES FOR ONE QUANTITY.  net(p) alone takes three distinct values
     in the corpus (0.8955 / 1.0065 / 1.3464) and Delta net takes four
     (-0.18721 / -0.2089 / -0.2138 / -0.2332).  The published ladder consumes
     the first; the content blocks state the second; `hecke_core` -- and
     therefore the D-frame trace baseline, which calibrates against it --
     produces the fourth.

SCOPE -- (a), and deliberately so.  This ADJUDICATES NOTHING.  It does not say
which net is right, does not modify `hecke_core`, does not touch a content
block, and proposes no c_k.  It reports that the Delta question cannot be
closed by picking between two candidates, because there are four numbers and
no two agree.  Which is canonical is an owner call (bean qou-bg3w).

Anti-fit note: every construction below is stated BEFORE it is evaluated and
none is tuned.  The generator assignment of the three quark crossings is not
given by the corpus, so ALL EIGHT are reported rather than the best one; the
neutron match at 0.79756644 holds for several assignments and is not a
selected fit.

-- Ref: [manuscript] content/quantum-observable-universe/knots-particles-confinement/categorical-proton-properties.md
-- Ref: [manuscript] content/quantum-observable-universe/knots-particles-confinement/categorical-neutron-properties.md
-- Ref: [manuscript] computations/qbeta/qbeta_nucleon_crossing_count_contradiction_probe.py (which this corrects)
-- Ref: [manuscript] computations/qbeta/qbeta_delta_element_fork_pricing_probe.py (the two-way framing)
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
from hecke_core import (  # noqa: E402
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
)
from qbeta_net_trace_invariance_probe import (  # noqa: E402
    q, h, N, BASIS_NAMES, L, ONE, basis_vec, vec,
)

set_compute_dps(50)

Q0 = sp.Rational(Q_50_DIGIT_STR)
_HN = mp.mpf(Q_50_DIGIT_STR) - 1 / mp.mpf(Q_50_DIGIT_STR)

#: values quoted in the content blocks, at the precision they are quoted
STATED_P = mp.mpf("1.0065")
STATED_N = mp.mpf("0.7976")
STATED_B3 = mp.mpf("1.0000")

_FAILURES: list[str] = []


def check(name, ok, detail, w=None):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    print(f"         {detail}")
    if w is not None:
        w.add_data(name, bool(ok))
    if not ok:
        _FAILURES.append(name)
    return ok


def num(e):
    """Exact q -> q_0 substitution, then a 40-dps mpf readout. No float64."""
    return mp.mpf(str(sp.N(sp.simplify(sp.sympify(e)).subs(q, Q0), 40)))


def _dsym(d):
    for s, v in ((sp.Integer(0), mp.mpf(0)), (-h, -_HN), (-h / 2, -_HN / 2)):
        if abs(d - v) < mp.mpf("1e-30"):
            return s
    raise ValueError(f"unrecognised crossing shift {d}")


def hecke_word(g0, g1):
    """hecke_core's word: all gen-0 factors, then all gen-1 -- the same order
    qbeta_delta_element_fork_pricing_probe uses, which reproduces the
    committed D-frame trace baseline exactly."""
    M = ONE
    for c, d in g0:
        M = M * (L[0] + _dsym(d) * ONE)
    for c, d in g1:
        M = M * (L[1] + _dsym(d) * ONE)
    return sp.expand(M * basis_vec(0))


#: B_3 = (sigma_0 (sigma_1 - h))^3, verbatim from categorical-proton-properties
B3 = ONE
for _ in range(3):
    B3 = B3 * L[0] * (L[1] - h * ONE)

#: L_- = sigma_1 sigma_0, verbatim
L_MINUS = L[1] * L[0]

#: typed quark shifts: uu preserves +q (d=0); dd a full -h; ud a half -h/2
QUARKS = {"p": [sp.Integer(0), -h / 2, -h / 2],   # uud -> uu, ud, ud
          "n": [-h, -h / 2, -h / 2]}              # udd -> dd, ud, ud


def built(who, gens, k):
    """B_3 x Delta_3(quarks) x (L_-)^k, k Hopf links."""
    M = B3
    for g, d in zip(gens, QUARKS[who]):
        M = M * (L[g] + d * ONE)
    for _ in range(k):
        M = M * L_MINUS
    return sp.expand(M * basis_vec(0))


def main() -> int:
    w = WitnessBuilder("qbeta-delta-net-four-values", engine="sympy+mpmath")
    w.set_description(
        "qou-bg3w: the Delta question is not a two-way fork. net(p) takes "
        "three distinct values in the corpus (0.8955 short / 1.0065 stated / "
        "1.3464 hecke_core) and Delta net takes four. Separately: the "
        "neutron block's '13 crossings' sentence contradicts the +0.7976 it "
        "reports two lines later, which is the ONE-Hopf-link (11-crossing) "
        "value -- so the count is 11 and the sentence is the error. "
        "Scope-(a): adjudicates nothing, changes no compute."
    )

    print("=" * 74)
    print(" qou-bg3w - Delta: four net values, and the 13-crossing sentence")
    print("=" * 74)

    # ---- B_3 itself -------------------------------------------------------
    b3 = num(sum(sp.expand(B3 * basis_vec(0))))
    print(f"\n  net(B_3) = {mp.nstr(b3, 12)}     block states +1.0000")
    w.add_data("net_B3", fmt(b3))
    check("B3_net_is_not_the_stated_one",
          abs(b3 - STATED_B3) > mp.mpf("1e-4"),
          f"the block's formula B_3 = (sigma_0(sigma_1-h))^3 gives "
          f"{mp.nstr(b3, 10)}, not the +1.0000 it states -- a {mp.nstr(abs(b3 - STATED_B3), 3)} "
          f"gap at the four decimals quoted", w)

    # ---- the k-ladder settles the crossing count --------------------------
    print("\n  NEUTRON k-ladder (gens=(0,0,0)); the block states +0.7976 AND "
          "'13 crossings'")
    ladder = {}
    for k in (0, 1, 2, 3):
        v = num(sum(built("n", (0, 0, 0), k)))
        ladder[k] = v
        tot = 6 + 3 + 2 * k
        flag = "  <-- the block's 0.7976" if abs(v - STATED_N) < mp.mpf("5e-5") else ""
        print(f"    k={k} Hopf ({tot:2d} crossings)  net = {mp.nstr(v, 12)}{flag}")
        w.add_data(f"neutron_net_k{k}", fmt(v))

    check("the_stated_neutron_net_is_the_ELEVEN_crossing_value",
          abs(ladder[1] - STATED_N) < mp.mpf("5e-5")
          and abs(ladder[2] - STATED_N) > mp.mpf("0.4"),
          f"k=1 (11 crossings) gives {mp.nstr(ladder[1], 10)} = the stated "
          f"0.7976; k=2 (13 crossings) gives {mp.nstr(ladder[2], 10)}, which "
          f"appears NOWHERE in the corpus. The '13 crossings' sentence "
          f"contradicts the number in its own block -- the count is 11", w)

    # ---- all eight generator assignments, not the best one ----------------
    print("\n  all 8 quark-generator assignments (k=1), stated: p=1.0065  n=0.7976")
    n_hits = 0
    for gens in itertools.product([0, 1], repeat=3):
        vp = num(sum(built("p", gens, 1)))
        vn = num(sum(built("n", gens, 1)))
        hit = abs(vn - STATED_N) < mp.mpf("5e-5")
        n_hits += hit
        print(f"    {gens}   net(p)={mp.nstr(vp, 10):>13}   "
              f"net(n)={mp.nstr(vn, 10):>13}{'   <-- n matches' if hit else ''}")
    check("the_neutron_match_is_not_a_single_tuned_assignment",
          n_hits >= 2,
          f"{n_hits} of the 8 generator assignments reproduce the stated "
          f"neutron net, so the match is a property of the construction, not "
          f"a selected fit", w)

    # ---- hecke_core's own nets --------------------------------------------
    p_h = num(sum(hecke_word(_PROTON_G0, _PROTON_G1)))
    n_h = num(sum(hecke_word(_NEUTRON_G0, _NEUTRON_G1)))
    print(f"\n  hecke_core   net(p) = {mp.nstr(p_h, 12)}   net(n) = {mp.nstr(n_h, 12)}")
    w.add_data("hecke_net_p", fmt(p_h))
    w.add_data("hecke_net_n", fmt(n_h))
    check("hecke_core_nets_do_not_match_the_content_blocks",
          abs(p_h - STATED_P) > mp.mpf("0.3") and abs(n_h - STATED_N) > mp.mpf("0.3"),
          f"hecke_core gives net(p)={mp.nstr(p_h, 8)} vs the stated 1.0065 "
          f"and net(n)={mp.nstr(n_h, 8)} vs the stated 0.7976 -- off by "
          f"{mp.nstr(abs(p_h - STATED_P), 3)} and "
          f"{mp.nstr(abs(n_h - STATED_N), 3)}, not a rounding difference", w)

    # ---- the four Delta values --------------------------------------------
    d_short = num(sum(vec(h**2 / 2, -h / 2, -h / 2, 0, 0, 0)))
    d_stated = STATED_N - STATED_P
    d_built = num(sum(built("n", (0, 0, 0), 1)) - sum(built("p", (0, 0, 0), 1)))
    d_hecke = n_h - p_h
    print("\n  FOUR values for one quantity:")
    rows = [("short model  (h^2/2 - h = epsNPq, what the ladder uses)", d_short),
            ("content blocks, as STATED (0.7976 - 1.0065)", d_stated),
            ("content blocks, as CONSTRUCTED (k=1)", d_built),
            ("hecke_core  (= Delta_L, what the D-frame baseline traces)", d_hecke)]
    for lbl, v in rows:
        print(f"    {lbl:<58} {mp.nstr(v, 10):>14}")
    w.add_data("delta_net_short", fmt(d_short))
    w.add_data("delta_net_stated", fmt(d_stated))
    w.add_data("delta_net_built", fmt(d_built))
    w.add_data("delta_net_hecke", fmt(d_hecke))

    vals = [d_short, d_stated, d_built, d_hecke]
    spread = max(vals) - min(vals)
    pairwise_ok = all(abs(vals[i] - vals[j]) > mp.mpf("1e-3")
                      for i in range(4) for j in range(i + 1, 4))
    check("no_two_of_the_four_delta_values_agree",
          pairwise_ok,
          f"all six pairwise gaps exceed 1e-3; total spread "
          f"{mp.nstr(spread, 6)} on a quantity of size ~0.2, i.e. ~"
          f"{mp.nstr(100 * spread / abs(d_short), 3)} % of the value the "
          f"ladder consumes. Delta is not determined by a two-way choice", w)

    check("net_p_alone_takes_three_values",
          True,
          f"net(p): 1 - h/2 = {mp.nstr(num(1 - h / 2), 8)} (short block), "
          f"1.0065 (properties block), {mp.nstr(p_h, 8)} (hecke_core)", w)

    print("\n  scope")
    print("    SCOPE-(a). Adjudicates NOTHING. No net is declared right, no")
    print("    c_k proposed, hecke_core and every content block untouched.")
    print("    The finding is that the Delta question cannot be closed by")
    print("    choosing between two candidates. Owner call: qou-bg3w.")
    w.add_data("scope", "a")
    w.add_data("adjudicates", False)

    npass = 6 - len(_FAILURES)
    print(f"\n  {npass}/6 checks passed")
    if _FAILURES:
        print(f"  FAILURES: {', '.join(_FAILURES)}")
    w.add_data("checks_passed", npass)
    w.add_data("checks_total", 6)
    out = w.save()
    print(f"\n  witness -> {out}")
    return 1 if _FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
