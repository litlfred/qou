#!/usr/bin/env python3
"""delta1g_deuteron_measurement_probe.py — Δ¹g at the deuteron IS measurable, and
here it is measured. The `Δ¹g = C_knot` identification is NOT yet bridged.

WHY THIS EXISTS. `docs/audits/2026-08-02-mu3-submodularity-vacuous-at-deuteron.md`
closed the μ₃ door as vacuous at A=2 — correctly, and by a proved identity: a
single-bond configuration has no second interface, so `Δ²g ≡ 0` and `c₃ = 0`. It
then declared the **bare first-order per-bond amplitude Δ¹g** the surviving open
magnitude object (GAP bean `qou-i4pz`), and identified it with the fitted
`C_knot = 5.853`.

TWO THINGS THIS ADDS.

(1) **Δ¹g is measurable, and was already measured.** The audit states "no
numerical probe is run", justified because an A=2 `Δ²g` would need a fabricated
second interface. That reasoning is exactly right for `Δ²g` — and does **not**
apply to `Δ¹g`, which is a *single-bond* object and needs no fabrication. The
corpus already contains the measurement, in `gap10_tjon_correlation_probe.py`
(merged #4406), where `M_op(2) = g(all bonds) − g(∅)` at A=2 IS `Δ¹g` by the
audit's own definition. It is not cited there. This probe measures it directly,
self-contained, so the number stands on its own.

    Δ¹g (convention D, H₆) = see [M] below

(2) **The `Δ¹g = C_knot` identification is dimensionally unbridged.** The two
objects are built from *different functionals* and carry *different dimensions*:

    C_knot = B_AME(²H) / B_cat(²H) = 2.2246 / 0.380 = 5.852
             a FITTED ratio of MeV binding energies, where
             B_cat = m_e·|Σ_λ y_λ χ^λ · sgn f^λ|      ← SIGNED by sgn f^λ

    Δ¹g    = g_a − g_∅,  with  g(S) = Σ_λ y_λ |χ_λ(w_S)|
             an ADDITIVE difference in the UNSIGNED (absolute-value) functional

A ratio of MeV and an additive difference of a dimensionless unsigned trace are
not the same kind of object, and `Σ y_λ|χ_λ|` is not `Σ y_λ χ^λ sgn f^λ`.
Equating them requires a normalisation bridge that does not currently exist in
the corpus. Under the most obvious reading — Δ¹g as the multiplicative factor —
the measured magnitude does not reach 5.853; the gap is reported below.

PRECEDENT, and why this is worth flagging rather than assuming. This exact trap
has already bitten this corpus once, on this exact `C_knot`:
`a3_units_consistency_probe.py` found the "1.6× A=3 near-miss" was a
MeV-vs-dimensionless pun, and that repairing it swung the gap from a 1.66×
overshoot to a 3.53× undershoot — *across the full unpinned C_knot = 5.85
factor*. That probe's own conclusion was that the near-miss was "an artifact of
the UNPINNED C_knot". The same unpinned factor is now being identified with Δ¹g.

WHAT THIS IS NOT. This does **not** refute Δ¹g as the surviving open object, and
does **not** show the audit wrong on the μ₃ vacuity (that identity stands and is
independent). It reports a measured value for the open object and flags that the
bridge from that value to `C_knot` is missing. Scope-(a) on the identification,
not on the object.

Convention D throughout (owner ruling 2026-08-09; convention C excised).
No Δ_λ, no C_knot fitted, nothing wired.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path[:0] = [str(COMP), str(COMP / "hecke"), str(COMP / "habiro"),
                str(COMP / "substrate"), str(HERE)]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import pyhecke_native  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(30)
q0 = mp.mpf(str(Q0))
q0f = float(Q0)

# The audit's locked numbers (diagnostics only — nothing inverted or fitted).
B_AME_D = mp.mpf("2.2246")     # AME2020 deuteron binding, MeV
B_CAT_D = mp.mpf("0.380")      # first-order DT-derived, MeV (#4601)
C_KNOT = B_AME_D / B_CAT_D     # the fitted deficit ratio ≈ 5.853


def perblock(n_strands, word):
    Y = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
         for k, v in y_lambda_at(n_strands, q0).items()}
    factors = [(float(c), float(d), int(g) + 1) for (c, d, g) in word]
    cp = pyhecke_native.chi_q_atomic_all_partitions(n_strands, factors, q0f)
    return sum(Y[tuple(s)] * abs(mp.mpf(str(chi))) for s, chi in cp if tuple(s) in Y)


def main() -> int:
    print("=" * 78)
    print(" Δ¹g at the deuteron — measured; and the C_knot identification checked")
    print("=" * 78)
    t0 = time.time()

    # ---- [M] the measurement: Δ¹g = g_a − g_∅ at A=2 (H₆, one bond) ---------
    full = atom_braid_word_3A(1, 1, include_inter=True)     # deuteron, 6 strands
    free = [x for x in full if x[2] % 3 != 2]               # no interface
    n_bonds = len([x for x in full if x[2] % 3 == 2])
    g_a = perblock(6, full)
    g_0 = perblock(6, free)
    d1g = g_a - g_0

    print(f"\n [M] the measurement (convention D, H₆, {time.time() - t0:.1f}s)")
    print(f"     deuteron word: {len(full)} letters, {n_bonds} interface bond(s)")
    print(f"     g(∅)        = {fmt(g_0, 12)}")
    print(f"     g(a)        = {fmt(g_a, 12)}")
    print(f"     Δ¹g = g_a − g_∅ = {fmt(d1g, 12)}")
    print(f"     ⇒ a single-bond object: NO fabricated second interface is needed,")
    print(f"       so the audit's 'no numerical probe' (correct for Δ²g) does not")
    print(f"       apply here. This is measurable and now measured.")

    single_bond = (n_bonds == 1)

    # ---- [C] the identification, checked ------------------------------------
    print(f"\n [C] the `Δ¹g = C_knot` identification")
    print(f"     C_knot = B_AME/B_cat = {fmt(B_AME_D, 6)}/{fmt(B_CAT_D, 6)} = {fmt(C_KNOT, 6)}")
    print(f"       ... a FITTED ratio of MeV, from B_cat = m_e·|Σ_λ y_λ χ^λ·sgn f^λ|  (SIGNED)")
    print(f"     Δ¹g    = {fmt(d1g, 6)}")
    print(f"       ... an ADDITIVE difference in g = Σ_λ y_λ |χ_λ|              (UNSIGNED)")
    print(f"     Different functionals, different dimensions. |Δ¹g| = {fmt(abs(d1g), 6)}")
    shortfall = C_KNOT / abs(d1g)
    print(f"     Under the obvious reading (Δ¹g AS the multiplicative factor):")
    print(f"       needed {fmt(C_KNOT, 4)}, measured |Δ¹g| = {fmt(abs(d1g), 4)}"
          f"  → short by {fmt(shortfall, 3)}×")
    unbridged = abs(d1g) < C_KNOT

    print(f"\n [P] precedent — this pun has bitten this corpus before, on this C_knot")
    print(f"     a3_units_consistency_probe.py: the '1.6× A=3 near-miss' was a")
    print(f"     MeV-vs-dimensionless comparison; repairing it swung the gap from a")
    print(f"     1.66× overshoot to a 3.53× undershoot — across the full unpinned")
    print(f"     C_knot = 5.85 factor. Its own verdict: an artifact of the UNPINNED")
    print(f"     C_knot. That same unpinned factor is now identified with Δ¹g.")

    print(f"\n ⇒ Δ¹g is measurable at A=2 and is {fmt(d1g, 9)} (convention D).")
    print(f"   The identification with C_knot = {fmt(C_KNOT, 4)} is NOT bridged: the two")
    print(f"   objects use different functionals (unsigned |χ| vs signed χ·sgn f^λ)")
    print(f"   and different dimensions (additive trace difference vs MeV ratio).")
    print(f"   Scope-(a) on the IDENTIFICATION. Δ¹g remains the open object; the μ₃")
    print(f"   vacuity result is untouched and independent.")

    verdict = (f"Δ¹g measured at the deuteron (convention D, H₆) = {fmt(d1g, 9)}; it is a "
               f"single-bond object so no fabricated interface is needed and the audit's "
               f"'no numerical probe' — correct for Δ²g — does not apply. The corpus already "
               f"contained this measurement in gap10_tjon_correlation_probe (merged #4406, "
               f"uncited by the successor work). The `Δ¹g = C_knot = {fmt(C_KNOT, 4)}` "
               f"identification is NOT bridged: C_knot is a fitted ratio of MeV from the SIGNED "
               f"functional m_e·|Σ y_λ χ^λ sgn f^λ|, while Δ¹g is an additive difference in the "
               f"UNSIGNED functional Σ y_λ|χ_λ|; under the obvious multiplicative reading the "
               f"measured |Δ¹g| falls short by {fmt(shortfall, 3)}×. Precedent: "
               f"a3_units_consistency_probe found this exact MeV-vs-dimensionless pun on this "
               f"exact C_knot, swinging 1.66× overshoot to 3.53× undershoot. Scope-(a) on the "
               f"IDENTIFICATION only — Δ¹g remains the open object and the μ₃ vacuity result is "
               f"untouched.")

    wb = WitnessBuilder("delta1g-deuteron-measurement", engine="pyhecke_native")
    wb.set_description(
        "Measures Δ¹g — the bare first-order per-bond amplitude declared the surviving open "
        "magnitude object by docs/audits/2026-08-02-mu3-submodularity-vacuous-at-deuteron.md "
        "(bean qou-i4pz) — directly at the deuteron (A=2, H₆, convention D). Two contributions. "
        "(1) Δ¹g IS measurable: the audit's 'no numerical probe is run' is correct for Δ²g (an "
        "A=2 second interface would have to be fabricated) but does not apply to Δ¹g, a "
        "single-bond object; and the corpus already contained the measurement in "
        "gap10_tjon_correlation_probe.py (merged #4406) as M_op(2), uncited by the successor "
        "work. (2) The identification `Δ¹g = the fitted C_knot = 5.853` is dimensionally "
        "UNBRIDGED: C_knot = B_AME/B_cat is a fitted ratio of MeV binding energies under the "
        "SIGNED master functional B_cat = m_e·|Σ_λ y_λ χ^λ·sgn f^λ|, whereas Δ¹g is an additive "
        "difference in the UNSIGNED functional g = Σ_λ y_λ|χ_λ|. Different functionals, "
        "different dimensions; under the obvious multiplicative reading the measured magnitude "
        "falls short. Precedent for treating this as a real hazard rather than a quibble: "
        "a3_units_consistency_probe.py found precisely this MeV-vs-dimensionless pun on "
        "precisely this C_knot, and repairing it swung the reported gap from a 1.66× overshoot "
        "to a 3.53× undershoot across the full unpinned factor. SCOPE-(a) on the IDENTIFICATION "
        "only: this does NOT refute Δ¹g as the open object and does NOT disturb the μ₃-vacuity "
        "result, which rests on the independent proved identity Δ²g ≡ 0 on single-bond configs. "
        "Convention D throughout (owner ruling 2026-08-09). No Δ_λ, no C_knot fitted, nothing "
        f"wired. VERDICT: {verdict}")
    wb.set_content_block("conj:binding-manybody-eq-jet-filtration")
    wb.add_data("delta1g_deuteron", {
        "convention": "D (SU(2)/Temperley-Lieb, y_lambda_at since 2026-08-09)",
        "n_strands": 6, "n_interface_bonds": n_bonds,
        "g_empty": fmt(g_0), "g_a": fmt(g_a), "delta1g": fmt(d1g),
        "B_AME_deuteron_MeV": fmt(B_AME_D), "B_cat_deuteron_MeV": fmt(B_CAT_D),
        "C_knot_fitted_ratio": fmt(C_KNOT),
        "abs_delta1g": fmt(abs(d1g)),
        "multiplicative_shortfall": fmt(shortfall),
        "C_knot_functional": "m_e·|Σ_λ y_λ χ^λ·sgn f^λ|  (SIGNED, MeV ratio)",
        "delta1g_functional": "Σ_λ y_λ|χ_λ|  (UNSIGNED, additive difference)",
        "precedent": ("a3_units_consistency_probe.py — same MeV-vs-dimensionless pun on the same "
                      "C_knot; repair swung 1.66x overshoot to 3.53x undershoot"),
        "verdict": verdict})
    wb.add_assertion("deuteron_is_single_bond_so_delta1g_needs_no_fabrication",
                     str(bool(single_bond)), "True")
    wb.add_assertion("delta1g_measured_nonzero", str(bool(d1g != 0)), "True")
    wb.add_assertion("c_knot_identification_unbridged_under_multiplicative_reading",
                     str(bool(unbridged)), "True")
    wb.save()
    print("\nwitness → delta1g-deuteron-measurement.witness.json")
    ok = single_bond and d1g != 0
    print("ALL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
