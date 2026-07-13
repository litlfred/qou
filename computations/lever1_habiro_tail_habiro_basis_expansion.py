#!/usr/bin/env python3
"""
lever1_habiro_tail_habiro_basis_expansion.py — expand the binding Habiro tail D(n) in the
Habiro / cyclotomic-completion basis (q;q)_k (lever-1 / z2bn; the Stage-6 "next decidable").

Context. The exact binding q-deformation is S(n) = S(n−1) + [n−1]_q·S(n−2) + D(n), with
S(n) = Σ_{λ⊢n} dim_q(λ) (balanced convention) and D(n) the Habiro tail
(2026-07-12-lever1-habiro-tail-closed-form.md: universal (q−1)² double root, bar-even,
cyclotomic through n=5, growing non-cyclotomic cofactor from n=6). Stage 6 (2026-06-28)
showed the tail is not a single low-order q-hypergeometric element and named the
cyclotomic-basis (q;q)_k expansion as the next decidable step; an external resurgence
dialog's "over ℤ" section (Habiro ring / q-Borel) independently points at the same basis.

THIS PROBE (exact sympy, no numerics in the expansion):
  1. Recomputes D(n), n = 4…9, from the categorical q-hook dim_q and verifies the
     published closed forms bit-for-bit (n=4: q²D(4)=(q−1)²Φ₃; n=5: q⁴D(5)=2(q−1)²Φ₂²Φ₃Φ₆).
  2. Normalizes P_n = q^{v(n)}·D(n) ∈ ℤ[q] (v(n) = −ldegree) and expands in the Habiro
     basis by successive division: c_k = P mod (1−q^{k+1}), P ← (P−c_k)/(1−q^{k+1}), so
     P_n = Σ_k c_k(q)·(q;q)_k with deg c_k ≤ k. Integrality is automatic (divisors have
     unit leading coefficient) — the CONTENT is the coefficient pattern:
     which c_k vanish, the expansion depth k_max(n), and the coefficient-height growth.
  3. Round-trips the expansion exactly and checks c₀ = 0 universally (the (q−1) root).

FINDING (scope-(a), exact): decidable Habiro-basis data for the tail — depth and height
tables; the growing depth is the basis-side face of the Stage-6–9 "no finite closed form"
verdict. No fit; no wiring; binding D(n) only (NOT the Q_β c_k ladder).

Audit: docs/audits/2026-07-12-alien-calculus-review-binding-gevrey-half.md
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
for p in (str(HERE / "substrate"), str(HERE)):
    if p not in sys.path:
        sys.path.insert(0, p)

import sympy as sp  # noqa: E402

q = sp.symbols('q')
NRANGE = range(4, 10)


def qint(k):
    return sp.cancel((q ** k - q ** (-k)) / (q - 1 / q))


def qfac(n):
    r = sp.Integer(1)
    for k in range(1, n + 1):
        r *= qint(k)
    return sp.cancel(r)


def partitions(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for r in partitions(n - k, k):
            yield (k,) + r


def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(row - j - 1) + (conj[j] - i - 1) + 1
            for i, row in enumerate(lam) for j in range(row)]


def dimq(lam):
    d = qfac(sum(lam))
    for h in hooks(lam):
        d = sp.cancel(d / qint(h))
    return d


def S(n):
    return sp.cancel(sum(dimq(l) for l in partitions(n)))


def habiro_expand(P):
    """P ∈ ℤ[q] → [c_0, c_1, ...] with P = Σ c_k·(q;q)_k, deg c_k ≤ k (successive division)."""
    R = sp.Poly(P, q)
    cs = []
    k = 0
    while not R.is_zero:
        div = sp.Poly(1 - q ** (k + 1), q)
        quo, rem = sp.div(R, div, q)
        cs.append(rem.as_expr())
        R = quo
        k += 1
    return cs


def pochhammer_qq(k):
    r = sp.Integer(1)
    for i in range(1, k + 1):
        r *= (1 - q ** i)
    return r


def main() -> int:
    print("=== lever-1: Habiro (q;q)_k-basis expansion of the binding tail D(n) ===\n")
    Sc = {n: S(n) for n in range(1, 10)}
    Phi = {m: sp.cyclotomic_poly(m, q) for m in (2, 3, 6)}

    results = {}
    closed_form_ok = True
    all_c0_zero = True
    roundtrip_ok = True

    print(f"  {'n':>2} {'v(n)':>4} {'deg P':>5} {'k_max':>5} {'first k≠0':>9} {'height':>8}  nonzero c_k (deg)")
    for n in NRANGE:
        D = sp.cancel(Sc[n] - Sc[n - 1] - qint(n - 1) * Sc[n - 2])
        num, den = sp.fraction(sp.together(D))
        # den is ± a power of q (Laurent); fold it in
        dpoly = sp.Poly(den, q)
        assert dpoly.length() == 1, f"non-monomial denominator at n={n}"
        v = dpoly.degree()
        sign = sp.sign(dpoly.LC())
        P = sp.expand(sign * num)          # P_n = q^{v}·D(n) ∈ ℤ[q]
        Ppoly = sp.Poly(P, q)
        assert all(c.is_Integer for c in Ppoly.all_coeffs()), f"non-integer P at n={n}"

        # closed-form verification (published table)
        if n == 4:
            closed_form_ok &= sp.expand(P - (q - 1) ** 2 * Phi[3]) == 0 and v == 2
        if n == 5:
            closed_form_ok &= sp.expand(
                P - 2 * (q - 1) ** 2 * Phi[2] ** 2 * Phi[3] * Phi[6]) == 0 and v == 4
        # universal (q−1)² root
        closed_form_ok &= sp.rem(P, (q - 1) ** 2, q) == 0

        cs = habiro_expand(P)
        rec = sp.expand(sum(c * pochhammer_qq(k) for k, c in enumerate(cs)))
        roundtrip_ok &= sp.expand(rec - P) == 0
        all_c0_zero &= cs[0] == 0
        nz = [(k, sp.degree(c, q) if c != 0 else -1) for k, c in enumerate(cs) if c != 0]
        height = max((max(abs(int(cc)) for cc in sp.Poly(c, q).all_coeffs())
                      for k, c in enumerate(cs) if c != 0), default=0)
        results[n] = {
            "v": int(v), "degP": int(Ppoly.degree()), "kmax": len(cs) - 1,
            "first_nonzero_k": nz[0][0] if nz else None,
            "height": int(height),
            "coeffs": {str(k): sp.srepr(c) if False else str(sp.expand(c))
                       for k, c in enumerate(cs) if c != 0},
        }
        print(f"  {n:>2} {v:>4} {Ppoly.degree():>5} {len(cs)-1:>5} "
              f"{nz[0][0] if nz else '-':>9} {height:>8}  "
              f"{[(k, d) for k, d in nz]}")

    print(f"\n  closed-form verification (n=4,5 vs published; (q−1)²|P_n all n): "
          f"{'PASS' if closed_form_ok else 'FAIL'}")
    print(f"  round-trip Σ c_k(q;q)_k = P_n exact: {'PASS' if roundtrip_ok else 'FAIL'}")
    print(f"  c₀ = 0 universally (the (q−1) root in the basis): "
          f"{'PASS' if all_c0_zero else 'FAIL'}")

    kmaxs = [results[n]["kmax"] for n in NRANGE]
    heights = [results[n]["height"] for n in NRANGE]
    depth_grows = all(kmaxs[i] <= kmaxs[i + 1] for i in range(len(kmaxs) - 1)) \
        and kmaxs[-1] > kmaxs[0]
    print(f"\n  depth k_max(n): {kmaxs} — growing; height: {heights}")
    print("  ⇒ the tail is Habiro-ring content of growing depth (basis-side face of the")
    print("    Stage-6–9 'no finite closed form' verdict); the normalization q^v(n) means")
    print("    these are expansions of q^{v}·D(n) — the Laurent tail itself lives in the")
    print("    q-localized completion.")

    ok = closed_form_ok and roundtrip_ok and all_c0_zero and depth_grows
    print(f"\n### Verdict: {'ALL CHECKS PASS' if ok else 'CHECK FAILED'}")

    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("lever1-habiro-tail-habiro-basis-expansion", engine="sympy")
        wb.set_description(
            "Lever-1 (z2bn): exact Habiro (q;q)_k-basis expansion of the binding tail D(n), "
            "n=4..9 (the Stage-6 queued next decidable; the external resurgence dialog's "
            "over-Z section points at the same basis). Recomputes D(n) from categorical q-hook "
            "dim_q, verifies the published closed forms (n=4: (q-1)^2 Phi3; n=5: "
            "2(q-1)^2 Phi2^2 Phi3 Phi6) and the universal (q-1)^2 root, then expands "
            "P_n=q^v D(n) in ZZ[q] by successive division by (1-q^(k+1)). Round-trip exact; "
            "c0=0 universally; depth k_max and coefficient height grow with n — the basis-side "
            "face of the no-finite-closed-form verdict. Exact symbolic; no fit; no wiring; "
            "binding D(n) only, not the Q_beta c_k ladder. Scope-(a).")
        for n in NRANGE:
            wb.add_data(f"n{n}", results[n])
        wb.add_data("depth_kmax_sequence", kmaxs)
        wb.add_data("height_sequence", heights)
        wb.add_assertion(
            name="habiro_basis_expansion_exact_c0_zero_depth_grows",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("closed forms verified (n=4,5) + (q-1)^2 root all n; round-trip exact; "
                    "c0=0 universally; depth k_max grows %s with heights %s."
                    % (kmaxs, heights)))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness skipped: {e})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
