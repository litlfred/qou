The cubic is symmetric under the exchange $X\leftrightarrow z$. Writing

$$
  F(X,z)= X^3+(z+1)X^2+(z^2+z+1)X+(z^3+z^2+z+1),
$$

$F(X,z)=F(z,X)$ is checked term by term. This involution $\iota\colon(X,z)\mapsto(z,X)$ is a *T-duality*. In homogeneous coordinates it is the swap $[X:z:w]\mapsto[z:X:w]$, an automorphism of the color curve $\mathcal{E}_{\mathrm{col}}=\{h_3(X,z,w)=0\}$ of [color elliptic](#prop:color-elliptic). It exchanges the two projections of $\mathcal{E}_{\mathrm{col}}$: the color fibre over $z$, the three roots of $F(\,\cdot\,,z)$, goes to the fibre over $z$ of the projection to the $X$-line. The internal and external degrees of freedom of Bring's surface are thus algebraically indistinguishable.

**Quotient space.**
Passing to the symmetric coordinates $u=X+z$, $v=Xz$, the curve becomes

```tex
\begin{equation}\label{eq:symmetric-quotient}
  v =  \frac{(u+1)(u^2+1)}{2u+1}.
\end{equation}
```

This is rational in $u$. Hence the quotient is $\mathcal{E}_{\mathrm{col}}/\langle\iota\rangle\cong\mathbb{P}^1(\mathbb{C})$. Folding the torus along its $X=z$ diagonal collapses it to a genus-$0$ Riemann sphere.

**Weierstrass normal form.**
Depressing the cubic via $X=t-\tfrac{z+1}{3}$ eliminates the quadratic term, and puts the fibrewise curve $\mathcal{E}_z\colon y^2=F(X,z)$ of [color elliptic](#prop:color-elliptic) in the Weierstrass form $y^2=t^3+p(z)t+r(z)$:

```tex
\begin{equation}\label{eq:weierstrass-depressed}
  t^{3}+p(z)t+r(z)=0,\qquad
  p=\frac{2z^2+z+2}{3},\quad
  r=\frac{5(4z^3+3z^2+3z+4)}{27}.
\end{equation}
```

The discriminant $\Delta(z)=-4p(z)^3-27r(z)^2$ equals $-D(z,1)$, where $D$ is the binary sextic of [color elliptic](#prop:color-elliptic). Its six roots are the singular fibres of the family $\mathcal{E}_z$. The $j$-invariant
$$
  j(\mathcal{E}_z)=\frac{-1728\cdot 4p(z)^3}{\Delta(z)}=\frac{256\,(2z^2+z+2)^3}{D(z,1)}
$$
has a pole at each of them.
