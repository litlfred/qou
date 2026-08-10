## Two Bloch--Wigner functions, and the prohibition between them

The Bloch--Wigner dilogarithm can be built two ways. The *angle-built* form is Milnor's sum of Lobachevsky values over the three dihedral angles of an ideal tetrahedron,

$$
  \Lambda(\theta_1) + \Lambda(\theta_2) + \Lambda(\theta_3),
$$

and is the form in which hyperbolic volume naturally appears. The *dilogarithm-built* form is the classical one,

$$
  \mathrm{Im}\, \mathrm{Li}_2(z) + \log\lVert z\rVert \cdot \arg(1 - z),
$$

and is the form in which the functional equations live.

Until they are known to agree, facts about one may not be transported to the other. The corpus records that prohibition explicitly, and the point of this block is that it is now lifted.

**Theorem.**
*For every $z$ with $\mathrm{Im}\, z > 0$,*

$$
  \Lambda(\theta_1) + \Lambda(\theta_2) + \Lambda(\theta_3)
  \;=\; \mathrm{Im}\, \mathrm{Li}_2(z) + \log\lVert z\rVert \cdot \arg(1 - z).
$$

## The proof needs one variable, not two

Matching the two sides looks like a two-variable problem, since both $\lVert z\rVert$ and $\arg z$ move. Fixing $\varphi = \arg z$ and moving along the ray $r \mapsto r e^{i\varphi}$ collapses it to one.

Along such a ray, $\theta_1 = \varphi$ is constant, so $\Lambda(\theta_1)$ contributes nothing to the derivative. The angle sum $\theta_1 + \theta_2 + \theta_3 = \pi$ then forces $\theta_3$ to move exactly opposite to $\theta_2$, so

$$
  \frac{d}{dr}\bigl(\Lambda(\theta_2) + \Lambda(\theta_3)\bigr)
    \;=\; \bigl(\log(2\sin\theta_3) - \log(2\sin\theta_2)\bigr)\,\theta_2' ,
$$

and the law of sines rewrites that bracket as $-\log r$. On the dilogarithm side the two terms contribute $\theta_2/r$ and $-\theta_2/r - \log r\cdot\theta_2'$, whose sum is again $-\log r \cdot \theta_2'$.

The two sides therefore have the same derivative along every ray, so their difference is constant on $(0, \infty)$; the already-proved unit-circle case at $r = 1$ kills the constant. This is the same "same derivative, pin the constant" shape used throughout this arc, and the law of sines is precisely what makes it available.

## What this does and does not settle about $\mathrm{Vol}(5_2)$

The immediate consequence is an exact dilogarithm expression for the $5_2$ constant. Writing $y_1$ for the root of $X^3 - 2X^2 + 3X - 1$ with positive imaginary part,

$$
  \mathrm{VOL}_{5_2} \;=\; 3\,\bigl(\mathrm{Im}\,\mathrm{Li}_2(y_1) + \log\lVert y_1\rVert\cdot\arg(1 - y_1)\bigr).
$$

**This is a conversion between two expressions for a defined quantity, not a computation of a knot invariant.** $\mathrm{VOL}_{5_2}$ is *defined* in the corpus as $3\,D(y_1)$; the theorem above rewrites that definition in dilogarithm form. It does not prove that the quantity so defined is the hyperbolic volume of the $5_2$ complement. That identification — that a particular triangulation's $\Lambda$-sum is the volume of a particular knot complement — is the geometric step, and it is untouched here.

The distinction matters because the numbers agree. Evaluating gives $3D(y_1) = 2.828122088330783\ldots$, which matches the literature value of $\mathrm{Vol}(5_2)$ to the precision available. That agreement is evidence that the definition was chosen correctly; it is not a proof that it was, and no argument in this arc supplies one.

A consistency check worth recording, since the corpus carries two cubics for $5_2$: $D$ takes the same value at the upper-half-plane root of $X^3 - 2X^2 + 3X - 1$ and at that of $X^3 - X^2 + 1$, agreeing to eighteen digits, even though the two roots have different moduli ($\approx 1.5247$ and $\approx 1.1510$). The two cubics are Landen-related and describe the same tetrahedron up to the shape-parameter symmetries $z \mapsto 1/(1-z) \mapsto 1 - 1/z$, which permute the three angles and so leave the $\Lambda$-sum fixed.

## Scope

The mathematics is not new. Kummer's identity and the Bloch--Wigner function are classical, the ideal-tetrahedron setting is Thurston's, and the shape-field framework is Neumann and Zagier's. What the corpus adds is the machine-checked proof and the radial reduction that makes it a one-variable argument.

Nothing here establishes that any triangulation is a triangulation *of* a knot complement — that is Thurston hyperbolisation together with Mostow rigidity, needing a theory of hyperbolic $3$-manifolds that neither Mathlib nor this corpus has. No volume conjecture is touched.
