> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](../braids-and-knots/mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](../braids-and-knots/rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

## Mass-volume factorization

**Parent statement:** The general volume-density factorization
$\mathfrak{m}(K) = \mathrm{Vol}(K) \cdot \rho_q$, with substrate
drag density $\rho_q = 1/\hbar_q^2$, is established in
[Kashaev volume-density](#rem:kashaev-volume-density). This block
specializes that formula to **atomic links** for the nuclear
binding regime.

At the particle-mass scale, the Kashaev-volume-density formula
gives $\mathfrak{m} = \mathrm{Vol}/\hbar_q^2 \approx 102 \cdot
\mathrm{Vol}$ in $m_e$ units (pinned via
$\mathfrak{m}(4_1) = m_\mu / m_e$). At the nuclear-binding
scale — orders of magnitude below particle mass — the factorization
takes a specialized form with the same geometric volume but a
**physical-scale density** $\rho_F$ instead of the categorical
$\rho_q$:

## Statement

**Conjecture.**
*Let $\mathcal{K}$ be the atomic braid of a derived atom
$\mathcal{A}(Z, N)$ ([atomic braid](#def:atomic-braid)), and let
$S^3 \setminus \overline{\mathcal{K}}$ denote the braid-closure
complement in the 3-sphere. Then the categorical mass endomorphism
factorizes as*

$$
  \mathfrak{m}_{\mathcal{K}}(q)
  \;=\;
  \rho(q, \mathcal{K}) \cdot V_{\mathrm{hyp}}(\overline{\mathcal{K}}),
$$

*where $V_{\mathrm{hyp}}$ is the hyperbolic volume computed via the
[Thurston sum](#prop:thurston-volume-additivity), and $\rho(q,
\mathcal{K})$ is the **Frobenius packing density** determined by
which Wedderburn blocks of $H_{3A}(q)$ are populated by
$\mathcal{K}$.*

## JSJ refinement

Applying the Jaco-Shalen-Johannson decomposition of the
complement $S^3 \setminus \overline{\mathcal{K}}$ into Seifert-fibered
and hyperbolic pieces $P_1, \ldots, P_k$, the formula refines to a
sum over hyperbolic pieces:

$$
  B(Z, N) \;=\; \sum_{P_i \text{ hyperbolic}}
  \rho_F(P_i) \cdot V_{\mathrm{hyp}}(P_i),
$$

where:

- **Seifert pieces** (torus-knot nucleons, $T_{m,n}$-type) contribute
 $V_{\mathrm{hyp}} = 0$ by [Thurston additivity](#prop:thurston-volume-additivity).
- **Hyperbolic pieces** (inter-nucleon glue, closed-shell
 Borromean-type links) carry the binding.
- The density $\rho_F(P_i)$ takes one of two values:

$$
  \rho_F(P_i)
  \;=\;
  \begin{cases}
    m_e & \text{if } P_i \text{ is single-chirality
                    (sym + std blocks only),} \\
    2 m_e & \text{if } P_i \text{ is CPT-saturated
                      (sym + std + alt blocks).}
  \end{cases}
$$

The factor $2 m_e$ is the $\gamma\gamma$ pair-creation threshold;
it arises whenever the alt Wedderburn block is non-by definition
populated, doubling the effective packing (see
[Frobenius packing density](#rem:frobenius-packing-density)).

## Supporting evidence

Pinning $\rho \in \{m_e, 2m_e\}$ and computing the hyperbolic volume
of the atomic link complement reproduces nuclear binding energies for
doubly-magic atoms within $\leq 6.2\%$:
${}^4\mathrm{He}$, ${}^{12}\mathrm{C}$, ${}^{16}\mathrm{O}$. For
light atoms, the atomic link complement is itself a named hyperbolic
knot from the standard census:

| atom | link / knot | $V$ | $\rho$ | $B_{\text{pred}}$ | $B_{\text{AME}}$ |
|:-----|:------------|:----|:-------|:------------------|:-----------------|
| D | $6_2$ | $4.400$ | $m_e$ | $2.249$ MeV | $2.225$ MeV |
| T | $8_{11}$ | $8.286$ | $2m_e$ | $8.468$ MeV | $8.482$ MeV |
| ${}^3\mathrm{He}$ | Borromean | $8G$ | $2m_e$ | $7.493$ MeV | $7.718$ MeV |
| ${}^4\mathrm{He}$ | 4 Borromean components | $4 \cdot 8G$ | $2m_e$ | $29.96$ MeV | $28.30$ MeV |

(Values from the atom-volume witness and AME2020. The ${}^4\mathrm{He}$
row gives the **first-principles geometric prediction**
$2m_e \cdot 4 \cdot 8G = 29.96$ MeV; the closed-shell refinement used
for larger atoms in [crossing-graded-mass-expansion](#conj:crossing-graded-mass-expansion)
uses the α-cluster baseline $B({}^4\mathrm{He}) = 28.30$ MeV directly
from AME. The $4 \cdot 8G$ notation denotes four Borromean-rings
complements summed — not the braid group $B_3$.)

### Not zero free parameters — the atom-to-link mapping gap

The $\leq 6.2\%$ above is obtained with a **per-atom choice** of both the
link/knot and the density $\rho \in \{m_e, 2m_e\}$; neither is yet
derived (see "Why this is a conjecture", points 1–2). The choices are
mutually **inconsistent**: D uses $6_2$ ($V=4.400$) whereas the
binding-link census assigns D the Hopf link ($V=0$,
[binding-link-volumes.witness.json](../../../computations/binding-link-volumes.witness.json)),
and ${}^3\mathrm{He}$ uses one Borromean copy ($8G$) while
${}^4\mathrm{He}$ uses four ($4\cdot 8G$). The companion probe
[rho-f-volume-binding-gap.witness.json](../../../computations/rho-f-volume-binding-gap.witness.json)
inverts $\rho_F\cdot V_{\mathrm{hyp}} = \Delta_{\mathrm{binding}}$ and
finds **no** fixed link primitive reproduces the light-isotope bindings
with $\rho \in \{m_e, 2m_e\}$ (`matches_within_10pct: []`; ${}^4$He
needs $\rho_F/m_e \approx 7.6$ on a single Borromean copy, not $2$).
The result is therefore a **per-isotope fit of the (link, $\rho$)
pair**, not a zero-parameter prediction — until the atom-to-link map and
the $\rho_F$ rule are derived.

## Why this is a conjecture

Factorization requires:

1. The atomic link complement admits a canonical JSJ decomposition
 compatible with the ambient Hecke algebra grading — verified
 computationally per atom, not proved in general.
2. The density $\rho_F(P_i)$ is determined locally by the Wedderburn
 profile of $P_i$ — stated but not derived from first principles
 (see [Frobenius packing density](#rem:frobenius-packing-density)).
3. The categorical mass endomorphism and the topological
 Thurston volume are literally equal (not only proportional with
 a $q$-dependent prefactor hidden in $\rho$) — this is the
 **volume conjecture at real $q$**, parallel to the classical
 statement \cite{murakami-murakami2001} at $q \to e^{2\pi i/N}$.
