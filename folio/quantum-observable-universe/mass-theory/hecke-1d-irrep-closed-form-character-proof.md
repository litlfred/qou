## Proof.

A 1-dimensional irrep $V_\lambda$ of $H_n(q)$ is determined by the
generator-image scalar $\rho_\lambda(\sigma_i) = \lambda_\sigma$,
which by the Iwahori-Hecke relation
$(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ must satisfy
$\lambda_\sigma \in \{+q,\, -q^{-1}\}$.  The two choices give the
trivial and sign 1-d irreps respectively (per
`prop:hecke-branching-trace-decomposition`).

For a typed braid $\beta = c_1 c_2 \cdots c_L$ with crossings
$c_\ell \in \{\sigma_i,\, \sigma_i^{-1},\, \sigma_i - h/2\}$, the
1-d action is multiplicative:

$$
  \rho_\lambda(\beta) \;=\; \prod_{\ell=1}^{L} \rho_\lambda(c_\ell),
$$

with the three crossing types contributing:

$$
\begin{aligned}
  \rho_\lambda(\sigma_i)              &= \lambda_\sigma, \\
  \rho_\lambda(\sigma_i^{-1})         &= \lambda_\sigma^{-1}, \\
  \rho_\lambda(\sigma_i - \tfrac{h}{2}\mathbf{1})
                                       &= \lambda_\sigma - \tfrac{h}{2}.
\end{aligned}
$$

Hence

$$
  \rho_\lambda(\beta)
   \;=\;
   \lambda_\sigma^{w(\beta)} \cdot
   \bigl(\lambda_\sigma - \tfrac{h}{2}\bigr)^{m(\beta)} .
$$

The $q$-character $\chi^\lambda_q(\beta) = \mathrm{tr}_{V_\lambda} \rho_\lambda(\beta) = \rho_\lambda(\beta)$
(trace on 1-d space).  Substituting $\lambda_\sigma = +q$ and using
$q - h/2 = q - (q - q^{-1})/2 = (q + q^{-1})/2 = [2]_q/2$:

$$
  \chi^{(n)}_q(\beta) \;=\; q^{w(\beta)} \cdot \bigl(\tfrac{[2]_q}{2}\bigr)^{m(\beta)}.
$$

Similarly $\lambda_\sigma = -q^{-1}$ gives $-q^{-1} - h/2 = -[2]_q/2$, so

$$
  \chi^{(1^n)}_q(\beta) \;=\; (-q^{-1})^{w(\beta)} \cdot \bigl(-\tfrac{[2]_q}{2}\bigr)^{m(\beta)}.
$$

The formulas hold for every $n$ because the 1-d Hecke irreps' generator
eigenvalues $\pm q^{\pm 1}$ are *substrate-derived* — they come from the
Hecke quadratic relation, not from any $n$-specific representation
combinatorics. $\blacksquare$

## Verification

Bit-exact at 50 dps for all atoms in $\{p, n, D, T, {}^{3}\mathrm{He}\}$
($n \in \{3, 5, 8\}$):
[`q-beta-1d-irrep-universal-closed-form.witness.json`](../../computations/q-beta-1d-irrep-universal-closed-form.witness.json).

## Role in the τ_M decomposition

The full Markov trace at any $n$ decomposes as

$$
  \mathrm{tr}_M(\beta)
   \;=\;
   y_{(n)} \cdot \chi^{(n)}_q(\beta)
   \;+\;
   \sum_{\substack{\lambda \vdash n \\ \dim V_\lambda \geq 2}}
     y_\lambda \cdot \chi^\lambda_q(\beta)
   \;+\;
   y_{(1^n)} \cdot \chi^{(1^n)}_q(\beta),
$$

where the **1-d backbone**
($y_{(n)} \chi^{(n)} + y_{(1^n)} \chi^{(1^n)}$) is fully closed-form
substrate-derivable for any $n$ via the formulas above, and the
$\dim \geq 2$ middle terms require the Hoefsmit seminormal matrix
characters (per `prop:hecke-branching-trace-decomposition`)
plus, for $\dim = 2$ irreps, the cos-resummation from
[$\mathfrak{Q}_\beta$ cos-resummation in convention D](#prop:q-beta-cos-resummation).

## Recursion to higher $n$

For $n \geq 4$ the trivial and sign irreps remain 1-dimensional with the
same generator eigenvalues, so this closed form extends without
modification to ${}^{4}$He ($H_{12}$), ${}^{6}$Li ($H_{18}$), and all heavier
isotopes.  Higher-dimensional irreps grow combinatorially (per
Robinson-Schensted), but their contribution to the 1-d backbone of
$\mathrm{tr}_M$ is captured by exactly the same closed forms — only the
$y_\lambda$ weights and the Hoefsmit matrices of the $\dim \geq 2$
blocks change with $n$.

The entire
1-d slice of the Wedderburn decomposition of $\mathrm{tr}_M$ is therefore a finite
closed-form expression in $(q, w, m)$, with **no $n$-dependence in
the formula** beyond the choice of trivial-vs-sign irrep.
