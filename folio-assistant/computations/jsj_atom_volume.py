#!/usr/bin/env python3
"""
JSJ-decomposed atom volume: properly-linked nucleons via SnapPy.

HYPOTHESIS (from this session's discussion).  The paper's binding scale
α = m_e · 8G uses Vol(Borromean) = 8G.  A nucleon (3 confined quarks)
is modelled as a Borromean-like 3-component hyperbolic link (NOT as a
torus knot / trefoil, which is Seifert-fibered with Vol = 0).

An atom's total link decomposes under JSJ into:
  - A hyperbolic pieces (one per nucleon, Vol = 8G each if Borromean)
  - inter-nucleon coupling pieces (may be torus or hyperbolic)

By Thurston, Vol_hyp(atom) = Σ Vol(hyperbolic JSJ pieces).

CLAIM.  Binding energy = m_e · [Vol_hyp(atom_linked) - Vol_hyp(free)]
where "free" is A disjoint Borromean rings and "atom_linked" adds
inter-nucleon linking that DECREASES hyperbolic volume (binding =
gluing cost in the JSJ sense).

TEST.  Use SnapPy to compute Vol for:
  (a) Single Borromean = 8G  (sanity check vs paper)
  (b) A disjoint Borromean rings = A·8G
  (c) Linked A-nucleon atom (various linking models)
"""
from __future__ import annotations

import sys
import json
import math
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0

CATALAN_G = 0.915965594177219015054603514932
VOL_BORROMEAN = 8.0 * CATALAN_G
M_E_MEV = 0.51099895


def snappy_volume(manifold_name: str) -> dict:
    try:
        import snappy
    except ImportError:
        return {"status": "no_snappy"}
    try:
        M = snappy.Manifold(manifold_name)
        try:
            M.simplify()
        except Exception as e:
            print(
                f"Warning: could not simplify manifold {manifold_name}: {e}",
                file=sys.stderr,
            )
        # SnapPy may return complex from non-hyperbolic edge cases; take real part.
        vol = float(M.volume().real) if hasattr(M.volume(), "real") else float(M.volume())
        sol = str(M.solution_type())
        n_tet = M.num_tetrahedra()
        n_cusps = M.num_cusps()
        return {"status": "ok", "manifold": manifold_name,
                 "volume": vol, "solution_type": sol,
                 "n_tetrahedra": n_tet, "n_cusps": n_cusps}
    except Exception as e:
        return {"status": f"err:{type(e).__name__}",
                 "manifold": manifold_name,
                 "message": str(e)[:200]}


def nucleon_volume_borromean() -> float:
    """Single-nucleon volume = Vol(Borromean rings).

    Borromean rings = L6a4 in Thistlethwaite's link table, =
    6^3_2 in Rolfsen's.  SnapPy's built-in name: 'L6a4'.
    """
    r = snappy_volume("L6a4")
    return r.get("volume", float("nan"))


def atom_free_volume_simple(A: int, V_nucleon: float) -> float:
    """Free baseline: A disjoint copies, Vol = A · V_nucleon.

    SnapPy computes disjoint unions with separate manifolds.  For
    simplicity we just multiply (rigorous: disjoint union's volume
    IS additive).
    """
    return A * V_nucleon


def try_linked_atom_manifolds() -> list[dict]:
    """Try several known multi-component hyperbolic link manifolds
    that could model atoms."""
    candidates = [
        # Single nucleon candidates
        ("L6a4",           "Borromean rings (proton, Vol=8G)"),
        ("4_1",            "Figure-8 knot (simplest hyperbolic)"),
        # Two-nucleon candidates
        ("L6a1",           "Two-component link 6a1"),
        ("L6a2",           "Two-component link 6a2"),
        ("L6a5",           "Two-component link 6a5"),
        ("L8a1",           "Two-component link 8a1"),
        ("L8a12",          "Two-component link 8a12"),
        # Three-component candidates
        ("L6a4",           "Borromean (3-comp) — again"),
        ("L8n3",           "Non-alternating 8-crossing 3-comp"),
        # Higher order
        ("L10n107",        "10-crossing non-alt link"),
        # Named 3-manifolds (cusped)
        ("m003",           "Gieseking manifold"),
        ("m004",           "Figure-8 knot complement"),
        ("s776",           "Magic manifold (3-cusped, Vol=Vol_min)"),
    ]
    results = []
    for name, desc in candidates:
        r = snappy_volume(name)
        r["description"] = desc
        results.append(r)
    return results


if __name__ == "__main__":
    print("=" * 100)
    print("JSJ ATOM VOLUME — SnapPy on hyperbolic link manifolds")
    print("=" * 100)

    # Sanity checks
    print(f"\n  Expected: Vol(Borromean) = 8G = {VOL_BORROMEAN:.6f}")
    vb = nucleon_volume_borromean()
    print(f"  SnapPy   Vol(L6a4)      = {vb:.6f}")
    print(f"  {'Match' if abs(vb - VOL_BORROMEAN) < 1e-3 else 'MISMATCH'}")
    print()
    print(f"  Catalog survey:")
    print(f"  {'name':>10} {'vol':>12} {'cusps':>7} {'tet':>5} desc")
    print("  " + "-" * 80)
    cat = try_linked_atom_manifolds()
    for r in cat:
        if r.get("status") == "ok":
            print(f"  {r.get('manifold', '?'):>10} "
                  f"{r.get('volume', 0):>12.6f} "
                  f"{r.get('n_cusps', 0):>7} "
                  f"{r.get('n_tetrahedra', 0):>5} "
                  f"{r.get('description', '')}")
        else:
            print(f"  {r.get('manifold', '?'):>10} "
                  f"{r.get('status', ''):>12} - - "
                  f"{r.get('description', '')}")

    # A·8G prediction vs AME
    print(f"\n{'=' * 80}")
    print("PREDICTION: B = m_e · A · 8G  (A independent Borromean nucleons)")
    print("=" * 80)
    print(f"  {'atom':>6} {'A':>3} {'B_AME':>10} {'V_free=A·8G':>14} "
          f"{'B_pred=m_e·V':>14} {'err_%':>10}")
    ATOMS = [("D", 2, 2.22452), ("T", 3, 8.4818), ("3He", 3, 7.7180),
              ("4He", 4, 28.2957), ("6Li", 6, 32.0),
              ("12C", 12, 92.16), ("16O", 16, 127.62)]
    rows = []
    for name, A, B_AME in ATOMS:
        V_free = A * VOL_BORROMEAN
        B_pred = M_E_MEV * V_free
        err = (B_pred - B_AME) / B_AME * 100
        print(f"  {name:>6} {A:>3} {B_AME:>10.4f} "
              f"{V_free:>14.4f} {B_pred:>+14.4f} {err:>+9.3f}%")
        rows.append({"atom": name, "A": A, "B_AME": B_AME,
                      "V_free_cat": V_free, "B_pred_MeV": B_pred,
                      "err_pct": err})

    # Interesting: A · 8G · m_e is systematically half of AME for A≥4.
    # Try 2m_e (pair threshold) as the density:
    print(f"\n{'=' * 80}")
    print("ALT 0: B = 2·m_e · A · 8G  (density = pair threshold 2m_e)")
    print("=" * 80)
    print(f"  2m_e = {2*M_E_MEV:.6f} MeV  (γγ pair-production threshold)")
    print(f"  {'atom':>6} {'A':>3} {'B_AME':>10} {'B_pred':>10} {'err_%':>10}")
    pair_threshold_rows = []
    for name, A, B_AME in ATOMS:
        V_free = A * VOL_BORROMEAN
        B_pred = 2 * M_E_MEV * V_free
        err = (B_pred - B_AME) / B_AME * 100
        print(f"  {name:>6} {A:>3} {B_AME:>10.4f} "
              f"{B_pred:>+10.4f} {err:>+9.3f}%")
        pair_threshold_rows.append({
            "atom": name, "A": A, "B_AME": B_AME,
            "B_pred_MeV": B_pred, "err_pct": err,
        })

    # Try alternative: B = m_e · Vol(linked_atom) with a ΔVol penalty
    # using a simple "proton-Borromean + per-pair coupling" model.
    # Placeholder: ΔVol per inter-nucleon coupling ~ -V_coupling.
    # Fit V_coupling from D to set the scale, predict others.
    print(f"\n{'=' * 80}")
    print("ALT: fit ΔVol-per-coupling from D, predict rest")
    print("=" * 80)
    # Under hypothesis B_pred = m_e · n_pairs · coupling_delta,
    # fitting to B(D) = 2.22 MeV with n_pairs(D) = 1 requires
    # coupling_delta = B(D)/m_e.  This is the V-per-coupling
    # directly, not V_free - V_linked (earlier formulation had a
    # sign/scale bug that gave +137% on D).
    V_from_D = ATOMS[0][2] / M_E_MEV    # B(D)/m_e
    coupling_delta = V_from_D            # ΔV_per_coupling
    print(f"  V_free(2) = 2·8G = {2 * VOL_BORROMEAN:.4f}")
    print(f"  V_linked(D) = B(D)/m_e = {V_from_D:.4f}")
    print(f"  ΔV_per_coupling = {coupling_delta:.4f}  (= V_from_D)")
    print()
    print(f"  {'atom':>6} {'A':>3} {'n_pairs':>7} {'V_free':>10} "
          f"{'V_coup':>10} {'V_atom':>10} {'B_pred':>10} {'err_%':>10}")
    alt_rows = []
    for name, A, B_AME in ATOMS:
        n_pairs = A * (A - 1) // 2        # all-pairs
        V_free = A * VOL_BORROMEAN
        V_coup_total = n_pairs * coupling_delta
        V_atom = V_free - V_coup_total
        B_pred_alt = M_E_MEV * V_coup_total
        err = (B_pred_alt - B_AME) / B_AME * 100
        print(f"  {name:>6} {A:>3} {n_pairs:>7} {V_free:>10.4f} "
              f"{V_coup_total:>10.4f} {V_atom:>10.4f} "
              f"{B_pred_alt:>+10.4f} {err:>+9.3f}%")
        alt_rows.append({"atom": name, "A": A, "n_pairs": n_pairs,
                          "V_free_cat": V_free,
                          "V_coupling_total": V_coup_total,
                          "V_atom_cat": V_atom,
                          "B_pred_MeV": B_pred_alt, "err_pct": err})

    # Third: adjacent-pairs-only (A-1 couplings, not all pairs)
    print(f"\n{'=' * 80}")
    print("ALT 2: adjacent-pairs-only couplings (A-1 couplings per atom)")
    print("=" * 80)
    # Re-fit from D
    # B(D) = m_e · 1 · coupling_delta_adj → coupling_delta_adj = B(D)/m_e
    coupling_delta_adj = ATOMS[0][2] / M_E_MEV
    print(f"  ΔV_per_adj_coupling (from D) = {coupling_delta_adj:.4f}")
    print()
    print(f"  {'atom':>6} {'A':>3} {'n_adj':>7} "
          f"{'B_pred':>10} {'err_%':>10}")
    adj_rows = []
    for name, A, B_AME in ATOMS:
        n_adj = max(A - 1, 0)
        B_pred_adj = M_E_MEV * n_adj * coupling_delta_adj
        err = (B_pred_adj - B_AME) / B_AME * 100
        print(f"  {name:>6} {A:>3} {n_adj:>7} "
              f"{B_pred_adj:>+10.4f} {err:>+9.3f}%")
        adj_rows.append({"atom": name, "A": A, "n_adjacent": n_adj,
                          "B_pred_MeV": B_pred_adj, "err_pct": err})

    witness = {
        "computation": "jsj-atom-volume",
        "description": (
            "Test the JSJ / hyperbolic-volume atom model.  Each nucleon "
            "modelled as Borromean rings (Vol=8G, hyperbolic).  Atom = "
            "either A disjoint Borromeans (free baseline) or A linked "
            "Borromeans (atom).  Binding = m_e · ΔVol.  Explores three "
            "counting schemes for the number of couplings: A·8G alone, "
            "all-pairs (C(A,2)), and adjacent-only (A-1)."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "Catalan_G": CATALAN_G,
            "Vol_Borromean_8G": VOL_BORROMEAN,
            "m_e_MeV": M_E_MEV,
            "q0": q0,
            "snappy_Vol_L6a4": vb,
        },
        "catalog": cat,
        "prediction_A_times_8G": rows,
        "prediction_2me_A_times_8G": pair_threshold_rows,
        "alt_all_pairs_from_D": alt_rows,
        "alt_adjacent_only_from_D": adj_rows,
    }
    out = Path(__file__).parent / "jsj-atom-volume.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
