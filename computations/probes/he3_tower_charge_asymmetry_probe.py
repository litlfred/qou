"""³He brane-tower charge-asymmetry probe — quantify the spurious mirror split.

Follow-up to `he3_brane_tower_structural_gap.py` (merged PR #2467), which showed
*ordinally* that the per-generator brane tower Σ_i −Li₂^q(−|V̂_i|) has the wrong
Z-ordering for the A=3 mirror pair (tower ³He > tritium, but ³He is the LESS
bound member). This probe makes the deficit *quantitative* and connects it to
the already-derived structural Coulomb work, WITHOUT introducing any fit.

Structural framing (charge symmetry / isospin):
  The strong nuclear force is charge-symmetric. The strong binding of the A=3
  mirror pair ³H(1p2n) / ³He(2p1n) should therefore be ~equal, and the observed
  B(³H) − B(³He) = 0.7638 MeV is ~entirely the Coulomb energy of ³He's pp pair
  (already derived as tanh(ln q₀)·B_pp, def:coulomb-charge / charge_coulomb_
  tn3he_derived.py — covers ~31%, the residual is a known-open, forbidden CAL-4
  magnitude). A *charge-symmetric* binding model must give tower(³He) ≈ tower(³H);
  the brane tower instead carries a spurious asymmetry Δtower = tower(³He) −
  tower(³H) > 0 that FAVORS ³He — the opposite sign to the physical split.

What this probe reports (all from production |V̂_i^full| + canonical constants;
no free parameter):
  1. Δtower = tower(³He) − tower(³H), and the scale-free fractional asymmetry
     Δtower / tower(³H). The SIGN is the rigorous result (scale-independent).
  2. For order-of-magnitude context only, E₀·Δtower in MeV with E₀ = m_e/(q₀(q₀−1))
     ≈ 4.186 MeV (the canonical per-block energy scale used by charge_coulomb_
     tn3he_derived.py). CAVEAT: the per-generator-tower → binding wiring is the
     z-Habiro hypothesis verdicted NON-production in PR #2467; this MeV figure is
     a cross-model order-of-magnitude comparison, not a binding prediction.
  3. The consequence for the fix: a structural Coulomb term (which makes ³He LESS
     bound) must overcome BOTH the physical 0.7638 MeV split AND the spurious
     E₀·Δtower tower asymmetry. So the pair-knot composite's job (the open
     "categorical two-like-charge brane-pairing invariant") is FIRST to remove
     the spurious Δtower (charge-symmetrise the proton near-pole pair), only THEN
     does the derived Coulomb split it correctly.

EXPLORATORY / audit-only — no production rewire, no fit. mpmath 50 dps.
Audit: docs/audits/2026-06-18-he3-tower-charge-asymmetry-and-pairknot.md
"""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

# Reuse the production per-generator |V̂_i^full| + the canonical −Li₂^q tower term
# from the merged diagnosis probe (single source of truth — no VHAT duplication).
_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent / "substrate"))
from he3_brane_tower_structural_gap import (  # noqa: E402
    Q0, VHAT, Z_N, B_AME, neg_li2q_neg,
)
from codata_constants import M_E_MEV  # noqa: E402 — CAL-1, never inline (P31)

mp.mp.dps = 50


def main() -> int:
    self_path = Path(__file__).resolve()
    script_hash = hashlib.sha256(self_path.read_bytes()).hexdigest()[:12]

    towers: dict[str, mp.mpf] = {}
    for atom, zs in VHAT.items():
        towers[atom] = sum(neg_li2q_neg(mp.mpf(s), Q0) for s in zs)

    t_T = towers["tritium"]
    t_He = towers["helium3"]
    d_tower = t_He - t_T                         # spurious mirror asymmetry
    frac_asym = d_tower / t_T                     # scale-free

    q0 = Q0
    E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))   # 𝔈₀ ≈ 4.186 MeV (canonical scale)
    asym_MeV_at_E0 = E0 * d_tower                 # cross-model OOM context only

    coulomb_split_AME = mp.mpf(str(B_AME["tritium"])) - mp.mpf(str(B_AME["helium3"]))

    # Signs: tower asymmetry favors ³He (d_tower > 0); physical binding favors ³H
    # (coulomb_split_AME > 0). Opposite sign ⇒ the tower asymmetry is spurious and
    # must be removed before a (³He-reducing) Coulomb term can give the right order.
    asym_opposes_physical = bool(d_tower > 0 and coulomb_split_AME > 0)
    # Is the spurious asymmetry (at the canonical scale) a non-negligible fraction
    # of the physical split it would have to be subtracted from?
    asym_over_split = asym_MeV_at_E0 / coulomb_split_AME

    print(f"{'atom':>9} {'Z,N':>5} {'tower Σ−Li₂^q':>16}")
    for atom in VHAT:
        Z, N = Z_N[atom]
        print(f"{atom:>9} {f'{Z},{N}':>5} {mp.nstr(towers[atom], 12):>16}")
    print()
    print(f"E₀ = m_e/(q₀(q₀−1))            = {mp.nstr(E0, 8)} MeV  (canonical scale)")
    print(f"Δtower = tower(³He) − tower(³H) = {mp.nstr(d_tower, 8)}   (FAVORS ³He — wrong sign)")
    print(f"fractional asymmetry Δtower/T  = {mp.nstr(frac_asym, 6)}  (scale-free)")
    print(f"E₀·Δtower (OOM context, MeV)   = {mp.nstr(asym_MeV_at_E0, 6)} MeV")
    print(f"AME T−³He split (physical)     = {mp.nstr(coulomb_split_AME, 6)} MeV  (FAVORS ³H)")
    print(f"E₀·Δtower / (T−³He split)      = {mp.nstr(asym_over_split, 6)}")
    print()
    print("VERDICT: the per-generator brane tower's mirror asymmetry Δtower>0 has "
          "the OPPOSITE sign to the physical split (³He less bound). At the "
          "canonical E₀ scale it is of the same order as the 0.76 MeV Coulomb "
          "split itself — so it is NOT a small correction. A charge-symmetric "
          "model must first REMOVE Δtower (the pair-knot composite's role) before "
          "the derived tanh(ln q₀) Coulomb term can split the mirror correctly. "
          "Quantifies why the z-Habiro brane tower is non-production (#2467) and "
          "scopes the open brane-pairing invariant.")

    assertions = [
        {"name": "tower_asymmetry_favors_He3",
         "computed": 1 if d_tower > 0 else 0, "expected": 1, "tolerance": 0,
         "note": "Δtower = tower(³He) − tower(³H) > 0 (tower over-binds the proton-rich member)"},
        {"name": "asymmetry_opposes_physical_split",
         "computed": 1 if asym_opposes_physical else 0, "expected": 1, "tolerance": 0,
         "note": "tower asymmetry sign opposes AME (³He less bound) — spurious"},
        {"name": "asymmetry_same_order_as_coulomb_split",
         "computed": 1 if mp.mpf("0.1") < asym_over_split else 0, "expected": 1,
         "tolerance": 0,
         "note": "E₀·Δtower ≳ 0.1×(T−³He split): not a negligible correction"},
    ]
    all_passed = all(a["computed"] == a["expected"] for a in assertions)

    witness = {
        "engine": "mpmath",
        "engineVersion": f"mpmath {mp.__version__}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "he3-tower-charge-asymmetry",
        "scriptFile": self_path.name,
        "scriptHash": script_hash,
        "contentBlock": "conj:brane-tower-z-habiro",
        "auditOnly": True,
        "auditDoc": "docs/audits/2026-06-18-he3-tower-charge-asymmetry-and-pairknot.md",
        "description": (
            "Quantifies the spurious charge-asymmetry of the per-generator brane "
            "tower for the A=3 mirror pair (³H/³He): Δtower = tower(³He) − tower(³H) "
            "> 0 favors the proton-rich member, OPPOSITE to the physical split "
            "(³He less bound). At the canonical E₀ = m_e/(q₀(q₀−1)) scale the "
            "asymmetry is the same order as the 0.76 MeV Coulomb split. No fit; "
            "production |V̂_i^full|, CAL-1 m_e, derived q₀. EXPLORATORY."
        ),
        "parameters": {
            "q_0_50dps": mp.nstr(Q0, 50),
            "tower_form": "−Li₂^q(−|V̂_i^full|) (production li2q, per-generator)",
            "E0_MeV": mp.nstr(E0, 12),
            "E0_def": "m_e/(q_0 (q_0 − 1)), CAL-1 m_e, canonical per-block scale",
            "scale_caveat": (
                "per-generator-tower → binding wiring is the z-Habiro hypothesis "
                "verdicted non-production in PR #2467; E0·Δtower is a cross-model "
                "order-of-magnitude figure, not a binding prediction."
            ),
        },
        "data": {
            "towers": {a: mp.nstr(towers[a], 16) for a in VHAT},
            "delta_tower_He3_minus_T": mp.nstr(d_tower, 16),
            "frac_asymmetry": mp.nstr(frac_asym, 12),
            "E0_times_delta_tower_MeV": mp.nstr(asym_MeV_at_E0, 12),
            "ame_T_minus_He3_split_MeV": mp.nstr(coulomb_split_AME, 12),
            "asym_over_split": mp.nstr(asym_over_split, 12),
        },
        "assertions": assertions,
        "allPassed": all_passed,
        "provenance": [
            "he3_brane_tower_structural_gap.py (VHAT, neg_li2q_neg) — PR #2467",
            "terms-2-3-atom-per-gen-mpfr-50dps.witness.json",
            "codata_constants.M_E_MEV (CAL-1)",
            "AME2020 (B_AME)",
        ],
    }
    out = self_path.parent.parent / "he3-tower-charge-asymmetry.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"\nwrote {out}   allPassed={all_passed}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
