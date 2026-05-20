Continuing the [Bring's surface example](#ex:brings-surface-concrete),
we extract the [substrate parameter](#def:substrate-parameter)
constructively — replacing "there exists $q$" with an explicit
algorithm.

**Step 1: the fundamental object.** Bring's QOU has
$\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ with fundamental
object $V = V_{1/2} \cong \mathbb{C}^2$.

**Step 2: braiding eigenvalues.** The braiding
$c_{V,V} \colon V \otimes V \to V \otimes V$ is the $R$-matrix of
$\mathrm{SU}_q(2)$, acting on the $4$-dimensional space
$V \otimes V$. This space decomposes as
$V_{1/2} \otimes V_{1/2} \cong V_1 \oplus V_0$
(spin-$1$ $\oplus$ spin-$0$). The $R$-matrix has eigenvalue $+q$ on
the symmetric summand $S^2 V \cong V_1$ and eigenvalue $-q^{-1}$ on
the antisymmetric summand $\Lambda^2 V \cong V_0$. In matrix form
on the standard basis $\{e_+ \otimes e_+,\, e_+ \otimes e_-,\,
e_- \otimes e_+,\, e_- \otimes e_-\}$:

$$
  R = \begin{pmatrix}
    q & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 1 & q - q^{-1} & 0 \\
    0 & 0 & 0 & q
  \end{pmatrix}.
$$

**Step 3: read off $q$.** Define $q := \lambda_+$, the eigenvalue of
$c_{V,V}$ on $S^2 V$. This is a concrete number, not an existential
assertion. The Hecke relation $(T - q)(T + q^{-1}) = 0$ is then
*verified* (not postulated) by checking that $R$ satisfies
$R^2 - (q - q^{-1})R - I = 0$.

**Step 4: non-degeneracy.** The QOU axiom $c_{V,V}^2 \neq \mathrm{id}$
forces $q \neq \pm 1$. The dagger structure
$c_{V,V}^{\dagger} = c_{V,V}^{-1}$ forces $|q| = 1$ or
$q \in \mathbb{R} \setminus \{0\}$.

**Bring's surface specialisation.** The Euler characteristic
$\chi(A) = -6$ constrains $q$ further. The quantum dimension of
$A = \mathcal{O}_q(\mathrm{SU}(2))$ satisfies
$\mathrm{tr}(\mathrm{id}_A) = [N]_q [N-1]_q / [1]_q$ at $N = 2$, giving
$\chi(A) = [2]_q [1]_q / [1]_q = [2]_q = q + q^{-1}$.
The Descartes condition $\chi(A) = 2 - 2g = -6$ requires
$q + q^{-1} = -6$, i.e. $q^2 + 6q + 1 = 0$, so
$q = -3 \pm 2\sqrt{2}$. The two roots are both negative
(consistent with $q + q^{-1} < 0$). Choosing the root closer to
zero:

$$
  q_{\mathrm{Bring}} = -3 + 2\sqrt{2} \approx -0.172.
$$

(The other root $q = -3 - 2\sqrt{2} \approx -5.83$ is its
reciprocal.) This *categorical* parameter lives in the Laurent
polynomial ring $\mathbb{Z}[q, q^{-1}]$; the *physical* substrate
parameter $q_0 = 1.109978595554181\ldots$ (50 dps) arises from the archimedean
realisation via the muon/electron mass ratio
([skein mass relation](#rem:skein-mass-relation)). The two are
related by the specialisation map
$\iota \colon \mathbb{Z}[q, q^{-1}] \to \mathbb{C}$.

**Summary.** The substrate parameter is not merely "known to exist" —
it is extracted by a three-step algorithm: (1) form $V \otimes V$,
(2) diagonalise $c_{V,V}$, (3) read off the symmetric eigenvalue.
On Bring's surface, the Descartes condition pins $q$ to a specific
algebraic number.
