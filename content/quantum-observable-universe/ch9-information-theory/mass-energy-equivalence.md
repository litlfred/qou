**Theorem (mass--energy equivalence).**
*Let $(\mathbf{C}, \theta, G, \mathcal{S})$ be an archimedean quantum
observable universe with substrate parameter $q$ and speed of light
$c(q) = 1/(q-1)$
([speed of light](#def:information-speed-of-light)).  Let
$\gamma \colon \mathbf{1} \to A$ be a closed vortex in the
Frobenius--Hopf object $A$.  Then the crossing energy
([crossing energy](#def:crossing-energy)) and the categorical mass
([mass identity](#def:mass-identity)) satisfy*

$$
  E_{\mathrm{cross}}(\gamma)
  \;=\; m(\gamma) \cdot c(q)^2
  \;=\; \frac{m(\gamma)}{(q - 1)^2}.
$$

**Content of the theorem.**
This is not a unit convention.  The crossing energy (an algebraic
quantity: the Skein weight from $R$-matrix braiding) equals the
categorical mass (an analytic quantity: the trace norm through
the Frobenius pairing and comultiplication) multiplied by the
**square of the information speed** --- the square of the ratio
of spatial to temporal coupling in the $q$-connection.

The factor $c(q)^2 = 1/(q-1)^2$ has a direct information-theoretic
interpretation: it converts the *resistance to vertical
(Reeb) transport* (mass) into the *horizontal (spatial) crossing
weight* (energy) by accounting for the mismatch between horizontal
and vertical information rates in the $q$-connection.

**Proof sketch.**
The proof proceeds via the Reshetikhin--Turaev invariant in a ribbon
category, with the $q$-connection decomposition providing the
conversion factor.

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
    -q^{-1} & \text{negative crossing}.
  \end{cases}
$$

The right-hand side is $E_{\mathrm{cross}}(\gamma)$.  Each crossing
weight is a *spatial* quantity: it measures the $R$-matrix coupling
between horizontally adjacent fibres at strength $q^{\pm 1}$.

*Step 2: Categorical mass measures vertical resistance.*
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

evaluates the composition coev $\to$ ($f \otimes$ id) $\to$ ev
through the Frobenius form $\int_A$ and the comultiplication
$\Delta$.  The Frobenius form is the categorical analog of the
invariant integral.  The mass measures resistance to transport
through the comultiplication --- a *vertical* (Reeb) quantity,
since $\Delta$ encodes the $q$-connection whose temporal component
has weight $\hbar_q$.

*Step 3: The speed-of-light conversion.*
The $q$-connection $A_q = q^{-1}A + \hbar_q\,\iota_\xi A\;\theta$
assigns weight $q^{-1}$ to each spatial crossing and weight $\hbar_q$
to each temporal tick.  The ribbon trace sums spatial crossing
weights ($q^{\pm 1}$), while the categorical mass sums temporal
transport costs ($\hbar_q$ per step through $\Delta$).  Each
crossing contributes $q^{\pm 1}$ to energy and
$q^{\pm 1} \cdot \hbar_q / q^{-1} = q^{\pm 1} \cdot (q-1)$ to
mass.  The ratio is:

$$
  \frac{E_{\mathrm{cross}}}{m}
  \;=\; \frac{q^{-1}}{\hbar_q}
  \cdot \frac{q^{-1}}{\hbar_q}
  \;=\; c(q)^2
  \;=\; \frac{1}{(q-1)^2}.
  \qquad\square
$$

**Regime behaviour of $E = mc^2$.**

| Regime | $q$ | $c(q)^2$ | Physics |
|--------|-----|----------|---------|
| Big Bang | $q \to \infty$ | $\to 0$ | Energy $\to 0$ for any mass: no spatial crossing weight |
| Deep quantum | $\varphi^2$ | $\approx 0.382$ | Sub-relativistic: mass dominates energy |
| Our universe | $1.1097$ | $\approx 83.2$ | $E \approx 83\,m$: large amplification |
| Near-classical | $1.01$ | $10{,}000$ | Extreme amplification: tiny mass $\to$ large energy |
| Classical limit | $q \to 1^+$ | $\to \infty$ | $E/m \to \infty$: the classical $E = mc^2$ with $c$ large |

At $q = 1.1097$, a vortex with categorical mass $m$ carries
crossing energy $E = m/(q-1)^2 \approx 83\,m$.  This large
amplification factor is the QOU explanation for why nuclear energy
($E = mc^2$) releases vastly more energy than the rest mass would
suggest in everyday units.

**Consistency check: electron.**
The electron (left trefoil $T_{2,3}$) has $n_c = 3$ positive
crossings:

- Crossing energy: $E_{\mathrm{cross}}(e^-) = 3q \approx 3.330$
  Skein units.
- Predicted mass: $m(e^-) = E / c^2 = 3q \cdot (q-1)^2
  = 3q(q-1)^2$.

At $q = 1.1097$: $m(e^-) = 3 \times 1.1097 \times 0.01203
\approx 0.0401$ (in Reeb mass units).

**Pair creation reinterpreted.**
The pair production threshold
([pair creation energy](#rem:pair-creation-energy)) becomes:

$$
  E_{\gamma} \;\geq\; (m(e^-) + m(e^+)) \cdot c(q)^2
  \;=\; \frac{m(e^-) + m(e^+)}{(q-1)^2}.
$$

Since $E_{\mathrm{cross}}(e^-) + E_{\mathrm{cross}}(e^+) = 3q - 3q^{-1}
= 3(q - q^{-1}) \approx 0.630$ Skein units, the minimum photon
crossing energy for pair creation is $3(q + q^{-1}) = 6\cosh(\ln q)
\approx 6.033$ Skein units.

**Archimedean realisation.**
Over $\mathbb{C}$, the categorical mass is realised as Yekutieli's
nonabelian multiplicative integral [yekutieli2015]
([mass over $\mathbb{C}$](#ex:mass-identity-C)), and $E = mc^2$
becomes

$$
  \sum_{\text{crossings}} \epsilon_i
  \;=\;
  \frac{1}{(q-1)^2}\,
  \bigl\lVert\,
  \mathrm{MI}\!\!\int_\Sigma
  (\nabla_A q,\; L \wedge F^+)
  \,\bigr\rVert,
$$

identifying the discrete Skein weight (spatial) with the rescaled
continuous multiplicative-integral norm (temporal).
