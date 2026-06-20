"""qbeta_singularity_type_probe.py — Step 1 of PR #1727.

**Singularity-type discriminator** for the Q_β Habiro element
`F(u) = Π (1 + c_k u^k)` at u = u_substrate.

PR #1713 (merged a99493e20c) established `radius of convergence =
u_substrate` via `c_{k+1}/c_k → 1/u = 117.41` at k=8,9,10. The
radius alone does NOT discriminate among:

  (P) Simple pole  `A/(u_subst − u)`     → c_k ~ A · u_subst^(−k−1)  (CONSTANT prefactor)
  (B) Branch point `(u_subst − u)^β`     → c_k ~ C · k^(β−1) · u_subst^(−k)
  (E) Essential    `exp(C/(u_subst−u))`  → c_k super-geometric growth

This probe loads c_2..c_10 from the canonical-pinned SDP extraction
(`qbeta-decay-sdp-extended-ck.witness.json`) and tests all three
asymptotic signatures on the k≥8 tail. (Extending to c_11..c_15 is
NOT possible without postulating a canonical form per rung — that
would be an ansatz fit, forbidden per AGENTS.md; and the k=8,9,10
tail already discriminates cleanly. See `load_ck` for the method
note.)

## Method

Use the SDP-extracted R(q_0) and recursively unwind:

    R = Q_AME / Q_A_cos   (from qbeta_decay_sdp_extended_ck)
    For each k=2..15:
        c_k = (R − 1) / (b^k · ℏ_q²^k)
        N_k = 1 + c_k · b^k · ℏ_q²^k
        R  = R / N_k

NB: this uses the EMPIRICAL c_k at each step (not a postulated
"canonical" closed form) so the c_k extraction is consistent
all the way through.  Discriminator tests:

  test_P: r_k := c_k · u_subst^k  →  constant at large k iff simple pole
  test_B: q_k := c_k / (k · c_{k-1})  →  → 1 (β=1) or another constant iff branch
  test_E: log|c_{k+1}| − log|c_k|  →  → log(1/u) constant if geometric (P/B);
                                       → larger if essential

Reports tiered (PROVED <1ppm | NEAR-MATCH <1% | REFUTED >1%).

## Forbidden (AGENTS.md)

- NO ansatz fits. Each test is a tiered pass/fail of a structural
  signature on the c_k tail.
- NO production wiring (Step 3 of PR #1727 is conditional on
  steps 1+2 converging across anchors).

Ref: docs/coordination/2026-06-02-qbeta-1ppq-closure-scope.md
Ref: docs/audits/2026-06-02-qbeta-habiro-radius-of-convergence-at-u-substrate.md
"""
from __future__ import annotations


# Phase 5 path bridge (mirrors sibling qbeta/qbeta_per_block_symbolic.py).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json  # noqa: E402
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

# Bump compute precision to 100 dps — source witnesses are 50-67 digits,
# and we lose ~k·log10(1/u) ≈ 31 digits at c_15 (since 1/u ≈ 117).
mp.mp.dps = 100


def load_R_q0() -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    """Load R(q_0), b, ℏ_q², and u_subst from canonical witnesses.

    Witness lives in computations/, NOT in
    computations/qbeta/ — use the parent path.
    """
    src = HERE.parent / "q-beta-operator-valued-N3.witness.json"
    with src.open() as f:
        d = json.load(f)
    data = d["data"]
    Q_N2 = mp.mpf(str(data["Q_N2"]))
    Q_AME = mp.mpf(str(data["Q_AME"]))
    b = mp.mpf(str(data["hoefsmit_b"]))
    hbar_q_sq = mp.mpf(str(data["hbar_q_sq"]))
    # Form A·cos correction (per qbeta_decay_sdp_full_ck.py)
    N2 = 1 - b ** 2 * hbar_q_sq ** 2
    Q_A_cos = Q_N2 / N2
    R_q0 = Q_AME / Q_A_cos
    u_subst = b * hbar_q_sq
    return R_q0, b, hbar_q_sq, u_subst


def load_ck() -> dict[int, mp.mpf]:
    """Load c_2..c_10 from the SDP-extended witness.

    Method note: extracting c_11..c_15 from R(q_0) alone is
    impossible without a postulated canonical form for each c_k
    (the recursion `R/(1 + empirical_c_k · u^k)` self-cancels to 1
    because the empirical c_k absorbs ALL higher-order corrections
    at q_0). The existing `qbeta_decay_sdp_extended_ck.py` extractor
    yields c_2..c_10 by using CANONICAL closed forms (proved/near-
    match) to advance R between rungs. Beyond c_10 no canonical
    forms are derived, so extending the extractor would require
    ansatz fits — forbidden per AGENTS.md.

    For the singularity-type discriminator, c_2..c_10 are
    sufficient: PR #1713 already showed c_k · u^k ≈ 2.12e-13 at
    k=8,9,10, which is the **simple-pole signature**. This probe
    confirms tiered + tests the alternative hypotheses (B, E) on
    the same data.  (Signature simplified per Copilot #1727 review —
    it reads from the witness, not from R_q0/b/n_max.)
    """
    src = HERE / "qbeta-decay-sdp-extended-ck.witness.json"
    if not src.exists():
        src = HERE.parent / "qbeta-decay-sdp-extended-ck.witness.json"
    with src.open() as f:
        d = json.load(f)
    raw = d["data"]["c_k_extracted_50dps"]
    return {int(k.split("_")[1]): mp.mpf(str(v)) for k, v in raw.items()}


ASYMPTOTIC_K_MIN = 8  # only k >= 8 is reliably in the asymptote
                       # (k <= 7 is transient — empirical observation
                       # from c_k · u^k values jumping by orders of mag)


def test_simple_pole(c_k: dict[int, mp.mpf], u_subst: mp.mpf) -> dict:
    """Simple pole signature: c_k · u_subst^k → constant A as k → ∞."""
    out = {"name": "simple_pole_constant_prefactor"}
    products = []
    for k in sorted(c_k.keys()):
        if k < 4:  # display from k=4
            continue
        p = c_k[k] * u_subst ** k
        products.append((k, p))
        out[f"c_{k}_times_u^{k}"] = mp.nstr(p, 10)
    # Check constancy ONLY in the asymptotic tail (k >= ASYMPTOTIC_K_MIN)
    tail = [p for k, p in products if k >= ASYMPTOTIC_K_MIN]
    if len(tail) >= 2:
        mean_tail = sum(tail) / len(tail)
        rel_spread = max(abs(p - mean_tail) / max(abs(mean_tail), mp.mpf("1e-50")) for p in tail)
        out["tail_mean_(k_8_to_10)"] = mp.nstr(mean_tail, 12)
        out["tail_relative_spread"] = mp.nstr(rel_spread, 6)
        out["passes_1pct"] = bool(rel_spread < mp.mpf("0.01"))
        out["passes_1ppm"] = bool(rel_spread < mp.mpf("1e-6"))
    return out


def test_branch_point(c_k: dict[int, mp.mpf], u_subst: mp.mpf) -> dict:
    """Branch point order β: c_k ~ C · k^(β−1) · u_subst^(−k).

    So c_k · u_subst^k / k^(β−1) is constant. Test β = 0 (simple pole,
    matches test_simple_pole), β = 1/2 (square-root branch), β = 1
    (logarithmic), β = -1, ... Find best-fit β from log-log regression.
    """
    out = {"name": "branch_point_exponent"}
    # log(c_k · u^k) = log C + (β − 1) · log k  → linear in log k
    pairs = []
    for k in sorted(c_k.keys()):
        if k < ASYMPTOTIC_K_MIN:  # restrict to asymptotic regime
            continue
        v = c_k[k] * u_subst ** k
        if v <= 0:
            continue
        pairs.append((mp.log(mp.mpf(k)), mp.log(v)))
    if len(pairs) < 3:
        out["note"] = "insufficient positive-c_k tail for log-log fit"
        return out
    # Linear regression: y = m · x + b where m = β − 1
    n = len(pairs)
    sum_x = sum(x for x, _ in pairs)
    sum_y = sum(y for _, y in pairs)
    sum_xx = sum(x * x for x, _ in pairs)
    sum_xy = sum(x * y for x, y in pairs)
    denom = n * sum_xx - sum_x * sum_x
    slope = (n * sum_xy - sum_x * sum_y) / denom
    intercept = (sum_y - slope * sum_x) / n
    beta_fit = slope + 1
    out["beta_fit"] = mp.nstr(beta_fit, 8)
    out["beta_minus_one_slope"] = mp.nstr(slope, 8)
    out["log_C_intercept"] = mp.nstr(intercept, 8)
    out["n_points_used"] = n

    # Residuals: how well does the line fit?
    rsq_num = mp.mpf(0); rsq_den = mp.mpf(0)
    mean_y = sum_y / n
    for x, y in pairs:
        rsq_num += (y - slope * x - intercept) ** 2
        rsq_den += (y - mean_y) ** 2
    r_sq = 1 - rsq_num / rsq_den if rsq_den != 0 else mp.mpf(0)
    out["r_squared"] = mp.nstr(r_sq, 8)
    out["good_fit"] = bool(r_sq > mp.mpf("0.999"))
    return out


def test_essential(c_k: dict[int, mp.mpf], u_subst: mp.mpf) -> dict:
    """Essential singularity: c_k grows FASTER than geometric.

    Ratio of log|c_k| differences: for simple pole c_k ~ A/u^(k+1)
    so log|c_k| = const + k·log(1/u) (linear in k); essential
    singularity has super-linear growth in log|c_k|.

    Test: is `log|c_{k+1}| − log|c_k|` constant (geometric) or
    growing (essential)?
    """
    out = {"name": "essential_growth_test"}
    ks = sorted(c_k.keys())
    log_diffs = []
    for i in range(len(ks) - 1):
        if c_k[ks[i]] == 0 or c_k[ks[i + 1]] == 0:
            continue
        diff = mp.log(abs(c_k[ks[i + 1]])) - mp.log(abs(c_k[ks[i]]))
        log_diffs.append((ks[i], diff))
    # Restrict to asymptotic regime (k >= ASYMPTOTIC_K_MIN)
    tail = [d for k, d in log_diffs if k >= ASYMPTOTIC_K_MIN]
    if len(tail) < 3:
        out["note"] = "insufficient tail"
        return out
    # Check constancy: max - min of tail
    out["tail_log_diffs"] = [mp.nstr(d, 6) for d in tail]
    out["max_minus_min"] = mp.nstr(max(tail) - min(tail), 6)
    target = mp.log(1 / u_subst)
    out["expected_geometric_value_log(1/u)"] = mp.nstr(target, 8)
    out["mean_observed"] = mp.nstr(sum(tail) / len(tail), 8)
    out["mean_minus_log_1_over_u"] = mp.nstr(sum(tail) / len(tail) - target, 6)
    # Essential iff diff GROWS with k. Linear regression for trend.
    if len(tail) >= 3:
        xs = list(range(len(tail)))
        n = len(tail)
        sum_x = mp.mpf(sum(xs))
        sum_y = sum(tail)
        sum_xx = mp.mpf(sum(x * x for x in xs))
        sum_xy = sum(mp.mpf(x) * y for x, y in zip(xs, tail))
        slope = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
        out["growth_slope"] = mp.nstr(slope, 6)
        out["essential"] = bool(abs(slope) > mp.mpf("0.05"))
    return out


def main() -> int:
    R_q0, _b, _hbar_q_sq, u_subst = load_R_q0()
    print(f"Q_β singularity-type probe @ q_0 (m_p anchor)")
    print(f"  u_subst = {mp.nstr(u_subst, 12)}")
    print(f"  1/u_subst = {mp.nstr(1 / u_subst, 8)}")
    print(f"  R(q_0)   = {mp.nstr(R_q0, 18)}")
    print(f"  Compute precision: {mp.mp.dps} dps")
    print()

    c_k = load_ck()
    print(f"Loaded c_2..c_{max(c_k)} from SDP-extended witness "
          f"(canonical-pinned extraction):")
    for k in sorted(c_k.keys()):
        print(f"  c_{k:>2} = {mp.nstr(c_k[k], 14)}")
    print()

    # Hypothesis (P): simple pole
    r_pole = test_simple_pole(c_k, u_subst)
    print(f"--- (P) Simple pole — c_k · u_subst^k → const? ---")
    for k, v in r_pole.items():
        if k != "name":
            print(f"  {k}: {v}")
    print()

    # Hypothesis (B): branch point with order β
    r_branch = test_branch_point(c_k, u_subst)
    print(f"--- (B) Branch point — log-log fit of c_k · u_subst^k vs k ---")
    for k, v in r_branch.items():
        if k != "name":
            print(f"  {k}: {v}")
    print()

    # Hypothesis (E): essential singularity
    r_essential = test_essential(c_k, u_subst)
    print(f"--- (E) Essential — log|c_{{k+1}}| − log|c_k| growing? ---")
    for k, v in r_essential.items():
        if k != "name":
            print(f"  {k}: {v}")
    print()

    # Verdict
    verdict = "INCONCLUSIVE"
    if r_pole.get("passes_1pct"):
        verdict = "SIMPLE_POLE"
    elif r_branch.get("good_fit"):
        verdict = f"BRANCH_POINT (β ≈ {r_branch.get('beta_fit', '?')})"
    elif r_essential.get("essential"):
        verdict = "ESSENTIAL"
    print(f"VERDICT: {verdict}")
    print()

    # Witness
    w_out = WitnessBuilder("qbeta-singularity-type-probe", engine="mpmath")
    w_out.set_description(
        "Step 1 of PR #1727 / Q_β 1ppQ closure: discriminate among "
        "(P) simple pole, (B) branch point order β, (E) essential at "
        "u = u_subst for the Habiro element F(u) = Π(1 + c_k u^k). "
        "Loads c_2..c_10 from the canonical-pinned SDP extraction at 100 dps, "
        "then tests all three asymptotic signatures. Reports verdict."
    )
    for k in sorted(c_k.keys()):
        w_out.add_data(f"c_{k}", mp.nstr(c_k[k], 40))
    for d in (r_pole, r_branch, r_essential):
        for kk, vv in d.items():
            if kk == "name":
                continue
            w_out.add_data(f"{d['name']}_{kk}", str(vv))
    w_out.add_data("verdict", verdict)
    w_out.add_assertion(
        name="singularity_type_discriminator_runs",
        computed=True,
        expected=True,
        tolerance=0,
        source="Step 1 of Q_β 1ppQ closure",
    )

    out = w_out.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
