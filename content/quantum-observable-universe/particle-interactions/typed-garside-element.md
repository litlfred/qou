Let $\mathcal{A}(Z, N)$ be a nucleus with $A = Z + N$ nucleons in
ordering $(t_0, \ldots, t_{A-1})$ where $t_i \in \{p, n\}$.  The
**typed Garside element** is the element
$\mathcal{G}(t_0, \ldots, t_{A-1}) \in H_A(q)$ built by the
Garside staircase with typed crossings
([typed crossing operator](#def:typed-crossing-operator)).

**Construction.**  The Garside staircase has $A - 1$ levels.
At level $\ell$ ($0 \leq \ell \leq A - 2$), strand $\ell + 1$
crosses all earlier strands $j = \ell, \ell - 1, \ldots, 0$
(right to left).  Each crossing is typed by the nucleon pair
$(t_j, t_{\ell+1})$:

```tex
\begin{equation}\label{eq:typed-garside}
  \mathcal{G}(t_0, \ldots, t_{A-1})
  \;=\;
  \prod_{\ell=0}^{A-2}
  \;\prod_{j=\ell}^{0}
  C(t_j,\, t_{\ell+1};\, \sigma_j)
\end{equation}
```

where $C(f_i, f_j; \sigma_k) = \sigma_k + d(f_i, f_j)$ is the
typed crossing operator with coefficients

$$
  d(p, p) = 0, \qquad
  d(n, n) = -(q - q^{-1}), \qquad
  d(p, n) = d(n, p) = -\tfrac{1}{2}(q - q^{-1}).
$$

The product contains $\binom{A}{2}$ factors — one for every
pair of nucleons — each at the correct generator position
$\sigma_j$ determined by the staircase sweep.  The result is
reduced to Gröbner--Shirshov normal form
([nuclear reduction](#prop:nuclear-groebner-reduction)) under
the braiding-induced ordering
([braiding-induced ordering](#prop:braiding-induced-ordering)).

**Comparison with adjacent-only construction.**
The transfer matrix chain
([transfer matrix operator](#def:transfer-matrix-operator))
computes vertex volumes $\hat{V}_i$ at each generator $\sigma_i$
by chaining the crossing coefficients with all positions $j > i$.
This captures the same pairwise crossing data as the Garside
staircase, but factored through scalar vertex volumes rather
than the full $H_A(q)$ element.

The typed Garside element retains the complete algebraic
structure: for ${}^4\mathrm{He}$ with ordering $[p, n, p, n]$,
the adjacent-only product $({\sigma_0 - h/2})({\sigma_1 - h/2})({\sigma_2 - h/2})$
gives $8$ NF terms with a spurious negative identity component
$-\frac{h^3}{8}$.  The full Garside staircase (all $6$ crossings)
gives $18$ NF terms with identity component exactly $0$, and
leading term equal to the Garside element
$\Delta_4 = \sigma_0\sigma_1\sigma_0\sigma_2\sigma_1\sigma_0$.

**Verified.**  For $A = 4$ (${}^4\mathrm{He}$, $6$ crossings):
$18$ NF terms.  For $A = 6$ (${}^6\mathrm{He}$, $15$ crossings):
$988$ NF terms.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
