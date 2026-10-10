*Under the Frobenius--Hopf antipode $S \colon \sigma \leftrightarrow
\sigma^{-1}$ on the Hecke algebra $H_n(R, q)$, the three log-functionals
in the Wedderburn mass formula
([Wedderburn mass formula](#thm:wedderburn-mass-formula)) behave as
follows: $\Phi_2$ and $\Phi_3$ carry the $S$-eigenvalues $+1$ and $-1$,
and $\Phi_1$ is not an $S$-eigenvector; only its symmetrised projection
$\Phi_1^{+} = \tfrac12(\Phi_1 + \Phi_1 \circ S)$ is $S$-even:*

See [Table 1](#tbl:frobenius-s-classification-table1-data).

*Together with the $S$-classification of every coefficient in the
formula:*

See [Table 2](#tbl:frobenius-s-classification-table2-data).

*Write $\Phi_1 = \Phi_1^{+} + \Phi_1^{-}$ with
$\Phi_1^{-} = \tfrac12(\Phi_1 - \Phi_1 \circ S)$, which is $S$-odd.
Term by term, the binding correction
$\alpha\bigl(\Phi_1 - 2[3]_q\,\Phi_2 + h_{\mathrm{A}}^2\,\Phi_3\bigr)$
decomposes as:*

```tex
\[
\begin{aligned}
\text{Term 1: } & \underbrace{1}_{+1} \cdot \bigl(\underbrace{\Phi_1^{+}}_{+1} + \underbrace{\Phi_1^{-}}_{-1}\bigr) & \text{(no $S$-eigenvalue)} \\
\text{Term 2: } & \underbrace{-2[3]_q}_{+1} \cdot \underbrace{\Phi_2}_{+1} = +1 & \text{($S$-even)} \\
\text{Term 3: } & \underbrace{h_{\mathrm{A}}^2}_{+1} \cdot \underbrace{\Phi_3}_{-1} = -1 & \text{($S$-odd)}
\end{aligned}
\]
```

*The $S$-odd part of the mass has two channels, $\Phi_1^{-}$ and the
chirality term $h_{\mathrm{A}}^2 \Phi_3$:*

$$
  \mathfrak{m}(S(\beta)) - \mathfrak{m}(\beta)
  = -2\alpha\bigl(\Phi_1^{-}(\beta) + h_{\mathrm{A}}^2\,\Phi_3(\beta)\bigr).
$$

*The chirality term is the only $S$-odd channel exactly when
$\alpha\,\Phi_1^{-}(\beta) = 0$, which does not hold in general.
Consequently, any $S$-symmetric ansatz for the binding correction
(such as the 2-term $\alpha$-blend
$\alpha V_{\mathrm{Frob}} + (1-\alpha) V_{\det}$, when both summands are
$S$-invariant) has vanishing $S$-difference, and reproduces the
$S$-difference of the mass only where the two channels cancel,
$\Phi_1^{-}(\beta) + h_{\mathrm{A}}^2\,\Phi_3(\beta) = 0$, regardless of
the mixing parameter.*
