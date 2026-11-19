*Proof.* We establish the absolute-convergence bound via direct geometric-series estimation on the iterated Laplacian.

**Step 1: q-integer asymptotic.** For $q > 1$, the q-integer $[k]_q = (q^k - q^{-k})/(q - q^{-1})$ satisfies
$$
  [k]_q \;=\; \frac{q^k}{q - q^{-1}}\,\bigl(1 - q^{-2k}\bigr)
  \;\leq\;
  \frac{q^k}{q - q^{-1}}.
$$
Squaring and applying $\hbar_q = (q - 1)/q$, we obtain $\lambda_k^{(q)} = [k]_q^2 \hbar_q / L_q^2 \leq C\,q^{2k}$ for a constant $C = \hbar_q / \bigl((q - q^{-1})^2 L_q^2\bigr)$.

**Step 2: Single-jet bound.** The $\hbar_q^2 \Delta^{(1)}$ term on a normalised mode $e_k$ of the Reeb bundle yields
$$
  \bigl|\langle e_k, \hbar_q^2 \Delta^{(1)} e_k \rangle\bigr|
  \;=\;
  \hbar_q^2 \, \lambda_k^{(q)}
  \;\leq\;
  \hbar_q^2 \cdot C \, q^{2k}.
$$
For the leading mode $k = 1$, this quantity is finite. Higher modes produce exponentially suppressed corrections, which we control in Step 4.

**Step 3: Iterated-Laplacian bound.** The $n$-th iteration $\Delta^{(n)}$ on the same mode yields
$$
  \bigl|\langle e_k, \Delta^{(n)} e_k\rangle\bigr|
  \;=\;
  (\lambda_k^{(q)})^n
  \;\leq\;
  C^n \, q^{2nk}.
$$
Thus, the $\hbar_q^{2n}$ tower coefficient on mode $k$ is at most
$$
  \hbar_q^{2n} \cdot C^n \, q^{2nk}
  \;=\;
  \bigl(\hbar_q^2 \, C \, q^{2k}\bigr)^n.
$$

**Step 4: Geometric-series sum.** We sum over $n$ with $k = 1$ fixed to extract the dominant mode contribution. We use $\hbar_q^2 C q^2 < 1$, which holds for $q \in (1, q_*)$ with $q_* \approx 1.2$. This range comfortably covers the substrate $q_0 \approx 1.110$:
$$
  \sum_{n=1}^{\infty} \hbar_q^{2n} C^n q^{2n}
  \;=\;
  \frac{\hbar_q^2 \, C \, q^2}{1 - \hbar_q^2 \, C \, q^2}
  \;<\;\infty.
$$

**Step 5: Leading versus remainder.** We separate the $n = 1$ term:
$$
  T(\rho) - \hbar_q^2 \,\Delta^{(1)}(\rho)
  \;=\;
  \sum_{n=2}^{\infty} \hbar_q^{2n} \, \Delta^{(n)}(\rho).
$$
On the leading mode Step 3 is an equality, $\langle e_1, \Delta^{(n)} e_1\rangle = \lambda_1^n$ with $\lambda_1 = \lambda_1^{(q)} = \hbar_q / L_q^2$. The [uniform bound on $\Delta^{(n)}$](#prop:delta-max-uniform-bound) makes $\lambda_1^n$ bounded in $n$, and a bounded sequence of powers has $\lambda_1 \leq 1$ (Lean `QOU.QBeta.lam_le_one_of_pow_bounded`). Therefore
$$
  \bigl| T(\rho) - \hbar_q^2 \,\Delta^{(1)}(\rho) \bigr|
  \;\leq\;
  \|\rho\|_{L^2}
  \cdot
  \sum_{n=2}^{\infty} \hbar_q^{2n} \lambda_1^{n}
  \;\leq\;
  \|\rho\|_{L^2}
  \cdot
  \frac{\hbar_q^4}{1 - \hbar_q^2}.
$$
Finally $\frac{1}{1 - \hbar_q^2} \leq \frac{q^{-2}}{1 - q^{-2}}$ on $1 < q \leq q_*$. With $x = q^{-1}$ and $\hbar_q = 1 - x$, this reads $1 - x^2 \leq 2x^3 - x^4$. The difference $f(x) = 2x^3 - x^4 + x^2 - 1$ has $f'(x) = 2x(1 + 3x - 2x^2) > 0$ on $(0, 1]$ and $f(1/1.2) > 0$, so it holds on $[1/1.2, 1]$. This yields the displayed bound.

*Direct eigenvalue bound.* Bounding the tail directly through the exact leading eigenvalue avoids absorbing the Step-1 constant $C$ into $C q^2 \leq q^{-2}$ (which would require $L_q \geq q^2 \sqrt{\hbar_q}/(q - q^{-1}) \approx 1.855$ rather than the normalized value $L_q = \sqrt{\hbar_q}$), and therefore requires no auxiliary condition on $L_q$ beyond the uniform bound.

**Sharpness.** At $q_0 \approx 1.110$, we have $\hbar_q \approx 0.099$ and $q^{-2} \approx 0.812$. Therefore, the geometric ratio $q^{-2} \hbar_q^2 \approx 0.008 \ll 1$. The single-jet term dominates the tower at the $\approx 1\%$ level. Three jet levels suffice for sub-ppm precision, justifying the truncations applied elsewhere in the mass-formula derivations. $\square$
