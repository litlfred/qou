#!/usr/bin/env python3
"""a4_interface_operator_driver_search_probe.py — does the INTERFACE OPERATOR
`I = c·σ + d` (Hecke eigenvalues `q, −q⁻¹`) supply a parameter-free driver for the
A=4 one-scalar magnitude `m`?  (bean qou-foh0, "NEXT HONEST STEP"; 0-fit.)

## What this answers

`A4InterfaceMagnitude.lean` proved the ⁴He ≥4-body magnitude is a ONE-SCALAR gate:
with the derived exchange spectrum `{±√5, ±1}`,

    det(I + G) = (1 − 5m²)(1 − m²),   b₄(m) = −ln det,   physical ⇔ m < 1/√5,

surjective in `m ∈ (0, 1/√5)` — so hitting the AME target by CHOOSING `m` is a FIT.
`qou-foh0`'s "next honest step" proposes deriving `m` from the interface operator
`I = c·σ + d` spectral data (`pp`: `c=1, d=0`, so the two channel eigenvalues are the
Hecke eigenvalues `λ_sym = q`, `λ_anti = −q⁻¹`) — a categorical driver, not an
anchor inversion.  This probe MEASURES whether that route works.

## Method (anti-fit — NO winner is ever selected)

Enumerate the natural *parameter-free* dimensionless functionals of `{λ_sym, λ_anti}`
(and the derived `h = 1 − q⁻¹`) at the canonical proton-pinned `q₀`.  Classify each:

* **scale-like** functionals (overlap ratios `1/q²`, the Markov factors `z_C, z_D`,
  `1/[2]_q`, geometric means) — the "how big is the exchange overlap" family;
* **gap-like** functionals (`(q²−1)/(q²+1)`, `h`) and their square roots — the
  "how split are the two channels" family.

For each: is it physical (`m < 1/√5`)? and how far from the required
`m*(b₄)=0.41642`, `m*(μ₄)=0.35182` (from the sibling diagnostic qou-j16x, `E₀`
normalization; both anchor-inversions, diagnostic-only, never wired)?

## The measured verdict (SCOPE-(a) — confirms qou-foh0's "no driver identified")

* Every **scale-like** functional OVERSHOOTS the writhe ceiling (`m ≥ 1/√5`): the
  naive braiding overlap is scope-(b) unphysical under either Markov convention
  (formalised, whole-window, in `A4InterfaceMagnitude.zD_unphysical`).
* The **gap-like** family + roots SPANS `(0.10, 0.44)` and so REACHES the target
  band — but no single functional matches a target to `< 0.1%`, and SEVERAL land in
  the band.  Reaching a target by *choosing among a rich functional family with no
  uniqueness principle* is exactly the signature of a fit (an anchor inversion in
  disguise).  So the interface operator does **not** single out `m`.

Complements the sibling qou-j16x (which tested derived *constants* as `m` and found
no `<0.1%` match): here the specific *interface-operator eigenvalue functionals*
named in foh0 are tested and the same negative holds.  The magnitude stays
scope-(a) open; nothing is wired; `free_parameters = 0`.

-- Ref: QOU.MassTheory.A4InterfaceMagnitude (det form, surjectivity, zD_unphysical)
-- Ref: computations/deltalambda/b4_nonsaturating_mstar_diagnostic.py (qou-j16x, m*, E₀)
-- Ref: computations/a_operator/a_operator_categorical.py (INTERFACE_COEFS: pp=(1,0))
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

_COMP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(_COMP), str(_COMP / "substrate"),
                str(_COMP.parent / "tools" / "qou-substrate" / "python")]

mp.mp.dps = 50


def q0_mp() -> mp.mpf:
    """Canonical proton-pinned q₀ as an exact-ish mpmath.mpf (never float64)."""
    try:
        from q_parameter import Q_MP  # exact mpf, proton pin (owner directive 2026-08-07)
        return mp.mpf(Q_MP)
    except Exception:
        # documented proton pin, 50-dps literal (constants.py::Q_50_DIGIT_STR head)
        # q0 read BY NAME (bean qou-9ugp, 2026-09-04). This was a 17-digit
        # hardcoded PROTON literal in a RETURN -- right value, wrong
        # mechanism, and a shape an assignment-keyed scan does not match.
        #
        # The import was missing (bean qou-lejl): the `try` above imports Q_MP
        # locally, and reading q0 BY NAME here replaced the literal without
        # adding the matching import -- so this FALLBACK raised NameError
        # instead of falling back, and only on the path taken when the `try`
        # fails. Mirrors the try's local-import shape; the canonical form
        # `from q_parameter import Q_50_DIGIT_STR` appears 619 times in tree.
        from q_parameter import Q_50_DIGIT_STR  # noqa: E402
        return mp.mpf(Q_50_DIGIT_STR)


def det_gate(m: mp.mpf) -> mp.mpf:
    """det(I + G) = (1 − 5m²)(1 − m²) — the derived {±√5,±1} spectral form."""
    return (1 - 5 * m ** 2) * (1 - m ** 2)


def b4_dimless(m: mp.mpf) -> mp.mpf:
    return -mp.log(det_gate(m))


def main() -> int:
    q = q0_mp()
    ceil = 1 / mp.sqrt(5)
    h = 1 - 1 / q
    # channel eigenvalues of the pp interface operator I = σ (c=1, d=0):
    lam_sym = q
    lam_anti = -1 / q
    abs_anti = abs(lam_anti)

    # required magnitudes (anchor-inversions; diagnostic-only; NEVER wired) — from
    # the sibling qou-j16x, E₀ = 4.18598 MeV normalization of the det-gate cumulant.
    mstar_b4 = mp.mpf("0.416420800556079151")
    mstar_mu4 = mp.mpf("0.351817429146571937")

    scale_like = {
        "|lam_anti/lam_sym| = 1/q^2": 1 / q ** 2,
        "|la|/(|ls|+|la|) = 1/(q^2+1)": 1 / (q ** 2 + 1),
        "z_C = sqrt(q)/(q+1) [conv-C, excised]": mp.sqrt(q) / (q + 1),
        "z_D = q^3/(q^2+1) [conv-D naive]": q ** 3 / (q ** 2 + 1),
        "1/[2]_q = 1/(q+1/q)": 1 / (q + 1 / q),
        "sqrt(|ls*la|)/ls = 1/q^{3/2}": mp.sqrt(abs_anti * lam_sym) / lam_sym,
        "1/q^3": 1 / q ** 3,
    }
    gap_like = {
        "(q^2-1)/(q^2+1)": (q ** 2 - 1) / (q ** 2 + 1),
        "h = 1-1/q": h,
        "h/2": h / 2,
        "(1-1/q^2)/2": (1 - 1 / q ** 2) / 2,
        "sqrt((q^2-1)/(q^2+1))": mp.sqrt((q ** 2 - 1) / (q ** 2 + 1)),
        "sqrt(1-1/q^2)": mp.sqrt(1 - 1 / q ** 2),
        "sqrt(h) = sqrt(1-1/q)": mp.sqrt(h),
        "sqrt(q-1)": mp.sqrt(q - 1),
    }

    def classify(cands: dict) -> dict:
        out = {}
        for name, m in cands.items():
            m = mp.mpf(m)
            five = 5 * m ** 2
            physical = bool(five < 1 and m ** 2 < 1)
            rel_b4 = abs(m - mstar_b4) / mstar_b4
            rel_mu4 = abs(m - mstar_mu4) / mstar_mu4
            out[name] = {
                "m": m, "5m2": five, "physical": physical,
                "b4_dimless": (b4_dimless(m) if physical else mp.mpf("nan")),
                "rel_to_mstar_b4": rel_b4, "rel_to_mstar_mu4": rel_mu4,
            }
        return out

    scale = classify(scale_like)
    gap = classify(gap_like)

    TOL_MATCH = mp.mpf("1e-3")  # the sibling's 0.1% "derived-lead" bar
    scale_all_overshoot = all(not v["physical"] for v in scale.values())
    gap_physical = [k for k, v in gap.items() if v["physical"]]
    # closest gap-family functional to either target, and its relative distance
    def best_rel(d):
        best = None
        for k, v in d.items():
            if not v["physical"]:
                continue
            r = min(v["rel_to_mstar_b4"], v["rel_to_mstar_mu4"])
            if best is None or r < best[1]:
                best = (k, r)
        return best
    best_gap = best_rel(gap)
    n_gap_in_band = sum(
        1 for v in gap.values()
        if v["physical"] and mp.mpf("0.30") < v["m"] < ceil
    )
    unique_driver = (best_gap is not None and best_gap[1] < TOL_MATCH
                     and n_gap_in_band == 1)

    # ---- report ----
    print(f"q0 = {mp.nstr(q, 20)}   1/sqrt5 = {mp.nstr(ceil, 10)}")
    print(f"required m*(b4) = {mp.nstr(mstar_b4, 10)}   m*(mu4) = {mp.nstr(mstar_mu4, 10)}")
    print("=" * 78)
    for label, d in (("SCALE-LIKE (overlap)", scale), ("GAP-LIKE (channel split) + roots", gap)):
        print(f"\n[{label}]")
        print(f"  {'functional':40s} {'m':>12s} {'5m^2':>8s} {'phys':>5s} {'rel m*(b4)':>11s}")
        for name, v in d.items():
            print(f"  {name:40s} {mp.nstr(v['m'], 8):>12s} {mp.nstr(v['5m2'], 5):>8s} "
                  f"{'Y' if v['physical'] else 'N':>5s} {mp.nstr(v['rel_to_mstar_b4'], 4):>11s}")
    print("=" * 78)
    print(f"scale-like ALL overshoot ceiling (scope-(b) unphysical): {scale_all_overshoot}")
    print(f"gap-like physical count: {len(gap_physical)}   in band (0.30, 1/sqrt5): {n_gap_in_band}")
    if best_gap is not None:
        print(f"closest physical functional to a target: {best_gap[0]}  rel={mp.nstr(best_gap[1], 4)}")
    verdict = (
        "SCOPE-(a): interface operator does NOT supply a parameter-free driver for m. "
        "Scale-like functionals overshoot (scope-(b)); the gap-like family + roots "
        "reaches the target band but no single functional matches a target to <0.1% and "
        "several land in the band, so any match is a functional-choice fit."
        if not unique_driver else
        "DERIVED-LEAD CANDIDATE: a UNIQUE parameter-free functional matches a target "
        "to <0.1% — inspect for a categorical uniqueness argument before any wiring."
    )
    print("=" * 78)
    print(f"VERDICT: {verdict}")

    # ---- witness ----
    try:
        from witness_base import WitnessBuilder
    except Exception:
        print("(witness_base unavailable — printing only)")
        return 0
    w = WitnessBuilder("a4-interface-operator-driver-search", engine="mpmath")
    w.set_description(
        "bean qou-foh0 'next honest step': does the interface operator I=c*sigma+d "
        "(pp: c=1,d=0; channel eigenvalues q, -1/q) supply a PARAMETER-FREE driver "
        "for the A=4 one-scalar magnitude m? Enumerates the natural functionals of "
        "{q,-1/q,h}; scale-like OVERSHOOT the writhe ceiling (scope-(b)), gap-like + "
        "roots REACH the target band with no uniqueness => any match is a "
        "functional-choice fit. Confirms/extends qou-j16x. m*/targets are "
        "anchor-inversions, diagnostic-only, NEVER wired; free_parameters=0. "
        "VERDICT: " + verdict
    )
    w.set_audit_only("docs/audits/2026-08-28-a4-interface-operator-driver-search.md")
    w.add_data("q0", mp.nstr(q, 30))
    w.add_data("inv_sqrt5", mp.nstr(ceil, 20))
    w.add_data("mstar_b4", mp.nstr(mstar_b4, 18))
    w.add_data("mstar_mu4", mp.nstr(mstar_mu4, 18))
    w.add_data("free_parameters", 0)
    w.add_data("targets_never_inverted_into_production", True)
    w.add_data("scale_like_all_overshoot", scale_all_overshoot)
    w.add_data("gap_like_physical_count", len(gap_physical))
    w.add_data("gap_like_in_band_count", int(n_gap_in_band))
    w.add_data("closest_functional_name", best_gap[0] if best_gap else "none")
    w.add_data("closest_functional_relerr", mp.nstr(best_gap[1], 8) if best_gap else "nan")
    w.add_data("unique_parameter_free_driver", bool(unique_driver))
    w.add_data("verdict", verdict)
    for fam, d in (("scale", scale), ("gap", gap)):
        for name, v in d.items():
            w.add_data(f"{fam}::{name}",
                       {"m": mp.nstr(v["m"], 15), "5m2": mp.nstr(v["5m2"], 12),
                        "physical": v["physical"],
                        "rel_mstar_b4": mp.nstr(v["rel_to_mstar_b4"], 8)})
    # A REAL check: the det-gate closed form matches its polynomial normal form.
    m_probe = mp.mpf("0.3")
    dev = abs(det_gate(m_probe) - (1 - 6 * m_probe ** 2 + 5 * m_probe ** 4))
    w.add_assertion("detG_closed_form_max_deviation", mp.nstr(dev, 12), "0.0",
                    tolerance="1e-40",
                    source="det=(1-5m^2)(1-m^2)=1-6m^2+5m^4 at m=0.3")
    w.add_assertion("scale_like_all_overshoot_ceiling",
                    1 if scale_all_overshoot else 0, 1,
                    source="every overlap-scale functional has 5m^2>=1 at q0")
    out = w.save()
    print(f"witness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
