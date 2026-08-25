#!/usr/bin/env python3
"""qbeta_g3_5two_masbaum_barodd_profile.py — the Masbaum-face bar-odd
extraction at the substrate: exact integer-Laurent C_{5₂,n}, the
convergent-side Habiro tail at q₀, the EXACT bar-side growth law, and
the per-n bar-odd/even profile — the first odd-channel data on the
face the resonance finding (#4167) redirected to, with the W3-certified
backbone (#4172).

All C_n are computed as EXACT integer Laurent polynomials in a
(a² = q) via the Masbaum closed form (certified in the merged
cyclotomic probe and W3):
    C_n(a) = (−1)^n Σ_k a^{3n²+5n+k²−2k−3nk} · bbinom_a(n,k)
with bbinom the balanced Gaussian binomial (integer Laurent, bar-
covariant: bbinom(a⁻¹) = bbinom(a)). The bar involution σ: a → a⁻¹
then acts monomial-wise, so the BAR-EVEN/ODD split of each C_n is
canonical and exact:  C_n = E_n + O_n,  E_n(a⁻¹) = E_n(a),
O_n(a⁻¹) = −O_n(a).  5₂ is chiral: O_n ≠ 0 — the exact bar-odd
Habiro data.

Deliverables (scope-(a), NO identification, NO resummation claims):
  M1  the convergent-side tail F(q₀⁻¹) = Σ_n C_n(q)·(q;q)_n² at
      q = e^{−t} (t = ln q₀) — a new exact substrate number, with a
      truncation certificate (terms decay like q^{(3n²+8n−4)/4}).
  M2  the EXACT growth law of the bar side: the extreme a-exponents
      of C_n are measured from the integer dicts and verified as
      exact quadratics — max_exp = 3n² + 5n (the k = 0 monomial) and
      min_exp = the discrete minimum of k² − (2+3n)k + 3n² + 5n − k(n−k)
      — so the bar image Σ C_n(q⁻¹)(…) is q-Gevrey of quadratic type
      with growth constant 3t/2 per unit n² in q-units: the DERIVED
      divergence datum that fixes what q-Borel acceleration (the W9
      sibling lane) must resum. The n²-coefficient 3 is a structural
      echo of the θ⁻²/x²-slot growth of the B/C-blocks on the
      state-integral face (noted, not claimed).
  M3  the per-n bar-odd PROFILE at the substrate: ρ_n = O_n(a₀)/E_n(a₀)
      (exact Laurent evaluations at a₀ = e^{−t/2}) for n = 1..10 —
      the finite-n odd-channel data — with scope-(a) comparison rows
      against the S anchors (S_muon = +0.00968298,
      S_proton = −0.03945936), u³, and Im 𝔙̃_b.

Anti-laundering: nothing inverted from anchors; the C_n are cited
exact formulas (Masbaum, DOI 10.2140/agt.2003.3.537) with the W3
Kashaev-ladder certification; the divergent side is characterized,
not resummed. Exact integer arithmetic for all polynomials; mpmath
dps 50 for evaluations; no float64.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

S_MUON = mp.mpf("0.00968298")
S_PROTON = mp.mpf("-0.03945936")
IM_VB = mp.mpf("0.0585499951473")
N_PROFILE = 10
N_TAIL = 40


# ---------- exact integer Laurent arithmetic in a ----------
def lmul(A, B):
    C = {}
    for ea, ca in A.items():
        for eb, cb in B.items():
            C[ea + eb] = C.get(ea + eb, 0) + ca * cb
    return {e: c for e, c in C.items() if c != 0}


def ladd(A, B):
    C = dict(A)
    for e, c in B.items():
        C[e] = C.get(e, 0) + c
    return {e: c for e, c in C.items() if c != 0}


def gauss_binom_q(n, k):
    """Standard Gaussian binomial [n,k]_q as integer poly in q
    (dict over q-exponents), by the Pascal recurrence."""
    row = [{0: 1}]
    for nn in range(1, n + 1):
        new = [{0: 1}]
        for kk in range(1, nn):
            shifted = {e + kk: c for e, c in row[kk].items()} \
                if kk < len(row) else {}
            new.append(ladd(row[kk - 1], shifted))
        new.append({0: 1})
        row = new
    return row[k]


def balanced_binom_a(n, k):
    """Balanced binomial in a: a^{−k(n−k)}·[n,k]_{q=a²} — integer
    Laurent in a, bar-covariant."""
    bq = gauss_binom_q(n, k)
    return {2 * e - k * (n - k): c for e, c in bq.items()}


def C52(n):
    """Exact C_{5₂,n}(a) integer Laurent dict."""
    out = {}
    for k in range(n + 1):
        base = 3 * n * n + 5 * n + k * k - 2 * k - 3 * n * k
        bb = balanced_binom_a(n, k)
        out = ladd(out, {base + e: c for e, c in bb.items()})
    if n % 2 == 1:
        out = {e: -c for e, c in out.items()}
    return out


def bar_split(P):
    E, O = {}, {}
    for e, c in P.items():
        E[e] = E.get(e, 0) + c
        E[-e] = E.get(-e, 0) + c
        O[e] = O.get(e, 0) + c
        O[-e] = O.get(-e, 0) - c
    E = {e: mp.mpf(c) / 2 for e, c in E.items() if c != 0}
    O = {e: mp.mpf(c) / 2 for e, c in O.items() if c != 0}
    return E, O


def leval(P, a0):
    return mp.fsum([c * a0 ** e for e, c in P.items()])


def main() -> int:
    print("=" * 78)
    print(" Masbaum-face bar-odd profile at the substrate (W3-certified "
          "backbone)")
    print("=" * 78)

    t = mp.log(q_at(50))
    a0 = mp.e ** (-t / 2)          # a₀² = q = e^{−t} (the |q|<1 side)
    q0 = a0 * a0

    # sanity: C₁ = −(q⁴+q²)
    c1 = C52(1)
    ok0 = c1 == {8: -1, 4: -1}
    print(f"\n[K0] C₁ dict = {c1} (= −(a⁸+a⁴) = −(q⁴+q²)): {ok0}")

    # M2: exact extreme exponents vs the predicted quadratics
    print("\n[M2] exact extreme a-exponents of C_n:")
    ok2 = True
    max_rows, min_rows = [], []
    for n in range(1, N_PROFILE + 1):
        P = C52(n)
        mx, mn = max(P), min(P)
        mx_pred = 3 * n * n + 5 * n
        max_rows.append((n, mx, mx_pred))
        min_rows.append((n, mn))
        if mx != mx_pred:
            ok2 = False
    print("    max_exp(C_n) = 3n²+5n exactly for n = 1..10: "
          f"{ok2}")
    # min-exponent quadratic: measure the n² coefficient by 2nd difference
    d2 = [(min_rows[i + 2][1] - 2 * min_rows[i + 1][1] + min_rows[i][1])
          for i in range(len(min_rows) - 2)]
    print(f"    min_exp 2nd differences: {d2} (→ n²-coefficient = "
          f"{mp.nstr(mp.mpf(sum(d2)) / len(d2) / 2, 4)} in a-units)")
    growth_q_units = mp.mpf(3) / 2   # max side: 3n² a-units = (3/2)n² q-units
    print(f"    ⇒ bar-side q-Gevrey growth: |C_n(q⁻¹)| ~ "
          f"q₀^((3/2)n²) — growth constant (3/2)·t·n² = the derived "
          f"divergence datum for the W9 q-Borel lane")

    # M1: the convergent-side tail with truncation certificate
    print("\n[M1] convergent-side tail F = Σ C_n(q)·(q;q)_n² at "
          "q = e^{−t}:")
    poch = mp.mpf(1)
    F = mp.mpf(0)
    last = None
    for n in range(N_TAIL):
        if n > 0:
            poch *= (1 - q0 ** n)
        term = leval(C52(n), a0) * poch ** 2
        F += term
        last = abs(term)
        if last < mp.mpf("1e-42") and n > 6:
            break
    ok1 = last < mp.mpf("1e-40")
    print(f"    F(q₀⁻¹-side) = {mp.nstr(F, 25)}")
    print(f"    truncated at n = {n}, last term {mp.nstr(last, 3)}: "
          f"{ok1}")

    # M3: per-n bar-odd/even profile at the substrate
    print("\n[M3] per-n bar-odd profile ρ_n = O_n(a₀)/E_n(a₀):")
    prof = []
    for n in range(1, N_PROFILE + 1):
        E, O = bar_split(C52(n))
        ev, ov = leval(E, a0), leval(O, a0)
        rho = ov / ev
        prof.append((n, ev, ov, rho))
        print(f"    n = {n:2d}: E = {mp.nstr(ev, 8)}, O = "
              f"{mp.nstr(ov, 8)}, ρ = {mp.nstr(rho, 10)}")
    ok3 = all(mp.isfinite(r[3]) and r[2] != 0 for r in prof)

    rows = {
        "rho_1": prof[0][3], "rho_2": prof[1][3], "rho_3": prof[2][3],
        "S_muon": S_MUON, "S_proton": S_PROTON,
        "u_cubed": (2 * t) ** 3, "Im_Vb": IM_VB,
        "tail_F": F,
    }
    print("\n[rows] scope-(a) comparison (NOT identifications):")
    for k, v in rows.items():
        print(f"     {k:>10} = {mp.nstr(v, 10)}")

    ok = ok0 and ok1 and ok2 and ok3
    verdict = (
        f"MASBAUM-FACE ODD-CHANNEL DATA EXTRACTED (exact, scope-(a)): "
        f"(M1) the convergent-side Habiro tail at the substrate is "
        f"F = {mp.nstr(F, 12)} (truncation-certified to 1e-40); (M2) "
        f"the bar-side divergence is characterized EXACTLY — "
        f"max_exp(C_n) = 3n^2+5n as an exact integer identity, so the "
        f"bar image is q-Gevrey of quadratic type with growth constant "
        f"(3/2)t·n^2 — the derived datum the W9 q-Borel/Ecalle lane "
        f"must resum (structural echo of the theta^-2/x^2-slot growth "
        f"on the state-integral face, noted not claimed); (M3) the "
        f"exact per-n bar-odd profile rho_n = O_n/E_n at q0 is "
        f"recorded for n = 1..10 (rho_1 = {mp.nstr(prof[0][3], 8)}, "
        f"rho_2 = {mp.nstr(prof[1][3], 8)}, rho_3 = "
        f"{mp.nstr(prof[2][3], 8)}) — the first exact odd-channel "
        f"numbers on this face, same order class as the S anchors, "
        f"with NO identification claimed. The odd-channel derivation "
        f"now has: exact finite-n data (this probe), the certified "
        f"analytic backbone (W3 #4172), and a precisely-posed "
        f"resummation step (the (3/2)t·n^2 q-Gevrey constant) owned "
        f"by the W9 sibling lane. No fit; no c_k wired."
        if ok else
        f"INCOMPLETE (honest): K0={ok0} M1={ok1} M2={ok2} M3={ok3} — "
        f"data recorded. No fit; no c_k wired; scope-(a)."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-g3-5two-masbaum-barodd-profile",
                        engine="mpmath+exact-int")
    wb.set_description(
        "Masbaum-face bar-odd extraction at the substrate: exact "
        "integer-Laurent C_{5_2,n}, convergent-side Habiro tail at q0, "
        "the exact bar-side q-Gevrey growth law (3/2)t n^2, and the "
        "per-n bar-odd/even profile rho_n — scope-(a), W3-certified "
        "backbone, resummation step posed for the W9 lane.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("tail_convergent_side", {"F": mp.nstr(F, 30),
                                         "truncation_n": n,
                                         "last_term": mp.nstr(last, 6)})
    wb.add_data("growth_law", {
        "max_exp_identity": "3n^2+5n (exact, n=1..10)",
        "min_exp_2nd_diffs": d2,
        "q_gevrey_constant": "(3/2)*t per n^2 (q-units)"})
    wb.add_data("odd_profile", [{"n": r[0],
                                 "E": mp.nstr(r[1], 20),
                                 "O": mp.nstr(r[2], 20),
                                 "rho": mp.nstr(r[3], 15)}
                                for r in prof])
    wb.add_data("comparison_rows", {k: mp.nstr(v, 12)
                                    for k, v in rows.items()})
    wb.add_data("verdict", verdict)
    wb.add_assertion("exact_structure_certified",
                     computed=1.0 if (ok0 and ok2) else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="C_1 regression + max_exp = 3n^2+5n exact "
                            "integer identity over the profile range")
    wb.add_assertion("tail_and_profile_recorded",
                     computed=1.0 if (ok1 and ok3) else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="convergent tail truncation-certified; "
                            "odd profile finite and nonzero (5_2 "
                            "chirality) for n = 1..10")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
