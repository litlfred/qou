#!/usr/bin/env python3
"""qbeta_g3_annihilator_certification.py — A_ω step 1, tranche 3: certify the
4₁ total-index assembly by the QUANTUM A-POLYNOMIAL annihilator (DGG eq C.7),
with operator conventions pinned analytically by the trefoil calibrator (C.9).

Why this closes the certification gap. Tranche 2 (merged #3826) left the
assembly open: candidate readings of eq (4.18) either diverge or near-miss the
single printed anchor (4.20). Appendix C supplies an anchor-independent
certificate: (C.7) is the quantum A-polynomial L̂₄₁ that ANNIHILATES the true
index I₄₁(m,e) at every charge, and (C.9) + the trefoil δ-index is a built-in
calibrator for how the operators act.

Glyph-decoded (C.7) (coordinate-aware extraction, minus/superscript rows
individually placed):

  L̂₄₁ = (q^{1/2}M̂ − q^{−1/2}M̂⁻¹)·ℓ̂⁻¹
        − (M̂ − M̂⁻¹)(M̂² + M̂⁻² − M̂ − M̂⁻¹ − q − q⁻¹)
        + (q^{−1/2}M̂ − q^{1/2}M̂⁻¹)·ℓ̂

Calibrator (analytic, from (C.9) L̂₃₁ = ℓ̂ + q^{3/2}M̂³ annihilating the
trefoil index δ_{e,3m}): writing M̂f = q^{a·m}f(m, e+s_M), ℓ̂f = σ·q^{e/2}
f(m+s_L, e), annihilation for ALL (m,e) forces uniquely

  M̂ f(m,e) = q^{m/2}·f(m, e−1),    ℓ̂ f(m,e) = −q^{e/2}·f(m+1, e)
  (⇒ ℓ̂⁻¹ f(m,e) = −q^{−e/2}·f(m−1, e)),

(support match ⇒ s_L = −s_M = +1; magnitude match ⇒ a = +1/2; cancellation ⇒
σ = −1). The probe re-verifies this symbolically on a grid rather than
asserting it.

Certification protocol: for each convergent candidate assembly (the tranche-2
survivors + charge-rescaled variants), compute R(m,e) = L̂₄₁·I over the grid
(m,e) ∈ [−2,2]², exact series arithmetic; CERTIFIED ⟺ R ≡ 0 through the valid
order at every grid point. The single printed anchor then only fixes the
overall monomial normalization — it is no longer load-bearing for structure.

Scope-(a); exact integer/monomial arithmetic; no fit; no c_k wired; the GGM
Stokes reading (step 2) starts only from a certified index.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_g3_fourone_index_assembly import (  # noqa: E402
    tet_norm, _dense_mul, series_str,
)
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

ORD = 44           # x-order for grid assemblies (q-order 22)
GRID = [(m, e) for m in range(-2, 3) for e in range(-2, 3)]
ANCHOR_11 = {2: -1, 4: -1, 6: 2, 8: 7, 10: 11, 12: 11, 14: 3}


# ---------------- Laurent-in-x series with shift: (shift, {deg: int}) -------
def sadd(a, b):
    (sha, da), (shb, db) = a, b
    sh = min(sha, shb)
    out = {}
    for d, c in da.items():
        out[d + sha - sh] = out.get(d + sha - sh, 0) + c
    for d, c in db.items():
        out[d + shb - sh] = out.get(d + shb - sh, 0) + c
    return sh, {d: c for d, c in out.items() if c != 0}


def smono(a, xpow, scal=1):
    sh, da = a
    return sh + xpow, {d: scal * c for d, c in da.items()}


def struncate_top(a, valid_abs):
    """Zero all coefficients above absolute x-degree valid_abs."""
    sh, da = a
    return sh, {d: c for d, c in da.items() if d + sh <= valid_abs}


# ------------------------------ assembly (from tranche 2, parametrized) ----
_asm_cache = {}


def assemble(m, e, order, pref_qcoef):
    key = (m, e, order, pref_qcoef)
    if key in _asm_cache:
        return _asm_cache[key]
    res = _assemble(m, e, order, pref_qcoef)
    _asm_cache[key] = res
    return res


def _assemble(m, e, order, pref_qcoef):
    """Σ_{e₂} q^{pref_qcoef·e₂} I_Δ(m−e₂, m+e−e₂) I_Δ(e−e₂, −e₂); None if
    non-convergent (flat/inward wings)."""
    e2max = 2 * order + 24
    terms = []
    for e2 in range(-e2max, e2max + 1):
        sh1, s1 = tet_norm(m - e2, m + e - e2, order)
        sh2, s2 = tet_norm(e - e2, -e2, order)
        terms.append((e2, sh1 + sh2 + 2 * pref_qcoef * e2, s1, s2))
    ms = min(t[1] for t in terms)
    if not all(t[1] - ms > order for t in terms if abs(t[0]) == e2max):
        return None
    out = {}
    for e2, lead, s1, s2 in terms:
        off = lead - ms
        if off > order:
            continue
        prod = _dense_mul(s1, s2, order - off)
        for d, c in enumerate(prod):
            if c:
                out[d + off] = out.get(d + off, 0) + c
    return ms, {d: c for d, c in out.items() if c != 0}


# --------------------- calibrator: trefoil annihilation, symbolic ----------
def trefoil_calibrate():
    """Verify (ℓ̂ + q^{3/2}M̂³)·δ_{e,3m} = 0 on a grid with the pinned actions,
    and that the 15 other action-convention combinations FAIL."""
    def delta(m, e):
        return 1 if e == 3 * m else 0

    def check(aM2, sM, sL, sig):
        # aM2 = 2a (so q^{aM2·m/2}); returns True if annihilated on grid
        for m in range(-4, 5):
            for e in range(-13, 14):
                # ℓ̂δ = σ q^{e/2} δ(m+sL, e); q^{3/2}M̂³δ = q^{3/2+3aM2·m/2}δ(m, e+3sM)
                # accumulate as (xpow, coeff) monomials — must cancel exactly
                acc = {}
                t1 = (e, sig * delta(m + sL, e))           # x^e = q^{e/2}
                t2 = (3 + 3 * aM2 * m, delta(m, e + 3 * sM))
                for xp, c in (t1, t2):
                    if c:
                        acc[xp] = acc.get(xp, 0) + c
                if any(v != 0 for v in acc.values()):
                    return False
        return True

    pinned = check(1, -1, 1, -1)
    others_fail = True
    n_pass = 0
    for aM2 in (1, -1):
        for sM in (1, -1):
            for sL in (1, -1):
                for sig in (1, -1):
                    if check(aM2, sM, sL, sig):
                        n_pass += 1
                        if (aM2, sM, sL, sig) != (1, -1, 1, -1):
                            others_fail = False
    return pinned, others_fail, n_pass


# --------------------- the annihilator L̂₄₁ applied to an assembly ----------
def annihilator_residual(pref_qcoef, m, e, order):
    """R(m,e) = L̂₄₁·I at charge (m,e); exact Laurent series in x.
    Uses: M̂f = q^{m/2}f(m,e−1) [x^m], ℓ̂f = −q^{e/2}f(m+1,e) [−x^e],
    ℓ̂⁻¹f = −q^{−e/2}f(m−1,e); M̂ᵏf = q^{km/2}f(m,e−k)."""
    def I(mm, ee):
        s = assemble(mm, ee, order, pref_qcoef)
        if s is None:
            raise RuntimeError("candidate non-convergent at grid point")
        return s

    terms = []
    # --- term 1: (q^{1/2}M̂ − q^{−1/2}M̂⁻¹)·ℓ̂⁻¹ ---
    # ℓ̂⁻¹I at (m,e): g(m,e) = −q^{−e/2} I(m−1, e)
    # then M̂g = q^{m/2} g(m, e−1) = −q^{m/2} q^{−(e−1)/2} I(m−1, e−1)
    terms.append(smono(I(m - 1, e - 1), 1 + m - (e - 1), -1))       # q^{1/2}M̂ℓ̂⁻¹
    # M̂⁻¹g = q^{−m/2} g(m, e+1) = −q^{−m/2}q^{−(e+1)/2} I(m−1, e+1); × −q^{−1/2}
    terms.append(smono(I(m - 1, e + 1), -1 - m - (e + 1), +1))
    # --- term 2: −(M̂ − M̂⁻¹)(M̂² + M̂⁻² − M̂ − M̂⁻¹ − q − q⁻¹)·I ---
    # product expands to pure M̂-powers: M̂³ − M̂² ... do it symbolically:
    # P = (M − M⁻¹)(M² + M⁻² − M − M⁻¹ − (q+q⁻¹))
    #   = M³ + M⁻¹·... expand exactly (M-powers with q-scalars):
    # (M)(M²)=M³; (M)(M⁻²)=M⁻¹; (M)(−M)=−M²; (M)(−M⁻¹)=−1(=M⁰);
    # (M)(−q−q⁻¹) = −(q+q⁻¹)M
    # (−M⁻¹)(M²)=−M; (−M⁻¹)(M⁻²)=−M⁻³; (−M⁻¹)(−M)=+1; (−M⁻¹)(−M⁻¹)=+M⁻²;
    # (−M⁻¹)(−q−q⁻¹)=+(q+q⁻¹)M⁻¹
    # NOTE: M̂-powers commute among themselves, so no q-ordering corrections here.
    Ppows = {3: [(0, 1)], 1: [(2, -1), (-2, -1), (0, -1)],
             2: [(0, -1)], 0: [(0, -1), (0, 1)],
             -1: [(0, 1), (2, 1), (-2, 1)], -3: [(0, -1)],
             -2: [(0, 1)]}
    # simplify: coefficient lists (xpow, coeff) per M-power
    for k, lst in Ppows.items():
        agg = {}
        for xp, c in lst:
            agg[xp] = agg.get(xp, 0) + c
        for xp, c in agg.items():
            if c == 0:
                continue
            # −P·I: M̂ᵏ I = q^{km/2} I(m, e−k) = x^{km} I(m, e−k)
            terms.append(smono(I(m, e - k), xp + k * m, -c))
    # --- term 3: (q^{−1/2}M̂ − q^{1/2}M̂⁻¹)·ℓ̂ ---
    # ℓ̂I at (m,e): h(m,e) = −q^{e/2} I(m+1, e)
    # M̂h = q^{m/2}h(m,e−1) = −q^{m/2}q^{(e−1)/2}I(m+1, e−1); × q^{−1/2}
    terms.append(smono(I(m + 1, e - 1), -1 + m + (e - 1), -1))
    # M̂⁻¹h = q^{−m/2}h(m,e+1) = −q^{−m/2}q^{(e+1)/2}I(m+1,e+1); × −q^{1/2}
    terms.append(smono(I(m + 1, e + 1), 1 - m + (e + 1), +1))

    tot = terms[0]
    for t in terms[1:]:
        tot = sadd(tot, t)
    return tot


def main() -> int:
    print("=" * 78)
    print(" A_ω step 1, tranche 3 — annihilator certification of the 4₁ index")
    print("=" * 78)

    # ---- [1] trefoil calibrator ----
    pinned, others_fail, n_pass = trefoil_calibrate()
    print(f"\n[1] trefoil calibrator: pinned actions annihilate δ(e,3m): {pinned}; "
          f"conventions passing: {n_pass} (uniqueness: {others_fail})")

    # ---- [2] annihilator residuals per candidate ----
    print("\n[2] L̂₄₁ residuals on the grid (exact; valid to the common window):")
    results = {}
    for pref in (-1, 1):
        label = f"q^({pref}·e₂)"
        try:
            max_nonzero = 0
            worst = None
            for (m, e) in GRID:
                r = annihilator_residual(pref, m, e, ORD)
                sh, d = struncate_top(r, ORD - 12)   # conservative common window
                nz = len(d)
                if nz > max_nonzero:
                    max_nonzero = nz
                    worst = (m, e, series_str((sh, d), 4) if d else "0")
            results[label] = {"max_nonzero_terms": max_nonzero, "worst": worst}
            print(f"    {label}: max nonzero residual terms over grid = "
                  f"{max_nonzero}" + (f"  (worst at {worst[0:2]}: {worst[2]})"
                                      if worst and max_nonzero else "  → ANNIHILATED"))
        except RuntimeError as ex:
            results[label] = {"error": str(ex)}
            print(f"    {label}: {ex}")

    certified = [k for k, v in results.items() if v.get("max_nonzero_terms") == 0]
    unique = len(certified) == 1

    # ---- [3] anchor status for the certified candidate ----
    anchor_note = "n/a"
    if certified:
        pref = -1 if "-1" in certified[0] else 1
        s = assemble(1, 1, 40, pref)
        sh, a = s
        hit = None
        for t in range(-6, 7):
            if all(a.get(d - sh - t, 0) == v for d, v in ANCHOR_11.items()):
                hit = t
        anchor_note = (f"matches printed (4.20) with monomial shift x^{hit}"
                       if hit is not None else
                       "does NOT match printed (4.20) at any monomial shift — "
                       "the anchor's charge normalization differs (U=2·log m); "
                       "the annihilator certificate is primary")
        print(f"\n[3] certified candidate {certified[0]} vs printed anchor: {anchor_note}")
        print(f"    I(1,1) = {series_str(s, 8)}")

    verdict = (
        f"Trefoil calibrator pins the operator actions "
        f"(M̂f=q^(m/2)f(m,e−1), ℓ̂f=−q^(e/2)f(m+1,e); unique among 16 "
        f"conventions: {others_fail}). Annihilator certification: "
        f"{'candidate ' + certified[0] + ' is ANNIHILATED by the quantum A-polynomial on the full grid — the assembly is CERTIFIED anchor-independently' if certified else 'no candidate annihilated — operator reading or assembly space needs revisit'}; "
        f"uniqueness {unique}. Anchor status: {anchor_note}. Exact arithmetic "
        f"throughout; scope-(a); no fit; no c_k wired."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-g3-annihilator-certification",
                        engine="python-int+mpmath")
    wb.set_description(
        "A_omega step 1 tranche 3: anchor-independent certification of the 4_1 "
        "total-index assembly by the quantum A-polynomial annihilator (DGG C.7, "
        "glyph-decoded), with operator conventions pinned analytically and "
        "verified by the trefoil calibrator (C.9). Certified assembly becomes "
        "the input for the GGM Stokes reading (step 2).")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("operator", "L41 = (q^(1/2)M - q^(-1/2)M^-1)l^-1 - (M - M^-1)"
                            "(M^2 + M^-2 - M - M^-1 - q - q^-1) + "
                            "(q^(-1/2)M - q^(1/2)M^-1)l")
    wb.add_data("actions", "Mf = q^(m/2) f(m,e-1); lf = -q^(e/2) f(m+1,e) "
                           "(trefoil-calibrated, unique)")
    wb.add_data("calibrator", {"pinned_ok": bool(pinned),
                               "unique": bool(others_fail),
                               "n_conventions_passing": n_pass})
    wb.add_data("residuals", {k: {kk: (str(vv) if not isinstance(vv, int) else vv)
                                  for kk, vv in v.items()}
                              for k, v in results.items()})
    wb.add_data("certified_candidates", certified)
    wb.add_data("anchor_status", anchor_note)
    wb.add_data("verdict", verdict)
    wb.add_assertion("trefoil_calibrator_pins_actions",
                     computed=1.0 if (pinned and others_fail) else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="(C.9) annihilates delta(e,3m) only for the pinned action convention")
    wb.add_assertion("assembly_certified_by_annihilator",
                     computed=1.0 if certified else 0.0, expected=1.0, tolerance=0.5,
                     source="L41 residual identically zero on the (m,e) grid for a candidate")
    wb.add_assertion("certified_candidate_unique",
                     computed=1.0 if unique else 0.0, expected=1.0, tolerance=0.5,
                     source="exactly one candidate assembly is annihilated")
    wb.save()
    return 0 if (pinned and certified) else 1


if __name__ == "__main__":
    raise SystemExit(main())
