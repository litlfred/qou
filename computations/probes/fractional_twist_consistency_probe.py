#!/usr/bin/env python3
"""fractional_twist_consistency_probe.py — is the non-abelian step σ^{2ℓ} consistent? And the 63.92° cross-check.
Bean `qou-jfx8` (owner 2026-10-12: "Test the non-abelian step: compute σ^{2ℓ} on all blocks at H₃/H₆ … check that it is
consistent"; "relate the 63.92° turning angle to existing corpus angles (Reeb angles) as a cross-check, not a fit").
Companion to `QOU/MassTheory/BringResidueEnergy.lean`.

σ_i^t := q^t P_+ + q^{−t} e^{iπt} P_−  on every irreducible block (seminormal matrices from
composition_feasibility_a2_probe, validated against committed characters), P_± the eigenprojectors of σ_i.
Checks, at t ∈ {1, 2ℓ = −1/3, 1/3, 1/2}:
  (a) group law  σ^s σ^t = σ^{s+t}  and  (σ^{2ℓ})^6 = σ^{−2}  (six fibre pairs = one negative full twist);
  (b) far commutativity  σ₁^t σ₃^t = σ₃^t σ₁^t  (H₆ blocks);
  (c) the braid relation  σ₁^t σ₂^t σ₁^t = σ₂^t σ₁^t σ₂^t  on every H₃ block;
  (d) trace-level Markov property of the fractional bridge letter on the deuteron composite in H₆:
      tr(W σ₂^t)/tr(W) = q^t w_S + q^{−t} e^{iπt} w_A (complex), and its real part = μ(t);
  (e) cross-check: turning angle 180°·(t* − 2ℓ) and its block-level analogues against the corpus Reeb angles
      θ_λ = arccos(χ_λ(C₅)/dim λ) and the C₅ fixed-point rotations ±72°, ±144°. Reported, never fitted.
mpmath 60 dps (complex); no floats.
-- Ref: [manuscript] bean qou-jfx8; BringFiberActionInstance.lean (reebCos)
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
mp.mp.dps = 60
import composition_feasibility_a2_probe as cf  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 60
Q = cf.Q
QI = 1 / Q
ELL = mp.mpf(-1) / 6


def mat(M):
    return mp.matrix(M)


def frac(S, t):
    n = S.rows
    I = mp.eye(n)
    Pp = (S + QI * I) / (Q + QI)
    Pm = (Q * I - S) / (Q + QI)
    return Q ** t * Pp + Q ** (-t) * mp.expjpi(t) * Pm


def norm(M):
    return max(abs(M[i, j]) for i in range(M.rows) for j in range(M.cols))


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    TOL = mp.mpf("1e-40")
    ts = {"1": mp.mpf(1), "2l=-1/3": 2 * ELL, "1/3": mp.mpf(1) / 3, "1/2": mp.mpf(1) / 2}
    rows = {}
    # (a), (c) on H3 blocks
    for shape in [(3,), (2, 1), (1, 1, 1)]:
        mats, dim = cf.sigmas(shape)
        S1, S2 = mat(mats[0]), mat(mats[1])
        for name, t in ts.items():
            br = norm(frac(S1, t) * frac(S2, t) * frac(S1, t) - frac(S2, t) * frac(S1, t) * frac(S2, t))
            rows[f"H3 {shape} braid t={name}"] = mp.nstr(br, 6)
        g = norm(frac(S1, 2 * ELL) ** 6 - frac(S1, -2))
        gl = norm(frac(S1, mp.mpf("0.3")) * frac(S1, mp.mpf("0.45")) - frac(S1, mp.mpf("0.75")))
        rows[f"H3 {shape} group law"] = mp.nstr(max(g, gl), 6)
    for k, v in rows.items():
        print(f"  {k}: {v}")
    check("group_law_and_six_pairs_eq_negative_full_twist_all_H3_blocks",
          all(mp.mpf(v) < TOL for k, v in rows.items() if "group law" in k), "spectral calculus of one generator")
    check("braid_relation_holds_at_t_1", all(mp.mpf(v) < TOL for k, v in rows.items() if k.endswith("t=1") and "braid" in k),
          "validation: the Hecke braid relation")
    brk = {k: v for k, v in rows.items() if "braid" in k and "(2, 1)" in k and not k.endswith("t=1")}
    braid_fails_fractional = all(mp.mpf(v) > mp.mpf("1e-6") for v in brk.values())
    check("braid_relation_FAILS_for_fractional_t_on_the_2dim_block", braid_fails_fractional,
          "σ_i^t do not generate a braid-group action: the non-abelian continuation is a one-generator object")
    # (b) far commutativity on H6 blocks, (d) Markov property of the fractional bridge
    P6 = cf.partitions_of(6)
    y6 = cf.load_y(6)
    pos = [l for l in P6 if y6[l] > 0]
    far = mp.mpf(0)
    for shape in pos:
        mats, dim = cf.sigmas(shape)
        far = max(far, norm(frac(mat(mats[0]), 2 * ELL) * frac(mat(mats[2]), 2 * ELL)
                            - frac(mat(mats[2]), 2 * ELL) * frac(mat(mats[0]), 2 * ELL)))
    check("far_commutativity_of_fractional_twists_H6", far < TOL, "polynomials in commuting generators")
    W = cf.nucleon_word(cf.B_P, 0, 1) + cf.nucleon_word(cf.B_N, 3, 4)
    y2 = {tuple(e["partition"]): mp.mpf(e["y_at_q0_50dps"]) for e in cf.Yw["data"]["by_n"]["2"]}
    wS, wA = y2[(2,)], y2[(1, 1)]
    num = mp.mpc(0)
    den = mp.mpf(0)
    blockvals = {}
    for shape in pos:
        mats, dim = cf.sigmas(shape)
        M = mp.eye(dim)
        for c, d, g in W:
            M = M * (c * mat(mats[g]) + d * mp.eye(dim))
        tW = sum(M[i, i] for i in range(dim))
        tWs = M * frac(mat(mats[2]), 2 * ELL)
        val = sum(tWs[i, i] for i in range(dim))
        blockvals[str(shape)] = val
        num += y6[shape] * val
        den += y6[shape] * tW
    pred = Q ** (2 * ELL) * wS + Q ** (-2 * ELL) * mp.expjpi(2 * ELL) * wA
    dev = abs(num / den - pred)
    print("  trace-level fractional bridge Markov value:", mp.nstr(num / den, 15), " predicted:", mp.nstr(pred, 15))
    check("fractional_bridge_markov_property_trace_level", dev < TOL, "Part A with σ^t ∈ span{1, σ}")
    check("real_part_equals_mu", abs(mp.re(num / den) - (Q ** (2 * ELL) * wS + Q ** (-2 * ELL) * mp.cos(2 * mp.pi * ELL) * wA)) < TOL,
          "BringResidueEnergy.mu")
    print("  block-level χ_λ(W σ₂^{2ℓ}) (complex):", {k: mp.nstr(v, 8) for k, v in blockvals.items()})

    # (e) cross-check of angles (no fit)
    phi = (1 + mp.sqrt(5)) / 2
    reeb = {"A": 0, "T1": mp.degrees(mp.acos(phi / 3)), "T2": mp.degrees(mp.acos((1 - mp.sqrt(5)) / 6)),
            "G": mp.degrees(mp.acos(mp.mpf(-1) / 4)), "H": mp.mpf(90), "C5 rot 1": mp.mpf(72), "C5 rot 2": mp.mpf(144)}
    turning = mp.mpf("63.9229894574")
    residue_part = 180 * (-2 * ELL)
    print(f"  turning angle 63.923° = residue part {mp.nstr(residue_part, 6)}° + t* part {mp.nstr(turning - residue_part, 6)}°")
    diffs = {k: mp.nstr(turning - v, 6) for k, v in reeb.items()}
    print("  corpus angles:", {k: mp.nstr(v, 8) for k, v in reeb.items()})
    print("  differences (turning − corpus):", diffs)
    nearest = min(reeb, key=lambda k: abs(turning - reeb[k]))
    check("no_corpus_angle_within_1_degree_(cross_check_recorded_not_fitted)",
          all(abs(turning - v) > 1 for v in reeb.values()), f"nearest {nearest}")

    ok_all = all(ok for _, ok, _ in checks)
    w = WitnessBuilder("fractional-twist-consistency", engine="mpmath")
    for name, ok, src in checks:
        w.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = w.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "q0 read from the committed y-lambda-at-q0 witness string via composition_feasibility_a2_probe",
        "description": ("PROBE (bean qou-jfx8): consistency of the fractional twist σ^{2ℓ}. Group law and six-pairs = σ^{−2} "
                        "hold; far commutativity holds; trace-level fractional Markov property holds; the braid relation "
                        "FAILS for fractional t on the 2-dim H3 block. Turning angle 63.92° compared with corpus Reeb angles: "
                        "no match within 1°. Nothing fitted."),
        "weight_family": "markov_y_lambda_convention_D",
        "matrix_checks": rows,
        "far_commutativity_dev": mp.nstr(far, 6),
        "fractional_bridge_markov": {"measured": mp.nstr(num / den, 30), "predicted": mp.nstr(pred, 30)},
        "block_values_complex": {k: mp.nstr(v, 30) for k, v in blockvals.items()},
        "corpus_angles_deg": {k: mp.nstr(v, 20) for k, v in reeb.items()},
        "turning_minus_corpus_deg": diffs,
        "turning_angle_split": {"residue_part_deg": mp.nstr(residue_part, 20), "t_star_part_deg": mp.nstr(turning - residue_part, 20)},
    })
    print("witness:", out)
    print(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
