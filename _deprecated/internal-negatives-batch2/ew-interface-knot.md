**Definition (electroweak interface knot $\bowtie_K$).**
*Let $R$ be the categorical coefficient ring with $q \in R$
generic (not a root of unity in $R$, $q \neq 1$). Inside the
$n = 6$ Hecke algebra $H_6(q)$ over $R$, the **electroweak
interface knot** $\bowtie_K$ is a non-empty word in the
**adjacent-pair generators** $\sigma_2$ and $\sigma_4$ — i.e. the
generators that connect the disjoint strand-pairs $(1,2),
(3,4), (5,6)$ on which the EW carriers
$W \leftrightarrow \sigma_1^{\,4}$, $Z \leftrightarrow \sigma_3^{\,6}$,
$H \leftrightarrow \sigma_5^{\,8}$ act
([`conj:hoefsmit-ew-cell-content`](#conj:hoefsmit-ew-cell-content)).*

*Concretely, $\bowtie_K$ is decomposed by its endpoints into three
sub-interfaces*

$$
  \bowtie_K \;=\; \bowtie_K^{(W \to Z)} \cdot \bowtie_K^{(Z \to H)} \cdot \bowtie_K^{(H \to W)},
$$

*where each $\bowtie_K^{(X \to Y)} \in H_6(q)$ is a word in
$\sigma_2$ (for $W \leftrightarrow Z$) or $\sigma_4$ (for
$Z \leftrightarrow H$) or both (for $W \leftrightarrow H$ with
$\sigma_2 \sigma_3 \sigma_4$-type bridge).*

### Categorical role

$\bowtie_K$ is the QOU analog of the inter-nucleon interface knot
$I$ from the W-3 derivation
([`prop:atomic-mass-gb-nf`](#prop:atomic-mass-gb-nf)), generalised
from nucleon coupling to gauge-boson coupling. In the deuteron
case, the interface knot $I = \sigma_3$ (the single generator
between the proton's $(1,2,3)$ strands and the neutron's
$(4,5,6)$ strands) contributed the $+1$ in $u_{\rm shift} = 18Z
+ 21N + 1$ — a single averaged crossing distinct from the
intra-nucleon shifts $18Z + 21N$.

In the EW case, $\bowtie_K$ encodes the **Higgs-vev induced
coupling** between gauge bosons. Pre-EWSB the bosons are
disjoint (free); post-EWSB the Higgs vacuum induces a non-trivial
interface — i.e. $\bowtie_K \neq \mathbf{1}$ — that mixes the
sym/alt eigenchannels and produces the $(W^3, B) \to (Z, \gamma)$
rotation of the standard model.

### Concrete EW braid with interface

The full EW braid representing the $W, Z, H$ sector with
Higgs-vev coupling is

$$
  \beta_{\rm EW}(\bowtie_K)
  \;:=\;
  \sigma_1^{\,4} \cdot \bowtie_K^{(W \to Z)} \cdot \sigma_3^{\,6}
  \cdot \bowtie_K^{(Z \to H)} \cdot \sigma_5^{\,8} \cdot \bowtie_K^{(H \to W)}
  \;\in\; H_6(q).
$$

The $\bowtie_K = \mathbf{1}$ (trivial) special case recovers the
disjoint-strand-pair product $\sigma_1^4 \sigma_3^6 \sigma_5^8$ —
the pre-EWSB free-boson sector. The discharge target for the
non-trivial $\bowtie_K$ is the Higgs-vev mechanism (open per
[`conj:categorical-higgs-mechanism`](#conj:categorical-higgs-mechanism)).

### Why $\bowtie_K$ is the right structure

Three reasons:

1. **Direct parallel with the deuteron derivation.** The W-3 D(u)
   closed-form derivation
   ([`prop:atomic-mass-gb-nf`](#prop:atomic-mass-gb-nf)) used the
   inter-nucleon interface knot to encode binding between
   otherwise-disjoint nucleons. The EW gauge-boson coupling is
   structurally analogous: the Higgs vacuum is the "binding agent"
   between the otherwise-disjoint $W, Z, H$ carriers.

2. **Resolves the simple-multiplicity Weinberg-angle failure.**
   The simple-uniform-multiplicity reading of $\cot\theta_W$
   gave $q_0^{-4} \approx 0.66$ vs CODATA $1.823$ (64% off,
   [`weinberg-angle-simple-falsified.witness.json`](https://github.com/litlfred/qou/blob/main/computations/weinberg-angle-simple-falsified.witness.json));
   the corrected non-uniform reading gave $1.669$ (8.4% off,
   [`weinberg-angle-corrected-probe.witness.json`](https://github.com/litlfred/qou/blob/main/computations/weinberg-angle-corrected-probe.witness.json)).
   Both readings are computed for $\bowtie_K = \mathbf{1}$ (no
   Higgs-vev coupling). The remaining 8.4% gap is plausibly
   exactly what the non-trivial $\bowtie_K$ supplies.

3. **Bar-self-duality breakdown is structural.** The
   $\bowtie_K = \mathbf{1}$ trace
   $\mathrm{tr}_{\rm pure}(\sigma_1^{\,4} \sigma_3^{\,6} \sigma_5^{\,8})
   = 4(q^{18}+q^{-18}) + 2(q^{10}+q^{-10}) + (q^6+q^{-6}) + 3(q^2+q^{-2})$
   is bar-self-dual term-by-term (each $\sigma_i^{2k}$ is on its
   own). With $\bowtie_K \neq \mathbf{1}$, the interface
   crossings introduce orientation-dependent contributions,
   breaking term-by-term bar-self-duality. The constrained-PSLQ
   null result
   ([`nv-pslq-tr-pure-basis.witness.json`](https://github.com/litlfred/qou/blob/main/computations/nv-pslq-tr-pure-basis.witness.json))
   on the bar-self-dual basis is **expected** — the actual
   structural form has $\bowtie_K$-induced asymmetry.

### Status

This is a **definition** in the QOU type system (kind:
`definition`), not a conjecture. The construction is internally
consistent (a specific element of $H_6(q)$ defined by a word in
adjacent-pair generators); whether the **specific** $\bowtie_K$
that realises the Higgs vacuum-expectation-value can be
identified categorically is the open question, deferred to
[`conj:categorical-higgs-mechanism`](#conj:categorical-higgs-mechanism)
(Step C).

The minimal non-trivial choice is

$$
  \bowtie_K^{\rm minimal}
  \;:=\;
  \sigma_2 \cdot \sigma_4 \cdot \sigma_2,
$$

— a $T_{2,3}$-shaped interface (single trefoil-like inter-pair
coupling, analogous to the deuteron's $\sigma_3$ inter-nucleon
single crossing). Whether this is the right Higgs-vev choice
requires either:

- a categorical-physics argument from
  [`conj:categorical-higgs-mechanism`](#conj:categorical-higgs-mechanism)
  Step C; or
- a numerical match against $\theta_W$ at appropriate
  precision, treated as a uniqueness witness rather than a
  derivation.

### Audit-flag impact

Authoring this definition unblocks:

- `conj:hoefsmit-ew-cell-content` §"Refinement (2026-05-06)" —
  provides the concrete $\bowtie_K$ to insert in $\beta_{\rm EW}$.
- `conj:weinberg-angle-categorical` §"Why this is plausible" —
  the missing Higgs-vev automorphism gets a concrete form via
  $\bowtie_K$.
- `conj:categorical-linking-operation` Property 5 (bar-involution
  compatibility) — the asymmetric contribution of $\bowtie_K$
  explains why naive bar-self-duality breaks term-by-term in the
  $\bowtie_K$-coupled trace.
- `conj:categorical-higgs-mechanism` Step C — Goldstone-eating
  is the operation that selects $\bowtie_K^{\rm physical}$ from
  the space of admissible interface knots.

**Witness.** No witness yet — recomputing the Hoefsmit pattern
enumeration under $\beta_{\rm EW}(\bowtie_K^{\rm minimal})$ is
the first concrete probe (action item).
