*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
*For a nucleus with $Z$ protons and $N$ neutrons ($A = Z + N$),
the symmetric channel eigenvalue product of the nuclear braid in the
$[2{,}1]$ representation of $H_3(R, q)$ is:*

$$
  \Lambda_{\mathrm{sym}}
  = q^{(Z-N)(A-1)/2} \cdot \Bigl(\frac{[2]_q}{2}\Bigr)^{\!ZN}
$$

*Its logarithm expands in the isospin variable $T = |Z - N|/2$ as:*

$$
  \ln|\Lambda_{\mathrm{sym}}|
  = \underbrace{\ell_2 \cdot \frac{A^2}{4}}_{\mathrm{(I)}}
  \;+\; \underbrace{\ell \cdot T \cdot A}_{\mathrm{(II)}}
  \;-\; \underbrace{\ell \cdot T}_{\mathrm{(III)}}
  \;-\; \underbrace{\ell_2 \cdot T^2}_{\mathrm{(IV)}}
$$

*where $\ell = \ln q$ and $\ell_2 = \ln([2]_q/2)$.*

*The four terms are:*

| *Term* | *Scaling* | *Origin* |
|:---:|:---:|:---:|
| *(I)* | *$A^2$* | *pn crossing count $ZN = A^2/4 - T^2$* |
| *(II)* | *$T \cdot A$* | *pp vs nn crossing excess $(Z-N)(A-1)/2$* |
| *(III)* | *$T$* | *linear isospin correction* |
| *(IV)* | *$T^2$* | *quadratic isospin (Casimir)* |

*The Coulomb correction arises separately from the standard channel,
where pp crossings contribute eigenvalue $q$ (not $[2]/2$), and the
excess*

$$
  \ln\Bigl(\frac{2q}{[2]_q}\Bigr)
  = \ln\Bigl(\frac{2q}{q + q^{-1}}\Bigr)
  \approx \frac{h^2}{2}
$$

*generates a term proportional to $Z(Z-1)$.*

*The $q$-integer $[c+1]$ in each Bethe--Weizsäcker coefficient counts
the geometric sum of eigenvalue powers over $c$ crossings:*

$$
  [c+1]_q = \sum_{j=0}^{c} q^{c - 2j}
$$

*For the Borromean braid ($c = 6$), this gives $[7]_q$.
For the figure-eight braid ($c = 4$), this gives $[5]_q$.*

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
  = \ell \cdot T(A - 1)
  + \ell_2 \cdot (A^2/4 - T^2)
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
  = W_{\mathrm{sym}} \cdot q^c
  + W_{\mathrm{std}} \cdot \frac{\sum_{j=0}^{c} q^{c-2j}}{2}
  + W_{\mathrm{alt}} \cdot q^{-c}
$$

The middle term is $[c{+}1]_q/2$, giving the $[c{+}1]$ factor in
the volume coefficient.  For the Borromean braid ($c = 6$):
$[7]_q \approx 7.63$.  For the figure-eight ($c = 4$):
$[5]_q \approx 5.22$.
$\square$
