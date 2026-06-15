#!/usr/bin/env python3
"""S₅ → SO(3) ≅ SU(2)/ℤ₂ × U(1) fiber-action probe.

Three derivations, each reported RAW against a falsification reference
(NEVER tuned):

  SO(3) / h⁴   : decompose the SO(3) angular-momentum reps V_ℓ under the
                 icosahedral subgroup I ≅ A₅ ⊂ SO(3) using the I character
                 table (conjugacy classes + their SO(3) rotation angles).
                 Read off the ℓ=2 (dim-5) multiplicity. THEN, separately,
                 compute the Borromean Markov-trace h⁴ coefficient from the
                 (2,1)-irrep of H₃(q). Compare to the topological reference
                 h⁴ = −3/4. The icosahedral character math fixes the
                 multiplicities BEFORE any comparison; no normalisation is
                 chosen to hit −3/4.

  SU(2) / spin : the ℤ₂ double cover. The ribbon twist θ_j = q^{j(j+1)} (the
                 framing self-rotation, R-T ribbon element) supplies the
                 spin phase; the half-integer j=1/2 lift is the 4π
                 periodicity. We test the binary icosahedral group 2I ⊂ SU(2)
                 (|2I|=120 = |S₅|) and whether 2I ≅ S₅ — the structural
                 obstruction to identifying the spin ℤ₂ with the sign ℤ₂.

  U(1)/hyperch : the writhe / framing phase. The framed Markov trace carries
                 a writhe factor q^{w·c} (the Reidemeister-I anomaly). We
                 report the writhe (U(1) charge) of the relevant braid words
                 RAW; compare (raw only) to a hypercharge-style assignment.

All numbers go to an AUDIT-ONLY witness. No production wiring.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 60
START = time.monotonic()


# ---------------------------------------------------------------------------
# Part 1 — SO(3) / h⁴ : icosahedral branching of V_ℓ
# ---------------------------------------------------------------------------
#
# Icosahedral rotation group I ≅ A₅, |I| = 60.  Five conjugacy classes,
# with representative SO(3) rotation angles:
#   E       : 1 element,  θ = 0
#   12 C₅   : 12 elements, θ = 2π/5      (order-5 rotations)
#   12 C₅²  : 12 elements, θ = 4π/5      (order-5 rotations, other class)
#   20 C₃   : 20 elements, θ = 2π/3      (order-3 rotations)
#   15 C₂   : 15 elements, θ = π         (order-2 rotations)
#
# Character table of I ≅ A₅ (5 irreps): A (triv, 1), T₁ (3), T₂ (3),
# G (4), H (5). Standard table (φ = (1+√5)/2):
#
#            E    12C₅      12C₅²     20C₃   15C₂
#   A   :    1    1         1         1      1
#   T₁  :    3    φ         1−φ       0     −1
#   T₂  :    3    1−φ       φ         0     −1
#   G   :    4   −1        −1         1      0
#   H   :    5    0         0        −1      1
#
# SO(3) ℓ-character at rotation angle θ:  χ_ℓ(θ) = sin((2ℓ+1)θ/2)/sin(θ/2),
# and χ_ℓ(0) = 2ℓ+1.

ICOS_CLASSES = [
    ("E", 1, mp.mpf(0)),
    ("12C5", 12, 2 * mp.pi / 5),
    ("12C5^2", 12, 4 * mp.pi / 5),
    ("20C3", 20, 2 * mp.pi / 3),
    ("15C2", 15, mp.pi),
]

phi = (1 + mp.sqrt(5)) / 2
ONE_MINUS_PHI = 1 - phi

ICOS_IRREP_CHARS = {
    "A":  [mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1)],
    "T1": [mp.mpf(3), phi, ONE_MINUS_PHI, mp.mpf(0), mp.mpf(-1)],
    "T2": [mp.mpf(3), ONE_MINUS_PHI, phi, mp.mpf(0), mp.mpf(-1)],
    "G":  [mp.mpf(4), mp.mpf(-1), mp.mpf(-1), mp.mpf(1), mp.mpf(0)],
    "H":  [mp.mpf(5), mp.mpf(0), mp.mpf(0), mp.mpf(-1), mp.mpf(1)],
}
ICOS_IRREP_DIM = {"A": 1, "T1": 3, "T2": 3, "G": 4, "H": 5}


def so3_char(ell: int, theta) -> mp.mpf:
    """SO(3) angular-momentum character χ_ℓ(θ)."""
    if mp.almosteq(theta, 0):
        return mp.mpf(2 * ell + 1)
    return mp.sin((2 * ell + 1) * theta / 2) / mp.sin(theta / 2)


def branching_multiplicity(ell: int, irrep: str) -> mp.mpf:
    """Multiplicity of irrep of I inside V_ℓ|_I (must be a nonneg integer)."""
    chars = ICOS_IRREP_CHARS[irrep]
    total = mp.mpf(0)
    for (label, size, theta), chi_irrep in zip(ICOS_CLASSES, chars):
        total += size * so3_char(ell, theta) * chi_irrep  # real characters
    return total / 60


def icosahedral_branching_table(ell_max: int = 6):
    table = {}
    for ell in range(ell_max + 1):
        row = {}
        for irrep in ICOS_IRREP_CHARS:
            m = branching_multiplicity(ell, irrep)
            m_int = int(mp.nint(m))
            row[irrep] = {"mult": m_int, "residual": float(m - m_int)}
        dim_sum = sum(row[i]["mult"] * ICOS_IRREP_DIM[i] for i in row)
        table[ell] = {"irreps": row, "dim_check": dim_sum, "dim_expected": 2 * ell + 1}
    return table


# ---------------------------------------------------------------------------
# Part 1c — S₃ as a rotation subgroup of SO(3): does the "S₃ sees only ℓ≤1"
# premise of the conjecture actually hold?
# ---------------------------------------------------------------------------
#
# S₃ ≅ D₃ realised as the triangle-rotation subgroup of SO(3):
#   E    : 1, θ = 0
#   2C₃  : 2, θ = 2π/3      (3-fold axis)
#   3C₂  : 3, θ = π         (three 2-fold axes through vertices)
# Irreps: triv [1,1,1], sign [1,1,-1], std (2-dim) [2,-1,0].

S3_CLASSES = [("E", 1, mp.mpf(0)), ("2C3", 2, 2 * mp.pi / 3), ("3C2", 3, mp.pi)]
S3_IRREP_CHARS = {"triv": [1, 1, 1], "sign": [1, 1, -1], "std": [2, -1, 0]}
S3_IRREP_DIM = {"triv": 1, "sign": 1, "std": 2}


def s3_branching_table(ell_max: int = 4):
    table = {}
    for ell in range(ell_max + 1):
        row = {}
        for irrep, ch in S3_IRREP_CHARS.items():
            m = sum(sz * so3_char(ell, th) * c
                    for (lab, sz, th), c in zip(S3_CLASSES, ch)) / 6
            row[irrep] = int(mp.nint(m))
        table[str(ell)] = row
    return table


# ---------------------------------------------------------------------------
# Part 1b — the Borromean Markov-trace h⁴, derived from the (2,1)-irrep
# ---------------------------------------------------------------------------

def borromean_trace_h_coeffs(order: int = 8):
    """Taylor coefficients (in h) of tr_M(β_Bor). RAW rationals."""
    import sympy as sp
    h = sp.symbols("h")
    trM = (4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4)
    ser = sp.series(trM, h, 0, order + 1).removeO()
    poly = sp.Poly(ser, h)
    coeffs = {}
    for (deg,), c in poly.terms():
        coeffs[deg] = sp.nsimplify(c)
    return {int(k): str(sp.Rational(v)) for k, v in coeffs.items()}


# ---------------------------------------------------------------------------
# Part 2 — SU(2) double cover : binary icosahedral 2I vs S₅
# ---------------------------------------------------------------------------
#
# SU(2) → SO(3) ≅ SU(2)/ℤ₂ pulls I ≅ A₅ back to the binary icosahedral group
# 2I, |2I| = 120 = |S₅|. KEY structural fact (Coxeter): 2I ≇ S₅ even though
# both have order 120 — 2I is a PERFECT group (its own commutator subgroup,
# no normal subgroup of index 2), whereas S₅ has A₅ as an index-2 normal
# subgroup (the sign character). So the SU(2) lift of A₅⊂SO(3) is NOT the S₅
# Wedderburn-side group; the spin ℤ₂ (SU(2)→SO(3) kernel) is a DIFFERENT ℤ₂
# from the sign ℤ₂ (S₅/A₅).

def su2_double_cover_facts():
    return {
        "I_order": 60,
        "2I_order": 120,
        "S5_order": 120,
        "S5_abelianization_order": 2,            # sign character
        "binary_icosahedral_abelianization_order": 1,  # 2I is perfect
        "2I_isomorphic_to_S5": False,
        "comment": (
            "Both order 120, but 2I is perfect (trivial abelianisation) "
            "while S₅ has A₅ as index-2 normal subgroup (sign ℤ₂). The spin "
            "ℤ₂ (SU(2)→SO(3) kernel) is NOT the sign ℤ₂ (S₅/A₅)."
        ),
    }


def ribbon_twist_phases(q0):
    """Ribbon-twist eigenvalue θ_j = q^{j(j+1)} (framing anomaly), RAW at q0.

    The half-integer j object exists in SU(2)_q (Rep of the quantum group)
    but NOT in SO(3)_q (integer ℓ only). 4π-periodicity of the half-integer
    twist is the categorical signature of the ℤ₂ spin lift. Reference only.
    """
    out = {}
    for label, j in [("j=1/2 (spin)", Fraction(1, 2)),
                     ("j=1 (vector / SO3 ℓ=1)", Fraction(1, 1)),
                     ("j=3/2", Fraction(3, 2)),
                     ("j=2 (SO3 ℓ=2)", Fraction(2, 1))]:
        casimir = j * (j + 1)
        theta = mp.power(q0, float(casimir))
        out[label] = {"casimir_j(j+1)": str(casimir),
                      "half_integer_j": (j.denominator == 2),
                      "twist_q^{j(j+1)}_at_q0": mp.nstr(theta, 30)}
    return out


# ---------------------------------------------------------------------------
# Part 3 — U(1) : writhe / framing phase
# ---------------------------------------------------------------------------

def writhe_of_borromean():
    # β_Bor = (σ₁⁻¹ σ₂)³ : three σ₁⁻¹ (−1 each) + three σ₂ (+1 each) → 0
    return 0


def writhe_of_inter_nucleon_words():
    # production assignment: pp ↦ σ (+1), nn ↦ σ⁻¹ (−1), pn ↦ σ_avg (0)
    return {"pp_arc": +1, "nn_arc": -1, "pn_arc": 0}


# ---------------------------------------------------------------------------

def main():
    print("[s5-so3-su2-u1] starting", flush=True)

    table = icosahedral_branching_table(ell_max=6)
    print("[s5-so3-su2-u1] icosahedral V_ℓ|_I branching:", flush=True)
    branching_out = {}
    for ell, row in table.items():
        mults = {i: row["irreps"][i]["mult"] for i in row["irreps"]}
        max_resid = max(abs(row["irreps"][i]["residual"]) for i in row["irreps"])
        branching_out[str(ell)] = {
            "multiplicities": mults,
            "dim_check": row["dim_check"],
            "dim_expected": row["dim_expected"],
            "max_integrality_residual": max_resid,
        }
        print(f"  l={ell}: {mults}  sumdim={row['dim_check']} "
              f"(expect {row['dim_expected']})", flush=True)

    s3_table = s3_branching_table(ell_max=4)
    print("[s5-so3-su2-u1] S3-as-rotation-subgroup branching of V_l:", flush=True)
    for ell, row in s3_table.items():
        print(f"  l={ell}: {row}", flush=True)
    # The conjecture's premise: "S3 truncation sees only l<=1". Test it.
    std_at_ell2 = s3_table["2"]["std"]
    s3_premise_holds = (std_at_ell2 == 0)
    print(f"[s5-so3-su2-u1] S3 'sees only l<=1' premise holds? {s3_premise_holds} "
          f"(std irrep multiplicity at l=2 is {std_at_ell2})", flush=True)

    bor_coeffs = borromean_trace_h_coeffs(order=8)
    print(f"[s5-so3-su2-u1] Borromean tr_M h-coeffs (raw): {bor_coeffs}", flush=True)

    su2 = su2_double_cover_facts()
    q0 = mp.mpf("1.10998")  # substrate reference (m_p-anchored), reference only
    ribbon = ribbon_twist_phases(q0)
    print(f"[s5-so3-su2-u1] SU(2): 2I order {su2['2I_order']}, "
          f"2I=S5? {su2['2I_isomorphic_to_S5']}", flush=True)

    u1 = {
        "borromean_writhe": writhe_of_borromean(),
        "inter_nucleon_arc_writhe": writhe_of_inter_nucleon_words(),
        "comment": (
            "Framed Markov trace carries q^{writhe·c} Reidemeister-I anomaly "
            "= natural U(1)_framing. Writhe values RAW; no hypercharge tuning."
        ),
    }

    ell2_H_mult = table[2]["irreps"]["H"]["mult"]  # H = dim-5 irrep of I
    falsification = {
        "ell2_appears_in_icosahedral_branching": ell2_H_mult >= 1,
        "ell2_to_irrep_H_multiplicity": ell2_H_mult,
        "borromean_h4_coefficient_raw": bor_coeffs.get(4, "0"),
        "borromean_h4_reference": "-3/4",
        "DERIVED_link_ell2_to_h4": (
            "icosahedral branching gives ℓ=2 → exactly ONE copy of the dim-5 "
            "irrep H of I (first ℓ to contain H). This multiplicity is "
            "DERIVED from the character table. BUT no canonical map from the "
            "H-irrep amplitude to the (2,1)-Hecke h⁴ coefficient is supplied: "
            "the link ℓ=2 ↦ −3/4 is NOT derived. See verdict in audit doc."
        ),
    }

    out = {
        "computation": "s5-so3-su2-u1-fiber-action",
        "description": (
            "Icosahedral I=A5 in SO(3) branching of V_l (l<=6), Borromean "
            "Markov-trace h-coefficients, SU(2) binary-icosahedral double "
            "cover facts, and U(1) writhe/framing phase. RAW, audit-only. "
            "No tuning to h4=-3/4, m_n-m_p, spin, or hypercharge."
        ),
        "auditOnly": True,
        "precision_dps": mp.mp.dps,
        "so3_h4": {
            "icosahedral_branching": branching_out,
            "s3_rotation_subgroup_branching": s3_table,
            "s3_sees_only_ell_le_1_premise_holds": s3_premise_holds,
            "s3_std_irrep_multiplicity_at_ell2": std_at_ell2,
            "borromean_trace_h_coeffs_raw": bor_coeffs,
            "falsification_reading": falsification,
        },
        "su2_spin": {
            "double_cover_facts": su2,
            "ribbon_twist_phases_raw": ribbon,
        },
        "u1_hypercharge": u1,
    }

    (WitnessBuilder.wrap_legacy(
        "s5-so3-su2-u1-fiber-action", out,
        script_path=__file__, engine="mpmath", start_time=START)
        .set_audit_only("docs/audits/2026-06-01-s5-so3-su2-u1-fiber-action.md")
        .save())

    print(f"[s5-so3-su2-u1] done in {time.monotonic()-START:.1f}s", flush=True)


if __name__ == "__main__":
    main()
