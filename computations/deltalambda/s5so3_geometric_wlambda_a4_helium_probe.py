#!/usr/bin/env python3
"""s5so3_geometric_wlambda_a4_helium_probe.py — the A=4 analog of #4392: the GENUINE
geometric (Beasley-Witten / WRT(S3/2I)) keystone W_lambda = d_q^2/D^2 re-weight of the
He-4 (H_12) atomic trace, forward, 0-fit, compared to the two AME-required A=4 magnitudes.

Context (option-e ledger, PROBE 2 = A=4 interface operator + conj:s5-so3-fiber-action)
--------------------------------------------------------------------------------------
#4378 (HeliumBrunnianDeficitMeasured) measured tau_L4 > 1 for the 4-component Brunnian
link => c4 = E0*(1-tau_L4) < 0, sign-COMPATIBLE with the derived mu4 = -4.591 (the
Route-3 sign wall's antecedent is measured FALSE).  So the A=4 SIGN is settled and the
MAGNITUDE is the live, OPEN test: does the interface operator + s5-so3 fiber action
SUPPLY the A=4 binding magnitude, forward and 0-fit?

The s5-so3 fiber action (conj:s5-so3-fiber-action) supplies the color-tube weight matrix
W_lambda over the He-4 Wedderburn blocks (lambda |- 12), normalized to sum 1 (the
color-tube block: "normalised to Sum W = 1").  The genuine geometric measure is the
Beasley-Witten / WRT(S3/2I) keystone weight W_geom = d_q(lambda)^2 / D^2, D^2 = Sum d_q^2
(WLambdaMTCLocalizationObligation.lean C1: Sum W_geom = 1, "NOT [n]_q!").  This is the
SAME measure #4392 forward-evaluated for A=3 (where it OVERSHOT mu3 by ~30x).

This probe forward-evaluates, 0-fit, on the precomputed canonical He-4 H_12 perblock
character table (chi-helium-4-h12-at-q0-50dps.witness.json, bean b0vf; colour-weighted
averaged-crossing convention, the production He-4 trace):
  * production tr_M   = Sum_lambda y_lambda * chi_lambda           (= 0.0553584, the canonical Frobenius trace)
  * geometric reweight S_geom = Sum_lambda W_geom_lambda * chi_lambda   (y_lambda -> W_geom)
  * abs-character forms Sum W |chi|  (the #4392 cluster form)
  * the s5-so3 Delta_lambda sign-weighted forms  Sum W chi sign(lambda)  (Option-E ansatz)
Only the weight system changes; chi_lambda, q0, the word are the canonical b0vf table.

STRICT anti-fit
---------------
W_geom is fixed by q0 + hook-lengths (0 fit).  B(4He)_AME = 28.29566 MeV and
|mu4| = 4.591 MeV enter ONLY as targets, never inverted.  We report where the geometric
number lands; we do NOT rescale to hit a target.  The pre-existing
a4_option_e_color_tube_closure.py applies an ad-hoc 10^3 "color-tube scale" chosen to
land on AME -- that is a FIT and is NOT used here.  Nothing wired; free_parameters = 0.

Structural bound (formalize-first, GeometricWLambdaA4HeliumBound.lean)
---------------------------------------------------------------------
A normalized measure W (Sum W_lambda = 1) gives |Sum W chi| <= max_lambda |chi_lambda|
(weighted-average bound).  Here max|chi| = 63.62 (lambda=(6,3,3)), so E0*max|chi| = 266 MeV
> B(4He) = 28.30: the bound does NOT exclude the target => NOT a scope-(b) exclusion, the
class is not pruned, the geometric number must be computed (this probe).
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
HERE = Path(__file__).resolve().parent
COMP = HERE.parent

CACHE = COMP / "chi-helium-4-h12-at-q0-50dps.witness.json"
d = json.loads(CACHE.read_text())
q0 = mp.mpf(d["q_0_50dps"])
m_e = mp.mpf("0.51099895069")
E0 = m_e / (q0 * (q0 - 1))                       # SAME E0 as #4392 / rho_F
B4He = mp.mpf("28.29566")                         # AME full 4He binding, target only
MU4 = mp.mpf("4.591048")                          # |mu4| 4-body simplex residual, target only
MU3 = mp.mpf("0.47076896")

bp = d["by_partition"]
chis = {tuple(it["partition"]): mp.mpf(it["chi_lambda"]) for it in bp}
ys = {tuple(it["partition"]): mp.mpf(it["y_lambda"]) for it in bp}


def q_int(m):
    return (q0**m - q0 ** (-m)) / (q0 - 1 / q0)


def hook_lengths(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    hs = []
    for i, row in enumerate(lam):
        for j in range(row):
            hs.append((row - 1 - j) + (conj[j] - 1 - i) + 1)
    return hs


def dq(lam):
    n = sum(lam)
    qf = mp.mpf(1)
    for m in range(1, n + 1):
        qf *= q_int(m)
    ph = mp.mpf(1)
    for h in hook_lengths(lam):
        ph *= q_int(h)
    return qf / ph


def dim_classical(lam):
    """Ordinary Young-diagram dimension f^lambda via the hook-length formula."""
    n = sum(lam)
    import math

    fact = math.factorial(n)
    ph = 1
    for h in hook_lengths(lam):
        ph *= h
    return fact // ph


def conj_part(lam):
    return tuple(sum(1 for x in lam if x >= i) for i in range(1, lam[0] + 1))


def delta_sign(lam):
    """Chirality sign sgn(w_0^{S_{lambda'}}) = (-1)^{sum C(c,2)} over conjugate columns."""
    conj = conj_part(lam)
    length = sum(c * (c - 1) // 2 for c in conj)
    return 1 if length % 2 == 0 else -1


dqsq = {lam: dq(lam) ** 2 for lam in chis}
D2 = sum(dqsq.values())
Wgeom = {lam: dqsq[lam] / D2 for lam in chis}
dims = {lam: dim_classical(lam) for lam in chis}
sgn = {lam: delta_sign(lam) for lam in chis}

sum_y = sum(ys.values())
sum_W = sum(Wgeom.values())
maxchi = max(abs(c) for c in chis.values())
argmax = max(chis, key=lambda l: abs(chis[l]))


def frob(weight, use_abs=False, use_sign=False, use_dim=False):
    tot = mp.mpf(0)
    for l in chis:
        term = chis[l]
        if use_abs:
            term = abs(term)
        if use_sign:
            term = term * sgn[l]
        if use_dim:
            term = term * dims[l]
        tot += weight[l] * term
    return tot


def main() -> int:
    print("=" * 92)
    print("A=4 GEOMETRIC W_lambda = d_q^2/D^2 (Beasley-Witten / WRT(S3/2I)) re-weight -- He-4 H_12")
    print(f"  q0={float(q0):.8f}  E0={float(E0):.6f} MeV  m_e={float(m_e):.6f}")
    print(f"  Sum y_lambda={float(sum_y):.6f} (NOT 1)   Sum W_geom={float(sum_W):.6f} (=1, C1)")
    print(f"  D^2=Sum d_q^2 = {mp.nstr(D2,8)}   max|chi|={float(maxchi):.4f} at {argmax}")
    print("=" * 92)

    # --- canonical forward objects (the #4392 analog: Sum W |chi|, and plain Frobenius) ---
    trM = frob(ys)                                  # production Frobenius tr_M
    S_geom_signed = frob(Wgeom)                     # Sum W_geom chi (signed characters)
    y_abs = frob(ys, use_abs=True)                  # Sum y |chi|
    geom_abs = frob(Wgeom, use_abs=True)            # Sum W_geom |chi|   (#4392 cluster form)

    # --- Option-E Delta_lambda sign-weighted forms (|Delta|=dim, sign=chirality) ---
    y_sign = frob(ys, use_sign=True)
    geom_sign = frob(Wgeom, use_sign=True)
    y_sign_dim = frob(ys, use_sign=True, use_dim=True)
    geom_sign_dim = frob(Wgeom, use_sign=True, use_dim=True)

    print(f"\n  production tr_M = Sum y chi              = {mp.nstr(trM,8)}")
    print(f"  geometric      = Sum W_geom chi          = {mp.nstr(S_geom_signed,8)}")
    print(f"  Sum y |chi|                              = {mp.nstr(y_abs,8)}")
    print(f"  Sum W_geom |chi|  (#4392 cluster form)   = {mp.nstr(geom_abs,8)}")
    print(f"  |Sum y   chi sign|      (Delta=sign)     = {mp.nstr(abs(y_sign),8)}")
    print(f"  |Sum W   chi sign|      (Delta=sign)     = {mp.nstr(abs(geom_sign),8)}")
    print(f"  |Sum y   chi sign dim|  (Delta=sign*dim) = {mp.nstr(abs(y_sign_dim),8)}")
    print(f"  |Sum W   chi sign dim|  (Delta=sign*dim) = {mp.nstr(abs(geom_sign_dim),8)}")

    # forward binding magnitudes (E0-scale, the canonical cluster scale)
    print("\n  --- forward magnitudes (x E0), vs targets B(4He)=28.296, |mu4|=4.591 ---")
    def report(name, S):
        c = E0 * abs(S)
        print(f"    E0*|{name:22s}| = {float(c):11.5f} MeV  = {float(c/B4He):8.4f}x B4He  = {float(c/MU4):9.4f}x |mu4|")
        return c
    c_geom_abs = report("Sum W_geom |chi|", geom_abs)
    c_y_abs = report("Sum y |chi|", y_abs)
    c_geom_signed = report("Sum W_geom chi", S_geom_signed)
    c_geom_sign = report("Sum W chi sign", geom_sign)
    c_geom_sign_dim = report("Sum W chi sign dim", geom_sign_dim)

    # reweight ratio r_geom (the #4392 quantity): cluster form Sum W|chi| / Sum y|chi|
    r_geom = geom_abs / y_abs
    print(f"\n  r_geom = (Sum W_geom |chi|)/(Sum y |chi|) = {mp.nstr(r_geom,6)}   (A=3 analog was 47.4)")
    print(f"  m_e * max|chi| = {float(m_e*maxchi):.4f} MeV  (normalized-W bound, x m_e)")
    print(f"  E0  * max|chi| = {float(E0*maxchi):.4f} MeV  (normalized-W bound, x E0)")

    # verdict: does ANY of the canonical geometric forms land on B4He or |mu4| 0-fit?
    cands = {
        "E0*Sum W_geom|chi|": c_geom_abs,
        "E0*Sum W_geom chi": c_geom_signed,
        "E0*Sum W chi sign": c_geom_sign,
        "E0*Sum W chi sign dim": c_geom_sign_dim,
    }
    lands_B = any(mp.mpf("0.9") < c / B4He < mp.mpf("1.1") for c in cands.values())
    lands_mu4 = any(mp.mpf("0.9") < c / MU4 < mp.mpf("1.1") for c in cands.values())
    if lands_B or lands_mu4:
        verdict = ("DERIVATION LEAD -- a canonical 0-fit geometric W_lambda form lands within "
                   "10% of an A=4 target (scrutinize for coincidence)")
    else:
        verdict = ("WALL(scope-a) -- no canonical 0-fit geometric W_lambda form lands on B(4He) "
                   "or |mu4|; the s5-so3 interface reweighting does NOT supply the A=4 magnitude "
                   "as-is (this construction alone). NOT a (b) exclusion: E0*max|chi|=266>28.3, so "
                   "the target is within the normalized-W span -- an EXACT hit needs a tuned weight = FIT.")

    print("\n" + "=" * 92)
    print(f"VERDICT: {verdict}")

    witness = {
        "schema": "witness/v1",
        "producer": "computations/deltalambda/s5so3_geometric_wlambda_a4_helium_probe.py",
        "computation": "s5so3-geometric-wlambda-a4-helium",
        "description": (
            "A=4 analog of #4392: genuine geometric (Beasley-Witten / WRT(S3/2I)) keystone "
            "W_lambda = d_q^2/D^2 (Sum=1, C1) re-weight of the canonical He-4 H_12 perblock trace "
            "(chi-helium-4-h12-at-q0-50dps, bean b0vf), forward 0-fit, vs the two A=4 targets "
            f"B(4He)_AME=28.29566 and |mu4|=4.591. E0={float(E0):.6f}. Production tr_M={float(trM):.6f}; "
            f"E0*Sum W_geom|chi|={float(c_geom_abs):.4f} MeV ({float(c_geom_abs/B4He):.3f}x B4He); "
            f"r_geom={float(r_geom):.4f}. B(4He) and mu4 targets only, NEVER inverted; the ad-hoc 10^3 "
            "color-tube scale in a4_option_e_color_tube_closure.py is a FIT and is NOT used. VERDICT: "
            + verdict
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "free_parameters": 0,
            "q0": str(q0), "E0_MeV": str(E0), "m_e_MeV": str(m_e),
            "level": "He-4 H_12 perblock Sum_{lambda|-12} weight * chi_lambda (production b0vf table)",
            "weight_systems": "production y_lambda (Sum=0.00435); geometric d_q^2/D^2 (Sum=1)",
            "D2_sum_dq2": str(D2),
            "max_abs_chi": str(maxchi),
            "argmax_partition": str(argmax),
            "note": "B4He=28.29566 & |mu4|=4.591 targets only; SAME chi/q0/word as b0vf; ONLY weight changes; 0 fit.",
        },
        "results": {
            "production": {"trM_sum_y_chi": str(trM), "sum_y_abs_chi": str(y_abs),
                           "E0_times_sum_y_abs_chi_MeV": str(c_y_abs)},
            "geometric": {
                "sum_Wgeom_chi_signed": str(S_geom_signed),
                "sum_Wgeom_abs_chi": str(geom_abs),
                "E0_times_sum_Wgeom_abs_chi_MeV": str(c_geom_abs),
                "over_B4He": str(c_geom_abs / B4He),
                "over_mu4": str(c_geom_abs / MU4),
                "r_geom_over_production": str(r_geom),
            },
            "delta_sign_forms": {
                "abs_sum_y_chi_sign": str(abs(y_sign)),
                "abs_sum_Wgeom_chi_sign": str(abs(geom_sign)),
                "E0_times_abs_sum_Wgeom_chi_sign_MeV": str(c_geom_sign),
                "abs_sum_y_chi_sign_dim": str(abs(y_sign_dim)),
                "abs_sum_Wgeom_chi_sign_dim": str(abs(geom_sign_dim)),
                "E0_times_abs_sum_Wgeom_chi_sign_dim_MeV": str(c_geom_sign_dim),
            },
            "normalized_W_bound": {
                "max_abs_chi": str(maxchi),
                "E0_times_max_abs_chi_MeV": str(E0 * maxchi),
                "m_e_times_max_abs_chi_MeV": str(m_e * maxchi),
                "bound_excludes_B4He": bool(E0 * maxchi < B4He),
                "note": "|Sum W chi| <= max|chi| for any Sum W=1; bound 266 MeV > 28.3 => target NOT excluded (not a (b))",
            },
            "targets": {"B4He_AME_MeV": str(B4He), "abs_mu4_MeV": str(MU4), "mu3_MeV": str(MU3)},
            "verdict": {
                "classification": verdict,
                "lands_on_B4He": bool(lands_B), "lands_on_mu4": bool(lands_mu4),
                "is_fit": False, "wired": False, "free_param_count": 0, "target_inverted": False,
                "ad_hoc_10cubed_scale": "FIT in a4_option_e_color_tube_closure.py; NOT used here",
                "anti_fit": "W_geom + y_lambda from q0 + hook-lengths; chi/q0/word = b0vf table; targets never inverted; nothing wired.",
            },
        },
        "scriptCommitSha": "uncommitted",
    }
    out = HERE / "s5so3-geometric-wlambda-a4-helium.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False))
    print(f"\nwitness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
