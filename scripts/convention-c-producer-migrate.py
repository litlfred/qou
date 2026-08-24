#!/usr/bin/env python3
"""Rewrite convention-C Markov-parameter definitions to convention D.

Companion to `convention-c-producer-audit.py`, which *finds* the sites. This one
rewrites them, and is deliberately conservative: it only touches a site when it
can recover the base symbol `q` with certainty, and reports everything else for
a human instead of guessing.

## The rewrite

    1/(X**0.5 + Y**0.5)   ->   q**3/(q**2 + 1)          [convention D]

where `q` is the recovered base. Recognised denominator shapes, with the base in
brackets:

    q0**0.5 + qi0**0.5                 [q0]   named inverse
    q0**0.5 + q0**(-0.5)               [q0]   same symbol, negated exponent
    mp.sqrt(Q0) + 1/mp.sqrt(Q0)        [Q0]   any sqrt callable
    sp.sqrt(q) + 1/sp.sqrt(q)          [q]
    mp.sqrt(q0) + mp.sqrt(qi)          [q0]   both sides sqrt of named pair
    q ** mpmath.mpf('0.5') + qi ** ...  [q]   mpf exponents

**Unrecoverable, and therefore skipped:** `sqrt_q + 1/sqrt_q`. Here the AST only
sees a symbol already holding a square root, and the base `q` is not present in
the expression. Rewriting it would mean guessing that `sqrt_q == sqrt(q)` for
some `q` in scope. Reported, not touched.

## Why the D form is spelled `q**3/(q**2 + 1)`

Numerically neutral: it uses only `**`, `*`, `/`, `+`, so it evaluates correctly
under `float`, `mpmath.mpf`, `sympy`, and `numpy` alike — which matters because
these 100+ sites span all four. The C forms had to call into `mp.sqrt` / `sp.sqrt`
/ `np.sqrt`; the D form calls nothing, which is the same "D leaves Q(q)" fact
that removed the base-field hypotheses in qou-hms1.

Integer `1` rather than `1.0` in the denominator: under sympy that keeps the
expression exact, and under float/mpf it promotes anyway.

## Usage

    python3 scripts/convention-c-producer-migrate.py --dry-run     # default
    python3 scripts/convention-c-producer-migrate.py --apply
    python3 scripts/convention-c-producer-migrate.py --apply --only computations
    python3 scripts/convention-c-producer-migrate.py --selftest

Never rewrites deliberately C-named targets (`z_C`, `z_c`, ...) or anything under
`tools/pyhecke/` (registry `blocked_migrations`), matching the audit's rules.
"""

from __future__ import annotations

import argparse
import ast
import pathlib
import re
import sys

DELIBERATE = re.compile(r"(_c\b|_C\b|C_|_c_|zc$|z_c)", re.I)
SKIP_PREFIXES = ("tools/pyhecke/",)


def _strip(node: ast.AST) -> ast.AST:
    """Peel a float() / mpf() / Decimal() wrapper off a base symbol."""
    while (isinstance(node, ast.Call) and node.args
           and isinstance(node.func, (ast.Name, ast.Attribute))):
        fname = node.func.id if isinstance(node.func, ast.Name) else node.func.attr
        if fname not in ("float", "mpf", "Decimal", "Float", "S"):
            break
        node = node.args[0]
    return node


def _sqrt_base(node: ast.AST):
    """If `node` is a square root of something, return that something."""
    node = _strip(node)
    # sqrt(X) / mp.sqrt(X) / sp.sqrt(X) / np.sqrt(X)
    if isinstance(node, ast.Call) and node.args:
        fname = node.func.id if isinstance(node.func, ast.Name) else \
                (node.func.attr if isinstance(node.func, ast.Attribute) else "")
        if fname == "sqrt":
            return _strip(node.args[0])
    # X ** 0.5  (also mpf('0.5'), mpmath.mpf('0.5'))
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Pow):
        e = ast.unparse(node.right).replace(" ", "")
        if e in ("0.5", ".5") or "'0.5'" in e or '"0.5"' in e:
            return _strip(node.left)
    return None


def _inv_sqrt_base(node: ast.AST):
    """If `node` is 1/sqrt(X) or X**(-0.5), return X."""
    node = _strip(node)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
        if isinstance(node.left, ast.Constant) and node.left.value in (1, 1.0):
            return _sqrt_base(node.right)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Pow):
        e = ast.unparse(node.right).replace(" ", "")
        if e in ("-0.5", "(-0.5)", "-.5") or "'-0.5'" in e or '"-0.5"' in e:
            return _strip(node.left)
    return None


def recover_base(value: ast.AST):
    """Return the base-`q` source text for a convention-C expression, or None."""
    if not (isinstance(value, ast.BinOp) and isinstance(value.op, ast.Div)):
        return None
    if not (isinstance(value.left, ast.Constant) and value.left.value in (1, 1.0)):
        return None
    den = value.right
    if not (isinstance(den, ast.BinOp) and isinstance(den.op, ast.Add)):
        return None
    a, b = den.left, den.right

    base = _sqrt_base(a)
    if base is None:
        return None
    base_src = ast.unparse(base)

    # b is 1/sqrt(same) or same**(-0.5)  -> unambiguous
    ib = _inv_sqrt_base(b)
    if ib is not None and ast.unparse(ib) == base_src:
        return base_src

    # b is sqrt(<inverse-named symbol>) -> accept only for a recognised naming
    sb = _sqrt_base(b)
    if sb is not None:
        other = ast.unparse(sb)
        if _is_inverse_name(base_src, other):
            return base_src
    return None


def _is_inverse_name(base: str, other: str) -> bool:
    """Is `other` the conventional name for 1/`base` in this corpus?

    Only the spellings actually present are accepted (`q0`/`qi0`, `Q0`/`QI`,
    `q`/`qi`, `_Q0`/`_QI0`, `Q`/`Q_INV`). A permissive rule here would silently
    rewrite `sqrt(a) + sqrt(b)` for unrelated `a`, `b`.
    """
    b, o = base.lstrip("_"), other.lstrip("_")
    pairs = {("q0", "qi0"), ("q", "qi"), ("Q0", "QI"), ("Q0", "QI0"),
             ("Q", "Q_INV"), ("q0", "qi"), ("Q0", "Q_INV"), ("q_val", "qi_val")}
    if (b, o) in pairs or (b.lower(), o.lower()) in {(x.lower(), y.lower()) for x, y in pairs}:
        return True
    # 1/base spelled inline as a name is not resolvable; reject.
    return False


# ---------------------------------------------------------------------------
# File-level guards.  Both were added after MEASURING that `--apply` did the
# wrong thing; neither is speculative.  See
# `computations/qbeta/qbeta_convention_c_migration_safety_probe.py`.
#
# G1  DELIBERATE C REFERENCE ELSEWHERE IN THE FILE.  The per-site `DELIBERATE`
#     check reads the TARGET NAME only, so it misses a C value bound to a
#     neutral name and then compared against a C reference.  Measured:
#     `qbeta_zcd_classical_coincidence_probe.py:213` binds `markovZ_prime`
#     (not C-named) purely to assert `markovZ_prime - z_C(q) == 0`.  Rewriting
#     it took that probe from 8/8 exit 0 to FAILED 1/8 exit 1, printing the
#     self-refuting line "1/(sqrt q + 1/sqrt q) = q**3/(q**2 + 1) = z_C".
#
# G2  THE VALUE FEEDS THE LADDER PHASE `alpha = (z - 1) * h / 2`.  Substituting
#     z_D there is the one move the corpus PROVES is not a migration
#     (`QOU.QBeta.decayLadder_zC_threeRow_ne_zero`, sorry-free): the ladder must
#     be RE-DERIVED, not re-evaluated.  Measured, and this is the dangerous
#     one because nothing fails: `qbeta_h_frame_rungs_probe.py:73` still exits
#     0 with all 3 assertions passing, while silently moving 14 mathematical
#     fields of a COMMITTED witness — including `h^3` from `-sqrt(3)/64` to
#     `1/16 - sqrt(3)/64` (a sign change), and the h^6 rung from purely
#     rational to irrational, contradicting that probe's own headline finding.

# G3  THE SITE IS A BAR IMAGE, AND BAR-SYMMETRY IS C-SPECIFIC.  Measured:
#       bar(z_C) = z_C           (ratio 1)      -- bar-symmetric
#       bar(z_D) = 1/(q^3 + q)   (ratio q^-4)   -- NOT bar-symmetric
#     So a line like
#         z_bar = 1/(sqrt(qi) + sqrt(q))   # = z (bar-symmetric)
#     is not a spelling of z that needs updating: it is the BAR IMAGE, and
#     under C it happens to coincide with z.  Substituting z_D there writes
#     `z_bar = z_D`, which is WRONG under D -- the bar image is q^-4 * z_D.
#     Neither G1 (no C-named symbol) nor G2 (no ladder phase) catches it.
#
#     STATUS, stated exactly, because I first claimed more than is true: the
#     motivating site `convergence_safe_vhat_tower.py:198` is in the AUDIT's
#     actionable list, but this migrator would NOT have rewritten it -- the
#     prefilter requires the value to start `1/(` and that line reads
#     `mp.mpf(1) / (...)`, so it never reaches any guard. G3 is therefore
#     PRE-EMPTIVE, not a fix for a live path: it exists so that widening the
#     prefilter (an obvious future improvement) cannot turn a bar image into
#     wrong mathematics. The hazard for a HUMAN working the audit's actionable
#     list is live today.
#     Converting such a site is a MATHS decision (what is the bar image under
#     D?), not a substitution, so it is handed to a human.

BAR_SITE = re.compile(r"(^|_)bar(_|$)|\bbar\s*\(|bar-symmetric|bar symmetric",
                      re.I)


def _file_has_c_reference(tree: ast.AST) -> bool:
    """G1: does anything in this file mention a deliberately C-named symbol?"""
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Attribute):
            nm = node.attr
        if nm and DELIBERATE.search(nm):
            return True
    return False


def _ladder_phase_targets(tree: ast.AST) -> set:
    """G2: names `N` used as `(N - 1) * <anything> / 2` — the ladder phase."""
    hits = set()
    for node in ast.walk(tree):
        # match  X / 2  where X is a Mult
        if not (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)):
            continue
        if not (isinstance(node.right, ast.Constant) and node.right.value == 2):
            continue
        mult = node.left
        if not (isinstance(mult, ast.BinOp) and isinstance(mult.op, ast.Mult)):
            continue
        for side in (mult.left, mult.right):
            inner = side
            while isinstance(inner, ast.BinOp) and isinstance(inner.op, ast.Mult):
                inner = inner.left
            if (isinstance(inner, ast.BinOp) and isinstance(inner.op, ast.Sub)
                    and isinstance(inner.left, ast.Name)
                    and isinstance(inner.right, ast.Constant)
                    and inner.right.value == 1):
                hits.add(inner.left.id)
    return hits


def migrate_file(path: pathlib.Path, apply: bool):
    """Return (rewritten, skipped) lists of (lineno, target, old, new_or_reason)."""
    try:
        src = path.read_text()
        tree = ast.parse(src)
    except (SyntaxError, UnicodeDecodeError, OSError):
        return [], []

    edits, skipped = [], []
    file_has_c_ref = _file_has_c_reference(tree)
    phase_targets = _ladder_phase_targets(tree)
    for n in ast.walk(tree):
        if not isinstance(n, (ast.Assign, ast.AnnAssign)):
            continue
        targets = n.targets if isinstance(n, ast.Assign) else [n.target]
        names = [t.id for t in targets if isinstance(t, ast.Name)]
        if not any("z" in nm.lower() for nm in names):
            continue
        if n.value is None:
            continue
        old_src = ast.unparse(n.value)
        # cheap pre-filter identical to the audit's shape test
        den_src = "".join(old_src.split())
        if not den_src.startswith(("1/(", "1.0/(")):
            continue
        if not ("0.5" in den_src or "sqrt" in den_src.lower()):
            continue
        if "**3" in den_src:
            continue
        nm = names[0]
        if DELIBERATE.search(nm):
            skipped.append((n.lineno, nm, old_src, "deliberately C-named"))
            continue
        # G3: bar images -- see the note above BAR_SITE.
        line_txt = ""
        try:
            line_txt = src.splitlines()[n.lineno - 1]
        except Exception:
            pass
        if BAR_SITE.search(nm) or BAR_SITE.search(line_txt):
            skipped.append((n.lineno, nm, old_src,
                            "G3: bar image — bar-symmetry is C-specific "
                            "(bar(z_D) = q^-4·z_D); substitution here is wrong"))
            continue
        if nm in phase_targets:
            skipped.append((n.lineno, nm, old_src,
                            "G2: feeds the ladder phase (z-1)*h/2 — a z-swap "
                            "here is NOT a migration; re-derivation required"))
            continue
        if file_has_c_ref:
            skipped.append((n.lineno, nm, old_src,
                            "G1: file also references a deliberately C-named "
                            "symbol — likely a C-vs-D comparison; needs a human"))
            continue
        base = recover_base(n.value)
        if base is None:
            skipped.append((n.lineno, nm, old_src, "base q not recoverable"))
            continue
        new_src = f"{base}**3 / ({base}**2 + 1)"
        edits.append((n.lineno, nm, old_src, new_src))

    if apply and edits:
        lines = src.split("\n")
        for lineno, nm, old_src, new_src in edits:
            i = lineno - 1
            # Replace on the physical line only when the old expression appears
            # verbatim; ast.unparse normalises spacing, so fall back to a
            # regex on the assignment's right-hand side.
            line = lines[i]
            if old_src in line:
                lines[i] = line.replace(old_src, new_src)
            else:
                m = re.match(r"^(\s*" + re.escape(nm) + r"\s*=\s*)(.*)$", line)
                if m and m.group(2).strip():
                    lines[i] = m.group(1) + new_src
                else:
                    continue
        path.write_text("\n".join(lines))
    return edits, skipped


def selftest() -> int:
    cases = [
        ("z = 1.0 / (q0**0.5 + qi0**0.5)",                 "q0"),
        ("z = 1.0 / (q0 ** 0.5 + q0 ** (-0.5))",           "q0"),
        ("z = 1.0 / (Q0 ** 0.5 + QI ** 0.5)",              "Q0"),
        ("z = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))",        "Q0"),
        ("z = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))",          "q"),
        ("z = 1.0 / (np.sqrt(q) + 1.0 / np.sqrt(q))",      "q"),
        ("z = 1 / (mp.sqrt(q0) + mp.sqrt(qi))",            "q0"),
        ("z = 1 / (q ** mpmath.mpf('0.5') + qi ** mpmath.mpf('0.5'))", "q"),
        ("z = 1.0 / (float(Q0) ** 0.5 + float(Q0) ** (-0.5))", "Q0"),
        ("z = 1 / (sqrt_q + 1 / sqrt_q)",                  None),   # unrecoverable
        ("z = 1 / (mp.sqrt(a) + mp.sqrt(b))",              None),   # unrelated pair
    ]
    bad = 0
    for src, want in cases:
        node = ast.parse(src).body[0].value
        got = recover_base(node)
        ok = (got == want)
        bad += not ok
        label = f"base={got!r}" if got else "skipped"
        print(f"  {'ok  ' if ok else 'FAIL'}  {label:<14} {src}")
    print(f"selftest: {len(cases)-bad}/{len(cases)}"
          + ("" if bad else " — recovers every recoverable base, refuses the rest."))
    return bad


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", default=None, help="restrict to a path prefix")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return 1 if selftest() else 0

    apply = args.apply and not args.dry_run
    roots = [args.only] if args.only else ["computations", "qou-mass", "tools"]

    n_edit = n_skip = n_files = 0
    skips = []
    for r in roots:
        base = pathlib.Path(r)
        if not base.exists():
            continue
        for p in sorted(base.rglob("*.py")):
            sp_ = str(p)
            if "_deprecated" in sp_ or sp_.startswith(SKIP_PREFIXES):
                continue
            edits, skipped = migrate_file(p, apply)
            if edits:
                n_files += 1
                n_edit += len(edits)
                if not args.quiet:
                    for lineno, nm, old, new in edits:
                        print(f"  {sp_}:{lineno}\n      - {nm} = {old}\n      + {nm} = {new}")
            for s in skipped:
                skips.append((sp_, *s))
            n_skip += len(skipped)

    print(f"\n{'APPLIED' if apply else 'DRY RUN'}: {n_edit} site(s) in {n_files} file(s)")
    if skips:
        print(f"\nSKIPPED ({len(skips)}) — need a human:")
        for path, lineno, nm, old, why in skips:
            print(f"  {path}:{lineno}  [{why}]  {nm} = {old[:70]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
