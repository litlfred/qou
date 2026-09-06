#!/usr/bin/env python3
"""Read the DIMENSION (and, at dimension 0, the DEGREE) off an msolve -g Groebner basis.

WHY THIS EXISTS.  msolve does two things: a degrevlex Groebner basis, then an FGLM
change-of-order producing the RUR.  For a high-degree ideal the second is routinely
the dominant cost, so a system whose RUR is out of reach may still yield its GB --
and the GB alone answers the question actually being asked of L6a4's obstruction
classes.  The dimension is determined by the staircase of leading monomials, and when
that dimension is 0 the degree is the number of standard monomials.  Neither needs a
parametrisation.

THE TWO FACTS THIS RELIES ON, both verified against msolve output rather than assumed:
  1. msolve -g prints each basis element with its LEADING monomial FIRST.
  2. the order is graded reverse lexicographical (msolve states it in the header, and
     this script REFUSES to proceed if the header says otherwise -- a lex or elimination
     order would make the first-term rule wrong and silently corrupt every answer).

DIMENSION.  For a monomial ideal, the Krull dimension is the largest size of a subset U
of the variables containing NO leading monomial's support -- i.e. LT(I) meets k[U] only
in 0.  Enumerated exactly over all subsets; at 11 variables that is 2048 tests.

DEGREE, at dimension 0 only.  The standard monomials -- those divisible by no leading
monomial -- form a basis of the quotient, and their count is the degree.  Dimension 0
guarantees a pure power of every variable appears among the leading monomials, so the
enumeration is finite and the per-variable bound is that pure power's exponent.
"""
import re
import sys
from itertools import combinations, product


def parse(path):
    txt = open(path).read()
    m = re.search(r'#variable order:\s*(.+)', txt)
    if not m:
        raise SystemExit("no '#variable order' header -- not an msolve -g file")
    varnames = [v.strip() for v in m.group(1).split(',') if v.strip()]
    order = re.search(r'#monomial order:\s*(.+)', txt)
    if not order or 'reverse lexicographical' not in order.group(1):
        raise SystemExit(f"REFUSING: order is {order and order.group(1).strip()!r}, "
                         "not degrevlex -- the leading-term-is-first rule does not hold")
    body = txt[txt.rindex('#---') + 4:]
    body = body[body.index('[') + 1: body.rindex(']')]
    lead = []
    for poly in body.split(','):
        poly = poly.strip()
        if not poly:
            continue
        first = poly.split('+')[0].split('-')[0].strip()   # leading term, with coefficient
        exps = [0] * len(varnames)
        for vp in first.split('*'):
            vp = vp.strip()
            if not vp or vp.isdigit():
                continue                                    # the numeric coefficient
            if '^' in vp:
                v, e = vp.split('^'); exps[varnames.index(v.strip())] = int(e)
            else:
                exps[varnames.index(vp)] = 1
        if any(exps):
            lead.append(tuple(exps))
    return varnames, lead


def dimension(varnames, lead):
    """Largest independent set of variables: one whose span contains no leading monomial."""
    n = len(varnames)
    supports = [{i for i, e in enumerate(m) if e} for m in lead]
    for size in range(n, -1, -1):
        for U in combinations(range(n), size):
            Us = set(U)
            if not any(s <= Us for s in supports):
                return size, [varnames[i] for i in U]
    return 0, []


def degree_dim0(varnames, lead):
    """Count standard monomials.  Valid ONLY at dimension 0."""
    n = len(varnames)
    bound = []
    for i in range(n):
        pure = [m[i] for m in lead if all(e == 0 for j, e in enumerate(m) if j != i) and m[i]]
        if not pure:
            return None                                     # not dimension 0 after all
        bound.append(min(pure))
    count = 0
    for expo in product(*[range(b) for b in bound]):
        if not any(all(expo[i] >= m[i] for i in range(n)) for m in lead):
            count += 1
    return count


def report(path):
    varnames, lead = parse(path)
    d, U = dimension(varnames, lead)
    print(f"{path}: {len(varnames)} vars, {len(lead)} leading monomials")
    print(f"  DIMENSION = {d}" + (f"   (independent set: {', '.join(U)})" if U else ""))
    if d == 0:
        deg = degree_dim0(varnames, lead)
        print(f"  DEGREE    = {deg}" if deg is not None else "  DEGREE    = (pure powers absent)")
    else:
        print("  positive dimensional -- msolve will refuse to parametrise it;"
              " a generic slice by this many hyperplanes cuts it to dimension 0")
    return d


def selftest():
    """Calibrate against ideals whose dimension and degree are known by hand."""
    import subprocess, tempfile, os
    cases = [
        ("x,y",   ["x^2-1", "y^2-1"],          0, 4),   # 1, x, y, xy
        ("x,y",   ["x^2", "x*y", "y^2"],       0, 3),   # 1, x, y
        ("x,y",   ["x*y"],                     1, None),
        ("x,y,z", ["x^2-1", "y^2-1", "z^2-1"], 0, 8),
        ("x,y,z", ["x-1", "y-2", "z-3"],       0, 1),   # a single point
    ]
    ok = True
    with tempfile.TemporaryDirectory() as td:
        for i, (vs, polys, want_d, want_deg) in enumerate(cases):
            src, out = os.path.join(td, f"t{i}.ms"), os.path.join(td, f"t{i}.gb")
            open(src, 'w').write(vs + "\n32003\n" + ",\n".join(polys) + "\n")
            subprocess.run(['msolve', '-t', '1', '-g', '2', '-f', src, '-o', out],
                           capture_output=True, timeout=120)
            varnames, lead = parse(out)
            d, _ = dimension(varnames, lead)
            deg = degree_dim0(varnames, lead) if d == 0 else None
            good = (d == want_d) and (want_deg is None or deg == want_deg)
            ok &= good
            print(f"  [{'ok' if good else 'FAIL'}] <{vs}> {polys}"
                  f" -> dim {d} (want {want_d}), degree {deg} (want {want_deg})")
    print("SELFTEST", "PASSED" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--selftest':
        sys.exit(selftest())
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    report(sys.argv[1])
