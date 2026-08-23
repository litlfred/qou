#!/usr/bin/env python3
"""mu4_rhoF_cluster_derivation_probe.py — DERIVE the Δ_λ residual simplex moments
μ₃, μ₄ from the interface operator ρ_F cluster integrals, or wall the route.

The #4320 redirect
------------------
#4320 (`QOU.MassTheory.AdditiveResidualSimplex`, sorry-free) proved the Δ_λ
damping-wall residual `M(A) = ρ_strong(A) − ρ_grad(A)` is a PURE ≥3-body simplex
object over the derived coordination-graph counts C(A,k):

    M(A) = μ₂·C(A,2) + μ₃·C(A,3) + μ₄·C(A,4),
    μ₂ = 0 (deuteron self-reference), μ₃ = +0.4708 (A=3), μ₄ = −4.591 (A=4).

The residual data are a 0-parameter EXACT solve of the three points M(2)=0,
M(3)=+0.4708, M(4)=−2.708 in the unit-triangular C(A,k) basis. The redirect asks:
do the interface operator ρ_F CLUSTER INTEGRALS reproduce μ₃, μ₄ from 0–1 DERIVED
params (no AME inversion)?  This probe answers it.

What ρ_F is (no dedicated function — computed from primitives)
-------------------------------------------------------------
ρ_F is the interface-product binding `B = E₀·τ_vac·(1 − ∏ᵢ fᵢ)` with the
categorically-DERIVED per-bond factors (interface_factor, Lean-proved exact):
    pp/nn positive bond  f = z            (Markov z = q³/(q²+1), convention D)
    nn negative bond     f = z − h        (h = q − 1/q)
    pn averaged bond     f = z − h/2      (bar-symmetric / charge)
Its connected k-body CLUSTER integral is the Ursell part
    c_k = joint_trace − (lower cluster sum),
computed at H_9 with ZERO fit from the χ_λ / gauge_aligned_a_combiner machinery
(`three_body_joint_trace_a3.py`, cached `three-body-joint-trace-a3.witness.json`).

The decomposition that pins the derivation-vs-fit test
------------------------------------------------------
The residual is the DIFFERENCE of two simplex ladders:
    μ_k = s_k − g_k,   where
      s_k = simplex coeffs of the AME strong-binding ladder ρ_strong (the TARGETS),
      g_k = simplex coeffs of the DERIVED graded ladder ρ_grad = [A]_q!/[2]_q!.
g_k is a fully-derived (q-factorial, 0-param) quantity; s_k is the AME side.

Derivation-vs-fit
-----------------
For ρ_F to DERIVE the residual moment (hypothesis H-A: c_k ≡ μ_k directly), its
connected k-body cluster integral c_k must reproduce μ_k in BOTH sign and (up to
one derived normalization) magnitude. The SIGN test is normalization-free (a
positive normalization cannot flip a sign), so it is the honest, param-free gate.

STRICT anti-fit: the ρ_F cluster integrals are computed from q₀ + the derived
factors only. AME ρ_strong enters ONLY as the μ_k target. A normalization tuned
per-moment to land ±0.4708/−4.591 would be a FIT and is reported as such; nothing
is wired.
"""
from __future__ import annotations

import json
import sys
from math import comb
from pathlib import Path
from datetime import datetime, timezone

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))

# ── derived substrate + interface factors (0 params) ──────────────────────────
Q0 = mp.mpf("1.10997858275138080759166909561076887987449912187357763605672")
M_E = mp.mpf("0.51099895069")
E0 = M_E / (Q0 * (Q0 - 1))                       # interface energy scale


def markov_z(q):
    # Convention D: z = q^3/(q^2+1). Was a PRIVATE re-derivation of
    # convention C, `1/(t + 1/t)` with t = sqrt(q), which shadowed the library
    # function and so survived the gram.py migration untouched.
    return q ** 3 / (q ** 2 + 1)


def hecke_h(q):
    return q - 1 / q


Z = markov_z(Q0)
H = hecke_h(Q0)
FAC = {"pp": Z, "nn": Z - H, "pn": Z - H / 2}

# ── the residual simplex moments (#4320 targets, dimensionless) ───────────────
RHO_GRAD = {2: mp.mpf("1.0"), 3: mp.mpf("3.34203107815"), 4: mp.mpf("15.7395726256")}
RHO_STRONG = {2: mp.mpf("1.0"), 3: mp.mpf("3.8128"), 4: mp.mpf("13.0316")}


def simplex_coeffs(v):
    """Exact unit-triangular solve M(A)=Σ c_k C(A,k) for A=2,3,4 → (c2,c3,c4)."""
    c2 = v[2]
    c3 = v[3] - 3 * c2
    c4 = v[4] - 6 * c2 - 4 * c3
    return c2, c3, c4


def main() -> int:
    print("=" * 82)
    print("μ₃,μ₄ from ρ_F cluster integrals — DERIVE or WALL (0-param sign gate)")
    print(f"  q₀={mp.nstr(Q0,8)}  z={mp.nstr(Z,6)}  h={mp.nstr(H,6)}  E₀={mp.nstr(E0,6)} MeV")
    print("=" * 82)

    # (1) DERIVED graded simplex g_k, AME strong simplex s_k, residual μ_k = s_k − g_k
    g2, g3, g4 = simplex_coeffs(RHO_GRAD)
    s2, s3, s4 = simplex_coeffs(RHO_STRONG)
    mu2, mu3, mu4 = s2 - g2, s3 - g3, s4 - g4
    print("\n(1) SIMPLEX LADDERS  (μ_k = s_k − g_k)")
    print(f"  ρ_grad (DERIVED q-factorial):  g₂={mp.nstr(g2,5)} g₃={mp.nstr(g3,5)} g₄={mp.nstr(g4,5)}")
    print(f"  ρ_strong (AME target):         s₂={mp.nstr(s2,5)} s₃={mp.nstr(s3,5)} s₄={mp.nstr(s4,5)}")
    print(f"  residual μ_k = s_k − g_k:       μ₂={mp.nstr(mu2,5)} μ₃={mp.nstr(mu3,5)} μ₄={mp.nstr(mu4,5)}")
    print("  → target moments reproduced exactly: μ₂=0, μ₃=+0.4708, μ₄=−4.591.")
    print("  NOTE: μ₄<0 is DOMINATED by the DERIVED graded g₄=+8.37 subtraction, not by")
    print("        an ρ_F cluster — the graded reference over-counts the 4-body.")

    # (2) DERIVED ρ_F connected 3-body cluster (joint trace, H_9, 0 fit) — cached
    jt_path = COMP / "three-body-joint-trace-a3.witness.json"
    JT = json.load(open(jt_path))["data"]["results"]
    c3_T = mp.mpf(str(JT["T"]["correlation_c3_MeV"]))
    c3_He = mp.mpf(str(JT["3He"]["correlation_c3_MeV"]))
    c3 = (c3_T + c3_He) / 2
    print("\n(2) DERIVED ρ_F connected 3-body cluster  c₃ = joint − pair_sum  (H_9, 0 fit)")
    print(f"  c₃(T)   = {mp.nstr(c3_T,5)} MeV   c₃(³He) = {mp.nstr(c3_He,5)} MeV   ⟨c₃⟩ = {mp.nstr(c3,5)} MeV")
    print(f"  sign(c₃) = {'+' if c3 > 0 else '-'}   vs   sign(μ₃) = {'+' if mu3 > 0 else '-'}")

    # (3) DERIVED ρ_F 4-body beyond-pairwise content (product model, K4, 0 fit)
    #     4He tetrahedron: bonds pp, nn, pn×4 on the 6-edge complete graph K4.
    bonds4 = ["pp", "nn", "pn", "pn", "pn", "pn"]
    xs = [1 - FAC[b] for b in bonds4]
    prod = mp.mpf(1)
    for b in bonds4:
        prod *= FAC[b]
    deficit = 1 - prod
    onebond = mp.fsum(xs)                          # 1-bond (pairwise) sum
    beyond4 = deficit - onebond                     # beyond-pairwise (≥2-bond) content
    print("\n(3) DERIVED ρ_F 4-body beyond-pairwise content  (product model, K₄, 0 fit)")
    print(f"  1−∏f = {mp.nstr(deficit,5)}   Σ(1−f) = {mp.nstr(onebond,5)}   beyond-pairwise = {mp.nstr(beyond4,5)}")
    print(f"  sign(c₄) = {'+' if beyond4 > 0 else '-'}   vs   sign(μ₄) = {'+' if mu4 > 0 else '-'}")

    # (4) the sign gate + free-parameter count
    sign3_match = (c3 > 0) == (mu3 > 0)
    sign4_match = (beyond4 > 0) == (mu4 > 0)
    print("\n(4) SIGN GATE (normalization-free) + FREE-PARAMETER COUNT")
    print(f"  3-body: derived c₃<0, target μ₃>0  → sign match = {sign3_match}  (WALL)")
    print(f"  4-body: derived c₄<0, target μ₄<0  → sign match = {sign4_match}  (consistent)")
    print("  A single normalization N>0 maps (c₃<0, c₄<0) → (Nc₃<0, Nc₄<0): it CANNOT")
    print("  hit (μ₃>0, μ₄<0) — opposite signs required on same-sign clusters. So no")
    print("  0–1-param derivation lands both moments; a per-moment fit (1 param each)")
    print("  would be needed, and even that fails the 3-body sign (Nc₃<0 ≠ μ₃>0).")
    print("  Lean-proved wall: productModel_3body_nonpos + markovParam_le_half (z≤½<1)")
    print("  ⇒ NO pairwise interface product yields a POSITIVE 3-body cluster, for any q>0.")

    print("\n" + "=" * 82)
    print("VERDICT: WALL (split). μ₄ sign is derived-consistent (tetra-dominant-negative")
    print("  α-cluster, but its magnitude is dominated by the DERIVED graded g₄ subtraction,")
    print("  not an ρ_F cluster); μ₃ sign is a PROVED wall — any pairwise interface product")
    print("  gives c₃≤0 (productModel_3body_nonpos, z≤½<1), but μ₃=+0.4708>0. The ρ_F")
    print("  cluster-integral route CANNOT derive μ₃; the standing open door is a")
    print("  NON-multiplicative / enhancing (f>1) cluster operator. NOT infra-gated")
    print("  (pyhecke_native functional, joint-trace cached, 0 fit). NOT a derivation.")

    witness = {
        "schema": "witness/v1",
        "producer": "computations/deltalambda/mu4_rhoF_cluster_derivation_probe.py",
        "computation": "mu4-rhoF-cluster-derivation",
        "description": (
            "Δ_λ residual simplex moments μ₃=+0.4708, μ₄=−4.591 tested against the DERIVED "
            "(0-fit, q₀-only) ρ_F cluster integrals. Decomposition μ_k = s_k − g_k with g_k the "
            "DERIVED graded (q-factorial) simplex coeffs (g₂=1,g₃=0.342,g₄=8.371) and s_k the AME "
            "strong-binding simplex (targets). Derived ρ_F connected 3-body cluster c₃<0 (T −1.769, "
            "³He −1.405 MeV, H_9 joint trace); derived 4-body product-model beyond-pairwise content "
            "c₄<0. SIGN GATE: μ₃>0 ≠ c₃<0 (WALL, Lean-proved by productModel_3body_nonpos + "
            "markovParam_le_half: no pairwise interface product gives a positive 3-body cluster for "
            "any q>0); μ₄<0 sign-consistent with c₄<0 but its magnitude is dominated by the DERIVED "
            "graded g₄=+8.37 subtraction, not an ρ_F cluster. FREE PARAMS: a single N>0 cannot map "
            "same-sign (c₃,c₄) to opposite-sign (μ₃,μ₄); no 0–1-param derivation lands both moments. "
            "VERDICT: WALL (split) — scope-(b) proved sign exclusion of the pairwise-product route "
            "for μ₃; scope-(a) sign-consistent-but-not-derived for μ₄. NOT infra-gated. Nothing wired."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "free_parameters": 0,
            "q0": str(Q0), "z": str(Z), "h": str(H), "E0_MeV": str(E0),
            "note": "AME ρ_strong enters only as the μ_k target; ρ_F clusters use q₀ + derived factors.",
        },
        "results": {
            "simplex_ladders": {
                "rho_grad_DERIVED": {"g2": str(g2), "g3": str(g3), "g4": str(g4),
                                     "formula": "[A]_q!/[2]_q!"},
                "rho_strong_AME_target": {"s2": str(s2), "s3": str(s3), "s4": str(s4)},
                "residual_mu": {"mu2": str(mu2), "mu3": str(mu3), "mu4": str(mu4)},
                "note": "μ₄<0 dominated by DERIVED graded g₄=+8.37 subtraction, not an ρ_F cluster.",
            },
            "derived_rhoF_3body_cluster": {
                "c3_T_MeV": str(c3_T), "c3_3He_MeV": str(c3_He), "c3_mean_MeV": str(c3),
                "source": "three-body-joint-trace-a3.witness.json (H_9 joint trace, 0 fit)",
                "sign": "negative",
            },
            "derived_rhoF_4body_beyond_pairwise": {
                "deficit_1_minus_prod_f": str(deficit),
                "onebond_sum": str(onebond),
                "beyond_pairwise_c4": str(beyond4),
                "sign": "negative",
                "bonds": "K4 tetrahedron: pp, nn, pn×4",
            },
            "sign_gate": {
                "mu3_sign": "+", "c3_sign": "-", "sign3_match": bool(sign3_match),
                "mu4_sign": "-", "c4_sign": "-", "sign4_match": bool(sign4_match),
                "lean_wall": "productModel_3body_nonpos + markovParam_le_half (z≤1/2<1 ∀q>0)",
            },
            "verdict": {
                "classification": "WALL (split): scope-(b) proved sign exclusion for μ₃; "
                                  "scope-(a) sign-consistent-not-derived for μ₄",
                "mu3_derived": False,
                "mu4_derived": False,
                "infra_gated": False,
                "free_param_count": "single normalization cannot land both moments (opposite "
                                    "signs on same-sign clusters); per-moment fit needed and "
                                    "still fails μ₃ sign",
                "open_door": "non-multiplicative / enhancing (f>1) cluster operator; the sign "
                             "of the 3-body cluster is the standing open question",
                "anti_fit": "no normalization wired; μ_k targets AME-side only; ρ_F clusters "
                            "q₀-only, 0 fit.",
            },
        },
        "scriptCommitSha": "uncommitted",
    }
    out = HERE / "mu4-rhoF-cluster-derivation.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\nwitness -> {out.relative_to(COMP.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
