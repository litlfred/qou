#!/usr/bin/env python3
"""Measure the q-integer definitions the duplication audit cannot reach.

Bean qou-b8vx.  `q_integer_duplication_audit.py` classifies a definition by
applying it to a symbolic q -- and gives up on any definition taking `n` ALONE
(`symbolic_signature`: `if len(args) < 2: return None`), because such a
definition reads its q from a MODULE GLOBAL.  That is a large fraction of the
corpus, and its convention was therefore UNMEASURED rather than measured-and-
agreeing.

This audit resolves those globals instead of guessing them.  For each blocked
definition it walks the module's own top-level assignments, evaluates them
symbolically against a single root symbol, binds the result into the
function's namespace, and only then applies the function to n = 2, 3, 5.

WHAT IT REFUSES TO DO.  It never assumes a name's meaning from its spelling.
`h` might be (q-1)/q, q - 1/q, or a loop variable that leaked; binding it by
name would manufacture a classification.  A name whose assignment this script
cannot evaluate leaves the definition UNRESOLVED and it is reported as such.
An unresolved definition is not evidence of agreement -- that conflation is
the whole reason this bean exists.

Exact sympy throughout; no float anywhere (NO-FLOAT64 binds audits too).
"""
from __future__ import annotations

import ast
import builtins
import pathlib
import sys
from collections import Counter

import sympy as sp

BUILTIN = set(dir(builtins))
Q = sp.Symbol('q', positive=True)
NAMEPAT = ('q_int', 'qint', 'qb', 'q_bracket', 'qbracket', 'q_num', 'bracket')

# Names that are LIBRARIES, not quantities -- bound to shims, never to q.
LIBS = {'mp', 'mpmath', 'sp', 'sympy', 'np', 'numpy', 'math'}
# Sources that MEAN "the substrate modulus".  A root assignment, not a guess:
# each is the corpus's own published entry point for q0.
ROOT_SOURCES = ('Q_50_DIGIT_STR', 'q_at', 'Q_MUON_50_DIGIT_STR', 'q_muon_at',
                'q_muon_frozen_at', 'Q_STR')

# Modules AGENTS.md designates as the canonical q0 accessors.  Inside one of
# these -- and ONLY inside one -- a subscript keyed "q" is the substrate
# modulus: `q_parameter` builds its anchor block as Q_MP = mpf(_d["q"]) from
# the anchor witness.  Scoping it to these modules is the difference between
# citing the corpus's own designation and inferring meaning from a spelling,
# which this audit otherwise refuses to do.
ANCHOR_MODULES = ('q_parameter', 'constants')
_ANCHOR_KEYS = ('"q"', "'q'")


class _Shim:
    """mpmath/numpy stand-in that keeps everything exact and symbolic."""
    def __getattr__(self, name):
        if name in ('mpf', 'mpmathify', 'convert'):
            return lambda x, *a, **k: sp.nsimplify(sp.sympify(x), rational=True)
        if name == 'sqrt':
            return sp.sqrt
        if name == 'mp':
            return self
        if name in ('dps', 'prec'):
            return 50
        return getattr(sp, name, lambda *a, **k: sp.nan)

    def __setattr__(self, name, value):
        pass


def top_level_assignments(tree: ast.Module) -> dict[str, ast.expr]:
    """Module-scope bindings, INCLUDING those inside a module-level try/if/with.

    `q_parameter` binds the whole anchor block inside a try, so a scan of
    unindented statements alone misses `Q_MP` -- the single most-imported
    modulus name in the corpus -- and reports every definition downstream of it
    as unmeasurable.  A name bound in a module-level `try:` body is a module
    binding; indentation is not scope in Python.
    """
    out: dict[str, ast.expr] = {}

    def walk_block(body):
        for node in body:
            if isinstance(node, ast.Assign):
                for t in node.targets:
                    if isinstance(t, ast.Name):
                        out.setdefault(t.id, node.value)
            elif isinstance(node, (ast.Try, ast.If, ast.With)):
                for attr in ('body', 'orelse', 'finalbody'):
                    walk_block(getattr(node, attr, []) or [])
                for h in getattr(node, 'handlers', []) or []:
                    walk_block(h.body)

    walk_block(tree.body)
    return out


def top_level_imports(tree: ast.Module) -> dict[str, str]:
    """name -> module it is imported FROM, for `from M import name [as alias]`.

    Also walks function bodies: this corpus routinely defers an import into a
    function to dodge a circular import, and `from q_parameter import Q_MP as
    _Q` inside a def is exactly as much a binding as one at module level.
    """
    out: dict[str, str] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            for a in node.names:
                out[a.asname or a.name] = f'{node.module}::{a.name}'
    return out


_MODULE_CACHE: dict[str, tuple[dict, dict] | None] = {}


def _find_module(modname: str) -> pathlib.Path | None:
    """Locate a corpus module by its bare import name.

    The corpus imports flat (`from q_parameter import ...`) because
    `_path_bridge` puts `computations/` on sys.path, so the import name is the
    file stem rather than a package path.
    """
    stem = modname.split('.')[-1]
    for r in (pathlib.Path('computations'), pathlib.Path('tools')):
        for cand in r.rglob(f'{stem}.py'):
            if '_deprecated' not in str(cand):
                return cand
    return None


def module_tables(modname: str):
    if modname in _MODULE_CACHE:
        return _MODULE_CACHE[modname]
    path = _find_module(modname)
    res = None
    if path is not None:
        try:
            t = ast.parse(path.read_text())
            res = (top_level_assignments(t), top_level_imports(t))
        except Exception:
            res = None
    _MODULE_CACHE[modname] = res
    return res


def resolve(name: str, assigns: dict[str, ast.expr], seen: frozenset[str],
            imports: dict[str, str] | None = None, depth: int = 0,
            in_anchor_module: bool = False):
    """Symbolic value of a module global, or None if not determinable.

    Returns (value, why) where why names the route -- 'root' for a name
    assigned from a published q0 entry point, 'derived' for one computed from
    other resolvable names.
    """
    imports = imports or {}
    if name in seen or depth > 6:
        return None, 'import cycle or depth limit'
    if name not in assigns:
        # Not assigned here -- is it IMPORTED?  Resolve it in its own module.
        if name in imports:
            mod, orig = imports[name].split('::')
            tables = module_tables(mod)
            if tables is None:
                return None, f'source module `{mod}` not found'
            a2, i2 = tables
            return resolve(orig, a2, seen | {name}, i2, depth + 1,
                           any(m in mod for m in ANCHOR_MODULES))
        return None, 'no top-level assignment'
    expr = assigns[name]
    src = ast.unparse(expr)
    if any(r in src for r in ROOT_SOURCES):
        return Q, 'root'                      # this name IS the substrate modulus
    if in_anchor_module and any(k in src for k in _ANCHOR_KEYS) and '[' in src:
        return Q, 'root (anchor-module q key)'
    ns: dict[str, object] = {'sp': sp, 'sympy': sp}
    shim = _Shim()
    ns['mp'] = ns['mpmath'] = shim
    ns['mpf'] = lambda x, *a, **k: sp.nsimplify(sp.sympify(x), rational=True)
    for sub in ast.walk(expr):
        if isinstance(sub, ast.Name) and isinstance(sub.ctx, ast.Load):
            if sub.id in ns or sub.id in BUILTIN:
                continue
            v, _ = resolve(sub.id, assigns, seen | {name}, imports, depth,
                           in_anchor_module)
            if v is None:
                return None, f'depends on unresolvable `{sub.id}`'
            ns[sub.id] = v
    try:
        val = eval(compile(ast.Expression(expr), '<g>', 'eval'), ns)  # noqa: S307
        val = sp.sympify(val)
    except Exception as exc:
        return None, f'not evaluable ({type(exc).__name__})'
    if not val.free_symbols & {Q}:
        return None, 'q-independent (a constant, not the modulus)'
    return val, 'derived'


def _sym(n, v): return (v**n - v**-n) / (v - 1/v)
def _cla(n, v): return (v**n - 1) / (v - 1)

FORMS = (('symmetric', _sym), ('classical', _cla),
         ('symmetric_in_sqrt_q', lambda n, v: _sym(n, sp.sqrt(v))),
         ('classical_in_sqrt_q', lambda n, v: _cla(n, sp.sqrt(v))),
         ('symmetric_in_q2', lambda n, v: _sym(n, v**2)))


def classify(sig) -> str:
    """Classify an INDEX-argument definition from its n = 2,3,5 signature."""
    if sig is None:
        return 'UNRESOLVED'
    for label, f in FORMS:
        if all(sp.simplify(s - f(n, Q)) == 0 for n, s in zip((2, 3, 5), sig)):
            return label
    return 'OTHER'


def classify_fixed_n(val, nmax: int = 12) -> str | None:
    """Classify a MODULUS-argument definition: [n]_q at one FIXED n.

    A one-argument definition is not necessarily q0-pinned.  Its argument may
    be the MODULUS, making it a fixed-n bracket -- `def q_int2(q): return
    q + 1/q` is [2]_q, complete and symbolically comparable, with no module
    global involved at all.  Calling it as though the argument were the index
    computes 2 + 1/2 and classifies noise.

    This is the SAME defect the duplication audit's `symbolic_signature`
    already guards against by trying both argument orders; the first version
    of THIS script did not, and reported five such definitions as OTHER.
    """
    if val is None:
        return None
    for label, f in FORMS:
        for n in range(1, nmax + 1):
            try:
                if sp.simplify(val - f(n, Q)) == 0:
                    return f'{label}[n={n}]'
            except Exception:
                continue
    return None


def main() -> int:
    roots = [pathlib.Path('computations'), pathlib.Path('tools')]
    blocked, results = 0, []
    for r in roots:
        for p in sorted(r.rglob('*.py')):
            if '_deprecated' in str(p):
                continue
            try:
                tree = ast.parse(p.read_text())
            except Exception:
                continue
            assigns = top_level_assignments(tree)
            imports = top_level_imports(tree)
            for node in tree.body:
                if not (isinstance(node, ast.FunctionDef)
                        and any(k in node.name.lower() for k in NAMEPAT)):
                    continue
                if len(node.args.args) >= 2:
                    continue                      # the duplication audit reaches these
                blocked += 1
                arg = node.args.args[0].arg if node.args.args else None
                local = {arg} if arg else set()
                for sub in ast.walk(node):
                    if isinstance(sub, ast.Assign):
                        for t in ast.walk(sub.targets[0]):
                            if isinstance(t, ast.Name):
                                local.add(t.id)
                free = {s.id for s in ast.walk(node)
                        if isinstance(s, ast.Name) and isinstance(s.ctx, ast.Load)
                        and s.id not in local and s.id not in BUILTIN}
                ns: dict[str, object] = {}
                shim = _Shim()
                why_fail = None
                for g in sorted(free):
                    if g in LIBS:
                        ns[g] = sp if g in ('sp', 'sympy') else shim
                        continue
                    if g in ('mpf', 'mpmathify'):
                        ns[g] = lambda x, *a, **k: sp.nsimplify(sp.sympify(x), rational=True)
                        continue
                    if g == 'lru_cache':
                        ns[g] = lambda *a, **k: (lambda f: f)
                        continue
                    v, why = resolve(g, assigns, frozenset(), imports)
                    if v is None:
                        why_fail = f'`{g}`: {why}'
                        break
                    ns[g] = v
                # FIRST: is the single argument the MODULUS rather than the
                # index?  Try f(q) symbolically; a fixed-n bracket answers here
                # and needs no globals at all.
                fixed = None
                try:
                    ns_m = dict(ns)
                    body_m = ast.get_source_segment(p.read_text(), node)
                    exec(compile(body_m, '<m>', 'exec'), ns_m)   # noqa: S102
                    fixed = classify_fixed_n(sp.sympify(ns_m[node.name](Q)))
                except Exception:
                    fixed = None
                if fixed:
                    results.append((p, node.name, fixed, None))
                    continue
                sig = None
                if why_fail is None:
                    body = ast.get_source_segment(p.read_text(), node)
                    try:
                        exec(compile(body, '<d>', 'exec'), ns)     # noqa: S102
                        f = ns[node.name]
                        sig = tuple(sp.cancel(sp.together(sp.sympify(f(n))))
                                    for n in (2, 3, 5))
                    except Exception as exc:
                        why_fail, sig = f'call failed ({type(exc).__name__})', None
                results.append((p, node.name, classify(sig), why_fail))

    print('=' * 74)
    print('q-INTEGER GLOBAL-RESOLUTION AUDIT  (bean qou-b8vx)')
    print('=' * 74)
    print(f'\ndefinitions taking n ALONE (blocked for the duplication audit): {blocked}\n')
    tally = Counter(v for _, _, v, _ in results)
    resolved = sum(c for k, c in tally.items() if k != 'UNRESOLVED')
    for k, c in tally.most_common():
        print(f'   {c:>4}  {k}')
    pct = 100.0 * resolved / blocked if blocked else 0.0
    print(f'\n   RESOLVED {resolved}/{blocked} ({pct:.1f}%) — previously 0')
    sq = [(p, n, v) for p, n, v, _ in results if 'sqrt_q' in v or 'q2' in v]
    if sq:
        print('\nSQRT-VARIABLE / q^2 SPELLINGS — symmetric convention at a\n  DIFFERENT ARGUMENT. qou-9nn0 found one of these to be a real defect\n  (the file needed [n]_q and computed [n]_sqrt(q)), so each needs its\n  own check against what its caller expects:')
        for p, n, v in sq:
            print(f'   {p}::{n}  -> {v}')
    cls = [(p, n) for p, n, v, _ in results if v.startswith('classical')]
    if cls:
        print('\nCLASSICAL — newly measured, previously invisible to the'
              ' convention audit (relevant to qou-gl58):')
        for p, n in cls:
            print(f'   {p}::{n}')
    if tally.get('OTHER'):
        print('\nOTHER — resolved but matching no known convention (inspect these):')
        for p, n, v, _ in results:
            if v == 'OTHER':
                print(f'   {p}::{n}')
    fails = Counter(w.split(':')[-1].strip() for _, _, v, w in results
                    if v == 'UNRESOLVED' and w)
    if fails:
        print('\nstill unresolved, by reason:')
        for w, c in fails.most_common(8):
            print(f'   {c:>4}  {w}')
    print('\nAn UNRESOLVED definition is UNMEASURED, not agreeing.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
