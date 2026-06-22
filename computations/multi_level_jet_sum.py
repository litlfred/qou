"""

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.
"""

#!/usr/bin/env python3
"""
Multi-level jet sum (STUB + single-level implementation).

Computes the mass tower summed across jet levels:

    𝔪(ρ) = Σ_{n=0}^{N} 𝔪^{(n)}(ρ)

where 𝔪^{(n)} is the per-level quadratic form from
rem:mass-endomorphism-jet-tower:

    𝔪^{(n)} = |Π V̂_i^{(n)}| + Σ Φ_q(|V̂_i^{(n)}|)
            + z² Σ_{i<j} Φ_q(|V̂_i^{(n)} V̂_j^{(n)}|)   (all pairs)

Two modes:

(a) generator-indexed (current): V̂_i^{(n)} is the
    atom_per_generator_volumes output at the braid on 3A strands
    (single level n=0 for now).  This is what tower_binding_full
    computes.

(b) SYT-cell-indexed (stub): V̂_k^{JM,(n)} via Jucys–Murphy
    eigenvalues at jet level n, summed over SYTs
    (rem:mass-tower-syt-cells).  Not yet implemented — requires
    jet-level propagation of V̂.

For now, this module implements the flat single-level sum and
a placeholder multi-level iterator that delegates to a
user-supplied per-level V̂ builder.  The implementation of
actually DIFFERENT V̂ at different jet levels is a separate
refactor (requires jet-lifted Hecke machinery).
"""
import sys
import json
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
import _path_bridge  # noqa: F401, E402 — substrate path bridge (codata_constants)
from codata_constants import M_P_MEV_VALIDATION  # noqa: E402 — full-precision m_p for E_0 anchor
from mass_endomorphism import q0, Phi_q, z_mark
from pyhecke.gram import atom_per_generator_volumes


def mass_per_level(vols, *, include_all_pairs: bool = True):
    """Per-level quadratic mass term.

    vols: list of dicts with key 'full' — V̂_i at this jet level.
    include_all_pairs: True for all (i<j); False for |i−j|=1 only
    (prop's adjacent-only form).
    """
    n = len(vols)
    desc = 1.0
    for v in vols:
        desc *= v["full"]
    desc = abs(desc)
    single = sum(Phi_q(v["full"]) for v in vols)
    cross = 0.0
    if include_all_pairs:
        for i in range(n):
            for j in range(i + 1, n):
                cross += z_mark ** 2 * Phi_q(
                    abs(vols[i]["full"] * vols[j]["full"]))
    else:
        for i in range(n - 1):
            cross += z_mark ** 2 * Phi_q(
                abs(vols[i]["full"] * vols[i + 1]["full"]))
    return desc, single, cross, desc + single + cross


def tower_sum(per_level_vols, *, include_all_pairs: bool = True):
    """Sum over jet levels: Σ_n 𝔪^{(n)}.

    per_level_vols: list (indexed by jet level n) of per-generator
    V̂ lists at that level.  If only one level is given, returns the
    single-level mass.
    """
    total = 0.0
    level_totals = []
    for n, vols in enumerate(per_level_vols):
        _, _, _, m_n = mass_per_level(vols, include_all_pairs=include_all_pairs)
        total += m_n
        level_totals.append({"level": n, "m_n": m_n, "n_gens": len(vols)})
    return total, level_totals


# ── Single-level binding via multi-level interface ──
# Uses tower_binding_full's atom_per_generator_volumes as the ONLY
# level; a genuine multi-level version would require per-level
# V̂-lifting that isn't implemented yet.

def get_ilp_ground(Z, N):
    p = Path(__file__).parent / "confinement-level-walk.witness.json"
    if not p.exists():
        return {"m_pp": 1, "m_pn": 1, "m_nn": 1}
    w = json.loads(p.read_text())
    atoms = w.get("levels", {}).get("3", {}).get("atoms", {})
    for _k, d in atoms.items():
        if d.get("Z") == Z and d.get("N") == N and not d.get("unstable"):
            return d["ground_state"]
    return {"m_pp": 1, "m_pn": 1, "m_nn": 1}


# Proton-tower calibration: m_proton_tower / m_proton_MeV, so that
# E_0_PROTON_TOWER_MEV · m_proton_tower_cat = 938.272 MeV.  Used by
# the H_3-per-generator tower path (tower_binding_full) as its
# per-cat-unit MeV conversion.  Distinct from the β-decay calibration
# E_0_BETA_DECAY_MEV = 0.78233341 MeV used by the canonical Markov-trace
# path — which path applies depends on which tower is being summed.
_M_PROTON_TOWER_CAT = 1178995.5254  # from mass_endomorphism.py witness
E_0_PROTON_TOWER_MEV = float(M_P_MEV_VALIDATION) / _M_PROTON_TOWER_CAT


def binding_flat_all_pairs(Z, N, E_0=E_0_PROTON_TOWER_MEV):
    """Flat single-level binding with all-pairs cross-term.

    Prop-compliant EXCEPT that |i−j|≥2 pairs are INCLUDED (against
    claim 1 of prop:mass-endomorphism-tower, which asserts adjacent
    only).  Matches the jet-brane reformulation
    (rem:mass-endomorphism-jet-tower) at a single jet level.

    ``E_0`` defaults to the proton-tower calibration
    (E_0_PROTON_TOWER_MEV) since this path uses the H_3-per-generator
    V̂ built via atom_per_generator_volumes — same convention as
    tower_binding_full.  The β-decay calibration (0.78233341 MeV) applies
    to the canonical Markov-trace path, not this tower.
    """
    gs = get_ilp_ground(Z, N)
    va = atom_per_generator_volumes(
        Z, N, include_inter=True,
        m_pp=gs["m_pp"], m_pn=gs["m_pn"], m_nn=gs["m_nn"])
    vf = atom_per_generator_volumes(Z, N, include_inter=False)
    total_a, _ = tower_sum([va], include_all_pairs=True)
    total_f, _ = tower_sum([vf], include_all_pairs=True)
    return E_0 * (total_f - total_a)


if __name__ == "__main__":
    ATOMS = [
        ("D",    1, 1,  2.22452),
        ("T",    1, 2,  8.481821),
        ("3He",  2, 1,  7.71804),
        ("4He",  2, 2, 28.295674),
        ("6Li",  3, 3, 32.0),
        ("9Be",  4, 5, 58.1650),
        ("10B",  5, 5, 64.750),
        ("12C",  6, 6, 92.161728),
        ("14N",  7, 7, 104.659),
        ("16O",  8, 8, 127.619),
    ]
    print("=" * 100)
    print("MULTI-LEVEL JET SUM — flat single-level, all-pairs quadratic")
    print(f"q₀ = {q0:.6f}, z² = {z_mark**2:.4f}")
    print("Jet-level multi-level summation is STUBBED — single level only.")
    print("=" * 100)

    results = []
    print(f"  {'Atom':>6} {'A':>3} {'B_AME':>8} {'B_pred':>10} {'|Δm/m|%':>10}")
    print("  " + "-" * 50)
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        B = binding_flat_all_pairs(Z, N)
        dm = abs(B - B_AME) / (A * float(M_P_MEV_VALIDATION)) * 100
        print(f"  {name:>6} {A:>3} {B_AME:>8.3f} {B:>10.3f} {dm:>9.4f}%")
        results.append({
            "atom": name, "Z": Z, "N": N, "A": A,
            "B_AME_MeV": B_AME, "B_pred_MeV": B,
            "delta_m_over_m_pct": dm,
        })

    stable = [r for r in results if r["A"] >= 6]
    if stable:
        errs = [r["delta_m_over_m_pct"] for r in stable]
        print(f"\nStable A≥6 mean |Δm/m|% = {sum(errs)/len(errs):.4f}%")

    witness = {
        "computation": "multi-level-jet-sum",
        "description": (
            "Multi-level jet sum of mass tower — CURRENT IMPL is a "
            "single-level flat sum with all-pairs quadratic term "
            "(matching rem:mass-endomorphism-jet-tower's single-"
            "level form).  A genuine multi-level version requires "
            "jet-lifted V̂ at each level n; per-level lift not yet "
            "implemented.  This module is a stub that documents the "
            "interface and provides the single-level flat sum for "
            "callers migrating from tower_binding_full."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": q0, "z_markov_sq": z_mark**2,
                        "include_all_pairs": True,
                        "multi_level_implemented": False},
        "results": results,
    }
    out = Path(__file__).parent / "multi-level-jet-sum.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
