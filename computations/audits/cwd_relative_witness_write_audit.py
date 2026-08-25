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
        if "_deprecated" in p.parts: continue
        h = scan(p)
        if h:
            n += 1
            print(f"  {p}")
            for ln, tgt, why, _node in h:
                print(f"      line {ln}: {why} -> {tgt}")
    print(f"\nscanned {len(files)} .py files under {len([r for r in ROOTS if r.exists()])} roots")
    print(f"producers writing a CWD-relative witness: {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
