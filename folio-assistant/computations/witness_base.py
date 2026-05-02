# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""
Unified witness infrastructure for QOU computation scripts.

Every Python computation that produces a witness statement should use
this module to ensure consistent structure, commit SHA tracking, and
content-block integration.

Usage:
    from witness_base import WitnessBuilder

    w = WitnessBuilder("my-computation", engine="sympy")
    w.set_description("Computes foo from bar")
    w.add_assertion("Vol(4_1)", computed=2.0298, expected=2.0298, tolerance=1e-10, source="SnapPy")
    w.add_parameter("q", q0)
    w.add_data("extra_result", {"key": "value"})
    w.set_content_block("prop:my-proposition")
    w.save()  # writes my-computation.witness.json

The output conforms to the ComputationWitness interface in
folio-assistant/schemas/types.ts.

@module folio-assistant/computations/witness_base
"""

import hashlib
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional, Union


# ── Git helpers ──────────────────────────────────────────────────

def _repo_root() -> Path:
    """Find the repository root (walk up from this file)."""
    d = Path(__file__).resolve().parent
    while d != d.parent:
        if (d / ".git").exists():
            return d
        d = d.parent
    return Path(__file__).resolve().parent.parent.parent


def _git_head_sha() -> str:
    """Return the current HEAD commit SHA."""
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=str(_repo_root()),
            stderr=subprocess.DEVNULL,
        ).decode().strip()
    except Exception:
        return "unknown"


def _git_file_sha(path: str) -> str:
    """Return the last commit SHA that touched a given file. `git log` exits
    cleanly with empty stdout for paths that have never been committed
    (e.g. a script generating its first witness pre-commit), so empty
    output is also normalised to "unknown" — matching `_git_head_sha`.

    Per Copilot review on PR #484: never return an ambiguous empty
    string; "unknown" is the canonical sentinel and serialises into
    witness JSON as a clear marker rather than `""`."""
    try:
        sha = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", path],
            cwd=str(_repo_root()),
            stderr=subprocess.DEVNULL,
        ).decode().strip()
        return sha if sha else "unknown"
    except Exception:
        return "unknown"


def file_content_hash(path: str, length: int = 12) -> str:
    """SHA-256 content hash (hex prefix) of a file, matching lean-witness.ts."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return hashlib.sha256(content.encode("utf-8")).hexdigest()[:length]


# ── Assertion type ───────────────────────────────────────────────

class Assertion:
    """A single named claim with computed vs expected values."""

    def __init__(
        self,
        name: str,
        computed: Union[float, str],
        expected: Union[float, str],
        tolerance: Optional[float] = None,
        unit: Optional[str] = None,
        source: Optional[str] = None,
    ):
        self.name = name
        self.computed = computed
        self.expected = expected
        self.tolerance = tolerance
        self.unit = unit
        self.source = source

    @property
    def passed(self) -> bool:
        if self.tolerance is None:
            return self.computed == self.expected
        try:
            return abs(float(self.computed) - float(self.expected)) <= self.tolerance
        except (ValueError, TypeError):
            return str(self.computed) == str(self.expected)

    def to_dict(self) -> dict:
        d: dict[str, Any] = {
            "name": self.name,
            "computed": self.computed,
            "expected": self.expected,
            "passed": self.passed,
        }
        if self.tolerance is not None:
            d["tolerance"] = self.tolerance
        if self.unit:
            d["unit"] = self.unit
        if self.source:
            d["source"] = self.source
        return d


# ── WitnessBuilder ───────────────────────────────────────────────

class WitnessBuilder:
    """
    Build a structured witness JSON conforming to ComputationWitness.

    Automatically captures:
      - Git commit SHA (HEAD and script file)
      - Script content hash (for staleness detection)
      - Timestamp
      - Engine and version
      - Execution duration

    Parameters
    ----------
    name : str
        Computation name (becomes the filename: `<name>.witness.json`).
    engine : str
        One of: "sympy", "mpmath", "snappea", "sage", "numpy", "python".
    engine_version : str, optional
        Explicit version string. Auto-detected if omitted.
    output_dir : str or Path, optional
        Directory for the witness file. Defaults to the directory of
        the calling script.
    """

    def __init__(
        self,
        name: str,
        engine: str = "python",
        engine_version: Optional[str] = None,
        output_dir: Optional[Union[str, Path]] = None,
    ):
        self.name = name
        self.engine = engine
        self.engine_version = engine_version or self._detect_version(engine)
        self._start_time = time.monotonic()

        # Get caller frame once for both output dir and script path
        import inspect
        caller_frame = inspect.stack()[1]
        caller_file = Path(caller_frame.filename).resolve()
        self._script_path = caller_file

        # Determine output directory
        if output_dir:
            self._output_dir = Path(output_dir)
        else:
            self._output_dir = caller_file.parent

        self.description: Optional[str] = None
        self.content_block: Optional[str] = None
        self.assertions: list[Assertion] = []
        self.parameters: dict[str, Any] = {}
        self.data: dict[str, Any] = {}
        self.caveats: list[str] = []

    @staticmethod
    def _detect_version(engine: str) -> str:
        """Auto-detect engine version."""
        try:
            if engine == "sympy":
                import sympy
                return f"sympy {sympy.__version__}"
            elif engine == "mpmath":
                import mpmath
                return f"mpmath {mpmath.__version__}"
            elif engine in ("snappea", "snappy"):
                import snappy
                return f"snappy {snappy.version()}"
            elif engine == "sage":
                return "sage (version not detected)"
            elif engine == "numpy":
                import numpy
                return f"numpy {numpy.__version__}"
            else:
                return f"python {sys.version.split()[0]}"
        except ImportError:
            return f"{engine} (not installed)"

    def set_description(self, desc: str) -> "WitnessBuilder":
        """Set the human-readable description."""
        self.description = desc
        return self

    def set_content_block(self, label: str) -> "WitnessBuilder":
        """Link this witness to a content block label (e.g. 'prop:foo')."""
        self.content_block = label
        return self

    def add_assertion(
        self,
        name: str,
        computed: Union[float, str],
        expected: Union[float, str],
        tolerance: Optional[float] = None,
        unit: Optional[str] = None,
        source: Optional[str] = None,
    ) -> "WitnessBuilder":
        """Add a named assertion."""
        self.assertions.append(
            Assertion(name, computed, expected, tolerance, unit, source)
        )
        return self

    def add_parameter(self, key: str, value: Any) -> "WitnessBuilder":
        """Record an input parameter."""
        self.parameters[key] = value
        return self

    def add_data(self, key: str, value: Any) -> "WitnessBuilder":
        """Attach arbitrary computation data."""
        self.data[key] = value
        return self

    def add_caveat(self, text: str) -> "WitnessBuilder":
        """Add a caveat or limitation note."""
        self.caveats.append(text)
        return self

    def is_fresh(self) -> bool:
        """Return True if an existing witness JSON on disk records the
        same script content hash as the current source.

        Use this to short-circuit expensive recomputations::

            w = WitnessBuilder("my-computation", engine="sympy")
            if w.is_fresh():
                print(f"✓ {w.name}.witness.json fresh; skipping")
                return
            ... # expensive compute
            w.add_assertion(...)
            w.save()

        Returns False if the witness file does not exist, is malformed,
        or records a different `scriptHash`.
        """
        out_path = self._output_dir / f"{self.name}.witness.json"
        if not out_path.is_file():
            return False
        try:
            with out_path.open("r", encoding="utf-8") as f:
                existing = json.load(f)
        except (json.JSONDecodeError, OSError):
            return False
        current_hash = file_content_hash(str(self._script_path))
        return existing.get("scriptHash") == current_hash

    def build(self) -> dict:
        """Build the witness dictionary (without writing to disk)."""
        duration_ms = int((time.monotonic() - self._start_time) * 1000)
        head_sha = _git_head_sha()
        script_sha = _git_file_sha(str(self._script_path))
        script_hash = file_content_hash(str(self._script_path))

        all_passed = all(a.passed for a in self.assertions)

        witness: dict[str, Any] = {
            # ── Structured fields (ComputationWitness interface) ──
            "engine": self.engine,
            "engineVersion": self.engine_version,
            "computedAt": datetime.now(timezone.utc).isoformat(),
            "commitSha": head_sha,
            "assertions": [a.to_dict() for a in self.assertions],
            "allPassed": all_passed,
            "durationMs": duration_ms,
            # ── Extended fields for staleness tracking ──
            "computation": self.name,
            "scriptFile": self._script_path.name,
            "scriptHash": script_hash,
            "scriptCommitSha": script_sha,
        }

        if self.description:
            witness["description"] = self.description
        if self.content_block:
            witness["contentBlock"] = self.content_block
        if self.parameters:
            witness["parameters"] = self.parameters
        if self.data:
            witness["data"] = self.data
        if self.caveats:
            witness["caveats"] = self.caveats

        return witness

    def save(self, extra: Optional[dict] = None) -> Path:
        """Build and write the witness JSON file. Returns the path."""
        witness = self.build()
        if extra:
            witness.update(extra)

        out_path = self._output_dir / f"{self.name}.witness.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(witness, f, indent=2, ensure_ascii=False, default=str)
            f.write("\n")

        print(f"✓ Witness: {out_path.name}  "
              f"({len(self.assertions)} assertions, "
              f"{'all passed' if witness['allPassed'] else 'FAILURES'})")

        return out_path


# ── Staleness checker ────────────────────────────────────────────

def check_witness_staleness(witness_path: str) -> dict:
    """
    Check if a witness JSON is stale relative to its script.

    Returns dict with:
      stale: bool
      reason: str (if stale)
      scriptHash: current vs recorded
      commitSha: current vs recorded
    """
    with open(witness_path, "r") as f:
        witness = json.load(f)

    result: dict[str, Any] = {
        "witnessFile": os.path.basename(witness_path),
        "stale": False,
    }

    # Check script hash
    script_file = witness.get("scriptFile")
    if script_file:
        script_path = os.path.join(os.path.dirname(witness_path), script_file)
        if os.path.exists(script_path):
            current_hash = file_content_hash(script_path)
            recorded_hash = witness.get("scriptHash")
            result["currentScriptHash"] = current_hash
            result["recordedScriptHash"] = recorded_hash
            if recorded_hash and current_hash != recorded_hash:
                result["stale"] = True
                result["reason"] = "script content changed since witness"
                return result

    # Check commit SHA (informational, not staleness)
    #
    # The commit SHA records WHEN the witness was generated, but doesn't
    # determine staleness. A new commit that doesn't touch the script
    # doesn't invalidate the witness. The scriptHash check above is the
    # authoritative staleness signal — if the script content is unchanged,
    # the witness is still valid regardless of intervening commits.
    commit_sha = witness.get("commitSha")
    if commit_sha and commit_sha != "unknown":
        current_head = _git_head_sha()
        result["currentCommitSha"] = current_head
        result["recordedCommitSha"] = commit_sha

    return result


# ── CLI ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Witness infrastructure utilities")
    sub = parser.add_subparsers(dest="command")

    # check-stale
    cs = sub.add_parser("check-stale", help="Check if a witness is stale")
    cs.add_argument("witness_file", help="Path to .witness.json")

    # check-all
    ca = sub.add_parser("check-all", help="Check all witnesses for staleness")

    args = parser.parse_args()

    if args.command == "check-stale":
        result = check_witness_staleness(args.witness_file)
        print(json.dumps(result, indent=2))
        sys.exit(1 if result["stale"] else 0)

    elif args.command == "check-all":
        comp_dir = Path(__file__).resolve().parent
        witnesses = sorted(comp_dir.glob("*.witness.json"))
        stale_count = 0
        for wf in witnesses:
            result = check_witness_staleness(str(wf))
            icon = "🔄" if result["stale"] else "✓"
            reason = f" — {result['reason']}" if result.get("reason") else ""
            print(f"  {icon} {wf.name}{reason}")
            if result["stale"]:
                stale_count += 1
        print(f"\n{len(witnesses) - stale_count} current, {stale_count} stale — {len(witnesses)} total")

    else:
        parser.print_help()
