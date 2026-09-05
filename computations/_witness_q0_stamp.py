"""Stamp `q0Anchor`/`q0Value` onto a HAND-ROLLED witness payload.

Bean `1j39` / `cmiy`, measured 2026-08-28.

WHY THIS EXISTS
---------------
`WitnessBuilder.build()` has called `resolve_q0_anchor_payload_first` since
`9d52483f5`, so every builder-based producer stamps itself on its next run. The
~1100 stamped witnesses in the corpus got there that way, and an unstamped one
from a builder producer is merely stale — regeneration fixes it.
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

**A producer that hand-rolls `json.dump` never reaches `build()`, so it never
stamps, and re-running it never will.** That is the one unstamped class
regeneration cannot fix.

🛑 CORRECTED 2026-08-28, same day this file landed. It read:

    "Every one of the 169 is from a hand-rolled producer."
    "That is the one unstamped class regeneration cannot fix."

applying the second sentence to the whole class. **Both are wrong about most
of it.** Re-measured with the extraction traps fixed (see below), of 120 named
producers only **17 hand-roll**; **62 use `WitnessBuilder` already** and their
witnesses are merely STALE — re-running them does stamp. The claim was wrong
about roughly four fifths of the population it described.

Do not restate the split from here either. It is computed by
[`audits/unstamped_q0_portability_split.py`](audits/unstamped_q0_portability_split.py),
which reports four buckets and what closes each: producer GONE (nothing to
port), producer uses WitnessBuilder (RE-RUN), producer HAND-ROLLS (this
helper), producer UNNAMED (no attribution to port). Run it; the number moved
within a single day the last time it was written down.

Two extraction traps produced wrong counts before that script settled, both of
which bit here — check them before trusting any figure about this class:

  1. `scriptFile` is **top-level**, not under a `witness` block. Reading
     `payload["witness"]["scriptFile"]` reports 0 named against a true 124.
  2. `scriptFile` holds a **bare basename**, not a repo-relative path.
     `Path(sf).exists()` then reads as "producer deleted" for 121 of 124,
     against a true 41.

What survives unchanged: every witness in the class already carries its pin
under a key `_Q0_FIELDS` knows, and nothing consults it.

WHY A STAMP RATHER THAN THE FULL `WitnessBuilder` PORT
-------------------------------------------------------
`1j39` proposes porting the producers to `WitnessBuilder`, and that remains the
right end state — it is bean `cmiy`, ~133 scripts, deliberately deferred. But
the port is a per-file refactor: a hand-rolled payload is an arbitrary dict, and
reshaping it into `add_data`/`add_assertion` calls rewrites the witness file's
structure. That is a large diff per producer.

This helper separates the two. It adds ONLY the two provenance keys and touches
nothing else in the payload, so:

  * no number moves, and no key is renamed or reordered;
  * the diff on each witness is exactly two added lines.

**Its scope is bucket C only** — the hand-rolled producers the split script
names. It is the wrong tool for bucket B: those already build through
`WitnessBuilder`, so adding a manual stamp beside `build()` would duplicate
what `build()` does on the next run. Re-run those instead.

It is NOT a substitute for `cmiy`. A stamped hand-rolled witness still lacks the
`environment`, `scriptHash`, `commitSha` and `precisionMetadata` blocks that
`WitnessBuilder` supplies. It closes the q0-provenance hole specifically, which
is what blocks the `qou-1c4y` migration from being verifiable.

USAGE
-----
    from _witness_q0_stamp import stamp_q0
    ...
    stamp_q0(witness, __file__)          # mutates in place, before json.dump
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as fh:
        json.dump(witness, fh, indent=1)
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import MutableMapping, Union

_REPO = Path(__file__).resolve().parent.parent
_SUBSTRATE = _REPO / "tools" / "qou-substrate" / "python"
if str(_SUBSTRATE) not in sys.path:
    sys.path.insert(0, str(_SUBSTRATE))


def _find_pin(node, depth: int = 0):
    """The q₀ the payload itself records, or None.

    Depth-limited to 3, matching the corpus measurement that found all 169
    resolvable-but-unstamped witnesses carry their pin at depth <= 3. A deeper
    match is more likely to be a recorded reference value in a data table than
    the pin the producer computed at, and stamping off one would be the same
    fabrication this guards against.
    """
    if depth > 3:
        return None
    if isinstance(node, dict):
        try:
            from qou_substrate.witness import _Q0_FIELDS
        except Exception:  # noqa: BLE001
            return None
        for k, v in node.items():
            if k in _Q0_FIELDS and isinstance(v, str) and v.startswith("1.1"):
                return v
        for v in node.values():
            found = _find_pin(v, depth + 1)
            if found is not None:
                return found
    return None


def stamp_q0(payload: MutableMapping, script_path: Union[str, "os.PathLike[str]"]) -> bool:
    """Add `q0Anchor` / `q0Value` to `payload`, in place. Returns whether it did.

    Payload-evidence-first, via the same resolver `WitnessBuilder.build()` uses,
    so a hand-rolled witness gets exactly the stamp a builder-based one would.
    That matters: `resolve_q0_anchor` alone consults the manifest and env var,
    which describe what the producer was *configured* to do rather than what it
    *did*, and those disagree systematically (85 producers read the muon anchor's
    definition directly while the manifest hands them proton — bean `qou-aj91`).
    Reading the payload first is what makes the stamp a statement about the
    numbers actually present.

    An EXISTING `q0Anchor` is never overwritten: a producer that already declares
    its anchor has said something deliberate, and silently replacing it would be
    the layer straddle this is meant to expose.

    Returns False, without raising, when the anchor cannot be determined — a
    payload with no recognisable pin, or a `qou_substrate` that will not import.
    A probe must not die because its provenance could not be labelled.
    """
    if "q0Anchor" in payload:
        return False
    try:
        from qou_substrate.witness import (
            _Q0_FIELDS,
            resolve_q0_anchor_payload_first,
        )
    except Exception:  # noqa: BLE001 — provenance is not worth killing a probe over
        return False

    # REQUIRE PAYLOAD EVIDENCE. `resolve_q0_anchor_payload_first` consults the
    # payload first but FALLS BACK to the manifest/env when the payload carries
    # no pin — measured: `{"zzz": 1}` resolves to ("proton", <proton pin>).
    #
    # That fallback is right for `WitnessBuilder`, which knows what q₀ the
    # producer was handed. It is WRONG here. A hand-rolled payload with no pin
    # is a payload we have no evidence about, and stamping the manifest default
    # onto it would assert a layer its numbers may not belong to — with a
    # provenance field vouching for the assertion. That is the straddle this
    # helper exists to expose, manufactured by the tool meant to reveal it.
    #
    # So an unstampable witness stays unstamped, which is honest and visible.
    if _find_pin(payload) is None:
        return False

    try:
        anchor, q0_value = resolve_q0_anchor_payload_first(payload, script_path)
    except Exception:  # noqa: BLE001
        return False
    if not anchor:
        return False
    payload["q0Anchor"] = anchor
    if q0_value:
        payload["q0Value"] = q0_value
    return True
