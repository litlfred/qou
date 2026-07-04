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
