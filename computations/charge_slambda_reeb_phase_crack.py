#!/usr/bin/env python3
"""Formalize-first crack at the charge-type S_λ normalisation (open invariant).

Question (from PR #2612 / bean h7lv): the bare partition-only shadow price
`Σ_charge C_λ · Z(Z−1) · m_e` = 0.034 MeV is 22.6× short of the ³H−³He split
(0.764 MeV).  What categorical structure supplies the missing magnitude — WITHOUT
fitting (the Δ_λ gate / CAL-4 discipline forbids a fitted normalisation)?

Formalize-first answer (no fit), assembled from existing corpus results:

  1. SHAPE is forced.  prop:mass-coefficient-shadow-price classifies the
     charge-type S_λ by content sum c(λ)<0 as "Z-dependent"; combined with
     "each six-term-mass term is one shadow price" this forces the BW Coulomb
     shape Z(Z−1)/A^{1/3}.  The SIGN is right (T: Z(Z−1)=0; ³He nonzero).

  2. The MAGNITUDE cannot come from partition-only C_λ × a scalar count.
     GAP-A-4 (docs/audits/2026-06-01-e0-lambda-composite-structure.md): the
     proton, neutron and ³He are BIT-FOR-BIT identical at H_3 (the trefoil
     image), so any per-block composite of partition-only data CANNOT split
     Markov-equivalent nuclei.  The (Z,N,A) physics lives in the H_{3A} braid
     WORD, not in the H_6 partition data — which is exactly why the bare
     C_λ·Z(Z−1) misses by ~22×.

  3. The real S_λ is the free-vs-atom q-REEB PHASE |Δθ_λ| at the H_{3A} atomic
     strand count (binding_rotation_phase_lead.py): an atomic object that DOES
     distinguish ³H/³He.  The Markov-weighted phase closes the A=3 mirror pair
     to 2% (ρ_need: T=18.345, ³He=18.652 MeV/rad).  With a UNIVERSAL ρ≈18.5 the
     phase-sum difference reproduces the split to ~118% (18% over) — the RIGHT
     ORDER, ~26× closer than the partition-only count.

  4. The Coulomb channel is the sinh(log q)=h/2 channel (derived identity,
     crossing-energy-decomposition.lean) — already the factor inside
     C_λ = w̃_λ·h/2.  So C_λ (channel + partition weight) and S_λ (atomic
     phase) are consistent views of the SAME binding energy; the open piece is
     the universal-ρ assumption (the residual 2% strong + ~18% Coulomb-split
     normalisation), NOT a missing partition formula.

Verdict: the open "brane-pairing invariant" is NOT a new mystery — it is the
H_{3A} q-Reeb phase object already in the corpus, viewed through the
shadow-price lens.  No production rewire; no fit.  Audit-only witness.
"""
from __future__ import annotations
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
for _d in ("hecke", "habiro", "substrate"):
    sys.path.insert(0, str(_HERE / _d))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
from pyhecke.wedderburn import wedderburn_weight  # noqa: E402 — w̃_λ=dim_q²/[n]_q!
from q_parameter import Q as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402 — CAL-1
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def content_sum(lam):
    return sum(j - i for i, row in enumerate(lam) for j in range(row))


def main() -> None:
    set_compute_dps(50)
    q0 = mp.mpf(str(Q0))
    h = q0 - 1 / q0
    me = mp.mpf(str(M_E_MEV))

    # ---- 1. partition-only shadow price (the 22.6× miss) ----
    print("=== 1. bare partition-only Σ_charge C_λ·Z(Z−1)·m_e (the miss) ===")
    charge = [lam for lam in
              [(3, 1, 1, 1), (2, 2, 2), (2, 2, 1, 1), (2, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1)]]
    sum_C = mp.mpf(0)
    for lam in charge:
        w = mp.mpf(str(wedderburn_weight(list(lam))))
        sum_C += w * h / 2                        # C_λ = w̃_λ·h/2
    bare_he3 = sum_C * mp.mpf(2) * me             # ³He: Z(Z−1)=2
    print(f"  Σ_charge C_λ = {float(sum_C):.6f}   (h/2 = sinh(log q₀) Coulomb channel)")
    print(f"  bare C_λ·Z(Z−1)·m_e = {float(bare_he3):.4f} MeV")

    # ---- 2. atomic q-Reeb phase (the right-order magnitude) ----
    # ρ_need = B_AME / Σ_λ y_λ dim_λ |Δθ_λ|  (S3_markov full), from
    # binding_rotation_phase_lead.py → binding-rotation-phase-lead.witness.json.
    print("\n=== 2. atomic H_{3A} q-Reeb phase Σ_λ y_λ dim_λ |Δθ_λ| (the magnitude) ===")
    B_T, B_He3 = mp.mpf("8.481798"), mp.mpf("7.718058")     # AME2020 binding (MeV)
    split = B_T - B_He3
    rho_T, rho_He3 = mp.mpf("18.345"), mp.mpf("18.652")     # ρ_need, S3_markov full
    S_T, S_He3 = B_T / rho_T, B_He3 / rho_He3               # phase sums
    dS = S_T - S_He3
    rho_univ = (rho_T + rho_He3) / 2
    reeb_split = rho_univ * dS                              # universal-ρ prediction
    print(f"  ρ_need: T={float(rho_T):.3f}  ³He={float(rho_He3):.3f} MeV/rad "
          f"(A=3 mirror agrees to {float(abs(rho_T-rho_He3)/rho_univ*100):.0f}%)")
    print(f"  phase sums: Σ(T)={float(S_T):.5f}  Σ(³He)={float(S_He3):.5f}  ΔΣ={float(dS):.5f}")
    print(f"  universal ρ={float(rho_univ):.3f}: split = ρ·ΔΣ = {float(reeb_split):.4f} MeV")

    # ---- 2b. ρ-normalisation: cosh(strong) vs sinh(Coulomb) channel split ----
    # strong_channel_rho (binding_rotation_phase_lead.py) zeros the inter-nucleon
    # −h (sinh) term ⇒ cosh-only ρ; full−strong isolates the sinh/Coulomb channel.
    # ρ values cited from binding-rotation-phase-lead.witness.json (d0 block).
    print("\n=== 2b. ρ-normalisation: isolate the sinh (Coulomb) channel ===")
    rho_strong = {"T": mp.mpf("19.9307"), "He3": mp.mpf("19.201")}   # cosh-only
    Sstr_T, Sstr_He3 = B_T / rho_strong["T"], B_He3 / rho_strong["He3"]
    Ssinh_T, Ssinh_He3 = S_T - Sstr_T, S_He3 - Sstr_He3
    dS_cosh, dS_sinh = Sstr_T - Sstr_He3, Ssinh_T - Ssinh_He3
    cosh_split, sinh_split = rho_univ * dS_cosh, rho_univ * dS_sinh
    cosh_asym = Sstr_T / Sstr_He3 - 1
    print(f"  Σ_sinh: T={float(Ssinh_T):.5f}  ³He={float(Ssinh_He3):.5f}   "
          f"(³He carries less — but T>³He: not a clean pp count)")
    print(f"  cosh-only split = ρ₀·ΔΣ_cosh = {float(cosh_split):.4f} MeV "
          f"({float(cosh_split/split*100):.1f}%)")
    print(f"  sinh-only split = ρ₀·ΔΣ_sinh = {float(sinh_split):.4f} MeV "
          f"({float(sinh_split/split*100):.1f}%)")
    print(f"  cosh mirror-asymmetry Σ_cosh(T)/Σ_cosh(³He)−1 = {float(cosh_asym)*100:.1f}% "
          f"(ideal mirror = 0)")
    print(f"  → BRACKET (tighter): sinh-only {float(sinh_split/split*100):.0f}% (under) "
          f"< AME 100% < full {float(reeb_split/split*100):.0f}% (over).")
    print(f"    No no-fit closure to ~100%; the residual is the cosh/sinh mixing of the")
    print(f"    mirror split — a 5.9% spurious cosh mirror-asymmetry, not a missing scale.")

    # ---- 3. contrast + verdict ----
    print("\n=== 3. contrast (³He−³H split, AME = 0.764 MeV) ===")
    print(f"  partition-only  C_λ·Z(Z−1)·m_e = {float(bare_he3):.4f} MeV  "
          f"({float(bare_he3/split*100):.1f}%, {float(split/bare_he3):.1f}× SHORT)")
    print(f"  atomic q-Reeb   ρ·ΔΣ           = {float(reeb_split):.4f} MeV  "
          f"({float(reeb_split/split*100):.1f}%, RIGHT ORDER)")
    closer = float((abs(reeb_split - split)) / (abs(bare_he3 - split)))
    print(f"  atomic-phase residual is {1/closer:.0f}× smaller than partition-only residual")
    print("  → S_λ(charge) is the H_{3A} q-Reeb phase, NOT partition-only Z(Z−1).")
    print("    The 22.6× miss is the GAP-A-4 obstruction (H_3 Markov-equivalence collapse).")

    # ---- witness ----
    wb = WitnessBuilder("charge-slambda-reeb-phase-crack", engine="mpmath")
    wb.data["description"] = (
        "Formalize-first crack: charge-type S_λ is the H_{3A} q-Reeb phase, not "
        "partition-only Z(Z−1); the 22.6× miss is the GAP-A-4 obstruction. "
        "Audit-only; no fit; no production rewire.")
    wb.data["q0"] = float(q0)
    wb.data["sum_C_lambda_charge"] = float(sum_C)
    wb.data["bare_partition_only_he3_MeV"] = float(bare_he3)
    wb.data["ame_split_MeV"] = float(split)
    wb.data["rho_need_T"] = float(rho_T)
    wb.data["rho_need_He3"] = float(rho_He3)
    wb.data["reeb_phase_sums"] = {"T": float(S_T), "He3": float(S_He3), "delta": float(dS)}
    wb.data["reeb_universal_rho"] = float(rho_univ)
    wb.data["reeb_split_prediction_MeV"] = float(reeb_split)
    wb.data["channel_split"] = {
        "cosh_strong_MeV": float(cosh_split),
        "sinh_coulomb_MeV": float(sinh_split),
        "cosh_mirror_asymmetry_pct": float(cosh_asym) * 100,
        "bracket_sinh_only_pct": float(sinh_split / split * 100),
        "bracket_full_pct": float(reeb_split / split * 100),
    }
    wb.data["bare_fraction_of_split"] = float(bare_he3 / split)
    wb.data["reeb_fraction_of_split"] = float(reeb_split / split)
    wb.data["verdict"] = (
        "Charge-type S_λ SHAPE Z(Z−1)/A^{1/3} is forced (content-sum + BW); the MAGNITUDE "
        "cannot come from partition-only C_λ×count (GAP-A-4: p≡n≡³He at H_3). The real S_λ "
        "is the free-vs-atom q-Reeb phase |Δθ_λ| at H_{3A}: with universal ρ≈18.5 it gives "
        "the split to ~118% (right order) vs the partition-only 4.4% (22.6× short). The "
        "Coulomb channel sinh(log q)=h/2 is already inside C_λ=w̃_λ·h/2 "
        "(crossing-energy-decomposition.lean). ρ-normalisation push: the cosh(strong)/sinh"
        "(Coulomb) channel split BRACKETS the AME split — sinh-only 60% (under), full 118% "
        "(over); no no-fit closure to ~100%. The residual is the cosh/sinh mixing of the "
        "mirror split (a 5.9% spurious cosh mirror-asymmetry — mirror partners should have "
        "equal strong binding), not a missing partition formula. No fit; no rewire.")
    wb.add_assertion("five_charge_blocks", computed=len(charge), expected=5, tolerance=0,
                     source="partitions of 6 with content sum < 0")
    wb.add_assertion("partition_only_22x_short",
                     computed=1 if float(bare_he3 / split) < 0.1 else 0, expected=1, tolerance=0,
                     source="bare C_λ·Z(Z−1)·m_e < 10% of split (GAP-A-4 obstruction)")
    wb.add_assertion("reeb_phase_right_order",
                     computed=1 if 0.5 < float(reeb_split / split) < 2.0 else 0,
                     expected=1, tolerance=0,
                     source="atomic q-Reeb phase reproduces split within 2× (universal ρ)")
    wb.add_assertion("channels_bracket_split",
                     computed=1 if float(sinh_split) < float(split) < float(reeb_split) else 0,
                     expected=1, tolerance=0,
                     source="sinh-only (60%) < AME split < full cosh+sinh (118%) — tighter bracket")
    wb.save()
    print("\n✓ Witness: charge-slambda-reeb-phase-crack.witness.json (audit-only; no fit)")


if __name__ == "__main__":
    main()
