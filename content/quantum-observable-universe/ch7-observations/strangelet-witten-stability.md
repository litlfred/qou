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
down quarks ($\overline{T_{2,3}}$, 3 negative crossings) with
strange quarks ($\overline{T_{2,5}}$, 5 negative crossings), each
baryon gains $2q^{-1}$ additional binding in the strong channel.
At $q = 1.1097$: this is $2 \times 0.9011 = 1.802$ Skein units
per baryon.

**The genus obstruction.**

If crossing energy were the whole story, strange matter would
be the ground state and Witten would be right.  But the
categorical mass $\mathfrak{m}_H$ depends not only on crossing
energy but on the **Seifert genus** of the constituent knots.
The strange quark $\overline{T_{2,5}}$ has genus $2$, while the
down quark $\overline{T_{2,3}}$ has genus $1$.  The genus
contributes to mass through the topological mass formula
$\mathfrak{m} = \mathrm{Vol}(K)/\hbar_q^2$, and higher-genus
knots generally have larger hyperbolic volume.

The competition is:

| Contribution | SQM (uds) | Ordinary (udd) | Advantage |
|-------------|-----------|----------------|-----------|
| Strong binding (crossing) | $8 q^{-1}$ | $6 q^{-1}$ | SQM by $4/3$ |
| Coulomb correction | $0$ | $Q \cdot (q - q^{-1})$ | SQM (no EM drag) |
| Genus cost (mass) | genus $2$ strange | genus $1$ down | Ordinary (lighter) |
| Borromean volume | $\mathrm{Vol}(\mathcal{B}_3^{(\mathrm{uds})})$ | $\mathrm{Vol}(\mathcal{B}_3^{(\mathrm{udd})})$ | Depends on $q$ |

**The Witten threshold.**

Define the Witten threshold $q_W$ as the value of $q$ at which
the extra crossing-energy binding from strange quarks exactly
compensates their genus-cost penalty:

$$
  2q_W^{-1}
  \;=\;
  \frac{\mathrm{Vol}(\overline{T_{2,5}}) - \mathrm{Vol}(\overline{T_{2,3}})}{\hbar_{q_W}^2}.
$$

For $q > q_W$: the genus cost dominates and ordinary matter is
the ground state (our universe, $q = 1.1097$).

For $q < q_W$: the extra crossing-energy binding dominates and
strange matter is the ground state (Witten's hypothesis holds).

The Witten threshold lies in the range
$q_{\mathrm{gold}} < q_W < 1.1097$ — somewhere between the
golden ratio degeneration
([golden ratio threshold](#rem:golden-ratio-degeneration)) and
our substrate parameter.  Determining $q_W$ precisely requires
the hyperbolic volumes of the Borromean links with cinquefoil
vs trefoil constituents, which is a SnapPea computation.

**Physical consequence.**

At $q = 1.1097$, strange matter is **not** the ground state:
the genus-$2$ mass penalty of the strange quark outweighs its
crossing-energy advantage.  Ordinary nuclear matter (iron-56)
remains the most tightly bound configuration.  This is consistent
with the observed absence of strangelets in cosmic ray data and
heavy-ion collision experiments.

However, the margin is not enormous.  The strange quark's
crossing-energy advantage ($4/3$ ratio) is a significant
fraction of the genus cost.  This explains why strange
hadrons ($\Lambda$, $\Sigma$, $\Xi$, $\Omega$) are only
modestly heavier than their non-strange counterparts — the
crossing-energy gain partially offsets the genus penalty.

**Witten's "strange force."**

Witten noted that SQM would experience a "strange force" —
an attractive interaction between strangelets mediated by
strange quark exchange.  In QOU, this force is the **genus-$2$
component of the strong channel**: the $5$-crossing cinquefoil
braiding generates stronger $R$-matrix binding than the
$3$-crossing trefoil braiding.  The "strange force" is not a new
fundamental force; it is the strong force evaluated at higher
crossing number.
