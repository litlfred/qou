import snappy
import snappy.ptolemy
import sys

knots = ["T(2,3)", "T(2,5)", "T(2,7)", "T(2,9)", "T(3,4)", "T(3,5)", "T(5,2)"]

for k in knots:
    print(f"Knot: {k}")
    try:
        L = snappy.Link(k)
        M = L.exterior()
        polys = snappy.ptolemy.ptolemy_variety(M, 2, 'all')
        print(f"  Found {len(polys)} Ptolemy varieties")
        for p in polys:
            print("  Variety:", p)
            # Find solutions and their complex volumes
            try:
                solutions = p.compute_solutions()
                for sol in solutions:
                    print("    Sol Vol:", sol.volume(), "CS:", sol.chern_simons())
            except Exception as e:
                print("    Failed to compute solutions:", e)
    except Exception as e:
        print("  Error:", e)
