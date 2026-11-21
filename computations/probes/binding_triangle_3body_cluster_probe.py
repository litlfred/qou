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
-3.20 MeV for T and -2.87 for 3He under the canonical convention (-2.45 / -2.13
under the legacy plain-sigma one) -- the SAME sign as the framework's joint-trace
c3 < 0, and OPPOSITE the attractive empirical b3 > 0.

(Those magnitudes read "-5.7 to -7.0 for T, -4.7 to -5.9 for 3He" until
2026-08-26. They were computed from HARDCODED convention-C tau_p / tau_n
combined with a live convention-D `Z_MK` -- see the constants below. The SIGN,
which is this probe's entire claim and is Lean-proved for any product model, is
unchanged; only the magnitudes were wrong.)

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
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)

Q0 = mp.mpf("1.10997858275138080759166909561076887987449912187357763605672")
M_E = mp.mpf("0.51099895069")
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
E0 = _qbeta_e0.order_zero_scaled(M_E, Q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
Z_MK = C.markov_z(Q0)
H_MK = C.hecke_h(Q0)
# 🛑 These were HARDCODED convention-C constants combined with a live
# convention-D `Z_MK` — a frame straddle (fixed 2026-08-26, bean `qou-cds4`).
#   TAU_P = mp.mpf("1.22036288908669305595736107223")
#   TAU_N = mp.mpf("0.7280918153466761555460727563") / (TAU_P * Z_MK)
# 1.2203628890866930... is the Phase 5q **convention-C** proton trace, and
# 0.7280918153466761... its convention-C deuteron. Back-solving TAU_N from a
# C-frame ratio while dividing by the D-frame `Z_MK` gave 0.97377, where the
# C-consistent value is 1.19486 — a factor 1.227 (= z_D/z_C) wrong, in a
# constant that then entered every row. Both constants were correct when
# written; the convention-D migration invalidated them silently, because a
# hardcoded float carries no convention label to audit.
#
# Sourced live from the canonical helper instead, so the frame cannot drift
# again. (That helper was itself fixed the same day — it had been dropping
# each nucleon's two intra-nucleon `averaged` crossings; bean `qou-qu2w`.)
TAU_P = C.compute_tau_M_nucleon_H3("p", Q0, dps=50)
TAU_N = C.compute_tau_M_nucleon_H3("n", Q0, dps=50)
B2 = AME_B_DEUTERON_MEV_VALIDATION
AME = {"T": AME_B_TRITIUM_MEV_VALIDATION, "3He": AME_B_HE3_MEV_VALIDATION}
TRIANGLE = {"T": (1, 2, ["pn", "pn", "nn"]), "3He": (2, 1, ["pp", "pn", "pn"])}


def fac(kind, f_pn):
    return {"pp": Z_MK, "nn": Z_MK - H_MK, "pn": f_pn}[kind]


def main():
    print("=" * 80)
    print("3-BODY CLUSTER (product model) -- full decomposition, sign NOT fixed by triangle")
    print(f"  E0={mp.nstr(E0,7)}  (0 tuned params)")
    print("=" * 80)
    rows = []
    # The sweep used to omit the CANONICAL convention entirely, comparing only
    # two non-canonical ones. Added third (owner ruling R3). It lands within
    # 0.02 % of bar-averaged — the δ/4 term — and does not change the verdict,
    # which is the useful thing to be able to say.
    from _li_2_q_util import flavor_split_leading
    _delta = flavor_split_leading(Q0)
    for conv, f_pn in [
        ("chi (pn=z)", Z_MK),
        ("bar-averaged (pn=z-h/2)", Z_MK - H_MK / 2),
        ("bring_color_weighted (canonical, R3)",
         Z_MK - H_MK * (mp.mpf(1) / 2 - _delta / 4)),
    ]:
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
    print("  The full beyond-pairwise sum (2-bond + 3-bond) is -2.13 to -3.20 MeV across all")
    print("  atoms and all THREE conventions -- SAME sign as the framework joint-trace")
    print("  c3 < 0, OPPOSITE the attractive empirical b3 > 0. Closing the triangle does NOT")
    print("  flip the sign; the +3-bond term alone (~+0.5 to +0.7) was a cherry-pick, not the")
    print("  physical 3-body force. The canonical colour-weighted row lands within 0.02% of")
    print("  bar-averaged, so the verdict does not depend on the p-n convention either.")
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
        "data": {"rows": rows,
                 # Worst case = the LEAST negative beyond-pairwise sum across
                 # every atom and every pn convention; the margin the sign
                 # claim below actually has (bean qou-srvu).
                 "max_beyond_pairwise_MeV": mp.nstr(
                     max(mp.mpf(r["beyond_pairwise_MeV"]) for r in rows), 10),
                 "n_rows_sharing_sign_with_empirical_b3": sum(
                     1 for r in rows if r["same_sign_as_b3"]),
                 "verdict": "multiplicative_3body_is_destructive_sign_not_fixed_by_triangle"},
    }
    import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _sys.path.insert(0, str(COMP / "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
    _wb = WitnessBuilder.wrap_legacy(
        "binding-triangle-3body-cluster", witness,
        script_path=__file__, engine="mpmath", start_time=_T0,
        output_dir=str(COMP),
    )
    # "The SIGN, which is this probe's entire claim and is Lean-proved for any
    # product model" (docstring). It was recorded per row as `same_sign_as_b3`
    # while the witness shipped `allPassed: true` over an EMPTY assertion list
    # (bean qou-srvu). The bar is 0 rows -- the claim's own logic, not a
    # fitted threshold; the worst row sits at -2.127 MeV, so the margin is the
    # whole distance to zero.
    _n_same = sum(1 for r in rows if r["same_sign_as_b3"])
    _wb.add_assertion(
        "beyond_pairwise_3body_never_shares_sign_with_empirical_b3",
        computed=str(_n_same), expected="0", tolerance="0",
        source="Lean ursell2_nonpos / ursell3_nonneg / productModel_3body_nonpos",
    )
    out = _wb.save()
    print(f"\nwitness -> {out.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
