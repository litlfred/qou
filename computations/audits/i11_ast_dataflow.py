#!/usr/bin/env python3
"""I11 AST-dataflow classifier — a SECOND-OPINION cross-check for the
substring-based `validation_as_input_audit.py`.

Motivation
──────────
The substring I11 audit (refined down 39 → 19 over several PRs) classifies
each *line* by local context. That hits a wall: the genuine I11 question —
does a `_VALIDATION` anchor flow into a **predicted** quantity (a hidden
fourth calibration) or only into a **comparison / display / recording**? —
is a *dataflow* question, not a line-local one. A comparison reference such
as `m_obs = Z·m_p + N·m_n − B_AME` (only ever subtracted from predictions)
and a true input use look identical line-by-line.

This tool answers it structurally: parse the AST, and for each use of an
anchor (and the values transitively derived from it) walk *up* through
carrier conversions and arithmetic to the sink. A use is **clean** iff the
sink is a comparison (`Compare`/`x − …`), a display (`nstr`/`print`/
f-string), a recording (`add_parameter`/dict value), a boolean guard, or an
assignment to a variable that is itself clean (recursive, memoised). It is a
**violation** iff the derived value is returned or passed to a compute
function — i.e. flows forward as a prediction.

The irreducible limit
─────────────────────
A value derived from an anchor and passed to a *generic* function (or
returned) is genuinely ambiguous — it may be a comparison reference or a
prediction; the AST cannot tell. So this classifier is **not strictly
better** than the substring one — it trades a different false-positive /
false-negative profile. Its real value is as a **cross-check**: scripts
flagged by BOTH methods are high-confidence genuine candidates; scripts
flagged by only one are the semantic-ambiguity cases that need a human.

Usage
─────
    python3 computations/audits/i11_ast_dataflow.py            # AST result
    python3 computations/audits/i11_ast_dataflow.py --cross-check
        # also read the substring audit's witness (if present) and print the
        # high-confidence intersection + the per-method-only disagreement sets
"""
from __future__ import annotations

import ast
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTE_ROOT = HERE.parent

VALIDATION_CONSTANTS = (
    "M_P_MEV_VALIDATION", "M_N_MEV_VALIDATION", "M_D_MEV_VALIDATION",
    "M_T_MEV_VALIDATION", "M_HE3_MEV_VALIDATION", "M_HE4_MEV_VALIDATION",
    "M_LI6_MEV_VALIDATION", "M_LI7_MEV_VALIDATION", "M_BE7_MEV_VALIDATION",
    "M_BE8_MEV_VALIDATION", "M_BE9_MEV_VALIDATION",
    "M_P_MEV_VALIDATION_ERR", "M_N_MEV_VALIDATION_ERR",
)
CARRIER_FUNCS = {"mpf", "float", "str", "Decimal", "fabs", "abs",
                 "round", "min", "max"}
DISPLAY_FUNCS = {"nstr", "print", "write", "warning", "info", "debug", "format"}
RECORDING_FUNCS = {"add_parameter", "add_data", "add_assertion", "add_caveat"}
CMP_KWARGS = {"expected", "target", "tolerance", "validation", "codata",
              "reference", "atol", "rtol", "places", "msg", "rel_tol", "abs_tol"}


def _func_name(call: ast.Call) -> str:
    f = call.func
    if isinstance(f, ast.Name):
        return f.id
    if isinstance(f, ast.Attribute):
        return f.attr
    return ""


class _Analyzer:
    def __init__(self, tree: ast.AST):
        self.parent: dict = {}
        for n in ast.walk(tree):
            for c in ast.iter_child_nodes(n):
                self.parent[c] = n
        self.var_loads: dict[str, list] = {}
        for n in ast.walk(tree):
            if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load):
                self.var_loads.setdefault(n.id, []).append(n)
        self._memo: dict[str, bool] = {}

    def is_clean_var(self, var: str, seen: frozenset = frozenset()) -> bool:
        if var in self._memo:
            return self._memo[var]
        if var in seen:
            return True  # recursion cycle — assume clean
        self._memo[var] = True  # optimistic, breaks recursion
        ok = all(self.is_clean_use(ld, seen | {var})
                 for ld in self.var_loads.get(var, []))
        self._memo[var] = ok
        return ok

    def is_clean_use(self, name_node: ast.Name, seen: frozenset = frozenset()) -> bool:
        cur = name_node
        while True:
            p = self.parent.get(cur)
            if p is None:
                return True
            if isinstance(p, ast.Call) and _func_name(p) in CARRIER_FUNCS and cur in p.args:
                cur = p; continue
            if isinstance(p, (ast.BinOp, ast.UnaryOp)):
                cur = p; continue
            if isinstance(p, ast.Compare):
                return True
            if isinstance(p, (ast.JoinedStr, ast.FormattedValue)):
                return True
            if isinstance(p, ast.Dict):
                return True
            if isinstance(p, ast.BoolOp):
                return True
            if isinstance(p, ast.IfExp):
                if cur is p.test:
                    return True
                cur = p; continue
            if isinstance(p, ast.keyword):
                return p.arg in CMP_KWARGS
            if isinstance(p, ast.Call):
                fn = _func_name(p)
                return fn in DISPLAY_FUNCS or fn in RECORDING_FUNCS
            if isinstance(p, ast.Assign) and cur is p.value:
                if len(p.targets) == 1 and isinstance(p.targets[0], ast.Name):
                    return self.is_clean_var(p.targets[0].id, seen)
                return False
            if isinstance(p, (ast.Return, ast.Yield)):
                return False
            if isinstance(p, (ast.Tuple, ast.List, ast.Subscript, ast.Starred)):
                cur = p; continue
            return False  # conservative default


def classify_script(path: Path):
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return None
    if not any(v in text for v in VALIDATION_CONSTANTS):
        return None
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return "PARSE_FAIL"
    found = {v for v in VALIDATION_CONSTANTS if v in text}
    an = _Analyzer(tree)
    bad = set()
    for v in found:
        for ld in an.var_loads.get(v, []):
            if not an.is_clean_use(ld):
                bad.add(ld.lineno)
    return {"violation_lines": sorted(bad)}


def _scan():
    flagged = {}
    parse_fail = 0
    for py in sorted(COMPUTE_ROOT.rglob("*.py")):
        if "_deprecated" in py.parts or "audits" in py.parts:
            continue
        if py.name == "codata_constants.py":
            continue  # the SOURCE of the constants
        r = classify_script(py)
        if r is None:
            continue
        if r == "PARSE_FAIL":
            parse_fail += 1
            continue
        if r["violation_lines"]:
            flagged[py.name] = r["violation_lines"]
    return flagged, parse_fail


def _substring_flagged():
    w = HERE / "validation-as-input-audit.witness.json"
    if not w.exists():
        return None
    d = json.loads(w.read_text())
    return {r["path"].split("/")[-1]
            for r in d.get("data", {}).get("rows", [])
            if r.get("result") == "i11_violation"}


def main() -> int:
    flagged, pf = _scan()
    print(f"AST-dataflow I11: {len(flagged)} scripts flagged "
          f"({sum(len(v) for v in flagged.values())} lines), {pf} parse-fail")
    for nm, lines in flagged.items():
        print(f"  {nm}: {lines}")
    if "--cross-check" in sys.argv:
        subs = _substring_flagged()
        if subs is None:
            print("\n(no substring witness present — run validation_as_input_audit.py first)")
            return 0
        astset = set(flagged)
        inter = subs & astset
        print(f"\n=== HIGH-CONFIDENCE (flagged by BOTH methods): {len(inter)} ===")
        for s in sorted(inter):
            print(f"  {s}")
        print(f"\nsubstring-only (AST cleared): {len(subs - astset)}; "
              f"AST-only (substring cleared): {len(astset - subs)} "
              f"— the semantic-ambiguity set (comparison-ref vs prediction).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
