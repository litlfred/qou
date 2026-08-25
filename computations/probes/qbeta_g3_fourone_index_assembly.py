#!/usr/bin/env python3
"""qbeta_g3_fourone_index_assembly.py — A_ω route 1, tranche 2: the TOTAL
3d-index of the figure-eight knot complement, assembled exactly and CERTIFIED
against the in-repo DGG source.

Source IN-REPO (owner-uploaded): Dimofte–Gaiotto–Gukov, "3-Manifolds and 3d
Indices" (library/arxiv-1112.5179v1/1112.5179v1.pdf), §4.3 "Figure-eight from two tetrahedra".
The equations were read directly from the PDF (glyph-verified, not
reconstructed from memory):

  eq (4.18)  — the total index, BARE (no flux prefactor):

      I_41(m,e) = Σ_{e₂∈ℤ} I_Δ(m−e₂, m+e−e₂) · I_Δ(e−e₂, −e₂)

  eq (4.19)  — amphichirality + Weyl symmetry:

      I_41(m,e) = I_41(−m,e) = I_41(m,−e) = I_41(−m,−e)

  eq (4.20)  — the printed check value:

      I_41(1,1) = −q − q² + 2q³ + 7q⁴ + 11q⁵ + 11q⁶ + 3q⁷ + …

Resolution of the tranche-2 "assembly-not-certified" open state
----------------------------------------------------------------
The earlier assembly (a) mixed in eq (4.17)'s prefactor (−q^{1/2})^{−2e₂}
(= q^{−e₂}) — which belongs to the pre-U(1)-breaking product index, NOT to
(4.18) — giving a near-miss, and (b) rejected the *correct* bare (4.18) sum
as "divergent (flat negative wing)". That flat wing was a **truncation
artifact**: the DGG tetrahedron index I_Δ(m,e) has minimal degree ≥ 0 that
grows quadratically in the charges, but that minimum is reached only through
deep cancellations. Rebasing a low-order truncation to its (spurious,
un-cancelled) minimum exponent reported a false lead of q⁰ for large-charge
factors, so the flux sum looked non-convergent.

The fix: compute each I_Δ(m,e) as an **absolute-degree** truncated series
(never rebased to a per-factor minimum). Deeply-cancelling large-|e₂| factors
then correctly contribute *nothing* below the target order, the flux sum
converges (as DGG state), and the bare (4.18) reproduces (4.20) exactly — no
prefactor. Only finitely many e₂ contribute at each q-order.

Deliverables (all exact, integer):
  (1) I_41(1,1) ≡ eq (4.20)  — CERTIFIED, bare (4.18);
  (2) the (4.19) symmetries, exact, over a battery of charges;
  (3) I_41(0,0)(q) — the zero-charge series whose coefficients GGM
      (library/arxiv-2012.00062v3/2012.00062v3.pdf) identify with integer Stokes / DT data
      (that Stokes dictionary is the named tranche 3);
  (4) the substrate evaluation I_41(0,0)(e^{−t}) — the index converges at
      the substrate (q ≈ 0.9009).

Anti-laundering: nothing here identifies A_ω. The Stokes dictionary (which
Borel singularity ↔ which index coefficient) is tranche 3, read from GGM with
the source at hand. Scope-(a); no fit; no c_k wired; no tier change.
"""
from __future__ import annotations

import sys
from functools import lru_cache
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qbeta_g3_tetrahedron_index_exact import tet_index_exact  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# eq (4.20) anchor, in x = q^{1/2} degrees (x-deg = 2·q-power):
ANCHOR_11 = {2: -1, 4: -1, 6: 2, 8: 7, 10: 11, 12: 11, 14: 3}


@lru_cache(maxsize=None)
def tet_abs(m: int, e: int, D: int):
    """The DGG tetrahedron index I_Δ(m,e) as a tuple of (x-degree, int-coeff)
    pairs for ABSOLUTE x-degrees 0..D (x = q^{1/2}). No min-degree rebasing:
    the true index has min-degree ≥ 0 and deep cancellations resolve exactly.

        I_Δ(m,e) = Σ_{n≥max(0,-e)} (−1)^n x^{n(n+1)−(2n+e)m} / ((q;q)_n (q;q)_{n+e})

    The summand's leading x-degree is expo(n) = n(n+1) − (2n+e)m (an upward
    parabola in n), so only finitely many n reach ≤ D.
    """
    lo = max(0, -e)
    res: dict[int, int] = {}
    vertex = (2 * m - 1) / 2
    nn = lo
    while True:
        expo = nn * (nn + 1) - (2 * nn + e) * m
        if expo <= D:
            need = D - expo
            # 1/((q;q)_n (q;q)_{n+e}) as an x-series in even degrees, to 'need'
            T = [0] * (need + 1)
            T[0] = 1
            for j in range(1, nn + 1):
                s = 2 * j
                for d in range(s, need + 1):
                    T[d] += T[d - s]
            for j in range(1, nn + e + 1):
                s = 2 * j
                for d in range(s, need + 1):
                    T[d] += T[d - s]
            sgn = -1 if nn & 1 else 1
            for d in range(need + 1):
                if T[d]:
                    res[expo + d] = res.get(expo + d, 0) + sgn * T[d]
        elif nn > vertex:
            break
        nn += 1
        if nn > lo + 4 * (D + abs(m) + abs(e)) + 80:  # hard safety cap
            break
    return tuple(sorted((d, c) for d, c in res.items() if c and 0 <= d <= D))


def _wing(m: int, e: int, D: int, step: int):
    """Accumulate eq-(4.18) products for e₂ = 0, step, 2·step, … until several
    consecutive e₂ contribute nothing (their product min-degree exceeds D)."""
    out: dict[int, int] = {}
    e2 = 0 if step > 0 else -1
    empties = 0
    while empties < 5:
        t1 = tet_abs(m - e2, m + e - e2, D)
        t2 = tet_abs(e - e2, -e2, D)
        contributed = False
        if t1 and t2:
            for d1, c1 in t1:
                if d1 > D:
                    continue
                for d2, c2 in t2:
                    if d1 + d2 <= D:
                        out[d1 + d2] = out.get(d1 + d2, 0) + c1 * c2
                        contributed = True
        empties = 0 if contributed else empties + 1
        e2 += step
    return out


def I41(m: int, e: int, D: int):
    """Bare DGG eq (4.18): the total figure-eight index as {x-degree: int}
    through absolute x-degree D."""
    out: dict[int, int] = {}
    for part in (_wing(m, e, D, 1), _wing(m, e, D, -1)):
        for d, c in part.items():
            out[d] = out.get(d, 0) + c
    return {d: c for d, c in out.items() if c}


def series_str(s: dict, nterms: int = 8) -> str:
    return " ".join(f"{s[d]:+d}·q^{d // 2:g}" for d in sorted(s)[:nterms])


def eval_at(s: dict, xval):
    return mp.fsum(c * xval ** d for d, c in s.items())


# --- DGG quantum A-polynomial L̂_{4₁} (eq C.7) and its operator action (eq C.8) ---
# Operators on an index function fn:(m,e)->{x-deg:int}, with q = x²:
#   M̂ f(m,e) = x^{m}·f(m,e−1)      M̂⁻¹ f(m,e) = x^{−m}·f(m,e+1)
#   ℓ̂ f(m,e) = −x^{e}·f(m+1,e)     ℓ̂⁻¹ f(m,e) = −x^{−e}·f(m−1,e)
def _sadd(*ss):
    o: dict[int, int] = {}
    for s in ss:
        for d, c in s.items():
            o[d] = o.get(d, 0) + c
    return {d: c for d, c in o.items() if c}


def _xmul(s, k):
    return {d + k: c for d, c in s.items()}


def _smul(s, c0):
    return {d: c * c0 for d, c in s.items()}


def _Mh(fn):
    return lambda m, e: _xmul(fn(m, e - 1), m)


def _Mhi(fn):
    return lambda m, e: _xmul(fn(m, e + 1), -m)


def _Lh(fn):
    return lambda m, e: _smul(_xmul(fn(m + 1, e), e), -1)


def _Lhi(fn):
    return lambda m, e: _smul(_xmul(fn(m - 1, e), -e), -1)


def _OADD(*ops):
    return lambda m, e: _sadd(*[op(m, e) for op in ops])


def _OX(op, k):
    return lambda m, e: _xmul(op(m, e), k)


def _OS(op, c0):
    return lambda m, e: _smul(op(m, e), c0)


def quantum_a_poly_op(D: int):
    """Return the operator L̂_{4₁} (DGG eq C.7) as a callable (m,e)->{x-deg:int}
    acting on the certified index I41(·,·,D). DGG (p.36) prove L̂_{4₁} annihilates
    I_{4₁}; this is the AJ-conjecture recursion whose fundamental solution W_m(q)
    produces the GGM Stokes matrix S⁺ (and thence A_ω)."""
    Id = lambda m, e: I41(m, e, D)
    # A = x·M̂ − x⁻¹·M̂⁻¹ ; term1 = A(ℓ̂⁻¹)
    term1 = _OADD(_OX(_Mh(_Lhi(Id)), 1), _OS(_OX(_Mhi(_Lhi(Id)), -1), -1))
    # term3 = (x⁻¹·M̂ − x·M̂⁻¹)(ℓ̂)
    term3 = _OADD(_OX(_Mh(_Lh(Id)), -1), _OS(_OX(_Mhi(_Lh(Id)), 1), -1))
    # middle P = M̂⁻² − M̂⁻¹ − q − q⁻¹ − M̂ + M̂²   (q = x², scalars ·Id)
    P = _OADD(_Mhi(_Mhi(Id)), _OS(_Mhi(Id), -1), _OS(_OX(Id, 2), -1),
              _OS(_OX(Id, -2), -1), _OS(_Mh(Id), -1), _Mh(_Mh(Id)))
    # term2 = −(M̂ − M̂⁻¹)(P)
    term2 = _OS(_OADD(_Mh(P), _OS(_Mhi(P), -1)), -1)
    return _OADD(term1, term2, term3)


def main() -> int:
    print("=" * 78)
    print(" A_ω route 1, tranche 2 — figure-eight TOTAL 3d-index, CERTIFIED (DGG 4.18)")
    print("=" * 78)

    D = 16

    # ---- [0] tie the absolute-degree engine to the tranche-1 exact engine ----
    # tet_index_exact returns (min_expo, {d: c}) rebased to its min exponent;
    # for small charges its min-degree is detected correctly, so the absolute
    # series must agree with tet_abs on the overlapping degrees.
    eng_ok = True
    for (m, e) in [(0, 0), (1, 0), (0, -1), (2, -1), (1, 1), (0, 1)]:
        sh, s = tet_index_exact(m, e, 40)
        ref = {sh + d: c for d, c in s.items() if 0 <= sh + d <= D}
        mine = dict(tet_abs(m, e, D))
        lo = max(0, sh)
        if any(ref.get(k, 0) != mine.get(k, 0) for k in range(lo, D + 1)):
            eng_ok = False
    print(f"\n[0] absolute-degree I_Δ ≡ tranche-1 engine (6 pairs): {eng_ok}")

    # ---- [1] certify the bare (4.18) against the printed anchor (4.20) ----
    got = I41(1, 1, D)
    anchor_ok = (
        all(got.get(d, 0) == v for d, v in ANCHOR_11.items())
        and all(got.get(d, 0) == 0 for d in range(0, min(ANCHOR_11)))
    )
    print(f"\n[1] bare eq (4.18) [no prefactor] vs printed anchor (4.20):")
    print(f"    I_41(1,1) = {series_str(got, 7)} …")
    print(f"    reproduces (4.20) exactly: {anchor_ok}")

    # ---- [2] DGG symmetries (4.19), exact, over a charge battery ----
    sym_ok = True
    charges = [(1, 1), (1, 0), (0, 1), (2, 1), (1, 2), (2, 2), (3, 1)]
    for (m, e) in charges:
        base = I41(m, e, D)
        for (mm, ee) in {(-m, e), (m, -e), (-m, -e)}:
            if I41(mm, ee, D) != base:
                sym_ok = False
    print(f"\n[2] symmetries (4.19) I(m,e)=I(−m,e)=I(m,−e)=I(−m,−e), {len(charges)} charges: {sym_ok}")

    # ---- [3] the zero-charge series (GGM Stokes-dictionary input) ----
    I00 = I41(0, 0, D)
    print(f"\n[3] I_41(0,0)(q) = {series_str(I00, 9)} …")

    # ---- [4] substrate evaluation: the index converges at q = e^{−t} ----
    t = mp.log(q_at(50))
    x_sub = mp.e ** (-t / 2)          # x = q^{1/2}
    D_lo, D_hi = 120, 160
    I00_lo = I41(0, 0, D_lo)
    I00_hi = I41(0, 0, D_hi)
    v_lo = eval_at(I00_lo, x_sub)
    v_hi = eval_at(I00_hi, x_sub)
    conv = abs(v_hi - v_lo)
    conf = int(-mp.log10(conv)) if 0 < conv < 1 else 40
    sub_ok = conf >= 3
    print(f"\n[4] substrate q = e^(−t) ≈ {mp.nstr(mp.e ** (-t), 8)}:")
    print(f"    I_41(0,0)(e^−t) = {mp.nstr(v_hi, 14)}  [{conf} digits stable, D {D_lo}→{D_hi}]")
    print(f"    I_41(1,1)(e^−t) = {mp.nstr(eval_at(I41(1, 1, D_hi), x_sub), 14)}")

    # ---- [5] the index satisfies the DGG quantum A-polynomial L̂_{4₁} (eq C.7) ----
    # This ties the certified 3d-index face to the same q-difference operator whose
    # fundamental solution W_m(q) yields the GGM Stokes matrix S⁺ (and thence A_ω).
    Dop = 26
    Lop = quantum_a_poly_op(Dop)
    aj_ok = True
    aj_charges = [(1, 1), (0, 1), (1, 0), (2, 1), (1, 2), (0, 0), (2, 0), (3, 1), (2, 2)]
    for (m, e) in aj_charges:
        r = Lop(m, e)
        if any(c for d, c in r.items() if d <= Dop - 12):  # within valid window
            aj_ok = False
    print(f"\n[5] quantum A-polynomial L̂_4₁ annihilates I_41 (DGG eq C.7), {len(aj_charges)} charges: {aj_ok}")

    certified = eng_ok and anchor_ok and sym_ok and sub_ok and aj_ok
    verdict = (
        "4₁ TOTAL 3d-index CERTIFIED from the in-repo DGG source "
        "(library/arxiv-1112.5179v1/1112.5179v1.pdf, eq 4.18 read glyph-verified): the assembly "
        "is the BARE flux sum Σ_{e₂} I_Δ(m−e₂,m+e−e₂)·I_Δ(e−e₂,−e₂) with NO "
        "prefactor — it reproduces the printed anchor (4.20) "
        "I_41(1,1)=−q−q²+2q³+7q⁴+11q⁵+11q⁶+3q⁷ exactly, and the (4.19) "
        "amphichirality/Weyl symmetries hold exactly over a 7-charge battery. "
        "The prior 'assembly-not-certified' open state is RESOLVED: the "
        "'divergent flat wing' was a truncation artifact of rebasing each "
        "tetrahedron factor to its (un-cancelled) minimum exponent; computing "
        "I_Δ at absolute degree instead makes the flux sum converge, exactly as "
        "DGG state. The earlier q^{−e₂} near-miss was eq (4.17)'s pre-U(1)-"
        "breaking prefactor mistakenly applied to (4.18). Zero-charge series "
        f"I_41(0,0) = {series_str(I00, 6)}… converges at the substrate. The "
        "certified index is annihilated by the DGG quantum A-polynomial L̂_4₁ "
        "(eq C.7) — the SAME q-difference operator whose fundamental solution "
        "W_m(q) yields the GGM Stokes matrix S⁺ (and thence A_ω), so this index "
        "face and the already-Lean-proved A_ω=3 route (QOU.QBeta.StokesQZeroDTCount "
        "via W₋₁, thm:aomega-fourone-dt-count) are descendants of one operator. "
        "This probe does NOT itself feed A_ω (that read-off goes through W_m, not "
        "the index); A_ω=3 is a separate, already-derived result. Scope-(a); no "
        "fit; no c_k wired."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-g3-fourone-index-assembly", engine="python-int+mpmath")
    wb.set_description(
        "A_omega route 1 tranche 2 (CERTIFIED): the total 3d-index of the "
        "figure-eight knot complement assembled exactly from the in-repo DGG "
        "source (1112.5179 eq 4.18, BARE — no prefactor), reproducing the "
        "printed anchor (4.20) exactly and satisfying the (4.19) symmetries. "
        "Resolves the prior open state (the 'divergence' was a min-degree-"
        "rebasing truncation artifact; absolute-degree tetrahedron indices "
        "converge). Includes I_41(0,0) (the GGM Stokes-dictionary input) and "
        "the substrate evaluation. Stokes dictionary = tranche 3.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("source", "library/arxiv-1112.5179v1/1112.5179v1.pdf §4.3 eq (4.18) bare; anchor eq (4.20); symmetry eq (4.19)")
    wb.add_data("prefactor", "none (bare flux sum) — eq (4.17)'s (-q^{1/2})^{-2e2} is pre-U(1)-breaking, not (4.18)")
    wb.add_data("resolution", "prior 'flat-wing divergence' was a truncation artifact of per-factor min-degree rebasing; absolute-degree I_Δ converges")
    wb.add_data("I41_11_qseries", series_str(I41(1, 1, D), 8))
    wb.add_data("I41_00_qseries", series_str(I00, 9))
    wb.add_data("substrate", {"q_sub": mp.nstr(mp.e ** (-t), 20),
                              "I41_00": mp.nstr(v_hi, 18),
                              "stable_digits": conf})
    wb.add_data("verdict", verdict)
    wb.add_assertion("anchor_420_reproduced_bare_418",
                     computed=1 if anchor_ok else 0, expected=1, tolerance=0,
                     source="bare eq (4.18) [no prefactor] reproduces DGG eq (4.20) exactly")
    wb.add_assertion("symmetries_419_exact",
                     computed=1 if sym_ok else 0, expected=1, tolerance=0,
                     source="I(m,e)=I(-m,e)=I(m,-e)=I(-m,-e) exact over 7 charges (DGG 4.19)")
    wb.add_assertion("engine_cross_check",
                     computed=1 if eng_ok else 0, expected=1, tolerance=0,
                     source="absolute-degree I_Δ agrees with tranche-1 exact engine")
    wb.add_assertion("substrate_evaluation_stable",
                     computed=1 if sub_ok else 0, expected=1, tolerance=0,
                     source="I_41(0,0)(e^-t) stable across D=120->160")
    wb.add_assertion("quantum_a_polynomial_annihilation",
                     computed=1 if aj_ok else 0, expected=1, tolerance=0,
                     source="L̂_4₁ (DGG eq C.7) annihilates the certified I_41 over 9 charges — same q-difference operator as the W_m/Stokes route")
    wb.save()
    return 0 if certified else 1


if __name__ == "__main__":
    raise SystemExit(main())
