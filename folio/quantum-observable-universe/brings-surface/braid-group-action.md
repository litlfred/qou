The symmetric group $S_5$ acts on Bring's surface ([Bring's curve](#rem:brings-curve)) by permuting $(x_0,\dots,x_4)$. This provides the maximal automorphism group (order $120$) for genus $4$. Three distinguished families of $S_3$ subgroups govern the interplay between the base coordinates $x_j$ and the spectral resolvents $w_k$ ([Lagrange resolvents](#rem:lagrange-resolvents)). Each is described using the braid group ([braid group](#def:braid-group)), the resolvent coordinates, and the $\mathrm{SU}(2)$/$\mathrm{SO}(3)$ matrices of [SU(2) generators](#def:su2-generators)–[SO(3) generators](#def:so3-generators).

**(i) Spacetime action ($\mathbb{P}^1(\mathbb{C})$ base).**
Fix the color coordinates $x_2,x_3,x_4$ as internal fiber degrees of freedom. The constraint $w_0=0$ forces $x_0+x_1=C$ (constant). The spacetime degrees of freedom collapse projectively to the ratio $z=x_0/x_1\in\mathbb{P}^1(\mathbb{C})$. The transposition $x_0\leftrightarrow x_1$ acts as the Möbius involution $z\mapsto 1/z$. This constitutes a $\pi$-rotation on $\mathbb{P}^1(\mathbb{C})$ and embeds into $\mathrm{SU}(2)$ as $\beta=\exp(\pi e_1)$. In the resolvent basis it acts as

```tex
\begin{equation}\label{eq:spacetime-shift}
  w_k \longmapsto 
  w_k+\tfrac{1}{\sqrt{5}}(1-\zeta^k)(x_1-x_0),
  \qquad k=1,\dots,4.
\end{equation}
```

This affine shift fixes the color modes and translates the $\mathbb{P}^1(\mathbb{C})$ fibre.

**(ii) Spectral $S_3$ (trefoil action).**
The frequency-coupled pairs $(w_1,w_4)$ and $(w_2,w_3)$ are permuted by the twist and flip involutions ([braid twist-flip](#def:braid-twist-flip)). The full $S_3$ structure emerges on the projective ratios

$$
  \eta_1=\frac{w_1}{w_2},\qquad\eta_2=\frac{w_3}{w_4}.
$$

The two involutions $\sigma_1,\sigma_2$ are reflections of this $D_3$, each inverting a ratio to swap one conjugate pair; their product $\sigma_1\sigma_2=\alpha$ is the order-$3$ rotation below, not a commuting involution (commuting reflections would generate the Klein four-group $V_4$, and $4\nmid 6$). The $2$-cycle (reflection) swaps the pairs $(w_1,w_4)\leftrightarrow(w_2,w_3)$. The $3$-cycle (rotation) sends $(\eta_1,\eta_2)\mapsto(\eta_1,\zeta^j\eta_2)$ for $j\in\{1,2,3\}$, permuting the three complex branches of the cubic constraint. The $\mathrm{SU}(2)$ representation assigns the $3$-cycle to $\alpha$ and the reflection to $\beta$. The $\mathrm{SO}(3)$ images act as the holonomy on the spectral energy distribution. $R_\alpha$ rotates the time-like resolvent pair $(\omega_2,\omega_3)$ and $R_\beta$ reflects the space-like axis $\omega_1$.

**(iii) Coordinate $S_3$.**
Fixing any two coordinates (say $x_0,x_1$) as a spacetime base and permuting the remaining three $(x_2,x_3,x_4)$ yields a stabiliser $\mathrm{Stab}(\{x_0,x_1\})\cong S_3\subset S_5$. There are $\binom{5}{2}=10$ such subgroups. In the resolvent basis a permutation $\sigma\in S_3$ of $(x_2,x_3,x_4)$ acts as

```tex
\begin{equation}\label{eq:coord-s3-shift}
  w_k \longmapsto 
  w_k+\tfrac{1}{\sqrt{5}}\sum_{j=2}^{4}
    \bigl(\zeta^{k\sigma(j)}-\zeta^{kj}\bigr)x_j.
\end{equation}
```

The $w_k$ transform as vector fields over the $(x_0,x_1)$ plane. The $S_3$ permutes how these fields couple to the base. The same $\mathrm{SO}(3)$ representation realises this action, now supplying the holonomy group on the internal fibre.

**Geometric $S_3$.**
When Bring's curve is viewed as a branched cover $\mathcal{S}\to\mathbb{P}^1$, a third family of $S_3$ subgroups arises. It permutes the three critical values of the covering map. These three families—spectral, coordinate, and geometric—correspond to the three copies of $S_3$ inside $S_5$ identified in [chirality and trefoil](#rem:chirality-trefoil).
