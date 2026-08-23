#!/usr/bin/env python3
"""EXPLORATORY shape-probe — volume-Wedderburn Δ_λ candidate test.

Tests the user proposal (2026-06-02): close the open per-partition binding
density Δ_λ via a *per-Wedderburn-block q-hyperbolic volume* — i.e.

    B(K) = m_e · Σ_{λ ⊢ 3A} y_λ(q_0) · χ^λ(β_K) · Vol_λ ,

with Vol_λ a PARAMETER-FREE function of the partition λ alone, computed
from geometry (NOT fit to the binding). The motivating object is the
quantum-6j / volume-conjecture per-block ideal-tetrahedron volume
(Costantino–Murakami); here we test cheap, parameter-free geometric
proxies for Vol_λ built from the Clausen / Lobachevsky function
Λ(θ) = ½·Cl_2(2θ) = ½·Im Li_2(e^{2iθ}) — the volume of an ideal
hyperbolic tetrahedron — evaluated on the cell-content angles of λ.

This is EXPLORATORY (per `.claude/skills/local/production-vs-exploratory-
discipline.md`): it probes whether ANY parameter-free Vol_λ rule
reproduces the AME binding of D / T / ³He / ⁴He *simultaneously* with the
SAME rule (no per-isotope refit). The witness asserts the *refutation*
(no rule closes all four under tolerance) so an expected-negative does
NOT break CI; a positive (some rule closes all four) is surfaced loudly
for promotion review and a categorical derivation of that rule.

Inputs (already cached, canonical q_0): the per-partition (y_λ, χ_λ)
tables in `chi-{deuteron,tritium,helium-3,helium-4}-*-at-q0-50dps.witness.json`.

It does NOT touch production. Δ_λ remains an open gate (GAP-A-3/A-4).
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: F401,E402

import json
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
HERE = Path(__file__).parent

# CAL-1 electron mass (CODATA, the binding energy scale ρ).
M_E_MEV = mp.mpf("0.51099895069")

# AME2020 binding energies (MeV) for the four light isotopes whose
# χ^λ caches exist. These are the *targets*, never inputs to Vol_λ.
AME_B = {
    "deuteron": mp.mpf("2.2245662"),
    "tritium": mp.mpf("8.4818"),
    "helium-3": mp.mpf("7.7180"),
    "helium-4": mp.mpf("28.29566"),
}
CHI_CACHE = {
    "deuteron": "chi-deuteron-h6-at-q0-50dps.witness.json",
    "tritium": "chi-tritium-h9-at-q0-50dps.witness.json",
    "helium-3": "chi-helium-3-h9-at-q0-50dps.witness.json",
    "helium-4": "chi-helium-4-h12-at-q0-50dps.witness.json",
}


def lobachevsky(theta: mp.mpf) -> mp.mpf:
    """Λ(θ) = ½ Im Li_2(e^{2iθ}) — ideal-tetrahedron volume function."""
    z = mp.e ** (2j * theta)
    return mp.im(mp.polylog(2, z)) / 2


def cell_contents(part: list[int]) -> list[int]:
    """Contents c = j - i over all cells (1-indexed rows i, cols j)."""
    return [j - i for i, row in enumerate(part) for j in range(len(_row_cols(row)))]


def _row_cols(row_len: int) -> range:
    return range(row_len)


def partition_cells(part: list[int]):
    """Yield (i, j) 0-indexed cells; content = j - i."""
    for i, row in enumerate(part):
        for j in range(row):
            yield i, j


def hook_lengths(part: list[int]) -> list[int]:
    """Hook length of every cell."""
    hooks = []
    cols = [0] * (max(part) if part else 0)
    # column heights
    colh = [0] * (max(part) if part else 0)
    for i, row in enumerate(part):
        for j in range(row):
            colh[j] += 1
    for i, row in enumerate(part):
        for j in range(row):
            arm = row - j - 1
            leg = colh[j] - i - 1
            hooks.append(arm + leg + 1)
    return hooks


# ── Parameter-free Vol_λ candidate rules (function of λ only) ──
def vol_clausen_content(part: list[int], n: int) -> mp.mpf:
    """Σ_cells |Λ(π·c/n)| — Lobachevsky volume on content angles."""
    return sum(abs(lobachevsky(mp.pi * (j - i) / n)) for i, j in partition_cells(part))


def vol_clausen_hook(part: list[int], n: int) -> mp.mpf:
    """Σ_cells Λ(π·h/(n+1)) — Lobachevsky volume on hook angles."""
    hs = hook_lengths(part)
    return sum(abs(lobachevsky(mp.pi * h / (n + 1))) for h in hs)


def vol_content_sq(part: list[int], n: int) -> mp.mpf:
    """Σ_cells c²  (dimensionless 'spread' — needs a global scale)."""
    return mp.mpf(sum((j - i) ** 2 for i, j in partition_cells(part)))


def vol_abs_content(part: list[int], n: int) -> mp.mpf:
    """Σ_cells |c|  (dimensionless — needs a global scale)."""
    return mp.mpf(sum(abs(j - i) for i, j in partition_cells(part)))


def vol_uniform(part: list[int], n: int) -> mp.mpf:
    """Vol_λ = 1 (scalar Path-C baseline; the global scale is the single
    knot volume). Known: D −6.3%, A≥3 −56% (binding_link_volumes.py).

    ⚠ Corrected 2026-08-15 (bean `qou-jdhm`): read "D +0.2%, A≥3 −60%".
    The deuteron figure was trace convention C, excised by owner ruling
    2026-08-09; under convention D it is −6.3%.  ("D" in this line means
    the *deuteron*, not the trace convention — the collision is
    unfortunate and is why the convention is now named explicitly.)"""
    return mp.mpf(1)


RULES = {
    "clausen_content": (vol_clausen_content, "zero-param (volume units)"),
    "clausen_hook": (vol_clausen_hook, "zero-param (volume units)"),
    "content_sq": (vol_content_sq, "1 global scale"),
    "abs_content": (vol_abs_content, "1 global scale"),
    "uniform": (vol_uniform, "1 global scale (= scalar Path-C)"),
}


def load_blocks(fname: str):
    d = json.load(open(HERE / fname))
    out = []
    for r in d["by_partition"]:
        out.append({
            "part": list(r["partition"]),
            "y": mp.mpf(r["y_lambda"]),
            "chi": mp.mpf(r["chi_lambda"]),
        })
    n = d["n_strands"]
    return out, n


def main() -> int:
    isotopes = {}
    for atom, fname in CHI_CACHE.items():
        if not (HERE / fname).exists():
            print(f"  SKIP {atom}: {fname} missing")
            continue
        blocks, n = load_blocks(fname)
        isotopes[atom] = (blocks, n, AME_B[atom])

    print(f"Loaded {len(isotopes)} isotopes: {', '.join(isotopes)}")
    print(f"m_e = {float(M_E_MEV)} MeV\n")

    TOL = mp.mpf("0.05")  # 5 % per-isotope tolerance for a "hit"
    results = {}
    any_rule_closes_all = False

    for rule_name, (vol_fn, kind) in RULES.items():
        # raw weighted sums S_K = Σ_λ y_λ χ_λ Vol_λ per isotope
        S = {}
        for atom, (blocks, n, _B) in isotopes.items():
            S[atom] = sum(b["y"] * b["chi"] * vol_fn(b["part"], n) for b in blocks)

        # Global scale: for zero-param volume-unit rules, scale=1 (m_e is
        # the only scale). For dimensionless rules, fit ONE global scale
        # across ALL isotopes (least-squares on B/m_e) — labelled 1-param.
        if kind.startswith("zero-param"):
            scale = mp.mpf(1)
        else:
            num = sum(S[a] * (isotopes[a][2] / M_E_MEV) for a in isotopes)
            den = sum(S[a] ** 2 for a in isotopes)
            scale = num / den if den != 0 else mp.mpf(0)

        per = {}
        worst = mp.mpf(0)
        for atom, (blocks, n, B) in isotopes.items():
            B_pred = M_E_MEV * scale * S[atom]
            err = (B_pred - B) / B
            per[atom] = {"B_pred_MeV": str(B_pred), "B_AME_MeV": str(B),
                         "rel_err": float(err)}
            worst = max(worst, abs(err))
        closes_all = worst <= TOL
        any_rule_closes_all = any_rule_closes_all or closes_all
        results[rule_name] = {"kind": kind, "global_scale": str(scale),
                              "worst_rel_err": float(worst),
                              "closes_all_within_5pct": bool(closes_all),
                              "per_isotope": per}
        print(f"── {rule_name}  [{kind}]  scale={float(scale):.4g}")
        for atom in isotopes:
            p = per[atom]
            print(f"    {atom:<10} B_pred={float(mp.mpf(p['B_pred_MeV'])):8.4f}  "
                  f"AME={float(mp.mpf(p['B_AME_MeV'])):8.4f}  "
                  f"err={p['rel_err']*100:+8.2f}%")
        print(f"    worst |err| = {float(worst)*100:.2f}%  "
              f"→ closes all 4 within 5%: {closes_all}\n")

    w = WitnessBuilder("probe-volume-wedderburn-delta-lambda", engine="mpmath")
    w.set_description(
        "EXPLORATORY: parameter-free per-Wedderburn-block q-hyperbolic "
        "volume Vol_λ as a Δ_λ closure candidate. B = m_e·Σ_λ y_λ χ^λ Vol_λ "
        "tested on D/T/³He/⁴He with the SAME rule (no per-isotope refit). "
        "Clausen/Lobachevsky volume on content & hook angles; dimensionless "
        "comparators carry one global scale. Δ_λ remains open (GAP-A-3/A-4)."
    )
    w.add_parameter("tolerance_pct", 5.0)
    w.add_parameter("isotopes", list(isotopes.keys()))
    w.add_data("rules", results)
    w.add_data("any_rule_closes_all_within_5pct", any_rule_closes_all)
    # Assert the REFUTATION (expected negative): no parameter-free rule
    # here closes all four. A positive flips this and surfaces loudly.
    w.add_assertion(
        name="no_cheap_volume_rule_closes_all_four",
        computed=str(int(not any_rule_closes_all)),
        expected="1",
        tolerance=0,
        source=("EXPECTED NEGATIVE: cheap geometric Vol_λ proxies do not "
                "reproduce all four bindings; the principled q-6j saddle "
                "volume remains the candidate to compute next."),
    )
    out = w.save()
    print(f"Witness: {out}")
    print(f"\nany rule closes all 4 within 5%: {any_rule_closes_all}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
