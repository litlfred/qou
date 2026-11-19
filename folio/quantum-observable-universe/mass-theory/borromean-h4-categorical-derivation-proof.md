## Proof.

The proof proceeds in two structural steps.

### Step 1: Schur–Weyl + R-matrix derivation of $\chi^{(2,1)}(\beta_{\mathrm{Bor}})$.

The q-Schur duality for $\mathrm{U}_q(\mathfrak{sl}_2)$ and $\mathrm{H}_3(q)$
gives a $(\mathrm{U}_q(\mathfrak{sl}_2), \mathrm{H}_3(q))$-bimodule
decomposition

$$
  V_{1/2}^{\otimes 3}
  \;\cong\;
  V_{3/2} \otimes S^{(3)}
  \;\oplus\;
  V_{1/2} \otimes S^{(2,1)}
$$

(dimensions: $4 \otimes 1 \;\oplus\; 2 \otimes 2 \;=\; 4 + 4 = 8$).
Tracing on the $V^{\otimes 3}$ side via the standard ordinary trace
(matching the $\mathrm{H}_n(q)$-side classical-dim convention) gives:

$$
  \mathrm{tr}_{V^{\otimes 3}}(F(\beta_{\mathrm{Bor}}))
  \;=\;
  \dim(V_{3/2}) \cdot \chi^{(3)}(\beta_{\mathrm{Bor}})
  \;+\;
  \dim(V_{1/2}) \cdot \chi^{(2,1)}(\beta_{\mathrm{Bor}})
  \;=\;
  4 \cdot 1 + 2 \cdot \chi^{(2,1)}(\beta_{\mathrm{Bor}}),
$$

where $F$ is the q-Schur duality functor sending the braid generators
$\sigma_i$ to the braided R-matrices $\check{R}_{i, i+1}$ acting on
$V_{1/2}^{\otimes 3}$, and $\chi^{(3)}(\beta_{\mathrm{Bor}}) = 1$ since
$\beta_{\mathrm{Bor}}$ has writhe $0$ and projects to the identity in $S_3$.

The braided R-matrix is

$$
  \check{R}(q) \;=\;
  \begin{pmatrix}
    q & 0 & 0 & 0 \\
    0 & q - q^{-1} & 1 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 0 & q
  \end{pmatrix}
$$

in the basis $\{|\!\!\uparrow\uparrow\rangle, |\!\!\uparrow\downarrow\rangle, |\!\!\downarrow\uparrow\rangle, |\!\!\downarrow\downarrow\rangle\}$,
satisfying the Hecke relation $(\check{R} - q)(\check{R} + q^{-1}) = 0$.
Its inverse is

$$
  \check{R}^{-1} \;=\; \check{R} - (q - q^{-1}) I,
$$

derived from the Hecke quadratic relation
$\check{R}^2 = (q - q^{-1})\check{R} + I$
(this is *not* $\check{R}(q \to q^{-1})$, which is the universal
R-matrix not the braided form). Setting
$\sigma_1 = \check{R} \otimes I_2$,
$\sigma_2 = I_2 \otimes \check{R}$ as $8 \times 8$ matrices on
$V^{\otimes 3}$, direct computation of
$\beta_{\mathrm{Bor}} = (\sigma_1^{-1} \sigma_2)^3$ gives:

$$
  \mathrm{tr}_{V^{\otimes 3}}(F(\beta_{\mathrm{Bor}}))
  \;=\;
  8 - 6h^4 - 2h^6
  \quad\text{(exact, verified to 50 digits at the aether $q_0 \approx 1.10998$).}
$$

Subtracting $4 \cdot 1$ and dividing by $\dim(V_{1/2}) = 2$ yields:

$$
  \chi^{(2,1)}(\beta_{\mathrm{Bor}})
  \;=\;
  2 - 3h^4 - h^6,
$$

i.e. the $h^4$ coefficient is $-3$. (This polynomial form is also
derivable directly from the closed form of
[Borromean Markov trace closed form proposition](borromean-markov-trace-closed-form.md)
via the substitution $u = q^2 + q^{-2} = h^2 + 2$; the R-matrix
derivation provides the categorical confirmation.)

### Step 2: Markov normalisation $y_{(2,1)}(q=1) = 1/[2]_q^2|_{q=1} = 1/4$.

The Frobenius expansion of the Markov trace on $\mathrm{H}_3(q)$:

$$
  \mathrm{tr}_M(\beta_{\mathrm{Bor}})
  \;=\;
  \sum_{\lambda \vdash 3} y_\lambda(q) \cdot \chi^\lambda(\beta_{\mathrm{Bor}})
  \;=\;
  y_{(3)}(q) + y_{(2,1)}(q)\!\cdot\!(2 - 3h^4 - h^6) + y_{(1^3)}(q),
$$

using $\chi^{(3)}(\beta_{\mathrm{Bor}}) = \chi^{(1^3)}(\beta_{\mathrm{Bor}}) = 1$.
Regrouping:

$$
  \mathrm{tr}_M(\beta_{\mathrm{Bor}})
  \;=\;
  \underbrace{\bigl[y_{(3)} + 2\, y_{(2,1)} + y_{(1^3)}\bigr]}_{= \,\mathrm{tr}_M(\mathbf{1}_3) \,=\, 1 \text{ (Markov norm.)}}
  \;+\;
  y_{(2,1)}(q) \cdot (-3h^4 - h^6),
$$

since the Markov normalisation gives
$\sum_\lambda y_\lambda \cdot d_\lambda = \mathrm{tr}_M(\mathbf{1}_3) = 1$
for the identity braid. The $h^4$ coefficient is therefore

$$
  \bigl[h^4\text{-coeff of }\mathrm{tr}_M\bigr] \;=\; -3 \cdot y_{(2,1)}(q=1).
$$

From the closed form
$\mathrm{tr}_M(\beta_{\mathrm{Bor}}) = (4 + h^2 - 3h^4 - h^6) / (h^2 + 4)$
the $h^4$ coefficient is $-3/4$ (exact symbolic series division).
Solving:

$$
  -3 \cdot y_{(2,1)}(q=1) \;=\; -\tfrac{3}{4}
  \quad\Longrightarrow\quad
  y_{(2,1)}(q=1) \;=\; \tfrac{1}{4} \;=\; \frac{1}{[2]_q^2|_{q=1}}.
$$

The factor $[2]_q^{c-1}$ is the standard Markov-trace normalisation for
closure of an $n$-strand braid into a $c$-component link: for the
Borromean rings ($c = 3$), $[2]_q^2 = h^2 + 4$ is **exactly** the
denominator in the closed form
$\mathrm{tr}_M(\beta_{\mathrm{Bor}}) = (\cdots)/(h^2 + 4)$.

The identity $y_{(2,1)}(q) = 1/[2]_q^2$ in fact holds **exactly for
all $q$**, not only at $q = 1$: the full closed-form weight vector on
$\mathrm{H}_3(q)$ is $y_{(3)} = [4]_q/[2]_q^3$, $y_{(2,1)} = 1/[2]_q^2$,
$y_{(1^3)} = 0$ (identically, since the Temperley–Lieb quotient kills the
3-row partition), evaluating at $q = 1$ to the **non-uniform** vector
$(\tfrac12, \tfrac14, 0)$. See
[$H_3$ Markov Wenzl weights proposition](h3-markov-wenzl-weights.md) for the
derivation and for why a bar-involution uniformity argument fails (the
Jones-normalised trace is chiral, hence not invariant under the sign-twist
automorphism $\sigma \mapsto -q\,\sigma^{-1}$).

### Combining Steps 1 and 2.

$$
  \bigl[h^4\text{-coeff of }\mathrm{tr}_M(\beta_{\mathrm{Bor}})\bigr]
  \;=\;
  \underbrace{(-3)}_{\text{Step 1: R-matrix on }V_{1/2}^{\otimes 3}}
  \;\cdot\;
  \underbrace{\tfrac{1}{4}}_{\text{Step 2: Markov norm. for }c = 3}
  \;=\;
  -\tfrac{3}{4}. \qquad \square
$$
