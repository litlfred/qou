**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark) — 1-dimensional Hecke irrep character, universal closed form).**

For any $n \geq 2$ and any typed braid $\beta \in B_n$ encoded as a
sequence of crossings of three types
$\{\sigma_i,\, \sigma_i^{-1},\, \sigma_i - h/2\cdot\mathbf{1}\}$
(the `operator-valued interface`
with $h = q - q^{-1}$), the $q$-character on each 1-dimensional
irreducible representation of $H_n(q)$ is given by the **universal
closed form**

$$
\boxed{
  \chi^{(n)}_q(\beta)
   \;=\;
   q^{w(\beta)} \cdot \bigl(\tfrac{[2]_q}{2}\bigr)^{m(\beta)}
  \qquad\text{and}\qquad
  \chi^{(1^n)}_q(\beta)
   \;=\;
   \bigl(-q^{-1}\bigr)^{w(\beta)} \cdot \bigl(-\tfrac{[2]_q}{2}\bigr)^{m(\beta)},
}
$$

where:

- $w(\beta) = \#(\sigma_i) - \#(\sigma_i^{-1})$ is the **writhe**
  (signed crossing count of the typed braid),
- $m(\beta)$ is the number of **averaged** (operator-valued
  $\sigma_i - h/2$) crossings,
- $[2]_q = q + q^{-1}$ is the standard quantum integer (so
  $[2]_q / 2 = (q + q^{-1})/2$ is the q-half-integer).

**The closed form is independent of $n$.** Only the choice of which
1-d irrep ($V_{(n)}$ trivial or $V_{(1^n)}$ sign) toggles the
sign of the eigenvalue $\lambda_\sigma \in \{+q,\, -q^{-1}\}$.

## Verification

Bit-exact at 50 dps for all atoms in $\{p, n, D, T, {}^{3}\mathrm{He}\}$
($n \in \{3, 5, 8\}$):
[`q-beta-1d-irrep-universal-closed-form.witness.json`](../../computations/q-beta-1d-irrep-universal-closed-form.witness.json).

## Role in the τ_M decomposition

The full Markov trace at any $n$ decomposes as

$$
  \tau_M(\beta)
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
[`prop:q-beta-cos-resummation`](#prop:q-beta-cos-resummation).

## Recursion to higher $n$

For $n \geq 4$ the trivial and sign irreps remain 1-dimensional with the
same generator eigenvalues, so this closed form extends without
modification to ${}^{4}$He ($H_{12}$), ${}^{6}$Li ($H_{18}$), and all heavier
isotopes.  Higher-dimensional irreps grow combinatorially (per
Robinson-Schensted), but their contribution to the 1-d backbone of
$\tau_M$ is captured by exactly the same closed forms — only the
$y_\lambda$ weights and the Hoefsmit matrices of the $\dim \geq 2$
blocks change with $n$.

This is a substantive **substrate-derivability result**: the entire
1-d slice of the Wedderburn decomposition of $\tau_M$ is a finite
closed-form expression in $(q, w, m)$, with **no $n$-dependence in
the formula** beyond the choice of trivial-vs-sign irrep.
