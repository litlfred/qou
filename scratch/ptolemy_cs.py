import snappy
import snappy.ptolemy

knots = ["T(2,3)", "T(2,5)", "T(2,7)", "T(2,9)", "T(3,4)", "T(3,5)", "T(5,2)"]

for k in knots:
    M = snappy.Manifold(k)
    print(f"Knot: {k}")
    try:
        from snappy.ptolemy.ptolemyObstructionClass import PtolemyObstructionClass
        # For torus knots, since they aren't hyperbolic, computing representations might be tricky.
        # But let's try ptolemy variety
        polys = snappy.ptolemy.ptolemy_variety(M, 2, 'all')
        for p in polys:
            print("  Variety:", p)
            # representations
            # reps = p.solutions()
            # ...
    except Exception as e:
        print("  Error:", e)
