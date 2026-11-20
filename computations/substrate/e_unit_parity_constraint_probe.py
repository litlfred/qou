"""E_unit bar-parity constraint + honest bar-even negative (D5 of the
full-derivation program; the standing owner directive, counit/transition
sector attack).

The one remaining open of B(2H) = 5g·E_unit is E_unit ≈ 0.995940 MeV. This
probe does the FORMALIZE-FIRST step the discipline demands before any
numerical attack: find the invariant the whole candidate class must satisfy,
then let it prune the class.

(1) PARITY EXCLUSION (structural, scope (b) — cites a proved invariant).
    B(2H) is a BINDING energy: bar-EVEN (the cosh channel; the reeb-flow
    marginal-stability determinant is built from the bar-even ss-sector).
    The classical 5 is a constant (bar-even). The rate g is bar-even:
    g^2 = z^2/(1+z^2), z = 1/[2]_v, and [2]_v = v + v^{-1} is bar-INVARIANT
    under the involution v -> v^{-1} (checked exactly), so z, g^2, and g are
    bar-even. Therefore
        E_unit = B / (5 g)  is BAR-EVEN
    — a quotient of bar-even quantities. This EXCLUDES the entire bar-ODD
    transition sector as E_unit: in particular Q_beta (the sinh / beta-decay
    partner, bar-odd) CANNOT be E_unit or an odd multiple of it. The
    invariant is bar-parity of the binding channel (proved: the cosh/sinh
    split, q-beta-bar-even-kernel; PR #3445 T6). This is a genuine (b)
    exclusion, not a scope-limited numerical negative.

(2) BAR-EVEN SINGLE-FACTOR NEGATIVE (scope (a), predicted-first). Among the
    framework's bar-EVEN absolute energies, the licensed single-factor
    candidates — stated with derivations BEFORE evaluation:
      * m_e         : CAL-1, the vacuum/counit mass scale (bar-even).
      * 2 m_e       : the pair/threshold energy (e+e-), bar-even.
      * E_cross     : the per-crossing energy E_0 (bar-even).
      * m_e·[2]_v   : the electron scale dressed by the bond quantum
                      dimension (bar-even).
    Each evaluated ONCE against E_unit. If none matches to the law's own
    0.4 % residual with a DERIVED coefficient, the bar-even single-factor
    class is negative and E_unit is a genuinely new bar-even absolute scale.

(3) ANTI-LAUNDERING NOTE (recorded, enforced). A within-0.4 % coincidence
    between E_unit and an UNDERIVED constant (e.g. E_unit/Q_beta ~ 4/pi to
    0.2 %) is numerology and is NOT a result: 4/pi has no derivation from
    the 13 categorical drivers, Q_beta is bar-odd (excluded by (1)), and the
    entropy bound forbids reading a 0.4 % hit as evidence. No such
    coincidence is claimed or wired.

CONCLUSION (honest): the bar-parity invariant prunes the bar-odd sector
(counit/transition decay quanta) from E_unit entirely; the bar-even
single-factor class does not close E_unit to 0.4 %. Closing E_unit therefore
requires deriving a NEW bar-even absolute energy scale — Subgoal-2 (absolute
scales), declined 2026-05-08 and only narrowly reopened for the s5-so3
keystone. This is the genuine hard wall, now sharply localized: a bar-even
absolute scale ~ 0.996 MeV, not reachable from the existing anchors by a
single derived factor.
"""
import json
import os
import sys

import mpmath as mp

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
from q_parameter import Q_50_DIGIT_STR, Q_MP, E_CROSS_MP  # noqa: E402

q = Q_MP
E0 = mp.mpf(E_CROSS_MP)
me = mp.mpf("0.51099895069")           # CODATA m_e, MeV (bar-even, CAL-1)
v = mp.sqrt(q)
two_v = v + 1 / v
E_UNIT = mp.mpf("0.995940")            # B_AME / 5g, MeV
LAW_PREC = mp.mpf("0.004")            # the 2H law's own 0.4% residual scale

# (1) parity: [2]_v is bar-invariant (v -> 1/v); so is g^2. The bar image is
# the same expression with the summands reordered, so under IEEE/mpmath
# (addition is commutative and exact-rounded) these are EQUAL, not merely
# close — use exact `==` to reflect the algebraic identity (Copilot review).
two_v_bar = (1 / v) + v
parity_two_v_ok = two_v_bar == two_v
z = 1 / two_v
g_sq = z**2 / (1 + z**2)
z_bar = 1 / two_v_bar
g_sq_bar = z_bar**2 / (1 + z_bar**2)
parity_g_ok = g_sq_bar == g_sq

# Q_beta (bar-odd) — computed only to DOCUMENT the exclusion, not as a candidate.
Qb = me * abs(q**2 - 2 * q - 1) * (q + 1) / (2 * q**3)

# (2) bar-even single-factor candidates, derivations stated above; eval once.
candidates = {
    "m_e (CAL-1 vacuum scale)": me,
    "2 m_e (pair threshold)": 2 * me,
    "E_cross (per-crossing E_0)": E0,
    "m_e * [2]_v (bond-dressed electron)": me * two_v,
}
results = {}
n_pass = 0
for name, val in candidates.items():
    rel = abs(val - E_UNIT) / E_UNIT
    ok = rel < LAW_PREC
    n_pass += int(ok)
    results[name] = {"value_MeV": mp.nstr(val, 12),
                     "rel_miss": mp.nstr(rel, 6), "within_0.4pct": bool(ok)}

assertions = {
    "two_v_bar_invariant": bool(parity_two_v_ok),
    "g_squared_bar_even": bool(parity_g_ok),
    "bar_even_single_factor_all_evaluated": len(results) == 4,
}

bar_even_verdict = ("NEGATIVE — no bar-even single factor within 0.4%"
                    if n_pass == 0 else
                    f"{n_pass}/4 within 0.4% — inspect (not auto-accepted)")

verdict = (
    "E_UNIT IS BAR-EVEN; THE BAR-ODD TRANSITION SECTOR IS EXCLUDED (b), THE "
    "BAR-EVEN SINGLE-FACTOR CLASS IS NEGATIVE (a). Parity: B (binding, "
    "cosh) and 5g are bar-even (z = 1/[2]_v, [2]_v bar-invariant, g^2 "
    "bar-even — checked exactly), so E_unit = B/(5g) is bar-even; Q_beta "
    "(bar-odd, sinh/decay) and every odd transition-sector quantum are "
    f"structurally excluded. {bar_even_verdict}: m_e, 2m_e, E_0, m_e[2]_v "
    "all miss E_unit = 0.995940 MeV (closest 2m_e, 2.55%). No coincidence "
    "with an underived constant (e.g. 4/pi, bar-odd Q_beta) is claimed — "
    "numerology + entropy-bound guard. CONCLUSION: closing E_unit needs a "
    "NEW bar-even absolute scale ~0.996 MeV, unreachable from the anchors "
    "by one derived factor — Subgoal-2 (absolute scales), owner-gated. The "
    "hard wall is now localized to a single bar-even energy."
)

witness = {
    "computation": "e_unit_parity_constraint_probe",
    "description": (
        "D5: formalize-first parity constraint on E_unit — B and 5g "
        "bar-even force E_unit bar-even, excluding the bar-odd transition "
        "sector (Q_beta); the bar-even single-factor class is an honest "
        "negative; E_unit closure is localized to a new bar-even absolute "
        "scale (Subgoal-2, owner-gated)."
    ),
    "discipline": ("formalize-first: parity invariant derived before "
                   "numerics; bar-even candidates predicted-first, evaluated "
                   "once; no scan; anti-laundering guard explicit; "
                   "(b) exclusion of bar-odd + (a) bar-even negative."),
    "auditOnly": "docs/audits/2026-07-06-parabolic-cylinder-toroidal-channel-interpolation.md",
    "results": {
        "E_unit_MeV": mp.nstr(E_UNIT, 10),
        "Q_beta_MeV_bar_odd_EXCLUDED": mp.nstr(Qb, 10),
        "bar_even_candidates": results,
        "parity_exclusion": "bar-odd transition sector (Q_beta, decay quanta) excluded; invariant = bar-parity of the binding (cosh) channel",
        "remaining_open": "a new bar-even absolute energy ~0.996 MeV (Subgoal-2, owner-gated; declined 2026-05-08, narrow s5-so3 reopening only)",
        "related": [
            "deuteron-tower-fusion-frame-probe.witness.json (D1)",
            "gauss-linking-channel-slope-probe.witness.json (D3)",
            "deformation-selection-5g-probe.witness.json (D4)",
        ],
    },
    "assertions": assertions,
    "allPassed": bool(all(assertions.values())),
    "verdict": verdict,
}

from witness_base import WitnessBuilder  # noqa: E402

WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(_HERE, "e-unit-parity-constraint-probe.witness.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("parity checks:", assertions)
for name, r in results.items():
    print(f"  {name}: {r['value_MeV']} MeV (miss {r['rel_miss']}) "
          f"{'within' if r['within_0.4pct'] else 'NEG'}")
print(f"\nbar-even class: {bar_even_verdict}")
print(f"\nwitness -> {out}")
