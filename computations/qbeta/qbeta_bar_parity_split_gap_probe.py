#!/usr/bin/env python3
"""Can the bar-parity-split gap be closed? Four routes, exact sympy, no floats.

Bean `qou-hlx8` / epic `qou-qs0e`; companion to `conj:bar-parity-split`
(demoted from prop on 2026-11-15, PR #7857). ANALYSIS ONLY: no witness, no
dashboard. Lean companion: `QOU/Mass/BarParitySplitGap.lean`.

Object: f(q) := tr^{z_D}(Delta), Delta = n - p, on the gamma-gamma-selected
nucleon word (the ruled Q_beta cell; reuses the census word builder exactly as
`qbeta_one_sided_weak_vertex_probe.py` does). The bar involution acts on a
letter c*s + d by s -> s^-1 = s - h and q -> 1/q (so h -> -h).

Routes (all symbolic in q; h = q - 1/q, z_D = q^3/(q^2+1)):
  R4  trace/bar intertwining: tr_z(bar w)(q) = tr_z(w)(1/q) on one letter iff
      z(q) - z(1/q) = h. Holds for z_D, fails for z_C. Checked on the full word.
  R2  f = h * g with g an explicit trace of context words (telescoping of the
      n - p letter differences, each = -h/2). Is g = f/h bar-even?  Is f
      bar-definite up to a power of q?
  R3  f_odd = (f - bar f)/2 = -(h/2) * g_even  and  f_even = -(h/2) * g_odd.
  R1  existence of F with identity readouts <=> parities of the readouts.
"""
from __future__ import annotations

import importlib.util
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python"):
    sys.path.insert(0, os.path.join(ROOT, _p))

_spec = importlib.util.spec_from_file_location(
    "_census", os.path.join(HERE, "qbeta_delta_candidate_census_probe.py"))
_census = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_census)
hm, h = _census.hm, _census.h

q = sp.symbols("q", positive=True)
H = q - 1 / q
ZD = q ** 3 / (q ** 2 + 1)
ZC = sp.sqrt(q) / (q + 1)

RESULTS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))


def bar(e):
    return sp.together(sp.sympify(e).subs(q, 1 / q))


def nf_of(letters):
    nf = [sp.Integer(1)] + [sp.Integer(0)] * 5
    for c, d, g in letters:
        nf = hm(nf, c, d, g)
    return nf


def tr(nf, zz):
    hz = h * zz + 1
    basis = [sp.Integer(1), zz, zz, zz ** 2, zz ** 2, zz * hz]
    return sp.factor(sp.together(sp.expand(sum(c * t for c, t in zip(nf, basis))).subs(h, H)))


def trw(letters, zz=ZD):
    return tr(nf_of(letters), zz)


U = lambda g: (sp.Integer(1), sp.Integer(0), g)
D = lambda g: (sp.Integer(1), -h, g)
UD = lambda g: (sp.Integer(1), -h / 2, g)
CORE = [U(0), D(1)] * 3
GLUON = [U(0), U(0)]
P_TAIL = [U(0), UD(0), UD(1)]
N_TAIL = [UD(0), UD(0), D(1)]


def bar_letters(ls):
    # c*s + d  ->  c*(s - h) + bar(d) ; d is a polynomial in h, bar(h) = -h
    return [(c, sp.expand(-c * h + d.subs(h, -h)), g) for c, d, g in ls]


def is_zero(e):
    return sp.simplify(sp.together(e)) == 0


def main() -> int:
    P12 = 2*q**12 - 6*q**10 + 3*q**8 - 6*q**6 + 5*q**4 - 5*q**2 + 2

    print("R4  trace / bar intertwining")
    check("one_letter_zD_satisfies_z(q)-z(1/q)=h", is_zero(ZD - bar(ZD) - H))
    check("one_letter_zC_fails_it", not is_zero(ZC - bar(ZC) - H),
          f"z_C(q)-z_C(1/q) = {sp.simplify(ZC - bar(ZC))}")
    wN, wP = CORE + N_TAIL + GLUON, CORE + P_TAIL + GLUON
    f = sp.factor(trw(wN) - trw(wP))
    check("base_f_matches_recorded_closed_form",
          is_zero(f - (q**2 - 1)*(q**4 + 1)*P12/(4*q**7*(q**2 + 1)**2)), f"f = {f}")
    fbarw = sp.factor(trw(bar_letters(wN)) - trw(bar_letters(wP)))
    check("full_word_trace_of_bar_Delta_equals_f(1/q)", is_zero(fbarw - bar(f)))
    for name, w in (("n-word", wN), ("p-word", wP)):
        check(f"intertwining_on_{name}", is_zero(trw(bar_letters(w)) - bar(trw(w))))

    print("\nR2  f = h * g (telescoping of the n - p letter differences)")
    # positions 1 and 3 of the tail differ: UD-U = -h/2, D-UD = -h/2
    W1 = CORE + [UD(0), D(1)] + GLUON          # n-letters after position 1 (pos 1 removed)
    W2 = CORE + [U(0), UD(0)] + GLUON          # p-letters before position 3 (pos 3 removed)
    g = sp.factor(-(trw(W1) + trw(W2)) / 2)
    check("f_equals_h_times_g", is_zero(f - H * g), f"g = {g}")
    g_even, g_odd = sp.factor((g + bar(g)) / 2), sp.factor((g - bar(g)) / 2)
    check("g_is_NOT_bar_even (so Q_beta/h is not bar-even)", not is_zero(g_odd),
          f"g_odd = {g_odd}")
    ratio = sp.factor(bar(f) / f)
    num, den = sp.fraction(ratio)
    mono = sp.Poly(sp.expand(num), q).length() == 1 and sp.Poly(sp.expand(den), q).length() == 1
    check("f_not_bar_definite_up_to_any_power_of_q", not mono, f"bar(f)/f = {ratio}")
    rev = sp.expand(q**12 * P12.subs(q, 1/q))
    check("P12_not_palindromic_nor_antipalindromic",
          not is_zero(rev - P12) and not is_zero(rev + P12), f"q^12 P12(1/q) = {rev}")
    gratio = sp.factor(bar(g) / g)
    gn, gd = sp.fraction(gratio)
    check("g_not_bar_definite_up_to_any_power_of_q",
          not (sp.Poly(sp.expand(gn), q).length() == 1 and sp.Poly(sp.expand(gd), q).length() == 1),
          f"bar(g)/g = {gratio}")

    print("\nR3  meaning of the bar-odd projection")
    f_odd, f_even = sp.factor((f - bar(f)) / 2), sp.factor((f + bar(f)) / 2)
    check("f_odd_equals_h_times_g_even", is_zero(f_odd - H * g_even), f"f_odd = {f_odd}")
    check("f_even_equals_h_times_g_odd", is_zero(f_even - H * g_odd), f"f_even = {f_even}")
    check("f_even_recorded_form",
          is_zero(f_even + H**2 * (q + 1/q) * (q**2 + q**-2) / 8))
    check("f_odd_equals_trace_of_bar_odd_part_of_Delta",
          is_zero(f_odd - (f - fbarw) / 2))

    print("\nR5  localisation of g_odd (exact subset interpolation, no word change)")
    # Bar one segment at a time (letter-level bar, kept at the same q), all 2^3
    # subsets of {core, tail, gluon}; Mobius-invert to single and cross effects.
    # Diagnostic only: the word is ruled and is NOT changed (qou-ales/qou-99qc).
    import itertools
    T1tail, T2tail = [UD(0), D(1)], [U(0), UD(0)]

    def g_sub(sub):
        c = bar_letters(CORE) if "core" in sub else CORE
        gl = bar_letters(GLUON) if "gluon" in sub else GLUON
        t1 = bar_letters(T1tail) if "tail" in sub else T1tail
        t2 = bar_letters(T2tail) if "tail" in sub else T2tail
        return sp.factor(-(trw(c + t1 + gl) + trw(c + t2 + gl)) / 2)

    segs = ("core", "tail", "gluon")
    G = {s: g_sub(set(s)) for r in range(4) for s in itertools.combinations(segs, r)}
    check("all_segments_barred_equals_g(1/q)", is_zero(G[segs] - bar(g)))
    eff = {}
    for r in range(1, 4):
        for s in itertools.combinations(segs, r):
            m = sum((-1) ** (r - k) * G[t] for k in range(r + 1)
                    for t in itertools.combinations(s, k))
            eff[s] = sp.factor(-m / 2)
            print(f"    contribution to g_odd of {s}: {eff[s]}")
    check("contributions_sum_to_g_odd", is_zero(sum(eff.values()) - g_odd))
    check("quark_tail_contributes_zero_alone_and_in_every_cross_term",
          all(is_zero(v) for k, v in eff.items() if "tail" in k))
    check("obstruction_is_core_plus_gluon_plus_their_cross_term",
          not is_zero(eff[("gluon",)]) and not is_zero(eff[("core", "gluon")]))
    check("core_trace_alone_is_bar_even", is_zero(trw(bar_letters(CORE)) - trw(CORE)))
    g_nogl = sp.factor(-(trw(CORE + T1tail) + trw(CORE + T2tail)) / 2)
    check("context_trace_without_gluon_pair_is_bar_even (diagnostic)",
          is_zero(g_nogl - bar(g_nogl)), f"g_without_gluon = {g_nogl}")

    print("\nR1  existence of F with identity readouts")
    # tau = (q + 1/q)/2 is bar-even; F := tau + f would need f bar-odd.
    tau = (q + 1 / q) / 2
    F = tau + f
    check("tau_bar_even", is_zero(tau - bar(tau)))
    check("F=tau+f_has_odd_part_not_f", not is_zero(sp.factor((F - bar(F)) / 2) - f))
    q2 = sp.Rational(2)
    v = f.subs(q, q2) + f.subs(q, 1 / q2)
    check("witness_q=2_f(2)+f(1/2)_nonzero", v != 0, f"f(2)+f(1/2) = {v}, f(2) = {f.subs(q, q2)}")

    nfail = sum(1 for _, ok, _ in RESULTS if not ok)
    print(f"\n{len(RESULTS) - nfail}/{len(RESULTS)} checks pass")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())
