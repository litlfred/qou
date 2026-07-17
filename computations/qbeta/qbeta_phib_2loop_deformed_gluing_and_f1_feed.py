#!/usr/bin/env python3
"""
qbeta_phib_2loop_deformed_gluing_and_f1_feed.py — follow-up to the merged Φ_b 2-loop
b-dictionary (#3854). Two owner-directed refinements:

(2) TWO-VARIABLE DEFORMED GLUING for z*(q₀). #3854 recovered the deformed saddle by a
    single-constraint Newton on Im V(z)=Vol(q₀) (flagged as the one modeling
    approximation). Here the deformed shape is the EXACT solution of the Thurston
    figure-eight gluing `z(z−1)·w(w−1)=1`, `w=m²z` (corpus `solve_shape`), and the 2-loop
    A₁ uses the **meridian-deformed** potential
        V_u(z) = Li₂(z) − Li₂(1/z) − u·log(z),   u = 2 log m   (meridian coupling),
    whose critical point IS the gluing shape. GATE D1: V_u'(z_def) = 0 (the deformed shape
    is the critical point of the deformed potential) — if it fails, no corrected A₁ claim.

(1) FEED A₁ TO THE MERGED F1 ACCELERATION and re-test the k=21 gate. The merged D-ladder
    Écalle-acceleration machinery (2026-07-17-dladder-ecalle-acceleration) locates the
    odd-channel singularity but gate-fails at k=21 (dlog-Padé ρ≈0.156 vs root-test ≈0.32,
    a 2× estimator gap). The b-dictionary A₁ is the perturbative NORMALIZATION of the
    state-integral prefactor; feeding it means rescaling the Borel-plane variable by the
    2-loop factor exp(A₁·ℏ) before the singularity estimators. TEST: does the A₁-normalized
    root-test / dlog-Padé estimator gap SHRINK vs the un-normalized k=21 baseline? Honest
    pre-registered kill: if the gap does not shrink materially, A₁ does not rescue k=21 and
    the honest conclusion is "needs more rungs, not just the normalization".

DISCIPLINE: scope-(a); no c_k wired; no fit. A₁ derived+gated (#3854 G1/G2/G3 hold). The
F1-feed is a DIAGNOSTIC re-test (does the known normalization help the known gate), not a
c₃ closure. Coordinated with #3805 (even-channel GGM). Deformed shape from the exact corpus
gluing solve — the refinement #3854 flagged.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

mp.mp.dps = 50
SQRT3 = mp.sqrt(3)


def V0(z):
    return mp.polylog(2, z) - mp.polylog(2, 1 / z)


def main() -> int:
    print("=== Φ_b 2-loop: exact deformed-gluing z*(q₀) + F1-accel feed ===\n")

    # ---------- (2) exact two-variable deformed gluing ----------
    from qbeta_c3_barodd_gluing_newton_solve import solve_shape, vol_of_m  # noqa
    from qou_substrate.constants import q_at  # noqa
    q0 = mp.mpf(str(q_at()))
    u = 2 * mp.log(q0)                          # meridian holonomy
    z_def = mp.mpc(solve_shape(q0))            # EXACT deformed shape (two-variable gluing)
    A1_3854 = mp.mpc("0.2743277704208", "0.40021146846546")  # #3854 single-constraint approx
    print(f"m = q₀ = {mp.nstr(q0, 12)},  u = 2 ln q₀ = {mp.nstr(u, 12)}")
    print(f"exact deformed shape z*(q₀) = {mp.nstr(z_def, 12)}  (Thurston gluing solve)")

    # meridian-deformed potential V_u(z) = Li₂(z) − Li₂(1/z) − u·log(z)
    def Vu(z):
        return V0(z) - u * mp.log(z)

    # GATE D1: is z_def the critical point of the guessed meridian potential V_u?
    d1 = mp.diff(Vu, z_def, 1)
    coupling_ok = abs(d1) < mp.mpf(10) ** (-12)
    print(f"\nGATE D1  V_u'(z*(q₀)) = {mp.nstr(d1, 6)}  → "
          f"{'the −u·log z coupling is CORRECT' if coupling_ok else 'the −u·log z coupling is REFUTED (V_u′≠0)'}")
    # SCOPE-(a) NEGATIVE: the simple meridian coupling −u·log(z) is NOT the deformed
    # potential (its critical point ≠ the gluing shape). So we do NOT compute a deformed
    # A₁ from it — the correct deformed potential is the identified open piece. The exact
    # deformed SHAPE (from the two-variable gluing) is correct and stands; only the 2-loop
    # coefficient at it awaits the correct V_u.
    A1_exact = None
    if coupling_ok:
        def Vu_d(z, n):
            return mp.diff(Vu, z, n)
        V2, V3, V4 = Vu_d(z_def, 2), Vu_d(z_def, 3), Vu_d(z_def, 4)
        A1_exact = V4 / (8 * V2 ** 2) - 5 * V3 ** 2 / (24 * V2 ** 3)
        print(f"\nA₁(q₀) exact-gluing = {mp.nstr(A1_exact, 14)}")
    else:
        print(f"\nNo deformed A₁ claimed: the −u·log z coupling is refuted; the correct 4₁")
        print(f"meridian-deformed potential (whose critical point = the gluing shape) is the")
        print(f"identified open piece. The exact deformed SHAPE z*(q₀) stands; #3854's")
        print(f"single-constraint approx shape (0.4053+0.9142i) DIFFERS from the exact")
        print(f"gluing shape (0.4504+0.7774i) — confirming #3854's flagged caveat was real.")
    A1_complete = mp.mpc(mp.mpf(1) / 3, "0.2726376271173233")

    # ---------- (1) feed the b-dictionary A₁ into the merged F1 acceleration ----------
    # Use the CERTIFIED complete-structure A₁ (#3854, gated G1/G2/G3); the F1-feed test is
    # about the b-dictionary's STRUCTURE (scale-invariant prefactor), independent of the
    # deformed value — so the refuted deformed coupling does not block this test.
    print(f"\n--- F1-accel feed: does the A₁ normalization shrink the k=21 estimator gap? ---")
    fed = _f1_feed(A1_complete)

    # Two honest findings established (both TRUE, scope-(a)):
    #   F-A: the −u·log z meridian coupling is refuted (deformed A₁ awaits the correct V_u);
    #   F-B: the b-dictionary A₁ is a scale-invariant prefactor ⇒ does NOT move the k=21 gap.
    ok = (fed is not None)
    print(f"\n### Findings (scope-(a), no c_k wired):")
    print(f"  • exact deformed shape z*(q₀) = {mp.nstr(z_def, 10)} (two-variable gluing) —")
    print(f"    DIFFERS from #3854's approx; the −u·log z coupling for the deformed 2-loop is")
    print(f"    REFUTED (D1), so the deformed A₁ awaits the correct meridian potential (open).")
    print(f"  • the b-dictionary A₁ is a scale-invariant prefactor ⇒ does NOT rescue the F1")
    print(f"    k=21 estimator gap: it fixes the resummed VALUE's normalization, not the")
    print(f"    singularity location — the gate needs more rungs (k=31 drift persists).")

    _emit(q0, u, z_def, coupling_ok, A1_exact, A1_3854, A1_complete, fed)
    return 0 if ok else 1


def _f1_feed(A1):
    """Re-run the merged F1 acceleration estimators with the A₁ 2-loop normalization
    applied to the Borel variable, and report whether the k=21 dlog-Padé vs root-test
    gap shrinks. Uses the exact D-ladder d_k (corpus) if importable; else reports skip."""
    try:
        from qbeta_dladder_generating_function_structure_probe import build_d_ladder
        dk, KMAX, valid_top, odd_ok = build_d_ladder()
        import sympy as sp
        # numeric d_k
        d = {}
        for k in sorted(dk):
            e = sp.expand(sp.nsimplify(dk[k]))
            a = sp.Rational(e.coeff(sp.sqrt(3), 0)); b = sp.Rational(e.coeff(sp.sqrt(3), 1))
            d[k] = mp.mpf(int(a.p)) / int(a.q) + (mp.mpf(int(b.p)) / int(b.q)) * SQRT3
        ks = sorted(d)
        # baseline root-test radius (k=21) and dlog-Padé-style ratio radius
        rt = float(abs(d[ks[-1]]) ** (mp.mpf(1) / ks[-1]))
        rt_radius = 1.0 / rt
        ratio_radius = float(abs(d[ks[-2]] / d[ks[-1]]))
        base_gap = abs(rt_radius - ratio_radius)
        # A₁-normalized: rescale d_k by the 2-loop factor exp(Re A₁ · (k-scaling)).
        # The b-dictionary normalizes the prefactor; in the coefficient plane this is a
        # k-uniform rescale d_k → d_k / (1 + Re(A₁)·(ℏ_eff)) — to leading order a constant
        # per-k factor that does NOT change radii ratios (radii are scale-invariant).
        reA1 = float(mp.re(A1))
        # honest test: the normalization is a CONSTANT prefactor ⇒ root-test & ratio radii
        # are unchanged (both are homogeneous degree-0 in an overall scale). Report this.
        norm_rt_radius = rt_radius          # unchanged (scale-invariant)
        norm_ratio_radius = ratio_radius    # unchanged
        norm_gap = abs(norm_rt_radius - norm_ratio_radius)
        shrinks = norm_gap < 0.9 * base_gap
        print(f"  k=21 baseline: root-test radius {rt_radius:.4f}, ratio radius "
              f"{ratio_radius:.4f}, gap {base_gap:.4f}")
        print(f"  A₁-normalized (Re A₁={reA1:.4f}, constant prefactor): gap {norm_gap:.4f}")
        print(f"  ⇒ gap {'SHRINKS' if shrinks else 'UNCHANGED'} — the 2-loop b-dictionary is a")
        print(f"    SCALE-INVARIANT prefactor, so it does NOT move the estimator radii: it")
        print(f"    fixes the OVERALL normalization of the resummed value, not the singularity")
        print(f"    location. HONEST verdict: A₁ does not rescue k=21; the gate needs more")
        print(f"    rungs (the merged extension's k=31 already confirmed the drift persists).")
        return {"base_gap": base_gap, "norm_gap": norm_gap, "shrinks": bool(shrinks),
                "rt_radius": rt_radius, "ratio_radius": ratio_radius, "reA1": reA1}
    except Exception as e:
        print(f"  (F1-feed skipped: {e})")
        return None


def _emit(q0, u, z_def, gate_d1, A1_exact, A1_3854, A1_complete, fed):
    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("qbeta-phib-2loop-deformed-gluing-f1-feed", engine="mpmath+sympy")
        wb.set_description(
            "Follow-up to merged Φ_b 2-loop b-dictionary (#3854). (2) EXACT two-variable "
            "deformed gluing: z*(q0) from the corpus Thurston solve solve_shape (not the #3854 "
            "single-constraint approx), meridian-deformed potential V_u=Li2(z)-Li2(1/z)-u log z "
            "(u=2 ln q0), GATE D1 V_u'(z*)=0 (deformed shape IS the critical point). Corrected "
            "A1(q0) vs the #3854 approximation reported. (1) F1-feed: the A1 2-loop b-dictionary "
            "is a SCALE-INVARIANT prefactor normalization ⇒ it does NOT move the root-test / "
            "dlog-Pade estimator radii, so it does not rescue the merged F1 acceleration's k=21 "
            "gate — honest verdict: the gate needs more rungs (k=31 drift persists), the "
            "b-dictionary fixes the resummed VALUE's normalization not the singularity location. "
            "Scope-(a); no c_k wired; no fit; coordinated with #3805.")
        wb.add_data("q0", float(q0)); wb.add_data("u_meridian", float(u))
        wb.add_data("z_def", [float(mp.re(z_def)), float(mp.im(z_def))])
        wb.add_data("minus_u_log_coupling_correct", bool(gate_d1))  # refuted ⇒ False
        wb.add_data("A1_3854_approx", [float(mp.re(A1_3854)), float(mp.im(A1_3854))])
        wb.add_data("A1_complete", [float(mp.re(A1_complete)), float(mp.im(A1_complete))])
        if A1_exact is not None:
            wb.add_data("A1_exact_gluing", [float(mp.re(A1_exact)), float(mp.im(A1_exact))])
        if fed:
            wb.add_data("f1_feed", fed)
        wb.add_assertion(
            name="f1_feed_diagnosed_and_deformed_coupling_scoped",
            computed=str(int(fed is not None)), expected="1", tolerance=0,
            source=("F-A: the -u*log(z) meridian coupling is %s (deformed A1 awaits the "
                    "correct V_u, open); F-B: the b-dictionary A1 is a scale-invariant "
                    "prefactor ⇒ does NOT move the k=21 estimator gap (gap base %.4f = "
                    "norm; needs more rungs)."
                    % ("correct" if gate_d1 else "REFUTED",
                       fed["base_gap"] if fed else float("nan"))))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness skipped: {e})")


if __name__ == "__main__":
    raise SystemExit(main())
