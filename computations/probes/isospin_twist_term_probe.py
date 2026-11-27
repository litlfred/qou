#!/usr/bin/env python3
"""
isospin_twist_term_probe.py -- accuracy epic qou-myts, ledger gap G2 (bean qou-tcl2).

WHAT IS DERIVED (Lean, QOU/Nuclear/IsospinCasimirTwist.lean, PR #9685)
--------------------------------------------------------------------
The Murphy product Phi_n = L_0 ... L_n (the full twist, by the cited identity
Delta^2 = L_1 ... L_n) acts on the two-row block of isospin T at level n by
q^{2c}, with c = T(T+1) + n(n-4)/4.  At fixed n the blocks differ only by
q^{2 T(T+1)}: coefficient 2 in powers of q, at every level.  On the lowest
block T = |T_z| (d = N - Z), 4 T(T+1) = d^2 + 2|d|, and a beta-minus step
(Z, N) -> (Z+1, N-1) changes T(T+1) by d (d >= 2), 0 (d = 1), d - 2 (d <= 0).

WHAT THIS PROBE DOES (diagnostic only; no producer number changes)
-----------------------------------------------------------------
The Q-CLT proxy maps a log-product to energy as B = -alpha * sum ln|V|, with
alpha = m_e * 8 * Catalan (computations/mass_table_comprehensive.py).  A factor
q^{2 T(T+1)} in that product therefore enters B as -/+ kappa * T(T+1), with

    kappa = 2 * alpha * ln q.

The SIGN is not fixed by the Lean result: it depends on whether the nucleus's
word carries Delta^2 or Delta^{-2}, which is the word axis (ledger gap G5).
So the probe reports BOTH signs and never picks one.

For every composite beta-minus row of scorecard Table 3.4b (same row filter as
scripts/generate-accuracy-scorecard.py and the sibling probe
composite_beta_sign_decomposition_probe.py), it reports the twist shift of
Q_beta = M(Z,N) - M(Z+1,N-1) - m_e, which is

    dQ = s * kappa * Delta[T(T+1)],   s = +1 (mass +kappa T(T+1)) or -1,

on the lowest-block hypothesis T = |T_z|.  It adds dQ to the current per-swap
baseline (repairs R0/R1/R2 of the sibling probe, recomputed here from the
committed witness), and counts the sign of the result.  Those counts are a
COMPARISON with AME signs; nothing is selected or tuned on them.

No empirical value enters the Lean statement.  m_e here is the literal the
proxy and the scorecard already use.
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

from _precision import set_compute_dps  # noqa: E402
from q_parameter import q_at  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
except ImportError:  # pragma: no cover
    WitnessBuilder = None

set_compute_dps()

M_E = mp.mpf("0.51099895069")  # the literal the scorecard subtracts


def casimir4(t: int) -> int:
    """4 T(T+1) written in t = 2T (Lean: casimir4)."""
    return t * (t + 2)


def delta_TT1_beta(d: int) -> mp.mpf:
    """Change of T(T+1) on the lowest block for (Z,N) -> (Z+1,N-1), d = N - Z."""
    return mp.mpf(casimir4(abs(d)) - casimir4(abs(d - 2))) / 4


def witness_rows():
    d = json.loads((COMP / "mass-table-comprehensive.witness.json").read_text())
    return {(r["Z"], r["N"]): r for r in d["data"]["rows"]}


def scorecard_beta_rows(by):
    """Row filter of generate-accuracy-scorecard.py, Table 3.4b."""
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
    zD = q ** 3 / (q ** 2 + 1)
    alpha = M_E * 8 * mp.catalan
    kappa = 2 * alpha * mp.log(q)

    by = witness_rows()
    rows = scorecard_beta_rows(by)
    composite = [(zn, v) for zn, v in rows if zn != (0, 1)]
    dm_np = mp.mpf(by[(0, 1)]["m_symbolic_MeV"]) - mp.mpf(by[(1, 0)]["m_symbolic_MeV"])
    bond = alpha * mp.log(zD / (zD - h))
    baselines = {
        "R0_as_is": None,               # the witness value row by row
        "R1_free_baseline": dm_np - M_E - bond,
        "R2_free_baseline_plus_Tz_even_bond": dm_np - M_E,
    }

    d_hist = collections.Counter(n - z for (z, n), _ in composite)
    report = {}
    for name, base in baselines.items():
        for s in (+1, -1):
            exo = 0
            for (z, n), v in composite:
                q0 = v if base is None else base
                if q0 + s * kappa * delta_TT1_beta(n - z) > 0:
                    exo += 1
            report[f"{name}|sign{'+' if s > 0 else '-'}"] = exo
        exo0 = sum(1 for _, v in composite if (v if base is None else base) > 0)
        report[f"{name}|no_twist"] = exo0

    # Lean-side identities, re-checked numerically over the range in use.
    lean_checks = all(
        casimir4(abs(d)) == d * d + 2 * abs(d) for d in range(-60, 61)
    ) and all(
        delta_TT1_beta(d) == (d if d >= 2 else (0 if d == 1 else d - 2)) for d in range(-60, 61)
    )

    checks = {
        "n_composite_rows": (len(composite), 1009),
        "lean_parabola_and_beta_step_identities": (lean_checks, True),
        "kappa_positive": (kappa > 0, True),
        "R0_no_twist_none_exothermic": (report["R0_as_is|no_twist"], 0),
    }
    ok = all(a == b for a, b in checks.values())

    print(f"alpha = {mp.nstr(alpha, 10)} MeV, ln q = {mp.nstr(mp.log(q), 10)}")
    print(f"kappa = 2 alpha ln q = {mp.nstr(kappa, 10)} MeV per unit T(T+1)")
    print(f"composite rows: {len(composite)}; parent d = N - Z range "
          f"{min(d_hist)}..{max(d_hist)}")
    print("exothermic counts (comparison with AME sign, which is + on every row):")
    for k, v in report.items():
        print(f"  {k:48s} {v:5d} / {len(composite)}")
    for k, (a, b) in checks.items():
        print(f"  [{'PASS' if a == b else 'FAIL'}] {k}: {a}")

    if WitnessBuilder is not None:
        wb = WitnessBuilder("isospin-twist-term", engine="mpmath")
        wb.set_description(
            "Gap G2 diagnostic: the derived q^{2T(T+1)} block factor of the full twist "
            "(Lean QOU.Nuclear.IsospinCasimirTwist) pushed through the Q-CLT proxy energy "
            "map, kappa = 2 alpha ln q, both signs, on the lowest block T = |T_z|; effect "
            "on the Table 3.4b composite beta-minus signs. Reported, never selected."
        )
        for k, (a, b) in checks.items():
            wb.add_assertion(k, computed=str(a), expected=str(b), tolerance="0")
        wb.add_data("alpha_MeV", mp.nstr(alpha, 15))
        wb.add_data("kappa_MeV_per_unit_TT1", mp.nstr(kappa, 15))
        wb.add_data("exothermic_counts", report)
        wb.add_data("parent_d_histogram", {str(k): v for k, v in sorted(d_hist.items())})
        wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
