#!/usr/bin/env python3
"""qbeta_odd_parity_avatar_reduction_probe.py
=============================================

Odd-parity-extended generating-function avatar for the Q_β c_k ladder —
and the structural reduction it forces.

## Motivation (follows directly from the cosh-avatar NEGATIVE)

The companion probe `qbeta_cosh_avatar_crossanchor_multicoeff_probe.py`
(PR #1866, merged) closed the EVEN-parity slice of PR #1824's
generating-function hypothesis structurally: every cos/cosh avatar is
even in u, so its Taylor series has zero odd coefficients ⇒ predicted
c_3 = 0, while the cal-anchored c_3 ≈ -2.07 ≠ 0.

The obvious next move is an ODD-parity extension. This probe shows that,
once two hard constraints from the canonical ladder are imposed, the
odd-parity extension **reduces exactly to the already-saturated
single-formula c_3 search** — i.e. the generating-function reframing
does not open new search space for c_3.

## The reduction argument

The Q_β precision ladder is
    F(u) = Q_β(u)/Q_A = Π_{k≥2} (1 + c_k u^k),   u = b·ℏ_q²
so as a Taylor series at u = 0:
    F(u) = 1 + 0·u + c_2 u² + c_3 u³ + O(u⁴),
with TWO hard constraints:
    (C1) c_1 = 0   — the ladder starts at k = 2 (no u¹ term)
    (C2) c_2 = -1  — Lean-proved exact, q-independent, EVEN

Write any odd-extended avatar as
    F(u) = A(u) · G(u),
where A(u) is the even baseline (cos(√2·u): A = 1 - u² + O(u⁴), giving
c_2 = -1) and G(u) carries the odd content. The lowest odd term G can
contribute while preserving (C1) is u³ (a u¹ term in G would violate
c_1 = 0). So
    G(u) = 1 + g·u³ + O(u⁴),   and then   c_3 = g.

Therefore **c_3 equals a single scalar g**. For g to be a derived
(non-fitted) categorical quantity it must be a closed-form function of
the substrate scalars; and to be a genuine closure it must reproduce
the cal-anchored c_3 target at BOTH the proton and muon anchors. That
is *exactly* the single-formula c_3 search that the 28-candidate
bracket (PR #1860 + predecessors) has already saturated.

The odd-parity requirement does add one structural filter: g must be
ODD under the bar involution q ↔ q⁻¹ (the source of the u³ odd term),
i.e. built from bar-antisymmetric combinations like h = q - q⁻¹,
(qᵏ - q⁻ᵏ), etc. This probe confirms that the natural bar-antisymmetric
scalars all fall inside the saturated bracket (none reproduces the c_3
target at both anchors).

## What this probe does

1. Confirms the reduction numerically: builds F(u) = cos(√2·u)·(1 + g·u³)
   for a symbolic g, Taylor-extracts c_2, c_3, and verifies c_2 = -1
   (independent of g) and c_3 = g exactly.

2. Tests a curated set of **intrinsic-odd (bar-antisymmetric) g
   candidates** against the cal-anchored c_3 target at BOTH anchors:
       h, h³, h·(q+q⁻¹), (q³-q⁻³), (q³-q⁻³)/(q-q⁻¹)=[3]_q·(odd?), …
   Each is a closed form in the substrate scalars; no fits.

3. Verdict: do any reproduce c_3 at both anchors within 1 ppm?
   Expected NEGATIVE (these live inside the saturated bracket); the
   value is the STRUCTURAL conclusion, not the per-candidate numbers.

## No-fit discipline

No free parameters. Every g candidate is a closed form in
{h, q, [n]_q}; reading it at q_proton and q_muon and comparing to the
empirical c_3 target is falsifiable, not a fit. The reduction argument
is the deliverable; AGENTS.md forbids a seventh fit ansatz, and this
probe proposes none — it explains why the generating-function reframing
cannot evade the saturated search.

## References

- Cosh-avatar even-parity NEGATIVE: `qbeta_cosh_avatar_crossanchor_multicoeff_probe.py` (PR #1866)
- Single-formula saturation: `docs/audits/2026-06-04-three-paths-refuted-roadmap-update.md`
- c_3 target inversion: `qbeta_utils.c3_target_at` (PR #1831)
- Generating-function hypothesis: `docs/audits/2026-06-04-ck-generating-function-derivation-chain-scope.md` (PR #1824)
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

from collections.abc import Callable

# Path bootstrap: the single sys.path.insert above (line 89) exists ONLY to
# put the computations cluster root on the path so `_path_bridge` can be
# imported; `_path_bridge` then bridges every sibling subdir (qbeta/,
# substrate/, …), so `qbeta_utils` and the substrate modules resolve. No
# further manual inserts beyond that one bootstrap line (avoids
# import-order shadowing).
from mpmath import mp, mpf, cos, sqrt, fabs  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import q_at, q_muon_at  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from qbeta_utils import c3_target_at, substrate_ladder_quantities  # noqa: E402

TOL_PPM = 1.0  # 1 ppm both-anchor closure threshold


def taylor_c2_c3(F: Callable[[mpf], mpf], step: mpf = mpf("1e-7")) -> tuple[mpf, mpf]:
    """Return (c_2, c_3) of F at u=0 via central finite differences.

    c_2 = F''(0)/2!,  c_3 = F'''(0)/3!.  Central differences are
    even/odd-symmetric so the leading error is O(step²); at mp.dps=70
    with step 1e-7 this resolves c_2, c_3 to ample precision.
    """
    # 2nd derivative: F(h) - 2F(0) + F(-h) = F''(0)·h² + O(h⁴)
    f0 = F(mpf(0))
    fp1, fm1 = F(step), F(-step)
    fp2, fm2 = F(2 * step), F(-2 * step)
    d2 = (fp1 - 2 * f0 + fm1) / (step * step)
    # 3rd derivative (central): (F(2h) - 2F(h) + 2F(-h) - F(-2h)) / (2h³)
    d3 = (fp2 - 2 * fp1 + 2 * fm1 - fm2) / (2 * step ** 3)
    # c_2 = d2/2!, c_3 = d3/3! — divide by the constants directly (2, 6).
    return d2 / 2, d3 / 6


def make_g_candidates(q: mpf) -> dict[str, mpf]:
    """Curated closed-form g candidates for the odd-parity u³ content.

    The list is MIXED by design:
    - **bar-antisymmetric** entries (odd under q ↔ q⁻¹, e.g. h, h³,
      q³−q⁻³, …) — these can legitimately source an odd u³ term in a
      generating function whose even part is cos(√2·u);
    - two **bar-EVEN controls** (the constant `-2` and `-(q²+q⁻²)`) —
      included deliberately so the `is_bar_odd` filter flags them as
      ineligible odd-parity sources (they are the best single-formula
      near-matches, retained to show even the near-matches fail the
      cross-anchor test).

    The `is_bar_odd` column in the output marks which is which.
    """
    sub = substrate_ladder_quantities(q)
    h, b, hbar_q = sub["h"], sub["b"], sub["hbar_q"]
    qi = 1 / q
    return {
        "h = q-q⁻¹":               h,
        "h³":                      h ** 3,
        "h·(q+q⁻¹)":               h * (q + qi),
        "q³-q⁻³":                  q ** 3 - qi ** 3,
        "-(q³-q⁻³)":               -(q ** 3 - qi ** 3),
        "h·b":                     h * b,
        "h/ℏ_q²":                  h / hbar_q ** 2,
        "-2·h/(q-q⁻¹)=-2":         mpf(-2),          # bar-even control (should fail the odd filter)
        "-(q²+q⁻²)·h/(q-q⁻¹)":     -(q ** 2 + qi ** 2),  # = -(q²+q⁻²), the best 15-cand single
    }


def is_bar_odd(gq: mpf, gqi: mpf, tol: mpf | None = None) -> bool:
    """Heuristic: a g candidate is bar-ODD if g(1/q) ≈ -g(q).

    Takes the PRE-EVALUATED candidate values `gq = g(q)` and
    `gqi = g(1/q)` so callers do not rebuild the whole candidate dict
    per check (the loop precomputes both maps once).  The tolerance, if
    not supplied, is tied to the active mpmath precision rather than
    hardcoded."""
    if tol is None:
        tol = mpf(10) ** -(mp.dps - 5)
    return fabs(gq + gqi) < tol * (1 + fabs(gq))


def main() -> int:
    set_compute_dps()

    me = mpf(str(M_E_MEV))
    q_codata = mpf(str(Q_BETA_MEV))
    qp = q_at(mp.dps)
    qm = q_muon_at(mp.dps)

    c3_p = c3_target_at(qp, q_codata, me)
    c3_m = c3_target_at(qm, q_codata, me)

    print("=" * 78)
    print(" Q_β c_3 odd-parity avatar — reduction to the saturated single-formula search")
    print("=" * 78)
    print(f"  c_3 target: proton = {fmt(c3_p)[:22]}  muon = {fmt(c3_m)[:22]}")
    print(f"  swing = {fmt(fabs(c3_p - c3_m))[:18]}")
    print()

    # ── Step 1: confirm the reduction c_3 = g for F = cos(√2 u)·(1 + g u³) ──
    print("  Step 1 — reduction check: F(u) = cos(√2·u)·(1 + g·u³)")
    SQRT2 = sqrt(mpf(2))
    g_probe = mpf("-2.069342577115168")  # arbitrary test g

    def F(u, _g=g_probe):                  # even baseline · (1 + g·u³)
        return cos(SQRT2 * u) * (1 + _g * u ** 3)

    c2_ext, c3_ext = taylor_c2_c3(F)
    print(f"    with g = {float(g_probe):.6f}:  c_2 = {float(c2_ext):.8f} (target -1),  "
          f"c_3 = {float(c3_ext):.8f} (= g)")
    reduction_ok = (fabs(c2_ext + 1) < mpf("1e-6") and
                    fabs(c3_ext - g_probe) < mpf("1e-6"))
    print(f"    reduction c_2=-1 (indep of g) AND c_3=g: "
          f"{'CONFIRMED' if reduction_ok else 'FAILED'}")
    print()

    # ── Step 2: test bar-antisymmetric g candidates at both anchors ──
    print("  Step 2 — bar-antisymmetric g candidates vs c_3 target (both anchors)")
    print(f"  {'candidate':<26}{'bar-odd?':>9}{'g(q_p)':>14}{'p-miss ppm':>13}{'m-miss ppm':>13}")
    gp = make_g_candidates(qp)
    gm = make_g_candidates(qm)
    g_inv = make_g_candidates(1 / qp)   # precompute g(1/q) once for bar-oddness
    rows = []
    closures = []
    for name in gp.keys():
        vp, vm = gp[name], gm[name]
        bar_odd = is_bar_odd(vp, g_inv[name])
        pm = float(fabs(vp - c3_p) / fabs(c3_p) * 1e6)
        mm = float(fabs(vm - c3_m) / fabs(c3_m) * 1e6)
        closure = pm < TOL_PPM and mm < TOL_PPM
        print(f"  {name:<26}{('yes' if bar_odd else 'no'):>9}"
              f"{float(vp):>14.6f}{pm:>13.1f}{mm:>13.1f}"
              f"{'  CLOSURE' if closure else ''}")
        rows.append({
            "candidate": name, "bar_odd": bar_odd,
            "g_proton": fmt(vp), "g_muon": fmt(vm),
            "proton_miss_ppm": pm, "muon_miss_ppm": mm, "closure": closure,
        })
        if closure:
            closures.append(name)
    print()

    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    if closures:
        print(f"  POSITIVE — {len(closures)} bar-odd g reproduces c_3 at both anchors:")
        for n in closures:
            print(f"    • {n}")
        verdict = "POSITIVE_ODD_PARITY_G_FOUND"
    else:
        print("  NEGATIVE — no bar-antisymmetric g reproduces c_3 at both anchors")
        print(f"  within {TOL_PPM} ppm.")
        verdict = "NEGATIVE_ODD_PARITY_REDUCES_TO_SATURATED_SEARCH"
    print()
    print("  STRUCTURAL CONCLUSION.  Imposing the ladder's two hard constraints")
    print("  — c_1 = 0 (starts at k=2) and c_2 = -1 (proved, even) — forces the")
    print("  odd-parity content of any generating-function avatar into a single")
    print("  scalar g with c_3 = g (Step 1, confirmed).  A closure therefore")
    print("  requires a closed-form bar-antisymmetric g(q) matching the c_3")
    print("  target at both anchors — which is EXACTLY the single-formula c_3")
    print("  search already saturated by the 28-candidate bracket (PR #1860 +")
    print("  predecessors).  The generating-function reframing of PR #1824 does")
    print("  NOT open new search space for c_3: the even slice is structurally")
    print("  empty (cosh-avatar probe, PR #1866) and the odd slice reduces to")
    print("  the saturated single-formula search (this probe).  Productive")
    print("  directions remain the q-difference ODE (PR #1824 §3.b) — where the")
    print("  c_k are coupled by a recurrence rather than read off a single")
    print("  closed form — and GAP-A-3 / GAP-A-4 categorical work.")

    # ── Witness ──
    wb = WitnessBuilder(
        "qbeta-odd-parity-avatar-reduction-probe", engine="mpmath",
    )
    wb.set_description(
        "Odd-parity extension of the Q_β c_k generating-function avatar. "
        "Shows that the ladder constraints c_1=0 (starts at k=2) and "
        "c_2=-1 (proved, even) force the odd content into a single scalar "
        "g with c_3=g, so an odd-parity closure reduces EXACTLY to the "
        "already-saturated single-formula c_3 search. Confirms the "
        "reduction numerically (c_2=-1 indep of g; c_3=g) and tests "
        "bar-antisymmetric closed-form g candidates at both anchors "
        "(all NEGATIVE — inside the saturated bracket). Companion to the "
        "cosh-avatar even-parity NEGATIVE (PR #1866); together they close "
        "the generating-function reframing of c_3 as not opening new "
        "search space. No fits."
    )
    wb.set_content_block("conj:qbeta-precision-ladder")
    wb.add_data("c3_target_proton", fmt(c3_p))
    wb.add_data("c3_target_muon", fmt(c3_m))
    wb.add_data("reduction_c3_equals_g_confirmed", reduction_ok)
    wb.add_data("g_candidates", rows)
    wb.add_data("n_closures", len(closures))
    wb.add_data("verdict", verdict)
    wb.add_data("structural_conclusion", (
        "Ladder constraints c_1=0 + c_2=-1 (even) force the odd-parity "
        "avatar content into a single scalar g with c_3=g. Closure ⇒ a "
        "closed-form bar-antisymmetric g(q) matching c_3 at both anchors "
        "= the saturated single-formula search. Generating-function "
        "reframing opens no new c_3 search space: even slice empty "
        "(PR #1866), odd slice reduces to saturated search (this probe). "
        "Remaining: q-difference ODE (coupled recurrence, PR #1824 §3.b) "
        "+ GAP-A-3/A-4."
    ))
    # Real invariant: the reduction c_3 = g holds (Step 1).
    wb.add_assertion(
        "reduction_c3_equals_g",
        computed=1.0 if reduction_ok else 0.0,
        expected=1.0,
        source=("For F(u)=cos(√2·u)·(1+g·u³): c_2=-1 independent of g, and "
                "c_3=g exactly (the odd-parity content collapses to one scalar)."),
    )
    # Real invariant: cross-anchor c_3 swing is resolvable (test has power).
    wb.add_assertion(
        "cross_anchor_swing_resolvable",
        computed=1.0 if fabs(c3_p - c3_m) > mpf("1e-3") else 0.0,
        expected=1.0,
    )
    wb.save()
    print()
    print("  Witness: qbeta-odd-parity-avatar-reduction-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
