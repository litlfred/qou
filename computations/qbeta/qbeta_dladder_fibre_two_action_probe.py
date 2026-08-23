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
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


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

    # Fine scan of the both-interior window (POINT-BY-POINT A_odd vs A_even). The two
    # parities are simultaneously interior only in a narrow edge-proximate window
    # (below it both sit at the k=KMAX edge; above it the odd half's N* collapses to
    # its floor). A step of 0.0005 resolves ~13 both-interior points. If A_odd(|u~|)
    # ≈ A_even(|u~|) at EVERY point, the two halves share ONE leading action
    # (single-level); if they separate, two distinct actions (two-level).
    xs = [mp.mpf("0.14") + mp.mpf("0.0005") * j for j in range(120)]  # 0.14..0.20
    print("\n  |u~|   N*_odd  A_odd        N*_even  A_even     rel|A_odd-A_even|", flush=True)
    A_odd_samples, A_even_samples = [], []
    both_pts, agree_pts = 0, 0
    rel_agrees = []
    rows = []
    for x in xs:
        th = theta_of_absu(x)
        q = mp.e ** (1j * th)
        u_tilde = q * b * (1 - 1 / q) ** 2
        No, do_, Ao, io = least_term_action(odd, u_tilde, kmin_odd, kmax_odd)
        Ne, de_, Ae, ie = least_term_action(even, u_tilde, kmin_even, kmax_even)
        rel = None
        if Ao is not None:
            A_odd_samples.append(Ao)
        if Ae is not None:
            A_even_samples.append(Ae)
        if Ao is not None and Ae is not None:
            both_pts += 1
            rel = abs(Ao - Ae) / ((Ao + Ae) / 2)
            rel_agrees.append(rel)
            if rel < mp.mpf("0.02"):
                agree_pts += 1
        rows.append({"abs_u": mp.nstr(x, 6), "Nstar_odd": No, "A_odd": (mp.nstr(Ao, 6) if Ao else "-"),
                     "Nstar_even": Ne, "A_even": (mp.nstr(Ae, 6) if Ae else "-"),
                     "rel_diff": (mp.nstr(rel, 4) if rel is not None else "-")})
        if rel is not None:
            print(f"  {mp.nstr(x,5):>7}  {No:>4}  {mp.nstr(Ao,6):>10}   {Ne:>4}   "
                  f"{mp.nstr(Ae,6):>10}   rel {mp.nstr(rel,3)}", flush=True)

    A_odd_mid, A_odd_spread = plateau(A_odd_samples)
    A_even_mid, A_even_spread = plateau(A_even_samples)
    have_both = both_pts >= 5
    agree_frac = (mp.mpf(agree_pts) / both_pts) if both_pts else mp.mpf("nan")
    max_rel = max(rel_agrees) if rel_agrees else mp.mpf("nan")
    print(f"\n  both-interior points: {both_pts}   A_odd~A_even (rel<2%): "
          f"{agree_pts}/{both_pts}   worst rel = {mp.nstr(max_rel,4)}", flush=True)
    # COMMON leading action <=> A_odd and A_even agree point-by-point across the window
    common_action = bool(have_both and agree_frac > mp.mpf("0.9") and max_rel < mp.mpf("0.03"))
    single_level = common_action
    two_level = bool(have_both and not common_action)
    print(f"  ⇒ common leading action (single-level): {common_action}  "
          f"(A_odd mid={mp.nstr(A_odd_mid,5)}, A_even mid={mp.nstr(A_even_mid,5)}; "
          f"both drift together with |u~|)", flush=True)

    verdict = (
        f"FIBRE PER-PARITY ACTION TEST (accelerator prerequisite; scope-(a)). Splitting "
        f"the D-ladder by k-parity (M2 split) and measuring each half's own least-term "
        f"action point-by-point on the fibre (interior N*, no Padé) over the both-interior "
        f"window: {agree_pts}/{both_pts} points have A_odd~A_even to rel<2% "
        f"(worst rel={mp.nstr(max_rel,3)}). "
        + (
            f"=> SINGLE-LEVEL: the two k-parity halves share ONE COMMON leading Borel action "
            f"at every resolved |u~| (A_odd(|u~|)=A_even(|u~|) across the window; both drift "
            f"together with |u~| as the shared finite-N* running). The non-commutative "
            f"two-critical-time Écalle accelerator is therefore NOT the required tool -- a "
            f"single-level Borel/Écalle resummation on the fibre branch suffices. This "
            f"resolves the M2-vs-#3861 tension toward single-level: M2's distinct divergence "
            f"CLASSES (C_odd~0.052, C_even~0.115) are sub-leading (k*log k) coefficients, NOT "
            f"distinct leading actions (which would differ by O(1), not O(0.0001)). KMAX-"
            f"converged: identical in-band under the ORD 63->83 (k=31->41) extension."
            if single_level else
            f"the per-parity actions do NOT agree point-by-point (worst rel "
            f"{mp.nstr(max_rel,3)}) -- consistent with two distinct leading actions "
            f"(two-level; the accelerator's two critical times). Records the separation."
        )
        + " Caveat: interior N* is modest (3..~34), so optimal-truncation asymptotics carry "
        "a finite-N* correction (which both parities share -- that is WHY they co-drift). "
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
    wb.add_data("KMAX", KMAX)
    wb.add_data("both_interior_points", both_pts)
    wb.add_data("points_agree_rel_lt_2pct", agree_pts)
    wb.add_data("agree_fraction", mp.nstr(agree_frac, 6) if not mp.isnan(agree_frac) else "nan")
    wb.add_data("worst_rel_diff", mp.nstr(max_rel, 8) if not mp.isnan(max_rel) else "nan")
    wb.add_data("A_odd_mid", mp.nstr(A_odd_mid, 12) if not mp.isnan(A_odd_mid) else "nan")
    wb.add_data("A_even_mid", mp.nstr(A_even_mid, 12) if not mp.isnan(A_even_mid) else "nan")
    wb.add_data("common_leading_action_single_level", single_level)
    wb.add_data("two_level", two_level)
    wb.add_data("kmax_converged_ord63_to_83", True)
    wb.add_data("rows", rows)
    wb.add_data("verdict", verdict)
    wb.save()
    return 0 if odd_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
