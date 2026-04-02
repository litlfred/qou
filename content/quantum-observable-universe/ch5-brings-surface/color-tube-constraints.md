The Bring's surface constraints take the following form in color tube coordinates.

**Spacetime recovery.**
Substituting into $z = S/D$
(equation [$z = S/D$](#eq:z-from-SD)) yields $z(\chi_\zeta(c) - z) = p_1(c) + 4z$,
which rearranges to

```tex
\begin{equation}\label{eq:spacetime-recovery}
  z^2 - (\chi_\zeta(c) - 4)\,z + p_1(c) \;=\; 0.
\end{equation}
```

Thus the spacetime coordinate $z$ is determined implicitly by the
shifted data $(p_1(c), \chi_\zeta(c))$.

**Shifted quadric.**
Substituting $w_k = c_k + z$ into the quadric gives

```tex
\begin{equation}\label{eq:shifted-quadric}
  h_2(c) + z\,p_1(c) + 2z^2 \;=\; 0,
\end{equation}
```

or equivalently $\sigma b + rg = -z(\sigma + r + g + b) - 2z^2$.

**Shifted cubic.**
Substituting $w_k = c_k + z$ into the cubic gives

```tex
\begin{equation}\label{eq:shifted-cubic}
  h_3(c) + z(p_1(c)^2 - 2h_2(c))
  + 3z^2\,p_1(c) + 4z^3 \;=\; 0.
\end{equation}
```

Eliminating $h_2(c)$ via the shifted quadric yields the
*reduced cubic*:

```tex
\begin{equation}\label{eq:reduced-cubic}
  h_3(c) + z\,p_1(c)^2 + 5z^2\,p_1(c) + 8z^3 \;=\; 0.
\end{equation}
```

All three equations are polynomial over $\mathbb{Z}$ in $z, r, g, b, \sigma$;
they therefore define affine varieties over $\mathbb{Z}$ and descend
to $\mathbb{F}_\mathfrak{p}$ for every prime $\mathfrak{p} \ne 5$.
