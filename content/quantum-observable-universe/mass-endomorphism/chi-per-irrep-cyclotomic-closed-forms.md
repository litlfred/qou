*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**All three $V_\lambda$ per-irrep character-difference closed forms — cyclotomic-factor pattern.**

Per user direction "V_2,1 — write all with 4 in denom — pattern,
where come from? check lit", "first prove formally V", "V_3 ε^k
pattern", "add Hoefsmit 2x2 matrix expansion", "can you prove all
generalizations": this block extends [`rem:chi-v3-closed-form-proof`](#rem:chi-v3-closed-form-proof)
to all three Wedderburn blocks of $H_3(q)$, exposing the
**unified cyclotomic-factor pattern**.

## Three closed forms

For the canonical typed-$\mathbf{B}_3$ braids
$\mathcal{B}_p$ (uud, $6\sigma + 3\sigma^{-1} + 2\ \mathrm{averaged}$)
and $\mathcal{B}_n$ (udd, $5\sigma + 4\sigma^{-1} + 2\ \mathrm{averaged}$),
the per-Wedderburn-block character differences are:

$$
\begin{aligned}
  \chi_{(3)}(\mathcal{B}_n) - \chi_{(3)}(\mathcal{B}_p)
   &= -\dfrac{(q^2 + 1)^2 (q^2 - 1)}{4 q}, \\[6pt]
  \chi_{(2,1)}(\mathcal{B}_n) - \chi_{(2,1)}(\mathcal{B}_p)
   &= -\dfrac{(q^4 + 1)(q^2 - 1)}{4 q^3}, \\[6pt]
  \chi_{(1,1,1)}(\mathcal{B}_n) - \chi_{(1,1,1)}(\mathcal{B}_p)
   &= -\dfrac{(q^2 + 1)^2 (q^2 - 1)}{4 q^5}.
\end{aligned}
$$

All three have the common prefactor $-\frac{(q^2 - 1)}{4 \cdot q^{?}}$
where the denominator power is $1, 3, 5$ for $\lambda = (3), (2,1), (1,1,1)$.

## Cyclotomic factorisation

See [Table 1](#tbl:chi-per-irrep-cyclotomic-closed-forms-table1-data).

Recall: $\Phi_1(q) = q-1$, $\Phi_2(q) = q+1$, $\Phi_4(q) = q^2+1$,
$\Phi_8(q) = q^4+1$.

**Two striking observations**:

1. **$V_{(3)}$ and $V_{(1,1,1)}$ share the identical numerator polynomial** — only the denominator differs ($q$ vs $q^5$). The denominator-power gap of $4$ exactly matches the factor by which the closed forms differ:
   $$\chi_{(1,1,1)}\text{-diff}(q) = \frac{\chi_{(3)}\text{-diff}(q)}{q^4}.$$
   This is the **conjugate-partition symmetry**: $(1,1,1)$ is the conjugate (transpose) of $(3)$, and the corresponding sign-rep $\leftrightarrow$ trivial-rep duality $\sigma_i \mapsto q$ vs $\sigma_i \mapsto -q^{-1}$ produces the $q \leftrightarrow -q^{-1}$ substitution that maps the two characters into each other.

2. **$V_{(2,1)}$ involves 8th roots of unity** ($\Phi_8 = q^4 + 1$, whose roots are the primitive 8th roots), while $V_{(3)}, V_{(1,1,1)}$ involve **4th roots** ($\Phi_4 = q^2 + 1$). This is consistent with the **Clifford depth** of the H_3 representations: V_(2,1) is the 2-d Hoefsmit irrep (Cl(3) depth), while the 1-d irreps V_(3), V_(1,1,1) are Cl(2) depth.

3. **Denominator power tracks the content sum**:
   - $c(\lambda) = \sum_{(i,j) \in \lambda} (j - i)$
   - $c((3)) = 0+1+2 = 3$, denominator $q$
   - $c((2,1)) = 0+1-1 = 0$, denominator $q^3$
   - $c((1,1,1)) = 0-1-2 = -3$, denominator $q^5$

   The denominator exponent is $p = 3 - \frac{2}{3} c(\lambda)$, mapping $c \in \{3, 0, -3\}$ to $p \in \{1, 3, 5\}$ exactly.

## Where the V_(2,1) closed form comes from

V_(2,1) is the **2-dimensional Hoefsmit irrep**. Each typed crossing
acts as a 2$\times$2 matrix on the SYT basis $\{v_{T_1}, v_{T_2}\}$:

- $\sigma_0 \mapsto \mathrm{diag}(q, -q^{-1})$ (diagonal, eigenvalues $q$ and $-q^{-1}$)
- $\sigma_1 \mapsto \begin{pmatrix} d_1 & b \\ b & d_2 \end{pmatrix}$ with $d_1 = q^3/(q^2 + 1), d_2 = -q^{-1}/(q^2 + 1), b = \sqrt{d_1 d_2 + 1}$
- $\sigma_i^{-1} \mapsto \sigma_i - (q - q^{-1}) I$
- averaged $\mapsto \frac{1}{2}(\sigma_i + \sigma_i^{-1})$

The character $\chi_{(2,1)}(\beta) = \mathrm{Tr}\bigl(\prod_{c \in \beta} M_c\bigr)$
where $M_c$ is the matrix for each crossing in the canonical word order
from `atomic_braid_to_crossings`.

The full matrix product expansion + trace, followed by `sympy.cancel +
sympy.factor`, yields $-(q^4+1)(q^2-1)/(4q^3)$ — the closed form above.
The probe `probe_per_wedderburn_block_ck.py` performs this symbolic
computation; the witness file records the result bit-exactly.

## Literature pointers

- **Cyclotomic Hecke algebras at depth $n$**: Ariki-Koike algebras and
  their representations carry cyclotomic structure tied to the
  parameters via $\Phi_d(q)$ factors. See e.g. Mathas, *Iwahori-Hecke
  Algebras and Schur Algebras of the Symmetric Group* (1999), §3 on
  Specht modules with cyclotomic decomposition.
- **Conjugate-partition character symmetry**: standard Hecke
  representation-theory fact; cf. Kassel, *Quantum Groups* (GTM 155)
  §V.5 on Iwahori-Hecke characters under partition conjugation.
- **Content sums and q-content invariants**: the
  q-content sum $c(\lambda)$ appears in the Hoefsmit seminormal-form
  axial distance formulae (Hoefsmit 1974 thesis); the relationship
  $\text{denominator exponent} \sim |c(\lambda)|$ for the character
  difference is a probe finding suggestive of a deeper
  hook-content-formula derivation.

## Lean theorems exported

All proved by `field_simp + ring` after unfolding (sorry-free):

See [Table 2](#tbl:chi-per-irrep-cyclotomic-closed-forms-table2-data).

## Compute wiring

Probe `probe_per_wedderburn_block_ck.py` (witness:
`per-wedderburn-block-ck.witness.json`) computes the symbolic
$\chi_\lambda(\mathcal{B}_p), \chi_\lambda(\mathcal{B}_n)$ via the existing
`q_character_on_braid_word` infrastructure, applies `sympy.cancel +
sympy.factor`, and reports the three closed forms above plus all
$\varepsilon^k$ coefficients ($k = 0..12$) of the difference at
$q = 1 + \varepsilon$. The witness data backs every Lean closed-form
theorem in this module empirically.
