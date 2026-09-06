"""Sweep the obstruction classes of a manifold's PGL(3,C) Ptolemy variety end to end.

One class per invocation: build the variety, run the FKR 1307.6697 sec 6.1
affine-unit elimination recording every substitution, append the saturation variable,
hand the result to msolve mod p and then over Q, and report the dimension and degree.

WHY THE SATURATION VARIABLE RATHER THAN Singular's sat().  Six runs were lost routing
this through Singular because sat() lives there; Singular std timed out at 39 minutes
on a system msolve settled in four.  Adding u with u*prod(coords) - 1 = 0 imposes
exactly the same condition -- every coordinate invertible -- and needs no sat() at all,
so the whole pipeline goes to msolve.  Engine choice, not mathematics, was the blocker.

WHERE THE NON-ZERO CONDITION GOES, and why it is NOT held through the elimination.
The elimination clears denominators via numer(q.subs(x, -B/A)), which ADDS the locus
{A = 0}.  snappy's t*prod(coords) - 1 = 0 forbids that locus, and an early version fed
it straight into the pool, where step 0 consumed it to solve for t -- leaving nothing
to cut the spurious components out, and every point of the resulting five-dimensional
variety was spurious.

The obvious repair is to PROTECT that equation and never eliminate t.  MEASURED, it
does not work.  t is then never substituted, so the held equation -- already a product
over all 28 coordinates -- is re-expanded against every substitution and grows without
bound: on L6a4 class 1 a single elimination step ran past ten minutes and the loop had
not finished after 35, against a route that settles the same class in minutes.

So do what the class-1 run that actually worked did: let the elimination consume t, and
re-impose the condition AFTERWARDS on the surviving variables as u*prod(rem) - 1 = 0.
That does NOT restore the condition by construction -- it forbids the REMAINING
coordinates from vanishing, not the eliminated ones, whose denominators could still
vanish at a solution.  Soundness comes from the ROUND TRIP instead
(ptolemy_exact_character.py), which lifts a solution and evaluates snappy's ORIGINAL
equations.  Never report a solution from this driver that has not round-tripped.

READING msolve, verified in both directions -- these markers are not interchangeable:

  char p:  [0, [p, n, d, ...]]        zero-dimensional, degree d, RUR follows
           [1, n, -1, []]             POSITIVE DIMENSION -- a refusal, NOT empty
           [-1]                       empty
  char 0:  [0, [1, []]]               no REAL solutions; says nothing about complex ones
           -P 1 -> [0, [0, n, d, ...]] the rational parametrization

A degree over Q that matches the degree mod p is the evidence that p was not a bad
prime.  A mismatch is a finding, not a nuisance.

Usage: ptolemy_class_sweep.py <manifold> <class> [degree-cap] [timeout-seconds] [threads]

BUDGET, measured.  Class 1 settles mod p in 373 s and over Q in 713 s.  Classes 2, 3
and 4 ALL exceeded 900 s mod p -- and class 2 keeps FEWER variables than class 1 (11
against 12), so variable count is not the cost and class 1 is simply the easy one.
Do not size the budget from class 1.
"""
import ast
import json
import pathlib
import re
import subprocess
import sys
import time

import snappy
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
PRIME = 32003


def build_reduced(name, kcls, cap, budget):
    M = snappy.Manifold(name)
    V = M.ptolemy_variety(3, obstruction_class=kcls, eliminate_fixed_ptolemys=True)
    vs = [str(v) for v in V.variables_with_non_zero_condition]
    plain = {str(v) for v in V.variables}
    alleq = [str(e) for e in V.equations_with_non_zero_condition]
    maineq = {str(e) for e in V.equations}
    sym = {v: sp.Symbol('x%d' % i) for i, v in enumerate(vs)}

    def conv(s):
        for v in sorted(vs, key=len, reverse=True):
            s = re.sub(r'\b%s\b' % re.escape(v), str(sym[v]), s)
        return s

    polys, held = [], []
    for e in alleq:
        p = sp.expand(sp.sympify(conv(e).replace('^', '**')))
        (polys if e in maineq else held).append(p)
    print(f"{name} c{kcls}: {len(polys)} main + {len(held)} non-zero-condition eqs,"
          f" {len(vs)} vars", flush=True)

    units = set()
    for p in held:
        for term in sp.Add.make_args(p):
            if not term.is_number:
                units |= term.free_symbols

    def unit_coeff(A):
        if A == 0:
            return False
        if not A.free_symbols:
            return True
        return A.free_symbols <= units and len(sp.Add.make_args(sp.expand(A))) == 1

    t0, elim, log = time.time(), 0, []
    while time.time() - t0 < budget:
        best = None
        for i, p in enumerate(polys):
            for x in sorted(p.free_symbols, key=str):
                if sp.Poly(p, x).degree() != 1:
                    continue
                A = sp.expand(p.coeff(x, 1))
                if not unit_coeff(A):
                    continue
                val = sp.cancel(-sp.expand(p.coeff(x, 0)) / A)
                cand, ok = [], True
                for j, q in enumerate(polys):
                    if j == i:
                        continue
                    r = sp.expand(sp.numer(sp.cancel(sp.together(q.subs(x, val)))))
                    if r != 0 and sp.total_degree(r) > cap:
                        ok = False
                        break
                    if r != 0:
                        cand.append(r)
                if ok:
                    score = (0 if not A.free_symbols else 1,
                             max([sp.total_degree(c) for c in cand] or [0]))
                    if best is None or score < best[0]:
                        best = (score, i, x, cand, val)
            if best and best[0][0] == 0:
                break
        if not best:
            break
        # `held` decides only which coefficients count as units; it is deliberately
        # NOT carried through the elimination -- see the docstring.
        _, i, x, polys, val = best
        log.append((str(x), str(val)))
        elim += 1

    rem = sorted(set().union(*[p.free_symbols for p in polys]) if polys else set(), key=str)
    print(f"  eliminated {elim} -> {len(rem)} vars, {len(polys)} eqs,"
          f" maxdeg {max([sp.total_degree(p) for p in polys] or [0])},"
          f" {time.time() - t0:.1f}s", flush=True)
    # Namespaced: the class-1 artifacts of PR #6815 are tracked and a downstream
    # lift depends on that exact substitution order, so a sweep re-run must not
    # silently replace them.  Calibrate by comparing DEGREES, not by overwriting.
    (HERE / f'{name}_c{kcls}_sweep_subs.json').write_text(json.dumps({
        'vars_original': [str(sym[v]) for v in vs], 'ptolemy_names': vs,
        'subs_order': log, 'remaining': [str(v) for v in rem]}, indent=1))
    return polys, rem


def write_ms(path, polys, rem, char):
    u = sp.Symbol('u')
    sat = u * sp.prod(rem) - 1
    body = ",\n".join(str(p).replace('**', '^') for p in list(polys) + [sat])
    path.write_text(",".join([str(v) for v in rem] + ['u']) + "\n" + str(char) + "\n"
                    + body + "\n")


def run_msolve(inp, out, extra, budget, threads=1):
    cmd = ['msolve', '-t', str(threads), '-f', str(inp), '-o', str(out)] + extra
    t0 = time.time()
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=budget)
    except subprocess.TimeoutExpired:
        return None, f"TIMEOUT after {budget}s", time.time() - t0
    log = (r.stdout or '') + (r.stderr or '')
    if r.returncode != 0:
        return None, f"msolve exit {r.returncode}: {log.strip()[:300]}", time.time() - t0
    try:
        data = ast.literal_eval(out.read_text().strip().rstrip(':'))
    except Exception as exc:
        return None, f"unparsable output: {exc}", time.time() - t0
    return data, log, time.time() - t0


def describe(data):
    """Turn an msolve result into a verdict, per the marker table in the docstring."""
    if data is None:
        return "no result", None
    if data == [-1] or (isinstance(data, list) and data and data[0] == -1):
        return "EMPTY", None
    if data[0] == 1:
        return "POSITIVE DIMENSION (refusal, not empty)", None
    body = data[1]
    if isinstance(body, list) and len(body) == 2 and body[0] == 1 and body[1] == []:
        return "zero-dimensional, no REAL solutions (complex ones not excluded)", None
    try:
        return f"zero-dimensional, degree {body[2]}", body[2]
    except Exception:
        return f"unrecognized shape {str(data)[:120]}", None


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else 'L6a4'
    kcls = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    cap = int(sys.argv[3]) if len(sys.argv) > 3 else 25
    budget = int(sys.argv[4]) if len(sys.argv) > 4 else 1200
    threads = int(sys.argv[5]) if len(sys.argv) > 5 else 1

    polys, rem = build_reduced(name, kcls, cap, budget)
    stem = f'{name}-c{kcls}-sweep'
    res = {"manifold": name, "obstruction_class": kcls, "degree_cap": cap,
           "variables": [str(v) for v in rem] + ['u'], "equations": len(polys) + 1}

    for tag, char, extra in (("modp", PRIME, []), ("charzero", 0, ['-P', '1'])):
        ms = HERE / f'{stem}-{tag}.ms'
        out = HERE / f'{stem}-rur-{tag}.res'
        write_ms(ms, polys, rem, char)
        data, log, secs = run_msolve(ms, out, extra, budget, threads)
        verdict, deg = describe(data)
        res[tag] = {"verdict": verdict, "degree": deg, "seconds": round(secs, 1)}
        print(f"  {tag}: {verdict}   ({secs:.1f}s)", flush=True)
        if data is None:
            print(f"    {log}", flush=True)

    dp, dz = res.get("modp", {}).get("degree"), res.get("charzero", {}).get("degree")
    if dp is not None and dz is not None:
        res["degrees_agree"] = (dp == dz)
        print(f"  degree mod {PRIME} = {dp}, over Q = {dz}: "
              + ("AGREE -- p is not a bad prime" if dp == dz
                 else "DISAGREE -- this is a finding, not a nuisance"), flush=True)

    (HERE / f'{name}-c{kcls}-sweep.json').write_text(json.dumps(res, indent=2) + "\n")
    print(f"  wrote {name}-c{kcls}-sweep.json", flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
