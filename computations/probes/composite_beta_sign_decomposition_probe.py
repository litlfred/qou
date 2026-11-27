#!/usr/bin/env python3
"""
composite_beta_sign_decomposition_probe.py -- accuracy epic qou-myts, vector 8
("the Q_beta ladder sign"; beans qou-wxhi / qou-cds1 were named as the home).

QUESTION
--------
The accuracy scorecard (scripts/generate-accuracy-scorecard.py, Table 3.4b)
reports 0 / 1,009 composite beta-minus rows exothermic. Where does the sign come
from?

ANSWER (measured here, exactly)
------------------------------
1. It is NOT the c_k ladder. Table 3.4b is a mass-table subtraction
       Q_pred(Z,N) = M(Z,N) - M(Z+1,N-1) - m_e
   over computations/mass-table-comprehensive.witness.json; no c_k enters.
2. Every one of the 1,009 composite rows has the SAME Q_pred, -1.793042 MeV
   (equal to the witness's 6-decimal rounding),
   independent of Z and A. So the table carries no nuclear information at all;
   it is one number repeated.
3. That number decomposes exactly into four pieces per n -> p swap:
       Q_swap = (m_n - m_p)_pred  -  m_e
                - alpha * ln( V(p-self) / V(n-self) )      [self term]
                - alpha * ln( f_pp / f_nn )                [bond term]
   with alpha = m_e * 8 * Catalan (the Q-CLT proxy scale),
   V(x-self) = product of the nucleon's two intra-generator volumes,
   f_pp = z_D, f_nn = z_D - h (the sigma / sigma^-1 bond letters).
   The probe recomputes all four from q0 in mpmath and checks the sum against
   the witness to its printed 6 decimals.

WHAT EACH PIECE IS
------------------
* self term (+0.556 MeV of binding per swap): the Q-CLT proxy B = -alpha*sum ln|V|
  has no free baseline, so a lone proton "binds" -0.5095 MeV and a lone neutron
  +0.0462 MeV. That is nucleon self-energy counted again inside B, on top of
  m_n - m_p already in the unbound mass. The ruled binding law (owner ruling
  2026-11-25, B = E0 * log(tr_free / tr_atom)) subtracts the free baseline, so
  this piece is a departure from the ruling, not physics.
* bond term (+1.563 MeV per swap): the T_z-odd slope of the bond channel, proved
  structural in QOU.MassTheory.BondChannelTzParity (charge-symmetric iff h = 0)
  and QOU.MassTheory.PairIsospinAssignment (C(f_pp) = -f_nn). The 1-D chain
  p..p n..n has Z-1 pp bonds, one pn bond and N-1 nn bonds, so a swap trades
  one nn bond for one pp bond and pays alpha*ln(f_pp/f_nn) every time.

REPAIRS PRICED (reported, NEVER selected against AME; no fitting)
-----------------------------------------------------------------
  R0  as is                                     Q_swap = -1.793 MeV
  R1  free-baseline subtraction (ruled law)     Q_swap = -1.237 MeV
  R2  R1 + T_z-even bond part (strong channel)  Q_swap = +0.325 MeV
R2 makes every row exothermic but with the same Q for every nucleus: the sign is
fixed, the content is still absent. Z- and A-dependence must come from the
Coulomb, T(T+1) and flavour terms owned by sibling work.

No empirical value enters any assertion except the reproduction check against
the committed witness. Scope (a): a statement about this construction.
"""
from __future__ import annotations

import collections
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
REPO = COMP.parent
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(REPO / "tools" / "pyhecke" / "python"))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import q_at  # noqa: E402
from pyhecke.atom import nucleon_gen_chains  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
except ImportError:  # pragma: no cover
    WitnessBuilder = None

set_compute_dps()

M_E = mp.mpf("0.51099895069")  # same literal the scorecard subtracts


def _chain_volume(chain, q, z):
    """z*a + b after walking (c, d) crossings from the identity, in mpmath."""
    h = q - 1 / q
    a, b = mp.mpf(0), mp.mpf(1)
    for c, d in chain:
        c, d = mp.mpf(c), mp.mpf(d)
        a, b = a * c * h + a * d + b * c, a * c + b * d
    return z * a + b


def nucleon_self_volume(quarks, q, z):
    g0, g1 = nucleon_gen_chains(quarks, q=q)
    return abs(_chain_volume(g0, q, z)) * abs(_chain_volume(g1, q, z))


def witness_rows():
    d = json.loads((COMP / "mass-table-comprehensive.witness.json").read_text())
    return {(r["Z"], r["N"]): r for r in d["data"]["rows"]}


def scorecard_beta_rows(by):
    """Exactly the row filter of generate-accuracy-scorecard.py (Table 3.4b)."""
    ame = json.loads((COMP / "data" / "ame2020.json").read_text())
    ame = ame if isinstance(ame, list) else next(v for v in ame.values() if isinstance(v, list))
    out = []
    for e in ame:
        z, n = int(e["Z"]), int(e["N"])
        if e.get("beta_decay_energy_estimated") or e.get("beta_decay_energy_keV") is None:
            continue
        if mp.mpf(str(e["beta_decay_energy_keV"])) / 1000 <= mp.mpf("0.01"):
            continue
        a, b = by.get((z, n)), by.get((z + 1, n - 1))
        if not a or not b or not a["m_symbolic_MeV"] or not b["m_symbolic_MeV"]:
            continue
        q = mp.mpf(a["m_symbolic_MeV"]) - mp.mpf(b["m_symbolic_MeV"]) - M_E
        out.append(((z, n), q))
    return out


def main() -> int:
    q = q_at(60)
    h = q - 1 / q
    z = q ** 3 / (q ** 2 + 1)
    alpha = M_E * 8 * mp.catalan

    by = witness_rows()
    dm_np = mp.mpf(by[(0, 1)]["m_symbolic_MeV"]) - mp.mpf(by[(1, 0)]["m_symbolic_MeV"])

    v_p = nucleon_self_volume(["u", "u", "d"], q, z)
    v_n = nucleon_self_volume(["u", "d", "d"], q, z)
    f_pp, f_nn = z, z - h

    self_term = alpha * mp.log(v_p / v_n)
    bond_term = alpha * mp.log(f_pp / f_nn)
    q_swap = dm_np - M_E - self_term - bond_term

    rows = scorecard_beta_rows(by)
    composite = [(zn, v) for zn, v in rows if zn != (0, 1)]
    hist = collections.Counter(mp.nstr(v, 7) for _, v in composite)
    vals = [v for _, v in composite]
    spread = max(vals) - min(vals)  # witness rows are printed to 6 decimals
    q_witness = composite[0][1]

    R1 = dm_np - M_E - bond_term
    R2 = dm_np - M_E

    checks = {
        "n_composite_rows": (len(composite), 1009),
        "all_composite_rows_equal_to_witness_rounding": (spread <= mp.mpf("2e-6"), True),
        "none_exothermic": (sum(1 for _, v in composite if v > 0), 0),
        "decomposition_reproduces_witness_to_1e-6": (abs(q_swap - q_witness) < mp.mpf("1e-6"), True),
        "self_term_positive": (self_term > 0, True),
        "bond_term_positive": (bond_term > 0, True),
        "R1_still_endothermic": (R1 < 0, True),
        "R2_exothermic": (R2 > 0, True),
    }
    ok = all(a == b for a, b in checks.values())

    print(f"composite rows: {len(composite)}, distinct Q values: {dict(hist)}")
    print(f"  (m_n - m_p)_pred = {mp.nstr(dm_np, 10)} MeV")
    print(f"  - m_e            = {mp.nstr(-M_E, 10)} MeV")
    print(f"  - self term      = {mp.nstr(-self_term, 10)} MeV  (no free baseline)")
    print(f"  - bond term      = {mp.nstr(-bond_term, 10)} MeV  (alpha ln f_pp/f_nn, T_z-odd)")
    print(f"  = Q_swap         = {mp.nstr(q_swap, 10)} MeV   witness {mp.nstr(q_witness, 10)}")
    print(f"R1 (ruled free baseline)        Q_swap = {mp.nstr(R1, 8)} MeV")
    print(f"R2 (R1 + T_z-even bond)         Q_swap = {mp.nstr(R2, 8)} MeV")
    for k, (a, b) in checks.items():
        print(f"  [{'PASS' if a == b else 'FAIL'}] {k}: {a}")

    if WitnessBuilder is not None:
        wb = WitnessBuilder("composite-beta-sign-decomposition", engine="mpmath")
        wb.set_description(
            "Table 3.4b composite beta-minus sign: every composite row has the same "
            "Q_pred; exact decomposition into nucleon split, m_e, a self term from the "
            "missing free baseline, and the T_z-odd bond term. Repairs priced, not selected."
        )
        for k, (a, b) in checks.items():
            wb.add_assertion(k, computed=str(a), expected=str(b), tolerance="0")
        for dk, dv in {
            "q_swap_MeV": mp.nstr(q_swap, 15),
            "q_witness_MeV": mp.nstr(q_witness, 15),
            "dm_np_pred_MeV": mp.nstr(dm_np, 15),
            "self_term_MeV": mp.nstr(self_term, 15),
            "bond_term_MeV": mp.nstr(bond_term, 15),
            "alpha_MeV": mp.nstr(alpha, 15),
            "f_pp": mp.nstr(f_pp, 15), "f_nn": mp.nstr(f_nn, 15),
            "V_p_self": mp.nstr(v_p, 15), "V_n_self": mp.nstr(v_n, 15),
            "repair_R1_free_baseline_q_swap_MeV": mp.nstr(R1, 15),
            "repair_R2_free_baseline_plus_Tz_even_bond_q_swap_MeV": mp.nstr(R2, 15),
            "n_composite_rows": len(composite),
            "q_spread_across_rows_MeV": mp.nstr(spread, 6),
        }.items():
            wb.add_data(dk, dv)
        wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
