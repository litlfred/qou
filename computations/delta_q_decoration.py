#!/usr/bin/env python3
"""
delta_q_decoration.py — Witness producer for the δ_q decoration of H_n(q).

Now a thin wrapper around the reusable `hecke_wedderburn` library.
Computes:

  1. δ_q for H_2(q) basis {1, σ_1} and force-carrier T_{2,9}
  2. δ_q for H_3(q) basis (6 NF elements) and force-carrier T_{3,5}
  3. Wedderburn decomposition of the bare H_2 molecular braid in H_4(q)
  4. Hypothesis test: bound-state projects onto force-carrier channels
     (3,1) and (2,1,1) per conj:force-carrier-intertwining-correspondence
  5. Algebraic identity α_EM = h² / [q · δ_q(T_29) · δ_q(T_35)]
     per prop:alpha-em-categorical-trace-ratio

Output: delta-q-decoration.witness.json

Reference content blocks:
  def:delta-q-decoration
  conj:force-carrier-intertwining-correspondence
  prop:alpha-em-categorical-trace-ratio
  rem:bound-state-frobenius-self-dual-channel
  conj:e-hartree-categorical-derivation
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as q0, Q_INV as qi0, HA, q_int
from hecke_wedderburn import (
    wedderburn_decompose, alpha_em_from_delta_q, force_carrier_channel,
    force_carrier_q_dim,
)

# ──────────────────────────────────────────────────────────────────────
WITNESS = {
    "engine": "python",
    "engineVersion": f"python {sys.version.split()[0]}",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "computation": "delta-q-decoration",
    "scriptFile": "delta_q_decoration.py",
    "description": (
        "δ_q Wedderburn decomposition for H_n(q), n=2,3,4. "
        "Tests the round-18 force-carrier intertwining correspondence "
        "(conj:force-carrier-intertwining-correspondence): does the "
        "bare H_2 molecular braid project onto the (3,1) and (2,1,1) "
        "Wedderburn channels matching T_{3,5} and T_{2,9} strand counts? "
        "Verifies the algebraic identity "
        "α_EM = h²/[q·δ_q(T_29)·δ_q(T_35)] "
        "(prop:alpha-em-categorical-trace-ratio)."
    ),
    "contentBlock": "def:delta-q-decoration",
    "parameters": {
        "q0": q0,
        "h": HA,
        "z": 1.0/(q0**0.5 + qi0**0.5),
    },
    "data": {},
    "assertions": [],
}

# ──────────────────────────────────────────────────────────────────────
# §1 — H_2(q) basis
# ──────────────────────────────────────────────────────────────────────
print("=" * 70)
print("§1  H_2(q)")
print("=" * 70)
H2 = {
    "identity_1": wedderburn_decompose([], 2),
    "sigma_1":    wedderburn_decompose([1], 2),
    "T_2_9":      wedderburn_decompose([1]*9, 2),
}
for name, dec in H2.items():
    print(f"\n  {name}:")
    for lam, v in dec.items():
        print(f"    λ={lam}: χ_λ = {v['chi_lambda']:>12.6f}, "
              f"dim_q = {v['dim_q_lambda']:>10.6f}, "
              f"w·χ/f = {v['trM_contribution']:>10.6f}")
WITNESS["data"]["H_2"] = H2

# ──────────────────────────────────────────────────────────────────────
# §2 — H_3(q) basis + T_{3,5}
# ──────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("§2  H_3(q)")
print("=" * 70)
H3 = {
    "identity_1":               wedderburn_decompose([], 3),
    "sigma_1":                  wedderburn_decompose([1], 3),
    "sigma_2":                  wedderburn_decompose([2], 3),
    "sigma_1_sigma_2":          wedderburn_decompose([1, 2], 3),
    "sigma_2_sigma_1":          wedderburn_decompose([2, 1], 3),
    "sigma_1_sigma_2_sigma_1":  wedderburn_decompose([1, 2, 1], 3),
    "T_3_5":                    wedderburn_decompose([1, 2]*5, 3),
}
for name, dec in H3.items():
    print(f"\n  {name}:")
    for lam, v in dec.items():
        print(f"    λ={lam}: χ_λ = {v['chi_lambda']:>12.6f}, "
              f"dim_q = {v['dim_q_lambda']:>10.6f}, "
              f"w·χ/f = {v['trM_contribution']:>10.6f}")
WITNESS["data"]["H_3"] = H3

# ──────────────────────────────────────────────────────────────────────
# §3 — H_2 molecular braid (bare) in H_4(q)
# ──────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("§3  H_4(q) — H_2 molecular braid (bare)")
print("=" * 70)
H4 = {"bare_molecule_b4": wedderburn_decompose([1, 2, 3], 4)}
for name, dec in H4.items():
    print(f"\n  {name}:")
    for lam, v in dec.items():
        print(f"    λ={lam}: χ_λ = {v['chi_lambda']:>12.6f}, "
              f"dim_q = {v['dim_q_lambda']:>10.6f}, "
              f"w·χ/f = {v['trM_contribution']:>10.6f}")
WITNESS["data"]["H_4"] = H4

# ──────────────────────────────────────────────────────────────────────
# §4 — Round-18 intertwining hypothesis
# ──────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("§4  Round-18 intertwining hypothesis (force-carrier channels)")
print("=" * 70)
bare = H4["bare_molecule_b4"]
target_T29 = force_carrier_channel(2, 4)   # (2,1,1)
target_T35 = force_carrier_channel(3, 4)   # (3,1)
contrib_31  = bare[target_T35]["trM_contribution"]
contrib_211 = bare[target_T29]["trM_contribution"]
contrib_22  = bare[(2, 2)]["trM_contribution"]
total_trM   = sum(v["trM_contribution"] for v in bare.values())

intertwining_supported = (
    abs(contrib_31)  > 1e-9 and
    abs(contrib_211) > 1e-9 and
    abs(contrib_22)  < 1e-9
)
print(f"\n  λ=(3,1)   [T_{{3,5}} channel]:   {contrib_31:>+10.6f}")
print(f"  λ=(2,1,1) [T_{{2,9}} channel]:   {contrib_211:>+10.6f}")
print(f"  λ=(2,2)   [exactly zero, exp]: {contrib_22:>+10.6f}")
print(f"  Intertwining hypothesis supported? {intertwining_supported}")

WITNESS["data"]["intertwining_hypothesis_test"] = {
    "molecular_braid_word": [1, 2, 3],
    "target_T29_channel":  list(target_T29),
    "target_T35_channel":  list(target_T35),
    "lambda_31_contribution":  float(contrib_31),
    "lambda_211_contribution": float(contrib_211),
    "lambda_22_contribution":  float(contrib_22),
    "total_trM": float(total_trM),
    "supported": bool(intertwining_supported),
    "reference": "conj:force-carrier-intertwining-correspondence",
    "all_lambdas": {str(lam): v["trM_contribution"] for lam, v in bare.items()},
}
WITNESS["assertions"].append({
    "name": "Bare H_2 molecular braid projects onto (3,1) [T_{3,5}] and (2,1,1) [T_{2,9}]; (2,2) zero",
    "computed": intertwining_supported,
    "expected": True,
    "passed":   intertwining_supported,
    "source":   "conj:force-carrier-intertwining-correspondence (round-18)",
})

# ──────────────────────────────────────────────────────────────────────
# §5 — α_EM categorical-trace identity
# ──────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("§5  α_EM = h² / [q · δ_q(T_{2,9}) · δ_q(T_{3,5})]")
print("=" * 70)
alpha_def, alpha_via, identity_match = alpha_em_from_delta_q()
delta_T29 = force_carrier_q_dim(2, 9)
delta_T35 = force_carrier_q_dim(3, 10)
print(f"\n  α_EM (definition)        = {alpha_def:.12e}")
print(f"  α_EM (via δ_q ratio)     = {alpha_via:.12e}")
print(f"  δ_q(T_{{2,9}}) = q^9 - q^-9   = {delta_T29:.10f}")
print(f"  δ_q(T_{{3,5}}) ≈ q^10 - q^-10 = {delta_T35:.10f}")
print(f"  Match within 10⁻¹²?      = {identity_match}")

WITNESS["data"]["alpha_em_identity"] = {
    "alpha_em_definition":    float(alpha_def),
    "alpha_em_via_delta_q":   float(alpha_via),
    "delta_q_T29":            float(delta_T29),
    "delta_q_T35_B2":         float(delta_T35),
    "match_within_1e_minus_12": bool(identity_match),
    "reference": "prop:alpha-em-categorical-trace-ratio",
}
WITNESS["assertions"].append({
    "name": "α_EM = h² / [q · δ_q(T_{2,9}) · δ_q(T_{3,5})] within 10⁻¹²",
    "computed": identity_match,
    "expected": True,
    "passed":   identity_match,
    "source":   "prop:alpha-em-categorical-trace-ratio (round-12/14)",
})

# ──────────────────────────────────────────────────────────────────────
# §6 — Frobenius self-duality check (round-18 remark)
# ──────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("§6  Frobenius self-duality of (3,1) ↔ (2,1,1) transpose pair")
print("=" * 70)
dim31  = bare[(3, 1)]["dim_q_lambda"]
dim211 = bare[(2, 1, 1)]["dim_q_lambda"]
w31    = bare[(3, 1)]["w_lambda"]
w211   = bare[(2, 1, 1)]["w_lambda"]
f31    = bare[(3, 1)]["f_lambda"]
f211   = bare[(2, 1, 1)]["f_lambda"]
self_dual = (
    abs(dim31 - dim211) < 1e-12 and
    abs(w31 - w211)     < 1e-12 and
    f31 == f211
)
print(f"\n  dim_q(V_(3,1))   = {dim31:.6f}")
print(f"  dim_q(V_(2,1,1)) = {dim211:.6f}  ⟹ equal: {abs(dim31-dim211)<1e-12}")
print(f"  w_(3,1)          = {w31:.6f}")
print(f"  w_(2,1,1)        = {w211:.6f}        ⟹ equal: {abs(w31-w211)<1e-12}")
print(f"  f_(3,1)          = {f31}")
print(f"  f_(2,1,1)        = {f211}             ⟹ equal: {f31 == f211}")
print(f"  Frobenius self-dual? {self_dual}")

WITNESS["data"]["frobenius_self_dual_check"] = {
    "dim_q_V_31":  float(dim31),
    "dim_q_V_211": float(dim211),
    "w_31":        float(w31),
    "w_211":       float(w211),
    "f_31":        int(f31),
    "f_211":       int(f211),
    "self_dual":   bool(self_dual),
    "reference":   "rem:bound-state-frobenius-self-dual-channel",
}
WITNESS["assertions"].append({
    "name": "(3,1) and (2,1,1) are transpose pair: equal dim_q, w, f",
    "computed": self_dual,
    "expected": True,
    "passed":   self_dual,
    "source":   "rem:bound-state-frobenius-self-dual-channel (round-18)",
})

# ──────────────────────────────────────────────────────────────────────
# §6b — Closed-form characters (round-19 task 1)
# ──────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("§6b Closed-form q-monomial χ_λ(σ_1·σ_2·σ_3)")
print("=" * 70)
chi_4    = bare[(4,)]["chi_lambda"]
chi_31_v = bare[(3, 1)]["chi_lambda"]
chi_22_v = bare[(2, 2)]["chi_lambda"]
chi_211_v= bare[(2, 1, 1)]["chi_lambda"]
chi_1111 = bare[(1, 1, 1, 1)]["chi_lambda"]

predictions = {
    "(4)":       (chi_4,    q0**3,        "q^3"),
    "(3,1)":     (chi_31_v, -q0,          "-q"),
    "(2,2)":     (chi_22_v, 0.0,          "0"),
    "(2,1,1)":   (chi_211_v, qi0,         "q^-1"),
    "(1,1,1,1)": (chi_1111, -qi0**3,      "-q^-3"),
}
print(f"\n{'λ':<10} {'χ_λ':>14} {'predicted':>14} {'closed-form':>14} {'match':>8}")
all_match = True
for lam_str, (got, pred, formula) in predictions.items():
    ok = abs(got - pred) < 1e-9
    print(f"  {lam_str:<8} {got:>+14.10f} {pred:>+14.10f} {formula:>14} {'✓' if ok else '✗':>8}")
    all_match = all_match and ok
WITNESS["data"]["closed_form_characters"] = {
    "chi_4_eq_q3":          abs(chi_4 - q0**3) < 1e-9,
    "chi_31_eq_neg_q":      abs(chi_31_v - (-q0)) < 1e-9,
    "chi_22_eq_zero":       abs(chi_22_v) < 1e-9,
    "chi_211_eq_q_inv":     abs(chi_211_v - qi0) < 1e-9,
    "chi_1111_eq_neg_qm3":  abs(chi_1111 - (-qi0**3)) < 1e-9,
    "all_match":            all_match,
    "reference":            "round-19 task 1 finding",
}
WITNESS["assertions"].append({
    "name": "All χ_λ(σ_1σ_2σ_3) are clean q-monomials (q^3, -q, 0, q^-1, -q^-3)",
    "computed": all_match,
    "expected": True,
    "passed":   all_match,
    "source":   "round-19 task 1 (closed-form)",
})

# ──────────────────────────────────────────────────────────────────────
# §6c — Dressed projection (round-19 task 2)
# ──────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("§6c Dressed H_2 molecular braid (T_dr = α·σ_2 + β·1, K-shell q^5)")
print("=" * 70)
alpha_dr = (q0**5 + qi0**5) / (q0 + qi0)
beta_dr  = q0**5 - alpha_dr * q0
dec_no_mid = wedderburn_decompose([1, 3], 4)
dressed_chars = {}
print(f"  α = (q^5+q^-5)/(q+q^-1) = {alpha_dr:.6f}")
print(f"  β = q^5 - α·q           = {beta_dr:.6f}")
print()
print(f"{'λ':<14} {'χ_bare':>10} {'χ_no_mid':>10} {'χ_dressed':>11} {'w·χ/f bare':>11} {'w·χ/f dressed':>14}")
total_dressed = 0.0
H4_dressed = {}
for lam in bare:
    chi_b = bare[lam]['chi_lambda']
    chi_nm = dec_no_mid[lam]['chi_lambda']
    chi_dr = alpha_dr * chi_b + beta_dr * chi_nm
    dressed_chars[lam] = chi_dr
    w = bare[lam]['w_lambda']
    f = bare[lam]['f_lambda']
    c_bare = w * chi_b / f
    c_dr = w * chi_dr / f
    total_dressed += c_dr
    H4_dressed[lam] = {
        "chi_bare":     float(chi_b),
        "chi_no_middle":float(chi_nm),
        "chi_dressed":  float(chi_dr),
        "w_lambda":     float(w),
        "f_lambda":     int(f),
        "trM_bare":     float(c_bare),
        "trM_dressed":  float(c_dr),
    }
    print(f"  {str(lam):<12} {chi_b:>+10.4f} {chi_nm:>+10.4f} {chi_dr:>+11.4f} {c_bare:>+11.4f} {c_dr:>+14.4f}")

force_carrier_dressed = H4_dressed[(3, 1)]["trM_dressed"] + H4_dressed[(2, 1, 1)]["trM_dressed"]
force_carrier_bare = H4_dressed[(3, 1)]["trM_bare"] + H4_dressed[(2, 1, 1)]["trM_bare"]
amplification = force_carrier_dressed / force_carrier_bare if abs(force_carrier_bare) > 1e-12 else 0.0
q5_q = float(q_int(5))
print()
print(f"  Total tr_M(σ_1·T_dr·σ_3) = {total_dressed:>+10.6f}")
print(f"  Force-carrier (3,1)+(2,1,1) bare    = {force_carrier_bare:>+10.6f}")
print(f"  Force-carrier (3,1)+(2,1,1) dressed = {force_carrier_dressed:>+10.6f}")
print(f"  Amplification ratio                 = {amplification:>10.4f}")
print(f"  Compare [5]_q at q_0                = {q5_q:>10.4f}  (close: {abs(amplification - q5_q)/q5_q < 0.05})")

WITNESS["data"]["dressed_braid"] = {
    "alpha_dr": float(alpha_dr),
    "beta_dr":  float(beta_dr),
    "per_lambda": {str(k): v for k, v in H4_dressed.items()},
    "total_trM_dressed": float(total_dressed),
    "force_carrier_bare":    float(force_carrier_bare),
    "force_carrier_dressed": float(force_carrier_dressed),
    "amplification_ratio":   float(amplification),
    "q_5_at_q0":             float(q5_q),
    "reference": "round-19 task 2 (dressed Wedderburn)",
}
WITNESS["assertions"].append({
    "name": "Force-carrier (3,1)+(2,1,1) amplifies by ≈ [5]_q under K-shell dressing",
    "computed": abs(amplification - q5_q)/q5_q < 0.05,
    "expected": True,
    "passed":   abs(amplification - q5_q)/q5_q < 0.05,
    "source":   "round-19 task 2 (dressed projection)",
})
WITNESS["assertions"].append({
    "name": "Dressing UNZEROES λ=(2,2) channel (selection-rule break)",
    "computed": abs(H4_dressed[(2,2)]["trM_dressed"]) > 1e-3,
    "expected": True,
    "passed":   abs(H4_dressed[(2,2)]["trM_dressed"]) > 1e-3,
    "source":   "round-19 task 2 (dressed projection)",
})

# ──────────────────────────────────────────────────────────────────────
# §7 — Save witness
# ──────────────────────────────────────────────────────────────────────
def _stringify_keys(obj):
    if isinstance(obj, dict):
        return {(str(k) if isinstance(k, tuple) else k): _stringify_keys(v)
                for k, v in obj.items()}
    if isinstance(obj, list):
        return [_stringify_keys(x) for x in obj]
    return obj

WITNESS["allPassed"] = all(a["passed"] for a in WITNESS["assertions"])
out_path = (WitnessBuilder

    .wrap_legacy("delta-q-decoration", _stringify_keys(WITNESS), script_path=__file__, engine="sympy")

    .save())

print(f"\n{'=' * 70}")
print(f"Witness written: {out_path}")
print(f"All assertions passed: {WITNESS['allPassed']}")
print(f"{'=' * 70}")
