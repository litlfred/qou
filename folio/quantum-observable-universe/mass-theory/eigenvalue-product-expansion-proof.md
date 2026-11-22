*Proof.*
The nuclear braid has three types of pairwise crossings.  In the
Hoefsmit seminormal basis
([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form)),
each crossing $c \cdot T_g + d \cdot I$ on the diagonal generator
$T_1 = \mathrm{diag}(q, -q^{-1})$ contributes eigenvalues:

| Crossing | $(c, d)$ | $\lambda_{\mathrm{sym}} = cq + d$ | $\lambda_{\mathrm{anti}} = -cq^{-1} + d$ |
|----------|---------|:---:|:---:|
| pp ($\sigma$) | $(1, 0)$ | $q$ | $-q^{-1}$ |
| nn ($\sigma^{-1}$) | $(1, -h)$ | $q^{-1}$ | $-q$ |
| pn (mixed) | $(1, -h/2)$ | $[2]/2$ | $-[2]/2$ |

The pn row uses $d = -h/2$, the $\delta = 0$ convention. Under the
colour-tube-weighted interface factor $d = -h(1/2 - \delta/4)$, with
$\delta$ the substrate flavour split of
[the substrate flavor split conjecture](#conj:flavor-split-substrate-mass), *both* pn
eigenvalues shift by the same $+h\delta/4$:

$$
  \lambda_{\mathrm{sym}} = \frac{[2]}{2} + \frac{h\delta}{4},
  \qquad
  \lambda_{\mathrm{anti}} = -\frac{[2]}{2} + \frac{h\delta}{4},
  \qquad
  \lambda_{\mathrm{sym}} + \lambda_{\mathrm{anti}}
    = \frac{h\delta}{2}
    = \frac{(q-1)^4 (q+1)^2 (q^2+1)}{6 q^5}.
$$

So the exact antisymmetry $\lambda_{\mathrm{anti}} = -\lambda_{\mathrm{sym}}$
is a property of $\delta = 0$, not of the pn crossing as such, and the
factorisation of $\Lambda_{\mathrm{sym}}$ below as a power of $[2]/2$ is
conditional on that convention. The shift is $h\delta/4 \approx 7.190 \times
10^{-5}$ at the substrate anchor.

The symmetric channel product over all crossings on $T_1$:

$$
  \Lambda_{\mathrm{sym}}
  = q^{n_{\mathrm{pp}}} \cdot (q^{-1})^{n_{\mathrm{nn}}}
    \cdot ([2]/2)^{n_{\mathrm{pn}}}
  = q^{n_{\mathrm{pp}} - n_{\mathrm{nn}}}
    \cdot ([2]/2)^{n_{\mathrm{pn}}}
$$

The crossing counts are:
$n_{\mathrm{pp}} = Z(Z{-}1)/2$,
$n_{\mathrm{nn}} = N(N{-}1)/2$,
$n_{\mathrm{pn}} = ZN$.

The exponent simplifies:

$$
  n_{\mathrm{pp}} - n_{\mathrm{nn}}
  = \frac{Z(Z{-}1) - N(N{-}1)}{2}
  = \frac{(Z{-}N)(Z{+}N{-}1)}{2}
  = T \cdot (A - 1)
$$

where $T = (Z - N)/2$ (signed isospin).

Taking the logarithm and substituting $Z = A/2 + T$, $N = A/2 - T$:

$$
  \ln|\Lambda_{\mathrm{sym}}|
  = \ell \cdot T(A - 1) +
  \ell_2 \cdot (A^2/4 - T^2)
$$

Expanding gives the four terms (I)--(IV).

Verified against explicit Hoefsmit matrix computation for all $N = Z$
nuclei ($T = 0$: ${}^4\mathrm{He}$, ${}^6\mathrm{Li}$, ${}^{12}\mathrm{C}$,
${}^{16}\mathrm{O}$) to machine precision.

**The $q$-integer identification.**
The volume coefficient involves $[c{+}1]_q$ where $c$ is the
confinement braid's crossing number.  This arises because the
$c$-crossing eigenvalue product in the symmetric channel is
$q^c$, and the Markov trace of $q^c$ in the $[2{,}1]$ representation
evaluates to:

$$
  \mathrm{tr}_M(q^c)
  = W_{\mathrm{sym}} \cdot q^c +
  W_{\mathrm{std}} \cdot \frac{\sum_{j=0}^{c} q^{c-2j}}{2} +
  W_{\mathrm{alt}} \cdot q^{-c}
$$

The middle term is $[c{+}1]_q/2$, giving the $[c{+}1]$ factor in
the volume coefficient.  For the Borromean braid ($c = 6$):
$[7]_q \approx 7.63$.  For the figure-eight ($c = 4$):
$[5]_q \approx 5.22$.
$\square$
