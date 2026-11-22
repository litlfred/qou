Let $z=x_0/x_1\in\mathbb{P}^1(\mathbb{C})$ be the projective spacetime ratio ([braid group action](#rem:braid-group-action)(i)). Let $h_3$ be the complete homogeneous symmetric cubic in three variables. On Bring's surface each color coordinate $x_i$, $i\in\{2,3,4\}$, satisfies $h_3(x_i,x_0,x_1)=0$. In the chart $x_1\neq0$, with color variable $X=x_i/x_1$, this is the cubic

```tex
\begin{equation}\label{eq:color-elliptic}
  X^3+(z+1)X^2+(z^2+z+1)X+(z^3+z^2+z+1)=0.
\end{equation}
```

The variable $X$ is so named because the geometry of the fibre is a weave of colorful twisted tubes with fractal boundary structure, capturing color, chirality, and rigidity. For fixed $z$ the cubic has three roots, $x_2/x_1$, $x_3/x_1$ and $x_4/x_1$, so the color fibre over $z$ consists of three points. Two elliptic curves arise from the cubic.

1. **The color curve.** As $z$ varies, the cubic cuts out a single curve. Its projective closure $\mathcal{E}_{\mathrm{col}}=\{h_3(X,z,w)=0\}\subset\mathbb{P}^2(\mathbb{C})$ is a smooth plane cubic, hence of genus $1$, with a single $j$-invariant. The projection $[X:z:w]\mapsto[z:w]$ exhibits it as a threefold cover of $\mathbb{P}^1(\mathbb{C})$, branched over the six zeros of the binary sextic $D(z,w)=16z^6+24z^5w+35z^4w^2+50z^3w^3+35z^2w^4+24zw^5+16w^6$. The discriminant of the cubic in $X$ is $-D(z,1)$. The point $z=\infty$ is not a branch point, since $D(1,0)=16$.
2. **The fibrewise curves.** For each $z$ with $D(z,1)\neq0$, the double cover $\mathcal{E}_z\colon y^2=F(X,z)$ of the $X$-line, branched over the three roots and $\infty$, is an elliptic curve. Here $F(X,z)$ is the left side of the cubic. Its $j$-invariant varies as a rational function of $z$, and $\mathcal{E}_z$ degenerates at the six zeros of $D$. The monodromy of $\mathcal{E}_z$ around these singular fibres recovers the holonomy generators $H_1,H_2$ of [holonomy of trefoil](#rem:holonomy-trefoil).
