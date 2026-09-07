#!/usr/bin/env python3
"""Drop the class hypothesis and ask Lean to prove it anyway.

Why this exists
---------------
`lean-axiom-provability-probe.py` asks "is this `axiom` free?".  It cannot see
the same defect one construct over.  A §3b-cond conditional class

    class C (args) : Prop where
      field : P
    theorem P_holds (args) [hi : C args] : P := hi.field

carries **zero** axioms and **zero** sorries.  `#print axioms` on `P_holds`
comes back clean, `lean-axiom-guard.py` counts nothing, and the vacuity
detectors see a theorem with a real proof term.  The unproved assertion has
moved into the SIGNATURE, where no axiom gate looks.

That is the honest §3b-cond pattern when `P` is genuinely open -- and it is a
vacuous barrier when `P` is not.  The two are indistinguishable by reading.

Method
------
For each self-assuming candidate (a theorem whose body projects a class field
whose type IS the conclusion): delete the instance binder that mentions the
class, replace the body with a short tactic block, and compile.  Exit 0 means
Lean proves the conclusion outright, so the class was standing in for nothing.

Soundness direction, same as the axiom probe: a PASS is a proof.  A FAIL is
evidence of nothing -- the tactic list is short on purpose.

**Every probe is preceded by a BASELINE compile of the file UNCHANGED.**  A
file that does not compile as it stands (a missing olean, a red import, an
unrelated error) makes every verdict about the probe's own environment rather
than about the class -- and it fails in the direction that reads as "the class
is load-bearing", which is the comfortable answer.  Baseline-red files are
reported `NOBASE` and excluded from the denominator.

Input is the candidate list from `lean-self-assuming-audit.py`, so this probe
inherits that scanner's recall and adds no detection of its own.

Usage:
  scripts/lean-class-hypothesis-vacuity-probe.py [--limit N] [--json OUT]
"""
from __future__ import annotations
import argparse, json, os, pathlib, re, subprocess, sys, tempfile

TACTICS = [
    "rfl",
    "trivial",
    "exact ⟨_, rfl⟩",
    "simp",
    "decide",
    "constructor <;> rfl",
    "positivity",
    "norm_num",
]
TACTIC_BLOCK = " := by\n  first\n" + "\n".join(f"  | {t}" for t in TACTICS) + "\n"

AUDIT = "scripts/lean-self-assuming-audit.py"
ENTRY_RE = re.compile(
    r"\n  (?:theorem|lemma) (\S+)\n    (\S+?):(\d+)\n    class field (\S+) : ", re.S)


def candidates(root: str) -> list[dict]:
    r = subprocess.run([sys.executable, AUDIT, root], capture_output=True, text=True)
    out = []
    for name, path, line, field in ENTRY_RE.findall(r.stdout + r.stderr):
        out.append(dict(name=name, path=path, line=int(line), field=field))
    return out


def decl_span(lines: list[str], line: int) -> tuple[int, int]:
    """[start, end) of the declaration whose header begins at 1-indexed `line`."""
    start = line - 1
    j = start + 1
    while j < len(lines):
        if lines[j].strip() == "":
            k = j
            while k < len(lines) and lines[k].strip() == "":
                k += 1
            if k < len(lines) and lines[k].startswith((" ", "\t")):
                j = k + 1
                continue
            break
        if not lines[j].startswith((" ", "\t")):
            break
        j += 1
    return start, j


def strip_instance_binder(sig: str, cls: str) -> str | None:
    """Remove the `[… : Cls …]` (or `[Cls …]`) binder naming `cls`.

    Returns None when no such binder is present -- the theorem is then not of
    the shape this probe is about and is skipped rather than mis-probed.
    """
    out, i, removed = [], 0, False
    while i < len(sig):
        if sig[i] == "[":
            depth, j = 1, i + 1
            while j < len(sig) and depth:
                if sig[j] == "[":
                    depth += 1
                elif sig[j] == "]":
                    depth -= 1
                j += 1
            inner = sig[i + 1:j - 1]
            if re.search(rf"(?<![.\w]){re.escape(cls)}(?![\w])", inner):
                removed = True
                i = j
                continue
            out.append(sig[i:j])
            i = j
            continue
        out.append(sig[i])
        i += 1
    return "".join(out) if removed else None


def compile_text(text: str, near: pathlib.Path, lean: str, lean_path: str,
                 timeout: int) -> tuple[int, str]:
    with tempfile.NamedTemporaryFile("w", suffix=".lean", delete=False,
                                     dir=near.parent) as fh:
        fh.write(text)
        tmp = pathlib.Path(fh.name)
    try:
        env = dict(os.environ, LEAN_PATH=lean_path)
        r = subprocess.run([lean, "-DautoImplicit=false", "-s", "65536", str(tmp)],
                           capture_output=True, text=True, timeout=timeout, env=env)
        return r.returncode, (r.stdout + r.stderr)[:300]
    except subprocess.TimeoutExpired:
        return 124, "TIMEOUT"
    finally:
        tmp.unlink(missing_ok=True)


def probe(path: pathlib.Path, c: dict, lean: str, lean_path: str,
          timeout: int) -> tuple[str, str]:
    lines = path.read_text().split("\n")
    start, end = decl_span(lines, c["line"])
    decl = "\n".join(lines[start:end])
    # split header from body at the top-level `:=`
    m = re.search(r":=", decl)
    if not m:
        return "SKIP", "no `:=` in declaration"
    sig = decl[:m.start()]
    cls = c["field"].split(".")[0]
    # the field prefix is the INSTANCE name; resolve the class from the binder
    bm = re.search(rf"\[\s*{re.escape(cls)}\s*:\s*([A-Za-z_][\w.']*)", sig)
    clsname = bm.group(1) if bm else cls
    stripped = strip_instance_binder(sig, clsname)
    if stripped is None:
        return "SKIP", f"no instance binder naming {clsname}"
    rc, msg = compile_text("\n".join(lines), path, lean, lean_path, timeout)
    if rc != 0:
        return "NOBASE", msg
    new = lines[:start] + (stripped + TACTIC_BLOCK).split("\n") + lines[end:]
    rc, msg = compile_text("\n".join(new), path, lean, lean_path, timeout)
    if rc == 124:
        return "TIMEOUT", msg
    return ("PROVABLE" if rc == 0 else "FAIL"), msg


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="content")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--json")
    a = ap.parse_args()

    lean = os.environ.get("LEAN_BIN", "lean")
    lean_path = os.environ.get("LEAN_PATH", "")
    if not lean_path:
        print("LEAN_PATH is empty — source scripts/lean-direct-env.sh first", file=sys.stderr)
        return 2

    cands = candidates(a.root)
    if a.limit:
        cands = cands[:a.limit]
    print(f"probing {len(cands)} self-assuming candidate(s)\n")
    rows = []
    for c in cands:
        p = pathlib.Path(c["path"])
        verdict, msg = probe(p, c, lean, lean_path, a.timeout)
        rows.append(dict(**c, verdict=verdict))
        mark = "***" if verdict == "PROVABLE" else "   "
        print(f"{mark} {verdict:9s} {c['name']}  [{c['path']}:{c['line']}]")
        if verdict == "PROVABLE":
            print(f"      the class hypothesis is a VACUOUS BARRIER — Lean closes it unaided")
        sys.stdout.flush()
    n = sum(1 for r in rows if r["verdict"] == "PROVABLE")
    scored = [r for r in rows if r["verdict"] in ("PROVABLE", "FAIL")]
    from collections import Counter
    tally = Counter(r["verdict"] for r in rows)
    print(f"\n{n} of {len(scored)} SCORED candidates provable without the class hypothesis")
    print("  " + "  ".join(f"{k}={v}" for k, v in sorted(tally.items())))
    if tally.get("NOBASE"):
        print(f"  {tally['NOBASE']} excluded: the file is RED before the probe touches it,")
        print("  so a FAIL there would have measured the environment, not the class.")
    if a.json:
        json.dump(rows, open(a.json, "w"), indent=1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
