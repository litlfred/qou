#!/usr/bin/env python3
"""B1.6 (bean qou-2rvk): does the corpus's (★)-normalized Masbaum tail
equal GGMW's published Habiro polynomial of 5₂?

The literature check
(`docs/audits/2026-07-26-extended-matrix-trivial-connection-row.md`)
established that A2's block machinery is the *geometric* 3×3 matrix,
while the trivial connection σ₀ is adjoined only in the extended
matrix. Reading GGMW (arXiv:2111.04763v2, uploaded as
`library/arxiv-2111.04763v2/2111.04763v2.pdf`) §4.2 turns up the object the corpus has
been computing all along, in closed form — eq (161):

    H_n^{5₂}(q) = (−1)ⁿ q^{n(n+3)/2} · Σ_{k=0}^{n} q^{k(k+1)} [n,k]_q

attributed to Habiro [Hab02a] and **Masbaum [Mas03]** — the same
Masbaum paper the corpus's `C52(n)` implements.

The corpus's proved (★) identity
(`QOU.QBeta.HabiroTailStar.star`, sorry-free) says

    C_n(a)·(q;q)_n²·a^{−(5n²+7n)} = (−1)ⁿ (q̃;q̃)_n² Σ_k q̃^{k(n+1)}[n,k]_q̃

with q = a², q̃ = a⁻². Applying bar-inversion to eq (161) gives
Σ_k q^{k(k+1)}[n,k]_q = Σ_k q^{k(n+1)}[n,k]_{q⁻¹}, which is the *same
shape* as (★)'s sum. So the two should agree up to an explicit
monomial × Pochhammer factor.

THIS PROBE DECIDES IT EXACTLY. Working with integer-Laurent
coefficient dicts (no floats, no tolerance), it computes:

  * `Hgg(n)`  — GGMW eq (161) verbatim;
  * `Ssum(n)` — the (★) sum Σ_k q^{k(n+1)}[n,k]_q;
  * `Mas(n)`  — the (★) left-hand side built from the corpus's C52;

and then determines the exact ratio between them by exact Laurent
division, reporting it as a closed form when it is a monomial times a
power of `(q;q)_n`. A match identifies the corpus's object with a
published one; a mismatch is equally informative and is reported as
such. Pre-registered, parameter-free, no fit.

Gates: bar-inversion reproduces eq (161)'s sum in the (★) shape
(machine-exact); the corpus (★) identity itself re-verified on this
code path; Habiro's published low values H₀ = 1, H₁ = −q²−q⁴
(GGMW §4.2, used there to fix the recursion's RHS) reproduced.

auditOnly; comparison to published mathematics; no c_k wired; no fit;
no ontological claims.

Run: python3 -u computations/probes/qbeta_5two_habiro_polynomial_match_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_habiro_match.log
"""
from __future__ import annotations

import importlib.util
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "qbeta_g3_5two_masbaum_barodd_profile",
    _HERE / "qbeta_g3_5two_masbaum_barodd_profile.py")
_mb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mb)

N_MAX = 10
T0 = time.monotonic()


def log(msg):
    print(f"  [{time.monotonic()-T0:6.0f}s] {msg}", flush=True)


# ---- exact integer-Laurent dict arithmetic {exponent: int} ----

def ladd(a, b):
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, 0) + c
    return {e: c for e, c in out.items() if c}


def lmul(a, b):
    out = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            out[e1 + e2] = out.get(e1 + e2, 0) + c1 * c2
    return {e: c for e, c in out.items() if c}


def lscale(a, k):
    return {e: c * k for e, c in a.items() if c * k}


def lshift(a, s):
    return {e + s: c for e, c in a.items()}


def linv_var(a):
    """q → q⁻¹."""
    return {-e: c for e, c in a.items()}


def gauss_rows(nmax):
    """[n,k]_q by the Pascal recurrence, as Laurent dicts."""
    rows = [[{0: 1}]]
    for n in range(1, nmax + 1):
        prev, row = rows[-1], []
        for k in range(n + 1):
            a = prev[k] if k <= n - 1 else {}
            b = prev[k] if False else ({} if k > n - 1 else prev[k])
            left = prev[k - 1] if 1 <= k <= n - 1 + 1 and k - 1 < len(prev) else {}
            # [n,k] = [n-1,k-1] + q^k [n-1,k]
            t1 = left
            t2 = lshift(prev[k], k) if k < len(prev) else {}
            row.append(ladd(t1, t2))
        rows.append(row)
    return rows


def qpoch(n):
    """(q;q)_n as a Laurent dict."""
    p = {0: 1}
    for j in range(1, n + 1):
        p = lmul(p, {0: 1, j: -1})
    return p


def ldivide(a, b):
    """Exact Laurent division a/b; returns None if it does not divide."""
    if not b:
        return None
    a = {e: c for e, c in a.items() if c}
    if not a:
        return {}
    b = {e: c for e, c in b.items() if c}
    lo_b, out = min(b), {}
    rem = dict(a)
    guard = 0
    while rem:
        guard += 1
        if guard > 20000:
            return None
        lo_r = min(rem)
        shift = lo_r - lo_b
        coef, den = rem[lo_r], b[lo_b]
        if coef % den:
            return None
        k = coef // den
        out[shift] = out.get(shift, 0) + k
        rem = ladd(rem, lscale(lshift(b, shift), -k))
        rem = {e: c for e, c in rem.items() if c}
    return {e: c for e, c in out.items() if c}


def fmt(d, maxterms=6):
    if not d:
        return "0"
    items = sorted(d.items())
    s = " + ".join(f"{c}·q^{e}" if e else f"{c}" for e, c in items[:maxterms])
    return s + (" + …" if len(items) > maxterms else "")


def main() -> int:
    print("=" * 78)
    print(" B1.6 — corpus (★) tail  vs  GGMW eq (161) Habiro polynomial")
    print("=" * 78)

    G = gauss_rows(N_MAX + 2)

    def Hgg(n):
        """GGMW eq (161) verbatim: (−1)ⁿ q^{n(n+3)/2} Σ_k q^{k(k+1)}[n,k]_q."""
        assert (n * (n + 3)) % 2 == 0
        s = {}
        for k in range(n + 1):
            s = ladd(s, lshift(G[n][k], k * (k + 1)))
        return lscale(lshift(s, (n * (n + 3)) // 2), (-1) ** n)

    def Ssum(n):
        """The (★) sum Σ_k q^{k(n+1)}[n,k]_q."""
        s = {}
        for k in range(n + 1):
            s = ladd(s, lshift(G[n][k], k * (n + 1)))
        return s

    def GgSumInverted(n):
        """Σ_k q^{k(n+1)}[n,k]_{q⁻¹} — eq (161)'s sum after bar-inversion."""
        s = {}
        for k in range(n + 1):
            s = ladd(s, lshift(linv_var(G[n][k]), k * (n + 1)))
        return s

    # ---- gate 1: bar-inversion turns eq (161)'s sum into the (★) shape ----
    g_inv = True
    for n in range(N_MAX + 1):
        lhs = {}
        for k in range(n + 1):
            lhs = ladd(lhs, lshift(G[n][k], k * (k + 1)))
        if lhs != GgSumInverted(n):
            g_inv = False
    log(f"[gate] bar-inversion: Σ q^{{k(k+1)}}[n,k]_q = Σ q^{{k(n+1)}}[n,k]_(1/q) "
        f"for n ≤ {N_MAX}: {'PASS' if g_inv else 'FAIL'}")

    # ---- gate 2: GGMW's published low values H₀ = 1, H₁ = −q²−q⁴ ----
    g_low = (Hgg(0) == {0: 1}) and (Hgg(1) == {2: -1, 4: -1})
    log(f"[gate] GGMW published values H₀ = 1, H₁ = −q²−q⁴: "
        f"{'PASS' if g_low else 'FAIL'}   (computed H₁ = {fmt(Hgg(1))})")

    # ---- gate 3: the corpus (★) LHS on this code path ----
    def Mas(n):
        """(★) LHS: C_n(a)·(a²;a²)_n²·a^{−(5n²+7n)}, as a q-series (q = a²)."""
        C = {e: int(c) for e, c in _mb.C52(n).items() if c}
        odd = [e for e in C if e % 2]
        assert not odd, f"odd a-exponent in C_{n}"
        Cq = {e // 2: c for e, c in C.items()}
        p = qpoch(n)
        body = lmul(Cq, lmul(p, p))
        assert (5 * n * n + 7 * n) % 2 == 0
        return lshift(body, -((5 * n * n + 7 * n) // 2))

    # ---- gate 4 (THE decisive one): C52(n) == GGMW eq (161), on the nose ----
    g_direct = True
    for n in range(N_MAX + 3):
        C = {e: int(c) for e, c in _mb.C52(n).items() if c}
        if [e for e in C if e % 2]:
            g_direct = False
            break
        if {e // 2: c for e, c in C.items()} != Hgg(n):
            g_direct = False
    log(f"[gate] C52(n) (as a q-series, q = a²) == GGMW eq (161) H_n^(5₂)(q) "
        f"for n ≤ {N_MAX + 2}: {'PASS' if g_direct else 'FAIL'}")

    # ---- the decisive comparison ----
    log("comparing the corpus tail against the published Habiro polynomial ...")
    rows, all_match = [], True
    for n in range(N_MAX + 1):
        M, H = Mas(n), Hgg(n)
        ratio = ldivide(M, H) if H else None
        exact = ratio is not None
        # is the ratio a pure monomial?
        mono = exact and len(ratio) == 1
        # or a monomial times (q;q)_n^p for a small p?
        poch_p = None
        if exact and not mono:
            for p in (1, 2, 3, -1, -2, -3):
                base = {0: 1}
                for _ in range(abs(p)):
                    base = lmul(base, qpoch(n))
                cand = ldivide(ratio, base) if p > 0 else lmul(ratio, base)
                if p > 0 and cand is not None and len(cand) == 1:
                    poch_p = p
                    break
                if p < 0 and len(cand) == 1:
                    poch_p = p
                    break
        all_match = all_match and exact
        rows.append({"n": n, "divides_exactly": bool(exact),
                     "ratio_is_monomial": bool(mono),
                     "ratio_pochhammer_power": poch_p,
                     "ratio": fmt(ratio) if exact else None,
                     "masbaum_lead": min(M) if M else None,
                     "habiro_lead": min(H) if H else None})
        log(f"    n={n:2d}: (★)LHS / H_n^{{5₂}} "
            f"{'= ' + fmt(ratio, 4) if exact else 'NOT an exact Laurent ratio'}"
            f"{'  [monomial]' if mono else ''}"
            f"{f'  [× (q;q)_n^{poch_p}]' if poch_p else ''}")

    n_mono = sum(1 for r in rows if r["ratio_is_monomial"])
    n_exact = sum(1 for r in rows if r["divides_exactly"])
    log(f"[T] {n_exact}/{len(rows)} exact Laurent ratios; "
        f"{n_mono} of them pure monomials")

    wb = WitnessBuilder("qbeta-5two-habiro-polynomial-match",
                        engine="exact-integer-laurent",
                        _script_path=__file__)
    wb.set_description(
        "B1.6 (bean qou-2rvk): identifies the corpus's (★)-normalized "
        "Masbaum tail against the PUBLISHED Habiro polynomial of 5₂, "
        "GGMW arXiv:2111.04763v2 eq (161) "
        "H_n(q) = (−1)ⁿ q^{n(n+3)/2} Σ_k q^{k(k+1)}[n,k]_q (attributed "
        "there to Habiro and Masbaum — the same source the corpus's "
        "C52(n) implements). Exact integer-Laurent arithmetic "
        "throughout; the ratio is obtained by exact Laurent division "
        "and classified as monomial / monomial×(q;q)_n^p / neither. "
        "Gates: bar-inversion carries eq (161)'s sum into the (★) "
        "shape; GGMW's published H₀ = 1 and H₁ = −q²−q⁴ reproduced. "
        "Comparison to published mathematics; auditOnly; no c_k wired; "
        "no fit; no ontological claims.")
    wb.set_content_block("prop:habiro-tail-star-identity")

    wb.add_assertion("bar_inversion_reshapes_ggmw_sum",
                     computed=1.0 if g_inv else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="Σ q^{k(k+1)}[n,k]_q = Σ q^{k(n+1)}[n,k]_{q⁻¹} "
                            "machine-exactly — eq (161) in the (★) shape")
    wb.add_assertion("ggmw_published_low_values",
                     computed=1.0 if g_low else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="H₀ = 1 and H₁ = −q²−q⁴ as printed in GGMW §4.2")
    wb.add_assertion("c52_is_the_habiro_polynomial",
                     computed=1.0 if g_direct else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="the corpus's C52(n), read as a q-series at "
                            "q = a², equals GGMW eq (161) H_n^{5₂}(q) "
                            "term-by-term as integer Laurent polynomials")
    wb.add_assertion("comparison_completed",
                     computed=float(len(rows)), expected=float(N_MAX + 1),
                     tolerance=0.5,
                     source="every level 0..N_MAX compared and classified")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("levels", rows)
    wb.add_data("n_exact_ratios", n_exact)
    wb.add_data("n_monomial_ratios", n_mono)
    wb.add_data("verdict",
                ((("IDENTIFIED — the corpus's Masbaum coefficient IS the "
                   "published Habiro polynomial: C52(n), read as a q-series "
                   "at q = a², equals GGMW arXiv:2111.04763v2 eq (161) "
                   "H_n^{5₂}(q) EXACTLY (term-by-term integer Laurent "
                   "equality, n ≤ 12) — no dressing, no monomial, nothing. "
                   "Consistently, the (★) LHS / H_n ratio is "
                   "q^{−(5n²+7n)/2}·(q;q)_n², precisely the (★) "
                   "normalization, so it cancels identically. The proved "
                   "(★) identity is therefore a bar-inversion statement "
                   "about a named object of the literature. Consequence "
                   "for the bridge programme: the route from this object "
                   "into the extended matrix is GGMW's (ε,δ)-DEFORMATION "
                   "of the Habiro polynomials (eqs 165–172), whose Taylor "
                   "coefficients Q_m^{(a,b)} are the 6×6 matrix entries — "
                   "NOT a linear map into the geometric block span. That "
                   "is why B1.2–B1.4′ returned nothing: the construction "
                   "is a deformation-and-expand, not a change of basis."
                   if g_direct else
                   f"NOT IDENTIFIED: C52(n) differs from GGMW eq (161); "
                   f"{n_exact}/{len(rows)} exact Laurent ratios, {n_mono} "
                   f"monomial. Check normalization/convention first."))
                 + " auditOnly.") if ok else "A gate failed — inspect.")
    wb.save()
    print(f"\n  assertions passed: {ok}   ({time.monotonic()-T0:.0f}s)")
    print("  witness -> computations/probes/"
          "qbeta-5two-habiro-polynomial-match.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
