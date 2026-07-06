Continuing the SU(2) example
([quantum universe on SU(2)](#ex:quantum-universe-su2)), we make
the Frobenius pairing concrete.

Set $A = \mathcal{O}(\mathrm{SU}(2))$ with pointwise multiplication
$\mu(f \otimes g) = fg$ and Frobenius form
$\int_A f = \int_{\mathrm{SU}(2)} f(x)\,d\mu_{\mathrm{Haar}}(x)$
(the Haar integral).  The Frobenius pairing is the composite

$$
  \langle f, g \rangle_A
  =  \int_A \!\circ \mu(f \otimes g)
  =  \int_{\mathrm{SU}(2)} f(x)g(x)\,d\mu_{\mathrm{Haar}}(x).
$$

This is the $L^2$ inner product on SU(2).

**Non-degeneracy.**  The pairing is non-degenerate because Haar
measure on a compact group has full support: if
$\langle f, \phi \rangle_A = 0$ for all $\phi \in A$, then $f = 0$ a.e.,
hence $f = 0$ in $A$.  Equivalently, the Peter–Weyl theorem gives
an orthonormal basis of matrix coefficients
$\{D^j_{mn}\}_{j \in \frac{1}{2}\mathbb{Z}_{\geq 0}}$ satisfying

$$
  \langle D^j_{mn}, D^{j'}_{m'n'} \rangle_A
  =  \frac{1}{2j+1}\delta_{jj'}\delta_{mm'}\delta_{nn'}.
$$

The isomorphism $A \xrightarrow{\sim} A^{\vee}$ sends each basis
element to its dual functional scaled by $1/(2j+1)$.

**Concrete calculation on $\mathbb{C}^2$.**  The matrix generators
of $\mathcal{O}(\mathrm{SU}(2))$ are
$\alpha, \beta, \bar{\alpha}, \bar{\beta}$ with
$|\alpha|^2 + |\beta|^2 = 1$.  The spin-$\tfrac{1}{2}$
matrix coefficients are $D^{1/2}_{mn} \in \{\alpha, \beta, -\bar{\beta}, \bar{\alpha}\}$.  We compute:

$$
  \langle \alpha, \alpha \rangle_A
  =  \int_{\mathrm{SU}(2)} |\alpha|^2d\mu
  =  \tfrac{1}{2},
  \qquad
  \langle \alpha, \beta \rangle_A
  =  \int_{\mathrm{SU}(2)} \alpha\beta\,d\mu
  =  0.
$$

The factor $\tfrac{1}{2} = 1/(2 \cdot \tfrac{1}{2} + 1)$ confirms
the Peter–Weyl normalisation for spin $j = \tfrac{1}{2}$.

**The snake identity** (non-degeneracy in categorical language):
the coevaluation $\tilde{\eta} \colon \mathbf{1} \to A \otimes A$
sends $1 \mapsto \sum_{j,m,n} (2j+1)D^j_{mn} \otimes \overline{D^j_{mn}}$.  The composite
$A \xrightarrow{\mathrm{id} \otimes \tilde{\eta}} A \otimes A \otimes A \xrightarrow{(\int_A \circ \mu) \otimes \mathrm{id}} A$ acts as

$$
  f  \longmapsto  \sum_{j,m,n} (2j+1)
  \langle f, D^j_{mn} \rangle_A \cdot \overline{D^j_{mn}}
  =  f,
$$

by Peter–Weyl completeness.  This is $\mathrm{id}_A$, confirming
non-degeneracy.
