#!/usr/bin/env python3
"""Which producers hardcode a q0 pin, and does it CONTRADICT their declaration?

Written after a grep-shaped claim of mine went wrong twice in the same hour,
in opposite directions. Both failures are cheap to repeat, so the checker
exists to make the answer measured rather than re-guessed.

**Failure 1 -- a grep counts comments.** `grep -l <muon literal>` reported 255
files and I read that as 255 defects. 33 of them mention the literal only in a
comment or docstring; the clearest case,
`deltalambda/t25_cinquefoil_deltalambda_sign_probe.py`, was a producer a prior
agent had ALREADY fixed to fail loudly, whose comment quotes the muon constant
while describing the behaviour it removed. A detector that reads prose as code
turns a fix into a finding.

**Failure 2 -- a comment is not the gate.** I then reported "78 under a proton
comment" as though 78 witnesses were mis-anchored. What decides a witness's
anchor is the `q0_anchor_manifest.json` DECLARATION, not the comment beside the
constant. Measured against declarations: of 407 declared producers, 23 carry a
muon literal in executable code and exactly **1** could not resolve
`q_parameter` -- and that one was the already-fixed probe above. The acute
"declared proton, computes muon" population is **0**, not 78.

So this reports three separate populations and refuses to conflate them:

  CONTRADICTS  a DECLARED producer whose pin literal disagrees with its
               declaration AND whose `q_parameter` import cannot resolve, so
               the literal is genuinely reached. This is the only defect
               class -- it manufactures a false `Q0_OK`.
  UNDECLARED   carries a pin literal but is absent from the manifest. Its
               witness lands `Q0_ANCHOR_MISSING`, a tolerated and visible
               state. Moving these to the proton pin is migration scope
               (`qou-1c4y`), NOT a flip.
  PROSE_ONLY   mentions a pin literal only in a comment or docstring. Not a
               finding. Frequently the OPPOSITE of one -- a note recording a
               fix.

Why `q_parameter` resolution is the deciding test rather than the literal's
presence: `q_parameter` lives in `computations/substrate/`, so a bare
`from q_parameter import q_at` does not resolve when a producer runs
standalone. A producer that reaches it computes at the canonical pin and its
literal is dead code; one that cannot reach it falls through to the literal.
`e_hartree_round24_molecular_reuse` was a real instance of the latter -- fixed
by importing `_path_bridge`, not by editing the constant, because a resolved
`q_at()` cannot go stale while a literal can.

Exit 1 on any CONTRADICTS. The other two counts are reported, never enforced.
"""
from __future__ import annotations

import io
import json
import pathlib
import subprocess
import sys
import time
import tokenize

_HERE = pathlib.Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))
sys.path.insert(0, str(_ROOT / "computations"))

PINS = {
    "muon": "1.1099785955573347",
    "proton": "1.1099785827513808",
}


def strip_comments_and_docstrings(src: str) -> str:
    """Return `src` with comments and docstrings removed.

    The whole point of the checker: a literal quoted in a comment that
    documents a REMOVED behaviour is the opposite of a defect.
    """
    out = io.StringIO()
    try:
        toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return src  # unparseable: fall back to raw, over-reporting not under-
    prev_end = (1, 0)
    last = None
    for tt, tv, start, end, _line in toks:
        if tt == tokenize.COMMENT:
            continue
        if tt == tokenize.STRING and last in (
                None, tokenize.INDENT, tokenize.NEWLINE, tokenize.NL):
            continue
        if start[0] > prev_end[0]:
            out.write("\n" * (start[0] - prev_end[0]))
            prev_end = (start[0], 0)
        out.write(" " * max(0, start[1] - prev_end[1]))
        out.write(tv)
        prev_end = end
        last = tt
    return out.getvalue()


_PROBE = (
    "import sys, os\n"
    "sys.path.insert(0, os.path.dirname(sys.argv[1]))\n"
    "try:\n"
    "    from q_parameter import q_at\n"
    "    print('OK')\n"
    "except Exception:\n"
    "    print('FAIL')\n"
)


def q_parameter_resolves(path: str) -> bool:
    """Can this file reach `q_parameter` as it is actually invoked?"""
    src = pathlib.Path(path).read_text(errors="replace")
    if "_path_bridge" in strip_comments_and_docstrings(src):
        return True
    try:
        out = subprocess.run([sys.executable, "-c", _PROBE, path],
                             capture_output=True, text=True,
                             timeout=60).stdout.strip()
    except subprocess.SubprocessError:
        return False
    return out == "OK"


def declared_anchor(path: str):
    from qou_substrate.witness import (  # noqa: PLC0415
        q0_anchor_is_declared, resolve_q0_anchor,
    )
    try:
        if not q0_anchor_is_declared(path):
            return None
        return resolve_q0_anchor(path)[0]
    except Exception:  # noqa: BLE001
        return None


def main() -> int:
    t0 = time.monotonic()
    literals = "|".join(p.replace(".", r"\.") for p in PINS.values())
    files = subprocess.run(
        ["grep", "-rlE", literals, "--include=*.py", "computations", "tools"],
        cwd=_ROOT, capture_output=True, text=True).stdout.split()

    contradicts, undeclared, prose_only, consistent = [], [], [], []
    for rel in files:
        path = str(_ROOT / rel)
        src = pathlib.Path(path).read_text(errors="replace")
        code = strip_comments_and_docstrings(src)
        found = {name for name, lit in PINS.items() if lit in code}
        if not found:
            prose_only.append(rel)
            continue
        anchor = declared_anchor(path)
        if anchor is None:
            undeclared.append(rel)
            continue
        # A declared producer whose literal matches its declaration is fine
        # whether or not the literal is reached.
        if anchor in found and len(found) == 1:
            consistent.append(rel)
            continue
        # Disagreement only bites when the literal is actually REACHED.
        if q_parameter_resolves(path):
            consistent.append(rel)
        else:
            contradicts.append({"file": rel, "declared": anchor,
                                "literals_in_code": sorted(found)})

    print("q₀ hardcoded-pin audit")
    print("=" * 62)
    print(f"  files mentioning a pin literal : {len(files)}")
    print(f"  PROSE_ONLY  (not a finding)    : {len(prose_only)}")
    print(f"  UNDECLARED  (migration scope)  : {len(undeclared)}")
    print(f"  consistent / literal not reached: {len(consistent)}")
    print(f"  CONTRADICTS (defect)           : {len(contradicts)}")
    for row in contradicts:
        print(f"    declared={row['declared']:7} carries="
              f"{','.join(row['literals_in_code']):8} {row['file']}")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    w = WitnessBuilder("q0-hardcoded-pin-audit", engine="python",
                       start_time=t0)
    w.set_description(
        "Producers hardcoding a q₀ pin literal, split three ways: CONTRADICTS "
        "(declared anchor disagrees with a literal the producer actually "
        "reaches — the only defect class), UNDECLARED (no manifest entry, so "
        "Q0_ANCHOR_MISSING; migration scope qou-1c4y), and PROSE_ONLY "
        "(literal appears only in a comment/docstring — frequently a note "
        "recording a FIX, which a raw grep misreads as a finding)."
    )
    w.add_data("counts", {
        "files_mentioning_literal": len(files),
        "prose_only": len(prose_only),
        "undeclared": len(undeclared),
        "consistent_or_unreached": len(consistent),
        "contradicts": len(contradicts),
    })
    w.add_data("contradicts", contradicts)
    w.add_data("undeclared", sorted(undeclared))
    w.add_data("prose_only", sorted(prose_only))
    w.add_assertion(
        name="no_declared_producer_reaches_a_contradicting_pin_literal",
        # Counts are exact integers -- passing them as floats would put three
        # raw float64 fields into the witness and trip the NO-FLOAT64 ratchet.
        computed=len(contradicts), expected=0, tolerance=0,
        source="a reached literal disagreeing with the manifest declaration "
               "manufactures a false Q0_OK",
    )
    print(f"Witness: {w.save()}")
    return 1 if contradicts else 0


if __name__ == "__main__":
    raise SystemExit(main())
