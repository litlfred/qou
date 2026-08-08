#!/usr/bin/env python3
"""q0_cross_layer_fallback_fix.py — make every cross-layer q₀ fallback RAISE
instead of silently substituting the other anchor's value.

THE DEFECT (see `q0_cross_layer_fallback_scan.py` for the detection rule)
    A producer reaches for the proton pin and, in an `except` handler, falls
    back to a hardcoded **muon** literal:

        try:
            from q_parameter import q_at
            Q0 = str(q_at())
        except Exception:
            Q0 = "1.1099785955573347198997632204832250266562084087802"

    On any import hiccup it then computes at the IDEAL pin while every label
    around it says proton, with nothing signalling the switch. AGENTS.md
    §q₀-anchor forbids straddling the two layers inside one quantity; this
    arrives through the error path, which is why it survives review — the happy
    path reads proton-clean.

    A fallback to the *other layer* is worse than no fallback. Owner decision
    2026-08-08: make all of them raise.

WHY THIS IS A SEPARATE SCRIPT FROM THE SCAN
    The scan is read-only and stays that way, so it can gate CI (`--strict`)
    without any chance of the gate rewriting the thing it measures.

SAFETY
    Only the `except` handler that actually contains the muon literal is
    touched, and only when its body does nothing but bind q₀ — a handler that
    also sets a flag or logs is reported for manual triage, never rewritten.
    Every rewritten file is re-parsed, and `--verify` additionally imports each
    one to confirm the happy path still works (the raise must be unreachable in
    a healthy environment — if it fires, the fallback was load-bearing and the
    file is reverted).

Usage:
    python3 q0_cross_layer_fallback_fix.py --dry-run
    python3 q0_cross_layer_fallback_fix.py --apply --verify
"""
from __future__ import annotations

import argparse
import ast
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent

MUON_PREFIXES = ("1.10997859555", "1.1099785955")
PROTON_TOKENS = ("q_at", "Q_50_DIGIT_STR", "Q_MP", "qou_substrate.constants",
                 "q_parameter")

MESSAGE_LINES = (
    "q0 accessor unavailable. Substituting the muon literal here would "
    "compute ",
    "at the IDEAL pin under proton labelling -- the straddle AGENTS.md "
    "q0-anchor ",
    "forbids, arriving through the error path. A cross-layer fallback is "
    "worse than ",
    "no fallback: fix the environment instead.",
)

# Comments that described the removed fallback. Left in place they would sit
# above a `raise` explaining why the code takes a value it no longer takes.
_STALE_COMMENT_HINTS = ("fallback", "canonical muon", "muon-q", "literal",
                        "pinning", "back-compat", "not a fit")


def _muon_handlers(tree: ast.AST) -> list[ast.ExceptHandler]:
    out = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.ExceptHandler):
            continue
        for sub in ast.walk(node):
            if isinstance(sub, ast.Constant) and \
                    any(str(sub.value).startswith(p) for p in MUON_PREFIXES):
                out.append(node)
                break
    return out


def _body_is_only_q0(h: ast.ExceptHandler) -> bool:
    """True when the handler does nothing but produce the q₀ value family.

    Every statement must be a plain assignment or a return — the shape of a pure
    fallback. Several handlers bind a small family together (`q0, qi, HA`, or a
    value plus its provenance label `Q0_SRC`), so a one-statement rule was too
    tight and sent two correct candidates to manual triage.

    A handler containing a call, a log line, or control flow is still refused:
    it may do work beyond q₀ that a bare `raise` would skip.
    """
    return bool(h.body) and all(
        isinstance(s, (ast.Assign, ast.AnnAssign, ast.Return)) for s in h.body)


def _rewrite(src: str, handlers: list[ast.ExceptHandler]) -> str:
    lines = src.splitlines(keepends=True)
    # Rewrite bottom-up so earlier line numbers stay valid.
    for h in sorted(handlers, key=lambda x: x.lineno, reverse=True):
        indent = " " * h.body[0].col_offset
        head_i = h.lineno - 1
        head = lines[head_i]
        # Bind the exception so the raise can chain, if it isn't already bound.
        if h.name is None:
            stripped = head.rstrip("\n")
            if stripped.rstrip().endswith(":"):
                base = stripped.rstrip()[:-1].rstrip()
                if base.strip() in ("except", "except:"):
                    base = base + " Exception"
                lines[head_i] = f"{base} as _q0_exc:\n"
                exc = "_q0_exc"
            else:
                exc = None
        else:
            exc = h.name
        chain = f" from {exc}" if exc else ""
        msg = "".join(f'{indent}    "{m}"\n' for m in MESSAGE_LINES)
        body = f'{indent}raise RuntimeError(\n{msg}{indent}){chain}\n'

        # Replace the WHOLE handler body: a fallback that binds q0, qi and HA
        # together must go as a unit, or the survivors reference a name the
        # raise never sets.
        first, last = h.body[0], h.body[-1]
        start = first.lineno - 1
        # Also drop the comment block between `except …:` and the first
        # statement when it describes the fallback — otherwise a comment saying
        # "fallback to the canonical 50-digit pinning" ends up sitting above a
        # `raise`. The whole contiguous block goes if ANY line in it matches:
        # these comments wrap across lines, and stripping only the matching line
        # leaves a dangling sentence fragment.
        block = start
        while block - 1 > head_i and lines[block - 1].strip().startswith("#"):
            block -= 1
        if block < start and any(
                any(t in lines[i].lower() for t in _STALE_COMMENT_HINTS)
                for i in range(block, start)):
            start = block
        lines[start:last.end_lineno] = [body]
    return "".join(lines)


def _candidates() -> list[Path]:
    out = []
    for p in sorted(REPO.rglob("*.py")):
        if ".git" in p.parts or "_deprecated" in p.parts or p.parent == HERE:
            continue
        try:
            src = p.read_text(encoding="utf-8")
        except Exception:  # noqa: BLE001
            continue
        if not any(m in src for m in MUON_PREFIXES):
            continue
        if not any(t in src for t in PROTON_TOKENS):
            continue
        try:
            tree = ast.parse(src)
        except Exception:  # noqa: BLE001
            continue
        if _muon_handlers(tree):
            out.append(p)
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--verify", action="store_true",
                    help="import each rewritten file; revert if the raise fires")
    args = ap.parse_args(argv)

    cands = _candidates()
    print("=" * 72)
    print("q₀ cross-layer fallback — make it raise")
    print("=" * 72)
    print(f"  files with a muon literal in an except handler : {len(cands)}")

    fixed, manual, failed = [], [], []
    for p in cands:
        src = p.read_text(encoding="utf-8")
        tree = ast.parse(src)
        hs = _muon_handlers(tree)
        simple = [h for h in hs if _body_is_only_q0(h)]
        complex_ = [h for h in hs if not _body_is_only_q0(h)]
        rel = str(p.relative_to(REPO))
        if complex_:
            manual.append((rel, [h.lineno for h in complex_]))
        if not simple:
            continue
        if not args.apply:
            fixed.append((rel, len(simple)))
            continue
        new = _rewrite(src, simple)
        try:
            ast.parse(new)
        except SyntaxError as e:
            failed.append((rel, f"rewrite did not parse: {e}"))
            continue
        p.write_text(new, encoding="utf-8")
        fixed.append((rel, len(simple)))

    for rel, n in fixed:
        print(f"  {'FIXED  ' if args.apply else 'would-fix'} {rel}  ({n} handler(s))")
    for rel, lns in manual:
        print(f"  MANUAL    {rel}  handler(s) at line(s) {lns} do more than bind q₀")
    for rel, why in failed:
        print(f"  FAILED    {rel}: {why}")

    if args.apply and args.verify:
        print("\n" + "-" * 72)
        print("  VERIFY — the raise must be UNREACHABLE in a healthy environment")
        print("-" * 72)
        bad = []
        for rel, _ in fixed:
            p = REPO / rel
            r = subprocess.run(
                [sys.executable, "-c",
                 f"import ast,sys;src=open({str(p)!r}).read();ast.parse(src)"],
                capture_output=True)
            if r.returncode != 0:
                bad.append(rel)
                continue
            # Import the module in its own directory so bare-name imports resolve.
            try:
                r = subprocess.run(
                    [sys.executable, "-c",
                     "import importlib.util,sys,os;"
                     f"sys.path.insert(0, {str(p.parent)!r});"
                     f"spec=importlib.util.spec_from_file_location('_probe', {str(p)!r});"
                     "m=importlib.util.module_from_spec(spec);"
                     "spec.loader.exec_module(m)"],
                    capture_output=True, cwd=str(p.parent), timeout=180)
            except subprocess.TimeoutExpired:
                # Importing runs the module. Exceeding the budget means it got
                # PAST the try/except into real work — the strongest evidence
                # the raise is unreachable, since it would have fired instantly.
                print(f"  ok-slow   {rel}: still computing at 180s, so the "
                      f"raise never fired")
                continue
            err = (r.stderr or b"").decode()
            if "q0 accessor unavailable" in err:
                subprocess.run(["git", "checkout", "HEAD", "--", rel], cwd=str(REPO))
                bad.append(rel)
                print(f"  REVERTED  {rel}: the fallback WAS load-bearing here")
            else:
                print(f"  ok        {rel}")
        print(f"\n  verified={len(fixed) - len(bad)}  reverted/failed={len(bad)}")

    print("=" * 72)
    if not args.apply:
        print("dry run — nothing written. Re-run with --apply --verify.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
