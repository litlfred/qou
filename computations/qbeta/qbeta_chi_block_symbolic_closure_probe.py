#!/usr/bin/env python3
"""qou-avt2, part 3: are `chi_block_{3,21,111}` the EXACT characters of the
nucleon word difference, as functions of q -- or only its values at q0?

THE QUESTION. `qbeta_delta_vs_deltaTbeta_settled_probe.py` (qou-avt5) showed
that chi_block_* reproduces chi_lambda(beta_n - beta_p) at q0, all three blocks.
It said explicitly what it had NOT measured: "the ratio's q-dependence. The
words are q0-BAKED (their `d` are literal -h(q0)/2, -h(q0))". So agreement at
one point is compatible with the closed forms being right, and equally with
their being a q0 coincidence. This settles which.

WHAT MADE IT ANSWERABLE. `pyhecke.atom.nucleon_gen_chains` takes an optional
`q`, and with a sympy symbol it returns the chains SYMBOLICALLY:

    proton  g0 = [sigma x4, avg, sigma x2]        g1 = [sigma^-1 x3, avg]
    neutron g0 = [sigma x3, avg, avg, sigma x2]   g1 = [sigma^-1 x4]

with avg = -h/2 appearing as (1-q^2)/(2q) and sigma^-1 as -h. So the words are
NOT intrinsically q0-baked -- only the module-level constants `_PROTON_G0` and
friends are, being materialised at import. The chains' STRUCTURE is
q-independent, exactly as that function's docstring claims, and this file
verifies that claim rather than relying on it (CHECK 1).

Combined with the exact symbolic character engine of
`qbeta_hecke_symbolic_seminormal_probe.py`, chi_lambda(beta_n - beta_p) is then
computable as a rational function of q and can be compared to the closed forms
SYMBOLICALLY.

A crossing is the ALGEBRA element c*sigma_g + d, not a group element, so the
word matrix is a product of (c*M_g + d*I) -- which is why the plain
signed-word path of the sibling probe is not reused here.

CHECKS
  1. The chain structure is q-independent: the template classification at two
     unrelated generic q agrees, and agrees with the committed q0-baked
     constants.
  2. Counits: eps(beta_p) = q^3 ([2]_q/2)^2 and eps(beta_n) = q ([2]_q/2)^2,
     confirming qou-avt6's reading of the same words from a second direction.
  3. THE QUESTION: chi_lambda(beta_n - beta_p) vs chi_block_lambda, symbolically
     in q, for lambda = (3), (2,1), (1,1,1).
  4. Numeric tie-back at q0 against the corpus's own chi_all_lambda, so a
     symbolic disagreement cannot be blamed on assembling the word differently.

Ref: computations/qbeta/qbeta_delta_vs_deltaTbeta_settled_probe.py (qou-avt5)
Ref: tools/pyhecke/python/pyhecke/atom.py (nucleon_gen_chains)
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/pyhecke/python", "computations", "computations/hecke",
           "computations/substrate", "computations/qbeta",
           "tools/qou-substrate/python"):
    _s = str(_ROOT / _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

from qbeta_hecke_mn_character_engine_probe import q, h  # noqa: E402
from qbeta_hecke_symbolic_seminormal_probe import seminormal  # noqa: E402

BLOCKS = ((3,), (2, 1), (1, 1, 1))

# The committed closed forms, from computations/qbeta/qbeta_utils.py.
CLOSED = {
    (3,):       -(q ** 2 - 1) * (q ** 2 + 1) ** 2 / (4 * q),
    (2, 1):      (q ** 2 - 1) * (-(q ** 4) - 1) / (4 * q ** 3),
    (1, 1, 1):  -(q ** 2 - 1) * (q ** 2 + 1) ** 2 / (4 * q ** 5),
}


def chains(quarks, qsym):
    """The nucleon word at symbolic q. GROUPED. The numeric tie-back kernel is
    `chi_all_lambda_any` since 2026-10-10 (byte-identical); the symbolic object
    below is still the grouped word, so a frame change means re-deriving it
    (bean `qou-11l4`). History follows.

    `chi_monotone_transfer.chi_all_lambda`, which this probe uses, accepts only
    a monotone generator sequence, and the canonical borromean word is
    non-monotone by construction (core `(sigma_0 sigma_1^-1)^3`): feeding it
    there raises `ValueError: non-monotone word: gen 0 after 1`. Measured, not
    inferred. So the frame changes when the KERNEL does
    (`chi_general_word.chi_all_lambda_any`, the remedy `closed_form_tau_M`
    already took), not when this function does.

    This one holds the QUARKS, so it asks `nucleon_word_letters` for the
    legacy word by name rather than concatenating the two chains itself --
    the same object, one caller closer to the definition. Beans `qou-11l4`
    (this probe is missing from `qou-y2o7`'s blast radius, which is marked
    completed) and `qou-t29k`.
    """
    from pyhecke.atom import nucleon_word_letters
    return [(c, sp.simplify(d), off) for c, d, off in
            nucleon_word_letters(list(quarks), q=qsym, intra_order="grouped")]


def classify(word, qsym):
    """Name each crossing by its template: sigma / sigma^-1 / avg."""
    hh = sp.simplify(qsym - 1 / qsym)
    out = []
    for c, d, g in word:
        dd = sp.simplify(d)
        if sp.simplify(dd) == 0:
            out.append((g, "sigma"))
        elif sp.simplify(dd + hh) == 0:
            out.append((g, "sigma_inv"))
        elif sp.simplify(dd + hh / 2) == 0:
            out.append((g, "avg"))
        else:
            out.append((g, f"other:{dd}"))
    return tuple(out)


def word_matrix(shape, word):
    mats = seminormal(shape)
    dim = mats[0].shape[0]
    out = sp.eye(dim)
    for c, d, g in word:
        out = out * (sp.sympify(c) * mats[g] + sp.sympify(d) * sp.eye(dim))
    return out


def chi(shape, word):
    return sp.cancel(sp.together(sp.expand(sp.trace(word_matrix(shape, word)))))


def counit(word):
    """eps of a typed word: sigma -> q, so each factor contributes c*q + d."""
    val = sp.Integer(1)
    for c, d, _ in word:
        val *= sp.sympify(c) * q + sp.sympify(d)
    return sp.cancel(sp.together(sp.expand(val)))


RESULTS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))


def main() -> int:
    print("qou-avt2 part 3 — are chi_block_* exact in q?\n")

    wp = chains(["u", "u", "d"], q)
    wn = chains(["u", "d", "d"], q)

    # ---- 1: the chain structure really is q-independent --------------------
    #
    # Done two ways, and NEITHER passes a fresh numeric q into
    # nucleon_gen_chains: that function refuses an mpf carrying only float64
    # information, and rightly so -- `allow_float64=True` would be declaring a
    # deliberately f64 sweep, which this is not.
    #
    #   (a) substitute two unrelated exact rationals into the SYMBOLIC chains
    #       and confirm the template classification does not move;
    #   (b) classify the COMMITTED q0-baked constants _PROTON_G0 / _NEUTRON_G0
    #       and friends, and confirm they carry the same structure -- which is
    #       what licenses reading a symbolic result back onto them.
    print("CHECK 1 — chain structure is q-independent")
    sig_sym_p, sig_sym_n = classify(wp, q), classify(wn, q)

    sub_ok = True
    for qval in (sp.Rational(13, 10), sp.Rational(77, 100)):
        for w, sig in ((wp, sig_sym_p), (wn, sig_sym_n)):
            wsub = [(c, sp.nsimplify(sp.simplify(d.subs(q, qval))), g) for c, d, g in w]
            if classify(wsub, qval) != sig:
                sub_ok = False
    check("chain_structure_invariant_under_substitution", sub_ok,
          f"q = 13/10 and 77/100; p: {[t for _, t in sig_sym_p]}")

    committed_ok, det = False, ""
    try:
        import mpmath as mpm
        mpm.mp.dps = 60
        from q_parameter import Q_50_DIGIT_STR as _Q50
        from pyhecke.atom import (_PROTON_G0, _PROTON_G1,
                                  _NEUTRON_G0, _NEUTRON_G1)
        qv = mpm.mpf(str(_Q50))
        hv = qv - 1 / qv

        def cl_committed(g0, g1):
            out = []
            for chain, gen in ((g0, 0), (g1, 1)):
                for c, d in chain:
                    dv = mpm.mpf(str(d))
                    if abs(dv) < mpm.mpf("1e-40"):
                        out.append((gen, "sigma"))
                    elif abs(dv + hv) < mpm.mpf("1e-40"):
                        out.append((gen, "sigma_inv"))
                    elif abs(dv + hv / 2) < mpm.mpf("1e-40"):
                        out.append((gen, "avg"))
                    else:
                        out.append((gen, "other"))
            return tuple(out)

        got_p = cl_committed(_PROTON_G0, _PROTON_G1)
        got_n = cl_committed(_NEUTRON_G0, _NEUTRON_G1)
        committed_ok = (got_p == sig_sym_p and got_n == sig_sym_n)
        det = f"n: {[t for _, t in sig_sym_n]}"
    except Exception as exc:
        det = f"could not run: {exc.__class__.__name__}: {exc}"
    check("committed_q0_constants_have_the_symbolic_structure",
          committed_ok, det)
    print()

    # ---- 2: counits, tying back to qou-avt6 --------------------------------
    print("CHECK 2 — counits reproduce qou-avt6's typed-word normal form")
    b2 = (q ** 2 + 1) / (2 * q)          # [2]_q / 2
    ep, en = counit(wp), counit(wn)
    check("counit_proton_is_q3_times_bracket2half_squared",
          sp.simplify(ep - q ** 3 * b2 ** 2) == 0, f"eps(beta_p) = {sp.factor(ep)}")
    check("counit_neutron_is_q_times_bracket2half_squared",
          sp.simplify(en - q * b2 ** 2) == 0, f"eps(beta_n) = {sp.factor(en)}")
    check("counit_difference_is_chi_block_3",
          sp.simplify(sp.cancel(en - ep) - CLOSED[(3,)]) == 0,
          "eps(beta_n - beta_p) = chi_block_3, symbolically")
    print()

    # ---- 3: THE QUESTION ---------------------------------------------------
    print("CHECK 3 — chi_lambda(beta_n - beta_p) vs the committed closed forms")
    diffs = {}
    for lam in BLOCKS:
        got = sp.cancel(chi(lam, wn) - chi(lam, wp))
        want = sp.cancel(sp.together(CLOSED[lam]))
        delta = sp.simplify(sp.cancel(got - want))
        diffs[lam] = (got, want, delta)
        print(f"    lambda = {lam}")
        print(f"      from the words : {sp.factor(got)}")
        print(f"      committed form : {sp.factor(want)}")
        print(f"      difference     : {sp.factor(delta)}")
        check(f"chi_block_{''.join(map(str, lam))}_exact_in_q", delta == 0)
    print()

    # ---- 4: numeric tie-back to the corpus's own evaluator -----------------
    print("CHECK 4 — numeric tie-back at q0 against chi_all_lambda")
    tie_ok, tie_detail = False, ""
    try:
        import mpmath as mpm
        mpm.mp.dps = 50
        from q_parameter import Q_50_DIGIT_STR as Q50
        from chi_general_word import chi_all_lambda_any as chi_all_lambda
        qv = mpm.mpf(str(Q50))
        wpn = chains(["u", "u", "d"], qv)
        wnn = chains(["u", "d", "d"], qv)
        cp = chi_all_lambda([(c, d, g) for c, d, g in wpn], 3, dps=50, q=qv)
        cn = chi_all_lambda([(c, d, g) for c, d, g in wnn], 3, dps=50, q=qv)
        worst = mpm.mpf(0)
        for lam in BLOCKS:
            mine = mpm.mpf(str(sp.N(diffs[lam][0].subs(q, sp.Rational(str(qv))), 45)))
            theirs = cn.get(tuple(lam), mpm.mpf(0)) - cp.get(tuple(lam), mpm.mpf(0))
            worst = max(worst, abs(mine - theirs))
        tie_ok = worst < mpm.mpf("1e-35")
        tie_detail = f"worst |Delta| = {mpm.nstr(worst, 8)} at 50 dps"
    except Exception as exc:
        tie_detail = f"could not run: {exc.__class__.__name__}: {exc}"
    check("numeric_tieback_to_chi_all_lambda", tie_ok, tie_detail)
    print()

    ok = all(r[1] for r in RESULTS)
    print(f"{sum(1 for r in RESULTS if r[1])}/{len(RESULTS)} checks passed")

    try:
        from qou_substrate.witness import WitnessBuilder
        wb = WitnessBuilder("qbeta-chi-block-symbolic-closure", _script_path=__file__)
        wb.set_description(
            "Whether chi_block_{3,21,111} are the exact q-rational characters of "
            "the nucleon word difference beta_n - beta_p, or only its values at "
            "q0. Settled symbolically, using nucleon_gen_chains with a sympy q."
        )
        wb.add_data("markov_convention", "not applicable — no z enters this computation")
        wb.add_data("q0_anchor",
                    "symbolic in q; the numeric tie-back (CHECK 4) uses the "
                    "committed q-pinning 50-digit value via q_parameter")
        wb.add_data("chi_from_words", {str(k): str(sp.factor(v[0])) for k, v in diffs.items()})
        wb.add_data("chi_committed", {str(k): str(sp.factor(v[1])) for k, v in diffs.items()})
        wb.add_data("difference", {str(k): str(sp.factor(v[2])) for k, v in diffs.items()})
        for name, passed, det in RESULTS:
            wb.add_assertion(name, "1" if passed else "0", "1", "0", source=det or None)
        wb.save()
        print("witness written")
    except Exception as exc:  # pragma: no cover
        print(f"witness NOT written ({exc.__class__.__name__}: {exc})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
