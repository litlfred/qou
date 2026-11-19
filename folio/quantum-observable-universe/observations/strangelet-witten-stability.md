Witten \cite{witten1984} conjectured that strange quark matter (SQM)—bulk matter with equal numbers of up, down, and strange quarks—is the absolute ground state of hadronic matter at zero pressure. 

The [strangelet crossing energy](#prop:strangelet-crossing-energy) provides a translation of Witten's hypothesis.

**Crossing-energy argument.**
The strangelet proposition yields three facts.
1. SQM is electromagnetically neutral ($Q = 0$).
2. Its crossing energy is purely strong.
3. Its strong binding per baryon exceeds neutron matter by a factor of $4/3$.

Replacing down quarks ($T_{2,3}^{\sigma}$, $3$ negative crossings) with strange quarks ($T_{2,5}^{\sigma}$, $5$ negative crossings) grants each baryon $2q^{-1}$ additional strong binding. At $q = q_0$, this gives $1.802$ Skein units per baryon.

**Jones polynomial obstruction.**
If crossing energy dominated, strange matter would be the ground state. However, all torus knots have zero hyperbolic volume. The mass of a baryon derives entirely from the Borromean linking, not the constituent knots ([building block knots](#rem:building-block-knots)). The strange quark is heavier because of its Jones polynomial.

The terminal resolution ([terminal resolution](#prop:terminal-resolution)) decomposes each hadronic link into a sum of unknots and Hopf links. These are weighted by coefficients dependent on the constituent Jones polynomials. At $q = q_0$:

| Quark | Knot | Jones polynomial | $\lvert J(q_0)\rvert$ |
|-------|------|-----------------|:-------------:|
| Up $\mathfrak{u}$ | $T_{2,3}$ | $-q^{-4} + q^{-3} + q^{-1}$ | $0.973$ |
| Down $\mathfrak{d}$ | $T_{2,3}^{\sigma}$ | $-q^{4} + q^{3} + q$ | $0.960$ |
| Strange $\mathfrak{s}$ | $T_{2,5}^{\sigma}$ | $-q^{10} + q^{9} - q^{8} + q^{7} + q^{5}$ | $1.176$ |

The strange quark Jones polynomial evaluates $22\%$ higher than the down quark Jones polynomial. The Skein polynomial cost per strange quark (replacing $\mathfrak{d} \to \mathfrak{s}$) is:

$$
  \delta M_{\mathrm{Skein}}
   \approx 
  \frac{|J_{\mathfrak{s}}| - |J_{\mathfrak{d}}|}{|J_{\mathfrak{d}}|}
   \times 
  \frac{V_B}{\hbar_q^2}
   \approx 
  0.225 \times 749
   \approx  168  \text{Skein units}.
$$

The Skein polynomial cost exceeds the crossing-energy gain ($1.80$ Skein units) by a factor of $93$. At zero pressure, strange matter is not the ground state.

**Competition at finite density.**
| Contribution | SQM (uds) | Ordinary (udd) | Advantage |
|-------------|-----------|----------------|-----------|
| Strong binding | $8 q^{-1}$ | $6 q^{-1}$ | SQM by $4/3$ |
| Coulomb correction | $0$ | $Q \cdot (q - q^{-1})$ | SQM (no EM drag) |
| Jones polynomial cost | $\lvert J_{\mathfrak{s}}\rvert = 1.176$ | $\lvert J_{\mathfrak{d}}\rvert = 0.960$ | Ordinary ($22\%$ lighter) |
| Borromean volume | $V_B = 7.328$ | $V_B = 7.328$ | Tie |

**Neutron star cores.**
At finite baryon density $\rho$, the Fermi energy $E_F$ adds energy per baryon. When $E_F$ exceeds $\delta M_{\mathrm{Skein}} \approx 168$ Skein units, strange quarks become accessible. Scaling by the proton mass gives:

$$
  E_F^{(\mathrm{threshold})}
   \approx 
  \frac{168}{749} \times 938  \mathrm{MeV}
   \approx  210  \mathrm{MeV}.
$$

This corresponds to $\rho_{\mathrm{hyp}} \approx 2\text{--}3\rho_0$. Above this density:
1. Strange baryons ($\Lambda$, $\Sigma$, $\Xi$, $\Omega$) appear.
2. The $4/3$ crossing-energy advantage creates a positive feedback. This lowers the Fermi energy and admits more strange quarks.
3. At $\rho \gtrsim 5\rho_0$, the matter approaches equal $(\mathfrak{u}, \mathfrak{d}, \mathfrak{s})$ composition.

The inner cores of massive neutron stars are strangelets. These are electromagnetically neutral, color-confined lumps of strange quark matter, stabilized by gravity and Fermi pressure.

**Parameter space.**
Strangelets require hadrons (confinement) and accessible strange quarks. This limits $q$:

| Regime | $q$ range | Strangelets? | Why |
|--------|-----------|:------------|-----|
| Deconfined | $q < q_{\mathrm{gold}} \approx 0.382$ | **No** | No hadrons; elliptic fiber degenerate, $S_5$ broken, quarks free |
| Sub-classical | $q_{\mathrm{gold}} < q < 1$ | **No** | Hadrons exist, but $\lvert J_{\mathfrak{s}}\rvert/\lvert J_{\mathfrak{d}}\rvert$ diverges as $q \to q_{\mathrm{gold}}$ |
| Classical limit | $q = 1$ | **Trivial** | All Jones polynomials evaluate to $1$; no mass differences |
| Physical | $q > 1$ (physical: $q_0$) | **Yes, at high density** | Jones polynomial cost finite; Fermi energy overcomes it at $\rho \gtrsim 2\rho_0$ |

Strangelets are a high-density phenomenon at the physical aether parameter.

**Strange force.**
Witten posited a "strange force" mediating attraction between strangelets. In QOU, this is the $5$-crossing component of the strong channel. The cinquefoil braiding generates stronger $R$-matrix binding than the trefoil. The "strange force" is the strong force evaluated at higher crossing number.
