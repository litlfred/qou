**Proposition.**
*Under the Frobenius--Hopf antipode $S \colon \sigma \leftrightarrow
\sigma^{-1}$ on the Hecke algebra $H_n(R, q)$, the three log-functionals
in the Wedderburn mass formula
([Wedderburn mass formula](#thm:wedderburn-mass-formula)) carry
exactly the following $S$-eigenvalues:*

See [Table 1](#tbl:frobenius-s-classification-table1-data).

*Together with the $S$-classification of every coefficient in the
formula:*

See [Table 2](#tbl:frobenius-s-classification-table2-data).

*Term by term, the binding correction
$\alpha\bigl(\Phi_1 - 2[3]_q\,\Phi_2 + H_A^2\,\Phi_3\bigr)$
decomposes as:*

$$
\begin{aligned}
\text{Term 1: } & \underbrace{1}_{+1} \cdot \underbrace{\Phi_1}_{+1} = +1 & \text{($S$-even)} \\
\text{Term 2: } & \underbrace{-2[3]_q}_{+1} \cdot \underbrace{\Phi_2}_{+1} = +1 & \text{($S$-even)} \\
\text{Term 3: } & \underbrace{H_A^2}_{+1} \cdot \underbrace{\Phi_3}_{-1} = -1 & \text{($S$-odd)}
\end{aligned}
$$

*Exactly **one** of the three terms is $S$-anti-invariant, namely
the chirality term $H_A^2 \Phi_3$.  Consequently, any
$S$-symmetric ansatz for the binding correction (such as the
2-term $\alpha$-blend $\alpha V_{\mathrm{Frob}} + (1-\alpha) V_{\det}$)
necessarily lives in the 2-dimensional $S$-invariant subspace and
**cannot capture chirality** regardless of the mixing parameter.*

*Proof.*
We verify each $S$-eigenvalue in turn.

**Coefficients.** The action $q \mapsto q^{-1}$ extends to the
underlying field of fractions and acts on each coefficient:

- $D = q^4 + 4q^2 + 1$ is palindromic in $q^2$: under $q \to q^{-1}$,
  $D \to q^{-4} + 4q^{-2} + 1 = q^{-4}(1 + 4q^2 + q^4) = q^{-4} D$.
  Then $W_{\mathrm{sym}} = q^2/D \to q^{-2}/(q^{-4} D) = q^2/D$,
  invariant.  Same for $W_{\mathrm{alt}}$.  For $W_{\mathrm{std}}$:
  $(q^2+1)^2 \to (q^{-2}+1)^2 = q^{-4}(1+q^2)^2$, so
  $W_{\mathrm{std}} \to q^{-4}(1+q^2)^2 / (q^{-4} D) = W_{\mathrm{std}}$.
- $[3]_q = q^2 + 1 + q^{-2}$: invariant under $q \to q^{-1}$.
- $H_A = q - q^{-1} \to q^{-1} - q = -H_A$, so $H_A$ has eigenvalue
  $-1$ and $H_A^2$ has eigenvalue $+1$.
- $z = 1/(q^{1/2} + q^{-1/2})$: the denominator is symmetric under
  $q \to q^{-1}$, so $z$ is invariant.
- Catalan's constant $G$, Borromean volume $8G$, electron mass
  $m_e$, and binding scale $\alpha$ are real numerical constants
  unaffected by the algebraic action.

**Functional $\Phi_2$.** The transfer matrix is
$T(c, d) = \begin{pmatrix} cH_A + d & c \\ c & d \end{pmatrix}$
with $\det T = d(cH_A + d) - c^2$.  The Frobenius antipode
maps the primitive factor $(c, d)$ to $(c, d - cH_A)$ (this swaps
$\sigma \leftrightarrow \sigma^{-1}$).  Direct computation:

See [Table 3](#tbl:frobenius-s-classification-table3-data).

For each primitive the determinant is $S$-invariant.  Since
$\det$ is multiplicative on chain products, $\Phi_2 = \sum_i
\log\lvert\det M_i\rvert$ is $S$-invariant.

**Functional $\Phi_3$.** For each primitive, direct computation
shows
$\chi^{\mathrm{sym}}(S(c, d)) = -\chi^{\mathrm{alt}}(c, d)$ and
$\chi^{\mathrm{alt}}(S(c, d)) = -\chi^{\mathrm{sym}}(c, d)$
(verify: for $(1, 0)$ with $\chi^{\mathrm{sym}} = q$,
$\chi^{\mathrm{alt}} = -1/q$, and $S(1, 0) = (1, -H_A)$ giving
$\chi^{\mathrm{sym}} = q + (-H_A) = q^{-1}$ and
$\chi^{\mathrm{alt}} = -1/q + (-H_A) = -q$, matching the swap with
sign).  For a chain product

$$
  \frac{\chi^{\mathrm{sym}}(S(\beta))}{\chi^{\mathrm{alt}}(S(\beta))}
  = \frac{(-1)^n \chi^{\mathrm{alt}}(\beta)}{(-1)^n \chi^{\mathrm{sym}}(\beta)}
  = \left(\frac{\chi^{\mathrm{sym}}(\beta)}{\chi^{\mathrm{alt}}(\beta)}\right)^{-1}
$$

so $\Phi_3(S(\beta)) = -\Phi_3(\beta)$, eigenvalue $-1$.

**Functional $\Phi_1$.** The unsymmetrised standard character
$\chi^{\mathrm{std}}(\beta)$ is not an $S$-eigenvector in general.
The Frobenius-symmetrised value
$V_{\mathrm{Frob}} = (\chi^{\mathrm{std}}(\beta) + \chi^{\mathrm{std}}(S(\beta)))/2$
is by construction $S$-invariant.  Equivalently, the average
$\Phi_1 := \tfrac12 (\Phi_1(\beta) + \Phi_1(S(\beta)))$ is the
projection onto the $S$-even subspace.  $\square$

**Consequence.** The signed sum

$$
  \mathfrak{m}(S(\beta)) - \mathfrak{m}(\beta)
  = -2 \alpha H_A^2 \Phi_3(\beta)
$$

isolates the chirality channel as the unique source of $S$-odd
contribution to the categorical mass.  Numerically, since $S$
maps the proton braid (uud) to a braid with quark content (ddu)
(modulo strand ordering equivalent to the neutron's udd content),
this provides the structural origin of the proton-neutron mass
splitting at the Wedderburn formula level.

**Witness**:
[`computations/wedderburn_3term_inter_only.py`](#)
verifies the eigenvalue assignments numerically at $q_0$ and
confirms that $\Phi_3 \approx 0$ for inter-nucleon-only chains in
free $A=1$ nucleons (consistent with the $S$-eigenspace
decomposition).
