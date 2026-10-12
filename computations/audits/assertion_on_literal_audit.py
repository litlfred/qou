#!/usr/bin/env python3
"""Assertions whose `computed` value traces to a hard-coded literal.

An assertion that measures nothing still records a result. The witness says the
quantity was checked; the code never computed it.

THE CASE THAT PROMPTED THIS (2026-08-30, bean `qou-58zw`).
`computations/qbeta/qbeta_markov_trace_compute_accuracy_diagnostic.py`:

    delta_S      = sp.Float(0)   # exactly 0 by SDP constraint
    delta_qbeta  = sp.Float(0)
    delta_ck     = sp.Float(0)
    delta_mn     = sp.Float(0)
    ...
    wb.add_assertion(name="tau_M_T_beta_L2_Markov_delta",
                     computed=float(delta_S), expected=0.0, tolerance=1e-50, ...)

None of the four is ever reassigned or computed — every other mention is a
`print` or the assertion itself. So the probe records "ZERO impact" on all four
canonical observables (tau_M(T_beta), Q_beta, c_k, m_n/Delta_pn) and its
description concludes *"the 'compute accuracy' question therefore has a clean
answer: ZERO impact"*, having measured none of them.

The comment `# exactly 0 by SDP constraint` may well be TRUE as mathematics.
That is not the defect. The defect is that a stated identity is presented as a
diagnostic result, and AGENTS.md names the cost precisely: a probe conclusion is
an ARGUMENT that reaches a bean, an audit doc, a PR body and a content block,
where nothing re-derives it.

WHY FIVE EXISTING AUDITS MISS IT
--------------------------------
Checked: `always_vacuous_assertion_scan`, `vacuous_pass_assertion_scan`,
`self_fulfilling_assertion_audit`, `ghost_value_sweep`,
`silent_self_check_audit`. **Zero hits on this file from any of them.** They
look for `computed == expected` SYNTACTICALLY. Here the vacuity is one
indirection away — `computed=float(delta_S)` where `delta_S = sp.Float(0)` —
and nothing follows the name back to its assignment.

METHOD. Per function body, track single-assignment locals whose value is a
numeric literal (bare, or wrapped in one of the known numeric constructors).
Then flag any `add_assertion(computed=...)` whose expression bottoms out in such
a name or in a literal directly. Reassignment anywhere in the function clears
the name — a variable that is computed later is not a literal, and assuming
otherwise is the false-positive mechanism the blindness taxonomy keeps
recording.

NOT FLAGGED, deliberately:
  * `expected=` — an expected value SHOULD usually be a literal; that is what
    makes it an expectation. Only `computed` is a measurement claim.
  * boolean/flag assertions built from a computed predicate.
  * names assigned more than once, or assigned from any call other than a
    numeric constructor.

Exit 0 when clean, 1 otherwise.

-- Ref: [manuscript] AGENTS.md "PROBES ARE NOT EXEMPT"
-- Ref: [manuscript] docs/audits/2026-08-15-detector-blindness-taxonomy.md
"""
from __future__ import annotations

import ast
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {"_deprecated", "fsh-guts", "__pycache__", "data", "node_modules"}

#: Calls that merely WRAP a literal without computing anything.
NUMERIC_CTORS = {"Float", "Integer", "Rational", "mpf", "mpmathify", "float",
                 "int", "Decimal", "S"}


def _literal_value(node: ast.AST):
    """The literal this expression denotes, or None if it computes anything.

    BOOLEANS ARE EXCLUDED, and the reason is a defect this audit had on its
    first run: `isinstance(False, int)` is True in Python, so a bare `bool`
    constant slipped through as a numeric literal. That flagged the honest
    guard-and-failure reporting idiom —

        except Exception:
            w.add_assertion(f"{k}_finite", computed=False, expected=True)
        if not HAVE_INFRA:
            w.add_assertion("infra_present", computed=False, expected=True, ...)

    — which is a probe correctly announcing that something did NOT work. That
    is the opposite of the defect this audit exists to find, and flagging it
    would train readers to ignore the report. Caught by spot-checking three
    hits before believing the count; two of the three were mine.
    """
    if (isinstance(node, ast.Constant) and isinstance(node.value, (int, float))
            and not isinstance(node.value, bool)):
        return node.value
    if isinstance(node, ast.Call):
        fname = (node.func.attr if isinstance(node.func, ast.Attribute)
                 else node.func.id if isinstance(node.func, ast.Name) else "")
        if fname in NUMERIC_CTORS and len(node.args) == 1:
            return _literal_value(node.args[0])
    if (isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub)):
        v = _literal_value(node.operand)
        return None if v is None else -v
    return None


def _literal_locals(fn: ast.AST) -> dict[str, float]:
    """Names assigned EXACTLY ONCE in this body, to a literal."""
    assigned: dict[str, list] = {}
    for node in ast.walk(fn):
        targets = []
        if isinstance(node, ast.Assign):
            targets = [(t, node.value) for t in node.targets]
        elif isinstance(node, (ast.AugAssign, ast.AnnAssign)) and node.value is not None:
            targets = [(node.target, node.value)]
        for tgt, val in targets:
            if isinstance(tgt, ast.Name):
                assigned.setdefault(tgt.id, []).append(val)
    # also treat a loop variable or comprehension target as non-literal
    for node in ast.walk(fn):
        if isinstance(node, ast.For) and isinstance(node.target, ast.Name):
            assigned.setdefault(node.target.id, []).append(None)
    out = {}
    for name, vals in assigned.items():
        if len(vals) != 1 or vals[0] is None:
            continue
        lit = _literal_value(vals[0])
        if lit is not None:
            out[name] = lit
    return out


def _traces_to_literal(node: ast.AST, lits: dict[str, float]):
    """Does this `computed=` expression bottom out in a literal?"""
    lit = _literal_value(node)
    if lit is not None:
        return lit
    if isinstance(node, ast.Name):
        return lits.get(node.id)
    if isinstance(node, ast.Call) and len(node.args) == 1:
        fname = (node.func.attr if isinstance(node.func, ast.Attribute)
                 else node.func.id if isinstance(node.func, ast.Name) else "")
        if fname in NUMERIC_CTORS:
            return _traces_to_literal(node.args[0], lits)
    return None


def scan_file(path: str) -> list[dict]:
    try:
        tree = ast.parse(open(path, encoding="utf-8", errors="replace").read())
    except (OSError, SyntaxError):
        return []
    out = []
    for fn in ast.walk(tree):
        if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Module)):
            continue
        lits = _literal_locals(fn)
        for node in ast.walk(fn):
            if not (isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Attribute)
                    and node.func.attr == "add_assertion"):
                continue
            kw = {k.arg: k.value for k in node.keywords if k.arg}
            comp = kw.get("computed")
            if comp is None:
                continue
            val = _traces_to_literal(comp, lits)
            if val is None:
                continue
            name = ""
            if node.args and isinstance(node.args[0], ast.Constant):
                name = str(node.args[0].value)[:60]
            elif isinstance(kw.get("name"), ast.Constant):
                name = str(kw["name"].value)[:60]
            # `comp.lineno`, not `node.lineno`: in a fluent builder chain every
            # chained Call carries the line the chain STARTS on, so several
            # assertions collapse onto one number. See the sibling tolerance
            # audit for the measured cases.
            out.append({"path": os.path.relpath(path, ROOT), "line": comp.lineno,
                        "assertion": name, "value": val,
                        "expr": ast.unparse(comp)[:60]})
    # one row per (file,line); Module-level and function-level walks can overlap
    seen, uniq = set(), []
    for r in out:
        k = (r["path"], r["line"])
        if k not in seen:
            seen.add(k)
            uniq.append(r)
    return uniq


_FIRES = '''
def f():
    d = sp.Float(0)
    w.add_assertion("a", computed=float(d), expected=0.0, tolerance=1e-50)
'''
_QUIET = '''
def g():
    d = compute_it()
    w.add_assertion("b", computed=float(d), expected=0.0, tolerance=1e-50)
def h():
    d = sp.Float(0)
    d = measure()
    w.add_assertion("c", computed=float(d), expected=0.0, tolerance=1e-50)
def i():
    w.add_assertion("d", computed=measured, expected=0.0, tolerance=1e-50)
'''


def _selftest() -> None:
    import tempfile
    for src, want in ((_FIRES, 1), (_QUIET, 0)):
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
            f.write(src)
            tmp = f.name
        try:
            got = len(scan_file(tmp))
            assert got == want, f"selftest: expected {want}, got {got}"
        finally:
            os.unlink(tmp)


def main(argv: list[str] | None = None) -> int:
    _selftest()
    argv = list(sys.argv[1:] if argv is None else argv)
    findings = []
    if argv and argv[0] == "--files":
        for a in argv[1:]:
            if a.endswith(".py") and os.path.exists(a):
                findings.extend(scan_file(os.path.abspath(a)))
    else:
        for root, dirs, files in os.walk(ROOT):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
            for fn in sorted(files):
                if fn.endswith(".py"):
                    findings.extend(scan_file(os.path.join(root, fn)))
    findings.sort(key=lambda r: (r["path"], r["line"]))
    print("=" * 78)
    print(" ASSERTIONS ON A HARD-CODED LITERAL — recorded as measurement, never measured")
    print("=" * 78)
    print(f"  flagged assertions : {len(findings)}")
    print(f"  files              : {len({f['path'] for f in findings})}")
    print("  selftest           : PASS (1 must-fire, 3 must-stay-quiet)")
    if findings:
        print()
        for f in findings:
            print(f"  {f['path']}:{f['line']}   computed={f['expr']}  -> literal {f['value']}")
            if f["assertion"]:
                print(f"      {f['assertion']}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
