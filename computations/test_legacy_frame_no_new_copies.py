#!/usr/bin/env python3
"""Guard: the legacy-marshalled frame stays in ONE named place — bean `qou-iu3m`.

`canonical_braid_marshalling.marshal_to_chi_lambda_braid` drops the crossing
`d`. For a nucleon chain that silently replaces `z - h/2` by `z` at the two
intra-nucleon `averaged` crossings, so a trace built on it differs from the
true one by 15.3 % (proton) / 27.3 % (neutron).

Some scripts NEED that frame: they compare a closed form against an empirical
slow path which is itself bound to `chi_lambda_braid`, and both sides of such
a comparison must sit in one frame. Those callers are correct and must not be
"fixed" (see `legacy_marshalled_frame`).

What is NOT correct is the frame living in anonymous local copies. It did, in
three places, two of them named after the canonical helper while returning
different numbers — and that invisibility is precisely why the `qou-qu2w`
defect went unnoticed: there was no single place saying "this frame is lossy",
so fixing one copy told you nothing about the others.

This test does not forbid using the legacy frame. It forbids using it WITHOUT
SAYING SO — i.e. calling the raw marshaller from a file that has not imported
the named module. Adding a caller is then a visible choice.

Run: python3 computations/test_legacy_frame_no_new_copies.py
"""
from __future__ import annotations

import ast
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

RAW = "marshal_to_chi_lambda_braid"
NAMED_MODULE = "legacy_marshalled_frame"

#: Files allowed to call the raw marshaller directly, with the reason.
#: Entries DRAIN, never grow — route a new caller through the named module.
RAW_CALLER_BASELINE: dict[str, str] = {
    "legacy_marshalled_frame.py": "the one named home; wraps it deliberately",
    "constit_factor_varying_q_phase5k2.py":
        "marshals the FULL atom word, not a nucleon chain — a different use "
        "of the same marshaller, and it names the frame in-file",
}


def _calls_raw(tree: ast.AST) -> bool:
    """True if the module actually CALLS the marshaller (not merely names it).

    Keyed on a call, not a substring: every one of these files mentions the
    marshaller in prose explaining the frame, and a substring check would
    flag the explanations along with the uses.
    """
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            name = getattr(f, "id", None) or getattr(f, "attr", None)
            if name == RAW:
                return True
    return False


def main() -> int:
    offenders: list[str] = []
    stale: list[str] = []
    named: list[str] = []
    seen: set[str] = set()

    for path in sorted(HERE.rglob("*.py")):
        rel = path.relative_to(HERE).as_posix()
        if "_deprecated/" in rel or rel == Path(__file__).name:
            continue
        try:
            src = path.read_text(encoding="utf-8", errors="replace")
            tree = ast.parse(src)
        except (OSError, SyntaxError):
            continue
        if not _calls_raw(tree):
            continue
        base = Path(rel).name
        seen.add(base)
        if base in RAW_CALLER_BASELINE:
            continue
        if NAMED_MODULE in src:          # named the frame: visible choice, fine
            named.append(rel)
            continue
        offenders.append(rel)

    stale = [k for k in RAW_CALLER_BASELINE if k not in seen]

    print("Legacy-marshalled frame — raw-marshaller callers")
    for base, why in sorted(RAW_CALLER_BASELINE.items()):
        mark = "ok  " if base in seen else "note"
        print(f"  {mark} {base}: {why}")
    for f in sorted(named):
        print(f"  ok   {f}: calls it directly but imports `{NAMED_MODULE}`, "
              f"so the frame is named in-file")
    for f in stale:
        print(f"  note baseline entry no longer needed, drop it: {f}")

    if offenders:
        print(f"\nFAIL ({len(offenders)}):")
        for f in offenders:
            print(f"  ✗ {f} calls {RAW}() without importing `{NAMED_MODULE}`.")
            print(f"    That marshaller DROPS the crossing `d`. If you need the")
            print(f"    legacy frame, import `{NAMED_MODULE}` so the choice is")
            print(f"    greppable; if you do not, use the canonical helper.")
        return 1

    print(f"\nPASS -- the legacy frame has one named home "
          f"({len(seen)} raw caller(s): {len(RAW_CALLER_BASELINE)} baselined, "
          f"{len(named)} self-declaring)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
