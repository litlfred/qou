#!/usr/bin/env python3
"""
Jet-lifted Hecke machinery — V̂ propagation across jet levels.

Per rem:mass-endomorphism-jet-tower, the mass tower sums per-level
quadratic contributions:

  𝔪(ρ) = Σ_{n=0}^{N}  𝔪^{(n)}(ρ)

This module implements the per-level V̂ propagation rule and the
resulting tower sum.  The jet tower is

  A_{n+1} = A_n ⊗ Ω^1(A_n)

with new generators at level n+1 arising from Kähler differentials
of A_n.  For the Iwahori–Hecke algebra, the explicit Kähler-
differential computation is not spelled out in the repo;
this module uses two alternative propagation rules as
APPROXIMATIONS to the correct jet lift:

(A) Markov stabilization lift
    V̂_i^{(n+1)} = z · V̂_i^{(n)}  (existing gens scaled by Markov
                                    parameter z)
    V̂_new^{(n+1)} = 1             (new Kähler gens trivial at this
                                    level — they contribute only at
                                    higher levels)
    Rationale: tr_M stabilization — adding a trivial strand multiplies
    the Markov trace by z.

(B) q-Plancherel-descent lift
    V̂_i^{(n+1)} = V̂_i^{(n)} · (fraction that does NOT descend)
    where the descent fraction is computed from q-Plancherel
    box-removal probabilities on Young diagrams.
    Rationale: jet-descent via partition box-removal per
    rem:mass-tower-syt-cells.

Both are STUBS — the true jet lift requires the explicit Kähler-
differential action on H_n(q), which is open (see
prop:jet-stratified-reduction for the abstract framework).

Usage:
    from jet_lifted_hecke import binding_multi_level
    result = binding_multi_level(Z=8, N=8, n_levels=5, lift="markov")
"""
import sys
import math
import json
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from mass_endomorphism import q0, Phi_q, z_mark
from hecke_core import atom_per_generator_volumes
from multi_level_jet_sum import mass_per_level, get_ilp_ground


def lift_markov(vols, level):
    """Markov-stabilization lift of V̂ from level 0 to level `level`.

    V̂_i^{(level)} = z^{level} · V̂_i^{(0)}
    """
    factor = z_mark ** level
    return [{"full": v["full"] * factor} for v in vols]


def lift_qplancherel(vols, level, q=None):
    """q-Plancherel-descent lift (stub).

    Uses an empirical descent-rate estimate: each jet-level-up
    contributes a factor (1 − 1/[n+level]_q) from box-addition
    to the Young diagram, placeholder for the full q-Plancherel
    transition probability.
    """
    if q is None:
        q = q0
    n = len(vols)
    if level == 0:
        return [dict(v) for v in vols]
    # [n+level]_q = (q^{n+level} - q^{-(n+level)}) / (q - q^{-1})
    m = n + level
    qi = 1.0 / q
    bracket = (q ** m - qi ** m) / (q - qi)
    factor = 1.0 - 1.0 / bracket
    factor = max(0.0, min(1.0, factor))
    # Apply factor `level` times (geometric decay)
    total_factor = factor ** level
    return [{"full": v["full"] * total_factor} for v in vols]


def binding_multi_level(Z, N, *, n_levels=5, lift="markov",
                          E_0=938.272 / 1178995.5254):
    """Multi-level jet-tower binding.

    At each jet level 0..n_levels−1:
      1. Lift V̂^{(0)} to V̂^{(n)} via the chosen lift rule.
      2. Compute per-level quadratic mass (all-pairs form).
      3. Accumulate.
    Binding = E_0 · (total_m_free − total_m_atom).
    """
    gs = get_ilp_ground(Z, N)
    va0 = atom_per_generator_volumes(
        Z, N, include_inter=True,
        m_pp=gs["m_pp"], m_pn=gs["m_pn"], m_nn=gs["m_nn"])
    vf0 = atom_per_generator_volumes(Z, N, include_inter=False)
    lift_fn = {"markov": lift_markov,
                "qplancherel": lift_qplancherel}[lift]

    total_a = 0.0
    total_f = 0.0
    per_level = []
    for n in range(n_levels):
        va_n = lift_fn(va0, n)
        vf_n = lift_fn(vf0, n)
        _, _, _, m_a = mass_per_level(va_n, include_all_pairs=True)
        _, _, _, m_f = mass_per_level(vf_n, include_all_pairs=True)
        total_a += m_a
        total_f += m_f
        per_level.append({
            "level": n,
            "m_atom": m_a,
            "m_free": m_f,
            "delta": m_f - m_a,
        })
    return {
        "Z": Z, "N": N, "A": Z + N, "n_levels": n_levels,
        "lift": lift,
        "m_atom_total": total_a,
        "m_free_total": total_f,
        "per_level": per_level,
        "B_MeV": E_0 * (total_f - total_a),
    }


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
    print("JET-LIFTED HECKE: multi-level V̂ propagation")
    print(f"q₀ = {q0:.6f}, z = {z_mark:.4f}")
    print("Lifts: (markov) V̂^(n) = z^n V̂^(0);  (qplancherel) box-")
    print("  addition-attenuated geometric decay.  Both are STUBS —")
    print("  the true Kähler-lift is open.")
    print("=" * 100)

    for lift in ["markov", "qplancherel"]:
        print(f"\n-- Lift: {lift} --")
        print(f"  {'Atom':>6} {'A':>3} {'N_lvl':>6} {'B_AME':>8} "
              f"{'B_pred':>10} {'|Δm/m|%':>10}")
        print("  " + "-" * 60)
        atoms_results = []
        for name, Z, N, B_AME in ATOMS:
            A = Z + N
            for N_lvl in [1, 3, 5, 10]:
                r = binding_multi_level(Z, N, n_levels=N_lvl, lift=lift)
                dm = (abs(r["B_MeV"] - B_AME) / (A * 938.272) * 100
                       if math.isfinite(r["B_MeV"]) else float("nan"))
                if N_lvl in [1, 5]:
                    print(f"  {name:>6} {A:>3} {N_lvl:>6} {B_AME:>8.3f} "
                          f"{r['B_MeV']:>10.3f} {dm:>9.4f}%")
                atoms_results.append({**r, "atom": name, "B_AME": B_AME,
                                       "delta_m_over_m_pct": dm})

        # Summary for stable atoms at N_lvl=5
        stable = [r for r in atoms_results
                   if r["A"] >= 6 and r["n_levels"] == 5
                   and math.isfinite(r["delta_m_over_m_pct"])]
        if stable:
            mean_err = sum(r["delta_m_over_m_pct"] for r in stable) / len(stable)
            print(f"  Stable A≥6, N=5: mean |Δm/m|% = {mean_err:.4f}%")

    # Witness
    all_results = []
    for lift in ["markov", "qplancherel"]:
        for name, Z, N, B_AME in ATOMS:
            for N_lvl in [1, 5]:
                r = binding_multi_level(Z, N, n_levels=N_lvl, lift=lift)
                r["atom"] = name
                r["B_AME"] = B_AME
                all_results.append(r)

    witness = {
        "computation": "jet-lifted-hecke",
        "description": (
            "Multi-level jet-tower binding with V̂ propagation at each "
            "jet level via one of two stub lifts: (a) Markov-"
            "stabilization V̂^(n) = z^n V̂^(0); (b) q-Plancherel-"
            "descent geometric decay.  Both converge to the single-"
            "level all-pairs result at N=1 (level 0 only), and "
            "extrapolate to the geometric sum at higher N.  True "
            "jet-lifted Kähler-differential propagation is not "
            "implemented — requires the explicit Ω^1(H_n(q)) action "
            "which is open in the repo."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": q0, "z_markov": z_mark,
                        "E_0_MeV_per_cat": 938.272 / 1178995.5254,
                        "lifts": ["markov", "qplancherel"]},
        "results": all_results,
    }
    out = Path(__file__).parent / "jet-lifted-hecke.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
