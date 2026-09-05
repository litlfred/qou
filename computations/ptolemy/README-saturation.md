# Saturating an FKR-reduced Ptolemy system

## The defect this exists to prevent

`fkr_affine_unit_elimination.py` substitutes `z = -B/A` and clears denominators with
`numer(q.subs(x, -B/A))`. Clearing multiplies through by a power of `A`, which **adds the
locus `{A = 0}` to the variety**. Points there are not on the Ptolemy variety.

snappy guards against exactly this by appending one equation, `t * prod(coords) - 1 = 0`,
forcing every coordinate invertible. The first version of the reduction fed that equation
into the elimination pool, where step 0 used it to solve for `t` itself
(`t = 1/prod`). The constraint then vanished and nothing cut the spurious loci out.

Measured consequence on L6a4 class 1: the reduced variety looked 5-dimensional of degree
18 over Q, and **all 18** points of a generic 5-fold slice lay on the spurious locus --
lifting them back drove one coordinate to `2.75e+471`. A retraction followed.

## Three fixes, in increasing order of practicality

1. **Hold the condition aside** (`fkr_affine_unit_elimination_saturated.py`): never
   eliminate `t`, never eliminate using that equation, substitute into it and re-append.
   Correct, but it drags a ~26-fold product through every substitution and its degree
   grows fast.
2. **Form `u * prod(factors) - 1` once at the end.** Correct, but with ~27 factors of
   degree up to 15 the single equation reaches degree ~400 -- not usable.
3. **Saturate by each variable** (`L6a4-c1-saturate-by-variables.sing`). *Preferred.*
   Every `A` produced by this reduction is a **monomial in the coordinates**, so `A = 0`
   forces some coordinate to zero. Therefore

       for each variable v:  I = sat(I, v)[1]

   removes every spurious component, using only degree-1 saturations. On L6a4 class 1 all
   four problem denominators (`x1*x10*...*x9`, `x1*x4`, `x2*x4`, `x2*x4*x8`) involve only
   *remaining* variables, so twelve cheap saturations suffice.

## The check that is not optional

`verify_reduction_roundtrip.py`. A reduced system being non-empty proves nothing about the
original: solve reduced, lift through the recorded substitutions, evaluate the ORIGINAL
equations, and require both a vanishing residual and no zero coordinate.

**Matching solution counts on a calibration case does NOT detect this.** 4_1 passed at
every stage under the broken reduction -- 6 solutions, 4 self-dual / 2 complex type,
correct number fields, clean lift -- because its solutions happen to avoid the spurious
locus. A calibration that passes is evidence about the cases it covers, never proof of
soundness. Only the round trip discriminates.

## Measured limits in this container (15 GB RAM)

| system | outcome |
|---|---|
| L6a4 c1 **unreduced** (28 vars, deg 27), Singular `std` mod 32003 | **needs > 10 GB — halts.** Twice reproduced: 9.1 GB at 20 min on the first attempt, 8.87 GB at 19 min then `halt 14` at the 10 GB cap on the second. Growth is accelerating (4.4 GB at 15 min), so a marginally higher cap will not help. |
| L6a4 c1 unreduced, **msolve** mod 32003 | **structurally impossible** — msolve announces `for esz = 33554432, segmentation fault will follow` and exits 139. An internal allocation ceiling, not a `ulimit`; raising memory does nothing. Three reproductions. |
| L6a4 c1–c3 **FKR-reduced + saturated**, Singular `sat` + `std` mod 32003 | 340–530 MB, flat. |

So the reduction is not optional for this manifold in this container -- it is a ~20x memory
reduction on the same question. The defect was never that FKR failed to reduce; it was
that the reduction was unsound. Saturation restores soundness while keeping the tractability.

**Singular halts gracefully at a `ulimit`** (`halt 14`, exit 14) rather than taking the
container down, so capping a speculative run is cheap insurance. msolve does not -- it
segfaults.
