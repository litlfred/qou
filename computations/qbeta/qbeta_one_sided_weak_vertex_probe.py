#!/usr/bin/env python3
"""What a one-sided (chirality-selective) flavour vertex does to the Q_beta trace.

Bean `qou-hlx7` (epic `qou-qs0e`). ANALYSIS ONLY: this probe writes NO witness
and does NOT touch the dashboard (`per_observable_100x_status.py`). It prints.

Lean companion: `QOU/QuarkState/OneSidedWeakVertex.lean` (sorry-free), which
proves, for one Hecke letter s with eigenprojectors P+ (eigenvalue q) and P-
(eigenvalue -q^-1):

  * the L-only flavour flip  W_L := P+ s^-1 P+ + P- s P-  =  q^-1 J,
  * the R-only flavour flip  W_R := P+ s P+ + P- s^-1 P-  =  q   J,
    with J := P+ - P- = (s + s^-1)/[2]_q,  J^2 = 1,
  * each is the UNIQUE element of the ambient algebra with that action on the
    two eigenlines (uniqueness from P+ + P- = 1), so the vertex is forced, not
    chosen -- but there are exactly TWO of them (L-only, R-only), exchanged by
    the bar involution, which fixes J.
  * the corpus's mixed "ud" crossing letter  s - h/2  equals ([2]_q/2) J.
    That is an OBSERVATION about the existing word, not an identification.

This probe measures, in exact sympy then a 60-dps mpmath readout (never
float64), what replacing / inserting such a vertex in the gamma-gamma-selected
nucleon word does to tr^{z_D}(Delta), Delta = n - p, and therefore to
Q_beta = |tr^{z_D}(Delta)| * E_0.

It reuses the census's word builder (`hm`, letters c*sigma_g + d) so the base
reproduces the scored cell `tr_conv_D = -0.15419488504723970565925...`.
"""
from __future__ import annotations

import importlib.util
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

# the scored cell, read from the dashboard producer's witness, not typed.
import json  # noqa: E402
with open(os.path.join(HERE, "qbeta-gamma-gamma-qbeta-prediction.witness.json")) as _fh:
    _SCORED_TR_CONV_D = json.load(_fh)["data"]["calibration"]["tr_conv_D"]
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python"):
    sys.path.insert(0, os.path.join(ROOT, _p))

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_2022_source import M_E_MEV, Q_BETA_MEV_AME  # noqa: E402
from qbeta_e0 import canonical as e0_canonical  # noqa: E402

mp.mp.dps = 60

_spec = importlib.util.spec_from_file_location(
    "_census", os.path.join(HERE, "qbeta_delta_candidate_census_probe.py"))
_census = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_census)
hm, h = _census.hm, _census.h

Q0 = sp.Rational(Q_50_DIGIT_STR)
H0 = Q0 - 1 / Q0
TWO_Q = sp.sqrt(h ** 2 + 4)            # [2]_q = q + q^-1, as a function of h (q > 0)
QSYM = (h + TWO_Q) / 2                 # q as a function of h (positive root)
ZD = QSYM ** 3 / (QSYM ** 2 + 1)       # convention D

RESULTS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))


def at_q0(e):
    return mp.mpf(str(sp.N(sp.sympify(e).subs(h, H0), 60)))


def nf_of(letters):
    nf = [sp.Integer(1)] + [sp.Integer(0)] * 5
    for c, d, g in letters:
        nf = hm(nf, c, d, g)
    return nf


def tr(nf, zz):
    hz = h * zz + 1
    basis = [sp.Integer(1), zz, zz, zz ** 2, zz ** 2, zz * hz]
    return sp.expand(sum(c * t for c, t in zip(nf, basis)))


U = lambda g: (sp.Integer(1), sp.Integer(0), g)          # sigma_g      (u)
D = lambda g: (sp.Integer(1), -h, g)                     # sigma_g^-1   (d)
UD = lambda g: (sp.Integer(1), -h / 2, g)                # sigma_g - h/2 (mixed)
J = lambda g: (2 / TWO_Q, -h / TWO_Q, g)                 # (s + s^-1)/[2]
QIJ = lambda g: (2 / (QSYM * TWO_Q), -h / (QSYM * TWO_Q), g)  # q^-1 J = W_L (u->d on L only)
QJ = lambda g: (2 * QSYM / TWO_Q, -h * QSYM / TWO_Q, g)       # q J    = W_R (u->d on R only)

CORE = [U(0), D(1)] * 3
GLUON = [U(0), U(0)]
P_TAIL = [U(0), UD(0), UD(1)]
N_TAIL = [UD(0), UD(0), D(1)]


def word(tail, extra=()):
    return CORE + list(tail) + GLUON + list(extra)


E0 = e0_canonical(q=Q_MP, m_e=mp.mpf(str(M_E_MEV)))
QB = mp.mpf(str(Q_BETA_MEV_AME))


def report(label, n_letters, p_letters):
    nfn, nfp = nf_of(n_letters), nf_of(p_letters)
    t = at_q0(tr([a - b for a, b in zip(nfn, nfp)], ZD))
    qb = abs(t) * E0
    print(f"    {label:58s} tr={mp.nstr(t, 18):>24s}  Q_b={mp.nstr(qb, 12)} MeV"
          f"  vs CODATA {mp.nstr((qb / QB - 1) * 100, 8)} %")
    return t


def main() -> int:
    print("STRUCTURE (exact, symbolic in h)")
    # UD letter equals ([2]/2) J as an affine letter c*s + d:
    c_ud, d_ud = sp.Integer(1), -h / 2
    c_j, d_j = 2 / TWO_Q, -h / TWO_Q
    check("ud_letter_is_half_[2]_times_J",
          sp.simplify(c_ud - TWO_Q / 2 * c_j) == 0 and sp.simplify(d_ud - TWO_Q / 2 * d_j) == 0)
    # J^2 = 1 in one-letter algebra: (c s + d)^2 = c^2(hs+1) + 2cds + d^2
    c, d = c_j, d_j
    check("J_squared_is_one",
          sp.simplify(c ** 2 * h + 2 * c * d) == 0 and sp.simplify(c ** 2 + d ** 2 - 1) == 0)

    print("\nBASE (must reproduce the scored cell)")
    t0 = report("base nuc11_interleaved", word(N_TAIL), word(P_TAIL))
    check("base_reproduces_tr_conv_D",
          abs(t0 - mp.mpf(_SCORED_TR_CONV_D)) < mp.mpf("1e-24"),
          mp.nstr(t0, 25))

    print("\nREPLACE the neutron's terminal d letter sigma_1^-1 (the only tail d)")
    t_blind = report("  -> sigma_1          (chirality-blind flip d->u)",
                     word([UD(0), UD(0), U(1)]), word(P_TAIL))
    # d-letter sigma^-1 flipped to sigma on ONE line only:
    #   L-only: eigenvalues (q, q) on (P+, P-)  ->  q (P+ - P-) = q J
    #   R-only: eigenvalues (q^-1, -q^-1)        ->  q^-1 J
    t_wl = report("  -> q J_1     (L-only d->u: sigma on L, sigma^-1 on R)",
                  word([UD(0), UD(0), QJ(1)]), word(P_TAIL))
    t_wr = report("  -> q^-1 J_1  (R-only d->u)",
                  word([UD(0), UD(0), QIJ(1)]), word(P_TAIL))

    print("\nINSERT a vertex at the end of the neutron word (n -> n * V)")
    t_ins = {}
    for g in (0, 1):
        t_ins[("J", g)] = report(f"  V = J_{g}", word(N_TAIL, [J(g)]), word(P_TAIL))
        t_ins[("qinvJ", g)] = report(f"  V = q^-1 J_{g}", word(N_TAIL, [QIJ(g)]), word(P_TAIL))
        t_ins[("qJ", g)] = report(f"  V = q J_{g}", word(N_TAIL, [QJ(g)]), word(P_TAIL))

    print("\nRELATIVE EFFECTS on |tr| (hence on Q_beta at fixed E_0)")
    for lab, t in (("blind flip", t_blind), ("L-only flip (qJ)", t_wl),
                   ("R-only flip (q^-1 J)", t_wr)):
        print(f"    {lab:28s} |tr'|/|tr0| - 1 = {mp.nstr(abs(t) / abs(t0) - 1, 15)}")
    for k, t in t_ins.items():
        print(f"    insert {k[0]}_{k[1]:<20d} |tr'|/|tr0| - 1 = {mp.nstr(abs(t) / abs(t0) - 1, 15)}")
    check("L_and_R_only_replacements_differ", abs(t_wl - t_wr) > mp.mpf("1e-30"),
          f"tr(qJ) - tr(q^-1 J) = {mp.nstr(t_wl - t_wr, 15)}")
    # trace is linear in each letter: replacing D(1) by U(1) vs by qJ_1 differ by
    # tr of the word with (U - qJ) in that slot; U - qJ = h P- (proved in Lean).

    print("\nBAR OBSERVATION (not a claim)")
    # f(q) := tr^{z_D(q)}(Delta)(h(q)) as an exact function; test f(1/q) = -f(q)
    nfn, nfp = nf_of(word(N_TAIL)), nf_of(word(P_TAIL))
    zz = sp.Symbol("zz")
    f = tr([a - b for a, b in zip(nfn, nfp)], zz)
    q0 = Q_MP
    zD = lambda qq: qq ** 3 / (qq ** 2 + 1)

    def fnum(qq):
        hh = sp.Float(mp.nstr(qq - 1 / qq, 70), 70)
        zv = sp.Float(mp.nstr(zD(qq), 70), 70)
        return mp.mpf(str(sp.N(f.subs({h: hh, zz: zv}), 60)))
    fq, fqi = fnum(q0), fnum(1 / q0)
    print(f"    f(q0)   = {mp.nstr(fq, 20)}")
    print(f"    f(1/q0) = {mp.nstr(fqi, 20)}   (bar-odd would mean f(1/q0) = -f(q0))")
    print(f"    f(q0)+f(1/q0) = {mp.nstr(fq + fqi, 20)},  f(q0)-f(1/q0) = {mp.nstr(fq - fqi, 20)}")
    # letter-level bar: sigma+d(h) -> sigma - h + d(-h), same algebra, traced at z_D(q)

    def bar_letters(ls):
        return [(cc, sp.expand(-h * cc + dd.subs(h, -h)), g) for cc, dd, g in ls]
    tb = at_q0(tr([a - b for a, b in zip(nf_of(bar_letters(word(N_TAIL))),
                                         nf_of(bar_letters(word(P_TAIL))))], ZD))
    print(f"    tr^zD(bar Delta) = {mp.nstr(tb, 20)}   vs tr^zD(Delta) = {mp.nstr(t0, 20)}")
    check("letter_bar_at_zD_q_equals_trace_at_inverse_q",
          abs(tb - fqi) < mp.mpf("1e-40"), f"|diff| = {mp.nstr(abs(tb - fqi), 5)}")
    check("trace_is_not_bar_odd", abs(fq + fqi) > mp.mpf("1e-3"),
          f"f(q0) + f(1/q0) = {mp.nstr(fq + fqi, 15)}")
    check("bar_maps_u_to_d_fixes_ud",
          bar_letters([U(0)])[0][1] == -h and sp.expand(bar_letters([UD(0)])[0][1] + h / 2) == 0
          and bar_letters([D(0)])[0][1] == 0)

    ok = all(r[1] for r in RESULTS)
    print(f"\n{sum(r[1] for r in RESULTS)}/{len(RESULTS)} checks pass")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
