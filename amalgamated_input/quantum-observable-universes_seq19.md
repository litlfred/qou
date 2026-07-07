<!-- FILE_START: instanton-intro.md -->
The gauge term $\int_A \mathrm{tr}_A(F_\nabla \wedge_q
\star_q F_\nabla)$ of the canonical action takes its extremal
value when the curvature is $\star_q$-self-dual; we make this
precise and read off the consequences for the categorical
Lagrangian on-shell.

Definition: Categorical instanton calls a connection $\nabla$ an
instanton when its curvature $F_\nabla \in \Omega^2(A)$
satisfies $\star_q F_\nabla = F_\nabla$. Proposition: Existence of the categorical instanton and Proposition: uniqueness of the categorical instanton, each with their proof blocks,
deliver an instanton from the QOU axioms. Remark: Instanton on-shell computes the Bogomolny decomposition: the second Chern
number $c_2(A)$ supplies the topological piece, the
anti-self-dual norm is forced to zero, and the gauge sector of
$\mathcal{L}_q$ collapses to a purely topological term plus the
matter coupling.

Lemma: Irreducibility from observability, with its proof,
reads the QOU observability axiom $\mathrm{Hom}(\mathbf{1},
\mathrm{Ad}(A)) = 0$ off any categorical instanton:
$\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A))$ has
only the zero morphism. Proposition: Self-duality from variation,
with its proof, shows that every critical point of the
Yang--Mills functional $\int_A \star_q F_\nabla \cdot F_\nabla$
is an instanton — the Bogomolny inequality saturates exactly on
self-dual curvature. Remark: Self-dual short exact sequence
records the $\Omega^2(A) = \Omega^+(A) \oplus \Omega^-(A)$
splitting of two-forms into the eigenspaces of $\star_q$.
Remark: Non-cocommutativity of the Hopf structure records
what fails at $q \neq 1$: $\Delta \neq \sigma \circ \Delta$,
controlled by the universal $R$-matrix, and identifies this
with the algebraic origin of quantum uncertainty. The next
section, **Non-vanishing of $d_q^2$**, asks the parallel
question for the deformed exterior derivative.

_(draft.)_
<!-- FILE_END: instanton-intro.md -->

<!-- FILE_START: categorical-instanton.md -->
Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) with connection
$\nabla$ ([categorical connection](#def:categorical-connection)) and
$q$-Hodge star $\star_q$ ([$q$-Hodge star](#def:q-hodge-star)).
The connection $\nabla$ is an **instanton** if its curvature
$F_\nabla \in \Omega^2(A)$ is $\star_q$-self-dual:

$$
  \star_q F_\nabla =  F_\nabla.
$$

Equivalently, the curvature factors through the self-dual projection:

```tex
\begin{equation}\label{eq:instanton-cd}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  A \otimes A \ar[r, "\nabla \circ \nabla"]
    \ar[dr, "0"']
  & \Omega^2(A) \ar[d, "\pi^-"] \\
  & \Omega^-(A)
\end{tikzcd}
\end{equation}
```

where $\pi^- = \tfrac{1}{2}(\mathrm{id} - \star_q)$ is the
anti-self-dual projector and $\Omega^-(A) = \ker(\mathrm{id} + \star_q)$.
<!-- FILE_END: categorical-instanton.md -->

<!-- FILE_START: categorical-instanton-exists.md -->
Let $(\mathbf{C}, A, \tau)$ be a
[quantum observable universe](#def:quantum-observable-universe) with
$q$-Hodge star $\star_q$.  Then there exists a
[categorical connection](#def:categorical-connection) $\nabla$ whose
curvature $F_\nabla$ is $\star_q$-self-dual — i.e. there exists a
[categorical instanton](#def:categorical-instanton).

Uniqueness (as an element of the instanton moduli) is
([uniqueness of categorical instantons](#prop:categorical-instanton-unique)).
<!-- FILE_END: categorical-instanton-exists.md -->

<!-- FILE_START: categorical-instanton-unique.md -->
Two [categorical instantons](#def:categorical-instanton) $\nabla_1$
and $\nabla_2$ of the same topological charge
$c_2(\nabla_i) = k \in H^4$ coincide up to a categorical gauge
transformation $g \in \mathrm{Aut}^\otimes(\tau)$:

$$
  \nabla_2 \;=\; g \cdot \nabla_1 \cdot g^{-1} + g\,dg^{-1}.
$$

Uniqueness is therefore uniqueness *of the gauge orbit*, not of the
connection itself — the categorical instanton moduli space
$\mathcal{M}^{\mathrm{inst}}_k$ is parameterised by $H^4$.
<!-- FILE_END: categorical-instanton-unique.md -->

<!-- FILE_START: instanton-on-shell.md -->
On an instanton background ([categorical instanton](#def:categorical-instanton)),
the curvature is $\star_q$-self-dual: $\star_q F_\nabla = F_\nabla$.
The Bogomolny decomposition ([self-duality](#prop:categorical-self-duality))
gives

$$
  \lVert F_\nabla \rVert^2
  = 
  \lVert F_\nabla^+ \rVert^2 + \lVert F_\nabla^- \rVert^2
  = 
  c_2(A) + 2\lVert F_\nabla^- \rVert^2,
$$

where $c_2(A)$ is the second Chern number (a topological invariant).
The instanton condition forces $F_\nabla^- = 0$, so the gauge sector
of the Lagrangian becomes purely topological:

$$
  \mathcal{D}_\nabla^{2} =  F_\nabla^+ =  c_2(A).
$$

The full Lagrangian ([categorical Lagrangian](#def:categorical-lagrangian))
therefore simplifies on-shell:

$$
  \mathcal{L}_q\big|_{\text{instanton}}
  = 
  c_2(A)
  + 
  \psi^* \otimes \mathcal{D}_\nabla\psi.
$$

```tex
\begin{equation}\label{eq:instanton-on-shell-cd}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \mathcal{L}_q \ar[r, equals]
  & \mathcal{D}_\nabla^2 + \psi^* \otimes \mathcal{D}_\nabla\psi
    \ar[d, "\text{instanton}"] \\
  & c_2(A) + \psi^* \otimes \mathcal{D}_\nabla\psi
\end{tikzcd}
\end{equation}
```

This has three consequences:

1. **No dynamical gauge degrees of freedom beyond topology.**
   The connection is determined (up to gauge equivalence) by the knot
   type $K$ of the localized knot
   ([knot--particle dictionary](#rem:knot-particle-dictionary)).  The
   topological sector $c_2(A)$ is fixed by $K$.

2. **All physics is in the matter equation.**
   On an instanton, varying $\psi$ gives
   $\mathcal{D}_\nabla\psi = 0$
   ([variational equations](#prop:variational-equations)), which completely
   determines the propagation of the state.

3. **The wavefront is determined by the background topology.**
   The Green's function of $\mathcal{D}_\nabla$ depends on the
   instanton $\nabla$, which in turn depends on the knot type of the
   material through which $\psi$ propagates.  Different materials
   (different $K$, different $c_2$) produce different diffraction
   patterns --- a prediction unique to QOU.
<!-- FILE_END: instanton-on-shell.md -->

<!-- FILE_START: categorical-irreducible.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe.
Any categorical instanton $\nabla$
([categorical instanton](#def:categorical-instanton)) is irreducible:
$\mathrm{Hom}_{\mathbf{C}}(\mathbf{1},\mathrm{Ad}(A)) = 0$.

```tex
\begin{equation}\label{eq:categorical-irreducible-diagram}
\begin{tikzcd}[column sep=2.5em]
  \mathbf{1} \ar[r, "0"] & \mathrm{Ad}(A)
\end{tikzcd}
\qquad\text{(the only morphism is zero)}
\end{equation}
```


While the proof reduces to a standard subsingleton elimination in Lean, identifying irreducibility as an intrinsic, universal property of all categorical instantons is a mathematically novel structural claim within the framework of the Quantum Observable Universe.
<!-- FILE_END: categorical-irreducible.md -->

<!-- FILE_START: categorical-self-duality.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
with volume form $\mathrm{vol} \in \Omega^n(A)$
([$q$-Hodge star](#def:q-hodge-star)).  Every connection $\nabla$
that is a critical point of the categorical Yang--Mills functional

$$
  S[\nabla] =  \int_A\!\bigl(\star_q(F_\nabla) \cdot F_\nabla\bigr)
$$

is an instanton ([categorical instanton](#def:categorical-instanton)).  That is,
the following diagram commutes:

```tex
\begin{equation}\label{eq:self-duality-cd}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  \Omega^2(A) \ar[r, "\star_q"] \ar[d, "\int_A(\cdot {*} \cdot)"']
  & \Omega^2(A) \ar[d, "\int_A(\cdot {*} \cdot)"] \\
  \mathbf{1} \ar[r, "\mathrm{id}"']
  & \mathbf{1}
\end{tikzcd}
\qquad\Longrightarrow\qquad
F_\nabla \in \Omega^+(A).
\end{equation}
```

<!-- FILE_END: categorical-self-duality.md -->

<!-- FILE_START: self-dual-ses.md -->
The $q$-Hodge star $\star_q$ ([$q$-Hodge star](#def:q-hodge-star)) is an
involution on $\Omega^2(A)$, so its eigenspaces give the splitting
$\Omega^2(A) = \Omega^+(A) \oplus \Omega^-(A)$ and hence
the short exact sequence

```tex
\begin{equation}\label{eq:self-dual-ses}
\begin{tikzcd}[column sep=2em]
  0 \ar[r]
  & \Omega^-(A)
    \ar[r, "\iota"]
  & \Omega^2(A)
    \ar[r, "\pi^+"]
  & \Omega^+(A)
    \ar[r]
  & 0
\end{tikzcd}
\end{equation}
```

where $\Omega^{\pm}(A) = \ker(\mathrm{id} \mp \star_q)$.
The instanton condition
([categorical instanton](#def:categorical-instanton)) is exactly
$F_\nabla \in \ker(\pi^-)$, i.e. $F_\nabla^- = 0$.
In the archimedean realisation ([self-dual curvature](#ex:self-dual-curvature)),
$\star_q$ specialises to $*_H$ and the sequence becomes
$0 \to \Gamma(\Lambda^-\!H^* \otimes \mathrm{Ad}(P)) \to \Gamma(\Lambda^2 H^* \otimes \mathrm{Ad}(P)) \to \Gamma(\Lambda^+\!H^* \otimes \mathrm{Ad}(P)) \to 0$.
<!-- FILE_END: self-dual-ses.md -->

<!-- FILE_START: hopf-non-cocommutativity.md -->
The Hopf comultiplication $\Delta \colon A \to A \otimes A$ of the
Frobenius--Hopf object is coassociative but *not* cocommutative
when $q \neq 1$.  Let $\sigma$ denote the tensor flip.  The
cocommutativity square

```tex
\begin{equation}\label{eq:non-cocommutativity}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  A
    \ar[r, "\Delta"]
    \ar[d, "\Delta"']
  & A \otimes A
    \ar[d, "\sigma"]
  \\
  A \otimes A
    \ar[r, equal]
  & A \otimes A
\end{tikzcd}
\quad\text{commutes}\;\Longleftrightarrow\; q \to 1\ \text{(symmetric-braiding limit)}.
\end{equation}
```

For $q \neq 1$ the failure is controlled by the universal $R$-matrix:
$\sigma \circ \Delta = \mathrm{Ad}_{R_q} \circ \Delta$,
where $R_1 = 1 \otimes 1$ recovers cocommutativity at $q = 1$.
This non-cocommutativity is the algebraic origin of quantum
uncertainty: it prevents simultaneous diagonalisation of comultiplication
and its transpose, which in turn prevents independent observations from
commuting ([two-observer parallelogram](#rem:two-observer-parallelogram)).
<!-- FILE_END: hopf-non-cocommutativity.md -->

