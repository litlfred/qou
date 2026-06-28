**Proposition.**
*Every per-partition contribution to the binding energy is the
LP-dual shadow price of that partition's Frobenius positivity
constraint, multiplied by its $q$-hook product and accumulated
step by step from $A = 1$ over the per-step (Young seminormal)
trace of the NF transition.  No special-case branching is
required for any value of $A$.*

*The unified accumulator is, for any partition $\lambda \vdash k$
($k = 2, \ldots, K$):*

$$
  B_\lambda(Z, N)
  = m_e \cdot H_q(\lambda) \cdot u_\lambda \cdot
    \big( \ln\big| \mathrm{tr}\, \mathbf{M}_\lambda^{(0..A)} \big|
          - \ln d_\lambda \big),
$$

*and the total unified correction is the sum:*

$$
  B_{\mathrm{unified}}(Z, N) = \sum_{\lambda} B_\lambda(Z, N).
$$

*Components:*
- *$H_q(\lambda) = \prod_{x \in \lambda} [h_x(\lambda)]_q$ is the
  $q$-hook product (the categorical scale $C_\lambda = m_e \cdot
  H_q(\lambda)$ — for $\lambda = (2,2)$ this is
  $[3]_q \cdot [2]_q^2 \approx 6.29$ MeV, the empirical Wigner
  scale \cite{satula1997});*
- *$u_\lambda = w_\lambda / d_\lambda - 1/[k]_q!$ is the LP-dual
  shadow price of $\lambda$'s Frobenius positivity constraint
  ([prop:mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price));
  the constant $1/[k]_q!$ is the dual variable of the
  normalisation $\mathbf{1}^T x = n_{\mathrm{target}}$ (the
  smallest $w_\lambda / d_\lambda$ across partitions of $k$,
  attained by the trivial sym/alt one-dimensional reps);*
- *$d_\lambda = \dim(\lambda)$ is the classical dimension (number
  of standard Young tableaux);*
- *$\mathbf{M}_\lambda^{(0..A)}$ is the Young-seminormal-form
  matrix product over all NF crossings introduced through
  step $A$, embedded into the Hecke generators
  $\sigma_1, \ldots, \sigma_{k-1}$ of $H_k(R, q)$ with cyclic
  generator index.*

*One-dimensional representations have $w_\lambda / d_\lambda =
1/[k]_q!$ (so $u_\lambda = 0$); they contribute nothing to
$B_{\mathrm{unified}}$.  Only mixing partitions
($d_\lambda \geq 2$) carry shadow-price weight.*

*Per-step formulation (energy-additive, restartable witness):*

$$
  \Delta B_\lambda(\mathrm{step}\ k)
  = m_e \cdot H_q(\lambda) \cdot u_\lambda \cdot
    \Big( \ln\big| \mathrm{tr}\, \mathbf{M}_\lambda^{(0..k)} \big|
        - \ln\big| \mathrm{tr}\, \mathbf{M}_\lambda^{(0..k-1)} \big| \Big),
$$

*so witness rows
$(A, Z_k, N_k, \mathrm{nuc}, \{\Delta B_\lambda\}_\lambda,
\mathrm{cumulative})$ uniquely determine the next.*
