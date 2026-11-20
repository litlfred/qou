#!/usr/bin/env python3
"""borromean_3body_cluster_sign_probe.py — the DERIVED Borromean (Brunnian,
irreducible) 3-body cluster: does its sign supply μ₃ = +0.4708 > 0, the sign
the multiplicative route provably cannot (#4354)?

The one open door #4354 left
----------------------------
#4354 (`QOU.MassTheory.Mu4RhoFCluster`, sorry-free) PROVED a 3-body SIGN wall:
no PAIRWISE (multiplicative) interface product `1 − ∏ᵢ fᵢ`, fᵢ ∈ [0,1], yields a
POSITIVE 3-body cluster (`productModel_3body_nonpos` + `markovParam_le_half`:
z ≤ ½ < 1 ∀ q>0). Yet the Δ_λ residual simplex (#4320) needs

    μ₂ = 0,   μ₃ = +0.4708 (> 0),   μ₄ = −4.591.

The DERIVED pairwise ρ_F cluster is c₃ < 0 (⟨T,³He⟩ = −1.59 MeV,
three-body-joint-trace-a3.witness.json). Surviving door: a NON-multiplicative,
ENHANCING 3-body operator.

The candidate: the Borromean irreducible 3-body operator (0 free params)
----------------------------------------------------------------------
The Borromean rings 𝓑₃ are the archetype of a BRUNNIAN 3-body object — three
components, every 2-sub-link TRIVIAL (unlinked), yet the whole genuinely 3-body
linked. So (i) the pairwise product VANISHES by construction (matches the #4354
wall exactly), and (ii) ALL content is the irreducible 3-body part — the
non-multiplicative operator the wall left open. It is already the mass formula's
`Vol(𝓑₃)·ρ` object (the H₃ Markov trace τ_Borr, GAP-A-4 Lean closed form).

The Ursell decomposition for a Brunnian object
----------------------------------------------
Connected 3-body cluster (binding units, framework convention B = E₀·(tr_free −
tr_atom), positive when a link REDUCES the trace):

    c₃ = joint − pair_sum − 1body_baseline.

For Borromean: every 2-sub-link is trivial ⇒ the pairwise binding contributions
B_a = B_b = B_c = 0 (each 2-sub-trace = unlink trace), so the pair_sum VANISHES
and the connected 3-body cluster is the FULL irreducible content:

    c₃^Borr = E₀·(τ_free − τ_Borr),   τ_free = τ(h=0) = 1 (3-component unlink).

CLOSED FORM (GAP-A-4, Lean BorromeanMarkovTrace):
    τ_Borr = (4 + h² − 3h⁴ − h⁶)/(h² + 4),   h = q − q⁻¹
    ⇒ 1 − τ_Borr = (3h⁴ + h⁶)/(h² + 4) = h⁴(3 + h²)/(h² + 4)  ≥ 0  ∀ real h,
      strictly > 0 for h ≠ 0 (q ≠ 1).

This positivity is UNCONSTRAINED by the #4354 `markovParam z ≤ ½` argument (that
bounds MULTIPLICATIVE pairwise products; the Borromean object is irreducible, not
a product of pairwise fᵢ). The sign of c₃^Borr is therefore free to be +, and the
closed form shows it IS +. The forward complement of #4354's ≤0 wall.

Discipline (STRICT anti-fit)
----------------------------
c₃^Borr is read from the DERIVED τ_Borr closed form (q₀ only, 0 free params — it
IS the 𝓑₃ object, no tuned enhancement). μ₃ = +0.4708 enters ONLY as the target
sign/scale. The honest gate is the SIGN (normalization-free). The MAGNITUDE is
reported with its error vs +0.4708; NO level-lift or enhancement factor is tuned
to hit it (that would be a FIT, and is NOT claimed / NOT wired). "No seventh
fit-based ansatz" + PROBE-4 KL-prune stand. Nothing wired.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

# q0 read BY NAME (bean qou-9ugp, 2026-09-04). This was a hardcoded PROTON
# literal -- the right VALUE by the wrong MECHANISM: it cannot follow the
# anchor, and it is invisible to the retired-pin drain because it never
# matched. Spellings across this family ran 13 to 60 digits for one pin.
import sys as _sys_qp  # noqa: E402
from pathlib import Path as _Path_qp  # noqa: E402
for _p_qp in (_Path_qp(__file__).resolve().parent.parent,
              _Path_qp(__file__).resolve().parent.parent / 'substrate'):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

set_compute_dps()
HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))

# ── derived substrate (0 params) ──────────────────────────────────────────────
Q0 = Q_MP
M_E = mp.mpf("0.51099895069")
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
E0 = _qbeta_e0.order_zero_scaled(M_E, Q0)                       # interface energy scale (MeV)
H = Q0 - 1 / Q0
Z = Q0**3 / (Q0**2 + 1)          # Markov z (for the g-channel)


def tau_borromean(h):
    """GAP-A-4 closed form: τ = |tr_M(β_Bor)| on H₃, β_Bor = (σ₁σ₂⁻¹)³."""
    return (4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4)


def li_2_q(x, q, qi):
    """Rogers q-dilogarithm Li₂^q(x) = Σ_{n≥1} x^n / (n·[n]_q),
    [n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹). Matches computations/_li_2_q_util.li_2_q."""
    hh = q - qi
    s = mp.mpf(0)
    xn = mp.mpf(1)
    for n in range(1, 400):
        xn *= x
        nq = (q**n - qi**n) / hh
        term = xn / (n * nq)
        s += term
        if abs(term) < mp.mpf(10) ** (-45):
            break
    return s


def main() -> int:
    qi = 1 / Q0
    tau = tau_borromean(H)
    tau_free = tau_borromean(mp.mpf(0))          # = 1 exactly (3-unlink)
    deficit = tau_free - tau                      # = (3h⁴+h⁶)/(h²+4)
    deficit_cf = (3 * H**4 + H**6) / (H**2 + 4)   # closed-form cross-check
    deficit_fac = H**4 * (3 + H**2) / (H**2 + 4)  # factored positivity form

    print("=" * 82)
    print("Borromean (Brunnian) irreducible 3-body cluster — SIGN + scale (0-fit)")
    print(f"  q₀={mp.nstr(Q0,10)}  h={mp.nstr(H,8)}  E₀={mp.nstr(E0,8)} MeV")
    print("=" * 82)
    print("\n(1) DERIVED Borromean H₃ trace (GAP-A-4 closed form)")
    print(f"  τ_Borr        = {mp.nstr(tau,12)}   (matches recompute's 0.9986 < 1)")
    print(f"  τ_free(unlink)= {mp.nstr(tau_free,12)}   (τ at h=0, 3-component unlink)")
    print(f"  1 − τ_Borr    = {mp.nstr(deficit,12)}")
    print(f"    closed form (3h⁴+h⁶)/(h²+4)   = {mp.nstr(deficit_cf,12)}")
    print(f"    factored     h⁴(3+h²)/(h²+4)  = {mp.nstr(deficit_fac,12)}  ≥ 0 ∀ real h")
    assert abs(deficit - deficit_cf) < mp.mpf(10) ** (-40)
    assert abs(deficit - deficit_fac) < mp.mpf(10) ** (-40)

    # ── (2) raw-trace binding cluster (framework B = E₀·(tr_free − tr_atom)) ──
    c3_raw = E0 * deficit
    print("\n(2) RAW-TRACE binding cluster  c₃^Borr = E₀·(τ_free − τ_Borr)")
    print(f"  c₃^Borr(raw) = {mp.nstr(c3_raw,8)} MeV   sign = {'+' if c3_raw > 0 else '-'}")

    # ── (3) Li₂^q g-channel cluster (same channel as the borromean tower) ──
    #   g(x) = −Li₂^q(−x); free = g(τ_free²)=g(1), atom = g(τ_free·τ_Borr).
    def g(x):
        return -li_2_q(-x, Q0, qi)
    c3_g = E0 * Z * Z * (g(tau_free * tau_free) - g(tau_free * tau))
    print("\n(3) Li₂^q g-CHANNEL cluster  c₃^Borr = E₀·z²·(g(τ_free²) − g(τ_free·τ_Borr))")
    print(f"  z={mp.nstr(Z,6)}  c₃^Borr(g) = {mp.nstr(c3_g,8)} MeV   "
          f"sign = {'+' if c3_g > 0 else '-'}")

    # ── (4) SIGN GATE vs μ₃, and honest scale error ──
    MU3 = mp.mpf("0.4708")   # #4320 residual simplex moment (dimensionless)
    c3_rhoF = mp.mpf("-1.587")  # DERIVED pairwise ρ_F cluster mean (T,³He), MeV — WALL side
    sign_match = (c3_raw > 0) == (MU3 > 0)
    print("\n(4) SIGN GATE (normalization-free honest gate) + scale")
    print(f"  target   μ₃           = {mp.nstr(MU3,5)}  (> 0)")
    print(f"  pairwise ρ_F  c₃      = {mp.nstr(c3_rhoF,5)} MeV  (< 0)  — #4354 WALL")
    print(f"  Borromean     c₃(raw) = {mp.nstr(c3_raw,5)} MeV  (> 0)  — SUPPLIES μ₃ sign")
    print(f"  SIGN MATCH (Borr vs μ₃) = {sign_match}   "
          f"(pairwise route sign match = FALSE, proved #4354)")
    err_vs_mu3 = c3_raw / MU3
    print(f"\n  MAGNITUDE (honest, NOT a gate — μ₃ is dimensionless, c₃ is MeV):")
    print(f"    c₃^Borr(raw) / μ₃ = {mp.nstr(err_vs_mu3,4)}  "
          f"(~{mp.nstr(MU3/c3_raw,3)}× short of +0.4708 read as MeV)")
    print(f"    c₃^Borr(raw) / |ρ_F c₃| = {mp.nstr(c3_raw/abs(c3_rhoF),4)}  "
          f"(~{mp.nstr(abs(c3_rhoF)/c3_raw,3)}× below the ρ_F ~1.5 MeV scale)")

    # ── (5) structural positivity ∀q (the formalize-first invariant) ──
    print("\n(5) STRUCTURAL POSITIVITY (the formalize-first invariant)")
    print("  1 − τ_Borr = h⁴(3+h²)/(h²+4) ≥ 0 ∀ real h, > 0 for h ≠ 0 (q ≠ 1).")
    print("  h⁴ ≥ 0, (3+h²) > 0, (h²+4) > 0  ⇒  deficit ≥ 0.  Sample check across q:")
    all_nonneg = True
    for qv in ["1.02", "1.05", "1.11", "1.20", "1.50", "2.00"]:
        hv = mp.mpf(qv) - 1 / mp.mpf(qv)
        d = (3 * hv**4 + hv**6) / (hv**2 + 4)
        all_nonneg = all_nonneg and (d >= 0)
        print(f"    q={qv:>5s}  h={mp.nstr(hv,5):>9s}  1−τ={mp.nstr(d,6):>11s}  ≥0 ✓")

    print("\n" + "=" * 82)
    print("VERDICT: DERIVED POSITIVE-SIGN LEAD (scope-(a)).")
    print("  c₃^Borr = E₀·(1 − τ_Borr) > 0 from the parameter-free 𝓑₃ trace (0 fit) —")
    print("  supplies exactly the μ₃ > 0 sign the pairwise MULTIPLICATIVE route provably")
    print("  CANNOT (#4354: productModel_3body_nonpos, z ≤ ½ < 1). The Brunnian object")
    print("  is non-multiplicative (pairwise sub-links trivial) so its cluster sign is")
    print("  NOT bounded by the z≤½ wall — the forward complement of that ≤0 wall.")
    print("  NOT A CLOSURE: bare-H₃ magnitude ~0.006 MeV is far below the +0.4708 / ~1.5")
    print("  MeV target scale; any level-lift/enhancement tuned to hit it would be a FIT")
    print("  (NOT claimed, NOT wired). Δ_λ remains open (per-λ, 2 anchors, sign≠magnitude).")

    witness = {
        "schema": "witness/v1",
        "producer": "computations/deltalambda/borromean_3body_cluster_sign_probe.py",
        "computation": "borromean-3body-cluster-sign",
        "description": (
            "The DERIVED Borromean (Brunnian, irreducible) 3-body cluster c₃^Borr = "
            "E₀·(τ_free − τ_Borr) with τ_free = τ(h=0) = 1 (3-unlink) and τ_Borr the "
            "GAP-A-4 H₃ Markov-trace closed form (4+h²−3h⁴−h⁶)/(h²+4). Being Brunnian "
            "(all 2-sub-links trivial) the pairwise binding vanishes and the whole "
            "content is the irreducible 3-body cluster. Closed form 1−τ_Borr = "
            "h⁴(3+h²)/(h²+4) ≥ 0 ∀ real h ⇒ c₃^Borr > 0 for q ≠ 1. This POSITIVE sign "
            "is the one μ₃ = +0.4708 needs and the one the MULTIPLICATIVE pairwise route "
            "provably CANNOT supply (#4354 productModel_3body_nonpos + markovParam_le_half, "
            "z ≤ ½ < 1). The Brunnian object is non-multiplicative so its sign is NOT "
            "bounded by the z≤½ wall. VERDICT: DERIVED POSITIVE-SIGN LEAD (scope-(a)); 0 "
            "free params. NOT a closure — bare-H₃ magnitude ~0.006 MeV ≪ +0.4708/~1.5 MeV "
            "target; any tuned level-lift/enhancement would be a FIT, not claimed, not "
            "wired. Δ_λ remains open."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "free_parameters": 0,
            "q0": str(Q0), "h": str(H), "z": str(Z), "E0_MeV": str(E0),
            "braid": "β_Bor = (σ₁σ₂⁻¹)³ on H₃ (Borromean, Brunnian)",
            "note": "μ₃ = +0.4708 enters only as target sign/scale; τ_Borr is q₀-only, 0 fit.",
        },
        "results": {
            "tau_borromean": str(tau),
            "tau_free_unlink": str(tau_free),
            "trace_deficit_1_minus_tau": str(deficit),
            "trace_deficit_closed_form": str(deficit_cf),
            "trace_deficit_factored": str(deficit_fac),
            "c3_borromean_raw_MeV": str(c3_raw),
            "c3_borromean_gchannel_MeV": str(c3_g),
            "c3_borromean_sign": "positive",
            "sign_gate": {
                "mu3_sign": "+", "mu3_value": str(MU3),
                "c3_borromean_sign": "+",
                "c3_pairwise_rhoF_sign": "-",
                "sign_match_borromean_vs_mu3": bool(sign_match),
                "pairwise_route_sign_match": False,
                "lean_wall_pairwise": "productModel_3body_nonpos + markovParam_le_half (z≤1/2<1)",
            },
            "magnitude_honest": {
                "c3_raw_over_mu3": str(err_vs_mu3),
                "shortfall_factor_vs_mu3": str(MU3 / c3_raw),
                "shortfall_factor_vs_rhoF_scale": str(abs(c3_rhoF) / c3_raw),
                "note": "μ₃ dimensionless, c₃ in MeV — scale comparison is indicative, "
                        "NOT the gate; the honest gate is the SIGN.",
            },
            "positivity_all_q": bool(all_nonneg),
            "verdict": {
                "classification": "DERIVED POSITIVE-SIGN LEAD (scope-(a))",
                "sign_supplied": True,
                "magnitude_closure": False,
                "free_param_count": 0,
                "is_fit": False,
                "wired": False,
                "complement_of_4354": (
                    "forward complement: #4354 proves multiplicative ⇒ cluster ≤ 0; "
                    "this proves Brunnian-irreducible ⇒ cluster ≥ 0. The μ₃ > 0 sign "
                    "SELECTS the Brunnian (non-multiplicative) operator."
                ),
                "delta_lambda_status": "OPEN — sign lead only; per-λ magnitude unclosed.",
                "anti_fit": "no enhancement/level-lift tuned to μ₃; τ_Borr q₀-only, 0 fit.",
            },
        },
        "scriptCommitSha": "uncommitted",
    }
    out = HERE / "borromean-3body-cluster-sign.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added.
    #
    # CORRECTED 2026-09-04 (bean qou-9ugp). This read "no q0 in this producer's
    # cone; stamp provenance only" and passed `q0_anchor=False`, which makes the
    # builder write `q0Anchor: "independent"` with the reason "no q0-dependent
    # field in this witness". That is FALSE: this witness's own `parameters`
    # carry q0 = 1.1099785827513808..., h = q0 - 1/q0, z = q0**3/(q0**2 + 1)
    # (convention D) and E0_MeV -- four fields that all move with the pin.
    #
    # It was invisible until now for the `qou-ftuv` reason:
    # `stamp_staleness_metadata` writes `q0Anchor` only inside
    # `if "q0Anchor" not in payload`, and the committed witness already carried a
    # `proton` key from an earlier pass. The stale key was masking the producer's
    # own declaration; re-running is what exposed it. Sixth false independence
    # declaration found in this drain.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    for _k in ("q0Anchor", "q0AnchorReason", "q0Value", "q0Values"):
        witness.pop(_k, None)          # do not inherit a stale stamp (qou-ftuv)
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None,
        q0_anchor="proton", q0_value=str(witness["parameters"]["q0"]))
    out.write_text(json.dumps(witness, indent=2))
    print(f"\nwitness -> {out.relative_to(COMP.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
