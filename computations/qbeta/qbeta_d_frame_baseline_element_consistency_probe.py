#!/usr/bin/env python3
"""The D-frame baseline's 92.1x is a CROSS-ELEMENT ratio, and it is not
"understated" -- the two consistent ratios BRACKET it.

# Ref: .beans/qou-bg3w--which-element-is-delta-two-nucleon-word-models-1-2.md
# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md
# Ref: computations/qbeta/qbeta_d_frame_trace_baseline_probe.py
# Ref: docs/audits/2026-08-28-cds1-two-nucleon-word-models.md

WHAT THE BASELINE PROBE DOES.  `qbeta_d_frame_trace_baseline_probe.py`
computes, in forty lines:

    chi   <- chi_all_lambda(_word(_PROTON_G0, _PROTON_G1), ...)   the LONG word
    eps   <- h**2 / 2 - h                                          hardcoded
    ratio <- |err(trace)| / |err(eps)|          =  92.1058

and reports that ratio as "the baseline gap is 92.1x the whole five-rung
ladder".  The trace is taken on `hecke_core`'s ELEVEN-crossing gen-grouped
nucleon words (Delta_L); the counit closed form `h^2/2 - h` is the ONE-/TWO-
crossing short model's (Delta_S).  Two different elements of H_3(q) -- bean
qou-bg3w -- so the ratio compares a property of one against a property of the
other.  Neither measurement is wrong; the RATIO is the straddle.

WHAT THIS PROBE FINDS.

 1. The two trace routes are ONE functional.  The baseline probe's Frobenius
    pairing sum_lambda y_lambda(q, N=2) chi^lambda and the Markov trace
    tr_M at z = z_D agree on Delta_L to every digit carried (< 1e-40).  This
    is what licenses pricing Delta_S's trace from its recorded closed form
    h^2/2 - h z, and it is checked rather than assumed.

 2. Priced consistently, the ratio is not one number but two, and they
    BRACKET the published one:

        on Delta_S    counit  +0.1678 %   trace  -43.157 %    ratio  257.26
        published     counit  +0.1678 %   trace  -15.451 %    ratio   92.11
        on Delta_L    counit +24.769 %    trace  -15.451 %    ratio    0.6237

 3. So "the published figure UNDERSTATES by 2.793x" -- this repo's own
    recorded reading of the straddle -- is itself DELTA_S-CONDITIONAL.  It
    understates by 2.793x against Delta_S and OVERSTATES by 148x against
    Delta_L.  A cross-element ratio has no single correction factor, because
    it is not an approximation to either consistent ratio.  Recorded because
    it is the same shape as the errors qou-bg3w already collects: a quantity
    true relative to one choice, reported as though the choice were not
    being made.

 4. The straddle picked the flattering half of each element.  Delta_S's
    counit is the corpus's best functional (+0.168 %) and Delta_L's trace is
    the better of the two traces (-15.5 % against -43.2 %).  Nothing is
    alleged about intent -- the counit is a hardcoded closed form and the
    trace is built from an imported word, so the two halves were never in
    the same place to be compared.  That is exactly why it survived.

WHAT IS NOT CLAIMED.  Which element Delta is -- that is qou-bg3w's open
owner call and this probe does not touch it.  Nor that either baseline is
wrong: each is a correct statement about the element it is computed on.

SCOPE-(a).  Pricing consistency only.  Excludes no functional, no element and
no convention; adjudicates no net value.  It does not move Q_beta, any mass,
any binding energy, or L2.

METHOD.  Exact throughout: sympy in q, substituted at the 50-digit q_0 as an
exact Rational, read out through mpmath at 50 dps.  No float64 anywhere, per
AGENTS.md -- probes are not exempt.
"""
from __future__ import annotations

import sys as _sys
import pathlib as _pl

# bootstrap: _path_bridge lives in computations/, one level up from this
# cluster dir, so it must reach sys.path BEFORE it is imported.
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))

import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_MP  # noqa: E402 -- exact mpf, not the f64 twin
from y_lambda_su_n import y_lambda_su_n  # noqa: E402
from chi_general_word import chi_all_lambda_any as chi_all_lambda  # noqa: E402
from hecke_core import (  # noqa: E402
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
)
from qou_substrate.constants import Q_NEUTRON_MEV, M_E_MEV  # noqa: E402

# the element machinery, reused rather than re-derived
from qbeta_delta_element_fork_pricing_probe import (  # noqa: E402
    q as q_sym, h as h_sym, vec, net, tr_M, num, Z, Z_D, _mult, _crossings,
)
from qbeta_net_trace_invariance_probe import basis_vec  # noqa: E402

set_compute_dps(50)

_FAILURES: list[str] = []


def check(name, passed, note, wb=None):
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
    print(f"         {note}")
    if wb is not None:
        wb.add_data(name, bool(passed))
        wb.add_assertion(name, computed="1" if passed else "0",
                         expected="1", tolerance="0")
    if not passed:
        _FAILURES.append(name)
    return passed


def _word(g0, g1):
    """The nucleon word. GROUPED -- a CHOICE, no longer forced: since 2026-10-10 the kernel is
    `chi_general_word.chi_all_lambda_any` (byte-identical output on this word),
    and the canonical word MOVES these numbers -- which frame to use is an owner
    call recorded in bean `qou-11l4`. The paragraph below is the history.

    `chi_monotone_transfer.chi_all_lambda`, which this probe uses, accepts only
    a monotone generator sequence. The canonical borromean word is non-monotone
    by construction -- its core is `(sigma_0 sigma_1^-1)^3` -- so feeding it
    here raises `ValueError: non-monotone word: gen 0 after 1`. Measured, not
    inferred. The frame therefore cannot be changed by editing this helper; it
    changes when the kernel does (`chi_general_word.chi_all_lambda_any`, the
    remedy `closed_form_tau_M` already took).

    Named via `grouped_word_from_chains` so the constraint is visible at the
    call site instead of one import line away. Beans `qou-11l4` (this probe is
    missing from `qou-y2o7`'s blast radius, which is marked completed) and
    `qou-t29k`. Output unchanged: the helper IS this concatenation, with the
    mpf conversion preserved per chain.

    Still the baseline probe's own word builder byte-for-byte, as this
    docstring said before -- its twin is now routed through the same
    named helper, so the two stay identical.
    """
    from pyhecke.atom import grouped_word_from_chains
    return grouped_word_from_chains(
        [(mp.mpf(str(c)), mp.mpf(str(d))) for c, d in g0],
        [(mp.mpf(str(c)), mp.mpf(str(d))) for c, d in g1],
    )


def main() -> int:
    q = Q_MP
    h = q - 1 / q
    me = mp.mpf(str(M_E_MEV))
    Qexp = mp.mpf(str(Q_NEUTRON_MEV))
    E0 = me / (q * (q - 1))

    wb = WitnessBuilder("qbeta-d-frame-baseline-element-consistency",
                        engine="sympy+mpmath")
    wb.set_description(
        "The D-frame trace baseline's published 92.1058x ratio takes its "
        "counit from Delta_S (the short model's closed form h^2/2 - h) and "
        "its Markov trace from Delta_L (hecke_core's 11-crossing gen-grouped "
        "words) -- two different elements of H_3(q), bean qou-bg3w. Priced "
        "consistently the ratio is 257.26x on Delta_S and 0.6237x on "
        "Delta_L, so the published figure is BRACKETED by the two rather "
        "than approximating either, and the recorded reading 'understates by "
        "2.793x' is itself Delta_S-conditional. Scope-(a): pricing "
        "consistency only; adjudicates no element and moves no observable.")

    print("=" * 74)
    print(" qou-bg3w — the D-frame baseline's ratio is cross-element")
    print("=" * 74)

    # ---- the two elements, built the way each side of the straddle does ---
    delta_s = vec(h_sym**2 / 2, -h_sym / 2, -h_sym / 2, 0, 0, 0)
    e0 = basis_vec(0)
    pw = sp.expand(_mult(_crossings(_PROTON_G0, _PROTON_G1)) * e0)
    nw = sp.expand(_mult(_crossings(_NEUTRON_G0, _NEUTRON_G1)) * e0)
    delta_l = sp.Matrix([sp.simplify(nw[i] - pw[i]) for i in range(6)])

    net_s, net_l = num(net(delta_s)), num(net(delta_l))
    trz_s = num(sp.simplify(tr_M(delta_s).subs(Z, Z_D)))
    trz_l = num(sp.simplify(tr_M(delta_l).subs(Z, Z_D)))

    # ---- 1. the baseline probe's OWN trace route, on Delta_L ---------------
    cp = chi_all_lambda(_word(_PROTON_G0, _PROTON_G1), 3, dps=50, q=q)
    cn = chi_all_lambda(_word(_NEUTRON_G0, _NEUTRON_G1), 3, dps=50, q=q)
    chi = {k: cn.get(k, mp.mpf(0)) - cp.get(k, mp.mpf(0))
           for k in set(cn) | set(cp)}
    y2 = y_lambda_su_n(3, q, 2)
    frob_l = mp.mpf(0)
    for sh, v in y2.items():
        frob_l += v * chi.get(tuple(sh), mp.mpf(0))

    print(f"\n  Frobenius sum_lambda y_lambda(N=2) chi^lambda (Delta_L) = "
          f"{mp.nstr(frob_l, 18)}")
    print(f"  Markov tr_M at z_D                        (Delta_L) = "
          f"{mp.nstr(trz_l, 18)}")
    wb.add_data("frobenius_N2_delta_L", fmt(frob_l))
    wb.add_data("markov_trace_zD_delta_L", fmt(trz_l))

    check("frobenius_pairing_at_N2_IS_the_markov_trace_at_zD",
          abs(frob_l - trz_l) < mp.mpf("1e-40"),
          "the two-row Frobenius pairing the baseline probe uses and the "
          "Markov trace at z_D agree on Delta_L to better than 1e-40. They "
          "are one functional, which is what licenses pricing Delta_S's "
          "trace from its recorded closed form h^2/2 - h z rather than "
          "rebuilding a word for it", wb)

    # ---- 2. price both functionals on BOTH elements ------------------------
    def err(val):
        return (abs(val) * E0 - Qexp) / Qexp

    e_net_s, e_net_l = err(net_s), err(net_l)
    e_tr_s, e_tr_l = err(trz_s), err(trz_l)

    print("\n  element      counit(net)              trace at z_D")
    for lbl, n_, t_, en, et in (("Delta_S", net_s, trz_s, e_net_s, e_tr_s),
                                ("Delta_L", net_l, trz_l, e_net_l, e_tr_l)):
        print(f"  {lbl}   {mp.nstr(n_, 16):>20}  {mp.nstr(en * 100, 6):>10} %"
              f"   {mp.nstr(t_, 16):>20}  {mp.nstr(et * 100, 6):>10} %")
    for k, v in (("net_delta_S", net_s), ("net_delta_L", net_l),
                 ("trace_zD_delta_S", trz_s), ("trace_zD_delta_L", trz_l),
                 ("err_net_delta_S", e_net_s), ("err_net_delta_L", e_net_l),
                 ("err_trace_delta_S", e_tr_s), ("err_trace_delta_L", e_tr_l)):
        wb.add_data(k, fmt(v))

    r_pub = abs(e_tr_l) / abs(e_net_s)       # what the baseline probe prints
    r_s = abs(e_tr_s) / abs(e_net_s)
    r_l = abs(e_tr_l) / abs(e_net_l)
    print(f"\n  published (trace on Delta_L / counit on Delta_S) = "
          f"{mp.nstr(r_pub, 8)}")
    print(f"  consistent on Delta_S                            = "
          f"{mp.nstr(r_s, 8)}")
    print(f"  consistent on Delta_L                            = "
          f"{mp.nstr(r_l, 8)}")
    wb.add_data("ratio_published_cross_element", fmt(r_pub))
    wb.add_data("ratio_consistent_delta_S", fmt(r_s))
    wb.add_data("ratio_consistent_delta_L", fmt(r_l))

    check("published_ratio_REPRODUCES_at_92_1058_and_is_cross_element",
          abs(r_pub - mp.mpf("92.1058")) < mp.mpf("0.01") and net_s != net_l,
          f"recomputing the baseline probe's ratio from these two elements "
          f"gives {mp.nstr(r_pub, 9)}, matching the committed 92.1058 -- "
          f"which is what identifies the attribution rather than merely "
          f"suggesting it. net(Delta_S) = {mp.nstr(net_s, 12)} and "
          f"net(Delta_L) = {mp.nstr(net_l, 12)} are different elements", wb)

    check("the_two_consistent_ratios_BRACKET_the_published_one",
          r_l < r_pub < r_s,
          f"{mp.nstr(r_l, 6)} < {mp.nstr(r_pub, 6)} < {mp.nstr(r_s, 6)}. The "
          f"published figure is not an approximation to either consistent "
          f"ratio -- it lies strictly between them, which is what a "
          f"cross-element ratio does and what a mis-measured one does not", wb)

    understate = r_s / r_pub
    overstate = r_pub / r_l
    print(f"\n  vs Delta_S: understates by {mp.nstr(understate, 6)}x")
    print(f"  vs Delta_L: overstates  by {mp.nstr(overstate, 6)}x")
    wb.add_data("understatement_vs_delta_S", fmt(understate))
    wb.add_data("overstatement_vs_delta_L", fmt(overstate))

    check("the_recorded_2_793x_understatement_is_DELTA_S_CONDITIONAL",
          abs(understate - mp.mpf("2.793")) < mp.mpf("0.01") and overstate > 100,
          f"this repo records the straddle as 'understating by 2.793x', "
          f"reproduced here as {mp.nstr(understate, 6)}x -- but only against "
          f"Delta_S. Against Delta_L the same figure OVERSTATES by "
          f"{mp.nstr(overstate, 6)}x. A cross-element ratio has no single "
          f"correction factor; quoting one silently fixes the element", wb)

    check("the_straddle_took_the_flattering_half_of_each_element",
          abs(e_net_s) < abs(e_net_l) and abs(e_tr_l) < abs(e_tr_s),
          f"Delta_S carries the better counit ({mp.nstr(e_net_s * 100, 6)} % "
          f"vs {mp.nstr(e_net_l * 100, 6)} %) and Delta_L the better trace "
          f"({mp.nstr(e_tr_l * 100, 6)} % vs {mp.nstr(e_tr_s * 100, 6)} %). "
          f"No intent is alleged: the counit is a hardcoded closed form and "
          f"the trace is built from an imported word, so the two halves were "
          f"never in one place to be compared -- which is why it survived", wb)

    print("\n  scope")
    print("    SCOPE-(a). Pricing consistency only. Adjudicates no element")
    print("    (qou-bg3w stays open), excludes no functional, and moves no")
    print("    observable -- not Q_beta, not a mass, not a binding, not L2.")
    wb.add_data("scope", "(a) pricing consistency only")

    total = 5
    print(f"\n  {total - len(_FAILURES)}/{total} checks passed")
    for f in _FAILURES:
        print(f"    FAILED: {f}")
    out = wb.save()
    print(f"\n  witness -> {out}")
    return 1 if _FAILURES else 0


if __name__ == "__main__":
    _sys.exit(main())
