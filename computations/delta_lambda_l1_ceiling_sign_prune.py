#!/usr/bin/env python3
"""Δ_λ ℓ¹-ceiling sign-only prune — magnitude-side analogue of the PROBE-4
KL-positivity prune.

Context
-------
The per-block binding closure (Track D / Option-E) is

    B(K)/m_e  =  Σ_λ  y_λ(q_0) · χ^λ(β_K) · Δ_λ(K),

with the *proven* chirality form (Lean PR #2416, sorry-free,
`S5SO3FiberAction.lean`)

    Δ_λ  =  sgn(w_0^{S_{λ'}}) · dim_λ        (sign-twist × Wedderburn dim).

The published evaluation undershoots every light isotope
(D −82.9 %, T −77.5 %, ³He −69.6 %, ⁴He −89.3 %).  Six fit-based closure
ansätze have failed and a 7th is barred by the three-calibration
discipline.  This script does **not** propose a closure.  It records a
*formalize-first* structural bound that PRUNES one sub-class of the
remaining search.

The invariant
-------------
Hold {y_λ, χ^λ} at their canonical values and hold the *magnitude*
|Δ_λ| = dim_λ fixed; let only the per-block *sign* vary — i.e. replace
sgn(w_0^{S_{λ'}}) by an arbitrary chirality rule s_λ ∈ {±1}.  The
contribution magnitude |y_λ χ^λ s_λ dim_λ| = |y_λ χ^λ dim_λ| is invariant
under the sign choice, so by the triangle inequality

    | Σ_λ  s_λ · (y_λ χ^λ dim_λ) |  ≤  Σ_λ |y_λ χ^λ dim_λ|  =:  ‖c‖₁ ,

for EVERY sign assignment {s_λ}.  ‖c‖₁ is therefore a hard ceiling on the
binding magnitude reachable by any sign/chirality re-derivation acting on
the existing term set.

The measurement (this script) shows ‖c‖₁ / |target| ∈ [0.36, 0.59] < 1 for
all of D/T/³He/⁴He.  Hence:

    (b) STRUCTURAL EXCLUSION (invariant: ℓ¹/triangle bound).  No sign- or
        chirality-only re-derivation of Δ_λ — keeping y_λ, χ^λ and
        |Δ_λ|=dim_λ fixed — can close the binding deficit; the ℓ¹ ceiling
        is 36–59 % of target.  A *magnitude-adding* ingredient is
        necessary: (i) a re-derived block magnitude |Δ_λ| ≠ dim_λ,
        (ii) re-weighted y_λ, or (iii) an additional term beyond the
        single Σ_λ sum (the T2–T6 many-body terms / A=4 interface
        operator).

This is the magnitude-side mirror of the PROBE-4 KL-positivity prune
(`docs/audits/2026-06-16-option-e-probe4-kl-positivity-prune.md`): PROBE-4
showed non-negative KL multiplicities supply |Δ_λ|=dim but never the
chirality sign; this shows the sign structure, even optimally reassigned,
never supplies the magnitude.  Together they bound the {sign-only} and
{current-magnitude-only} sub-classes from both sides.

Inputs are READ from canonical pinned witnesses (no q_0 re-solve, no tr_M
recompute, no pyhecke) — the diagnostic is pure ℓ¹ arithmetic on
already-canonical values, so it is reproducible in any environment and is
NOT subject to the ad-hoc-env witness skew.  dim_λ and the sign are pure
combinatorics (hook-length + Young-subgroup longest-element sign).

Producer for: computations/delta-lambda-l1-ceiling-sign-prune.witness.json
"""
from __future__ import annotations
from computations.substrate.codata_constants import AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION, M_E_MEV
import json, math, os, hashlib, datetime

HERE = os.path.dirname(os.path.abspath(__file__))


# ---- partition combinatorics (exact integers) ----
def dim_irrep(part: list[int]) -> int:
    """Classical S_n irrep dimension via the hook-length formula."""
    n = sum(part)
    maxc = part[0]
    col = [0] * maxc
    for r in part:
        for j in range(r):
            col[j] += 1
    hooks = 1
    for i, r in enumerate(part):
        for j in range(r):
            hooks *= (r - j - 1) + (col[j] - i - 1) + 1
    return math.factorial(n) // hooks


def conj(part: list[int]) -> list[int]:
    return [sum(1 for r in part if r > j) for j in range(part[0])]


def sgn_w0_young(part: list[int]) -> int:
    """Sign of the longest element of the Young subgroup S_part = ∏ S_{part_i}.
    The longest element of S_m has sign (-1)^{m(m-1)/2}."""
    s = 1
    for m in part:
        if (m * (m - 1) // 2) % 2 == 1:
            s = -s
    return s


def delta_sgndim(part: list[int]) -> int:
    """Proven Δ_λ form (PR #2416): sgn(w_0^{S_{λ'}}) · dim_λ."""
    return sgn_w0_young(conj(part)) * dim_irrep(part)


def witness_provenance(path: str) -> dict:
    d = json.load(open(path))
    return {
        "file": os.path.basename(path),
        "scriptHash": d.get("scriptHash"),
        "scriptCommitSha": d.get("scriptCommitSha"),
        "computedAt": d.get("computedAt"),
    }


# CODATA m_e; B_AME values from delta-lambda-canonical-residual.witness.json
M_E_MEV = M_E_MEV
ISOTOPES = {
    # name : (chi witness, n=3A key, B_AME MeV, Z, N, A)
    "D":   ("atom-chi-rust-d.witness.json",   "6",  2.224566, 1, 1, 2),
    "T":   ("atom-chi-rust-t.witness.json",   "9",  AME_B_TRITIUM_MEV_VALIDATION, 1, 2, 3),
    "3He": ("atom-chi-rust-3he.witness.json", "9",  7.718043, 2, 1, 3),
    "4He": ("atom-chi-rust-4he.witness.json", "12", AME_B_HE4_MEV_VALIDATION, 2, 2, 4),
}


def main() -> None:
    ywit = os.path.join(HERE, "y-lambda-at-q0.witness.json")
    ydat = json.load(open(ywit))["data"]["by_n"]
    q0 = json.load(open(ywit))["parameters"]["q_0"]

    rows = []
    sources = {"y_lambda": witness_provenance(ywit)}
    all_below = True
    for name, (chif, nkey, B, Z, N, A) in ISOTOPES.items():
        chipath = os.path.join(HERE, chif)
        chi = json.load(open(chipath))["data"]["atom"]["by_partition"]
        sources[f"chi_{name}"] = witness_provenance(chipath)
        yl = {tuple(e["partition"]): float(e["y_at_q0_50dps"]) for e in ydat[nkey]}

        net = 0.0
        l1 = 0.0
        pos = 0.0
        neg = 0.0
        for e in chi:
            p = tuple(e["partition"])
            c = yl[p] * float(e["chi_lambda"]) * delta_sgndim(list(p))
            net += c
            l1 += abs(c)
            if c > 0:
                pos += c
            else:
                neg += c
        target = -B / M_E_MEV  # binding is a negative energy contribution
        ceiling_ratio = l1 / abs(target)          # < 1  ⟹  sign-only fix impossible
        net_ratio = net / target                  # published undershoot fraction
        survive = net / l1 if l1 else 0.0          # magnitude surviving cancellation
        if ceiling_ratio >= 1.0:
            all_below = False
        rows.append({
            "atom": name, "Z": Z, "N": N, "A": A,
            "B_AME_MeV": B,
            "target_units_m_e": target,
            "net_sum_units_m_e": net,
            "l1_ceiling_units_m_e": l1,
            "pos_sum": pos, "neg_sum": neg,
            "net_over_target": net_ratio,
            "l1_ceiling_over_target": ceiling_ratio,
            "net_over_l1_survival": survive,
        })

    witness = {
        "engine": "python",
        "engineVersion": "pure-arithmetic-on-canonical-witnesses",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "computation": "delta-lambda-l1-ceiling-sign-prune",
        "scriptFile": "delta_lambda_l1_ceiling_sign_prune.py",
        "scriptHash": hashlib.sha256(open(__file__, "rb").read()).hexdigest()[:12],
        "description": (
            "ℓ¹-ceiling sign-only prune for the per-block binding closure "
            "B/m_e = Σ_λ y_λ χ^λ Δ_λ with the proven Δ_λ = sgn(w_0^{S_λ'})·dim_λ "
            "(PR #2416). For every sign reassignment s_λ∈{±1}, "
            "|Σ s_λ y_λ χ^λ dim_λ| ≤ ‖c‖₁ (triangle inequality). Measured "
            "‖c‖₁/|target| ∈ [0.36,0.59] < 1 for D/T/³He/⁴He ⟹ (b) STRUCTURAL: "
            "no sign/chirality-only re-derivation closes the binding deficit; "
            "a magnitude-adding ingredient is necessary. Magnitude-side mirror "
            "of the PROBE-4 KL-positivity prune. Pure ℓ¹ arithmetic on canonical "
            "y_λ + χ^λ witnesses (no recompute) — env-skew-immune."
        ),
        "invariant": "triangle/ell1: |Σ_λ s_λ a_λ| ≤ Σ_λ |a_λ| for all s_λ∈{±1}",
        "scope": "(b) structural-exclusion of the {sign/chirality-only on fixed y_λ,χ^λ,|Δ_λ|=dim} sub-class",
        "delta_lambda_form": "sgn(w_0^{S_{lambda'}}) * dim_lambda (proven, Lean PR #2416, S5SO3FiberAction.lean)",
        "parameters": {"q_0": q0, "m_e_MeV": M_E_MEV},
        "source_witnesses": sources,
        "data": {
            "rows": rows,
            "all_isotopes_l1_ceiling_below_target": all_below,
            "l1_ceiling_over_target_range": [
                min(r["l1_ceiling_over_target"] for r in rows),
                max(r["l1_ceiling_over_target"] for r in rows),
            ],
        },
        "allPassed": all_below,
    }
    out = os.path.join(HERE, "delta-lambda-l1-ceiling-sign-prune.witness.json")
    from witness_base import WitnessBuilder
    WitnessBuilder.wrap_legacy("atom-chi-rust-d", witness, script_path=__file__).save()
if __name__ == "__main__":
    main()
