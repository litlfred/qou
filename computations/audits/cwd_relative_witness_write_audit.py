"""Which producers write a witness to a path relative to the CALLER'S CWD?

A relative target lands wherever the producer was invoked from. For a BARE name
that means an orphan in the caller's directory while the tracked witness is
left untouched -- so a re-run READS AS A REPRODUCTION. Measured cost (bean
qou-nxxw): three runs and two wrong conclusions on one file, because diffing
the committed witness after such a run compares it against itself.

For a REPO-ROOT-RELATIVE name (`computations/x.witness.json`) it works from the
root -- the normal case -- and orphans from anywhere else, e.g. a run from
`computations/` writes `computations/computations/x.witness.json`.

Result on `main` 2026-08-25: **16**, all the root-relative form, all
`open("computations/...", "w")`. The bare form is down to 0 with
`free-neutron-decay.py` fixed.

WRITE CONTEXT ONLY. A grep matches audits that merely READ witnesses by name;
a first attempt returned 5 files of which 4 were readers.

TWO WAYS THIS SCAN LIES, BOTH MADE HERE BEFORE BEING CAUGHT:

1. **It reported 0 because it scanned no files.** The roots were relative
   (`Path("computations")`), so running the script from any other directory
   resolved them to nothing and `rglob` yielded an empty set. The selftests
   below still passed -- they run on synthetic source strings, not the corpus --
   so a scan of zero files printed a confident zero. Roots are now absolute,
   derived from `__file__`. A scan that reports 0 must also be able to say how
   many files it opened; check that before believing it.
2. **It excluded any target containing "/".** That drops the root-relative
   form, which is 16 of the 16 found. Excluding it left exactly the class that
   dominates.

Blind spot that remains, stated rather than discovered later: LITERAL string
targets only. An f-string or computed name is invisible. That is not
hypothetical -- `chi_at_q0_via_hoefsmit_mpfr.py` builds
`f"chi-{atom}-h{n}-at-q{tag}-50dps.witness.json"` and this scan cannot see it
(it is correct anyway: `HERE /`-based, and the hash tag deliberately
quarantines a non-anchor cache).

Run: python3 -u computations/audits/cwd_relative_witness_write_audit.py
"""
import ast, pathlib, sys

_REPO = pathlib.Path(__file__).resolve().parent.parent.parent
ROOTS = [_REPO / d for d in ("computations", "tools", "scripts", "qou-mass")]

def is_bare_witness_str(node):
    return (isinstance(node, ast.Constant) and isinstance(node.value, str)
            and node.value.endswith(".witness.json")
            and not node.value.startswith("/"))   # any RELATIVE target, with or
            # without a directory component. Excluding "/"-containing names --
            # my first version did -- drops `Path("computations/x.witness.json")`,
            # which is equally cwd-relative and orphans from any cwd but the root.

class Scan(ast.NodeVisitor):
    def __init__(self):
        # name -> (lineno, target, node). The NODE matters: a target can be an
        # implicit concatenation spanning two source lines, so a line-based
        # match misses it. Measured: 7 of 16 sites, in two apparent classes
        # that were really one -- the literal is not on the line the call is on.
        self.bare = {}
        self.hits = []

    def visit_Assign(self, node):
        # x = Path("bare.witness.json")   /   x = "bare.witness.json"
        v = node.value
        tgt = None
        if isinstance(v, ast.Call) and isinstance(v.func, ast.Name) and v.func.id == "Path" \
           and v.args and is_bare_witness_str(v.args[0]):
            tgt = v.args[0].value
        elif is_bare_witness_str(v):
            tgt = v.value
        if tgt:
            lit_node = v.args[0] if isinstance(v, ast.Call) else v
            for t in node.targets:
                if isinstance(t, ast.Name):
                    self.bare[t.id] = (node.lineno, tgt, lit_node)
        self.generic_visit(node)

    def visit_Call(self, node):
        f = node.func
        # open(X, "w") / X.open("w") / X.write_text(...) / json.dump(_, open(X,"w"))
        def flag(name, lineno, why):
            if name in self.bare:
                ln, tgt, lit_node = self.bare[name]
                self.hits.append((lineno, tgt, why, lit_node))
        if isinstance(f, ast.Name) and f.id == "open" and node.args:
            mode = node.args[1].value if len(node.args) > 1 and isinstance(node.args[1], ast.Constant) else \
                   next((k.value.value for k in node.keywords if k.arg == "mode"
                         and isinstance(k.value, ast.Constant)), "r")
            if "w" in str(mode) or "a" in str(mode):
                if isinstance(node.args[0], ast.Name):
                    flag(node.args[0].id, node.lineno, f"open(..., {mode!r})")
                elif is_bare_witness_str(node.args[0]):
                    self.hits.append((node.lineno, node.args[0].value,
                                      f"open(literal, {mode!r})", node.args[0]))
        if isinstance(f, ast.Attribute):
            base = f.value
            if f.attr in ("write_text", "write_bytes") and isinstance(base, ast.Name):
                flag(base.id, node.lineno, f".{f.attr}()")
            if f.attr == "open" and isinstance(base, ast.Name):
                mode = node.args[0].value if node.args and isinstance(node.args[0], ast.Constant) else "r"
                if "w" in str(mode) or "a" in str(mode):
                    flag(base.id, node.lineno, f".open({mode!r})")
        self.generic_visit(node)

def scan(path):
    try: tree = ast.parse(path.read_text(errors="ignore"))
    except SyntaxError: return []
    s = Scan(); s.visit(tree); return s.hits

def main() -> int:
    # --- selftest: the known positive (pre-fix free-neutron-decay) and its fix ---
    POS = 'from pathlib import Path\nout = Path("free-neutron-decay.witness.json")\nwith out.open("w") as f:\n    pass\n'
    NEG = 'from pathlib import Path\nout = Path(__file__).resolve().parent / "free-neutron-decay.witness.json"\nwith out.open("w") as f:\n    pass\n'
    class T:
        def __init__(self, s): self.s = s
        def read_text(self, **k): return self.s
    DIRPOS = ('from pathlib import Path\n'
              'out = Path("computations/x.witness.json")\n'
              'out.write_text("{}")\n')
    LITPOS = 'import json\njson.dump({}, open("x.witness.json", "w"))\n'
    if not scan(T(POS)): print("SELFTEST FAILED: known positive not detected"); sys.exit(1)
    if not scan(T(DIRPOS)): print("SELFTEST FAILED: dir-prefixed relative not detected"); sys.exit(1)
    if not scan(T(LITPOS)): print("SELFTEST FAILED: open(literal,'w') not detected"); sys.exit(1)
    if scan(T(NEG)):     print("SELFTEST FAILED: fixed form flagged"); sys.exit(1)
    print("selftest: known positive detected, fixed form clean\n")

    n = 0
    files = [q for R in ROOTS if R.exists() for q in R.rglob("*.py")]
    if not files:
        print("REFUSING to report: scanned 0 files. Roots:", [str(r) for r in ROOTS])
        return 2
    for p in sorted(files):
        if ("_deprecated" in p.parts or "fsh-guts" in p.parts): continue
        h = scan(p)
        if h:
            n += 1
            print(f"  {p}")
            for ln, tgt, why, _node in h:
                print(f"      line {ln}: {why} -> {tgt}")
    print(f"\nscanned {len(files)} .py files under {len([r for r in ROOTS if r.exists()])} roots")
    print(f"producers writing a CWD-relative witness: {n}")
    return 0




# ---------------------------------------------------------------------------
#  SECOND DETECTOR — COMPUTED targets.
#
#  The scan above is LITERAL-only and says so. This closes that gap: a target
#  built by an f-string, an os.path.join, or a name is invisible to it. The
#  question is the same one, asked of an expression instead of a string: does
#  the path ROOT in __file__ / a dir constant (safe), or in nothing (the
#  defect)?
#
#  MEASURED on main 2026-08-25: 756 computed-target writes, 746 rooted safely,
#  and exactly ONE real defect --
#  `computations/substrate/lever1_habiro_element_fit.py`, an
#  `os.path.join("computations", "substrate", ...)` with no root at all. The
#  remaining nine are pytest `tmp_path` fixtures and WitnessBuilder's own
#  `self._output_dir`, both correct.
#
#  FOUR WAYS THIS ANALYSIS LIED BEFORE IT WAS RIGHT, all found by reading the
#  flagged code rather than trusting the count:
#    162  -- judged the root by NAME, so `os.path.join(_here, ...)` read as
#            unrooted although `_here = os.path.dirname(__file__)`.
#     34  -- followed a single chain, which stops the moment an assignment is
#            not a bare Name: `_COMPUTATIONS = HERE.parent` ends it and HERE is
#            never examined. Needs a fixpoint.
#     12  -- kept only the LAST assignment, so `root = os.path.dirname(root)`
#            hid the `__file__` origin two lines above; and a single-pass
#            visitor had not yet seen `def _here()` declared BELOW its use.
#      0  -- an edit removed the `hits.append` and the scan reported nothing at
#            all, which is the same "the harness is empty" failure the file
#            count above exists to catch.
# ---------------------------------------------------------------------------

def mentions_witness(node) -> bool:
    """Does this expression involve a '.witness.json' anywhere in it?"""
    for n in ast.walk(node):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and ".witness.json" in n.value:
            return True
        if isinstance(n, ast.JoinedStr):
            for v in n.values:
                if isinstance(v, ast.Constant) and isinstance(v.value, str) \
                   and ".witness.json" in v.value:
                    return True
    return False


# Roots that are legitimately NOT __file__-derived. Reported separately rather
# than left under "not rooted", because a standing list of known-fine entries
# invites the next agent to re-litigate them -- the same defect the
# no-free-parameter certificate had with A_omega (fixed 2026-08-25).
BY_DESIGN = {
    "tmp_path": "pytest fixture -- a per-test temp dir is the correct target",
    "self":     "WitnessBuilder's own writer; `_output_dir` is supplied by the "
                "caller, so this IS the API that makes other producers safe",
}

SAFE_ROOTS = {"HERE", "_HERE", "_HERE_W", "OUT_DIR", "WITNESS_DIR", "_OUT", "REPO", "ROOT", "_REPO"}

def roots_in(node):
    """Return the set of base Names / __file__ tokens the expression starts from."""
    out = set()
    for n in ast.walk(node):
        if isinstance(n, ast.Name):
            out.add(n.id)
        if isinstance(n, ast.Attribute) and n.attr == "__file__":
            out.add("__file__")
        if isinstance(n, ast.Constant) and n.value == "__file__":
            out.add("__file__")
    return out

class ComputedScan(ast.NodeVisitor):
    def __init__(self, src):
        self.src = src
        self.assigned = {}   # name -> LIST of value nodes (all assignments)
        self.funcs = {}      # name -> FunctionDef, for `_here()` style roots
        self.hits = []
    def visit_Assign(self, node):
        for t in node.targets:
            if isinstance(t, ast.Name):
                self.assigned.setdefault(t.id, []).append(node.value)
        self.generic_visit(node)
    def _check(self, expr, lineno, why):
        # resolve one level of indirection
        target = expr
        if isinstance(expr, ast.Name) and self.assigned.get(expr.id):
            # `assigned` maps to a LIST now (all assignments, so a
            # reassignment cannot hide a __file__ origin). Resolve to the one
            # that actually names a witness, else the last.
            cands = self.assigned[expr.id]
            target = next((c for c in cands if mentions_witness(c)), cands[-1])
        if not mentions_witness(target):
            return
        if isinstance(target, ast.Constant):
            return                       # the landed audit's territory
        # FIXPOINT expansion. A single-chain walk stops the moment an
        # assignment is not a bare Name -- `_COMPUTATIONS = HERE.parent` ends
        # it, and HERE never gets examined. Expand every root name through its
        # assignment (and through a def, for `_here()` style roots) until the
        # set stops growing, then ask once whether __file__ appears anywhere.
        # Measured cost of not doing this: 162 flagged, then 34, both wrong.
        seen, frontier = set(), set(roots_in(target))
        found = "__file__" in frontier
        while frontier and not found:
            nm = frontier.pop()
            if nm in seen:
                continue
            seen.add(nm)
            if nm in SAFE_ROOTS:
                found = True; break
            srcs = list(self.assigned.get(nm, []))
            fn = self.funcs.get(nm)
            if fn is not None:
                srcs.append(fn)
            if not srcs:
                continue
            if any("__file__" in ast.unparse(x) for x in srcs):
                found = True; break
            for x in srcs:
                frontier |= roots_in(x)
        safe = found
        self.hits.append((lineno, why, ast.unparse(target)[:90], sorted(seen)[:5], safe))

    def visit_Call(self, node):
        f = node.func
        if isinstance(f, ast.Name) and f.id == "open" and node.args:
            mode = node.args[1].value if len(node.args) > 1 and isinstance(node.args[1], ast.Constant) else "r"
            if "w" in str(mode) or "a" in str(mode):
                self._check(node.args[0], node.lineno, f"open(...,{mode!r})")
        if isinstance(f, ast.Attribute):
            if f.attr in ("write_text", "write_bytes"):
                self._check(f.value, node.lineno, f".{f.attr}()")
            if f.attr == "open" and node.args and isinstance(node.args[0], ast.Constant) \
               and ("w" in str(node.args[0].value) or "a" in str(node.args[0].value)):
                self._check(f.value, node.lineno, f".open({node.args[0].value!r})")
        self.generic_visit(node)


def scan_computed(files):
    """(safe, unrooted_rows) over every COMPUTED-target witness write."""
    safe_n, rows, by_design = 0, [], []
    for q in files:
        if ("_deprecated" in q.parts or "fsh-guts" in q.parts):
            continue
        try:
            tree = ast.parse(q.read_text(errors="ignore"))
        except SyntaxError:
            continue
        sc = ComputedScan("")
        # PRE-PASS: a def or assignment can appear AFTER the write that uses it.
        for n in ast.walk(tree):
            if isinstance(n, ast.FunctionDef):
                sc.funcs[n.name] = n
            elif isinstance(n, ast.Assign):
                for t in n.targets:
                    if isinstance(t, ast.Name):
                        sc.assigned.setdefault(t.id, []).append(n.value)
        sc.visit(tree)
        for ln, why, expr, r, safe in sc.hits:
            if safe:
                safe_n += 1
            elif set(r) & set(BY_DESIGN):
                by_design.append((q, ln, why, expr, sorted(set(r) & set(BY_DESIGN))[0]))
            else:
                rows.append((q, ln, why, expr, r))
    return safe_n, rows, by_design


_C_POS = ('import os\nout = os.path.join("computations", "x.witness.json")\n'
          'open(out, "w")\n')
_C_NEG_CHAIN = ('import os\nHERE = os.path.dirname(__file__)\n'
                '_C = HERE\nopen(os.path.join(_C, "x.witness.json"), "w")\n')
_C_NEG_REASSIGN = ('import os\nroot = os.path.dirname(os.path.abspath(__file__))\n'
                   'root = os.path.dirname(root)\n'
                   'open(os.path.join(root, "x.witness.json"), "w")\n')
_C_NEG_LATEDEF = ('import os\nopen(os.path.join(_here(), "x.witness.json"), "w")\n'
                  'def _here():\n    return os.path.dirname(os.path.abspath(__file__))\n')


def _selftest_computed() -> list[str]:
    """Each case is a shape that produced a WRONG answer before it was fixed."""
    import tempfile, os as _os
    bad = []
    cases = [("bare join, no root", _C_POS, True),
             ("chain through a non-Name assignment", _C_NEG_CHAIN, False),
             ("root REASSIGNED after a __file__ origin", _C_NEG_REASSIGN, False),
             ("def appears BELOW its use", _C_NEG_LATEDEF, False)]
    with tempfile.TemporaryDirectory() as td:
        for name, src, want_flag in cases:
            f = pathlib.Path(td) / (name.replace(" ", "_").replace(",", "") + ".py")
            f.write_text(src)
            _, rows, _ = scan_computed([f])
            got = bool(rows)
            if got != want_flag:
                bad.append(f"{name}: expected flag={want_flag}, got {got}")
    return bad


if __name__ == "__main__":
    _bad = _selftest_computed()
    if _bad:
        print("COMPUTED-TARGET SELFTEST FAILED:")
        for b in _bad:
            print("  ", b)
        sys.exit(1)
    print("computed-target selftest: 4/4 ok\n")
    _files = [q for R in ROOTS if R.exists() for q in R.rglob("*.py")]
    if not _files:
        print("REFUSING to report: scanned 0 files.")
        sys.exit(2)
    _safe, _rows, _bd = scan_computed(_files)
    print(f"COMPUTED-target witness writes : {_safe + len(_rows) + len(_bd)}")
    print(f"  rooted in __file__ / a dir const (SAFE) : {_safe}")
    print(f"  by design, not __file__-rooted          : {len(_bd)}")
    print(f"  ACTIONABLE                              : {len(_rows)}")
    if _bd:
        print("\n  by design (do NOT re-litigate):")
        for _q, _ln, _why, _expr, _k in _bd:
            print(f"    {_q.name}:{_ln}  {_expr}")
            print(f"        {_k} -- {BY_DESIGN[_k]}")
    for _q, _ln, _why, _expr, _r in _rows:
        print(f"    {_q}:{_ln}  {_why}")
        print(f"        {_expr}")
    sys.exit(main())
