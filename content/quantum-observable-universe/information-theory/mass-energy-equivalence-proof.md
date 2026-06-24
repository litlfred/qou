*
The proof proceeds via the Reshetikhin--Turaev invariant in a ribbon
category, with the $q$-connection decomposition providing the
conversion factor.

*Step 1: Ribbon trace computes crossing energy.*
In the rigid :refterm[monoidal category]{#monoidal-category} $\mathbf{C}$, the Frobenius--Hopf
object $A$ carries a ribbon structure (braiding + twist).  For a
composite $\mathfrak{H}$ represented by the braid word
$\beta \in B_n$, the Reshetikhin--Turaev construction \[reshetikhin1991]
gives

$$
  \mathrm{tr}_{\mathrm{ribbon}}(\rho(\beta))
  = 
  \sum_{\text{crossings in } \beta}
  \begin{cases}
    q   & \text{positive crossing}, \\
    -q^{-1} & \text{negative crossing}.
  \end{cases}
$$

The right-hand side is $E_{\mathfrak{H}}$.  Each crossing
weight is a *spatial* quantity: it measures the $R$-matrix coupling
between horizontally adjacent fibres at strength $q^{\pm 1}$.

*Step 2: Categorical mass measures vertical resistance.*
The categorical mass of a closed vortex
$\varrho \colon \mathbf{1} \to A$ is

$$
  \mathfrak{m}_\varrho
  = 
  \bigl\lVert
    \mathrm{tr}\bigl(
      (\textstyle\int_A \otimes \mathrm{id})
      \circ \Delta \circ \varrho
    \bigr)
  \bigr\rVert
$$

where $\varrho$ denotes a generic closed vortex (morphism from
the unit object).  The Frobenius form $\int_A$ and the
comultiplication $\Delta$ encode the $q$-connection.  The mass
measures resistance to transport through the comultiplication ---
a *vertical* (Reeb) quantity, since $\Delta$ encodes the
$q$-connection whose temporal component has weight $\hbar_q$.

*Step 3: The speed-of-light conversion.*
The $q$-connection $A_q = q^{-1}A + \hbar_q\iota_\xi A\varTheta$
assigns weight $q^{-1}$ to each spatial crossing and weight $\hbar_q$
to each temporal tick.  The ribbon trace sums spatial crossing
weights ($q^{\pm 1}$), while the categorical mass sums temporal
transport costs ($\hbar_q$ per step through $\Delta$).  Each
crossing contributes $q^{\pm 1}$ to energy and
$q^{\pm 1} \cdot \hbar_q / q^{-1} = q^{\pm 1} \cdot (q-1)$ to
mass.  The ratio is:

$$
  \frac{E_{\mathfrak{H}}}{\mathfrak{m}_{\mathfrak{H}}}
  =  \frac{q^{-1}}{\hbar_q}
  \cdot \frac{q^{-1}}{\hbar_q}
  =  c_q^2
  =  \frac{1}{(q-1)^2}.
  \qquad
$\qquad\blacksquare$
