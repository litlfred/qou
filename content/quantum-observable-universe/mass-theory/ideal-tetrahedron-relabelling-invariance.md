## Relabelling an ideal tetrahedron

A shape parameter records a tetrahedron *together with a choice of which pair of opposite edges is called first*. The map

$$
  z \;\longmapsto\; \frac{1}{1-z}
$$

changes that choice without changing the tetrahedron. Any volume formula written in terms of $z$ must therefore be invariant under it, and if it is not, the formula is measuring the labelling rather than the geometry.

**Proposition.**
*Relabelling cyclically permutes the three dihedral angles, and the volume is unchanged:*

$$
  \operatorname{vol}\Bigl(\tfrac{1}{1-z}\Bigr) \;=\; \operatorname{vol}(z) .
$$

The mechanism is that $\Lambda(\theta_1) + \Lambda(\theta_2) + \Lambda(\theta_3)$ is symmetric under cycling its arguments, together with the two identities

$$
  \frac{1}{\,1 - \frac{1}{1-z}\,} = 1 - \frac{1}{z},
  \qquad
  1 - \frac{1}{\;\frac{1}{1-z}\;} = z ,
$$

which say that the second edge parameter of the relabelled tetrahedron is the third of the original, and the third is the first.

## Where this is load-bearing

It is what makes the $5_2$ volume expression a theorem rather than a coincidence. SnapPy's triangulation of $5_2$ has shapes $(y_1,\; 1/(1-y_1),\; y_1)$ — the middle tetrahedron carries the **second edge parameter** of $y_1$, not $y_1$ itself. An earlier model in this corpus took all three to be $y_1$ and obtained the right total for a reason it did not state. With relabelling invariance the total $3\,D(y_1)$ follows from the actual shapes, and the earlier agreement is explained rather than relied upon.

## The law of sines

The same structure supplies the metric relation

$$
  \lVert z \rVert \;=\; \frac{\sin\theta_2}{\sin\theta_3} ,
$$

the ideal-tetrahedron law of sines, which is the identity that makes the radial argument in Kummer's identity work: it is exactly the statement that a certain derivative along the ray vanishes.
