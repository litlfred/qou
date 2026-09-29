#!/usr/bin/env python3
"""Q_beta decay channel convention registration — the numeric shadow (bean qou-b3nk).

Companion to the Lean bricks in
``QOU/QBeta/MarkovZFullBarCondition.lean`` (sorry-free, lean-direct exit 0)
and the ``disputed`` registration of the ``qbeta-decay`` channel in
``docs/coordination/trace-convention-registry.json``.  Full analysis:
``docs/audits/2026-08-15-qbeta-decay-channel-convention-disputed-registration.md``.

WHAT THIS PROBE VERIFIES (proton pin q0 throughout; 65 dps compute, 50 dps
serialisation; sympy exact where marked):

  1. REGISTRY CROSS-CHECK — z_C, z_D and both weight vectors recomputed from
     scratch (Markov linear system solve) match the registry's 50-dps strings
     to <= 1e-40.
  2. THE ESCAPE IS THE CONVENTION'S, NOT THE INSTANCE'S — the convention-C
     Ocneanu solve at q0 has y_(1^3) = 0.02274... != 0.  (This is the correct
     witness for "C carries the third row".  The witness quoted by the
     2026-08-15 validity audit — the explicit class inhabitant
     y = (z, 1/2 - z, z) of ``CanonicalMarkovWeightsH3`` — is NOT an Ocneanu
     z-trace at z_C at all: its sigma_0 functional value is h/2 exactly
     (sympy, z-independent), not z_C.  Same conclusion, corrected witness.)
  3. JONES-PIN FAILURE, EXACT — the coincidence locus of z_C*(q+q^-1) = q^2
     in s = sqrt(q) is s^7 + s^5 - s^4 - 1 = 0, which factors EXACTLY as
     (s - 1)*(s^6 + s^5 + 2*s^4 + s^3 + s^2 + s + 1); the second factor has
     all-positive coefficients, so the locus is empty for s > 1.  This is
     the sympy mirror of Lean ``decayLadder_zC_not_jones``; combined with
     ``threeRow_ne_zero_of_ocneanu_ne`` it gives the mutual-exclusivity
     brick ``decayLadder_zC_threeRow_ne_zero``.
  4. FULL-BAR CONDITION, NUMERIC SHADOW at q0 — |bar(z_D) - (z_D - h)| = 0
     to <= 1e-45 while bar(z_C) - (z_C - h) = h ~ 0.209 (exact: = h, since
     z_C is bar-even).  Symbolic original: markov_z_full_bar_condition_probe.py
     (2026-08-08, exact in q, family identity for symbolic N).
  5. N_eff POINTWISE — the fibre-rank inversion of z_C at q0 is 2.5995...,
     not an integer (and q-dependent per the full-bar witness): z_C is the
     categorical trace on no fixed-rank fibre.

SCOPE — scope-(a) throughout; this probe ADJUDICATES NO CONVENTION.  It is
the measurement layer under the ``disputed`` registration: C is underived
(a stipulation whose cited referent, 'the Markov--Jones parameter' of
rem:markov-axioms-primitive, has read z_D since the 2026-08-09 excision) and
fails two structural conditions each of which would exclude it IF demanded
(full-bar covariance; fixed-rank fibre membership) — but neither demand is
itself derived for the decay channel, and no corpus block derives the decay
fibre.  D is conditionally forced on named unproved premises only
(conj:binding-qbeta-complex-volume same-object identification, or trace
bar-compatibility).  Nothing wired; no c_k value or tier changes.

Conventions: proton pin (AGENTS 2026-08-07 owner directive); no muon-built
cache is read.
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: E402, F401

from qou_substrate import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

import json  # noqa: E402

REG = ROOT / "docs" / "coordination" / "trace-convention-registry.json"

DPS = 65
SER = 50


def z_C(q: mp.mpf) -> mp.mpf:
    return mp.sqrt(q) / (1 + q)


def z_D(q: mp.mpf) -> mp.mpf:
    return q ** 3 / (q ** 2 + 1)


def solve_weights(q: mp.mpf, z: mp.mpf) -> dict[str, mp.mpf]:
    """Solve the H_3(q) Markov system tr(1)=1, tr(s0)=z, tr(s0 s1)=z^2
    in the Frobenius basis (character table of MarkovTraceTLUniqueness.lean)."""
    h = q - 1 / q
    A = mp.matrix([
        [1, 2, 1],
        [q, h, -1 / q],
        [q ** 2, -1, 1 / q ** 2],
    ])
    b = mp.matrix([mp.mpf(1), z, z ** 2])
    y = mp.lu_solve(A, b)
    return {"(3)": y[0], "(2,1)": y[1], "(1^3)": y[2]}


def main() -> int:
    mp.mp.dps = DPS
    q0 = q_at(DPS)

    reg = json.loads(REG.read_text())
    conv = {r["id"]: r for r in reg["conventions"]}

    wb = WitnessBuilder("qbeta-decay-channel-convention-status", engine="mpmath")
    wb.set_description(
        "Numeric shadow of the qbeta-decay 'disputed' registration: registry "
        "cross-check of z_C/z_D and both weight vectors; y_(1^3)(z_C) != 0 "
        "as the corrected escape witness (the explicit class inhabitant is "
        "not an Ocneanu z-trace: its sigma_0 value is h/2 exactly); exact "
        "factorisation of the z_C Jones-pin coincidence locus (empty for "
        "s > 1, Lean decayLadder_zC_not_jones); full-bar condition numeric "
        "shadow (D holds, C fails by exactly h); N_eff(z_C, q0) = 2.5995... "
        "non-integer. Adjudicates NO convention (scope-(a))."
    )

    checks: dict[str, bool] = {}
    tol = mp.mpf("1e-40")

    # ── 1. registry cross-check ────────────────────────────────────────
    zc, zd = z_C(q0), z_D(q0)
    checks["zC_matches_registry"] = (
        abs(zc - mp.mpf(conv["C"]["z_at_q0"])) <= tol
    )
    checks["zD_matches_registry"] = (
        abs(zd - mp.mpf(conv["D"]["z_at_q0"])) <= tol
    )
    yC = solve_weights(q0, zc)
    yD = solve_weights(q0, zd)
    for lam, key in (("(3)", "(3)"), ("(2,1)", "(2,1)"), ("(1^3)", "(1^3)")):
        checks[f"yC{lam}_matches_registry"] = (
            abs(yC[lam] - mp.mpf(conv["C"]["weights_at_q0"][key])) <= tol
        )
        checks[f"yD{lam}_matches_registry"] = (
            abs(yD[lam] - mp.mpf(conv["D"]["weights_at_q0"][key])) <= tol
        )

    # ── 2. the escape is the convention's, not the instance's ─────────
    checks["yC_1cubed_nonzero"] = abs(yC["(1^3)"]) > mp.mpf("1e-3")
    # exact, sympy: the explicit inhabitant y = (z, 1/2 - z, z) has
    # sigma_0 functional value h/2 for EVERY z — it is not an Ocneanu
    # z-trace unless z = h/2.
    qs, zs = sp.symbols("q z", positive=True)
    hs_ = qs - 1 / qs
    inst_sigma0 = zs * qs + (sp.Rational(1, 2) - zs) * hs_ + zs * (-1 / qs)
    checks["instance_sigma0_is_h_over_2_exact"] = (
        sp.simplify(inst_sigma0 - hs_ / 2) == 0
    )
    h0 = q0 - 1 / q0
    inst_gap = abs(h0 / 2 - zc)
    checks["instance_is_not_zC_trace_at_q0"] = inst_gap > mp.mpf("0.1")

    # ── 3. Jones-pin failure, exact ────────────────────────────────────
    s = sp.Symbol("s", positive=True)
    locus = s ** 7 + s ** 5 - s ** 4 - 1
    factored = (s - 1) * (s ** 6 + s ** 5 + 2 * s ** 4 + s ** 3 + s ** 2 + s + 1)
    checks["jones_pin_locus_factors_exactly"] = sp.expand(locus - factored) == 0
    # numeric shadow at q0
    jones_gap = zc * (q0 + 1 / q0) - q0 ** 2
    checks["zC_fails_jones_pin_at_q0"] = abs(jones_gap) > mp.mpf("0.01")
    # and z_D satisfies it exactly (the D identity z*(q+1/q) = q^2)
    checks["zD_satisfies_jones_pin"] = (
        abs(zd * (q0 + 1 / q0) - q0 ** 2) <= mp.mpf("1e-45")
    )

    # ── 4. full-bar condition, numeric shadow ──────────────────────────
    qbar = 1 / q0
    fullbar_D = z_D(qbar) - (zd - h0)
    fullbar_C = z_C(qbar) - (zc - h0)
    checks["zD_full_bar_holds_at_q0"] = abs(fullbar_D) <= mp.mpf("1e-45")
    checks["zC_full_bar_fails_by_exactly_h"] = abs(fullbar_C - h0) <= mp.mpf("1e-45")

    # ── 5. N_eff pointwise ─────────────────────────────────────────────
    # z_N = h/(1 - q^(-2N))  =>  N = -ln(1 - h/z) / (2 ln q)
    n_eff = -mp.log(1 - h0 / zc) / (2 * mp.log(q0))
    checks["neff_zC_between_2_and_3"] = mp.mpf(2) < n_eff < mp.mpf(3)
    checks["neff_zC_not_integer"] = (
        abs(n_eff - 2) > mp.mpf("0.1") and abs(n_eff - 3) > mp.mpf("0.1")
    )

    all_pass = all(checks.values())

    wb.add_parameter("dps_compute", DPS)
    wb.add_parameter("dps_serialize", SER)
    wb.add_parameter("q0_pin", "proton (q_at; AGENTS 2026-08-07 owner directive)")
    wb.add_parameter("q0", mp.nstr(q0, SER))
    wb.add_parameter("uses_muon_built_cache", False)

    wb.add_data("checks", {k: bool(v) for k, v in checks.items()})
    wb.add_data("z_C_at_q0", mp.nstr(zc, SER))
    wb.add_data("z_D_at_q0", mp.nstr(zd, SER))
    wb.add_data("yC_at_q0", {k: mp.nstr(v, SER) for k, v in yC.items()})
    wb.add_data("yD_at_q0", {k: mp.nstr(v, SER) for k, v in yD.items()})
    wb.add_data("instance_sigma0_value", "h/2 exactly (z-independent, sympy)")
    wb.add_data("instance_vs_zC_gap_at_q0", mp.nstr(inst_gap, SER))
    wb.add_data("jones_pin_gap_zC_at_q0", mp.nstr(jones_gap, SER))
    wb.add_data("jones_pin_locus", "s^7+s^5-s^4-1 = (s-1)(s^6+s^5+2s^4+s^3+s^2+s+1)")
    wb.add_data("full_bar_residual_D", mp.nstr(fullbar_D, SER))
    wb.add_data("full_bar_residual_C_minus_h", mp.nstr(fullbar_C - h0, SER))
    wb.add_data("neff_zC_at_q0", mp.nstr(n_eff, SER))
    wb.add_data(
        "lean",
        {
            "file": "folio/quantum-observable-universe/lean/QOU/QBeta/MarkovZFullBarCondition.lean",
            "decls": [
                "QOU.QBeta.zD_full_bar_covariant",
                "QOU.QBeta.barEven_fullBar_forces_classical",
                "QOU.QBeta.zC_fails_fullBar",
                "QOU.QBeta.decayLadder_zC_not_jones",
                "QOU.QBeta.decayLadder_zC_threeRow_ne_zero",
            ],
            "axioms": "propext, (Classical.choice,) Quot.sound — no sorryAx",
        },
    )
    wb.add_data(
        "registration",
        {
            "channel": "qbeta-decay",
            "status": "disputed",
            "definitional_convention": None,
            "production_convention": "C",
            "open_item_bean": "qou-b3nk",
        },
    )

    wb.add_assertion(
        "checks_failed", sum(1 for v in checks.values() if not v), 0,
        source="mpmath 65 dps + sympy exact",
    )

    wb.add_caveat(
        "Scope-(a): adjudicates no convention. The full-bar exclusion of C is "
        "conditional on trace bar-compatibility (tr(bar y) = bar(tr y)) — the "
        "standard Ocneanu-trace property, asserted context, not proved. The "
        "fibre-integrality exclusion of C is conditional on the decay trace "
        "being a categorical fibre trace. Neither premise is derived for the "
        "decay channel; no corpus block derives the decay fibre."
    )
    wb.add_caveat(
        "A z-swap C->D under the existing ladder is NOT a migration: the "
        "2026-08-15 sensitivity probe measured c_3 -> ~-974, implied c_2 -> "
        "-9.3, and rung-convergence collapse. D-adoption requires ladder "
        "re-derivation."
    )

    # q0 anchor: this probe DOES read the substrate modulus — `q0 = q_at(DPS)`
    # above, the package-layer (proton-pinned) accessor, per the 2026-08-07
    # owner directive that new compute defaults to the experimental pin. The
    # pin was already recorded as an `add_parameter("q0_pin", ...)`, but that
    # lands under `data` where the audit reading body["q0Anchor"] cannot see
    # it — which is why this witness counted as MISSING while visibly naming
    # its pin. Declared here where the audit reads, with the matching value.
    path = wb.save({"q0Anchor": "proton", "q0Value": mp.nstr(q0, SER)})

    print("=" * 70)
    print("Q_beta decay channel convention status — numeric shadow")
    print("=" * 70)
    print(f"  z_C(q0) = {mp.nstr(zc, 20)}   z_D(q0) = {mp.nstr(zd, 20)}")
    print(f"  yC = {[mp.nstr(v, 12) for v in yC.values()]}")
    print(f"  yD = {[mp.nstr(v, 12) for v in yD.values()]}")
    print(f"  y_(1^3)(z_C) = {mp.nstr(yC['(1^3)'], 20)}  (the corrected escape witness)")
    print(f"  instance sigma_0 value = h/2 (exact); gap to z_C at q0 = {mp.nstr(inst_gap, 12)}")
    print(f"  Jones-pin gap at z_C  = {mp.nstr(jones_gap, 20)}")
    print(f"  full-bar residual: D = {mp.nstr(fullbar_D, 6)}, C - h = {mp.nstr(fullbar_C - h0, 6)}")
    print(f"  N_eff(z_C, q0) = {mp.nstr(n_eff, 20)}")
    print()
    for k, v in checks.items():
        print(f"  [{'PASS' if v else 'FAIL'}] {k}")
    print()
    print(f"  ALL CHECKS {'PASS' if all_pass else 'FAIL'}")
    print(f"  witness -> {path}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
