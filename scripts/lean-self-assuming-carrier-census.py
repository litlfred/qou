#!/usr/bin/env python3
"""Census, not sample: which self-assuming projections have an INHABITED carrier?

`docs/audits/2026-08-30-sizing-the-self-assuming-projection-drain.md` established
the discriminator and applied it to **12 sampled** declarations of 112, finding 0
legitimate -- and stated its own uncertainty honestly: *"0 of 12 does not mean 0
of 112 ... consistent with a true legitimate rate up to roughly 25 % at 95 %
confidence."*

Checking a carrier is a few seconds, so the sample was never necessary. This runs
the same discriminator over EVERY candidate the scanner currently reports.

    A projection is the legitimate Mathlib accessor idiom ONLY when
    something BUILDS the bundle.

Carrier resolution, in order:
  1. the binder `[ivar : Carrier ...]` / `(ivar : Carrier ...)` in the theorem's
     own signature -- authoritative, since that is what the body projects from;
  2. failing that, the `class`/`structure` in the same file declaring a field of
     the projected name.

Unresolved candidates are printed as `??` rather than silently dropped: a census
that quietly loses rows is a sample wearing a census's name.

Usage:  scripts/lean-self-assuming-carrier-census.py [--root content]
"""
from __future__ import annotations
import argparse, importlib.util, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "carrier_inhabited", HERE / "lean-carrier-inhabited-check.py")
_chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_chk)

ROW = re.compile(r"\n  (?:theorem|lemma) (\S+)\n    (\S+?):(\d+)\n    class field (\S+) : ")


def resolve(path: str, line: int, field: str) -> str | None:
    ivar, fname = field.split(".")[0], field.split(".")[-1]
    lines = pathlib.Path(path).read_text(errors="ignore").split("\n")
    sig = "\n".join(lines[line - 1:line + 14])
    m = re.search(rf"[\[\(]\s*{re.escape(ivar)}\s*:\s*(?:@)?([A-Za-z_][\w.']*)", sig)
    if m:
        return m.group(1)
    for i, l in enumerate(lines):
        dm = re.match(r"\s*(?:class|structure)\s+([A-Za-z_][\w.']*)", l)
        if not dm:
            continue
        j, fields = i + 1, []
        while j < len(lines) and (lines[j].startswith((" ", "\t")) or not lines[j].strip()):
            fm = re.match(r"\s+(\w+)\s*:", lines[j])
            if fm:
                fields.append(fm.group(1))
            j += 1
        if fname in fields:
            return dm.group(1)
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="content")
    a = ap.parse_args()

    if not _chk.builders(_chk.SELFTEST[0]):
        print("REFUSING: the inhabitation control is not found; run "
              "scripts/lean-carrier-inhabited-check.py --selftest", file=sys.stderr)
        return 2

    r = subprocess.run([sys.executable, str(HERE / "lean-self-assuming-audit.py"), a.root],
                       capture_output=True, text=True)
    rows = ROW.findall(r.stdout + r.stderr)
    carriers: dict[str, list[str]] = {}
    unresolved = []
    for name, path, line, field in rows:
        c = resolve(path, int(line), field)
        (carriers.setdefault(c, []) if c else unresolved).append(name) \
            if c else unresolved.append(name)
    print(f"{len(rows)} candidates over {len(carriers)} distinct carriers\n")
    inh = un = 0
    for c in sorted(carriers):
        b = _chk.builders(c.split(".")[-1], a.root)
        inh, un = (inh + 1, un) if b else (inh, un + 1)
        tag = "INHABITED  " if b else "uninhabited"
        print(f"  {len(b):>2}  {c:<44} {tag}  ({len(carriers[c])} decl)")
    for n in unresolved:
        print(f"  ??  carrier unresolved: {n}")
    tot = inh + un
    print(f"\ninhabited {inh}  uninhabited {un}  of {tot} resolved carriers"
          f"  ({inh / tot:.0%} legitimate accessor idiom)" if tot else "")
    if unresolved:
        print(f"{len(unresolved)} candidate(s) unresolved — not counted either way")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
