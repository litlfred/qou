The
[Yang–Mills surreal bound](#rem:yang-mills-surreal-bound) gives the
mass-gap statement at substrate order $\Delta_q \asymp \varepsilon^3$
but explicitly defers the **Wightman-axiom portion** of the
Millennium Prize statement — the regularity programme of recovering a
standard renormalised QFT as the standard part of the $q$-deformed
substrate. This conjecture supplies the bridge: the Reeb
$\mathbb{Z}_2$ acting on the
[Frobenius pairing](#def:frobenius-hopf-substrate) furnishes
Osterwalder–Schrader reflection positivity in the archimedean
realisation, which together with the surreal mass gap is the
Osterwalder–Schrader sufficient input for Wightman reconstruction.

**Conjecture (OS reflection positivity from the Reeb $\mathbb{Z}_2$).**
*Let $\theta$ denote the antipodal $\mathbb{Z}_2 \subset U(1)_{\xi}$
inside the Reeb $U(1)$ — equivalently, the chart-swap involution
$\iota : Z \mapsto Z^{-1}$ on the
[contact affine chart](#def:contact-affine-chart) at $\varTheta = \pi$,
per [chart-swap $U(1)$ is the Reeb flow](#rem:reeb-u1-chart-swap).
Then the [Frobenius pairing](#def:frobenius-hopf-substrate)
$\langle\,\cdot\,,\,\cdot\,\rangle_F$ on $A$ satisfies reflection
positivity under $\theta$:*

$$
  \langle  \theta(\phi),  \phi  \rangle_F  \geq  0
  \qquad \text{for every state } \phi \in A_+,
$$

*with equality iff $\phi$ vanishes on the positive-time half of the
Reeb decomposition. Under the
[archimedean realization](#def:archimedean-realization-functor)
$\tau_{\mathrm{arch}}$ this categorical positivity descends to the
Osterwalder–Schrader reflection-positivity axiom of the four
Euclidean Wightman correlation functions
$\tau_{\mathrm{arch}}\bigl(\langle \phi_1 \cdots \phi_n \rangle_F\bigr)$
on the $\varepsilon \to 0$ standard manifold $\mathbb{R}^4$.*

## Why $\mathbb{Z}_2$ ⊂ $U(1)_{\xi}$ is the OS reflection

The Osterwalder–Schrader reflection $\theta_{\mathrm{OS}}$ on
Euclidean spacetime is reflection in the $\tau = 0$ hyperplane,
i.e. $(x_1, x_2, x_3, \tau) \mapsto (x_1, x_2, x_3, -\tau)$. In the
categorical contact-geometric formulation, Euclidean time is the
Reeb parameter $t$ along $\xi$
([categorical Reeb derivation](#def:categorical-reeb)), so
$\theta_{\mathrm{OS}}$ acts on the contact affine chart as
$\phi_t \mapsto \phi_{-t}$. The categorical realisation of this
involution is precisely the antipodal $\mathbb{Z}_2$ subgroup at
$\varTheta = \pi$ of the chart-swap $U(1)$ family $\rho_\varTheta : z
\mapsto e^{i\varTheta} z$ — the $U(1)$ that the
[chart-swap–Reeb identification](#rem:reeb-u1-chart-swap)
shows coincides with the Reeb flow $U(1)$.

There is therefore no separate OS reflection to construct: it is
already present in the categorical infrastructure as the
$\mathbb{Z}_2$ subgroup of the Reeb circle.

## Why the Frobenius pairing automatically respects it

The Frobenius pairing is by construction symmetric:
$\Psi = S^2 = \mathrm{id}_A$, so
$\langle a, b \rangle_F = \langle b, a \rangle_F$. Under the
$\theta$-action on $A$, the antipode $S$ swaps the two factors and
inverts the Reeb flow direction. Symmetry of the Frobenius pairing
under $\Psi$ implies $\theta$-invariance of the pairing up to the
sign captured by the Reeb-half decomposition. The conjecture is the
**positivity** statement — that for any state $\phi$ supported on the
positive-time Reeb half, $\langle \theta(\phi), \phi \rangle_F$
evaluates to a non-negative scalar in $\mathrm{End}_{\mathbf{C}}(\mathbf{1})$.

The positivity refines the symmetry: symmetry alone gives
$\langle \theta(\phi), \phi \rangle_F = \langle \phi, \theta(\phi)
\rangle_F$ (so the quantity is self-conjugate / real), but does not
force the real value to be $\geq 0$. The extra structural input
needed is that the antipode-twisted pairing $\langle \theta(\cdot),
\cdot \rangle_F$ descends through $\tau_{\mathrm{arch}}$ to a
positive-definite inner product on the half-line $L^2(\mathbb{R}_{>0})$.

## Why the surreal bound + this conjecture ⇒ Wightman

The Osterwalder–Schrader theorem
[`osterwalder1973`, `osterwalder1975`] states: a family of Euclidean
correlation functions $\{S_n\}$ on $\mathbb{R}^4$ defines a Wightman
QFT on Minkowski space iff
(OS0) temperedness, (OS1) Euclidean covariance, (OS2) reflection
positivity, (OS3) symmetry, and (OS4) cluster decomposition all hold.

In the QOU framework:

| OS axiom | QOU input |
|----------|-----------|
| OS0 (temperedness) | $\tau_{\mathrm{arch}}$ images of partial products $\Phi_n$ are tempered by the [archimedean limit conjecture](#conj:dilogarithm-archimedean-limit) at every $x \in (0, 1)$. |
| OS1 (Euclidean covariance) | $S_5$-action on Bring's coordinate ring is the categorical lift of the $\mathrm{SO}(4) / \mathrm{Spin}(4)$ rotation group, and the [$\mathbb{Z}_2 \hookrightarrow U(1)_{\xi}$](#rem:reeb-u1-chart-swap) hierarchy is the Euclidean time translation. |
| **OS2 (reflection positivity)** | **This conjecture.** |
| OS3 (symmetry / locality) | Categorical permutation symmetry of the Frobenius pairing; $\Psi = S^2 = \mathrm{id}_A$. |
| OS4 (cluster decomposition) | Mass gap $\Delta_q \asymp \varepsilon^3$ from the [surreal bound](#rem:yang-mills-surreal-bound) gives exponential clustering at separation $r$: $|S_n(\cdots) - S_k(\cdots) S_{n-k}(\cdots)| \lesssim e^{-\Delta_q r}$. |

OS0, OS1, OS3 are categorically built-in. OS4 is the
[surreal mass-gap statement](#rem:yang-mills-surreal-bound). **OS2 is
the open input** — this conjecture. Granting it, the OS theorem
reconstructs a Wightman QFT on $\mathbb{R}^4$ as the standard part of
the $q$-deformed substrate, completing the Wightman-axiom portion of
the Yang–Mills millennium statement that
[`yang-mills-surreal-bound`](#rem:yang-mills-surreal-bound) flagged
as outstanding.

## Why it is conjectural

The positivity statement involves three open ingredients:

1. **Categorical positivity of the antipode-twisted pairing.** The
   Frobenius pairing is constructively non-degenerate but neither the
   QOU axioms nor the
   [Frobenius–Hopf substrate definition](#def:frobenius-hopf-substrate)
   currently impose positivity of $\langle \theta(\cdot), \cdot
   \rangle_F$. The conjecture is the structural claim that the
   substrate, being a $C^*$-Frobenius–Hopf algebra in the
   archimedean specialisation (where $q = q_0 \in \mathbb{R}_{>1}$),
   inherits positivity from the $C^*$-norm.

2. **Stability under $\tau_{\mathrm{arch}}$.** The archimedean
   realisation functor must commute with the positivity restriction:
   $\tau_{\mathrm{arch}}\bigl(\langle\theta(\phi),\phi\rangle_F\bigr) =
   \bigl\langle\theta_{\mathrm{OS}}\tau_{\mathrm{arch}}(\phi),\,
   \tau_{\mathrm{arch}}(\phi)\bigr\rangle_{L^2(\mathbb{R}^4)}$.
   Equivalently, the OS reflection on the standard Euclidean correlation
   functions is the $\tau_{\mathrm{arch}}$-image of the Reeb antipodal
   $\mathbb{Z}_2$ action. This follows from the
   [chart-swap–Reeb identification](#rem:reeb-u1-chart-swap) once
   $\tau_{\mathrm{arch}}$ is shown to preserve the $U(1)_{\xi}$-action
   on contact charts.

3. **Mathlib infrastructure.** A complete proof needs a Frobenius
   structure on the categorical $C^*$-completion and the Wightman
   reconstruction theorem — neither in Mathlib today. The conjecture
   is packaged as the typeclass
   `QOU.AppendixSurreals.OSReflectionPositivity`, with one field
   stating the positivity inequality. The class is the §3b-cond
   conditional-class input for the Wightman-axiom theorem; granting
   the class instance, the surreal bound completes OS reconstruction.

## Conclusion

The Wightman-axiom portion of the Yang–Mills millennium statement —
the regularity programme deferred by
[`yang-mills-surreal-bound`](#rem:yang-mills-surreal-bound) — reduces
(modulo the conditional-class instance above) to the **structural
positivity of the antipode-twisted Frobenius pairing**. The
reflection involved is not a separate piece of analytic continuation
but the antipodal $\mathbb{Z}_2$ subgroup of the Reeb $U(1)$, made
visible by the
[chart-swap–Reeb identification](#rem:reeb-u1-chart-swap). The
categorical infrastructure already houses every OS ingredient except
this positivity — packaging it as a class isolates the *single*
remaining input the substrate needs to supply a Wightman QFT.
