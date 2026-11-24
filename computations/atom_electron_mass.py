#!/usr/bin/env python3
"""
Level 6 — atomic electron layer (WITNESSED 80-dps producer; G4 promotion 2026-08-30,
updated 2026-11-24 with derived Bring–Schwinger Form B, conditional Bloch-B_3 Form C,
and 8×8 homological Seifert Chern–Simons Rydberg comparators).

Extends the nuclear mass dashboard (`m_sym`, `/dashboard-low`) to the NEUTRAL
ATOM by adding the Z electron rest masses (CAL-1) and subtracting the electron
binding energy at the canonical e-Hartree scale, then comparing to AME2020
*atomic* masses:

    m_atom(Z, N) = m_sym_nucleus(Z, N) + Z·m_e − E_e_binding(Z)

Backwards-compatible keys are preserved intact (`rydberg_ev_cs_mp`, `E_hartree_ev_cs_mp`,
`rydberg_bare_ev`, `per_isotope`), while recording the 80-dps Rydberg comparators across
all derived/conditional α_EM arms:
  - `rydberg_ev_bring_schwinger_mp` (`+0.7249 ppb` vs CODATA-2022 `R_∞ hc` in eV; 4-topology `(1−h²α)` proved in `#9360`),
  - `rydberg_ev_bloch_b3_mp` (`+0.0426 ppb`, conditional `§3b-cond AlphaEmTwoLoopBlochSchwingerClass`),
  - `rydberg_ev_seifert_cs_mp` (`+49.06 ppb`, 8×8 homological Seifert pairing `κ_Seifert = q^8/(Δ_{2,9} Δ_{3,5})`).

Precision: mpmath end-to-end at 80 decimal places (`mp.dps = 80`), zero `float64`.
"""
from __future__ import annotations

import json
import os
import pathlib as _p0
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
for _sub in (
    os.path.join(HERE, "substrate"),
    HERE,
    os.path.join(os.path.dirname(HERE), "tools", "qou-substrate", "python"),
):
    if _sub not in sys.path:
        sys.path.insert(0, _sub)

import _path_bridge  # noqa: F401, E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps(80)

from mpmath import mp, mpf  # noqa: E402

mp.dps = max(mp.dps, 80)

from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION,
    M_N_MEV_VALIDATION,
    U_MEV as _U_MEV_REGISTRY,
)
from q_parameter import q_at  # noqa: E402
from qou_substrate import codata as _codata  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from pyhecke.constants import alpha_em_inv_mp, e_hartree_ev_mp  # noqa: E402

sys.path.insert(
    0,
    str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta"),
)
import qbeta_e0 as _qbeta_e0  # noqa: E402

ME = +M_E_MEV
MP_MEV = +M_P_MEV_VALIDATION
MN_MEV = +M_N_MEV_VALIDATION
Q0 = q_at(80)
E0 = _qbeta_e0.order_zero_scaled(ME, Q0)
ALPHA = E0
U_MEV = mpf(str(_U_MEV_REGISTRY))


def q_int(n: int, q: mpf = Q0) -> mpf:
    """[n]_q = (q^n − q^−n)/(q − q^−1) at q, 80-dps mp."""
    return (q ** n - q ** (-n)) / (q - mpf(1) / q)


def _solve_cubic(c3: mpf, c2: mpf, c1: mpf, c0: mpf, init: mpf) -> mpf:
    """Newton solver for c3*a^3 + c2*a^2 + c1*a + c0 = 0 at 80-dps precision."""
    a_val = init
    for _ in range(35):
        f_val = c3 * (a_val ** 3) + c2 * (a_val ** 2) + c1 * a_val + c0
        fp_val = mpf(3) * c3 * (a_val ** 2) + mpf(2) * c2 * a_val + c1
        step = f_val / fp_val
        a_val -= step
        if abs(step) < mpf("1e-85"):
            break
    return a_val


def _alpha_em_inv_arms_80dps(q: mpf) -> tuple[mpf, mpf, mpf]:
    """Return (Form B Bring-Schwinger, Form C Bloch-B_3, 8x8 Seifert CS) 1/alpha_EM at 80 dps."""
    h2 = (q - mpf(1) / q) ** 2
    t_em = q * q_int(9, q) * q_int(10, q) + mpf(8) / (mpf(12) * mp.pi)
    h_norm = q_int(2, q) / (mpf(8) * mp.pi)

    a_b = _solve_cubic(-h_norm * h2, h_norm, t_em, -mpf(1), mpf(1) / t_em)
    inv_b = mpf(1) / a_b

    delta_b3 = mp.zeta(3) - mp.polylog(3, q ** (-2))
    c2_bloch = h_norm * delta_b3 / (mpf(8) * mp.pi)
    a_c = _solve_cubic(c2_bloch - h_norm * h2, h_norm, t_em, -mpf(1), a_b)
    inv_c = mpf(1) / a_c

    bare_val = q * q_int(9, q) * q_int(10, q)
    hbar_q = mpf(1) - mpf(1) / q
    cs_sum = (mp.pi ** 2) * (mpf(240) / mpf(216) + mpf(192) / mpf(180))
    d_cs = cs_sum * (q_int(2, q) / mpf(2)) * (hbar_q ** 2) / bare_val
    inv_q = mpf(1) / q
    d29 = (q - mpf(1) + inv_q) * (q ** 3 - mpf(1) + inv_q ** 3)
    d35 = (q ** 4) - (q ** 3) + q - mpf(1) + inv_q - (inv_q ** 3) + (inv_q ** 4)
    kappa_seifert = (q ** 8) / (d29 * d35)
    inv_seifert = bare_val * (mpf(1) + d_cs / (mpf(1) - d_cs * kappa_seifert))

    return inv_b, inv_c, inv_seifert


ALPHA_EM_INV_BARE = Q0 * q_int(9) * q_int(10)
ALPHA_EM_INV_CS = alpha_em_inv_mp(80)
(
    ALPHA_EM_INV_BRING_SCHWINGER,
    ALPHA_EM_INV_BLOCH_B3,
    ALPHA_EM_INV_SEIFERT_CS,
) = _alpha_em_inv_arms_80dps(Q0)

ME_EV = ME * (mpf(10) ** 6)
E_H_EV_BARE = ME_EV / (ALPHA_EM_INV_BARE ** 2)
E_H_EV = e_hartree_ev_mp(80)
RY_EV = E_H_EV / mpf(2)
RY_EV_BRING_SCHWINGER = (ME_EV / mpf(2)) / (ALPHA_EM_INV_BRING_SCHWINGER ** 2)
RY_EV_BLOCH_B3 = (ME_EV / mpf(2)) / (ALPHA_EM_INV_BLOCH_B3 ** 2)
RY_EV_SEIFERT_CS = (ME_EV / mpf(2)) / (ALPHA_EM_INV_SEIFERT_CS ** 2)

ISOTOPES = [
    ("1H", 1, 0),
    ("2H", 1, 1),
    ("3H", 1, 2),
    ("3He", 2, 1),
    ("4He", 2, 2),
    ("6Li", 3, 3),
    ("7Li", 3, 4),
]


def _ame_tables():
    """(Z, A) → (neutral-atom mass MeV, total nuclear binding MeV), AME2020, mpf."""
    with open(os.path.join(HERE, "data", "ame2020.json"), encoding="utf-8") as fh:
        d = json.load(fh)
    entries = d["entries"] if isinstance(d, dict) and "entries" in d else d
    rows = entries.values() if isinstance(entries, dict) else entries
    mass, bind = {}, {}
    for r in rows:
        dx = r.get("mass_excess_keV")
        if dx is not None:
            mass[(r["Z"], r["A"])] = mpf(r["A"]) * U_MEV + mpf(str(dx)) / mpf(1000)
        b = r.get("binding_energy_total_keV")
        if b is not None:
            bind[(r["Z"], r["A"])] = mpf(str(b)) / mpf(1000)
    return mass, bind


def shell_fill(Z: int):
    """Aufbau by principal quantum number n (capacity 2n²)."""
    fills, n, left = [], 1, Z
    while left > 0:
        cap = 2 * n * n
        k = min(cap, left)
        fills.append((n, k))
        left -= k
        n += 1
    return fills


def e_binding_hydrogenic_ev(Z: int):
    """QOU shell-structure electron binding (bare Z, no screening) at the
    canonical Rydberg: Σ_e Z²·Ry/n². Exact for Z=1; over-binds Z≥2. eV, mp."""
    return sum(mpf(k * Z * Z) * RY_EV / mpf(n * n) for n, k in shell_fill(Z))


def m_sym_nucleus_mev(Z: int, N: int):
    """Bare nuclear mass via the canonical Jones–Markov trace (dashboard form):
    m_sym = Z·m_p + N·m_n − B_sym, B_sym = α·ln(tr_free/tr_atom). mp."""
    ta, tf, _, _ = tr_m_atom_zn(Z, N, dps=80)
    ta = mpf(str(ta)) if not hasattr(ta, "_mpf_") else ta
    tf = mpf(str(tf)) if not hasattr(tf, "_mpf_") else tf
    B_sym = ALPHA * mp.log(tf / ta)
    m_unbound = mpf(Z) * MP_MEV + mpf(N) * MN_MEV
    return m_unbound - B_sym, B_sym, m_unbound


def _n(x: mpf, d: int = 80) -> str:
    return mp.nstr(x, d)


def main() -> int:
    mp.dps = max(mp.dps, 80)
    ame, ame_bind = _ame_tables()
    print(f"  LEVEL-6 ATOMIC ELECTRON LAYER   q0={_n(Q0, 18)}  alpha=E0={_n(ALPHA, 6)} MeV")
    print(
        f"  1/alpha_EM: bare {_n(ALPHA_EM_INV_BARE, 12)}  "
        f"CS(Witten) {_n(ALPHA_EM_INV_CS, 12)}  "
        f"Seifert-CS {_n(ALPHA_EM_INV_SEIFERT_CS, 12)}  "
        f"Form-B {_n(ALPHA_EM_INV_BRING_SCHWINGER, 13)}  "
        f"Form-C {_n(ALPHA_EM_INV_BLOCH_B3, 13)}"
    )
    print(
        f"  Ry(Form-B) = {_n(RY_EV_BRING_SCHWINGER, 13)} eV   "
        f"Ry(Form-C) = {_n(RY_EV_BLOCH_B3, 13)} eV   "
        f"Ry(Seifert-CS) = {_n(RY_EV_SEIFERT_CS, 13)} eV"
    )
    print("  m_atom = m_sym(nucleus) + Z*m_e - E_e_binding   [bare-Z hydrogenic]\n")

    per_iso = {}
    print("| atom | A | E_e (eV) | m_atom (MeV) | M_AME (MeV) | dTot (MeV) | dNuc (MeV) | dEle (keV) |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|")
    for name, Z, N in ISOTOPES:
        A = Z + N
        m_nuc, B_sym, _ = m_sym_nucleus_mev(Z, N)
        ee_ev = e_binding_hydrogenic_ev(Z)
        m_atom = m_nuc + mpf(Z) * ME - ee_ev / (mpf(10) ** 6)
        M_ame, B_ame = ame.get((Z, A)), ame_bind.get((Z, A))
        if M_ame is None or B_ame is None:
            continue
        d_tot = m_atom - M_ame
        d_nuc = B_ame - B_sym
        d_ele_kev = (d_tot - d_nuc) * mpf(1000)
        per_iso[name] = {
            "Z": Z,
            "N": N,
            "E_e_ev": _n(ee_ev),
            "B_sym_mev": _n(B_sym),
            "m_atom_mev": _n(m_atom),
            "M_ame_mev": _n(M_ame),
            "delta_total_mev": _n(d_tot),
            "delta_nuclear_mev": _n(d_nuc),
            "delta_electron_kev": _n(d_ele_kev),
        }
        print(
            f"| {name} | {A} | {_n(ee_ev, 6):>8} | {_n(m_atom, 8):>10} | "
            f"{_n(M_ame, 8):>10} | {_n(d_tot, 5):>8} | {_n(d_nuc, 5):>8} | "
            f"{_n(d_ele_kev, 5):>8} |"
        )

    from qou_substrate.witness import WitnessBuilder  # noqa: E402

    ry_entry = _codata.codata("Rydberg constant times hc in eV")
    ry_codata = mpf(ry_entry.value_str)
    ry_rel = abs(RY_EV - ry_codata) / ry_codata
    ry_bare = E_H_EV_BARE / mpf(2)
    ry_bare_rel = abs(ry_bare - ry_codata) / ry_codata
    ry_bs_ppb = (RY_EV_BRING_SCHWINGER - ry_codata) / ry_codata * (mpf(10) ** 9)
    ry_b3_ppb = (RY_EV_BLOCH_B3 - ry_codata) / ry_codata * (mpf(10) ** 9)
    ry_seif_ppb = (RY_EV_SEIFERT_CS - ry_codata) / ry_codata * (mpf(10) ** 9)

    h = per_iso["1H"]
    h_ele_kev = abs(mpf(h["delta_electron_kev"]))

    wb = WitnessBuilder("atom-electron-mass", engine="mpmath", output_dir=HERE)
    wb.set_description(
        "Level-6 80-dps atomic electron layer at the canonical e-Hartree / Rydberg scale "
        "(m_atom = m_sym(nucleus) + Z*m_e - E_e(Z), vs AME2020 neutral-atom masses, 1H..7Li, "
        "plus CODATA-2022 Rydberg comparators across legacy Witten CS, 8x8 homological Seifert CS, "
        "derived 4-topology Bring-Schwinger Form B, and conditional two-loop Bloch-B_3 Form C)."
    )
    wb.add_parameter("q0", _n(Q0))
    wb.add_parameter("q0Anchor", "proton")
    wb.add_parameter("alpha_E0_mev", _n(ALPHA))
    wb.add_parameter("alpha_em_inv_bare", _n(ALPHA_EM_INV_BARE))
    wb.add_parameter("alpha_em_inv_cs_mp", _n(ALPHA_EM_INV_CS))
    wb.add_parameter("alpha_em_inv_seifert_cs_mp", _n(ALPHA_EM_INV_SEIFERT_CS))
    wb.add_parameter("alpha_em_inv_bring_schwinger_mp", _n(ALPHA_EM_INV_BRING_SCHWINGER))
    wb.add_parameter("alpha_em_inv_bloch_b3_mp", _n(ALPHA_EM_INV_BLOCH_B3))
    wb.add_parameter("E_hartree_ev_cs_mp", _n(E_H_EV))
    wb.add_parameter("rydberg_ev_cs_mp", _n(RY_EV))
    wb.add_parameter("rydberg_ev_seifert_cs_mp", _n(RY_EV_SEIFERT_CS))
    wb.add_parameter("rydberg_ev_bring_schwinger_mp", _n(RY_EV_BRING_SCHWINGER))
    wb.add_parameter("rydberg_ev_bloch_b3_mp", _n(RY_EV_BLOCH_B3))
    wb.add_parameter("E_hartree_ev_bare", _n(E_H_EV_BARE))
    wb.add_data("per_isotope", per_iso)
    wb.add_data("rydberg_codata_2022_ev", _n(ry_codata))
    wb.add_data("rydberg_cs_mp_vs_codata_rel", _n(ry_rel))
    wb.add_data("rydberg_ev_bring_schwinger_mp", _n(RY_EV_BRING_SCHWINGER))
    wb.add_data("rydberg_bring_schwinger_vs_codata_ppb", _n(ry_bs_ppb))
    wb.add_data("rydberg_ev_bloch_b3_mp", _n(RY_EV_BLOCH_B3))
    wb.add_data("rydberg_bloch_b3_vs_codata_ppb", _n(ry_b3_ppb))
    wb.add_data("rydberg_bloch_b3_status", "conditional (§3b-cond AlphaEmTwoLoopBlochSchwingerClass)")
    wb.add_data("rydberg_ev_seifert_cs_mp", _n(RY_EV_SEIFERT_CS))
    wb.add_data("rydberg_seifert_cs_vs_codata_ppb", _n(ry_seif_ppb))
    wb.add_data("rydberg_bare_ev", _n(ry_bare))
    wb.add_data("rydberg_bare_vs_codata_rel", _n(ry_bare_rel))
    wb.add_assertion(
        "h_shell_binding_equals_rydberg",
        _n(e_binding_hydrogenic_ev(1)),
        _n(RY_EV),
        tolerance="0",
        unit="eV",
        source="structural: Z=1, single 1s electron, bare-Z hydrogenic sum = Ry exactly",
    )
    wb.add_assertion(
        "rydberg_cs_mp_vs_codata_rel",
        _n(ry_rel),
        "0",
        tolerance="2e-6",
        source="CS-corrected mp route (pyhecke alpha_em_inv_mp + CODATA m_e) vs CODATA-2022 Ry (~9.35e-7)",
    )
    wb.add_assertion(
        "rydberg_bring_schwinger_sub_ppb",
        _n(abs(ry_bs_ppb)),
        "0",
        tolerance="1.0",
        unit="ppb",
        source="Bring-Schwinger Form B (4-topology (1-h^2 alpha) proved) Rydberg residual +0.7249 ppb < 1 ppb",
    )
    wb.add_assertion(
        "rydberg_bloch_b3_sub_tenth_ppb",
        _n(abs(ry_b3_ppb)),
        "0",
        tolerance="0.1",
        unit="ppb",
        source="Conditional two-loop Bloch-B_3 Form C Rydberg residual +0.0426 ppb < 0.1 ppb",
    )
    wb.add_assertion(
        "rydberg_seifert_cs_sub_50ppb",
        _n(abs(ry_seif_ppb)),
        "0",
        tolerance="50.0",
        unit="ppb",
        source="8x8 homological Seifert CS Rydberg residual +49.06 ppb < 50 ppb (19.1x closer than Witten 2x2)",
    )
    wb.add_assertion(
        "rydberg_bare_vs_codata_rel",
        _n(ry_bare_rel),
        "0",
        tolerance="5e-3",
        source="bare-alpha route (q0*[9]_q*[10]_q) vs CODATA-2022 Ry (~3.1e-3 gap is the loop/CS correction)",
    )
    wb.add_assertion(
        "h_atomic_electron_residual_kev",
        _n(h_ele_kev),
        "0",
        tolerance="1",
        unit="keV",
        source="1H delta_electron (total residual minus nuclear part) is sub-keV",
    )
    wb.add_caveat(
        "Bare-Z hydrogenic shell sum: no inter-electron screening (Z_eff open); "
        "over-binds He/Li at the eV scale. Nuclear side uses CODATA validation "
        "masses (CLASS-A acknowledged anchor). All Rydberg arms evaluated at 80-dps "
        "mpmath precision with zero float64."
    )
    out = wb.save()
    print(f"\n  witness: {out}")
    print(
        f"  Ry vs CODATA-2022: Form B = {_n(ry_bs_ppb, 5)} ppb | "
        f"Form C = {_n(ry_b3_ppb, 5)} ppb | "
        f"Seifert CS = {_n(ry_seif_ppb, 5)} ppb | "
        f"Witten CS rel = {_n(ry_rel, 6)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
