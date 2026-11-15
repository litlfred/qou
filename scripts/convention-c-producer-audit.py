#!/usr/bin/env python3
"""Find convention-C definitions of the Markov parameter in live Python producers.

The producer-layer counterpart to `folio/pipeline/trace-convention-audit.ts`,
which walks `content/**` only. Nothing walked the producers, and three
successive hand-greps of that surface returned 70, then 13, then 182.

## Why grep cannot do this

The corpus spells `z = 1/(q^{1/2} + q^{-1/2})` at least fifteen ways:

    1.0 / (q0**0.5 + qi0**0.5)          1 / (mp.sqrt(Q0) + 1/mp.sqrt(Q0))
    1.0 / (q0 ** 0.5 + q0 ** (-0.5))    1 / (sp.sqrt(q) + 1/sp.sqrt(q))
    1.0 / (Q0 ** 0.5 + QI ** 0.5)       1 / (np.sqrt(q) + 1.0/np.sqrt(q))
    1 / (q ** mpmath.mpf('0.5') + ...)  1 / (sqrt_q + 1 / sqrt_q)
    1 / (q0**mpf('0.5') + q0**mpf('-0.5'))

with the reciprocal named `q0`, `qi`, `qi0`, `Q_INV`, `_QI0`, `sqrt_q`, `q_val`,
or spelled inline; and the result bound to `z`, `z_mark`, `z_markov`, `Z_MARKOV`,
`z_sym`, `zmkv`, `ZS`, `z_q`, `_z`, ... A regex tuned to any subset silently
misses the rest, and a looser one (`0.5 + `) matches unrelated arithmetic. Both
failure modes actually happened, in that order.

So this walks the **AST**: any assignment whose target name contains `z` and
whose value has the shape `1 / (<something with a square root> + <anything>)`.
Shape-matching, not spelling-matching.

## What counts, and what deliberately does not

* **Deliberately C-named** targets (`z_C`, `z_c`, `z_C_expr`, ...) are excluded.
  A variable that says it is convention C is a labelled comparison, not a defect
  — the same principle the content axis uses for `C_LABEL`.
* **`tools/pyhecke/`** is reported separately, but the excuse comes from the
  REGISTRY, not from the path. Three buckets, in order of how well accounted
  the site is, and **only the first is excused from the actionable count**:

  1. **BLOCKED on C by design** — a `blocked_migrations` row names that exact
     file.
  2. **DECLARED C in `evaluators.z`, R10-waived** — the symbol is a registered
     C evaluator whose module is listed in `intra_module_split_waivers`. R9
     imports it and asserts its value numerically on every run, so this is a
     *stronger* record than a blocked row, which is only prose. It is still
     **actionable**: the waiver says in terms that the split is "an open
     defect, not an approved design". Declaring a thing does not fix it, and a
     declaration that shrinks the count is a way to make the inventory smaller
     without making the corpus better.
  3. **C with NO registry row (unexplained)** — anything else under
     `tools/pyhecke/`. Actionable.

  The path-prefix version was too generous. One row covered `gram.py::z`, and
  three *function-local* C definitions sheltered under the same label — two of
  them inside `gram.py` itself. When `z` migrated to D on 2026-08-15 (bean
  `qou-w8zz`) and the row was resolved, a prefix classifier would have gone on
  calling those three "by design" indefinitely.

  Bucket 2 exists because resolving that row correctly — emptying
  `blocked_migrations` — reclassified four fully-registered sites as
  "unexplained", so the registry and this detector disagreed about the same
  four while both worked as designed. Splitting them also stopped the blanket
  label hiding a real one: `pyhecke/atom.py:691` is a live C `z_mark`, consumed
  at :713, in a module (`pyhecke.atom`) that **no** waiver covers.
* `_deprecated/` is skipped entirely.

Results are stratified, because the layers carry very different risk: a probe
that computes a C-era number for its own consumption is not the same defect as
the shipped `qou-mass` package doing it.

## Usage

    python3 scripts/convention-c-producer-audit.py            # summary
    python3 scripts/convention-c-producer-audit.py --list     # every site
    python3 scripts/convention-c-producer-audit.py --json out.json
    python3 scripts/convention-c-producer-audit.py --selftest

Exit 1 when any non-deliberate site outside the blocked-by-design set is found,
so it can gate. It does **not** currently gate CI — auto-triggers are disabled
repo-wide (owner directive 2026-06-30, Actions billing).
"""

from __future__ import annotations

import argparse
import ast
import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / "lib"))
from convention_c_names import (  # noqa: E402
    deliberate_c_kind, is_deliberate_c_name, selftest_rows)

ROOTS = ("computations", "qou-mass", "tools")

#: A target whose own name declares it convention C is a labelled comparison.
#:
#: This was a single case-folded regex until 2026-08-25, and `re.I` folded its
#: `C_` alternative into `c_`, so it matched ordinary identifiers -- `c_k`,
#: `q_fac_n`, `desc_tr_M`, `__doc__`. See `scripts/lib/convention_c_names.py`
#: for the measurement and for why the obvious widening was rejected.
DELIBERATE = is_deliberate_c_name

#: The registry blocks this path on C by design (`blocked_migrations`).
BLOCKED_BY_DESIGN = "tools/pyhecke/"


def _is_unit_numerator(node: ast.AST) -> bool:
    """Is this a literal one, however the corpus spells it?

    `1`, `1.0` -- and `mpf(1)` / `mp.mpf(1)` / `mpmath.mpf("1")`, which is how
    the corpus writes it, because the NO-FLOAT64 discipline requires carrying
    `mpmath.mpf` rather than a bare Python literal.

    That is the whole reason this matters.  The detector accepted only the bare
    literal, so **complying with the precision discipline made a site invisible
    to the convention detector** -- one house rule blinding another.  Measured
    2026-08-23: teaching it `mpf(1)` took the actionable count from 1 to 11,
    every one of them `1/(sqrt(q) + sqrt(q_inv))` in the Markov role, two of
    them named outright (`Z_MARK`, `z_mark`).  Beans `qou-324i` / `qou-rh31`.
    """
    if isinstance(node, ast.Constant) and node.value in (1, 1.0):
        return True
    if isinstance(node, ast.Call):
        fn = ast.unparse(node.func).split(".")[-1]
        if fn in ("mpf", "mpmathify", "Integer", "Rational") and node.args:
            a = node.args[0]
            if isinstance(a, ast.Constant) and str(a.value).strip('"\'') in ("1", "1.0"):
                return True
    return False


#: Single-argument numeric casts that wrap a value without changing which
#: convention produced it. Blind spelling #14, found 2026-08-22: a convention-C
#: expression inside `float(+( ... ))` is an `ast.Call`, so every shape matcher
#: below bailed at its first isinstance check and the site scanned clean.
#: Measured: `computations/probes/markov_reduction_h3_to_h4_verify.py:60` binds
#: z = 0.4993203342 (= z_C) and this audit reported 0 sites for that file, while
#: the probe's conclusion is cited in `QOU/Machinery/MarkovTraceOnHecke.lean`
#: as the evidence for keystone ingredient 2.
_NUMERIC_CASTS = {"float", "complex", "mpf", "mpmath.mpf", "mp.mpf", "Decimal"}


def unwrap_casts(node: ast.AST) -> ast.AST:
    """Strip numeric-cast calls and unary +/- to expose the arithmetic shape.

    `float(+(1/(sqrt(q) + 1/sqrt(q))))` and `1/(sqrt(q) + 1/sqrt(q))` are the
    same convention; only the second was matchable before. Unary `-` is
    stripped too: `-z_C` is still C-derived and still worth flagging.

    Deliberately conservative -- only SINGLE-argument calls to a known cast
    name are unwrapped, so `Fraction(a, b)` and `round(x, n)` are untouched.
    """
    while True:
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            node = node.operand
            continue
        if (isinstance(node, ast.Call) and len(node.args) == 1
                and not node.keywords
                and ast.unparse(node.func) in _NUMERIC_CASTS):
            node = node.args[0]
            continue
        return node


def is_c_form(node: ast.AST) -> bool:
    """Does this expression have the shape ``1 / (<sqrt-ish> + <anything>)``?

    Deliberately shape-based. It does not try to confirm the second summand is
    the reciprocal of the first — that would need symbolic evaluation, and any
    ``1/(sqrt(...) + ...)`` bound to a ``z``-named variable is worth a human
    look regardless.

    ``**3`` anywhere in the denominator rejects the match: convention D is
    ``q**3/(q**2+1)``, and a stray cube is a strong signal this is not the
    half-argument form.
    """
    node = unwrap_casts(node)
    if not (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)):
        return False
    if not _is_unit_numerator(node.left):
        return False
    den = node.right
    if not (isinstance(den, ast.BinOp) and isinstance(den.op, ast.Add)):
        return False
    # Whitespace-normalised: `ast.unparse` emits `q ** 3`, so a naive `"**3"`
    # test never fires. The selftest caught exactly that.
    src = "".join(ast.unparse(den).split())
    return ("0.5" in src or "sqrt" in src.lower()) and "**3" not in src


def is_c_form_halfarg(node: ast.AST):
    """Convention C written in the HALF-ARGUMENT variable: ``z = r/(r**2 + 1)``.

    With ``r = q^{1/2}``,

        1/(q^{1/2} + q^{-1/2}) = 1/(r + 1/r) = r/(r² + 1)

    so this is the same convention with no square root visible anywhere — no
    ``sqrt`` call, no ``0.5`` exponent, nothing for `is_c_form` to match. It was
    a false-negative class of the audit until `y_lambda_cyclotomic_factor.py:48`
    turned up still on C after the surface had been reported clear.

    The trap is that it looks like convention D. D is ``q**3/(q**2+1)``; this is
    ``r**1/(r**2+1)``, and in the half-argument variable D reads
    ``r**6/(r**4+1)``. Same silhouette, different exponents.

    Returns the base symbol source, or None.
    """
    if not (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)):
        return None
    num = ast.unparse(node.left)
    den = node.right
    if not (isinstance(den, ast.BinOp) and isinstance(den.op, ast.Add)):
        return None
    d = "".join(ast.unparse(den).split())
    return num if d in (f"{num}**2+1", f"1+{num}**2") else None


def _sqrt_of(node: ast.AST):
    """If `node` is a square root of a single symbol, return that symbol's source.

    Accepts `sqrt(X)` under any module alias, and `X ** 0.5` however the corpus
    spells the exponent (`0.5`, `mpf("0.5")`, `mp.mpf('0.5')`). A square root of
    a COMPOUND expression returns None -- `mp.sqrt(q**4 + q**2 + 1)` is a
    polynomial norm, not `q^{1/2}`.
    """
    node = unwrap_casts(node)
    if isinstance(node, ast.Call) and len(node.args) == 1:
        if ast.unparse(node.func).split(".")[-1] == "sqrt":
            a = unwrap_casts(node.args[0])
            return ast.unparse(a) if isinstance(a, ast.Name) else None
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Pow):
        if not isinstance(unwrap_casts(node.left), ast.Name):
            return None
        e = "".join(ast.unparse(node.right).split()).strip("'\"")
        for lit in ("0.5", ".5", "mpf(0.5)", "mpf('0.5')", 'mpf("0.5")'):
            if e == lit or e.endswith("mpf('0.5')") or e.endswith('mpf("0.5")') \
                    or e.endswith("mpf(0.5)"):
                return ast.unparse(unwrap_casts(node.left))
        return None
    return None


def is_c_form_direct(node: ast.AST):
    """Convention C written DIRECTLY: ``z = sqrt(q) / (q + 1)``.

    Algebraically identical to the reciprocal form the rest of this file
    matches -- ``sqrt(q)/(q+1) == 1/(sqrt(q) + 1/sqrt(q))``, the same number
    ``0.4993203342`` -- but structurally nothing like it. There is no unit
    numerator, so `is_c_form` bails at `_is_unit_numerator`; the numerator is
    not the same symbol as the denominator's square, so `is_c_form_halfarg`
    bails too. Bound to an ordinary name like `z`, the site is invisible to
    every matcher here. Blind spelling #15, bean `qou-l7j1`.

    It is the *spelling*, not the position, that hides these -- which makes it
    a distinct class from the tuple-return blind spot (`_li_2_q_util.py:302`
    went unreported while `:312` was listed) even though both present as "the
    detector's list is a floor, not a census".

    Requires the denominator to be exactly ``<base> + 1`` (or ``1 + <base>``)
    for the SAME base the numerator takes the root of. That is what keeps the
    precision: ``sqrt(q)/(q**2 + 1)`` and ``sqrt(q)/(q + 2)`` are different
    numbers and are not matched. With the base tied, any hit IS `z_C` as an
    algebraic identity, so this widening cannot produce a false positive about
    the VALUE -- only about whether that value is playing the Markov role,
    which is the same judgement every other matcher here leaves to the reader.

    Returns the base symbol source, or None.
    """
    node = unwrap_casts(node)
    if not (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)):
        return None
    base = _sqrt_of(node.left)
    if base is None:
        return None
    den = unwrap_casts(node.right)
    if not (isinstance(den, ast.BinOp) and isinstance(den.op, ast.Add)):
        return None
    d = "".join(ast.unparse(den).split())
    b = "".join(base.split())
    return base if d in (f"{b}+1", f"1+{b}", f"{b}+1.0", f"1.0+{b}") else None


def _defines_convention_d(src: str, sym: str) -> bool:
    """Does `src` bind `sym` to the convention-D Markov parameter?

    Matches `<sym> = <base>**3 / (<base>**2 + 1)` modulo whitespace and the
    choice of base name -- the same normalisation `is_c_form` uses, since
    `ast.unparse` spells it `q ** 3`. Assignment only, at module level or not;
    a comment mentioning D does not count.
    """
    try:
        tree = ast.parse(src)
    except (SyntaxError, ValueError):
        return False
    for n in ast.walk(tree):
        if not isinstance(n, (ast.Assign, ast.AnnAssign)):
            continue
        targets = n.targets if isinstance(n, ast.Assign) else [n.target]
        if not any(isinstance(t, ast.Name) and t.id == sym for t in targets):
            continue
        if n.value is None:
            continue
        s = "".join(ast.unparse(n.value).split())
        base = s.split("**3", 1)[0]
        if base and s in (f"{base}**3/({base}**2+1)", f"{base}**3/(1+{base}**2)"):
            return True
    return False


def _module_path_of(file: str) -> str:
    """`tools/pyhecke/python/pyhecke/gram.py` -> `pyhecke.gram`.

    The LAST occurrence of the package name is the package root; the first is
    the containing directory, which yields the nonsense
    `pyhecke.python.pyhecke.gram`. The selftest caught exactly that, which is
    why this is a named function with its own fixtures rather than four lines
    inline reading from the live registry.
    """
    parts = pathlib.Path(file).with_suffix("").parts
    pkg = next((c for c in reversed(parts[:-1])
                if c not in ("python", "src", "tools", "lib")), None)
    if pkg and pkg in parts:
        i = len(parts) - 1 - parts[::-1].index(pkg)
        return ".".join(parts[i:])
    return parts[-1] if parts else file


def declared_c_files(repo: pathlib.Path):
    """Files whose C is DECLARED in the registry — registered, not unexplained.

    `blocked_migrations` is no longer the only way the registry accounts for a
    convention-C symbol. A site can also be recorded as a C entry under
    `evaluators.z`, where R9 imports it and asserts its value numerically, with
    its module listed in `intra_module_split_waivers`. That is a STRONGER
    record than a blocked row ever was: a blocked row is prose, an evaluator
    entry is checked against the running code on every validator run.

    Without this, emptying `blocked_migrations` -- which is what resolving the
    gram.py row correctly DID -- silently reclassifies four fully-registered
    sites as "NO registry row (unexplained)". The registry and this detector
    then disagree about the same four sites while both are working as designed.

    Declared does NOT mean excused. The R10 waiver says in terms that the split
    is "an open defect, not an approved design", so these stay ACTIONABLE and
    stay in the count; only the LABEL changes. A positive declaration has to be
    visible in the count rather than swallowed by it, or the declaration
    becomes a way to make the inventory smaller without making the corpus
    better.
    """
    reg = repo / "docs/coordination/trace-convention-registry.json"
    try:
        r = json.loads(reg.read_text())
    except (OSError, json.JSONDecodeError):
        return {}
    waived = set(r.get("intra_module_split_waivers", []))
    out: dict[str, list] = {}
    for e in r.get("evaluators", {}).get("z", []):
        if e.get("convention") != "C":
            continue
        mod, sym = e.get("module", ""), e.get("symbol", "")
        if mod not in waived:
            continue
        f = e.get("file") or _file_of_module(repo, mod)
        if f:
            out.setdefault(f, []).append(sym)
    return {f: sorted(set(syms)) for f, syms in out.items()}


def _file_of_module(repo: pathlib.Path, mod: str):
    """Best-effort module dotted-path -> repo-relative file."""
    tail = mod.replace(".", "/") + ".py"
    for cand in repo.rglob("*/" + tail):
        if ("_deprecated" not in str(cand) and "fsh-guts" not in str(cand)) and "node_modules" not in str(cand):
            return str(cand.relative_to(repo))
    return None


def rederivation_blocked_files(repo: pathlib.Path):
    """Files the registry records as PENDING the qou-cds1 ladder re-derivation.

    A third way the registry accounts for a convention-C site, alongside
    `blocked_migrations` (stays C permanently, by design) and the `evaluators.z`
    + `intra_module_split_waivers` pair (declared, R9-asserted). These sites
    must NOT stay on C -- but a z_D substitution changes what the site ASSERTS
    rather than the coordinate it asserts it in, so the migration is carried by
    the re-derivation, not by a sweep.

    Measured, per row: `z_C` is bar-EVEN and `z_D` is bar-NEITHER, so every
    bar-parity result stated for `z` has no D-frame statement to migrate TO;
    `ord_{q=1}(z - 1/2)` is 2 under C and 1 under D, so the even-order premise
    of the T3 exclusion is simply false under D; the ladder phase `(z-1)h/2`
    moves 22.6 % at the proton pin.

    Like `declared_c_files`, this ACCOUNTS FOR a site without EXCUSING it:
    these stay in the actionable count and only the label changes. A registry
    row that shrinks the headline number would be a way to make the inventory
    smaller without making the corpus better -- which is the failure this whole
    detector exists to prevent.
    """
    reg = repo / "docs/coordination/trace-convention-registry.json"
    try:
        rows = json.loads(reg.read_text()).get("blocked_on_rederivation", [])
    except (OSError, json.JSONDecodeError):
        return {}
    out: dict[str, list] = {}
    for r in rows:
        f, sym = r.get("file", ""), r.get("symbol", "")
        if not f or not sym:
            continue
        # VERIFY THE PREMISE, exactly as blocked_symbols does: a row asserting
        # a site is still C is a liability the moment the site moves to D.
        try:
            src = (repo / f).read_text()
        except OSError:
            src = ""
        if src and _defines_convention_d(src, sym):
            print(f"  REGISTRY STALE: {f}::{sym} is registered under "
                  f"blocked_on_rederivation but the file defines it as "
                  f"convention D. Drop the row; the site has migrated.")
            continue
        out.setdefault(f, []).append(sym)
    return {f: sorted(set(v)) for f, v in out.items()}


def closed_form_measured_clear(repo: pathlib.Path):
    """(file, symbol) pairs whose half-power the registry records as MEASURED clear.

    `scan_closed_forms` is static. Its fingerprint is a half-integer power of `q`
    in the source of a trace/weight binding, and that is a SHAPE -- the question
    it stands in for is whether the quantity the binding RETURNS carries one.
    Usually those agree. When they do not, the discriminator is the answer, not
    the source, and a static scanner cannot reach it.

    So a row here does NOT drop the site from the report. It labels it with the
    measurement, so the next drain does not re-derive it, and leaves the count
    alone -- the same accounting-without-excusing rule `blocked_on_rederivation`
    follows. Suppressing instead would be how the previous four detector blind
    spots were made (`docs/audits/2026-08-15-detector-blindness-taxonomy.md`):
    a rule broad enough to skip this site would also skip a genuinely C-derived
    closed form back-substituted the same way.
    """
    reg = repo / "docs/coordination/trace-convention-registry.json"
    try:
        rows = json.loads(reg.read_text()).get("closed_form_measured_clear", [])
    except (OSError, json.JSONDecodeError):
        return {}
    out = {}
    for r in rows:
        f, sym = r.get("file", ""), r.get("symbol", "")
        if f and sym:
            out[(f, sym)] = r.get("verdict", "measured clear")
    return out


def blocked_symbols(repo: pathlib.Path):
    """The (module, symbol) pairs the registry deliberately leaves on C.

    Read from `blocked_migrations` rather than hardcoded, so a registry edit
    re-arms this automatically — the same rule the content axis follows.
    """
    reg = repo / "docs/coordination/trace-convention-registry.json"
    try:
        rows = json.loads(reg.read_text()).get("blocked_migrations", [])
    except (OSError, json.JSONDecodeError):
        return []
    out = []
    for r in rows:
        f, sym = r.get("file", ""), r.get("symbol", "")
        if not f or not sym:
            continue
        # VERIFY THE PREMISE. A blocked row asserts the symbol is still C; if
        # the file has since moved to D, every "leak" derived from this row is
        # a false positive, and the row itself is the defect.
        #
        # This is not hypothetical. gram.py moved to D on 2026-08-15 (bean
        # qou-w8zz) and this row was not updated with it, so R9 went red on
        # main and this detector reported 25 production sites "receiving
        # convention C" that were receiving D. A detector that trusts a record
        # inherits the record's staleness -- the same failure the whole
        # excision has been unpicking, arriving in the tool built to find it.
        src_path = repo / f
        try:
            src = src_path.read_text()
        except OSError:
            src = ""
        if src and _defines_convention_d(src, sym):
            print(f"  REGISTRY STALE: {f}::{sym} is registered as convention "
                  f"{r.get('stays', '?')} under blocked_migrations, but the file "
                  f"defines it as convention D. Every leak derived from this row "
                  f"is a false positive; fix the registry, not the callers.")
            continue
        mod = _module_path_of(f)
        out.append((mod, sym, r.get("reason", ""), r.get("bean", "")))
    return out


#: A name that plausibly denotes the substrate parameter.
_Q_LIKE = re.compile(r"^_?[qQ][A-Za-z0-9_]{0,6}$")

#: A binding that names a Markov trace or a Wedderburn weight -- the
#: quantities that are rational in q under convention D, so a half-integer
#: power in one is z_C showing through.
#: `bond` / `f_pp` / `f_pn` / `f_nn` added 2026-08-25 (bean `qou-l7j1`). Per-bond
#: energies are Wedderburn weights by another name, and they are where the
#: half-integer power actually surfaced: `mirror_split_milnor_one_third_probe.py`
#: writes `f_nn` and `f_pn` with `q0 ** mpf("1.5")` two lines under an
#: unlabelled `z = sqrt(q0)/(q0+1)`.
#:
#: MEASURED before adding, because over-breadth is this scanner's whole risk
#: (its first version returned 50 sites, nearly all legitimate square roots).
#: Corpus-wide the widening adds exactly THREE bindings, all in that one file,
#: all genuine -- 3/3. It buys the bean's own named instance and nothing else,
#: and all three land in the second tier rather than the actionable count.
TRACE_OR_WEIGHT = re.compile(
    r"tr_?M|trace|^W\d|_W\d|\bW\d+\b|y_lam|y_lambda|weight|wenzl|hopf|census"
    r"|bond|^f_(pp|pn|nn|np)$",
    re.I)


def _is_q_like(node: ast.AST) -> bool:
    return isinstance(node, ast.Name) and bool(_Q_LIKE.match(node.id))


def _half_integer(node: ast.AST):
    """If `node` is a half-but-not-whole number, return it; else None.

    Accepts the literal `0.5`/`1.5`, `mp.mpf("1.5")`, `sp.Rational(3, 2)` and
    `sp.Rational(1, 2)` — the spellings this corpus actually uses for a
    half-integer exponent.
    """
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        v = float(node.value)
        return v if (v * 2) % 2 == 1 else None
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        inner = _half_integer(node.operand)
        return None if inner is None else -inner
    if isinstance(node, ast.Call):
        fn = ast.unparse(node.func)
        if fn.endswith("mpf") and node.args:
            return _half_integer(node.args[0]) if not isinstance(
                node.args[0], ast.Constant) or not isinstance(
                node.args[0].value, str) else (
                    float(node.args[0].value)
                    if (float(node.args[0].value) * 2) % 2 == 1 else None)
        if fn.endswith("Rational") and len(node.args) == 2:
            try:
                num, den = node.args[0].value, node.args[1].value
                return num / den if den == 2 and num % 2 == 1 else None
            except (AttributeError, TypeError, ZeroDivisionError):
                return None
    return None


def scan_closed_forms(roots=ROOTS, c_files=()):
    """Find CONVENTION-C-SPECIALISED CLOSED FORMS -- the third blind spot.

    Migrating `z` is not migrating the file. Quantities DERIVED from `z` get
    written out in closed form, and a closed form derived under convention C
    carries `z_C`'s square root where the general identity has none:

        tr_M(sigma_1^2) = h*z + 1        at z_C  ->  1 + (q-1)/q^{1/2}
        y_(2)  = (q*z + 1)/(q^2 + 1)     at z_C  ->  (q^{3/2}+q+1)/(q^3+q^2+q+1)

    `scan()` cannot see either: it keys on an assignment target containing
    `z`, and these are named `trM_sigma1_sq`, `W2`, `W11`, `census_hopf`. Four
    such sites had to be found by hand after the producers they live in were
    already reported migrated, and one of them (`trM_symbolic`) was missed even
    then -- caught only because the file cross-checks its symbolic path against
    its numeric one.

    So the fingerprint is not the name, it is the EXPONENT. Convention D is
    rational in `q`; a half-integer power of the substrate parameter cannot
    arise from it. Two shapes are matched:

        sqrt(q) / q**0.5 / q**1.5 / q**mpf("1.5") / q**Rational(3,2)
        rt = sqrt(q)  ...  rt**3            (indirect, one hop)

    `sqrt` of a COMPOUND expression is not matched — `mp.sqrt(q**4+q**2+1)` is
    a legitimate polynomial norm, not `q^{1/2}`.

    Reported for files that ALSO define `z` the convention-D way: in a file
    still wholly on C a square root is expected and is `scan()`'s business,
    whereas in a migrated file it is a leftover.

    ## That rationale had a hole, and `c_files` is the patch (bean `qou-l7j1`)

    "is `scan()`'s business" ASSUMES `scan()` SEES THE FILE. When the file's
    `z` used a spelling no matcher knew -- `z = sqrt(q)/(q+1)`, blind spelling
    #15 -- `scan()` missed it, this function skipped it by design, and the file
    was invisible to **both halves of the audit** at once. Worked instance:
    `deltalambda/mirror_split_milnor_one_third_probe.py` binds that `z` and
    then writes `f_pp`/`f_pn`/`f_nn` bond weights carrying `q0 ** 1.5` -- which
    is exactly the half-integer fingerprint this function exists to catch.

    Half the fix is `is_c_form_direct`, which makes `scan()` see it. The other
    half is here: a file `scan()` reports as C is passed in as `c_files` and
    its closed forms are collected into a SEPARATE, second-tier bucket. They
    are not defects *yet* -- the file's `z` is the defect and is already in the
    actionable list -- but they are work that the `z` migration does not
    finish, and an agent who migrates only the `z` will otherwise call the file
    done. Keeping them out of the actionable count preserves the narrowing
    below; surfacing them at all is what stops the two halves of the audit
    pointing at each other.

    ## Narrowed to trace/weight bindings, deliberately

    The first version of this matched any half-power of `q` in a D-migrated
    file and returned 50 sites, most of them legitimate. `q^{1/2}` is not by
    itself a convention-C marker: `q^{1/2}+q^{-1/2}` is `[2]_{sqrt q}`, the
    Temperley–Lieb loop parameter at half-argument, and it turns up in Wenzl
    positivity, in pair-skein formulas, and in the Jones variable change
    `t = q^{-2}`, `A^2 = -q`. `trace-convention-audit.ts` records the same
    finding on the content side: 58 files carry the expression and flagging
    them "would repeat the loose-grep error that once reported 70 producers
    where the truth was 13".

    So the match is narrowed to a half-power appearing in a binding whose NAME
    says it is a trace or a Wedderburn weight — `trM`, `tr_m`, `W2`, `W11`,
    `y_lambda`, `weight`, `hopf`, `census`. That is exactly the claim the
    detector makes: those quantities are rational in `q` under D, so a square
    root in one is `z_C` showing through. A half-power anywhere else is
    somebody's legitimate `sqrt`, and not this detector's business.

    Bindings whose name declares convention C (`..._C`, `census_hopf_C`) are
    exempt, matching how `scan()` treats deliberately C-named targets: a
    labelled cross-convention reference is a comparison, not a defect.
    """
    out = []
    for r in roots:
        base = pathlib.Path(r)
        if not base.exists():
            continue
        for p in sorted(base.rglob("*.py")):
            sp_ = str(p)
            if ("_deprecated" in sp_ or "fsh-guts" in sp_) or "/from_scratch/" in sp_:
                continue
            try:
                src = p.read_text()
                tree = ast.parse(src)
            except (SyntaxError, UnicodeDecodeError, OSError):
                continue
            # Files that have already moved to D: a square root there is a
            # leftover. Files `scan()` reports as still on C: second tier --
            # see the docstring; their `z` is the listed defect, these are the
            # work it does not finish.
            pending = sp_ in c_files
            if not pending:
                if "**3" not in "".join(src.split()).replace("* *", "**"):
                    continue
                if not any(_defines_convention_d(src, t.id)
                           for n in ast.walk(tree)
                           if isinstance(n, ast.Assign)
                           for t in n.targets if isinstance(t, ast.Name)) \
                   and not any(_returns_convention_d(fn) for fn in ast.walk(tree)
                               if isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef))):
                    continue

            # locals bound to sqrt(q), for the one-hop `rt**3` shape
            roots_of_q = {
                t.id for n in ast.walk(tree) if isinstance(n, ast.Assign)
                for t in n.targets if isinstance(t, ast.Name)
                if isinstance(n.value, ast.Call)
                and ast.unparse(n.value.func).endswith("sqrt")
                and n.value.args and _is_q_like(n.value.args[0])
            }

            def _half_power_in(node):
                """First half-power of q inside `node`, or None."""
                for n in ast.walk(node):
                    if isinstance(n, ast.Call) and ast.unparse(n.func).endswith("sqrt") \
                            and n.args and _is_q_like(n.args[0]):
                        return f"sqrt({ast.unparse(n.args[0])})"
                    if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Pow):
                        if _is_q_like(n.left) and _half_integer(n.right) is not None:
                            return ast.unparse(n)
                        if (isinstance(n.left, ast.Name) and n.left.id in roots_of_q
                                and isinstance(n.right, ast.Constant)
                                and isinstance(n.right.value, int)
                                and n.right.value % 2 == 1):
                            return f"{ast.unparse(n)}  (with {n.left.id} = sqrt(q))"
                return None

            # Only bindings that NAME a trace or a Wedderburn weight. See the
            # docstring: a half-power elsewhere is somebody's legitimate sqrt.
            for n in ast.walk(tree):
                names, value = [], None
                if isinstance(n, ast.Assign) and n.value is not None:
                    names = [t.id for t in n.targets if isinstance(t, ast.Name)]
                    value = n.value
                elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    names, value = [n.name], n
                if not names or value is None:
                    continue
                if not any(TRACE_OR_WEIGHT.search(nm) for nm in names):
                    continue
                if any(DELIBERATE(nm) for nm in names):
                    continue
                hit = _half_power_in(value)
                if hit:
                    out.append((sp_, getattr(value, "lineno", n.lineno),
                                f"{names[0]} <- {hit}", pending))
    return out


#: Selftest fixtures for blind spelling #17 (D arm as a call). Module level so
#: the selftest reads as three contrasting sources rather than inline strings.
_D_CALL_SRC = (
    "def markov_z(q):\n    return q ** 3 / (q ** 2 + 1)\n"
    "def z_of(q, conv):\n"
    "    if conv == 'D': return markov_z(q)\n"
    "    if conv == 'C': return mp.sqrt(q) / (q + 1)\n"
)
_C_CALL_SRC = (
    "def markov_z(q):\n    return 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))\n"
    "def z_of(q, conv):\n"
    "    if conv == 'D': return markov_z(q)\n"
    "    if conv == 'C': return mp.sqrt(q) / (q + 1)\n"
)
_UNRESOLVED_SRC = (
    "def z_of(q, conv):\n"
    "    if conv == 'D': return some_unknown_helper(q)\n"
    "    if conv == 'C': return mp.sqrt(q) / (q + 1)\n"
)


def _is_literal_d(v: ast.AST) -> bool:
    """Is this expression literally `x**3/(x**2+1)` (either factor order)?"""
    while isinstance(v, ast.UnaryOp) and isinstance(v.op, ast.UAdd):
        v = v.operand
    s = "".join(ast.unparse(v).split())
    b = s.split("**3", 1)[0]
    return bool(b) and s in (f"{b}**3/({b}**2+1)", f"{b}**3/(1+{b}**2)")


def _resolve_callee_returns_d(name: str, tree, path: str, repo=None) -> bool:
    """Does `name`, resolved to its definition, return the literal D form?

    Blind spelling #17, found 2026-08-29 (bean `qou-1jny`).  The dispatcher
    test below matched only the INLINE `q**3/(q**2+1)`, so a two-arm
    comparison helper whose D arm CALLS the canonical parameter --

        def z_of(q, convention):
            if convention == "D":
                return markov_z(q)          # <- canonical D, as a call
            if convention == "C":
                return mp.sqrt(q) / (q + 1)

    -- read as a bare convention-C leak, and `he4_body_order_shortfall_
    location_probe.z_of` was counted ACTIONABLE for exactly that reason while
    its own docstring scopes the C arm "never wired".  The same D-arm-as-call
    defeats `convention-c-value-audit.py`'s co-binding hint, which looks for a
    z_D *binding* in the scope and finds a call.

    Note which way the incentive runs: re-spelling `q**3/(q**2+1)` inline
    passes, and calling the canonical helper -- the DRY thing, the thing that
    survives the next convention migration -- fails.  One house rule blinding
    another, the same shape as the `mpf(1)` note in `_is_unit_numerator`.

    Resolution is by SHAPE at the definition, never by the callee's name.  A
    name test would be the evasion surface the comparison ledger exists to
    close, and it would be wrong on this corpus's own history:
    `mu4_rhoF_cluster_derivation_probe.markov_z` was "a PRIVATE re-derivation
    of convention C ... which shadowed the library function and so survived
    the gram.py migration untouched".  Same name, opposite convention.  So an
    unresolvable callee is NOT a dispatcher: it stays actionable.
    """
    if repo is None:
        repo = pathlib.Path(".")
    # A local def in the same module wins, exactly as Python resolves it.
    for n in ast.walk(tree):
        if isinstance(n, ast.FunctionDef) and n.name == name:
            return any(isinstance(r, ast.Return) and r.value is not None
                       and _is_literal_d(r.value) for r in ast.walk(n))
    # Otherwise follow `from <module> import <name>` to the defining file.
    for n in ast.walk(tree):
        if not isinstance(n, ast.ImportFrom) or not n.module:
            continue
        if not any(a.asname == name or (a.asname is None and a.name == name)
                   for a in n.names):
            continue
        real = next((a.name for a in n.names
                     if a.asname == name or a.name == name), name)
        stem = n.module.rsplit(".", 1)[-1]
        here = pathlib.Path(path).parent
        for cand in (here / f"{stem}.py", *repo.rglob(f"{stem}.py")):
            try:
                sub = ast.parse(cand.read_text())
            except (SyntaxError, UnicodeDecodeError, OSError):
                continue
            for d in ast.walk(sub):
                if isinstance(d, ast.FunctionDef) and d.name == real:
                    return any(isinstance(r, ast.Return) and r.value is not None
                               and _is_literal_d(r.value) for r in ast.walk(d))
    return False


def _returns_convention_d(fn, tree=None, path=None, repo=None) -> bool:
    """Does this function return `q**3/(q**2+1)`, inline or via a call?

    `tree`/`path` are the enclosing module; without them only the inline form
    is recognised, which is the pre-2026-08-29 behaviour.
    """
    for r in ast.walk(fn):
        if not isinstance(r, ast.Return) or r.value is None:
            continue
        v = r.value
        while isinstance(v, ast.UnaryOp) and isinstance(v.op, ast.UAdd):
            v = v.operand
        if _is_literal_d(v):
            return True
        if (tree is not None and isinstance(v, ast.Call)
                and isinstance(v.func, (ast.Name, ast.Attribute))):
            nm = ast.unparse(v.func).split(".")[-1]
            if _resolve_callee_returns_d(nm, tree, path or ".", repo):
                return True
    return False


def scan_reexports(roots=ROOTS, repo: pathlib.Path = None):
    """Find where a registry-BLOCKED convention-C symbol escapes its module.

    `blocked_migrations` records a symbol that stays on convention C for a
    stated reason — for `pyhecke.gram.z` it is that `G_INV = np.linalg.inv(G)`
    runs at module import and the Markov–Gram is singular under D, so flipping
    the line silently corrupts every consumer of `G_INV`.

    That exception is only sound while the symbol stays *inside* the blocked
    module. It does not:

        computations/substrate/hecke_core.py:61
            from pyhecke.gram import (z, W_SYM, W_STD, W_ALT, ...)

    and then production computations do `from hecke_core import z as Z_MARKOV`
    and use it as the Markov parameter. The registry's containment is a
    statement about one file; nothing checked that the file kept it.

    `is_c_form` cannot see this — there is no `1/(sqrt(q) + ...)` anywhere, just
    an import. So the audit reported the producer surface clear while the
    shared substrate module was handing convention C to every caller that asked
    for `z`.

    Two levels are reported: modules importing the blocked symbol directly, and
    modules importing it from *those* (the actual consumer surface).
    """
    repo = repo or pathlib.Path(".")
    blocked = blocked_symbols(repo)
    if not blocked:
        return []

    direct, out = {}, []
    for mod, sym, reason, bean in blocked:
        tail = mod.rsplit(".", 1)[-1]
        for r in roots:
            base = pathlib.Path(r)
            if not base.exists():
                continue
            for p in sorted(base.rglob("*.py")):
                sp = str(p)
                if ("_deprecated" in sp or "fsh-guts" in sp) or sp.startswith(BLOCKED_BY_DESIGN):
                    continue
                try:
                    tree = ast.parse(p.read_text())
                except (SyntaxError, UnicodeDecodeError, OSError):
                    continue
                for n in ast.walk(tree):
                    if not isinstance(n, ast.ImportFrom) or not n.module:
                        continue
                    if not (n.module == mod or n.module.endswith(f".{tail}") or n.module == tail):
                        continue
                    for a in n.names:
                        if a.name != sym:
                            continue
                        out.append((sp, n.lineno, f"{mod}.{sym}", a.asname or sym,
                                    "direct", reason, bean))
                        direct[pathlib.Path(sp).stem] = a.asname or sym

    # Second hop: who imports the re-exported name from the leaking module.
    for r in roots:
        base = pathlib.Path(r)
        if not base.exists():
            continue
        for p in sorted(base.rglob("*.py")):
            sp = str(p)
            if ("_deprecated" in sp or "fsh-guts" in sp) or sp.startswith(BLOCKED_BY_DESIGN):
                continue
            if pathlib.Path(sp).stem in direct:
                continue
            try:
                tree = ast.parse(p.read_text())
            except (SyntaxError, UnicodeDecodeError, OSError):
                continue
            for n in ast.walk(tree):
                if not isinstance(n, ast.ImportFrom) or not n.module:
                    continue
                src = n.module.rsplit(".", 1)[-1]
                if src not in direct:
                    continue
                for a in n.names:
                    if a.name == direct[src]:
                        out.append((sp, n.lineno, f"{src}.{a.name}", a.asname or a.name,
                                    "via " + src, "", ""))
    return out


def _half_argument_vars(tree: ast.AST) -> set:
    """Names `t` for which the file declares `<q-like> = t ** 2`.

    Such a `t` IS `sqrt(q)`, so `z = 1/(t + 1/t)` is convention C written with
    no square root anywhere -- no `sqrt` call, no `0.5` exponent, and not the
    `t/(t**2+1)` shape `is_c_form_halfarg` matches either. It is the third
    spelling of C and it defeated both z-detectors:

        t = sp.symbols("t", positive=True)
        q = t ** 2
        z = 1 / (t + 1 / t)          # <- convention C, invisible

    Shape alone cannot decide this, and that is the point: `1/(q + 1/q)` is
    `1/[2]_q`, the Temperley-Lieb loop reciprocal, which the selftest requires
    NOT be flagged. The two are character-for-character identical and differ
    only in whether the variable is `q` or `sqrt(q)`. So the file has to say
    so, and here it does -- `q = t ** 2` is the declaration.
    """
    out = set()
    for n in ast.walk(tree):
        if not isinstance(n, ast.Assign) or n.value is None:
            continue
        if not any(_is_q_like(t) for t in n.targets):
            continue
        v = n.value
        if (isinstance(v, ast.BinOp) and isinstance(v.op, ast.Pow)
                and isinstance(v.left, ast.Name)
                and isinstance(v.right, ast.Constant) and v.right.value == 2):
            out.add(v.left.id)
    return out


def is_c_form_reciprocal(node: ast.AST, half_vars: set):
    """`1 / (t + 1/t)` where `t` is a declared half-argument variable."""
    if not half_vars:
        return None
    if not (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)):
        return None
    if not _is_unit_numerator(node.left):
        return None
    den = node.right
    if not (isinstance(den, ast.BinOp) and isinstance(den.op, ast.Add)):
        return None
    d = "".join(ast.unparse(den).split())
    for t in half_vars:
        if d in (f"{t}+1/{t}", f"1/{t}+{t}"):
            return t
    return None


def _area_of(path: str) -> str:
    """The area label a blocked/declared site is reported under.

    Kept deliberately coarse — it names where to LOOK, not what the site is.
    """
    for pfx in ("tools/pyhecke/", "computations/probes/", "computations/qbeta/",
                "computations/deltalambda/", "qou-mass/", "tools/"):
        if path.startswith(pfx):
            return pfx.rstrip("/")
    return path.split("/", 1)[0] if "/" in path else path


def classify(path: str, blocked_files=(), declared_files=(),
             rederivation_files=()) -> str:
    """Bucket a site. `blocked_files` comes from the registry, not from here.

    This used to label EVERY site under `tools/pyhecke/` "BLOCKED on C by
    design", justified by a single `blocked_migrations` row for
    `gram.py::z`. The blanket was too wide: the row covered the module-level
    `z` and nothing else, while three function-local C definitions sheltered
    under the same label -- two of them inside `gram.py` itself.

    When `gram.py::z` moved to D and the row was resolved, those three stopped
    having any registry basis at all, and a path-prefix classifier would have
    gone on calling them "by design" forever. Deriving the label from the
    registry means a site is only excused while a row actually excuses it.
    """
    if path in blocked_files:
        # The bucket name carries the AREA, not a fixed "tools/pyhecke" — a
        # blocked row is keyed on a file path and nothing restricts it to that
        # package. It read "tools/pyhecke — BLOCKED on C by design" for every
        # blocked file until 2026-08-25, when the first non-pyhecke row landed
        # (computations/probes/markov_reduction_h3_to_h4_verify.py, bean
        # qou-ze9n) and the summary line filed a computations/ probe under a
        # tools/ heading. Harmless to the count, but the count is not what a
        # reader uses to go find the site.
        return f"{_area_of(path)} — BLOCKED on C by design (registry)"
    if path in declared_files:
        return ("tools/pyhecke — DECLARED C in evaluators.z, R10-waived "
                "(open defect, still actionable)")
    if path in rederivation_files:
        # NOT excused. The row records WHY a z-swap is invalid here so the next
        # drain does not re-derive that from scratch; it does not claim the site
        # is finished. See `blocked_on_rederivation_note` in the registry.
        return (f"{_area_of(path)} — BLOCKED on the qou-cds1 re-derivation "
                "(registry, still actionable)")
    if path.startswith(BLOCKED_BY_DESIGN):
        return "tools/pyhecke — C with NO registry row (unexplained)"
    # computations/from_scratch/README.md declares the whole directory
    # DEPRECATED for production (2026-05-29, #1422 decision A') -- kept for
    # pedagogy, "not re-pursued". Same status as _deprecated/, which is
    # skipped outright; bucketed rather than skipped so it stays countable.
    if "/from_scratch/" in path:
        return "from_scratch — DEPRECATED for production (its own README)"
    if "/sage-examples/" in path:
        return "tools/sage-examples — examples, not producers"
    name = pathlib.Path(path).name
    if "/probes/" in path or name.endswith("_probe.py") or "probe" in name:
        return "probes / exploratory"
    if path.startswith("qou-mass"):
        return "qou-mass — SHIPPED PACKAGE"
    if "/sweeps/" in path:
        return "sweeps"
    return "computations — live producers"


def scan(roots=ROOTS, blocked_files=(), declared_files=(), rederivation_files=()):
    """Yield (path, lineno, target_name, source, bucket, deliberate)."""
    for r in roots:
        base = pathlib.Path(r)
        if not base.exists():
            continue
        for p in sorted(base.rglob("*.py")):
            sp = str(p)
            if ("_deprecated" in sp or "fsh-guts" in sp):
                continue
            try:
                tree = ast.parse(p.read_text())
            except (SyntaxError, UnicodeDecodeError, OSError):
                continue
            half_vars = _half_argument_vars(tree)
            for n in ast.walk(tree):
                if not isinstance(n, (ast.Assign, ast.AnnAssign)):
                    continue
                targets = n.targets if isinstance(n, ast.Assign) else [n.target]
                names = [t.id for t in targets if isinstance(t, ast.Name)]
                if not any("z" in nm.lower() for nm in names):
                    continue
                if n.value is None:
                    continue
                if not (is_c_form(n.value) or is_c_form_halfarg(n.value)
                        or is_c_form_reciprocal(n.value, half_vars)
                        or is_c_form_direct(n.value)):
                    continue
                nm = names[0]
                yield (sp, n.lineno, nm, ast.unparse(n.value),
                       classify(sp, blocked_files, declared_files,
                                rederivation_files),
                       bool(DELIBERATE(nm)))

            # RETURNED, not assigned. The scan above keys off an assignment
            # TARGET, so a function that computes the convention straight into
            # its return statement has no target to match and was invisible:
            #
            #     def z_mp(dps=...):
            #         ...
            #         return +(1 / (_mp.sqrt(q) + _mp.sqrt(qi_)))
            #
            # That is `pyhecke.gram.z_mp`, a public 50-dps entry point, and it
            # went unreported through every sweep that claimed the surface was
            # clear. The analogue of "target name contains z" is "function name
            # contains z", which keeps the same guard against matching
            # unrelated `1/(sqrt(...)+...)` arithmetic.
            for fn in ast.walk(tree):
                if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                if "z" not in fn.name.lower():
                    continue
                # A function that returns BOTH a C form and the D form is a
                # convention DISPATCHER, not a defect -- its C branch is the
                # labelled comparison, by construction.
                #
                # qbeta_kc21_parity_convention_immunity_probe.z_of(q, conv)
                # returns sqrt(q)/(1+q) for "C", q**3/(q**2+1) for "D", and
                # q/(1+q**2) for "X (control, in no channel; genericity probe
                # only)". The half-argument matcher fired on the X CONTROL --
                # `q/(1+q^2)` is exactly the r/(r^2+1) shape -- and a control
                # deliberately chosen to be in no channel is the opposite of a
                # convention-C leak.
                #
                # The DELIBERATE exemption could not catch it: it keys on the
                # target NAME, and here the name is `z_of` with the label in a
                # docstring and a branch guard. Returning D somewhere in the
                # same function is the machine-checkable signal.
                dispatcher = _returns_convention_d(fn, tree, sp)
                for r in ast.walk(fn):
                    if not isinstance(r, ast.Return) or r.value is None:
                        continue
                    val = r.value
                    # `+expr` is used in this corpus to pin mpmath precision;
                    # unwrap it or the shape never matches.
                    while isinstance(val, ast.UnaryOp) and isinstance(val.op, ast.UAdd):
                        val = val.operand
                    if not (is_c_form(val) or is_c_form_halfarg(val)
                            or is_c_form_direct(val)):
                        continue
                    yield (sp, r.lineno, f"{fn.name}() -> return",
                           ast.unparse(val),
                           "convention dispatcher (returns C and D) — labelled comparison"
                           if dispatcher else classify(sp, blocked_files,
                                                      declared_files,
                                                      rederivation_files),
                           bool(DELIBERATE(fn.name)) or dispatcher)


def selftest() -> int:
    """Prove the matcher accepts every spelling in the corpus and rejects D.

    A detector that cannot fail is worse than none — the same rule the content
    axis is held to. These fixtures are the real spellings found in
    `computations/`, plus the convention-D forms that must NOT match.
    """
    should_match = [
        "1.0 / (q0**0.5 + qi0**0.5)",
        "1.0 / (q0 ** 0.5 + q0 ** (-0.5))",
        "1.0 / (Q0 ** 0.5 + QI ** 0.5)",
        "1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))",
        "1 / (sp.sqrt(q) + 1 / sp.sqrt(q))",
        "1.0 / (np.sqrt(q) + 1.0 / np.sqrt(q))",
        "1 / (sqrt_q + 1 / sqrt_q)",
        "1 / (q ** mpmath.mpf('0.5') + qi ** mpmath.mpf('0.5'))",
        "1 / (q0 ** mpf('0.5') + q0 ** mpf('-0.5'))",
        "1 / (mp.sqrt(q0) + mp.sqrt(qi))",
        # The mpf(1) numerator. The NO-FLOAT64 discipline requires carrying
        # mpmath.mpf rather than a bare literal, so this is how the corpus
        # actually writes it -- and until 2026-08-23 the matcher accepted only
        # the bare `1`, which meant complying with one house rule made a site
        # invisible to the other. Teaching it took actionable 1 -> 11.
        "mpf(1) / (mp.sqrt(q) + mp.sqrt(qi))",
        "mp.mpf(1) / (mp.sqrt(q) + mp.sqrt(q_inv))",
        "_mp.mpf(1) / (_mp.sqrt(_q) + _mp.sqrt(_qi))",
    ]
    half = [
        ("t / (t ** 2 + 1)", True),        # convention C in r = sqrt(q)
        ("r/(r**2 + 1)", True),
        ("t ** 6 / (t ** 4 + 1)", False),  # convention D in r = sqrt(q)
        ("q ** 3 / (q ** 2 + 1)", False),  # convention D in q
    ]
    should_not = [
        "q ** 3 / (q ** 2 + 1)",          # convention D
        "q0**3 / (q0**2 + 1)",            # convention D
        "1 / (q + 1 / q)",                # 1/[2]_q — the TL loop reciprocal, not z
        "2 / (a + b)",                    # not a reciprocal of the right shape
        "1 / (q ** 3 + q ** 0.5)",        # cube present -> rejected
    ]
    # Blind spelling #14 (2026-08-22): the C expression inside a numeric cast.
    # Every matcher bailed at its first isinstance check, so the site scanned
    # clean while binding z = 0.4993203342 = z_C. Found live at
    # computations/probes/markov_reduction_h3_to_h4_verify.py:60, whose
    # conclusion MarkovTraceOnHecke.lean cites as keystone evidence.
    should_match += [
        "float(+(1.0 / (mp.sqrt(Q) + 1.0 / mp.sqrt(Q))))",   # the live spelling
        "float(1 / (sqrt(q) + 1 / sqrt(q)))",
        "complex(1 / (q ** 0.5 + q ** -0.5))",
        "-(1 / (mp.sqrt(q) + 1 / mp.sqrt(q)))",              # -z_C is still C
        "mp.mpf(1 / (sqrt(q) + 1 / sqrt(q)))",
    ]
    should_not += [
        # The unwrap must stay conservative: multi-arg and unknown calls are
        # NOT casts, and D inside a cast is still D.
        "float(q ** 3 / (q ** 2 + 1))",   # convention D, cast -> still D
        "Fraction(1, q + 1 / q)",         # 2-arg, not a cast
        "round(1 / (sqrt(q) + 1 / sqrt(q)), 6)",  # 2-arg -> not unwrapped
    ]
    bad = 0
    for src in should_match:
        ok = is_c_form(ast.parse(src, mode="eval").body)
        print(f"  {'ok  ' if ok else 'FAIL'}  matches: {src}")
        bad += not ok
    for src in should_not:
        ok = not is_c_form(ast.parse(src, mode="eval").body)
        print(f"  {'ok  ' if ok else 'FAIL'}  rejects: {src}")
        bad += not ok
    for src, want in half:
        got = is_c_form_halfarg(ast.parse(src, mode="eval").body) is not None
        ok = got == want
        verb = "flags" if want else "clears"
        print(f"  {'ok  ' if ok else 'FAIL'}  half-arg {verb}: {src}")
        bad += not ok
    # The re-export detector. `is_c_form` is blind to these by construction --
    # there is no arithmetic to shape-match, only an import -- so it needs its
    # own fixtures or it could silently match nothing forever.
    # Fixtures, not the live registry. These used to assert "the registry has
    # a blocked row", which passed only while one existed -- so resolving
    # gram.py::z turned two green checks red without any logic changing. A
    # selftest that fails when the DATA moves is testing the data.
    checks = [
        ("package root is the LAST occurrence, not the first",
         _module_path_of("tools/pyhecke/python/pyhecke/gram.py") == "pyhecke.gram"),
        ("a plain package path resolves",
         _module_path_of("src/foo/bar.py") == "foo.bar"),
        ("a bare file resolves to its stem",
         _module_path_of("gram.py") == "gram"),
    ]
    # The return-form blind spot. `scan` keyed off an assignment target, so a
    # function returning the convention directly had nothing to match on --
    # five live producers and pyhecke.gram.z_mp went unreported through every
    # sweep that called the surface clear.
    def _returns_found(src: str) -> int:
        tree = ast.parse(src)
        n = 0
        for fn in ast.walk(tree):
            if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if "z" not in fn.name.lower():
                continue
            for r in ast.walk(fn):
                if not isinstance(r, ast.Return) or r.value is None:
                    continue
                v = r.value
                while isinstance(v, ast.UnaryOp) and isinstance(v.op, ast.UAdd):
                    v = v.operand
                n += is_c_form(v) or bool(is_c_form_halfarg(v))
        return n

    # The closed-form scanner. Its whole risk is over-breadth -- the first
    # version returned 50 sites in D-migrated files, nearly all legitimate
    # square roots, which is the loose-grep error this repo has now made
    # twice. These fixtures pin the narrowing.
    def _in_tmp_pkg(body: str, fn):
        """Write `body` as a one-module root and run `fn(rootname)` inside it."""
        import os
        import tempfile
        d = pathlib.Path(tempfile.mkdtemp())
        (d / "m.py").write_text(body)
        cwd = pathlib.Path.cwd()
        try:
            os.chdir(d.parent)
            return fn(d.name)
        finally:
            os.chdir(cwd)

    def _cf(src: str) -> int:
        return _in_tmp_pkg("z = q ** 3 / (q ** 2 + 1)\n" + src,
                           lambda r: len(scan_closed_forms(roots=(r,))))

    def _cf_pending(body: str):
        """(actionable, second-tier) closed-form counts for a whole module."""
        def run(r):
            live = [x for x in scan(roots=(r,)) if not x[5]]
            rows = scan_closed_forms(roots=(r,), c_files={x[0] for x in live})
            return (sum(1 for x in rows if not x[3]), sum(1 for x in rows if x[3]))
        return _in_tmp_pkg(body, run)

    def _scan_src_count(body: str) -> int:
        return _in_tmp_pkg(body, lambda r: len(list(scan(roots=(r,)))))

    # The reciprocal form `1/(t + 1/t)` with `q = t**2` declared. Decidable
    # ONLY from that declaration: it is character-for-character `1/[2]_q`, the
    # Temperley-Lieb loop reciprocal, which must not be flagged. These two
    # fixtures are the whole justification for reading the declaration.
    def _hv(src):
        return _half_argument_vars(ast.parse(src))

    def _recip(src, decl="t = sp.symbols('t')\nq = t ** 2\n"):
        tree = ast.parse(decl + src)
        hv = _half_argument_vars(tree)
        return any(is_c_form_reciprocal(n.value, hv)
                   for n in ast.walk(tree)
                   if isinstance(n, ast.Assign) and n.value is not None)

    checks += [
        ("`q = t ** 2` declares t as the half-argument variable",
         _hv("t = sp.symbols('t')\nq = t ** 2\n") == {"t"}),
        ("no such declaration -> no half-argument variables",
         _hv("q = sp.symbols('q')\nx = q * 2\n") == set()),
        ("`z = 1/(t + 1/t)` with q = t**2 IS convention C",
         _recip("z = 1 / (t + 1 / t)\n")),
        ("the same shape WITHOUT the declaration is 1/[2]_q, not z",
         not _recip("z = 1 / (q + 1 / q)\n", decl="q = sp.symbols('q')\n")),
        ("convention D in the half-argument variable is not flagged",
         not _recip("z = t ** 6 / (t ** 4 + 1)\n")),
        ("a trace closed form with sqrt(q) is flagged",
         _cf("def trM_hopf(q):\n    return 1 + (q - 1) / mp.sqrt(q)\n") == 1),
        ("a Wedderburn weight with q**1.5 is flagged",
         _cf("def wenzl_weights(q):\n    W2 = (q ** 1.5 + q + 1) / d\n    return W2\n") >= 1),
        ("`rt = sqrt(q)` then `rt**3` is flagged through the alias",
         _cf("rt = sp.sqrt(q)\nW2 = (rt ** 3 + q + 1) / d\n") == 1),
        ("sqrt of a POLYNOMIAL is not a half-power of q",
         _cf("def trM_x(q):\n    return mp.sqrt(q ** 4 + q ** 2 + 1)\n") == 0),
        ("a half-power OUTSIDE a trace/weight binding is left alone",
         _cf("def loop_param(q):\n    return mp.sqrt(q) + 1 / mp.sqrt(q)\n") == 0),
        ("a deliberately C-named trace form is exempt",
         _cf("def trM_hopf_census_form_C(q):\n    return 1 + (q - 1) / mp.sqrt(q)\n") == 0),
        ("a file with no convention-D z is not scanned at all",
         len(scan_closed_forms(roots=("nonexistent-dir-xyz",))) == 0),
        ("a bare `return 1/(sqrt(q)+1/sqrt(q))` is found",
         _returns_found("def z_factor(q):\n    return 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))\n") == 1),
        ("mpmath's precision-pinning unary + does not hide it",
         _returns_found("def z_mp(d):\n    return +(1 / (_mp.sqrt(q) + _mp.sqrt(qi_)))\n") == 1),
        ("a convention-D return is NOT flagged",
         _returns_found("def z_mp(d):\n    return q ** 3 / (q ** 2 + 1)\n") == 0),
        ("a function whose name has no z is left alone",
         _returns_found("def loop(q):\n    return 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))\n") == 0),
        # The three pyhecke buckets. Only a blocked_migrations row excuses a
        # site; a registry DECLARATION accounts for it without excusing it,
        # which is the distinction that stopped four registered sites reading
        # as "unexplained" when blocked_migrations was correctly emptied.
        ("a blocked_migrations row excuses a site",
         classify("tools/pyhecke/python/pyhecke/gram.py",
                  blocked_files={"tools/pyhecke/python/pyhecke/gram.py"})
         .startswith("tools/pyhecke — BLOCKED")),
        ("a DECLARED site is labelled as declared, not unexplained",
         "DECLARED C in evaluators.z" in
         classify("tools/pyhecke/python/pyhecke/gram.py",
                  declared_files={"tools/pyhecke/python/pyhecke/gram.py"})),
        ("declaring a site does NOT excuse it -- it stays actionable",
         "still actionable" in
         classify("tools/pyhecke/python/pyhecke/gram.py",
                  declared_files={"tools/pyhecke/python/pyhecke/gram.py"})),
        ("an undeclared pyhecke site is still unexplained",
         classify("tools/pyhecke/python/pyhecke/atom.py",
                  declared_files={"tools/pyhecke/python/pyhecke/gram.py"})
         .endswith("(unexplained)")),
        ("a blocked row outranks a declaration for the same file",
         classify("tools/pyhecke/python/pyhecke/gram.py",
                  blocked_files={"tools/pyhecke/python/pyhecke/gram.py"},
                  declared_files={"tools/pyhecke/python/pyhecke/gram.py"})
         .startswith("tools/pyhecke — BLOCKED")),
        # blocked_on_rederivation: the third accounting channel. It must label
        # WITHOUT excusing -- a row that shrank the headline count would let the
        # inventory get smaller while the corpus stayed the same.
        ("a re-derivation-blocked site is labelled as such",
         "BLOCKED on the qou-cds1 re-derivation" in
         classify("computations/qbeta/p.py",
                  rederivation_files={"computations/qbeta/p.py"})),
        ("a re-derivation-blocked site stays ACTIONABLE",
         "still actionable" in
         classify("computations/qbeta/p.py",
                  rederivation_files={"computations/qbeta/p.py"})
         and not any(e in classify("computations/qbeta/p.py",
                                   rederivation_files={"computations/qbeta/p.py"})
                     for e in ("BLOCKED on C by design", "DEPRECATED for production"))),
        ("a permanent blocked_migrations row still outranks a re-derivation row",
         classify("computations/probes/m.py",
                  blocked_files={"computations/probes/m.py"},
                  rederivation_files={"computations/probes/m.py"})
         .endswith("BLOCKED on C by design (registry)")),
        # closed_form_measured_clear: a LABEL, never a suppression. The site must
        # still be reported; only an annotation is added. A future edit that
        # turned this into a filter would be caught by the count assertion in
        # the second test.
        ("the live registry records the measured-clear closed form",
         ("computations/probes/qbeta_5two_categorical_markov_volume_probe.py",
          "ocneanu_weights") in closed_form_measured_clear(pathlib.Path("."))),
        ("a measured-clear row does NOT remove the site from scan_closed_forms",
         any(c[0].endswith("qbeta_5two_categorical_markov_volume_probe.py")
             for c in scan_closed_forms(roots=("computations/probes",)))),
        # The live registry must actually carry the seven qbeta-cone rows.
        # A FLOOR plus membership, not an exact count. This asserted `== 7`
        # and went red on 2026-08-29 when `e65c8b8151` legitimately registered
        # more rows -- an exact count turns every deliberate registration into
        # a test failure, which trains the next agent to edit the number
        # without reading it. The property that matters is that the qbeta cone
        # is actually covered and that rows are not silently LOST.
        ("the live registry records the qbeta-cone re-derivation blocks",
         len(rederivation_blocked_files(pathlib.Path("."))) >= 7
         and any("qbeta" in f for f in rederivation_blocked_files(pathlib.Path(".")))),
        # declared_c_files reads the LIVE registry: a C evaluator whose module
        # is NOT waived must not be silently treated as declared.
        ("an unwaived C evaluator does not count as declared",
         "pyhecke/atom.py" not in
         " ".join(declared_c_files(pathlib.Path(".")))),
        # A convention DISPATCHER is a labelled comparison by construction.
        # qbeta_kc21_parity_convention_immunity_probe.z_of returns C, D and an
        # X control (q/(1+q^2), "in no channel"); the half-argument matcher
        # fired on the CONTROL. DELIBERATE could not help -- the label is in a
        # docstring and a branch guard, not the name.
        ("a function returning BOTH C and D is a dispatcher, not a defect",
         _returns_convention_d(ast.parse(
             "def z_of(q, conv):\n"
             "    if conv == 'C': return mp.sqrt(q) / (1 + q)\n"
             "    if conv == 'D': return q ** 3 / (q ** 2 + 1)\n"
             "    return q / (1 + q ** 2)\n").body[0])),
        ("a function returning only C is NOT a dispatcher",
         not _returns_convention_d(ast.parse(
             "def z_mp(d):\n    return 1 / (mp.sqrt(q) + mp.sqrt(qi))\n").body[0])),
        # Blind spelling #17 (bean `qou-1jny`): the D arm written as a CALL to
        # the canonical parameter rather than re-spelled inline. Resolution is
        # by SHAPE at the definition -- the two negatives below are what keep
        # this from degenerating into a name whitelist, which this corpus has
        # already been burned by (a `markov_z` that was privately convention C).
        ("a dispatcher whose D arm is a CALL resolved to a local D def",
         _returns_convention_d(ast.parse(_D_CALL_SRC).body[1],
                               ast.parse(_D_CALL_SRC), "t.py")),
        ("a call resolving to a convention-C def is NOT a dispatcher",
         not _returns_convention_d(
             ast.parse(_C_CALL_SRC).body[1], ast.parse(_C_CALL_SRC), "t.py")),
        ("an UNRESOLVABLE callee is NOT a dispatcher",
         not _returns_convention_d(
             ast.parse(_UNRESOLVED_SRC).body[0], ast.parse(_UNRESOLVED_SRC), "t.py")),
        ("the real he4 z_of is now recognised as a dispatcher",
         _returns_convention_d(
             next(n for n in ast.walk(ast.parse(pathlib.Path(
                 "computations/probes/he4_body_order_shortfall_location_probe.py"
             ).read_text()))
                 if isinstance(n, ast.FunctionDef) and n.name == "z_of"),
             ast.parse(pathlib.Path(
                 "computations/probes/he4_body_order_shortfall_location_probe.py"
             ).read_text()),
             "computations/probes/he4_body_order_shortfall_location_probe.py")),
        ("a file defining z the convention-D way is recognised as D",
         _defines_convention_d("z = q0 ** 3 / (q0 ** 2 + 1)", "z")),
        ("the reversed-denominator spelling is recognised as D",
         _defines_convention_d("z = q ** 3 / (1 + q ** 2)", "z")),
        ("a convention-C definition is NOT mistaken for D",
         not _defines_convention_d("z = 1 / (q ** 0.5 + q ** (-0.5))", "z")),
        ("a mere comment mentioning D does not count as a definition",
         not _defines_convention_d("# convention D: q**3/(q**2+1)\nz = 0.4993", "z")),
    ]
    # ------------------------------------------------------------------
    # The DELIBERATE name classifier (bean `qou-4bq3`). Until 2026-08-25 this
    # was `re.compile(r"(_c\b|_C\b|C_|_c_|zc$|z_c)", re.I)`, and `re.I` folded
    # the `C_` alternative into `c_`, so it matched ordinary identifiers.
    # Measured over every identifier in `computations/`, `qou-mass/` and
    # `tools/`: 1112 distinct names / 5316 occurrences matched ONLY through
    # that collision, including `c_k` (128 uses), `__doc__` (96),
    # `exec_module`, `cyclotomic_poly`, `MAGIC_NUMBERS` and `basic_edges`.
    #
    # These fixtures are the regression lock. EVERY entry in the MUST-NOT half
    # matched the old pattern, so this block fails against it -- a guard that
    # cannot fail on its own known positive is worth nothing.
    checks += list(selftest_rows())

    # The two ends of the classifier's own reasoning, pinned separately from
    # the name list so a future narrowing cannot quietly drop either:
    checks += [
        # Bare `C` is a Wedderburn block label (`A, C, D = 1.0, 1.0, 1.0`) and
        # the multiplicative Jucys-Murphy Casimir `C = sum_k L_k` -- 598 uses
        # across 162 files. The old regex did not match it; nor may this one.
        ("a bare `C` is a block label / Casimir, not a convention",
         not is_deliberate_c_name("C")),
        # The trailing camelCase widening was MEASURED at ~45 % precision (22
        # genuine against 26 false of 50 candidate names) and REJECTED. If a
        # later change adopts it, this fixture fails and the docstring in
        # `scripts/lib/convention_c_names.py` has to be re-argued first.
        ("the ~45 %-precision camelCase widening stays rejected",
         not any(map(is_deliberate_c_name,
                     ("detC", "okC", "aC", "coefsC", "CShR4", "SL2C")))),
        # The kind tag is what lets a B3 verdict name its basis.
        ("a z-anchored name reports the strongest basis",
         deliberate_c_kind("z_c") == "z_C"),
        ("a plain `_C_` token is reported as the weaker basis",
         deliberate_c_kind("pin_C") == "_C_"),
    ]

    # ------------------------------------------------------------------
    # Blind spelling #15 -- `z = sqrt(q)/(q+1)` (bean `qou-l7j1`). The SAME
    # NUMBER as `1/(sqrt q + 1/sqrt q)`, 0.4993203342, and no matcher here saw
    # it: no unit numerator for `is_c_form`, and the numerator is not the
    # denominator's square root for `is_c_form_halfarg`. Three live instances,
    # one of them (`mirror_split_milnor_one_third_probe.py`) also hiding its
    # own `q0 ** 1.5` bond weights behind the miss.
    #
    # The rejects are the precision: the base must be TIED, or this widens into
    # every quotient with a square root on top.
    _direct = [
        ("mp.sqrt(q0) / (q0 + 1)", "q0"),
        ("sqrt(q) / (1 + q)", "q"),
        ("q ** 0.5 / (q + 1)", "q"),
        ("q0 ** mp.mpf('0.5') / (q0 + 1)", "q0"),
        ("float(mp.sqrt(Q) / (Q + 1))", "Q"),          # inside a numeric cast
        ("mp.sqrt(q) / (q ** 2 + 1)", None),           # not q+1 -- a different number
        ("mp.sqrt(q) / (q + 2)", None),                # not q+1
        ("mp.sqrt(q) / (p + 1)", None),                # base NOT tied
        ("q ** 3 / (q ** 2 + 1)", None),               # convention D
        ("mp.sqrt(q ** 4 + q ** 2 + 1) / (q + 1)", None),  # sqrt of a polynomial
    ]
    for src, want in _direct:
        got = is_c_form_direct(ast.parse(src, mode="eval").body)
        verb = f"flags (base {want})" if want else "rejects"
        checks.append((f"direct spelling {verb}: {src}", got == want))

    checks += [
        # `scan` must actually consult the new matcher, not merely define it.
        ("`scan` reports a direct-spelling z (the whole point of #15)",
         _scan_src_count("z = mp.sqrt(q0) / (q0 + 1)\n") == 1),
        ("`scan` still ignores a direct-spelling D",
         _scan_src_count("z = q0 ** 3 / (q0 ** 2 + 1)\n") == 0),
        # The second-tier bucket. A file wholly on C used to be skipped by
        # `scan_closed_forms` on the reasoning that `scan` would report it --
        # which failed exactly when `scan` could not see it.
        ("a C file's closed forms are collected as SECOND TIER, not actionable",
         _cf_pending("z = mp.sqrt(q0) / (q0 + 1)\n"
                     "W2 = (q0 ** 1.5 + q0 + 1) / d\n") == (0, 1)),
        ("a D file's closed forms stay in the ACTIONABLE tier",
         _cf_pending("z = q0 ** 3 / (q0 ** 2 + 1)\n"
                     "W2 = (q0 ** 1.5 + q0 + 1) / d\n") == (1, 0)),
        ("a file on neither convention is still not scanned at all",
         _cf_pending("W2 = (q0 ** 1.5 + q0 + 1) / d\n") == (0, 0)),
        # Per-bond energies are Wedderburn weights by another name. Measured at
        # 3/3 corpus-wide before adding; `f_pp`/`f_pn`/`f_nn` only, not any
        # `f_xx`, so an unrelated two-letter f-name is still left alone.
        ("a per-bond weight with a half-power is a trace/weight binding",
         _cf("f_nn = (q ** 1.5 - q ** 3 + 1) / (q * (q + 1))\n") == 1),
        ("`bond` in the name is enough",
         _cf("eps_bond = mp.sqrt(q)\n") == 1),
        ("an unrelated two-letter f-name is NOT a bond weight",
         _cf("f_ab = mp.sqrt(q)\n") == 0),
    ]
    for name, ok in checks:
        print(f"  {'ok  ' if ok else 'FAIL'}  reexport: {name}")
        bad += not ok

    total = len(should_match) + len(should_not) + len(half) + len(checks)
    print(f"selftest: {total - bad}/{total}"
          + ("" if bad else " — matcher accepts every corpus spelling and rejects convention D."))
    return bad


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true", help="print every site")
    ap.add_argument("--json", metavar="OUT")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return 1 if selftest() else 0

    blocked_files = {r.get("file", "") for r in
                     __import__("json").loads(
                         pathlib.Path("docs/coordination/trace-convention-registry.json")
                         .read_text()).get("blocked_migrations", [])}
    declared_files = declared_c_files(pathlib.Path("."))
    rederivation_files = rederivation_blocked_files(pathlib.Path("."))
    rows = list(scan(blocked_files=blocked_files,
                     declared_files=set(declared_files),
                     rederivation_files=set(rederivation_files)))
    live = [r for r in rows if not r[5]]
    deliberate = [r for r in rows if r[5]]

    buckets = Counter(r[4] for r in live)
    files = defaultdict(set)
    for r in live:
        files[r[4]].add(r[0])

    print("convention-C Markov-parameter definitions in live Python (AST-verified)\n")
    for k, v in buckets.most_common():
        print(f"  {v:4d} sites / {len(files[k]):3d} files   {k}")
    print(f"\n  {len(deliberate):4d} sites               deliberately C-named — labelled comparisons, not defects")

    # Only a site with a live registry row is excused. "unexplained"
    # pyhecke sites count as actionable -- that is the whole point of
    # deriving the label from the registry instead of the path.
    # Excused: a live registry row, or a directory whose own README declares
    # itself out of production. tools/sage-examples is NOT excused -- nothing
    # declares it dead, and an example teaching convention C is arguably worse
    # than a producer using it, because examples get copied.
    _EXCUSED = ("BLOCKED on C by design", "DEPRECATED for production")
    actionable = sum(v for k, v in buckets.items()
                     if not any(e in k for e in _EXCUSED))
    print(f"\n  ACTIONABLE (excludes blocked-by-design): {actionable} sites")

    # A file `scan()` reports as still on C is passed in, so its closed forms
    # are collected too -- into the SECOND-TIER bucket below, never the count.
    # Without this a file whose `z` used an unmatched spelling was invisible to
    # both halves of the audit at once (bean `qou-l7j1`).
    closed_all = scan_closed_forms(c_files={r[0] for r in live})
    closed = [c for c in closed_all if not c[3]]
    pending = [c for c in closed_all if c[3]]
    if closed:
        print(f"\n  C-SPECIALISED CLOSED FORMS: {len(closed)} trace/weight binding(s) in "
              f"convention-D files still carry a half-integer power of q.")
        print("  Migrating z is not migrating the file: h*z+1 and (q*z+1)/(q^2+1) are")
        print("  rational under D, so a square root in one is z_C showing through.")
        cleared = closed_form_measured_clear(pathlib.Path("."))
        for path, line, what, _ in closed:
            sym = what.split(" <- ")[0].strip()
            mark = cleared.get((path, sym))
            print(f"    {path}:{line}   {what}")
            if mark:
                print(f"        [{mark}] — registry `closed_form_measured_clear`. "
                      f"Still listed on purpose; re-verify by RUNNING it, not by reading it.")
    if pending:
        print(f"\n  SECOND TIER — {len(pending)} closed form(s) in files whose z is STILL C "
              f"(listed above).")
        print("  NOT in the actionable count: the z is the defect. These are the work the")
        print("  z migration does NOT finish — re-derive them, do not substitute z_D.")
        for path, line, what, _ in pending:
            print(f"    {path}:{line}   {what}")

    leaks = scan_reexports(repo=pathlib.Path("."))
    if leaks:
        direct = [l for l in leaks if l[4] == "direct"]
        hops = [l for l in leaks if l[4] != "direct"]
        print(f"\n  BLOCKED-SYMBOL LEAKS: {len(direct)} module(s) re-export a registry-blocked "
              f"convention-C symbol; {len(hops)} further consumer(s) import it from them.")
        print("  The registry exempts a symbol INSIDE its module. Nothing kept it there.")
        for path, line, sym, asname, how, reason, bean in direct:
            print(f"    {path}:{line}   {sym}  ->  {asname}   [{bean or 'no bean'}]")
        if args.list:
            for path, line, sym, asname, how, _, _ in hops:
                print(f"      {how:16s} {path}:{line}   {sym} -> {asname}")
        elif hops:
            print(f"    (--list to see the {len(hops)} downstream consumers)")

    if args.list:
        print()
        for path, line, nm, src, bucket, _ in sorted(live):
            print(f"  {path}:{line}\n      {nm} = {src[:90]}")

    if args.json:
        pathlib.Path(args.json).write_text(json.dumps([
            {"path": p, "line": l, "target": nm, "source": s,
             "bucket": b, "deliberate": d}
            for p, l, nm, s, b, d in rows
        ], indent=2))
        print(f"\n  json -> {args.json}")

    return 1 if actionable else 0


if __name__ == "__main__":
    sys.exit(main())
