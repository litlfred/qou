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
