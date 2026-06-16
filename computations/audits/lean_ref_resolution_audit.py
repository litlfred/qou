"""I12 audit — content-block `lean.ref` resolution against Lean source.

For every content-block `.ts` with a `lean.ref` URI of the form
`<package>:<Decl.Path>`, attempts the same resolution the export
pipeline performs (per CLAUDE.md §0a):

  1. Sibling lookup     — `<paperDir>/<chapter>/<rootName>.lean`
  2. Lake-root lookup   — `<lakeRoot>/<Decl/Path>.lean`
  3. Grep fallback      — any `.lean` file declaring the named decl

A `lean.ref` "resolves" only if at least one of (1)/(2)/(3) returns
a file that actually declares the named identifier (via `def`,
`theorem`, `lemma`, `proposition`, `class`, `structure`,
`instance`, `axiom`, `abbrev`, or `noncomputable def`).

Emits `lean-ref-resolution-audit.witness.json` with a per-block
classification.  This is the I12 audit promised by the
`local/compute-integration-watcher` skill's pattern catalogue,
operationalising the 305-hit count from the 2026-05-18 idle sweep
([PR #737](https://github.com/litlfred/qou/pull/737)).

Failure modes classified:

  - `unregistered_package`     — the `<package>` prefix is not in
                                 `folio-assistant/schemas/lean-packages.ts`
  - `sibling_missing`          — kind=definition (which schema requires
                                 a sibling) but no sibling `.lean` exists
  - `sibling_no_decl`          — sibling exists but does not declare the
                                 named identifier
  - `lake_root_missing`        — Lake-tree path resolved from the Decl
                                 path does not exist
  - `lake_root_no_decl`        — Lake-tree file exists but does not
                                 declare the named identifier
  - `grep_no_match`            — neither (1) nor (2) hit; full-repo
                                 grep also returns 0 hits
  - `ok`                       — at least one resolution route hit

Note: this is a STATIC text check; it does not run `lake build` or
verify type-correctness.  A `ok` result means "the declaration exists
under the claimed name somewhere reachable"; it does not certify the
declaration is what the .md describes.

Usage:
    python3 computations/lean_ref_resolution_audit.py [--strict]

With --strict, exits non-zero if any non-ok class is observed
(suitable for CI gating once the 305-hit baseline has been brought
down).  Without --strict, returns 0 and reports the breakdown.
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

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from witness_base import WitnessBuilder  # noqa: E402

REPO_ROOT = HERE.parent.parent
CONTENT_ROOT = REPO_ROOT / "content"

# Mirror of folio-assistant/schemas/lean-packages.ts LEAN_PACKAGES.
# Kept inline here because Python doesn't import .ts and the registry
# is small + stable.  See content/pipeline/migrate-lean-refs.ts for
# the JS resolver this audit shadows.
LEAN_PACKAGES = {
    "qou":      {"paperDir": "quantum-observable-universe",
                 "lakeRoot": "content/quantum-observable-universe/lean",
                 "lib": "QOU"},
    "ugb":      {"paperDir": "unital-groebner-bases",
                 "lakeRoot": "content/unital-groebner-bases/lean",
                 "lib": "UGB"},
    "fred2005": {"paperDir": "fred2005-formal-groups",
                 "lakeRoot": "content/fred2005-formal-groups/lean",
                 "lib": "Fred2005"},
}

# Only match `ref: "..."` inside a `lean: { ... }` block, not
# inside `simulator: { ref: ... }` etc.  Multi-line tolerant.
LEAN_REF_RX = re.compile(
    r'lean:\s*\{[^}]*?ref:\s*"([^:"]+):([^"]+)"',
    re.DOTALL,
)
# Block kind is encoded in the builder function name used at the
# `export default <builder>(…)` call site (see content/schema/builders.ts).
# Capture any identifier (rather than a hard-coded list) so newly-added
# builders in `content/schema/builders.ts` automatically flow through —
# the audit's downstream consumers can decide whether each captured
# kind is "provable" / "definition" / "remark" / etc. via their own
# allow-lists.  Older blocks used a `kind: "<name>"` field in the
# manifest object; KIND_LEGACY_RX preserves that fallback.
KIND_RX = re.compile(
    r'^export\s+default\s+([A-Za-z_][A-Za-z_0-9]*)\s*\(',
    re.MULTILINE,
)
KIND_LEGACY_RX = re.compile(r'kind:\s*"([a-z]+)"')

# Lean declaration kinds we recognise as "declaring" a name.  Match
# `def foo`, `theorem foo`, `noncomputable def foo`, etc.  Trailing
# `{` / `(` / `:` / whitespace breaks the boundary.
DECL_KEYWORDS = (
    "def", "theorem", "lemma", "proposition", "corollary",
    "class", "structure", "instance", "axiom", "abbrev",
)


def _decl_rx(decl_path: str) -> re.Pattern:
    """Regex that matches a top-level declaration of `decl_path` in a
    .lean file body.  Accepts any **suffix** of the dotted path —
    i.e. for URI `QOU.QExponential.unique` the file may declare
    `theorem unique` (inside `namespace QOU.QExponential`),
    `theorem QExponential.unique` (inside `namespace QOU`), or
    `theorem QOU.QExponential.unique` (no enclosing namespace).
    Allows `noncomputable` / `private` / `protected` / `partial` /
    `unsafe` prefixes plus zero-or-more leading `@[…]` attribute
    modifiers on the same line (e.g. `@[simp] theorem foo …`)."""
    parts = decl_path.split(".")
    # All non-empty suffixes of the dotted path — longest first so the
    # regex engine prefers the more-qualified match when both apply.
    suffixes = ['.'.join(parts[i:]) for i in range(len(parts))]
    suffixes.sort(key=len, reverse=True)
    alt = "|".join(re.escape(s) for s in suffixes)
    kws = "|".join(DECL_KEYWORDS)
    return re.compile(
        rf'^\s*(?:@\[[^\]]*\]\s*)*'
        rf'(?:(?:noncomputable|private|protected|partial|unsafe)\s+)*'
        rf'(?:{kws})\s+(?:{alt})\b',
        re.MULTILINE,
    )


def _classify_one(ts_path: Path) -> dict[str, Any]:
    """Audit one `.ts` content-block file for lean.ref resolution."""
    try:
        text = ts_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        return {"path": str(ts_path.relative_to(REPO_ROOT)),
                "result": "read_error", "detail": str(e)}

    ref_match = LEAN_REF_RX.search(text)
    if not ref_match:
        return None  # block has no lean.ref — skip silently

    pkg, decl_path = ref_match.group(1), ref_match.group(2)

    kind_match = KIND_RX.search(text) or KIND_LEGACY_RX.search(text)
    kind = kind_match.group(1) if kind_match else "unknown"

    row: dict[str, Any] = {
        "path": str(ts_path.relative_to(REPO_ROOT)),
        "ref": f"{pkg}:{decl_path}",
        "kind": kind,
        "pkg": pkg,
        "decl_path": decl_path,
    }

    if pkg not in LEAN_PACKAGES:
        row["result"] = "unregistered_package"
        return row

    pkg_meta = LEAN_PACKAGES[pkg]

    # The sibling-decl and grep-fallback regexes both accept any
    # suffix of the dotted decl_path (handles `namespace QOU` +
    # `theorem QExponential.unique` style declarations).
    decl_rx = _decl_rx(decl_path)

    # (1) Sibling lookup — same directory, same basename, .lean
    # extension.  The sibling root name is the .ts basename (e.g.
    # `flavor-dressing-functor.ts` → `flavor-dressing-functor.lean`).
    sibling_path = ts_path.with_suffix(".lean")
    sibling_exists = sibling_path.exists()
    sibling_declares = False
    if sibling_exists:
        try:
            sib_text = sibling_path.read_text(encoding="utf-8")
            sibling_declares = bool(decl_rx.search(sib_text))
        except (OSError, UnicodeDecodeError):
            pass
    row["sibling_exists"] = sibling_exists
    row["sibling_declares"] = sibling_declares

    # (2) Lake-root lookup — translate `qou:QOU.A.B.C` to
    # `<lakeRoot>/QOU/A/B/C.lean`.
    lake_path = REPO_ROOT / pkg_meta["lakeRoot"] / (decl_path.replace(".", "/") + ".lean")
    lake_exists = lake_path.exists()
    lake_declares = False
    if lake_exists:
        try:
            lake_text = lake_path.read_text(encoding="utf-8")
            lake_declares = bool(decl_rx.search(lake_text))
        except (OSError, UnicodeDecodeError):
            pass
    row["lake_root_exists"] = lake_exists
    row["lake_root_declares"] = lake_declares

    # Also try (2'): parent of leaf (e.g. `qou:QOU.A.B.foo` → look in
    # `<lakeRoot>/QOU/A/B.lean`).  Some files group multiple decls
    # under one module.
    lake_parent_path = REPO_ROOT / pkg_meta["lakeRoot"] / (
        "/".join(decl_path.split(".")[:-1]) + ".lean"
    )
    lake_parent_declares = False
    if lake_parent_path.exists():
        try:
            lp_text = lake_parent_path.read_text(encoding="utf-8")
            lake_parent_declares = bool(decl_rx.search(lp_text))
        except (OSError, UnicodeDecodeError):
            pass
    row["lake_parent_declares"] = lake_parent_declares

    # (3) Grep fallback — repo-wide ripgrep / grep for the decl
    # keyword + any suffix of the dotted path.  Cheaper than a Lean
    # run, more permissive than (1)/(2).  Suffix alternation lets us
    # catch `theorem Foo.bar` declared inside `namespace QOU`.
    grep_hit = False
    grep_hit_under_lake_root = False
    grep_suffixes = ['.'.join(decl_path.split(".")[i:])
                     for i in range(len(decl_path.split(".")))]
    grep_suffixes.sort(key=len, reverse=True)
    grep_alt = "|".join(re.escape(s) for s in grep_suffixes)
    try:
        # Mirror _decl_rx: accept zero-or-more leading `@[…]`
        # attribute brackets, then any combo of
        # noncomputable/private/protected/partial/unsafe, then the
        # decl keyword + a dotted suffix of the URI's decl_path.
        rg = subprocess.run(
            ["grep", "-rln", "-E",
             rf"^[[:space:]]*(@\[[^]]*\][[:space:]]*)*"
             rf"((noncomputable|private|protected|partial|unsafe)[[:space:]]+)*"
             rf"({'|'.join(DECL_KEYWORDS)})[[:space:]]+({grep_alt})\b",
             "--include=*.lean", str(REPO_ROOT)],
            capture_output=True, text=True, timeout=30,
        )
        if rg.returncode == 0 and rg.stdout.strip():
            grep_hit = True
            hit_paths = rg.stdout.strip().splitlines()
            row["grep_hits"] = hit_paths[:5]
            # If grep finds the decl under the package's Lake root
            # (and the file is part of the Lake build), the URI is
            # resolvable — the lean.ref's purpose is to identify the
            # decl, not to pin it to an exact filename.  This catches
            # the common CamelCase-file-with-snake_case-leaf pattern
            # (e.g. `QOU.MassEndomorphism.delta_max_uniform_bound`
            # actually living in `QOU/MassEndomorphism/DeltaMaxUniformBound.lean`).
            lake_root_abs = str((REPO_ROOT / pkg_meta["lakeRoot"]).resolve())
            for hp in hit_paths:
                if str(Path(hp).resolve()).startswith(lake_root_abs):
                    grep_hit_under_lake_root = True
                    break
    except (subprocess.SubprocessError, OSError):
        pass
    row["grep_hit"] = grep_hit
    row["grep_hit_under_lake_root"] = grep_hit_under_lake_root

    # Classify.
    if sibling_declares or lake_declares or lake_parent_declares:
        row["result"] = "ok"
        if sibling_declares:
            row["resolved_via"] = "sibling"
        elif lake_declares:
            row["resolved_via"] = "lake_root"
        else:
            row["resolved_via"] = "lake_parent"
    elif grep_hit_under_lake_root:
        # The decl is in a Lake-tree file the URI's path didn't match
        # exactly (typically CamelCase-file vs snake_case-leaf), but
        # the decl IS reachable.  Lake build will resolve it.
        row["result"] = "ok"
        row["resolved_via"] = "grep_under_lake_root"
    elif sibling_exists and not sibling_declares:
        row["result"] = "sibling_no_decl"
    elif kind == "definition" and not sibling_exists:
        row["result"] = "sibling_missing"
    elif lake_exists and not lake_declares:
        row["result"] = "lake_root_no_decl"
    elif not lake_exists and grep_hit:
        row["result"] = "lake_root_missing_grep_hit"
    elif not grep_hit:
        row["result"] = "grep_no_match"
    else:
        row["result"] = "lake_root_missing"

    return row


def main() -> int:
    strict = "--strict" in sys.argv

    rows: list[dict[str, Any]] = []
    for ts in sorted(CONTENT_ROOT.rglob("*.ts")):
        # Skip schema / pipeline / generated.
        rel = ts.relative_to(CONTENT_ROOT)
        if rel.parts[0] in ("schema", "pipeline"):
            continue
        if ts.name.endswith(".d.ts"):
            continue
        result = _classify_one(ts)
        if result is None:
            continue
        rows.append(result)

    # Buckets.
    buckets: dict[str, list[str]] = {}
    for r in rows:
        buckets.setdefault(r["result"], []).append(r["path"])

    # Print summary.
    print("=" * 80)
    print(f"I12 audit — content-block lean.ref resolution  ({len(rows)} blocks)")
    print("=" * 80)
    for cls, paths in sorted(buckets.items(), key=lambda x: -len(x[1])):
        print(f"\n  {cls}  ({len(paths)} blocks)")
        for p in paths[:8]:
            print(f"    {p}")
        if len(paths) > 8:
            print(f"    … and {len(paths) - 8} more")
    print()
    print(f"Summary:")
    print(f"  total blocks with lean.ref:   {len(rows)}")
    print(f"  ok (resolves):                {len(buckets.get('ok', []))}")
    print(f"  needs fix (any non-ok):       {sum(len(v) for k, v in buckets.items() if k != 'ok')}")

    # Build witness.
    b = (
        WitnessBuilder("lean-ref-resolution-audit", engine="python")
        .set_description(
            "I12 audit per local/compute-integration-watcher: walk every "
            "content/.../*.ts content-block file with a `lean.ref` URI of the "
            "form `<package>:<Decl.Path>` and attempt the 3-step resolution "
            "the export pipeline performs (sibling → Lake-root → grep). "
            "Classifies each as `ok` or one of six failure modes. Operationalises "
            "the 305-hit I12 count from the 2026-05-18 idle sweep (PR #737)."
        )
        .set_content_block(
            "I12 antipattern (compute-integration-watcher.md §antipatterns)"
        )
        .add_parameter("total_blocks_with_lean_ref", len(rows))
        .add_data("by_result", {k: len(v) for k, v in buckets.items()})
        .add_data("rows", rows)
        .add_assertion(
            name="no_unregistered_package_prefixes",
            computed=1.0 if "unregistered_package" not in buckets else 0.0,
            expected=1.0, tolerance=0.0,
            unit="boolean",
            source="Every lean.ref prefix must appear in LEAN_PACKAGES "
                   "(folio-assistant/schemas/lean-packages.ts).",
        )
        .add_assertion(
            name="ok_count_matches_total_minus_failures",
            computed=float(len(buckets.get("ok", []))),
            expected=float(len(rows)),
            tolerance=0.0,
            unit="count (gates only at full closure)",
            source="Closure gate: when this passes, every content-block "
                   "lean.ref resolves to an actual declaration.  Currently "
                   "informational; the production-side fix is a follow-up "
                   "PR per the watcher's §5j spawn protocol.",
        )
    )
    out = b.save()
    print(f"\nWitness: {out}")

    if strict and any(k != "ok" for k in buckets):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
