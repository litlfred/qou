#!/usr/bin/env python3
"""
Level 6 — atom→electron mass wiring (diagnostic; exploratory, no fit, no witness).

Extends the nuclear mass dashboard (`m_sym`, `/dashboard-low`) to the NEUTRAL
ATOM by adding the Z electron rest masses (CAL-1) and subtracting the electron
binding energy at the canonical e-Hartree scale, then comparing to AME2020
*atomic* masses.

    m_atom(Z, N) = m_sym_nucleus(Z, N) + Z·m_e − E_e_binding(Z)

What is canonical here
----------------------
  m_sym nucleus    Z·m_p + N·m_n − B_sym,  B_sym = α·ln(tr_free / tr_atom) from
                   the one Jones–Markov transfer trace (identical to
                   /dashboard-low). α = E₀ = m_e / (q₀(q₀−1)).
  Z·m_e            electron rest mass, the CAL-1 anchor (M_E_MEV).
  e-Hartree scale  E_h = α_EM²·m_e c²  (hecke_core.E_HARTREE_EV ≈ 27.211 eV);
                   Rydberg Ry = E_h/2 ≈ 13.606 eV. α_EM is the QOU-derived
                   1/(q[9]_q[10]_q) ≈ 1/137.036. The α² *scaling* is EXACT in R
                   (conj:e-hartree-categorical-derivation, round 20); the 1/n²
                   shell spacing is derived (round 8b); the absolute E_h unit is
                   the CAL-1 m_e c² (owner-declined Subgoal-2).
  capacity         neutral atom = Z electrons; shell filling / noble-gas closure
                   {2,10,18,36,54,86} is the ElectronShell.bindingMultiplicity
                   (SDP active dual support, ElectronShell.lean). For Z ≤ 3 the
                   filling is trivial (1s¹, 1s², 1s²2s¹).

What is NOT derived (flagged, sub-keV → irrelevant to the mass comparison)
-------------------------------------------------------------------------
  inter-electron screening (Z_eff): the hydrogenic shell sum below uses bare Z,
  which over-binds multi-electron atoms (He, Li). Screening is the open
  magnitude piece of the e-Hartree conjecture. It is an eV-scale effect; the
  nuclear B_sym error is MeV-scale, so it never affects the atomic-mass residual.

Honest bottom line: the electron terms (Z·m_e exact; E_e_binding sub-keV) are
correctly book-kept, but the atomic-mass residual is dominated ~entirely by the
nuclear B_sym model error (MeV). Hydrogen (Z=1) is the clean showcase: its
atomic mass is reproduced to the 13.6 eV electron-binding level purely from
canonical constants + the e-Hartree scale.
"""
from __future__ import annotations

import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "substrate"))
sys.path.insert(0, HERE)

from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION,
    M_N_MEV_VALIDATION,
)
from hecke_core import E_HARTREE_EV, alpha_em  # noqa: E402
from q_parameter import Q as _Q  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402

ME = float(M_E_MEV)          # CAL-1
MP = float(M_P_MEV_VALIDATION)
MN = float(M_N_MEV_VALIDATION)
Q0 = float(_Q)
E0 = ME / (Q0 * (Q0 - 1.0))   # α = E₀ (same as the dashboard)
ALPHA = E0
E_H_EV = float(E_HARTREE_EV)  # canonical Hartree, ≈ 27.211 eV
RY_EV = E_H_EV / 2.0          # Rydberg, ≈ 13.606 eV
U_MEV = 931.49410242          # AME atomic mass unit

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
    """(Z, A) → (neutral-atom mass MeV, total nuclear binding MeV) from AME2020."""
    d = json.loads(open(os.path.join(HERE, "data", "ame2020.json")).read())
    entries = d["entries"] if isinstance(d, dict) and "entries" in d else d
    rows = entries.values() if isinstance(entries, dict) else entries
    mass, bind = {}, {}
    for r in rows:
        dx = r.get("mass_excess_keV")
        if dx is not None:
            mass[(r["Z"], r["A"])] = r["A"] * U_MEV + dx / 1000.0
        b = r.get("binding_energy_total_keV")
        if b is not None:
            bind[(r["Z"], r["A"])] = b / 1000.0
    return mass, bind


def shell_fill(Z: int):
    """Aufbau by principal quantum number n (capacity 2n²); returns list of
    (n, electrons_in_shell). Trivial/exact for the low isotopes; the noble-gas
    closures {2,10,18,...} fall out of the cumulative 2n² capacities."""
    fills, n, left = [], 1, Z
    while left > 0:
        cap = 2 * n * n
        k = min(cap, left)
        fills.append((n, k))
        left -= k
        n += 1
    return fills


def e_binding_hydrogenic_ev(Z: int) -> float:
    """QOU shell-structure electron binding (bare Z, no screening) at the
    canonical Rydberg: Σ_e Z²·Ry/n². Exact for Z=1; over-binds for Z≥2
    (screening = open inter-electron piece). eV."""
    return sum(k * (Z * Z) * RY_EV / (n * n) for n, k in shell_fill(Z))


def m_sym_nucleus_mev(Z: int, N: int):
    """Bare nuclear mass via the canonical Jones–Markov trace, identical to the
    dashboard: m_sym = Z·m_p + N·m_n − B_sym, B_sym = α·ln(tr_free/tr_atom)."""
    ta, tf, _, _ = tr_m_atom_zn(Z, N, dps=50)
    ta, tf = float(ta), float(tf)
    B_sym = ALPHA * math.log(tf / ta)
    m_unbound = Z * MP + N * MN
    return m_unbound - B_sym, B_sym, m_unbound


def main() -> int:
    ame, ame_bind = _ame_tables()
    print(f"  LEVEL-6 ATOM→ELECTRON MASS   "
          f"q₀={Q0:.6f}  α=E₀={ALPHA:.4f} MeV  "
          f"1/α_EM={1/float(alpha_em):.4f}  E_Hartree={E_H_EV:.4f} eV  "
          f"Ry={RY_EV:.4f} eV")
    print("  m_atom = m_sym(nucleus) + Z·m_e − E_e_binding   "
          "[E_e_binding at the canonical e-Hartree scale; bare-Z hydrogenic]\n")

    # --- Table A: electron-shell binding (the new Level-6 term) --------------
    print("### Electron binding  E_e (QOU shell structure @ e-Hartree scale, bare-Z)")
    print("| atom | Z | shell fill | E_e (eV) | E_e (MeV) | note |")
    print("|---|--:|:--|--:|--:|:--|")
    for name, Z, N in ISOTOPES:
        fill = "·".join(f"n{n}:{k}" for n, k in shell_fill(Z))
        ee = e_binding_hydrogenic_ev(Z)
        note = "= H ionization (exact)" if Z == 1 else "over-binds (no screening)"
        print(f"| {name} | {Z} | {fill} | {ee:>8.2f} | {ee/1e6:>10.2e} | {note} |")

    # --- Table B: atomic mass vs AME, residual decomposed -------------------
    #   Δ_total = m_atom − M_AME(atom)  splits exactly into
    #     Δ_nuclear  = B_AME − B_sym                 (nuclear binding error, MeV)
    #     Δ_electron = Δ_total − Δ_nuclear           (e-binding + CODATA/AME
    #                                                 convention, sub-keV)
    print("\n### Atomic mass  m_atom vs AME2020 (atomic), residual decomposed")
    print("| atom | A | m_sym(nuc) | +Z·m_e | −E_e | = m_atom | M_AME(atom) | "
          "Δ total (MeV) | Δ nuclear=B_AME−B_sym | Δ electron (keV) |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|")
    for name, Z, N in ISOTOPES:
        A = Z + N
        m_nuc, B_sym, m_unb = m_sym_nucleus_mev(Z, N)
        zme = Z * ME
        ee_mev = e_binding_hydrogenic_ev(Z) / 1e6
        m_atom = m_nuc + zme - ee_mev
        M_ame = ame.get((Z, A))
        B_ame = ame_bind.get((Z, A))
        if M_ame is None or B_ame is None:
            continue
        d_tot = m_atom - M_ame
        d_nuc = B_ame - B_sym                 # = m_nuc − (Z·m_p+N·m_n−B_AME)
        d_ele_kev = (d_tot - d_nuc) * 1e3     # sub-keV remainder
        print(f"| {name} | {A} | {m_nuc:>9.3f} | {zme:>6.3f} | "
              f"{ee_mev*1e3:>6.3f} keV | {m_atom:>9.3f} | {M_ame:>10.3f} | "
              f"{d_tot:>+8.3f} | {d_nuc:>+8.3f} | {d_ele_kev:>+8.3f} |")

    print("\n  Reading: the Z·m_e term (MeV) is exact CAL-1; E_e_binding is the new")
    print("  Level-6 term, sub-keV at the e-Hartree scale (13.6 eV for ¹H, exact).")
    print("  Δ total splits into Δ nuclear (= B_AME−B_sym, MeV — the whole story)")
    print("  and Δ electron (sub-keV: e-binding screening + CODATA/AME convention).")
    print("  ¹H reproduces M_H atomic to the 13.6 eV electron-binding level from")
    print("  canonical constants alone.")
    print("\n  Discipline: exploratory diagnostic — no production rewire, no fit, no")
    print("  witness (mirrors /dashboard-low and #2343). Screening (Z_eff) is the")
    print("  open inter-electron magnitude piece of conj:e-hartree-categorical-")
    print("  derivation; it is eV-scale and never reaches the mass residual.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
