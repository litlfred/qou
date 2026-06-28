**Definition (spin involution on a Frobenius $*$-algebra).**
Let $(A, \tau, {}^*)$ be a Frobenius $*$-algebra over a
commutative ring $R$ — i.e., a Frobenius algebra equipped with
an $R$-linear involutive anti-homomorphism ${}^* : A \to A$
($(ab)^* = b^* a^*$, $(a^*)^* = a$) such that $\tau$ is
$*$-compatible ($\tau(a^*) = \tau(a)$ in the real case;
$\tau(a^*) = \overline{\tau(a)}$ otherwise). A *spin involution*
on $(A, \tau, {}^*)$ is an $R$-linear map $\sigma : A \to A$
satisfying

1. **Involution**: $\sigma \circ \sigma = \mathrm{id}_A$.
2. **Anti-multiplicative**:
   $\sigma(a b) = \sigma(b)\, \sigma(a)$ for all $a, b \in A$.
3. **Trace-invariant**: $\tau \circ \sigma = \tau$.
4. **$*$-compatible**: $\sigma(a^*) = \sigma(a)^*$ for all $a$.

The $\mathbb{Z}/2$ grading $A = A_+ \oplus A_-$ by
$\sigma$-eigenvalue is the *spin grading*; $A_+$ is the
*spin-singlet sector* and $A_-$ is the *spin-doublet sector*.

**Hypothesis (2 invertible).** Throughout this proposition we
assume $2 \in R^\times$ — i.e., the base ring $R$ contains
$\tfrac{1}{2}$. This is satisfied when $R$ is a field of
characteristic $\neq 2$ (in particular $\mathbb{Q}$,
$\mathbb{R}$, $\mathbb{C}$, $\mathbb{Z}[\tfrac{1}{2}]$, or any
$\mathbb{Q}$-algebra). For the QOU substrate $R = \mathbb{R}$ or
$R = \mathbb{Q}(q)$ this holds. Without this hypothesis, the
$A_\pm$ projections $a_\pm := \tfrac{1}{2}(a \pm \sigma(a))$ are
ill-defined; an alternative additive decomposition (without
division) exists when $A$ has an idempotent splitting
$\mathbf{1} = e_+ + e_-$ with $\sigma(e_\pm) = \pm e_\pm$, but
that is more restrictive.

Every $a \in A$ has the canonical decomposition
$a = a_+ + a_-$ with $a_\pm := \tfrac{1}{2}(a \pm \sigma(a)) \in
A_\pm$. The *isospin third-component* is **defined on
$\sigma$-eigenvectors**:

$$
  T_3(a) \;=\; \tfrac{1}{2}\,\mathrm{sgn}_\sigma(a)
  \;\in\; \{-\tfrac{1}{2},\, 0,\, +\tfrac{1}{2}\},
$$

with $T_3(a) = 0$ for $a \in A_+$ (singlet, $\sigma(a) = a$)
and $T_3(a) = \pm \tfrac{1}{2}$ for $a \in A_-$ realising
$\sigma(a) = \pm a$. For a general $a \in A$, $T_3$ is read
off the $A_\pm$-projection $a = a_+ + a_-$.

**Proposition (spin-invariance of the LP-dual).**
*Let $(A, \tau)$ be a Frobenius algebra with spin involution
$\sigma$. Let $c \in A$ be $\sigma$-invariant ($\sigma(c) = c$).
Let $\Sigma$ be a $\sigma$-stable set of central idempotents of
$A$ (i.e., $\sigma(\pi_\lambda) \in \{\pi_\mu : \mu \in
\Sigma\}$ for every $\lambda \in \Sigma$). For any $\beta \in A$,
the optimal dual variable $y_0^*$ of the operator-selection LP*

$$
  \min_{x \in A}\; \tau(c \cdot x)
  \quad \text{s.t.} \quad
  \tau(\beta^* \beta \cdot x) = n_{\mathrm{target}}(\beta), \;\;
  \tau(\pi_\lambda \cdot x) \geq 0 \;\; \forall \lambda \in \Sigma
$$

*satisfies*

$$
  y_0^*\bigl(\sigma(\beta)\bigr) \;=\; y_0^*(\beta).
$$
