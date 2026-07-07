<!-- FILE_START: categorical-action-intro.md -->
The Lagrangian $\mathcal{L}_q$ is an endomorphism
of $A$; we now trace it to a morphism $\mathbf{1} \to
\mathbf{1}$ and read off the gravity, gauge, and matter terms
that the QOU axioms force into the result. The trace is supplied
by the rigid duality: no spacetime measure is invoked.

Definition: Categorical action defines $\mathfrak{S} = \mathrm{tr}
(\Phi) = \mathrm{ev}_A \circ (\mathrm{id}_{A^\vee} \otimes \Phi)
\circ \mathrm{coev}_A$ for a physics endomorphism $\Phi \in
\mathrm{End}_{\mathbf{C}}(A)$. Proposition: Existence of the categorical action — with its proof — verifies the construction,
and Proposition: uniqueness of the categorical action (given $\Phi$) — with its proof — fixes $\mathfrak{S}$ up to the identity
$\mathfrak{S} = \mathrm{tr}(\Phi)$. Remark: Categorical action notation and Remark: Categorical action notation on $\mathrm{SU}(2)$ collect the trace, partial trace,
adjoint section, and Frobenius--Ricci shorthand used throughout
the rest of the chapter.

The closing block is Proposition: Canonical action of a quantum observable universe: the choice $\Phi_q = \mathcal{L}_q$ delivers
$\mathfrak{S}_q = \mathrm{tr}(\mathcal{L}_q)$, which expands —
via the Frobenius--Hopf decomposition of $\mathcal{D}_\nabla^2$
— into three terms (gravity $\mathrm{tr}(q R_{\int})$, gauge
$\int_A \mathrm{tr}_A(F_\nabla \wedge_q \star_q F_\nabla)$,
matter $\int_A(\psi^* \cdot \mathcal{D}_\nabla \psi)$),
uniquely up to a single scalar $\lambda \in R^\times$ tracking
the normalisation of $\int_A$. The next section, **Variational
equations and wavefronts**, varies this action with respect to
its three inputs and reads off the field equations.

_(draft.)_
<!-- FILE_END: categorical-action-intro.md -->

<!-- FILE_START: categorical-action.md -->
Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)).
A :defterm[categorical action]{#categorical-action} on $(\mathbf{C}, A, \tau)$ is a morphism
$\mathfrak{S} \colon \mathbf{1} \to \mathbf{1}$ of the form

```tex
\begin{equation}\label{eq:categorical-action}
  \mathfrak{S}
  = 
  \mathrm{ev}_A
    \circ
    \bigl(\mathrm{id}_{A^\vee} \otimes \Phi\bigr)
    \circ
    \mathrm{coev}_A,
\end{equation}
```

where $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$ is called the
*physics endomorphism*.

```tex
\begin{equation}\label{eq:categorical-action-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \mathbf{1}
    \ar[r, "\mathrm{coev}_A"]
    \ar[rr, bend right=25, "\mathfrak{S}"']
  & A \otimes A^{\vee}
    \ar[r, "\Phi \otimes \mathrm{id}"]
  & A \otimes A^{\vee}
    \ar[r, "\mathrm{ev}_A"]
  & \mathbf{1}
\end{tikzcd}
\qquad\text{(categorical action)}
\end{equation}
```

The evaluation $\mathrm{ev}_A \colon A^\vee \otimes A \to \mathbf{1}$
and coevaluation $\mathrm{coev}_A \colon \mathbf{1} \to A \otimes A^\vee$
are the structure maps of the rigid duality on $A$
([rigid :refterm[monoidal category]{#monoidal-category}](#def:rigid-monoidal-category)).  Composing
them with an inserted endomorphism produces the categorical trace:

$$
  \mathfrak{S} = \mathrm{tr}(\Phi).
$$

As a string diagram, the action is a single closed loop with $\Phi$
inserted --- the morphism $\mathbf{1} \to \mathbf{1}$ obtained by
"tracing out" the internal degrees of freedom of $A$.  The rigid
structure provides the integration; the physics endomorphism encodes the
dynamics.

The trace $\mathrm{tr}(\Phi)$ used here is the categorical trace of an
endomorphism of a dualizable object in a balanced monoidal category
\cite{stolz-teichner-2012}.  Cf.\ the spectral-action trace
$\mathrm{Tr}\,\chi(D/\Lambda)$ \cite{chamseddine-connes-1997}.
<!-- FILE_END: categorical-action.md -->

<!-- FILE_START: categorical-action-exists.md -->
Let $(\mathbf{C}, A, \tau)$ be a
[quantum observable universe](#def:quantum-observable-universe) and
$\Phi \in \mathrm{End}_{\mathbf{C}}(A)$ a physics endomorphism.  Then
the [categorical action](#def:categorical-action)
$\mathfrak{S}_\Phi \colon \mathbf{1} \to \mathbf{1}$, defined as the
composite
$\mathrm{ev}_A \circ (\mathrm{id}_{A^\vee} \otimes \Phi) \circ \mathrm{coev}_A$,
exists as a morphism in $\mathbf{C}$ and equals the categorical
trace $\mathrm{tr}(\Phi)$.
Cf.\ \cite{stolz-teichner-2012}.

Uniqueness given $\Phi$ is
([uniqueness of categorical action](#prop:categorical-action-unique)).
<!-- FILE_END: categorical-action-exists.md -->

<!-- FILE_START: categorical-action-unique.md -->
For a fixed physics endomorphism $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$,
the [categorical action](#def:categorical-action)
$\mathfrak{S}_\Phi = \mathrm{tr}(\Phi)$ is uniquely determined.  Any
morphism $\mathbf{1} \to \mathbf{1}$ that factors as
$\mathrm{ev}_A \circ (\mathrm{id}_{A^\vee} \otimes \Phi) \circ \mathrm{coev}_A$
equals $\mathrm{tr}(\Phi)$.
<!-- FILE_END: categorical-action-unique.md -->

<!-- FILE_START: categorical-action-notation.md -->
Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) equipped with
substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)),
$q$-Hodge star $\star_q$ ([$q$-Hodge star](#def:q-hodge-star)),
a connection $\nabla$ ([categorical connection](#def:categorical-connection)),
and a section $\psi \colon \mathbf{1} \to A$ (a "state").
The following notation is used in
[categorical action](#def:categorical-action):

- $\mathrm{tr} \colon \mathrm{End}_{\mathbf{C}}(A) \to R$ is the
  *categorical trace* (the composition
  $\mathrm{coev} \to \mathrm{id} \to \mathrm{ev}$ via the rigid
  structure).
- $R_{\int} \in \mathrm{End}_{\mathbf{C}}(A)$ is the
  *Frobenius--Ricci endomorphism*: the curvature of the
  Frobenius form $\int_A$ itself, defined by
  $R_{\int} = (\mathrm{id}_A \otimes \int_A) \circ F_{\nabla_{\int}}$,
  where $\nabla_{\int}$ is the canonical connection on $A$ induced
  by $\int_A$ via $\nabla_{\int}(a) = \int_A(a_{(1)}) \otimes a_{(2)} - a \otimes 1$
  (Sweedler notation: $\Delta(a) = a_{(1)} \otimes a_{(2)}$,
  summation suppressed).
- $\mathrm{tr}_A \colon \mathrm{End}_{\mathbf{C}}(A \otimes \Omega^{\bullet}(A)) \to \mathrm{End}_{\mathbf{C}}(\Omega^{\bullet}(A))$ is the
  *partial trace* over the $A$ factor.
- $\psi^* = \int_A \circ S(\psi) \colon A \to \mathbf{1}$ is the
  *adjoint section* (antipode composed with the Frobenius form).
- $D_\nabla = q^{-1}\nabla + (1 - q^{-1})\iota_\xi\nabla$ is
  the *$q$-deformed covariant derivative*, where $\xi$ is the
  Reeb derivation of $A$
  ([Reeb decomposition](#ex:reeb-decomposition)).
<!-- FILE_END: categorical-action-notation.md -->

<!-- FILE_START: categorical-action-notation-su2.md -->
Continuing [connection on $\mathrm{SU}(2)$](#ex:connection-su2), take
$A = \mathcal{O}(\mathrm{SU}(2))$ with Haar integral $\int_A = \int_G$,
connection $\nabla f = df + \mathcal{A} \cdot f$, and a state
$\psi \in A$ (a function on the group).

- *Categorical trace.*  For $T \in \mathrm{End}(V_j)$,
  $\mathrm{tr}(T) = \sum_m \langle j,m \mid T \mid j,m \rangle$
  is the usual matrix trace.
- *Frobenius--Ricci.*  $R_{\int}$ measures curvature of
  the Haar integral itself: on $\mathrm{SU}(2)$ (flat Haar measure),
  $R_{\int} = 0$ in the classical limit $q = 1$.
- *Adjoint section.*  For
  $\psi \colon \mathbb{C} \to A$, the adjoint is
  $\psi^*(f) = \int_G \overline{\psi(g)}f(g)dg$, i.e. the
  inner product with $\psi$ under the Haar integral.
- *$q$-deformed derivative.*  At $q = 1$,
  $D_\nabla = \nabla$ (ordinary covariant derivative).  For
  $q \neq 1$, the Reeb component is re-weighted, coupling the
  connection to the contact geometry.
<!-- FILE_END: categorical-action-notation-su2.md -->

<!-- FILE_START: qou-canonical-action.md -->
Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) equipped with
connection $\nabla$ ([categorical connection](#def:categorical-connection)),
substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)),
$q$-Hodge star $\star_q$ ([$q$-Hodge star](#def:q-hodge-star)),
and state $\psi \colon \mathbf{1} \to A$.
Then $(\mathbf{C}, A, \tau)$ determines a
([categorical action](#def:categorical-action)), unique up to a scalar
$\lambda \in R^{\times}$,

$$
  \mathfrak{S}_q
  = 
  \mathrm{tr}(\mathcal{L}_q),
$$

where $\mathcal{L}_q = \mathcal{L}_q(\nabla, \psi)$ is the categorical
Lagrangian ([categorical Lagrangian](#def:categorical-lagrangian)) and
$\Phi_q = \mathcal{L}_q$ is the physics endomorphism. The square of the
Dirac operator
([categorical Dirac operator](#def:categorical-dirac-operator))
decomposes via the Frobenius--Hopf structure as

$$
  \mathcal{D}_\nabla^{2}
  = 
  q \cdot R_{\int} +  \mathrm{tr}_A\!\bigl(
    F_\nabla \wedge_q \star_q F_\nabla
  \bigr),
$$

and applying the categorical trace term by term yields the
gravity $+$ gauge $+$ matter decomposition

```tex
\begin{equation}\label{eq:canonical-action-decomposition}
  \mathfrak{S}_q
  = 
  \underbrace{%
    \int_A \mathrm{tr}_A\bigl(q \cdot R_{\int}\bigr)
  }_{\text{gravity}}
  + 
  \underbrace{%
    \int_A \mathrm{tr}_A\bigl(
      F_\nabla \wedge_q \star_q F_\nabla
    \bigr)
  }_{\text{gauge}}
  + 
  \underbrace{%
    \int_A\!\bigl(\psi^* \cdot \mathcal{D}_\nabla\psi\bigr)
  }_{\text{matter}}.
\end{equation}
```

**Proof.** The categorical trace factors as $\mathrm{tr} = \int_A \circ
\mathrm{tr}_A$ --- the Frobenius form $\int_A \colon A \to \mathbf{1}$ after
the partial trace $\mathrm{tr}_A \colon \mathrm{End}(A) \to A$ --- so all
three summands share the *same* integration $\int_A$: there is one trace,
applied term by term, not three distinct integrations, with notation as in
[categorical action notation](#sec:categorical-action-notation).
Here $\mathrm{tr} = \mathrm{ev}_A \circ (\mathrm{id}_{A^\vee} \otimes {-}) \circ \mathrm{coev}_A = \int_A \circ \mathrm{tr}_A$ is the
categorical trace, which plays the role of spacetime integration;
$R_{\int}$ is the Frobenius--Ricci endomorphism; and
$F_\nabla = \nabla^2$ is the curvature.  In the matter term the state
bilinear $\psi^* \cdot \mathcal{D}_\nabla\psi \in A$ is already a
density, so $\int_A$ applies directly --- equivalently
$\int_A \mathrm{tr}_A(\psi^* \otimes \mathcal{D}_\nabla\psi)$.
Cf.\ the gravity + gauge + matter decomposition of the
Chamseddine--Connes spectral action
\cite{chamseddine-connes-1997, connes1996}, and the categorical
trace framework \cite{stolz-teichner-2012}.

The same action admits two equivalent right-hand sides.  The *trace form*
(string diagram) carries the categorical trace on each term,

$$
  \mathfrak{S}_q
  = \mathrm{tr}(q R_{\int})
  + \mathrm{tr}(F_\nabla \wedge_q \star_q F_\nabla)
  + \mathrm{tr}(\psi^* \otimes \mathcal{D}_\nabla\psi),
$$

while the *integral form* (Frobenius / Stokes) carries the Frobenius
form $\int_A$ after the partial trace $\mathrm{tr}_A$,

$$
  \mathfrak{S}_q
  = \int_A \mathrm{tr}_A(q R_{\int})
  + \int_A \mathrm{tr}_A(F_\nabla \wedge_q \star_q F_\nabla)
  + \int_A(\psi^* \cdot \mathcal{D}_\nabla\psi).
$$

The two agree termwise by $\mathrm{tr} = \int_A \circ \mathrm{tr}_A$.
The string-diagram form is well defined and unique by
([existence](#prop:categorical-action-exists),
[uniqueness](#prop:categorical-action-unique)) --- these pin the action
*as the trace*, with no reference to an integral.  The integral form
adds a single identification: $\int_A$ is the Markov trace, which
Yekutieli's non-abelian Stokes theorem equates with the surface-ordered
multiplicative integral
$\overrightarrow{\textstyle\prod}\!\int_\Sigma F_\nabla$ of the
curvature ([Yekutieli--Stokes remark](#rem:yekutieli-stokes)).  So the
gauge term is literally the Yang--Mills curvature integral, and the
categorical action $\mathfrak{S}_q$ is the analogue of Hamilton's
classical $S = \int L\,\mathrm{d}t$: $\int_A$ (Frobenius
form $=$ Markov trace $=$ Yekutieli integral) plays the role of
integration over spacetime, $\mathcal{L}_q$ the Lagrangian density.

For uniqueness, the evaluation and coevaluation maps are
determined up to unique isomorphism by the duality data, and the
Frobenius--Hopf axioms fix the decomposition of $\mathcal{D}_\nabla^2$
into curvature terms.  The residual ambiguity is a single scalar
$\lambda \in R^{\times}$: the normalization of the Frobenius form
$\int_A$.  Replacing $\int_A$ by $\lambda\!\int_A$ sends
$\mathfrak{S}_q \mapsto \lambda\mathfrak{S}_q$.  This is the
categorical analog of the choice of physical units --- it corresponds
to the freedom in choosing $G$, $g^2$, and $\hbar$ in the archimedean
realization ([Remark](#rem:physicist-translation)). $\blacksquare$
<!-- FILE_END: qou-canonical-action.md -->

<!-- FILE_START: canonical-action-obstruction.md -->
The scalar ambiguity of the
([canonical action](#prop:qou-canonical-action)) is controlled by the same
obstruction that governs the forgetful functor $\tau$. The observability
axiom
$\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
([QOU axiom 2](#def:quantum-observable-universe)) ensures that the
trace $\mathrm{tr} \colon \mathrm{End}(A) \to R$ is faithful --- no
endomorphism is "invisible" to integration.  Relaxing this condition
(allowing hidden symmetries, $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) \neq 0$) introduces a nontrivial kernel in the trace, and the
obstruction to recovering a well-defined action is classified by the
same cohomology class $\kappa \in H^2(\mathcal{S}, \mathcal{B})$
that obstructs lifting in the Yekutieli sense
([Yekutieli lifting condition](#def:yekutieli-lifting-condition);
[Yekutieli--Stokes remark](#rem:yekutieli-stokes)).
<!-- FILE_END: canonical-action-obstruction.md -->

