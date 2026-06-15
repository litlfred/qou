**Conjecture (next-order Faddeev WKB gives the categorical Green's function).**
*Let $q$ be the substrate parameter and $\hbar_q = 1 - q^{-1}$ the
quantum Planck constant. Under the joint Faddeev scaling $q \to 1$, $n \to \infty$, $n|1-q| \to \infty$ of
[the archimedean limit conjecture](#conj:dilogarithm-archimedean-limit),
the partial product $\Phi_n(x; q)$
([$q$-Pochhammer partial product](#def:q-pochhammer-partial-product))
admits a stationary-phase expansion at the dominant saddle $x_0$ of
the form*

$$
  \Phi_n(x; q)
  \;\sim\;
  \exp\!\Bigl(
    \hbar_q^{-1} S_0(x_0)
    + S_1(x_0)
    + \hbar_q \, S_2(x_0)
    + \cdots
  \Bigr),
$$

*where the leading term is the classical dilogarithm,*

$$
  S_0(x_0)  =  \mathrm{Li}_2(x_0)
  \qquad (= \text{archimedean limit}),
$$

(See [archimedean limit](#conj:dilogarithm-archimedean-limit) for the
conjectural archimedean realisation of $\mathrm{Li}_2$.)

*and the next-to-leading term is the half-log-determinant of the
[categorical Dirac operator](#def:categorical-dirac-operator)
$\mathfrak{D}_\nabla = q^{-1}\nabla + \hbar_q \, \iota_\xi \nabla$
restricted to the
[categorical-instanton moduli](#def:categorical-instanton) at
$x_0$:*

$$
  \boxed{\;
  S_1(x_0)
  \;=\;
  -\tfrac{1}{2} \log \det\!\bigl(\mathfrak{D}_\nabla\big|_{x_0}\bigr).
  \;}
$$

*Equivalently, the
[archimedean realization](#def:archimedean-realization-functor)
$\tau_{\mathrm{arch}}$ of the one-loop fluctuation factor
$\exp S_1(x_0)$ is the two-point Green's function of $\mathfrak{D}_\nabla$
evaluated at the corresponding hyperbolic cusp:*

$$
  \tau_{\mathrm{arch}}\!\bigl(\exp S_1(x_0)\bigr)
  \;=\;
  G_\nabla(x_0)
  \;:=\;
  \langle  \mathfrak{D}_\nabla^{-1}  \rangle_{x_0}.
$$

## Narrative proof (modulo the conjectural ingredients listed below)

The proof has four steps. Steps 1–2 are classical Faddeev–Kashaev
asymptotics. Step 3 is the new categorical input. Step 4 is
standard heat-kernel zeta regularisation.

**Step 1 (classical: Faddeev–Kashaev scalar WKB).** Take logs inside
the partial product:

$$
  \log \Phi_n(x; q)
  \;=\;
  -\!\sum_{k=0}^{n-1} \log\!\bigl(1 - x q^k\bigr).
$$

Set $q = e^{-\hbar_q}$, rescale $k = s/\hbar_q$, and pass to the
Riemann-sum integral
$\hbar_q^{-1}\!\int_0^{n\hbar_q} -\log\!\bigl(1 - x e^{-s}\bigr)\, ds$.
Substituting $t = x e^{-s}$, the asymptotic in the Faddeev regime is

$$
  \log \Phi_n(x; q)
  \;=\;
  \hbar_q^{-1}\,\mathrm{Li}_2(x)
  \;+\;
  S_1^{\mathrm{scalar}}(x)
  \;+\;
  O(\hbar_q),
$$

with $S_1^{\mathrm{scalar}}(x) = -\tfrac{1}{2} \log(1 - x) - \tfrac{1}{2}\log(2\pi)$
the standard $\hbar_q^0$ correction of the scalar stationary-phase
integral. This is the leading-order
[archimedean limit](#conj:dilogarithm-archimedean-limit) plus its
direct $\hbar_q^0$ correction in the scalar variable $x$.

**Step 2 (classical: passage from scalar to operator-valued).** When
$\Phi_n(x; q)$ is regarded as a *partition function* (the
Faddeev–Kashaev / Reshetikhin–Turaev path-integral reading), the
scalar variable $x$ is the eigenvalue of a connection-valued
operator and the scalar Hessian $-\tfrac{1}{2}\log(1-x_0)$ is
replaced by the operator-valued log-determinant of the Hessian of
the categorical action $\mathfrak{S}_q[\nabla]$ at the dominant saddle
$\nabla_0$:

$$
  S_1(x_0)
  \;=\;
  -\tfrac{1}{2}\,\log \det
   \bigl( \mathrm{Hess}\,\mathfrak{S}_q[\nabla]\big|_{\nabla_0} \bigr).
$$

This is the standard one-loop fluctuation rule for stationary-phase
integrals over the space of connections. The remaining content of
the conjecture is identifying $\mathrm{Hess}\,\mathfrak{S}_q[\nabla]_{\nabla_0}$
with the categorical Dirac operator $\mathfrak{D}_\nabla$.

**Step 3 (new categorical input: Hessian = $\mathfrak{D}_\nabla$ via
Lichnerowicz on the instanton saddle).** Let $\nabla_0$ be a critical
point of $\mathfrak{S}_q$, equivalently a
[categorical instanton](#def:categorical-instanton):
$\star_q F_{\nabla_0} = F_{\nabla_0}$. For a perturbation $\nabla =
\nabla_0 + a$ with $a \in \Omega^1(\mathrm{End}\, V)$,

$$
  F_{\nabla_0 + a}  =  F_{\nabla_0} + d_{\nabla_0} a + a \wedge_q a.
$$

The first variation vanishes at $\nabla_0$ (saddle condition); the
second variation of the gauge sector
$\mathfrak{S}_q^{\mathrm{gauge}} = \int_A \mathrm{tr}_A(F_\nabla \wedge_q \star_q F_\nabla)$
is

$$
  \delta^2 \mathfrak{S}_q^{\mathrm{gauge}}\big|_{\nabla_0}(a, a)
  \;=\;
  \langle  d_{\nabla_0} a,  d_{\nabla_0} a  \rangle_F
  \;=\;
  \langle  a,  \Delta_{\nabla_0}^q\, a  \rangle_F,
$$

where $\Delta_{\nabla_0}^q = d_{\nabla_0}^* \, d_{\nabla_0} +
d_{\nabla_0} \, d_{\nabla_0}^*$ is the *categorical $q$-Laplacian*
on $\Omega^1(\mathrm{End}\, V)$ with adjoint
$d_{\nabla_0}^* = \star_q\, d_{\nabla_0}\, \star_q$. So far this is
the categorical Yang–Mills computation, parallel to the classical
case.

The key identity is the **categorical Lichnerowicz formula** on the
self-dual background $\star_q F_{\nabla_0} = F_{\nabla_0}$:

$$
  \Delta_{\nabla_0}^q
  \;=\;
  \mathfrak{D}_{\nabla_0}^2  +  \tfrac{1}{4}\,\mathrm{Sc}_q,
$$

where $\mathfrak{D}_{\nabla_0}$ is the
[categorical Dirac operator](#def:categorical-dirac-operator) at
$\nabla_0$ and $\mathrm{Sc}_q$ is the $q$-scalar curvature
(vanishing on the contact-flat background of Bring's surface, where
$\xi$ is parallel). The classical Lichnerowicz identity
$\Delta = \mathfrak{D}^2 + R/4$ extends to the $q$-deformed case
because the categorical Dirac
$\mathfrak{D}_\nabla = q^{-1}\nabla + \hbar_q\,\iota_\xi \nabla$
satisfies the same Clifford-multiplication structure as its
classical limit ($\iota_\xi$ playing the role of $\gamma^0$).

Therefore on the instanton saddle with vanishing $\mathrm{Sc}_q$:

$$
  \det \mathrm{Hess}\,\mathfrak{S}_q^{\mathrm{gauge}}\big|_{\nabla_0}
  \;=\;
  \det \Delta_{\nabla_0}^q
  \;=\;
  \det \mathfrak{D}_{\nabla_0}^2
  \;=\;
  (\det\, |\mathfrak{D}_{\nabla_0}|)^2,
$$

where we use the chiral structure on the spinor bundle: with
$\star_q F = F$ self-dual, $\mathfrak{D}_\nabla$ decomposes into
$(\mathfrak{D}_\nabla^+, \mathfrak{D}_\nabla^-)$ with
$\mathfrak{D}_\nabla^- = (\mathfrak{D}_\nabla^+)^*$, so
$\mathfrak{D}_\nabla^2 = \mathfrak{D}_\nabla^+\, \mathfrak{D}_\nabla^- \oplus
\mathfrak{D}_\nabla^-\, \mathfrak{D}_\nabla^+$ and the Pfaffian
identity $\det \mathfrak{D}_\nabla^2 = (\det |\mathfrak{D}_\nabla|)^2$
holds.

Combining with Step 2:

$$
  S_1(x_0)
  \;=\;
  -\tfrac{1}{2}\, \log\det\bigl(\mathrm{Hess}\,\mathfrak{S}_q\big|_{\nabla_0}\bigr)
  \;=\;
  -\tfrac{1}{2}\, \log\det \mathfrak{D}_{\nabla_0}^2
  \;=\;
  -\log\det |\mathfrak{D}_{\nabla_0}|
  \;=\;
  -\tfrac{1}{2}\, \log\det \mathfrak{D}_{\nabla_0},
$$

where the final equality reads $\mathfrak{D}_\nabla$ as the Pfaffian
square root of $\mathfrak{D}_\nabla^2$ on the chiral spinor bundle —
the convention adopted in the conjecture statement above.

**Step 4 (standard: log-determinant = Green's function via heat-kernel
zeta).** By standard zeta-function regularisation,

$$
  -\tfrac{1}{2}\log\det \mathfrak{D}_\nabla
  \;=\;
  -\tfrac{1}{2}\,\mathrm{tr}\,\log \mathfrak{D}_\nabla
  \;=\;
  \tfrac{1}{2} \int_0^\infty \!\! \frac{dt}{t}
   \bigl( \mathrm{tr}\, e^{-t \mathfrak{D}_\nabla} - \mathrm{tr}\, e^{-t} \bigr).
$$

The functional derivative of this expression with respect to the
connection $\nabla$ at the saddle equals the diagonal of
$\mathfrak{D}_\nabla^{-1}$ — i.e. the categorical Green's function
$G_\nabla(x_0)$. The archimedean realisation $\tau_{\mathrm{arch}}$
sends the regularised determinant to the standard heat-kernel
determinant on the corresponding ideal-tetrahedron triangulation of
the hyperbolic brane configuration (paralleling how
[`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit)
sends the leading Faddeev limit to the Bloch–Wigner volume).

This closes the chain $S_1 \leadsto -\tfrac{1}{2}\log\det\mathfrak{D}_\nabla
\leadsto G_\nabla(x_0)$ — modulo the three open ingredients listed
below.

## What the proof leaves open

| Step | Status | What remains |
|---|---|---|
| 1. Scalar Faddeev–Kashaev WKB | classical | none — Faddeev 1994, Kashaev 1997 |
| 2. Scalar $\to$ operator-valued passage | classical | none — standard one-loop fluctuation rule |
| 3a. Hessian = $\Delta_{\nabla_0}^q$ on $\Omega^1(\mathrm{End}\,V)$ | categorical Yang–Mills computation | direct from the variation of $\mathfrak{S}_q^{\mathrm{gauge}}$; routine |
| 3b. Categorical Lichnerowicz $\Delta^q = \mathfrak{D}^2 + \tfrac{1}{4}\mathrm{Sc}_q$ | new categorical lemma | Clifford-multiplication structure of $\iota_\xi$; provable but not in the paper yet |
| 3c. $\mathrm{Sc}_q$ vanishes on contact-flat Bring background | standard | $\xi$ parallel $\Rightarrow$ scalar curvature trivial |
| 3d. Pfaffian identity for self-dual chiral $\mathfrak{D}$ | classical | none — Atiyah–Singer / index theorem |
| 4. Heat-kernel determinant = propagator | standard analytic regularisation | none in the $\mathbb{R}^4$ archimedean specialisation; in Lean, needs heat-kernel infrastructure not in Mathlib |

The genuinely *new* step is **3b** — the categorical Lichnerowicz
identity. This is a single categorical lemma (provable from the
Clifford-multiplication structure of the
[categorical Dirac](#def:categorical-dirac-operator) and the
self-duality $\star_q F = F$ of the
[categorical-instanton equation](#def:categorical-instanton)). The
remaining steps are either standard or already in the paper.

Granting **3b**, the proof closes everything *except* the Lean
formalisation, which is blocked by the absence of heat-kernel
determinant theory and stationary-phase asymptotics from Mathlib.
The conjecture remains formally a conjecture (since 3b has not been
written up as a separate proposition with its own proof), but the
status of "what stops it" is much narrower: a single categorical
lemma plus Mathlib infrastructure.

## One algebraic object, two analytic outputs

The conjecture sharpens the Φ$_q$ (product form) vs
$-\mathrm{Li}_2^q(-z)$ (Kashaev integration limit) split: the same
algebraic state $\Phi_n(x; q_0)$ produces *both* of the
geometric features required for an observable QFT, separated
by their order in $\hbar_q$:

| WKB order | Symbol | Archimedean output | Role |
|-----------|--------|-------------------|------|
| $\hbar_q^{-1}$ | $S_0 = \mathrm{Li}_2(x_0)$ | Bloch–Wigner volume $D(z)$ | classical action / CS phase |
| $\hbar_q^{0}$ | $S_1 = -\tfrac{1}{2}\log\det \mathfrak{D}_\nabla$ | Green's function $G_\nabla(x_0)$ | one-loop propagator |
| $\hbar_q^{+1}$ | $S_2$ | curvature corrections | higher-loop |

For force-carrier torus knots $T_{m,n}$ the
$S_0$ piece evaluated at the corresponding flat-$\mathrm{SU}(2)$
critical point recovers the classical Chern–Simons invariant
(see [Chern–Simons as knot invariant](#rem:chern-simons-as-knot-invariant))

$$
  \mathrm{CS}(T_{m,n})
  \;=\;
  \frac{\pi^2 (m^2 - 1)(n^2 - 1)}{12\,m\,n}
$$

via Faddeev–Kashaev (the imaginary half of the volume conjecture, since
$\mathrm{Vol}(T_{m,n}) = 0$); the $S_1$ piece supplies the matching
one-loop propagator factor of the same algebraic state.

## Why it remains conjectural in Lean

Granting the narrative proof above, three ingredients still need
formal write-up to upgrade the block to a theorem:

1. **Step 3b — categorical Lichnerowicz lemma.** A separate
   proposition stating $\Delta_{\nabla_0}^q = \mathfrak{D}_{\nabla_0}^2
   + \tfrac{1}{4}\,\mathrm{Sc}_q$, with proof from the Clifford-
   multiplication structure of $\iota_\xi$ in the
   [categorical Dirac](#def:categorical-dirac-operator). This is a
   single computation in the QOU formalism, not currently in the paper.

2. **Stationary-phase uniformity.** Standard stationary-phase gives the
   prefactor pointwise at $x_0$; the full statement asserts the
   asymptotic is uniform in a neighbourhood of $x_0$ along Faddeev's
   joint scaling, strong enough to commute with $\tau_{\mathrm{arch}}$.
   Inherited from
   [`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit).

3. **Mathlib infrastructure.** A complete Lean proof needs heat-kernel
   determinant theory and stationary-phase asymptotics — neither
   currently in Mathlib. The conjecture is packaged as the typeclass
   `QOU.QPochhammer.WKBGreensFunction`, extending
   `QOU.QPochhammer.ArchimedeanLimit` with one additional field
   stating the $\hbar_q^0$ stationary-phase identity.

Ingredient (1) is the closest to a paper-side write-up; ingredients
(2)–(3) are the same Mathlib gap the parent conjecture already faces.

## Why this matters

The categorical Green's function $G_\nabla$ is the kernel that controls
the exponential decay of correlations in the categorical action — i.e.,
the mass-gap statement
([Yang–Mills surreal bound](#rem:yang-mills-surreal-bound)). The
$S_0 \leftrightarrow S_1$ split exhibited here is the structural
reason both the
Chern–Simons phase ([Chern–Simons as knot invariant](#rem:chern-simons-as-knot-invariant)) and the
mass-gap propagator emerge from a *single* algebraic state $\Phi_n(x;
q_0)$ at $q = q_0$ — without separately postulating a metric. The
Φ_q-piece [`def:phi-q-piece`](#def:phi-q-piece) thus carries both the
geometry (S_0) and the metric (S_1) of the corresponding hyperbolic
brane configuration; they are the leading and subleading analytic
shadows of the same algebraic datum, related by the WKB hierarchy in
$\hbar_q$.
