#!/usr/bin/env python3
"""NEGATIVE-finding guard: block PURGED non-canonical forms from
re-entering production compute.

Motivation
----------
The framework has repeatedly seen a non-canonical form get purged
(with a documented NEGATIVE finding) and then *silently re-enter*
production via a sibling branch. Concretely:

  - `lambda_scale_yekutieli_extended` (the Yekutieli per-cell
    `λ_Y = λ_A − G·h²` correction) was falsified by the S₄↓S₃
    bijection (κ = +0.5, not −G) in PR #985, yet a later sibling
    wired it back into the production proton script; it had to be
    purged a *second* time in PR #1027.
  - `lambda_scale_family_a` was removed in PR #1089 under the owner
    directive "no lambda-scale ANYWHERE in production" (λ_scale was
    absorbed into the per-knot `VolDensity(K)` evaluation, PR #1080),
    but the symbol kept reappearing.

A purge is only durable if a guard *keeps it purged*. This audit is
that guard: it walks production compute and fails (under `--strict`)
if any production script **imports, defines, or uses** a banned
purged form.

Why AST, not grep
-----------------
The honest historical record *mentions* these symbols by name in
comments and docstrings ("the legacy `lambda_scale_family_a` alias
was removed 2026-05-24…"). A text grep flags those false positives.
We parse each file with `ast` instead: comments are dropped and
docstrings/registry strings become `ast.Constant` nodes, so only a
genuine `import` / `def` / `Name` reference — i.e. real code that
would resurrect the form — is flagged. This audit's own banned
registry (string literals below) is therefore invisible to itself.

Banned registry
----------------
Narrow and provenance-backed. We do NOT ban:
  - the Yekutieli non-abelian Stokes functor (canonical for most of
    the paper — only the empirical `−G·h²` *correction* is purged);
  - `linking_weight_family_a` (the PROVED Family A replacement);
  - `y_lambda_*` / `delta_lambda_*` (canonical Frobenius weights y_λ
    and the Δ_λ binding-closure gate — distinct from `lambda_scale`);
  - the module FILENAME `lambda_scale_all_c_i_family_a.py` (canonical
    Family A script; it exports `linking_weight_family_a`).

Run:
    python3 noncanonical_reentry_audit.py [--strict]

Emits `noncanonical-reentry-audit.witness.json`.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import argparse
import ast
import sys
from pathlib import Path

# `_path_bridge` (imported above) already puts the computations/ root and
# every cluster subdir — including substrate/, where witness_base lives —
# on sys.path. No further import-time path mutation is needed (Copilot
# review, PR #1819: keep import side-effects to the single bridge insert).
HERE = Path(__file__).resolve().parent
COMPUTE_ROOT = HERE.parent

# ---------------------------------------------------------------------------
# Banned registry — each entry carries reason + purge provenance so the
# witness is self-documenting and a reviewer can trace every ban.
# ---------------------------------------------------------------------------

BANNED_SYMBOLS = [
    {
        "symbol": "lambda_scale_yekutieli_extended",
        "reason": (
            "Yekutieli per-cell curvature correction λ_Y = λ_A − G·h². "
            "Falsified by the S₄↓S₃ half-symmetric bijection (κ = +0.5, "
            "not −G) — a substrate-q₀ numerical coincidence, not a "
            "categorical theorem. The Yekutieli non-abelian Stokes "
            "functor itself stays canonical; only this empirical "
            "correction is purged."
        ),
        "purged_by": "PR #985 (NEGATIVE) / PR #1027 (production revert)",
        "canonical_replacement": "linking_weight_family_a (Family A, PROVED Wedderburn identity)",
    },
    {
        "symbol": "lambda_scale_family_a",
        "reason": (
            "Legacy lambda-scale alias. Owner directive 2026-05-24: "
            "'no lambda-scale ANYWHERE in production'. λ_scale was "
            "absorbed into the per-knot VolDensity(K) evaluation."
        ),
        "purged_by": "PR #1080 (absorb into VolDensity) / PR #1089 (alias removal)",
        "canonical_replacement": "linking_weight_family_a / vol_density_borromean",
    },
]

BANNED_MODULES = [
    {
        "module": "lambda_yekutieli_extended_borromean",
        "reason": (
            "Purged Yekutieli-extended driver script (quarantined in "
            "_deprecated/yekutieli-purged/). Importing it re-introduces "
            "the falsified −G·h² production refinement."
        ),
        "purged_by": "commit 71d674da1 (2026-05-24)",
    },
]

# Catch-all: the owner directive bans the entire lambda-scale family of
# *symbols* from production. `linking_weight_family_a` (canonical) has no
# such prefix, so this never fires on canonical code. It applies only to
# imported/defined SYMBOLS — module FILENAMES that retain the historical
# `lambda_scale_` prefix are unaffected (see BANNED_MODULES exactness).
BANNED_SYMBOL_PREFIX = "lambda_scale_"

# Directories that are NOT production compute (exploratory / quarantined /
# generated). Re-entry is only meaningful for production.
EXCLUDED_DIRS = {
    "_deprecated",      # quarantined purged scripts
    "probes",           # exploratory probes (allowed to reference banned forms)
    "script-qa",        # JSON sidecars (no .py, but skip anyway)
    "__pycache__",
    "data",
}

# This guard itself (its registry strings are ast.Constant, so already
# invisible — but skip by name for clarity).
SELF_NAME = "noncanonical_reentry_audit.py"


def _symbol_banned(name: str) -> dict | None:
    """Return a ban record if `name` is a banned production symbol."""
    for e in BANNED_SYMBOLS:
        if name == e["symbol"]:
            return {"kind": "exact-symbol", **e}
    if name.startswith(BANNED_SYMBOL_PREFIX):
        return {
            "kind": "lambda-scale-prefix",
            "symbol": name,
            "reason": (
                "Owner directive 2026-05-24: 'no lambda-scale ANYWHERE in "
                "production'. Any `lambda_scale_*` symbol is banned; use "
                "linking_weight_family_a / VolDensity(K) instead."
            ),
            "purged_by": "PR #1080 / #1089 (lambda-scale family)",
            "canonical_replacement": "linking_weight_family_a / vol_density_borromean",
        }
    return None


def _module_banned(name: str) -> dict | None:
    """Return a ban record if `name` is a banned purged module."""
    if name is None:
        return None
    # Tolerate dotted / relative module paths — match the final component.
    leaf = name.rsplit(".", 1)[-1]
    for e in BANNED_MODULES:
        if leaf == e["module"]:
            return {"kind": "purged-module", **e}
    return None


def audit_file(path: Path) -> list[dict]:
    """AST-scan one production file; return a list of violation dicts."""
    text = path.read_text(errors="replace")
    try:
        tree = ast.parse(text, filename=str(path))
    except SyntaxError as exc:
        return [{
            "kind": "parse-error",
            "line": getattr(exc, "lineno", 0) or 0,
            "symbol": "",
            "reason": f"could not parse: {exc.msg}",
        }]

    rel = str(path.relative_to(COMPUTE_ROOT))
    violations: list[dict] = []

    for node in ast.walk(tree):
        # `import X` / `import X as Y` — banned module imported directly, OR
        # a banned symbol used as a top-level module name (e.g. `import
        # lambda_scale_family_a`), OR a non-banned module aliased to a
        # banned name (`import x as lambda_scale_family_a`). Cover all
        # three (Gemini + Copilot review, PR #1819).
        if isinstance(node, ast.Import):
            for alias in node.names:
                rec = _module_banned(alias.name) or _symbol_banned(alias.name)
                if rec:
                    violations.append({
                        "kind": "import-module",
                        "line": node.lineno,
                        "symbol": alias.name,
                        "ban": rec,
                    })
                if alias.asname:
                    rec_as = _symbol_banned(alias.asname) or _module_banned(alias.asname)
                    if rec_as:
                        violations.append({
                            "kind": "import-alias",
                            "line": node.lineno,
                            "symbol": alias.asname,
                            "ban": rec_as,
                        })

        # `from M import S [as A]` — banned module OR banned symbol.
        elif isinstance(node, ast.ImportFrom):
            mod_rec = _module_banned(node.module)
            if mod_rec:
                violations.append({
                    "kind": "import-from-module",
                    "line": node.lineno,
                    "symbol": node.module or "",
                    "ban": mod_rec,
                })
            for alias in node.names:
                # A banned MODULE can also be pulled in as a symbol from a
                # parent package — `from pkg import
                # lambda_yekutieli_extended_borromean` — so check BOTH the
                # symbol registry and the module registry (Gemini review,
                # PR #1819: ImportFrom module-as-symbol bypass).
                rec = _symbol_banned(alias.name) or _module_banned(alias.name)
                if rec:
                    violations.append({
                        "kind": "import-symbol",
                        "line": node.lineno,
                        "symbol": alias.name,
                        "ban": rec,
                    })
                if alias.asname:
                    rec_as = _symbol_banned(alias.asname) or _module_banned(alias.asname)
                    if rec_as:
                        violations.append({
                            "kind": "import-alias",
                            "line": node.lineno,
                            "symbol": alias.asname,
                            "ban": rec_as,
                        })

        # `def lambda_scale_X(...)` / `class lambda_scale_X` — re-defining a
        # banned form (Gemini review, PR #1819: ClassDef parallels FunctionDef).
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            rec = _symbol_banned(node.name)
            if rec:
                violations.append({
                    "kind": "def",
                    "line": node.lineno,
                    "symbol": node.name,
                    "ban": rec,
                })

        # Bare reference / call to a banned symbol — `lambda_scale_family_a(Q)`
        # without an explicit import (e.g. brought in by a glob import), or
        # any other `lambda_scale_*` name (owner directive). Exact registry
        # + prefix (Copilot review, PR #1819).
        elif isinstance(node, ast.Name):
            rec = _symbol_banned(node.id)
            if rec:
                violations.append({
                    "kind": "name-use",
                    "line": node.lineno,
                    "symbol": node.id,
                    "ban": rec,
                })

        # Attribute access `mod.lambda_scale_family_a(...)` — a banned form
        # resurrected via `import mod; mod.<banned>(...)` rather than a direct
        # import (Copilot review, PR #1819). Exact registry + prefix.
        elif isinstance(node, ast.Attribute):
            rec = _symbol_banned(node.attr)
            if rec:
                violations.append({
                    "kind": "attribute-use",
                    "line": node.lineno,
                    "symbol": node.attr,
                    "ban": rec,
                })

        # Keyword-argument NAME at a call site `foo(lambda_scale_family_a=v)`
        # — the value is being passed in under the banned form's name
        # (Gemini review, PR #1819, high). `node.arg` is None for **kwargs
        # spread; skip those.
        elif isinstance(node, ast.keyword) and node.arg:
            rec = _symbol_banned(node.arg)
            if rec:
                violations.append({
                    "kind": "keyword-arg-use",
                    "line": node.lineno,
                    "symbol": node.arg,
                    "ban": rec,
                })

        # Parameter name in a function signature `def f(lambda_scale_X=None)`
        # — signals the function accepts the banned form as input
        # (Gemini review, PR #1819, high).
        elif isinstance(node, ast.arg):
            rec = _symbol_banned(node.arg)
            if rec:
                violations.append({
                    "kind": "param-def",
                    "line": node.lineno,
                    "symbol": node.arg,
                    "ban": rec,
                })

    for v in violations:
        v["path"] = rel
    return violations


def _is_production(path: Path) -> bool:
    parts = set(path.relative_to(COMPUTE_ROOT).parts)
    if parts & EXCLUDED_DIRS:
        return False
    if path.name == SELF_NAME:
        return False
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description="NEGATIVE-finding re-entry guard")
    ap.add_argument("--strict", action="store_true",
                    help="exit non-zero if any banned form re-entered production")
    args = ap.parse_args()

    py_files = sorted(
        p for p in COMPUTE_ROOT.rglob("*.py") if _is_production(p)
    )

    all_violations: list[dict] = []
    parse_errors: list[dict] = []
    for p in py_files:
        for v in audit_file(p):
            if v["kind"] == "parse-error":
                v["path"] = str(p.relative_to(COMPUTE_ROOT))
                parse_errors.append(v)
            else:
                all_violations.append(v)

    # Group for the report.
    by_file: dict[str, list[dict]] = {}
    for v in all_violations:
        by_file.setdefault(v["path"], []).append(v)

    print("=" * 72)
    print("NEGATIVE-finding re-entry guard — purged non-canonical forms")
    print("=" * 72)
    print(f"  production scripts scanned : {len(py_files)}")
    print(f"  banned symbols registered  : {len(BANNED_SYMBOLS)} "
          f"(+ prefix '{BANNED_SYMBOL_PREFIX}*')")
    print(f"  banned modules registered  : {len(BANNED_MODULES)}")
    print(f"  parse errors (skipped)     : {len(parse_errors)}")
    print(f"  RE-ENTRY VIOLATIONS        : {len(all_violations)}")
    if by_file:
        print("\n  Offenders:")
        for fp in sorted(by_file):
            print(f"    {fp}")
            for v in by_file[fp]:
                print(f"       line {v['line']:>4}  [{v['kind']}]  "
                      f"{v['symbol']}  — {v['ban']['reason'][:70]}…")
    else:
        print("\n  ✓ No purged non-canonical form has re-entered production.")

    # Witness. (witness_base lives in substrate/, already on sys.path via
    # _path_bridge — no extra insert needed.)
    from witness_base import WitnessBuilder  # noqa: E402

    w = WitnessBuilder("noncanonical-reentry-audit", engine="python")
    w.set_description(
        "NEGATIVE-finding guard. AST-scans production compute "
        "(computations/, excluding _deprecated/, probes/, "
        "data/) and fails if any script imports, defines, or uses a PURGED "
        "non-canonical form. Registry: lambda_scale_yekutieli_extended "
        "(Yekutieli −G·h² correction, falsified PR #985/#1027), "
        "lambda_scale_family_a (lambda-scale alias, removed PR #1089), the "
        "lambda_scale_* symbol prefix (owner directive 'no lambda-scale "
        "ANYWHERE in production'), and the purged module "
        "lambda_yekutieli_extended_borromean. Uses AST so historical "
        "mentions in comments/docstrings are not false-positives. "
        "Detection covers direct imports, module-as-symbol imports "
        "(from pkg import <banned-module>), def, bare-name use, and "
        "attribute access (mod.<banned>); strict mode also fails on "
        "unparseable production scripts so there is no blind spot. Keeps "
        "the documented purges durable against silent sibling-branch "
        "re-entry."
    )
    w.set_content_block("prop:three-calibration-inputs")
    w.add_data("production_scripts_scanned", len(py_files))
    w.add_data("banned_symbols", BANNED_SYMBOLS)
    w.add_data("banned_modules", BANNED_MODULES)
    w.add_data("banned_symbol_prefix", BANNED_SYMBOL_PREFIX)
    w.add_data("excluded_dirs", sorted(EXCLUDED_DIRS))
    w.add_data("violation_count", len(all_violations))
    w.add_data("violations", all_violations)
    w.add_data("parse_error_count", len(parse_errors))
    w.add_assertion(
        "no_purged_form_reentered_production",
        computed=len(all_violations),
        expected=0,
        tolerance=0,
    )
    # A production file that cannot be parsed is a blind spot: a banned form
    # could hide inside it and the AST scan would never see it (Copilot
    # review, PR #1819). Assert zero unparseable scripts so strict mode is
    # actually complete, not just "complete for the files that happened to
    # parse".
    w.add_assertion(
        "no_unparseable_production_scripts",
        computed=len(parse_errors),
        expected=0,
        tolerance=0,
    )
    w.save()

    if args.strict and (all_violations or parse_errors):
        if parse_errors:
            print("\n  STRICT: unparseable production script(s) — audit blind "
                  "spot, failing:")
            for pe in parse_errors:
                print(f"    {pe['path']}  line {pe['line']}: {pe['reason']}")
        if all_violations:
            print("\n  STRICT: re-entry detected — failing.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
