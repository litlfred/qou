#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical multi-anchor cross-check
"""Substrate derivation probe v3 — λ_⋆ shape-dependent candidates.

v1 falsified universal [A−2]_q; v2 falsified four simple
multiplicative Z/N-dependent candidates.  v3 tests candidates
derived from the **shape of the dominant partition λ_⋆(Z, N)** as
extracted from the crystal Path A witness
`per-irrep-pole-atom-crystal.witness.json`.

The dominant partition for every atom is a hook
$\\lambda_\\star(Z, N) = (w, 1^{d-1})$ with

    w = Z + 2N + 1,    d = 2Z + N

(verified empirically across {p, D, T, ³He, ⁴He}).  The Z↔N
asymmetry is encoded as `w − d = N − Z + 1`.

Empirical `Δ_coupling / (E_0 · log(1/h))` coefficients to match
(numerical, from v1 probe):

  atom  (Z,N)    coefficient
  ³He   (2,1)    0.837
  T     (1,2)    0.969
  ⁴He   (2,2)    2.011  (= [2]_q)

This probe enumerates the natural q-deformed shape invariants of
λ_⋆ and checks which (if any) reproduces all three coefficients
simultaneously to ≤ 5 %.

Diagnostic only — does NOT fit Δ_coupling to AME.

`auditOnly`: docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md

Witness: `a-minus-2-q-substrate-probe-v3.witness.json`

@module folio-assistant/computations/probe_a_minus_2_q_substrate_v3
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from mpmath import mp, mpf  # noqa: E402

from codata_constants import M_E_MEV  # noqa: E402
from q_parameter import HA_MP, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 50


def _mpf_from_str(s: str) -> "mpf":
    return mpf(s)


def q_int(n, q):
    """[n]_q := (q^n − q^{−n}) / (q − q^{−1}). 0 if n = 0; negative for n < 0."""
    if n == 0:
        return mp.mpf(0)
    return (q ** n - q ** (-n)) / (q - 1 / q)


def q_factorial(n, q):
    if n < 0:
        raise ValueError(f"q_factorial(n) requires n ≥ 0, got {n}")
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= q_int(k, q)
    return out


def q_binomial(n, k, q):
    if k < 0 or k > n:
        return mp.mpf(0)
    return q_factorial(n, q) / (q_factorial(k, q) * q_factorial(n - k, q))


def q_dim_hook(w, d, q):
    """q-dimension of the hook partition (w, 1^{d-1}) of n = w + d − 1.

    Frame-Robinson-Thrall q-deformation:
        dim_q = [n]_q! / ∏_{cells} [hook_length]_q
    Hook lengths for hook(w, 1^{d-1}): {n} ∪ {1..w-1} ∪ {1..d-1}.
    """
    n = w + d - 1
    return (
        q_factorial(n, q)
        / (q_int(n, q) * q_factorial(w - 1, q) * q_factorial(d - 1, q))
    )


def main() -> int:
    # ── Load Δ_cat values ──────────────────────────────────────────
    msei = json.loads(
        (HERE / "magic-shell-empirical-instantiation.witness.json").read_text()
    )
    pad = msei["data"]["per_atom_delta_cat"]
    dc = {
        atom_key: _mpf_from_str(pad[atom_key]["delta_cat_MeV_50dps"])
        for atom_key in ("deuteron", "tritium", "he3", "he4")
    }

    # ── Load λ_⋆ shape from crystal Path A witness ─────────────────
    cpa = json.loads(
        (HERE / "per-irrep-pole-atom-crystal.witness.json").read_text()
    )
    lambda_star = {}
    for a in cpa["data"]["atoms"]:
        key = (a["Z"], a["N"])
        lam = tuple(a["min_total_lambda"])
        # Verify it's a hook (w, 1^{d-1})
        w = lam[0]
        d = len(lam)
        is_hook = all(l == 1 for l in lam[1:])
        # Verify the Z/N-encoded formula
        expected_w = a["Z"] + 2 * a["N"] + 1
        expected_d = 2 * a["Z"] + a["N"]
        formula_holds = (w == expected_w) and (d == expected_d) and is_hook
        lambda_star[key] = {
            "lambda": list(lam), "w": w, "d": d,
            "is_hook": is_hook, "formula_holds": formula_holds,
        }

    # ── Substrate parameters ───────────────────────────────────────
    q0 = Q_MP
    h_q = HA_MP
    log_inv_h = mp.log(1 / h_q)
    m_e = M_E_MEV
    E0 = m_e / (q0 * (q0 - 1))
    base = E0 * log_inv_h  # The empirical denominator

    builder = (
        WitnessBuilder("a-minus-2-q-substrate-probe-v3", engine="mpmath")
        .set_description(
            "v3 follow-up: tests λ_⋆ shape-derived q-invariants as "
            "candidate substrate forms for the Δ_coupling(Z, N) / "
            "(E_0 · log(1/h)) empirical coefficients (0.837 at ³He, "
            "0.969 at T, 2.011 at ⁴He).  Loads dominant partition "
            "shape from per-irrep-pole-atom-crystal.witness.json: "
            "λ_⋆(Z, N) = (Z + 2N + 1, 1^{2Z + N − 1}).  Z↔N "
            "asymmetry is encoded in (w, d) directly.  Diagnostic "
            "only — does NOT fit to AME."
        )
        .set_audit_only(
            "docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md"
        )
        .add_parameter("mp_dps", mp.dps)
        .add_parameter("q_0_50dps", mp.nstr(q0, 50))
        .add_parameter("E_0_MeV_50dps", mp.nstr(E0, 50))
        .add_parameter("log_inv_h_50dps", mp.nstr(log_inv_h, 50))
        .add_parameter("base_MeV_50dps", mp.nstr(base, 50))
    )

    # ── Anchor table ──────────────────────────────────────────────
    anchor_definitions = {
        (2, 1): ("³He", dc["he3"] - dc["deuteron"]),
        (1, 2): ("T",   dc["tritium"] - dc["deuteron"]),
        (2, 2): ("⁴He", dc["he4"] - 2 * dc["he3"]),
    }

    # ── Candidate q-invariants of λ_⋆ ──────────────────────────────
    def candidate_values(Z, N):
        info = lambda_star[(Z, N)]
        w, d = info["w"], info["d"]
        A = Z + N
        return {
            # Width / depth alone:
            "C1_w_q":     q_int(w, q0),
            "C2_d_q":     q_int(d, q0),
            "C3_w-1_q":   q_int(w - 1, q0),
            "C4_d-1_q":   q_int(d - 1, q0),
            # Linear shape combinations:
            "C5_w-d_q":   q_int(w - d, q0),
            "C6_w-d+1_q": q_int(w - d + 1, q0),
            "C7_w+d_q":   q_int(w + d, q0),
            # Ratios:
            "C8_w_over_d_q":    q_int(w, q0) / q_int(d, q0),
            "C9_d_over_w_q":    q_int(d, q0) / q_int(w, q0),
            "C10_w-1_over_d-1": (q_int(w - 1, q0) / q_int(d - 1, q0)
                                 if d > 1 else mp.mpf(0)),
            # Z/N direct (matches the audit-doc D-2 q-Catalan family):
            "C11_N+1_over_Z+1_q": (q_int(N + 1, q0) / q_int(Z + 1, q0)),
            "C12_Z_q_x_N_q_div_A_q": (
                q_int(Z, q0) * q_int(N, q0) / q_int(A, q0)
                if A > 0 else mp.mpf(0)
            ),
            # q-dim of λ_⋆:
            "C13_q_dim_hook":   q_dim_hook(info["w"], info["d"], q0),
            "C14_one_over_q_dim": (
                mp.mpf(1) / q_dim_hook(info["w"], info["d"], q0)
                if q_dim_hook(info["w"], info["d"], q0) != 0 else mp.mpf(0)
            ),
            # q-binomial structure:
            "C15_qbinom_n-1_w-1": q_binomial(w + d - 2, w - 1, q0),
            # Inverse q-Catalan (recover [A−2]_q at doubly-magic):
            "C16_A-2_q":     q_int(A - 2, q0),
        }

    candidate_names = list(candidate_values(2, 1).keys())

    # ── Build the results table ────────────────────────────────────
    results = []
    for (Z, N), (label, anchor) in anchor_definitions.items():
        info = lambda_star[(Z, N)]
        coeff_empirical = anchor / base
        cvs = candidate_values(Z, N)
        row = {
            "label": label, "Z": Z, "N": N, "A": Z + N,
            "lambda_star": info["lambda"],
            "w": info["w"], "d": info["d"], "w_minus_d": info["w"] - info["d"],
            "anchor_MeV_50dps": mp.nstr(anchor, 50),
            "anchor_MeV": float(anchor),
            "coefficient_empirical": float(coeff_empirical),
            "candidates": {
                name: {
                    "value_50dps": mp.nstr(v, 50),
                    "value": float(v),
                    "gap_pct": (
                        float(100 * (v - coeff_empirical) / coeff_empirical)
                    ),
                }
                for name, v in cvs.items()
            },
        }
        results.append(row)

    builder.add_data("results", results)
    builder.add_data(
        "lambda_star_formula_verified",
        all(lambda_star[k]["formula_holds"] for k in lambda_star),
    )

    # ── Print summary ──────────────────────────────────────────────
    print("=" * 100)
    print("  v3 — λ_⋆ shape-derived candidates  (target = empirical coefficient)")
    print(f"  base = E_0 · log(1/h) = {float(base):.6f} MeV")
    print("=" * 100)
    print()
    print(f"  {'atom':<5}{'(Z,N)':<8}{'λ_⋆':<22}{'w':>3}{'d':>3}"
          f"{'empirical coeff':<20}")
    print("  " + "-" * 60)
    for r in results:
        zn = f"({r['Z']},{r['N']})"
        print(f"  {r['label']:<5}{zn:<8}{str(r['lambda_star']):<22}"
              f"{r['w']:>3}{r['d']:>3}{r['coefficient_empirical']:<20.6f}")
    print()

    print("  Per-candidate gap %  (compact view, ≤ 5 % marked ✓):")
    print(f"  {'candidate':<26}" + "".join(f"{r['label']:<10}" for r in results))
    print("  " + "-" * 90)
    for name in candidate_names:
        line = f"  {name:<26}"
        all_within = True
        for r in results:
            g = r["candidates"][name]["gap_pct"]
            mark = "✓" if abs(g) <= 5.0 else " "
            line += f"{g:+8.2f}{mark} "
            if abs(g) > 5.0:
                all_within = False
        if all_within:
            line += " ← SURVIVOR"
        print(line)
    print()

    # ── Verdict ────────────────────────────────────────────────────
    survivors = []
    for name in candidate_names:
        all_within = all(
            abs(r["candidates"][name]["gap_pct"]) <= 5.0
            for r in results
        )
        if all_within:
            survivors.append(name)
    builder.add_data("survivors_within_5pct", survivors)
    print(f"  Survivors across all 3 anchors (≤ 5 %): "
          f"{survivors or 'NONE'}")

    builder.add_assertion(
        name="lambda_star_formula_w_eq_Z_plus_2N_plus_1",
        computed=int(all(
            lambda_star[k]["formula_holds"] for k in lambda_star
        )),
        expected=1,
    )

    out_path = builder.save()
    print(f"\n  Witness emitted: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
