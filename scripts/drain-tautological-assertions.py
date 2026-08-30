"""Class-A drain: carry the asserts' result into the witness assertion.

Applies to any function that BOTH contains `assert` statements AND ends in an
`add_assertion` whose `computed` and `expected` are the same literal. The
asserts do the real work and abort on failure; the witness recorded a constant
that would pass with the checking code deleted (bean qou-26f2).

Transformation, per qualifying function:
  * declare `_ok: list[bool] = []`
  * `assert X, m`  ->  `_ok.append(bool(X))` then `assert _ok[-1], m`
    (X evaluated once; abort semantics preserved exactly)
  * `computed=<lit>, expected=<lit>`  ->  `computed=all(_ok), expected=True`
"""
import ast, pathlib, re, sys

LIT = re.compile(r'^(True|False|1|0|1\.0|0\.0|"0"|"1"|\'0\'|\'1\'|-?\d+)$')

def taut_assertion_nodes(fn):
    out = []
    for n in ast.walk(fn):
        if not isinstance(n, ast.Call): continue
        f = n.func
        nm = f.attr if isinstance(f, ast.Attribute) else (f.id if isinstance(f, ast.Name) else None)
        if nm != "add_assertion": continue
        kw = {k.arg: k.value for k in n.keywords if k.arg}
        c, e = kw.get("computed"), kw.get("expected")
        if c is None or e is None: continue
        if ast.dump(c) != ast.dump(e): continue
        if not LIT.match(ast.unparse(c).strip()): continue
        out.append(n)
    return out

def transform(path):
    src = pathlib.Path(path).read_text()
    try: tree = ast.parse(src)
    except SyntaxError: return 0, 0
    lines = src.split("\n")
    edits, nfn, nass = [], 0, 0
    for fn in ast.walk(tree):
        if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)): continue
        asserts = [a for a in ast.walk(fn) if isinstance(a, ast.Assert)]
        tauts = taut_assertion_nodes(fn)
        if not asserts or not tauts: continue
        nfn += 1; nass += len(tauts)
        for a in asserts:
            s0, e0 = a.lineno - 1, (a.end_lineno or a.lineno) - 1
            ind = re.match(r"\s*", lines[s0]).group(0)
            test = ast.unparse(a.test)
            msg = f", {ast.unparse(a.msg)}" if a.msg is not None else ""
            edits.append((s0, e0, [f"{ind}_ok.append(bool({test}))", f"{ind}assert _ok[-1]{msg}"]))
        b0 = fn.body[0]
        anchor = (b0.end_lineno or b0.lineno) if isinstance(b0, ast.Expr) and isinstance(b0.value, ast.Constant) else b0.lineno - 1
        ind = re.match(r"\s*", lines[fn.body[-1].lineno - 1]).group(0)
        edits.append((anchor, anchor - 1, [f"{ind}_ok: list[bool] = []"]))
        # Right-to-left within a line. `computed=X, expected=X` often sits on ONE
        # line, and replacing `computed`'s value first shifts every later column
        # on that line, so an `expected` edit applied at its original offset
        # lands inside the keyword itself and produces `expeTrued=`. That is
        # valid Python -- py_compile accepts it -- and only fails at run time.
        repl = []
        for c in tauts:
            for k in c.keywords:
                if k.arg not in ("computed", "expected"): continue
                if k.value.lineno != (k.value.end_lineno or k.value.lineno): continue
                repl.append((k.value.lineno - 1, k.value.col_offset, k.value.end_col_offset,
                             "all(_ok)" if k.arg == "computed" else "True"))
        for ln_i, c0, c1, new_txt in sorted(repl, key=lambda x: (-x[0], -x[1])):
            ln = lines[ln_i]
            lines[ln_i] = ln[:c0] + new_txt + ln[c1:]
    for s0, e0, repl in sorted(edits, key=lambda x: -x[0]):
        lines[s0:e0 + 1] = repl
    out = "\n".join(lines)
    try: ast.parse(out)
    except SyntaxError: return 0, 0          # refuse to write anything unparseable
    pathlib.Path(path).write_text(out)
    return nfn, nass

# Paths this must never touch. A test's `add_assertion("b", computed="1",
# expected="1")` is FIXTURE DATA constructed to exercise the builder, not a
# corpus tautology, and rewriting it silently changes what the test asserts.
# Learned the hard way on `tools/qou-substrate/tests/
# test_declared_tolerance_literal.py`, which the first run mangled.
EXCLUDE = ("/tests/", "/test_", "conftest", "/fixtures/")


def excluded(path: str) -> bool:
    return any(x in path.replace("\\", "/") for x in EXCLUDE)


if __name__ == "__main__":
    tf = ta = nfiles = 0
    for p in sys.argv[1:]:
        if excluded(p):
            print(f"  skipped (test/fixture): {p}")
            continue
        f, a = transform(p)
        if a: nfiles += 1; tf += f; ta += a
    print(f"files changed {nfiles}; functions {tf}; assertions retargeted {ta}")
