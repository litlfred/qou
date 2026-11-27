#!/usr/bin/env python3
"""
ring_mass_alpha_beta_probe.py -- accuracy epic qou-myts.
Owner, 2026-11-27: "Is there ring binding. And. Alpha/beta decay?"

PRE-REGISTRATION (written before the first run; nothing below is tuned)
-----------------------------------------------------------------------
Masses are the mass table's ruled law, recomputed from its own functions so that
nuclei the table omits (4He, 3He, ...) are covered:
  M(Z,N) = Z m_p + N m_n - B_ruled(Z,N) + E_EM(Z,A) + kappa*T(T+1),
  B_ruled = binding_ruled_tz_even (PR #9675), E_EM = em_energy_mev at the
  CAL-3 conditional radius (PR #9691), twist kappa = 2 alpha ln q, T = |N-Z|/2
  (PR #9685 / #9706). m_p, m_n are the table's own nucleon rows. The recomputation
  is checked against every table row that has m_ruled_em_MeV (to 1e-6 MeV per nucleon, the
  witness rounding) before anything is scored.

Two arms for the nucleon split Delta = m_n - m_p. Both are reported; neither is
selected against data.
  TABLE: Delta as carried by the mass table, (m_n - m_p)_pred = 0.836433 MeV.
  RING:  Delta read on the ring mass of def:mass-identity (PR #9789):
         U = -q d/dq log m, eps_n = q^-2 eps_p, so U_n - U_p = 2 (np_cell_U),
         and in electron units Delta = (2/U_e) m_e with U_e = 3 - D[4]/[4].
The RING arm moves every beta Q by (Delta_ring - Delta_table). It cancels in
every alpha Q, since parent - daughter - 4He has no net n<->p change.

Ring binding. On the ring mass, U is additive over split components, so the
binding of a bound braid class against its split constituents is
E0 * log(m_free / m_bound). That is the ruled log law, so "ring binding" is the
law the table already uses; this probe adds no new binding term.

SCORE B (beta, two-sided): sign(Q_model) == sign(Q_exp), every measured AME
  beta-minus Q with |Q| > 10 keV, A > 1.
SCORE A (alpha): Q_alpha = M(Z,N) - M(Z-2,N-2) - M(2,2); Q_exp from AME mass
  excesses (measured ones only). Sign agreement over |Q_exp| > 10 keV, and on
  the alpha-unstable side (Q_exp > 0) alone.
FREE NEUTRON (RING arm): Q = Delta_ring - m_e.

AME is used only for scores. Scope (a): a statement about this construction.

RESULT (first run, main 462f5cc2a, recorded after the fact)
----------------------------------------------------------
  Delta_np: TABLE 0.836433, RING 0.411328 MeV (U_e = 2.484628).
  Free neutron, RING arm: Q = -0.0997 MeV, so the ring split alone makes the
    free neutron stable. The split is below m_e: 2/U_e = 0.805 < 1.
  Beta, two-sided: TABLE 1508/2245, RING 1507/2245. The arms differ by one row
    in total but move 21 rows between the two sides.
  Alpha: 1129/2373. The model calls 2360 of 2373 alpha-unstable. That makes the
    unstable side 1117/1118 trivially and the stable side 12/1255. The twist
    cancels in Q_alpha, since N-Z is unchanged. What is left is E_EM(parent) -
    E_EM(daughter) against a 4He that is bound 4.2x too weakly: ruled + EM gives
    6.74 MeV against AME 28.30. The per-bond log law has no saturation term that
    would make 4He special. This is a scope-(a) negative.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
from _precision import set_compute_dps  # noqa: E402
from q_parameter import q_at  # noqa: E402
from mass_table_comprehensive import binding_ruled_tz_even  # noqa: E402
from coulomb_isospin_channel import em_energy_mev, r_rms_cal3_conditional  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
except ImportError:  # pragma: no cover
    WitnessBuilder = None

set_compute_dps()
M_E = mp.mpf("0.51099895069")
THRESH = mp.mpf("0.010")
def main() -> int:
    q = q_at(60)
    alpha = M_E * 8 * mp.catalan
    kappa = 2 * alpha * mp.log(q)
    i4 = q**3 + q + 1 / q + q**-3
    di4 = 3 * q**3 + q - 1 / q - 3 * q**-3
    U_e = 3 - di4 / i4
    d_ring = 2 / U_e * M_E

    rows = json.loads((COMP / "mass-table-comprehensive.witness.json").read_text())["data"]["rows"]
    by = {(r["Z"], r["N"]): r for r in rows}
    d_table = mp.mpf(by[(0, 1)]["m_symbolic_MeV"]) - mp.mpf(by[(1, 0)]["m_symbolic_MeV"])
    m_p = mp.mpf(by[(1, 0)]["m_symbolic_MeV"])
    m_n = mp.mpf(by[(0, 1)]["m_symbolic_MeV"])
    twist_in_table = any("B_twist_MeV" in r for r in rows)

    def tt(z, n):
        t = mp.mpf(abs(n - z)) / 2
        return t * (t + 1)

    cache = {}

    def M(z, n, twist=True):
        key = (z, n, twist)
        if key in cache:
            return cache[key]
        a = z + n
        rb = binding_ruled_tz_even(z, n, q)
        if rb is None:
            return None
        e = em_energy_mev(z, a, r_rms_cal3_conditional(a)) if z >= 2 else mp.mpf(0)
        m = z * m_p + n * m_n - rb["B_pred_MeV"] + e + (kappa * tt(z, n) if twist else 0)
        cache[key] = m
        return m

    # reproduce the table before scoring (no twist: main's column carries EM only)
    worst = mp.mpf(0)
    n_cmp = 0
    for (z, n), r in by.items():
        if r.get("m_ruled_em_MeV") and z + n >= 2 and not twist_in_table:
            # witness prints 6 decimals; m_p, m_n rounding scales with A
            worst = max(worst, abs(M(z, n, twist=False) - mp.mpf(r["m_ruled_em_MeV"])) / (z + n + 1))
            n_cmp += 1
    reproduced = n_cmp > 0 and worst < mp.mpf("1e-6")
    print(f"table reproduction: {n_cmp} rows, max |dM|/(A+1) = {mp.nstr(worst, 3)} MeV")
    b_he4 = binding_ruled_tz_even(2, 2, q)["B_pred_MeV"] - em_energy_mev(2, 4, r_rms_cal3_conditional(4))
    print(f"4He ruled binding (with EM, no twist since T=0): {mp.nstr(b_he4, 8)} MeV (AME 28.296, comparison only)")
    keys_used = "recomputed ruled law + EM + twist"
    twist_wired = twist_in_table

    ame = json.loads((COMP / "data" / "ame2020.json").read_text())
    ame = ame if isinstance(ame, list) else next(v for v in ame.values() if isinstance(v, list))
    me = {(int(e["Z"]), int(e["N"])): mp.mpf(str(e["mass_excess_keV"])) / 1000
          for e in ame if not e.get("mass_excess_estimated") and e.get("mass_excess_keV") is not None}

    beta = []
    for e in ame:
        if e.get("beta_decay_energy_estimated") or e.get("beta_decay_energy_keV") is None:
            continue
        z, n = int(e["Z"]), int(e["N"])
        if n < 1 or z + n < 2:
            continue
        a, b = M(z, n), M(z + 1, n - 1)
        if a is None or b is None:
            continue
        qe = mp.mpf(str(e["beta_decay_energy_keV"])) / 1000
        if abs(qe) > THRESH:
            beta.append((a - b - M_E, qe))

    m_he = M(2, 2)
    alph = []
    for (z, n), mex in me.items():
        if z < 3 or n < 3 or (z - 2, n - 2) not in me or (2, 2) not in me:
            continue
        a, b = M(z, n), M(z - 2, n - 2)
        if a is None or b is None:
            continue
        qe = mex - me[(z - 2, n - 2)] - me[(2, 2)]
        if abs(qe) > THRESH:
            alph.append((a - b - m_he, qe, z + n))

    def bscore(shift):
        ok = sum(1 for qm, qe in beta if ((qm + shift) > 0) == (qe > 0))
        pos = [p for p in beta if p[1] > 0]
        neg = [p for p in beta if p[1] < 0]
        return (ok, len(beta), sum(1 for qm, _ in pos if qm + shift > 0), len(pos),
                sum(1 for qm, _ in neg if qm + shift < 0), len(neg))

    bt = bscore(mp.mpf(0))
    br = bscore(d_ring - d_table)
    a_ok = sum(1 for qm, qe, _ in alph if (qm > 0) == (qe > 0))
    a_pos = [p for p in alph if p[1] > 0]
    a_pos_ok = sum(1 for qm, _, _ in a_pos if qm > 0)
    a_neg_ok = sum(1 for qm, qe, _ in alph if qe < 0 and qm < 0)
    a_model_pos = sum(1 for qm, _, _ in alph if qm > 0)
    q_n_ring = d_ring - M_E

    print(f"masses: {keys_used}; kappa = {mp.nstr(kappa, 6)} MeV")
    print(f"Delta_np  TABLE {mp.nstr(d_table, 8)} MeV   RING (2/U_e) m_e {mp.nstr(d_ring, 8)} MeV  (U_e = {mp.nstr(U_e, 8)})")
    print(f"free neutron Q, RING arm: {mp.nstr(q_n_ring, 8)} MeV")
    print(f"BETA TABLE {bt[0]}/{bt[1]} (b- {bt[2]}/{bt[3]}, b+/EC {bt[4]}/{bt[5]})")
    print(f"BETA RING  {br[0]}/{br[1]} (b- {br[2]}/{br[3]}, b+/EC {br[4]}/{br[5]})")
    print(f"ALPHA      {a_ok}/{len(alph)} sign agree; alpha-unstable side {a_pos_ok}/{len(a_pos)}, "
          f"stable side {a_neg_ok}/{len(alph) - len(a_pos)}; model calls {a_model_pos} alpha-unstable")
    if a_pos:
        heavy = [p for p in a_pos if p[2] >= 150]
        print(f"  alpha-unstable with A >= 150: {sum(1 for p in heavy if p[0] > 0)}/{len(heavy)}")

    if WitnessBuilder is not None:
        wb = WitnessBuilder("ring-mass-alpha-beta", engine="mpmath")
        wb.set_description("Beta (two arms for Delta_np: table vs ring mass) and alpha decay direction "
                           "from the ruled-law mass table; pre-registered, AME only for scoring.")
        wb.add_assertion("table_reproduced_1e-6_per_nucleon", computed=str(reproduced), expected="True", tolerance="0")
        wb.add_assertion("ring_np_cell_positive", computed=str(d_ring > 0), expected="True", tolerance="0")
        for k, v in {
            "masses": keys_used, "table_rows_compared": n_cmp, "table_max_abs_dM_per_nucleon_MeV": mp.nstr(worst, 6), "B_4He_ruled_em_MeV": mp.nstr(b_he4, 12),
            "kappa_MeV": mp.nstr(kappa, 12), "U_e": mp.nstr(U_e, 15),
            "delta_np_table_MeV": mp.nstr(d_table, 12), "delta_np_ring_MeV": mp.nstr(d_ring, 12),
            "free_neutron_Q_ring_MeV": mp.nstr(q_n_ring, 12),
            "beta_table": f"{bt[0]}/{bt[1]}", "beta_table_minus_side": f"{bt[2]}/{bt[3]}",
            "beta_table_plus_side": f"{bt[4]}/{bt[5]}",
            "beta_ring": f"{br[0]}/{br[1]}", "beta_ring_minus_side": f"{br[2]}/{br[3]}",
            "beta_ring_plus_side": f"{br[4]}/{br[5]}",
            "alpha": f"{a_ok}/{len(alph)}", "alpha_unstable_side": f"{a_pos_ok}/{len(a_pos)}",
            "alpha_stable_side": f"{a_neg_ok}/{len(alph) - len(a_pos)}",
            "alpha_model_unstable_count": a_model_pos,
        }.items():
            wb.add_data(k, v)
        wb.save()
    return 0 if reproduced else 1


if __name__ == "__main__":
    sys.exit(main())
