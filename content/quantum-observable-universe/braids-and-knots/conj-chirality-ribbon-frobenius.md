The chirality factor $a_K = 1 + w(K) \cdot h$, where $w(K)$ is the
writhe of the knot $K$ and $h = q - q^{-1}$, is derived to first
order in $h$ from the Kauffman framing formula applied to the ribbon
twist on $H_n(R, q)$
([prop:chirality-writhe-ribbon-derivation](#prop:chirality-writhe-ribbon-derivation)).
This conjecture states the exact (all-orders) form and asserts that
the first-order truncation is the correct chirality factor for all
confined knots in the model.

## Statement

**Conjecture.**
*Let $K$ be a confined knot with writhe $w(K)$ and canonical Hecke
braid element $T_w \in H_{n_0}(R, q)$.  The chirality factor of $K$
in the mass formula
([thm:knot-mass-formula-unified](#thm:knot-mass-formula-unified))
is the exact Wedderburn-weighted ribbon-twist ratio:*

$$
  a_K
  \;=\;
  \frac{
    \sum_\lambda w_\lambda(q)\, q^{2 w(K) c(\lambda)}\, \chi_\lambda(T_w)
  }{
    \sum_\lambda w_\lambda(q)\, \chi_\lambda(T_w)
  },
$$

*where:*
- *$w_\lambda(q)$ are the Wenzl-bridge Markov weights
  ([prop:alpha-k-derivation-procedure](#prop:alpha-k-derivation-procedure)),*
- *$c(\lambda) = \sum_{x \in \lambda}(\mathrm{col}(x) - \mathrm{row}(x))$
  is the total content of the Young diagram $\lambda$,*
- *$\chi_\lambda(T_w)$ is the Hecke character of $T_w$ in the
  Wedderburn summand $\lambda$.*

*Furthermore, for all nucleon and nuclear knots appearing in the QOU
model, this exact form equals $1 + w(K) \cdot h$ to the precision
required by the $0.75\%$ accuracy of the mass formula.*

## Derivation sketch

**Step 1: Ribbon twist.**  In the Hecke algebra $H_n(q)$, the ribbon
element $\theta$ acts on each irreducible $V_\lambda$ as scalar
multiplication by $\theta_\lambda = q^{c(\lambda)}$, where
$c(\lambda) = \sum_{x \in \lambda}(j(x) - i(x))$ is the
Frobenius content of $\lambda$ ($i(x)$ = row, $j(x)$ = column of
cell $x$).

**Step 2: Framing change.**  Under a $+1$ framing change
($w(K) \mapsto w(K) + 1$), the Kauffman framing formula gives:

$$
  J_K(q)\big|_{w+1}
  \;=\;
  q^{c(\mu)} \cdot J_K(q)\big|_w,
$$

where $\mu$ is the dominant representation label for the standard
colored Jones polynomial.  The factor $q^{c(\mu)}$ is exactly
$\theta_\mu$, the ribbon twist eigenvalue.

**Step 3: Full writhe.**  After $w(K)$ framing changes, each
$V_\lambda$-component picks up $q^{w(K) \cdot 2c(\lambda)}$
(squared because the twist appears twice — once for each end of
the strand that closes the braid).  The Markov trace then gives the
ratio in the conjecture statement.

**Step 4: First-order expansion.**

$$
  q^{2 w(K) c(\lambda)}
  \;=\;
  e^{2 w(K) c(\lambda) \log q}
  \;=\;
  1 + 2 w(K) c(\lambda) \log q + O(h^2).
$$

Since $\log q = \tfrac{1}{2} h + O(h^3)$ (with $q = e^{h/2}$
in the standard normalization), the leading correction is
$w(K) c(\lambda) h$.  After Markov-averaging over $\lambda$ with
weights $w_\lambda \chi_\lambda(T_w)$, the numerator gives
$1 + w(K) h \langle c(\lambda) \rangle_\beta + O(h^2)$, where
$\langle c(\lambda) \rangle_\beta$ is the Plancherel-weighted mean
content.

The conjecture splits along **chirality class**:

- **Amphichiral case (verified, 2026-05-09).** For amphichiral knots
  the writhe $w(K) = 0$ and the bar-involution / transposition
  symmetry $\chi^\lambda(T_w) = \chi^{\lambda^T}(T_w)$ combines with
  $c(\lambda^T) = -c(\lambda)$ to give
  $\langle c(\lambda) \rangle_\beta = 0$ exactly.  The chirality
  factor is then $a_K = 1 + 0 \cdot 0 \cdot h + O(h^2) = 1 + O(h^2)$,
  matching the empirical pattern $(1+h)(1-h) = 1 - h^2$ observed for
  $D, T, {}^3\mathrm{He}, {}^4\mathrm{He}$.  Numerical confirmation
  for the figure-eight knot $4_1$ at $q_0$ is recorded in
  `chirality-avg-content.witness.json`:
  $\langle c(\lambda) \rangle_{4_1} = -2.3 \times 10^{-15}$
  (numerically zero at 50-dps precision).

- **Chiral case (open).** For chiral nucleon and nuclear knots the
  conjecture asserts $\langle c(\lambda) \rangle_\beta$ takes a
  specific structural value (not zero, not necessarily one).  The
  earlier conjectured value $\langle c \rangle = 1$ was empirically
  falsified for the deuteron $^2$H ($w = +4$,
  $\langle c \rangle_\beta \in \{-3.78, +2.51\}$ depending on
  inter-nucleon-crossing convention; see falsification table at
  `chirality-writhe-ribbon-derivation.md:122–126`).  The correct
  structural form for chiral knots remains the open piece of GAP-A-2.

## Proof obligations

1. **Ribbon-twist eigenvalue.**  Verify that
   $\theta_\lambda = q^{c(\lambda)}$ in the Hecke-algebra ribbon
   structure used in the QOU model (not the quantum-group normalization,
   which may differ by a global phase).

2. **Mean-content identity (amphichiral).**  *Discharged 2026-05-09
   for the figure-eight $4_1$ via direct $H_3(R, q_0)$ computation*
   (`chirality-avg-content.witness.json`).  Generalisation to all
   amphichiral knots follows from the bar-involution symmetry
   $\chi^\lambda = \chi^{\lambda^T}$, which is structural in
   $H_n(q)$.

3. **Mean-content identity (chiral, open).**  For chiral nucleon and
   nuclear knots ($3_1$ proton, $5_2$ neutron, $6_2$ deuteron, $8_{11}$
   tritium, $L_{6a4}$ ${}^3\mathrm{He}$, etc.), determine the correct
   value of $\langle c(\lambda) \rangle_\beta$.  The earlier
   $\langle c \rangle = 1$ ansatz is falsified for $^2$H.  This is
   the residual open piece of the conjecture.

4. **$O(h^2)$ bound.**  Estimate the second-order correction
   $O(h^2)$ at $q = q_0$ and show it is $< 0.75\%$ of the leading
   term (matching the overall mass-formula accuracy).

5. **Exact formula.**  For at least one chiral knot (trefoil $3_1$ as
   the proton model), evaluate the exact formula and compare with the
   first-order result.

## Relationship to GAP-A-2

This conjecture directly addresses GAP-A-2 of the
[derivation audit report](#prose:derivation-audit-report).

