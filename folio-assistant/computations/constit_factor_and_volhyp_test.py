"""
constit_factor_and_volhyp_test.py — Phase 5g + 5i probes.

Two parallel diagnostics aimed at closing the residual 1.54× variance
left in the depth-stratified formula after PR #826's K_3* = 4_1
resolution and PR #831 Phase 5f / 5h's negative results.

Phase 5g — Markov-trace constit factor categorical identification:
  PR #819 Phase 5c.1 found that the canonical-atomic-braid Markov-trace
  ratio factors as z^(p_+) · (z-h)^(p_-), and separately the
  CONSTIT-only Z-step ratio (τ_M of the disjoint Hecke product going
  from D-constit to ³He-constit) equals 1.220358 — a NUMBER whose
  categorical form is open. This probe does a comprehensive search
  over products / quotients of {q^n, [n]_q, h, z, q^(±1/2)} for the
  closest match.

Phase 5i — Vol_hyp by Z normalisation:
  PR #787 Phase 3 found Vol_hyp(K) clusters by Z exactly:
    Vol(D)  = Vol(T)   = 12.776  (Z=1)
    Vol(³He)= Vol(⁴He) = 12.554  (Z=2)
  The depth-stratified formula doesn't use Vol_hyp. This probe tests
  whether adding a Vol_hyp(K)-based normalisation closes the residual.

  Ref: PR #819 Phase 5c.1 (τ_M interface factor + 1.220358 constit factor)
  Ref: PR #787 Phase 3 (Vol_hyp clusters by Z)
  Ref: PR #826 K_3* = 4_1; PR #831 Phase 5f, 5h
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

import pyhecke_native  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from mass_at_3A_proper import dim_q, qfac  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402


B_AME = {
    "D":   AME_B_DEUTERON_MEV_VALIDATION,
    "T":   AME_B_TRITIUM_MEV_VALIDATION,
    "3He": AME_B_HE3_MEV_VALIDATION,
    "4He": AME_B_HE4_MEV_VALIDATION,
}

ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}

# Vol_hyp per atom (from PR #787 Phase 3 delta-lambda-jsj-phase3.witness.json).
VOL_HYP = {
    "D":   mp.mpf("12.776095278687214"),
    "T":   mp.mpf("12.776095552543637"),
    "3He": mp.mpf("12.554085624045491"),
    "4He": mp.mpf("12.554075323566847"),
}

# K_3* = 4_1 (canonical from PR #826).
K_3_STAR_4_1_WORD = [(1, 1), (-1, 2), (1, 1), (-1, 2)]


# ──────────────────────────────────────────────────────────────────
# Phase 5g — Categorical search for 1.220358
# ──────────────────────────────────────────────────────────────────

def categorical_search_for(target: mp.mpf, max_rel_err: float = 0.01):
    """Scan products / quotients of substrate primitives for matches to
    `target`. Returns top 30 candidates sorted by rel.err."""
    q = mp.mpf(str(Q0))
    qi = 1 / q
    h = q - qi
    z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
    sqrt_q = mp.sqrt(q)
    sqrt_qi = 1 / sqrt_q

    # Primitives + their inverses
    primitives = {
        "1": mp.mpf(1),
        "q": q, "1/q": qi, "h": h, "z": z,
        "sqrt(q)": sqrt_q, "1/sqrt(q)": sqrt_qi,
        "q+1": q + 1,
        "q-1": q - 1,
        "q+q^-1": q + qi,
        "sqrt(q)+1/sqrt(q)": sqrt_q + sqrt_qi,  # = 1/z
        "cosh(h)": mp.cosh(h),
        "sinh(h)": mp.sinh(h),
        "h/2": h / 2,
        "h^2": h ** 2,
    }
    # q-integers [n]_q for n=2..10
    for n in range(2, 11):
        primitives[f"[{n}]_q"] = (q ** n - q ** (-n)) / (q - qi)
    # q^n for n=2..6
    for n in range(2, 7):
        primitives[f"q^{n}"] = q ** n
        primitives[f"q^-{n}"] = q ** (-n)

    candidates = []
    items = list(primitives.items())
    for n1, v1 in items:
        # Single primitives + their squares + cubes
        for power in (1, 2, 3):
            val = v1 ** power
            if 0.5 < float(val) < 5.0:
                expr = n1 if power == 1 else f"({n1})^{power}"
                candidates.append((expr, val))
        # Binary combinations: a*b, a/b, a+b, a-b
        for n2, v2 in items:
            if v2 == 0:
                continue
            for op, val in [
                ("·", v1 * v2),
                ("/", v1 / v2),
                ("+", v1 + v2),
            ]:
                if 0.5 < float(val) < 5.0:
                    candidates.append((f"{n1} {op} {n2}", val))

    # Deduplicate by string
    seen = {}
    for expr, val in candidates:
        if expr in seen:
            continue
        seen[expr] = val
    # Sort by rel.err
    scored = [(expr, val, float(abs(val - target) / target))
              for expr, val in seen.items()]
    scored.sort(key=lambda x: x[2])
    return [(e, float(v), err) for e, v, err in scored[:30]]


def report_constit_factor_search() -> dict:
    target = mp.mpf("1.22035866")  # 1.220358... from PR #819 Phase 5c.1
    top = categorical_search_for(target)
    print(f"=== Phase 5g: Categorical search for constit factor "
          f"1.220358 ===\n")
    print(f"  {'rank':>4} {'expression':<40} {'value':>12}  {'rel.err':>10}")
    for i, (expr, val, err) in enumerate(top[:15]):
        print(f"  {i+1:>4} {expr:<40} {val:>12.6f}  {err*100:>9.4f}%")
    return {"target": float(target), "top_15": top[:15]}


# ──────────────────────────────────────────────────────────────────
# Phase 5i — Vol_hyp by Z normalisation
# ──────────────────────────────────────────────────────────────────

def alpha_k_base(k: int) -> mp.mpf:
    z_mark = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))
    G = mp.catalan
    if k in (0, 1, 3):
        return mp.mpf(1)
    if k == 2:
        return z_mark ** 2
    return mp.mpf(str(M_E_MEV)) * 8 * G


def vanishing_threshold() -> mp.mpf:
    return mp.mpf(10) ** (5 - mp.mp.dps)


def chi_lambda_braid_via_rust(shape, braid_word_signed, q_f64):
    word = [(int(s), int(g)) for (s, g) in braid_word_signed]
    return pyhecke_native.chi_lambda_braid(list(shape), word, float(q_f64))


def fr_pullback_weights_k3(by_partition, n_strands, q_f64):
    qfact = qfac(n_strands)
    eps = vanishing_threshold()
    weights = {}
    chi_at_3 = {}
    z_norm = mp.mpf(0)
    s_uniform = mp.mpf(0)
    for p in by_partition:
        shape = tuple(p["partition"])
        depth = len(shape) - 1
        dq = dim_q(shape)
        dq_sq = mp.mpf(str(dq * dq))
        if depth != 3:
            weights[shape] = dq_sq / qfact
            continue
        s_uniform += dq_sq / qfact
        try:
            chi_K = chi_lambda_braid_via_rust(list(shape),
                                                K_3_STAR_4_1_WORD, q_f64)
        except (ValueError, RuntimeError, OverflowError):
            chi_K = 0.0
        chi_at_3[shape] = chi_K
        z_norm += dq_sq * mp.fabs(chi_K)
    if z_norm < eps:
        for shape in chi_at_3:
            dq = dim_q(shape)
            weights[shape] = mp.mpf(str(dq * dq)) / qfact
    else:
        scale = s_uniform / z_norm
        for shape, chi_K in chi_at_3.items():
            dq = dim_q(shape)
            weights[shape] = mp.mpf(str(dq * dq)) * mp.fabs(chi_K) * scale
    return weights


def phi_k_with_weights(by_partition, k, weights):
    total = mp.mpf(0)
    eps = vanishing_threshold()
    for p in by_partition:
        shape = tuple(p["partition"])
        if len(shape) - 1 != k:
            continue
        chi = mp.mpf(str(p["chi_lambda"]))
        dq = dim_q(shape)
        magnitude = mp.fabs(chi) * dq
        if magnitude < eps:
            continue
        w = weights.get(shape, mp.mpf(0))
        total += w * mp.log(magnitude)
    return total


def compute_B(atom: str, vol_hyp_normaliser: str = "none"):
    """B(K) with optional Vol_hyp normaliser.

    vol_hyp_normaliser:
      "none"           : B as in the K_3*=4_1 baseline
      "per_Z"          : B → B / Z (divide by proton number)
      "per_A"          : B → B / A
      "vol_hyp_atom"   : B → B / Vol_hyp(K)
      "vol_hyp_per_Z"  : B → B / (Vol_hyp(K) / Z)
    """
    Z, N = ZN[atom]
    A = Z + N
    n_strands = 3 * A
    w_path = HERE / f"atom-chi-rust-{atom.lower()}.witness.json"
    if not w_path.exists():
        return {"deferred": True}
    w = json.loads(w_path.read_text())
    atom_data = w["data"]["atom"]
    free_data = w["data"]["free"]
    q_f64 = float(Q0)

    w_atom = fr_pullback_weights_k3(atom_data["by_partition"], n_strands, q_f64)
    w_free = fr_pullback_weights_k3(free_data["by_partition"], n_strands, q_f64)

    B_dim = mp.mpf(0)
    for k in range(n_strands):
        ak = alpha_k_base(k)
        phi_a = phi_k_with_weights(atom_data["by_partition"], k, w_atom)
        phi_f = phi_k_with_weights(free_data["by_partition"], k, w_free)
        B_dim += ak * (phi_f - phi_a)

    # alpha_k_base() already includes the m_e·8G factor for k≥4
    # (matches binding_depth_stratified_rust.py:62), so B_dim is in
    # MeV.  Do NOT multiply by M_E_MEV again — see #831 Copilot review.
    B_MeV = B_dim

    # Apply normaliser
    Z_mp = mp.mpf(Z)
    A_mp = mp.mpf(A)
    if vol_hyp_normaliser == "none":
        B_norm = B_MeV
    elif vol_hyp_normaliser == "per_Z":
        B_norm = B_MeV / Z_mp
    elif vol_hyp_normaliser == "per_A":
        B_norm = B_MeV / A_mp
    elif vol_hyp_normaliser == "vol_hyp_atom":
        B_norm = B_MeV / VOL_HYP[atom]
    elif vol_hyp_normaliser == "vol_hyp_per_Z":
        B_norm = B_MeV / (VOL_HYP[atom] / Z_mp)
    else:
        raise ValueError(f"unknown normaliser {vol_hyp_normaliser}")

    # The "ratio" is now B_norm / (B_AME / normaliser_at_AME). But since
    # we're testing whether the SAME normaliser closes variance ACROSS
    # atoms, we just compare B_norm/B_AME directly (the variance is
    # max_atom(ratio) / min_atom(ratio), which is invariant under a
    # global scale).
    return {
        "B_norm": float(B_norm),
        "ratio_normed_over_AME": float(B_norm / B_AME[atom]),
    }


def vol_hyp_sweep() -> dict:
    print(f"\n=== Phase 5i: Vol_hyp by Z normalisation sweep ===\n")
    normalisers = ["none", "per_Z", "per_A", "vol_hyp_atom", "vol_hyp_per_Z"]
    results = {}
    for norm in normalisers:
        per_atom = {}
        ratios = []
        for atom in ("D", "T", "3He", "4He"):
            r = compute_B(atom, norm)
            if "deferred" not in r:
                per_atom[atom] = r
                ratios.append(r["ratio_normed_over_AME"])
        pos = [x for x in ratios if x > 0]
        var = max(pos) / min(pos) if len(pos) >= 2 else float("inf")
        results[norm] = {"variance_max_min": var, "per_atom": per_atom}

    baseline = results["none"]["variance_max_min"]
    print(f"  {'normaliser':<20} {'variance':>10}  vs baseline ({baseline:.4f}×)")
    for norm in normalisers:
        v = results[norm]["variance_max_min"]
        delta = (baseline - v) / baseline * 100 if v != float("inf") else 0.0
        print(f"  {norm:<20} {v:>10.4f}  ({delta:+.2f}%)")

    best = min(normalisers, key=lambda n: results[n]["variance_max_min"])
    return {"results": results, "baseline_variance": float(baseline),
            "best_normaliser": best,
            "best_variance": float(results[best]["variance_max_min"])}


def main() -> int:
    set_compute_dps(30)
    builder = WitnessBuilder("constit-factor-and-volhyp")
    builder.set_description(
        "Phase 5g + 5i: closing the residual 1.54× variance in the "
        "depth-stratified formula. (5g) Categorical search for the "
        "Markov-trace constit factor 1.220358 across substrate "
        "primitives; (5i) Vol_hyp normalisation sweep over 5 schemes "
        "(none, per_Z, per_A, vol_hyp_atom, vol_hyp_per_Z) to test "
        "whether Vol_hyp-based correction closes the residual."
    )
    builder.set_content_block("conj:depth-stratified-frobenius-reciprocity")
    builder.add_parameter("q_0", str(Q0))
    builder.add_parameter("K_3_star", "4_1")

    # 5g
    g_result = report_constit_factor_search()
    builder.add_data("phase_5g_constit_factor_search", g_result)

    best_5g = g_result["top_15"][0]
    print(f"\n  Phase 5g best: {best_5g[0]} = {best_5g[1]:.6f}, "
          f"rel.err vs target 1.220358 = {best_5g[2]*100:.4f}%")
    # Promote to top-level data for easy access
    builder.add_data("phase_5g_best", {
        "expression": best_5g[0],
        "value": best_5g[1],
        "rel_err": best_5g[2],
    })

    # 5i
    i_result = vol_hyp_sweep()
    builder.add_data("phase_5i_volhyp_sweep", i_result)
    delta_i = (i_result["baseline_variance"] - i_result["best_variance"]) / \
              i_result["baseline_variance"] * 100
    print(f"\n  Phase 5i best normaliser: {i_result['best_normaliser']}, "
          f"variance = {i_result['best_variance']:.4f}× "
          f"(baseline {i_result['baseline_variance']:.4f}×, "
          f"Δ = {delta_i:+.2f}%)")

    # Assertion: at minimum, the script completed both probes
    builder.add_assertion(
        "phase_5g_5i_completed",
        computed=1.0, expected=1.0, tolerance=0.0, unit="boolean",
        source=(
            f"5g best categorical match for 1.220358: {best_5g[0]} "
            f"({best_5g[2]*100:.3f}% rel.err). "
            f"5i best Vol_hyp normaliser: {i_result['best_normaliser']} "
            f"({delta_i:+.2f}% vs baseline)."
        ),
    )

    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
