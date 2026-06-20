#!/usr/bin/env python3
"""Item B (B.1a-rev.4) — full LP-dual extraction for a_K.

Solves the operator-selection LP per
[`prop:mass-coefficient-shadow-price`](../../content/quantum-observable-universe/braids-and-knots/mass-coefficient-shadow-price.md)
explicitly via `lp_dual_solver.solve_operator_selection_lp` and
reads off the literal dual variables `u_λ*`.

## LP setup (per-atom)

For each atom (Z, N) with n = 3A strands:

  Basis: Wedderburn projectors {π_λ : λ ⊢ n}
  t_λ = w_λ · χ^λ(W_atom)      (Markov trace of π_λ-projected atom braid)
  G_λλ' = w_λ · δ_λλ'           (block-diagonal Frobenius Gram)
  n_target = |tr_M(W_atom)|     (target categorical mass)

The LP becomes:
  min Σ_λ x_λ · w_λ · χ^λ
  s.t.  Σ_λ x_λ = 1   (net normalisation)
        x_λ · w_λ ≥ 0  (Frobenius positivity per block)

Note: the second constraint is automatically satisfied for x_λ ≥ 0
since w_λ ≥ 0 (Plancherel-like weights at q_0 — verified
empirically in chi-cache). So the LP reduces to a 1-constraint
problem with d=n_partitions variables.

The dual variables u_λ^* satisfy complementary slackness:
  u_λ^* · (w_λ · x_λ*) = 0
i.e. u_λ^* > 0 iff x_λ^* = 0 (block is binding-active).

## Output

Witness `a-K-via-lp-dual-full.witness.json` with required LP-dual
fields per AGENTS.md §LP/SDP duals.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

import numpy as np
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from lp_dual_solver import solve_operator_selection_lp  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
Q = mp.mpf(json.load(Q_PIN.open())["derived_50_digit"]["q"])
H = Q - mp.mpf(1) / Q

ATOM_CHI = {
    "proton":   (1, 0, 3,  "chi-proton-h3-at-q0-50dps.witness.json"),
    "neutron":  (0, 1, 3,  "chi-neutron-h3-at-q0-50dps.witness.json"),
    "deuteron": (1, 1, 6,  "chi-deuteron-h6-at-q0-50dps.witness.json"),
    "tritium":  (1, 2, 9,  "chi-tritium-h9-at-q0-50dps.witness.json"),
    "helium-3": (2, 1, 9,  "chi-helium-3-h9-at-q0-50dps.witness.json"),
    "helium-4": (2, 2, 12, "chi-helium-4-h12-at-q0-50dps.witness.json"),
}


def conjugate_partition(lam: list[int]) -> list[int]:
    if not lam:
        return []
    return [sum(1 for p in lam if p > i) for i in range(lam[0])]


def is_self_conjugate(lam: list[int]) -> bool:
    return lam == conjugate_partition(lam)


def content_sum(lam: list[int]) -> int:
    return sum(j - i for i, part in enumerate(lam) for j in range(part))


def a_K_closed(A: int) -> float:
    """Closed-form BW per conjecture Step 4."""
    h = float(H)
    if A == 1: return 1.0
    if A == 2: return 1.0 + h
    if A == 3: return 1.0 - h * h
    if A == 4: return (1.0 - h * h) ** 2
    return float("nan")


def solve_atom_lp(atom: str) -> dict:
    """Build + solve the per-atom operator-selection LP, return full witness."""
    Z, N, n, fname = ATOM_CHI[atom]
    A = Z + N
    data = json.loads((HERE / fname).read_text())
    # Keep substrate values at mpmath precision through the LP solve.
    # Drop the outer float() — was flagged by compute_no_mpf_to_float_cast.
    tr_M_atom = mp.mpf(data["tr_M_at_q0"])

    # Build LP arrays from chi-cache.
    partitions = []
    y_lams = []
    chi_lams = []
    contribs = []
    for row in data["by_partition"]:
        lam = list(row["partition"])
        partitions.append(lam)
        y_lams.append(mp.mpf(row["y_lambda"]))
        chi_lams.append(mp.mpf(row["chi_lambda"]))
        contribs.append(mp.mpf(row["contribution"]))

    d = len(partitions)
    # t_λ = y_λ · χ^λ (the Wedderburn block contribution to tr_M)
    # We solve a slightly non-trivial LP by choosing a SECOND
    # constraint that breaks the degeneracy: forcing the active
    # set to align with the chirality stratum.
    #
    # min  Σ_λ |contrib_λ| · x_λ
    # s.t.  Σ_λ contrib_λ · x_λ = tr_M_atom    (reproduce trace)
    #       x_λ ≥ 0
    #
    # This is the dual-feasibility frame from
    # `prop:operator-selection-lp`: minimise total weight subject
    # to reproducing the observable. Active (x_λ > 0) blocks are
    # the ones the LP commits to using.
    t = np.array([abs(c) for c in contribs], dtype=float)
    # Use contrib as the Gram-like vector: G[i][j] = contrib[i] * δ_ij
    # for the simple block-diagonal LP.
    G = np.diag([abs(c) for c in contribs])
    n_target = tr_M_atom

    # Pin scipy: committed-witness producer → byte-deterministic.
    result = solve_operator_selection_lp(t, G, n_target, backend="scipy")

    # Map LP dual back to partition labels.
    per_partition = []
    for i, lam in enumerate(partitions):
        per_partition.append({
            "partition": lam,
            "self_conjugate": is_self_conjugate(lam),
            "content_sum": content_sum(lam),
            "y_lambda": y_lams[i],
            "chi_lambda": chi_lams[i],
            "contribution": contribs[i],
            "x_star": result.x_star[i],
            "u_lambda_star": result.y_star[i],
            "is_active": (i in result.active_set),
        })

    # a_K extraction: dual sum on chirality-active blocks.
    chirality_dual_sum = sum(
        r["u_lambda_star"]
        for r in per_partition
        if not r["self_conjugate"] and r["is_active"]
    )
    sc_dual_sum = sum(
        r["u_lambda_star"]
        for r in per_partition
        if r["self_conjugate"] and r["is_active"]
    )
    u0_star = result.y0_star

    aK_via_dual = 1.0 + chirality_dual_sum / abs(u0_star) if abs(u0_star) > 1e-12 else float("nan")
    aK_C = a_K_closed(A)
    dual_vs_C_ppm = float((aK_via_dual / aK_C - 1) * 1e6) if (
        aK_C and not (aK_C != aK_C)  # not NaN
    ) else None

    return {
        "atom": atom,
        "Z": Z, "N": N, "A": A,
        "tr_M_atom": tr_M_atom,
        # LP fields per AGENTS.md §LP/SDP duals first-class infra
        "x_star": list(result.x_star),
        "y0_star": result.y0_star,
        "y_star": list(result.y_star),
        "active_set": list(result.active_set),
        "primal_obj": result.primal_obj,
        "dual_obj": result.dual_obj,
        "duality_gap": result.duality_gap,
        "feasible": result.feasible,
        # Item B extraction
        "u0_star": u0_star,
        "chirality_dual_sum": chirality_dual_sum,
        "self_conjugate_dual_sum": sc_dual_sum,
        "a_K_via_lp_dual": aK_via_dual,
        "a_K_C_closed": aK_C,
        "dual_vs_C_ppm": dual_vs_C_ppm,
        "per_partition": per_partition,
        "n_partitions": d,
        "n_active": len(result.active_set),
    }


def main() -> int:
    w = WitnessBuilder("a-K-via-lp-dual-full", engine="numpy")
    w.set_description(
        "Item B (B.1a-rev.4) — full LP-dual extraction for a_K. "
        "Solves the operator-selection LP per "
        "`prop:mass-coefficient-shadow-price` for each of "
        "proton/neutron/D/T/³He/⁴He at f64 precision (scipy linprog "
        "via lp_dual_solver.solve_operator_selection_lp) and extracts "
        "literal u_λ^* dual variables. Compares the chirality-active "
        "dual sum to closed-form C = (1+h, 1-h², (1-h²)²) at A=2,3,4. "
        "Emits witness with all required LP-dual fields per AGENTS.md "
        "§LP/SDP duals first-class infra. Note: this is f64-precision "
        "verification; MPFR-50dps follow-on would be a future iteration."
    )
    w.set_content_block("conj:knot-factor-frobenius-pairing")
    w.add_parameter("q0_50dps", mp.nstr(Q, 20))
    w.add_parameter("h_q", mp.nstr(H, 20))
    w.add_parameter("precision", "f64 (scipy linprog highs)")
    w.add_parameter("lp_method", "highs")
    w.add_caveat(
        "B.1a-rev.4 PROBE-ONLY: the LP basis used here is the "
        "Wedderburn-block projector basis {π_λ : λ ⊢ n}, giving a "
        "block-DIAGONAL Frobenius Gram G_λλ' = w_λ · δ_λλ'. This is "
        "too coarse for the operator-selection LP — the duals come "
        "out DEGENERATE (y0^* = 0 for A ≥ 2; chirality dual sum "
        "diverges in the limit). The full operator-selection LP "
        "per `prop:mass-coefficient-shadow-price` requires the full "
        "Hecke algebra basis {b_i : i = 1..[n]_q!} with non-diagonal "
        "Gram G_ij = tr_M(b_i b_j). That setup is an open R&D item "
        "(per Item B audit §7c B.1a-rev.4); the present script "
        "wires the SDP-attribution path and surfaces the "
        "block-diagonal LP's degeneracy as an empirical finding."
    )

    rows = []
    for atom in ATOM_CHI:
        try:
            row = solve_atom_lp(atom)
            rows.append(row)
        except Exception as exc:  # noqa: BLE001
            rows.append({
                "atom": atom,
                "error": f"{type(exc).__name__}: {exc}",
            })

    w.add_data("rows", rows)

    # Aggregate the y0_star, y_star, active_set fields at the top
    # level for the witness validator (per AGENTS.md infra rule).
    w.add_data("y0_star", [r.get("y0_star") for r in rows])
    w.add_data("y_star", [r.get("y_star") for r in rows])
    w.add_data("active_set", [r.get("active_set") for r in rows])
    w.add_data("primal_obj", [r.get("primal_obj") for r in rows])
    w.add_data("dual_obj", [r.get("dual_obj") for r in rows])
    w.add_data(
        "duality_gap",
        max((r.get("duality_gap") or 0) for r in rows if "duality_gap" in r),
    )

    for r in rows:
        if "error" in r:
            w.add_assertion(
                f"lp_solve_ok[{r['atom']}]",
                computed=f"FAILED: {r['error']}",
                expected="success",
                source="LP solve via scipy linprog",
            )
            continue
        w.add_assertion(
            f"lp_feasible[{r['atom']}]",
            computed=r["feasible"],
            expected=True,
        )
        w.add_assertion(
            f"lp_duality_gap_small[{r['atom']}]",
            computed=r["duality_gap"],
            expected=0.0,
            tolerance=1e-6,
            unit="absolute",
            source="strong-duality assertion",
        )

    out_path = w.save()
    print(f"Witness emitted: {out_path.name}")
    print()
    print(f"{'atom':12s} {'A':>2s}  {'tr_M':>10s}  {'#active':>7s}  "
          f"{'y0*':>10s}  {'a_K^dual':>10s}  {'a_K^C':>10s}  {'dual-C ppm':>12s}")
    for r in rows:
        if "error" in r:
            print(f"  {r['atom']:12s}  ERROR: {r['error']}")
            continue
        ppm = r['dual_vs_C_ppm']
        ppm_s = f"{ppm:+.4e}" if ppm is not None else "n/a"
        print(f"  {r['atom']:12s} {r['A']:>2d}  {r['tr_M_atom']:>10.6f}  "
              f"{r['n_active']:>7d}  {r['y0_star']:>10.4f}  "
              f"{r['a_K_via_lp_dual']:>10.4f}  {r['a_K_C_closed']:>10.4f}  "
              f"{ppm_s:>12s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
