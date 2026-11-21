#!/usr/bin/env python3
"""The E_0 tower factor is a ONE-PARAMETER FAMILY in L_q; the implemented value pins L_q = sqrt(hbar_q).

# Ref: content/.../lean/QOU/QBeta/TowerGeometricSum.lean  (towerSum_iterated, sorry-free)
# Ref: content/.../observations/brane-tower-q-laplacian-decay-proof.md  (Step 3, an EQUALITY)
# Ref: computations/qbeta/qbeta_e0.py                    (canonical() = tower_summed())
# Ref: docs/audits/2026-09-12-zd-gap-anatomy-and-three-undone-migrations.md

WHY THIS EXISTS.  Bean `qou-y3bm` was closed with ONE hypothesis left isolated:
is `Delta^{(n)}` level-independent?  It is NOT, and the corpus already said so --
`prop:brane-tower-q-laplacian-decay` Step 3 states an EQUALITY,

    |<e_k, Delta^{(n)} e_k>| = (lambda_k^{(q)})^n ,   lambda_k = [k]_q^2 * hbar_q / L_q^2

so `Delta^{(n)}` is the n-th ITERATE of the q-Laplacian.  `towerSum_of_const` is a
true theorem whose hypothesis this object does not satisfy.

CONSEQUENCE, and it is the point: the tower is geometric in `hbar_q^2 * lambda_k`,
not in `hbar_q^2`, so the factor is

    1 / (1 - hbar_q^2 * lambda_k)

and equals the implemented `1/(1 - hbar_q^2)` EXACTLY WHEN `lambda_k = 1`.  At the
leading mode `[1]_q = 1`, so that pins

    L_q = sqrt(hbar_q)

`L_q` is the *q-deformed filament length* -- a FREE geometric scale
(`fluid-dynamics/discrete-vortex-spectrum`; the Kelvin derivation takes `L_q = L`,
the period).  So `qbeta_e0.tower_summed` DOES carry a hidden parameter, and this
probe names it and prices the choice.

IT CHANGES NOTHING.  `qbeta_e0` is untouched; this measures what adopting it
assumes.  Whether `L_q = sqrt(hbar_q)` is the right filament length is a modelling
question for the owner, not something to settle by picking the value that
reproduces the current number -- that would be the selection-against-the-target
the anti-fit directive forbids, one level up.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / p) for p in
                ("computations", "computations/substrate", "tools/qou-substrate/python",
                 "computations/qbeta")]
from mpmath import mp, mpf, nstr, sqrt

mp.dps = 50
ASSERTS: list[tuple[str, bool, str]] = []
failures = []


def check(label, ok, detail=""):
    print(f"  {'ok  ' if ok else 'FAIL'} {label}" + (f"   {detail}" if detail else ""))
    ASSERTS.append((label, bool(ok), detail))
    if not ok:
        failures.append(label)


import qou_substrate.constants as C
q = mpf(C.Q_50_DIGIT_STR)
hbar = 1 - 1 / q
me = mpf(str(C.M_E_MEV))
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
E0_base = _qbeta_e0.order_zero_scaled(me, q)          # the order-zero scale


def lam(k, Lq):
    """lambda_k^(q) = [k]_q^2 * hbar_q / L_q^2."""
    qi = (q ** k - q ** (-k)) / (q - 1 / q)
    return qi ** 2 * hbar / Lq ** 2


def tower(lam_val):
    return 1 / (1 - hbar ** 2 * lam_val)


print("CLAIM 1 - the implemented factor corresponds to lambda_1 = 1, i.e. L_q = sqrt(hbar_q)")
Lq_star = sqrt(hbar)
print(f"       hbar_q          = {nstr(hbar,12)}")
print(f"       sqrt(hbar_q)    = {nstr(Lq_star,12)}   <- the L_q the implemented factor pins")
print(f"       lambda_1 there  = {nstr(lam(1, Lq_star),12)}")
check("at L_q = sqrt(hbar_q) the leading eigenvalue is exactly 1",
      abs(lam(1, Lq_star) - 1) < mpf("1e-40"),
      f"lambda_1 - 1 = {nstr(abs(lam(1,Lq_star)-1),4)}")
check("and the tower factor there equals the implemented 1/(1 - hbar^2)",
      abs(tower(lam(1, Lq_star)) - 1 / (1 - hbar ** 2)) < mpf("1e-40"),
      f"both = {nstr(1/(1-hbar**2),12)}")

print("\nCLAIM 2 - a DIFFERENT L_q gives a different E_0, at the same scale as the whole effect")
print(f"       {'L_q':>22} {'lambda_1':>18} {'tower factor':>16} {'E_0 (MeV)':>16} {'vs impl.':>11}")
impl = tower(lam(1, Lq_star))
rows = {}
for nm, Lq in (("sqrt(hbar_q)  [implemented]", Lq_star),
               ("1  (Kelvin L_q = L, L=1)", mpf(1)),
               ("hbar_q", hbar),
               ("q - 1/q  ( = h )", q - 1 / q)):
    lv = lam(1, Lq)
    tw = tower(lv)
    rows[nm] = {"L_q": nstr(Lq, 12), "lambda_1": nstr(lv, 12),
                "tower_factor": nstr(tw, 12), "E0_MeV": nstr(E0_base * tw, 12),
                "rel_vs_implemented_pct": nstr((tw / impl - 1) * 100, 6)}
    print(f"       {nm:>22} {nstr(lv,10):>18} {nstr(tw,12):>16} "
          f"{nstr(E0_base*tw,12):>16} {nstr((tw/impl-1)*100,4):>10}%")
spread = max(abs(mpf(r["rel_vs_implemented_pct"])) for r in rows.values())
check("the L_q choice moves E_0 by at least as much as the tower correction itself",
      spread > mpf("0.5"),
      f"widest departure {nstr(spread,4)}% against a total tower correction of "
      f"{nstr((impl-1)*100,4)}% -- so the choice of L_q is not a detail, it IS the effect")

print("\nCLAIM 3 - convergence is not automatic for every L_q")
bad = [nm for nm, r in rows.items() if mpf(r["lambda_1"]) * hbar ** 2 >= 1]
check("all four sampled L_q keep hbar^2*lambda_1 < 1 (the series converges)",
      not bad, f"non-convergent samples: {bad or 'none'}")
_Lq_crit = sqrt(hbar) * hbar     # lambda_1 = 1/hbar^2  =>  L_q^2 = hbar^3
print(f"       divergence threshold: L_q <= sqrt(hbar_q^3) = {nstr(sqrt(hbar**3),10)}")
check("the divergence threshold is well below every sampled L_q",
      sqrt(hbar ** 3) < min(mpf(r["L_q"]) for r in rows.values()),
      "so the series converges across the plausible range; the issue is the VALUE, "
      "not convergence")

print("\nCLAIM 4 - qbeta_e0 is UNCHANGED by this probe")
import qbeta_e0
check("qbeta_e0.canonical() still returns the tower_summed value",
      abs(qbeta_e0.canonical() - E0_base / (1 - hbar ** 2)) < mpf("1e-30"),
      f"{nstr(qbeta_e0.canonical(),12)} MeV -- measured, not modified")

print(f"\n=== {len(ASSERTS)-len(failures)}/{len(ASSERTS)} checks ok" if not failures
      else f"\n=== FAILURES: {failures}")

try:
    from witness_base import WitnessBuilder
except ImportError as e:
    print(f"witness skipped: {e}")
    WitnessBuilder = None
if WitnessBuilder is not None:
    w = WitnessBuilder("qbeta-e0-tower-lq-dependence")
    w.set_description(
        "Resolves the one hypothesis qou-y3bm left open, with a NEGATIVE: Delta^{(n)} "
        "is NOT level-independent. prop:brane-tower-q-laplacian-decay Step 3 is an "
        "EQUALITY, |<e_k, Delta^{(n)} e_k>| = (lambda_k)^n, so Delta^{(n)} is the n-th "
        "ITERATE of the q-Laplacian. The tower is therefore geometric in hbar_q^2*lambda_k "
        "and sums to 1/(1 - hbar_q^2*lambda_k); the implemented 1/(1 - hbar_q^2) is the "
        "lambda_k = 1 member, which pins L_q = sqrt(hbar_q). L_q is a FREE geometric "
        "scale, so qbeta_e0.tower_summed does carry a hidden parameter -- now named and "
        "priced. Lean: towerSum_iterated / towerSum_iterated_eq_simple_iff / "
        "leadingMode_lam_eq_one_iff, sorry-free. Measures only; qbeta_e0 unchanged."
    )
    w.add_data("implemented_pins_Lq", nstr(Lq_star, 20))
    w.add_data("tower_factor_family", rows)
    w.add_data("total_tower_correction_pct", nstr((impl - 1) * 100, 10))
    w.add_data("divergence_threshold_Lq", nstr(sqrt(hbar ** 3), 12))
    w.add_data("hypothesis_of_towerSum_of_const_is_false", True)
    w.add_data("open_question_is_a_modelling_call",
               "is L_q = sqrt(hbar_q) the right q-deformed filament length? Choosing it "
               "because it reproduces the current E_0 would be selection against the "
               "target. Owner call.")
    for label, ok, detail in ASSERTS:
        w.add_assertion(f"{label}{' -- ' + detail if detail else ''}",
                        computed="true" if ok else "false", expected="true")
    w.save()
    print("witness written")
sys.exit(1 if failures else 0)
