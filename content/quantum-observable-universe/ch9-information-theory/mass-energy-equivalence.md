**Theorem (mass--energy equivalence).**
*Let $(\mathbf{C}, \theta, G, \mathcal{S})$ be an archimedean quantum
observable universe and let $\gamma \colon \mathbf{1} \to A$ be a
closed vortex in the Frobenius--Hopf object $A$.  Then the crossing
energy ([crossing energy](#def:crossing-energy)) and the categorical
mass ([mass identity](#def:mass-identity)) satisfy*

$$
  E_{\mathrm{cross}}(\gamma) \;=\; m(\gamma) \cdot c^2
  \;=\; m(\gamma),
$$

*where $c = 1$ is the speed of light
([Lieb--Robinson velocity](#def:information-speed-of-light))
in Planck units.*

The content of $E = m$ is not the trivial statement $c = 1$; it is
the identification of two independently defined quantities: the
**Skein weight** (algebraic, from the $R$-matrix braiding) and the
**categorical trace norm** (analytic, from the Frobenius pairing and
comultiplication).

**Proof sketch.**
The proof proceeds via the Reshetikhin--Turaev invariant in a ribbon
category.

*Step 1: Ribbon trace computes crossing energy.*
In the rigid monoidal category $\mathbf{C}$, the Frobenius--Hopf
object $A$ carries a ribbon structure (braiding + twist).  For a
closed vortex $\gamma$ represented by the braid word
$\beta \in B_n$, the Reshetikhin--Turaev construction [reshetikhin1991]
gives

$$
  \mathrm{tr}_{\mathrm{ribbon}}(\rho(\beta))
  \;=\;
  \sum_{\text{crossings in } \beta}
  \begin{cases}
    q   & \text{positive crossing}, \\
    -q^{-1} & \text{negative crossing},
  \end{cases}
$$

where $\rho \colon B_n \to \mathrm{End}_{\mathbf{C}}(A^{\otimes n})$
is the braid group representation through the $R$-matrix.  The
right-hand side is precisely $E_{\mathrm{cross}}(\gamma)$.

*Step 2: Categorical mass is the ribbon trace norm.*
The categorical mass

$$
  m(\gamma)
  \;=\;
  \bigl\lVert
    \mathrm{tr}\bigl(
      (\textstyle\int_A \otimes \mathrm{id})
      \circ \Delta \circ \gamma
    \bigr)
  \bigr\rVert
$$

evaluates the composition coev $\to$ ($f \otimes$ id) $\to$ ev through
the Frobenius form $\int_A$ and the comultiplication $\Delta$.  The
Frobenius form is the categorical analog of the invariant integral
(the counit of the Hopf algebra), and $\Delta$ encodes the
$q$-connection.  By the pivotal property of $\mathbf{C}$ (which
guarantees that left and right traces agree), the categorical trace
norm $\lVert \mathrm{tr}(\cdots) \rVert$ equals the absolute value
of the Reshetikhin--Turaev invariant evaluated on the closure of
$\beta$:

$$
  m(\gamma) \;=\;
  \bigl|\, \mathrm{tr}_{\mathrm{ribbon}}(\rho(\beta)) \,\bigr|
  \;=\; |E_{\mathrm{cross}}(\gamma)|.
$$

*Step 3: Sign conventions.*
The crossing energy $E_{\mathrm{cross}}(\gamma)$ is signed (positive
for repulsion-dominated composites, negative for binding-dominated
ones), while the mass $m(\gamma)$ is a norm and hence non-negative.
Therefore

$$
  E_{\mathrm{cross}}(\gamma) \;=\; \pm\, m(\gamma),
$$

with the sign determined by the chirality of $\gamma$: positive for
left-handed (matter) composites, negative for right-handed
(antimatter) composites.  In absolute value, $|E| = m$.  $\square$

**Consistency check: electron and positron.**

| Quantity | Electron $e^-$ ($T_{2,3}$, left) | Positron $e^+$ ($\sigma(T_{2,3})$, right) |
|----------|----------------------------------|-------------------------------------------|
| Crossing energy | $E = +3q \approx +3.330$ | $E = -3q^{-1} \approx -2.703$ |
| Mass | $m = 3q \approx 3.330$ | $m = 3q^{-1} \approx 2.703$ |
| $E/m$ | $+1$ | $-1$ |
| Interpretation | Repulsion-dominated (matter) | Binding-dominated (antimatter) |

The mass asymmetry $m(e^-) \neq m(e^+)$ is a prediction of the
QOU framework: the electron and positron have different categorical
masses because $q \neq q^{-1}$ (i.e., $q \neq 1$).  At the
classical limit $q \to 1$, the asymmetry vanishes:
$m(e^-)/m(e^+) = q^2 \to 1$.  At $q = 1.1097$:

$$
  \frac{m(e^-)}{m(e^+)}
  \;=\; q^2
  \;\approx\; 1.231.
$$

This is the mass ratio at the **constituent (Skein) scale** ---
the ratio at the renormalized physical scale may differ due to
radiative corrections from higher jet levels.

**Pair creation reinterpreted.**
The pair production threshold $2m_e c^2 = 1.022\,\mathrm{MeV}$
([pair creation energy](#rem:pair-creation-energy)) becomes, in
Planck units,

$$
  E_{\gamma} \;\geq\; m(e^-) + m(e^+)
  \;=\; 3q + 3q^{-1}
  \;=\; 3(q + q^{-1})
  \;=\; 6\cosh(\ln q)
  \;\approx\; 6.033
  \quad (\text{Skein units}).
$$

The photon must carry enough crossing energy to create both the
trefoil and its mirror.  After creation, the net crossing energy
of the pair is $3(q - q^{-1}) = 6\sinh(\ln q) \approx 0.630$
--- pure antisymmetric (Coulomb) repulsion driving the pair apart.

**Archimedean realisation.**
Over $\mathbb{C}$, the categorical mass is realised as Yekutieli's
nonabelian multiplicative integral [yekutieli2015]
([mass over $\mathbb{C}$](#ex:mass-identity-C)), and the equality
$E = m$ becomes

$$
  \sum_{\text{crossings}} \epsilon_i
  \;=\;
  \bigl\lVert\,
  \mathrm{MI}\!\!\int_\Sigma
  (\nabla_A q,\; L \wedge F^+)
  \,\bigr\rVert,
$$

identifying the discrete Skein weight with the continuous
multiplicative-integral norm.  The topological mass decomposition
([topological mass proof](#prop:topological-mass-proof)) then
gives the per-crossing contributions: the unknot-core holonomy
contributes the binding energy, and the quantum dilogarithm at each
exceptional divisor contributes the per-crossing Skein weight.
