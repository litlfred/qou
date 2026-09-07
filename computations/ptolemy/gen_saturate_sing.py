#!/usr/bin/env python3
"""Emit the Singular saturation script for a Ptolemy class -- snappy's OWN route.

WHY THIS AND NOT THE FKR-REDUCED SYSTEM.  snappy computes Ptolemy varieties by handing
Magma the FULL system and saturating: Groebner basis over Q, then Saturation(I, x_i) for
every variable in turn with the basis recomputed each time, then dimension, then a change
of order and primary decomposition (snappy/ptolemy/magma/default.magma_template).

The corpus instead runs a custom FKR affine-unit elimination first.  That is much smaller
-- 11 variables against 27 -- and it is why class 1 settles in minutes.  But it clears
denominators via numer(q.subs(x,-B/A)), which ADDS the locus {A=0}, so its answers are
provisional until a point round-trips, and that is what forced the #6815 retraction.

snappy's route has the opposite trade: bigger system, but saturation removes the
degenerate components BY CONSTRUCTION, so a dimension it reports needs no round trip.
Singular is Sage's Groebner engine, so running this here is what `compute_solutions`
would do under Sage, without Sage installed.

Usage: gen_saturate_sing.py <manifold> <class> [char]   (char 0 = over Q, as snappy does)
"""
import sys
import warnings
warnings.filterwarnings('ignore')
import snappy

name = sys.argv[1] if len(sys.argv) > 1 else 'L6a4'
kcls = int(sys.argv[2]) if len(sys.argv) > 2 else 2
char = sys.argv[3] if len(sys.argv) > 3 else '0'

M = snappy.Manifold(name)
V = M.ptolemy_variety(3, obstruction_class=kcls, eliminate_fixed_ptolemys=True)
vs = [str(v) for v in V.variables]
eqs = [str(e) for e in V.equations]

out = f'{name}-c{kcls}-saturate-full.sing'
with open(out, 'w') as f:
    f.write('LIB "elim.lib";\n')
    f.write(f'ring r = {char}, ({",".join(vs)}), dp;\n')
    f.write('ideal I = ' + ',\n '.join(eqs) + ';\n')
    f.write('int t0 = timer;\n')
    # snappy's template saturates by EVERY variable, recomputing the basis each time.
    for v in vs:
        f.write(f'I = sat(I, {v})[1];\n')
    f.write('ideal G = std(I);\n')
    f.write('printf("saturated by all %s vars in %s sec | GB size %s | dim %s",\n'
            f'        {len(vs)}, timer-t0, size(G), dim(G));\n')
    f.write('if (size(G)==1 && G[1]==1) {\n')
    f.write(f'  printf("EMPTY after saturation -> class {kcls} has NO genuine points");\n')
    f.write('} else {\n')
    f.write(f'  printf("NON-EMPTY after saturation -> genuine points EXIST in class {kcls}");\n')
    f.write('}\n')
    f.write('quit;\n')
print(f'{out}: {len(vs)} vars, {len(eqs)} equations, char {char}')
