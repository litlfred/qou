**Preliminaries.**

* **$\widehat{A}$**: the **isomorphism-class index set of simple
  $A$-modules** — equivalently, the indexing set of Wedderburn
  blocks of a finite-dim semisimple algebra $A$.  Standard
  representation-theory notation (analogous to $\widehat{G}$ for
  the unitary dual of a group).  For $A = H_n(R, q)$,
  $\widehat{A} = \{\lambda \vdash n\}$ (partitions of $n$).

* **Vortex**: a morphism $\varrho \colon \mathbf{1} \to A$ in the
  rigid :refterm[monoidal category]{#monoidal-category} of the quantum observable universe —
  i.e., a closed element of $A$ arising as the closure of a braid
  $\beta \in B_n$
  ([Hecke mass element](#def:hecke-mass-element)).  Each vortex has
  a Hecke-algebra representative $\sigma_w \in H_n(R, q)$ whose Markov
  trace is the categorical mass
  ([categorical mass, Markov](#prop:categorical-mass-markov)).
  In physics: particles (quarks, nucleons, nuclei) are vortices.

* **$C_{\dim_q}$**: the "C" stands for **Casimir** (Lie-algebra /
  TQFT terminology); "co-" because it is the Frobenius-pairing
  dual of the unit $1 = \sum_\lambda p_\lambda$, **not** the
  standard quadratic Casimir $\Omega = \sum_i e_i \otimes e^i$.
  See §"Uniqueness of $C_{\dim_q}$" below.

**Setup.**
Let $(A, \tau)$ be a finite-dimensional semisimple self-dual
Frobenius algebra over $\mathbb{C}$ with non-degenerate symmetric
bilinear form $\tau \colon A \to \mathbb{C}$ and Wedderburn
decomposition

$$
  A \;=\; \bigoplus_{\lambda \in \widehat{A}}
          \mathrm{Mat}_{d_\lambda}(\mathbb{C}),
$$

where $d_\lambda$ is the classical dimension of block $B_\lambda$.
Let $p_\lambda \in A$ be the central idempotent of block $\lambda$,
and let $\dim_q(\lambda) \in \mathbb{C}^\times$ denote any
non-vanishing "quantum dimension" function on blocks (e.g., for
$A = H_n(R, q)$ with Markov trace, $\dim_q$ is the $q$-hook-length
dimension giving $\tau(p_\lambda) = \dim_q(\lambda) \, d_\lambda
/ [n]_q!$).

**Theorem (Frobenius quantum-co-dimension trace).**
\*The **quantum-co-dimension element**

$$
  C_{\dim_q}
  \;:=\;
  \sum_{\lambda \in \widehat{A}}
    \frac{1}{\dim_q(\lambda) \cdot \tau(p_\lambda)}
    \cdot p_\lambda
  \;\in\; Z(A)
$$

*lies in the centre of $A$ and satisfies*

$$
  \boxed{
    \tau\bigl(C_{\dim_q}\bigr)
    \;=\;
    \sum_{\lambda \in \widehat{A}} \frac{1}{\dim_q(\lambda)}.
  }
$$
