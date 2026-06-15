#!/usr/bin/env python3
"""Joint mass-tower SDP confinement solver.

Implements the design specification of
[prop:joint-tower-sdp-confinement](
  ../../content/quantum-observable-universe/braids-and-knots/joint-tower-sdp-confinement.md).

PHASE 3a — H_3 ground-truth VERIFIER:

  At small confinement levels the canonical T_w per atom is already
  known from confined-particle.md.  This module runs the known
  σ-words through gb_filtration_jet_tracker.py to produce per-atom
  GB-filtration + jet-order certificates, then verifies the cross-
  level consistency constraints (4) of the design spec.

  No actual semidefinite-program solver is invoked yet — that lands
  at Phase 3b when scaling to H_12 (⁴He), H_18 (⁶Li), H_21 (⁷Li)
  where the canonical T_w is NOT known and must be solved for.

  The verifier output is the structured certificate
        Φ(q_0) = {(T_w(𝔥), Filt(𝔥), JetLog(𝔥))}_{𝔥 ∈ ℛ}
  exactly as consumed by prop:atom-knot-mass-derivation.

Test cases (Phase 3a):
  - quark    n_0 = 1  T_w = σ_0 (trivial single-strand)
  - electron n_0 = 2  T_w = σ_1^3 in H_2
  - proton   n_0 = 3  T_w = (σ_1 σ_2^{-1})^3 in H_3 with flav-uud
  - neutron  n_0 = 3  T_w = (σ_1 σ_2^{-1})^3 in H_3 with flav-udd

  Cross-level edges verified:
    nucleon (H_3) ←─ 3 ⊗ quark (H_1^{⊗3})

Output:
  joint-tower-sdp-h3.witness.json with per-atom certificate +
  cross-level consistency check log.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from gb_filtration_jet_tracker import HeckeElement, perm_to_canonical_word


# ───────────────────────────────────────────────────────────────────
# Registry of known canonical T_w from confined-particle.md
# (only the small-strand entries where the answer is direct).
# ───────────────────────────────────────────────────────────────────

REGISTRY = [
    {
        "name": "quark",
        "ell": 0,
        "n_0": 1,
        "braid_word": [],          # identity in H_1 (trivial single strand)
        "constituents": [],        # no sub-tower
        "rho_factor": 0,           # confined; mass invariant zero alone
    },
    {
        "name": "electron",
        "ell": 1,
        "n_0": 2,
        "braid_word": [1, 1, 1],   # σ_1^3 in H_2
        "constituents": [],        # no sub-tower (lepton)
        "rho_factor": 1,
    },
    {
        "name": "proton",
        "ell": 1,
        "n_0": 3,
        "braid_word": [1, -2, 1, -2, 1, -2],  # (σ_1 σ_2^{-1})^3 in H_3
        "constituents": ["quark", "quark", "quark"],   # 3⊗quark
        "rho_factor": 1,
        "flavour_tag": "uud",
    },
    {
        "name": "neutron",
        "ell": 1,
        "n_0": 3,
        "braid_word": [1, -2, 1, -2, 1, -2],  # same body, different flavour
        "constituents": ["quark", "quark", "quark"],
        "rho_factor": 1,
        "flavour_tag": "udd",
    },
]


# ───────────────────────────────────────────────────────────────────
# Per-atom solver: feed braid through gb_filtration_jet_tracker.
# ───────────────────────────────────────────────────────────────────

def solve_per_atom(entry: dict) -> dict:
    """Run the canonical braid through GB-NF reduction; emit
    structured certificate matching the design spec (Wedderburn-block
    × filtration grade × jet position → coefficient)."""
    n_0 = entry["n_0"]
    word = entry["braid_word"]

    if n_0 == 1 or not word:
        # Trivial: H_1 has only the identity element T_e with coefficient 1.
        # The "certificate" is the identity Hecke element.
        cert = {"0": [{"perm": list(range(1, n_0 + 1)),
                       "canonical_word": [],
                       "coefficient_in_q": "1"}]}
        return {
            "name": entry["name"],
            "n_0": n_0,
            "braid_word_input": word,
            "filtration_certificate": cert,
            "filtration_shape": {0: 1},
            "max_grade": 0,
            "jet_log": [],
            "n_steps": 0,
            "n_hecke_relations_fired": 0,
            "constituents": entry.get("constituents", []),
            "flavour_tag": entry.get("flavour_tag", None),
            "rho_factor": entry.get("rho_factor", 1),
        }

    # Reduce via gb_filtration_jet_tracker
    E = HeckeElement.identity(n_0)
    for i in word:
        if i > 0:
            E = E.right_mul_T(i)
        else:
            E = E.right_mul_T_inv(-i)

    cert = E.filtration_certificate()
    structured = {
        str(grade): [
            {"perm": list(w),
             "canonical_word": list(perm_to_canonical_word(w)),
             "coefficient_in_q": c}
            for w, c in sorted(terms)
        ]
        for grade, terms in cert.items()
    }
    filtration_shape = {grade: len(terms) for grade, terms in cert.items()}
    max_grade = max(cert.keys()) if cert else 0
    n_hecke = sum(1 for ev in E.jet_log if ev.relation == "hecke-quadratic")

    return {
        "name": entry["name"],
        "n_0": n_0,
        "braid_word_input": word,
        "filtration_certificate": structured,
        "filtration_shape": filtration_shape,
        "max_grade": max_grade,
        "jet_log": [
            {"step": ev.step, "multiplier": ev.multiplier,
             "predecessor": list(ev.predecessor), "successor": list(ev.successor),
             "filtration_before": ev.filtration_before,
             "filtration_after": ev.filtration_after,
             "relation": ev.relation}
            for ev in E.jet_log
        ],
        "n_steps": len(E.jet_log),
        "n_hecke_relations_fired": n_hecke,
        "constituents": entry.get("constituents", []),
        "flavour_tag": entry.get("flavour_tag", None),
        "rho_factor": entry.get("rho_factor", 1),
    }


# ───────────────────────────────────────────────────────────────────
# Cross-level consistency verifier (constraint (4) of design spec).
# ───────────────────────────────────────────────────────────────────

def verify_cross_level_consistency(parent_cert: dict, child_certs: list) -> dict:
    """Verify the canonical embedding π : ⊗_i H_{n_0(child_i)} ↪ H_{n_0(parent)}.

    For Phase 3a (nucleon ← 3⊗quark) the embedding sends each child
    H_1 (trivial identity element T_e) to a strand of the parent H_3.
    The parent's filtration certificate must include a non-zero
    coefficient on T_e (= identity element of H_3, grade 0) — this is
    the "vacuum" contribution that the quarks contribute.

    Verifier output: pass / fail + diagnostic.
    """
    parent_grade_0 = parent_cert["filtration_certificate"].get("0", [])
    has_grade_0 = len(parent_grade_0) > 0

    # The embedding π_{nucleon ← 3⊗quark} sends ⊗_i T_e^{(quark_i)}
    # to T_e^{(nucleon)} in H_3.  The check is that the parent
    # has a non-trivial T_e component (grade-0 term) — verified by
    # presence in filtration_certificate["0"].
    sum_child_n_0 = sum(c["n_0"] for c in child_certs)
    embedding_dimension_match = (sum_child_n_0 == parent_cert["n_0"])

    return {
        "parent": parent_cert["name"],
        "children": [c["name"] for c in child_certs],
        "embedding_codomain_n_0": parent_cert["n_0"],
        "embedding_domain_n_0": sum_child_n_0,
        "embedding_dimension_match": embedding_dimension_match,
        "parent_has_grade_0": has_grade_0,
        "parent_grade_0_terms": parent_grade_0,
        "verification_passes": embedding_dimension_match and has_grade_0,
    }


# ───────────────────────────────────────────────────────────────────
# Driver.
# ───────────────────────────────────────────────────────────────────

def main():
    base = Path(__file__).parent
    out_path = base / "joint-tower-sdp-h3.witness.json"

    print("══════════════════════════════════════════════════════════════════════")
    print("  Joint mass-tower SDP — Phase 3a verifier (H_3 ground truth)")
    print("══════════════════════════════════════════════════════════════════════")

    # Step 1: per-atom certificates
    per_atom_certs = []
    for entry in REGISTRY:
        cert = solve_per_atom(entry)
        per_atom_certs.append(cert)
        flavour = (f" (flavour {cert['flavour_tag']})"
                   if cert.get("flavour_tag") else "")
        print(f"\n──── {cert['name']}{flavour}, n_0 = {cert['n_0']} ────")
        print(f"  braid: {cert['braid_word_input']}")
        print(f"  filtration shape: {cert['filtration_shape']}")
        print(f"  max grade: {cert['max_grade']}")
        print(f"  jet steps: {cert['n_steps']}, "
              f"Hecke relations fired: {cert['n_hecke_relations_fired']}")
        print(f"  ρ factor: {cert['rho_factor']}")

    # Lookup table by name for cross-level checks.
    by_name = {c["name"]: c for c in per_atom_certs}

    # Step 2: cross-level consistency (constraint (4))
    edges = []
    for entry in REGISTRY:
        if not entry.get("constituents"):
            continue
        parent = by_name[entry["name"]]
        children = [by_name[c] for c in entry["constituents"]]
        check = verify_cross_level_consistency(parent, children)
        edges.append(check)

    print(f"\n══════════════════════════════════════════════════════════════════════")
    print(f"  Cross-level consistency (constraint (4) of design spec)")
    print(f"══════════════════════════════════════════════════════════════════════")
    for chk in edges:
        flag = "✓" if chk["verification_passes"] else "✗"
        print(f"  {flag} {chk['parent']} ← " +
              " + ".join(chk["children"]) +
              f"  (n_0: {chk['embedding_domain_n_0']} → {chk['embedding_codomain_n_0']})")

    # Step 3: emit witness
    witness = {
        "computation": "joint-tower-sdp-h3",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Phase 3a verifier: runs known canonical T_w for "
            "{quark, electron, proton, neutron} through "
            "gb_filtration_jet_tracker to produce structured "
            "certificates matching prop:joint-tower-sdp-confinement. "
            "Verifies cross-level consistency for nucleon ← 3⊗quark. "
            "No SDP solver invoked yet — that lands at Phase 3b for "
            "H_12 (⁴He) and beyond."
        ),
        "design_spec": "prop:joint-tower-sdp-confinement",
        "consumed_by": "prop:atom-knot-mass-derivation",
        "phase": "3a",
        "registry": REGISTRY,
        "per_atom_certificates": per_atom_certs,
        "cross_level_consistency_checks": edges,
        "summary": {
            "n_atoms": len(per_atom_certs),
            "all_consistent": all(e["verification_passes"] for e in edges),
            "max_grade_observed": max(c["max_grade"] for c in per_atom_certs),
            "total_jet_steps": sum(c["n_steps"] for c in per_atom_certs),
            "total_hecke_relations_fired": sum(c["n_hecke_relations_fired"]
                                                for c in per_atom_certs),
            "next_steps": [
                "Phase 3b: extend to H_6 (²H), H_9 (³H, ³He), H_12 (⁴He). "
                "Canonical T_w not yet known for these — needs actual SDP "
                "solver (cvxpy or scipy.optimize with PSD constraints).",
                "Phase 3c: extend to H_18 (⁶Li), H_21 (⁷Li). Replaces the "
                "deprecated li-atom-knot-search.witness.json with principled "
                "derivations.",
            ],
        },
    }

    with open(out_path, "w") as f:
        json.dump(witness, f, indent=2, ensure_ascii=False)
    print(f"\n→ wrote {out_path}")
    print(f"  atoms: {witness['summary']['n_atoms']}, "
          f"all consistent: {witness['summary']['all_consistent']}")


if __name__ == "__main__":
    main()
