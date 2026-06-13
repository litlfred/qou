*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark) — Hoefsmit V_(2,1) Markov-symmetrized cos resummation, non-trivial Markov machinery for the 2-dimensional irrep).**

The 1-d Hecke irreps admit the universal closed form
[`prop:hecke-1d-irrep-closed-form-character`](#prop:hecke-1d-irrep-closed-form-character).
The 2-d irrep $V_{(2,1)}$ of $H_3(q)$ is the first non-trivial case
and requires the **Hoefsmit seminormal action**:

$$
  \rho_{(2,1)}(\sigma_0) \;=\; \begin{pmatrix} q & 0 \\ 0 & -q^{-1} \end{pmatrix},
  \quad
  \rho_{(2,1)}(\sigma_1) \;=\; \begin{pmatrix} d_1 & b \\ c & d_2 \end{pmatrix},
$$

where the matrix entries are Hoefsmit's standard Young tableau (SYT)
formulas:

$$
\begin{aligned}
  d_1 &= \frac{q^3}{q^2 + 1}, \qquad d_2 = -\frac{q^{-1}}{q^2 + 1}, \\
  b &= \sqrt{d_1 \cdot d_2 + 1} \quad\text{(off-diagonal coupling)}, \qquad c = b.
\end{aligned}
$$

(The off-diagonal $b^2 = d_1 d_2 + 1$ identity is the Hecke-quadratic
constraint on $\sigma_1$; the choice $c = b$ is a gauge convention.)

Both Hoefsmit matrices satisfy the **matrix-level Hecke quadratic**
$M^2 = (q - q^{-1}) \cdot M + I$:

| quantity | $\sigma_0$ (diagonal) | $\sigma_1$ (off-diagonal) |
|---|---|---|
| trace | $q - q^{-1}$ | $d_1 + d_2 = q - q^{-1}$ |
| determinant | $-1$ | $d_1 d_2 - b^2 = -1$ |
| $M^2$ | $(q-q^{-1}) M + I$ | $(q-q^{-1}) M + I$ |

The trace/determinant equalities reduce the off-diagonal matrix
identity to Cayley-Hamilton on $\mathbb{R}^{2 \times 2}$ — formalized
in `hoefsmit_sigma1_trace_eq`, `hoefsmit_sigma1_det_eq`, and
`hoefsmit_sigma1_hecke_quadratic`.

## Markov symmetrization at single wrap

For a typed braid $\beta = c_1 c_2 \cdots c_L$ on $V_{(2,1)}$, the
**Markov-traced character** symmetrizes over the two eigenphases of
$\rho_{(2,1)}$ along the braid evolution. At leading order, the
single-wrap eigenphase is

$$
  \alpha \;=\; \frac{(z - 1) \, h}{2}, \qquad
  z = \tfrac{1}{\sqrt q + 1/\sqrt q}, \quad h = q - q^{-1},
$$

per [`prop:beta-decay-transfer-matrix`](#prop:beta-decay-transfer-matrix).
The symmetrized character is

$$
  \chi^{(2,1),\mathrm{symm}}_q \;:=\;
   \tfrac{1}{2}\bigl(\mathrm{tr}\,\rho_{(2,1)}(\beta) \cdot e^{+i\alpha}
                     + \mathrm{tr}\,\rho_{(2,1)}(\beta) \cdot e^{-i\alpha}\bigr)
   \;=\; \mathrm{tr}\,\rho_{(2,1)}(\beta) \cdot \cos\alpha.
$$

In the Markov-trace context, this is exactly the form that emerges
from the cyclic constraint $\tau_M(xy) = \tau_M(yx)$ combined with
the bar involution $q \leftrightarrow q^{-1}$ — see
[`prop:q-beta-cos-resummation`](#prop:q-beta-cos-resummation).

## Closed-form decomposition (joint with 1-d closed forms)

At single wrap for any $\beta \in B_n$ encoded as a typed-crossing
list with writhe $w$ and averaged-count $m$, the full Markov trace
decomposes as

$$
\boxed{
  \tau_M(\beta)
   \;=\;
   y_{(n)} \cdot \chi^{(n)}_q(\beta)
   \;+\;
   \sum_{\substack{\lambda \vdash n \\ \dim V_\lambda \geq 2}}
     y_\lambda \cdot \chi^{\lambda,\mathrm{symm}}_q(\beta)
   \;+\;
   y_{(1^n)} \cdot \chi^{(1^n)}_q(\beta),
}
$$

with the 1-d closed forms from
[`prop:hecke-1d-irrep-closed-form-character`](#prop:hecke-1d-irrep-closed-form-character)
and the dim-2 cos symmetrization from
[`prop:q-beta-cos-resummation`](#prop:q-beta-cos-resummation).

For $H_3$ this is fully closed-form substrate-derivable (only one
2-d irrep, $V_{(2,1)}$). For $H_5$ and beyond, additional 2+-dim irreps
appear ($V_{(3,2)}, V_{(2,2,1)},$ etc.); each requires its own
Hoefsmit matrix and Markov-symmetrized cos analog.

## Empirical anchor

At $q_0$, the Hoefsmit V_(2,1) matrix entries (from
[`probe_q_beta_per_irrep_cos.py`](../../folio-assistant/computations/probe_q_beta_per_irrep_cos.py)
and the existing `hecke_characters.build_seminormal_matrices` infrastructure):

| quantity | value at $q_0$ |
|----------|---:|
| $\chi^{(2,1)}_q(\mathcal{B}_p)$ | $+1.8077033201$ |
| $\chi^{(2,1)}_q(\mathcal{B}_n)$ | $+1.7008888501$ |
| $\Delta \chi^{(2,1)}_q$   | $+0.1068144700$ |
| $y_{(2,1)} \cdot \Delta \chi^{(2,1)}_q$ | $+0.0913335577$ |
| Markov-symmetrized factor $\cos\alpha$ | $0.99863..$ |

After symmetrization the V_(2,1) contribution combines with the 1-d
contributions to give $Q_\beta = Q_\beta^A \cdot \cos((z-1)h/2)$ at
the cos-resummation level (305 ppm residual against CODATA).
