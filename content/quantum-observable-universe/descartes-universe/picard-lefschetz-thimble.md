Let $F(z, \mathbf{c}) = \mathbf{c}^3 + (4z+1)\mathbf{c}^2 + (6z^2+3z+1)\mathbf{c} + (4z^3+3z^2+2z+1)$ denote the color-tube cubic, and let $\lambda_{\mathrm{SW}}^{(k)}$ denote the Seiberg--Witten differential at vertical degree $k$ on the exceptional divisor $\mathcal{S}_c$ of Bring's surface.

We define the Seiberg--Witten action as the antiderivative

$$
S(z) = \int^z \lambda_{\mathrm{SW}}^{(1)}(z')\, dz'
$$

where $\lambda_{\mathrm{SW}}^{(1)} = dc/dz = -(\partial F/\partial z)/(\partial F/\partial c)$ is the prolonged SW differential obtained by implicit differentiation of the color-tube cubic. The critical points of $S$ are the values $z_c \in \mathbb{C}$ where the color-tube discriminant vanishes:

$$
\Delta(z_c) = 0, \qquad \Delta(z) = 18abcd - 4b^3d + b^2c^2 - 4ac^3 - 27a^2d^2
$$

with $a=1$, $b=4z+1$, $c=6z^2+3z+1$, $d=4z^3+3z^2+2z+1$. At these points, two color sheets merge and $\partial F/\partial \mathbf{c} = 0$ for a repeated root, producing a pole in $\lambda_{\mathrm{SW}}^{(1)}$.

The discriminant polynomial $\Delta(z)$ has degree 6 with no real roots. Its six complex roots come in three conjugate pairs; the pair closest to the physical spacetime ratio $z_0 = \sqrt{q_0} - 1/\sqrt{q_0}$ is

$$
z_c^{\pm} \approx 0.106 \pm 0.937\,i.
$$

For each critical point $z_c$, the Picard--Lefschetz thimble $\mathcal{J}_{z_c}$ is the steepest-:refterm[descent]{#descent} contour of $\operatorname{Re}(S)$ emanating from $z_c$:

$$
\mathcal{J}_{z_c} = \bigl\{ z(t) \in \mathbb{C} \;\big|\; \tfrac{dz}{dt} = -\overline{\nabla S(z)},\; z(0) = z_c,\; \operatorname{Im}(S(z(t))) = \operatorname{Im}(S(z_c)) \bigr\}.
$$

The Hessian at each critical point determines the initial thimble direction:

$$
H(z_c) = \frac{\partial^2 S}{\partial z^2}\bigg|_{z=z_c}.
$$

The thimble $\mathcal{J}_{z_c}$ departs from $z_c$ along the direction $e^{i\varTheta}$ where $\varTheta = -\tfrac{1}{2}\arg H(z_c)$, and the anti-thimble $\mathcal{K}_{z_c}$ departs along $e^{i(\varTheta + \pi/2)}$.

We decompose the original real-axis integration contour $\gamma \subset \mathbb{R}$ into thimbles via:

$$
\gamma = \sum_\sigma n_\sigma \, \mathcal{J}_\sigma, \qquad n_\sigma = \langle \mathcal{K}_\sigma, \gamma \rangle \in \mathbb{Z}
$$

where $n_\sigma$ are the intersection numbers of the anti-thimbles $\mathcal{K}_\sigma$ with $\gamma$.

## Categorical license: PL is the archimedean realisation of non-abelian Stokes

The Picard–Lefschetz thimble decomposition above is an
intrinsically archimedean construction: thimbles are objects in
$\mathbb{C}$ and the steepest-:refterm[descent]{#descent} ODE requires a complex
metric.  The categorical license to use PL on the archimedean side
of the fibre functor $\tau \colon R \hookrightarrow \mathbb{C}$ is
provided by the non-abelian Stokes theorem of \cite{yekutieli2015}:
the categorical surface integral
([Yekutieli–Stokes remark](#rem\:yekutieli-stokes),
[topological mass holonomy](#prop\:topological-mass-formula))
collapses, after applying $\tau$, to a finite sum of point residues
at the discriminant locus — exactly the thimble decomposition above.
The full bridging argument is recorded in
([PL ↔ Yekutieli Stokes](#rem\:pl-yekutieli-stokes)).  See also
([SW-period thimble equivalence](#prop\:sw-period-thimble-equivalence))
for the four-way correspondence GB filtration $\equiv$ jet order
$\equiv$ PL degree under $\tau$.
