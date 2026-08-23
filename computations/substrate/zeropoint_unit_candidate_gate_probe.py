"""E_unit zero-point candidate family through the predicted-first gate (D2
of the full-derivation program).

PREDICTED-FIRST DERIVATION (stated before any evaluation, per the SS2f
gate). The toroidal ladder theorem (prop:hoefsmit-toroidal-ladder-locus)
forces the half-integer degree k - 1/2: in the oscillator reading of the
Hecke tower (Res.Ind = Ind.Res + Id, the Fock structure), the -1/2 is a
ZERO-POINT. If the 2H unit were this zero-point energy, its value would be
half a winding quantum of the relevant tower direction, times a canonical
energy anchor:

    E_zp(direction, anchor) = x(direction) * anchor,
      x(hyperbolic) = cosh(eta) - 1 = (q - q^{-1})^2 / 2   (eta = 2 ln q)
      x(compact)    = 1 - cos(2*pi/3) = 3/2                (zeta_3 winding)

with anchor in {m_e, E_0} — the only two canonical energy scales admitted
by the SS3d/SS2f discipline (single-factor class). This licenses exactly
FOUR candidates. Bounded enumeration, not a scan; each is evaluated ONCE
against the ledger target E_unit = 0.995940 MeV and recorded honestly.

Expected structure of a pass: match well inside the law's own 0.4 %
residual scale. Anything worse is a NEGATIVE and prunes the zero-point
family for the unit (scope (a): the family is excluded AS THE UNIT under
these two anchors; the zero-point reading of the -1/2 itself is untouched).
"""
import json
import os
import sys

import mpmath as mp

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

# 50-dps canonical exports (Copilot review: the f64 Q / E_CROSS exports
# truncate to ~16 digits; use the high-precision names).
from q_parameter import Q_50_DIGIT_STR, E_CROSS_MP  # noqa: E402

q = mp.mpf(Q_50_DIGIT_STR)
M_E = mp.mpf("0.51099895069")      # CODATA m_e, MeV
E0 = mp.mpf(E_CROSS_MP)            # canonical crossing energy anchor, 50 dps
E_UNIT_TARGET = mp.mpf("0.995940")  # SS2f ledger, MeV

x_hyp = (q - 1 / q) ** 2 / 2       # cosh(2 ln q) - 1
x_cpt = mp.mpf(3) / 2              # 1 - cos(2 pi / 3)

candidates = {
    "zp_hyperbolic_x_me": x_hyp * M_E,
    "zp_hyperbolic_x_E0": x_hyp * E0,
    "zp_compact_x_me": x_cpt * M_E,
    "zp_compact_x_E0": x_cpt * E0,
}

# pass criterion: within the law's own residual scale (0.4 %)
results = {}
n_pass = 0
for name, val in candidates.items():
    rel = abs(val - E_UNIT_TARGET) / E_UNIT_TARGET
    ok = rel < mp.mpf("0.004")
    n_pass += int(ok)
    results[name] = {
        "value_MeV": mp.nstr(val, 12),
        "rel_miss_vs_E_unit": mp.nstr(rel, 6),
        "passes_0.4pct": bool(ok),
    }

assertions = {
    "bounded_enumeration_four_candidates": len(candidates) == 4,
    "all_candidates_evaluated": len(results) == 4,
}

family_verdict = (
    "NEGATIVE — zero-point family pruned as the unit" if n_pass == 0
    else f"{n_pass}/4 candidate(s) inside 0.4% — inspect before any further step"
)

verdict = (
    f"ZERO-POINT UNIT FAMILY: {family_verdict}. Derivation stated first "
    "(forced -1/2 = Fock zero-point; half a winding quantum x canonical "
    "anchor), four licensed candidates evaluated once each against the "
    "SS2f target E_unit = 0.995940 MeV. Scope (a): this excludes the "
    "zero-point reading AS THE 2H UNIT under the m_e / E_0 anchors only; "
    "it does not exclude the zero-point interpretation of the forced "
    "-1/2 itself, and proposes nothing. The E_unit open stands."
)

witness = {
    "computation": "zeropoint_unit_candidate_gate_probe",
    "description": (
        "D2: the toroidal zero-point (forced -1/2) unit-candidate family "
        "through the predicted-first gate — derivation first, bounded "
        "4-candidate enumeration, honest recording."
    ),
    "discipline": ("predicted-first: derivation stated before evaluation; "
                   "bounded enumeration (4), not a scan; entropy bound "
                   "respected; (a)-scoped."),
    "auditOnly": "docs/audits/2026-07-06-parabolic-cylinder-toroidal-channel-interpolation.md",
    "results": {
        "q0": mp.nstr(q, 20),
        "E0_anchor_MeV": mp.nstr(E0, 12),
        "E_unit_target_MeV": mp.nstr(E_UNIT_TARGET, 10),
        "x_hyperbolic": mp.nstr(x_hyp, 12),
        "x_compact": mp.nstr(x_cpt, 6),
        "candidates": results,
        "n_pass": n_pass,
    },
    "assertions": assertions,
    "allPassed": bool(all(assertions.values())),
    "verdict": verdict,
}

from witness_base import WitnessBuilder  # noqa: E402

WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(_HERE, "zeropoint-unit-candidate-gate-probe.witness.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2, ensure_ascii=False)
    f.write("\n")

for name, r in results.items():
    print(f"  {name}: {r['value_MeV']} MeV  (miss {r['rel_miss_vs_E_unit']})  "
          f"{'PASS' if r['passes_0.4pct'] else 'NEG'}")
print(f"\nfamily: {family_verdict}")
print(f"\nwitness -> {out}")
