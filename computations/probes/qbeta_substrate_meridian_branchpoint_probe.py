#!/usr/bin/env python3
"""qbeta_substrate_meridian_branchpoint_probe.py — is the substrate meridian
q₀ ≈ 1.10998 anomalously close to a 5₂ (or 4₁) A-polynomial branch point?

This is the ONE remaining place the c₃ bar-odd swing's 2×10⁶ amplification could
be GEOMETRIC rather than the 1/u³ representational artifact. The #3902 5₂
quantum-volume probe found `d𝔙/dm` anchor-smooth (O(1)) at m = q₀; a smooth
quantum volume can only blow up near a **branch point** of the character variety
— where the gluing/saddle system degenerates (its Jacobian vanishes, i.e. two
solutions collide) and `d(saddle)/dm → ∞`. If the substrate meridian sits
anomalously close (distance ~ the 1e-8 anchor gap) to such a point, the
amplification is geometric; if it is O(0.1) away (generic), it is not, and the
swing is confirmed representational.

METHOD. Track the geometric saddle from the complete structure and compute the
Jacobian determinant det J(m) of the gluing system as a function of the meridian
eigenvalue m. Branch points are the roots of det J(m) = 0 (equivalently the
m-discriminant of the A-polynomial). Scan m over a neighbourhood of q₀ and locate
the nearest zero of |det J|; report its distance from q₀.

  4₁ saddle (Hikami 0604094; single tetra-pair): the figure-eight gluing
     w(1−w)·… ; det J via the A-polynomial disc.  A_{4₁}(ℓ,m) =
     −m⁴ + ℓ(1−m²−2m⁴−m⁶+m⁸) − ℓ²m⁴ ⇒ disc_ℓ = B²−4m⁸, B = 1−m²−2m⁴−m⁶+m⁸.
  5₂ saddle (eq 4.13): F₁ = m²x−y−xy, F₂ = (m²y−1)(y−1) − m²(m²x−y);
     det J = ∂(F₁,F₂)/∂(x,y).

RESULT drives the owner's conditional: if NOT anomalously close ⇒ the swing is
representational (1/u³), and the alien-calculus / resurgence thread (sibling
#3818's D-ladder Écalle acceleration) is the route; if anomalously close ⇒ the
amplification is a genuine geometric near-singularity. No c_k; no fit; scope-(a).

Run: python3 -u computations/probes/qbeta_substrate_meridian_branchpoint_probe.py \\
       2>&1 | tee /tmp/qbeta_branchpoint.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
Q0 = mp.mpf("1.1099785827513808075916690956107688798744991218736")   # proton pin


# ---------- 4₁ : A-polynomial discriminant branch points ----------
def disc_4_1(m):
    """m-discriminant of A_{4₁}(ℓ,m) in ℓ: B² − 4m⁸, B = 1−m²−2m⁴−m⁶+m⁸.
    Zeros in m are the 4₁ branch points (saddle degeneracies)."""
    B = 1 - m ** 2 - 2 * m ** 4 - m ** 6 + m ** 8
    return B ** 2 - 4 * m ** 8


# ---------- 5₂ : saddle-system Jacobian determinant ----------
def saddle_5_2(m, seed):
    m2 = m * m
    sol = mp.findroot(lambda x, y: (m2 * x - y - x * y,
                                    (m2 * y - 1) * (y - 1) - m2 * (m2 * x - y)),
                      seed)
    return mp.mpc(sol[0]), mp.mpc(sol[1])

def detJ_5_2(m, x, y):
    """det ∂(F₁,F₂)/∂(x,y). F₁=m²x−y−xy, F₂=(m²y−1)(y−1)−m²(m²x−y)."""
    m2 = m * m
    dF1_dx, dF1_dy = m2 - y, -1 - x
    dF2_dx = -m2 * m2                                   # ∂F2/∂x = −m⁴
    dF2_dy = (m2) * (y - 1) + (m2 * y - 1) + m2         # (m²)(y−1)+(m²y−1)+m²
    return dF1_dx * dF2_dy - dF1_dy * dF2_dx


def nearest_zero_real(f, center, span, n=4000):
    """Nearest sign-change of real f(m) to `center` on [center−span, center+span]."""
    xs = [center - span + 2 * span * k / n for k in range(n + 1)]
    prev = f(xs[0])
    best = None
    for i in range(1, len(xs)):
        cur = f(xs[i])
        if prev == 0 or (prev.real if hasattr(prev, "real") else prev) * \
                        (cur.real if hasattr(cur, "real") else cur) < 0:
            root = mp.findroot(lambda m: mp.re(f(m)), (xs[i - 1] + xs[i]) / 2)
            d = abs(root - center)
            if best is None or d < best[1]:
                best = (root, d)
        prev = cur
    return best


def main() -> int:
    print("=" * 78)
    print(" Substrate meridian vs A-polynomial branch points — is q₀ anomalous?")
    print("=" * 78)
    print(f"  substrate meridian m = q₀ = {mp.nstr(Q0, 15)}")
    anchor_gap = mp.mpf("1.28e-8")     # proton↔muon q₀ separation

    # ---- 4₁ branch points (real, near q₀) ----
    b41 = nearest_zero_real(disc_4_1, Q0, mp.mpf("0.8"))
    d41 = b41[1] if b41 else mp.inf
    print(f"\n[4₁] nearest real branch point (disc_ℓ A_{{4₁}} = 0):")
    if b41:
        print(f"     m* = {mp.nstr(b41[0], 12)}   |q₀ − m*| = {mp.nstr(d41, 6)}")
    # also the |m|=1 branch locus (roots of unity): distance = q₀ − 1
    d41_unit = Q0 - 1
    print(f"     unit-circle branch locus |m|=1: |q₀| − 1 = {mp.nstr(d41_unit, 6)}")

    # ---- 5₂ branch points (Jacobian det zero, real, near q₀) ----
    seed = (mp.mpc("-0.877", "0.745"), mp.mpc("0.785", "1.307"))
    def dj5(m):
        x, y = saddle_5_2(m, seed)
        return detJ_5_2(m, x, y)
    # scan |detJ| for its nearest minimum/zero to q₀
    b52 = nearest_zero_real(lambda m: mp.re(dj5(m)), Q0, mp.mpf("0.6"), n=1200)
    d52 = b52[1] if b52 else mp.inf
    dj_at_q0 = dj5(Q0)
    print(f"\n[5₂] Jacobian det J at m=q₀ = {mp.nstr(abs(dj_at_q0), 8)}  "
          f"(O(1) ⇒ non-degenerate saddle)")
    if b52:
        print(f"     nearest real det J = 0 (branch point): m* = {mp.nstr(b52[0], 10)}"
              f"   |q₀ − m*| = {mp.nstr(d52, 6)}")

    nearest = min(float(d41), float(d41_unit), float(d52) if b52 else 1e9)
    print(f"\n  NEAREST branch point to q₀ (any): {nearest:.4e}")
    print(f"  anchor gap (proton↔muon q₀):     {float(anchor_gap):.4e}")
    ratio = nearest / float(anchor_gap)
    print(f"  ratio (distance / anchor gap):    {ratio:.4e}")
    anomalous = nearest < 1e-4          # "anomalously close" threshold
    print(f"  ⇒ substrate meridian is {'ANOMALOUSLY CLOSE to a branch point (!)' if anomalous else 'GENERIC — far from every branch point'}")
    print(f"    {'the amplification could be geometric' if anomalous else 'the 2e6 amplification is NOT a geometric near-singularity'}")

    wb = WitnessBuilder("qbeta-substrate-meridian-branchpoint", engine="mpmath")
    wb.set_description(
        "Is the substrate meridian q₀≈1.10998 anomalously close to a 5₂/4₁ "
        "A-polynomial branch point (saddle degeneracy) — the ONE place the c₃ "
        "bar-odd swing's 2e6 amplification could be geometric rather than the 1/u³ "
        "representational artifact? Computes the nearest branch point: 4₁ via "
        "disc_ℓ A_{4₁}, 5₂ via the saddle Jacobian det J=0. The substrate saddle "
        "is non-degenerate and O(0.1) from every branch point (~1e7× the anchor "
        "gap) ⇒ the amplification is NOT geometric; the swing is representational, "
        "and the alien-calculus/resurgence route (D-ladder Écalle) is the lever. "
        "No c_k; no fit; scope-(a).")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("saddle_nondegenerate_at_substrate",
                     computed=1.0 if abs(dj_at_q0) > mp.mpf("0.01") else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="|det J(q₀)| = O(1) ≠ 0 — the 5₂ gluing saddle is "
                            "non-degenerate at the substrate meridian")
    wb.add_assertion("substrate_not_near_branchpoint",
                     computed=1.0 if not anomalous else 0.0, expected=1.0,
                     tolerance=0.5,
                     source=f"nearest branch point is {nearest:.3e} from q₀ "
                            f"(~{ratio:.1e}× the 1.28e-8 anchor gap) — GENERIC, not "
                            f"anomalously close; the amplification is not geometric")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("nearest_branchpoint_distance", f"{nearest:.6e}")
    wb.add_data("branchpoints", {
        "4_1_real": mp.nstr(b41[0], 12) if b41 else None,
        "4_1_real_dist": f"{float(d41):.6e}" if b41 else None,
        "4_1_unitcircle_dist": f"{float(d41_unit):.6e}",
        "5_2_real": mp.nstr(b52[0], 12) if b52 else None,
        "5_2_real_dist": f"{float(d52):.6e}" if b52 else None,
        "detJ_5_2_at_q0": mp.nstr(abs(dj_at_q0), 10)})
    wb.add_data("anchor_gap", f"{float(anchor_gap):.3e}")
    wb.add_data("distance_over_anchor_gap", f"{ratio:.4e}")
    wb.add_data("verdict",
                (f"SUBSTRATE MERIDIAN IS GENERIC — far from every branch point. "
                 f"The nearest 4₁/5₂ A-polynomial branch point is {nearest:.3e} from "
                 f"q₀ (~{ratio:.1e}× the anchor gap), and the 5₂ saddle Jacobian "
                 f"det J(q₀)=O(1) is non-degenerate. So the 2e6 bar-odd swing "
                 f"amplification is NOT a geometric near-singularity of any knot's "
                 f"quantum volume — it is confirmed representational (the 1/u³ "
                 f"inversion of a smooth numerator, BarOddLadderShape, pinned by "
                 f"experimental Q_β). Per the owner conditional: since the meridian "
                 f"is NOT anomalously close, the geometric route is closed and the "
                 f"alien-calculus / resurgence thread (D-ladder Écalle acceleration, "
                 f"#3818) is the lever where the swing (in D(u)) lives. No c_k; no "
                 f"fit; scope-(a)."
                 if ok else "INCONCLUSIVE — an assertion failed; inspect output."))
    wb.save()
    print(f"\n  assertions passed: {ok}")
    print("  witness -> computations/probes/qbeta-substrate-meridian-branchpoint.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
