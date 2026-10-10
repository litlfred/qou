#!/usr/bin/env python3
"""Detect the DECOY-HYPOTHESIS shape in Lean carriers (bean `qou-qcy6`).

A carrier declares

    P       : Prop            -- the decoy: the instance chooses what it means
    active  : P               -- ...and proves it
    impl_x  : P -> C          -- one or more implications INTO the conclusions

An instance must supply both `active : P` and `impl_x : P -> C`, so it must
supply `C`.  The conclusion therefore holds in every instance -- the class is
NOT unsatisfiable.  The defect is that the decoy carries no information: a class
asserting `C` outright is interderivable, so a theorem proved as
`ctx.impl_x ctx.active` derives nothing.  Machine-checked in
`scripts/lean/probes/decoy-hypothesis-eliminable.lean` (exit 0).

Why `proof-no-self-assuming-projection` cannot see it: that criterion wants a
proof term that IS a projection, `ctx.field`.  Here it is `ctx.field ctx.other`
-- an APPLICATION.  The arrow is what makes it read as a derivation from a
stated hypothesis, and what hides it.

Candidates, not verdicts.
"""
import re
import sys
import pathlib

sys.path.insert(0, "scripts/lib")
from lean_decl_scan import blank_comments  # noqa: E402

CARRIER = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*"
    r"(class|structure)\s+([A-Za-z_][A-Za-z0-9_'.]*)"
)
# `(.*)` not `(.+?)`: a field whose type begins on the NEXT line writes
# `name :` with nothing after the colon.  Requiring one character there made
# such a line fail to match, so it fell through to the continuation branch and
# was appended to the PRECEDING field -- swallowing the `impl_` field this
# detector exists to find.  Measured: that bug hid
# `KnotParticleGenerationContext`, the class machine-checked in
# `scripts/lean/probes/decoy-hypothesis-eliminable.lean`.
FIELD = re.compile(r"^\s+([A-Za-z_][A-Za-z0-9_']*)\s*:\s*(.*)$")


def carriers(path):
    """Yield (name, line, {field: type}) for each carrier in the file.

    Field types are JOINED ACROSS CONTINUATION LINES.  A field whose type starts
    on the next line -- common for the wide `impl_` implications this detector
    exists to find -- otherwise parses with an empty type and is silently
    dropped.  Measured: without this, `KnotParticleGenerationContext` (the very
    class machine-checked in `scripts/lean/probes/decoy-hypothesis-eliminable.lean`)
    was ABSENT from the results, and the count read 12 instead of the true
    figure.  A detector that misses its own worked example is wrong; that is how
    this was caught.
    """
    lines = blank_comments(path.read_text(encoding="utf-8", errors="replace")).split("\n")
    cur = None
    start = 0
    fields = {}
    last = None
    for i, ln in enumerate(lines):
        m = CARRIER.match(ln)
        if m:
            if cur:
                yield cur, start, fields
            cur, start, fields, last = m.group(2), i + 1, {}, None
            continue
        if cur is None:
            continue
        if ln.strip() and not ln[0].isspace():
            yield cur, start, fields
            cur, fields, last = None, {}, None
            continue
        f = FIELD.match(ln)
        if f:
            last = f.group(1)
            fields[last] = f.group(2)
        elif last and ln.strip():
            # continuation of the previous field's type
            fields[last] = (fields[last] + " " + ln.strip()).strip()
    if cur:
        yield cur, start, fields


hits = []
for p in sorted(pathlib.Path("folio").rglob("*.lean")):
    for name, line, fields in carriers(p):
        props = {n for n, t in fields.items() if t.strip() == "Prop"}
        if not props:
            continue
        for prop in props:
            proofs = [n for n, t in fields.items() if t.strip() == prop]
            impls = [n for n, t in fields.items()
                     if re.match(rf"^{re.escape(prop)}\s*(→|->)", t.strip())]
            if proofs and impls:
                hits.append((str(p), line, name, prop, proofs, impls))

print(f"DECOY-HYPOTHESIS candidates: {len(hits)}  across "
      f"{len({h[0] for h in hits})} files\n")
for f, line, name, prop, proofs, impls in hits:
    print(f"  {name}.{prop}  ({len(impls)} impl field(s))   {f.split('/')[-1]}:{line}")
    print(f"      proof={proofs[0]}  impls={', '.join(impls)}")

# --- self-test -------------------------------------------------------------
# The class machine-checked in `scripts/lean/probes/decoy-hypothesis-eliminable.lean`
# MUST appear.  It is the worked example, so a run that omits it is measuring
# the parser rather than the corpus -- which is exactly what happened twice
# while this script was being written (12 candidates, then 11, against a true
# 17).  Both times the count looked plausible and nothing announced the loss.
_ANCHOR = "KnotParticleGenerationContext"
if not any(h[2] == _ANCHOR for h in hits):
    print(f"\nSELF-TEST FAILED: {_ANCHOR} absent — the parser is dropping "
          f"fields, not the corpus lacking the shape. Do NOT quote this count.",
          file=sys.stderr)
    sys.exit(1)
print(f"\nself-test OK: {_ANCHOR} present (the machine-checked worked example)")

