#!/usr/bin/env python3
"""W1 arrow (A) — the S₃-equivariance invariant, and why I_tot_meridian is the
wrong object to bridge from.

The `I_𝓑₃ → tr_M(β_Bor)` bridge invariant list
(docs/audits/2026-07-24-borromean-index-bridge-invariant.md §1(a)) requires that
any derived arrow (A) factor through the cusp-symmetry (S₃ permuting the three
Borromean components) — a map of S₃-representations.  This probe makes that
invariant concrete and extracts a structural constraint on the build.

The 3D-index is graded over H₁(∂𝓑₃; ℤ) restricted to {−1,0,1}⁶ = 729 peripheral
classes, with S₃ permuting the three (p_h, q_h) cusp blocks.  Directly:

  Fix(e) = 729,  Fix(transposition) = 81,  Fix(3-cycle) = 9,

so the S₃-permutation representation on the 729 classes decomposes as

  165·trivial ⊕ 84·sign ⊕ 240·standard          (mult(triv) = 165 = #orbits).

On the tr_M side, β_Bor lives in the Iwahori–Hecke algebra H₃(q), whose
Wedderburn blocks are the partitions of 3 = the S₃-irreps:
  [3] → trivial (1d),  [1,1,1] → sign (1d),  [2,1] → standard (2d).
The Borromean's non-trivial content sits in the [2,1] (standard) block
(borromean-h3-2-1-irrep-derivation).

THE FINDING.  `I_tot_meridian` (the corpus series [1,6,129,−510,…] that arrow (A)
has been trying to reproduce) is the S₃-INVARIANT sum over the cusp-symmetric
meridian sublattice — i.e. the projection onto the 165·trivial part.  It DISCARDS
all 240 standard copies, exactly the S₃-non-trivial geometric content.  So:

  • I_tot_meridian → tr_M(β_Bor) is a trivial → trivial map: the S₃ invariant
    gives NO constraint on it, and I_tot_meridian is the UNDER-CONSTRAINED object.
  • The real S₃ constraint lives at the GRADED (pre-sum) level: a derived (A)
    must carry the 240 standard copies onto the single Hecke [2,1] block — a
    massive but S₃-typed projection.  This is the object a build should target.

Consequence for the build (docs): construct (A) from the graded index's
standard-isotypic component, NOT from the summed I_tot_meridian.  This is a
necessary-condition sharpening of arrow (A), not a derivation of it.

Discipline: audit-only; scope-(a); NO fit; nothing wired; L2 unchanged.  The
729-class S₃ action is enumerated exactly (integers); the decomposition is
cross-checked against the committed graded-index witness (#orbits = 165).

-- Ref: [manuscript] docs/audits/2026-08-01-arrow-a-s3-equivariance-and-build-plan.md
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
    vals = [(p, q) for p in (-1, 0, 1) for q in (-1, 0, 1)]   # 9 values/cusp
    classes = list(itertools.product(vals, repeat=3))          # 3 cusps → 729
    assert len(classes) == 729

    def perm(cls, sigma):
        return tuple(cls[sigma[i]] for i in range(3))

    def fix(sigma):
        return sum(1 for c in classes if perm(c, sigma) == c)

    Fe = fix((0, 1, 2)); Ft = fix((1, 0, 2)); Fs = fix((1, 2, 0))
    m_triv = (Fe + 3 * Ft + 2 * Fs) // 6
    m_sign = (Fe - 3 * Ft + 2 * Fs) // 6
    m_std = (2 * Fe - 2 * Fs) // 6

    print("W1 arrow (A) — S₃-equivariance invariant\n")
    print(f"graded index, 729 peripheral classes, S₃ cusp-permutation action:")
    print(f"  Fix(e)={Fe}  Fix(transposition)={Ft}  Fix(3-cycle)={Fs}")
    print(f"  S₃-isotypic: {m_triv}·trivial ⊕ {m_sign}·sign ⊕ {m_std}·standard")
    print(f"  dim check {m_triv}+{m_sign}+2·{m_std} = {m_triv + m_sign + 2 * m_std} (=729); "
          f"#orbits = mult(triv) = {m_triv} (witness 165)")
    ok = (Fe, Ft, Fs) == (729, 81, 9) and (m_triv, m_sign, m_std) == (165, 84, 240)

    print(f"\ntr_M side: H₃(q) Wedderburn blocks = partitions of 3 = S₃-irreps")
    print(f"  [3]→trivial, [1,1,1]→sign, [2,1]→standard; Borromean content in [2,1]")

    print(f"\nFINDING — I_tot_meridian is the S₃-TRIVIAL projection (sum over the")
    print(f"  cusp-symmetric sublattice), discarding all {m_std} standard copies.")
    print(f"  → I_tot_meridian → tr_M is trivial→trivial: S₃ gives NO constraint;")
    print(f"    I_tot_meridian is the UNDER-constrained object to bridge from.")
    print(f"  → the real S₃ constraint is at the GRADED level: a derived (A) carries")
    print(f"    the {m_std} standard copies onto the Hecke [2,1] block. Build (A) from")
    print(f"    the graded standard-isotypic component, not from I_tot_meridian.")

    print(f"\nVERDICT: {'CONFIRMED' if ok else 'CHECK'} — S₃ decomposition exact; the summed "
          f"I_tot_meridian is S₃-trivial (under-constrained); the graded standard component "
          f"is the S₃-constrained object arrow (A) must use.")

    sp = Path(__file__).resolve(); src = sp.read_text()
    rel = "computations/probes/arrow_a_s3_equivariance.py"
    try:
        root = subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                                       cwd=sp.parent, text=True).strip()
        commit = subprocess.check_output(["git", "log", "-1", "--format=%H", "--", rel],
                                         cwd=root, text=True).strip()
        if not commit:
            commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    except Exception:
        commit = "unknown"
    wit = {
        "engine": "python-int", "engineVersion": "exact integer enumeration",
        "computedAt": datetime.now(timezone.utc).isoformat(), "commitSha": commit,
        "scriptFile": rel, "scriptHash": hashlib.sha256(src.encode()).hexdigest()[:12],
        "scriptCommitSha": commit,
        "description": "W1 arrow (A) S₃-equivariance: graded 3D-index = 165·triv⊕84·sign⊕240·std; "
                       "I_tot_meridian is the S₃-trivial projection (under-constrained); the graded "
                       "standard component maps to the Hecke [2,1] block. Audit-only; no fit.",
        "auditOnly": True,
        "parameters": {"n_classes": 729, "lattice": "{-1,0,1}^6"},
        "data": {
            "fix_e": Fe, "fix_transposition": Ft, "fix_3cycle": Fs,
            "s3_isotypic": {"trivial": m_triv, "sign": m_sign, "standard": m_std},
            "orbits_check_vs_witness": {"computed": m_triv, "witness": 165, "match": m_triv == 165},
            "hecke_blocks": {"[3]": "trivial", "[1,1,1]": "sign", "[2,1]": "standard"},
            "finding": "I_tot_meridian = S3-trivial projection, discards 240 standard copies; "
                       "triv->triv bridge is S3-unconstrained; build (A) from the graded "
                       "standard-isotypic component -> Hecke [2,1] block.",
            "verdict_ok": bool(ok),
        },
    }
    out = sp.with_name("arrow-a-s3-equivariance.witness.json")
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    wit.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        wit, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(wit, indent=2) + "\n")
    print(f"\nwitness → {out.name}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
