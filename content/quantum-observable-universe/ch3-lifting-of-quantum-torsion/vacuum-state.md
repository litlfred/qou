Let $(\mathcal{C}, A, \omega)$ be a quantum observable universe
([Definition](#def:quantum-observable-universe)); let $q$ denote the substrate parameter.  Let
$\mathcal{A}_\infty$ be its direct limit algebra
([Definition](#def:direct-limit-algebra)).  Let $G_q =
\mathrm{Aut}^{\otimes}(\omega)$ be the quantum gauge group
([Definition](#def:quantum-gauge-group)), acting on
$\mathcal{A}_\infty$ by conjugation.  Then there exists a unique
$R$-linear functional
$\varphi \colon \mathcal{A}_\infty \to R$ that is $G_q$-invariant:
$$
  \varphi(g \cdot a) = \varphi(a)
  \quad\text{for all } g \in G_q,\;
  a \in \mathcal{A}_\infty.
$$
In the archimedean realisation, $G_q = \mathrm{SU}_q(2)$ and
$\varphi$ is the unique $\mathrm{SU}(2)$-invariant state on the
$C^*$-algebraic direct limit.

---

The algebra $\mathcal{A}_\infty$ is the direct limit of the fibre algebras
$\Gamma(J^1 E_n,\, \mathrm{SU}_{q_n}(2))$
([Definition](#def:direct-limit-algebra)), each of which is a
$C^*$-algebra carrying a continuous $\mathrm{SU}(2)$ action by automorphisms.

*Existence.*
At each finite level $n$ the algebra
$\Gamma(J^1 E_n,\, \mathrm{SU}_{q_n}(2))$ is a type-I $C^*$-algebra
(it is a section algebra of a locally trivial bundle with compact fibre).
By compactness of $\mathrm{SU}(2)$, averaging any state $\psi_n$ over the
Haar measure $\mu$ produces an $\mathrm{SU}(2)$-invariant state:
$$
  \omega_n(a)
  \;=\;
  \int_{\mathrm{SU}(2)} \psi_n(g \cdot a)\; d\mu(g).
$$
The descent homomorphisms $\mathfrak{d}_n$ ([Lemma](#lem:descent)) are
equivariant and surjective, so the invariant states $\{\omega_n\}$ form a
compatible system.  By the universal property of the direct limit, they
determine a state $\omega$ on $\mathcal{A}_\infty$ satisfying
$\omega(g \cdot a) = \omega(a)$.

*Uniqueness.*
The vanishing condition
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ of the quantum observable
universe axioms implies that the trivial representation appears with
multiplicity one in each $\Gamma(J^1 E_n,\, \mathrm{SU}_{q_n}(2))$ (it
occurs only in the scalar summand $\mathbb{C} \cdot \mathbf{1}$).  Any
$\mathrm{SU}(2)$-invariant state must factor through the projection onto
this trivial isotypic component, which is one-dimensional.  Hence
$\omega$ is the unique such state.
