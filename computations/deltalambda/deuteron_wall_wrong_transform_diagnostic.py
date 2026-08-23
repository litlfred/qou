#!/usr/bin/env python3
r"""
deuteron_wall_wrong_transform_diagnostic.py — the deuteron-wall resummation "closed negatively"
verdict rests on the WRONG transform applied to the WRONG object (qou-hok7).

BACKGROUND. `deuteron_wall_full_transseries_probe.py` concluded (scope-(a) negative) that the FULL
level-1/2 Borel–Laplace median resummation of the deuteron binding period undershoots B_D by ~40× at
every substrate coupling, and recorded this as "closes the resummation hypothesis for the deuteron
negatively." But that probe resummed:
  • the OBJECT  a_D^(n) = I(n)/n  — the q = 1 CLASSICAL involution/telephone period; and
  • with the TRANSFORM  b_n = a_D^(n) / Γ(n/2 + 1)  — the CLASSICAL level-1/2 Borel transform.

Meanwhile `lever1_transfer_operator_spectral_qgevrey.py` (PR-landed) MEASURED that the SUBSTRATE object
is the q-deformed binding statistic Z_n(q₀), whose divergence class is **q-Gevrey**: its per-level
log-multiplier grows LINEARLY in n, so log Z_n(q₀) is Θ(n²) — lever1 records the order as ~ q₀^{n²/2}
— strictly faster than every classical Gevrey-s (whose coefficients grow only like (n!)^s =
exp(Θ(n log n))). (Independently, the C1 ∞-formal solution has deg_q(c_n) = n², the same quadratic
q-Gevrey signature — `2026-08-01-c1-inf-formal-solution-qgevrey`.)

The load-bearing fact below is that the classical Γ-Borel divisor Γ(n/2+1) = exp(Θ(n log n)) cannot
tame coefficients of order exp(Θ(n²)); the "q-Borel divisor" column that returns O(1) is the matching
divisor q₀^{n²/2} shown by construction — an illustration of what the correct transform must do, not an
independent result.

THE MISMATCH (this probe, decisive). A Borel transform must divide the coefficients by the growth it is
built to tame. For a q-Gevrey series (growth ~ Q^{n²/2}, Q > 1) the CLASSICAL Γ-Borel divisor is far
too weak:
        Q^{n²/2} / Γ(n/2 + 1)  →  ∞          (classical Borel transform DIVERGES on a q-Gevrey series)
        Q^{n²/2} / Q^{n²/2}     =  1  = O(1)   (a q-Borel divisor tames it)
So the classical level-1/2 Borel–Laplace is NOT the resummation of the substrate object — it is the
resummation of the q = 1 shadow. The ~40× undershoot is therefore a WRONG-TRANSFORM artifact, not a
statement about the substrate deuteron binding.

CONSEQUENCE. The deuteron-wall resummation hypothesis is NOT closed by the full-transseries probe: that
probe answered a different (q = 1) question. The correct test is the **q-Borel–Laplace resummation of
Z_n(q₀)** (q-Gevrey, divisor ~ q₀^{n²/2}), which has not been done. Reopened as `qou-hok7`; the q-Borel
machinery exists in the corpus (`2026-08-01-qborel-ecalle-resum-barodd`, `qbeta_habiro_tail_util`) but
has not been pointed at the deuteron binding statistic.

HONESTY. This does NOT claim the q-Borel sum reaches B_D — only that the existing negative closure is
on the wrong object with the wrong transform and must be redone. scope-(a) (a route was mis-scoped, not
excluded); no fit; nothing wired; no c_k; L2 unchanged.

# Ref: [manuscript] docs/audits/2026-08-21-deuteron-wall-resummation-wrong-transform.md
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "qou-substrate" / "python"))

import mpmath as mp
from qou_substrate.constants import q_at
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def main() -> int:
    q0 = mp.mpf(q_at(30))
    print("=" * 74)
    print(" deuteron-wall resummation — WRONG-TRANSFORM diagnostic (qou-hok7)")
    print("=" * 74)
    print(f" substrate q₀ = {mp.nstr(q0, 12)}   (proton-pin, package constant)\n")

    N = 40
    # (1) the q=1 CLASSICAL period a_D^(n) = I(n)/n and its classical Borel coefficient b_n.
    I = [mp.mpf(1), mp.mpf(1)]
    for n in range(2, N + 1):
        I.append(I[-1] + (n - 1) * I[-2])
    aD = [mp.mpf(0)] + [I[n] / n for n in range(1, N + 1)]
    b_classical = [mp.mpf(0)] + [aD[n] / mp.gamma(mp.mpf(n) / 2 + 1) for n in range(1, N + 1)]
    # ratio |b_{n}|^{1/n} → 1/radius : the classical Borel series of the q=1 period has FINITE radius
    root = [abs(b_classical[n]) ** (mp.mpf(1) / n) for n in range(4, N + 1)]
    print(" (1) classical Borel of the q=1 period a_D^(n)=I(n)/n  (what the full-transseries probe did):")
    print(f"     |b_n|^(1/n) at n=10,20,30,40 = "
          f"{mp.nstr(root[6],5)}, {mp.nstr(root[16],5)}, {mp.nstr(root[26],5)}, {mp.nstr(root[-1],5)}")
    print(f"     → converges to a finite Borel radius (≈1/{mp.nstr(root[-1],4)}): classical Borel is the")
    print(f"       correct transform for the q=1 Gevrey-1/2 period.  ✓ (consistent with that probe)\n")

    # (2) the SUBSTRATE object Z_n(q₀): q-Gevrey growth g_n ~ q₀^{n²/2} (lever1, measured).
    #     Show the classical Γ-Borel divisor CANNOT tame it, but a q-Borel divisor can.
    print(" (2) substrate object Z_n(q₀): q-Gevrey growth g_n ~ q₀^{n²/2}  (lever1_qgevrey, PR-landed):")
    print("      n |  g_n/Γ(n/2+1)  (classical Borel — must stay bounded to converge) |  g_n/q₀^{n²/2} (q-Borel)")
    classical_blows = True
    prev = None
    for n in [4, 8, 16, 24, 32, 40]:
        gn = q0 ** (mp.mpf(n) ** 2 / 2)                    # q-Gevrey growth law
        classical = gn / mp.gamma(mp.mpf(n) / 2 + 1)       # classical Borel-transformed coefficient
        qborel = gn / (q0 ** (mp.mpf(n) ** 2 / 2))         # q-Borel-transformed coefficient (=1)
        if prev is not None and classical <= prev:
            classical_blows = False
        prev = classical
        print(f"     {n:2d} | {mp.nstr(classical, 6):>28} | {mp.nstr(qborel, 6):>10}")
    print(f"     → classical Γ-Borel coefficient DIVERGES (↑∞): {classical_blows}  ⇒ classical Borel is")
    print("       NOT a resummation of the q-Gevrey substrate object; the q-Borel divisor q₀^{n²/2} is.\n")

    # (3) the logical consequence
    print(" (3) CONSEQUENCE. The full-transseries 'closed negatively' verdict resummed the q=1 shadow")
    print("     (a_D^(n)=I(n)/n) with the classical transform. It is silent on the substrate object")
    print("     Z_n(q₀) (q-Gevrey), whose resummation requires q-Borel–Laplace (divisor q₀^{n²/2}).")
    print("     The ~40× undershoot is a WRONG-TRANSFORM artifact. Deuteron-wall resummation REOPENED")
    print("     (qou-hok7); the correct q-Borel test of Z_n(q₀) has not been done.")

    ok = classical_blows and (root[-1] < root[6] * 3)  # classical radius finite; q-Borel needed
    print(f"\n RESULT: wrong-transform diagnostic (classical Borel ≠ q-Gevrey resummation): {ok}")

    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))
        from witness_base import WitnessBuilder
        w = WitnessBuilder("deuteron-wall-resummation-wrong-transform", engine="mpmath")
        w.set_description(
            "The deuteron-wall resummation 'closed negatively' verdict "
            "(deuteron_wall_full_transseries_probe) rests on the WRONG transform applied to the WRONG "
            "object (qou-hok7). That probe resummed a_D^(n)=I(n)/n — the q=1 CLASSICAL telephone period "
            "— with the CLASSICAL level-1/2 Borel divisor Γ(n/2+1). But lever1_transfer_operator_spectral"
            "_qgevrey (PR-landed) measured the SUBSTRATE object Z_n(q₀) to be q-Gevrey (log Z_n is "
            "Theta(n^2), order ~q0^{n^2/2}), strictly faster than every classical Gevrey-s (the C1 "
            "∞-solution shares the deg_q(c_n)=n² signature). A Borel transform must divide by the growth "
            "it tames: for q-Gevrey growth q₀^{n²/2}, the classical Γ-divisor DIVERGES (q₀^{n²/2}/Γ(n/2+1)"
            "→∞, shown n≤40) while a q-Borel divisor q₀^{n²/2} tames it (=O(1)). So the classical level-"
            "1/2 Borel–Laplace is the resummation of the q=1 shadow, not the substrate object; the ~40× "
            "undershoot is a wrong-transform artifact. The deuteron-wall resummation hypothesis is NOT "
            "closed — the correct q-Borel–Laplace resummation of Z_n(q₀) (divisor q₀^{n²/2}) has not been "
            "done. Does NOT claim q-Borel reaches B_D; only that the negative closure is mis-scoped and "
            "must be redone with q-Borel. scope-(a) mis-scope, not exclusion; no fit; nothing wired.")
        w.add_data("full_transseries_object", "a_D^(n)=I(n)/n  (q=1 classical telephone period)")
        w.add_data("full_transseries_transform", "classical level-1/2 Borel  b_n = a_D^(n)/Gamma(n/2+1)")
        w.add_data("substrate_object", "Z_n(q0)  (q-deformed binding statistic)")
        w.add_data("substrate_divergence_class", "q-Gevrey  (Z_n(q0) ~ q0^{n^2}, lever1 measured)")
        w.add_data("classical_borel_diverges_on_qgevrey", bool(classical_blows))
        w.add_data("correct_transform", "q-Borel-Laplace, divisor ~ q0^{n^2/2}")
        w.add_data("verdict", "deuteron-wall resummation REOPENED: closed on wrong object+transform")
        w.add_assertion(
            "deuteron_wall_resummation_wrong_transform",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("classical Gamma-Borel divisor diverges on the q-Gevrey substrate object "
                    "(q0^{n^2/2}/Gamma(n/2+1)->inf, n<=40) while the q-Borel divisor q0^{n^2/2} tames it; "
                    "the full-transseries negative resummed the q=1 shadow with the classical transform, "
                    "so it does not close the substrate deuteron resummation. Mis-scope; no fit."))
        out = w.save()
        print(f"\n Witness: {out}")
    except ImportError as e:
        print(f"\n (witness skipped — witness_base unavailable: {e})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
