The cubic is symmetric under the exchange $X\leftrightarrow z$. Writing

$$
  F(X,z)= X^3+(z+1)X^2+(z^2+z+1)X+(z^3+z^2+z+1),
$$

gives $F(X,z)=F(z,X)$ term by term. This involution $\iota\colon(X,z)\mapsto(z,X)$ is a *T-duality*. It identifies every color fibre $\mathcal{E}_z$ with its dual spacetime wrapping $\mathcal{E}_X$. The internal and external degrees of freedom of Bring's surface are thus algebraically indistinguishable.

**Quotient space.**
Passing to the symmetric coordinates $u=X+z$, $v=Xz$, the curve becomes

```tex
\begin{equation}\label{eq:symmetric-quotient}
  v =  \frac{(u+1)(u^2+1)}{2u+1}.
\end{equation}
```

This is rational in $u$. Hence the quotient is $\mathcal{E}_z/\langle\iota\rangle\cong\mathbb{P}^1(\mathbb{C})$. Folding the torus along its $X=z$ diagonal collapses it to a genus-$0$ Riemann sphere.

**Weierstrass normal form.**
Depressing the cubic via $X=t-\tfrac{z+1}{3}$ eliminates the quadratic term:

```tex
\begin{equation}\label{eq:weierstrass-depressed}
  t^{3}+p(z)t+q(z)=0,\qquad
  p=\frac{2z^2+z+2}{3},\quad
  q=\frac{5(4z^3+3z^2+3z+4)}{27}.
\end{equation}
```

The discriminant $\Delta(z)=-4p(z)^3-27q(z)^2$ is a polynomial in $z$. Its roots determine the singular fibres of the elliptic fibration $\mathcal{S}\to\mathbb{P}^1(\mathbb{C})$. At those roots, the $j$-invariant $j(\mathcal{E}_z)=-1728\cdot 64p(z)^3/\Delta(z)$ degenerates.
