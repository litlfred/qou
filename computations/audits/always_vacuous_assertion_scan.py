#!/usr/bin/env python3
"""Assertions whose computed and expected are the SAME expression -- vacuous for
all data, not merely at zero. The compute-side `theorem X : X = X := rfl`.

Finding the hits was the easy half. The useful half is the triage, because
measured on this corpus (238 hits, 3247 producers) **none of them is a false
claim** -- they fall into three shapes with completely different consequences,
and a sweep that "fixed" them uniformly would do damage:

  ASSERT-BACKED  The verification really happened, in bare `assert` statements
                 a few lines up; the add_assertion only RECORDS the outcome.
                 e.g. `borel_propertime_moment_attack_probe.block_a1` integrates
                 s^n e^-s symbolically and `assert val == factorial(n-1)` for
                 every n, then records ("moment_identity_gamma", "0", "0").
                 Sound today. Two problems, neither of them the tautology:
                 the evidence is invisible to any reader of the witness, and
                 `python -O` DELETES assert statements -- under -O the whole
                 verification silently vanishes while the witness still reports
                 passed:true. Latent, not live: nothing in this repo runs -O.

  SELF-REPORT    "probe_completed", "audit_completed", "kernel_ran". A record
                 that the script reached the end. Vacuous, harmless, noise --
                 the witness already carries `computedAt`. Not worth a sweep.

  VERDICT-RECORD The author's CONCLUSION, stated as a passing assertion:
                 "frobenius_dual_refuted_scope_a", computed="1", expected="1".
                 The reasoning is real and lives in `description`/`source`, the
                 numbers live in `add_data`. Nothing was tested. Not false --
                 but it inflates `allPassed` with a proposition no code
                 evaluated, and an audit reading assertion outcomes cannot tell
                 it from a checked one.

The subset worth fixing is flagged HAS-LOCAL: a verdict-record whose enclosing
function already binds a boolean-ish local (`all_match`, `verdict`, `*_ok`).
That is a CANDIDATE, never a verdict -- "a boolean exists in scope" is not
"that boolean is what the assertion meant", and each needs reading. The worked
case is `qbeta_per_block_uniform_rule_verify`, where `all_match` was computed,
passed to add_data, and then NOT asserted; the assertion beside it recorded a
tautology named "..._holds" while the real finding (the rule fails by ~28%)
sat unasserted in `data.finding`.
"""
import argparse
import ast
import re
import subprocess
import sys

sys.path.insert(0, "computations/audits")
from _source_normalise import code_only  # noqa: E402

SELF_REPORT = re.compile(
    r"(completed|_ran$|executed|recorded|emitted|loaded|assembled|present"
    r"|available|attempted|reported|documented|runs$|identified|evaluated"
    r"|compared|extracted|computed$|passed$)", re.I)
BOOLISH = re.compile(r"(all_|_ok$|ok$|holds|match|passed|verdict|survives|success|is_)")


def _name_of(call, kw):
    nm = kw.get("name")
    if isinstance(nm, ast.Constant):
        return str(nm.value)
    if call.args and isinstance(call.args[0], ast.Constant):
        return str(call.args[0].value)
    return "?"


def scan(paths):
    hits = []
    for f in paths:
        try:
            src = open(f, encoding="utf-8").read()
            tree = ast.parse(code_only(src))
        except Exception:
            continue
        funcs = [n for n in ast.walk(tree)
                 if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
        for n in ast.walk(tree):
            if not (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                    and n.func.attr == "add_assertion"):
                continue
            kw = {k.arg: k.value for k in n.keywords if k.arg}
            c, e = kw.get("computed"), kw.get("expected")
            if c is None or e is None:
                continue
            try:
                if ast.dump(c) != ast.dump(e):
                    continue
            except Exception:
                continue

            name = _name_of(n, kw)
            # Innermost enclosing function, or module scope.
            encl = [fn for fn in funcs
                    if fn.lineno <= n.lineno <= (fn.end_lineno or fn.lineno)]
            encl.sort(key=lambda fn: (fn.end_lineno or fn.lineno) - fn.lineno)
            scope = encl[0] if encl else tree

            backed = any(isinstance(x, ast.Assert) for x in ast.walk(scope))
            literal = isinstance(c, ast.Constant)
            locals_ = {t.id for x in ast.walk(scope) if isinstance(x, ast.Assign)
                       for t in x.targets if isinstance(t, ast.Name)}
            boolish = sorted(v for v in locals_ if BOOLISH.search(v))

            if backed:
                shape = "ASSERT-BACKED"
            elif SELF_REPORT.search(name):
                shape = "SELF-REPORT"
            else:
                shape = "VERDICT-RECORD"

            hits.append(dict(file=f, line=n.lineno, expr=ast.unparse(c), name=name,
                             shape=shape, literal=literal,
                             has_local=boolish if shape == "VERDICT-RECORD" else []))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shape", choices=["ASSERT-BACKED", "SELF-REPORT", "VERDICT-RECORD"],
                    help="show only this shape")
    ap.add_argument("--has-local", action="store_true",
                    help="only VERDICT-RECORDs with a boolean-ish local in scope "
                         "(the fixable candidates)")
    args = ap.parse_args()

    files = [p for p in subprocess.run(["git", "ls-files", "computations"],
                                       capture_output=True, text=True).stdout.split()
             if p.endswith(".py") and ("_deprecated" not in p and "fsh-guts" not in p)]
    hits = sorted(scan(files), key=lambda h: (h["file"], h["line"]))

    counts = {}
    for h in hits:
        counts[h["shape"]] = counts.get(h["shape"], 0) + 1
    fixable = [h for h in hits if h["has_local"]]

    print(f"producers scanned: {len(files)}")
    print(f"assertions with IDENTICAL computed and expected: {len(hits)}")
    for s in ("ASSERT-BACKED", "SELF-REPORT", "VERDICT-RECORD"):
        print(f"  {s:<15} {counts.get(s, 0):>4}")
    print(f"  {'of which HAS-LOCAL (fixable candidates)':<15} {len(fixable):>4}")
    print()

    shown = hits
    if args.shape:
        shown = [h for h in shown if h["shape"] == args.shape]
    if args.has_local:
        shown = [h for h in shown if h["has_local"]]

    for h in shown:
        print(f"  [{h['shape']}] {h['file']}:{h['line']}")
        print(f"      computed == expected == {h['expr']}")
        print(f"      named: \"{h['name']}\"")
        if h["has_local"]:
            print(f"      candidate locals in scope: {', '.join(h['has_local'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
