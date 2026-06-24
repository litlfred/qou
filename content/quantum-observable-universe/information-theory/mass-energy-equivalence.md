**Theorem (mass--energy equivalence).**
*Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be an archimedean quantum
observable universe with substrate parameter $q$ and speed of light
$c_q = 1/(q-1)$
([speed of light](#def\:information-speed-of-light)).  Let
$\mathfrak{H}$ be a knot composite in the Frobenius--Hopf object $A$.  Then
the crossing energy
([crossing energy](#def\:crossing-energy)) and the categorical mass
([mass identity](#def\:mass-identity)) satisfy*

$$
  E_{\mathfrak{H}}
  =  \mathfrak{m}_{\mathfrak{H}} \cdot c_q^2
  =  \frac{\mathfrak{m}_{\mathfrak{H}}}{(q - 1)^2}.
$$

**Content of the theorem.**
This is not a unit convention.  The crossing energy (an algebraic
quantity: the Skein weight from $R$-matrix braiding) equals the
categorical mass (an analytic quantity: the trace norm through
the Frobenius pairing and comultiplication) multiplied by the
**square of the information speed** --- the square of the ratio
of spatial to temporal coupling in the $q$-connection.

The factor $c_q^2 = 1/(q-1)^2$ has a direct information-theoretic
interpretation: it converts the *resistance to vertical
(Reeb) transport* (mass) into the *horizontal (spatial) crossing
weight* (energy) by accounting for the mismatch between horizontal
and vertical information rates in the $q$-connection.

*

$$

**Regime behaviour of $E = \mathfrak{m} \cdot c_q^2$.**

| Regime          | $q$            | $c_q^2$         | Physics                                                          |
| --------------- | -------------- | --------------- | ---------------------------------------------------------------- |
| Deep-quantum    | $q \to \infty$ | $\to 0$         | Energy $\to 0$ for any mass: no spatial crossing weight          |
| Deep quantum    | $\varphi^2$    | $\approx 0.382$ | Sub-relativistic: mass dominates energy                          |
| Our universe    | $q_0$          | $\approx 83.2$  | $E \approx 83\mathfrak{m}$: large amplification                  |
| Near-classical  | $1.01$         | $10{,}000$      | Extreme amplification: tiny mass $\to$ large energy              |
| Classical limit | $q \to 1^+$    | $\to \infty$    | $E/\mathfrak{m} \to \infty$: classical $E = mc^2$ with $c$ large |

At $q = q_0$, a vortex with categorical mass $\mathfrak{m}$
carries crossing energy
$E = \mathfrak{m}/(q-1)^2 \approx 83\mathfrak{m}$.
This large amplification factor is the QOU explanation for why
nuclear energy ($E = mc^2$) releases vastly more energy than the
rest mass would suggest in everyday units.

**Consistency check: electron.**
The electron (left trefoil $T_{2,3}$) has $n_c = 3$ positive
crossings:

* Crossing energy: $E_{e^-} = 3q \approx 3.330$
  Skein units.
* Predicted mass: $\mathfrak{m}_{e^-} = E \cdot (q-1)^2 = 3q(q-1)^2$.

At $q = q_0$: $\mathfrak{m}_{e^-} = 3 q_0 \times 0.01203 \approx 0.0401$ (in Reeb mass units).

**Pair creation reinterpreted.**
The pair production threshold
([pair creation energy](#rem\:pair-creation-energy)) becomes:

$$
  E_{\gamma}  \geq 
  (\mathfrak{m}_{e^-} + \mathfrak{m}_{e^+}) \cdot c_q^2
  =  \frac{\mathfrak{m}_{e^-} + \mathfrak{m}_{e^+}}{(q-1)^2}.
$$

The net crossing energy of the pair is
$E_{e^-} + E_{e^+} = 3(q - q^{-1}) \approx 0.630$ (pure Coulomb repulsion).  But the minimum photon
energy must supply both **absolute** crossing energies:
$|E_{e^-}| + |E_{e^+}| = 3q + 3q^{-1} = 3(q + q^{-1}) = 6\cosh(\ln q) \approx 6.033$ Skein units.

**Archimedean realisation.**
Over $\mathbb{C}$, the categorical mass is realised as Yekutieli's
nonabelian multiplicative integral \[yekutieli2015]
([mass over $\mathbb{C}$](#ex\:mass-identity-C)), and
$E_{\mathfrak{H}} = \mathfrak{m}_{\mathfrak{H}} \cdot c_q^2$ becomes

$$
  \sum_{\text{crossings}} \epsilon_i
  = 
  \frac{1}{(q-1)^2}
  \bigl\lVert
  \mathrm{MI}\!\!\int_\Sigma
  (\nabla_A q, L \wedge F^+)
  \bigr\rVert,
$$

identifying the discrete Skein weight (spatial) with the rescaled
continuous multiplicative-integral norm (temporal).
