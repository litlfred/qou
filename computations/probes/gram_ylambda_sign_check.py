#!/usr/bin/env python3
"""Which y_lambda vanish, and what are their SIGNS, under convention D at n=3?

Written to settle a specific cross-agent question (S2/#5185 vs S1/#5187):
does convention D put a NEGATIVE weight on a Wedderburn block, and is that
the same fact as the Temperley-Lieb radical seen from the trace side?

ANSWER: no, and no. Under D the two surviving weights are both strictly
POSITIVE for q > 1 and the single dead weight is EXACTLY ZERO --

    y_(3)   = (q^4+1)/(q^2+1)^2   > 0
    y_(2,1) = q^2/(q^2+1)^2       > 0        <- two rows; SURVIVES
    y_(1^3) = 0                              <- three rows; the radical

-- which is a positive SEMIdefinite form, exactly what a Temperley-Lieb
trace looks like, and sum(dim^2) over the zero weights is 1 = the measured
corank at n=3 (gram_radical_cellular_revalidation.py).

The relayed claim was that in the instance y = (z, 1/2 - z, z) the weight
1/2 - z_D is negative. That instance satisfies the NORMALISATION h1 only;
it fails h2 and h3, so H_3(q) under convention D does not realise it, and
1/2 - z_D is not y_(2,1). The last block below checks exactly that, so the
refutation is reproducible rather than asserted.

Uses the corpus's own three defining equations (TemperleyLiebTower --
the same hypotheses `conventionD_kills_antisymmetriser` takes, so this
solve reproduces that Lean theorem rather than assuming a variant):
  y3 + 2*y21 + y13                      = 1
  q*y3 + (q - 1/q)*y21 - (1/q)*y13      = z
  q^2*y3 - y21 + (1/q^2)*y13            = z^2
solved symbolically over Q(q) with z = z_D = q^3/(q^2+1), then z = z_C.
"""
import sympy as sp

q = sp.Symbol('q', positive=True)
y3, y21, y13 = sp.symbols('y3 y21 y13')

def solve_for(z, name):
    eqs = [
        sp.Eq(y3 + 2*y21 + y13, 1),
        sp.Eq(q*y3 + (q - 1/q)*y21 - (1/q)*y13, z),
        sp.Eq(q**2*y3 - y21 + (1/q**2)*y13, z**2),
    ]
    sol = sp.solve(eqs, [y3, y21, y13], dict=True)[0]
    print(f"=== {name}:  z = {sp.simplify(z)} ===")
    rows = []
    for lbl, sym, nrows, dim in [("(3)", y3, 1, 1), ("(2,1)", y21, 2, 2), ("(1^3)", y13, 3, 1)]:
        v = sp.simplify(sp.cancel(sp.together(sol[sym])))
        zero = sp.simplify(v) == 0
        # sign for q > 1
        sgn = None
        if not zero:
            vals = [sp.nsimplify(v.subs(q, sp.Rational(r))) for r in
                    (sp.Rational(11,10), sp.Rational(3,2), sp.Rational(2), sp.Rational(5))]
            fl = [float(x) for x in vals]
            if all(x > 0 for x in fl): sgn = "POSITIVE for q>1"
            elif all(x < 0 for x in fl): sgn = "NEGATIVE for q>1"
            else: sgn = f"MIXED {fl}"
        rows.append((lbl, nrows, dim, v, zero, sgn))
        print(f"  y_{lbl:6s} rows={nrows} dim={dim}  = {v}")
        print(f"        identically zero: {zero}    sign: {sgn}")
    # corank prediction from the dead set
    dead = sum(d*d for (_, _, d, _, z0, _) in rows if z0)
    print(f"  --> sum of dim^2 over IDENTICALLY-ZERO weights = {dead}"
          f"   (measured corank at n=3 is 1)")
    print()
    return rows

zD = q**3/(q**2 + 1)
solve_for(zD, "convention D")

# convention C: z = 1/(q^(1/2) + q^(-1/2))
s = sp.sqrt(q)
zC = 1/(s + 1/s)
solve_for(zC, "convention C")

print("=== S1's relayed instance y = (z, 1/2 - z, z): is that the n=3 D weight vector? ===")
sol = sp.solve([
    sp.Eq(y3 + 2*y21 + y13, 1),
    sp.Eq(q*y3 + (q - 1/q)*y21 - (1/q)*y13, zD),
    sp.Eq(q**2*y3 - y21 + (1/q**2)*y13, zD**2),
], [y3, y21, y13], dict=True)[0]
print("  actual y3   =", sp.simplify(sol[y3]))
print("  actual y21  =", sp.simplify(sol[y21]))
print("  actual y13  =", sp.simplify(sol[y13]))
print("  is y3 == z_D ?  ", sp.simplify(sol[y3] - zD) == 0)
print("  is y21 == 1/2 - z_D ?", sp.simplify(sol[y21] - (sp.Rational(1,2) - zD)) == 0)
print("  is y13 == z_D ?  ", sp.simplify(sol[y13] - zD) == 0)


print("=== does the relayed instance satisfy h2/h3 at all? ===")
q = sp.Symbol('q', positive=True)
z = q**3/(q**2 + 1)

y3, y21, y13 = z, sp.Rational(1, 2) - z, z

eqs = {
    "h1  normalisation  y3 + 2 y21 + y13 = 1":
        sp.simplify(y3 + 2*y21 + y13 - 1),
    "h2  tr(sigma)      q y3 + (q-1/q) y21 - (1/q) y13 = z":
        sp.simplify(q*y3 + (q - 1/q)*y21 - (1/q)*y13 - z),
    "h3  tr(sigma sig') q^2 y3 - y21 + (1/q^2) y13 = z^2":
        sp.simplify(q**2*y3 - y21 + (1/q**2)*y13 - z**2),
}
for k, v in eqs.items():
    print(f"  residual of {k}\n      = {v}   -> satisfied: {v == 0}")

print()
print("  y_(2,1) under S1's instance = 1/2 - z_D =",
      sp.simplify(sp.Rational(1,2) - z))
print("  at q=1.11:", float((sp.Rational(1,2) - z).subs(q, sp.Rational(111,100))))
print("  y_(2,1) ACTUALLY (solving h1,h2,h3) = q^2/(q^2+1)^2 ,",
      "at q=1.11:", float((q**2/(q**2+1)**2).subs(q, sp.Rational(111,100))))
print()
print("  2q^3 - q^2 - 1 factorisation check (S1's positivity core):",
      sp.factor(2*q**3 - q**2 - 1))
print("  so z_D > 1/2 for q > 1: ", sp.simplify(z - sp.Rational(1,2)))
