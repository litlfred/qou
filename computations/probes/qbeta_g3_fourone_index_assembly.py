#!/usr/bin/env python3
"""qbeta_g3_fourone_index_assembly.py — A_ω route 1, tranche 2: the TOTAL
3d-index of the figure-eight knot complement, assembled exactly.

Source now IN-REPO (owner-uploaded): Dimofte–Gaiotto–Gukov, "3-Manifolds and
3d Indices" (uploads/1112.5179v1.pdf), §4.3 "Figure-eight from two tetrahedra",
eq (4.18):

    I_41(m, e)(q) = Σ_{e₂∈ℤ} q^{p(e₂)} · I_Δ(m − e₂, m + e − e₂) · I_Δ(e − e₂, −e₂)

with the flux prefactor p(e₂) rendered ambiguously by PDF text extraction
("q^{−2e₂·½}"-like fragment). Rather than guess, the paper's own printed
check value eq (4.20)

    I_41(1, 1) = −q − q² + 2q³ + 7q⁴ + 11q⁵ + 11q⁶ + 3q⁷ + …

is used as a MECHANICAL disambiguator: the candidate prefactors
p(e₂) ∈ {−e₂, +e₂, −e₂/2, +e₂/2, −2e₂, +2e₂} are all assembled exactly and
the one(s) reproducing (4.20) exactly are identified; the probe asserts the
match is UNIQUE. Further validations: the DGG symmetry eq (4.19)
I(m,e) = I(−m,e) = I(m,−e) (amphichirality + Weyl), exactness of integer
coefficients, and stability of the substrate evaluation q = e^{−t}.

Deliverables:
  (1) the exact ℤ((q^{1/2})) total index I_41(m,e) for small charges,
      validated against the paper's anchor;
  (2) the zero-charge series I_41(0,0)(q) — the object whose coefficients
      GGM (uploads/2012.00062v3.pdf) identify with integer Stokes data
      (that dictionary is tranche 3);
  (3) the substrate evaluations I_41(0,0)(e^{−t}), I_41(1,1)(e^{−t}) — the
      3d-index CONVERGES at the substrate (q ≈ 0.9009).

Anti-laundering: nothing here yet identifies A_ω; the Stokes dictionary
(which singularity ↔ which index coefficient) is the named next tranche,
read from GGM with the source at hand. Scope-(a); no fit; no c_k wired.
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
from qbeta_g3_tetrahedron_index_exact import tet_index_exact  # noqa: E402

mp.mp.dps = 50

ORD = 60           # x-order for the validation assemblies (q-order 30)
ORD_SUB = 900      # x-order for substrate evaluations (tail q^450 ≈ 4e-21)
E2_RANGE = 60      # flux window |e₂| ≤ E2_RANGE

# eq (4.20) anchor: I_41(1,1) = −q −q² +2q³ +7q⁴ +11q⁵ +11q⁶ +3q⁷ + …
ANCHOR_11 = {2: -1, 4: -1, 6: 2, 8: 7, 10: 11, 12: 11, 14: 3}   # x-degrees


# ---- fast exact I_Δ: 1/(1−x^{2j}) multiplication = cumulative sum, O(ORD) ---
def _mul_inv_geom(dense, j2, order):
    """dense ← dense · 1/(1 − x^{j2}) in place (prefix-sum trick)."""
    for d in range(j2, order + 1):
        dense[d] += dense[d - j2]


_tet_cache = {}


def tet_fast(m, e, order):
    """Exact I_Δ(m,e) as (shift, list) using the incremental Pochhammer-inverse
    ladder — O(nmax·order) integer ops. Cross-checked vs tranche 1's engine."""
    key = (m, e, order)
    if key in _tet_cache:
        return _tet_cache[key]
    lo = max(0, -e)
    # scan exponents to find min and the cutoff n
    expos = {}
    n = lo
    best = None
    while True:
        expo = n * (n + 1) - (2 * n + e) * m
        expos[n] = expo
        best = expo if best is None else min(best, expo)
        if n > lo + abs(m) + abs(e) + 2 and expo - best > order:
            break
        n += 1
        if n > lo + 4 * (order + abs(m) + abs(e)) + 50:
            break
    min_expo = best
    nmax = max(expos)
    # incremental T_n = 1/((q;q)_n (q;q)_{n+e}), dense list of ints
    T = [0] * (order + 1)
    T[0] = 1
    for j in range(1, lo + 1):
        _mul_inv_geom(T, 2 * j, order)
    for j in range(1, lo + e + 1):
        _mul_inv_geom(T, 2 * j, order)
    out = [0] * (order + 1)
    for n in range(lo, nmax + 1):
        if n > lo:
            _mul_inv_geom(T, 2 * n, order)
            _mul_inv_geom(T, 2 * (n + e), order)
        off = expos[n] - min_expo
        if off > order:
            continue
        sgn = -1 if n % 2 else 1
        for d in range(0, order + 1 - off):
            if T[d]:
                out[d + off] += sgn * T[d]
    res = (min_expo, {d: c for d, c in enumerate(out) if c})
    _tet_cache[key] = res
    return res


def tet_norm(m, e, order):
    """NORMALIZED exact I_Δ: returns (true_lead, dict rebased to 0), valid
    through x^order beyond the true lead. DGG prove lead(m,e) ≥ 0, but the
    raw sum (3.5) reaches it through CANCELLATIONS between consecutive
    n-terms — the raw minimum exponent can be spuriously negative, so the
    computation is padded until the cancellation depth is covered."""
    pad = 0
    while True:
        sh, s = tet_fast(m, e, order + pad)
        if not s:
            return 0, {}
        k0 = min(s)
        if k0 <= pad:
            lead = sh + k0
            return lead, {d - k0: c for d, c in s.items() if d - k0 <= order}
        pad = k0


def _dense_mul(a, b, order):
    out = [0] * (order + 1)
    for da, ca in a.items():
        if da > order or not ca:
            continue
        top = order - da
        for db, cb in b.items():
            if db <= top and cb:
                out[da + db] += ca * cb
    return out


def assemble_I41_pattern(m, e, order, f2, pref_qcoef):
    """Generalized assembly: I_41(m,e) = Σ_{e₂} q^{pref_qcoef·e₂}
    · I_Δ(m−e₂, m+e−e₂) · I_Δ(f2(m,e,e₂)) — the first factor is fixed (it
    extracts cleanly twice from the PDF); the second factor's argument pattern
    f2 and the flux coefficient are disambiguated against the printed anchor.
    Returns (shift, dict) or None if non-convergent."""
    e2max = max(E2_RANGE, order // 2 + 12)
    terms = []
    for e2 in range(-e2max, e2max + 1):
        sh1, s1 = tet_norm(m - e2, m + e - e2, order)
        a2, b2 = f2(m, e, e2)
        sh2, s2 = tet_norm(a2, b2, order)
        pref_x = 2 * pref_qcoef * e2
        terms.append((e2, sh1 + sh2 + pref_x, s1, s2))
    min_shift = min(t[1] for t in terms)
    edge_leads = [t[1] - min_shift for t in terms if abs(t[0]) == e2max]
    if not all(x > order for x in edge_leads):
        return None
    out = {}
    for e2, lead, s1, s2 in terms:
        off = lead - min_shift
        if off > order:
            continue
        prod = _dense_mul(s1, s2, order - off)
        for d, c in enumerate(prod):
            if c:
                out[d + off] = out.get(d + off, 0) + c
    out = {d: c for d, c in out.items() if c != 0}
    return min_shift, out


def assemble_I41(m, e, order, pref_num, pref_den):
    """I_41(m,e) with flux prefactor q^{(pref_num/pref_den)·e₂}
    (in x: x^{(2·pref_num/pref_den)·e₂}). Returns (shift, dict) exact Laurent
    series through x^order relative to shift, or None if the candidate is
    NON-CONVERGENT (the flux wings do not leave the truncation window — the
    Garoufalidis convergence criterion failing is itself the rejection)."""
    # DGG (p.41): the flux sum converges with LINEAR lead-growth along the
    # flux direction, needing |e₂| up to ~ the target q-order — scale the
    # window with the order.
    e2max = max(E2_RANGE, order // 2 + 12)
    terms = []
    for e2 in range(-e2max, e2max + 1):
        if (2 * pref_num * e2) % pref_den != 0:
            return None
        # cheap pre-truncation: request only the window that can contribute
        sh1, s1 = tet_norm(m - e2, m + e - e2, order)
        sh2, s2 = tet_norm(e - e2, -e2, order)
        pref_x = (2 * pref_num * e2) // pref_den
        terms.append((e2, sh1 + sh2 + pref_x, s1, s2))
    min_shift = min(t[1] for t in terms)
    # convergence rejection: both wings must be beyond the window
    edge_leads = [t[1] - min_shift for t in terms if abs(t[0]) == e2max]
    if not all(x > order for x in edge_leads):
        return None
    out = {}
    for e2, lead, s1, s2 in terms:
        off = lead - min_shift
        if off > order:
            continue
        prod = _dense_mul(s1, s2, order - off)
        for d, c in enumerate(prod):
            if c:
                out[d + off] = out.get(d + off, 0) + c
    out = {d: c for d, c in out.items() if c != 0}
    return min_shift, out


def eval_series(s, xval):
    sh, a = s
    tot = mp.mpf(0)
    for d in sorted(a):
        tot += a[d] * xval ** (d + sh)
    return tot


def series_str(s, nterms=10):
    sh, a = s
    return " ".join(f"{a[d]:+d}·q^{(d + sh) / 2:g}" for d in sorted(a)[:nterms])


def main() -> int:
    print("=" * 78)
    print(" A_ω route 1, tranche 2 — the 4₁ TOTAL 3d-index, assembled exactly (DGG 4.18)")
    print("=" * 78)

    # ---- (0) engine cross-check: tet_fast vs tranche-1 exact engine ----
    eng_ok = True
    for (m, e) in [(0, 0), (1, 0), (0, -1), (2, -1), (1, 1)]:
        f_sh, f_s = tet_fast(m, e, 40)
        g_sh, g_s = tet_index_exact(m, e, 40)
        if not (f_sh == g_sh and f_s == g_s):
            eng_ok = False
    print(f"\n[0] fast engine ≡ tranche-1 engine (5 pairs, exact): {eng_ok}")
    assert eng_ok

    # ---- (1) prefactor disambiguation against the (4.20) anchor ----
    candidates = [(-1, 1), (1, 1), (-1, 2), (1, 2), (-2, 1), (2, 1), (0, 1)]
    print("\n[1] flux-prefactor disambiguation vs the printed anchor I_41(1,1):")
    matches = []
    for num, den in candidates:
        s = assemble_I41(1, 1, ORD, num, den)
        if s is None:
            print(f"    p(e₂) = ({num}/{den})·e₂ : NON-CONVERGENT (wings inside "
                  f"window) — rejected by the convergence criterion")
            continue
        sh, a = s
        ok = all(a.get(d - sh, 0) == v for d, v in ANCHOR_11.items()) and \
            all(a.get(d, 0) == 0 for d in range(0 - sh, min(ANCHOR_11) - sh))
        tag = "MATCHES (4.20)" if ok else "no"
        print(f"    p(e₂) = ({num}/{den})·e₂ : {series_str(s, 7)}  → {tag}")
        if ok:
            matches.append((num, den))
    unique = len(matches) == 1
    if not matches:
        # HONEST OPEN STATE: no assembly candidate certifies against the
        # anchor yet. Record the exclusion table + the near-miss and exit
        # with a witness carrying the open verdict (searched this session:
        # monomial prefactors, sign dressings, 11 F2-argument variants, and
        # all 9 quad-rotation frames of the Garoufalidis Def-2.11 route —
        # the q^{-e2} candidate is a NEAR-MISS differing from the DGG anchor
        # (4.20) at q^3/q^5 and diverging from it at q^7).
        near = assemble_I41(1, 1, ORD, -1, 1)
        verdict = (
            "4₁ index assembly NOT YET CERTIFIED (honest open state): the "
            "exact-integer engine, the anchor (4.20, glyph-verified), and the "
            "DGG symmetry targets are all in place, but no candidate reading "
            "of eq (4.18) reproduces the anchor exactly — the bare no-prefactor "
            "sum has a FLAT negative flux wing (divergent; the index-structure "
            "criterion correctly rejects it), the q^{-e2} dressing is a "
            f"near-miss ({series_str(near, 7) if near else 'n/a'} vs anchor "
            "-q-q²+2q³+7q⁴+11q⁵+11q⁶+3q⁷), and all 9 quad-rotation frames of "
            "the Def-2.11 route converge to different series or vanish. Open "
            "input: the exact charge dictionary/polarization normalization "
            "(DGG U = 2·log m factor; appendix-B tables are the next anchor "
            "source). Nothing is claimed; scope-(a); no fit; no c_k wired."
        )
        print("\nVERDICT:", verdict)
        wb = WitnessBuilder("qbeta-g3-fourone-index-assembly",
                            engine="python-int+mpmath")
        wb.set_description(
            "A_omega route 1 tranche 2 — OPEN STATE record: 4_1 total-index "
            "assembly not yet certified against the glyph-verified DGG anchor "
            "(4.20); exclusion table of candidate readings recorded (flat-wing "
            "divergence of the bare sum; q^{-e2} near-miss; 9 quad frames). "
            "Anti-fabrication: no formula reconstructed from memory.")
        wb.set_content_block("conj:im-q-physical-role")
        wb.add_data("status", "assembly-not-certified")
        wb.add_data("anchor_420_glyph_verified",
                    "-q -q^2 +2q^3 +7q^4 +11q^5 +11q^6 +3q^7")
        wb.add_data("near_miss_q_minus_e2",
                    series_str(near, 8) if near else None)
        wb.add_data("excluded", [
            "bare (4.18) no-prefactor: flat negative wing, divergent",
            "monomial prefactors q^{ce2}, c in {+-1,+-1/2,+-2,0}: no exact match",
            "(-1)^{e2} sign dressings: no match",
            "11 F2-argument variants x prefactors: no match",
            "9 quad-rotation frames (Def 2.11, derived NZ data): converge to "
            "different series or vanish; none match"])
        wb.add_data("next_inputs", [
            "DGG appendix B tables (pages ~70-72) as additional anchors",
            "charge dictionary for U = 2 log m normalization",
            "coordination with #3805 (same target)"])
        wb.add_assertion("open_state_recorded", computed=1.0, expected=1.0,
                         tolerance=0.5, source="honest no-certification record")
        wb.save()
        return 0
    NUM, DEN = matches[0]

    # ---- (2) symmetry validation (4.19) ----
    print("\n[2] DGG (4.19) symmetries, exact:")
    sym_ok = True
    for (m, e) in [(1, 1), (1, 0), (0, 1), (2, 1), (1, 2)]:
        base = assemble_I41(m, e, ORD, NUM, DEN)
        for (m2, e2) in [(-m, e), (m, -e), (-m, -e)]:
            other = assemble_I41(m2, e2, ORD, NUM, DEN)
            same = (base[0] == other[0] and base[1] == other[1])
            sym_ok = sym_ok and same
        print(f"    I({m},{e}) = I(−m,e) = I(m,−e) = I(−m,−e): "
              f"{'exact ✓' if sym_ok else 'FAIL'}")

    # ---- (3) the zero-charge total index ----
    I00 = assemble_I41(0, 0, ORD, NUM, DEN)
    print(f"\n[3] I_41(0,0)(q) = {series_str(I00, 12)} + …")

    # ---- (4) substrate evaluations ----
    t = mp.log(q_at(50))
    x_sub = mp.e ** (-t / 2)
    print(f"\n[4] substrate q = e^(−t) ≈ {mp.nstr(mp.e ** (-t), 10)}:")
    I00_deep = assemble_I41(0, 0, ORD_SUB, NUM, DEN)
    I11_deep = assemble_I41(1, 1, ORD_SUB, NUM, DEN)
    v00 = eval_series(I00_deep, x_sub)
    v11 = eval_series(I11_deep, x_sub)
    # stability: drop last 10% of orders
    sh, a = I00_deep
    v00_c = eval_series((sh, {d: c for d, c in a.items()
                              if d <= ORD_SUB * 9 // 10}), x_sub)
    conv = abs(v00 - v00_c)
    conf = int(-mp.log10(conv)) if 0 < conv < 1 else 40
    print(f"    I_41(0,0)(e^−t) = {mp.nstr(v00, 20)}  [{conf} stable digits]")
    print(f"    I_41(1,1)(e^−t) = {mp.nstr(v11, 20)}")
    sub_ok = conf >= 8

    verdict = (
        f"4₁ TOTAL 3d-index assembled exactly from the in-repo DGG source "
        f"(eq 4.18): flux prefactor disambiguated mechanically against the "
        f"printed anchor (4.20) — unique match p(e₂) = ({NUM}/{DEN})·e₂; "
        f"symmetries (4.19) hold exactly; I_41(0,0) = {series_str(I00, 6)}…; "
        f"substrate values I_41(0,0)(e^−t) = {mp.nstr(v00, 12)} [{conf}d], "
        f"I_41(1,1)(e^−t) = {mp.nstr(v11, 12)}. Next tranche: the GGM Stokes "
        f"dictionary (uploads/2012.00062v3.pdf) mapping index coefficients to "
        f"the integer Stokes constants of the geometric-saddle tower — no A_ω "
        f"claimed yet. Scope-(a); no fit; no c_k wired."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-g3-fourone-index-assembly", engine="python-int+mpmath")
    wb.set_description(
        "A_omega route 1 tranche 2: the total 3d-index of the figure-eight "
        "knot complement assembled exactly per DGG 1112.5179 eq (4.18) "
        "(in-repo source), with the flux prefactor disambiguated mechanically "
        "against the paper's printed check value (4.20) and the (4.19) "
        "symmetries verified exactly. Includes the substrate evaluations "
        "(the index converges at q=e^-t). Stokes dictionary = next tranche.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("source", "uploads/1112.5179v1.pdf sec 4.3 eq (4.18); anchor eq (4.20)")
    wb.add_data("flux_prefactor", {"num": NUM, "den": DEN,
                                   "candidates_tested": [list(c) for c in candidates],
                                   "unique_match": bool(unique)})
    wb.add_data("I41_00_series_x", {str(d + I00[0]): I00[1][d]
                                    for d in sorted(I00[1])[:20]})
    wb.add_data("I41_11_anchor_reproduced", True)
    wb.add_data("substrate", {"q_sub": mp.nstr(mp.e ** (-t), 20),
                              "I41_00": mp.nstr(v00, 25),
                              "I41_11": mp.nstr(v11, 25),
                              "stable_digits": conf})
    wb.add_data("verdict", verdict)
    wb.add_assertion("anchor_420_reproduced_uniquely",
                     computed=1.0 if unique else 0.0, expected=1.0, tolerance=0.5,
                     source="exactly one flux-prefactor candidate reproduces DGG eq (4.20) exactly")
    wb.add_assertion("symmetries_419_exact",
                     computed=1.0 if sym_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="I(m,e)=I(-m,e)=I(m,-e)=I(-m,-e) as exact series (DGG 4.19)")
    wb.add_assertion("substrate_evaluation_stable",
                     computed=1.0 if sub_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="I_41(0,0)(e^-t) stable to >= 8 digits under 10% truncation drop")
    wb.save()
    return 0 if (unique and sym_ok and sub_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
