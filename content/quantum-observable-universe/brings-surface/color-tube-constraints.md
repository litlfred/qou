**Spectral form (canonical).**
In the spectral coordinates — the Lagrange resolvents $w_k$, $k \in \{0,\dots,4\}$, of [color tube coordinates](#def:color-tube-coordinates) — the Bring's surface constraints are simply the vanishing of the first three power sums,

```tex
\begin{equation}\label{eq:spectral-power-sums}
  p_1(w) =  p_2(w) =  p_3(w) =  0 .
\end{equation}
```

This is the canonical statement: it carries no $z$-dependence at all. The color tube coordinates are the *shifted* chart $c_k = w_k - z$, and every $z$-dependent term in the equations below is an artifact of that shift. Transporting [$p_m(w) = 0$](#eq:spectral-power-sums) through $w_k = c_k + z$ forces the tube-chart power sums to the closed values

$$
  p_1(c) = -5z, \qquad p_2(c) = 5z^2, \qquad p_3(c) = -5z^3,
$$

that is $p_m(c) = (-1)^m \, 5 \, z^m$. The three shift laws and this transport are machine-checked (`QOU.Mass.ColorTubeSpectralBridge`: `psum1_shift`, `psum2_shift`, `psum3_shift`, `tube_psum1_of_bring`, `tube_psum2_of_bring`, `tube_psum3_of_bring`), as is the corresponding shift for the three-variable [color tube cubic](#eq:color-tube-cubic) and its Vieta rows.

The Bring's surface constraints take the following form in color tube coordinates.

**Spacetime recovery.**
Substituting into $z = S/D$ (equation [$z = S/D$](#eq:z-from-SD)) yields $z(\chi_\zeta(c) - z) = p_1(c) + 4z$, which rearranges to

```tex
\begin{equation}\label{eq:spacetime-recovery}
  z^2 - (\chi_\zeta(c) - 4)z + p_1(c) =  0.
\end{equation}
```

Thus the shifted data $(p_1(c), \chi_\zeta(c))$ determines the spacetime coordinate $z$ implicitly.

**Shifted quadric.**
Substituting $w_k = c_k + z$ into the quadric gives

```tex
\begin{equation}\label{eq:shifted-quadric}
  h_2(c) + zp_1(c) + 2z^2 =  0,
\end{equation}
```

or equivalently $\sigma b + rg = -z(\sigma + r + g + b) - 2z^2$.

**Shifted cubic.**
Substituting $w_k = c_k + z$ into the cubic gives

```tex
\begin{equation}\label{eq:shifted-cubic}
  h_3(c) + z(p_1(c)^2 - 2h_2(c))
  + 3z^2p_1(c) + 4z^3 =  0.
\end{equation}
```

Eliminating $h_2(c)$ via the shifted quadric yields the *reduced cubic*:

```tex
\begin{equation}\label{eq:reduced-cubic}
  h_3(c) + zp_1(c)^2 + 5z^2p_1(c) + 8z^3 =  0.
\end{equation}
```

All three equations are polynomials over $\mathbb{Z}$ in $z, r, g, b, \sigma$. They define affine varieties over $\mathbb{Z}$ and descend to $\mathbb{F}_\mathfrak{p}$ for every prime $\mathfrak{p} \ne 5$.

**Commutative-limit specialisation.**
Under the weight identification of [prop:x5-bring-weight-identification](#prop:x5-bring-weight-identification), the weight-$(-1)$ Lagrange resolvent $w_1$ on Bring's surface corresponds canonically to the affine coordinate $x$ on the hyperelliptic quintic $\mathcal{X}_5 \colon y^2 = x^5 - 1$. Restricting the full $S_5$-symmetric color-tube system to its cyclic $\mathbb{Z}_5 \subset S_5$ residue isolates this single weight channel. The three color coordinates $r, g, b$ and the shift $z$ collapse to observables on the single $\mathrm{U}(1)$ phase tube of [rem:u1-phase-tube](#rem:u1-phase-tube). Evaluated along $w_2 = w_3 = w_4 = 0$, the shifted quadric and cubic reduce to the single-variable identity $x^5 - 1 = y^2$ that defines $\mathcal{X}_5$.
