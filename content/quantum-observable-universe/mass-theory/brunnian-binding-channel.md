**Proposition.** *Let a nuclear composite be assembled from component knots whose pairwise
inter-component linking pattern is Brunnian — every pairwise Gauss linking number vanishes, as for
the Borromean carrier $\mathrm{L6a4}$ of ${}^3\mathrm{He}$/${}^4\mathrm{He}$. Then the mutual
binding contribution to the [crossing energy](#def:crossing-energy) is carried entirely by the
sign-blind coordination-count channel, and the signed linking-number channel is identically zero.
Consequently the binding multiplier is an unsigned coordination count, complementary in bar-parity
to the bar-even mass self-trace, and can never coincide with it.*

## Setup

Write the mutual (inter-component) crossing energy of a component pair with $n_+$ positive and
$n_-$ negative crossings in the Skein-signed form $n_+ q - n_- q^{-1}$. The proved decomposition of
[crossing energy](#def:crossing-energy) splits it into two channels:

$$
  \underbrace{\tfrac{1}{2}(n_+ - n_-)(q + q^{-1})}_{\text{signed (strong, }\cosh\text{) channel}}
  \;+\;
  \underbrace{\tfrac{1}{2}(n_+ + n_-)(q - q^{-1})}_{\text{unsigned (Coulomb, }\sinh\text{) channel}} .
$$

The signed multiplicity is the writhe $n_+ - n_- = 2\,\mathrm{lk}$, the Gauss linking number; the
unsigned multiplicity is the crossing count $n_+ + n_-$, a coordination count.

## The Brunnian channel

A Brunnian pair has vanishing pairwise linking number, $\mathrm{lk} = 0$, i.e. $n_+ = n_-$. The
signed channel then vanishes and the entire mutual/binding energy is the unsigned count channel; for
a crossing pair at a substrate modulus $q > 1$ this channel is strictly positive. So the binding
energy is nonzero even where the pairwise linking number is zero — the coordination count, not the
Gauss linking number, is the correct binding carrier for a Brunnian nuclear link. A minimal Brunnian
bond ($n_+ = n_- = 1$, the pairwise pattern inside $\mathrm{L6a4}$) contributes exactly one
coordination unit, so a fully coordinated cluster carries $\binom{A}{2}$ units and per-nucleon
$z = A - 1$; which pairs bond is the coordination-graph question, saturation-limited for heavy $A$
(the complete graph is excluded there, `QOU.Mass.CoordinationSaturation`).

The deuteron sits at the boundary: its Hopf carrier has $\mathrm{lk} = 1 \neq 0$ and coordination
$z = 1$, so signed and unsigned channels coincide there. The two invariants agree for a Hopf-bonded
pair and diverge only at $A \geq 3$, where the unsigned count is the non-vanishing one.

## Why the assignment is forced — bar-parity

Under the bar-involution $q \mapsto q^{-1}$ the count (binding) channel is bar-odd, while the mass
self-trace $\mathrm{lw} = \tfrac{1}{c+1}\sum_{\lambda \vdash c+1} \dim_q \lambda$ is bar-even —
every quantum dimension satisfies $\dim_q = \dim_{q^{-1}}$ (for the fundamental
$[2]_q = q + q^{-1}$). A nonzero bar-even function is never bar-odd, so a binding multiplier and a
mass multiplier occupy complementary bar-parity sectors and can never be the same object. This is
the same $\cosh$/$\sinh$ split the framework uses for the bar-even meson scale and its bar-odd
$Q_\beta$ partner. The assignment mass $\leftrightarrow$ self-trace, binding $\leftrightarrow$
coordination count is therefore a parity fact, not a modelling choice.

## Scope

The channel structure, the Brunnian reduction, the coordination-unit map for minimal bonds, and the
bar-parity orthogonality are proved (`QOU.Mass.BrunnianBindingChannel`, sorry-free). The two further
residuals are now also settled. The mass $\leftrightarrow$ self, binding $\leftrightarrow$ mutual
assignment is a theorem of the crossing partition plus the mass-deficit definition of binding
($B = \sum_i m_i^{\text{isolated}} - m^{\text{assembly}} = -(\text{mutual energy})$; the self
energies cancel), so binding is exactly the inter-component pairing
(`QOU.Mass.SelfMutualPartition`, sorry-free); and the crossing-count $\to$ coordination coefficient
is $\tfrac{1}{2}\lvert\text{inter-crossings}\rvert$ in general, giving $\binom{A}{2}$ units and
per-nucleon $z = A-1$ for a complete graph of minimal single clasps. This is the discrete
counterpart of the unsigned-invariant resolution reached independently on the electromagnetic-linking
side. The one modelling step not lifted is the identification of the substrate mass observable with
this crossing energy at the full Markov-trace granularity (the self energy closes to the
q-dimension self-trace $\mathrm{lw}$; the archimedean dressing
$\mathfrak{m} = \mathfrak{m}_e\,\mathrm{Vol}\,\mathrm{lw}/\hbar_q^2$). The exact saturated fraction
$B/A/\mathfrak{m}_N \approx \hbar_q^2$ is a numerical coincidence, not a prediction: the empirical
$B/A$ peaks at $0.954\,\hbar_q^2$ near $A \approx 60$ and falls, and the fundamental volume
coefficient is $a_V/\mathfrak{m}_N \approx 1.71\,\hbar_q^2$.
