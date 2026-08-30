#!/usr/bin/env python3
"""Find Lean declarations whose FULLY-QUALIFIED name is declared in two or
more modules of the QOU library.

Why this matters. Two modules that declare the same fully-qualified name can
never both be imported: Lean rejects the second with

    error: import M failed, environment already contains 'N' from M'

so every such pair silently partitions the library into two halves that can
never meet. Nothing in the ordinary workflow surfaces it — each module
compiles alone, `grep -c sorry` reads clean, and the break only appears when
some third module finally tries to import both. That is exactly how
`QOU.Archimedean.R_q` (two modules, byte-identical bodies) took 180 modules
off the verified corpus while every one of them still read sorry-free
(beans `qou-lksc`, `qou-kfcl`).

Two-stage by design, because the parser alone is not trustworthy here:

  * PROPOSE (default) — a regex/namespace-stack pass over the tree. Cheap,
    over-reports. Calibration cost the following false-positive classes, each
    found by measurement and each fixed here: an `import` line indented
    inside a docstring; `namespace`/`abbrev` text inside a `/- -/` comment;
    `section ... end` popping the namespace stack; and — the one that
    dominated — a dotted declaration name (`def A5Irrep.dim`) truncated at
    its first component, which manufactured a "duplicate" out of every
    inductive's namespace.
  * VERIFY (`--verify`) — for each proposed pair, write a two-line probe that
    imports both modules and run `lean` on it. A pair is reported only if the
    compiler actually says `environment already contains`. Measured on
    `main` 2026-08-30: 28 proposed pairs, **26 confirmed**, 2 benign.

The verdict is the compiler's. Treat the propose stage as a candidate list.

SCOPE — what this does NOT see. The scan walks
`content/quantum-observable-universe/lean/QOU/` only. Content-block `.lean`
siblings under `content/<paper>/<chapter>/` are a separate surface: they
compile standalone, cannot import one another, and win **candidate 1** of
`lean.ref` resolution ahead of anything in the Lake tree. So a clean run here
is not evidence that a name is unambiguous in the corpus.

That surface is not hypothetical and it overlaps this one. `QOU.Archimedean.T_pp`
is declared three times: `lean/QOU/Archimedean/TransferMatrix.lean` (10
importers), `lean/QOU/Archimedean/beta_decay_transfer_matrix.lean` (0), and
`mass-theory/beta-decay-transfer-matrix.lean` — a content sibling in the SAME
namespace, drifted from the library copy (97 vs 195 lines; `Matrix (Fin 2)
(Fin 2) ℝ` vs a bespoke `TM`). Draining a pair by renaming in the library file
would push a drifted mirror further apart rather than closer, so co-ordinate
with the mirror-drift population (bean `qou-u87j`, `check-mirror-drift.ts`)
before renaming anything that has a content sibling.

Usage:
    python3 scripts/lean-duplicate-fqn-audit.py                 # propose
    python3 scripts/lean-duplicate-fqn-audit.py --verify        # compiler check
    python3 scripts/lean-duplicate-fqn-audit.py --verify --check-baseline
    python3 scripts/lean-duplicate-fqn-audit.py --verify --write-baseline

`--check-baseline` is a ratchet: it fails on any confirmed pair that is not
already in `docs/audits/lean-duplicate-fqn-baseline.json`. The baseline
drains, never grows — a new collision is a defect, not a new normal.

`--verify` needs a LEAN_PATH that resolves the QOU oleans; pass `--lean-path`
or set LEAN_PATH. See AGENTS.md §"VERIFY a single file with lean-direct" —
never `lake build` against a restored olean cache.
"""
from __future__ import annotations

import argparse
import collections
import itertools
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LEANROOT = REPO / "content/quantum-observable-universe/lean"
BASELINE = REPO / "docs/audits/lean-duplicate-fqn-baseline.json"

DECL = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*"
    r"(?:def|abbrev)\s+([A-Za-z_][\w'.]*)"
)
# A `private` declaration's environment name is mangled per module
# (`_private.<module>.0.<Ns>.<name>`), so it can never collide with anything in
# another module -- not with another private of the same name, and not with a
# public one. Excluding it from the propose stage is sound, not a recall loss.
PRIV = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)?(?:\w+\s+)*?private\b")
NS = re.compile(r"^\s*namespace\s+([\w.]+)")
SEC = re.compile(r"^\s*section\b")
END = re.compile(r"^\s*end\b")
IMP = re.compile(r"^import\s+([\w.]+)")   # column 0: a docstring may indent one
LINE_CMT = re.compile(r"--.*$")
# Terminates a declaration body: the next top-level form. Shared with
# scripts/lean-name-surface-audit.py, which compares bodies across surfaces.
STOP = re.compile(
    r"^\s*(?:@\[|namespace\b|end\b|open\b|section\b|variable\b|theorem\b|lemma\b|"
    r"instance\b|structure\b|class\b|inductive\b|example\b|attribute\b|"
    r"(?:private\s+|protected\s+|noncomputable\s+)*(?:def|abbrev)\b)"
)


def strip_block_comments(text: str) -> str:
    """Blank out /- ... -/ (nesting-aware), preserving line structure."""
    out, i, depth, n = [], 0, 0, len(text)
    while i < n:
        if text.startswith("/-", i):
            depth += 1
            out.append("  ")
            i += 2
            continue
        if text.startswith("-/", i) and depth:
            depth -= 1
            out.append("  ")
            i += 2
            continue
        ch = text[i]
        out.append(ch if (depth == 0 or ch == "\n") else " ")
        i += 1
    return "".join(out)


def modname(p: Path) -> str:
    return str(p.relative_to(LEANROOT).with_suffix("")).replace("/", ".")


def scan() -> dict[str, set[str]]:
    """FQN -> set of modules declaring it."""
    declmods: dict[str, set[str]] = collections.defaultdict(set)
    for p in sorted((LEANROOT / "QOU").rglob("*.lean")):
        mod = modname(p)
        lines = strip_block_comments(
            p.read_text(encoding="utf-8", errors="replace")
        ).splitlines()
        stack: list[tuple[str, str]] = []
        for ln in lines:
            if IMP.match(ln):
                continue
            if (m := NS.match(ln)):
                stack.append(("ns", m.group(1)))
                continue
            if SEC.match(ln) and not DECL.match(ln):
                stack.append(("sec", ""))
                continue
            if END.match(ln) and stack:
                stack.pop()
                continue
            if (m := DECL.match(ln)):
                if PRIV.match(ln):
                    continue
                ns = ".".join(x for kind, x in stack if kind == "ns")
                fq = f"{ns}.{m.group(1)}" if ns else m.group(1)
                declmods[fq].add(mod)
    return declmods


def propose(declmods) -> list[tuple[str, str, str]]:
    out = []
    for fq, mods in sorted(declmods.items()):
        if len(mods) < 2:
            continue
        for a, b in itertools.combinations(sorted(mods), 2):
            out.append((fq, a, b))
    return out


def verify(pairs, lean_path: str) -> list[dict]:
    env = dict(os.environ, LEAN_PATH=lean_path)
    confirmed = []
    with tempfile.TemporaryDirectory() as td:
        probe = Path(td) / "DupProbe.lean"
        for fq, a, b in pairs:
            probe.write_text(f"import {a}\nimport {b}\n")
            r = subprocess.run(
                ["lean", str(probe)], env=env, capture_output=True, text=True
            )
            blob = r.stdout + r.stderr
            for line in blob.splitlines():
                if "environment already contains" in line:
                    confirmed.append(
                        {"fqn": fq, "modules": [a, b],
                         "lean_error": line.split("error: ", 1)[-1].strip()}
                    )
                    break
    return confirmed


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true",
                    help="confirm each proposed pair with the Lean compiler")
    ap.add_argument("--lean-path", default=os.environ.get("LEAN_PATH", ""))
    ap.add_argument("--check-baseline", action="store_true")
    ap.add_argument("--write-baseline", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    # A baseline check without --verify would fall through the propose-only
    # branch below and `return 0` having examined nothing -- a gate that
    # reports success without looking. Both baseline modes imply --verify.
    if args.check_baseline or args.write_baseline:
        args.verify = True

    pairs = propose(scan())
    if not args.verify:
        print(f"proposed duplicate-FQN module pairs: {len(pairs)}")
        print("  (candidates only — re-run with --verify; the compiler decides)")
        for fq, a, b in pairs:
            print(f"  {fq}\n      {a}\n    + {b}")
        return 0

    if not args.lean_path:
        print("--verify needs --lean-path or LEAN_PATH", file=sys.stderr)
        return 2

    confirmed = verify(pairs, args.lean_path)
    key = lambda d: (d["fqn"], tuple(d["modules"]))
    print(f"proposed pairs: {len(pairs)}   COMPILER-CONFIRMED collisions: {len(confirmed)}")
    for d in sorted(confirmed, key=key):
        print(f"  {d['fqn']}\n      {d['modules'][0]}\n    + {d['modules'][1]}")

    if args.write_baseline:
        BASELINE.parent.mkdir(parents=True, exist_ok=True)
        BASELINE.write_text(json.dumps(
            {"schema": "lean-duplicate-fqn/v1",
             "note": "Ratchet: this list drains, never grows.",
             "pairs": sorted(confirmed, key=key)}, indent=2) + "\n")
        print(f"wrote {BASELINE.relative_to(REPO)} ({len(confirmed)} pairs)")
        return 0

    if args.check_baseline:
        base = json.loads(BASELINE.read_text())["pairs"] if BASELINE.exists() else []
        known = {key(d) for d in base}
        new = [d for d in confirmed if key(d) not in known]
        drained = known - {key(d) for d in confirmed}
        if drained:
            print(f"\n{len(drained)} baseline pair(s) drained — regenerate with "
                  f"--write-baseline")
        if new:
            print(f"\nFAIL: {len(new)} NEW duplicate-FQN collision(s):")
            for d in sorted(new, key=key):
                print(f"  {d['fqn']}  {d['modules'][0]} + {d['modules'][1]}")
            return 1
        print("\nOK: no new collisions")
    if args.json:
        print(json.dumps(confirmed, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
