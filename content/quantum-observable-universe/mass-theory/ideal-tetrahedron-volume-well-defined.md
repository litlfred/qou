## A shape parameter is a choice; the volume must not be

An ideal tetrahedron is recorded by a single complex number $z$ in the upper half plane. But that number is not intrinsic to the tetrahedron: it is read off a chosen edge. The other two edges give

$$
  z' = \frac{1}{1 - z}, \qquad z'' = 1 - \frac{1}{z},
$$

and these three edge parameters satisfy $z\,z'\,z'' = -1$. Relabelling the tetrahedron cycles them.

So before any volume can be attributed to *the tetrahedron*, the quantity assigned to $z$ must be shown to survive that relabelling. Otherwise it is a property of the bookkeeping.

**Theorem.**
*For every $z$ with $\mathrm{Im}\, z > 0$, the volume of the relabelled tetrahedron equals the volume of the original:*

$$
  D\!\left(\frac{1}{1-z}\right) \;=\; D(z).
$$

The mechanism is immediate once the volume is written in Lobachevsky form. Relabelling cycles the three dihedral angles — $\theta_1 \mapsto \theta_2 \mapsto \theta_3 \mapsto \theta_1$ — and the volume is the *symmetric* sum $\Lambda(\theta_1) + \Lambda(\theta_2) + \Lambda(\theta_3)$, so the three terms are merely permuted. Nothing analytic is involved; the content is entirely in the fact that the angle assignment cycles.

## Why a definitional layer was the missing piece

The interesting point is what this makes possible rather than what it says.

Before it, the sentence $\mathrm{Vol}(5_2) = 3\,D(y_1)$ was not a false Lean proposition — it was not a *statable* one. Mathlib has no hyperbolic $3$-manifolds, and the only objects named "volume" in this corpus were decimal literals and a placeholder that returns zero identically. An equation written against those cannot be proved; it can only be false or vacuous. That is a sharper failure than "unproved", and it is easy to miss, because a vacuous statement compiles.

What the definitional layer supplies is the subject of the sentence: an ideal tetrahedron with a shape, its volume in both the Lobachevsky and dilogarithm forms (proved equal), an ideal triangulation as $n$ tetrahedra, its volume as the sum, the edge parameters with their product relation, and the gluing equations in both product and angle form. The theorem above is the well-definedness that makes the first of these legitimate.

With it, a statement like "the volume of this triangulation is $3\,D(y_1)$" becomes a theorem about a defined object rather than a sentence with no subject.

## What is still not defined — and this is the load-bearing caveat

**The volume of a topological $3$-manifold.** Nothing here connects an ideal triangulation to a knot complement. The definitional layer defines the volume *of a triangulation*, which is a sum over shapes that the definition itself supplies. It does not define, and does not compute, the hyperbolic volume of $5_2$.

That connection is Thurston's hyperbolisation together with Mostow rigidity — the latter being what makes the volume a topological invariant rather than a property of a chosen triangulation — and it requires a theory of hyperbolic $3$-manifolds that neither Mathlib nor this corpus has. The gap is not narrowed by anything above; it is only made visible, by giving the two sides of it distinct names.

## Scope

The mathematics is not new: ideal tetrahedra, their shape parameters and the relabelling action are Thurston's, and the volume formula is Milnor's, in the shape-field setting of Neumann and Zagier. What the corpus contributes is the formalisation, and the discipline of separating "the volume of a triangulation" — defined and computable — from "the volume of a knot complement" — neither.

No volume conjecture is touched.
