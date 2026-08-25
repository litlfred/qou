#!/usr/bin/env python3
"""Keystone axiom guard — `#print axioms` as a QA gate, not a one-off check.

Motivation (2026-08-07). Two keystones were merged claiming a discharge that a
per-declaration axiom check refutes: `OVTopAssembly.sum_numSYT_sq_eq_factorial`
and everything reindexed from it depend on `sorryAx`. File-level `grep sorry` is
a *screen*; the proof term is the *verdict*. See
`docs/audits/2026-08-07-ov-cone-axiom-audit-overclaim-correction.md`.

This script pins the measured axiom status of named declarations so that:

  * a declaration recorded `clean` that starts depending on `sorryAx` FAILS the
    gate (regression — the usual direction of harm);
  * a declaration recorded `sorryAx` that becomes clean is reported as a
    PROMOTION (someone closed an upstream gap; update the registry and the
    claims that were scoped around it).

Usage
-----
    scripts/lean-axiom-guard.py                 # check every entry
    scripts/lean-axiom-guard.py --filter TAIL   # substring filter on decl name
    scripts/lean-axiom-guard.py --registry F    # alternate registry file
    scripts/lean-axiom-guard.py --print-modules # the modules that must be built

Exit codes: 0 = all as recorded; 1 = regression; 2 = environment/setup problem.
A promotion alone exits 0 (it is good news) but prints a LOUD notice.

Registry format (one entry per line, `#` comments allowed):

    <import-module> | <fully-qualified-decl> | clean|sorryAx

The Lean root is `content/quantum-observable-universe/lean`; `LEAN_PATH` must
already be set for lean-direct use (see `.claude/skills/local/lean-environment-setup.md`
— restore the olean cache first, and note that a declaration's own module olean
must exist).

WHAT MUST BE BUILT FIRST — only the registry's own modules
----------------------------------------------------------
The probe file imports exactly the modules named in the registry and nothing
else, so this gate does **not** need the `QOU` root or a whole-tree build.
`--print-modules` emits that list, so a caller builds precisely the
prerequisites without duplicating the registry here:

    lake build $(scripts/lean-axiom-guard.py --print-modules)

This is recorded because the opposite was believed, and the belief is what kept
the gate unrun: bean `qou-agrd` asserted "the guard imports the **`QOU` root**,
which transitively needs the whole tree built". It does not, and never did.
Measured 2026-08-15: four of the five registry oleans were already present and
exactly one — `QOU.BraidsAndKnots.PlancherelNormalisation` — was missing.
Building that single module took 329 s and made the gate run clean on all seven
declarations. The diagnosis, not the difficulty, was the blocker.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

LEAN_ROOT = Path("content/quantum-observable-universe/lean")

# Measured 2026-08-07 by `#print axioms`. Keep sorted by module for readability.
DEFAULT_REGISTRY = """
# --- the (TAIL) first-instance chain (covariance-kernel epic qou-x631) ---
# The SIGN is genuinely sorry-free and is the content of the (TAIL) instance.
QOU.BraidsAndKnots.YoungDiagramTailFirstInstance | QOU.BraidsAndKnots.YoungDiagramTailFirstInstance.nuV_top_nonneg | clean
# The SYT-encoding bridge is genuinely sorry-free.
QOU.BraidKnot.SYTEncodingBridgeTwo | QOU.BraidKnot.SYTEncodingBridge.numSYT_eq_numStandardYoungTableaux | sorryAx-free-expected-clean-alias
QOU.BraidKnot.SYTEncodingBridgeTwo | QOU.BraidKnot.SYTEncodingBridge.numStandardYoungTableaux_le_numSYT | clean

# --- known-BAD: the RSK identity and everything reindexed from it ---
# The real gap is upstream (RegularRepBlockTrace's sorry on the specialised
# lemma, plus the Specht-core cone: 16 of 23 modules carry sorry).
QOU.BraidKnot.OVTopAssembly | QOU.BraidKnot.OVTopAssembly.sum_numSYT_sq_eq_factorial | sorryAx
QOU.BraidKnot.RSKBurnsideDischarge | QOU.BraidKnot.RSKBurnsideDischarge.rskBurnsideHolds | sorryAx
QOU.BraidsAndKnots.PlancherelNormalisation | QOU.BraidsAndKnots.PlancherelNormalisation.sum_sytDim_sq_eq_factorial | sorryAx
QOU.BraidsAndKnots.PlancherelNormalisation | QOU.BraidsAndKnots.PlancherelNormalisation.nuV_top_closed_form_unconditional | sorryAx
"""


def parse_registry(text: str) -> list[tuple[str, str, str]]:
    out: list[tuple[str, str, str]] = []
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 3:
            print(f"axiom-guard: malformed registry line: {raw!r}", file=sys.stderr)
            sys.exit(2)
        module, decl, expected = parts
        # Tolerate the alias marker used for entries whose module differs from
        # the declaration's own namespace.
        if expected.startswith("sorryAx-free"):
            expected = "clean"
        if expected not in {"clean", "sorryAx"}:
            print(f"axiom-guard: bad expectation {expected!r} in: {raw!r}", file=sys.stderr)
            sys.exit(2)
        out.append((module, decl, expected))
    return out


def _module_path(mod: str) -> Path:
    return LEAN_ROOT / (mod.replace(".", "/") + ".lean")


def _olean_path(mod: str) -> Path:
    return LEAN_ROOT / ".lake/build/lib/lean" / (mod.replace(".", "/") + ".olean")


def _qou_imports(src: Path) -> list[str]:
    out: list[str] = []
    try:
        for line in src.read_text().splitlines():
            m = re.match(r"^import\s+(QOU\.\S+)", line)
            if m:
                out.append(m.group(1))
            elif line.strip() and not line.startswith(("--", "/-", "import")):
                break
    except OSError:
        pass
    return out


def _dirty_paths() -> set[str]:
    """Repo-relative paths with uncommitted content changes (staged or not)."""
    try:
        proc = subprocess.run(
            ["git", "status", "--porcelain", "--", str(LEAN_ROOT)],
            capture_output=True, text=True, timeout=120,
        )
    except (FileNotFoundError, subprocess.SubprocessError):
        return set()          # no git → fall back to mtime for everything
    out: set[str] = set()
    for line in proc.stdout.splitlines():
        # "XY path" or "XY old -> new"; take the final path.
        path = line[3:].strip()
        if "->" in path:
            path = path.split("->")[-1].strip()
        out.add(path.strip('"'))
    return out


def _commit_time(src: Path) -> float | None:
    """Unix time of the commit that last touched `src`, or None if unavailable."""
    try:
        proc = subprocess.run(
            ["git", "log", "-1", "--format=%ct", "--", str(src)],
            capture_output=True, text=True, timeout=120,
        )
    except (FileNotFoundError, subprocess.SubprocessError):
        return None
    val = proc.stdout.strip()
    return float(val) if val else None


def _effective_source_time(src: Path, dirty: set[str]) -> float:
    """Source timestamp that survives a fresh clone.

    ⚠ A plain `src.stat().st_mtime` is WRONG here, and wrong in the direction that
    disables the gate. A clone or checkout stamps every file with the checkout time,
    which is later than any olean restored from a build cache — so an mtime comparison
    reports the entire import cone stale in exactly the environment this gate is meant
    to run in (fresh container or CI runner + `lean-cache-restore.sh`).

    Measured 2026-08-15: mtime flagged 15 modules stale — `Specht` source 10:08, olean
    03:33 — while `lake build`, which hashes content, replayed all 3285 jobs as already
    up to date. The sources had not changed since a commit that PREDATED the oleans; only
    the checkout timestamp was newer. Left as-is this would have made the gate refuse to
    report on every CI run, which is the same "protects nothing" outcome as never running
    it, reached from the opposite direction.

    So: for a file with no uncommitted changes, use the time of the commit that last
    touched it — stable across clones. For a DIRTY file, fall back to mtime, because a
    local edit is precisely the case the staleness check exists for and there is no
    commit to trust.
    """
    try:
        rel = str(src.relative_to(Path.cwd()))
    except ValueError:
        rel = str(src)
    if rel not in dirty:
        ct = _commit_time(src)
        if ct is not None:
            return ct
    return src.stat().st_mtime


def check_freshness(entries: list[tuple[str, str, str]]) -> list[str]:
    """Return human-readable staleness complaints.

    The guard reads whatever `.olean`s are on disk. A *missing* olean already fails
    loudly, but a **stale** one passes silently and reports the axiom status of an old
    snapshot — which is worthless, and worse than worthless because it looks like
    assurance. (Found 2026-08-15: the guard reported all-match against 9-day-old oleans
    while five of the underlying sorries had been closed upstream and three declarations
    had moved files.) So walk the transitive QOU import cone of every registry module and
    flag any olean older than its own source.

    "Older than its own source" is measured by `_effective_source_time`, not raw mtime —
    see there for why raw mtime disables the gate on a fresh clone.
    """
    problems: list[str] = []
    seen: set[str] = set()
    dirty = _dirty_paths()
    stack = [m for m, _, _ in entries]
    while stack:
        mod = stack.pop()
        if mod in seen:
            continue
        seen.add(mod)
        src, ole = _module_path(mod), _olean_path(mod)
        if not src.exists():
            continue
        stack.extend(_qou_imports(src))
        if not ole.exists():
            problems.append(f"{mod}: olean MISSING")
            continue
        if ole.stat().st_mtime < _effective_source_time(src, dirty):
            problems.append(f"{mod}: olean STALE (source is newer)")
    return problems


def run_axiom_check(entries: list[tuple[str, str, str]]) -> dict[str, set[str]]:
    """Return {decl: set-of-axioms}. One lean invocation for the whole batch."""
    modules = sorted({m for m, _, _ in entries})
    body = "".join(f"import {m}\n" for m in modules)
    body += "".join(f"#print axioms {d}\n" for _, d, _ in entries)

    # The file must live under the Lean root (lean rejects outside paths).
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".lean", prefix="AxiomGuard", dir=LEAN_ROOT, delete=False
    ) as fh:
        fh.write(body)
        tmp = Path(fh.name)
    try:
        proc = subprocess.run(
            ["lean", tmp.name],
            cwd=LEAN_ROOT,
            capture_output=True,
            text=True,
            timeout=3600,
        )
    except FileNotFoundError:
        print("axiom-guard: `lean` not on PATH — restore the toolchain first.", file=sys.stderr)
        sys.exit(2)
    finally:
        tmp.unlink(missing_ok=True)

    out = proc.stdout + proc.stderr
    if "object file" in out and "does not exist" in out:
        print("axiom-guard: a module olean is missing; build it lean-direct first:", file=sys.stderr)
        for line in out.splitlines():
            if "does not exist" in line:
                print("  " + line.strip(), file=sys.stderr)
        sys.exit(2)

    # `#print axioms X` prints: 'X' depends on axioms: [a, b,\n c]
    found: dict[str, set[str]] = {}
    for m in re.finditer(
        r"'([^']+)' depends on axioms: \[([^\]]*)\]", out, re.S
    ):
        decl = m.group(1)
        axs = {a.strip() for a in m.group(2).split(",") if a.strip()}
        found[decl] = axs
    # A declaration proved without any axiom prints a different sentence.
    for m in re.finditer(r"'([^']+)' does not depend on any axioms", out):
        found[m.group(1)] = set()
    if not found:
        print("axiom-guard: no `#print axioms` output parsed. Raw:", file=sys.stderr)
        print(out[:2000], file=sys.stderr)
        sys.exit(2)
    return found


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", type=Path, default=None)
    ap.add_argument("--filter", default=None, help="substring filter on declaration name")
    ap.add_argument(
        "--print-modules",
        action="store_true",
        help="print the modules this gate needs built (space-separated) and exit; "
             "feed to `lake build` — the gate does NOT need the QOU root",
    )
    args = ap.parse_args()

    if not LEAN_ROOT.is_dir():
        print(f"axiom-guard: run from the repo root (missing {LEAN_ROOT})", file=sys.stderr)
        return 2

    text = args.registry.read_text() if args.registry else DEFAULT_REGISTRY
    entries = parse_registry(text)
    if args.filter:
        entries = [e for e in entries if args.filter in e[1]]
    if not entries:
        print("axiom-guard: nothing to check")
        return 0

    # `--print-modules` answers BEFORE the freshness gate, deliberately: it is a pure
    # query over the registry that touches no olean, and its whole purpose is to tell a
    # caller what to build. Gating it on a fresh build would make the flag unusable in
    # exactly the situation it exists for — a cold or stale tree.
    if args.print_modules:
        # Deliberately bare stdout: this is consumed by `lake build $(...)`.
        print(" ".join(sorted({m for m, _, _ in entries})))
        return 0

    stale = check_freshness(entries)
    if stale:
        print("axiom-guard: refusing to report — the olean set does not match the source.",
              file=sys.stderr)
        for pr in sorted(stale):
            print("  " + pr, file=sys.stderr)
        print("\nRebuild the affected modules lean-direct, then re-run. A verdict from a stale\n"
              "olean set is not assurance — it is the axiom status of an old snapshot.",
              file=sys.stderr)
        return 2

    found = run_axiom_check(entries)

    regressions: list[str] = []
    promotions: list[str] = []
    missing: list[str] = []
    for _, decl, expected in entries:
        if decl not in found:
            missing.append(decl)
            continue
        has_sorry = "sorryAx" in found[decl]
        status = "sorryAx" if has_sorry else "clean"
        mark = "ok  " if status == expected else "FAIL"
        print(f"  [{mark}] {decl}: {status} (recorded {expected})")
        if status == expected:
            continue
        if expected == "clean" and has_sorry:
            regressions.append(decl)
        else:
            promotions.append(decl)

    if missing:
        print("\naxiom-guard: declarations not found in the environment:", file=sys.stderr)
        for d in missing:
            print("  " + d, file=sys.stderr)
        return 2

    if promotions:
        print("\n*** PROMOTION — an upstream gap closed: " + ", ".join(promotions))
        print("    Update the registry AND the claims that were scoped around the sorryAx.")
    if regressions:
        print("\n*** REGRESSION — these were clean and now depend on sorryAx:")
        for d in regressions:
            print("      " + d)
        return 1
    print("\naxiom-guard: all declarations match their recorded axiom status.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
