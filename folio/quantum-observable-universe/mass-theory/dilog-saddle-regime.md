The quasi-classical potential governing the Kashaev asymptotics of the
figure-eight knot $4_1$ is the imaginary part of the dilogarithm on
the unit circle,

$$
  V(\theta) \;=\; \mathrm{Im}\,\mathrm{Li}_2(e^{i\theta}),
$$

the Clausen function $\mathrm{Cl}_2(\theta)$
([Clausen function $\mathrm{Cl}_2$](#rem:clausen-function-mathlib-filler)).
Its critical points solve

$$
  \frac{d}{d\theta}\,\mathrm{Im}\,\mathrm{Li}_2(e^{i\theta})
  \;=\;
  -\log\bigl|2\sin(\theta/2)\bigr|
  \;=\; 0
  \quad\Longrightarrow\quad
  \bigl|2\sin(\theta/2)\bigr| = 1
  \quad\Longrightarrow\quad
  \theta = \frac{\pi}{3}.
$$

Evaluating the potential at this root yields the hyperbolic volume of
the regular ideal tetrahedron,

$$
  V(\pi/3) \;=\; \mathrm{Cl}_2(\pi/3) \;\approx\; 1.01494,
$$

and since the $4_1$ complement is glued from two such tetrahedra,

$$
  \mathrm{Vol}(4_1) \;=\; 2\,\mathrm{Cl}_2(\pi/3) \;\approx\; 2.02988.
$$

This saddle computation is the concrete $4_1$ instance of the
[Kashaev volume conjecture](#conj:kashaev-volume-conjecture)
asymptotics. Blocks that invoke the dilog saddle regime — the
continuum $c_3$ geometry discussion, the
[$\Phi_q$/AJ machinery identification](#prop:phi-q-aj-machinery-identification),
and the
[$q_0$ Stokes-region identification](#conj:q-zero-stokes-region-identification)
— reference this derivation rather than repeating it.
