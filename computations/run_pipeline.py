#!/usr/bin/env python3
"""
Witness pipeline runner with dependency DAG.

Scans all .py computation scripts, extracts their imports to build a
dependency graph, checks staleness via witness_base, and runs only
stale scripts in topological order.

Usage:
    # Dry run: show what would be recomputed
    python3 run_pipeline.py --dry-run

    # Run all stale witnesses
    python3 run_pipeline.py

    # Run only witnesses linked to content blocks
    python3 run_pipeline.py --content-only

    # Force rerun of a specific script + dependents
    python3 run_pipeline.py --force topological-mass-table.py

    # Parallel execution (independent scripts run concurrently)
    python3 run_pipeline.py --jobs 4

Persistence:
    The CI side of this runner is split in two:

    - `.github/workflows/publish.yml` regenerates stale witnesses for
      every PR build but produces only an ephemeral artifact (1-day
      retention) — nothing is pushed back to git, so a fresh PR sees
      the same scripts as stale and re-pays the cost.
    - `.github/workflows/witness-refresh.yml` runs the *same* command
      on `push` to `main` (and nightly / on workflow_dispatch) and
      commits the refreshed `*.witness.json` files back to `main` as
      `github-actions[bot]`. Subsequent CI passes then see the
      regenerated witnesses as current and skip the rerun.

    Treat commits authored by `github-actions[bot]` with the message
    prefix `chore(witnesses): refresh ...` as machine-generated drift;
    do not hand-edit them.

Legacy cleanup:
    `cleanup_legacy_witnesses.py` codifies the heuristic from
    `_deprecated/README.md` (no contentBlock, no live importer, no
    audit-md citation, not auditOnly, not referenced by full filename
    from CI/scripts/pipeline) and moves matching scripts + their
    `*.witness.json` sidecars into `_deprecated/`.

Architecture:
    1. Scan *.py for `from X import` / `import X` to build DAG
    2. Check each *.witness.json for staleness (scriptHash mismatch)
    3. Topological sort: if A depends on B and B is stale, A is stale too
    4. Run stale scripts in dependency order
    5. Regenerate hecke_startup_cache.json first if sources changed

@module computations/run_pipeline
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import os
import re
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import Optional

COMP_DIR = Path(__file__).resolve().parent

# Scripts that are infrastructure, not witnesses
INFRA_SCRIPTS = {
    "q_parameter.py",
    "experimental_constants.py",
    "hecke_core.py",
    "hecke_engine.py",
    "hecke_symbolic.py",
    "hecke_characters.py",
    "hecke_division.py",
    "witness_base.py",
    "hecke_startup_cache.py",
    "run_pipeline.py",
}

# ── Dependency extraction ────────────────────────────────────────

_IMPORT_RE = re.compile(
    r"^\s*(?:from\s+([\w_]+)\s+import|import\s+([\w_]+))", re.MULTILINE
)

def _local_module_name(py_file: Path) -> str:
    """Convert filename to importable module name."""
    return py_file.stem


def _extract_local_imports(py_file: Path) -> set[str]:
    """Extract imports that refer to local computation scripts."""
    try:
        content = py_file.read_text(encoding="utf-8")
    except Exception:
        return set()

    # Map of module_name -> filename for all .py in COMP_DIR
    local_modules = {
        p.stem: p.name for p in COMP_DIR.glob("*.py")
    }
    # Also handle hyphenated names (file: foo-bar.py, import: foo_bar)
    for p in COMP_DIR.glob("*.py"):
        underscore_name = p.stem.replace("-", "_")
        local_modules[underscore_name] = p.name

    imports = set()
    for m in _IMPORT_RE.finditer(content):
        mod = m.group(1) or m.group(2)
        if mod in local_modules:
            imports.add(local_modules[mod])
    return imports


def build_dependency_graph() -> dict[str, set[str]]:
    """Build {script: set of scripts it depends on}."""
    graph = {}
    for py_file in sorted(COMP_DIR.glob("*.py")):
        if py_file.name in INFRA_SCRIPTS:
            continue
        deps = _extract_local_imports(py_file)
        # Remove self-references and infra
        deps.discard(py_file.name)
        graph[py_file.name] = deps
    return graph


def _topological_sort(graph: dict[str, set[str]]) -> list[str]:
    """Kahn's algorithm: return scripts in dependency order."""
    in_degree = defaultdict(int)
    for node in graph:
        if node not in in_degree:
            in_degree[node] = 0
        for dep in graph[node]:
            if dep in graph:  # only count edges to non-infra nodes
                in_degree[node] += 1

    queue = sorted([n for n in graph if in_degree[n] == 0])
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node)
        # Find nodes that depend on this one
        for other, deps in graph.items():
            if node in deps:
                in_degree[other] -= 1
                if in_degree[other] == 0 and other not in result:
                    queue.append(other)
                    queue.sort()

    # Add any remaining (cycle detection)
    for node in graph:
        if node not in result:
            result.append(node)
    return result


# ── Staleness checking ───────────────────────────────────────────

def _witness_path(script_name: str) -> Optional[Path]:
    """Find the witness JSON for a script."""
    stem = Path(script_name).stem
    # Try hyphenated name first (most common), then underscored
    for name in [stem, stem.replace("_", "-")]:
        p = COMP_DIR / f"{name}.witness.json"
        if p.exists():
            return p
    return None


_WITNESSES_BY_PRODUCER: "dict[str, list[Path]] | None" = None


_SCRIPTFILE_RE = re.compile(r'"scriptFile"\s*:\s*"([^"]+)"')


def _witnesses_by_producer() -> "dict[str, list[Path]]":
    """Map producer script basename → every witness it emits (by ``scriptFile``).

    Lets ``_is_stale`` q₀-check **multi-shard** producers — a producer that
    emits many witnesses (e.g. ``canonical_isotope_witness.py`` → the per-Z
    shards ``canonical-isotope-witness-Z00..Z118``) — not just the single
    ``_witness_path`` primary. Built once and cached for the process.
    """
    global _WITNESSES_BY_PRODUCER
    if _WITNESSES_BY_PRODUCER is None:
        m: "dict[str, list[Path]]" = {}
        for wf in COMP_DIR.glob("*.witness.json"):
            # Regex prefix-scan for `scriptFile` rather than a full json.loads —
            # witness JSONs can be very large and the field sits near the top.
            try:
                with wf.open(encoding="utf-8") as fh:
                    head = fh.read(8192)
                    mm = _SCRIPTFILE_RE.search(head)
                    if mm is None and len(head) == 8192:
                        mm = _SCRIPTFILE_RE.search(head + fh.read())
            except OSError:
                continue
            if mm:
                m.setdefault(Path(mm.group(1)).name, []).append(wf)
        _WITNESSES_BY_PRODUCER = m
    return _WITNESSES_BY_PRODUCER


def _is_stale(script_name: str) -> tuple[bool, str]:
    """Check whether a producer's witness(es) are stale or missing.

    Covers **multi-shard** producers: gathers the ``_witness_path`` primary
    AND every shard the producer emits (by ``scriptFile``), checks the
    producer's ``scriptHash``, then q₀-staleness across all of them. A
    multi-shard producer with no single primary (e.g. ``canonical_isotope``)
    is evaluated on its shards rather than reported "no witness file".

    Returns (is_stale, reason).
    """
    script_path = COMP_DIR / script_name
    primary = _witness_path(script_name)
    witnesses = list(_witnesses_by_producer().get(script_name, ()))
    if primary is not None and primary not in witnesses:
        witnesses.insert(0, primary)

    if not witnesses:
        return True, "no witness file"

    # scriptHash: the producer's recorded hash (from the primary, or any
    # shard that records one) vs the current script content.
    if script_path.exists():
        import hashlib
        current_hash = hashlib.sha256(
            script_path.read_text(encoding="utf-8").encode()
        ).hexdigest()[:12]
        recorded_hashes: set[str] = set()
        for wp in witnesses:
            try:
                rh = json.loads(
                    wp.read_text(encoding="utf-8")
                ).get("scriptHash")
            except (json.JSONDecodeError, OSError):
                return True, f"malformed witness ({wp.name})"
            if rh:
                recorded_hashes.add(rh)
        # Any shard recording a different scriptHash means the producer changed
        # since that shard was generated — catches mixed/partial regeneration
        # (don't stop at the first matching hash).
        drifted_hashes = recorded_hashes - {current_hash}
        if drifted_hashes:
            return True, f"script changed ({sorted(drifted_hashes)[0]} → {current_hash})"

    # q₀-awareness: the scriptHash gate above is blind to changes in IMPORTED
    # constants (a substrate q₀ re-pin leaves the producer byte-identical —
    # the systemic cause of stale-witness accumulation after 2026-05-28).
    # Flag a witness — primary OR any shard — whose embedded q₀ differs from
    # the current substrate q₀, so the auto-refresh (witness-refresh.yml /
    # publish.yml regen) regenerates it. Warn-and-heal: `_is_stale` only drives
    # regeneration, never a hard CI failure. Audit / state-tracking witnesses
    # are exempt (they may record an old q₀ on purpose). Reuses
    # witness_constant_staleness.py (#1500).
    from witness_constant_staleness import (
        Q0_SHAPE, AUDIT_SUFFIXES, matches_live_q0)
    from qou_substrate.constants import Q_50_DIGIT_STR
    cur = Q_50_DIGIT_STR[:14]  # "1." + 12 significant digits, for the message
    for wp in witnesses:
        if wp.name.endswith(AUDIT_SUFFIXES):
            continue
        try:
            raw = wp.read_text(encoding="utf-8")
        except OSError:
            continue
        # Compare at each recorded value's OWN precision, not at a fixed
        # width — a witness that serializes q₀ short is not stale, and
        # slicing both to 14 chars reported it as such. Here that misfire
        # cost recurring regeneration rather than a red gate, because this
        # path is warn-and-heal: it would re-run the producer on every pass
        # and the rewritten witness would be flagged again next time.
        drifted = {m.group(0) for m in Q0_SHAPE.finditer(raw)
                   if not matches_live_q0(m.group(0))}
        if drifted:
            return True, f"stale q₀ in {wp.name} ({sorted(drifted)[0]} ≠ {cur})"

    return False, "current"


_INFRA_HASH_FILE = COMP_DIR / ".infra-hashes.json"


def _check_infra_staleness() -> set[str]:
    """Check if any INFRA_SCRIPTS have changed since last recorded hashes.

    Compares current file hashes against stored hashes in .infra-hashes.json.
    Updates the stored hashes after comparison.

    Returns the set of infra script filenames that have changed.
    """
    import hashlib

    # Load stored hashes
    stored: dict[str, str] = {}
    if _INFRA_HASH_FILE.exists():
        try:
            stored = json.loads(_INFRA_HASH_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            stored = {}

    current: dict[str, str] = {}
    changed: set[str] = set()

    for name in sorted(INFRA_SCRIPTS):
        path = COMP_DIR / name
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8")
        h = hashlib.sha256(content.encode()).hexdigest()[:12]
        current[name] = h
        if stored.get(name) != h:
            changed.add(name)

    # Persist updated hashes
    try:
        _INFRA_HASH_FILE.write_text(
            json.dumps(current, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    except OSError:
        pass

    return changed


def _has_content_block(script_name: str) -> Optional[str]:
    """Check if this script's witness is linked to a content block."""
    witness_path = _witness_path(script_name)
    if witness_path is None:
        return None
    try:
        witness = json.loads(witness_path.read_text(encoding="utf-8"))
        return witness.get("contentBlock")
    except Exception:
        return None


# ── Execution ────────────────────────────────────────────────────

def _run_script(script_name: str, timeout: int = 300) -> tuple[bool, float, str]:
    """Run a computation script. Returns (success, elapsed_s, output)."""
    script_path = COMP_DIR / script_name
    t0 = time.monotonic()
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(COMP_DIR),
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        elapsed = time.monotonic() - t0
        output = result.stdout[-500:] if result.stdout else ""
        if result.returncode != 0:
            output += f"\nSTDERR: {result.stderr[-300:]}" if result.stderr else ""
        return result.returncode == 0, elapsed, output
    except subprocess.TimeoutExpired:
        return False, time.monotonic() - t0, f"TIMEOUT after {timeout}s"
    except Exception as e:
        return False, time.monotonic() - t0, str(e)


# ── Main ─────────────────────────────────────────────────────────

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Run stale witness computations in dependency order"
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would run without executing")
    parser.add_argument("--content-only", action="store_true",
                        help="Only run witnesses linked to content blocks")
    parser.add_argument("--force", nargs="*", metavar="SCRIPT",
                        help="Force rerun of specific scripts + dependents")
    parser.add_argument("--jobs", "-j", type=int, default=1,
                        help="Number of parallel jobs (default: 1). Scripts are "
                             "grouped into dependency levels and scripts within "
                             "the same level run concurrently.")
    parser.add_argument("--timeout", type=int, default=300,
                        help="Per-script timeout in seconds (default: 300)")
    parser.add_argument("--list-deps", action="store_true",
                        help="Show dependency graph and exit")
    parser.add_argument("--list-orphaned", action="store_true",
                        help="List witnesses not linked to content blocks")
    args = parser.parse_args()

    # Build dependency graph
    graph = build_dependency_graph()
    order = _topological_sort(graph)

    if args.list_deps:
        print(f"Dependency graph ({len(graph)} scripts):\n")
        for script in order:
            deps = graph.get(script, set())
            dep_str = ", ".join(sorted(deps)) if deps else "(none)"
            cb = _has_content_block(script)
            tag = f" → {cb}" if cb else ""
            print(f"  {script}: {dep_str}{tag}")
        return

    if args.list_orphaned:
        print("Witnesses NOT linked to content blocks:\n")
        orphaned = []
        for script in order:
            wp = _witness_path(script)
            if wp and not _has_content_block(script):
                orphaned.append((script, wp.name))
        for script, witness in orphaned:
            print(f"  {witness}  ← {script}")
        print(f"\n{len(orphaned)} orphaned / {len(order)} total")
        return

    # Determine staleness
    stale = {}
    forced = set(args.force) if args.force else set()

    # Check if any infra script has changed vs stored hashes
    infra_changed = _check_infra_staleness()

    for script in order:
        if script in forced:
            stale[script] = "forced"
            continue

        is_s, reason = _is_stale(script)
        if is_s:
            stale[script] = reason
            continue

        # Propagate: if any infra dependency changed, mark stale
        if infra_changed:
            deps = graph.get(script, set())
            changed_infra_deps = deps & infra_changed
            if changed_infra_deps:
                dep_names = ", ".join(sorted(changed_infra_deps))
                stale[script] = f"infra dependency changed: {dep_names}"
                continue

        # Propagate: if any dependency is stale, this is stale too
        deps = graph.get(script, set())
        for dep in deps:
            if dep in stale:
                stale[script] = f"dependency {dep} is stale"
                break

    # Filter content-only
    if args.content_only:
        stale = {s: r for s, r in stale.items() if _has_content_block(s)}

    # Report
    run_order = [s for s in order if s in stale]

    print(f"Pipeline status: {len(stale)} stale / {len(order)} total scripts\n")

    if not run_order:
        print("All witnesses are current. Nothing to do.")
        return

    for script in run_order:
        cb = _has_content_block(script)
        tag = f" [{cb}]" if cb else ""
        print(f"  {'[DRY]' if args.dry_run else '[ → ]'} {script}: {stale[script]}{tag}")

    if args.dry_run:
        print(f"\nDry run: {len(run_order)} scripts would be executed.")
        return

    # Execute
    print(f"\nRunning {len(run_order)} scripts...\n")

    # First: refresh startup cache if sources changed
    cache_script = COMP_DIR / "hecke_startup_cache.py"
    if cache_script.exists():
        print("  Refreshing startup cache...")
        subprocess.run(
            [sys.executable, str(cache_script)],
            cwd=str(COMP_DIR),
            capture_output=True,
        )

    successes = 0
    failures = 0
    total_time = 0.0

    if args.jobs <= 1:
        # Sequential path (original behaviour)
        for i, script in enumerate(run_order, 1):
            cb = _has_content_block(script)
            tag = f" [{cb}]" if cb else ""
            print(f"  [{i}/{len(run_order)}] {script}{tag}...", end=" ", flush=True)

            ok, elapsed, output = _run_script(script, timeout=args.timeout)
            total_time += elapsed

            if ok:
                successes += 1
                print(f"OK ({elapsed:.1f}s)")
            else:
                failures += 1
                print(f"FAILED ({elapsed:.1f}s)")
                last_line = output.strip().split("\n")[-1] if output else "(no output)"
                print(f"         {last_line}")
    else:
        # Parallel path: group run_order into dependency levels, then
        # run each level concurrently.  A script's level is 1 +
        # max(level(dep) for dep in stale deps); scripts with no stale
        # deps are at level 0.
        from concurrent.futures import ProcessPoolExecutor, as_completed

        stale_set = set(run_order)
        level_of: dict[str, int] = {}

        def _level(script: str, on_stack: set[str]) -> int:
            """Compute level via memoized DFS; robust to imperfect topo
            order (e.g. when toposort's cycle-detection fallback puts
            dependents before deps in run_order). Per F3 fix on PR
            #588 — earlier `level_of[d]` lookup KeyError'd on
            markov_trace_canonical.py because run_order is not a
            strict topological sequence."""
            if script in level_of:
                return level_of[script]
            if script in on_stack:
                return 0  # cycle: break here
            on_stack.add(script)
            stale_deps = graph.get(script, set()) & stale_set
            lvl = 1 + max(
                (_level(d, on_stack) for d in stale_deps), default=-1)
            on_stack.discard(script)
            level_of[script] = lvl
            return lvl

        for script in run_order:
            _level(script, set())

        levels: dict[int, list[str]] = {}
        for script, lvl in level_of.items():
            levels.setdefault(lvl, []).append(script)

        max_level = max(levels)
        n_workers = min(args.jobs, len(run_order))
        print(f"  Parallel: {n_workers} workers, {max_level + 1} dependency levels\n")

        done = 0
        total = len(run_order)
        with ProcessPoolExecutor(max_workers=n_workers) as ex:
            for lvl in range(max_level + 1):
                batch = sorted(levels.get(lvl, []))
                if not batch:
                    continue
                print(f"  Level {lvl}: {len(batch)} scripts")
                futures = {
                    ex.submit(_run_script, script, args.timeout): script
                    for script in batch
                }
                for fut in as_completed(futures):
                    script = futures[fut]
                    ok, elapsed, output = fut.result()
                    total_time += elapsed
                    done += 1
                    cb = _has_content_block(script)
                    tag = f" [{cb}]" if cb else ""
                    if ok:
                        successes += 1
                        print(f"  [{done}/{total}] {script}{tag}: OK ({elapsed:.1f}s)")
                    else:
                        failures += 1
                        last_line = output.strip().split("\n")[-1] if output else "(no output)"
                        print(f"  [{done}/{total}] {script}{tag}: FAILED ({elapsed:.1f}s)")
                        print(f"         {last_line}")

    print(f"\nDone: {successes} ok, {failures} failed, {total_time:.1f}s total")


if __name__ == "__main__":
    main()
