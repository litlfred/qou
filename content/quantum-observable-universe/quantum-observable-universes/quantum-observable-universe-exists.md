**Proposition.**
*Let $G$ be a compact, connected, semisimple Lie group with complexified
Lie algebra $\mathfrak{g}$.  Let $M$ be a compact oriented manifold
admitting a principal $G$-bundle $P \to M$ whose adjoint bundle
$\mathrm{Ad}(P) = P \times_{G} \mathfrak{g}$ satisfies the measurability
condition*

$$
  c_{1}\!\bigl(\mathrm{Ad}(P)\bigr) = 0
  \qquad\text{and}\qquad
  c_{2}\!\bigl(\mathrm{Ad}(P)\bigr) = 0.
$$

*Then there exists a
[quantum observable universe](#def:quantum-observable-universe)
$(\mathbf{C}, A, \tau)$ satisfying the four QOU axioms ---
non-degenerate integration, observability, measurability, and the
categorical volume constraint --- whose archimedean realisation has
state bundle $\mathcal{S} = P \times_{G} V_{\mathrm{std}}$.*

*Explicitly, one may take*

$$
  \mathbf{C} = \mathbf{Rep}\bigl(U_{q}(\mathfrak{g})\bigr),
  \qquad
  A = \mathcal{O}_{q}(G),
  \qquad
  \tau = \mathrm{forget},
$$

*where $q \in \mathbb{C}^{\times}$ is the substrate parameter
([substrate parameter](#def:substrate-parameter)), $U_{q}(\mathfrak{g})$
is the Drinfeld--Jimbo quantum group, $\mathcal{O}_{q}(G)$ is its
restricted dual Hopf algebra, and the Frobenius form $\int_{A}$ is the
Haar state on $\mathcal{O}_{q}(G)$
([$\mathrm{SU}(2)$-QOU](#ex:qou-su2)).*

The measurability hypothesis on $P$ is not vacuous but admits common
realisations: for $G = \mathrm{SU}(2)$ and $M$ a contact CR 3-manifold,
$c_{1}(\mathrm{Ad}(P)) = 0$ is automatic ($G$ is simply connected)
while $c_{2}(\mathrm{Ad}(P)) = 0$ selects the topologically trivial
sector.  Non-vanishing $c_{2}$ is also admissible with $q = e^{\pi i/(k +
h^{\vee})}$ a root of unity, replacing $\mathbf{C}$ by the modular
tensor category $\mathbf{Rep}_{k}(\widehat{\mathfrak{g}})$ at level
$k = \langle c_{2}, [M] \rangle$ (Reshetikhin--Turaev).  Both regimes
establish existence.  No universal-property uniqueness holds: a QOU is
a *structure*, not a universal object.

The proof is constructive: we exhibit $(\mathbf{C}, A, \tau)$ and
verify the four axioms in
[proof of QOU existence](#prf:quantum-observable-universe-exists).

\cite{woronowicz1987, woronowicz1988, reshetikhin1991, kassel1995, chari1994}
