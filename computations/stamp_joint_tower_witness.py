#!/usr/bin/env python3
"""Stamp provenance onto the Rust joint-tower-sdp witness.

This is the missing half of a two-step producer, restored as code.

`tools/hecke-engine/src/bin/joint-tower-sdp` emits the certificate payload but
cannot stamp the corpus's provenance fields: it does not know its own source
path, the git head, or how `qou_substrate` classifies a q0 anchor. On `main`
those fields were present anyway --

    scriptFile  scriptHash  scriptCommitSha  commitSha  q0Anchor  durationMs

-- put there by a step that exists nowhere in the tree, alongside the
truncation that is now `--truncate-for-repo`. Both halves were uncommitted, and
`scriptCommitSha: "unknown"` on the committed witness is the fingerprint of
that: a stamper that could not resolve the file it was stamping.

Regenerating without this would silently DROP six provenance fields, so the
"reproducible" witness would be a regression on the unreproducible one.

Usage (the second half of the command in `computations/README.md`):

    python3 computations/stamp_joint_tower_witness.py \
        computations/joint-tower-sdp-rust.witness.json

Idempotent: re-stamping refreshes the hashes and timestamp, nothing else.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))

from qou_substrate.witness import WitnessBuilder  # noqa: E402

#: The Rust producer, relative to the repo root. `scriptHash` is the hash of
#: THIS file, so an edit to the emitter shows up as witness staleness exactly
#: as it would for a Python producer.
PRODUCER = ROOT / "tools" / "hecke-engine" / "src" / "bin" / "joint_tower_sdp.rs"

#: The two pins a q0 can legitimately be. Neither is the producer's default.
_PINS = {
    "1.1099785827513808": "physical_proton",
    "1.1099785955573347": "ideal_muon",
}


def q0_anchor_reason(q: float | None, anchor: str) -> str:
    """Say WHAT is undetermined, not merely that something is.

    `q0_anchor_consistency_audit` flags this witness with: *"anchor=ambiguous
    with no q0AnchorReason -- states that the pin is undetermined, but not WHAT
    is undetermined, so nothing records how it could ever be resolved."* That is
    a fair criticism and it is fixable here rather than by widening the audit's
    tolerance. The committed witness on `main` carries the bare `"ambiguous"`
    with no reason; this supplies one.
    """
    if anchor != "ambiguous":
        return (f"producer evaluates at the {anchor} pin; q_0 = {q} matches it "
                f"to within 1e-12 relative")
    if q is None:
        return "witness records no q_0_numeric, so no anchor can be resolved"
    prot = float("1.1099785827513808")
    ppm = abs(prot - q) / prot * 1e6
    return (
        f"q_0 = {q} matches NEITHER canonical pin: it is {ppm:.0f} ppm from the "
        f"proton pin 1.1099785827513808 and a comparable distance from the muon "
        f"pin 1.1099785955573347, so it is not an evaluation at either layer. "
        f"This is the producer's hardcoded default (--q0), not a substrate "
        f"determination. RESOLVABLE by re-running with `--q0 <pin>`; the "
        f"resulting eigenvalues would move, which is why it is not done "
        f"silently. Until then the numeric half is a shape check, not a value "
        f"-- see the witness's `deprecated.reason`."
    )


def classify_q0(q: float | None) -> str:
    """Name the anchor, or say the modulus is neither pin.

    The committed witness carries `q0Anchor: "ambiguous"`, and that is correct
    rather than a gap: the producer's default `q_0 = 1.1097` is **251 ppm** from
    the canonical proton pin, so it is not an evaluation at either layer. This
    recomputes the classification instead of copying the old string forward, so
    a future run at a real pin gets labelled as one.
    """
    if q is None:
        return "ambiguous"
    for pin, name in _PINS.items():
        # Compare at the width the witness records. A pin agreeing to 1e-12
        # relative IS that pin; 1.1097 agrees with neither to 1e-4.
        if abs(float(pin) - q) <= 1e-12 * abs(float(pin)):
            return name
    return "ambiguous"


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    path = Path(argv[1]).resolve()
    payload = json.loads(path.read_text())

    anchor = classify_q0(payload.get("q_0_numeric"))
    WitnessBuilder.stamp_staleness_metadata(
        payload,
        script_path=PRODUCER,
        engine="rust",
        engine_version=f"hecke-engine {payload.get('engine', {}).get('version', '?')}",
        q0_anchor=anchor,
    )
    payload["q0AnchorReason"] = q0_anchor_reason(payload.get("q_0_numeric"), anchor)
    # `engine` is an OBJECT here (name/version/language), not the string the
    # stamper writes. Restore the producer's own richer value rather than let
    # provenance stamping flatten it -- the same downgrade the stamper's own
    # docstring warns about for `sympy+mpmath`.
    payload["engine"] = json.loads(path.read_text()).get("engine", "rust")
    payload["scriptFile"] = PRODUCER.name

    path.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"stamped {path.name}")
    print(f"  scriptFile       {payload['scriptFile']}")
    print(f"  scriptHash       {payload['scriptHash']}")
    print(f"  scriptCommitSha  {payload['scriptCommitSha']}")
    print(f"  commitSha        {payload['commitSha']}")
    print(f"  q0Anchor         {payload['q0Anchor']}  (q_0 = {payload.get('q_0_numeric')})")
    print(f"  q0AnchorReason   {payload['q0AnchorReason'][:76]}…")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
