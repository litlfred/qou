The Markov trace on the Iwahori--Hecke algebra $H_r(q)$ induces,
via Schur orthogonality, a **unique** inner product on the
representation ring $R(H_r(q))$.

## Statement

**Proposition.**
*Let $H_r(q)$ be the Iwahori--Hecke algebra on $r$ strands with
parameter $q \neq 0, 1$, and let
$R(H_r(q)) = \bigoplus_{\lambda \vdash r} \mathbb{Z} \cdot [\lambda]$
be its representation ring.*

**(i)** *The Markov trace
$\mathrm{tr}_M \colon H_r(q) \to \mathbb{Q}(q^{1/2})$ descends to a
bilinear form on $R(H_r(q))$:*

$$
  \langle [\lambda],\, [\mu] \rangle_{\mathrm{RJ}}
  \;=\;
  d_\lambda(q) \cdot \delta_{\lambda\mu},
$$

*where $d_\lambda(q) = \prod_{\Box \in \lambda}
\frac{[h(\Box)]_q}{[h'(\Box)]_q}$ is the quantum dimension
(hook-length formula) and $[n]_q = (q^{n/2} - q^{-n/2})/(q^{1/2} - q^{-1/2})$.*

**(ii)** *This inner product is **unique** (up to overall scalar):
Schur orthogonality for the irreducible characters
$\chi_\lambda$ of $H_r(q)$ forces*

$$
  \mathrm{tr}_M\!\bigl(\chi_\lambda \cdot \chi_\mu\bigr)
  \;=\;
  d_\lambda(q) \cdot \delta_{\lambda\mu}.
$$

*Any bilinear form on $R(H_r(q))$ that is diagonal in the irrep
basis and compatible with the Markov trace normalization
$\mathrm{tr}_M(1) = 1$ is a scalar multiple of
$\langle -,\, - \rangle_{\mathrm{RJ}}$.*

**(iii)** *The Rosso--Jones invariant of a torus knot
$\tau(r,s)$ is the evaluation of this inner product on the
full-twist element $\omega^s$:*

$$
  J(\tau(r,s))
  \;=\;
  \sum_{\lambda \vdash r} d_\lambda(q) \cdot \omega_\lambda^s
  \;=\;
  \langle \omega^s,\, \mathbf{1} \rangle_{\mathrm{RJ}},
$$

*where $\omega_\lambda = q^{c_\lambda}$ is the eigenvalue of the
full twist on irrep $\lambda$ and $c_\lambda$ is the content
of $\lambda$.*

## Proof

**(i)** The Markov trace factors through the Grothendieck ring:
$\mathrm{tr}_M(a) = \sum_\lambda d_\lambda(q) \cdot
\mathrm{tr}_\lambda(a)$, where $\mathrm{tr}_\lambda$ is the
character of irrep $\lambda$.  Restricting to the class
functions (which are spanned by $\{\chi_\lambda\}$) gives the
stated diagonal form.

**(ii)** The irreps $\{\chi_\lambda : \lambda \vdash r\}$ form an
orthogonal basis of the center $Z(H_r(q))$ under the Markov
trace pairing.  Schur orthogonality
$\mathrm{tr}_M(\chi_\lambda \chi_\mu) = d_\lambda \delta_{\lambda\mu}$
is a standard consequence of the semisimplicity of $H_r(q)$ for
generic $q$ \cite{rosso-jones1993}.  Any other bilinear form
diagonal in $\{\chi_\lambda\}$ and normalized at the identity
differs only by rescaling the Markov parameter $z$.

**(iii)** The Rosso--Jones formula \cite{rosso-jones1993}
decomposes $J(\tau(r,s))$ over irreps of $H_r(q)$.  Each irrep
contributes its quantum dimension $d_\lambda(q)$ times the
$s$-th power of its full-twist eigenvalue $\omega_\lambda$.
This is precisely the inner product
$\langle \omega^s, \mathbf{1} \rangle_{\mathrm{RJ}}$.  $\square$
