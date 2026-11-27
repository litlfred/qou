**Proposition (conditional on [Quarks as Borromean-linked unknots in the exceptional divisor](#conj:borromean-quark)).**

The 1-d Hecke irreps use the universal closed form in [Universal closed form for 1-d Hecke irrep characters](#prop:hecke-1d-irrep-closed-form-character). The 2-d irrep $V_{(2,1)}$ of $H_3(q)$ requires the **Hoefsmit seminormal action**:

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

For a typed braid $\beta$ on $V_{(2,1)}$, the posited Markov-traced character symmetrizes over two conjugate eigenphases $\{e^{+i\alpha}, e^{-i\alpha}\}$ of the single-wrap transfer operator:

$$
  \alpha \;=\; \frac{(z - 1) \, h}{2}, \qquad z = \frac{q^3}{q^2 + 1}, \quad h = q - q^{-1}.
$$

Under this eigenphase ansatz, the symmetrized character evaluates to $\chi^{(2,1),\mathrm{symm}}_q = \mathrm{tr}\,\rho_{(2,1)}(\beta) \cdot \cos\alpha$. (Because $z(q^{-1}) = \bigl(q(q^2 + 1)\bigr)^{-1} = z(q) - h \neq z(q)$, the phase $\alpha$ is not odd under $q \mapsto q^{-1}$, so the cosine factor enters as a conditional ansatz rather than a consequence of bar symmetry alone.)

At single wrap, for any $\beta \in B_n$ with writhe $w$ and averaged-count $m$, the full Markov trace decomposes under this ansatz as:

$$
\boxed{
  \mathrm{tr}_M(\beta) \;=\; y_{(n)} \cdot \chi^{(n)}_q(\beta) \;+\; \sum_{\substack{\lambda \vdash n \\ \dim V_\lambda \geq 2}} y_\lambda \cdot \chi^{\lambda,\mathrm{symm}}_q(\beta) \;+\; y_{(1^n)} \cdot \chi^{(1^n)}_q(\beta),
}
$$

with $y_{(1^3)} = 0$ identically at $n = 3$ for $z = q^3/(q^2 + 1)$. For $H_3$, $V_{(2,1)}$ is the unique $2$-dimensional irreducible representation; for $H_5$ and beyond, higher-rank Hook and two-row modules enter analogously.

At $q_0$, the Hoefsmit $V_{(2,1)}$ matrix entries yield $\Delta \chi^{(2,1)}_q = +0.1068144700$. Because $|\cos\alpha| \leq 1$, dressing the $z = q^3/(q^2 + 1)$ free-neutron difference base ($\mathfrak{Q}_\beta \approx 0.4491\;\text{MeV}$) by $\cos\alpha$ acts as a contraction and does not close the residual against CODATA ($0.7823\;\text{MeV}$); the retired $305\;\text{ppm}$ match combined the superseded $z = 1$ Form-A base with the half-argument phase weight $1/(\sqrt{q} + 1/\sqrt{q})$ and does not carry over to $z = q^3/(q^2 + 1)$.
