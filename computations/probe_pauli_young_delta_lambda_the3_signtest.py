#!/usr/bin/env python3
"""EXPLORATORY — the decisive T/³He sign test for the Pauli-Young / Wigner-SU(4)
Δ_λ projection (the angle proposed in PR #2461).

CONTEXT. PR #2461 ("generalize Pauli-channel → weighted channels") proposes that
the open per-partition binding density Δ_λ in

    B(K) = m_e · Σ_{λ ⊢ 3A} y_λ(q₀) · χ^λ(β_K) · Δ_λ

is a **spin-isospin Young-symmetry (Pauli) projection** — i.e. Δ_λ is a
multiplicity / dimension coming from the Wigner SU(4) = SU(2)_S × SU(2)_I action
on each nucleon's 4-dim internal space (the corpus already carries this angle:
`particle-interactions/wigner-su4-from-spin-isospin.md`,
`mass-theory/schur-weyl-mass-decomposition.ts`). PR #2461 calls it "NOVEL" and
"untested".

It is **neither novel nor untested** in its decisive instance. The
`2026-06-02-volume-wedderburn-delta-lambda-probe.md` audit already surfaced the
sharp necessary condition: T (³H) and ³He share n = 9 (same 30 partitions, same
y_λ), so the *entire* binding split is

    (B_T − B_³He)/m_e = Σ_λ Δ_λ · v_λ ,     v_λ := y_λ · (χ^λ(β_T) − χ^λ(β_³He)),

a single number = +1.4947. This script makes the refutation a THEOREM, not a
scan:

  1. A Pauli / spin-isospin Young-symmetry projection Δ_λ = ⟨χ^λ, χ_{spin⊗iso}⟩
     is a multiplicity ⇒ **Δ_λ ≥ 0** for every λ. So the achievable set is the
     non-negative cone. We compute the sign census of v_λ. If v_λ ≤ 0 for every
     λ, then Σ_λ Δ_λ v_λ ≤ 0 < +1.4947 for EVERY non-negative Δ_λ — the whole
     family (Pauli-Young included) cannot even reach the right sign.

  2. We also evaluate the concrete Wigner-SU(4) weight Δ_λ = dim GL(4)-irrep(λ)
     (= #SSYT(λ, 4 letters), the Schur-Weyl multiplicity of the strand space
     (ℂ⁴)^⊗9) and report Σ_λ Δ_λ v_λ vs the target.

  3. Structural reason (corpus, 2026-05-24-isospin-categorical-source.md): the
     T/³He split IS isospin BREAKING (the 305 ppm h = q−q⁻¹ bar-anti-symmetric
     anomaly). A Wigner-SU(4)/isospin-SYMMETRIC projection produces zero
     breaking by construction — T and ³He are partners in one supermultiplet,
     so the symmetric prediction for the differential is exactly 0.

EXPECTED NEGATIVE (CI-safe per production-vs-exploratory-discipline). Touches no
production. Δ_λ remains open (GAP-A-3/A-4); this CLOSES the Pauli-Young branch.
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401,E402 — puts substrate/ (witness_base) on path
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
HERE = Path(__file__).parent

M_E_MEV = mp.mpf("0.51099895069")
AME_B = {"tritium": AME_B_TRITIUM_MEV_VALIDATION, "helium-3": mp.mpf("7.7180")}
CHI = {
    "tritium": "chi-tritium-h9-at-q0-50dps.witness.json",
    "helium-3": "chi-helium-3-h9-at-q0-50dps.witness.json",
}


def load(fname: str):
    with open(HERE / fname, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    rows = {tuple(r["partition"]): {"y": mp.mpf(r["y_lambda"]),
                                    "chi": mp.mpf(r["chi_lambda"])}
            for r in d["by_partition"]}
    return rows, d["n_strands"]


def conjugate(part):
    if not part:
        return []
    m = part[0]
    return [sum(1 for p in part if p > j) for j in range(m)]


def dim_gl(part, N: int) -> int:
    """dim of the GL(N) irreducible with highest weight `part`
    = #SSYT(part, alphabet of N) via the hook-content formula
        Π_cells (N + content) / hook,   content = col − row (0-indexed).
    Zero automatically when part has more than N rows."""
    conj = conjugate(part)
    num = Fraction(1)
    den = Fraction(1)
    for i, row in enumerate(part):
        for j in range(row):
            content = j - i
            arm = row - j - 1
            leg = conj[j] - i - 1
            hook = arm + leg + 1
            num *= (N + content)
            den *= hook
    val = num / den
    assert val.denominator == 1, (part, val)
    return int(val)


def main() -> int:
    T, nT = load(CHI["tritium"])
    H, nH = load(CHI["helium-3"])
    assert nT == nH == 9, (nT, nH)
    parts = sorted(T, reverse=True)
    assert set(parts) == set(H), "partition sets must match for the same-n test"

    target = (AME_B["tritium"] - AME_B["helium-3"]) / M_E_MEV  # +1.4947

    # y_λ must agree between T and ³He (same n ⇒ same Plancherel weights)
    max_y_drift = max(abs(T[p]["y"] - H[p]["y"]) for p in parts)

    rows = []
    npos = nneg = nzero = 0
    vmax = mp.mpf("-1e99")
    vmin = mp.mpf("1e99")
    sum_v = mp.mpf(0)              # uniform Δ_λ = 1
    sum_su4 = mp.mpf(0)           # Wigner-SU(4): Δ_λ = dim GL(4)(λ)
    sum_su4_pos = mp.mpf(0)       # the part a non-negative weight could keep
    for p in parts:
        y = T[p]["y"]
        dchi = T[p]["chi"] - H[p]["chi"]
        v = y * dchi
        su4 = dim_gl(list(p), 4)
        if v > 0:
            npos += 1
        elif v < 0:
            nneg += 1
        else:
            nzero += 1
        vmax = max(vmax, v)
        vmin = min(vmin, v)
        sum_v += v
        sum_su4 += su4 * v
        if v > 0:
            sum_su4_pos += su4 * v
        rows.append({"partition": list(p), "nrows": len(p),
                     "y_lambda": mp.nstr(y, 8),
                     "delta_chi": mp.nstr(dchi, 8),
                     "v_lambda": mp.nstr(v, 8),
                     "dim_gl4": su4})

    # The decisive family-level fact: a non-negative Δ_λ can produce a positive
    # differential ONLY if some v_λ > 0. If every v_λ ≤ 0 the whole cone fails.
    family_can_reach_sign = npos > 0
    sup_over_nonneg = "+inf" if family_can_reach_sign else mp.nstr(max(vmax, mp.mpf(0)), 6)

    print(f"target (B_T−B_³He)/m_e = {mp.nstr(target, 8)}")
    print(f"max |y_λ drift| T vs ³He = {mp.nstr(max_y_drift, 4)}  (should be ~0)")
    print(f"\nv_λ = y_λ·(χ^λ_T − χ^λ_³He) sign census over {len(parts)} partitions:")
    print(f"    positive: {npos}    negative: {nneg}    zero: {nzero}")
    print(f"    v_max = {mp.nstr(vmax, 6)}   v_min = {mp.nstr(vmin, 6)}")
    print(f"\nDifferential under candidate Δ_λ weights (target {mp.nstr(target, 6)}):")
    print(f"    uniform   Δ_λ=1          : Σ v_λ          = {mp.nstr(sum_v, 6)}")
    print(f"    Wigner-SU(4) Δ_λ=dimGL4  : Σ dimGL4·v_λ   = {mp.nstr(sum_su4, 6)}")
    print(f"\nFamily verdict: a NON-NEGATIVE Δ_λ can reach the + sign of the "
          f"target?  {family_can_reach_sign}")
    if not family_can_reach_sign:
        print("  ⇒ v_λ ≤ 0 ∀λ: EVERY non-negative Δ_λ gives Σ≤0 < +1.4947.")
        print("    The whole Pauli/SU(4) Young-symmetry family is REFUTED — it")
        print("    cannot even produce the SIGN of the T/³He split.")
    else:
        print(f"  ⇒ {npos} partition(s) carry v_λ>0; sup over the non-negative")
        print("    cone is unbounded, so SOME non-negative weight fits — but an")
        print("    unconstrained free fit, not a derivation. The concrete")
        print(f"    Wigner-SU(4) weight gives {mp.nstr(sum_su4, 6)} vs {mp.nstr(target, 6)}.")

    # show the strongest-signed blocks
    rows_by_absv = sorted(rows, key=lambda r: -abs(float(r["v_lambda"])))
    print("\n  largest |v_λ| blocks (partition, nrows, v_λ, dimGL4):")
    for r in rows_by_absv[:8]:
        print(f"    {str(r['partition']):<22} rows={r['nrows']} "
              f"v={r['v_lambda']:>12}  dimGL4={r['dim_gl4']}")

    w = WitnessBuilder("probe-pauli-young-delta-lambda-the3-signtest",
                       engine="mpmath")
    w.set_description(
        "EXPLORATORY: decisive T/³He same-n sign test for the Pauli-Young / "
        "Wigner-SU(4) Δ_λ projection proposed in PR #2461. A spin-isospin "
        "Young-symmetry multiplicity is Δ_λ≥0; the T/³He differential "
        "(B_T−B_³He)/m_e=+1.4947 is the entire same-n binding split. Reports "
        "the v_λ=y_λ·Δχ_λ sign census (whether any non-negative Δ_λ can reach "
        "the +sign) and the concrete Δ_λ=dim GL(4)-irrep(λ) evaluation. "
        "Δ_λ remains open (GAP-A-3/A-4)."
    )
    w.add_parameter("n_strands", 9)
    w.add_parameter("n_partitions", len(parts))
    w.add_data("target_diff", mp.nstr(target, 16))
    w.add_data("max_y_drift", mp.nstr(max_y_drift, 6))
    w.add_data("sign_census", {"positive": npos, "negative": nneg, "zero": nzero})
    w.add_data("v_max", mp.nstr(vmax, 16))
    w.add_data("v_min", mp.nstr(vmin, 16))
    w.add_data("diff_uniform", mp.nstr(sum_v, 16))
    w.add_data("diff_wigner_su4_dimGL4", mp.nstr(sum_su4, 16))
    w.add_data("nonneg_family_can_reach_target_sign", bool(family_can_reach_sign))
    w.add_data("sup_over_nonnegative_cone", str(sup_over_nonneg))
    w.add_data("by_partition", rows)
    # Expected-negative assertion: the concrete Wigner-SU(4) weight misses the
    # target (sign and/or magnitude). CI-safe.
    su4_hits = abs(sum_su4 - target) <= mp.mpf("0.05") * abs(target)
    w.add_assertion(
        name="wigner_su4_delta_lambda_misses_the3_differential",
        computed=str(int(not su4_hits)),
        expected="1",
        tolerance=0,
        source=(f"EXPECTED NEGATIVE: Wigner-SU(4) Δ_λ=dimGL4 gives "
                f"{mp.nstr(sum_su4, 6)} for (B_T−B_³He)/m_e vs target "
                f"{mp.nstr(target, 6)}; "
                + ("v_λ≤0 ∀λ so NO non-negative Δ_λ reaches the +sign — the "
                   "Pauli/SU(4) Young-symmetry family is refuted at the sign "
                   "level (isospin-symmetric projection cannot supply the "
                   "isospin-breaking T/³He split)."
                   if not family_can_reach_sign else
                   "non-negative cone is unbounded so a free fit exists, but "
                   "the principled Wigner-SU(4) weight is not it.")),
    )
    out = w.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
