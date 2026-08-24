#!/usr/bin/env python3
"""qbeta_g3_tetrahedron_index_exact.py — A_ω route 1 (GGM 3d-index), tranche 1:
the DGG tetrahedron index as an EXACT integer q^{1/2}-series, with an exact
triality certificate, cross-implementation validation, and the substrate
evaluation q = e^{−t}.

Context (A_ω epic, bean qou-esx7 / route bean qou-zezz; duplication with
#3805's float scaffold `computations/probes/tetrahedron_index.py` is
owner-authorized — different context, and two INDEPENDENT implementations
agreeing is the strongest validation available while the literature hosts
are proxy-blocked).

The object:  I_Δ(m, e)(q) = Σ_{n≥max(0,−e)} (−1)^n
                 q^{ n(n+1)/2 − (n + e/2)·m } / ( (q;q)_n (q;q)_{n+e} ).

This tranche works in x = q^{1/2} with EXACT integer coefficients (the sum
telescopes to a Laurent-free ℤ[[x]] element for each (m,e) after clearing the
overall monomial): the 3d-index's defining virtue for the A_ω program is that
its Stokes data are INTEGERS, so the arithmetic should be integer-exact from
the start, not float.

Deliverables:
  (1) exact series for a battery of (m,e) (ORD adjustable);
  (2) EXACT triality certificate: which monomial-prefactor relation
      I_Δ(m,e) = ±x^k · I_Δ(m', e') holds as a series identity (the float
      harness in #3805 could only rank residuals; exact series DECIDES);
  (3) cross-implementation check vs an independent float evaluation at
      q = 1/10 (agreement of two implementations written independently);
  (4) the substrate evaluation q = e^{−t} (t = ln q₀ ⇒ q ≈ 0.9009, real,
      inside the unit disk — the index CONVERGES at the substrate; slow decay
      needs a deep truncation, handled).

Honest boundary (anti-fabrication): the m004 (4₁) TOTAL index requires the
flux-sum gluing rule (DGG §4.3 / Garoufalidis arXiv:1208.1663 §4) assembling
two I_Δ factors with the triangulation's NZ data. arXiv and the scholar
mirrors are proxy-blocked in this sandbox, and the rule will NOT be
reconstructed from memory — the assembly is the named next tranche, to be
done with the source at hand. Nothing here claims the 4₁ index or any Stokes
constant. Scope-(a); no fit; no c_k wired; no tier change.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

ORD = 240          # series order in x = q^{1/2}  (⇒ q-order 120)
ORD_SUB = 1700     # deep order for the substrate evaluation (q ≈ 0.9)


# ---------------- exact integer series in x = q^{1/2} (dict deg -> int) ----
def ser_mul(a, b, order):
    out = {}
    for da, ca in a.items():
        if da > order:
            continue
        for db, cb in b.items():
            d = da + db
            if d <= order:
                out[d] = out.get(d, 0) + ca * cb
    return out


def ser_inv_unit(a, order):
    """Inverse of a series with a(0) = 1, exact integer coefficients."""
    assert a.get(0) == 1
    inv = {0: 1}
    # Newton-free triangular inversion
    for d in range(1, order + 1):
        s = 0
        for k in range(1, d + 1):
            if k in a and (d - k) in inv:
                s += a[k] * inv[d - k]
        if s:
            inv[d] = -s
    return inv


def pochhammer_x(n, order):
    """(q;q)_n as a series in x (q = x²)."""
    out = {0: 1}
    for j in range(1, n + 1):
        out = ser_mul(out, {0: 1, 2 * j: -1}, order)
    return out


def tet_index_exact(m, e, order):
    """I_Δ(m,e) as (shift, dict): x^shift · Σ c_d x^d with c_d ∈ ℤ.
    The n-th term has x-exponent n(n+1) − (2n+e)m − (its Pochhammer part is
    unit-constant). Negative powers are handled by a global shift."""
    lo = max(0, -e)
    # collect terms as (exponent, series) then combine over a common shift
    terms = []
    min_expo = None
    for n in range(lo, order + 2):
        expo = n * (n + 1) - (2 * n + e) * m
        if min_expo is None or expo < min_expo:
            min_expo = expo
        # convergence: once expo - min_expo exceeds order for all larger n, stop.
        # exponent grows ~ n² for large n, so break when the quadratic dominates:
        if n > abs(m) + abs(e) + 2 and expo - min_expo > order:
            break
        inv = ser_inv_unit(
            ser_mul(pochhammer_x(n, order), pochhammer_x(n + e, order), order),
            order)
        terms.append((n, expo, inv))
    out = {}
    for n, expo, inv in terms:
        off = expo - min_expo
        sgn = -1 if n % 2 else 1
        for d, c in inv.items():
            dd = d + off
            if dd <= order:
                out[dd] = out.get(dd, 0) + sgn * c
    out = {d: c for d, c in out.items() if c != 0}
    return min_expo, out


def ser_eq(s1, s2, order):
    """Exact equality of (shift, dict) series through x^order (common frame)."""
    (sh1, a), (sh2, b) = s1, s2
    if sh1 != sh2:
        # re-align by shifting the smaller
        if sh1 < sh2:
            b = {d + (sh2 - sh1): c for d, c in b.items()}
            sh2 = sh1
        else:
            a = {d + (sh1 - sh2): c for d, c in a.items()}
            sh1 = sh2
    top = order - max(abs(sh1), abs(sh2))
    for d in range(0, top + 1):
        if a.get(d, 0) != b.get(d, 0):
            return False, d
    return True, None


def ser_scale_monomial(s, k, sign):
    """(±1)·x^k · s  for integer k (can be negative — adjust shift)."""
    sh, a = s
    return sh + k, ({d: sign * c for d, c in a.items()})


def eval_series(s, xval, order):
    sh, a = s
    tot = mp.mpf(0)
    for d in sorted(a):
        if d > order:
            break
        tot += a[d] * xval ** (d + sh)
    return tot


# ------------------------ independent float check (vs #3805's approach) ----
def tet_index_float(m, e, q, nmax=60):
    lo = max(0, -e)
    tot = mp.mpf(0)
    for n in range(lo, nmax + 1):
        den = mp.mpf(1)
        for j in range(1, n + 1):
            den *= (1 - q ** j)
        for j in range(1, n + e + 1):
            den *= (1 - q ** j)
        tot += (-1) ** n * q ** (mp.mpf(n * (n + 1)) / 2
                                 - (mp.mpf(n) + mp.mpf(e) / 2) * m) / den
    return tot


def main() -> int:
    print("=" * 78)
    print(" A_ω route 1, tranche 1 — exact-integer DGG tetrahedron index + triality")
    print("=" * 78)

    battery = [(0, 0), (0, 1), (1, 0), (0, -1), (1, 1), (2, -1), (1, -2), (-1, 2)]

    # ---- (1) exact series ----
    series = {}
    print(f"\n[1] exact ℤ[[x]] series (x = q^(1/2), ORD {ORD}):")
    for (m, e) in battery:
        sh, s = tet_index_exact(m, e, ORD)
        series[(m, e)] = (sh, s)
        lead = [f"{s.get(d, 0):+d}·x^{d + sh}" for d in sorted(s)[:6]]
        print(f"    I_Δ({m},{e}) = {' '.join(lead)} + …")

    # ---- (2) exact triality certificate ----
    # test I_Δ(m,e) ?= ±x^k · I_Δ(-e-m, m)  over k ∈ [-8, 8], sign ∈ {+,-}
    print("\n[2] exact triality certificate: I_Δ(m,e) vs ±x^k·I_Δ(−e−m, m):")
    found = {}
    all_consistent = True
    for (m, e) in battery:
        target = series[(m, e)]
        m2, e2 = -e - m, m
        sh2, s2 = tet_index_exact(m2, e2, ORD)
        hit = None
        for sign in (1, -1):
            for k in range(-8, 9):
                ok, _ = ser_eq(target, ser_scale_monomial((sh2, s2), k, sign),
                               ORD - 10)
                if ok:
                    hit = (sign, k)
                    break
            if hit:
                break
        found[(m, e)] = hit
        print(f"    ({m:>2},{e:>2}) → (−e−m, m) = ({m2:>2},{e2:>2}): "
              f"{'sign %+d, x^%d' % hit if hit else 'NO monomial relation ≤ |k|≤8'}")
        if hit is None:
            all_consistent = False
    # the certificate: for each battery element a relation exists, and the
    # (sign, k) pattern is the function of (m,e) the assembly tranche will use.
    triality_ok = all_consistent

    # ---- (3) cross-implementation check at q = 1/10 ----
    print("\n[3] cross-implementation: exact series vs independent float at q=0.1:")
    x01 = mp.sqrt(mp.mpf("0.1"))
    max_dev = mp.mpf(0)
    for (m, e) in battery:
        ex = eval_series(series[(m, e)], x01, ORD)
        fl = tet_index_float(m, e, mp.mpf("0.1"))
        dev = abs(ex - fl)
        max_dev = max(max_dev, dev)
    cross_ok = max_dev < mp.mpf("1e-30")
    print(f"    max |exact − float| over battery = {mp.nstr(max_dev, 4)}  ok={cross_ok}")

    # ---- (4) substrate evaluation q = e^{−t} ----
    t = mp.log(q_at(50))
    q_sub = mp.e ** (-t)
    x_sub = mp.e ** (-t / 2)
    print(f"\n[4] substrate: q = e^(−t) = {mp.nstr(q_sub, 12)} (|q|<1 ⇒ the index "
          f"CONVERGES at the substrate; tail x^{ORD_SUB} ≈ "
          f"{mp.nstr(x_sub ** ORD_SUB, 3)}):")
    sh00, s00 = tet_index_exact(0, 0, ORD_SUB)
    I00_sub = eval_series((sh00, s00), x_sub, ORD_SUB)
    # truncation control: drop the last 10% of orders and compare
    I00_sub_c = eval_series((sh00, {d: c for d, c in s00.items()
                                    if d <= ORD_SUB * 9 // 10}), x_sub, ORD_SUB)
    conv = abs(I00_sub - I00_sub_c)
    conf = int(-mp.log10(conv)) if 0 < conv < 1 else 40
    print(f"    I_Δ(0,0)(q_sub) = {mp.nstr(I00_sub, 20)}  [{conf} stable digits]")
    sub_ok = conf >= 8

    verdict = (
        f"Exact-integer DGG tetrahedron index established: ℤ[[x]] series for "
        f"{len(battery)} (m,e) pairs; EXACT triality certificate "
        f"({'all battery pairs satisfy a ±x^k monomial relation' if triality_ok else 'INCOMPLETE'}); "
        f"cross-implementation agreement with an independent float evaluation to "
        f"{mp.nstr(max_dev, 2)}; substrate evaluation I_Δ(0,0)(e^−t) = "
        f"{mp.nstr(I00_sub, 12)} [{conf}d] — the index converges AT the substrate "
        f"(q = e^−t ≈ 0.90). Honest boundary: the m004 flux-sum gluing rule (DGG "
        f"§4.3 / Garoufalidis 1208.1663 §4) is the named pending input — literature "
        f"hosts proxy-blocked, rule NOT reconstructed from memory; the 4₁ total "
        f"index and any Stokes constant remain unclaimed. Scope-(a); no fit; no "
        f"c_k wired."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-g3-tetrahedron-index-exact", engine="python-int+mpmath")
    wb.set_description(
        "A_omega route 1 tranche 1: exact-integer DGG tetrahedron index "
        "I_Delta(m,e) as Z[[x]] series (x=q^(1/2)), exact triality certificate "
        "(monomial-prefactor relation decided as a series identity), "
        "cross-implementation validation vs an independent float evaluation, and "
        "the substrate evaluation q=e^(-t) (converges at the substrate). The m004 "
        "flux-sum assembly is the named pending input (literature blocked; not "
        "reconstructed from memory). Duplication with #3805 owner-authorized.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("battery", [list(p) for p in battery])
    wb.add_data("series_leading_terms", {
        f"{m},{e}": {str(d + series[(m, e)][0]): series[(m, e)][1][d]
                     for d in sorted(series[(m, e)][1])[:10]}
        for (m, e) in battery})
    wb.add_data("triality_certificate", {
        f"{m},{e}": (list(found[(m, e)]) if found[(m, e)] else None)
        for (m, e) in battery})
    wb.add_data("cross_implementation_max_dev", mp.nstr(max_dev, 6))
    wb.add_data("substrate", {"q_sub": mp.nstr(q_sub, 20),
                              "I_delta_00": mp.nstr(I00_sub, 25),
                              "stable_digits": conf})
    wb.add_data("pending_input",
                "m004 flux-sum gluing rule (DGG sec 4.3 / Garoufalidis "
                "arXiv:1208.1663 sec 4) — required for the 4_1 total index; "
                "NOT reconstructed from memory (anti-fabrication)")
    wb.add_data("verdict", verdict)
    wb.add_assertion("triality_monomial_relation_all_pairs",
                     computed=1.0 if triality_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="exact series identity I(m,e) = ±x^k I(-e-m,m) found for every battery pair")
    wb.add_assertion("cross_implementation_agreement",
                     computed=1.0 if cross_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="exact-series evaluation matches independent float implementation < 1e-30 at q=0.1")
    wb.add_assertion("substrate_evaluation_stable",
                     computed=1.0 if sub_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="I_Delta(0,0)(e^-t) stable to >= 8 digits under 10% truncation drop")
    wb.save()
    return 0 if (triality_ok and cross_ok and sub_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
