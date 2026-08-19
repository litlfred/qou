#!/usr/bin/env python3
# polynomial_q_not_applicable: static source audit; emits no numeric physics.
"""Mixed mpmath/float64 **arithmetic** audit — the leak no other gate can see.

Owner directive: "NO FLOAT64", and AGENTS.md §"PROBES ARE NOT EXEMPT" rule 3:
*a float64 input poisons the whole result.*

**Why this exists — the measured blind spot.** The NO-FLOAT64 family already
has two layers, and this defect slips between them:

* `witness_float64_padding_audit.py` works at the **value** level. Its
  discriminator is "is this string the expansion of its nearest binary64?",
  which is decisive for `fmt(mpf(<a float64>))` — and **blind** the moment the
  float64 is multiplied by anything exact. Measured:

  | expression | serialized value is caught? |
  |---|---|
  | `fmt(mpf(f64))` | **yes** |
  | `fmt(mpf_exact * mpf(f64))` | **no** |
  | `fmt(sum(mpf_exact_k * mpf(f64)))` | **no** |

  One exact factor launders the value past the detector while the result still
  carries only ~16 good digits.

* `mpf_float_source_audit.py` works at the **construction** site — `mpf(0.1)`,
  `mpf(float(x))`. This defect involves **no `mpf()` call at all**: the float64
  enters through *arithmetic*, so that gate never looks at it.

* `numpy_mpmath_dtype_leak_audit.py` guards the opposite direction (an mpf
  reaching a numpy array, which costs speed). This is float64 reaching an
  mpmath expression, which costs digits.

**The worked case that motivated it** (bean `qou-stqr`,
`h6_deuteron_free_word_chi_lambda_probe.py`). Its substrate `q0`/`h` were
corrected to 50 dps and the probe was reported clean. The payload was not:

    y6  = {k: float(v) for k, v in y_lambda_at(6, q0).items()}   # exact -> f64
    trM = 0.0
    trM += y6[lam] * chi_lambda_of_word(...)   # `-> float`, numpy np.trace

so a 50-digit `q0` sat in the witness beside a payload good to ~1e-15. Both
existing gates were green throughout.

**What is reported.** A binary operation, or an augmented assignment, with one
operand traced to an mpmath source and the other to a float64 source:

| tag | inferred from |
|---|---|
| `MPF` | `mp.*(...)`, `mpf(...)`, `mpmathify(...)`, a corpus function annotated `-> mpf`, a name bound to any of these |
| `F64` | `float(...)`, `math.*`, `statistics.*`, `numpy.*`, `.item()/.sum()/.trace()`, a corpus function annotated `-> float`, a non-representable float literal, a name bound to any of these |

Return annotations are resolved **across files** by a first pass over the tree,
which is what lets `chi_lambda_of_word(...) -> float` be recognised at its call
site in another module.

**ADVISORY, deliberately.** Inference from annotations and local binding is
high-recall, not sound: a `-> float` annotation may be stale, and a name may be
rebound in a branch this pass does not follow. So findings are **candidates for
an agent verdict**, in the same spirit as the vacuity-audit ledger — the
machine flags, a human or agent adjudicates. `--strict` fails only on rows
above the baseline, so the surface can only shrink.

Marking a deliberate mix (a cross-check that *measures* the float64 gap, as
`h6` now does):

    gap = abs(mpf(chi64) - chi_mp) / chi_mp   # float64-intentional: measuring
                                              # the f64 floor as a cross-check

Output: `mpf-mixed-arithmetic-audit.witness.json`.
"""
from __future__ import annotations

import argparse
import ast
import json
import sys
from pathlib import Path

from mpmath import mp, mpf

mp.dps = 60

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SEARCH_ROOTS = [ROOT / "computations", ROOT / "tools"]
BASELINE = HERE / "mpf-mixed-arithmetic-baseline.json"
MARKER = "float64-intentional"

MPF_CTORS = {"mpf", "mpmathify"}
MPF_MODULES = {"mp", "mpmath"}
F64_MODULES = {"math", "statistics", "np", "numpy"}
F64_METHODS = {"item", "sum", "trace", "mean", "std"}
ARITH_OPS = (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.FloorDiv)

MPF = "MPF"
F64 = "F64"


def _exactly_representable(v: float) -> bool:
    return mpf(repr(v)) == mpf(v)


# ── pass 1: corpus-wide return-annotation registry ────────────────────────
def _ann_name(node) -> str:
    """Flatten a return annotation to a bare name (`float`, `mpf`, …)."""
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value.split(".")[-1]
    return ""


def build_registry(files: list[Path]) -> dict[str, str]:
    """function name -> MPF | F64, from `-> mpf` / `-> float` annotations.

    A name annotated inconsistently across files is dropped rather than
    guessed at — an ambiguous name would manufacture false positives at every
    call site.
    """
    seen: dict[str, set[str]] = {}
    defs: dict[str, int] = {}
    for p in files:
        try:
            tree = ast.parse(p.read_text(encoding="utf-8"), filename=str(p))
        except Exception:
            continue
        for n in ast.walk(tree):
            if not isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            defs[n.name] = defs.get(n.name, 0) + 1
            a = _ann_name(n.returns) if n.returns is not None else ""
            tag = MPF if a in ("mpf", "mpmath") else F64 if a == "float" else ""
            if tag:
                seen.setdefault(n.name, set()).add(tag)
    # A name defined more than ONCE in the corpus is dropped, even when only
    # one definition carries an annotation. Bare-name resolution cannot tell
    # the two apart, and a single mis-annotated namesake poisons every call
    # site of the real one. Measured: a probe-local helper
    # `def tr_M_atomic(label: str) -> float` in path_b_defect_binding_probe.py
    # tagged the canonical SYMBOLIC markov_peel.tr_M_atomic (unannotated,
    # returns a sympy expression) as float64, producing a false positive in
    # atomic_tr_m_mpfr_50dps.py — a file whose value is genuinely exact via
    # sp.N(..., 50).
    return {k: v.pop() for k, v in seen.items()
            if len(v) == 1 and defs.get(k, 0) == 1}


# ── pass 2: per-function float64 TAINT propagation ────────────────────────
#
# The first cut of this file asked "is a binop mixing an mpf with a float64?".
# That framing FAILED on the exact case it was written for (pre-fix
# `h6_deuteron_free_word_chi_lambda_probe.py`, 0 candidates): the accumulator
# was seeded `0.0` (exactly representable, so untagged), the weights came out
# of a `dict.get()`, and `y_lambda_at` carries no return annotation — so both
# operands were UNtagged and the pair never matched {MPF, F64}.
#
# The defect is not "mpf meets float64". It is **float64 provenance reaching a
# high-precision serializer** — a value good to ~1e-16 written out at 50 dps.
# So this tracks TAINT to a SINK, which is what the h6 witness actually did.

SINKS = {"fmt", "_fmt"}          # the canonical _precision serializer
NSTR = {"nstr"}                  # mp.nstr(x, n) with n > 17 digits
F64_CONSTS = {"h", "q0", "qi", "z"}   # pyhecke.gram module constants


class Tainter:
    """Propagate float64 provenance forward through a function body."""

    def __init__(self, registry: dict[str, str], rel: str, lines: list[str],
                 gram_names: set[str]):
        self.reg = registry
        self.rel = rel
        self.lines = lines
        self.gram = gram_names
        self.tainted: set[str] = set()
        self.mpf_names: set[str] = set()
        self.rows: list[dict] = []

    # -- provenance -------------------------------------------------------
    def f64(self, node) -> bool:
        """Does this expression carry float64 provenance?"""
        if node is None:
            return False
        if isinstance(node, ast.Name):
            return node.id in self.tainted or node.id in self.gram
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            return not _exactly_representable(node.value)
        if isinstance(node, ast.Call):
            f = node.func
            if isinstance(f, ast.Name):
                if f.id in MPF_CTORS:
                    # mpf(<tainted>) preserves the taint — it does not heal it.
                    return any(self.f64(a) for a in node.args)
                if f.id == "float":
                    return True
                if self.reg.get(f.id) == F64:
                    return True
                return any(self.f64(a) for a in node.args)
            if isinstance(f, ast.Attribute):
                mod = getattr(f.value, "id", "")
                if mod in F64_MODULES:
                    return True
                if f.attr in F64_METHODS:
                    return True
                if mod in MPF_MODULES or f.attr in MPF_CTORS:
                    return any(self.f64(a) for a in node.args)
                if self.reg.get(f.attr) == F64:
                    return True
                # `d.get(k, default)` inherits the container's taint.
                return self.f64(f.value) or any(self.f64(a) for a in node.args)
            return False
        if isinstance(node, ast.Attribute):
            return (node.attr in F64_CONSTS
                    and getattr(node.value, "id", "") in ("G", "gram"))
        if isinstance(node, ast.Subscript):
            return self.f64(node.value)
        if isinstance(node, ast.BinOp):
            return self.f64(node.left) or self.f64(node.right)
        if isinstance(node, ast.UnaryOp):
            return self.f64(node.operand)
        if isinstance(node, (ast.Tuple, ast.List, ast.Set)):
            return any(self.f64(e) for e in node.elts)
        if isinstance(node, (ast.ListComp, ast.SetComp, ast.GeneratorExp)):
            return self.f64(node.elt)
        if isinstance(node, ast.DictComp):
            return self.f64(node.value)
        if isinstance(node, ast.Dict):
            return any(self.f64(v) for v in node.values)
        if isinstance(node, ast.IfExp):
            return self.f64(node.body) or self.f64(node.orelse)
        return False

    def marked(self, lineno: int) -> bool:
        ctx = " ".join(self.lines[max(0, lineno - 3): lineno + 1])
        return MARKER in ctx

    def record(self, node, kind: str, detail: str) -> None:
        line = (self.lines[node.lineno - 1].strip()
                if node.lineno <= len(self.lines) else "")
        self.rows.append({
            "file": self.rel, "line": node.lineno, "kind": kind,
            "detail": detail, "source": line[:120],
            "class": "marked" if self.marked(node.lineno) else "CANDIDATE",
        })

    # -- sinks ------------------------------------------------------------
    def check_sinks(self, node) -> None:
        for n in ast.walk(node):
            if not isinstance(n, ast.Call):
                continue
            nm = getattr(n.func, "attr", None) or getattr(n.func, "id", "")
            if nm in SINKS and n.args and self.f64(n.args[0]):
                self.record(n, "serialized", f"{nm}(<float64-tainted>)")
            elif nm in NSTR and len(n.args) >= 2 and self.f64(n.args[0]):
                d = n.args[1]
                if isinstance(d, ast.Constant) and isinstance(d.value, int) \
                        and d.value > 17:
                    self.record(n, "printed",
                                f"nstr(<float64-tainted>, {d.value})")

    def visit_body(self, body) -> None:
        for st in body:
            if isinstance(st, ast.Assign):
                self.check_sinks(st.value)
                t = self.f64(st.value)
                for tgt in st.targets:
                    if isinstance(tgt, ast.Name):
                        (self.tainted.add if t else self.tainted.discard)(tgt.id)
            elif isinstance(st, ast.AugAssign):
                self.check_sinks(st.value)
                if isinstance(st.target, ast.Name) and self.f64(st.value):
                    self.tainted.add(st.target.id)
            elif isinstance(st, (ast.For, ast.While, ast.If, ast.With, ast.Try)):
                for f in ("test", "iter"):
                    if getattr(st, f, None) is not None:
                        self.check_sinks(getattr(st, f))
                if isinstance(st, ast.For) and isinstance(st.target, ast.Name) \
                        and self.f64(st.iter):
                    self.tainted.add(st.target.id)
                for attr in ("body", "orelse", "finalbody"):
                    if getattr(st, attr, None):
                        self.visit_body(getattr(st, attr))
                for h in getattr(st, "handlers", []) or []:
                    self.visit_body(h.body)
            elif isinstance(st, (ast.FunctionDef, ast.AsyncFunctionDef)):
                saved = set(self.tainted)
                # Parameters named like a tainted caller-side value stay
                # untainted: cross-function flow is out of scope, and guessing
                # it manufactures false positives.
                self.visit_body(st.body)
                self.tainted = saved
            elif isinstance(st, (ast.Expr, ast.Return)):
                if st.value is not None:
                    self.check_sinks(st.value)


def gram_float_names(tree: ast.Module) -> set[str]:
    """Names bound to the deliberately-float64 `pyhecke.gram` constants.

    `gram.h` / `q0` / `qi` / `z` are documented as the bit-stable float64 path
    (bean qou-jtbo); a consumer that imports one and serializes it at 50 dps is
    exactly the h6 defect one layer up.
    """
    out: set[str] = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.ImportFrom) and (n.module or "").endswith("gram"):
            for a in n.names:
                if a.name in F64_CONSTS:
                    out.add(a.asname or a.name)
    return out


def audit_file(p: Path, registry: dict[str, str]) -> list[dict]:
    try:
        src = p.read_text(encoding="utf-8")
        tree = ast.parse(src, filename=str(p))
    except Exception:
        return []
    t = Tainter(registry, p.relative_to(ROOT).as_posix(), src.splitlines(),
                gram_float_names(tree))
    t.visit_body(tree.body)
    return t.rows


def scan() -> tuple[list[dict], dict[str, str]]:
    files = [p for root in SEARCH_ROOTS if root.exists()
             for p in sorted(root.rglob("*.py"))
             if "_deprecated" not in p.parts]
    registry = build_registry(files)
    rows: list[dict] = []
    for p in files:
        rows.extend(audit_file(p, registry))
    return rows, registry


def self_test() -> int:
    """Exercise the tracker on the shape this gate exists to catch.

    Case 1 IS the pre-fix `h6_deuteron_free_word_chi_lambda_probe.py` payload,
    reduced: a dict comprehension applying `float()` to exact weights, an
    accumulator seeded `0.0`, weights drawn back out with `.get()`, and the
    total serialized with `fmt`. The first version of this audit scored ZERO on
    it — that regression is what this case pins.
    """
    src = '''
import math
import mpmath as mp
from _precision import fmt
def chi(x) -> float: ...
def yl(n): ...
def h6_pre_fix():                       # the motivating defect
    q0 = mp.mpf("1.1099785827513808")
    y6 = {k: float(v) for k, v in yl(6).items()}
    trM = 0.0
    for lam in (1, 2):
        y = y6.get(lam, 0.0)
        trM += y * chi(lam)
    return fmt(trM), fmt(q0)            # first is FAKE 50 dps, second is real
def clean():
    a = mp.mpf("1.5")
    b = mp.sqrt(a)
    return fmt(a * b)                   # exact throughout -> not flagged
def mpf_does_not_heal():
    x = float(3)
    return fmt(mp.mpf(x))               # mpf() around a float64 is still f64
def printed_wide():
    z = math.sqrt(2.0)
    return mp.nstr(z, 30)               # 30 digits of a float64
def printed_narrow():
    z = math.sqrt(2.0)
    return mp.nstr(z, 12)               # honest width -> not flagged
def marked_ok():
    c = float(1) / 3
    # float64-intentional: measuring the f64 floor as a cross-check
    return fmt(c)
'''
    reg = {"chi": F64}
    t = Tainter(reg, "<self-test>", src.splitlines(), set())
    t.visit_body(ast.parse(src).body)
    got = {r["line"] for r in t.rows if r["class"] == "CANDIDATE"}
    lines = src.splitlines()

    def line_of(frag: str) -> int:
        return next(i + 1 for i, l in enumerate(lines) if frag in l)

    want = {line_of("return fmt(trM), fmt(q0)"),
            line_of("return fmt(mp.mpf(x))"),
            line_of("return mp.nstr(z, 30)")}
    reject = {line_of("return fmt(a * b)"),
              line_of("return mp.nstr(z, 12)"),
              line_of("return fmt(c)")}
    missed, spurious = want - got, got & reject
    # The h6 line carries TWO fmt calls; only the tainted one may be reported.
    h6 = line_of("return fmt(trM), fmt(q0)")
    n_h6 = sum(1 for r in t.rows if r["line"] == h6)
    if n_h6 != 1:
        missed |= {h6}
    if missed or spurious:
        print("SELF-TEST FAILED:")
        for ln in sorted(missed):
            print(f"   MISSED   line {ln}: {lines[ln - 1].strip()}")
        for ln in sorted(spurious):
            print(f"   SPURIOUS line {ln}: {lines[ln - 1].strip()}")
        return 1
    print(f"SELF-TEST PASSED — {len(want)} tainted sinks caught (the pre-fix h6 "
          "payload through dict-comp/.get()/accumulator, mpf() around a float64, "
          f"a 30-digit nstr), {len(reject)} clean shapes not flagged (exact "
          "arithmetic, honest 12-digit nstr, marked cast); and the exact q0 on "
          "the h6 line was NOT flagged alongside the tainted total.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if candidates exceed the baseline")
    ap.add_argument("--list", action="store_true", help="print every candidate")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    rows, registry = scan()
    cands = [r for r in rows if r["class"] == "CANDIDATE"]
    marked = [r for r in rows if r["class"] == "marked"]
    by_file: dict[str, int] = {}
    for r in cands:
        by_file[r["file"]] = by_file.get(r["file"], 0) + 1

    base = 0
    if BASELINE.exists():
        base = json.loads(BASELINE.read_text()).get("candidates", 0)

    print("=" * 74)
    print("MIXED mpmath/float64 ARITHMETIC AUDIT — the leak between the gates")
    print("=" * 74)
    print(f"  candidates         : {len(cands)}")
    print(f"  marked deliberate  : {len(marked)}")
    print(f"  files affected     : {len(by_file)}")
    print(f"  annotated fns known: {len(registry)} "
          f"({sum(1 for v in registry.values() if v == F64)} -> float, "
          f"{sum(1 for v in registry.values() if v == MPF)} -> mpf)")
    print(f"  baseline           : {base}")
    print(f"  OVER baseline      : {max(0, len(cands) - base)}")

    if by_file:
        print("\n  worst files:")
        for f, c in sorted(by_file.items(), key=lambda kv: -kv[1])[:12]:
            print(f"    {c:>4}  {f}")
    if args.list:
        print("\n  candidates:")
        for r in cands:
            print(f"    {r['file']}:{r['line']}  [{r['left']} {r['kind']} "
                  f"{r['right']}]\n        {r['source']}")

    print("\n  These are CANDIDATES for an agent verdict, not proved defects:")
    print("  a `-> float` annotation can be stale, and a name can be rebound")
    print(f"  in a branch this pass does not follow. Mark a deliberate mix")
    print(f"  `# {MARKER}: <reason>` (e.g. a cross-check that MEASURES the")
    print("  float64 gap). Fix a real one by carrying mpmath end to end.")

    out = HERE / "mpf-mixed-arithmetic-audit.witness.json"
    out.write_text(json.dumps({
        "schema": "witness/v1",
        "name": "mpf-mixed-arithmetic-audit",
        "description": "Static detection of arithmetic mixing an mpmath value with "
                       "a float64-sourced one. Sits between the value-level padding "
                       "ratchet (blind once a float64 is multiplied by anything "
                       "exact) and the construction-level mpf(<float>) gate (blind "
                       "because no mpf() call is involved). Advisory: high-recall "
                       "candidates for agent verdict.",
        "data": {"candidates": len(cands), "marked": len(marked),
                 "files": len(by_file), "baseline": base,
                 "by_file": by_file, "rows": cands},
    }, indent=2) + "\n")
    print(f"\nWrote {out.name}")
    return 1 if (args.strict and len(cands) > base) else 0


if __name__ == "__main__":
    sys.exit(main())
