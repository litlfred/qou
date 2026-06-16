"""I8 audit — substrate-pure scripts leaking float64.

A script is "substrate-pure" if its docstring claims canonical /
substrate-pure / 50-dps / mpmath precision.  Such a script should
not silently degrade derived quantities through float64 — yet
several historical scripts do precisely this (e.g. `float(x)` on
a 50-dps `mp.mpf`, or comparing two mpf values via `==`).

The I8 antipattern in `local/compute-integration-watcher`:

  A substrate-pure script does any of:
    - `np.float64(<derived>)`
    - `float(<derived>)` cast on a non-input mpf
    - `f"{x:.3f}"` / `f"{x:.6e}"` precision-clipping on a derived
      mpf used in any subsequent computation
    - `<a> == <b>` comparison on derived mpf values

The audit walks every Python script and:

  1. Detects substrate-pure-claim banner (docstring / module
     comment).
  2. For banner-bearing scripts, greps the body for the four
     antipattern shapes.
  3. Classifies the script + emits per-line evidence.

Limitations:
  - Static — does not actually run the script; some `float(x)`
    casts that re-enter mpmath via `mp.mpf(str(x))` are false-
    positive.  Mark `false_positive_candidate` rather than
    `violation` when the offending line is followed within 3
    lines by `mp.mpf(...)` re-wrapping.
  - Witness-emit `float(x)` calls (final-step JSON serialization)
    are recognised — when the cast occurs inside a `.add_data(`
    or `.add_parameter(` builder call, classified as
    `ok_witness_emit`.

Emits `float64-leak-audit.witness.json`.

Usage:
    python3 folio-assistant/computations/float64_leak_audit.py [--strict]
"""



from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import re
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from witness_base import WitnessBuilder  # noqa: E402

REPO_ROOT = HERE.parent.parent

# Banners that flag a script as substrate-pure / canonical.  Match
# in the module docstring (first """ ... """).
SUBSTRATE_BANNER_PATTERNS = (
    r"substrate.{0,15}pure",
    r"canonical.{0,15}precision",
    r"50.{0,5}dps",
    r"mpmath.{0,30}canonical",
    r"q-?canonical",
    r"\bcanonical\b.*\b(?:probe|production)\b",
)

# Antipattern shapes.  Each tuple: (label, regex, optional FP guard).
# Regex matches the suspicious LINE (not entire file).
ANTIPATTERN_RX = (
    ("np_float64",      re.compile(r"\bnp\.float64\s*\(")),
    ("float_cast",      re.compile(r"\bfloat\s*\(")),
    ("fstring_precision_f", re.compile(r'f["\'][^"\']*\{[^}]*:\s*\.\d+f\}')),
    ("fstring_precision_e", re.compile(r'f["\'][^"\']*\{[^}]*:\s*\.\d+e\}')),
    ("mpf_eq_compare",  re.compile(r"\bmp\.mpf\s*\([^)]+\)\s*==\s*")),
)

# Witness-emit recognition — when the suspicious line is inside or
# adjacent to a builder call, classify as ok.
BUILDER_CONTEXT_RX = re.compile(r"\.(add_data|add_parameter|add_assertion)\b")
# Display-context recognition — print(...) calls, mp.nstr(...) wraps,
# and other formatting-only contexts.  These don't leak precision into
# downstream computation.
DISPLAY_CONTEXT_RX = re.compile(r"\b(print|mp\.nstr|logger|warnings\.warn|sys\.stderr\.write)\b")
# Comparison / sort / dict-key contexts — float(x) used here doesn't
# propagate into mpmath computation.  Matches: `< N`, `> N`, `< 1e-N`,
# `key=lambda ...`, `abs(float(...))`, `"key": float(...)` (raw dict),
# `assert ...`, and ppm/percent-display patterns.
COMPARISON_CONTEXT_RX = re.compile(
    r"(?:(?:<|>|<=|>=|==|!=)\s*\d|key\s*=\s*lambda|\bassert\b|\bppm\b|_pct\b|\bgap_[a-z]\b|reverse=True)"
)
# Dict-value serialization — `"key": float(x)` writes the value into a
# (string-keyed) dict, almost always for witness/JSON output, not a compute
# input (refinement, 2026-06-16: this was the dominant remaining I8 FP class —
# `"B_arch_MeV": float(B_arch)` etc.).
DICT_VALUE_RX = re.compile(r"""["'][^"']*["']\s*:\s*[^,]*\bfloat\s*\(""")
# `# noqa: I8 — <reason>` explicit triage marker.
NOQA_I8_RX = re.compile(r"#\s*noqa:\s*I8\b", re.IGNORECASE)
# Mp re-wrap on next line: `mp.mpf(str(...))` indicates the float
# cast is just a stringification step, not a precision leak.
MP_REWRAP_RX = re.compile(r"\bmp\.mpf\s*\(\s*str\s*\(")


def _classify_line_context(lines: list[str], idx: int) -> str:
    """Look at ±3 lines around idx for false-positive cues.
    Returns:
        - 'ok_noqa' if line carries `# noqa: I8 — <reason>` marker
        - 'ok_witness_emit' if inside a builder call
        - 'ok_display' if inside a print / nstr / logger call
        - 'ok_comparison' if a comparison / sort / assert context
        - 'false_positive_candidate' if re-wrapped via mp.mpf(str(...))
        - 'violation' otherwise.
    """
    if NOQA_I8_RX.search(lines[idx]):
        return "ok_noqa"
    # Check the same line first for display context — print / nstr
    # wraps on the same line as the float cast are unambiguous.
    if DISPLAY_CONTEXT_RX.search(lines[idx]):
        return "ok_display"
    if COMPARISON_CONTEXT_RX.search(lines[idx]):
        return "ok_comparison"
    if DICT_VALUE_RX.search(lines[idx]):
        return "ok_witness_emit"  # `"key": float(x)` — serialization, not input
    # Multi-line context window — catches f-strings split across
    # print(\n  f"..."\n) and similar.
    start = max(0, idx - 3)
    end = min(len(lines), idx + 4)
    window = "\n".join(lines[start:end])
    if DISPLAY_CONTEXT_RX.search(window):
        return "ok_display"
    if BUILDER_CONTEXT_RX.search(window):
        return "ok_witness_emit"
    if MP_REWRAP_RX.search(window):
        return "false_positive_candidate"
    return "violation"


def _blank_triple_quoted(text: str) -> str:
    """Return `text` with triple-quoted-string and comment CONTENT replaced
    by spaces, preserving newlines/columns (line numbers unchanged). Single-
    and double-quoted strings (incl. f-strings) are LEFT INTACT so the
    f-string precision patterns still match.

    Uses Python's tokenizer so it is robust to every edge case the simpler
    regex/toggle approaches missed — single-line `\"\"\"...\"\"\"`, an
    unbalanced `\"\"\"` inside a comment, etc. (Gemini #2379). Falls back to
    a regex blank only if the source does not tokenize."""
    import io
    import tokenize as _tok

    def _is_triple(s: str) -> bool:
        body = s.lstrip("rbfRBFuU")
        return body.startswith('"""') or body.startswith("'''")

    try:
        toks = list(_tok.generate_tokens(io.StringIO(text).readline))
    except (_tok.TokenError, IndentationError, SyntaxError, ValueError):
        return re.sub(r'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'',
                      lambda m: re.sub(r"[^\n]", " ", m.group(0)), text)

    grid = [list(line) for line in text.splitlines(keepends=True)]
    for tok in toks:
        if tok.type == _tok.COMMENT or (
            tok.type == _tok.STRING and _is_triple(tok.string)
        ):
            (sr, sc), (er, ec) = tok.start, tok.end
            for r in range(sr, er + 1):
                ri = r - 1
                if ri >= len(grid):
                    continue
                c0 = sc if r == sr else 0
                c1 = ec if r == er else len(grid[ri])
                for c in range(c0, min(c1, len(grid[ri]))):
                    if grid[ri][c] != "\n":
                        grid[ri][c] = " "
    return "".join("".join(r) for r in grid)


def _classify_script(path: Path) -> dict[str, Any] | None:
    """Audit one Python script for I8 violations."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    if "import" not in text:
        return None

    # Check for substrate-pure banner in the module docstring.
    doc_match = re.search(r'^"""(.*?)"""', text, re.DOTALL)
    docstring = doc_match.group(1) if doc_match else ""
    has_banner = any(
        re.search(p, docstring, re.IGNORECASE) for p in SUBSTRATE_BANNER_PATTERNS
    )
    if not has_banner:
        return None  # only audit scripts claiming substrate purity

    rel = path.relative_to(REPO_ROOT)
    row: dict[str, Any] = {
        "path": str(rel),
        "substrate_banner": True,
    }

    lines = text.splitlines()
    # Scan a copy with triple-quoted-string CONTENT blanked, so a `float(`
    # inside a docstring (the dominant I8 false-positive class) is not
    # matched — covers both multi-line and single-line `"""..."""` strings.
    # f-strings (single/double quoted) are preserved so their precision
    # patterns still match. Snippets/context use the ORIGINAL lines.
    scan_lines = _blank_triple_quoted(text).splitlines()
    hits: list[dict[str, Any]] = []

    for i, line in enumerate(lines):
        # Strip comments first (use the docstring-blanked variant for matching).
        scan_part = re.sub(r"#.*$", "", scan_lines[i]) if i < len(scan_lines) else ""
        for label, rx in ANTIPATTERN_RX:
            if rx.search(scan_part):
                # Classify in context.
                ctx = _classify_line_context(lines, i)
                hits.append({
                    "line_number": i + 1,
                    "pattern": label,
                    "context": ctx,
                    "code_snippet": re.sub(r"#.*$", "", line).strip()[:120],
                })

    row["hit_count"] = len(hits)
    row["violation_count"] = sum(1 for h in hits if h["context"] == "violation")
    row["display_count"] = sum(1 for h in hits if h["context"] == "ok_display")
    row["comparison_count"] = sum(1 for h in hits if h["context"] == "ok_comparison")
    row["noqa_count"] = sum(1 for h in hits if h["context"] == "ok_noqa")
    row["witness_emit_count"] = sum(
        1 for h in hits if h["context"] == "ok_witness_emit"
    )
    row["false_positive_count"] = sum(
        1 for h in hits if h["context"] == "false_positive_candidate"
    )
    row["hits"] = hits[:20]  # cap for witness size

    if row["violation_count"] > 0:
        row["result"] = "i8_violation"
    elif (row["witness_emit_count"] > 0
          or row["display_count"] > 0
          or row["false_positive_count"] > 0):
        row["result"] = "ok_with_display_or_fp"
    else:
        row["result"] = "ok_no_leaks"
    return row


def main() -> int:
    strict = "--strict" in sys.argv

    rows: list[dict[str, Any]] = []
    total_substrate_scripts = 0
    # Scan the whole compute tree (HERE.parent = computations/), not just
    # this audit's own dir. Pre-reorg this script lived in the compute dir
    # and scanned its siblings via HERE.glob; after the move to
    # computations/audits/ that glob saw only 2 files (a vacuous green).
    # Walk computations/ recursively, skipping _deprecated.
    for py in sorted((HERE.parent).rglob("*.py")):
        if "_deprecated" in py.parts:
            continue
        if py.name.startswith("_"):
            continue
        if py.name == "float64_leak_audit.py":
            continue
        result = _classify_script(py)
        if result is None:
            continue
        rows.append(result)
        total_substrate_scripts += 1

    buckets: dict[str, list[dict[str, Any]]] = {}
    for r in rows:
        buckets.setdefault(r["result"], []).append(r)

    # Sort violation bucket by violation count descending.
    if "i8_violation" in buckets:
        buckets["i8_violation"].sort(key=lambda r: -r["violation_count"])

    print("=" * 80)
    print(f"I8 audit — float64 leaks in substrate-pure scripts")
    print(f"({total_substrate_scripts} scripts carry a substrate-pure banner)")
    print("=" * 80)
    for cls in ("i8_violation", "ok_with_display_or_fp", "ok_no_leaks"):
        rs = buckets.get(cls, [])
        if not rs:
            continue
        print(f"\n  {cls}  ({len(rs)} scripts)")
        for r in rs[:12]:
            extras = ""
            if r["result"] == "i8_violation":
                extras = f"  {r['violation_count']} violation(s)"
            print(f"    {r['path']:<70s}{extras}")
        if len(rs) > 12:
            print(f"    … and {len(rs) - 12} more")
    print()
    print(f"Summary:")
    print(f"  substrate-pure-banner scripts: {total_substrate_scripts}")
    print(f"  i8_violation:                  {len(buckets.get('i8_violation', []))}")
    print(f"  ok_with_display_or_fp:         {len(buckets.get('ok_with_display_or_fp', []))}")
    print(f"  ok_no_leaks:                   {len(buckets.get('ok_no_leaks', []))}")

    b = (
        WitnessBuilder("float64-leak-audit", engine="python")
        .set_description(
            "I8 audit per local/compute-integration-watcher: scripts whose "
            "docstrings claim substrate-pure / canonical / 50-dps precision "
            "are scanned for float64 leaks — `np.float64(...)`, `float(...)` "
            "casts on derived mpf values, f-string precision clipping, and "
            "`==` comparison on mpf values. Antipattern shapes are matched "
            "against the four catalogue items. False-positive guards: lines "
            "inside builder `add_data` / `add_parameter` / `add_assertion` "
            "calls are classified as `ok_witness_emit` (final-step JSON "
            "serialization is expected); lines followed within 3 by "
            "`mp.mpf(str(...))` re-wrap are `false_positive_candidate`."
        )
        .set_content_block(
            "I8 antipattern (compute-integration-watcher.md §antipatterns)"
        )
        .add_parameter("substrate_banner_scripts_total", total_substrate_scripts)
        .add_data("by_result", {k: len(v) for k, v in buckets.items()})
        .add_data("rows", rows)
        .add_assertion(
            name="no_i8_violations",
            computed=1.0 if "i8_violation" not in buckets else 0.0,
            expected=1.0, tolerance=0.0,
            unit="boolean (1.0 = no substrate-pure script leaks float64)",
            source="Closure gate: when this passes, every substrate-pure-"
                   "banner script keeps its derived mpf values through "
                   "the final witness emit without precision loss.",
        )
    )
    out = b.save()
    print(f"\nWitness: {out}")

    if strict and "i8_violation" in buckets:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
