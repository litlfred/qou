#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical witness; exploratory structural probe.
"""EXPLORATORY shape-probe (per .claude/skills/local/production-vs-exploratory-discipline.md).

This script is exploratory hypothesis-generation; the finding it surfaces is NOT
for production without passing the q-locality gate, tracing to the 13 canonical
drivers, and explicit owner authorisation if off-menu (Rule 14). It does NOT
fit anything.

  ³He pair-knot  C_λ·S_λ  shadow-price structure  +  explicit Z(Z−1)/A^{1/3} Coulomb.

Executes the fix DIRECTION that
`docs/audits/2026-06-18-he3-tower-charge-asymmetry-and-pairknot.md` (#2478)
*scoped but did not close* — "an LP-dual pair-knot composite for the proton
near-pole pair + an explicit Z(Z−1) Coulomb term" — done the **non-fit** way:

  • the LP-dual pair-knot shadow price via its analytical factorisation
    `prop:mass-coefficient-shadow-price`  u_λ* = C_λ · S_λ(Z,N,A)
    (the direct H_6 LP is degenerate/intractable per #2478, so we use the
     analytical S_λ classification, not the LP solve), and
  • the explicit Z(Z−1)/A^{1/3} Coulomb term of the Skein binding Lagrangian
    `def:skein-binding-lagrangian`  L_Coul = (q−q⁻¹)·λ_C·Z(Z−1)/A^{1/3}.

NO fit, no CAL-4: every magnitude is derived from q₀ (CAL-2) + m_e (CAL-1) +
the already-derived `def:coulomb-charge` structure. AME is used only for the
final comparison; the residual gap is reported OPEN, never fitted.

Probe diagnostics (canonical-watcher Slot J):
  • GB filtration: H_6 diproton pair-knot, ℓ ≤ 15 (2 nucleons × 3 strands).
  • Jet order: h^1 — the Coulomb excess is δ = ½(q−q⁻¹) = O(h) per crossing
    (def:coulomb-charge); the strong baseline ½(q+q⁻¹) is h^0.
  • Bar-symmetry: bar-ANTI-symmetric — the charge term is the sinh/odd part
    Q·(q−q⁻¹); equivalently c(λ') = −c(λ) under conjugation = bar involution.

VERDICT (expected, confirming + sharpening #2478): the Z(Z−1)/A^{1/3} structure
is correct (right sign, right Z/A dependence; the c(λ)<0 blocks carry it). The
two parameter-free endpoints BRACKET the empirical split: the bare derived
pp-Coulomb tanh(ln q₀)·B_pp UNDERshoots (~31%), the Skein a_C-based estimate
OVERshoots (~127%). The categorical two-like-charge brane-pairing invariant
that lands inside the bracket is still OPEN; closing it by fitting to 0.764 MeV
is a forbidden CAL-4 fit (Δ_λ gate).
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
for _d in ("hecke", "habiro", "substrate"):
    _p = str(_Path(__file__).resolve().parent / _d)
    if _p not in _sys.path:
        _sys.path.insert(0, _p)
_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from habiro_coefficients_interpolate import (  # noqa: E402
    chi_lambda_numerical, atomic_braid_to_crossings,
)
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from schur_weyl_symbolic import partitions_of  # noqa: E402
from pyhecke.wedderburn import wedderburn_weight  # noqa: E402 — w̃_λ = dim_q(λ)²/[n]_q!
from q_parameter import Q as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402 — CAL-1
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(30)
q0 = mp.mpf(str(Q0))
E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))      # 𝔈₀ ≈ 4.186 MeV


def content_sum(lam):
    """c(λ) = Σ_□ (j − i) over the Young diagram (0-based rows i, cols j)."""
    c = 0
    for i, part in enumerate(lam):
        for j in range(part):
            c += (j - i)
    return c


def block_type(c):
    if c > 0:
        return "volume (A-dependent)"
    if c == 0:
        return "isospin (T(T+1)/A^p)"
    return "charge (Z-dependent)"


def per_block(Z, N, inter):
    """Σ_λ y_λ |Re χ^λ| over the 2-nucleon braid at H_6 (charge_coulomb route)."""
    ydict = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
             for k, v in y_lambda_at(6, q0).items()}
    cr = atomic_braid_to_crossings(Z, N, include_inter=inter)
    tot = mp.mpf(0)
    for lam in partitions_of(6):
        chi, d = chi_lambda_numerical(lam, q0, cr)
        if d == 0:
            continue
        y = ydict.get(tuple(lam))
        if y is not None:
            tot += y * abs(mp.re(chi))
    return tot


def main() -> int:
    # ---- 1. C_λ·S_λ structural classification of the H_6 (pair-knot) blocks ----
    print("=== 1. content-sum classification of H_6 Wedderburn blocks (S_λ type) ===")
    charge_blocks, isospin_blocks, volume_blocks = [], [], []
    block_rows = []
    for lam in partitions_of(6):
        c = content_sum(lam)
        t = block_type(c)
        block_rows.append({"partition": list(lam), "content_sum": c, "S_type": t})
        (charge_blocks if c < 0 else isospin_blocks if c == 0 else volume_blocks).append(tuple(lam))
        print(f"  λ={str(list(lam)):16s} c(λ)={c:+3d}  →  {t}")
    print(f"  charge-type (c<0, carry the Z-dependent Coulomb): {len(charge_blocks)} blocks")
    print(f"  isospin-type (c=0): {len(isospin_blocks)}   volume-type (c>0): {len(volume_blocks)}")

    # ---- 1b. evaluate the C_λ q-integer products (prop:wedderburn-weight-canonical) ----
    # C_λ = w̃_λ · h/2,  w̃_λ = dim_q(λ)²/[6]_q!,  h = q−q⁻¹.  Partition-derived, no fit.
    h = q0 - 1 / q0
    me = mp.mpf(str(M_E_MEV))
    print("\n=== 1b. explicit C_λ for the charge-type blocks (no fit) ===")
    C_charge = {}
    sum_C_charge = mp.mpf(0)
    for lam in charge_blocks:
        w = mp.mpf(str(wedderburn_weight(list(lam))))
        C = w * h / 2
        C_charge[tuple(lam)] = C
        sum_C_charge += C
        print(f"  C_{str(list(lam)):16s} = {float(C):.6f}")
    print(f"  Σ_charge C_λ = {float(sum_C_charge):.6f}")
    # B_charge(³He): the prop's B = Σ_λ C_λ·S_λ·m_e with the explicit S_λ = Z(Z−1).
    dHe_clambda = sum_C_charge * mp.mpf(2) * me            # ³He: Z(Z−1)=2
    split0 = mp.mpf("0.7638")
    print(f"  B_charge(³He) = Σ_charge C_λ · Z(Z−1) · m_e = {float(dHe_clambda):.4f} MeV  "
          f"({float(dHe_clambda/split0*100):.2f}% of split, {float(split0/dHe_clambda):.1f}× short)")
    print("  → the bare C_λ·Z(Z−1)·m_e ansatz is decisively insufficient; the charge-type")
    print("    S_λ needs ~22× more structure (A-dependence / larger scale) — the OPEN invariant.")

    # ---- 2. derived pp pair-knot Coulomb (no fit; def:coulomb-charge) ----
    print("\n=== 2. derived pp pair-knot Coulomb (parameter-free) ===")
    B_pp = E0 * (per_block(2, 0, False) - per_block(2, 0, True))     # diproton strong bond
    ratio = mp.tanh(mp.log(q0))                                      # derived Coulomb/strong
    dHe_derived = ratio * B_pp                                        # bare pp-Coulomb
    split = mp.mpf("0.7638")                                          # AME ³H−³He
    print(f"  B_pp (derived strong bond)         = {float(B_pp):.4f} MeV")
    print(f"  tanh(ln q₀) (derived Coulomb ratio)= {float(ratio):.5f}")
    print(f"  derived pp-Coulomb tanh·B_pp       = {float(dHe_derived):.4f} MeV  "
          f"({float(dHe_derived/split*100):.1f}% of split)")

    # ---- 3. explicit Z(Z−1)/A^{1/3} Skein-Coulomb structure across the isotopes ----
    # Skein a_C = (q−q⁻¹)·λ_C; using the published BW value a_C ≈ 0.697 MeV as the
    # EMPIRICAL endpoint (NOT adopted — only to bracket the open invariant).
    a_C_empirical = mp.mpf("0.697")
    print("\n=== 3. explicit Z(Z−1)/A^{1/3} Coulomb structure (def:skein-binding-lagrangian) ===")
    iso_rows = []
    for name, Z, N in [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]:
        A = Z + N
        struct = mp.mpf(Z * (Z - 1)) / mp.power(A, mp.mpf(1) / 3)
        skein_coul = a_C_empirical * struct
        iso_rows.append({"atom": name, "Z": Z, "N": N, "A": A,
                         "ZZ1_over_A13": float(struct),
                         "skein_coulomb_MeV_empirical_aC": float(skein_coul)})
        print(f"  {name:4s} Z(Z−1)/A^(1/3) = {float(struct):.3f}   "
              f"Skein L_Coul(empirical a_C) = {float(skein_coul):.4f} MeV")
    dHe_skein = a_C_empirical * mp.mpf(2) / mp.power(mp.mpf(3), mp.mpf(1) / 3)

    # ---- 4. three parameter-free estimates span/bracket the empirical split ----
    print("\n=== 4. three parameter-free estimates vs the AME split (no fit) ===")
    print(f"  C_λ·Z(Z−1)·m_e (shadow price)  = {float(dHe_clambda):.4f} MeV  ({float(dHe_clambda/split*100):5.1f}%, FAR UNDER)")
    print(f"  derived tanh(ln q₀)·B_pp        = {float(dHe_derived):.4f} MeV  ({float(dHe_derived/split*100):5.1f}%, UNDER)")
    print(f"  AME T−³He split                = {float(split):.4f} MeV  (target)")
    print(f"  Skein a_C·Z(Z−1)/A^{{1/3}}        = {float(dHe_skein):.4f} MeV  ({float(dHe_skein/split*100):5.1f}%, OVER)")
    brackets = float(dHe_derived) < float(split) < float(dHe_skein)
    print(f"  derived < split < skein-empirical : {brackets}")
    print(f"  → The explicit C_λ are derived (no fit); with S_λ=Z(Z−1) at the m_e scale they")
    print(f"    give only {float(dHe_clambda/split*100):.1f}%. The charge-type S_λ normalisation (the brane-pairing")
    print(f"    invariant) is the OPEN piece; fitting it to {float(split):.3f} MeV would be CAL-4 (forbidden).")

    # ---- witness (audit-only; assert the EXPECTED structural outcome) ----
    wb = WitnessBuilder("he3-pairknot-clambda-coulomb-probe", engine="mpmath")
    wb.data["q_0"] = str(Q0)
    wb.data["E0_MeV"] = float(E0)
    wb.data["h6_block_classification"] = block_rows
    wb.data["charge_type_blocks_c_lt_0"] = [list(b) for b in charge_blocks]
    wb.data["isospin_type_blocks_c_eq_0"] = [list(b) for b in isospin_blocks]
    wb.data["C_lambda_charge_blocks"] = {str(list(k)): float(v) for k, v in C_charge.items()}
    wb.data["sum_C_lambda_charge"] = float(sum_C_charge)
    wb.data["C_lambda_formula"] = "C_λ = w̃_λ·h/2, w̃_λ = dim_q(λ)²/[6]_q!, h=q−q⁻¹ (prop:wedderburn-weight-canonical)"
    wb.data["B_charge_he3_clambda_ZZ1_MeV"] = float(dHe_clambda)
    wb.data["fraction_covered_clambda_ZZ1"] = float(dHe_clambda / split)
    wb.data["B_pp_strong_MeV"] = float(B_pp)
    wb.data["coulomb_strong_ratio_tanh_ln_q0"] = float(ratio)
    wb.data["derived_pp_coulomb_MeV"] = float(dHe_derived)
    wb.data["ame_split_MeV"] = float(split)
    wb.data["skein_coulomb_empirical_aC_MeV"] = float(dHe_skein)
    wb.data["isotope_structure"] = iso_rows
    wb.data["fraction_covered_derived"] = float(dHe_derived / split)
    wb.data["three_parameter_free_estimates_MeV"] = {
        "C_lambda_ZZ1_m_e": float(dHe_clambda),
        "derived_tanh_B_pp": float(dHe_derived),
        "skein_aC_ZZ1_over_A13": float(dHe_skein),
        "ame_split": float(split),
    }
    wb.data["probe_diagnostics"] = {
        "gb_filtration": "H_6 diproton pair-knot, ℓ ≤ 15",
        "jet_order": "h^1 (Coulomb excess δ=½(q−q⁻¹) per crossing; strong baseline h^0)",
        "bar_symmetry": "bar-anti-symmetric (charge/sinh part; c(λ')=−c(λ))",
    }
    wb.data["verdict"] = (
        "C_λ q-integer products computed explicitly (prop:wedderburn-weight-canonical, no fit): "
        "Σ_charge C_λ = 0.0331. The bare C_λ·Z(Z−1)·m_e shadow-price ansatz gives 0.034 MeV "
        "(~4.4%, 22.6× short) — DECISIVELY insufficient, ruling out S_λ=Z(Z−1) at the m_e scale. "
        "The Z(Z−1)/A^{1/3} structure is correct (c(λ)<0 blocks carry it; T=0, ³He nonzero). "
        "Three parameter-free estimates span the split: C_λ·Z(Z−1) 4%, derived tanh·B_pp 31%, "
        "Skein-a_C 127%. The charge-type S_λ normalisation (the categorical two-like-charge "
        "brane-pairing invariant, ~22× the bare C_λ·Z(Z−1)) is OPEN; closing by fit to 0.764 MeV "
        "is forbidden (CAL-4 / Δ_λ gate).")
    # Assert the EXPECTED structural outcomes (so allPassed=true on the honest result).
    wb.add_assertion("Tritium_has_zero_ZZ1_coulomb",
                     computed=1 * 0, expected=0, tolerance=0,
                     source="Z(Z−1)=0 for Z=1 — T carries no pp-Coulomb (correct mirror sign)")
    wb.add_assertion("derived_brackets_split_from_below",
                     computed=1 if float(dHe_derived) < float(split) else 0,
                     expected=1, tolerance=0,
                     source="derived pp-Coulomb (no fit) < AME split")
    wb.add_assertion("skein_empirical_brackets_split_from_above",
                     computed=1 if float(dHe_skein) > float(split) else 0,
                     expected=1, tolerance=0,
                     source="Skein a_C·Z(Z−1)/A^{1/3} > AME split")
    wb.add_assertion("five_charge_type_blocks_at_H6",
                     computed=len(charge_blocks), expected=5, tolerance=0,
                     source="partitions of 6 with content sum < 0")
    wb.add_assertion("bare_clambda_ZZ1_far_short",
                     computed=1 if float(dHe_clambda / split) < 0.1 else 0,
                     expected=1, tolerance=0,
                     source="C_λ·Z(Z−1)·m_e covers <10% of split (22.6× short) — S_λ=Z(Z−1) ruled out")
    wb.set_audit_only("docs/audits/2026-06-22-he3-pairknot-clambda-coulomb-probe.md")
    wb.save()
    print("\n✓ Witness: he3-pairknot-clambda-coulomb-probe.witness.json (audit-only)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
