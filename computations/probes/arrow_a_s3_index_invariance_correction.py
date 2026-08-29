#!/usr/bin/env python3
"""W1 arrow (A) — CORRECTION to PR #4498: the 3D-index is S₃-INVARIANT
(trivial isotypic only), so there is no "graded standard component" to build
from. The corrected (stronger) finding replaces it.

WHAT #4498 GOT WRONG.  PR #4498 computed the S₃-isotypic decomposition of the
729-dimensional representation SPACE ℂ[classes] = 165·triv ⊕ 84·sign ⊕ 240·std,
and then claimed I_tot_meridian "discards the 240 standard copies" and that a
derived arrow (A) should "build from the graded standard component."  That
conflated the representation-SPACE decomposition with the index FUNCTION's
content.

THE FACT.  The 3D-index function b ↦ I_𝓑₃(b) is S₃-INVARIANT: I(σ·b) = I(b) for
every cusp permutation σ (the S₃ symmetry of 𝓑₃ is realised by isometries).
This is corpus-verified — the graded-index witness stores ONE q-series per
S₃-orbit (165 entries for 729 classes; orbit-size distribution {1:9, 3:72, 6:84})
and its symmetry menu lists the cusp permutations as exact table symmetries
(2026-07-24 §2: "729 classes × 6 permutations, direct equality").

CONSEQUENCE.  An S₃-invariant vector lives ENTIRELY in the trivial isotypic
(dim 165 = #orbits).  So the index carries ZERO sign and ZERO standard content —
the 84·sign + 240·std live in the representation space, NOT in the index vector.
Therefore:

  1. I_tot_meridian (the sum over the meridian sublattice) and the graded index
     carry the SAME (trivial) S₃-content; I_tot discards NOTHING.  (#4498's
     "discards 240 standard copies" is false.)
  2. The S₃-equivariance invariant is VACUOUS for arrow (A): a trivial-rep index
     mapping to the S₃-invariant scalar tr_M(β_Bor) is automatically consistent
     and unconstrained.  S₃ does not constrain (A) — at any level.
  3. THE REAL (corrected) STRUCTURAL POINT — a rep-theoretic gap.  tr_M(β_Bor)'s
     underlying operator ρ(β_Bor) lives in the Hecke H₃(q) block [2,1] = the
     STANDARD S₃-irrep (borromean-h3-2-1-irrep-derivation), while the 3D-index is
     trivial-only.  So the STANDARD structure of the binding operator is NOT
     sourced by the 3D-index; it is CATEGORICAL (Hecke/Wedderburn).  Arrow (A)
     can fix only the S₃-invariant SCALAR tr_M; the [2,1] operator structure must
     come from the categorical side.

CORRECTED BUILD GUIDANCE (supersedes #4498 step 1).  Do NOT try to source
tr_M's standard structure from the index (impossible — the index is trivial).
Arrow (A) is a map of S₃-SCALARS (index total → tr_M scalar); the operator/[2,1]
content of the binding is Hecke-categorical and enters through arrow (B) and the
Wedderburn structure, not through (A).

Discipline: audit-only; scope-(a); no fit; nothing wired; L2 unchanged.  This is
an honest self-correction of a merged claim (#4498), per the anti-laundering /
"before declaring" disciplines.

-- Ref: [manuscript] docs/audits/2026-08-01-arrow-a-s3-index-invariance-correction.md
"""
from __future__ import annotations

import hashlib
import itertools
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    # 1. Representation-space decomposition of C[729] (as in #4498) — CORRECT as such.
    vals = [(p, q) for p in (-1, 0, 1) for q in (-1, 0, 1)]
    classes = list(itertools.product(vals, repeat=3))
    def perm(c, s): return tuple(c[s[i]] for i in range(3))
    def fix(s): return sum(1 for c in classes if perm(c, s) == c)
    Fe, Ft, Fs = fix((0, 1, 2)), fix((1, 0, 2)), fix((1, 2, 0))
    space = {"trivial": (Fe + 3 * Ft + 2 * Fs) // 6,
             "sign": (Fe - 3 * Ft + 2 * Fs) // 6,
             "standard": (2 * Fe - 2 * Fs) // 6}

    # 2. The index FUNCTION is S₃-invariant (constant on orbits) — the corpus
    #    witness is REQUIRED (it IS the evidence): 165 orbit-keyed q-series over
    #    729 classes ⇒ one value per S₃-orbit ⇒ S₃-invariant. Do NOT fall back to
    #    hard-coded sizes — that would let the verdict pass without the evidence.
    wpath = Path(__file__).resolve().parent / "borromean-3d-index-graded.witness.json"
    if not wpath.exists():
        print(f"ERROR: required witness not found: {wpath.name}. Cannot verify the "
              f"S₃-invariance of the index without it — aborting (no verdict).")
        return 2
    gt = json.loads(wpath.read_text())["data"]["graded_table_nonzero"]
    orbit_keyed = len(gt)
    sizes = {}
    for v in gt.values():
        sizes[v["orbit_size"]] = sizes.get(v["orbit_size"], 0) + 1
    # the witness stores ONE q-series per orbit and Σ orbit_size = 729 ⇒ the index
    # is constant on orbits (S₃-invariant); check the class count closes exactly.
    n_classes = sum(k * n for k, n in sizes.items())

    print("W1 arrow (A) — CORRECTION to #4498: the 3D-index is S₃-invariant\n")
    print(f"representation space C[729]: {space['trivial']}·triv ⊕ {space['sign']}·sign "
          f"⊕ {space['standard']}·std   (this is the SPACE, not the index)")
    print(f"index FUNCTION: S₃-INVARIANT (constant on orbits) — witness stores "
          f"{orbit_keyed} orbit-keyed q-series; orbit sizes {sizes}")
    print(f"  ⇒ the index vector lives in the trivial isotypic ONLY (dim {space['trivial']});")
    print(f"    it has ZERO sign and ZERO standard content.")

    print(f"\nCorrected finding (supersedes #4498):")
    print(f"  1. I_tot_meridian and the graded index have the SAME (trivial) S₃-content;")
    print(f"     I_tot discards NOTHING — #4498's 'discards 240 standard copies' is FALSE.")
    print(f"  2. S₃-equivariance is VACUOUS for arrow (A): trivial index → trivial scalar tr_M.")
    print(f"  3. rep-theoretic GAP: tr_M's operator lives in Hecke [2,1]=STANDARD, index is")
    print(f"     trivial-only ⇒ tr_M's [2,1] structure is CATEGORICAL, not index-sourced.")
    print(f"     Arrow (A) fixes only the S₃-invariant scalar; the operator structure is Hecke.")

    ok = ((Fe, Ft, Fs) == (729, 81, 9)
          and space == {"trivial": 165, "sign": 84, "standard": 240}
          and orbit_keyed == 165 and n_classes == 729)
    print(f"\nVERDICT: {'CONFIRMED' if ok else 'CHECK'} — index is S₃-invariant (trivial-only, "
          f"{space['trivial']} = #orbits); #4498's 'graded standard component' does not exist; "
          f"S₃ is vacuous for (A); tr_M's standard structure is categorical.")

    sp = Path(__file__).resolve(); src = sp.read_text()
    rel = "computations/probes/arrow_a_s3_index_invariance_correction.py"
    # Provenance: commitSha = repo HEAD at emission (what the provenance audit
    # wants); scriptCommitSha = this script's last-change commit (falls back to
    # HEAD when the file is not yet committed).
    try:
        root = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], cwd=sp.parent, text=True).strip()
        head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
        script_commit = subprocess.check_output(["git", "log", "-1", "--format=%H", "--", rel], cwd=root, text=True).strip() or head
    except Exception:
        head = script_commit = "unknown"
    wit = {
        "engine": "python-int", "engineVersion": "exact integer enumeration",
        "computedAt": datetime.now(timezone.utc).isoformat(), "commitSha": head,
        "scriptFile": rel, "scriptHash": hashlib.sha256(src.encode()).hexdigest()[:12], "scriptCommitSha": script_commit,
        "description": "CORRECTION to #4498: the 3D-index is S₃-invariant (trivial isotypic only); "
                       "no graded standard component exists; S₃ is vacuous for arrow (A); tr_M's "
                       "[2,1] standard structure is categorical, not index-sourced. Audit-only.",
        "auditOnly": True,
        "parameters": {"corrects_pr": 4498},
        "data": {
            "rep_space_decomposition": space,
            "index_function_isotypic": "trivial only (S3-invariant; constant on orbits)",
            "orbit_keyed_entries": orbit_keyed, "orbit_sizes": sizes,
            "correction": "#4498 conflated rep-space (240 std) with the index vector (trivial only); "
                          "no graded standard component exists to build from.",
            "corrected_finding": "S3 vacuous for (A); tr_M [2,1]-standard structure is categorical/Hecke, "
                                 "not sourced by the trivial-only 3D-index.",
            "verdict_ok": bool(ok),
        },
    }
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    wit.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        wit, script_path=__file__, engine=None, q0_anchor=False)
    (sp.with_name("arrow-a-s3-index-invariance-correction.witness.json")).write_text(json.dumps(wit, indent=2) + "\n")
    print(f"\nwitness → arrow-a-s3-index-invariance-correction.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
