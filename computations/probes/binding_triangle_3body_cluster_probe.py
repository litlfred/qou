#!/usr/bin/env python3
"""3-body cluster in the multiplicative model -- CORRECTED (the sign is NOT fixed).

CORRECTION (2026-06-23, owner caught the error). An earlier version of this probe
claimed that "closing the triangle flips the 3-body cluster to attractive,
matching the Mayer b3 to +4.9%". That was WRONG -- it cherry-picked the single
top (3-bond) cluster term `+c*PROD(1-f)` and compared it to the empirical b3,
ignoring the (negative) 2-bond clusters that are part of the same physical
3-body content.

The honest decomposition of the product-model binding
`B = E0*tau_vac*(1 - PROD f)` over the triangle bonds is

    B = [1-bond clusters: +c*SUM x]            (pairwise)
      + [2-bond clusters: -c*SUM x_i x_j]      (negative)
      + [3-bond cluster:  +c*x_a x_b x_c]      (positive)

with x = 1-f.  The **physical beyond-pairwise 3-body content** is the SUM of the
higher clusters (2-bond + 3-bond), and it is strongly NEGATIVE (destructive):
-5.7 to -7.0 MeV for T, -4.7 to -5.9 for 3He -- the SAME sign as the framework's
joint-trace c3 < 0, and OPPOSITE the attractive empirical b3 > 0 (4x too big).

So closing the triangle does NOT flip the physical sign. The individual cluster
signs DO alternate by bond-count parity (Lean: ursell2_nonpos / ursell3_nonneg),
but the multiplicative deficit's full many-body content is destructive at every
order -- a structural property of a saturating product, proved sorry-free as
`QOU.BraidKnot.Cluster.productModel_3body_nonpos`: for ANY product model
B(S)=c(1-PROD f), c>=0, f in [0,1], the beyond-pairwise 3-body content
c*(Sf - PROD f - 2) <= 0. This holds for the signed closed-form trace
(tau_M = tau_vac*PROD f, which factorises and saturates too) AND the |chi|
combiner. So an attractive (positive) 3-body force requires a genuinely
NON-multiplicative / cooperative combiner -- an enhancing interface f>1, or a
true 3-body operator that is not a product of pairwise factors -- NOT a sign
convention on a product, and NOT the bond topology.
"""
import time as _time  # noqa: E402 — wall-clock anchor for witness durationMs
_T0 = _time.monotonic()
import json
import sys
from pathlib import Path

import mpmath as mp

# Path bridge (moved above the set_compute_dps() call — it is what
# puts computations/substrate on sys.path so `_precision` resolves).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
REPO = Path(__file__).resolve().parents[2]
COMP = REPO / "computations"
sys.path.insert(0, str(COMP))
import closed_form_tau_M as C  # noqa: E402

Q0 = mp.mpf("1.10997858275138080759166909561076887987449912187357763605672")
M_E = mp.mpf("0.51099895069")
E0 = M_E / (Q0 * (Q0 - 1))
Z_MK = C.markov_z(Q0)
H_MK = C.hecke_h(Q0)
TAU_P = mp.mpf("1.22036288908669305595736107223")
TAU_N = mp.mpf("0.7280918153466761555460727563") / (TAU_P * Z_MK)
B2 = mp.mpf("2.224566")
AME = {"T": mp.mpf("8.481798"), "3He": mp.mpf("7.718043")}
TRIANGLE = {"T": (1, 2, ["pn", "pn", "nn"]), "3He": (2, 1, ["pp", "pn", "pn"])}


def fac(kind, f_pn):
    return {"pp": Z_MK, "nn": Z_MK - H_MK, "pn": f_pn}[kind]


def main():
    print("=" * 80)
    print("3-BODY CLUSTER (product model) -- full decomposition, sign NOT fixed by triangle")
    print(f"  E0={mp.nstr(E0,7)}  (0 tuned params)")
    print("=" * 80)
    rows = []
    for conv, f_pn in [("chi (pn=z)", Z_MK), ("bar-averaged (pn=z-h/2)", Z_MK - H_MK / 2)]:
        print(f"\n--- pn convention: {conv} ---")
        for atom in ["T", "3He"]:
            Z, N, bonds = TRIANGLE[atom]
            tau_vac = TAU_P**Z * TAU_N**N
            c = E0 * tau_vac
            xs = [1 - fac(b, f_pn) for b in bonds]
            one = c * mp.fsum(xs)                                          # 1-bond (pairwise)
            two = -c * mp.fsum([xs[i] * xs[j] for i in range(3) for j in range(i + 1, 3)])
            three = c * xs[0] * xs[1] * xs[2]                              # 3-bond (the cherry-pick)
            beyond = two + three                                          # FULL 3-body content
            b3 = AME[atom] - 3 * B2
            print(f"  {atom:4s} 1-bond={mp.nstr(one,5):>8}  2-bond={mp.nstr(two,5):>8}"
                  f"  3-bond={mp.nstr(three,5):>7}  | beyond-pair={mp.nstr(beyond,5):>8}"
                  f"  vs empirical b3={mp.nstr(b3,4)}  same_sign={(beyond>0)==(b3>0)}")
            rows.append({"atom": atom, "pn_convention": conv,
                         "one_bond_MeV": mp.nstr(one, 10), "two_bond_MeV": mp.nstr(two, 10),
                         "three_bond_MeV": mp.nstr(three, 10),
                         "beyond_pairwise_MeV": mp.nstr(beyond, 10),
                         "empirical_b3_MeV": mp.nstr(b3, 10),
                         "same_sign_as_b3": bool((beyond > 0) == (b3 > 0))})

    print("\n" + "=" * 80)
    print("VERDICT (corrected): the multiplicative model's 3-body content is DESTRUCTIVE.")
    print("  The full beyond-pairwise sum (2-bond + 3-bond) is -4.7 to -7.0 MeV for all")
    print("  atoms/conventions -- SAME sign as the framework joint-trace c3 < 0, OPPOSITE the")
    print("  attractive empirical b3 > 0. Closing the triangle does NOT flip the sign; the")
    print("  +3-bond term alone (~+1.9) was a cherry-pick, not the physical 3-body force.")
    print("  Per-cluster signs alternate by parity (proved), but the SUM is bounded <= 0:")
    print("  productModel_3body_nonpos (Lean) proves c*(Sf - PROD f - 2) <= 0 for any product")
    print("  model, signed or |chi|. So an attractive 3-body force needs a NON-multiplicative")
    print("  cooperative combiner (an enhancing f>1 interface, or a true 3-body operator that")
    print("  is not a product of pairwise factors) -- NOT a sign convention on a product.")

    witness = {
        "computation": "binding-triangle-3body-cluster",
        "description": ("CORRECTED: product-model 3-body content. The full beyond-pairwise "
                        "(2-bond + 3-bond) clusters sum to -4.7..-7.0 MeV (destructive), opposite "
                        "empirical b3 > 0. Closing the triangle does NOT flip the sign; the prior "
                        "'+u3 matches b3' claim cherry-picked the top cluster term and is retracted. "
                        "The sign candidate is the chirality involution (|chi| vs signed trace)."),
        "scriptFile": "computations/probes/binding_triangle_3body_cluster_probe.py",
        "parameters": {"q_0": str(Q0), "E0_MeV": str(E0), "tau_p": str(TAU_P),
                       "tau_n": str(TAU_N), "free_parameters": 0},
        "data": {"rows": rows, "verdict": "multiplicative_3body_is_destructive_sign_not_fixed_by_triangle"},
    }
    import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _sys.path.insert(0, str(COMP / "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
    out = WitnessBuilder.wrap_legacy(
        "binding-triangle-3body-cluster", witness,
        script_path=__file__, engine="mpmath", start_time=_T0,
        output_dir=str(COMP),
    ).save()
    print(f"\nwitness -> {out.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
