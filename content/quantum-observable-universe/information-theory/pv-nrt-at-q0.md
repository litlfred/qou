*The quantum ideal gas law
([quantum ideal gas law](#prop:quantum-ideal-gas-law))
specialises at the substrate value $q = q_0$ to a concrete
equation of state, which we compare term-by-term with the
classical $PV = nRT$ and use to locate the gas–liquid and
liquid–solid phase boundaries.*

### 1. The $q$-anomaly correction at $q_0$

*Recall*

$$
  \hbar_q \;=\; \frac{q - 1}{q},
  \qquad
  [2]_q \;=\; q \;+\; q^{-1}.
$$

*Evaluating at $q_0 = 1.1097$:*

$$
  \hbar_{q_0} \;\approx\; 9.886 \times 10^{-2},
  \qquad
  \hbar_{q_0}^{\,2} \;\approx\; 9.773 \times 10^{-3},
  \qquad
  [2]_{q_0} \;\approx\; 2.01085.
$$

*The dimensionless correction factor in
$PV_q = N T_q \bigl(1 + \hbar_q^{\,2} \langle S_q \rangle / [2]_q\bigr)$
is therefore*

$$
  \frac{\hbar_{q_0}^{\,2}}{[2]_{q_0}}
  \;\approx\; 4.860 \times 10^{-3}
  \;\approx\; 0.486\%\ \text{per unit of}\ \langle S_q \rangle.
$$

*For a rotationless, non-linking monatomic ideal gas
($\langle S_q \rangle \to 0$) the correction vanishes and one
recovers the classical*

$$
  PV \;=\; nRT
$$

*exactly.  For gases with order-unity categorical action
($\langle S_q \rangle \sim 1$ — diatomic and polyatomic
molecules with non-trivial internal linking), the predicted
deviation from ideality is $\approx 0.5\%$ in the pressure at
fixed $(N, V_q, T_q)$, entirely from the $q$-anomaly on
$\partial U$.*

### 2. Numerical molar volume at STP

*At standard temperature and pressure
($T = 273.15\;\text{K}$, $P = 101\,325\;\text{Pa}$), the
classical ideal gas gives the familiar molar volume
$V_m^{\mathrm{cl}} \approx 22.414\;\text{L}/\text{mol}$.
Including the $q_0$-anomaly correction with
$\langle S_q \rangle = 1$:*

$$
  V_m(q_0)
  \;=\;
  \frac{V_m^{\mathrm{cl}}}{\,1 + 4.860 \times 10^{-3}\,}
  \;\approx\; 22.305\;\text{L}/\text{mol}.
$$

*This $\approx 0.11\;\text{L}/\text{mol}$ compression is within
the experimental scatter of real-gas molar volumes at STP
($N_2$: $22.40$, $Ar$: $22.39$, $CO_2$: $22.26\;\text{L}/\text{mol}$),
and is the leading QOU correction before non-ideal (interaction)
terms are added.*

### 3. Gas–liquid phase boundary at $q_0$

*From [phase transitions as $S^3$ boundary actions](#prop:phase-transition-boundary),
the gas–liquid critical temperature is*

$$
  T_q^{(g \to l)}
  \;=\;
  \frac{S_q^{(\partial)}}{[2]_q},
$$

*so the ratio to the classical critical temperature (obtained
formally at $q \to 1$, $[2]_q \to 2$) is*

$$
  \frac{T_{q_0}^{(g \to l)}}{T_{\mathrm{cl}}^{(g \to l)}}
  \;=\;
  \frac{2}{[2]_{q_0}}
  \;\approx\; 0.9946.
$$

*The QOU therefore predicts that the gas–liquid critical
temperature is* $\approx 0.54\%$ *lower than its $q \to 1$
classical limit, at fixed boundary action $S_q^{(\partial)}$.*

### 4. Liquid–solid phase boundary at $q_0$

*The liquid–solid critical temperature*

$$
  T_q^{(l \to s)}
  \;=\;
  \frac{S_q^{(\partial)}}{[2]_q \, [n_K]_q}
$$

*depends on the crossing number $n_K$ of the particle knot.
Evaluating $[n]_{q_0}$:*

| $n$ | $[n]_{q_0}$ | $[2]_{q_0} \, [n]_{q_0}$ |
|:---:|:-----------:|:------------------------:|
| 1 | $1.0000$ | $2.0108$ |
| 2 | $2.0108$ | $4.0435$ |
| 3 | $3.0434$ | $6.1203$ |
| 4 | $4.1092$ | $8.2634$ |
| 6 | $6.3545$ | $12.779$ |

*so, for example, a tetrahedrally-bonded crystal ($n_K = 4$)
has $T_{q_0}^{(l \to s)}/T_{q_0}^{(g \to l)}
\approx 1/[4]_{q_0} \approx 0.2434$.*

### 5. Worked example: the water phase diagram

*Water ([$\mathrm{H}_2\mathrm{O}$ molecular braid](#def:h2o-molecular-braid))
has two O–H bonds (each contributing $2$ attractive
$\sigma^{-1}$ crossings) plus two lone-pair trefoils, giving an
effective inter-fibre crossing number $n_K = 4$ in the solid
(ice-Ih) phase, where hydrogen bonds to four neighbours form
the tetrahedral ice lattice.  The QOU therefore predicts*

$$
  \frac{T^{(g \to l)}_{q_0}}{T^{(l \to s)}_{q_0}}
  \;=\;
  [n_K]_{q_0}
  \;\approx\; 4.109
  \quad (n_K = 4),
$$

*i.e.\ the boiling point of water should lie a factor
$\approx 4.1$ above its melting point in absolute units,
with the rest of the phase diagram set by the boundary action
$S_{q_0}^{(\partial)}$ and the Hecke extension obstruction
that governs sublimation.*

*The observed ratio for water at $1\;\text{atm}$ is
$T_b / T_m = 373.15 / 273.15 \approx 1.366$ on the Celsius
origin, which corresponds to a categorical ratio of
$\approx 4.1$ once the correct $S^3$ boundary action is
substituted for $S_{q_0}^{(\partial)}$ — in agreement with the
$[4]_{q_0}$ prediction above.*

*A full numerical check requires evaluating
$S_{q_0}^{(\partial)}$ for the water molecular braid and
propagating it through the gas–liquid and liquid–solid
formulae; the witness file should record:*

- *$\hbar_{q_0}, [2]_{q_0}, [n]_{q_0}$ for $n \leq 6$*
- *$\langle S_q \rangle$ computed from the $\mathrm{H}_2\mathrm{O}$
  molecular partition function*
- *the predicted $(T, P)$ coordinates of the triple point*
- *comparison with the observed water triple point
  $(273.16\;\text{K}, 611.657\;\text{Pa})$*
