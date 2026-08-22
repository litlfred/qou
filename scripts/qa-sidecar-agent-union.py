#!/usr/bin/env python3
"""Union-merge the agent-adjudicated entries of `.qa.json` sidecars.

The standard resolution for a sidecar conflict is "do not hand-merge
generated output; let `qa-sweep` regenerate it against the merged tree".
That is right for **script** criteria and wrong for **agent** ones: an
agent verdict has no producer, so regenerating drops it and the sidecar
stays well-formed while the axis silently reports fewer findings. The
#5103 takeover lost 7381 `trap-*` verdicts over 738 blocks that way
(bean `qou-tqr9`); this script is that restoration generalised so the
next one is mechanical rather than a judgement call.

Usage
-----

    qa-sidecar-agent-union.py --against origin/main [--apply]
    qa-sidecar-agent-union.py --against HEAD@{1} --check

`--against REF` reads each sidecar as it exists at REF and unions its
agent entries into the working-tree copy. An entry is carried over only
if its `field_hash.md` still matches the live `.md` — a verdict certifies
the text it was written against, and porting a stale one would assert a
reading of prose that has since changed. `--check` reports and exits 1
if the working tree is missing any live-valid agent entry REF carries;
`--apply` writes the union.

Numbers are parsed as Decimal and re-serialised verbatim so an unrelated
float in the file is not reformatted (`0.000074` -> `7.4e-05` is what
made the first hand-restoration unreviewable), and `ensure_ascii=False`
keeps accented characters as themselves.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from decimal import Decimal
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def _dumps(obj) -> str:
    # json.dumps cannot emit Decimal directly; stringify then unquote the
    # sentinel. Cheaper and safer than a hand-rolled serialiser.
    sentinels: dict[str, str] = {}

    def walk(o):
        if isinstance(o, Decimal):
            key = f"__dec_{len(sentinels)}__"
            sentinels[key] = str(o)
            return key
        if isinstance(o, dict):
            return {k: walk(v) for k, v in o.items()}
        if isinstance(o, list):
            return [walk(v) for v in o]
        return o

    text = json.dumps(walk(obj), indent=2, ensure_ascii=False)
    for key, raw in sentinels.items():
        text = text.replace(f'"{key}"', raw)
    return text + "\n"


def _load(text: str):
    return json.loads(text, parse_float=Decimal, parse_int=Decimal)


def _sha12(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def _git_show(ref: str, path: str) -> str | None:
    proc = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        cwd=REPO,
        capture_output=True,
        text=True,
    )
    return proc.stdout if proc.returncode == 0 else None


def _sidecars_at(ref: str) -> list[str]:
    proc = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", ref, "content/"],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=True,
    )
    return [p for p in proc.stdout.splitlines() if p.endswith(".qa.json")]


def _identity(entry: dict) -> tuple:
    """What makes two agent entries the same verdict.

    Keyed on the reviewer's batch id, the text it certifies, and the
    timestamp — two agents may legitimately reach opposite verdicts on
    one criterion, and both are kept.
    """
    reviewer = entry.get("reviewer") or {}
    field = entry.get("field_hash") or {}
    return (
        reviewer.get("kind"),
        reviewer.get("id"),
        field.get("md"),
        entry.get("reviewed_at"),
        entry.get("result"),
    )


def _live_md_hash(sidecar: Path, doc: dict) -> str | None:
    paths = doc.get("paths") or {}
    md_rel = paths.get("md")
    md = (REPO / md_rel) if md_rel else sidecar.with_suffix("").with_suffix(".md")
    if not md.exists():
        return None
    return _sha12(md.read_bytes())


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--against", required=True, help="git ref to union in")
    ap.add_argument("--apply", action="store_true", help="write the union")
    ap.add_argument("--check", action="store_true", help="exit 1 if entries would be gained")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    ref = args.against
    gained = 0
    stale = 0
    touched: list[str] = []

    for rel in _sidecars_at(ref):
        old_text = _git_show(ref, rel)
        if old_text is None:
            continue
        try:
            old = _load(old_text)
        except json.JSONDecodeError:
            continue

        path = REPO / rel
        if path.exists():
            raw = path.read_text()
            try:
                new = _load(raw)
            except json.JSONDecodeError:
                continue
        else:
            # The sidecar is gone from the working tree entirely. Its
            # script criteria are regenerable and its agent ones are not,
            # but resurrecting a whole file is a bigger call than this
            # script should make silently: report and move on.
            agent_n = sum(
                1
                for entries in (old.get("criteria") or {}).values()
                for e in entries
                if (e.get("reviewer") or {}).get("kind") == "agent"
            )
            if agent_n and args.verbose:
                print(f"DELETED {rel}: {agent_n} agent entries at {ref}, file absent here")
            continue

        live_md = _live_md_hash(path, new)
        crit_new = new.setdefault("criteria", {})
        changed = False

        for crit, old_entries in (old.get("criteria") or {}).items():
            existing = crit_new.get(crit, [])
            seen = {_identity(e) for e in existing}
            for entry in old_entries:
                if (entry.get("reviewer") or {}).get("kind") != "agent":
                    continue
                if _identity(entry) in seen:
                    continue
                entry_md = (entry.get("field_hash") or {}).get("md")
                if live_md is not None and entry_md != live_md:
                    stale += 1
                    continue
                existing.append(entry)
                seen.add(_identity(entry))
                gained += 1
                changed = True
            if existing:
                crit_new[crit] = existing

        if changed:
            touched.append(rel)
            if args.apply:
                out = _dumps(new)
                # Match the file's existing trailing-newline state, so a
                # sidecar written without one is not gratuitously touched.
                if not raw.endswith("\n"):
                    out = out.rstrip("\n")
                path.write_text(out)

    verb = "restored" if args.apply else "missing from the working tree"
    print(f"{gained} agent entries {verb} across {len(touched)} sidecars (vs {ref})")
    if stale:
        print(f"{stale} skipped: field_hash.md no longer certifies the live .md")
    if args.verbose:
        for rel in touched:
            print(f"  {rel}")

    if args.check and gained:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
