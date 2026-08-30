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
                   /dashboard-low). α = E₀ = m_e / (q₀(q₀−1)).
  Z·m_e            electron rest mass, the CAL-1 anchor (M_E_MEV).
  e-Hartree scale  E_h = α_EM²·m_e c²; Rydberg Ry = E_h/2. α_EM here is the
                   BARE derived value α_EM⁻¹ = q₀·[9]_q·[10]_q, computed at 60
                   dps from Q_50_DIGIT_STR (mpmath end-to-end). The CS-corrected
                   value (ALPHA_EM_INV_DERIVED ≈ 137.03594) exists only at
                   float64 in pyhecke.constants and is recorded as a
                   comparison parameter, never used in the mp arithmetic.
  capacity         neutral atom = Z electrons; hydrogenic shell sum Σ Z²·Ry/n²
                   with aufbau capacity 2n². Exact for Z = 1.

What is NOT derived (flagged)
-----------------------------
  inter-electron screening (Z_eff): bare Z over-binds He/Li (eV-scale, open).
  nuclear side: Z·m_p + N·m_n uses the CODATA validation masses (CLASS-A
  acknowledged anchor, as in hydrogen_step_by_step.py) — the e-layer terms are
  the derived content of this witness, the nuclear side is context.

Precision: mpmath end-to-end at COMPUTE dps 60; float() appears only in
display f-strings. AME comparison targets enter as mpf(str(·)) of the
published keV values (MEASURED inputs).
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "substrate"))
sys.path.insert(0, HERE)

from mpmath import mp, mpf  # noqa: E402

mp.dps = 60

from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION,
    M_N_MEV_VALIDATION,
    U_MEV as _U_MEV_REGISTRY,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402

# CS-corrected α_EM (float64-only in pyhecke.constants; comparison parameter)
from hecke_core import E_HARTREE_EV as _E_H_EV_F64  # noqa: E402
from pyhecke.constants import ALPHA_EM_INV_DERIVED as _ALPHA_INV_CS_F64  # noqa: E402

ME = +M_E_MEV                      # CAL-1 (already mpf in the registry)
MP_MEV = +M_P_MEV_VALIDATION       # CLASS-A validation anchor
MN_MEV = +M_N_MEV_VALIDATION       # CLASS-A validation anchor
Q0 = mpf(Q_50_DIGIT_STR)           # proton pin (q_parameter resolves anchor)
E0 = ME / (Q0 * (Q0 - 1))          # α = E₀, mp
ALPHA = E0
U_MEV = +_U_MEV_REGISTRY if not isinstance(_U_MEV_REGISTRY, float) else mpf(str(_U_MEV_REGISTRY))


def q_int(n: int):
    """[n]_q = (q^n − q^−n)/(q − q^−1) at q₀, mp."""
    return (Q0 ** n - Q0 ** (-n)) / (Q0 - 1 / Q0)


ALPHA_EM_INV_BARE = Q0 * q_int(9) * q_int(10)      # bare derived α_EM⁻¹, mp
ALPHA_EM_BARE = 1 / ALPHA_EM_INV_BARE
ME_EV = ME * mpf(10) ** 6                           # m_e c² in eV, exact CAL-1
E_H_EV = ALPHA_EM_BARE ** 2 * ME_EV                 # Hartree (bare α), eV, mp
RY_EV = E_H_EV / 2                                  # Rydberg, eV, mp

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
    d = json.loads(open(os.path.join(HERE, "data", "ame2020.json")).read())
    entries = d["entries"] if isinstance(d, dict) and "entries" in d else d
    rows = entries.values() if isinstance(entries, dict) else entries
    mass, bind = {}, {}
    for r in rows:
        dx = r.get("mass_excess_keV")
        if dx is not None:
            mass[(r["Z"], r["A"])] = r["A"] * U_MEV + mpf(str(dx)) / 1000
        b = r.get("binding_energy_total_keV")
        if b is not None:
            bind[(r["Z"], r["A"])] = mpf(str(b)) / 1000
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
    return sum(k * (Z * Z) * RY_EV / (n * n) for n, k in shell_fill(Z))


def m_sym_nucleus_mev(Z: int, N: int):
    """Bare nuclear mass via the canonical Jones–Markov trace (dashboard form):
    m_sym = Z·m_p + N·m_n − B_sym, B_sym = α·ln(tr_free/tr_atom). mp."""
    ta, tf, _, _ = tr_m_atom_zn(Z, N, dps=50)
    ta, tf = mpf(ta) if not hasattr(ta, "_mpf_") else ta, mpf(tf) if not hasattr(tf, "_mpf_") else tf
    B_sym = ALPHA * mp.log(tf / ta)
    m_unbound = Z * MP_MEV + N * MN_MEV
    return m_unbound - B_sym, B_sym, m_unbound


def _n(x, d=50):
    return mp.nstr(x, d)


def main() -> int:
    ame, ame_bind = _ame_tables()
    print(f"  LEVEL-6 ATOMIC ELECTRON LAYER   q0={_n(Q0, 17)}  alpha=E0={_n(ALPHA, 6)} MeV")
    print(f"  bare 1/alpha_EM = q0*[9]_q*[10]_q = {_n(ALPHA_EM_INV_BARE, 12)}   "
          f"(CS-corrected f64 comparison: {_ALPHA_INV_CS_F64:.10f})")
    print(f"  E_Hartree(bare) = {_n(E_H_EV, 10)} eV   Ry = {_n(RY_EV, 10)} eV   "
          f"(pyhecke f64 E_h: {_E_H_EV_F64:.6f} eV)")
    print("  m_atom = m_sym(nucleus) + Z*m_e - E_e_binding   [bare-Z hydrogenic]\n")

    per_iso = {}
    print("| atom | A | E_e (eV) | m_atom (MeV) | M_AME (MeV) | dTot (MeV) | dNuc (MeV) | dEle (keV) |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|")
    for name, Z, N in ISOTOPES:
        A = Z + N
        m_nuc, B_sym, _ = m_sym_nucleus_mev(Z, N)
        ee_ev = e_binding_hydrogenic_ev(Z)
        m_atom = m_nuc + Z * ME - ee_ev / mpf(10) ** 6
        M_ame, B_ame = ame.get((Z, A)), ame_bind.get((Z, A))
        if M_ame is None or B_ame is None:
            continue
        d_tot = m_atom - M_ame
        d_nuc = B_ame - B_sym
        d_ele_kev = (d_tot - d_nuc) * 1000
        per_iso[name] = {
            "Z": Z, "N": N,
            "E_e_ev": _n(ee_ev),
            "B_sym_mev": _n(B_sym),
            "m_atom_mev": _n(m_atom),
            "M_ame_mev": _n(M_ame),
            "delta_total_mev": _n(d_tot),
            "delta_nuclear_mev": _n(d_nuc),
            "delta_electron_kev": _n(d_ele_kev),
        }
        print(f"| {name} | {A} | {float(ee_ev):>8.3f} | {float(m_atom):>10.3f} | "
              f"{float(M_ame):>10.3f} | {float(d_tot):>+8.3f} | {float(d_nuc):>+8.3f} | "
              f"{float(d_ele_kev):>+8.3f} |")

    # ── Witness ──────────────────────────────────────────────────────────
    from qou_substrate.witness import WitnessBuilder  # noqa: E402

    ry_codata = mpf("13.605693122990")  # CODATA-2022 Rydberg, eV (comparison)
    ry_rel = abs(RY_EV - ry_codata) / ry_codata
    ry_cs_f64 = mpf(repr(_E_H_EV_F64)) / 2  # CS-corrected route (f64-limited)
    ry_cs_rel = abs(ry_cs_f64 - ry_codata) / ry_codata
    h = per_iso["1H"]
    h_ele_kev = abs(mpf(h["delta_electron_kev"]))

    wb = WitnessBuilder("atom-electron-mass", engine="mpmath", output_dir=HERE)
    wb.set_description(
        "Level-6 atomic electron layer at the canonical e-Hartree scale "
        "(bare derived alpha_EM^-1 = q0*[9]_q*[10]_q, mp end-to-end): "
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
    wb.add_parameter("alpha_em_inv_bare", _n(ALPHA_EM_INV_BARE))
    wb.add_parameter("alpha_em_inv_cs_f64_comparison", repr(_ALPHA_INV_CS_F64))
    wb.add_parameter("E_hartree_ev_bare", _n(E_H_EV))
    wb.add_parameter("rydberg_ev_bare", _n(RY_EV))
    wb.add_data("per_isotope", per_iso)
    wb.add_data("rydberg_codata_2022_ev", _n(ry_codata))
    wb.add_data("rydberg_bare_vs_codata_rel", _n(ry_rel))
    wb.add_data("rydberg_cs_f64_ev", _n(ry_cs_f64))
    wb.add_data("rydberg_cs_f64_vs_codata_rel", _n(ry_cs_rel))
    wb.add_assertion(
        "h_shell_binding_equals_rydberg",
        _n(e_binding_hydrogenic_ev(1)),
        _n(RY_EV),
        tolerance="0",
        unit="eV",
        source="structural: Z=1, single 1s electron, bare-Z hydrogenic sum = Ry exactly",
    )
    wb.add_assertion(
        "rydberg_bare_vs_codata_rel",
        _n(ry_rel),
        "0",
        tolerance="5e-3",
        source="bare-alpha route (q0*[9]_q*[10]_q, mp-exact) vs CODATA-2022 Ry; the ~3.1e-3 gap IS the CS-tower correction the bare route omits",
    )
    wb.add_assertion(
        "rydberg_cs_f64_vs_codata_rel",
        _n(ry_cs_rel),
        "0",
        tolerance="1e-5",
        source="CS-corrected route (pyhecke ALPHA_EM_INV_DERIVED, float64-limited, rounded 511000.0 eV m_e) vs CODATA-2022 Ry",
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
        "exists only at float64 in pyhecke.constants (and its E_HARTREE_EV uses "
        "a rounded 511000.0 eV electron mass) — recorded as comparison only."
    )
    out = wb.save()
    print(f"\n  witness: {out}")
    print(f"  Ry(bare) vs CODATA rel: {_n(ry_rel, 6)}   "
          f"1H delta_electron: {_n(h_ele_kev, 6)} keV")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
