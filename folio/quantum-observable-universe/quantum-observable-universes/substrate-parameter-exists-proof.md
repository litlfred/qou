
The braiding $c_{V,V} \colon V \otimes V \to V \otimes V$ of the QOU
provides the aether parameter categorically — no external choice is
needed.

**Step 1 (spectral decomposition).** The volume constraint
$\epsilon \colon \Lambda^2 V \twoheadrightarrow \mathbf{1}$ splits
$V \otimes V = S^2 V \oplus \Lambda^2 V$ into eigenspaces of
$c_{V,V}$.  Since $\Lambda^2 V \cong \mathbf{1}$ is simple and
$\dim S^2 V = 3$, the braiding acts by scalars
$\lambda_+ \in \mathrm{End}(\mathbf{1})$ on $S^2 V$ and
$\lambda_- \in \mathrm{End}(\mathbf{1})$ on $\Lambda^2 V$.

**Step 2 (define $q$).** Set $q := \lambda_+$.  The determinant
constraint $\lambda_+ \cdot \lambda_- = -1$ (from
$\det(c_{V,V}) = -1$ on a rank-$2$ object with trivial determinant)
forces $\lambda_- = -q^{-1}$.  Therefore $c_{V,V}$ satisfies the
Hecke relation
$(T - q)(T + q^{-1}) = 0$
([braiding eigenvalue extraction](#prop:braiding-eigenvalue-extraction)).

**Step 3 (non-degeneracy).** The QOU assumption
$c_{V,V}^2 \neq \mathrm{id}$ ensures $q \neq \pm 1$.  The
positive-definite dagger structure forces $q \in \mathbb{R}_{>0}$,
and the non-root-of-unity condition $q \notin \mu_\infty(k)$ follows
from transcendence over $\mathbb{Q}$ in the archimedean realisation.

**Step 4 (agreement with $d_q$).** The categorical $q$ extracted from
the braiding coincides with the interpolation parameter in
$d_q = q^{-1}d + (1 - q^{-1})\pi_V \circ d$: both are
characterised as the unique $q \in \mathrm{End}(\mathbf{1})$ for
which the Iwahori--Hecke algebra $H_n(q)$ acts faithfully on
$V^{\otimes n}$.

In the archimedean realisation, the constant aether field
$q(p) = q_0 > 1$ for all $p$ satisfies the classicality bound
$q \ge 1$ and positivity. Non-constant aether fields arise from
the Reeb flow parameterisation of the categorical
$\mathrm{End}(\mathbf{1})$-valued coordinate.
