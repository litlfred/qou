#!/usr/bin/env python3
"""qbeta_5two_one_instanton_nodd_probe.py — the one-instanton magnitude test.

Formalize-first companion to `QOU/QBeta/OneInstantonNormalization.lean` (PR #4246).
The A3 shape probe (`qbeta_5two_sigma3_nodd_shape_probe.py`, #3927) tested the
**linear** hypothesis `N_odd ∝ Im(ι₁₃)` (raw geometric quantum-volume Im part) and
found it MONOTONE with slope ≈ 0.196 at q₀ — no zero crossing, ~12× short of the
committed `A′(q*) ≈ 2.37` (`BarOddLadderShape`).

This probe tests the DISTINCT **one-instanton** hypothesis the literature identifies
(Écalle bridge equation; GGM resurgence of complex Chern–Simons; audit
`2026-07-25-aomega-normalization-one-instanton-map.md`):

    N_odd(q) = 𝒜 · e^{ −Re 𝔙(q)/(π ℏ) } · sin( Im 𝔙(q)/(π ℏ) )    ( · P, set = 1 )

where 𝔙(q) = V₁ − V₃ is the complex Chern–Simons action (the Borel singularity
ω·2πi), and the zero-crossing comes from the **CS-phase oscillation**
`sin(Im 𝔙/πℏ)`, NOT from Im 𝔙 = 0 (which the raw form lacked). The Lean brick proves
this product shape's slope at a simple zero is log-derivative-free (matching the
committed `hasDerivAt_S_at_qstar`); this probe asks the MAGNITUDE question:

  (i)   does `sin(Im 𝔙/πℏ)` cross zero in the substrate window?
  (ii)  at that zero q_z, is the amplitude `𝒜·e^{−Re𝔙/πℏ}` at the O(10⁻⁶) scale of
        the committed A = S·u³?
  (iii) is the slope `dN_odd/dq|_{q_z} = 𝒜·e^{−Re𝔙/πℏ}·cos(·)·(Im 𝔙/πℏ)′` within
        reach of A′(q*) ≈ 2.37?

DISCIPLINE (STRICT — anti-fit). PARAMETER-FREE: 𝒜 = 1 (the base integer b=0 Stokes
amplitude, GZWeightGeneral), P = 1, ℏ = log q (the GGM q = e^ℏ convention — NOT
tuned). NOTHING is adjusted to hit q* or A′. The result is REPORTED as-is: a match is
evidence for the one-instanton map; a miss is a scope-(a) constraint on the prefactor
P / ℏ-scaling, NOT an ingredient exclusion and NOT a refutation of the Lean structural
consistency. No c_k wired; no AME inversion; μ never fixed from QOU data.

Run: python3 -u computations/probes/qbeta_5two_one_instanton_nodd_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_oneinst.log
"""
from __future__ import annotations

import sys
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

Q0 = mp.mpf("1.1099785827513808075916690956107688798744991218736")
A_PRIME_QSTAR = mp.mpf("2.3716")   # committed N_odd numerator slope at q* (BarOddLadderShape)
U_Q0 = mp.mpf("0.008520")          # substrate lever u = b·ℏ_q² at q₀ (A = S·u³ scale ref)


def _load_saddle_module():
    sys.argv = [sys.argv[0]]
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import qbeta_g3_5two_saddle_exact_predictions as p  # noqa
    return p


def main() -> int:
    p = _load_saddle_module()

    def frak_V(q):
        """Complex CS action 𝔙(q) = V₁ − V₃ (the Borel singularity, = 2πi·ι₁₃)."""
        u = 2 * mp.log(q)
        d = p.order_saddles(p.saddle_roots(mp.e ** u))
        V1 = p.V_of(u, d[0])[0]
        V3 = p.V_sigma3(u, d[2])[0]
        return V1 - V3

    def hbar(q):
        return mp.log(q)                      # GGM q = e^ℏ (parameter-free, not tuned)

    def phase(q):
        return mp.im(frak_V(q)) / (mp.pi * hbar(q))

    def amp(q):
        return mp.e ** (-mp.re(frak_V(q)) / (mp.pi * hbar(q)))   # 𝒜=1, P=1

    def N_odd(q):
        return amp(q) * mp.sin(phase(q))

    print("=" * 78)
    print(" 5₂ one-instanton N_odd magnitude test (parameter-free; 𝒜=1, P=1, ℏ=log q)")
    print("=" * 78)

    assertions = []

    def check(name, passed, **kw):
        assertions.append({"name": name, "passed": bool(passed),
                           **{k: v for k, v in kw.items() if v is not None}})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    # ---- scan the phase + N_odd across the substrate window ----
    print("\n  q         Re𝔙        Im𝔙       phase/π     amp=e^{-Re𝔙/πℏ}   N_odd")
    qs = [mp.mpf(s) for s in ("1.02", "1.05", "1.08", "1.11", "1.15", "1.20", "1.30")]
    phases, nodds = [], []
    for q in qs:
        V = frak_V(q); ph = phase(q); a = amp(q); n = N_odd(q)
        phases.append(ph); nodds.append(n)
        print(f"  {mp.nstr(q,5):>6}  {mp.nstr(mp.re(V),6):>9}  {mp.nstr(mp.im(V),6):>8}"
              f"  {mp.nstr(ph/mp.pi,6):>9}  {mp.nstr(a,4):>14}   {mp.nstr(n,4)}")

    # (i) does N_odd (i.e. sin(phase)) change sign in the window?
    signs = [1 if v > 0 else -1 for v in nodds]
    crosses = any(signs[k] != signs[k + 1] for k in range(len(signs) - 1))
    print(f"\n  N_odd sign-changes in the window: {crosses}   "
          f"(phase/π spans {mp.nstr(min(phases)/mp.pi,5)} .. {mp.nstr(max(phases)/mp.pi,5)})")
    check("one_instanton_nodd_has_zero_crossing", crosses,
          source="sin(Im𝔙/πℏ) oscillation produces a zero of N_odd in the substrate "
                 "window — the feature the RAW Im(ι₁₃) form (A3 probe) lacked")

    # (ii) locate the nearest phase-zero q_z (sin=0 ⇔ phase = kπ) and measure there.
    # Honest comparisons (a coincidental A′·u³ "amplitude match" was retracted after a
    # critical-distance re-check): the ROBUST quantity is the slope at the zero vs A′;
    # the lever 1/u³ CANCELS in the S-slope ratio, so it does NOT rescue the gap.
    def phase_minus_k(q, k):
        return phase(q) - k * mp.pi
    k0 = int(mp.nint(phase(Q0) / mp.pi))
    q_z = None
    for k in (k0 - 1, k0, k0 + 1):
        try:
            qz = mp.findroot(lambda q: phase_minus_k(q, k), Q0)
            if mp.im(qz) == 0 and mp.mpf("1.0") < qz < mp.mpf("1.5"):
                if q_z is None or abs(qz - Q0) < abs(q_z - Q0):
                    q_z = qz
        except Exception:
            pass

    # committed references
    N_ODD_ANCHOR = mp.mpf("2.5e-8")     # |N_odd| ~ |S_swing|·u³ (S_swing~0.04) near the anchors
    slope_orders = mag_orders = loc_off = None
    if q_z is not None:
        h = mp.mpf("1e-7")
        slope = (N_odd(q_z + h) - N_odd(q_z - h)) / (2 * h)
        a_z = amp(q_z)
        loc_off = abs(q_z - Q0)
        slope_orders = abs(mp.log(abs(slope) / A_PRIME_QSTAR, 10)) if slope != 0 else mp.inf
        mag_orders = abs(mp.log(abs(a_z) / N_ODD_ANCHOR, 10)) if a_z != 0 else mp.inf
        print(f"\n  nearest phase-zero q_z = {mp.nstr(q_z,10)}")
        print(f"  (i)  zero-location offset |q_z − q₀| = {mp.nstr(loc_off,4)}  "
              f"(~1e6× the anchor gap ⇒ NOT pinned to q*)")
        print(f"  (ii) slope dN_odd/dq|_{{q_z}} = {mp.nstr(slope,5)}   vs A′(q*)="
              f"{mp.nstr(A_PRIME_QSTAR,5)}   → {mp.nstr(slope_orders,3)} orders short")
        print(f"       (lever cancels: S-slope ratio = A-slope ratio, so 1/u³ does NOT close it)")
        print(f"  (iii) prefactor 𝒜·e^{{-Re𝔙/πℏ}}={mp.nstr(a_z,4)} vs |N_odd|(anchor)~"
              f"{mp.nstr(N_ODD_ANCHOR,3)} → {mp.nstr(mag_orders,3)} orders too large")
    else:
        print("\n  no real phase-zero located in [1.0,1.5] near q₀")

    # HONEST assertions: only the structural zero-crossing passes parameter-free.
    check("one_instanton_slope_far_below_A_prime",
          (slope_orders is not None) and slope_orders > mp.mpf("2"),
          computed=(None if slope_orders is None else f"{mp.nstr(slope_orders,3)} orders short"),
          source="parameter-free one-instanton slope at its zero is ~4 orders below "
                 "A′≈2.37; the 1/u³ lever cancels in the ratio and does NOT rescue it — "
                 "a derived prefactor/ℏ-scaling is required (must not be fitted)")
    check("one_instanton_zero_not_pinned_to_qstar",
          (loc_off is not None) and loc_off > mp.mpf("1e-3"),
          computed=(None if loc_off is None else f"|q_z−q₀|={mp.nstr(loc_off,4)}"),
          source="the phase-zero q_z is ~0.009 from q₀≈q* (~1e6× the anchor gap) — the "
                 "parameter-free form does not place the zero at q*")

    print("\n" + "=" * 78)
    n_pass = sum(a["passed"] for a in assertions)
    print(f" one-instanton magnitude test: {n_pass}/{len(assertions)} checks "
          f"(zero-crossing PASS; slope/location/amplitude all OFF, parameter-free)")
    print("=" * 78)
    print("\nHONEST VERDICT (scope-a). Parameter-free (𝒜=1, P=1, ℏ=log q), the "
          "one-instanton form supplies the ZERO-CROSSING STRUCTURE the raw monotone "
          "Im(ι₁₃) form lacked — but it does NOT reproduce N_odd quantitatively: the "
          "slope at its zero is ~4 orders below A′≈2.37 (the 1/u³ lever cancels and "
          "does not rescue it), the zero is ~0.009 off q*, and the prefactor is ~100× "
          "too large near the anchors. So the one-instanton is the STRUCTURALLY "
          "necessary ingredient (only thing producing a zero) but INSUFFICIENT "
          "parameter-free; the closing prefactor/ℏ-scaling must be DERIVED, not tuned. "
          "A coincidental A′·u³ 'amplitude match' from an earlier version is RETRACTED. "
          "No fit; no c_k wired; μ never fixed from QOU data. The Lean structural "
          "consistency (OneInstantonNormalization.lean) stands regardless.")

    # ---- witness ----
    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("qbeta-5two-one-instanton-nodd", engine="mpmath")
        w.set_description(
            "One-instanton magnitude test for the A_ω normalization map "
            "(OneInstantonNormalization.lean, PR #4246). Parameter-free (𝒜=1, P=1, "
            "ℏ=log q) test of N_odd = e^{-Re𝔙/πℏ}·sin(Im𝔙/πℏ) against the committed "
            "BarOddLadderShape (A′≈2.37, |N_odd|~2.5e-8 at anchors). HONEST RESULT "
            "(scope-a): the sin oscillation supplies the ZERO-CROSSING STRUCTURE "
            "(q_z≈1.1013) the raw Im(ι₁₃) form lacked, but parameter-free it does NOT "
            "reproduce N_odd quantitatively — slope at the zero ~4 orders below A′ (the "
            "1/u³ lever CANCELS in the ratio, does not rescue it), zero ~0.009 off q*, "
            "prefactor ~100× too large near the anchors. The one-instanton is the "
            "structurally necessary ingredient but insufficient parameter-free; the "
            "closing prefactor/ℏ-scaling must be DERIVED not tuned. An earlier "
            "coincidental A′·u³ 'amplitude match' is RETRACTED. No fit; no c_k wired.")
        for a in assertions:
            w.add_assertion(a["name"], computed=1 if a["passed"] else 0, expected=1,
                            tolerance=0.5, source=a.get("source", ""))
        if q_z is not None:
            w.add_data("q_z_phase_zero", mp.nstr(q_z, 12))
            w.add_data("zero_location_offset_from_q0", mp.nstr(loc_off, 6))
            w.add_data("prefactor_at_qz", mp.nstr(a_z, 8))
            w.add_data("N_odd_anchor_scale", mp.nstr(N_ODD_ANCHOR, 4))
            w.add_data("prefactor_too_large_orders", mp.nstr(mag_orders, 4))
            w.add_data("slope_at_qz", mp.nstr(slope, 8))
            w.add_data("A_prime_qstar", mp.nstr(A_PRIME_QSTAR, 6))
            w.add_data("slope_gap_orders", mp.nstr(slope_orders, 4))
        out = w.save()
        print(f"witness → {out.name}")
    except Exception as e:  # pragma: no cover
        print(f"(witness save skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
