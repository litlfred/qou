#!/usr/bin/env python3
"""
Level 6 — atomic electron layer (WITNESSED producer; G4 promotion 2026-08-30).

Extends the nuclear mass dashboard (`m_sym`, `/dashboard-low`) to the NEUTRAL
ATOM by adding the Z electron rest masses (CAL-1) and subtracting the electron
binding energy at the canonical e-Hartree scale, then comparing to AME2020
*atomic* masses.

    m_atom(Z, N) = m_sym_nucleus(Z, N) + Z·m_e − E_e_binding(Z)

History: through 2026-08-29 this was an exploratory diagnostic (no witness).
Promoted to a witnessed producer per gap G4 of
docs/audits/2026-08-29-mass-provenance-breakdown-and-gap-map.md: the
/dashboard-low atomic table imports its electron binding from the AME
Lunney-Pearson empirical fit, while the framework-derived e-Hartree route
lived only here, unwitnessed. This witness records the derived e-layer so the
fit-vs-derived comparison is auditable. The dashboard itself is NOT rewired by
this promotion (that swap is a separate, owner-visible decision).

What is canonical here
----------------------
  m_sym nucleus    Z·m_p + N·m_n − B_sym,  B_sym = α·ln(tr_free / tr_atom) from
                   the one Jones–Markov transfer trace (identical to
                   /dashboard-low). α = E₀ = m_e / (q₀(q₀−1)) alongside the
                   untruncated closed-form tower E₀^tower = m_e·q₀/((q₀−1)(2q₀−1)).
  Z·m_e            electron rest mass, the CAL-1 anchor (M_E_MEV).
  e-Hartree scale  E_h = α_EM²·m_e c²; Rydberg Ry = E_h/2. α_EM here is the
                   CS-corrected derived value via meson_em_sinh_closed_form
                   alpha_em_inv_derived(q₀, order=None) (mpmath end-to-end),
                   recorded alongside the bare α_EM⁻¹ = q₀·[9]_q·[10]_q and the
                   1-loop Form-B Bring–Schwinger cubic root α_EM⁻¹.
  capacity         neutral atom = Z electrons; hydrogenic shell sum Σ Z²·Ry/n²
                   with aufbau capacity 2n². Exact for Z = 1.

Precision: mpmath end-to-end at COMPUTE dps 60 (zero float64 intermediates).
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "substrate"))
sys.path.insert(0, HERE)

import _path_bridge  # noqa: F401, E402
from mpmath import mp, mpf  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps(60)

from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION,
    M_N_MEV_VALIDATION,
    U_MEV as _U_MEV_REGISTRY,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from meson_em_sinh_closed_form import alpha_em_inv_derived  # noqa: E402

ME = mpf(str(M_E_MEV))                      # CAL-1
MP_MEV = mpf(str(M_P_MEV_VALIDATION))       # CLASS-A validation anchor
MN_MEV = mpf(str(M_N_MEV_VALIDATION))       # CLASS-A validation anchor
Q0 = mpf(Q_50_DIGIT_STR)                    # proton pin
E0 = ME / (Q0 * (Q0 - mpf(1)))              # order-0 α = E₀^(0), mp
E0_TOWER = (ME * Q0) / ((Q0 - mpf(1)) * (mpf(2) * Q0 - mpf(1)))  # untruncated E₀^(∞) = E₀^(0)/(1 - ℏ_q²)
ALPHA = E0
U_MEV = mpf(str(_U_MEV_REGISTRY))


def q_int(n: int) -> mpf:
    """[n]_q = (q^n − q^−n)/(q − q^−1) at q₀, mp."""
    return (Q0 ** n - Q0 ** (-n)) / (Q0 - mpf(1) / Q0)


ALPHA_EM_INV_BARE = Q0 * q_int(9) * q_int(10)            # bare derived α_EM⁻¹, mp
ALPHA_EM_INV_CS = alpha_em_inv_derived(Q0, order=None)   # CS-corrected exact resummation, mp

# 1-loop Form-B Bring–Schwinger cubic root α_EM⁻¹:
_H0 = Q0 - mpf(1) / Q0
_H_HAB = q_int(2) / (mpf(8) * mp.pi)
_T_EM = ALPHA_EM_INV_BARE + mpf(2) / (mpf(3) * mp.pi)
_A_EM_FORMA = (-_T_EM + mp.sqrt(_T_EM ** 2 + mpf(4) * _H_HAB)) / (mpf(2) * _H_HAB)
_A_EM_FORMB = mp.findroot(
    lambda a: -_H_HAB * (_H0 ** 2) * (a ** 3) + _H_HAB * (a ** 2) + _T_EM * a - mpf(1),
    _A_EM_FORMA,
)
ALPHA_EM_INV_BRING_SCHWINGER = mpf(1) / _A_EM_FORMB

ME_EV = ME * (mpf(10) ** 6)                                         # m_e c² in eV, exact CAL-1
E_H_EV_BARE = ME_EV / (ALPHA_EM_INV_BARE ** 2)                      # Hartree at bare α, eV, mp
E_H_EV = ME_EV / (ALPHA_EM_INV_CS ** 2)                             # Hartree at CS α (canonical), mp
RY_EV = E_H_EV / mpf(2)                                             # Rydberg (CS-corrected), eV, mp
E_H_EV_BRING_SCHWINGER = ME_EV / (ALPHA_EM_INV_BRING_SCHWINGER ** 2)
RY_EV_BRING_SCHWINGER = E_H_EV_BRING_SCHWINGER / mpf(2)

# Low-isotope set, mirroring /dashboard-low plus protium ¹H (A=1 showcase).
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
    with open(os.path.join(HERE, "data", "ame2020.json")) as fh:
        d = json.loads(fh.read())
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


def e_binding_hydrogenic_ev(Z: int, ry_ev: mpf | None = None) -> mpf:
    """QOU shell-structure electron binding (bare Z, no screening) at the
    canonical Rydberg: Σ_e Z²·Ry/n². Exact for Z=1; over-binds Z≥2. eV, mp."""
    ry = RY_EV if ry_ev is None else ry_ev
    return sum(mpf(k * (Z * Z)) * ry / mpf(n * n) for n, k in shell_fill(Z))


def m_sym_nucleus_mev(Z: int, N: int, e0_scale: mpf | None = None):
    """Bare nuclear mass via the canonical Jones–Markov trace (dashboard form):
    m_sym = Z·m_p + N·m_n − B_sym, B_sym = α·ln(tr_free/tr_atom). mp."""
    alpha_scale = ALPHA if e0_scale is None else e0_scale
    ta, tf, _, _ = tr_m_atom_zn(Z, N, dps=50)
    ta = mpf(str(ta)) if not hasattr(ta, "_mpf_") else ta
    tf = mpf(str(tf)) if not hasattr(tf, "_mpf_") else tf
    B_sym = alpha_scale * mp.log(tf / ta)
    m_unbound = mpf(Z) * MP_MEV + mpf(N) * MN_MEV
    return m_unbound - B_sym, B_sym, m_unbound


def _n(x, d=50):
    return mp.nstr(x, d)


def main() -> int:
    ame, ame_bind = _ame_tables()
    print(f"  LEVEL-6 ATOMIC ELECTRON LAYER   q0={_n(Q0, 17)}  alpha=E0={_n(ALPHA, 6)} MeV  (E0_tower={_n(E0_TOWER, 6)} MeV)")
    print(f"  1/alpha_EM: bare {_n(ALPHA_EM_INV_BARE, 12)}  CS-corrected(mp) {_n(ALPHA_EM_INV_CS, 12)}  Bring-Schwinger {_n(ALPHA_EM_INV_BRING_SCHWINGER, 13)}")
    print(f"  E_Hartree(CS,mp) = {_n(E_H_EV, 10)} eV   Ry = {_n(RY_EV, 10)} eV   "
          f"(Bring-Schwinger Ry: {_n(RY_EV_BRING_SCHWINGER, 10)} eV)")
    print("  m_atom = m_sym(nucleus) + Z*m_e - E_e_binding   [bare-Z hydrogenic]\n")

    per_iso = {}
    print("| atom | A | E_e (eV) | m_atom (MeV) | M_AME (MeV) | dTot (MeV) | dNuc (MeV) | dEle (keV) |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|")
    for name, Z, N in ISOTOPES:
        A = Z + N
        m_nuc, B_sym, _ = m_sym_nucleus_mev(Z, N)
        B_sym_tower = B_sym * (E0_TOWER / ALPHA)
        ee_ev = e_binding_hydrogenic_ev(Z)
        ee_ev_bs = e_binding_hydrogenic_ev(Z, ry_ev=RY_EV_BRING_SCHWINGER)
        m_atom = m_nuc + mpf(Z) * ME - ee_ev / (mpf(10) ** 6)
        M_ame, B_ame = ame.get((Z, A)), ame_bind.get((Z, A))
        if M_ame is None or B_ame is None:
            continue
        d_tot = m_atom - M_ame
        d_nuc = B_ame - B_sym
        d_ele_kev = (d_tot - d_nuc) * mpf(1000)
        per_iso[name] = {
            "Z": Z, "N": N,
            "E_e_ev": _n(ee_ev),
            "E_e_bring_schwinger_ev": _n(ee_ev_bs),
            "B_sym_mev": _n(B_sym),
            "B_sym_E0_tower_mev": _n(B_sym_tower),
            "m_atom_mev": _n(m_atom),
            "M_ame_mev": _n(M_ame),
            "delta_total_mev": _n(d_tot),
            "delta_nuclear_mev": _n(d_nuc),
            "delta_electron_kev": _n(d_ele_kev),
        }
        print(f"| {name} | {A} | {_n(ee_ev, 7):>8s} | {_n(m_atom, 9):>10s} | "
              f"{_n(M_ame, 9):>10s} | {_n(d_tot, 6):>8s} | {_n(d_nuc, 6):>8s} | "
              f"{_n(d_ele_kev, 6):>8s} |")

    # ── Witness ──────────────────────────────────────────────────────────
    from qou_substrate.witness import WitnessBuilder  # noqa: E402

    ry_codata = mpf("13.605693122990")  # CODATA-2022 Rydberg, eV (comparison)
    ry_rel = abs(RY_EV - ry_codata) / ry_codata           # CS route (canonical)
    ry_bs_rel = abs(RY_EV_BRING_SCHWINGER - ry_codata) / ry_codata
    ry_bare = E_H_EV_BARE / mpf(2)
    ry_bare_rel = abs(ry_bare - ry_codata) / ry_codata    # bare route
    h = per_iso["1H"]
    h_ele_kev = abs(mpf(h["delta_electron_kev"]))

    wb = WitnessBuilder("atom-electron-mass", engine="mpmath", output_dir=HERE)
    wb.set_description(
        "Level-6 atomic electron layer at the canonical e-Hartree scale "
        "(bare derived alpha_EM^-1 = q0*[9]_q*[10]_q, CS-resummed alpha_EM^-1, "
        "and Form-B Bring-Schwinger cubic alpha_EM^-1, mp end-to-end): "
        "m_atom = m_sym(nucleus) + Z*m_e - E_e(Z), vs AME2020 neutral-atom "
        "masses, 1H..7Li. G4 promotion of the previously unwitnessed "
        "diagnostic (docs/audits/2026-08-29-mass-provenance-breakdown-and-"
        "gap-map.md). The /dashboard-low atomic table still uses the AME "
        "empirical B_el fit; this witness is the derived-side comparator, "
        "not a production rewire."
    )
    wb.add_parameter("q0", _n(Q0))
    wb.add_parameter("q0Anchor", "proton")
    wb.add_parameter("alpha_E0_mev", _n(ALPHA))
    wb.add_parameter("alpha_E0_tower_mev", _n(E0_TOWER))
    wb.add_parameter("alpha_em_inv_bare", _n(ALPHA_EM_INV_BARE))
    wb.add_parameter("alpha_em_inv_cs_mp", _n(ALPHA_EM_INV_CS))
    wb.add_parameter("alpha_em_inv_bring_schwinger_mp", _n(ALPHA_EM_INV_BRING_SCHWINGER))
    wb.add_parameter("E_hartree_ev_cs_mp", _n(E_H_EV))
    wb.add_parameter("rydberg_ev_cs_mp", _n(RY_EV))
    wb.add_parameter("E_hartree_ev_bring_schwinger_mp", _n(E_H_EV_BRING_SCHWINGER))
    wb.add_parameter("rydberg_ev_bring_schwinger_mp", _n(RY_EV_BRING_SCHWINGER))
    wb.add_parameter("E_hartree_ev_bare", _n(E_H_EV_BARE))
    wb.add_data("per_isotope", per_iso)
    wb.add_data("rydberg_codata_2022_ev", _n(ry_codata))
    wb.add_data("rydberg_cs_mp_vs_codata_rel", _n(ry_rel))
    wb.add_data("rydberg_bring_schwinger_mp_vs_codata_rel", _n(ry_bs_rel))
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
        source="CS-corrected mp route (meson_em_sinh_closed_form.alpha_em_inv_derived + CODATA m_e; float64 excised, bean qou-ozvb) vs CODATA-2022 Ry; the ~9.4e-7 residual is the structural alpha_EM gap (-468 ppb, doubled)",
    )
    wb.add_assertion(
        "rydberg_bare_vs_codata_rel",
        _n(ry_bare_rel),
        "0",
        tolerance="5e-3",
        source="bare-alpha route (q0*[9]_q*[10]_q) vs CODATA-2022 Ry; the ~3.1e-3 gap IS the CS-tower correction the bare route omits",
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
        "masses (CLASS-A acknowledged anchor). The CS-corrected alpha_EM tower "
        "and E_Hartree are mp end-to-end via alpha_em_inv_derived(q0)."
    )
    out = wb.save()
    print(f"\n  witness: {out}")
    print(f"  Ry(CS,mp) vs CODATA rel: {_n(ry_rel, 6)}   "
          f"Ry(Bring-Schwinger) vs CODATA rel: {_n(ry_bs_rel, 6)}   "
          f"1H delta_electron: {_n(h_ele_kev, 6)} keV")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
