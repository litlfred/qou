Suppose $q, q' \in \mathrm{End}(\mathbf{1})$ are both aether
parameters for the same QOU $(\mathbf{C}, A, \tau)$.  Each extracts
from the same braiding $c_{V,V}$ via the spectral decomposition
of [existence](#thm:substrate-parameter-exists).

**Step 1 (spectral data is intrinsic).**  The rigid monoidal
structure and the volume constraint
$\epsilon \colon \Lambda^2 V \twoheadrightarrow \mathbf{1}$
determine the canonical splitting
$V \otimes V = S^2 V \oplus \Lambda^2 V$ uniquely as the eigenspace
decomposition of $c_{V,V}$ under the induced
$H_2(q)$-action (the braiding generates the two-strand
Iwahori--Hecke algebra, the $q$-deformation of $S_2$); neither
summand involves a choice.  Hence
the eigenvalues $\lambda_+, \lambda_- \in \mathrm{End}(\mathbf{1})$
of $c_{V,V}$ on $S^2 V$ and $\Lambda^2 V$ are intrinsic invariants.

**Step 2 (Hecke relation pins eigenvalue pair).**  By
[braiding eigenvalue extraction](#prop:braiding-eigenvalue-extraction),
$c_{V,V}$ satisfies $(T - \lambda_+)(T - \lambda_-) = 0$ with
$\lambda_+ \lambda_- = -1$.  Thus the unordered pair
$\{\lambda_+, \lambda_-\} = \{q, -q^{-1}\}$ is determined by the
QOU, so $q \in \{\lambda_+, -\lambda_-^{-1}\}$, and the same for
$q'$.

**Step 3 (positivity pins the sign).**  The
[positive-definite dagger structure](#prop:positive-definite-dagger)
induced by $(\int_A, S)$ forces $q \in \mathbb{R}_{>0}$: the
$q$-eigenvalue of the symmetric braiding channel must be strictly
positive because
$\langle \cdot, \cdot \rangle_q = \int_A \circ \mu \circ (S \otimes
c_{V,V})$ is positive definite only when the $S^2 V$-eigenvalue
is positive.  The same constraint applies to $q'$.

**Step 4 (conclusion).**  From Step 2, $q, q' \in
\{\lambda_+, -\lambda_-^{-1}\}$; from Step 3 both are positive.
Since $\lambda_+ > 0$ and $-\lambda_-^{-1} = q$ (from
$\lambda_+ \lambda_- = -1$), the two candidates coincide:
$q = q' = \lambda_+$.  In the archimedean realisation, the same
argument applies pointwise on $M$, so the aether field
$q \colon M \to \mathbb{R}_{>0}$ is uniquely determined by the
QOU data.  $\square$
