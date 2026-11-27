#!/usr/bin/env python3
# polynomial_q_not_applicable: reproducibility audit; no symbolic-q logic.
"""Witness reproducibility byte-equality check (P32).

For each registered builder script that writes a `*.derivation.json`
file, snapshot the on-disk output, re-run the builder, and assert
the new output is byte-equal to the snapshot. A builder that fails
this check is non-deterministic — typically because of dict-iteration
order, embedded timestamps, float-precision drift, or PYTHONHASHSEED-
dependent output.

This is the **infra-discipline** counterpart to the existing static
scanners (`compute_audit_scan.py`) and the chain validators
(`derivation_chain_validator.py`). It is the deferred Priority-3.2
item from
[`docs/audits/2026-05-12-canonical-derivation-compute-review.md §4`](../../docs/audits/2026-05-12-canonical-derivation-compute-review.md).

Why it matters
--------------

* `*.derivation.json` files are committed to the repo and consumed
  downstream (e.g. `derivation_chain_validator.py`,
  `derivation_chain_audit.py`, the docs pipeline). A non-deterministic
  builder silently rewrites them on every CI run, polluting diffs and
  making git-blame meaningless.
* The blocker for previously documenting P3.2 was uncertainty about
  whether reproducibility was actually achievable. Pre-flight survey
  on 2026-05-12 confirmed 2/2 sampled builders are byte-equal across
  two runs (`build_q0_anchor_chain.py` 48ms;
  `build_atomic_braid_recipe_d_chain.py` ~1s).

Usage
-----

    python computations/witness_reproducibility_check.py

    # Strict mode: exit non-zero if any builder fails (for CI)
    python computations/witness_reproducibility_check.py --strict

    # Limit to one builder for fast local dev
    python computations/witness_reproducibility_check.py \\
        --only build_q0_anchor_chain.py

Design — explicit registry, not auto-discovery
----------------------------------------------

The registry below lists ``(builder_script, output_file)`` pairs
explicitly rather than auto-discovering them via grep. This is
deliberate:

* Some builders (e.g. ``build_six_term_substrate_model_b.py``) take
  CLI args that affect the output filename — auto-discovery would
  guess wrong.
* Some scripts that mention ``.derivation.json`` are validators that
  *read* but don't *write* (e.g. ``derivation_chain_validator.py``).
* An explicit registry is auditable: a reviewer can read the list
  and immediately see which chains are protected. Auto-discovery
  hides the coverage question.

To add a new builder: append a tuple to ``BUILDER_REGISTRY``. The
checker will automatically include it on the next run.

Audit-only: results live in
``docs/audits/2026-05-12-canonical-derivation-compute-review.md``.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import argparse
import hashlib
import shutil
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ── Builder registry (explicit) ──────────────────────────────────
# Each entry: (builder script under HERE, output file under HERE).
# Keep sorted alphabetically by script name. Add a brief comment
# justifying any builder that needs CLI args or env vars.
BUILDER_REGISTRY: list[tuple[str, str]] = [
    # Single-output, no-arg builders (the easy 11)
    ("build_atomic_braid_recipe_4he_chain.py",
     "atomic-braid-recipe-4he.derivation.json"),
    ("build_atomic_braid_recipe_d_chain.py",
     "atomic-braid-recipe-d.derivation.json"),
    ("build_atomic_braid_recipe_n_chain.py",
     "atomic-braid-recipe-n.derivation.json"),
    ("build_atomic_braid_recipe_p_chain.py",
     "atomic-braid-recipe-p.derivation.json"),
    ("build_markov_trace_assembly_deuteron_chain.py",
     "markov-trace-assembly-deuteron.derivation.json"),
    ("build_markov_trace_assembly_neutron_chain.py",
     "markov-trace-assembly-neutron.derivation.json"),
    ("build_neutron_mass_50dps_chain.py",
     "neutron-mass-50dps.derivation.json"),
    ("build_proton_mass_50dps_chain.py",
     "proton-mass-50dps.derivation.json"),
    ("build_q0_anchor_chain.py",
     "q0-anchor.derivation.json"),
    ("build_term7_s_crystal_4he_chain.py",
     "term7-s-crystal-4he.derivation.json"),
    ("braid_encoding_audit.py",
     "markov-trace-assembly-proton.derivation.json"),
]

# Per-builder timeout (seconds). Keep generous to accommodate the
# heavier 50dps mass chains.
PER_BUILDER_TIMEOUT_S = 600


def _file_hash(path: Path) -> str:
    """SHA-256 of file content (used for diff display, not just byte-equal)."""
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _check_one(script: str, output: str) -> dict:
    """Snapshot output, re-run script, compare. Return result dict.

    Side-effect protection: snapshots the mtime+content of EVERY
    file in HERE before the run, and restores any non-registered
    file that the builder mutates. This catches the common pattern
    where a chain-builder also emits a sibling ``*.witness.json``
    via ``WitnessBuilder`` — those always drift on metadata
    (computedAt, engineVersion, commitSha) and would otherwise leave
    the working tree dirty after every reproducibility run.
    """
    script_path = HERE / script
    output_path = HERE / output

    result: dict = {
        "script": script,
        "output": output,
        "status": "unknown",
        "snapshot_sha256": None,
        "rerun_sha256": None,
        "snapshot_bytes": None,
        "rerun_bytes": None,
        "rerun_seconds": None,
        "side_effects_restored": 0,
        "note": None,
    }

    if not script_path.exists():
        result["status"] = "skip"
        result["note"] = f"script not found: {script}"
        return result
    if not output_path.exists():
        result["status"] = "skip"
        result["note"] = (
            f"output not found before run: {output} — run the "
            f"builder once to produce a baseline first."
        )
        return result

    # Snapshot the registered output
    snapshot_path = output_path.with_suffix(".derivation.json.snapshot")
    shutil.copy2(output_path, snapshot_path)
    result["snapshot_sha256"] = _file_hash(snapshot_path)
    result["snapshot_bytes"] = snapshot_path.stat().st_size

    # Snapshot the dir-level state for side-effect protection.
    # We hash every regular file in HERE; after the run we restore
    # any non-registered file whose hash changed. We deliberately
    # avoid recursing into subdirectories (witness data,
    # from_scratch/, etc.) to keep the cost bounded.
    pre_state: dict[Path, tuple[bytes, int]] = {}
    for child in HERE.iterdir():
        if not child.is_file():
            continue
        # Skip the snapshot path itself (just created)
        if child == snapshot_path:
            continue
        try:
            data = child.read_bytes()
            pre_state[child] = (data, child.stat().st_mode)
        except OSError:
            continue

    # Re-run the builder
    t0 = time.monotonic()
    try:
        proc = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=HERE,
            capture_output=True,
            text=True,
            timeout=PER_BUILDER_TIMEOUT_S,
            check=False,
        )
    except subprocess.TimeoutExpired:
        result["status"] = "timeout"
        result["note"] = f"timed out after {PER_BUILDER_TIMEOUT_S}s"
        shutil.move(str(snapshot_path), str(output_path))
        result["rerun_seconds"] = f"{PER_BUILDER_TIMEOUT_S:.3f}"
        return result
    result["rerun_seconds"] = f"{time.monotonic() - t0:.3f}"

    if proc.returncode != 0:
        result["status"] = "error"
        result["note"] = (
            f"builder exited {proc.returncode}: "
            f"{(proc.stderr or proc.stdout)[-300:].strip()}"
        )
        shutil.move(str(snapshot_path), str(output_path))
        # Still restore side-effects (the builder may have written
        # partial output before failing).
        _restore_side_effects(pre_state, output_path, result)
        return result

    if not output_path.exists():
        result["status"] = "error"
        result["note"] = (
            f"builder ran successfully but output {output} disappeared"
        )
        shutil.move(str(snapshot_path), str(output_path))
        _restore_side_effects(pre_state, output_path, result)
        return result

    result["rerun_sha256"] = _file_hash(output_path)
    result["rerun_bytes"] = output_path.stat().st_size

    # Determinism verdict on the registered output
    if result["snapshot_sha256"] == result["rerun_sha256"]:
        result["status"] = "pass"
    else:
        result["status"] = "drift"
        result["note"] = (
            "byte-equality failed — builder is non-deterministic "
            "across runs. Likely causes: dict-iteration order "
            "(set PYTHONHASHSEED=0), embedded timestamp, "
            "float-precision drift, environment-dependent module "
            "ordering, or a hand-edit to the committed JSON that "
            "the script does not reproduce."
        )
    # Always restore the registered output snapshot
    shutil.move(str(snapshot_path), str(output_path))
    # Restore side-effects (other files the builder mutated)
    _restore_side_effects(pre_state, output_path, result)
    return result


def _restore_side_effects(
    pre_state: dict[Path, tuple[bytes, int]],
    registered_output: Path,
    result: dict,
) -> None:
    """Restore any non-registered file mutated by the builder.

    This protects sibling ``*.witness.json`` files written via
    ``WitnessBuilder`` (which drift on every run due to embedded
    timestamps) from polluting the working tree.
    """
    for child, (data, mode) in pre_state.items():
        if child == registered_output:
            continue
        if not child.exists():
            # Builder deleted this file — restore it.
            try:
                child.write_bytes(data)
                child.chmod(mode)
                result["side_effects_restored"] += 1
            except OSError:
                pass
            continue
        try:
            current = child.read_bytes()
        except OSError:
            continue
        if current != data:
            try:
                child.write_bytes(data)
                child.chmod(mode)
                result["side_effects_restored"] += 1
            except OSError:
                pass


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Witness reproducibility byte-equality check (P32)."
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero if any builder fails byte-equality.",
    )
    parser.add_argument(
        "--only",
        action="append",
        default=None,
        help="Limit run to specific builder script(s). Repeatable.",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run built-in unit self-test for non-vacuous assertion gating (bean qou-coyy).",
    )
    args = parser.parse_args()

    if args.self_test:
        try:
            from witness_base import WitnessBuilder
        except ImportError:
            sys.path.insert(0, str(HERE))
            from witness_base import WitnessBuilder
        w_fail = WitnessBuilder("witness-reproducibility-check-test", engine="python")
        w_fail.add_assertion(
            "all_checked_builders_byte_reproducible",
            computed="4",
            expected="0",
            tolerance="0",
            source="self-test: 4 drifting builders must fail allPassed (bean qou-coyy)",
        )
        assert w_fail.build()["allPassed"] is False, "Expected allPassed=False when fail_count=4"
        w_pass = WitnessBuilder("witness-reproducibility-check-test", engine="python")
        w_pass.add_assertion(
            "all_checked_builders_byte_reproducible",
            computed="0",
            expected="0",
            tolerance="0",
            source="self-test: 0 drifting builders passes allPassed (bean qou-coyy)",
        )
        assert w_pass.build()["allPassed"] is True, "Expected allPassed=True when fail_count=0"
        print("SELF-TEST PASSED (2/2 cases, bean qou-coyy)")
        return 0

    registry = BUILDER_REGISTRY
    if args.only:
        wanted = set(args.only)
        registry = [
            (s, o) for (s, o) in registry if s in wanted
        ]
        if not registry:
            print(
                f"--only matched no registered builders. "
                f"Available: {sorted(s for s, _ in BUILDER_REGISTRY)}"
            )
            return 2

    print(
        f"witness-reproducibility-check (P32): "
        f"{len(registry)} builders to check"
    )
    print("=" * 60)

    results = []
    for script, output in registry:
        print(f"  → {script:48s}", end="", flush=True)
        r = _check_one(script, output)
        results.append(r)
        marker = {
            "pass": "✓",
            "drift": "✗",
            "error": "!",
            "timeout": "⏱",
            "skip": "?",
        }.get(r["status"], "?")
        secs = r.get("rerun_seconds")
        secs_str = f"{secs:>6s}s" if isinstance(secs, str) else (
            f"{secs:6.2f}s" if isinstance(secs, (int, float)) else "  -- "
        )
        print(f"  {marker} {r['status']:7s}  {secs_str}")
        if r["note"]:
            print(f"      note: {r['note']}")

    # Summary
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1

    print()
    print("Summary:")
    for status in ("pass", "drift", "error", "timeout", "skip"):
        if status in by_status:
            print(f"  {status:7s}: {by_status[status]:3d}")

    pass_count = by_status.get("pass", 0)
    fail_count = (
        by_status.get("drift", 0)
        + by_status.get("error", 0)
        + by_status.get("timeout", 0)
    )
    total_checkable = pass_count + fail_count
    pass_ratio = (
        f"{pass_count / total_checkable:.16f}" if total_checkable else None
    )

    # Emit witness
    try:
        from witness_base import WitnessBuilder
    except ImportError:
        sys.path.insert(0, str(HERE))
        from witness_base import WitnessBuilder

    w = (
        WitnessBuilder(
            "witness-reproducibility-check",
            engine="python",
        )
        .set_description(
            "Per-builder byte-equality reproducibility check for "
            "*.derivation.json files. Snapshot → re-run → compare. "
            "P32 from .claude/skills/local/compute-audit.md."
        )
        .set_audit_only(
            "docs/audits/2026-05-12-canonical-derivation-compute-review.md"
        )
        .add_parameter("registry_size", len(BUILDER_REGISTRY))
        .add_parameter("checked", len(registry))
        .add_parameter("strict", args.strict)
        .add_data("by_status", by_status)
        .add_data("pass_ratio", pass_ratio)
        .add_data("results", results)
        .add_assertion(
            "all_checked_builders_byte_reproducible",
            computed=str(fail_count),
            expected="0",
            tolerance="0",
            source=(
                "Every checked builder in BUILDER_REGISTRY must reproduce "
                "its committed *.derivation.json byte-for-byte across runs "
                "(drift + error + timeout == 0; bean qou-coyy)."
            ),
        )
        .add_caveat(
            "Per-builder timeout = 600s. A timeout means the builder "
            "is too slow for routine reproducibility checking, NOT "
            "that it is non-deterministic; mark such builders for "
            "audit-only / off-CI verification."
        )
        .add_caveat(
            "Auto-restore: the checker always moves the snapshot back "
            "over the regenerated output, so the working tree is not "
            "mutated by this script. If a check FAILS the regenerated "
            "content is discarded and the original committed content "
            "is preserved."
        )
        .add_caveat(
            "Registry is explicit (BUILDER_REGISTRY) — auto-discovery "
            "would mis-attribute outputs for builders with CLI args. "
            "Add new builders manually to extend coverage."
        )
    )
    w.save()

    if args.strict and fail_count > 0:
        print()
        print(f"FAIL: {fail_count} builder(s) failed reproducibility.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
