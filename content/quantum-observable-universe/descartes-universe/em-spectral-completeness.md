**Setup (commutative ring of coefficients).**
Throughout, the categorical structure is $R$-enriched over

$$
  R \;=\; \mathbb{Z}\bigl[q^{\pm 1/2},\, (q - q^{-1})^{-1}\bigr].
$$

Let $(\mathbf{C}, A, \tau)$ be a rigid braided monoidal category
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

*Proof.*
The braiding eigenvalue extraction
([eigenvalue extraction](#prop:braiding-eigenvalue-extraction))
shows that $c_{A,A}$ satisfies the Hecke minimal polynomial

$$
  (c_{A,A} - q^{1/2})(c_{A,A} + q^{-1/2}) \;=\; 0
$$

in $E$.  The two eigenvalues $q^{1/2}, -q^{-1/2}$ are distinct
(their difference $q^{1/2} + q^{-1/2}$ is a unit in $R$), so the
minimal polynomial splits over $R$ and Bezout produces orthogonal
idempotents

$$
  e_- \;=\; \frac{q^{1/2} \cdot \mathrm{id} - c_{A,A}}{q^{1/2} + q^{-1/2}},
  \qquad
  e_+ \;=\; \mathrm{id} - e_-.
$$

These are central in $E$ since $c_{A,A}$ generates the centraliser of
the diagonal $R$-action by Schur--Weyl-Hecke duality.  Statement (2)
follows from $H_2(R, q) \cong E$ being free of rank $2$ over $R$: $E$
has at most two simple summands, and $e_\pm$ realise them.  The
singlet identification $V_- \cong \mathbf{1}$ is the standard
Schur-functor decomposition $A \otimes A = S^2 A \oplus \Lambda^2 A$
with $\Lambda^2 A \cong \mathbf{1}$ when $A$ is the fundamental of
$\mathrm{SU}_q(2)$.  Statement (4) is the Wedderburn trace identity
([Wedderburn trace](#prop:wedderburn-trace-identity)) at $n = 2$.
$\square$
