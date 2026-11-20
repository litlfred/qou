#!/usr/bin/env python3
"""qou-99qc / Option E: every candidate `Delta` the corpus has ever built needs
a Wenzl level, and NOT ONE of them needs an admissible level.

# Ref: computations/qbeta/qbeta_delta_candidate_census_probe.py   (the candidates)
# Ref: computations/qbeta/qbeta_augmentation_is_a_markov_trace_probe.py  (z = q is a Markov trace)
# Ref: computations/qbeta/qbeta_wenzl_level_decides_the_functional_probe.py (z(r))
# Ref: docs/audits/2026-09-05-qbeta-functional-decision-options.md  (Option E)
# Ref: computations/probes/qbeta_offl_ratio_candidates_unfalsifiable_probe.py (method precedent)

WHAT OPTION E IS, AND WHY IT LOOKED UNBOUNDED. The decision document's Option E
is "keep an admissible functional and find the element it should act on", and it
prices the cost as "Real research. Unbounded." That pricing is what this probe
attacks -- not by searching for an element, which would be selection against the
target and therefore a fit under AGENTS.md "NO FITTING", but by measuring what
the corpus's OWN already-constructed candidates require.

THE REFRAME. `Q_beta = |eps(Delta)| * E_0`. On the H_3(q) normal-form basis the
Markov trace at parameter z is the vector

    TR(z) = [1, z, z, z^2, z^2, z(h z + 1)]      h = q - 1/q

so for a FIXED element `Delta` the prediction is a QUADRATIC in z. Requiring it
to reproduce the measured Q_beta therefore does not leave a free choice: it
determines z, up to which of two roots and which sign. So

    "which element Delta"   and   "which functional eps"

are not two independent questions -- each candidate element NAMES the functional
it would need. And by the Wenzl level relation (Q^r = z_W/(1 - Q + z_W), Q = q^2,
z_W = q z) that functional is a LEVEL:

    z(r) = q^(2r-1) (q^2 - 1) / (q^(2r) - 1),   r = 1 -> augmentation,
                                                r = 2 -> convention D.

Admissibility is exactly `r in {1, 2}` (integer levels 1 and 2 are the only ones
whose weight support is a Wenzl truncation of H_3; r = 1.1238831038, the level the
published closed form needs, is why `z = 1` is inadmissible). So Option E has a
SHARP acceptance test, computable per candidate in closed form:

    does this Delta require r = 1 or r = 2, to within experimental sigma?

WHAT IS MEASURED. Every candidate in `qbeta_delta_candidate_census_probe` --
the 9-crossing `build_nucleon_nf`, the 11-crossing interleaved `build_atom_nf_exact`,
the 11-crossing gen-grouped `nucleon_gen_chains`, the short normal-form `Delta_S`,
and all 16 readings of the properties blocks' own recipe -- is imported, not
re-derived, and its required level is solved.

WHAT THIS IS NOT. It is not a search: no element is proposed, none is selected,
and the 16-variant family is reported as a RANGE precisely because picking the
best-landing member is the fit this repo forbids. It wires nothing. Scope-(a):
it says these candidates do not close Option E, not that no element can.

THE FALSIFIABILITY HALF. The 16 constructed variants differ only by choices the
source blocks never make (which generator each quark crossing sits on, and the
Hopf orientation). If that unstated freedom moves the required level by more than
the gap between admissible levels, then a candidate landing on r = 1 or r = 2
would be an artifact of the assignment rather than evidence -- the shape of
argument `qou-offl` uses. The spread is measured, not asserted.

WHAT CAME OUT, and neither was the thing being looked for.

1. LEVEL 1 IS BLIND TO BRAID ORDER. The augmentation is multiplicative, so it is
   a product over the letters of a word and the ORDER drops out. Measured: the
   interleaved and gen-grouped 11-crossing models carry the same typed-crossing
   multiset in a different order and have IDENTICAL augmentation to 20 digits,
   while their convention-D traces differ in the third. All 16 readings of the
   properties blocks' recipe likewise share one augmentation value. So an Option E
   element that differs from an existing one only by re-ordering or by a different
   quark-generator assignment is, at level 1, the SAME NUMBER. To move the level-1
   value you must change the crossing multiset, not the braid.

2. THE BRACKETING IS UNIVERSAL, AND THAT IS THE OBSTRUCTION. On every candidate,
   level 1 OVERSHOOTS Q_beta and level 2 UNDERSHOOTS it. By the intermediate value
   theorem the required level then lies strictly between the two admissible ones --
   which is exactly why it is never one of them. Measured required levels run
   1.1258 to 1.4912; the closest approach to an admissible level is 0.126 away.
   This turns Option E's acceptance test into something an author can aim at:

       AN ELEMENT THAT CLOSES OPTION E MUST HAVE ITS LEVEL-1 AND LEVEL-2 VALUES
       ON THE SAME SIDE OF Q_beta.

   No re-ordering or re-assignment within the existing families can do it, and a
   candidate that brackets can be rejected without solving anything.

ARITHMETIC. Exact sympy in h over Q, the pin as an exact Rational from the
50-digit proton string, readout through mpmath at 60 dps. No float64 anywhere
(AGENTS.md NO-FLOAT64; probes are not exempt).

Run: python3 -u computations/qbeta/qbeta_option_e_required_level_probe.py \
       2>&1 | tee /tmp/qbeta_option_e_required_level.log
"""
from __future__ import annotations

import importlib.util
import itertools
import os
import sys
import warnings

import sympy as sp

warnings.filterwarnings("ignore")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations/substrate", "computations", "tools/pyhecke/python",
           "tools/qou-substrate/python"):
    sys.path.insert(0, os.path.join(ROOT, _p))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

set_compute_dps(60)
mp.mp.dps = 60

# ---- reuse the census's candidate constructors; do not reimplement them ----
_CEN = os.path.join(ROOT, "computations", "qbeta",
                    "qbeta_delta_candidate_census_probe.py")
_spec = importlib.util.spec_from_file_location("_census", _CEN)
_census = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_census)

h = _census.h                      # the symbolic h used by the candidates
hm = _census.hm                    # hoefsmit/NF multiply
ZERO, ONE = _census.ZERO, _census.ONE

q = sp.Symbol("q", positive=True)
z = sp.Symbol("z")

Q0 = sp.Rational(Q_50_DIGIT_STR)
H0 = Q0 - 1 / Q0

# ---- experimental / calibration inputs, from the corpus's own tables -------
from codata_2022_source import (  # noqa: E402
    M_E_MEV, Q_BETA_MEV_AME, Q_BETA_MEV_AME_ERR,
)

MP_Q0 = Q_MP
MP_ME = mp.mpf(str(M_E_MEV))
MP_QB = mp.mpf(str(Q_BETA_MEV_AME))
MP_QB_ERR = mp.mpf(str(Q_BETA_MEV_AME_ERR))

E0 = MP_ME / (MP_Q0 * (MP_Q0 - 1))            # base energy, MeV
TARGET = MP_QB / E0                            # the required |eps(Delta)|
SIGMA_REL = MP_QB_ERR / MP_QB                  # 779.7 ppb

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


def at_q0(e) -> mp.mpf:
    """Exact h -> h(q_0), then a 60-dps readout. Never float64."""
    return mp.mpf(str(sp.N(sp.sympify(e).subs(h, H0), 60)))


# ---------------------------------------------------------------- the trace
def tr_symbolic(nf, zz):
    """tr_M^z of an NF 6-vector, exact in h and zz.

    Slot order is the census's BASIS = [gamma, sigma_0, sigma_1, L-, L+, e^-].
    L+ and L- carry the same weight z^2, so the slot swap the census warns
    about cannot change this value -- but the order is taken from the census
    module rather than restated, so it cannot drift either.
    """
    hz = h * zz + 1
    tr_basis = [sp.Integer(1), zz, zz, zz ** 2, zz ** 2, zz * hz]
    return sp.expand(sum(c * t for c, t in zip(nf, tr_basis)))


def delta_of(model, *a, **kw):
    """Delta = neutron - proton, coordinatewise in the NF basis."""
    n = model("n", *a, **kw)
    p = model("p", *a, **kw)
    return [sp.expand(x - y) for x, y in zip(n, p)]


# --------------------------------------------------------- the level ladder
def z_of_level(r):
    """z(r) = q^(2r-1)(q^2-1)/(q^(2r)-1) at the proton pin, mpmath."""
    Q = MP_Q0
    return Q ** (2 * r - 1) * (Q ** 2 - 1) / (Q ** (2 * r) - 1)


def level_of_z(zv):
    """Invert z(r) numerically. Returns None when no real level exists."""
    try:
        return mp.findroot(lambda r: z_of_level(r) - zv, mp.mpf("1.5"))
    except Exception:
        for seed in ("0.5", "1.0", "2.0", "3.0", "5.0", "-1.0"):
            try:
                return mp.findroot(lambda r: z_of_level(r) - zv, mp.mpf(seed))
            except Exception:
                continue
        return None


def required_zs(nf):
    """Solve |tr^z(Delta)| = TARGET for z. Quadratic, both signs -> <=4 roots.

    Returns real roots only, as mpf, sorted.
    """
    expr = tr_symbolic(nf, z).subs(h, H0)
    poly = sp.Poly(sp.expand(expr), z)
    out = []
    for sgn in (1, -1):
        # coefficients as exact Rationals; the target enters as a 60-dps mpf,
        # so solve numerically in mpmath rather than mixing the two in sympy.
        cs = [mp.mpf(str(sp.N(c, 60))) for c in poly.all_coeffs()]
        cs = list(cs)
        cs[-1] = cs[-1] - sgn * TARGET
        try:
            roots = mp.polyroots(cs, maxsteps=200, extraprec=200)
        except Exception:
            continue
        for rt in roots:
            if abs(mp.im(rt)) < mp.mpf("1e-40"):
                out.append(mp.re(rt))
    return sorted(out)


def report(label: str, nf, w=None):
    """Print the per-candidate row and return its record."""
    net = at_q0(tr_symbolic(nf, sp.Integer(1)))
    aug = at_q0(tr_symbolic(nf, Q0))
    zD = Q0 ** 3 / (Q0 ** 2 + 1)
    trD = at_q0(tr_symbolic(nf, zD))
    rec = {
        "net_z1": mp.nstr(net, 25),
        "tr_aug_z_eq_q": mp.nstr(aug, 25),
        "tr_conv_D": mp.nstr(trD, 25),
        "pct_aug": mp.nstr((abs(aug) * E0 / MP_QB - 1) * 100, 8),
        "pct_D": mp.nstr((abs(trD) * E0 / MP_QB - 1) * 100, 8),
    }
    zs = required_zs(nf)
    levels = []
    for zv in zs:
        if zv <= 0:
            levels.append(None)
            continue
        levels.append(level_of_z(zv))
    rec["required_z"] = [mp.nstr(v, 20) for v in zs]
    rec["required_level"] = [(mp.nstr(v, 20) if v is not None else "no real level")
                             for v in levels]
    print(f"  {label:<34s} aug {rec['pct_aug']:>12s} %   D {rec['pct_D']:>12s} %")
    print(f"  {'':<34s} required levels r = "
          + ", ".join(rec["required_level"]))
    return rec, zs, levels


def admissible_level(rv, tol) -> bool:
    """Is this level an admissible one (1 or 2), within tolerance?"""
    if rv is None:
        return False
    return bool(min(abs(rv - 1), abs(rv - 2)) < tol)


def main() -> int:
    print("qou-99qc Option E — what level does each corpus candidate require?\n")
    print(f"  E_0            = {mp.nstr(E0, 25)} MeV")
    print(f"  Q_beta (AME)   = {mp.nstr(MP_QB, 12)} +- {mp.nstr(MP_QB_ERR, 4)} MeV"
          f"  (sigma = {mp.nstr(SIGMA_REL * 10**9, 6)} ppb)")
    print(f"  TARGET |eps|   = {mp.nstr(TARGET, 25)}\n")

    _census._assert_slots()
    check("census_slot_order_pinned", True,
          "L+/L- slots taken from the census module, not restated here")

    # ---- CHECK 0: the trace vector validates itself at z = q ---------------
    print("\nCHECK 0 — TR(z = q) reproduces the augmentation on the whole basis")
    aug_expected = [sp.Integer(1), q, q, q ** 2, q ** 2, q ** 3]
    hq = q - 1 / q
    tr_at_q = [sp.Integer(1), q, q, q ** 2, q ** 2, q * (hq * q + 1)]
    same = all(sp.simplify(a - b) == 0 for a, b in zip(aug_expected, tr_at_q))
    check("TR_at_z_eq_q_is_the_augmentation", same,
          "basis 1, s0, s1, s1s0, s0s1, s0s1s0 -> 1, q, q, q^2, q^2, q^3; "
          "q(hq+1) = q^3 identically")

    # ---- CHECK 1: the level ladder calibrates -----------------------------
    print("\nCHECK 1 — the level ladder z(r), against three known points")
    zD = MP_Q0 ** 3 / (MP_Q0 ** 2 + 1)
    check("z_of_level_1_is_q", abs(z_of_level(1) - MP_Q0) < mp.mpf("1e-45"),
          f"z(1) = {mp.nstr(z_of_level(1), 20)}")
    check("z_of_level_2_is_z_D", abs(z_of_level(2) - zD) < mp.mpf("1e-45"),
          f"z(2) = {mp.nstr(z_of_level(2), 20)} = q^3/(q^2+1)")
    r1 = level_of_z(mp.mpf(1))
    check("level_of_z_eq_1_is_the_published_noninteger",
          r1 is not None and abs(r1 - mp.mpf("1.1238831038")) < mp.mpf("1e-8"),
          f"r(z=1) = {mp.nstr(r1, 12)} — the published closed form's level")

    # ---- CHECK 2: Delta_S calibrates against the decision document ---------
    print("\nCHECK 2 — Delta_S reproduces the decision document's two cells")
    delta_S = [h ** 2 / 2, -h / 2, -h / 2, ZERO, ZERO, ZERO]
    aug_S = at_q0(tr_symbolic(delta_S, Q0))
    trD_S = at_q0(tr_symbolic(delta_S, sp.Rational(Q0 ** 3 / (Q0 ** 2 + 1))))
    pct_aug_S = (abs(aug_S) * E0 / MP_QB - 1) * 100
    pct_D_S = (abs(trD_S) * E0 / MP_QB - 1) * 100
    check("delta_S_augmentation_is_plus_12_470_pct",
          abs(pct_aug_S - mp.mpf("12.470")) < mp.mpf("0.001"),
          f"{mp.nstr(pct_aug_S, 8)} % — decision doc says +12.470 %")
    check("delta_S_convention_D_is_minus_43_157_pct",
          abs(pct_D_S - mp.mpf("-43.157")) < mp.mpf("0.001"),
          f"{mp.nstr(pct_D_S, 8)} % — decision doc says -43.157 %")

    # ---- CHECK 3: the census's `net` is the COORDINATE SUM, not tr^{z=1} ---
    print("\nCHECK 3 — calibration against the committed census, and the")
    print("          coordinate-sum-vs-trace gap it exposes")
    census_nets = {
        "nuc9_build_nucleon_nf": "-0.1882906014713827704417372201264506584168",
        "nuc11_interleaved": "-0.2271597117655695709663935951013034119594",
        "nuc11_gen_grouped": "-0.2331977113156587020400640333246765343358",
    }
    models = {
        "nuc9_build_nucleon_nf": _census.nuc9,
        "nuc11_interleaved": _census.nuc11_interleaved,
        "nuc11_gen_grouped": _census.nuc11_gen_grouped,
    }
    deltas = {}
    for name, fn in models.items():
        d = delta_of(fn)
        deltas[name] = d
        coord = at_q0(sum(d))
        want = mp.mpf(census_nets[name])
        check(f"coordinate_sum_matches_census__{name}",
              abs(coord - want) < mp.mpf("1e-30"),
              f"{mp.nstr(coord, 25)}")

    # The two functionals differ by exactly h * (e^- coordinate) -- symbolically,
    # before any pin. This is why `net` is NOT tr at z = 1: the trace weights e^-
    # by z(hz+1) = h+1 at z = 1, the coordinate sum weights it by 1.
    for name, d in deltas.items():
        gap = sp.simplify(sum(d) - tr_symbolic(d, sp.Integer(1)) + h * d[5])
        check(f"coordsum_minus_trace_is_h_times_e_minus__{name}", gap == 0,
              f"e^- = {sp.factor(d[5])}")
    e_zero = {n: sp.simplify(d[5]) == 0 for n, d in deltas.items()}
    check("only_the_gen_grouped_model_has_vanishing_e_minus",
          e_zero["nuc11_gen_grouped"] and not e_zero["nuc9_build_nucleon_nf"]
          and not e_zero["nuc11_interleaved"],
          "so the corpus's 'coordinate sum = tr at z=1' identification holds on "
          "the gen-grouped model only — the census already flags this as "
          "e_minus_nonzero_on_some_long_models")

    deltas["delta_S_short_normal_form"] = delta_S

    # ---- CHECK 4: the required level, per candidate ------------------------
    print("\nCHECK 4 — required level per candidate (the Option E acceptance test)")
    records = {}
    all_levels: list[tuple[str, object]] = []
    for name, d in deltas.items():
        rec, zs, lv = report(name, d)
        records[name] = rec
        for v in lv:
            all_levels.append((name, v))

    # ---- CHECK 5: the 16-variant constructed family, as a RANGE ------------
    print("\nCHECK 5 — the properties blocks' own recipe, all 16 readings")
    var_levels = []
    var_pct_aug = []
    for gens in itertools.product((0, 1), repeat=3):
        for hopf in ((1, 0), (0, 1)):
            d = delta_of(_census.nuc11_constructed, gens=gens, hopf=hopf)
            aug = at_q0(tr_symbolic(d, Q0))
            var_pct_aug.append((abs(aug) * E0 / MP_QB - 1) * 100)
            for zv in required_zs(d):
                if zv > 0:
                    lv = level_of_z(zv)
                    if lv is not None:
                        var_levels.append(lv)
                        all_levels.append((f"constructed{gens}{hopf}", lv))
    check("constructed_family_is_16_readings", len(var_pct_aug) == 16,
          "8 quark-generator assignments x 2 Hopf orientations")
    if var_pct_aug:
        lo, hi = min(var_pct_aug), max(var_pct_aug)
        print(f"    augmentation residual across the 16: "
              f"[{mp.nstr(lo, 8)} %, {mp.nstr(hi, 8)} %], "
              f"spread {mp.nstr(hi - lo, 8)} points")
    if var_levels:
        rlo, rhi = min(var_levels), max(var_levels)
        print(f"    required level across the 16:        "
              f"[{mp.nstr(rlo, 10)}, {mp.nstr(rhi, 10)}], "
              f"spread {mp.nstr(rhi - rlo, 8)}")
        check("assignment_freedom_moves_the_required_level",
              (rhi - rlo) > mp.mpf("1e-6"),
              f"spread {mp.nstr(rhi - rlo, 8)} — an UNSTATED choice in the "
              "source blocks moves the level, so a landing on r=1 or r=2 "
              "would be an assignment artifact, not evidence")

    # ---- CHECK 5b: level 1 is ORDER-BLIND, level 2 is not -----------------
    print("\nCHECK 5b — what the augmentation can and cannot see")
    d_int = deltas["nuc11_interleaved"]
    d_gen = deltas["nuc11_gen_grouped"]
    aug_int = at_q0(tr_symbolic(d_int, Q0))
    aug_gen = at_q0(tr_symbolic(d_gen, Q0))
    zD_r = sp.Rational(Q0 ** 3 / (Q0 ** 2 + 1))
    D_int = at_q0(tr_symbolic(d_int, zD_r))
    D_gen = at_q0(tr_symbolic(d_gen, zD_r))
    check("augmentation_cannot_see_braid_ORDER",
          abs(aug_int - aug_gen) < mp.mpf("1e-40"),
          "the interleaved and gen-grouped models carry the SAME typed-crossing "
          "multiset in a different order; eps_aug is multiplicative, so it is a "
          "product over letters and the order drops out — "
          f"both {mp.nstr(aug_int, 20)}")
    check("convention_D_CAN_see_braid_order",
          abs(D_int - D_gen) > mp.mpf("1e-6"),
          f"tr_D differs: {mp.nstr(D_int, 12)} vs {mp.nstr(D_gen, 12)}")
    check("all_16_constructed_share_the_augmentation",
          var_pct_aug and (max(var_pct_aug) - min(var_pct_aug)) < mp.mpf("1e-20"),
          "same consequence: the 8 generator assignments x 2 Hopf orientations "
          "change only the ORDER, so level 1 is blind to all 16 — an Option E "
          "element that differs from an existing one only by ordering is, at "
          "level 1, the same number")

    check("augmentation_equals_the_bean_s_chi_3_of_the_word_difference",
          abs(aug_int - mp.mpf("-0.26038764179012078")) < mp.mpf("1e-16"),
          "qou-99qc records chi_(3)(beta_n - beta_p) = -0.26038764179012078 by a "
          "character-table route; at level 1 only the (3) row survives "
          "(y_(3) = 1, y_(2,1) = y_(1^3) = 0), so the augmentation IS chi_(3) — "
          f"this probe gets {mp.nstr(aug_int, 20)} from the Markov trace instead")

    # ---- CHECK 5c: the bracketing is universal, and that IS the obstruction -
    print("\nCHECK 5c — every candidate BRACKETS the target, hence needs r in (1,2)")
    brackets = {}
    for name, d in deltas.items():
        a = abs(at_q0(tr_symbolic(d, Q0))) * E0
        b = abs(at_q0(tr_symbolic(d, zD_r))) * E0
        brackets[name] = (a > MP_QB) and (b < MP_QB)
    check("level_1_overshoots_and_level_2_undershoots_on_every_candidate",
          all(brackets.values()),
          "aug > Q_beta > tr_D for all of "
          + ", ".join(brackets) + " — so by continuity the required level lies "
          "strictly BETWEEN the two admissible ones, and is therefore not one "
          "of them")
    print("    DESIGN CONSTRAINT for Option E, derived rather than asserted:")
    print("    an element that closes Option E must have its level-1 and level-2")
    print("    values on the SAME side of Q_beta. Every candidate the corpus has")
    print("    built brackets it, so no amount of re-ordering or re-assignment")
    print("    within these families can succeed.")

    # ---- CHECK 6: the headline ---------------------------------------------
    print("\nCHECK 6 — does ANY candidate require an admissible level?")
    tol = mp.mpf("1e-3")
    hits = [(n, v) for n, v in all_levels if admissible_level(v, tol)]
    best = None
    for n, v in all_levels:
        if v is None:
            continue
        d = min(abs(v - 1), abs(v - 2))
        if best is None or d < best[2]:
            best = (n, v, d)
    if best is not None:
        print(f"    closest approach: {best[0]} at r = {mp.nstr(best[1], 12)}, "
              f"distance {mp.nstr(best[2], 8)} from the nearer admissible level")
    check("no_corpus_candidate_requires_an_admissible_level",
          len(hits) == 0,
          f"{len(all_levels)} required levels solved across "
          f"{len(deltas)} named candidates + 16 constructed variants; "
          f"{len(hits)} within {mp.nstr(tol, 3)} of r = 1 or r = 2")

    # ---- CHECK 7: no float64 ----------------------------------------------
    print("\nCHECK 7 — arithmetic hygiene")
    check("all_readouts_are_mpf",
          isinstance(E0, mp.mpf) and isinstance(TARGET, mp.mpf),
          "E_0 and TARGET are mpmath mpf at 60 dps; candidates are exact in h")

    ok = all(r[1] for r in RESULTS)
    print()
    print(f"{sum(1 for r in RESULTS if r[1])}/{len(RESULTS)} checks passed")
    print()
    print("VERDICT — Option E has a sharp acceptance test, and every element the")
    print("corpus has built fails it. Each candidate Delta NAMES the functional it")
    print("would need (tr is quadratic in z, so the target determines z), and that")
    print("functional is a Wenzl level. None of the levels is 1 or 2. Scope-(a):")
    print("these candidates do not close Option E; no claim is made that none can.")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("qbeta-option-e-required-level")
        w.set_description(
            "Option E (qou-99qc) reframed as a level test: on the H_3(q) normal-form "
            "basis tr_M^z is quadratic in z, so a candidate Delta DETERMINES the "
            "functional it would need, and that functional is a Wenzl level. Solves "
            "the required level for every candidate in the corpus's own Delta census "
            "plus all 16 readings of the properties blocks' recipe. None requires an "
            "admissible level (r = 1 augmentation, r = 2 convention D). Selects "
            "nothing; scope-(a)."
        )
        w.add_data("markov_convention",
                   "both admissible parameters are evaluated: z = q (level 1, the "
                   "augmentation) and z_D = q^3/(q^2+1) (level 2, convention D)")
        w.add_data("q0_anchor", "proton")
        w.add_data("q0_value", Q_50_DIGIT_STR)
        w.add_data("E0_MeV", mp.nstr(E0, 30))
        w.add_data("target_abs_eps", mp.nstr(TARGET, 30))
        w.add_data("Q_beta_sigma_ppb", mp.nstr(SIGMA_REL * 10**9, 8))
        w.add_data("per_candidate", records)
        if var_pct_aug:
            w.add_data("constructed_16_augmentation_residual_pct",
                       {"min": mp.nstr(min(var_pct_aug), 12),
                        "max": mp.nstr(max(var_pct_aug), 12)})
        if var_levels:
            w.add_data("constructed_16_required_level",
                       {"min": mp.nstr(min(var_levels), 15),
                        "max": mp.nstr(max(var_levels), 15)})
        if best is not None:
            w.add_data("closest_approach",
                       {"candidate": best[0], "level": mp.nstr(best[1], 15),
                        "distance_to_nearer_admissible": mp.nstr(best[2], 12)})
        w.add_caveat(
            "Scope-(a). It measures the candidates the corpus has ALREADY built; "
            "it does not show that no element can require an admissible level, and "
            "Option E stays open."
        )
        w.add_caveat(
            "Deliberately NOT a search. Enumerating elements until one lands on "
            "r = 1 or r = 2 would be selection against the target — a fit under "
            "AGENTS.md 'NO FITTING'. The 16-variant family is reported as a range "
            "for exactly that reason; its best-landing member is not a result."
        )
        w.add_caveat(
            "The level ladder z(r) is the n = 3 Wenzl relation "
            "Q^r = z_W/(1 - Q + z_W) with Q = q^2, z_W = q z; admissibility as "
            "'r in {1,2}' is the n = 3 statement, checked at n = 3..7 in "
            "qbeta_wenzl_level_decides_the_functional_probe but not proved for all n."
        )
        w.add_caveat(
            "The candidate constructors are IMPORTED from "
            "qbeta_delta_candidate_census_probe, so any defect in those models "
            "propagates here unchanged. This probe adds no model of its own."
        )
        w.add_caveat(
            "Q_beta is the AME-2020 value; the CODATA-2022-derived one differs by "
            "+191 ppb (bean qou-0e2p). At the residual scale seen here (tens of "
            "percent) that choice is immaterial, and it is NOT immaterial for any "
            "claim at the sigma = 779.7 ppb level."
        )
        for name, passed, det in RESULTS:
            w.add_assertion(name, "1" if passed else "0", "1", "0",
                            source=det or None)
        try:
            from qou_substrate.witness import WitnessBuilder as WB2
            WB2.stamp_staleness_metadata(
                w, script_path=__file__, engine="python+sympy+mpmath",
                q0_anchor="proton", q0_value=Q_50_DIGIT_STR)
        except Exception:
            pass
        w.save()
        print("witness written")
    except Exception as exc:  # pragma: no cover
        print(f"witness NOT written ({exc.__class__.__name__}: {exc})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
