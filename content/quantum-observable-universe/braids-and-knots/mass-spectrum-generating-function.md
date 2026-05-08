**Remark (the confined Laurent polynomial as mass-spectrum generating
function — functorial equivalence, not identity).**
*The relation "confined Laurent polynomial $=$ mass" is not a literal
equality. The polynomial $P_K(q) \in \mathbb{Z}[q^{\pm 1/2}]$ is a
graded Euler characteristic; the macroscopic mass is a scalar.
The two are linked by a functorial composition: a categorical
generating function whose evaluation at the substrate parameter
$q_0$ collapses to the observed scalar.*

## The polynomial is a generating function, not a number

Let $M_K$ denote the stable highest-weight KLR module
\cite{khovanovlauda2009, brundankleshchev2009} associated to the
braid closure $\hat{\beta}_K$. The
[Observation Frame](#def:observation) $\tau$ takes the graded
Euler characteristic,

$$
  P_K(q)
  \;=\;
  \sum_{d \in \mathbb{Z}}
    \dim_R \mathrm{Hom}_{\mathcal{K}_n}(P_d, M_K) \, q^d
  \;\in\; \mathbb{Z}_{\geq 0}[q^{\pm 1/2}],
$$

where the sum is finite — confinement is the homological boundedness
of $M_K$ under the jet/filtration order ([confinement
level](#def:confinement-level)). The word "confined" is not
decorative: an unbounded module would yield an infinite power series
(formally an infinite mass tower); the bound truncates this to a
genuine Laurent polynomial.

## Reading the polynomial: spectrum, not a single value

Each term $c_d q^d$ of $P_K(q)$ has an independent physical reading:

- **Exponent $d$** — the **graded Hecke energy**: a $\mathbb{Z}$-grading
  shift counting topological complexity (crystal-operator depth in
  $M_K$). Higher $d$ = higher internal topological tension.
- **Coefficient $c_d$** — the **microstate degeneracy**: the number
  of orthogonal Hom-channels carrying that energy. Coefficients are
  structurally non-negative integers
  ([structural positivity](#rem:categorical-mass-positivity)).

Read this way, $P_K(q)$ is the **mass spectrum** of $K$ — a partition
function over its internal homological slices. The terms are *mass
components*; their sum (after evaluation) is the macroscopic mass.

## Functorial equivalence via substrate evaluation

The macroscopic, measurable mass is the **evaluation** of $P_K(q)$ at
the substrate value $q_0 \approx 1.1097$:

$$
  \boxed{\;\;
    M_K
    \;\approx\;
    m_0 \cdot \bigl|P_K(q_0)\bigr|
  \;\;}
$$

(see [two-tier scaling](#rem:two-tier-scaling-pq) for the
factorisation into the Tier-1 quantum-dimension normalisation and the
Tier-2 base-mass anchor $m_0$). The composition

$$
  M_K
  \;\xrightarrow{\;\tau\;}\;
  P_K(q)
  \;\xrightarrow{\;\mathrm{ev}_{q_0}\;}\;
  P_K(q_0)
  \;\xrightarrow{\;m_0\,|\cdot|\;}\;
  M_K \in \mathbb{R}_{\geq 0}
$$

is the **functorial equivalence** linking the categorical state, its
generating function, and the physical observable. None of the three
arrows is an identity: $\tau$ is decategorification (loses
isomorphism information), $\mathrm{ev}_{q_0}$ is specialisation
(loses generic-$q$ structure — see the open issue in
[unified knot-mass formula](#thm:knot-mass-formula-unified)), and
$m_0\,|\cdot|$ is unit conversion.

## Why the distinction matters

Conflating the polynomial with the mass produces three failure modes:

1. **A polynomial cannot equal a scalar.** Any agent or formalisation
   that writes "$P_K(q) = M_K$" type-checks as nonsense. The correct
   statement is $M_K \approx m_0 \cdot |P_K(q_0)|$.
2. **The microstate spectrum is invisible.** Treating $P_K$ as a
   single number erases the degeneracy structure carried by
   coefficients $c_d$ and the energy structure carried by exponents
   $d$ — exactly the data needed to compute branching ratios and
   resonance widths.
3. **The substrate dependence is hidden.** A single electron has a
   single mass on a scale because the substrate $q_0$ is fixed by
   the ambient vacuum, not because the spectrum has only one term.
   The polynomial is the topological engine; the scalar is its
   output at the operating point of our universe.

## Authoring guidance

When stating mass results in `.md` or `.lean`:

- **Do** write "$P_K(q)$ is the mass-spectrum generating function of
  $K$, and $M_K \approx m_0 \cdot |P_K(q_0)|$".
- **Do not** write "$P_K(q)$ is the mass of $K$" or "$P_K = M_K$".
- The Lean side carries this via the [mass identity](#def:mass-identity)
  definition (categorical state $\to$ polynomial) and the calibration
  blocks ([three calibration inputs](#prop:three-calibration-inputs))
  for the Tier-2 conversion.
