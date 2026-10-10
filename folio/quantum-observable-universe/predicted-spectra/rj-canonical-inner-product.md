The Markov trace on the Iwahori–Hecke algebra $H_r(q)$ induces a unique inner product on the representation ring $R(H_r(q))$ via Schur orthogonality.

## Statement

**Proposition.**
*Let $H_r(q)$ be the Iwahori–Hecke algebra on $r$ strands with parameter $q \neq 0, 1$. Let $R(H_r(q)) = \bigoplus_{\lambda \vdash r} \mathbb{Z} \cdot [\lambda]$ be its representation ring.*

**(i)** *The Markov trace $\mathrm{tr}_M \colon H_r(q) \to \mathbb{Q}(q)$ uses the canonical Markov parameter $z = q^3/(q^2+1) = q^2/[2]_q$. It descends to a bilinear form on $R(H_r(q))$:*

$$
  \langle [\lambda], [\mu] \rangle_{\mathrm{RJ}}
  = 
  d_\lambda(q) \cdot \delta_{\lambda\mu},
$$

*where $d_\lambda(q) = \prod_{\Box \in \lambda} \frac{[2 + c(\Box)]_q}{[h(\Box)]_q}$ is the $U_q(\mathfrak{sl}_2)$ quantum dimension of $V_\lambda$. Here $c(\Box)$ is the content and $h(\Box)$ the hook length (arm $+$ leg $+ 1$) of cell $\Box$ in the Young diagram $\lambda$, and $[n]_q = (q^n - q^{-n})/(q - q^{-1})$. The Markov block weights are $w_\lambda = \mathrm{tr}_M(p_\lambda) = d_\lambda(q)/[2]_q^{\,r}$ for a minimal idempotent $p_\lambda$. Because $d_\lambda = 0$ whenever $\lambda$ has more than two rows, the form is degenerate: its radical is spanned by the classes $[\lambda]$ with more than two rows, and it is non-degenerate on the span of the two-row classes.*

**(ii)** *This inner product is unique up to an overall scalar. Schur orthogonality for the irreducible characters $\chi_\lambda$ of $H_r(q)$ forces:*

$$
  \mathrm{tr}_M\!\bigl(\chi_\lambda \cdot \chi_\mu\bigr)
  = 
  d_\lambda(q) \cdot \delta_{\lambda\mu}.
$$

*Any bilinear form on the two-row part of $R(H_r(q))$ that is diagonal in the irrep basis and compatible with the Markov trace normalization $\mathrm{tr}_M(1) = 1$ is a scalar multiple of $\langle -, - \rangle_{\mathrm{RJ}}$.*

**(iii)** *The Rosso–Jones invariant of a torus knot $\tau(r,s)$ is the evaluation of this inner product on the full-twist element $\omega^s$:*

$$
  J(\tau(r,s))
  = 
  \sum_{\lambda \vdash r} d_\lambda(q) \cdot \omega_\lambda^s
  = 
  \langle \omega^s, [\mathrm{triv}] \rangle_{\mathrm{RJ}},
$$

*where $\omega_\lambda = q^{c_\lambda}$ is the eigenvalue of the full twist on irrep $\lambda$, and $c_\lambda$ is the content of $\lambda$.*

Until 2026-10-10 this proposition used the excised convention-C parameter $z = (q^{1/2} + q^{-1/2})^{-1}$, with values in $\mathbb{Q}(q^{1/2})$, half-integer $q$-integers and the quantum dimension $\prod [h(\Box)]_q/[h'(\Box)]_q$; under that convention the form had no radical. Part (iii) has not been re-verified after the change: in particular the full-twist eigenvalue on the antisymmetric channel carries the sign of the Hecke eigenvalue $-q^{-1}$, which $\omega_\lambda = q^{c_\lambda}$ does not show.
