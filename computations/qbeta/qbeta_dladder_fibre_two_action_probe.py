#!/usr/bin/env python3
"""qbeta_dladder_fibre_two_action_probe.py

Accelerator prerequisite (companion to the fibre-branch Stokes-ambiguity probe):
IS the bar-odd Q_β D-ladder genuinely TWO-LEVEL (two distinct Borel actions -> a
non-commutative two-critical-time Écalle accelerator is needed AND is handed its two
times), or SINGLE-LEVEL (one action -> the accelerator is overkill and the swing is a
plain single Borel object)? This is THE structural gate on the whole Écalle program
(M2 of the merged Phi_b probe #3818 found two distinct divergence CLASSES
C_odd~0.052, C_even~0.115; my #3861 found the parity ORDERS soften toward a common
value at k=31 -- an unresolved tension).

The fibre-branch probe showed the fibre-resolved effective action A_eff(|u~|)=
-|u~|ln(delta_np) DRIFTS 0.38->0.23 across the transition band -- exactly what a SUM
of two Gevrey series with distinct actions A1,A2 produces (A_eff interpolates between
them as |u~| grows and the dominant level switches). This probe resolves that: it
splits the ladder by k-parity (the M2 split: odd k>=3 vs even k>=4) and measures EACH
half's OWN least-term action on the fibre, where N* sweeps the interior cleanly (on
the substrate both are pinned at the k=KMAX edge, unmeasurable). No Padé, no fit.

Decision:
  * two clean, DISTINCT per-parity action plateaus  => TWO-LEVEL confirmed; the two
    plateaus ARE the accelerator's critical-time actions (a concrete deliverable);
  * both drift to a COMMON value                    => single-level; accelerator not
    needed; the #3861 softening wins.

DISCIPLINE: scope-(a) structural measurement. No fit (nothing tuned to CODATA), no
c_k wired, nothing to production, no tier change. Reuses the exact Q(sqrt3) d_k.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import substrate_ladder_quantities  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

ORD = int(sys.argv[1]) if len(sys.argv) > 1 else 63
sys.argv = [sys.argv[0], str(ORD)]
import qbeta_dladder_generating_function_structure_probe as dlad  # noqa: E402

mp.mp.dps = 50


def to_mpf(v):
    return mp.mpf(str(sp.N(v, 46)))


def least_term_action(coeffs, u_tilde, kmin, kmax):
    """optimal-truncation least term of the sub-series {k: c_k u~^k}; return
    (N*, delta, A_eff=-|u~|ln delta) with A_eff only when N* is interior."""
    terms = {k: coeffs[k] * u_tilde ** k for k in coeffs}
    Nstar = min(terms, key=lambda k: abs(terms[k]))
    delta = abs(terms[Nstar])
    interior = (kmin < Nstar < kmax)
    A = (-abs(u_tilde) * mp.log(delta)) if (interior and delta > 0) else None
    return Nstar, delta, A, interior


def plateau(vals):
    """mid + fractional spread of a list of A_eff samples."""
    if len(vals) < 2:
        return (vals[0] if vals else mp.mpf("nan")), mp.mpf("nan")
    lo, hi = min(vals), max(vals)
    mid = (lo + hi) / 2
    return mid, ((hi - lo) / mid if mid != 0 else mp.inf)


def main() -> int:
    print(f"building exact D-ladder at ORD={ORD} ...", flush=True)
    dk_sym, KMAX, valid_top, odd_ok = dlad.build_d_ladder()
    dk = {k: to_mpf(dk_sym[k]) for k in dk_sym if k >= 1}
    KMAX = max(dk)
    odd = {k: dk[k] for k in dk if k % 2 == 1 and k >= 3}
    even = {k: dk[k] for k in dk if k % 2 == 0 and k >= 4}
    kmin_odd, kmax_odd = min(odd), max(odd)
    kmin_even, kmax_even = min(even), max(even)
    print(f"  KMAX={KMAX}  odd_ok={odd_ok}  |odd|={len(odd)} (k={kmin_odd}..{kmax_odd})  "
          f"|even|={len(even)} (k={kmin_even}..{kmax_even})", flush=True)

    q0 = q_at(50)
    b = substrate_ladder_quantities(q0)["u"] / (1 - 1 / q0) ** 2

    def theta_of_absu(x):
        return 2 * mp.asin(mp.sqrt(x / (4 * b)))

    # scan the transition band on the fibre where each parity's N* is interior
    xs = [mp.mpf("0.08") + mp.mpf("0.004") * j for j in range(60)]   # 0.08..0.316
    print("\n  |u~|   N*_odd  A_odd        N*_even  A_even", flush=True)
    A_odd_samples, A_even_samples = [], []
    rows = []
    for x in xs:
        th = theta_of_absu(x)
        q = mp.e ** (1j * th)
        u_tilde = q * b * (1 - 1 / q) ** 2
        No, do_, Ao, io = least_term_action(odd, u_tilde, kmin_odd, kmax_odd)
        Ne, de_, Ae, ie = least_term_action(even, u_tilde, kmin_even, kmax_even)
        if Ao is not None:
            A_odd_samples.append(Ao)
        if Ae is not None:
            A_even_samples.append(Ae)
        rows.append({"abs_u": mp.nstr(x, 6), "Nstar_odd": No, "A_odd": (mp.nstr(Ao, 6) if Ao else "-"),
                     "Nstar_even": Ne, "A_even": (mp.nstr(Ae, 6) if Ae else "-")})
        if io or ie:
            print(f"  {mp.nstr(x,5):>7}  {No:>4}  {mp.nstr(Ao,6) if Ao else '   -   ':>10}   "
                  f"{Ne:>4}   {mp.nstr(Ae,6) if Ae else '   -   ':>10}", flush=True)

    A_odd_mid, A_odd_spread = plateau(A_odd_samples)
    A_even_mid, A_even_spread = plateau(A_even_samples)
    print(f"\n  odd  action plateau: mid={mp.nstr(A_odd_mid,6)}  frac.spread="
          f"{mp.nstr(A_odd_spread,4)}  (n={len(A_odd_samples)})", flush=True)
    print(f"  even action plateau: mid={mp.nstr(A_even_mid,6)}  frac.spread="
          f"{mp.nstr(A_even_spread,4)}  (n={len(A_even_samples)})", flush=True)

    # distinctness: the two plateaus separated by more than their spreads?
    have_both = (not mp.isnan(A_odd_mid)) and (not mp.isnan(A_even_mid))
    sep = abs(A_odd_mid - A_even_mid) if have_both else mp.mpf("nan")
    rel_sep = (sep / ((A_odd_mid + A_even_mid) / 2)) if have_both else mp.mpf("nan")
    both_flat = have_both and (A_odd_spread < mp.mpf("0.20")) and (A_even_spread < mp.mpf("0.20"))
    distinct = have_both and (rel_sep > mp.mpf("0.15")) and \
        (sep > (A_odd_spread * A_odd_mid + A_even_spread * A_even_mid))
    two_level = bool(both_flat and distinct)
    print(f"\n  |A_odd - A_even| = {mp.nstr(sep,6)}  (rel {mp.nstr(rel_sep,4)})  "
          f"both_flat={both_flat}  distinct={distinct}", flush=True)

    verdict = (
        f"FIBRE PER-PARITY ACTION TEST (accelerator prerequisite; scope-(a)). Splitting "
        f"the D-ladder by k-parity (M2 split) and measuring each half's own least-term "
        f"action on the fibre (interior N*, no Padé): "
        f"odd-half action mid={mp.nstr(A_odd_mid,5)} (spread {mp.nstr(A_odd_spread,3)}, "
        f"n={len(A_odd_samples)}); even-half action mid={mp.nstr(A_even_mid,5)} (spread "
        f"{mp.nstr(A_even_spread,3)}, n={len(A_even_samples)}); separation "
        f"|A_odd-A_even|={mp.nstr(sep,5)} (rel {mp.nstr(rel_sep,3)}). "
        + (
            f"BOTH plateaus are flat AND distinct => TWO-LEVEL CONFIRMED: the D-ladder is a "
            f"sum of two Gevrey series with DISTINCT Borel actions, so the non-commutative "
            f"two-critical-time Écalle accelerator IS the required tool, and these two "
            f"actions ARE its critical times. This resolves the M2-vs-#3861 tension toward "
            f"two-level and hands the accelerator its inputs."
            if two_level else
            f"the plateaus are NOT cleanly flat-and-distinct at k<=31 "
            f"({'both flat but not separated -> single-level leaning (accelerator may be overkill; #3861 softening)' if both_flat and not distinct else 'per-parity actions still drifting -> the two-level inputs are NOT resolvable at k=31 (a legitimate negative: the accelerator cannot be fed clean critical times from this length; more exact rungs or a genuine transseries fit is required)'}). "
            f"Honest: does NOT confirm two clean actions; records what k=31 can and cannot support."
        )
        + " Caveat: interior N* is modest, so optimal-truncation asymptotics are coarse. "
        "No fit; no c_k wired; nothing to production; no tier change."
    )
    print("\nVERDICT:", verdict, flush=True)

    wb = WitnessBuilder("qbeta-dladder-fibre-two-action", engine="mpmath")
    wb.set_description(
        "Accelerator prerequisite: split the D-ladder by k-parity and measure each "
        "half's own fibre least-term action to decide two-level (distinct actions, "
        "accelerator needed + fed) vs single-level (common action).")
    wb.set_audit_only("docs/audits/2026-07-18-dladder-fibre-two-action.md")
    wb.add_assertion("d_ladder_exact_odd_ok", str(bool(odd_ok)), "True")
    wb.add_assertion("both_parities_have_interior_samples", str(have_both), "True")
    wb.add_data("A_odd_mid", mp.nstr(A_odd_mid, 12) if not mp.isnan(A_odd_mid) else "nan")
    wb.add_data("A_odd_frac_spread", mp.nstr(A_odd_spread, 8) if not mp.isnan(A_odd_spread) else "nan")
    wb.add_data("A_even_mid", mp.nstr(A_even_mid, 12) if not mp.isnan(A_even_mid) else "nan")
    wb.add_data("A_even_frac_spread", mp.nstr(A_even_spread, 8) if not mp.isnan(A_even_spread) else "nan")
    wb.add_data("separation_abs", mp.nstr(sep, 12) if not mp.isnan(sep) else "nan")
    wb.add_data("separation_rel", mp.nstr(rel_sep, 8) if not mp.isnan(rel_sep) else "nan")
    wb.add_data("both_flat", bool(both_flat))
    wb.add_data("distinct", bool(distinct))
    wb.add_data("two_level_confirmed", two_level)
    wb.add_data("rows", rows)
    wb.add_data("verdict", verdict)
    wb.save()
    return 0 if odd_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
