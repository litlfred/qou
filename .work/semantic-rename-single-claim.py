#!/usr/bin/env python3
"""Rename single `claim : Prop` → `claim_<block_name>` based on file's
namespace + block title.

For each .lean file with a single `claim : Prop` field, extract the
block name from the namespace/theorem name and use it to construct a
semantic identifier.

E.g., `theorem kelvin_dispersion_derivation [ctx] : ctx.claim` →
`theorem kelvin_dispersion_derivation [ctx] : ctx.claim_kelvin_dispersion_derivation`.

Pure cosmetic — improves grep-ability and reader orientation.
"""

from __future__ import annotations

import re
import pathlib
import sys


def upgrade_lean_file(lean_path: pathlib.Path) -> bool:
    text = lean_path.read_text()

    # Detect single `claim : Prop` field (NOT `claim_i, claim_ii, ...`)
    if not re.search(r'^  claim : Prop$', text, re.MULTILINE):
        return False
    if 'ctx.claim' not in text:
        return False

    # Find the theorem name (matches the file's base name in snake_case)
    # Pattern: `theorem <theorem_name> [ctx : ...] : ctx.claim`
    m = re.search(
        r'theorem (\w+) \[ctx : \w+\] : ctx\.claim\b',
        text,
    )
    if not m:
        return False

    theorem_name = m.group(1)
    # The new field name uses the theorem name (already snake_case)
    new_field = f'claim_{theorem_name}'
    # Cap length
    if len(new_field) > 60:
        new_field = new_field[:60].rstrip('_')

    # Rename `claim : Prop` → `claim_<theorem_name> : Prop`
    text = re.sub(
        r'(^  claim)( : Prop$)',
        rf'\1_{theorem_name}\2',
        text, count=1, flags=re.MULTILINE,
    )
    # Rename `ctx.claim` → `ctx.claim_<theorem_name>` (but only the plain ref)
    text = re.sub(
        r'\bctx\.claim\b(?!_)',
        f'ctx.claim_{theorem_name}',
        text,
    )

    lean_path.write_text(text)
    return True


def main() -> int:
    targets = sys.argv[1:]
    if not targets:
        targets = []
        for p in pathlib.Path('content/quantum-observable-universe/lean/QOU').rglob('*.lean'):
            text = p.read_text()
            if re.search(r'^  claim : Prop$', text, re.MULTILINE):
                targets.append(str(p))

    changed = 0
    unchanged = 0
    for tgt in targets:
        p = pathlib.Path(tgt)
        if not p.is_file():
            continue
        if upgrade_lean_file(p):
            changed += 1
        else:
            unchanged += 1

    print(f'Done. {changed} renamed, {unchanged} unchanged.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
