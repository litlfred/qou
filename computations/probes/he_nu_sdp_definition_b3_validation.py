#!/usr/bin/env python3
"""Candidate operational definition of ν_SDP — validated on the B₃ atoms (D, ³He).

EXPLORATORY — derive-or-validate, no fit. Follow-up to the #2552 finding that no
solver computes ν_SDP (= ρ_F, the magic-A prefactor); the confirmed D/T/³He = 1,2,2
were hardcoded ("manual-historical-volume-match").

This probe tests one concrete, parameter-free operational definition against the two
confirmed atoms whose canonical braid lives in B₃ (so the H₃ Hoefsmit seminormal
is available in pure Python):

  CANDIDATE:  ν_SDP(K_w) = #{ λ ⊢ 3, λ ≠ (3) :  ρ_λ(T_w) lies in the PSD cone }
              (the symmetric part (M+Mᵀ)/2 ⪰ 0; the trivial rep (3) is EXCLUDED
               because ρ_(3)(T_w) = q^writhe > 0 is always positive — it is never an
               informative confinement channel).

Result (q₀ ≈ 1.10998):
  • D   (6_2,  writhe +2): triv (3) PSD [excluded]; std (2,1) sym-eigs [−0.89,+0.03]
        → NOT PSD; sign (1,1,1) +0.81 → PSD.  #non-trivial PSD = 1 = ν_SDP(D) ✓
  • ³He (L6a4, writhe  0): triv (3) PSD [excluded]; std (2,1) sym-eigs [+0.98,+1.01]
        → PSD; sign (1,1,1) +1.00 → PSD.        #non-trivial PSD = 2 = ν_SDP(³He) ✓

The discriminator is the std (2,1) block. The naive total PSD-block count (2, 3) does
NOT match (1, 2); excluding the always-positive trivial rep does.

CAVEAT (honest, 2-point validation): D and ³He are the only confirmed atoms in B₃.
On these two points the rule coincides with "(#PSD blocks) − 1". The third confirmed
atom T (8_11, ν=2) is in B₅ and needs the H₅ Hoefsmit seminormal (deferred to the
Rust crate) to DISCRIMINATE this rule from the "−1" reading. ⁴He application: count
the non-trivial PSD blocks of ρ_λ(T_w) over λ ⊢ 12 (needs Hoefsmit at H₁₂). This
probe does NOT extrapolate ⁴He — it pins + validates the definition on what is
computable today.

Hoefsmit H₃ standard (2,1) rep inlined from joint_tower_sdp_solver_v2.py
(self-contained; no cross-tree import). Reference: Geck–Pfeiffer §5.4 / Mathas Def 3.32.

Output: he-nu-sdp-definition-b3-validation.witness.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
# Canonical substrate q₀ (proton-pinned; tools/qou-substrate constants.py::q_at,
# == computations/q_parameter.Q). Inlined as the f64 literal to keep the probe
# self-contained (q_parameter's _path_bridge import chain is fragile from probes/).
Q0 = 1.1099785955573347

# ── Hoefsmit H₃ standard (2,1) rep at q₀ (inlined; cf. joint_tower_sdp_solver_v2.py) ──
def _hoefsmit_h3_standard(q):
    rho_T1 = np.array([[q, 0.0], [0.0, -1.0 / q]])
    denom = q * q + 1.0
    a = -1.0 / (q * denom)
    d = (q ** 3) / denom
    c = (q ** 4 + q * q + 1.0) / (denom * denom)
    rho_T2 = np.array([[a, 1.0], [c, d]])
    return rho_T1, rho_T2


def _rho_std(word, q):
    T1, T2 = _hoefsmit_h3_standard(q)
    h = q - 1.0 / q
    T1i, T2i = T1 - h * np.eye(2), T2 - h * np.eye(2)
    M = np.eye(2)
    for i in word:
        M = M @ {1: T1, -1: T1i, 2: T2, -2: T2i}[i]
    return M


def _rho_trivial(word, q):
    h = q - 1.0 / q
    v = 1.0
    for i in word:
        v *= q if i > 0 else (q - h)   # σ⁻¹ ↦ q⁻¹
    return v


def _rho_sign(word, q):
    h = q - 1.0 / q
    v = 1.0
    for i in word:
        v *= (-1.0 / q) if i > 0 else (-1.0 / q - h)   # σ⁻¹ ↦ −q
    return v


TOL = 1e-9
# B₃ confirmed atoms (canonical braid words + ν_SDP per the kashaev block).
ATOMS = {
    "D":   {"knot": "6_2",  "word": [1, -2, 1, 1, 1, -2],   "nu_canonical": 1},
    "3He": {"knot": "L6a4", "word": [-1, 2, -1, 2, -1, 2],  "nu_canonical": 2},
}


def block_psd(word, q):
    triv = _rho_trivial(word, q)
    sgn = _rho_sign(word, q)
    M = _rho_std(word, q)
    eigs = np.linalg.eigvalsh((M + M.T) / 2.0)
    return {
        "(3)":       {"value": float(triv), "psd": bool(triv >= -TOL), "trivial": True},
        "(2,1)":     {"eigs": [float(eigs[0]), float(eigs[1])],
                      "psd": bool(eigs.min() >= -TOL), "trivial": False},
        "(1,1,1)":   {"value": float(sgn), "psd": bool(sgn >= -TOL), "trivial": False},
    }


def main() -> int:
    print("=" * 80)
    print("  Candidate ν_SDP definition — B₃ validation (D, ³He)   q₀ = "
          f"{Q0:.8f}")
    print("  ν_SDP := #{ λ ≠ (3) : ρ_λ(T_w) PSD }  (exclude the always-positive trivial rep)")
    print("=" * 80)
    rows = []
    all_ok = True
    for name, info in ATOMS.items():
        b = block_psd(info["word"], Q0)
        nontrivial_psd = [lam for lam, d in b.items()
                          if not d["trivial"] and d["psd"]]
        nu_pred = len(nontrivial_psd)
        total_psd = sum(1 for d in b.values() if d["psd"])
        ok = (nu_pred == info["nu_canonical"])
        all_ok = all_ok and ok
        print(f"\n  {name} ({info['knot']}):")
        print(f"    (3)     triv  = {b['(3)']['value']:+.5f}  "
              f"{'PSD' if b['(3)']['psd'] else 'neg'}  [excluded: q^writhe>0]")
        print(f"    (2,1)   std   eigs(sym) = [{b['(2,1)']['eigs'][0]:+.4f}, "
              f"{b['(2,1)']['eigs'][1]:+.4f}]  {'PSD' if b['(2,1)']['psd'] else 'NOT PSD'}")
        print(f"    (1,1,1) sign  = {b['(1,1,1)']['value']:+.5f}  "
              f"{'PSD' if b['(1,1,1)']['psd'] else 'neg'}")
        print(f"    → non-trivial PSD blocks = {nontrivial_psd}  ⇒ ν_pred = {nu_pred}"
              f"   (canonical {info['nu_canonical']})  {'✓' if ok else '✗ MISMATCH'}")
        print(f"      [naive total PSD count = {total_psd} — does NOT match]")
        rows.append({"atom": name, "knot": info["knot"], "writhe": sum(
            1 if i > 0 else -1 for i in info["word"]),
            "blocks": b, "nu_predicted": nu_pred, "nu_canonical": info["nu_canonical"],
            "total_psd_count": total_psd, "match": ok})

    print("\n" + "=" * 80)
    print(f"  VALIDATION: {'PASS' if all_ok else 'FAIL'} — candidate reproduces "
          f"ν_SDP on both B₃ atoms (D=1, ³He=2)." if all_ok else
          "  VALIDATION: FAIL")
    print("  CAVEAT: 2 data points (both B₃); coincides with '(#PSD)−1' here. The")
    print("  discriminator is T (8_11, B₅, ν=2) — needs H₅ Hoefsmit (Rust). ⁴He needs H₁₂.")
    print("=" * 80)

    witness = {
        "computation": "he-nu-sdp-definition-b3-validation",
        "kind": "exploratory-probe",
        "description": (
            "Candidate operational definition ν_SDP = #{non-trivial Wedderburn blocks "
            "λ≠(n) with ρ_λ(T_w) PSD}, validated on the two confirmed B₃ atoms (D, ³He). "
            "Follow-up to #2552 (no solver computed ν_SDP). The trivial rep is excluded "
            "(q^writhe>0 always). Discriminator block = std (2,1). No fit."
        ),
        "engine": "numpy", "q0": float(Q0),
        "definition": "nu_SDP = count of lambda != (n) with rho_lambda(T_w) symmetric-part PSD",
        "atoms": rows,
        "validation_pass": all_ok,
        "caveats": [
            "2 data points, both B_3; on these two the rule equals (#PSD blocks)-1.",
            "Discriminator T (8_11) is B_5 — needs H_5 Hoefsmit (Rust crate) to confirm.",
            "He-4 application needs Hoefsmit at H_12 (p(12)=77 blocks); NOT extrapolated here.",
        ],
        "refs": ["PR #2552 (no-solver-computes-nu_SDP finding)",
                 "computations/joint_tower_sdp_solver_v2.py (H_3 Hoefsmit source)",
                 "content/quantum-observable-universe/mass-theory/kashaev-density-equals-sdp-multiplicity.md"],
        "discipline": "EXPLORATORY — validate-or-refute a definition, no fit, no forced ⁴He number.",
    }
    out = HERE.parent / "he-nu-sdp-definition-b3-validation.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"  witness: {out}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
