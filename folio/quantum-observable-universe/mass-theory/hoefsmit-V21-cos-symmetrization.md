**Proposition (conditional on [Borromean quark conjecture](#conj:borromean-quark)).**

The 1-d Hecke irreps use the universal closed form in [Hecke one-dimensional irreducible-representation closed form character proposition](#prop:hecke-1d-irrep-closed-form-character). The 2-d irrep $V_{(2,1)}$ of $H_3(q)$ requires the **Hoefsmit seminormal action**:

$$
  \rho_{(2,1)}(\sigma_0) \;=\; \begin{pmatrix} q & 0 \\ 0 & -q^{-1} \end{pmatrix},
  \quad
  \rho_{(2,1)}(\sigma_1) \;=\; \begin{pmatrix} d_1 & b \\ c & d_2 \end{pmatrix},
$$

where the matrix entries derive from Hoefsmit's standard Young tableau formulas:

$$
  d_1 = \frac{q^3}{q^2 + 1}, \qquad d_2 = -\frac{q^{-1}}{q^2 + 1}, \qquad b = c = \sqrt{d_1 \cdot d_2 + 1}.
$$

Both matrices satisfy the matrix-level Hecke quadratic $M^2 = (q - q^{-1}) \cdot M + I$. The trace equals $q - q^{-1}$ and the determinant equals $-1$. Cayley-Hamilton on $\mathbb{R}^{2 \times 2}$ verifies the off-diagonal identity.

For a typed braid $\beta$ on $V_{(2,1)}$, the Markov-traced character symmetrizes over the two eigenphases of $\rho_{(2,1)}$. At leading order, the single-wrap eigenphase is

$$
  \alpha \;=\; \frac{(z - 1) \, h}{2}, \qquad z = \tfrac{1}{\sqrt q + 1/\sqrt q}, \quad h = q - q^{-1}.
$$

The symmetrized character evaluates to $\chi^{(2,1),\mathrm{symm}}_q = \mathrm{tr}\,\rho_{(2,1)}(\beta) \cdot \cos\alpha$. This cos-resummation arises from the cyclic constraint $\mathrm{tr}_M(xy) = \mathrm{tr}_M(yx)$ combined with the bar involution.

At single wrap, for any $\beta \in B_n$ with writhe $w$ and averaged-count $m$, the full Markov trace decomposes as:

$$
\boxed{
  \mathrm{tr}_M(\beta) \;=\; y_{(n)} \cdot \chi^{(n)}_q(\beta) \;+\; \sum_{\substack{\lambda \vdash n \\ \dim V_\lambda \geq 2}} y_\lambda \cdot \chi^{\lambda,\mathrm{symm}}_q(\beta) \;+\; y_{(1^n)} \cdot \chi^{(1^n)}_q(\beta).
}
$$

For $H_3$, $V_{(2,1)}$ is the only 2-d irrep. For $H_5$ and beyond, additional irreps appear, each requiring its Hoefsmit matrix and Markov-symmetrized cos analog.

At $q_0$, the Hoefsmit $V_{(2,1)}$ matrix entries yield $\Delta \chi^{(2,1)}_q = +0.1068144700$. The symmetrized contribution combines with the 1-d forms to give $\mathfrak{Q}_\beta = \mathfrak{Q}_\beta^A \cdot \cos((z-1)h/2)$, matching CODATA to 305 ppm at the cos-resummation level.
