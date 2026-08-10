#!/usr/bin/env python3
"""Kill-switch (bean 754x, step 4): does charge-symmetric core + Coulomb reproduce the mirror split?

The gg-production probe showed that a flavor-blind inter-nucleon bond makes the strong binding
EXACTLY charge-symmetric, collapsing the production ΔB_sym mirror splits to 0 — so under the
correct (gg) core the mirror-nucleus binding difference must come from somewhere else. Standard
nuclear physics says that "somewhere else" is the electrostatic (Coulomb) repulsion of the like
protons: the higher-Z mirror member is LESS bound by its extra Coulomb energy. This probe wires
the textbook Coulomb energy and runs the bean's kill-switch:

    ΔB(lo − hi)  ?=  ΔE_C(hi − lo)        [charge-symmetric strong core ⇒ split is all Coulomb]

with the uniform-charged-sphere energy
    E_C(Z) = (3/5) · Z(Z−1) · α_EM · ℏc / R,   R = R₀ · A^{1/3},
taken from the CANONICAL `coulomb_energy` module: α_EM DERIVED from q₀ (not CODATA) and
R₀ = λ̄_π = ℏc/m_π the CAL-3 length (not the empirical 1.2 fm). NOT a fit.

STATUS (2026-08-10) — two corrections, both material.

(1) The inputs were stale. This probe carried its own copy of the Coulomb constants
    (`ALPHA_HBAR_C_MEV_FM = 1.43996` CODATA, `R0_FM = 1.2` empirical, both float64) which
    bean qou-usft had already replaced in `coulomb_energy.py`. The fix never propagated.
    Importing the canonical functions improves every pair:

        pair       residual (CS+Coulomb − AME), MeV      worst-case error
        3H/3He     +0.235  ->  +0.084
        7Li/7Be    +0.614  ->  +0.272                    37 %  ->  17 %
        13C/13N    +0.672  ->  +0.116

(2) The verdict prose was stale and contradicted the committed numbers. It asserted
    "CS+Coulomb 20–40 % vs production 200–350 %". The production σ/σ⁻¹ figure has not been
    200–350 % since `_bond_type_L` changed on 2026-08-08 (the Reeb-override removal); it is
    now 0–53 %, and at 3H/3He it is 0.002 MeV — near-exact. All verdict figures are now
    COMPUTED from the rows; do not re-hardcode them.

Consequently the headline assertion — CS+Coulomb beats production on EVERY pair — is
currently FALSE, failing on 3H/3He alone, and is left failing rather than weakened. Read it
with the spread: the σ/σ⁻¹ form that lands 0.002 MeV out at 3H/3He is 0.652 and 1.589 MeV out
at the other two, so the single hit is a coincidence, not support for a strong-CSB mechanism.
What the probe does establish on its own terms is the second assertion: the derived Coulomb
term reproduces all three splits to 17 % worst-case, inside the Nolen–Schiffer band.

(a) scope-limited throughout: this constrains these constructions as evaluated; it excludes
no ingredient. Does not rewire production (owner-gated; the strong core's charge symmetry is
gated on `conj:s5-so3-fiber-action`).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from math import comb  # noqa: E402

import mass_binding_dashboard as mbd  # noqa: E402
import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# ── Coulomb inputs now come from the CANONICAL module (2026-08-10) ────────
# This probe used to carry its own copy:
#
#     ALPHA_HBAR_C_MEV_FM = 1.43996   # CODATA, float64
#     R0_FM = 1.2                     # empirical saturation constant, float64
#
# Both defects were fixed in `coulomb_energy.py` by bean qou-usft — α_EM is
# DERIVED from q₀ (not CODATA), the length is the CAL-3 reduced pion Compton
# wavelength λ̄_π = ℏc/m_π (not the empirical 1.2 fm), and everything is mpmath.
# The fix never propagated here, so this probe kept consuming an experimental
# α_EM and an empirical radius while the dashboard next to it used neither.
# That is exactly the provenance leak the fix existed to close: a PREDICTED
# observable quietly depending on experimental inputs.
#
# Importing the canonical functions instead of redefining them is the whole
# point — `mirror_displacement_mev` was written for this probe's kill-switch.
from coulomb_energy import (  # noqa: E402
    alpha_em_hbar_c_mev_fm,
    coulomb_energy_mev,
    mirror_displacement_mev,
    R0_FM,
)

# Mirror pairs as (lower-Z member, Z, N, higher-Z member, Z, N).
# The lower-Z member is the more-bound one (less Coulomb repulsion).
MIRROR_PAIRS = [("3H", 1, 2, "3He", 2, 1), ("7Li", 3, 4, "7Be", 4, 3),
                ("13C", 6, 7, "13N", 7, 6)]


def run():
    me, q0, E0 = mbd._constants()
    L = mbd._bond_type_L()          # production flavor-only σ/σ⁻¹ per-bond L
    ame = mbd._ame_table()

    def Bsym_prod(Z, N):
        return E0 * (comb(Z, 2) * L["pp"] + Z * N * L["pn"] + comb(N, 2) * L["nn"])

    def bame(Z, A):
        t = ame.get((Z, A))
        return t[0] if t else None

    rows = []
    for (lo, Zlo, Nlo, hi, Zhi, Nhi) in MIRROR_PAIRS:
        A = Zlo + Nlo
        # Split orientation: B(lower-Z) − B(higher-Z), positive (lower-Z is more bound).
        # Strong-core charge-symmetric split is 0 by the gg result (L_pp=L_pn=L_nn);
        # the higher-Z member loses ΔE_C of binding to extra Coulomb repulsion.
        dB_strong_cs = 0.0
        dE_coulomb = float(mirror_displacement_mev(Zhi, Zlo, A))  # > 0
        dB_pred = dB_strong_cs + dE_coulomb          # B(lo) − B(hi) predicted
        dB_ame = None
        blo, bhi = bame(Zlo, A), bame(Zhi, A)
        if blo is not None and bhi is not None:
            dB_ame = blo - bhi                        # B(lo) − B(hi), AME (> 0)
        dB_prod = Bsym_prod(Zlo, Nlo) - Bsym_prod(Zhi, Nhi)  # production σ/σ⁻¹, same orientation
        rows.append({
            "pair": f"{lo}-{hi}", "lo": lo, "hi": hi, "A": A,
            # No per-row R_fm: it is exactly R0_FM·A^{1/3}, and both are already
            # recorded (`data.r0_fm`, `data.rows[].A`). Adding it would push this
            # witness's raw-float64 count 28 -> 31, i.e. a ratchet REGRESSION, to
            # carry a number the reader can already reconstruct.
            "E_C_lo": float(coulomb_energy_mev(Zlo, A)),
            "E_C_hi": float(coulomb_energy_mev(Zhi, A)),
            "dE_coulomb": dE_coulomb, "dB_pred_cs_plus_coulomb": dB_pred,
            "dB_AME": dB_ame, "dB_prod_sigma": dB_prod,
            "resid_cs_coulomb": (dB_pred - dB_ame) if dB_ame is not None else None,
            "resid_prod": (dB_prod - dB_ame) if dB_ame is not None else None,
        })
    return {"q0": q0, "E0_MeV": E0,
            "alpha_hbar_c": float(alpha_em_hbar_c_mev_fm()),
            "r0_fm": float(R0_FM), "rows": rows}


def report(res):
    print("# Coulomb kill-switch — charge-symmetric core + Coulomb vs production σ/σ⁻¹ (bean 754x)\n")
    print(f"E₀ = {res['E0_MeV']:.4f} MeV   α_EM·ℏc = {res['alpha_hbar_c']:.7f} MeV·fm (DERIVED from q₀)"
          f"   R₀ = λ̄_π = {res['r0_fm']:.7f} fm (CAL-3)  — no CODATA α_EM, no empirical r₀\n")
    print("Mirror split B(lower-Z) − B(higher-Z), MeV — positive: lower-Z is more bound:\n")
    print("| pair | A | ΔE_Coulomb | CS-core + Coulomb | ΔB_AME | production σ/σ⁻¹ |")
    print("|---|--:|--:|--:|--:|--:|")
    for r in res["rows"]:
        ame = f"{r['dB_AME']:+.3f}" if r["dB_AME"] is not None else "n/a"
        print(f"| {r['pair']} | {r['A']} | {r['dE_coulomb']:+.3f} | {r['dB_pred_cs_plus_coulomb']:+.3f} "
              f"| {ame} | {r['dB_prod_sigma']:+.3f} |")

    print("\n| pair | residual (CS+Coulomb − AME) | residual (production − AME) | error ratio |")
    print("|---|--:|--:|--:|")
    for r in res["rows"]:
        if r["resid_cs_coulomb"] is None:
            continue
        rc, rp = r["resid_cs_coulomb"], r["resid_prod"]
        ratio = abs(rp / rc) if rc else float("inf")
        print(f"| {r['pair']} | {rc:+.3f} | {rp:+.3f} | {ratio:.1f}× |")

    print("\n## Verdict\n")
    rows_ok = [r for r in res["rows"] if r["resid_cs_coulomb"] is not None]
    frac = [abs(r["resid_cs_coulomb"] / r["dB_AME"]) for r in rows_ok if r["dB_AME"]]
    fracp = [abs(r["resid_prod"] / r["dB_AME"]) for r in rows_ok if r["dB_AME"]]
    # Every figure below is computed from the rows above. It used to be prose
    # asserting "CS+Coulomb 20–40 % vs production 200–350 %"; those constants went
    # stale when `_bond_type_L` changed on 2026-08-08 (the Reeb-override removal),
    # and the committed text then contradicted the committed numbers. Do not
    # re-hardcode them.
    wins = [r for r in rows_ok
            if abs(r["resid_cs_coulomb"]) < abs(r["resid_prod"])]
    print(f"- Charge-symmetric core + DERIVED Coulomb reproduces the three mirror splits to "
          f"{min(frac) * 100:.0f}–{max(frac) * 100:.0f}%.")
    print(f"- The production σ/σ⁻¹ B_sym splits are off by "
          f"{min(fracp) * 100:.0f}–{max(fracp) * 100:.0f}%.")
    print(f"- CS+Coulomb beats production on {len(wins)}/{len(rows_ok)} pairs.")
    if len(wins) == len(rows_ok):
        print("- Kill-switch PASSES on every pair: the mirror split is Coulomb on a "
              "charge-symmetric strong core.")
    else:
        lost = [r["pair"] for r in rows_ok if r not in wins]
        print(f"- Kill-switch does NOT pass on: {', '.join(lost)}. The σ/σ⁻¹ form happens to "
              f"land closer there, so this run does NOT establish the Coulomb mechanism on "
              f"those pairs. Reported as measured — scope-(a), no ingredient excluded either way.")
    print("- Disposition unchanged and owner-gated: no production rewire here. The strong "
          "core's charge symmetry is gated on `conj:s5-so3-fiber-action` (s5-so3 keystone).")


def main(argv=None):
    res = run()
    report(res)
    w = WitnessBuilder("coulomb-mirror-killswitch-probe", engine="python")
    w.set_description(
        "Bean 754x step 4 kill-switch: tests whether a charge-symmetric strong core (gg result: "
        "mirror dB_sym=0) plus uniform-sphere Coulomb E_C=(3/5)Z(Z-1)*alpha*hbar_c/(R0*A^1/3) "
        "reproduces the AME mirror-nucleus binding splits for 3H/3He, 7Li/7Be, 13C/13N. "
        "REWIRED 2026-08-10 onto the canonical `coulomb_energy` module: alpha_EM DERIVED from q0 "
        "(was CODATA 1.43996) and R0 = lambda_bar_pi = hbar_c/m_pi, the CAL-3 length (was the "
        "empirical 1.2 fm) - both float64 copies that bean qou-usft had already fixed upstream but "
        "which never propagated here. Every pair improves; worst-case error 37% -> 17%, inside the "
        "Nolen-Schiffer band. The verdict figures are now COMPUTED, not asserted: the old prose "
        "claimed production over-splits by 200-350%, which went stale when _bond_type_L changed on "
        "2026-08-08; it is now 0-53%. The every-pair assertion consequently FAILS on 3H/3He, where "
        "the sigma/sigma^-1 form lands 0.002 MeV out by coincidence (it is 0.652 and 1.589 MeV out "
        "on the other two pairs); left failing rather than weakened. (a) scope-limited; no "
        "production rewire (owner-gated)."
    )
    w.add_data("q0", res["q0"])
    w.add_data("E0_MeV", res["E0_MeV"])
    w.add_data("alpha_hbar_c_MeV_fm", res["alpha_hbar_c"])
    w.add_data("r0_fm", res["r0_fm"])
    w.add_data("rows", res["rows"])
    # Assertion: CS-core + Coulomb beats production by a large factor on every mirror pair.
    ok = all(
        (r["resid_cs_coulomb"] is not None and r["resid_prod"] is not None
         and abs(r["resid_cs_coulomb"]) < abs(r["resid_prod"]))
        for r in res["rows"]
    )
    worst_frac = max(
        (abs(r["resid_cs_coulomb"] / r["dB_AME"]) for r in res["rows"] if r["dB_AME"]),
        default=1.0,
    )
    # KEPT AS-IS AND CURRENTLY FAILING (2026-08-10). Do not weaken it to go green.
    # It fails on exactly one pair, 3H/3He, where the production sigma/sigma^-1
    # form lands 0.002 MeV from AME - near-exact, and by coincidence: that same
    # form is 0.652 and 1.589 MeV out on the other two pairs. A single accidental
    # hit is not evidence for the sigma mechanism, but the assertion as written
    # says "every pair", so it is false and is reported false.
    w.add_assertion(
        "cs_core_plus_coulomb_beats_production_on_every_mirror_pair",
        computed=1 if ok else 0, expected=1, tolerance=0,
        source="Charge-symmetric core + DERIVED Coulomb has a SMALLER residual to ΔB_AME than the "
               "production sigma/sigma^-1 B_sym on every mirror pair (3H/3He, 7Li/7Be, 13C/13N). "
               f"Currently {'PASSES' if ok else 'FAILS'}: beats production on "
               f"{sum(1 for r in res['rows'] if r['resid_cs_coulomb'] is not None and r['resid_prod'] is not None and abs(r['resid_cs_coulomb']) < abs(r['resid_prod']))}"
               f"/{len(res['rows'])} pairs. CS+Coulomb worst-case error {worst_frac * 100:.0f}%.",
    )
    # The independent, positive claim this probe now supports on its own terms:
    # the DERIVED Coulomb term lands every mirror split inside the Nolen-Schiffer
    # scale. This is a separate test, not a relaxation of the one above - it says
    # nothing about beating the sigma form.
    w.add_assertion(
        "derived_coulomb_reproduces_every_mirror_split_within_nolen_schiffer_scale",
        computed=1 if worst_frac < 0.20 else 0, expected=1, tolerance=0,
        source="With alpha_EM DERIVED from q0 and the CAL-3 length R0 = lambda_bar_pi (canonical "
               "`coulomb_energy` module, not this probe's former CODATA/empirical copy), the "
               "charge-symmetric core + Coulomb reproduces all three mirror splits to "
               f"{worst_frac * 100:.0f}% worst-case - inside the ~20% uniform-sphere / "
               "Nolen-Schiffer band for light nuclei. Was 37% worst-case on the old inputs.",
    )
    out = w.save()
    print(f"\nwitness → {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
