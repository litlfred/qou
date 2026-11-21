#!/usr/bin/env python3
"""qbeta_d_eigenphase_real_or_imaginary_probe.py -- is the convention-D N=1
eigenphase REAL (factor cos <= 1) or IMAGINARY (factor cosh >= 1)?

Beans `qou-cds1` (the c_k ladder under convention D) and `qou-pdix` (the N=1
phase). Lean companion:
`folio/quantum-observable-universe/lean/QOU/QBeta/DEigenphaseRealOrImaginary.lean`.

DIAGNOSTIC ONLY. Nothing is fitted, no element or cell is selected, nothing is
wired into production, the dashboard or any witness other than this one.

## Why the question is live

On the owner-ruled base (eps := tr_M at z_D, ruling 2026-09-08) the required
correction factor F_required = Q_codata / Q_base EXCEEDS 1 in every scored cell
(1.17 to 1.76; `qbeta_ladder_form_cannot_reach_ruled_base_probe.py`, PR #8098).
The ladder's N=1 factor is cos(alpha - u/2) <= 1 for every REAL alpha, so the
only ladder-side lever above 1 is an IMAGINARY phase alpha = i a, for which
cos(i a) = cosh a >= 1. The 2026-08-31 obstruction
(`HolonomySpectrumSignObstruction.lean`: real spectrum => cosh >= 1) excluded
that route on the RETIRED z = 1 base, where F_required < 1; on the ruled base
the same fact points the other way and re-opens it. This probe asks whether
anything the corpus derives makes the D phase imaginary.

## What "eigenphase" can mean, and what each reading gives

The Lean companion proves the classification this probe applies:

  (L1) A 2x2 block M with det M > 0 has half-normalised trace
       t = tr M / (2 sqrt det M). Its eigenphase phi (eigenvalues
       sqrt(det) e^{+-i phi}) is REAL iff t^2 <= 1 (complex-conjugate
       spectrum), and IMAGINARY, phi = i a with t = cosh a, iff t >= 1
       (real positive spectrum). The N=1 factor t exceeds 1 ONLY in the
       second case. [`factor_gt_one_iff_imaginary_phase` family]
  (L2) A phase f(q) with REAL coefficients that is BAR-ODD, f(1/q) = -f(q),
       is real on the real q-axis and purely imaginary on |q| = 1.
       So cos(f) is <= 1 at real q and >= 1 (a cosh) on the unit circle.
       [`bar_odd_real_coeff_im_on_circle`]
  (L3) The ladder phase alpha_D = (z_D - 1) h / 2 is a real rational function
       of q; for 1 < q with q^3 < q^2 + 1 (which holds at q_0) it is strictly
       negative and hence REAL and nonzero. It vanishes exactly where
       q^3 = q^2 + 1. Its bar-odd part beta_D = alpha_D - h^2/4 is bar-odd.
       [`alphaD_neg`, `alphaD_bar_sum`]

Measured here, at the proton pin, 60 dps:

  (1) the V_(2,1) block of every scored Delta (the only >= 2-dim irrep of
      H_3(q), hence the only place a matrix eigenphase can live): its trace,
      determinant, discriminant and phase type;
  (2) that convention D enters ONLY through the scalar Markov weights
      w_lambda(z) -- the block itself is z-free -- and that the D trace
      already CONTAINS the block's trace, so any cosh in it is counted once
      already;
  (3) alpha_D and beta_D at q_0 (real), and beta_D on the Wick-rotated slice
      q = exp(i log q_0) (purely imaginary), with the cosh it would give,
      against arccosh(F_required) per cell.

## Scope

(a) for every number. (b) only where the Lean companion supplies the
invariant: real phase => factor <= 1 (Real.cos_le_one); bar-odd real-coefficient
phase => real on the real axis (L2). It does NOT claim no imaginary phase can
be derived; it says which readings the corpus carries and what each gives.

## Precision

sympy exact in Q(q) for the representation; mpmath at 60 dps for every
readout. No float64: no `float(` outside display, no `math.`, no `statistics`.
"""
from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations/substrate", "computations", "tools/qou-substrate/python"):
    sys.path.insert(0, os.path.join(ROOT, _p))

import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from codata_2022_source import M_E_MEV, Q_BETA_MEV_AME  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = 60
set_compute_dps(DPS)
mp.mp.dps = DPS

# ---- the census's candidate constructors: imported, never re-implemented ----
_CEN = os.path.join(ROOT, "computations", "qbeta",
                    "qbeta_delta_candidate_census_probe.py")
_spec = importlib.util.spec_from_file_location("_census", _CEN)
_census = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_census)
H_SYM = _census.h                       # the census's symbolic h

q = sp.Symbol("q", positive=True)
zs = sp.Symbol("z")
HQ = q - 1 / q                          # h as a function of q

Q0 = sp.Rational(Q_50_DIGIT_STR)
MP_Q0 = mp.mpf(Q_50_DIGIT_STR)
MP_ME = mp.mpf(str(M_E_MEV))
MP_QB = mp.mpf(str(Q_BETA_MEV_AME))
E0 = MP_ME / (MP_Q0 * (MP_Q0 - 1))      # order-zero E_0 (the probe's base)

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {detail}\n")


def mpv(e) -> mp.mpf:
    """Exact sympy expression in q -> value at q_0, 60 dps. Never float64."""
    return mp.mpf(str(sp.N(sp.sympify(e).subs(q, Q0), DPS + 5)))


# --------------------------------------------------------------- V_(2,1)
# Hecke convention of the census (hm_sym): sigma^2 = h sigma + 1, eigenvalues
# q and -1/q. sigma_0 diagonal; sigma_1 fixed by tr = h, det = -1 and the
# braid relation. Off-diagonal: b = 1, c = a d + 1 (tr / det are similarity
# invariants, so this gauge choice changes no number reported below).
S0 = sp.Matrix([[q, 0], [0, -1 / q]])
_a, _d = sp.symbols("a d")
_sol = sp.solve([_a + _d - HQ, q * _a - _d / q + 1], [_a, _d], dict=True)[0]
A1, D1 = sp.simplify(_sol[_a]), sp.simplify(_sol[_d])
S1 = sp.Matrix([[A1, 1], [sp.simplify(A1 * D1 + 1), D1]])
I2 = sp.eye(2)
#: the census's NF basis order [gamma, sigma_0, sigma_1, L-, L+, e^-], with
#: right multiplication (hm_sym): L- = sigma_1 sigma_0, L+ = sigma_0 sigma_1.
BASIS_21 = [I2, S0, S1, S1 * S0, S0 * S1, S0 * S1 * S0]
BASIS_3 = [1, q, q, q ** 2, q ** 2, q ** 3]               # sigma -> q
BASIS_111 = [1, -1 / q, -1 / q, 1 / q ** 2, 1 / q ** 2, -1 / q ** 3]  # sigma -> -1/q


def rho21(nf, swap=False):
    nf = [sp.sympify(c).subs(H_SYM, HQ) for c in nf]
    if swap:                                   # L- <-> L+ (census slot warning)
        nf = nf[:3] + [nf[4], nf[3]] + nf[5:]
    M = sp.zeros(2, 2)
    for c, B in zip(nf, BASIS_21):
        M += c * B
    return M.applyfunc(sp.simplify)


def chi_scalar(nf, basis):
    return sp.simplify(sum(sp.sympify(c).subs(H_SYM, HQ) * b
                           for c, b in zip(nf, basis)))


def tr_markov(nf, zz):
    """The census trace vector TR(z) = [1, z, z, z^2, z^2, z(hz+1)]."""
    tv = [1, zz, zz, zz ** 2, zz ** 2, zz * (HQ * zz + 1)]
    return sp.simplify(sum(sp.sympify(c).subs(H_SYM, HQ) * t
                           for c, t in zip(nf, tv)))


def classify(trv: mp.mpf, detv: mp.mpf):
    """Eigenphase type of a real 2x2 block (Lean companion, L1)."""
    disc = trv ** 2 - 4 * detv
    if detv > 0:
        t = trv / (2 * mp.sqrt(detv))
        if disc < 0:
            return "REAL phase (complex-conjugate spectrum)", t, disc
        if t > 0:
            return "IMAGINARY phase (real positive spectrum): t = cosh a", t, disc
        return "pi + i a (real negative spectrum)", t, disc
    if detv < 0:
        return "pi/2 + i a (real spectrum of opposite signs)", None, disc
    return "degenerate (det = 0)", None, disc


def main() -> int:
    print("=" * 78)
    print(" Is the convention-D N=1 eigenphase real or imaginary?")
    print("=" * 78 + "\n")

    zD = q ** 3 / (q ** 2 + 1)
    mp_zD = mpv(zD)
    h0 = mpv(HQ)

    # ---- 0. the representation is a genuine H_3(q) representation ----------
    hecke = all(sp.simplify(S * S - (HQ * S + I2)) == sp.zeros(2, 2) for S in (S0, S1))
    braid = sp.simplify(S0 * S1 * S0 - S1 * S0 * S1) == sp.zeros(2, 2)
    chi_cox = sp.simplify((S0 * S1).trace())
    check("v21_is_a_hecke_representation",
          hecke and braid and chi_cox == -1,
          "sigma^2 = h sigma + 1 for both generators, the braid relation holds "
          "exactly, and chi_(2,1)(sigma_0 sigma_1) = -1 (the standard Hecke "
          "character value). Exact in Q(q).")

    # ---- 1. the Markov weights: D enters as SCALARS only -------------------
    w3, w21, w111 = sp.symbols("w3 w21 w111")
    eqs = []
    for k in range(6):
        e = [0] * 6
        e[k] = 1
        eqs.append(sp.Eq(w3 * chi_scalar(e, BASIS_3)
                         + w21 * sp.simplify(rho21(e).trace())
                         + w111 * chi_scalar(e, BASIS_111),
                         tr_markov(e, zs)))
    wsol = sp.solve(eqs, [w3, w21, w111], dict=True)
    ok_w = len(wsol) == 1
    W = wsol[0] if ok_w else {}
    w111_D = sp.simplify(W.get(w111, sp.nan).subs(zs, zD)) if ok_w else sp.nan
    check("markov_trace_is_a_weighted_character_sum_and_D_kills_1_1_1",
          ok_w and w111_D == 0,
          "TR(z) = w_3(z) chi_3 + w_21(z) chi_21 + w_111(z) chi_111 holds on all "
          "six NF basis elements with a UNIQUE weight vector, and w_111(z_D) = 0 "
          "exactly (convention D is the two-row trace). So D changes only the "
          "three scalars w_lambda; the V_(2,1) block of an element does not "
          "contain z at all. Weights: w_3 = "
          f"{sp.factor(W.get(w3, sp.nan))}, w_21 = {sp.factor(W.get(w21, sp.nan))}, "
          f"w_111 = {sp.factor(W.get(w111, sp.nan))}.")

    # ---- 2. the scored elements' V_(2,1) blocks -----------------------------
    cands = {
        "nuc9": _census.delta(_census.nuc9("n"), _census.nuc9("p")),
        "nuc11_interleaved": _census.delta(_census.nuc11_interleaved("n"),
                                           _census.nuc11_interleaved("p")),
        "nuc11_gen_grouped": _census.delta(_census.nuc11_gen_grouped("n"),
                                           _census.nuc11_gen_grouped("p")),
        "Delta_S": [H_SYM ** 2 / 2, -H_SYM / 2, -H_SYM / 2, 0, 0, 0],
    }
    # calibration targets: tr^{z_D} from qbeta-option-e-required-level witness
    trD_committed = {
        "nuc9": "-0.1290754381703192805582969",
        "nuc11_interleaved": "-0.1541948850472397056592555",
        "nuc11_gen_grouped": "-0.1580160043414912980550614",
        "Delta_S": "-0.106235639848092790892142",
    }
    rows = []
    calib_ok, swap_ok, decomp_ok = True, True, True
    print("  element               tr V21        det V21        disc          type")
    for name, nf in cands.items():
        M = rho21(nf)
        Msw = rho21(nf, swap=True)
        tr21, det21 = sp.simplify(M.trace()), sp.simplify(M.det())
        trv, detv = mpv(tr21), mpv(det21)
        swap_ok &= abs(mpv(Msw.det()) - detv) < mp.mpf(10) ** -50 and \
            abs(mpv(Msw.trace()) - trv) < mp.mpf(10) ** -50
        kind, t, disc = classify(trv, detv)
        c3, c111 = chi_scalar(nf, BASIS_3), chi_scalar(nf, BASIS_111)
        trD = mpv(tr_markov(nf, zD))
        calib_ok &= abs(trD - mp.mpf(trD_committed[name])) < mp.mpf(10) ** -24
        recomposed = mpv(W[w3].subs(zs, zD) * c3 + W[w21].subs(zs, zD) * tr21
                         + W[w111].subs(zs, zD) * c111)
        decomp_ok &= abs(recomposed - trD) < mp.mpf(10) ** -50
        F_req = MP_QB / (abs(trD) * E0)
        rows.append({
            "element": name, "tr_V21": mp.nstr(trv, 30), "det_V21": mp.nstr(detv, 30),
            "disc_V21": mp.nstr(disc, 30), "phase_type": kind,
            "half_normalised_trace": (mp.nstr(t, 30) if t is not None else None),
            "chi_3": mp.nstr(mpv(c3), 30), "tr_zD": mp.nstr(trD, 30),
            "V21_share_of_tr_zD": mp.nstr(mpv(W[w21].subs(zs, zD)) * trv / trD, 20),
            "F_required_order_zero_E0": mp.nstr(F_req, 20),
            "arccosh_F_required": mp.nstr(mp.acosh(F_req), 20),
        })
        print(f"  {name:<20} {mp.nstr(trv, 10):>12} {mp.nstr(detv, 10):>14} "
              f"{mp.nstr(disc, 10):>13}   {kind}")
    print()

    check("calibration_reproduces_committed_tr_zD",
          calib_ok,
          "tr^{z_D}(Delta) for all four elements reproduces "
          "qbeta-option-e-required-level.witness.json to 1e-24, so the elements "
          "are the dashboard's own.")
    check("block_type_is_independent_of_the_L_slot_convention",
          swap_ok,
          "tr and det of every V_(2,1) block are unchanged under the census's "
          "L-/L+ slot swap (reversal is a transpose in this rep).")
    check("D_trace_already_contains_the_V21_block",
          decomp_ok,
          "for every element, tr^{z_D}(Delta) = w_3(z_D) chi_3 + w_21(z_D) "
          "tr(V21 block) exactly. If a block had real positive spectrum, its "
          "cosh would ALREADY be inside eps_D; multiplying a separate cosh on "
          "top would count it twice.")
    n_imag = sum(1 for r in rows if r["phase_type"].startswith("IMAGINARY"))
    types = sorted({r["phase_type"] for r in rows})
    check("no_scored_element_has_an_imaginary_V21_eigenphase",
          n_imag == 0,
          f"phase types found: {types}. {n_imag} of {len(rows)} blocks have real "
          "positive spectrum, which is the only case where the half-normalised "
          "trace is a cosh >= 1. Delta_S's block is traceless with det = -h^2/4: "
          "eigenvalues +-h/2, phase exactly pi/2.")

    # ---- 3. the ladder's own phase, on both real slices --------------------
    alphaD = (zD - 1) * HQ / 2
    betaD = alphaD - HQ ** 2 / 4
    bar = lambda e: sp.simplify(e.subs(q, 1 / q))  # noqa: E731
    bar_sum_ok = sp.simplify(alphaD + bar(alphaD) - HQ ** 2 / 2) == 0
    bar_odd_ok = sp.simplify(betaD + bar(betaD)) == 0
    a0, b0 = mpv(alphaD), mpv(betaD)
    zero_locus = sp.simplify(sp.numer(sp.together(zD - 1)))
    check("alpha_D_is_real_and_negative_at_q0",
          a0 < 0 and bar_sum_ok and bar_odd_ok,
          f"alpha_D(q_0) = {mp.nstr(a0, 25)} (real, < 0); its zero locus is "
          f"{zero_locus} = 0, the real root of which is ~1.46557 > q_0. "
          f"alpha_D(q) + alpha_D(1/q) = h^2/2 exactly (the D bar defect), and "
          f"beta_D = alpha_D - h^2/4 = {mp.nstr(b0, 25)} is exactly bar-odd. "
          "Both are real at real q, so the ladder factor is a cos, <= 1.")

    # Wick-rotated slice: q = exp(i eta_0), eta_0 = log q_0 (NOT a physical
    # evaluation -- the substrate is real by the CAL-2 ruling; this only
    # measures what the cosh reading would give if the phase lived there).
    eta0 = mp.log(MP_Q0)
    qc = mp.expj(eta0)
    hc = qc - 1 / qc
    zDc = qc ** 3 / (qc ** 2 + 1)
    aDc = (zDc - 1) * hc / 2
    bDc = aDc - hc ** 2 / 4
    check("beta_D_is_purely_imaginary_on_the_unit_circle_alpha_D_is_not",
          abs(mp.re(bDc)) < mp.mpf(10) ** -50 and abs(mp.re(aDc)) > mp.mpf(10) ** -6,
          f"at q = exp(i log q_0): beta_D = {mp.nstr(bDc, 20)} (real part "
          f"{mp.nstr(mp.re(bDc), 3)}), alpha_D = {mp.nstr(aDc, 20)}. The bar-odd "
          "part turns imaginary there, as the Lean lemma says it must; alpha_D "
          "itself does not, because of its bar defect h^2/2. So under D only "
          "the bar-odd projection has a definite real/imaginary type.")

    cosh_wick = mp.cosh(mp.im(bDc))
    need = [mp.acosh(MP_QB / (abs(mpv(tr_markov(nf, zD))) * E0)) for nf in cands.values()]
    ratio_min = min(need) / abs(mp.im(bDc))
    check("even_the_wick_rotated_cosh_is_far_too_small",
          cosh_wick < min(MP_QB / (abs(mpv(tr_markov(nf, zD))) * E0)
                          for nf in cands.values()),
          f"cosh(|Im beta_D|) on that slice = {mp.nstr(cosh_wick, 20)}; the "
          f"needed phase a = arccosh(F_required) ranges "
          f"{mp.nstr(min(need), 8)} to {mp.nstr(max(need), 8)} across the four "
          f"order-zero cells, against |beta_D| = {mp.nstr(abs(mp.im(bDc)), 8)}: "
          f"at least {mp.nstr(ratio_min, 6)}x too small. Diagnostic only; no "
          "cell is chosen, none is scored.")

    # ---- 4. CURRENT RULINGS (owner, 2026-11-20 / 11-21) ---------------------
    # Section 2 uses the census elements and the one-term z_D trace on an
    # order-zero E_0. All three are SUPERSEDED (docs/coordination/
    # owner-rulings.md): the photon is gamma = 1 + phi0 s0 + phi1 s1 +
    # phi01 s0 s1^-1, Q_beta comes from gamma-gamma pair production on the
    # base V^3 = (s0 s1^-1)^3 (the same element for p and n), and the scored
    # cell is the T^3 weight split eps_flavour(V^3) times the canonical
    # (tower-summed) E_0. On three quark strands the two-term Lagrangian
    # trace's connected part vanishes for every word
    # (BetaRoutesTwoTerm.pairSum_eq_of_total_eq), so the two-term value of
    # this cell equals the one-term value. Section 2 rows are kept, labelled.
    for r in rows:
        r["superseded"] = ("census element, one-term trace, order-zero E_0; "
                           "replaced by the V^3 weight-split cell below")
    Vb = sp.simplify(S0 * S1.inv())
    V3 = sp.simplify(Vb ** 3)
    cur_rows = []
    cur_types = []
    for nm, M in (("V = s0 s1^-1 (photon vertex)", Vb), ("V^3 (scored base)", V3),
                  ("V^-3", sp.simplify(V3.inv()))):
        trv, detv = mpv(M.trace()), mpv(M.det())
        kind, t, disc = classify(trv, detv)
        cur_types.append(kind)
        cur_rows.append({"element": nm, "tr_V21": mp.nstr(trv, 30),
                         "det_V21": mp.nstr(detv, 30), "disc_V21": mp.nstr(disc, 30),
                         "phase_type": kind,
                         "half_normalised_trace": (mp.nstr(t, 30) if t is not None else None)})
        print(f"  {nm:<30} tr {mp.nstr(trv, 12):>16}  det {mp.nstr(detv, 6):>6}  {kind}")
    print()
    check("current_base_V3_has_no_imaginary_V21_eigenphase",
          not any(k.startswith("IMAGINARY") for k in cur_types),
          f"V_(2,1) blocks of the corrected-photon vertex, V^3 and V^-3: "
          f"{cur_types}. det V = det(s0) det(s1)^-1 = 1, so V^3 is in SL_2; "
          "a cosh >= 1 would need real positive spectrum, which none has.")

    # exact form of the eigenphase (QOU.QBeta.PhotonVertexEigenphase)
    trV_ok = sp.simplify(Vb.trace() + (1 + HQ ** 2)) == 0
    trV3_ok = sp.simplify(2 - V3.trace() - HQ ** 4 * (q ** 2 + 1 + q ** -2)) == 0
    theta3 = 2 * mp.asin(mpv(HQ ** 2 * sp.sqrt(q ** 2 + 1 + q ** -2) / 2))
    theta3_direct = mp.acos(mpv(V3.trace()) / 2)
    check("vertex_eigenphase_exact_form",
          trV_ok and trV3_ok and abs(theta3 - theta3_direct) < mp.mpf(10) ** -50,
          "tr V = -(1 + h^2) and 2 - tr V^3 = h^4 [3]_q exactly in Q(q), so the "
          "V^3 eigenphase is theta = 2 arcsin(h^2 sqrt([3]_q)/2) = "
          f"{mp.nstr(theta3, 25)} at q_0: real, O(h^2). A ladder factor built on it "
          f"is cos(theta) = {mp.nstr(mp.cos(theta3), 20)} < 1.")

    # scored cell: eps_flavour(V^3) = (q^2-1) P(q) / (q^4 (q^2+1)^3)
    # (QOU.QBeta.FlavourWeightSplit.epsFlavour_V3_eq, sorry-free)
    Pq = q**12 - 3*q**10 + 3*q**8 - 5*q**6 + 3*q**4 - 3*q**2 + 1
    epsF = (q**2 - 1) * Pq / (q**4 * (q**2 + 1)**3)
    epsF0 = mpv(epsF)
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import qbeta_e0 as _e0
    E0c = mp.mpf(_e0.canonical())
    QB_scored = abs(epsF0) * E0c
    wpath = (Path(__file__).resolve().parents[1] / "probes" /
             "qbeta_flavour_weight_split" / "qbeta-flavour-weight-split.witness.json")
    wtxt = wpath.read_text()
    import json as _json
    def _find_v3(node):
        if isinstance(node, dict):
            if node.get("element") == "V^3" and "eps_flavour" in node:
                return node
            node = list(node.values())
        if isinstance(node, list):
            for x in node:
                hit = _find_v3(x)
                if hit is not None:
                    return hit
        return None
    v3w = _find_v3(_json.loads(wtxt))
    xok = v3w is not None \
        and abs(epsF0 - mp.mpf(v3w["eps_flavour"])) < mp.mpf(10) ** -40 \
        and abs(QB_scored - mp.mpf(v3w["Q_beta_MeV"])) < mp.mpf(10) ** -25
    # whole gamma-gamma tower V^{3k}: eps = -h (1 + 2 cos k theta) / [2]^3
    # (W = V_3 + V_(2,1); V acts as 1 on V_3). Checked against the committed
    # V^3, V^6, V^9 values; bounded by 3h/[2]^3 for every k
    # (PhotonVertexEigenphase.tower_bracket_le_three).
    two_q = mpv(q + 1 / q)
    tower_ok = True
    tower_rows = []
    def _all_rows(node):
        if isinstance(node, dict):
            if str(node.get("element", "")).startswith("V^") and "eps_flavour" in node:
                yield node
            for v in node.values():
                yield from _all_rows(v)
        elif isinstance(node, list):
            for v in node:
                yield from _all_rows(v)
    seen = set()
    for r in _all_rows(_json.loads(wtxt)):
        k = int(r["element"][2:]) // 3
        if k in seen:
            continue
        seen.add(k)
        pred = -h0 * (1 + 2 * mp.cos(k * theta3)) / two_q ** 3
        tower_ok &= abs(pred - mp.mpf(r["eps_flavour"])) < mp.mpf(10) ** -35
        tower_rows.append({"k": k, "eps_closed_form": mp.nstr(pred, 30),
                           "eps_committed": r["eps_flavour"]})
    QB_sup = 3 * h0 * E0c / two_q ** 3
    check("gamma_gamma_tower_closed_form_and_bound",
          tower_ok and len(seen) >= 3 and MP_QB / QB_sup > 1,
          f"eps_flavour(V^(3k)) = -h (1 + 2 cos k theta)/[2]^3 reproduces the "
          f"committed k = {sorted(seen)} to 1e-35. Since |1 + 2 cos| <= 3, every "
          f"tower member and every probability-weighted average of them gives "
          f"Q_beta <= 3h E_0/[2]^3 = {mp.nstr(QB_sup, 12)} MeV, i.e. F_required "
          f">= {mp.nstr(MP_QB / QB_sup, 8)}. A factor above 1 needs weights "
          "summing to more than 2.4 (a multiplicity), which the corpus does not "
          "derive.")

    F_cur = MP_QB / QB_scored
    a_need = mp.acosh(F_cur)
    short = a_need / abs(mp.im(bDc))
    check("scored_cell_reproduced_and_cosh_lever_still_far_too_small",
          xok and F_cur > 1 and cosh_wick < F_cur,
          f"|eps_flavour(V^3)| E_0^canonical = {mp.nstr(QB_scored, 15)} MeV "
          f"(matches qbeta-flavour-weight-split.witness.json); F_required = "
          f"{mp.nstr(F_cur, 12)} > 1, so a real ladder phase (factor <= 1) "
          f"cannot reach it. A cosh reading needs a = {mp.nstr(a_need, 10)}, "
          f"against the Wick-rotated |beta_D| = {mp.nstr(abs(mp.im(bDc)), 8)}: "
          f"{mp.nstr(short, 6)}x short. Diagnostic only; CODATA in this ratio only.")

    allp = all(ok for _, ok, _ in RESULTS)
    print(f"  {sum(ok for _, ok, _ in RESULTS)}/{len(RESULTS)} checks passed")

    wb = WitnessBuilder("qbeta-d-eigenphase-real-or-imaginary", engine="mpmath")
    for nm, ok, det in RESULTS:
        wb.add_assertion(nm, computed="PASS" if ok else "FAIL", expected="PASS",
                         tolerance="exact", source=det)
    wb.save({
        "description": (
            "Diagnostic for beans qou-cds1 / qou-pdix: is the convention-D N=1 "
            "eigenphase real (cos <= 1) or imaginary (cosh >= 1)? (1) No scored "
            "Delta has a V_(2,1) block with real positive spectrum, the only "
            "case giving a cosh. (2) Convention D enters only through the scalar "
            "Markov weights, w_111(z_D) = 0, and the D trace already contains "
            "the V_(2,1) block, so a separate cosh would double count. (3) The "
            "ladder phase alpha_D and its bar-odd part beta_D are real at real "
            "q; beta_D is purely imaginary on |q| = 1, but even there its cosh "
            "is far below every F_required. No fit, no selection, no wiring."),
        "beans": ["qou-cds1", "qou-pdix"],
        "q0Anchor": "proton",
        "q0Value": mp.nstr(MP_Q0, 50),
        "E0_order_zero_MeV": mp.nstr(E0, 30),
        "markov_weights": {str(k): str(sp.factor(v)) for k, v in W.items()},
        "alpha_D_q0": mp.nstr(a0, 40),
        "beta_D_q0": mp.nstr(b0, 40),
        "beta_D_unit_circle": mp.nstr(bDc, 30),
        "alpha_D_unit_circle": mp.nstr(aDc, 30),
        "cosh_wick": mp.nstr(cosh_wick, 30),
        "elements_superseded": rows,
        "current_rulings": {
            "rulings": "photon s0 s1^-1 (2026-11-20); Q_beta from gamma-gamma, "
                       "T^3 weight-split scored cell (2026-11-20); two-term "
                       "Lagrangian trace on all beta routes (2026-11-21)",
            "two_term_note": "connected two-term part is 0 on three quark "
                             "strands (BetaRoutesTwoTerm.pairSum_eq_of_total_eq)",
            "elements": cur_rows,
            "theta_V3": mp.nstr(theta3, 40),
            "tower": tower_rows,
            "Q_beta_tower_sup_MeV": mp.nstr(QB_sup, 30),
            "eps_flavour_V3": mp.nstr(epsF0, 40),
            "E0_canonical_MeV": mp.nstr(E0c, 30),
            "Q_beta_scored_MeV": mp.nstr(QB_scored, 30),
            "F_required": mp.nstr(F_cur, 20),
            "arccosh_F_required": mp.nstr(a_need, 20),
            "cosh_lever_shortfall": mp.nstr(short, 10),
        },
        "scope": ("(a) for every number; (b) only for real phase => factor <= 1 "
                  "and bar-odd real-coefficient phase => real on the real axis, "
                  "both proved in DEigenphaseRealOrImaginary.lean."),
    })
    return 0 if allp else 1


if __name__ == "__main__":
    raise SystemExit(main())
