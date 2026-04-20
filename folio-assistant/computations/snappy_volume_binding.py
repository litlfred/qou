#!/usr/bin/env python3
"""
SnapPy-volume binding probe — Kashaev-axiomatised mass formula.

ASSUMES: 𝔪(K) = Vol(K) / ℏ_q²  (Physical-Observations axiom).
COMPUTES: Vol(K) directly via SnapPy for atom and free braid closures.
COMPARES: B(D) = [Vol(free) − Vol(atom)] / ℏ_q²  against AME 2.2246 MeV.

The Hecke-factor encoding of the atom braid includes superposed
factors (e.g. ud pair = ½(σ + σ⁻¹) · I) that are NOT pure braids.
For the pure-topology Vol(K), we use a committed pure-braid
representative:

  PROTON  (uud)  — σ₀σ₁σ₀   (3 strands, trefoil Δ₃)
  NEUTRON (udd)  — σ₀⁻¹σ₁σ₀⁻¹  (3 strands, mirror-trefoil-adjacent)
  ATOM (Z, N)    — stacked nucleon braids on 3A strands + inter-
                   nucleon crossings between consecutive nucleons

(matches pair-production-nf.py convention where e⁻ = σ₀σ₁σ₀ and
e⁺ = σ₀⁻¹σ₁⁻¹σ₀⁻¹ as pure-braid particle representatives.)

FREE BASELINE: disjoint union of nucleon braids on 3A strands but
                without inter-nucleon crossings.

If the formula works, B_pred should match AME B(D) = 2.2246 MeV.
"""
from __future__ import annotations

import sys
import json
import math
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0

HBAR_Q = (q0 - 1.0) / q0
HBAR_Q_SQ = HBAR_Q * HBAR_Q

# E_0 as in rest of pipeline — topological volume is in natural units;
# the calibration ℏ_q² converts to MeV relative to β-decay Q.
M_E_MEV = 0.51099895
E_0_BETA_DECAY_MEV = 0.782


def proton_braid_on(n_strands: int, offset: int = 0) -> list[int]:
    """Proton as pure-braid word in B_{n_strands}, using generators
    σ_{offset}, σ_{offset+1}.

    Trefoil Δ₃ = σ_i σ_{i+1} σ_i.
    """
    if offset + 1 >= n_strands - 1:
        return []
    return [offset + 1, offset + 2, offset + 1]    # 1-indexed SnapPy


def neutron_braid_on(n_strands: int, offset: int = 0) -> list[int]:
    """Neutron as pure-braid word: σ_{offset}⁻¹σ_{offset+1}σ_{offset}⁻¹.

    Mirror-trefoil-adjacent (one σ flipped for udd content).
    """
    if offset + 1 >= n_strands - 1:
        return []
    return [-(offset + 1), offset + 2, -(offset + 1)]  # 1-indexed


def atom_braid_pure(Z: int, N: int, include_inter: bool = True
                      ) -> tuple[list[int], int]:
    """Pure-braid word for atom on 3A strands.

    Returns (word, n_strands) where word is a list of 1-indexed SnapPy
    braid generators (σ_i = i, σ_i⁻¹ = -i).
    """
    A = Z + N
    n_strands = 3 * A
    word: list[int] = []
    ordering = ['p'] * Z + ['n'] * N
    for k, nuc in enumerate(ordering):
        offset = 3 * k           # generators starting at σ_{3k+1}
        if nuc == 'p':
            word.extend(proton_braid_on(n_strands, offset=offset))
        else:
            word.extend(neutron_braid_on(n_strands, offset=offset))
        # Inter-nucleon crossing at σ_{3k+3} (1-indexed)
        if include_inter and k < A - 1:
            word.append(3 * k + 3)
    return word, n_strands


def snappy_volume_of_braid(word: list[int], n_strands: int) -> dict:
    """Compute hyperbolic volume of the braid closure via SnapPy."""
    try:
        import snappy
    except ImportError:
        return {"status": "no_snappy"}
    try:
        link = snappy.Link(braid_closure=word)
    except Exception as e:
        return {"status": f"link_error:{type(e).__name__}",
                 "message": str(e)[:100]}
    # Get the exterior as a 3-manifold
    try:
        M = link.exterior()
        try:
            M.simplify()
        except Exception:
            pass
        vol = M.volume()
        # May return a low-precision approximation; normalize
        vol_val = float(vol)
    except Exception as e:
        return {"status": f"volume_error:{type(e).__name__}",
                 "message": str(e)[:100], "word": word,
                 "n_strands": n_strands}
    try:
        solution_type = str(M.solution_type())
    except Exception:
        solution_type = "unknown"
    try:
        n_tet = M.num_tetrahedra()
    except Exception:
        n_tet = None
    return {
        "status": "ok",
        "volume": vol_val,
        "solution_type": solution_type,
        "n_tetrahedra": n_tet,
        "n_components": len(link.link_components),
        "word": word,
        "n_strands": n_strands,
    }


if __name__ == "__main__":
    print("=" * 100)
    print("SnapPy VOLUME BINDING — Kashaev-axiomatised mass")
    print(f"  q₀ = {q0:.6f}")
    print(f"  ℏ_q² = {HBAR_Q_SQ:.6e}")
    print(f"  density ρ = 1/ℏ_q² = {1.0/HBAR_Q_SQ:.4f}")
    print("=" * 100)

    # Check pure-braid words first
    for name, (Z, N) in [("D", (1, 1)), ("T", (1, 2)), ("3He", (2, 1)),
                           ("4He", (2, 2))]:
        w_atom, n_s = atom_braid_pure(Z, N, include_inter=True)
        w_free, _ = atom_braid_pure(Z, N, include_inter=False)
        print(f"\n  {name} (Z={Z}, N={N}, n_strands={n_s}):")
        print(f"    atom word: {w_atom}")
        print(f"    free word: {w_free}")

    # Compute volumes for each via SnapPy
    print(f"\n{'=' * 80}")
    print("SnapPy volume computations")
    print("=" * 80)
    ATOMS = [
        ("D",    1, 1, 2.22452),
        ("T",    1, 2, 8.481821),
        ("3He",  2, 1, 7.71804),
        ("4He",  2, 2, 28.295674),
    ]
    results = []
    for name, Z, N, B_AME in ATOMS:
        w_atom, n_s = atom_braid_pure(Z, N, include_inter=True)
        w_free, _ = atom_braid_pure(Z, N, include_inter=False)
        r_atom = snappy_volume_of_braid(w_atom, n_s)
        r_free = snappy_volume_of_braid(w_free, n_s)
        vol_atom = r_atom.get("volume", float("nan"))
        vol_free = r_free.get("volume", float("nan"))
        # Mass via ρ · V
        m_atom = (vol_atom / HBAR_Q_SQ) if math.isfinite(vol_atom) else float("nan")
        m_free = (vol_free / HBAR_Q_SQ) if math.isfinite(vol_free) else float("nan")
        # Binding
        B_pred_cat = m_free - m_atom if (
            math.isfinite(m_atom) and math.isfinite(m_free)) else float("nan")
        # Need to decide calibration — use E_0_BETA_DECAY for now
        B_pred_MeV = E_0_BETA_DECAY_MEV * B_pred_cat if math.isfinite(B_pred_cat) else float("nan")
        err = ((B_pred_MeV - B_AME) / B_AME * 100
                if math.isfinite(B_pred_MeV) and B_AME else float("nan"))
        print(f"\n  {name} (B_AME = {B_AME} MeV)")
        print(f"    atom: status={r_atom.get('status')} "
              f"vol={vol_atom:.4f} "
              f"sol={r_atom.get('solution_type')} "
              f"components={r_atom.get('n_components')}")
        print(f"    free: status={r_free.get('status')} "
              f"vol={vol_free:.4f} "
              f"sol={r_free.get('solution_type')} "
              f"components={r_free.get('n_components')}")
        print(f"    ΔVol = {vol_free - vol_atom if (math.isfinite(vol_atom) and math.isfinite(vol_free)) else 'N/A':>+.4f}")
        print(f"    B_pred_cat = ΔVol/ℏ_q² = {B_pred_cat:>+.4f}")
        print(f"    B_pred_MeV (E_0=0.782) = {B_pred_MeV:>+.4f}  "
              f"err = {err:>+.4f}%")
        results.append({
            "atom": name, "Z": Z, "N": N, "A": Z + N,
            "B_AME_MeV": B_AME,
            "word_atom": w_atom,
            "word_free": w_free,
            "vol_atom": vol_atom,
            "vol_free": vol_free,
            "solution_type_atom": r_atom.get("solution_type"),
            "solution_type_free": r_free.get("solution_type"),
            "delta_vol": (vol_free - vol_atom
                            if (math.isfinite(vol_atom) and math.isfinite(vol_free))
                            else None),
            "B_pred_cat": B_pred_cat,
            "B_pred_MeV": B_pred_MeV,
            "err_pct": err,
        })

    witness = {
        "computation": "snappy-volume-binding",
        "description": (
            "Kashaev-axiomatised mass formula: 𝔪(K) = Vol(K)/ℏ_q² "
            "evaluated via SnapPy on pure-braid representatives of the "
            "atom and free-atom closures.  B(Z,N) = [Vol(free) − "
            "Vol(atom)] / ℏ_q² · E_0.  Tests whether the topological "
            "mass formula reproduces AME binding when computed from "
            "pure topology (bypassing the categorical derivation).  "
            "Pure-braid words: proton = σ₀σ₁σ₀ (trefoil); neutron = "
            "σ₀⁻¹σ₁σ₀⁻¹; atom = per-nucleon stacking + inter-nucleon "
            "σ_{3k+2} crossings.  Caveat: the Hecke 'ud' superposition "
            "½(σ + σ⁻¹) is collapsed to a single σ representative for "
            "purposes of topological-invariant extraction."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q0": q0, "hbar_q": HBAR_Q, "hbar_q_sq": HBAR_Q_SQ,
            "rho_q": 1.0 / HBAR_Q_SQ,
            "E_0_MeV": E_0_BETA_DECAY_MEV,
        },
        "atoms": results,
    }
    out = Path(__file__).parent / "snappy-volume-binding.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
