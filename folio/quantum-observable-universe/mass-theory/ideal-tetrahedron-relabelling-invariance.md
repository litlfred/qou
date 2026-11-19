## Relabelling an ideal tetrahedron

A shape parameter records a tetrahedron *together with a choice of which pair of opposite edges is called first*. The map

$$
  z \;\longmapsto\; \frac{1}{1-z}
$$

changes that choice without changing the tetrahedron. Any volume formula written in terms of $z$ must therefore be invariant under it, and if it is not, the formula is measuring the labelling rather than the geometry.

**Proposition.**
*Relabelling cyclically permutes the three dihedral angles, and the volume is unchanged:*

$$
  \mathrm{vol}\Bigl(\tfrac{1}{1-z}\Bigr) \;=\; \mathrm{vol}(z) .
$$

The mechanism is that $\Lambda(\theta_1) + \Lambda(\theta_2) + \Lambda(\theta_3)$ is symmetric under cycling its arguments, together with the two identities

$$
  \frac{1}{\,1 - \frac{1}{1-z}\,} = 1 - \frac{1}{z},
  \qquad
  1 - \frac{1}{\;\frac{1}{1-z}\;} = z ,
$$

which say that the second edge parameter of the relabelled tetrahedron is the third of the original, and the third is the first.

## Downstream applications of relabelling invariance

This invariance makes the $5_2$ volume identity a theorem rather than a numerical coincidence. The standard three-tetrahedron ideal triangulation of the $5_2$ complement carries shape parameters $(y_1,\; 1/(1-y_1),\; y_1)$: the middle tetrahedron carries the **second edge parameter** $1/(1-y_1)$ rather than $y_1$ itself. By relabelling invariance, $D(1/(1-y_1)) = D(y_1)$, so the total hyperbolic volume $3\,D(y_1)$ follows directly from the true tetrahedral shapes.

## The law of sines

The same structure supplies the metric relation

$$
  \lVert z \rVert \;=\; \frac{\sin\theta_2}{\sin\theta_3} ,
$$

the ideal-tetrahedron law of sines, which is the identity that makes the radial argument in Kummer's identity work: it is exactly the statement that a certain derivative along the ray vanishes.
