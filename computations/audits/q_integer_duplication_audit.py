#!/usr/bin/env python3
"""Do the corpus's many local [n]_q definitions agree — compared SYMBOLICALLY?

Bean qou-c041. A prior grep found ~192 files defining their own quantum integer
against 21 importing `qou_substrate.constants.q_int`, and read that as
gratuitous duplication. This audit tests that reading, and finds something
different: a convention split.

METHOD. AST-based, and symbolic in q — never an evaluation at q0. Each
candidate function is parsed, normalised through `ast.unparse` (comments,
spacing and local naming drop out), then applied to a SYMPY SYMBOL `q` at
several n and simplified. Two definitions are the same iff they simplify to the
same rational function of q, which is exact and q-independent.

Why not evaluate at q0: two genuinely different functions can agree at a point,
and a numeric comparison would silently merge them. It would also make the
answer depend on a pinned anchor, which a question about *definitions* should
not. (This audit was first written numerically and corrected on owner
instruction — "make those symbolic, not q_0".)

NO-FLOAT64: nothing here is evaluated in floating point at all. The comparison
is over exact symbolic expressions.
"""
from __future__ import annotations

import ast
import pathlib
import sys
from collections import defaultdict

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[2]
NAMES = {"q_int", "qint", "q_integer", "qb", "qbracket", "bracket", "q_num"}
SKIP = ("_deprecated", ".lake", "node_modules", "/tests/")

Q = sp.Symbol("q", positive=True)

#: Conventions we can name.  Keyed by the simplified [n]_q for n = 2, 3, 5.
def _sig(expr_fn):
    return tuple(sp.simplify(sp.together(expr_fn(n))) for n in (2, 3, 5))

SYMMETRIC = _sig(lambda n: (Q**n - Q**-n) / (Q - 1 / Q))     # (q^n - q^-n)/(q - q^-1)
CLASSICAL = _sig(lambda n: (Q**n - 1) / (Q - 1))             # (q^n - 1)/(q - 1), Gaussian
SQRTNORM  = _sig(lambda n: (Q**n - 1) / (sp.sqrt(Q) - 1 / sp.sqrt(Q)))
SYMM_Q2   = _sig(lambda n: (Q**(2 * n) - Q**(-2 * n)) / (Q**2 - Q**-2))


class _ShimModule:
    """Stand in for mpmath so a definition written against it stays symbolic."""
    mpf = staticmethod(lambda x: sp.nsimplify(x, rational=True)
                       if not isinstance(x, sp.Basic) else x)
    sqrt = staticmethod(sp.sqrt)
    exp = staticmethod(sp.exp)
    log = staticmethod(sp.log)
    cosh = staticmethod(sp.cosh)
    sinh = staticmethod(sp.sinh)
    pi = sp.pi
    mp = type("mp", (), {"dps": 40})()


def candidates():
    out = []
    for base in ("computations", "tools"):
        for p in (ROOT / base).rglob("*.py"):
            s = str(p)
            if any(k in s for k in SKIP):
                continue
            try:
                tree = ast.parse(p.read_text(errors="ignore"))
            except SyntaxError:
                continue
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name in NAMES:
                    try:
                        body = ast.unparse(node.body)
                    except Exception:
                        continue
                    out.append((p.relative_to(ROOT), node.name,
                                tuple(a.arg for a in node.args.args), body))
    return out


def symbolic_signature(body: str, args: tuple[str, ...]):
    """Apply the definition to a symbolic q. None if q0-pinned or opaque.

    Argument order is DETERMINED, not guessed: both orders are tried and the
    one whose n=2 result actually depends on q is kept.  An earlier version
    guessed from the parameter name (`args[0] in ("n","m","k")`) and got
    `computations/h2s_chirality_residue_s3_holonomy.py` backwards, producing
    `4**q / 2**q` — a signature with q in the exponent, which no q-integer has.
    """
    if len(args) < 2:
        return None                       # takes n only: pinned to a module global
    src = f"def _f({', '.join(args)}):\n" + "\n".join(
        "    " + ln for ln in body.splitlines())
    shim = _ShimModule()
    ns = {"mp": shim, "mpmath": shim, "sp": sp, "sympy": sp}
    try:
        exec(compile(src, "<q>", "exec"), ns)          # noqa: S102 — audits own tree
    except Exception:
        return None
    f = ns["_f"]

    def attempt(n_first):
        out = []
        for n in (2, 3, 5):
            try:
                v = f(n, Q) if n_first else f(Q, n)
                e = sp.cancel(sp.together(sp.nsimplify(sp.sympify(v),
                                                       rational=True)))
            except Exception:
                return None
            if e.has(Q**Q) or any(a.exp.has(Q) for a in e.atoms(sp.Pow)
                                  if a.exp.free_symbols):
                return None               # q in an exponent: wrong arg order
            out.append(e)
        return tuple(out)

    return attempt(True) or attempt(False)


def same(a, b) -> bool:
    """Symbolic EQUALITY, not identity of representation.

    `q + 1/q` and `1.0*q + 1.0/q` are the same function; an earlier version
    clustered on the printed form and reported them as two.
    """
    try:
        return all(sp.simplify(x - y) == 0 for x, y in zip(a, b))
    except Exception:
        return False


def main() -> int:
    cands = candidates()
    print(f"candidate [n]_q definitions: {len(cands)} in "
          f"{len({c[0] for c in cands})} files\n")

    by_arity = defaultdict(int)
    for _, _, args, _ in cands:
        by_arity[len(args)] += 1
    print("by arity:")
    for k in sorted(by_arity):
        note = ("q0-PINNED (takes n only; q comes from a module global)"
                if k < 2 else "q-parametric")
        print(f"  {k} arg(s): {by_arity[k]:4d}   <- {note}")

    reps, opaque, floats = [], 0, []
    for p, name, args, body in cands:
        sig = symbolic_signature(body, args)
        if sig is None:
            opaque += 1
            continue
        if any(isinstance(a, sp.Float) for s in sig for a in s.atoms(sp.Float)):
            floats.append((str(p), name))
        for r in reps:
            if same(r[0], sig):
                r[1].append((str(p), name))
                break
        else:
            reps.append((sig, [(str(p), name)]))
    groups = {tuple(sig): mem for sig, mem in reps}

    print(f"\ncompared symbolically : {sum(len(v) for v in groups.values())}")
    print(f"not symbolically evaluable : {opaque}"
          "   (q0-pinned, or needing module globals)")
    print(f"\nDISTINCT SYMBOLIC FORMS: {len(groups)}")
    for i, (sig, members) in enumerate(
            sorted(groups.items(), key=lambda e: -len(e[1])), 1):
        # Label by symbolic EQUALITY, not by identity of representation.
        # An earlier version used `sig == SYMMETRIC`, which failed on
        # (q**2+1)/q vs q + 1/q — the same function, canonicalised differently —
        # and mislabelled 126 definitions UNRECOGNISED. Same defect as the
        # clustering bug, one line over.
        label = ("SYMMETRIC  (q^n-q^-n)/(q-q^-1)" if same(sig, SYMMETRIC) else
                 "CLASSICAL  (q^n-1)/(q-1)" if same(sig, CLASSICAL) else
                 "SQRT-NORMALISED  (q^n-1)/(q^(1/2)-q^(-1/2))"
                 if same(sig, SQRTNORM) else
                 "SYMMETRIC in q^2" if same(sig, SYMM_Q2) else "UNRECOGNISED")
        print(f"\n  form {i}: {len(members):4d} definition(s)   {label}")
        print(f"     [2]_q = {sig[0]}")
        if sig != SYMMETRIC:
            for f, n in sorted(set(members))[:8]:
                print(f"       {f}  ({n})")
            if len(set(members)) > 8:
                print(f"       ... and {len(set(members)) - 8} more")

    if floats:
        print(f"\nNO-FLOAT64: {len(floats)} definition(s) carry a float literal "
              "in the q-integer itself")
        for f, n in sorted(set(floats))[:10]:
            print(f"    {f}  ({n})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
