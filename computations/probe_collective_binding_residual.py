#!/usr/bin/env python3
"""EXPLORATORY shape-probe (per .claude/skills/local/production-vs-exploratory-discipline.md).

Exploratory hypothesis-generation; the structural finding NARROWS the
collective-binding search (formalize-first) — it does NOT fit a closed form
and introduces no production coefficient. The Δ_λ "no 7th ansatz" gate stands.

PROBE — what STRUCTURAL FORM must the collective binding residual take?
======================================================================

The interface probe ([probe_sdp_interface_selection.py]) showed the per-bond
linear chain `B_sym = α[(Z−1)L_pp + L_pn + (N−1)L_nn]` under-binds A ≥ 4 by a
factor the p-n interface cannot fix (2.41× joint-tower ceiling), and that the
residual is "collective / magic-A". This probe pins down the residual's
STRUCTURAL FORM, to tell the keystone (beans w5tg/z2bn/thb7; A=4 interface
operator #2750) what kind of term is missing — BEFORE any closed-form search.

THE STRUCTURAL ARGUMENT (formalize-first, near-proof level)
-----------------------------------------------------------
`B_sym` is a SUM over the (A−1) monotone adjacency bonds, each bond's
log-suppression `L_{pp|pn|nn} ≥ 0` a fixed per-bond-type constant.  Hence the
per-nucleon binding

    B_sym / A = α · [ (Z−1)L_pp + L_pn + (N−1)L_nn ] / A

is a weighted mean of the three FIXED bond constants — it can only track the
bond-type COMPOSITION, which varies monotonically along the tower.  An
ADDITIVE per-bond sum therefore has **no mechanism to produce a saturation
PEAK** at a specific mass number.

The empirical `B_AME / A`, by contrast, **peaks sharply at ⁴He** (the
doubly-magic α-core) and dips for the Li isotopes — the textbook nuclear
saturation curve.  A monotone (additive) quantity cannot reproduce a curve
with an interior maximum.  ∴ the missing term is **non-additive / collective**,
and the location of the peak (⁴He) identifies it as **4-body α-saturation** —
NOT a 2-body or per-bond correction.

This is the formalize-first narrowing: do NOT search for a per-bond or
pairwise `f(bonds)` collective factor; the term is 4-body (⁴He / Borromean
saturation), consistent with the magic-volume's "exact-at-⁴He" construction
and the A=4 interface-operator / s5-so3 keystone direction.

No float64 (owner ruling 2026-06-09): mpmath at the 50-dps floor.

Usage:
    python3 probe_collective_binding_residual.py
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from mass_binding_dashboard import _ame_table, _constants, _bond_type_L  # noqa: E402

DPS = 50

# Every isotope is instant: B_sym needs only the three cached bond constants.
# (Z, N) chosen to span the ⁴He saturation peak + the Li dip + the slow rise.
TOWER = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
         ("6Li", 3, 3), ("7Li", 3, 4), ("9Be", 4, 5), ("12C", 6, 6),
         ("16O", 8, 8)]


def B_sym(alpha, Lbond, Z, N):
    bpp, bpn, bnn = (alpha * Lbond["pp"], alpha * Lbond["pn"], alpha * Lbond["nn"])
    pn = bpn if (Z >= 1 and N >= 1) else mp.mpf(0)
    return max(Z - 1, 0) * bpp + pn + max(N - 1, 0) * bnn


def main():
    mp.mp.dps = DPS
    me, q0, alpha, g8 = _constants()
    alpha = mp.mpf(str(alpha))
    ame = _ame_table()
    Lbond = {k: mp.mpf(str(v)) for k, v in _bond_type_L().items()}

    rows = []
    for name, Z, N in TOWER:
        A = Z + N
        t = ame.get((Z, A))
        if not t:
            continue
        bame = mp.mpf(str(t[0]))
        bs = B_sym(alpha, Lbond, Z, N)
        rows.append({
            "name": name, "A": A, "B_sym": bs, "B_AME": bame,
            "F": bame / bs, "R": bame - bs,
            "bs_perA": bs / A, "ba_perA": bame / A,
        })

    print("=" * 76)
    print("PROBE — structural form of the collective binding residual")
    print("=" * 76)
    print(f"alpha=E0={mp.nstr(alpha,8)} MeV   "
          f"L_pp={mp.nstr(Lbond['pp'],6)} L_pn={mp.nstr(Lbond['pn'],6)} "
          f"L_nn={mp.nstr(Lbond['nn'],6)}")
    print()
    print(f"{'iso':<5}{'A':>3}{'B_sym':>9}{'B_AME':>9}{'F=AME/sym':>11}"
          f"{'B_sym/A':>9}{'B_AME/A':>9}")
    for r in rows:
        print(f"{r['name']:<5}{r['A']:>3}{float(r['B_sym']):>9.3f}"
              f"{float(r['B_AME']):>9.3f}{float(r['F']):>11.3f}"
              f"{float(r['bs_perA']):>9.3f}{float(r['ba_perA']):>9.3f}")

    # ---- two honest structural signals -------------------------------------
    by = {r["name"]: r for r in rows}

    def he4_local_excess(key):
        """Fractional ⁴He excess over the linear A=3↔A=6 interpolation of the
        per-nucleon quantity `key` — isolates the ⁴He local spike from the
        smooth A-trend (so the global ¹⁶O rise does not mask it)."""
        a3 = (by["3H"][key] + by["3He"][key]) / 2          # A=3 neighbour avg
        a6 = by["6Li"][key]                                # A=6 neighbour
        interp4 = a3 + (a6 - a3) * (mp.mpf(4) - 3) / (mp.mpf(6) - 3)
        return (by["4He"][key] - interp4) / interp4

    exc_ame = he4_local_excess("ba_perA")                  # AME ⁴He local spike
    exc_sym = he4_local_excess("bs_perA")                  # chain ⁴He local spike
    F_lo, F_hi = by["3H"]["F"], by["16O"]["F"]             # general collective rise

    print()
    print("-" * 76)
    print("STRUCTURAL SIGNALS — what the additive chain cannot do")
    print("-" * 76)
    print("  (A) general collective under-binding (grows with A):")
    print(f"      F = B_AME/B_sym rises {float(F_lo):.2f} (³H) → {float(F_hi):.2f} "
          f"(¹⁶O); B_sym/A saturates ~{float(by['16O']['bs_perA']):.1f} while "
          f"B_AME/A climbs to ~{float(by['16O']['ba_perA']):.1f}.")
    print("  (B) ⁴He α-magic LOCAL spike (over the A=3↔A=6 interpolation):")
    print(f"      B_AME/A ⁴He excess = {float(exc_ame)*100:+.0f}%   (sharp local max)")
    print(f"      B_sym/A ⁴He excess = {float(exc_sym)*100:+.0f}%   (no spike — "
          f"additive chain is smooth through A=4)")

    # Honest test: the additive chain shows NO ⁴He local enhancement (|excess|
    # small) while AME shows a large positive one. Both signals ⇒ collective.
    he4_spike_only_in_ame = bool(exc_ame > mp.mpf("0.30") and abs(exc_sym) < mp.mpf("0.15"))
    general_collective = bool(F_hi > mp.mpf("1.5"))
    collective_required = bool(he4_spike_only_in_ame and general_collective)

    print()
    print("=" * 76)
    print(f"VERDICT: a NON-ADDITIVE (collective) term is required, with a 4-body "
          f"⁴He component? {collective_required}")
    if collective_required:
        print("  • (A) The per-bond chain under-binds by a collective factor that")
        print("    GROWS with A (F → ~2.1) — a tower-wide non-additive deficit.")
        print("  • (B) ON TOP of that, B_AME/A has a sharp ⁴He LOCAL spike "
              f"({float(exc_ame)*100:+.0f}%)")
        print("    entirely absent from the additive chain "
              f"({float(exc_sym)*100:+.0f}%): the additive sum of")
        print("    fixed bond constants is smooth through A=4 and cannot produce")
        print("    a doubly-magic α-core singularity.")
        print("  ⇒ the missing physics is collective; the ⁴He spike fingerprints a")
        print("    4-BODY α-core (⁴He / Borromean) term — NOT a per-bond / pairwise")
        print("    correction. NARROWS the keystone: pursue the A=4 interface")
        print("    operator / magic-volume(⁴He-exact) / s5-so3 4-body assembly.")
        print("  (formalize-first narrowing; no closed-form fit — Δ_λ gate stands.)")
    print("=" * 76)

    _emit_witness(rows, alpha, exc_ame, exc_sym, F_lo, F_hi, collective_required)


def _emit_witness(rows, alpha, exc_ame, exc_sym, F_lo, F_hi, collective_required):
    try:
        from witness_base import WitnessBuilder
    except Exception as e:                                # pragma: no cover
        print(f"[witness skipped: {e}]")
        return
    w = WitnessBuilder("probe-collective-binding-residual", engine="mpmath")
    w.set_description(
        "EXPLORATORY: structural form of the collective binding residual. The "
        "additive per-bond chain shows NO ⁴He local spike and under-binds by a "
        "factor growing with A ⇒ the missing term is non-additive (collective), "
        "with a 4-body ⁴He α-core component.")
    w.add_parameter("compute_dps", DPS)
    w.add_parameter("alpha_E0_MeV", mp.nstr(alpha, 20))
    w.add_parameter("tower", [r["name"] for r in rows])
    w.add_data("per_nucleon", {r["name"]: {
        "A": r["A"], "B_sym_per_A": mp.nstr(r["bs_perA"], 10),
        "B_AME_per_A": mp.nstr(r["ba_perA"], 10),
        "F_AME_over_sym": mp.nstr(r["F"], 10)} for r in rows})
    w.add_data("he4_local_excess_AME", mp.nstr(exc_ame, 8))
    w.add_data("he4_local_excess_Bsym", mp.nstr(exc_sym, 8))
    w.add_data("F_collective_rise", {"3H": mp.nstr(F_lo, 8), "16O": mp.nstr(F_hi, 8)})
    # assert the structural claim (allPassed=true on the EXPECTED-positive
    # outcome): the additive chain is refuted as the whole story; a collective
    # 4-body term is required.
    w.add_assertion(
        "collective_4body_term_required_he4_spike_absent_from_additive_chain",
        computed=int(collective_required), expected=1, tolerance=None,
        source=f"⁴He local excess: AME={mp.nstr(exc_ame,4)} vs "
               f"B_sym={mp.nstr(exc_sym,4)}; F rises {mp.nstr(F_lo,3)}→{mp.nstr(F_hi,3)}")
    w.set_audit_only(
        "docs/audits/2026-06-25-sdp-interface-selection-fit-vs-derivation.md")
    out = w.save()
    print(f"[witness → {out}]")


if __name__ == "__main__":
    main()
