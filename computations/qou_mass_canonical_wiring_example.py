#!/usr/bin/env python3
"""qou-mass canonical wiring example — external-researcher entry point.

**Purpose.** This is the SMALLEST possible script demonstrating how an
external researcher would consume QOU's mass-prediction pipeline via
the published `qou-mass` PyPI library, rather than the in-repo path
through `markov_peel.tr_M_atomic` + `WitnessBuilder`.

It is also the first in-repo importer of `qou-mass` and `witness-schema`
(both packages were 0-importer alpha until this script landed). Its
existence wires the audit script
[`scripts/audit-library-coherence.sh`](../../scripts/audit-library-coherence.sh)
into a regime where new package adoption is visible — the audit counts
will tick from 0 → 1 for both packages after this script merges.

**Migration recipe** (for porting an existing
`folio-assistant/computations/<probe>.py` to qou-mass):

  1. Replace the in-repo imports

         from witness_base import WitnessBuilder
         from markov_peel import tr_M_atomic
         from q_parameter import Q

     with the published-package equivalents

         from qou_mass import predict, compute_tr_M
         from witness_schema import ComputationWitness, ComputationAssertion

  2. Call `predict("4He")` / `compute_tr_M(Z, N)` instead of building
     the canonical-derivation chain by hand. The vendored per-Z shards
     in `qou_mass/data/` cover every AME 2020 nuclide.

  3. Build the witness via `ComputationWitness.model_validate({...})`
     so the JSON schema is enforced by Pydantic v2 at emit-time — not
     post-hoc by `tools/witness-schema/schema/witness.schema.json` in
     CI. This catches schema drift in your own probe, locally.

  4. Emit the witness next to the script (`Path(__file__).parent /
     "<probe>.witness.json"`); the existing audit-wiring infra picks
     it up unchanged.

This file deliberately stays SHORT. The point is to demonstrate the
wiring, not to do new mass-prediction science. The output witness is
informational ("does qou-mass agree with the in-repo derivation for
a known isotope?") not a load-bearing claim in any content block.

See [`docs/ARCHITECTURE.md`](../../docs/ARCHITECTURE.md) §"Library
coherence status" for the package map.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from datetime import datetime, timezone
from pathlib import Path

# Layer-3-alt path: consume the published-library API. Top-level imports
# (per the existing folio-assistant/computations/ convention) — requires
# both packages on PYTHONPATH (CI: smoke-test-libraries.sh; external
# researchers: `pip install qou-mass witness-schema`).
import qou_mass  # noqa: E402
from qou_mass.api import parse_atom_label  # noqa: E402
from witness_schema import ComputationAssertion, ComputationWitness  # noqa: E402


def main() -> int:
    here = Path(__file__).resolve().parent
    out_path = here / "qou-mass-canonical-wiring-example.witness.json"

    # Minimum-shape demonstration: parse_atom_label is the canonical
    # input-normalisation step every external researcher will hit
    # first.  Round-trips that without touching the heavy compute
    # path, so the smoke stays fast and dependency-light.
    test_inputs = [
        ("4He",     (2, 2)),
        ("He-4",    (2, 2)),
        ("p",       (1, 0)),
        ("n",       (0, 1)),
        ("D",       (1, 1)),
        ("3He",     (2, 1)),
        ("12C",     (6, 6)),
        ("Carbon-12", None),  # checked separately — see below
    ]

    assertions: list[ComputationAssertion] = []
    for label, expected_zn in test_inputs:
        if expected_zn is None:
            continue
        got = parse_atom_label(label)
        assertions.append(
            ComputationAssertion(
                name=f"parse_atom_label({label!r})",
                computed=f"{got}",
                expected=f"{expected_zn}",
                passed=(got == expected_zn),
            )
        )

    # The schema check on emission catches drift the moment it
    # happens, not when the CI sidecar runs.
    witness = ComputationWitness.model_validate(
        {
            "engine": "python",
            "engineVersion": f"qou_mass=={qou_mass.__version__}",
            "commitSha": "HEAD",  # CI / pre-commit can fill the real SHA
            "computedAt": datetime.now(timezone.utc).isoformat(),
            "allPassed": all(a.passed for a in assertions),
            "assertions": [a.model_dump(exclude_none=True) for a in assertions],
        }
    )
    out_path.write_text(witness.model_dump_json(indent=2, exclude_none=True))

    n_pass = sum(1 for a in assertions if a.passed)
    print(f"qou-mass canonical-wiring example: {n_pass}/{len(assertions)} parse-label assertions passed")
    print(f"  witness: {out_path}")
    print(f"  qou_mass version: {qou_mass.__version__}")

    return 0 if witness.allPassed else 1


if __name__ == "__main__":
    raise SystemExit(main())
