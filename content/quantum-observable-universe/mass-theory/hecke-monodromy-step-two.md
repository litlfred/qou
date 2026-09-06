**Conjecture (Step 2 as monodromy).** Let $P(X, z) = X^3 + (z+1)X^2 + (z^2+z+1)X + (z^3+z^2+z+1)$ be the colour cubic, whose root $X(z)$ and its jets are the Seiberg--Witten periods, and let $\Delta \subset \mathbb{C}$ be its discriminant locus in $z$. The substrate connection on $\mathbb{C} \setminus \Delta$ has braid-group monodromy $\varrho \colon B_n \to H_n(q)$ into the Hecke tower carrying the Markov trace, such that for every generator $g_i = \varrho(\sigma_i)$:

1. the Hecke quadratic $g_i^2 = (q - q^{-1})\, g_i + 1$ holds, together with the braid relation $g_i g_{i+1} g_i = g_{i+1} g_i g_{i+1}$ and far commutation;
2. under the classical specialisation $\varepsilon \colon H_n(q) \to \mathbb{Q}S_n$ each $g_i$ becomes an involution, $\varepsilon(g_i)^2 = 1$ --- the Picard--Lefschetz transposition of the two roots of $P$ that collide at a branch point.

The two Stokes eigenvalues $q$ and $-q^{-1}$ of the curvature polynomial $F(\sigma) = \sigma^2 - (q - q^{-1})\sigma - 1$ are then a consequence: $(g_i - q)(g_i + q^{-1}) = 0$.

## What is derived and what is conjectured

The discriminant is the reciprocal irreducible sextic $16z^6 + 24z^5 + 35z^4 + 50z^3 + 35z^2 + 24z + 16$, with six simple complex branch points and no branching at infinity. Continuing the three roots of $P$ around each branch point gives a transposition every time; three distinct transpositions occur, so the monodromy group is $S_3$, and the ordered product of the six local monodromies is the identity. On the two colliding roots a transposition is the swap, an involution with eigenvalues $\pm 1$ and minimal polynomial $\sigma^2 - 1 = (\sigma - q)(\sigma + q^{-1})|_{q=1}$. So item 2, and the $q = 1$ specialisation of item 1, are theorems about the geometry the framework already carries. Pushing item 1 through $\varepsilon$ and using item 2 forces $\varepsilon\bigl((q - q^{-1})\, g_i\bigr) = 0$: the classical shadow forgets exactly the deformation parameter.

What remains conjectural is the deformation $1 \mapsto q$ itself: no connection with $q$-deformed monodromy has been constructed, and the curvature form the chain names is stipulated rather than computed. The literature model is Kohno--Drinfeld: the monodromy of a Knizhnik--Zamolodchikov connection factors through $H_n(q)$. At real level that monodromy has unit-modulus eigenvalues, which the real substrate pin $q_0 \approx 1.11$ is not; a Knizhnik--Zamolodchikov realisation therefore requires the non-unitary level $k + 2 = 2\pi i/\ln q_0 \approx 60.218\, i$ in the convention $q = e^{2\pi i/(k+2)}$. Whether the substrate connection is such a connection is the open construction.

## Lean structure

The class `QOU.Mass.HeckeMonodromy` carries items 1 and 2 as its four fields (`quad`, `braid`, `far_comm`, `shadow_involution`). Derived from it without further hypotheses: `hecke_factor` (the eigenvalue factorisation), `shadow_hecke_at_one`, and `shadow_kills_h`. The classical shadow itself is proved unconditionally in `QOU.Mass.HeckeQuadraticClassicalShadow` (the swap is an involution satisfying the $q = 1$ quadratic), and the unit-modulus obstruction in `QOU.Mass.KZUnitModulusPrune`.
