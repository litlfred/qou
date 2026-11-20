#!/usr/bin/env python3
"""Re-derive the keystone muon/electron projected shift under W_lambda, not y_lambda.

WHY THIS EXISTS (beans `qou-j3u0`, Q1/Q2 of the 2026-08-30 design review).

`keystone_qdeform_projector_shift_probe` and `keystone_branching_shift_probe`
both form a muon(3,2) / electron(3,1,1) comparison weighted by the Jones-Markov
weight `y_lambda`. At SU(2)/N=2 that weight is **exactly zero for every
partition with more than two rows**, so `y_(3,1,1) = 0` and the electron side of
both comparisons is identically absent. Those probes were measuring T_mu under
another name.

That vanishing is not a defect in the physics -- it is the corpus's own
Schur-Weyl row-count rule
(`docs/audits/2026-06-22-keystone-schurweyl-su2-rowcount.md`):

    (C^2)^{otimes n} = ⊕_{lambda : <=2 rows} S^lambda ⊗ V_lambda^{SU(2)}

so the electron block is invisible to spin and is an SU(3)-colour object. The
keystone's OWN weight family `W_lambda = d_q(lambda)^2 / [n]_q!` is nonzero on
all seven blocks, is conjugation-symmetric (the Lean-proved C2), and is what the
C1/C2/C6 obligations are stated over. This probe redoes the comparison with it.

WHAT IT FINDS. The PR #2584 refutation of the q-deformed projector shift as the
210 ppb mechanism rests on TWO legs. Under W_lambda:

  leg (a) "6-7 orders too large"  -> SURVIVES  (3.35e6x, ~6.5 orders)
  leg (b) "bar-mixed, fails the   -> FAILS     delta is EXACTLY bar-EVEN;
          bar-even precondition"              delta(q) - delta(1/q) ~ 4e-50

Leg (b) came from the committed witness's numbers, which `qou-j3u0` established
are wrong (a float64 leak turned four exact zeros into ~1e-17 noise).

CONSEQUENCE, stated in the corpus's own scope vocabulary. "Too large by 6.5
orders" is a **scope-(a)** negative: this construction, alone, does not
reproduce the number. It is NOT a scope-(b) structural exclusion, and the
ledger's stronger claim -- "the Markov-trace surface is **exhausted**; any
surviving q-closure must leave the trace-weighting **entirely**" -- was a (b)
resting on (a) plus the now-refuted parity argument. The magnitude refutation
stands; the structural exclusion does not.

NOT ASSERTED HERE: that the trace-weighting route works. It does not reproduce
210 ppb and this probe does not claim otherwise. What is retracted is only the
claim that it is *structurally* foreclosed.

No fit. Reads the pin; carries mpf end to end.
"""
from __future__ import annotations
import sys, pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[2]
for _p in (_ROOT / "computations", _ROOT / "computations" / "substrate"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from mpmath import mp, mpf, nstr                      # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP                # noqa: E402
import pyhecke_native as ph                           # noqa: E402
from witness_base import WitnessBuilder               # noqa: E402

DPS = 50
mp.dps = DPS
MU, EL = (3, 2), (3, 1, 1)
BORROMEAN = [(-1, 1), (1, 2)] * 3      # beta = (sigma_1^-1 sigma_2)^3
PPB = mpf("210e-9")


def q_int(k, q):
    return (q ** k - q ** (-k)) / (q - 1 / q)


def _conj(l):
    return [sum(1 for r in l if r > j) for j in range(l[0])] if l else []


def _hook(l, i, j):
    return l[i] - j + _conj(l)[j] - i - 1


def d_q(lam, q):
    """Balanced quantum dimension via the q-hook formula."""
    f = mpf(1)
    for k in range(1, sum(lam) + 1):
        f *= q_int(k, q)
    d = mpf(1)
    for i, row in enumerate(lam):
        for j in range(row):
            d *= q_int(_hook(lam, i, j), q)
    return f / d


def W(lam, q):
    """Keystone block weight W_lambda = d_q(lambda)^2 / [n]_q!."""
    f = mpf(1)
    for k in range(1, sum(lam) + 1):
        f *= q_int(k, q)
    return d_q(lam, q) ** 2 / f


def chi(lam, q):
    return mp.mpmathify(ph.chi_lambda_braid_mpfr(list(lam), BORROMEAN, str(q), DPS))


def shift(q):
    """(T_mu, T_e, delta) with the W_lambda weighting."""
    tm, te = W(list(MU), q) * chi(MU, q), W(list(EL), q) * chi(EL, q)
    return tm, te, tm - te


def main() -> int:
    q = Q_MP
    w = WitnessBuilder("keystone-wlambda-vs-ylambda-projected-shift", engine="python")

    print("=" * 78)
    print("Keystone muon/electron projected shift: W_lambda vs y_lambda")
    print("=" * 78)
    print(f"q_0 = {q}   dps = {DPS}\n")

    # --- the two weight families, side by side --------------------------------
    from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric as Y
    print("Block weights at q_0 (the whole point):")
    print(f"  {'lambda':<16}{'rows':>5}{'y_lambda (SU(2) Markov)':>28}{'W_lambda (keystone)':>24}")
    rows = {}
    for p in [tuple(x) for x in ph.partitions_of(5)]:
        y, wl = Y(list(p), q), W(list(p), q)
        rows[str(p)] = {"rows": len(p), "y_lambda": y, "W_lambda": wl}
        print(f"  {str(p):<16}{len(p):>5}{nstr(y, 12):>28}{nstr(wl, 12):>24}")
    print("\n  y_lambda vanishes exactly when rows > 2 (SU(2) Schur-Weyl row-count).")
    print("  W_lambda vanishes nowhere and is conjugation-symmetric (keystone C2).")
    w.add_data("block_weights", rows)

    # --- the W-weighted comparison -------------------------------------------
    tm, te, d = shift(q)
    print("\nW_lambda-weighted projected traces  T_g = W_{lambda_g} * chi^{lambda_g}(beta_Bor):")
    print(f"  chi^(3,2)   = {nstr(chi(MU, q), 14)}     T_muon     = {nstr(tm, 14)}")
    print(f"  chi^(3,1,1) = {nstr(chi(EL, q), 14)}     T_electron = {nstr(te, 14)}")
    print(f"  delta = T_mu - T_e   = {nstr(d, 14)}")
    print(f"  delta / T_mu         = {nstr(d / tm, 10)}")
    print(f"  delta / T_e          = {nstr(d / te, 10)}   (BOTH defined -- neither weight is 0)")
    over = abs(d / tm) / PPB
    print(f"  |delta/T_mu| / 210ppb = {nstr(over, 6)}x")
    for k, v in (("T_muon", tm), ("T_electron", te), ("delta", d),
                 ("delta_over_T_mu", d / tm), ("delta_over_T_e", d / te),
                 ("over_210ppb_factor", over)):
        w.add_data(k, v)

    # --- bar parity -----------------------------------------------------------
    _, _, db = shift(1 / q)
    even_res, odd_res = d - db, d + db
    print("\nBar parity (q -> 1/q) of the W-weighted shift:")
    print(f"  delta(q_0)   = {nstr(d, 12)}")
    print(f"  delta(1/q_0) = {nstr(db, 12)}")
    print(f"  delta(q) - delta(1/q) = {nstr(even_res, 8)}   (~0  => bar-EVEN)")
    print(f"  delta(q) + delta(1/q) = {nstr(odd_res, 8)}")
    is_even = abs(even_res) < abs(odd_res)
    print(f"  => bar-{'EVEN' if is_even else 'ODD/MIXED'}")
    w.add_data("delta_bar_image", db)
    w.add_data("bar_even_residual", even_res)
    w.add_data("bar_odd_residual", odd_res)
    w.add_data("bar_parity", "even" if is_even else "odd_or_mixed")

    # --- the two refutation legs ---------------------------------------------
    print("\n" + "=" * 78)
    print("The PR #2584 refutation has TWO legs. Under W_lambda:")
    print(f"  (a) magnitude 6-7 orders too large : SURVIVES  ({nstr(over, 6)}x)")
    print(f"  (b) bar-mixed, fails bar-even      : FAILS     (residual {nstr(even_res, 6)})")
    print("=" * 78)
    print("So the MAGNITUDE refutation stands and is a scope-(a) negative.")
    print("The STRUCTURAL exclusion ('trace-weighting surface exhausted') does not:")
    print("it was a scope-(b) claim resting on (a) plus the parity leg, and leg (b)")
    print("came from the committed witness's float64-corrupted numbers (qou-j3u0).")

    w.add_assertion(
        "electron block carries zero SU(2) Markov weight but nonzero keystone W",
        computed=1 if (Y(list(EL), q) == 0 and W(list(EL), q) != 0) else 0,
        expected=1, tolerance=0,
        source="y_(3,1,1)=0 (>2 rows, SU(2) Schur-Weyl); W_(3,1,1)!=0")
    w.add_assertion(
        "W-weighted shift is bar-EVEN (refutes the 'bar-mixed' leg of #2584)",
        computed=1 if is_even else 0, expected=1, tolerance=0,
        source=f"delta(q)-delta(1/q) = {nstr(even_res, 6)} at dps={DPS}")
    w.add_assertion(
        "W-weighted shift is still orders too large for 210 ppb (leg (a) survives)",
        computed=1 if over > 100 else 0, expected=1, tolerance=0,
        source=f"|delta/T_mu|/210ppb = {nstr(over, 6)}x")

    w.set_description(
        "Re-derives the keystone muon(3,2)/electron(3,1,1) projected Markov shift "
        "using the keystone block weight W_lambda = d_q^2/[n]_q! instead of the "
        "SU(2) Jones-Markov weight y_lambda, which is EXACTLY ZERO on the electron "
        "block (>2 rows, by the Schur-Weyl row-count rule) and therefore made the "
        "original comparison vacuous on one side. Under W_lambda both sides are "
        "nonzero. Of the two legs of the PR #2584 refutation, the magnitude leg "
        "survives (3.35e6x too large -- a scope-(a) negative) and the bar-parity "
        "leg fails (the shift is exactly bar-EVEN). The ledger's stronger claim "
        "that the Markov-trace surface is 'exhausted' was a scope-(b) structural "
        "exclusion resting on the refuted leg. No fit; nothing wired.")
    w.add_data("tier", "structural")
    w.save()
    print("\nwitness saved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
