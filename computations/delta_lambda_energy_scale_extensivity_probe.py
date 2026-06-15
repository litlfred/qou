#!/usr/bin/env python3
"""Δ_λ(K) attack — energy-scale vs missing-extensivity decomposition, with the
active set tracked through the nucleon-by-nucleon knot construction.

EXPLORATORY (no production rewire). Owner directive 2026-06-10: "attack the
Δ_λ(K) gate / energy-scale — keep track of active sets through knot operations
as nucleons constructed."

## The decomposition

The canonical binding (`binding_canonical.py`, Jones–Markov trace) is

    B_pred(K) = Q_β · Δtr(K),   Δtr(K) = tr_M(W_free) − tr_M(W_atom)

and the per-isotope residual gate is Δ_λ(K) = B_AME(K) / B_pred(K). This probe
splits Δ_λ into two structurally distinct factors:

    Δ_λ(K) = (E_0 / Q_β) · r(K),      r(K) ≡ Δ_λ(K) · Q_β / E_0

where E_0 = m_e / (q_0 (q_0 − 1)) ≈ 4.186 MeV is the canonical energy scale and
Q_β(n) ≈ 0.782 MeV is the free-neutron β-decay Q-value used as the (wrong)
multiplier in binding_canonical.

### Finding 1 — the deuteron gap IS the energy scale
E_0/Q_β = 5.351 and Δ_λ(D) = 4.78, so r(D) ≈ 0.89 ≈ 1. The 1-bond nucleus is
reproduced (to ~11 %) by the energy-scale swap alone: B_pred should use E_0,
not Q_β. This is NOT a fit — E_0 is the canonical scale already in the
framework (e_0_full_mev); Q_β was a mis-identification (see binding_canonical
docstring + the in-file naming note).

### Finding 2 — the residual r(K) is MISSING EXTENSIVITY
Δtr(K) **saturates** toward 1 as A grows (tr_free → 1 trivial-rep limit,
tr_atom → small) — it is an *intensive* quantity, bounded, so B_pred = Q_β·Δtr
∈ [0.47, 0.71] cannot grow with A. Physical binding B_AME is *extensive*
(∝ number of nucleon–nucleon bonds). Hence the residual r(K) tracks the bond
count C(A,2) = A(A−1)/2 (D:0.89~1, T:2.52~3, ³He:2.19~3, ⁴He:7.41~6) — a rough
~O(1)·bonds near-match, NOT a clean law (³He≠T at equal A shows p/n
composition matters; ⁴He is over-bound — alpha magic). The structural verdict
is robust even though the scalar law is not: **a single global trace
difference is intensive; binding is extensive, so the formula is missing a
per-bond sum.** This is exactly the direction of the operator combiner (#2080)
and the per-nucleus volume route (#2078).

## Active set through the knot construction

As each nucleon adds 3 strands + one bridge crossing (the nested-bridge braid
β = β_0·σ_3·β_1·σ_6·…), the few-row active set [n],[n−1,1],[n−2,2],[n−3,3]
carries 90 % of tr_M at every A (from the LOSSLESS matrix-M caches — the cap
that skipped high-dim λ is now dropped, #2089 commit 054efed7). The probe
reports the active set per A and the trace scale, making visible that the
trace DIFFERENCE does not accumulate one bond's worth per added nucleon — the
active-set contribution to Δtr saturates, which is Finding 2 at the partition
level.

> Convention caveat: the matrix-M caches are the SIGN-ONLY (chi_q_via_gp)
> crossing convention; binding_canonical is the AVERAGED-crossing trace. The
> few-row DOMINANCE structure is shared (both are Markov traces at q_0 ≈ 1.11,
> where small irreps dominate), so the active-set picture is illustrative of
> the saturation; the binding numbers themselves come from binding_canonical
> (convention-correct).

Output: delta-lambda-energy-scale-extensivity.witness.json
"""
from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

from witness_base import WitnessBuilder  # noqa: E402

# Lossless matrix-M caches (sign-only convention) for the active-set view.
CHI_CACHE = {
    (1, 1): "chi-deuteron-h6-at-q0-50dps-matrix-m.witness.json",
    (1, 2): "chi-tritium-h9-at-q0-50dps-matrix-m.witness.json",
    (2, 1): "chi-helium-3-h9-at-q0-50dps-matrix-m.witness.json",
}


def _energy_scales() -> tuple[float, float, float]:
    """(m_e, Q_β, E_0) in MeV, E_0 = m_e/(q_0(q_0−1))."""
    from q_parameter import Q as q0
    from experimental_constants import Q_NEUTRON_MEV as Qb
    from codata_constants import M_E_MEV as me
    me, q0, Qb = float(me), float(q0), float(Qb)
    return me, Qb, me / (q0 * (q0 - 1.0))


def active_set(Z: int, N: int):
    """Top partitions (≥90% of tr_M) + few-row fraction, from the LOSSLESS
    matrix-M cache. Returns None if the cache is absent or still truncated."""
    f = CHI_CACHE.get((Z, N))
    if not f or not (HERE / f).exists():
        return None
    w = json.loads((HERE / f).read_text())
    bp = w.get("by_partition") or w.get("data", {}).get("by_partition")
    if any(e.get("chi_lambda") == "skipped-max-dim" for e in bp):
        return {"status": "TRUNCATED_CACHE — rerun lossless producer"}
    valid = [(str(e["partition"]), abs(float(e["contribution"])),
              int(e.get("dim", 0)), len(e["partition"])) for e in bp]
    tot = sum(c for _, c, _, _ in valid)
    valid.sort(key=lambda x: -x[1])
    cum, top = 0.0, []
    for p, c, d, r in valid:
        cum += c
        top.append({"partition": p, "dim": d, "rows": r,
                    "frac": round(c / tot, 4)})
        if cum >= 0.9 * tot:
            break
    fewrow = sum(c for _, c, _, r in valid if r <= 4) / tot
    return {
        "n_partitions_total": len(bp),
        "n_in_active_90pct": len(top),
        "tr_M_signonly": round(tot, 6),
        "fewrow_frac_rows_le_4": round(fewrow, 5),
        "active_partitions": top,
    }


def main() -> int:
    t0 = time.time()
    me, Qb, E0 = _energy_scales()
    scale = E0 / Qb

    bc = json.loads((HERE / "binding-canonical.witness.json").read_text())
    res = [r for r in bc["data"]["results"] if r.get("status") == "solved"]

    rows = []
    for r in res:
        Z, N, A = r["Z"], r["N"], r["A"]
        ta = float(r["tr_M_atom"].strip("()").split("+")[0])
        tf = float(r["tr_M_free"].strip("()").split("+")[0])
        dtr = tf - ta
        B_ame = float(r["B_AME_MeV"])
        B_pred = float(r["B_MeV"])
        dl = B_ame / B_pred
        rK = dl * Qb / E0            # residual after the energy-scale swap
        bonds = A * (A - 1) // 2     # nucleon–nucleon bond count C(A,2)
        rows.append({
            "atom": r["atom"], "Z": Z, "N": N, "A": A,
            "B_AME_MeV": round(B_ame, 4),
            "B_pred_Qbeta_MeV": round(B_pred, 4),
            "B_pred_E0_MeV": round(E0 * dtr, 4),     # the energy-scale-fixed pred
            "Delta_tr": round(dtr, 5),
            "Delta_lambda": round(dl, 3),
            "r_residual": round(rK, 3),              # Δ_λ · Q_β/E_0
            "bonds_C_A_2": bonds,
            "r_over_bonds": round(rK / bonds, 3),
            "B_AME_per_bond": round(B_ame / bonds, 3),
            "Delta_tr_per_bond": round(dtr / bonds, 4),
            "active_set": active_set(Z, N),
        })

    # Saturation + extensivity fits (log-scale growth vs A).
    As = [r["A"] for r in rows]
    dtrs = [r["Delta_tr"] for r in rows]
    bames = [r["B_AME_MeV"] for r in rows]

    def _loglin(xs, ys):
        # slope of log(y) vs x by least squares (growth rate per nucleon)
        lx = list(xs); ly = [math.log(v) for v in ys]
        n = len(lx); sx = sum(lx); sy = sum(ly)
        sxx = sum(a * a for a in lx); sxy = sum(a * b for a, b in zip(lx, ly))
        return (n * sxy - sx * sy) / (n * sxx - sx * sx)

    growth_dtr = _loglin(As, dtrs)      # ≈ 0 if Δtr saturates (intensive)
    growth_bame = _loglin(As, bames)    # > 0 (extensive)

    w = WitnessBuilder("delta-lambda-energy-scale-extensivity",
                       engine="python", start_time=t0)
    w.set_description(
        "Δ_λ(K) attack: splits the canonical binding residual into "
        "Δ_λ = (E_0/Q_β)·r(K). Finding 1 — the DEUTERON gap is the energy "
        "scale (E_0/Q_β=5.35 ≈ Δ_λ(D)=4.78 → r(D)≈0.89≈1; use E_0 not Q_β). "
        "Finding 2 — the residual r(K) is MISSING EXTENSIVITY: Δtr saturates "
        "(intensive, →1) while B_AME is extensive (∝ bonds C(A,2)); r(K) "
        "tracks the bond count (rough O(1)·bonds, not a clean law). Active "
        "set (few-row, 90% of tr_M) tracked across the nucleon-by-nucleon "
        "knot construction from the LOSSLESS matrix-M caches (#2089 cap fix). "
        "EXPLORATORY — no production rewire; points at the per-bond operator "
        "combiner (#2080) / per-nucleus volume (#2078) as the extensive fix."
    )
    w.add_parameter("m_e_MeV", round(me, 6))
    w.add_parameter("Q_beta_n_MeV", round(Qb, 6))
    w.add_parameter("E_0_MeV", round(E0, 4))
    w.add_parameter("E0_over_Qbeta", round(scale, 4))
    w.add_data("rows", rows)
    w.add_data("findings", {
        "F1_energy_scale": {
            "E0_over_Qbeta": round(scale, 4),
            "Delta_lambda_D": round(rows[0]["Delta_lambda"], 3),
            "r_D": round(rows[0]["r_residual"], 3),
            "verdict": "deuteron (1 bond) ≈ pure energy-scale: use E_0 not Q_β "
                       "(r_D≈0.89≈1, 11% residual).",
        },
        "F2_extensivity": {
            "log_growth_per_A_Delta_tr": round(growth_dtr, 4),
            "log_growth_per_A_B_AME": round(growth_bame, 4),
            "verdict": "Δtr saturates (log-growth≈%.2f/A, intensive→1) while "
                       "B_AME is extensive (log-growth≈%.2f/A). r(K) tracks "
                       "bonds C(A,2). The single global trace difference is "
                       "intensive; binding is extensive → missing per-bond "
                       "sum." % (growth_dtr, growth_bame),
        },
        "next": "Extensive fix = per-bond/per-interface binding (sum over "
                "nucleon pairs), not a global Δtr. Aligns with #2080 operator "
                "combiner + #2078 per-nucleus volume. NOT a Δ_λ scalar law "
                "(³He≠T at A=3; ⁴He over-bound) — structural, not fitted.",
    })
    # Assertion: the energy-scale swap makes the deuteron residual O(1).
    w.add_assertion(
        name="deuteron_residual_is_order_one_after_energy_scale",
        computed=rows[0]["r_residual"], expected=1.0, tolerance=0.2,
        source="r(D) = Δ_λ(D)·Q_β/E_0 ≈ 1 ⇒ the 1-bond deuteron gap is the "
               "energy-scale mismatch (Q_β vs E_0), not the structural Δ_λ.",
    )
    # Assertion: Δtr saturates (near-zero log-growth) — the extensivity gap.
    w.add_assertion(
        name="Delta_tr_is_intensive_saturating",
        computed=abs(growth_dtr), expected=0.0, tolerance=0.30,
        source="log-growth of Δtr per nucleon ≈ 0 (saturates →1) while B_AME "
               "grows — the single trace difference cannot be extensive.",
    )
    out = w.save()

    # Console
    print("=" * 92)
    print(" Δ_λ(K) = (E_0/Q_β)·r(K)   energy-scale + extensivity decomposition")
    print(f"  m_e={me:.4f}  Q_β={Qb:.4f}  E_0={E0:.4f} MeV   E_0/Q_β={scale:.3f}")
    print("=" * 92)
    print(f" {'atom':>6}{'A':>3}{'B_AME':>8}{'Bpred_Qb':>9}{'Bpred_E0':>9}"
          f"{'Δtr':>8}{'Δ_λ':>8}{'r=Δλ·Qb/E0':>11}{'bonds':>6}{'r/bonds':>8}{'active':>8}")
    print(" " + "-" * 90)
    for r in rows:
        a = r["active_set"]
        act = (f"{a['n_in_active_90pct']}/{a['n_partitions_total']}"
               if a and "n_in_active_90pct" in a else "—")
        print(f" {r['atom']:>6}{r['A']:>3}{r['B_AME_MeV']:>8.2f}"
              f"{r['B_pred_Qbeta_MeV']:>9.3f}{r['B_pred_E0_MeV']:>9.3f}"
              f"{r['Delta_tr']:>8.3f}{r['Delta_lambda']:>8.2f}"
              f"{r['r_residual']:>11.2f}{r['bonds_C_A_2']:>6}"
              f"{r['r_over_bonds']:>8.2f}{act:>8}")
    print(" " + "-" * 90)
    print(f" F1 energy scale: r(D)={rows[0]['r_residual']:.2f}≈1 → deuteron gap "
          f"is Q_β-vs-E_0 (use E_0).")
    print(f" F2 extensivity : Δtr log-growth {growth_dtr:+.3f}/A (saturates) vs "
          f"B_AME {growth_bame:+.3f}/A (extensive) → r(K)~bonds C(A,2).")
    for r in rows:
        a = r["active_set"]
        if a and "active_partitions" in a:
            tops = ", ".join(f"{p['partition']}({p['frac']:.2f})"
                             for p in a["active_partitions"][:4])
            print(f"   {r['atom']:>6} A={r['A']} active≥90%: {tops}  "
                  f"fewrow={a['fewrow_frac_rows_le_4']:.3f}")
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
