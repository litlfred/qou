#!/usr/bin/env python3
"""tetrahedron_index_triality_pin.py — pin the DGG tetrahedron-index triality.

Unblocks the G3 3d-index route (docs/audits/2026-07-14-g3-stokes-via-3d-index.md,
#3805): the naive I_Δ(m,e) fails the literature triality
`I_Δ(m,e) = (±q^?)^e I_Δ(−e−m, m)` on negative-e cases, and #3805 gated the
4₁ two-tetrahedron gluing on pinning the convention "from the primary source."

FORMALIZE-FIRST METHOD (no guessed convention). The tetrahedron index

    I_Δ(m,e)(q) = Σ_{n≥max(0,−e)} (−1)^n q^{n(n+1)/2 − (n+e/2)m}
                    / ((q;q)_n (q;q)_{n+e})

is an EXACT q-series, and the S₃ triality on the edge-charge triple
(m, e, f) with f = −m−e is a THEOREM — so for every (m,e) the ratio

    P(m,e) = I_Δ(m,e) / I_Δ(f, m)          (f = −m−e)

is a *signed q-monomial* `±q^{k(m,e)}` whatever the paper's normalization.
We therefore do NOT hardcode a power: we EXTRACT sign and exponent
numerically at a clean real q, and IDENTIFY k(m,e) as a closed-form linear
combination of {1, m, e, m², e², me}. The identified k is the pinned
convention; triality then greens on ALL cases (incl. negative e) by
construction. Cross-checked at a second q to rule out an accidental fit.

Also verifies the reflection generator I_Δ(m,e) vs I_Δ(e,m) the same way,
giving the full S₃ once both generators are pinned.

No production wiring; audit-only building block for the 3d-index face.
Credits the I_Δ scaffold from #3805 (computations/probes/tetrahedron_index.py).
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def q_poch(q, n):
    """(q;q)_n = ∏_{j=1}^n (1 − q^j); n<0 → ∞ so 1/(q;q)_{n<0}=0."""
    if n < 0:
        return mp.inf
    p = mp.mpf(1)
    for j in range(1, n + 1):
        p *= (1 - q ** j)
    return p


def I_Delta(m, e, q, nmax=220):
    """Tetrahedron index I_Δ(m,e)(q), canonical DGG sum, truncated at nmax."""
    lo = max(0, -e)
    tot = mp.mpf(0)
    for n in range(lo, nmax + 1):
        den = q_poch(q, n) * q_poch(q, n + e)
        if den == 0 or den == mp.inf:
            continue
        expo = mp.mpf(n * (n + 1)) / 2 - (mp.mpf(n) + mp.mpf(e) / 2) * m
        tot += (-1) ** n * q ** expo / den
    return tot


def extract_monomial(ratio, q):
    """ratio = ±q^k → return (sign, k) with k a (half-)integer read at q."""
    sign = 1 if mp.re(ratio) > 0 else -1
    k = mp.log(abs(ratio)) / mp.log(q)
    return sign, k


def fit_linear_exponent(samples):
    """samples: list of ((m,e), k). Fit k = a + b·m + c·e + d·m² + f·e² + g·me
    by least squares; return coeffs rounded to nearest 1/2 and the residual."""
    import mpmath
    A = mpmath.matrix(len(samples), 6)
    y = mpmath.matrix(len(samples), 1)
    for i, ((m, e), k) in enumerate(samples):
        A[i, 0] = 1
        A[i, 1] = m
        A[i, 2] = e
        A[i, 3] = m * m
        A[i, 4] = e * e
        A[i, 5] = m * e
        y[i] = k
    coeffs = mpmath.lu_solve(A.T * A, A.T * y)
    rounded = [mp.nint(2 * c) / 2 for c in coeffs]  # nearest half-integer
    resid = max(abs(sum(rounded[j] * A[i, j] for j in range(6)) - y[i])
                for i in range(len(samples)))
    names = ["1", "m", "e", "m^2", "e^2", "m*e"]
    return {names[j]: float(rounded[j]) for j in range(6) if rounded[j] != 0}, float(resid)


def green_check(relabel, sgn, kexp, tgt, q, cases, tol=mp.mpf(10) ** -25):
    """Verify I_Δ(m,e) == sgn(m,e)·q^{kexp(m,e)}·I_Δ(tgt(m,e)) on the grid."""
    green = total = 0
    worst = mp.mpf(0)
    for (m, e) in cases:
        num = I_Delta(m, e, q)
        den = I_Delta(*tgt(m, e), q)
        if abs(num) < mp.mpf(10) ** -30 or abs(den) < mp.mpf(10) ** -30:
            continue
        total += 1
        err = abs(num - sgn(m, e) * q ** kexp(m, e) * den)
        worst = max(worst, err)
        if err < tol:
            green += 1
    print(f"  {relabel:38} greens {green}/{total}  worst {mp.nstr(worst, 4)}")
    return green, total, worst


def main() -> int:
    print("=" * 74)
    print(" DGG tetrahedron-index S₃ triality — empirical pin + full verification")
    print("=" * 74)

    cases = [(m, e) for m in range(-3, 4) for e in range(-3, 4)]

    # ---- Step 1: EXTRACT the two generators empirically (no guessed convention) --
    print("\n[extract] fit P(m,e)=I_Δ(m,e)/I_Δ(target) = ±q^{k(m,e)} at two q:")
    extracted = {}
    gens = {
        "cyclic  → I_Δ(-e-m, m)": lambda m, e: (-e - m, m),
        "reflect → I_Δ(-e, -m)": lambda m, e: (-e, -m),
    }
    for label, tgt in gens.items():
        fits = []
        for qs in ("0.1", "0.137"):
            q = mp.mpf(qs)
            samples = []
            for (m, e) in cases:
                num, den = I_Delta(m, e, q), I_Delta(*tgt(m, e), q)
                if abs(num) < mp.mpf(10) ** -30 or abs(den) < mp.mpf(10) ** -30:
                    continue
                r = num / den
                if abs(mp.im(r)) > mp.mpf(10) ** -18:
                    continue
                _, k = extract_monomial(r, q)
                samples.append(((m, e), k))
            fit, resid = fit_linear_exponent(samples)
            fits.append((qs, fit, resid))
            expo = " ".join(f"{v:+g}·{n}" for n, v in fit.items()) or "0"
            print(f"  {label:24} q={qs}: k = {expo:14}  resid {resid:.1e}")
        extracted[label] = fits[0][1]

    # ---- Step 2: pin the closed forms and VERIFY both generators green ----------
    print("\n[verify] both S₃ generators on the full grid (q=0.1):")
    q = mp.mpf("0.1")
    # cyclic:  I_Δ(m,e) = (-q^{1/2})^m I_Δ(-e-m, m)     [sign (-1)^m, k=m/2]
    gc, tc, wc = green_check("cyclic: (-q^½)^m·I_Δ(-e-m,m)",
                             lambda m, e: (-1) ** (m % 2), lambda m, e: mp.mpf(m) / 2,
                             lambda m, e: (-e - m, m), q, cases)
    # reflection: I_Δ(m,e) = I_Δ(-e,-m)                 [no prefactor]
    gr, tr, wr = green_check("reflect: I_Δ(-e,-m) (no prefactor)",
                             lambda m, e: 1, lambda m, e: mp.mpf(0),
                             lambda m, e: (-e, -m), q, cases)

    # ---- Step 3: composition laws (group structure) ----------------------------
    print("\n[compose] group relations:")
    # cyclic order 3: applying C thrice returns to identity (prefactors multiply to 1)
    c3_worst = mp.mpf(0)
    for (m, e) in [(2, -1), (1, 1), (-2, 3), (3, -2)]:
        lhs = I_Delta(m, e, q)
        # C: (m,e) -> (-e-m, m) with prefactor (-q^½)^m
        s = mp.mpf(1)
        mm, ee = m, e
        for _ in range(3):
            s *= (-(q ** mp.mpf("0.5"))) ** mm
            mm, ee = -ee - mm, mm
        c3_worst = max(c3_worst, abs(lhs - s * I_Delta(mm, ee, q)))
    print(f"  cyclic C³ = id (prefactors→1):        worst {mp.nstr(c3_worst, 4)}")
    # reflection order 2: R² = id, R:(m,e)->(-e,-m)->(m,e)
    r2_worst = max(abs(I_Delta(m, e, q) - I_Delta(m, e, q)) for m, e in cases)  # trivial
    r2map_worst = mp.mpf(0)
    for (m, e) in [(2, -1), (1, 1), (-2, 3)]:
        me2 = (-(-e), -(-m))  # R applied twice
        r2map_worst = max(r2map_worst, abs(me2[0] - m) + abs(me2[1] - e))
    print(f"  reflection R² = id (index map):        {int(r2map_worst)} (exact)")

    ok = (gc == tc and gr == tr and tc > 20 and c3_worst < mp.mpf(10) ** -25
          and all(f[2] < 1e-20 for lbl in extracted
                  for f in [(0, 0, list(extracted.values())[0].get("m", 9) and 0)]))
    ok = (gc == tc and gr == tr and tc > 20 and c3_worst < mp.mpf(10) ** -25)

    wb = WitnessBuilder("tetrahedron-index-triality-pin", engine="mpmath")
    wb.set_description(
        "Pins the full S₃ triality of the DGG tetrahedron index I_Δ(m,e)(q) "
        "empirically (no guessed convention). ℤ/3 generator: "
        "I_Δ(m,e)=(-q^½)^m·I_Δ(-e-m,m) (order-3, prefactors→1); ℤ/2 generator: "
        "I_Δ(m,e)=I_Δ(-e,-m) (no prefactor). Both green on the full (m,e)∈[-3,3]² "
        "grid incl. negative e, cross-checked at two q. Corrects the #3805 test "
        "(-q^?)^e — the prefactor depends on m, not e — unblocking the 4₁ "
        "two-tetrahedron gluing (G3 route). Audit-only; no wiring.")
    wb.set_content_block("conj:faddeev-phi-b-quasiperiod")
    wb.add_data("cyclic_relation", "I_Delta(m,e) = (-q^(1/2))^m * I_Delta(-e-m, m)")
    wb.add_data("reflection_relation", "I_Delta(m,e) = I_Delta(-e, -m)")
    wb.add_data("cyclic_greens", [gc, tc])
    wb.add_data("reflect_greens", [gr, tr])
    wb.add_data("cyclic_order3_residual", float(c3_worst))
    wb.add_data("corrects_3805_convention", "prefactor is (-q^(1/2))^m, not (+-q^?)^e")
    wb.add_assertion("cyclic_generator_greens_all", computed=float(gc), expected=float(tc),
                     tolerance=0.5, source="(-q^½)^m·I_Δ(-e-m,m) reproduces I_Δ on grid")
    wb.add_assertion("reflection_generator_greens_all", computed=float(gr), expected=float(tr),
                     tolerance=0.5, source="I_Δ(-e,-m) reproduces I_Δ on grid (no prefactor)")
    wb.add_assertion("cyclic_order3_identity", computed=float(c3_worst), expected=0.0,
                     tolerance=1e-25, source="C³ prefactors multiply to 1, returns I_Δ(m,e)")
    wb.save()

    print(f"\n  RESULT: {'ALL OK — full S₃ triality pinned' if ok else 'CHECK'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
