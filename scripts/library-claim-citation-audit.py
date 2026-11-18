#!/usr/bin/env python3
"""
library-claim-citation-audit — verify that citations in a folio link to the
specific result/claim in the ingested paper (`library/<doc-id>/blocks/<block-id>`
or `<doc-id>#<kind>:<number>`), and that every cited mathematical claim is
Lean-proved (here or in Mathlib) with zero `sorry`/`axiom` — or flagged to be
proved in Lean.

Usage:
    python3 scripts/library-claim-citation-audit.py [--root <folio-root>] [--json] [--limit N]
"""

from __future__ import annotations

import os
import runpy
import sys

TOOLS_SCRIPT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "folio-assistant",
    "cat-harness-tools",
    "scripts",
    "library-claim-citation-audit.py",
)

if __name__ == "__main__":
    if os.path.exists(TOOLS_SCRIPT):
        runpy.run_path(TOOLS_SCRIPT, run_name="__main__")
    else:
        sys.stderr.write(f"missing {TOOLS_SCRIPT}\n")
        sys.exit(2)
