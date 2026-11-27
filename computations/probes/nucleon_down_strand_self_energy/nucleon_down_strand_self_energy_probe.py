"""Per-down-strand self term of the categorical Lagrangian (beans qou-myts, qou-99qc).

Pre-registration: PREREGISTRATION.md (this directory), written before any MeV.
Lean: QOU.Nuclear.NucleonDownStrandSelfEnergy.

Part A (exact, sympy over Q(q), full tower n = 2..5):
  * the Hecke generator on V⊗V satisfies (σ - q)(σ + q⁻¹) = 0;
  * the Leibniz Cartan operator H_tot = Σ_s H_s commutes with every σ_i on V^{⊗n},
    so the degree-1 self term is constant on every weight space, hence on every
    Wedderburn block λ ⊢ n, to all orders in q;
  * on each basis state H_tot = n - 2 n_d (one down strand moves it by -2);
  * the Weyl-even self part Σ_s H_s² = n·1 (flavour-blind).
Part B (mpmath, 80 dps, proton q₀): the variants of the pre-registration, in MeV.
CODATA m_n - m_p enters only as a ratio in the comparison block.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent))
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401, E402
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps(80)

import itertools  # noqa: E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from mpmath import mpf  # noqa: E402

mp.mp.dps = max(mp.mp.dps, 80)

from qou_substrate import codata as _codata  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qbeta import qbeta_e0  # noqa: E402

DPS = 80
M_E = mpf(_codata.codata("electron mass energy equivalent in MeV").value_str)
DM_NP_EXP = (mpf(_codata.codata("neutron mass energy equivalent in MeV").value_str)
             - mpf(_codata.codata("proton mass energy equivalent in MeV").value_str))

q = sp.symbols("q", positive=True)
H1 = sp.diag(1, -1)          # Cartan on one strand: u = +1, d = -1
I2 = sp.eye(2)


def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = sp.kronecker_product(out, m)
    return out


SIGMA = sp.Matrix([[q, 0, 0, 0],
                   [0, q - 1 / q, 1, 0],
                   [0, 1, 0, 0],
                   [0, 0, 0, q]])


def sigma_i(n, i):
    return kron(*([I2] * i + [SIGMA] + [I2] * (n - i - 2))) if n > 2 else SIGMA


def h_strand(n, s):
    return kron(*([I2] * s + [H1] + [I2] * (n - s - 1)))


def part_a():
    checks = {}
    hecke = sp.simplify((SIGMA - q * sp.eye(4)) * (SIGMA + sp.eye(4) / q))
    checks["hecke_relation"] = hecke == sp.zeros(4, 4)
    for n in range(2, 6):
        Htot = sp.zeros(2 ** n, 2 ** n)
        Hsq = sp.zeros(2 ** n, 2 ** n)
        for s in range(n):
            hs = h_strand(n, s)
            Htot += hs
            Hsq += hs * hs
        comm = all(sp.simplify(sigma_i(n, i) * Htot - Htot * sigma_i(n, i)) == sp.zeros(2 ** n, 2 ** n)
                   for i in range(n - 1))
        diag_ok = True
        for k, bits in enumerate(itertools.product((0, 1), repeat=n)):   # 1 = down
            nd = sum(bits)
            diag_ok &= Htot[k, k] == n - 2 * nd
        checks[f"n{n}_Htot_commutes_with_all_sigma"] = bool(comm)
        checks[f"n{n}_Htot_equals_n_minus_2nd"] = bool(diag_ok and Htot.is_diagonal())
        checks[f"n{n}_weyl_even_self_flavour_blind"] = Hsq == n * sp.eye(2 ** n)
    return checks


def part_b(q0):
    h = 1 - 1 / q0
    E0 = qbeta_e0.order_zero(q=q0, m_e=M_E)
    E0t = qbeta_e0.canonical(q=q0, m_e=M_E)
    forms = {
        "V0_velocity": lambda E: mpf(0),
        "V1_canonical_cartan": lambda E: 2 * h * E,
        "V2_canonical_charge_extension": lambda E: (h - h ** 2) * E,
        "Vref_gibbs_cell_2logq": lambda E: 2 * mp.log(q0) * E,
    }
    out = {"q0": fmt(q0), "h_1_minus_qinv": fmt(h), "E0_order_zero": fmt(E0), "E0_tower": fmt(E0t)}
    rows = {}
    for name, f in forms.items():
        for tag, E in (("E0_order_zero", E0), ("E0_tower", E0t)):
            v = f(E)
            rows[f"{name}|{tag}"] = {"MeV": fmt(v), "ratio_to_codata": fmt(v / DM_NP_EXP)}
            print(f"  {name:32s} {tag:14s} {mp.nstr(v, 12):>16s} MeV  ratio {mp.nstr(v / DM_NP_EXP, 8)}")
    return out, rows, h


def main():
    wb = WitnessBuilder("nucleon-down-strand-self-energy", engine="sympy+mpmath")
    wb.set_description(
        "Per-down-strand self term of the categorical Lagrangian: exact full-tower checks "
        "(n = 2..5, symbolic q) that the Leibniz Cartan self term is n - 2n_d on every weight "
        "space and commutes with the Hecke action, Weyl-even self terms are flavour-blind; then "
        "the pre-registered Legendre variants in MeV at the proton q0 (QOU.Nuclear."
        "NucleonDownStrandSelfEnergy)."
    )
    ca = part_a()
    for k, v in ca.items():
        print(f"  [A] {k}: {'PASS' if v else 'FAIL'}")
    q0 = mpf(q_at(DPS))
    print(f"\n[B] proton q0 = {mp.nstr(q0, 20)}")
    meta, rows, h = part_b(q0)
    order_ok = 2 * h < 2 * mp.log(q0) and h - h ** 2 < 2 * h
    ok = all(ca.values()) and bool(order_ok)
    wb.add_data("lean_module", "QOU.Nuclear.NucleonDownStrandSelfEnergy")
    wb.add_data("beans_referenced", ["qou-myts", "qou-99qc"])
    wb.add_data("exact_checks", {k: bool(v) for k, v in ca.items()})
    wb.add_data("anchor", meta)
    wb.add_data("variants", rows)
    wb.add_data("codata_comparison_only", {"dm_np_MeV": fmt(DM_NP_EXP)})
    path = wb.save({"q0Anchor": "proton"})
    print(f"\nwitness: {path}\nALL CHECKS {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
