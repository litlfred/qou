The Skein binding Lagrangian
([Skein binding Lagrangian](#def:skein-binding-lagrangian)) is
the canonical action $\mathcal{S}_q$
([canonical action](#def:qou-canonical-action)) evaluated on the
multi-nucleon Hopf link.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q$, categorical Lagrangian $\mathcal{L}_q$
([categorical Lagrangian](#def:categorical-lagrangian)), and
canonical action $\mathcal{S}_q = \mathrm{tr}(\mathcal{L}_q)$.
Let $L = p\,\mathfrak{p} \bowtie n\,\mathfrak{n}$ be a
multi-nucleon Hopf link with $p$ protons
([categorical proton](#def:categorical-proton)) and $n$ neutrons
([categorical neutron](#def:categorical-neutron)).  Then

$$
  \mathcal{S}_q\big|_{\psi = L}
  \;=\;
  \underbrace{E_0}_{\text{gravity (const.)}}
  \;+\;
  \mathcal{L}_{\mathrm{bind}}[L]
$$

where $E_0 = \mathrm{tr}(q \cdot R_{\int})$ is a constant
independent of $(p, n)$ and $\mathcal{L}_{\mathrm{bind}}$ is
the five-term Skein binding Lagrangian.

**Proof.**
The canonical action decomposes as
$\mathcal{S}_q = \mathcal{S}_{\mathrm{grav}}
+ \mathcal{S}_{\mathrm{gauge}}
+ \mathcal{S}_{\mathrm{matter}}$.
We evaluate each sector on the state
$\psi = L = p\,\mathfrak{p} \bowtie n\,\mathfrak{n}$.

*Step 1: Gravity sector.*
The gravity term $\mathcal{S}_{\mathrm{grav}} =
\mathrm{tr}(q \cdot R_{\int})$ depends on the Frobenius--Ricci
curvature $R_{\int}$, which is a property of the Frobenius--Hopf
object $A$ alone — not of the state $\psi$.  It is therefore
constant in $(p, n)$ and equals $E_0$.

*Step 2: Gauge sector — volume and surface.*
The gauge term is

$$
  \mathcal{S}_{\mathrm{gauge}}
  \;=\;
  \int_A \!\circ\, \mathrm{tr}_A\!\bigl(
    F_\nabla \wedge_q \star_q F_\nabla
  \bigr).
$$

When $\psi = L$, the curvature $F_\nabla = \nabla^2$ is supported
on the Hopf junctions of the multi-nucleon link.  Each
nearest-neighbour nucleon pair $(i, j)$ contributes a junction with
curvature localised at the crossing.  The $q$-deformed wedge
product $\wedge_q$ evaluates to the Skein weight
$\mathcal{S}_{ij}(q)$ at each crossing (this is the definition of
$\wedge_q$ on the Hecke algebra
[R-matrix braiding](#def:r-matrix-braiding)).

Summing over all junctions and separating bulk from boundary:

$$
  \mathcal{S}_{\mathrm{gauge}}\big|_L
  \;=\;
  \sum_{\substack{(i,j) \\ \text{bulk}}} \mathcal{S}_{ij}(q)
  \;-\;
  \sum_{\substack{(i,j) \\ \text{boundary}}} \delta\mathcal{S}_{ij}
$$

The bulk sum counts $\sim A$ junctions, each with average weight
$\tfrac{1}{2}(q + q^{-1}) \cdot \lambda_V$, giving
$\mathcal{L}_{\mathrm{vol}}$.  The boundary deficit (nucleons with
fewer neighbours) subtracts $\sim A^{2/3}$ junctions, giving
$\mathcal{L}_{\mathrm{surf}}$.

*Step 3: Gauge sector — Coulomb splitting.*
The Skein weight $\mathcal{S}_{ij}(q)$ at a crossing depends on
the crossing sign, which is determined by the relative meridional
winding of nucleons $i$ and $j$
([crossing asymmetry](#rem:skein-crossing-asymmetry)):

- $\mathfrak{p}$--$\mathfrak{p}$: positive crossings, weight $q$
- $\mathfrak{p}$--$\mathfrak{n}$: mixed, weight
  $\tfrac{1}{2}(q + q^{-1})$
- $\mathfrak{n}$--$\mathfrak{n}$: negative crossings, weight
  $q^{-1}$

Separating the $\mathfrak{p}$--$\mathfrak{p}$ excess from the
baseline:

$$
  \sum_{(i,j)} \mathcal{S}_{ij}
  \;=\;
  \underbrace{%
    \frac{q + q^{-1}}{2} \cdot (\text{all pairs})
  }_{\text{baseline (already in vol + surf)}}
  \;+\;
  \underbrace{%
    \frac{q - q^{-1}}{2} \cdot \binom{p}{2}
  }_{\text{Coulomb excess}}
  \;-\;
  \underbrace{%
    \frac{q - q^{-1}}{2} \cdot \binom{n}{2}
  }_{\text{nn attractive correction}}
$$

The Coulomb term $\mathcal{L}_{\mathrm{Coul}}$ is the
$\mathfrak{p}$--$\mathfrak{p}$ excess, scaled by $1/A^{1/3}$ from
the geometric radius of the link.  The $\mathfrak{n}$--$\mathfrak{n}$
attractive correction is absorbed into the effective volume term
(it contributes equally to all large-$A$ nuclei along the
stability line where $n \approx p$).

*Step 4: Matter sector — Pauli and pairing.*
The matter term is

$$
  \mathcal{S}_{\mathrm{matter}}
  \;=\;
  \int_A\!\bigl(\psi^* \cdot \mathcal{D}_\nabla\,\psi\bigr).
$$

When $\psi = L$, the Dirac operator
([categorical Dirac operator](#def:categorical-dirac-operator))
$\mathcal{D}_\nabla = q^{-1}\nabla + (1 - q^{-1})\iota_\xi\nabla$
acts on each nucleon in $L$.  The adjoint section
$\psi^* = \int_A \circ S(\psi)$ pairs nucleons via the antipode.

For identical nucleons ($\mathfrak{p}\mathfrak{p}$ or
$\mathfrak{n}\mathfrak{n}$ pairs), the hadron
([hadron](#def:hadron)) uses the antisymmetric product, imposing
$\psi^* \cdot \psi = -\psi \cdot \psi^*$.  The cost of this
antisymmetry, when $n \neq p$, is the asymmetry energy:

$$
  \mathcal{S}_{\mathrm{matter}}\big|_{\text{asymmetry}}
  \;=\;
  \lambda_A \cdot \frac{(n - p)^2}{4A}
  \;=\; \mathcal{L}_{\mathrm{Pauli}}.
$$

When $p$ and $n$ are both even, the nucleon pairs form closed Hopf
loops under the antipode pairing, contributing an additional
binding $\pm \lambda_P / A^{1/2}$ — the pairing term
$\mathcal{L}_{\mathrm{pair}}$.

*Step 5: Assembly.*
Combining steps 1--4:

$$
  \mathcal{S}_q\big|_L
  \;=\;
  E_0
  \;+\;
  \bigl(\mathcal{L}_{\mathrm{vol}}
  - \mathcal{L}_{\mathrm{surf}}
  - \mathcal{L}_{\mathrm{Coul}}
  - \mathcal{L}_{\mathrm{Pauli}}
  + \mathcal{L}_{\mathrm{pair}}\bigr)
  \;=\;
  E_0 + \mathcal{L}_{\mathrm{bind}}[L].
$$

The nuclear binding energy is therefore not an independent
physical input but a direct evaluation of the categorical
canonical action at the multi-nucleon Hopf link configuration.
The substrate parameter $q$ controls all five terms: strong
binding via $(q + q^{-1})/2$, electromagnetic repulsion via
$(q - q^{-1})/2$, and fermionic exclusion via the
$q$-deformed Dirac operator.
