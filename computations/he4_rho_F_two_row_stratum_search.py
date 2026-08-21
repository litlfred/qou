"""ρ_F derivation attempt (qou-2row) — ρ_F is not a categorical constant; "2" is the rounded ⁴He value.

Follows item 2 (`he4_rho_F_cpt_mechanism_refuted.py`): the CPT alt-block-doubling mechanism for
ρ_F(⁴He)=2 is refuted under the canonical convention (alt block empty; exact two-row dominance). This
probe is the genuine derivation ATTEMPT — and reaches an honest structural wall.

## Attempt 1 — a fit-free two-row-stratum ratio (canonical ⁴He H₁₂ weights)

Candidates from the nonzero two-row Frobenius weights (y_λ, χ_λ at q₀; tr_M = Σ y_λ χ_λ = 0.16097):

  Σ y_λ / y_[12]              = 3.354
  Σ_{2-row} y_λ / y_[12]      = 2.354
  (y_[12]+y_[11,1]) / y_[12]  = 1.782   (closest, but −5.7% AND cherry-picks 2 of 7 blocks = a fit)
  Σ (y·χ) / (y·χ)_[12]        = 16.774
  tr_M / y_[12]               = 40.591

Target ρ_F(⁴He) = B_AME/(m_e·A·8G) = 1.889. **No principled ratio reproduces it.**

## Attempt 2 — is ρ_F even a constant? (the decisive check)

ρ_F = B_AME/(m_e·A·8G) across the doubly-magic LIGHT nuclei (the formula's stated domain):

  nucleus  (Z,N)     ρ_F(obs)   ρ_F(strong, Coulomb added back)
  ⁴He      (2,2)     1.889      1.948
  ¹⁶O      (8,8)     2.130      2.390
  ⁴⁰Ca     (20,20)   2.284      2.803

**ρ_F is NOT a constant.** It drifts monotonically upward with A (1.89 → 2.13 → 2.28 observed), and
adding back the Coulomb energy makes the drift WORSE, not better (1.95 → 2.39 → 2.80 — spreading
further from 2, because Coulomb grows ~Z² faster than the binding). So the integer "2" is the
ROUNDED ⁴He value, not a universal categorical prefactor: `B = ρ_F·m_e·A·8G` with a fixed ρ_F=2 is a
light-nucleus approximation that degrades as A grows.

## Verdict — the derivation target is ill-posed, and that is why it does not close

`ρ_F` is a per-nucleus, A-dependent effective prefactor. There is no single categorical constant to
derive: the CPT alt-block route is refuted (empty block), a two-row-stratum ratio gives no match, and
the value itself is not 2 away from ⁴He. A genuine derivation would have to reproduce the
A-DEPENDENCE `ρ_F(A)` (1.89 → 2.28), not "which integer" — a strictly harder target that no
categorical quantity in the corpus supplies. Honest wall: ρ_F stays an empirical, A-dependent
magic-shell prefactor; ρ_F(⁴He)=2 is a ⁴He-specific rounding, not a derived universal.

Scope-(a): three structural routes tested and shown insufficient; no proved exclusion of every
possible construction. No fit; no wiring; q₀ proton-anchored. Beaned qou-2row / qou-58r5.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
import q_parameter as qp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

HE4 = HERE / "chi-helium-4-h12-at-q0-50dps.witness.json"
VOL_L6A4 = "7.327724753417752"
# doubly-magic light nuclei (name, Z, N, A, B_AME MeV)
DOUBLY_MAGIC = [("4He", 2, 2, 4, "28.295674"),
                ("16O", 8, 8, 16, "127.619336"),
                ("40Ca", 20, 20, 40, "342.052000")]


def main() -> int:
    set_compute_dps(50)
    me = mp.mpf(str(qp.M_E_MEV))
    G8 = mp.mpf(VOL_L6A4)

    # Attempt 1 — two-row ratios
    w = json.load(open(HE4))
    nz = [e for e in w["by_partition"] if mp.mpf(str(e["y_lambda"])) != 0]
    nz.sort(key=lambda e: -mp.mpf(str(e["y_lambda"])))
    y = [mp.mpf(str(e["y_lambda"])) for e in nz]
    c = [mp.mpf(str(e["contribution"])) for e in nz]
    trM = mp.mpf(str(w["tr_M_at_q0"]))
    y0, c0 = y[0], c[0]
    target = mp.mpf(DOUBLY_MAGIC[0][4]) / (me * 4 * G8)
    cands = {
        "Sum_y/y[12]": sum(y) / y0,
        "Sum_2row_y/y[12]": (sum(y) - y0) / y0,
        "(y[12]+y[11,1])/y[12]": (y0 + y[1]) / y0,
        "Sum(y*chi)/(y*chi)[12]": sum(c) / c0,
        "tr_M/y[12]": trM / y0,
    }
    print("=" * 78)
    print("ρ_F derivation attempt (qou-2row)")
    print("=" * 78)
    print(f"\n[Attempt 1] fit-free two-row ratios vs target ρ_F(⁴He)={mp.nstr(target,6)}:")
    best = min(cands.items(), key=lambda kv: abs(kv[1] / target - 1))
    for name, val in cands.items():
        print(f"   {name:<26}{mp.nstr(val,6):>10}  ({mp.nstr((val/target-1)*100,4)}%)")
    print(f"   closest {best[0]} at {mp.nstr((best[1]/target-1)*100,3)}% — cherry-picks blocks (fit). NO match.")

    # Attempt 2 — is ρ_F constant across doubly-magic light nuclei?
    print("\n[Attempt 2] ρ_F = B_AME/(m_e·A·8G) across doubly-magic light nuclei:")
    rhos = []
    for name, Z, N, A, B in DOUBLY_MAGIC:
        rho = mp.mpf(B) / (me * A * G8)
        Ec = mp.mpf("0.7") * Z * (Z - 1) / mp.mpf(A) ** mp.mpf("0.333333")
        rho_s = (mp.mpf(B) + Ec) / (me * A * G8)
        rhos.append(rho)
        print(f"   {name:<5}(Z={Z:<2}N={N:<2})  ρ_F(obs)={mp.nstr(rho,6)}   ρ_F(strong)={mp.nstr(rho_s,6)}")
    spread = (max(rhos) - min(rhos)) / min(rhos)
    print(f"   ⇒ ρ_F drifts 1.89→2.28 (obs); Coulomb makes it WORSE (1.95→2.80). NOT a constant "
          f"(spread {mp.nstr(spread*100,3)}%).")

    print("\n### Verdict: ρ_F is a per-nucleus A-dependent effective prefactor — no categorical constant")
    print("    to derive. '2' is the rounded ⁴He value. CPT route refuted, two-row ratio no-match, and")
    print("    the value is not even 2 away from ⁴He. A real derivation must reproduce ρ_F(A) (1.89→2.28),")
    print("    a harder target no corpus quantity supplies. Honest wall.")

    not_constant = spread > mp.mpf("0.1")   # >10% drift ⇒ not a constant
    no_ratio_match = abs(best[1] / target - 1) > mp.mpf("0.05")
    ok = not_constant and no_ratio_match
    wb = WitnessBuilder("he4-rho-F-two-row-stratum-search", engine="python (mpf 50 dps; reads ⁴He H₁₂ witness)")
    wb.set_description(
        "qou-2row derivation attempt for ρ_F(⁴He). Attempt 1: no fit-free two-row Frobenius ratio "
        "reproduces ρ_F=1.889 (closest 1.782, −5.7%, cherry-picks blocks). Attempt 2 (decisive): ρ_F "
        "is NOT a constant — B_AME/(m_e·A·8G) drifts 1.889 (⁴He) → 2.130 (¹⁶O) → 2.284 (⁴⁰Ca) across "
        "doubly-magic light nuclei, and Coulomb add-back makes it worse (1.95→2.39→2.80). So '2' is "
        "the rounded ⁴He value, not a universal categorical prefactor. Verdict: ρ_F is a per-nucleus "
        "A-dependent effective prefactor; the CPT alt-block route is refuted, a two-row ratio gives no "
        "match, and there is no constant to derive — a real derivation must reproduce ρ_F(A), which no "
        "corpus quantity supplies. Honest wall. Scope-(a); no fit; no wiring; q₀ proton-anchored.")
    wb.add_parameter("q0_anchor", "proton/experimental (q_parameter.Q_MP)")
    wb.add_data("target_rho_F_he4", mp.nstr(target, 12))
    wb.add_data("rho_F_obs", {n: mp.nstr(r, 8) for (n, *_), r in zip(DOUBLY_MAGIC, rhos)})
    wb.add_data("rho_F_drift_spread_frac", mp.nstr(spread, 8))
    wb.add_data("closest_two_row_ratio", {best[0]: mp.nstr(best[1], 8)})
    wb.add_assertion(
        name="rho_F_not_a_constant_and_no_two_row_ratio_derives_it",
        computed=bool(ok), expected=True, tolerance=0,
        source=("ρ_F=B_AME/(m_e·A·8G) drifts >10% across doubly-magic light nuclei (1.889→2.130→2.284; "
                "Coulomb worsens it to 1.95→2.80), so it is not a categorical constant — '2' is a ⁴He "
                "rounding. AND the closest fit-free two-row ratio misses 1.889 by >5%. Both structural "
                "routes fail; the derivation target (a constant) is ill-posed. Scope-(a). No fit."))
    out = wb.save()
    print(f"\nWitness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
