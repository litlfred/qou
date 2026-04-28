**Remark (affine-chart origin of $i$ and $q$).**
Both categorical coordinates of [$\mathbb{P}(V)$](#def:projective-line-object)
arise from a single piece of data — the **transition between two
affine charts** — but in two distinct regimes of the deformation
family.  The Reeb chart of [contact affine chart](#def:contact-affine-chart)
is one of two natural affine charts; the other is the antipodal chart
swapped by the polar involution.  Writing $z$ for the affine
coordinate on $U_0$ and $w$ for the antipodal chart $U_1$, the
transition on $U_0 \cap U_1$ is

$$
  z \cdot w  =  \kappa,
$$

with the *categorical coordinate* $\kappa$ recording the chart-glue
data.

**Quantum case: $\kappa = q^{-1}$.**  For
$\mathbb{P}_q(V) = G_q/T_q$ ([quantum gauge group](#def:quantum-gauge-group))
the fibre-functor image $\mathcal{O}_q(\mathbb{P}^1)$ has generators
$x, y$ satisfying the quantum-plane relation $yx = q\,xy$.  The
two affine charts are

$$
  z  =  y x^{-1}\;\text{on}\; U_0, \qquad
  w  =  x y^{-1}\;\text{on}\; U_1,
$$

and the chart-transition coefficient is

$$
  z\,w  =  y x^{-1} \cdot x y^{-1}  =  q^{-1},
$$

so $q$ is *literally the chart-transition coefficient* on
$\mathbb{P}_q(V)$, in agreement with the eigenvalue extraction of
[braiding-eigenvalue-extraction](#prop:braiding-eigenvalue-extraction)
under the convention
[$q := \lambda_+$](#rem:braiding-unit-circle-convention).

**Commutative case: $\kappa = 1$ collapses, $i$ from chart-swap.**  At
$q = 1$ ([commutative QOU](#def:commutative-qou)) the chart-transition
$z w = 1$ becomes the classical inversion, and the categorical
coordinate degenerates: $\kappa - \kappa^{-1} = 0$.  The chart-swap
involution

$$
  \iota \colon  z  \longmapsto  z^{-1}, \qquad \iota^2 = \mathrm{id},
$$

generates a $\mathbb{Z}_2$ in $\mathrm{Aut}(\mathbb{P}(V))$.  Its
linearisation on $T_p\mathbb{P}(V)$ at any fixed point ($z = \pm 1$)
acts by $-1$.  Recovering a continuous categorical coordinate requires
a *square root of $\iota$*: a one-parameter family
$\rho_\varTheta\colon z \mapsto e^{i\varTheta} z$ with $\rho_\pi = \iota$
and $\rho_{\pi/2}$ the *quarter-turn between the two charts*.  The
quarter-turn generator is

$$
  \rho_{\pi/2}  =  i \cdot \mathrm{id}_V \in \mathrm{End}_{R[i]}(V),
$$

and this is the categorical coordinate $i = \sqrt{\lambda_-}$.  The
square root resides in $R[i]$ rather than $R$ for exactly the same
reason that $z w = q^{-1}$ does not collapse to $z w = 1$ in the
quantum case: a non-trivial chart-transition is the carrier of the
categorical coordinate.

**Same construction, two regimes.**

| Object | Chart transition | Categorical coordinate |
|--------|------------------|-----------------------|
| $\mathbb{P}_q(V)$ | $z\,w = q^{-1}$ (continuous deformation) | $q \in \mathrm{End}_R(\mathbf{1})$ |
| $\mathbb{P}(V)$ at $q=1$ | $z\,w = 1$, $\iota: z \mapsto z^{-1}$ ($\mathbb{Z}_2$) | $i = \sqrt{\iota|_{T_p}} \in \mathrm{End}_{R[i]}(\mathbf{1})$ |
| $\mathbb{P}(V)$ over $R[i]$ | $z\,w = 1$, $\rho_\varTheta: z \mapsto e^{i\varTheta} z$ ($\mathrm{U}(1)$) | $i$ as quarter-turn generator |

The hierarchy of the categorical-coordinate group is therefore an
expansion of chart-transition automorphisms,

$$
  \underbrace{\mathbb{Z}_2}_{\iota,\;\text{chart-swap}}
  \;\hookrightarrow\;
  \underbrace{\mathbb{Z}_4}_{\iota,\;\pm i}
  \;\hookrightarrow\;
  \underbrace{\mathrm{U}(1)}_{\rho_\varTheta,\;\text{rotation}}
  \;\hookrightarrow\;
  \underbrace{\mathrm{U}_q(1)}_{q\text{-deformation}},
$$

with each inclusion adding one more layer of chart-transition
automorphism.

**Choice up to sign.**  The two square roots $\pm i$ of $\iota$
correspond to the two ways of orienting the quarter-turn;
$\mathbb{P}(V)$ determines the unordered pair $\{+i, -i\}$ but not
the element.  The Galois action $\mathrm{Gal}(R[i]/R) = \mathbb{Z}_2$
exchanging $\pm i$ is the same $\mathbb{Z}_2$ as the braiding
orientation choice $c_{V,V} \leftrightarrow c_{V,V}^{-1}$ of
[i as braiding orientation](#rem:i-as-braiding-orientation): the
sign ambiguity in the chart-transition square root *is* the
arrow-of-time choice.
