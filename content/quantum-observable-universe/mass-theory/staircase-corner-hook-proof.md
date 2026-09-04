**Proof.**
*The corner cell $(0, 0)$ has arm length $k - 1$ (the row $0$ of
$\rho_k$ has $k$ cells, so $k - 1$ cells lie strictly to the right
of the corner) and leg length $k - 1$ (the column $0$ has $k$
cells, so $k - 1$ cells lie strictly below the corner).
Adding the corner cell itself gives
$h_{\mathrm{corner}}(\rho_k) = (k-1) + (k-1) + 1 = 2k - 1$. $\square$*

This combinatorial identity makes the exponent of the
[staircase EW-residual conjecture](#conj:staircase-ew-residual)
*available*: the observed pairwise eigenvalue ratio
$q^{1/h_{\mathrm{corner}}(\rho_k)}$ in the spectrum of
$\beta_{\mathrm{EW}} \, \bowtie_K^{\mathrm{minimal}}$ on
$V_{\rho_k}$ matches this corner hook as the inverse exponent.
For $k = 3$ that is the $q^{1/5}$ factor which takes the
cot $\theta_W$ gap from $2.19\%$ to $0.13\%$; for $k = 4$ it is
the $q^{1/7}$ scale reported at relative error $0.14\%$ in the
dim-$768$ spectrum.

**Availability is not derivation, and the identity above supplies
only the former.** The exponent was chosen as the closest of an
enumerated candidate sweep which ranged well beyond the hook
lengths, so a hook expression existing for the winner is a
property of the hook lengths rather than evidence about the
spectrum. Neither figure is a framework accuracy result. Two
further facts bear on how far the identity can be carried: the
$k = 4$ prediction was not testable as stated, the top eigenvalue
there being degenerate; and $\rho_k$ has $k$ rows, so by the
Schur–Weyl row cap every $k \geq 3$ names a block with no states
at the framework's fibre dimension $N = 2$. The identity
$h_{\mathrm{corner}}(\rho_k) = 2k-1$ is a theorem about the
diagram and stands on its own.
