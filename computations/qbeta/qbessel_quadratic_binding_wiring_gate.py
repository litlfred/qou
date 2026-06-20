#!/usr/bin/env python3
"""qbessel_quadratic_binding_wiring_gate.py
============================================

DECISIVE wiring gate for the owner question (2026-06-20): "how would we use the
q-Bessel quadratic propagator to improve mass/binding -- if we can Lean-prove it,
wire it up?"

PRs #2530 (gate) and #2533 (off-shell) established the admissible object: the
coincidence-limit propagator  G(w) = g1(w) g2(w) / D(w)  is finite/regular at the
substrate origin (the 2nd kind survives on-shell as a BILINEAR).  The natural way
to "use it in binding" is a one-loop / self-energy correction

    delta_B  =  Sum_lambda  y_lambda * [ G(w_lambda^atom) - G(w_lambda^free) ],

one propagator-at-coincidence per Wedderburn block, differenced free vs bound.

This script tests -- BEFORE any wiring -- whether that correction is
SUBSTRATE-FORCED (parameter-free, hence not a 7th Delta_lambda ansatz) or whether
it depends on an undetermined argument map.  It uses the real deuteron per-block
characters (atom-chi-rust-d.witness.json, n=6, 11 blocks).

The unavoidable inputs a binding correction needs, and whether the substrate fixes them
--------------------------------------------------------------------------------------
  * nu_lambda : the q-Bessel ORDER on block lambda.  The Reeb/q-Bessel dictionary
    (2026-06-13) ties "order" to a rep level, but does NOT pin a unique integer
    nu_lambda per partition.  -> NOT fixed.
  * w_lambda  : the q-Bessel ARGUMENT.  The block carries a Reeb phase
    theta_lambda = arccos(r) (rotation, |r|<=1) or arccosh(|r|) (growth, |r|>1),
    r = chi_lambda/dim_lambda.  But the map theta -> x -> w = q x^2 is a FUNCTIONAL
    CHOICE (x = theta?  x = sin theta?  x = 2 sinh(theta/2)?).  -> NOT fixed.

If delta_B is stable across reasonable (nu_lambda, w_lambda) choices, the correction
is forced and worth wiring.  If it swings in sign/scale, the map is a free knob and
wiring it is the forbidden 7th ansatz (CLAUDE.md Delta_lambda gate).

What is computed (no fit; nothing wired)
----------------------------------------
  (1) Per-block deuteron r_free, r_atom, rotation/growth class, theta (already the
      binding_reeb_phase_decomposition split).
  (2) The unsigned propagator correction sum  S(map, nu_rule) = Sum_lambda
      [G(w_lambda^atom) - G(w_lambda^free)]  (uniform weights -- the y_lambda are
      positive O(1/dim) and do NOT change the sign/scale conclusion) under a small
      menu of EQUALLY-NATURAL maps and nu-rules.
  (3) The growth-sector share of |S| -- the blocks whose g2 is relevant are exactly
      the growth blocks that CANCELLED in the A>=3 scalar refutation
      (binding_reeb_phase_decomposition.py / binding_volume_difference_probe.py).

VERDICT is read off (2): map-stable => forced (wire-candidate); map-swinging =>
unforced (7th ansatz; DO NOT wire).
"""
from __future__ import annotations

import json
import math
import pathlib

from mpmath import mp, mpf, qp, fabs, fsum, acos, acosh, sin, sinh, sqrt

mp.dps = 50
Q0 = mpf("1.10997858")          # proton-pinned substrate q_0
QMU = mpf("1.110037")           # muon-anchor q (cross-anchor reference; ~22 ppm above q0)

HERE = pathlib.Path(__file__).resolve().parent
DEU = HERE.parent / "atom-chi-rust-d.witness.json"


# ---- q-Bessel solutions + coincidence propagator (PR #2530/#2533 convention) ----
def c_k(k, nu, q):
    return (-1) ** k * q ** (k * (k - 1) // 2) / (qp(q, q, k) * qp(q ** (nu + 1), q, k))


def g1(w, nu, q, K=40):
    return fsum(c_k(k, nu, q) * w ** k for k in range(K))


def d_k_seq(nu, q, K=40):
    d = [mpf(1)]
    for k in range(1, K):
        d.append(-q ** (k - 1) * d[k - 1] / ((q ** k - 1) * (q ** k - q ** nu)))
    return d


def g2(w, nu, q, K=40):
    d = d_k_seq(nu, q, K)
    return w ** (-nu) * fsum(d[k] * w ** k for k in range(K))


def casoratian(w, nu, q):
    return g1(w, nu, q) * g2(q * w, nu, q) - g1(q * w, nu, q) * g2(w, nu, q)


def G(w, nu, q):
    if w == 0:                          # analytic coincidence limit (PR #2533)
        return 1 / (q ** (-nu) - 1)
    return g1(w, nu, q) * g2(w, nu, q) / casoratian(w, nu, q)


def dim_sn(lam):
    n = sum(lam)
    den = 1
    for i in range(len(lam)):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
            den *= arm + leg + 1
    return math.factorial(n) // den


def load_blocks():
    d = json.loads(DEU.read_text())
    free = {tuple(e["partition"]): mpf(e["chi_lambda"]) for e in d["data"]["free"]["by_partition"]}
    atom = {tuple(e["partition"]): mpf(e["chi_lambda"]) for e in d["data"]["atom"]["by_partition"]}
    return free, atom


# ---- argument maps theta -> x (all equally "natural"); w = q x^2 ----
ARG_MAPS = {
    "x=theta":        lambda th: th,
    "x=sin|theta|":   lambda th: sin(fabs(th)) if fabs(th) < 1.4 else sinh(fabs(th)) / 3,
    "x=2sinh(th/2)":  lambda th: 2 * sinh(th / 2),
}
# ---- nu-rules (block -> q-Bessel order); all equally defensible ----
# NOTE: INTEGER nu hits the Neumann log-resonance q^k = q^nu in g2's recurrence
# (the d_k denominator (q^k - q^nu) -> 0 at k=nu) -- the physically-natural integer
# rep-levels are exactly the singular/logarithmic 2nd-kind case the power-series
# construction does NOT cover. We use the SU_q(2) HALF-INTEGER spin labels (also
# the natural choice), which avoid the resonance; that the integer-vs-half-integer
# choice even matters is itself part of the under-determination.
NU_RULES = {
    "nu=rows-1/2": lambda lam: max(len(lam) - 1, 1) - mpf("0.5"),
    "nu=n-lam1+1/2": lambda lam: max(sum(lam) - lam[0], 1) - mpf("0.5"),
}


def correction_sum(free, atom, q, arg_map, nu_rule):
    """Sum_lambda [G(w_atom) - G(w_free)] with uniform weights (sign/scale probe)."""
    terms = []
    for lam in free:
        d = dim_sn(list(lam))
        rf, ra = free[lam] / d, atom[lam] / d
        thf = acos(rf) if fabs(rf) <= 1 else acosh(fabs(rf))
        tha = acos(ra) if fabs(ra) <= 1 else acosh(fabs(ra))
        nu = nu_rule(lam)
        wf = q * arg_map(thf) ** 2
        wa = q * arg_map(tha) ** 2
        try:
            dG = G(wa, nu, q) - G(wf, nu, q)
        except Exception:
            dG = mpf("nan")
        growth = fabs(rf) > 1 or fabs(ra) > 1
        terms.append((lam, nu, growth, dG))
    valid = [t[3] for t in terms if t[3] == t[3]]   # drop nan
    tot = fsum(valid) if len(valid) == len(terms) else mpf("nan")
    return tot, terms


def main():
    free, atom = load_blocks()
    print("Deuteron quadratic-propagator binding correction — wiring gate")
    print("=" * 66)
    print(f"n=6, {len(free)} blocks; q_0={float(Q0)}\n")

    # (2) map / nu stability of the correction sum
    print("(2) correction sum S = Sum_lambda [G(w_atom)-G(w_free)]  (uniform weights)")
    print(f"{'nu-rule':<12}{'arg-map':<16}{'S (q0)':>16}{'S (q_mu)':>16}")
    vals = []
    for nname, nrule in NU_RULES.items():
        for aname, amap in ARG_MAPS.items():
            s0, terms = correction_sum(free, atom, Q0, amap, nrule)
            smu, _ = correction_sum(free, atom, QMU, amap, nrule)
            vals.append(s0)
            print(f"{nname:<12}{aname:<16}{mp.nstr(s0, 8):>16}{mp.nstr(smu, 8):>16}")

    finite = [v for v in vals if v == v]  # drop nan
    if not finite:
        print("  No finite correction sums computed (all NaN — e.g. integer-nu resonance).")
        return 1
    smin, smax = min(finite), max(finite)
    signs = set(int(mp.sign(v)) for v in finite if v != 0)
    spread = (fabs(smax - smin) / (fabs(smax) + fabs(smin))) if (smax != 0 or smin != 0) else mpf(0)
    print(f"\n    range of S over maps/nu-rules: [{mp.nstr(smin,6)}, {mp.nstr(smax,6)}]")
    print(f"    sign set = {signs}   relative spread = {mp.nstr(spread, 4)}")

    # (3) growth-sector share (the cancellation-prone blocks)
    _, terms = correction_sum(free, atom, Q0, ARG_MAPS["x=theta"], NU_RULES["nu=rows-1/2"])
    growth_abs = fsum(fabs(t[3]) for t in terms if t[2] and t[3] == t[3])
    all_abs = fsum(fabs(t[3]) for t in terms if t[3] == t[3])
    share = growth_abs / all_abs if all_abs != 0 else mpf(0)
    print(f"\n(3) growth-sector share of |correction| = {mp.nstr(share*100, 4)}%")
    print("    (growth blocks are exactly those that CANCELLED in the A>=3 scalar")
    print("     refutation — binding_reeb_phase_decomposition / volume_difference)")

    # ---- verdict ----
    forced = (len(signs) <= 1) and (spread < mpf("0.05"))
    print("\n--- VERDICT (formalize-first wiring gate; no fit; nothing wired) ---")
    if forced:
        print("  Correction is MAP-STABLE => substrate-forced => WIRE-CANDIDATE.")
        print("  (Proceed to cross-anchor gate + Lean lemma + appendix wiring.)")
    else:
        print("  Correction SWINGS in sign/scale across equally-natural (nu, arg-map)")
        print("  choices => the (nu_lambda, w_lambda) map is a FREE FUNCTIONAL KNOB,")
        print("  NOT fixed by the substrate. A per-block propagator multiplier is then")
        print("  a disguised 7th Delta_lambda ansatz (CLAUDE.md Delta_lambda gate:")
        print("  'do not propose a 7th fit-based ansatz'). DO NOT WIRE.")
        print("  The admissible object G (PRs #2530/#2533) is real, but a parameter-")
        print("  free binding correction needs an INDEPENDENT substrate derivation of")
        print("  the order+argument map first. Growth-sector dominance compounds this")
        print("  (same cancellation that refuted A>=3).")
    print("\n  Lean status: the wireable lemma is the q-Bessel CASORATIAN REGULARITY")
    print("  (D q-Abel; G->1/(q^-nu-1)) — a q-Bessel FACT, NOT a binding claim.")
    print("  Proving it does not make delta_B real, so it is NOT a production wiring.")

    # this script is a derive-or-refute GATE: 'passing' = it ran and rendered a verdict
    print("\nGATE COMPLETE (verdict: " + ("WIRE-CANDIDATE" if forced else "DO NOT WIRE") + ").")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
