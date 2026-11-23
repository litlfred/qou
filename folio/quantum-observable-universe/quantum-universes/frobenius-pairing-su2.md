The Frobenius pairing is made concrete on $\mathrm{SU}(2)$, with the coordinate ring and Haar integral of the $\mathrm{SU}(2)$ example below.

Set $A = \mathcal{O}(\mathrm{SU}(2))$ with pointwise multiplication $\mu(f \otimes g) = fg$ and Haar integral $\int_A f = \int_{\mathrm{SU}(2)} f(x)\,d\mu_{\mathrm{Haar}}(x)$. The Frobenius pairing is the $L^2$ inner product:

$$
  \langle f, g \rangle_A
  =  \int_{\mathrm{SU}(2)} f(x)g(x)\,d\mu_{\mathrm{Haar}}(x).
$$

**Non-degeneracy.** Haar measure has full support. If $\langle f, \phi \rangle_A = 0$ for all $\phi \in A$, then $f = 0$ a.e., hence $f = 0$. The Peter–Weyl theorem provides an orthonormal basis of matrix coefficients $\{D^j_{mn}\}$ satisfying:

$$
  \langle D^j_{mn}, D^{j'}_{m'n'} \rangle_A
  =  \frac{1}{2j+1}\delta_{jj'}\delta_{mm'}\delta_{nn'}.
$$

The isomorphism $A \xrightarrow{\sim} A^{\vee}$ sends each basis element to its dual functional scaled by $1/(2j+1)$.

**Concrete calculation on $\mathbb{C}^2$.** The matrix generators of $\mathcal{O}(\mathrm{SU}(2))$ are $\alpha, \beta, \bar{\alpha}, \bar{\beta}$ with $|\alpha|^2 + |\beta|^2 = 1$. The spin-$\tfrac{1}{2}$ coefficients are $D^{1/2}_{mn} \in \{\alpha, \beta, -\bar{\beta}, \bar{\alpha}\}$, and the pairing evaluates to

$$
  \langle \alpha, \alpha \rangle_A = \tfrac{1}{2}, \qquad \langle \alpha, \beta \rangle_A = 0.
$$

The factor $\tfrac{1}{2}$ confirms the normalisation for spin $j = \tfrac{1}{2}$.

**The snake identity.** The coevaluation $\tilde{\eta} \colon \mathbf{1} \to A \otimes A$ sends $1 \mapsto \sum_{j,m,n} (2j+1)D^j_{mn} \otimes \overline{D^j_{mn}}$. The composite $A \xrightarrow{\mathrm{id} \otimes \tilde{\eta}} A \otimes A \otimes A \xrightarrow{(\int_A \circ \mu) \otimes \mathrm{id}} A$ acts as:

$$
  f  \longmapsto  \sum_{j,m,n} (2j+1)
  \langle f, D^j_{mn} \rangle_A \cdot \overline{D^j_{mn}} = f.
$$

This is $\mathrm{id}_A$, confirming non-degeneracy.
