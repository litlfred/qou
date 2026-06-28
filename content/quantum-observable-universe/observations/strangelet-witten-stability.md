Witten \cite{witten1984} conjectured that **strange quark matter**
(SQM) — bulk matter with roughly equal numbers of up, down, and
strange quarks — might be the absolute ground state of hadronic
matter at zero pressure.  If true, ordinary nuclear matter (protons
and neutrons bound in iron-56) is metastable: it would be
energetically favorable for nuclei to convert entirely to strange
matter, prevented only by a large energy barrier.

The [strangelet crossing energy](#prop:strangelet-crossing-energy)
gives a precise QOU translation of Witten's hypothesis.

**The crossing-energy argument for SQM stability.**

The strangelet proposition establishes three facts:
1. SQM is electromagnetically neutral ($Q = 0$) — a topological
   identity, independent of $q$.
2. Its crossing energy is purely strong — no Coulomb correction.
3. Its strong binding per baryon exceeds neutron matter by a
   factor of $4/3$.

Fact (3) is the QOU version of Witten's observation: by replacing
down quarks ($T_{2,3}^{\sigma}$, 3 negative crossings) with
strange quarks ($T_{2,5}^{\sigma}$, 5 negative crossings), each
baryon gains $2q^{-1}$ additional binding in the strong channel.
At $q = q_0$: this is $2 \times 0.9011 = 1.802$ Skein units
per baryon.

**The Jones polynomial obstruction.**

If crossing energy were the whole story, strange matter would
be the ground state and Witten would be right.  But all torus
knots have **zero hyperbolic volume** — the mass of a baryon
comes entirely from the Borromean linking, not from the
constituent knots ([building block knots](#rem:building-block-knots)).
The strange quark is not heavier because of its genus.  It is
heavier because of its **Jones polynomial**.

The terminal resolution
([terminal resolution](#prop:terminal-resolution)) decomposes
each hadronic link into a sum of unknots and Hopf links weighted
by Skein polynomial coefficients.  These coefficients depend on
the Jones polynomial of each constituent.  At $q = q_0$:

| Quark | Knot | Jones polynomial | $\lvert J(q_0)\rvert$ |
|-------|------|-----------------|:-------------:|
| Up $\mathfrak{u}$ | $T_{2,3}$ | $-q^{-4} + q^{-3} + q^{-1}$ | $0.973$ |
| Down $\mathfrak{d}$ | $T_{2,3}^{\sigma}$ | $-q^{4} + q^{3} + q$ | $0.960$ |
| Strange $\mathfrak{s}$ | $T_{2,5}^{\sigma}$ | $-q^{10} + q^{9} - q^{8} + q^{7} + q^{5}$ | $1.176$ |

The strange quark's Jones polynomial evaluates **$22\%$ higher**
than the down quark's.  This excess enters the Skein resolution
of the baryon link as a larger coefficient on the Hopf link mass
terms, producing a heavier baryon.  The Skein polynomial cost
per strange quark (replacing $\mathfrak{d} \to \mathfrak{s}$) is

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

The crossing-energy gain from the extra $2$ negative crossings is
only $1.80$ Skein units.  The Skein polynomial cost exceeds the
crossing-energy gain by a factor of $\sim 93$.  At zero pressure,
strange matter is **decisively not** the ground state.

**The competition at finite density.**

| Contribution | SQM (uds) | Ordinary (udd) | Advantage |
|-------------|-----------|----------------|-----------|
| Strong binding (crossing) | $8 q^{-1}$ | $6 q^{-1}$ | SQM by $4/3$ |
| Coulomb correction | $0$ | $Q \cdot (q - q^{-1})$ | SQM (no EM drag) |
| Jones polynomial cost | $\lvert J_{\mathfrak{s}}\rvert = 1.176$ | $\lvert J_{\mathfrak{d}}\rvert = 0.960$ | Ordinary ($22\%$ lighter) |
| Borromean volume | $V_B = 7.328$ (same) | $V_B = 7.328$ (same) | Tie |

**Location of strangelets: neutron star cores.**

At finite baryon density $\rho$, the Fermi energy $E_F$
provides additional energy per baryon.  When $E_F$ exceeds the
Skein polynomial cost $\delta M_{\mathrm{Skein}} \approx 168$
Skein units, strange quarks become energetically accessible.
In physical units, scaling by the proton mass:

$$
  E_F^{(\mathrm{threshold})}
   \approx 
  \frac{168}{749} \times 938  \mathrm{MeV}
   \approx  210  \mathrm{MeV}.
$$

This corresponds to a density $\rho_{\mathrm{hyp}} \approx 2\text{--}3\rho_0$ (two to three times nuclear saturation
density), consistent with the onset of hyperonic matter in
nuclear physics calculations.  Above this density:

1. **Strange baryons** ($\Lambda$, $\Sigma$, $\Xi$, $\Omega$)
   appear alongside protons and neutrons.
2. The $4/3$ crossing-energy advantage of strange quarks creates
   a **positive feedback**: more strange quarks lower the Fermi
   energy, allowing even more strange quarks.
3. At $\rho \gtrsim 5\rho_0$, the matter is approximately
   equal in $(\mathfrak{u}, \mathfrak{d}, \mathfrak{s})$ —
   this IS a strangelet.

**The inner cores of massive neutron stars are strangelets.**
A $2M_\odot$ neutron star has central density
$\rho_c \approx 5\text{--}8\rho_0$, well above the hyperon
threshold.  The core is a macroscopic strangelet: an
electromagnetically neutral, color-confined lump of strange
quark matter, stabilized by gravity and Fermi pressure.

**The $q$ parameter space.**

Strangelets require both hadrons (confinement) and accessible
strange quarks (Fermi energy exceeding the Jones polynomial
cost).  This constrains the $q$ range:

| Regime | $q$ range | Strangelets? | Why |
|--------|-----------|:------------|-----|
| Deconfined | $q < q_{\mathrm{gold}} \approx 0.382$ | **No** | No hadrons at all — elliptic fiber degenerate, $S_5$ broken, quarks free |
| Sub-classical | $q_{\mathrm{gold}} < q < 1$ | **No** | Hadrons exist but $\lvert J_{\mathfrak{s}}\rvert/\lvert J_{\mathfrak{d}}\rvert$ diverges as $q \to q_{\mathrm{gold}}$ — strange quarks become infinitely expensive near the degeneration |
| Classical limit | $q = 1$ | **Trivial** | All Jones polynomials evaluate to $1$; no mass differences, no flavor physics |
| Physical | $q > 1$ (ours: $q_0$) | **Yes, at high density** | Jones polynomial cost finite; Fermi energy can overcome it at $\rho \gtrsim 2\rho_0$ |

Below $q_{\mathrm{gold}}$: there are no hadrons, so there are no
strangelets.  The concept does not apply.  Between
$q_{\mathrm{gold}}$ and $q = 1$: the Jones polynomial of the
cinquefoil grows faster than the trefoil's as $q$ approaches the
golden ratio degeneration, because the higher-degree polynomial
$(-q^{10} + q^9 - q^8 + q^7 + q^5)$ has more terms that
amplify near the instability.  Strange quarks become
**more expensive**, not less, as $q$ decreases toward the
degeneration.

Strangelets are a **high-density phenomenon at the physical
substrate parameter**, not a low-$q$ phenomenon.

**Witten's "strange force."**

Witten noted that SQM would experience a "strange force" —
an attractive interaction between strangelets mediated by
strange quark exchange.  In QOU, this force is the
$5$-crossing component of the strong channel: the cinquefoil
braiding generates stronger $R$-matrix binding than the trefoil
braiding.  The "strange force" is not a new fundamental force;
it is the strong force evaluated at higher crossing number.
The extra $2q^{-1}$ binding per baryon is small compared to
the total Borromean binding ($749$ Skein units), but at high
density it accumulates across the entire neutron star core.
