The Bring surface constraints take the following form in color tube coordinates.

**Spacetime recovery.**
Substituting into $z = S/D$
yields $z(\widetilde{D} - z) = \widetilde{S} + 4z$,
which rearranges to

```tex
\begin{equation}\label{eq:spacetime-recovery}
  z^2 - (\widetilde{D} - 4)\,z + \widetilde{S} \;=\; 0.
\end{equation}
```

Thus the spacetime coordinate $z$ is determined implicitly by the
shifted data $(\widetilde{S}, \widetilde{D})$.

**Shifted quadric.**
Substituting $w_k = c_k + z$ into the quadric
gives

```tex
\begin{equation}\label{eq:shifted-quadric}
  \widetilde{Q} + z\,\widetilde{S} + 2z^2 \;=\; 0,
\end{equation}
```

or equivalently $\sigma b + rg = -z(\sigma + r + g + b) - 2z^2$.

**Shifted cubic.**
Substituting $w_k = c_k + z$ into the cubic
gives

```tex
\begin{equation}\label{eq:shifted-cubic}
  \widetilde{C} + z(\widetilde{S}^2 - 2\widetilde{Q})
  + 3z^2\,\widetilde{S} + 4z^3 \;=\; 0.
\end{equation}
```

Eliminating $\widetilde{Q}$ via the shifted quadric yields the
*reduced cubic*:

```tex
\begin{equation}\label{eq:reduced-cubic}
  \widetilde{C} + z\,\widetilde{S}^2 + 5z^2\,\widetilde{S} + 8z^3 \;=\; 0.
\end{equation}
```

All three equations are polynomial over $\mathbb{Z}$ in $z, r, g, b, \sigma$;
they therefore define affine varieties over $\mathbb{Z}$ and descend
to $\mathbb{F}_\mathfrak{p}$ for every prime $\mathfrak{p} \ne 5$.
