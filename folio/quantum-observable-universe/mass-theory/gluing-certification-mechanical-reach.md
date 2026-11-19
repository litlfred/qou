## Exact algebraic reach of gluing certification

Shape fields identified from a triangulation give the edge and cusp equations a purely algebraic form: with $P$ the minimal polynomial and each shape $z_j = Q_j(\theta)$ an explicit element of $\mathbb{Q}(\theta)$, the verification lives in $\mathbb{Q}[x]/(P)$ and no numerics enter at any step.

Two consequences make the whole thing mechanical.

**Every identity holds at an arbitrary root.** Because the computation is in the quotient ring, each equation holds at *every* root of $P$ rather than merely the geometric one. This removes the root-selection problem entirely — otherwise one would have to prove that a quartic or a degree-14 polynomial has a root in the upper half plane before saying anything at all. Which root is geometric is a separate, numerical question.

**Every proof is a single deterministic step.** Clearing denominators turns $\prod z^{a} (z')^{b} (z'')^{c} = 1$ into the polynomial identity

$$
  \prod_j z_j^{a_j}\,\prod_j (z_j-1)^{c_j}
  \;=\;
  \prod_j (1-z_j)^{b_j}\,\prod_j z_j^{c_j},
$$

whose difference is divisible by $P$ *exactly*. The cofactor comes from exact polynomial division and the proof is one linear-combination step; non-vanishing of each $z_j$ and $1-z_j$ comes from a Bézout certificate. Nothing is guessed, and a wrong candidate fails at generation rather than producing an unprovable claim.

## Cusp equations were expected to be harder and are not

Cusp equations carry **negative** exponents, which suggests they need each parameter's inverse as an explicit polynomial plus integer-power bookkeeping threaded through every statement. They do not. Every edge parameter is a unit, so

$$
  \prod \mathrm{param}^{e} = 1
  \quad\Longleftrightarrow\quad
  \prod_{e>0} \mathrm{param}^{e} \;=\; \prod_{e<0} \mathrm{param}^{-e},
$$

and both sides now carry **natural** exponents. Clearing denominators reduces the whole thing to the edge case, and no integer-power machinery appears anywhere.

## Two predicted ceilings, neither of which exists

The obvious worries about scaling this up are that the certificates grow with the field degree, and that the product over tetrahedra outruns the available finite-product lemmas. Both were expected to bite; both were measured, and neither did.

**Degree.** The certificates do grow — cofactor degree roughly quadruples and emitted size grows fivefold from degree 4 to degree 9. But the manifold with a degree-14 shape field, whose single largest certificate is over thirty thousand characters, verifies in about two minutes. The naive extrapolation overshoots because **cost tracks the number of ring-normalisation calls far more than the size of any one of them.** Wide-but-few is cheap.

**Tetrahedron count.** The finite-product lemmas available off the shelf stop at eight, which reads like a hard limit at nine tetrahedra. It is a limit on the *named lemmas* rather than on the argument: the successor form iterates unaided and unfolds the product at any count. A fourteen-tetrahedron triangulation certifies by the same single step as a two-tetrahedron one.

Net reach: shape-field degrees $2$ through $14$, triangulations of $2$ through $14$ tetrahedra, with each manifold's identities assembled into a certificate that the triangulation satisfies its gluing system — not merely a pile of separate equations.

## Completeness and geometric properties outside gluing certification

The identities hold at an **arbitrary root**, so flat shapes are permitted throughout and **hyperbolicity is not established anywhere** — that needs $\mathrm{Im} z > 0$, which is a genuinely separate condition and is exactly the gap the trefoil exhibits: its flat shapes satisfy the edge equations exactly.

Nothing here says any of these triangulations is a triangulation *of* a knot complement. That is Thurston hyperbolisation together with Mostow rigidity, and it needs a theory of hyperbolic 3-manifolds that this development does not have.

**None of the underlying mathematics is new.** What is contributed is the exact, mechanically checked form, and the measurement of how far it reaches before anything breaks.
