#!/usr/bin/env python3
"""
Empirical probe: does the adjacent-only restriction in
prop:mass-endomorphism-tower matter?

The prop's formula
   𝔪 = |Π V̂_i| + Σ Φ_q(|V̂_i|) + z² Σ_{|i−j|=1} Φ_q(|V̂_i V̂_j|)
restricts the quadratic term to ADJACENT generator pairs.  The
argument (§prop proof) — "far-commuting σ_iσ_j with |i−j|≥2 give
no independent blow-up centre" — is asserted in the repo but not
proved (audit report).

This probe tests the claim EMPIRICALLY.  Using the existing H_3
per-generator V̂_i (well-behaved, in [0, 1] range), we compute the
tower mass under three cross-term variants:

  adjacent   — z² · Σ_{|i−j|=1}       Φ_q(|V̂_i V̂_j|)   (prop form)
  full       — z² · Σ_{i<j}           Φ_q(|V̂_i V̂_j|)   (all pairs)
  full_z2pow — z^{2|i−j|} · Σ_{i<j}   Φ_q(|V̂_i V̂_j|)   (distance-graded,
                                                         z² per adj step)

For each atom, we report:
  • m_atom, m_free under each cross_mode
  • B_pred = E_0 · (m_free − m_atom)
  • |Δm/m|% vs B_AME

If adjacent-only is correct (claim 1 holds), "full" should give
SIGNIFICANTLY DIFFERENT / WORSE binding than "adjacent".  If the
"no independent centre" claim is wrong, "full" or "full_z2pow"
should give BETTER binding (closer to B_AME).

Uses the existing atom_per_generator_volumes (H_3 per-generator
shortcut).  Separately noted: claim 2 (H_3 shortcut) is
unauthorized by the prop; this probe deliberately uses it to
isolate the effect of cross-mode only.  A follow-up probe would
run the same comparison with proper H_{3A} weights (task 1 fix).
"""
import sys
import json
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from mass_endomorphism import q0, Phi_q, z_mark
from hecke_core import atom_per_generator_volumes, E_0_CALIBRATION_MEV


def mass_from_tower_probe(vols, cross_mode="adjacent"):
    """Tower mass with configurable cross-term mode.

    Matches mass_endomorphism.mass_from_tower for ``adjacent``; adds
    ``full`` (all pairs) and ``full_z2pow`` (distance-graded)
    variants to isolate the effect of the prop's adjacent-only
    restriction.
    """
    n = len(vols)
    desc = 1.0
    for v in vols:
        desc *= v["full"]
    desc = abs(desc)
    single = sum(Phi_q(abs(v["full"])) for v in vols)
    cross = 0.0
    if cross_mode == "adjacent":
        for i in range(n - 1):
            cross += z_mark ** 2 * Phi_q(
                abs(vols[i]["full"] * vols[i + 1]["full"]))
    elif cross_mode == "full":
        for i in range(n):
            for j in range(i + 1, n):
                cross += z_mark ** 2 * Phi_q(
                    abs(vols[i]["full"] * vols[j]["full"]))
    elif cross_mode == "full_z2pow":
        for i in range(n):
            for j in range(i + 1, n):
                cross += (z_mark ** (2 * (j - i))) * Phi_q(
                    abs(vols[i]["full"] * vols[j]["full"]))
    else:
        raise ValueError(cross_mode)
    return desc, single, cross, desc + single + cross


def get_ilp_ground(Z, N):
    """Level-walk ILP ground state from cache (defaults to 1,1,1)."""
    p = Path(__file__).parent / "confinement-level-walk.witness.json"
    if not p.exists():
        return {"m_pp": 1, "m_pn": 1, "m_nn": 1}
    w = json.loads(p.read_text())
    atoms = w.get("levels", {}).get("3", {}).get("atoms", {})
    for _k, d in atoms.items():
        if d.get("Z") == Z and d.get("N") == N and not d.get("unstable"):
            return d["ground_state"]
    return {"m_pp": 1, "m_pn": 1, "m_nn": 1}


def binding_probe(Z, N, cross_mode, *, m_pp=None, m_pn=None, m_nn=None,
                    E_0=None):
    """Compute binding for (Z, N) under given cross_mode.

    Defaults to the level-walk ILP ground state (consistent with
    tower_binding_full.py).
    """
    gs = get_ilp_ground(Z, N)
    mpp = m_pp if m_pp is not None else gs["m_pp"]
    mpn = m_pn if m_pn is not None else gs["m_pn"]
    mnn = m_nn if m_nn is not None else gs["m_nn"]
    vols_atom = atom_per_generator_volumes(
        Z, N, include_inter=True, m_pp=mpp, m_pn=mpn, m_nn=mnn)
    vols_free = atom_per_generator_volumes(Z, N, include_inter=False)
    _, _, _, total_a = mass_from_tower_probe(vols_atom, cross_mode=cross_mode)
    _, _, _, total_f = mass_from_tower_probe(vols_free, cross_mode=cross_mode)
    if E_0 is None:
        from mass_endomorphism import mass_from_tower as _raw
        _, _, _, m_p_tower = _raw(atom_per_generator_volumes(
            1, 0, include_inter=False))
        # Proton tower mass (Z=1, N=0): actually free-proton mass in cat units
        # Fallback to the known constant:
        E_0 = 938.272 / 1178995.5254
    return {
        "Z": Z, "N": N, "A": Z + N,
        "m_pp": mpp, "m_pn": mpn, "m_nn": mnn,
        "cross_mode": cross_mode,
        "m_atom": total_a, "m_free": total_f,
        "B_MeV": E_0 * (total_f - total_a),
        "E_0_MeV_per_cat": E_0,
    }


if __name__ == "__main__":
    ATOMS = [
        ("D",    1, 1,  2.22452),
        ("T",    1, 2,  8.481821),
        ("3He",  2, 1,  7.71804),
        ("4He",  2, 2, 28.295674),
        ("6Li",  3, 3, 32.0),
        ("7Li",  3, 4, 39.244529),
        ("9Be",  4, 5, 58.1650),
        ("10B",  5, 5, 64.750),
        ("12C",  6, 6, 92.161728),
        ("14N",  7, 7, 104.659),
        ("16O",  8, 8, 127.619),
    ]

    print("=" * 116)
    print("PROBE: adjacent vs all-pairs cross-term in prop:mass-endomorphism-tower")
    print(f"q₀ = {q0}")
    print(f"Using H_3 per-generator V̂ (same as tower_binding_full)")
    print("=" * 116)

    all_results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        M_total = A * 938.272
        row = {"atom": name, "Z": Z, "N": N, "A": A, "B_AME": B_AME}
        for mode in ["adjacent", "full", "full_z2pow"]:
            r = binding_probe(Z, N, cross_mode=mode)
            row[f"B_{mode}"] = r["B_MeV"]
            row[f"dm_m_pct_{mode}"] = abs(r["B_MeV"] - B_AME) / M_total * 100
            row[f"m_atom_{mode}"] = r["m_atom"]
            row[f"m_free_{mode}"] = r["m_free"]
        all_results.append(row)

    # Table
    print(f"\n  {'Atom':>6} {'A':>3} {'B_AME':>8} "
          f"{'B_adj':>10} {'B_full':>10} {'B_zpow':>10}  "
          f"{'|Δm/m|%_adj':>11} {'full':>8} {'zpow':>8}")
    print("  " + "-" * 100)
    for r in all_results:
        print(f"  {r['atom']:>6} {r['A']:>3} {r['B_AME']:>8.3f} "
              f"{r['B_adjacent']:>10.3f} {r['B_full']:>10.3f} "
              f"{r['B_full_z2pow']:>10.3f}  "
              f"{r['dm_m_pct_adjacent']:>10.4f}% "
              f"{r['dm_m_pct_full']:>7.4f}% "
              f"{r['dm_m_pct_full_z2pow']:>7.4f}%")

    # Diagnostic: adjacent vs full delta per atom
    print(f"\nDiagnostic: far-commuting cross-term excess (B_full − B_adjacent)")
    print(f"  {'Atom':>6} {'A':>3} {'ΔB (MeV)':>12} {'ΔB / B_AME':>11}")
    for r in all_results:
        dB = r["B_full"] - r["B_adjacent"]
        print(f"  {r['atom']:>6} {r['A']:>3} {dB:>+12.3f} "
              f"{dB/r['B_AME']*100:>+10.2f}%")

    # Summary
    adj_errs = [r["dm_m_pct_adjacent"] for r in all_results]
    full_errs = [r["dm_m_pct_full"] for r in all_results]
    zpow_errs = [r["dm_m_pct_full_z2pow"] for r in all_results]
    print(f"\n  |Δm/m|% summary (heavy-atom bias):")
    print(f"    adjacent:   min={min(adj_errs):.3f}%, "
          f"max={max(adj_errs):.3f}%, mean={sum(adj_errs)/len(adj_errs):.3f}%")
    print(f"    full:       min={min(full_errs):.3f}%, "
          f"max={max(full_errs):.3f}%, mean={sum(full_errs)/len(full_errs):.3f}%")
    print(f"    full_z2pow: min={min(zpow_errs):.3f}%, "
          f"max={max(zpow_errs):.3f}%, mean={sum(zpow_errs)/len(zpow_errs):.3f}%")

    # Interpretation
    print()
    better = sum(1 for r in all_results
                 if r["dm_m_pct_full"] < r["dm_m_pct_adjacent"])
    worse = sum(1 for r in all_results
                if r["dm_m_pct_full"] > r["dm_m_pct_adjacent"])
    print(f"  full gives SMALLER |Δm/m|% on {better}/{len(all_results)} atoms,"
          f" LARGER on {worse}")
    better_zp = sum(1 for r in all_results
                    if r["dm_m_pct_full_z2pow"] < r["dm_m_pct_adjacent"])
    print(f"  full_z2pow gives SMALLER |Δm/m|% on "
          f"{better_zp}/{len(all_results)} atoms")

    # Witness
    witness = {
        "computation": "adjacent-vs-full-probe",
        "description": (
            "Empirical probe of prop:mass-endomorphism-tower claim 1 "
            "(far-commuting σ_iσ_j with |i−j|≥2 give no independent "
            "blow-up centre).  Compares three cross-term modes "
            "(adjacent / full / full_z2pow) on 11 atoms using the "
            "existing atom_per_generator_volumes (H_3 per-generator "
            "V̂).  If claim 1 holds, 'adjacent' should be the best fit "
            "to B_AME; if it fails, 'full' or 'full_z2pow' should be "
            "better, indicating a missing quadratic-far-commuting "
            "term in the prop."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": q0, "E_0_MeV_per_cat": E_0_CALIBRATION_MEV},
        "results": all_results,
        "summary": {
            "adjacent_mean_err": sum(adj_errs)/len(adj_errs),
            "full_mean_err": sum(full_errs)/len(full_errs),
            "full_z2pow_mean_err": sum(zpow_errs)/len(zpow_errs),
            "n_atoms_full_better": better,
            "n_atoms_full_worse": worse,
        },
    }
    out = Path(__file__).parent / "adjacent-vs-full-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
