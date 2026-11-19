*Proof.*
Each $S$-eigenvalue is verified in turn.

**Coefficients.** The action $q \mapsto q^{-1}$ extends to the
underlying field of fractions and acts on each coefficient:

- $D = q^4 + 4q^2 + 1$ is palindromic in $q^2$: under $q \to q^{-1}$,
  $D \to q^{-4} + 4q^{-2} + 1 = q^{-4}(1 + 4q^2 + q^4) = q^{-4} D$.
  Then $W_{\mathrm{sym}} = q^2/D \to q^{-2}/(q^{-4} D) = q^2/D$,
  invariant.  Same for $W_{\mathrm{alt}}$.  For $W_{\mathrm{std}}$:
  $(q^2+1)^2 \to (q^{-2}+1)^2 = q^{-4}(1+q^2)^2$, so
  $W_{\mathrm{std}} \to q^{-4}(1+q^2)^2 / (q^{-4} D) = W_{\mathrm{std}}$.
- $[3]_q = q^2 + 1 + q^{-2}$: invariant under $q \to q^{-1}$.
- $h_{\mathrm{A}} = q - q^{-1} \to q^{-1} - q = -h_{\mathrm{A}}$, so $h_{\mathrm{A}}$ has eigenvalue
  $-1$ and $h_{\mathrm{A}}^2$ has eigenvalue $+1$.
- $z$: at the canonical weight $z = q^3/(q^2+1)$ the action gives
  $z \mapsto 1/(q(q^2+1)) = z - h_{\mathrm{A}}$, the negative-crossing loop
  value $\mathrm{tr}_M(\sigma^{-1})$. So $z$ is not an $S$-eigenvector: $S$
  exchanges the two loop values. Equivalently, the Markov trace commutes with
  $S$, $\mathrm{tr}_M(S(X)) = S(\mathrm{tr}_M(X))$, and the relation
  $z(q^{-1}) = z(q) - h_{\mathrm{A}}$ is exactly the condition for this. (The
  excised convention-C weight $1/(q^{1/2}+q^{-1/2})$ is fixed by $S$, but its
  trace does not commute with $S$.)
- Catalan's constant $G$, Borromean volume $8G$, electron mass
  $m_e$, and binding scale $\alpha$ are real canonical constants
  unaffected by the algebraic action.

**Functional $\Phi_2$.** The transfer matrix is
$T(c, d) = \begin{pmatrix} ch_{\mathrm{A}} + d & c \\ c & d \end{pmatrix}$
with $\det T = d(ch_{\mathrm{A}} + d) - c^2$.  The Frobenius antipode
maps the primitive factor $(c, d)$ to $(\bar c, \bar d - \bar c h_{\mathrm{A}})$,
where the bar is $q \mapsto q^{-1}$ on the coefficients (this swaps
$\sigma \leftrightarrow \sigma^{-1}$ and inverts $q$; without barring the
coefficients, $ud = (1, -h_{\mathrm{A}}/2)$ would map to
$(1, -3h_{\mathrm{A}}/2)$ rather than to itself).  Direct computation:

See [Table 3](#tbl:frobenius-s-classification-table3-data).

For each primitive the determinant is $S$-invariant.  Since
$\det$ is multiplicative on chain products, $\Phi_2 = \sum_i
\log\lvert\det M_i\rvert$ is $S$-invariant.

**Functional $\Phi_3$.** Write an element of the two-strand Hecke algebra as
$X = c\,\sigma + d$, with characters $\chi^{\mathrm{sym}}(X) = cq + d$ and
$\chi^{\mathrm{alt}}(X) = -c q^{-1} + d$ (the eigenvalues $q$ and $-q^{-1}$ of
$\sigma$). The bar involution sends $\sigma \mapsto \sigma^{-1} = \sigma - h_{\mathrm{A}}$
and $q \mapsto q^{-1}$, so $S(c\sigma + d) = \bar c\,\sigma + (\bar d - \bar c\,h_{\mathrm{A}})$,
where $\bar{\ }$ is $q \mapsto q^{-1}$ on the coefficients. It is a ring
automorphism (semilinear over $q \mapsto q^{-1}$), so $S$ of a chain product is
the product of the barred factors.

Call $X$ *bar-homogeneous of sign* $\varepsilon \in \{\pm 1\}$ if
$\bar c = \varepsilon c$ and $\bar d = -\varepsilon d$. Two facts follow by
direct expansion, using $\bar h_{\mathrm{A}} = -h_{\mathrm{A}}$ and
$q - h_{\mathrm{A}} = q^{-1}$:

1. *Character swap.* If $X$ is homogeneous of sign $\varepsilon$, then
   $\chi^{\mathrm{sym}}(S X) = \varepsilon c\,(q - h_{\mathrm{A}}) - \varepsilon d
   = -\varepsilon\,\chi^{\mathrm{alt}}(X)$ and
   $\chi^{\mathrm{alt}}(S X) = -\varepsilon c\,(q^{-1} + h_{\mathrm{A}}) - \varepsilon d
   = -\varepsilon\,\chi^{\mathrm{sym}}(X)$.
2. *Closure.* With $\sigma^2 = h_{\mathrm{A}}\sigma + 1$,
   $(a\sigma + b)(c\sigma + d) = (ac\,h_{\mathrm{A}} + ad + bc)\,\sigma + (ac + bd)$.
   If the factors are homogeneous of signs $\varepsilon, \varepsilon'$, every
   monomial of the $\sigma$-coefficient has bar-sign $-\varepsilon\varepsilon'$
   and every monomial of the constant term has bar-sign $\varepsilon\varepsilon'$,
   so the product is homogeneous of sign $-\varepsilon\varepsilon'$.

The three primitives $(1, 0)$, $(1, -h_{\mathrm{A}})$, $(1, -h_{\mathrm{A}}/2)$
are homogeneous of sign $+1$ (the coefficient $1$ is bar-invariant and $0$,
$-h_{\mathrm{A}}$, $-h_{\mathrm{A}}/2$ are bar-anti-invariant), and the unit
$(0, 1)$ is homogeneous of sign $-1$. By closure every chain product $X_i$
entering $\Phi_3$ is homogeneous, of sign $(-1)^{n-1}$ for $n$ primitive
factors, and by the character swap

$$
  \frac{\chi^{\mathrm{sym}}(S X_i)}{\chi^{\mathrm{alt}}(S X_i)}
  = \frac{-\varepsilon\,\chi^{\mathrm{alt}}(X_i)}{-\varepsilon\,\chi^{\mathrm{sym}}(X_i)}
  = \left(\frac{\chi^{\mathrm{sym}}(X_i)}{\chi^{\mathrm{alt}}(X_i)}\right)^{-1}.
$$

The sign $\varepsilon$ cancels, so only homogeneity matters, not the parity of
$n$. The identity holds in the field of rational functions and so at every
evaluation point where both characters are nonzero. Taking
$\log\lvert\cdot\rvert$ and summing over $i$ gives
$\Phi_3(S(\beta)) = -\Phi_3(\beta)$, eigenvalue $-1$.

*Scope.* The argument is for chains of bar-homogeneous factors, which
includes every chain of the three primitives (and the nucleon and electron
crossings of the same form). It is not a property of $\Phi_3$ on all of the
Hecke algebra. For a general element, $\chi^{\mathrm{sym}}$ and
$\chi^{\mathrm{alt}}$ are bar-equivariant, since both are ring homomorphisms
and $\chi(\sigma^{-1}) = \overline{\chi(\sigma)}$. So $S$ acts on $\Phi_3$, as
on $\Phi_1$, by the evaluation flip $q_0 \mapsto q_0^{-1}$, which is not a
sign change in general. Example: $X = \sigma + 1$ is not homogeneous, and the
product of the two ratios is
$-(q+1)^2/(q-1)^2 \neq \pm 1$, so $\Phi_3 + \Phi_3 \circ S$ picks up
$2\log\lvert (q_0+1)/(q_0-1) \rvert \neq 0$ from this factor.
Numerically, one finds $\lvert\Phi_3 + \Phi_3 \circ S\rvert \lesssim 10^{-51}$ at the proton
pin (mpmath, 50 digits) on all seven of its chains.

**Functional $\Phi_1$.** Because the canonical Markov trace commutes with
$S$, $S$ acts on $\Phi_1$ by inverting the evaluation point:
$\Phi_1(S(\beta); q_0) = \Phi_1(\beta; q_0^{-1})$. The raw $\Phi_1$ is
therefore not an $S$-eigenvector. It splits as
$\Phi_1 = \Phi_1^{+} + \Phi_1^{-}$ with
$\Phi_1^{\pm} = \tfrac12\bigl(\Phi_1(\beta) \pm \Phi_1(S(\beta))\bigr)$;
the eigenvalue $+1$ in Table 1 is that of the projection $\Phi_1^{+}$, which is
$S$-even by construction, and $\Phi_1^{-}$ is $S$-odd. $\square$

**Corollary.** Since $\Phi_2$ is $S$-even and $\Phi_3$ is $S$-odd,

$$
  \mathfrak{m}(S(\beta)) - \mathfrak{m}(\beta)
  = -2 \alpha \bigl(\Phi_1^{-}(\beta) + h_{\mathrm{A}}^2 \Phi_3(\beta)\bigr).
$$

The chirality term is the unique $S$-odd channel only when $\Phi_1^{-}$
vanishes. It does not vanish in general: on the proton chain $uud$ at the
proton pin, $\Phi_1^{-} \approx 0.0526$ against
$h_{\mathrm{A}}^2 \Phi_3 \approx 0.00912$, a ratio $\approx 5.77$.

Since $S$ maps the proton braid (uud) to a braid with quark content (ddu),
the $S$-odd part of the mass is the structural carrier of the
proton-neutron splitting at the Wedderburn formula level, and it has two
sources, $\Phi_1^{-}$ and $h_{\mathrm{A}}^2\Phi_3$, not one.
