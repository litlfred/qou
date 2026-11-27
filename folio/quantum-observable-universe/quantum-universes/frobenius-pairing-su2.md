The Frobenius pairing is made concrete on $\mathrm{SU}(2)$, with the coordinate ring and Haar integral of the $\mathrm{SU}(2)$ example below.

Set $A = \mathcal{O}(\mathrm{SU}(2))$ with pointwise multiplication $\mu(f \otimes g) = fg$ and Haar integral $\int_A f = \int_{\mathrm{SU}(2)} f(x)\,d\mu_{\mathrm{Haar}}(x)$. The bilinear Frobenius pairing is

$$
  \langle f, g \rangle_A
  =  \int_{\mathrm{SU}(2)} f(x)g(x)\,d\mu_{\mathrm{Haar}}(x),
$$

which relates to the sesquilinear $L^2$ / GNS inner product via complex conjugation: $\langle f, g \rangle_{L^2} = \int_{\mathrm{SU}(2)} \overline{f(x)}g(x)\,d\mu_{\mathrm{Haar}}(x) = \langle \bar{f}, g \rangle_A$.

**Non-degeneracy.** Haar measure has full support: for any $f \in A$, setting $\phi = \bar{f} \in A$ gives $\langle \phi, f \rangle_A = \int_{\mathrm{SU}(2)} |f(x)|^2\,d\mu_{\mathrm{Haar}}(x)$, so $\langle \phi, f \rangle_A = 0$ for all $\phi \in A$ forces $f = 0$. The Peter--Weyl theorem provides an orthogonal basis of matrix coefficients $\{D^j_{mn}\}$ satisfying

$$
  \langle \overline{D^j_{mn}}, D^{j'}_{m'n'} \rangle_A
  =  \frac{1}{2j+1}\delta_{jj'}\delta_{mm'}\delta_{nn'}.
$$

(On the non-symmetric quantum deformation of $\mathcal{O}(\mathrm{SU}(2))$ constructed in the next chapter, Woronowicz's Peter--Weyl orthogonality replaces $2j + 1$ by the categorical dimension $\dim_q(V_j)$ and weights each row index $m$ by the modular Nakayama factor of the Haar state.) The isomorphism $A \xrightarrow{\sim} A^{\vee}$ sends $\overline{D^j_{mn}}$ to the dual coordinate functional of $D^j_{mn}$ scaled by $1/(2j+1)$.

**Concrete calculation on $\mathbb{C}^2$.** The matrix generators of $\mathcal{O}(\mathrm{SU}(2))$ are $\alpha, \beta, \bar{\alpha}, \bar{\beta}$ with $|\alpha|^2 + |\beta|^2 = 1$. The spin-$\tfrac{1}{2}$ coefficients are $D^{1/2}_{mn} \in \{\alpha, \beta, -\bar{\beta}, \bar{\alpha}\}$, and the bilinear pairing evaluates to

$$
  \langle \bar{\alpha}, \alpha \rangle_A = \tfrac{1}{2}, \qquad \langle \alpha, \alpha \rangle_A = 0, \qquad \langle \bar{\alpha}, \beta \rangle_A = 0.
$$

The factor $\tfrac{1}{2}$ confirms the normalisation for spin $j = \tfrac{1}{2}$.

**The snake identity.** The coevaluation $\tilde{\eta} \colon \mathbf{1} \to A \otimes A$ sends $1 \mapsto \sum_{j,m,n} (2j+1)D^j_{mn} \otimes \overline{D^j_{mn}}$. The composite $A \xrightarrow{\mathrm{id} \otimes \tilde{\eta}} A \otimes A \otimes A \xrightarrow{(\int_A \circ \mu) \otimes \mathrm{id}} A$ acts as:

$$
  f  \longmapsto  \sum_{j,m,n} (2j+1)
  \langle f, D^j_{mn} \rangle_A \cdot \overline{D^j_{mn}} = f.
$$

This is $\mathrm{id}_A$, confirming non-degeneracy.
