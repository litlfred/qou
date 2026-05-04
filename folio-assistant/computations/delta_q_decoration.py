#!/usr/bin/env python3
"""
delta_q_decoration.py — Witness producer for the δ_q decoration of H_n(q).

Now a thin wrapper around the reusable `hecke_wedderburn` library.
Computes:

  1. δ_q for H_2(q) basis {1, σ_1} and force-carrier T_{2,9}
  2. δ_q for H_3(q) basis (6 NF elements) and force-carrier T_{3,5}
  3. Wedderburn decomposition of the bare H_2 molecular braid in H_4(q)
  4. Hypothesis test: bound-state projects onto force-carrier channels
     (3,1) and (2,1,1) per prop:force-carrier-intertwining-correspondence
  5. Algebraic identity α_EM = h² / [q · δ_q(T_29) · δ_q(T_35)]
     per prop:alpha-em-categorical-trace-ratio

Output: delta-q-decoration.witness.json

Reference content blocks:
  def:delta-q-decoration
  prop:force-carrier-intertwining-correspondence
  prop:alpha-em-categorical-trace-ratio
  rem:bound-state-frobenius-self-dual-channel
  conj:e-hartree-categorical-derivation
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA
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
        "(prop:force-carrier-intertwining-correspondence): does the "
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
    "reference": "prop:force-carrier-intertwining-correspondence",
    "all_lambdas": {str(lam): v["trM_contribution"] for lam, v in bare.items()},
}
WITNESS["assertions"].append({
    "name": "Bare H_2 molecular braid projects onto (3,1) [T_{3,5}] and (2,1,1) [T_{2,9}]; (2,2) zero",
    "computed": intertwining_supported,
    "expected": True,
    "passed":   intertwining_supported,
    "source":   "prop:force-carrier-intertwining-correspondence (round-18)",
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
out_path = Path(__file__).parent / "delta-q-decoration.witness.json"
with open(out_path, "w") as f:
    json.dump(_stringify_keys(WITNESS), f, indent=2, default=str)

print(f"\n{'=' * 70}")
print(f"Witness written: {out_path}")
print(f"All assertions passed: {WITNESS['allPassed']}")
print(f"{'=' * 70}")
