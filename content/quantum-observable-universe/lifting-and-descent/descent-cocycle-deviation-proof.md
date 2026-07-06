**Proof.**
The transition functions at level $n+1$ relate to those at level $n$ via $g_{ij}^{(n+1)} = a_{ij}^{(n)} \cdot g_{ij}^{(n)}$, where $a_{ij}^{(n)} \in \mathcal{O}_M^{\times}$ is the local lift datum ([Yekutieli triple](#def:yekutieli-triple)). Computing the cocycle deviation at level $n+1$:

```tex
\begin{align*}
  g_{ijk}^{(n+1)}
  &= g_{ij}^{(n+1)} \cdot g_{jk}^{(n+1)} \cdot (g_{ik}^{(n+1)})^{-1} \\
  &= (a_{ij}^{(n)} \cdot g_{ij}^{(n)}) \cdot (a_{jk}^{(n)} \cdot g_{jk}^{(n)})
     \cdot (a_{ik}^{(n)} \cdot g_{ik}^{(n)})^{-1}.
\end{align*}
```

Because $a_{ij}^{(n)}$ is central in the gerbe band $\mathcal{O}_M^{\times}$, the gauge factors commute past the $a$-factors, yielding

$$
  g_{ijk}^{(n+1)}
  =
  a_{ij}^{(n)} \cdot a_{jk}^{(n)} \cdot (a_{ik}^{(n)})^{-1}
  \cdot g_{ijk}^{(n)}.
$$

The vanishing of $g_{ijk}^{(n+1)}$ in Cech cohomology imposes the twisted $2$-cocycle equation

$$
  d(g_{ijk}^{(n)})
  =
  a_{ij}^{(n)} \cdot g_{ijk}^{(n)} \cdot (a_{jk}^{(n)})^{-1},
$$

where the left-hand side is the Cech coboundary $\delta^2(g^{(n)})_{ijk}$ and the right-hand side is twisted conjugation by the $2$-morphisms. $\square$
