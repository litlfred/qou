**Setup (commutative ring of coefficients).**
Throughout, the categorical structure is $R$-enriched over

$$
  R \;=\; \mathbb{Z}\bigl[q^{\pm 1/2},\, (q - q^{-1})^{-1}\bigr].
$$

Let $(\mathbf{C}, A, \tau)$ be a rigid :refterm[braided monoidal category]{#braided-monoidal-category}
$R$-enriched with self-dual fundamental object $A$ of categorical
dimension $\dim_q A = [2]_q \in R$, and $\tau \colon \mathbf{C} \to
R\text{-mod}$ the fibre functor.

**Theorem (two-strand spectral completeness).**
*The Frobenius $R$-algebra $E := \mathrm{End}_{\mathbf{C}}(A \otimes A)$
is a free $R$-module of rank $2$ with the following structure.*

1. *There exist exactly two non-zero central idempotents
   $e_+, e_- \in E$ with $e_+ + e_- = \mathrm{id}_{A \otimes A}$ and
   $e_+ \cdot e_- = 0$.*
2. *Each $e_\pm$ projects onto a simple summand:*
   $$
     A \otimes A \;\cong\; V_+ \oplus V_-,
     \qquad e_\pm A^{\otimes 2} = V_\pm.
   $$
   *The summand $V_-$ is canonically isomorphic to the unit object
   $\mathbf{1}$ — a singlet of $R$-rank one.*
3. *The braiding decomposes as*
   $$
     c_{A,A} \;=\; q^{1/2}\, e_+ \;-\; q^{-1/2}\, e_-,
   $$
   *and $\{q^{1/2},\, -q^{-1/2}\}$ are the only eigenvalues of
   $c_{A,A}$ on $A \otimes A$.*
4. *(Plancherel completeness.) The Plancherel weights*
   $$
     w_+ \;=\; \frac{(\dim_q V_+)^2}{[2]_q!},
     \qquad
     w_- \;=\; \frac{(\dim_q V_-)^2}{[2]_q!}
   $$
   *satisfy $w_+ + w_- = 1$ in $R \otimes \mathbb{Q}$.*
