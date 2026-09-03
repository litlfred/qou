#!/usr/bin/env python3
"""qou-l790: triage the CRITICAL `compute_no_mpf_to_float_cast` findings —
mpmath/sympy values downcast to float64.

WHY NOW. These findings were INVISIBLE until 2026-08-26. `script-sweep` walked
a doubled path and audited zero scripts in every content repo, exiting 0 with
"0 findings" (bean `qou-z8x9`, fixed in litlfred/folio-assistant#136). With the
walker fixed the sweep reports 3814 scripts and **106 critical**, and
`compute_no_mpf_to_float_cast` is the ONLY script-quality criterion at critical
severity — so all 106 are precision destruction, the defect class AGENTS.md is
most emphatic about ("a float64 input poisons the whole result").

NOT ONE OF THEM IS IN `_deprecated/`. All 106 are live.

WHY AST AND NOT REGEX. My first pass at this classified by regex and was wrong
in BOTH directions in the same run: it called `"abs_tr_M": float(mp.fabs(...))`
a string literal (it is a real cast on the value side of a dict entry — the
leading quote is the KEY), and it missed the one genuine string-literal false
positive, `float64_leak_audit.py`, whose `.set_description()` prose contains
the words "`float(...)` casts". A regex cannot tell code from prose about code.
`ast` can, so this walks the tree.

The sweep reports at most ONE hit per file (`first_hit`), so "106 findings" is
really "106 FILES with at least one". This counts every cast in each.

CLASSES, and what each is worth:

  assertion_kwarg   `computed=` / `expected=` / `tolerance=` on add_assertion.
                    A REAL defect against a documented convention: that method's
                    own docstring says pass them as STRINGS "to keep a value out
                    of float64 — that is the drained convention (qou-t0rf)".
                    Mechanical to fix and safe.
  anchor_truncated  The 50-digit substrate anchor cast to a double, e.g.
                    `q = float(mp.mpf(Q_50_DIGIT_STR))`. This is the single
                    widest leak shape in the corpus's history — `_avg_color_delta`
                    carried exactly it. NOT automatically a defect: a numpy path
                    may cast at its boundary DELIBERATELY, which AGENTS.md
                    permits ("consumers that genuinely need f64 cast at their own
                    boundary, where the loss is visible"). Needs per-file eyes.
  serialised        A cast on the value side of a dict entry or a witness field.
                    Should carry `_precision.fmt` instead.
  evalf_discarded   `float(expr.evalf(30))` — computes at 30 digits and throws
                    them away. Real, and often trivially fixable.
  display           Inside an f-string, `print`, or `.format`. EXPLICITLY
                    PERMITTED by AGENTS.md ("permitted only inside an f-string
                    for display"), though `mp.nstr` is preferred.
  string_literal    The text appears inside a quoted string — prose, not code.
                    A false positive of the checker.
  other/<parent>    Everything else, split by syntactic parent — undivided
                    it is the largest bucket and tells you nothing. The split
                    is what makes it actionable: `other/arithmetic_operand` is
                    a float64 COMPUTATION, which AGENTS.md forbids outright,
                    whereas `other/collected_into_list` is usually a report row
                    and much weaker.

This script CLASSIFIES and does not fix. Draining is separate, needs the
owner's scoping, and the `anchor_truncated` and `other` classes need judgement
per file rather than a sweep.
"""

from __future__ import annotations

import ast
import collections
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/qou-substrate/python", "computations"):
    _s = str(_ROOT / _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

#: Names whose values are exact and must not be silently doubled.
EXACT_HINTS = ("mp", "mpmath", "mpf", "sympy", "sp", "Rational", "Fraction")
ASSERTION_KWARGS = {"computed", "expected", "tolerance"}


def _is_float_call(node: ast.AST) -> bool:
    if not isinstance(node, ast.Call):
        return False
    f = node.func
    if isinstance(f, ast.Name) and f.id == "float":
        return True
    # np.float64(...) / numpy.float64(...)
    return isinstance(f, ast.Attribute) and f.attr in ("float64", "float_")


def _arg_looks_exact(node: ast.Call) -> bool:
    """Does the cast's ARGUMENT come from mpmath / sympy / an exact rational?

    Deliberately generous: this decides only whether the cast is interesting,
    and the classifier below is what carries the verdict.
    """
    if not node.args:
        return False
    for sub in ast.walk(node.args[0]):
        if isinstance(sub, ast.Name) and sub.id in EXACT_HINTS:
            return True
        if isinstance(sub, ast.Attribute):
            v = sub.value
            if isinstance(v, ast.Name) and v.id in EXACT_HINTS:
                return True
            if sub.attr in ("evalf", "subs", "mpf", "mpmath"):
                return True
        if isinstance(sub, ast.Call):
            fn = sub.func
            if isinstance(fn, ast.Attribute) and fn.attr in ("evalf", "mpf", "subs"):
                return True
            if isinstance(fn, ast.Name) and fn.id in ("mpf", "mpmathify"):
                return True
    return False


def classify(tree: ast.Module, src_lines: list[str]) -> list[tuple[int, str, str]]:
    """Return (lineno, class, source-line) for every interesting float cast."""
    # Parent map — ast gives no parent pointers.
    parent: dict[ast.AST, ast.AST] = {}
    for n in ast.walk(tree):
        for c in ast.iter_child_nodes(n):
            parent[c] = n

    out: list[tuple[int, str, str]] = []
    for node in ast.walk(tree):
        if not _is_float_call(node) or not _arg_looks_exact(node):
            continue
        line = getattr(node, "lineno", 0)
        text = src_lines[line - 1].strip() if 0 < line <= len(src_lines) else ""

        # Walk up a bounded number of parents to find the governing context.
        kind = "other"
        cur: ast.AST | None = node
        for _ in range(6):
            par = parent.get(cur)
            if par is None:
                break
            if isinstance(par, ast.keyword) and par.arg in ASSERTION_KWARGS:
                kind = "assertion_kwarg"
                break
            if isinstance(par, ast.JoinedStr) or isinstance(par, ast.FormattedValue):
                kind = "display"
                break
            if isinstance(par, ast.Call):
                fn = par.func
                nm = fn.attr if isinstance(fn, ast.Attribute) else getattr(fn, "id", "")
                if nm in ("print", "format", "nstr"):
                    kind = "display"
                    break
            if isinstance(par, ast.Dict):
                kind = "serialised"
                break
            if isinstance(par, ast.Assign):
                tgts = [t.id for t in par.targets if isinstance(t, ast.Name)]
                if any(t.lower().startswith("q") for t in tgts):
                    kind = "anchor_truncated"
                break
            cur = par

        if kind == "other":
            flat = ast.dump(node)
            if "Q_50_DIGIT_STR" in text or "Q_50_DIGIT_STR" in flat:
                kind = "anchor_truncated"
            elif "evalf" in flat:
                kind = "evalf_discarded"

        # `other` is the largest bucket and useless undivided, so name the
        # syntactic parent. The split is what makes it actionable: an
        # `arithmetic_operand` is a float64 COMPUTATION, which AGENTS.md
        # forbids outright, while `collected_into_list` is usually a report
        # row and much weaker.
        if kind == "other":
            par = parent.get(node)
            kind = "other/" + (
                "returned" if isinstance(par, ast.Return)
                else "compared" if isinstance(par, ast.Compare)
                else "arithmetic_operand" if isinstance(par, ast.BinOp)
                else "collected_into_list" if isinstance(par, (ast.List, ast.Tuple, ast.Set))
                else "passed_to_a_call" if isinstance(par, ast.Call)
                else "assigned_to_a_name" if isinstance(par, ast.Assign)
                else f"kwarg_{par.arg}" if isinstance(par, ast.keyword)
                else type(par).__name__ if par is not None
                else "toplevel"
            )
        out.append((line, kind, text))
    return out


def main() -> int:
    sweep = Path("/tmp/mpf-cast.json")
    if sweep.exists():
        data = json.loads(sweep.read_text())
        files = [r["script_path"] for r in data["results"]
                 if r.get("fail_critical", 0) > 0]
        src = "script-sweep --only compute_no_mpf_to_float_cast"
    else:
        files = sorted(str(p.relative_to(_ROOT))
                       for p in (_ROOT / "computations").rglob("*.py"))
        src = "full computations/ walk (sweep JSON absent)"
    print(f"input: {len(files)} file(s) from {src}\n")

    counts: collections.Counter[str] = collections.Counter()
    per_file: dict[str, list[tuple[int, str, str]]] = {}
    literal_fp: list[str] = []
    unparsable: list[str] = []

    for rel in files:
        p = _ROOT / rel
        try:
            text = p.read_text()
            tree = ast.parse(text)
        except Exception as exc:
            unparsable.append(f"{rel}: {exc.__class__.__name__}")
            continue
        hits = classify(tree, text.splitlines())
        if not hits:
            # The checker flagged it but AST finds no cast on an exact value:
            # the match was inside a string literal — prose about the pattern.
            literal_fp.append(rel)
            counts["string_literal_FALSE_POSITIVE"] += 1
            continue
        per_file[rel] = hits
        for _, kind, _ in hits:
            counts[kind] += 1

    total = sum(len(v) for v in per_file.values())
    print(f"files with a real cast : {len(per_file)}")
    print(f"TOTAL casts            : {total}   (the sweep reports only "
          f"first_hit, so it undercounts)")
    print(f"checker false positives: {len(literal_fp)}")
    for f in literal_fp:
        print(f"    {f}")
    if unparsable:
        print(f"unparsable             : {len(unparsable)}")
        for f in unparsable[:5]:
            print(f"    {f}")
    print()
    for kind, n in counts.most_common():
        print(f"  {n:5}  {kind}")

    print("\n=== assertion_kwarg — the mechanically-safe class ===")
    shown = 0
    for rel, hits in sorted(per_file.items()):
        for line, kind, text in hits:
            if kind == "assertion_kwarg" and shown < 20:
                print(f"  {rel}:{line}\n      {text[:100]}")
                shown += 1

    try:
        from qou_substrate.witness import WitnessBuilder
        wb = WitnessBuilder("mpf-float-cast-triage", _script_path=__file__)
        wb.set_description(
            "AST triage of the critical compute_no_mpf_to_float_cast findings, "
            "made visible by the qou-z8x9 sweeper fix. Classifies; does not fix."
        )
        wb.add_data("q0_anchor", "none — a source-level AST scan, nothing is evaluated")
        wb.add_data("markov_convention", "not applicable")
        wb.add_data("counts", dict(counts))
        wb.add_data("total_casts", total)
        wb.add_data("files_with_casts", len(per_file))
        wb.add_data("checker_false_positives", literal_fp)
        wb.add_caveat(
            "`anchor_truncated` and `other` are NOT automatically defects — a "
            "numpy consumer may cast at its own boundary deliberately, which "
            "AGENTS.md permits. Those two classes need per-file judgement; only "
            "`assertion_kwarg` is mechanically safe to drain."
        )
        # Was `add_assertion("…", "1", "1", "0")` (bean `qou-26f2`) — a constant
        # that could not tell the sweep-JSON input from the `_deprecated/`-laden
        # fallback walk, so it read PASS in the one mode where the claim it makes
        # is false. Count the deprecated paths in the input instead: the checker
        # scores every `_deprecated/` script `n/a`, never `fail`, so a sweep-fed
        # run has 0 by construction and a fallback run fails loudly — which is
        # the correct verdict there, since that run's counts are a whole-tree
        # scan, not this audit's finding set.
        deprecated_in_input = sorted(
            rel for rel in files
            if rel.startswith("_deprecated/") or "/_deprecated/" in rel
        )
        wb.add_data("deprecated_paths_in_input", deprecated_in_input)
        wb.add_assertion("all_findings_are_live_not_deprecated",
                         str(len(deprecated_in_input)), "0", "0",
                         unit="files under _deprecated/",
                         source=f"{len(deprecated_in_input)} of the {len(files)} "
                                f"flagged files are under _deprecated/ (input: {src})")
        wb.save()
        print("\nwitness written")
    except Exception as exc:  # pragma: no cover
        print(f"\nwitness NOT written ({exc.__class__.__name__}: {exc})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
