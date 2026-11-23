#!/usr/bin/env python3
"""EW/Higgs SDP probe — exploratory.

Per the 2026-05-02 NV-1 audit (`docs/audits/2026-05-02-nv-frob-filter-conjectures.md`),
the paper has no block identifying W±, Z as specific torus knots — this
is the principal blocker for deriving the weak-scale crossing count N_v.

The Bring genus-4 inventory (`docs/audits/...` §Bring-surface inventory)
shows there are no unidentified torus knots on Bring at genus ≤ 4. Three
remaining paths for W±, Z:
    α — non-Bring genus-2 torus links (T(2,6) → Z, T(2,8) → H per
        `knot-particle-generation.md`)
    β — T_{3,5} double-duty (paper-internal speculation in
        `unmapped-torus-knots.md` lines 104–111)
    γ — non-torus knots (e.g. figure-eight 4_1 for Higgs per
        `topological-mass-trefoil.md`)

This probe runs the joint-tower SDP infrastructure on a candidate
EW/Higgs registry covering all three paths, to see which produce
feasible PSD certificates at H_3 and which require deferral to Rust
seminormal_mn at higher n.

Outputs: ew-higgs-sdp-probe.witness.json
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from joint_tower_sdp_solver import REGISTRY as REGISTRY_PHASE_3A  # noqa
from joint_tower_sdp_solver import solve_per_atom
from joint_tower_sdp_solver_v2 import (
    sdp_feasibility_h3,
    q_0_NUMERIC,
)
import mpmath as mp
from _precision import set_compute_dps, fmt
from qou_substrate.constants import Q_50_DIGIT_STR

# Ref: [leitner2026] conj:electroweak-higgs-torus-link-triplet
set_compute_dps()
Q_PROTON = mp.mpf(Q_50_DIGIT_STR)  # proton pin (package layer)

# ───────────────────────────────────────────────────────────────────
# EW/Higgs candidate registry — three paths.
# ───────────────────────────────────────────────────────────────────
# Mass values (PDG): m_W = 80.379 GeV, m_Z = 91.188 GeV, m_H = 125.25 GeV.

REGISTRY_EW_HIGGS = [
    # ─── Path α: non-Bring genus-2 candidates ────────────────────────
    {
        "name": "Z_T26_path_alpha",
        "particle": "Z^0",
        "knot_or_link": "T(2,6)  [2-component torus link, Solomon's]",
        "braid_word": [1, 1, 1, 1, 1, 1],   # σ_1^6 in B_2
        "braid_strand_count": 2,
        "genus": 2,
        "mass_GeV": 91.188,
        "path": "α: non-Bring genus-2 torus link",
        "ref": "knot-particle-generation.md",
    },
    {
        "name": "H_T28_path_alpha",
        "particle": "Higgs",
        "knot_or_link": "T(2,8)  [2-component torus link]",
        "braid_word": [1, 1, 1, 1, 1, 1, 1, 1],   # σ_1^8 in B_2
        "braid_strand_count": 2,
        "genus": 3,
        "mass_GeV": 125.25,
        "path": "α: non-Bring genus-3 torus link",
        "ref": "knot-particle-generation.md",
    },
    {
        "name": "W_T24_path_alpha",
        "particle": "W^±",
        "knot_or_link": "T(2,4)  [2-component torus link, Solomon's seal]",
        "braid_word": [1, 1, 1, 1],   # σ_1^4 in B_2
        "braid_strand_count": 2,
        "genus": 1,
        "mass_GeV": 80.379,
        "path": "α: non-Bring genus-1 torus link (lighter than Z)",
        "ref": "knot-particle-generation.md (analog)",
    },

    # ─── Path β: T_{3,5} double-duty (Bring-saturating) ──────────────
    {
        "name": "weak_T35_path_beta",
        "particle": "weak triplet (W±, Z combined as T_{3,5})",
        "knot_or_link": "T(3,5) [genus-4 torus knot, Bring-saturating]",
        "braid_word": [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],   # (σ_1 σ_2)^5 in B_3
        "braid_strand_count": 3,
        "genus": 4,
        "mass_GeV": None,  # composite; SDP probes structure
        "path": "β: T_{3,5} carries weak interaction (already on Bring)",
        "ref": "unmapped-torus-knots.md:104-111",
    },

    # ─── Path γ: non-torus knots ─────────────────────────────────────
    {
        "name": "H_4_1_path_gamma",
        "particle": "Higgs",
        "knot_or_link": "4_1 (figure-eight, hyperbolic, NOT torus)",
        "braid_word": [1, -2, 1, -2],   # standard B_3 representation
        "braid_strand_count": 3,
        "genus": 1,
        "mass_GeV": 125.25,
        "path": "γ: non-torus hyperbolic knot",
        "ref": "topological-mass-trefoil.md",
    },
    {
        "name": "Z_5_2_path_gamma",
        "particle": "Z^0",
        "knot_or_link": "5_2 (5-crossing prime knot, hyperbolic)",
        "braid_word": [1, 1, 1, -2, 1, -2],   # standard B_3 representation
        "braid_strand_count": 3,
        "genus": 1,
        "mass_GeV": 91.188,
        "path": "γ: non-torus hyperbolic knot",
        "ref": "speculative",
    },
    {
        "name": "W_3_1_path_gamma",
        "particle": "W^±",
        "knot_or_link": "3_1 (trefoil, but reused — see comment)",
        "braid_word": [1, 1, 1],   # σ_1^3 in B_2 → T(2,3)
        "braid_strand_count": 2,
        "genus": 1,
        "mass_GeV": 80.379,
        "path": "γ: trefoil (already used for electron — speculative reuse)",
        "ref": "speculative",
    },
]


def solve_ew_entry(entry: dict) -> dict:
    """Run GB-filtration certificate + SDP feasibility (when n=3)."""
    n = entry["braid_strand_count"]
    word = entry["braid_word"]

    structural_entry = {
        "name": entry["name"],
        "ell": 2,
        "n_0": n,
        "braid_word": word,
        "rho_factor": 1,
    }
    cert = solve_per_atom(structural_entry)
    cert["particle"] = entry["particle"]
    cert["knot_or_link"] = entry["knot_or_link"]
    cert["genus"] = entry["genus"]
    cert["mass_GeV"] = entry["mass_GeV"]
    cert["path"] = entry["path"]
    cert["ref"] = entry["ref"]

    if n == 3:
        try:
            sdp_check = sdp_feasibility_h3(word, q_0_NUMERIC)
            cert["sdp_feasibility"] = sdp_check
            cert["sdp_feasibility_status"] = "checked"
        except Exception as e:
            cert["sdp_feasibility_status"] = f"error: {e}"
    elif n == 2:
        # B_2 has trivial Hecke quotient (one generator, one relation).
        # PSD check is straightforward: σ_1^k acts as q^k on sym, (-q^{-1})^k on alt.
        # Exact closed form at the proton q0 (mpmath, no float64): q^k > 0 for
        # every k, and (-q^{-1})^k >= 0 iff k is even, so PSD is decided by
        # the parity of k, not by a numerical threshold.
        q = Q_PROTON
        k = sum(1 if w > 0 else -1 for w in word)
        sym_eig = q ** k
        alt_eig = (-1 / q) ** k
        cert["sdp_feasibility"] = {
            "B_2_sym_eigenvalue": fmt(sym_eig),
            "B_2_alt_eigenvalue": fmt(alt_eig),
            "B_2_sym_psd": True,
            "B_2_alt_psd": k % 2 == 0,
            "all_blocks_psd_or_close": k % 2 == 0,
            "k": k,
            "comment": (
                "B_2 Hecke has only sym + alt blocks. σ_1^k eigenvalues: "
                "q^k (sym), (-q^{-1})^k (alt). Alt sign = (-1)^k."
            ),
        }
        cert["sdp_feasibility_status"] = "checked (B_2 closed form)"
    else:
        cert["sdp_feasibility_status"] = (
            f"DEFERRED to Rust: B_{n} requires Hoefsmit seminormal at H_{n}"
        )
    return cert


def main():
    base = Path(__file__).parent
    out_path = base / "ew-higgs-sdp-probe.witness.json"

    print("=" * 70)
    print("  EW/Higgs SDP probe — exploratory (NV-1 path-finder)")
    print("=" * 70)

    per_entry_certs = []
    for entry in REGISTRY_EW_HIGGS:
        print(f"\n──── {entry['name']} ({entry['particle']} / {entry['knot_or_link']}) ────")
        print(f"  path: {entry['path']}")
        print(f"  braid word: {entry['braid_word']}  in B_{entry['braid_strand_count']}")
        cert = solve_ew_entry(entry)
        per_entry_certs.append(cert)
        print(f"  filtration shape: {cert['filtration_shape']}")
        print(f"  jet steps: {cert['n_steps']}, "
              f"Hecke fires: {cert['n_hecke_relations_fired']}")
        sf = cert.get("sdp_feasibility_status", "—")
        print(f"  SDP status: {sf}")
        if cert.get("sdp_feasibility_status") in ("checked", "checked (B_2 closed form)"):
            sdp = cert["sdp_feasibility"]
            if "trivial_(3)" in sdp:
                print(f"    triv (3):       {sdp['trivial_(3)']['value']:+.6e}  "
                      f"{'PSD' if sdp['trivial_(3)']['psd'] else 'NOT PSD'}")
                print(f"    sign (1,1,1):   {sdp['sign_(1,1,1)']['value']:+.6e}  "
                      f"{'PSD' if sdp['sign_(1,1,1)']['psd'] else 'NOT PSD'}")
                print(f"    std (2,1) min eig: {sdp['standard_(2,1)']['min_eigenvalue']:+.6e}  "
                      f"{'PSD' if sdp['standard_(2,1)']['psd_symmetric_part'] else 'NOT PSD'}")
                print(f"    ALL PSD: {sdp['all_blocks_psd_or_close']}")
            else:
                print(f"    sym eig: {mp.nstr(mp.mpf(sdp['B_2_sym_eigenvalue']), 7)}  "
                      f"{'PSD' if sdp['B_2_sym_psd'] else 'NOT PSD'}")
                print(f"    alt eig: {mp.nstr(mp.mpf(sdp['B_2_alt_eigenvalue']), 7)}  "
                      f"{'PSD' if sdp['B_2_alt_psd'] else 'NOT PSD'}")
                print(f"    ALL PSD: {sdp['all_blocks_psd_or_close']}")

    witness = {
        "computation": "ew-higgs-sdp-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "purpose": (
            "Exploratory probe of the joint-tower SDP infrastructure on "
            "candidate EW/Higgs torus-knot identifications. Maps to the "
            "three remaining paths (α non-Bring genus-2; β T_{3,5} double-"
            "duty; γ non-torus) per docs/audits/2026-05-02-nv-frob-filter-"
            "conjectures.md NV-1 §Bring-surface inventory."
        ),
        "q_0_numeric": fmt(Q_PROTON),
        "q_0_numeric_h3_solver": "float64 q_0_NUMERIC of joint_tower_sdp_solver_v2 (H_3 entries only; not changed here)",
        "registry": REGISTRY_EW_HIGGS,
        "per_entry_certificates": per_entry_certs,
        "summary": {
            "n_entries": len(per_entry_certs),
            "psd_pass": sum(
                1 for c in per_entry_certs
                if c.get("sdp_feasibility", {}).get("all_blocks_psd_or_close", False)
            ),
            "psd_fail": sum(
                1 for c in per_entry_certs
                if c.get("sdp_feasibility_status") in ("checked", "checked (B_2 closed form)")
                and not c.get("sdp_feasibility", {}).get("all_blocks_psd_or_close", False)
            ),
            "deferred": sum(
                1 for c in per_entry_certs
                if "DEFERRED" in c.get("sdp_feasibility_status", "")
            ),
        },
    }
    with open(out_path, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(witness, f, indent=2, ensure_ascii=False, default=str)
    print(f"\n→ wrote {out_path}")
    print(f"  PSD pass: {witness['summary']['psd_pass']} / "
          f"PSD fail: {witness['summary']['psd_fail']} / "
          f"deferred: {witness['summary']['deferred']}")


if __name__ == "__main__":
    main()
