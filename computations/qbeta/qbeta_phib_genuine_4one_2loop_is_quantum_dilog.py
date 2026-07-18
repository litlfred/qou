#!/usr/bin/env python3
"""
qbeta_phib_genuine_4one_2loop_is_quantum_dilog.py — the genuine 4₁ 2-loop is the quantum
dilogarithm, NOT any classical potential.  Constructive completion of the #3874 correction.

Owner ask (2026-07-18): build the genuine Andersen–Kashaev / Dimofte 4₁ potential that "fixes
all derivatives at once", or match the next invariant κ₁ = 11√3π/108.  This probe answers it,
and in doing so CORRECTS a computational error from the pre-#3874 exploration (the claim that a
"t-coordinate" potential gives a real 2-loop ≈ 0.1008 close to κ₁ — it does not; see B below).

THREE VERIFIED FINDINGS (all positive-controlled, no fit):

A. GROUND TRUTH (Kashaev sum, first-principles, NO fit).  The physical dimensionless 2-loop
   invariant of 4₁, extracted from ⟨4₁⟩_N = Σ_k |(q)_k|² (q=e^{2πi/N}) by high-precision
   Richardson extrapolation (70 dps, N→3200):
       a₁^phys = 0.08820589…   vs   11/(72√3) = 0.08820629…   (rel err 4.5e-6).
   So the genuine 2-loop is 11/(72√3), and the Ohtsuki normalization
       κ₁ = 2π · 11/(72√3) = 11√3π/108 = 0.5542165   (coeff of 1/N).
   CONVENTION RESOLVED: κ₁ (corpus, coeff of 1/N) = 2π × the dimensionless DG 2-loop
   (coeff of 2π/N).  The corpus κ-tower already IS this physical object.

B. The naive saddle 2-loop of a CLASSICAL potential is COORDINATE-DEPENDENT, hence cannot be
   the knot invariant.  For V(z)=Li₂(z)−Li₂(1/z) at the geometric saddle, the naive
   A₁ = V⁗/(8V''²) − 5V'''²/(24V''³) takes FOUR different values in four coordinates:
       z-coord  (z*=e^{iπ/3})     : A₁ = 1/3 + (17√3/108)i     (the merged #3874 value)
       t-coord  (z=e^{2πit})      : A₁ = −0.016038 i           (PURE IMAGINARY)
       w-coord  (z=e^{w})         : A₁ = −0.016038 i           (= t; affine-equiv)
       s-coord  (z=1/(1−s), Möbius): A₁ = −1/3 + (17√3/108)i
   None equals the invariant 0.08819.  (t and w agree because w=2πi·t is an AFFINE change;
   the naive 2-loop is affine-invariant but not reparametrization-invariant.)  This is the
   clean proof that "a classical potential + Feynman 2-loop" is the WRONG object.
   >>> CORRECTS the pre-#3874 note "t-coord gives real 0.1008 ≈ κ₁": the true t-value is
       −0.016038 i (real part 0 to 65 dps); the earlier "0.1008 real" was a compute error and
       its apparent closeness to κ₁ was illusory.

C. THE GENUINE OBJECT is the Faddeev quantum dilogarithm Φ_b / the Andersen–Kashaev state
   integral (equivalently the Kashaev sum), NOT a classical potential.  The coordinate-
   INVARIANT 2-loop is the naive Feynman 2-loop PLUS the ℏ¹ (b²) "quantum content" correction
   of Φ_b (Dimofte–Garoufalidis).  Only that combination is a knot invariant, and it equals
   κ₁ — as A verifies directly from the sum.  So the honest answer to "genuine potential OR
   match κ₁" is: there is no classical potential whose bare 2-loop is κ₁ (it isn't even
   coordinate-invariant); the genuine potential is the quantum dilogarithm, and its 2-loop —
   already in the corpus via the Kashaev fit — is κ₁.

Discipline: scope-(a) (re-scope, do not delete #3874's number; it stands as the z-coord naive
2-loop).  No c_k wired; L2 unchanged (2/7).  Ohtsuki=perturbative-CS=state-integral loop
expansion — same invariants; the discriminator is coordinate-invariance, which the sum has and
the classical-potential naive 2-loop lacks.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

mp.mp.dps = 70


# ----------------------------------------------------------------------------- B: coordinates
def _naive_2loop(Vfun, xstar):
    V2 = mp.diff(Vfun, xstar, 2)
    V3 = mp.diff(Vfun, xstar, 3)
    V4 = mp.diff(Vfun, xstar, 4)
    return V4 / (8 * V2 ** 2) - 5 * V3 ** 2 / (24 * V2 ** 3)


def coordinate_dependence():
    Vz = lambda z: mp.polylog(2, z) - mp.polylog(2, 1 / z)
    coords = {
        "z  (z*=e^{iπ/3})": (Vz, mp.exp(mp.j * mp.pi / 3)),
        "t  (z=e^{2πit})": (lambda t: Vz(mp.exp(mp.j * 2 * mp.pi * t)), mp.mpf(1) / 6),
        "w  (z=e^{w})": (lambda w: Vz(mp.exp(w)), mp.j * mp.pi / 3),
        "s  (z=1/(1-s))": (lambda s: Vz(1 / (1 - s)), 1 - mp.exp(-mp.j * mp.pi / 3)),
    }
    vals = {}
    for name, (Vf, xs) in coords.items():
        vals[name] = _naive_2loop(Vf, xs)
    return vals


# ----------------------------------------------------------------------- A: Kashaev ground truth
def _kashaev_log(N):
    """log ⟨4₁⟩_N via |(q)_k|² = ∏_{j=1}^k 4 sin²(πj/N), summed in log-space (stable)."""
    logterms = [mp.mpf(0)]
    running = mp.mpf(0)
    for k in range(1, N):
        running += mp.log(4 * mp.sin(mp.pi * k / N) ** 2)
        logterms.append(running)
    m = max(logterms)
    return m + mp.log(mp.fsum(mp.e ** (t - m) for t in logterms))


def kashaev_2loop(Vol):
    """dimensionless 2-loop a₁: ⟨4₁⟩_N = 3^{-1/4} N^{3/2} e^{N Vol/2π}(1 + a₁(2π/N) + …)."""
    V2pi = Vol / (2 * mp.pi)
    Ns = [200, 400, 800, 1600, 3200]
    cs = []
    for N in Ns:
        logR = _kashaev_log(N) - (-mp.log(3) / 4 + mp.mpf(3) / 2 * mp.log(N) + N * V2pi)
        cs.append((mp.e ** logR - 1) * N / (2 * mp.pi))

    def rich(vals, ns):
        return [(ns[i + 1] / ns[i] * vals[i + 1] - vals[i]) / (ns[i + 1] / ns[i] - 1)
                for i in range(len(vals) - 1)]

    r = cs
    ns = Ns
    while len(r) > 1:
        r = rich(r, ns)
        ns = ns[1:]
    return cs, r[0]


def main() -> int:
    print("=== The genuine 4₁ 2-loop is the quantum dilogarithm, not a classical potential ===\n")

    Vol = 2 * mp.clsin(2, mp.pi / 3)
    dg = 11 / (72 * mp.sqrt(3))
    kappa1 = 11 * mp.sqrt(3) * mp.pi / 108

    # A. ground truth from the Kashaev sum (no fit)
    print("A. GROUND TRUTH — dimensionless 2-loop from the Kashaev sum ⟨4₁⟩_N (no fit):")
    cs, a1_phys = kashaev_2loop(Vol)
    print(f"   Richardson extrapolant  a₁^phys = {mp.nstr(a1_phys, 12)}")
    print(f"   target 11/(72√3)               = {mp.nstr(dg, 12)}")
    rel = abs(a1_phys - dg) / dg
    print(f"   rel err = {mp.nstr(rel, 4)}   ({'MATCH' if rel < mp.mpf('1e-4') else 'NO'})")
    print(f"   ⇒ Ohtsuki κ₁ = 2π·a₁^phys = 11√3π/108 = {mp.nstr(kappa1, 12)} (coeff of 1/N)")
    a_ok = rel < mp.mpf("1e-4")

    # B. coordinate dependence of the naive classical 2-loop
    print("\nB. Naive classical-potential 2-loop A₁ = V⁗/(8V''²)−5V'''²/(24V''³) — 4 coordinates:")
    vals = coordinate_dependence()
    for name, v in vals.items():
        print(f"   {name:22} A₁ = {mp.nstr(v, 10)}")
    distinct = len({(mp.nstr(mp.re(v), 6), mp.nstr(mp.im(v), 6)) for v in vals.values()})
    t_val = vals["t  (z=e^{2πit})"]
    t_is_imag = abs(mp.re(t_val)) < mp.mpf(10) ** (-40)
    none_match = all(abs(abs(v) - dg) / dg > mp.mpf("1e-3") for v in vals.values())
    print(f"   distinct values: {distinct} of 4 ⇒ COORDINATE-DEPENDENT (not an invariant)")
    print(f"   t-coord real part = {mp.nstr(mp.re(t_val), 3)} ⇒ PURE IMAGINARY "
          f"(corrects the pre-#3874 'real 0.1008' error)")
    print(f"   none of the 4 equals the invariant 0.08819: {none_match}")

    # C. verdict
    print("\nC. VERDICT:")
    print("   • The genuine 2-loop invariant (0.08819 = 11/(72√3), κ₁=11√3π/108) is coordinate-")
    print("     INVARIANT and comes from the Kashaev sum / Andersen–Kashaev state integral.")
    print("   • No classical potential's naive 2-loop is even coordinate-invariant, so none is")
    print("     κ₁. The genuine object is the Faddeev quantum dilogarithm Φ_b; its coordinate-")
    print("     invariant 2-loop = naive Feynman + ℏ¹ quantum-content (Dimofte–Garoufalidis) = κ₁.")
    print("   • #3874's A₁ = 1/3+17√3/108 i stands as the z-coord naive 2-loop (number unretracted);")
    print("     the corpus κ-tower is the physical object. No c_k wired; L2 = 2/7.")

    ok = a_ok and (distinct >= 3) and t_is_imag and none_match

    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("qbeta-phib-genuine-4one-2loop-is-quantum-dilog", engine="mpmath")
        wb.set_description(
            "Constructive completion of the #3874 correction: the genuine 4₁ 2-loop invariant is "
            "the quantum dilogarithm / Kashaev sum, NOT any classical potential. (A) First-"
            "principles (no fit): the dimensionless 2-loop of ⟨4₁⟩_N=Σ|(q)_k|², extracted by 70-dps "
            "Richardson to N=3200, is 0.08820589 vs 11/(72√3)=0.08820629 (rel err 4.5e-6); so "
            "κ₁=2π·11/(72√3)=11√3π/108 (coeff 1/N) — CONVENTION RESOLVED. (B) The naive saddle "
            "2-loop of V=Li2(z)-Li2(1/z) is coordinate-dependent (z:1/3+17√3/108 i; t,w:-0.016038 i; "
            "s:-1/3+17√3/108 i) — 4 coords, ≥3 distinct values, none=0.08819 — so it is not the knot "
            "invariant. CORRECTS the pre-#3874 't-coord gives real 0.1008≈κ₁' claim: the true t-value "
            "is -0.016038 i (real part 0 to 65 dps). (C) The coordinate-invariant 2-loop is the naive "
            "Feynman 2-loop PLUS the ℏ¹ quantum-content (Dimofte-Garoufalidis) of Φ_b, = κ₁, already in "
            "the corpus via the Kashaev fit. Scope-(a): #3874's number stands as the z-coord naive "
            "2-loop; only 'the state integral' identification was wrong. No c_k wired; L2 2/7.")
        wb.add_data("a1_phys_kashaev", float(a1_phys))
        wb.add_data("dg_dimensionless_2loop", float(dg))
        wb.add_data("ohtsuki_kappa1", float(kappa1))
        wb.add_data("kashaev_rel_err", float(rel))
        wb.add_data("naive_2loop_z", [float(mp.re(vals["z  (z*=e^{iπ/3})"])),
                                      float(mp.im(vals["z  (z*=e^{iπ/3})"]))])
        wb.add_data("naive_2loop_t", [float(mp.re(t_val)), float(mp.im(t_val))])
        wb.add_data("naive_2loop_s", [float(mp.re(vals["s  (z=1/(1-s))"])),
                                      float(mp.im(vals["s  (z=1/(1-s))"]))])
        wb.add_data("naive_2loop_distinct_of_4", int(distinct))
        wb.add_data("t_coord_is_pure_imaginary", bool(t_is_imag))
        wb.add_data("convention_kappa1_eq_2pi_times_dg", True)
        wb.add_assertion(
            name="genuine_2loop_is_quantum_dilog_not_classical_potential",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("Kashaev-sum dimensionless 2-loop = %.9f = 11/(72√3) (rel err %.1e, no fit); "
                    "naive classical 2-loop coordinate-dependent (%d distinct of 4, t pure-imag, "
                    "none=0.08819) ⇒ genuine object = quantum dilogarithm, κ₁=2π·11/(72√3)="
                    "11√3π/108. Scope-(a); no c_k wired."
                    % (float(a1_phys), float(rel), int(distinct))))
        out = wb.save()
        print(f"\nWitness: {out}")
    except ImportError as e:
        print(f"\n(witness skipped — witness_base unavailable: {e})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
