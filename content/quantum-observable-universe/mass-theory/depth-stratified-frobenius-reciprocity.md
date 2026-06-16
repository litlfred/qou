**Conjecture (Frobenius-reciprocity ideal restriction at low curvature-rank).**

*The unified curvature-rank mass formula
([`prop:unified-curvature-rank-mass-formula`](#prop:unified-curvature-rank-mass-formula))
$$
  \mathfrak{m}_{q, \mathcal{K}}(\mathcal{T})
  \;=\; \sum_{k = 0}^{n-1} \alpha_k \cdot \Phi_k(\mathcal{K}, \mathcal{T})
$$
admits a **Frobenius-reciprocity (FR) refinement at low curvature-rank
$k \le 3$**: the depth-$k$ Wedderburn weight
$\tilde w_\lambda = \dim_q^2 V_\lambda / [n]_q!$ in $\Phi_k$ is
**not uniform** over partitions $\lambda$ of depth $k$, but **restricts
to the distinguished hyperbolic-knot ideal at depth $k$** via
Frobenius reciprocity for the center inclusion
$Z(H_3) \hookrightarrow Z(H_n)$ through the depth-$k$ knot-ideal projector.*

*Concretely: for each low curvature-rank $k \in \{1, 2, 3\}$ there is
a distinguished hyperbolic knot $K_k^*$. Empirical resolution at
$k = 3$ (per , with
canonical braid words cross-verified against KnotInfo via hyperbolic
volume): $K_3^* = 4_1$ (figure-eight knot) gives the best variance
reduction at 1.551$\times$ (+14.8% vs 1.82$\times$ baseline), consistent with the
Fricke-trace derivation in
[`prop:chirality-from-frobenius-self-pairing`](#prop:chirality-from-frobenius-self-pairing)
giving $\chi_{4_1}((2,1)) = 2 - [3]_q$ at $H_3$. The previously
asserted $K_3^* = 6_1$ (Stevedore) does NOT empirically validate —
6_1 regresses the variance to 1.878$\times$ (worse than baseline). At
$k = 1, 2$ the distinguished knots are unnamed — open structural
question. The depth-$k$ contribution to the mass formula is*

$$
  \boxed{\;
    \Phi_k^{\mathrm{FR}}(\mathcal{K}, \mathcal{T})
     :=
    \sum_{\substack{\lambda \,\vdash\, n \\ \mathrm{depth}(\lambda) = k}}
      \widetilde{w}_\lambda^{(K_k^*)} \cdot
      \log\!\Bigl|\!\!\int_{A_\lambda}\!\! \rho(\beta_\mathcal{K}) \cdot \mathcal{T}\Bigr|
  \;}
  \tag{FR}
$$

*where the **FR-restricted weight** $\widetilde{w}_\lambda^{(K_k^*)}$
is the Frobenius-reciprocity pullback of $\dim_q^2 / [n]_q!$ through
the knot-ideal central projector $e_{K_k^*} \in Z(H_n)$:*

$$
  \widetilde{w}_\lambda^{(K_k^*)}
   :=
  \frac{\dim_q^2 V_\lambda \cdot \chi^\lambda(e_{K_k^*})}
       {[n]_q! \cdot \sum_{\mu \,\vdash\, n, \mathrm{depth}(\mu) = k}
         \dim_q^2 V_\mu \cdot \chi^\mu(e_{K_k^*})}.
$$

### Why FR

The Frobenius integral $\int_{A_\lambda} \rho(\beta_\mathcal{K}) \cdot \mathcal{T}$
at low curvature-rank "factors through specific hyperbolic-knot
ideals" per
[`prop:plancherel-term-7-formulation`](#prop:plancherel-term-7-formulation)
§*Why universal at $k \ge 4$*. The **categorical content** of this
factorisation is **Frobenius reciprocity** for the center inclusion
$Z(H_3) \hookrightarrow Z(H_n)$:

| Frobenius reciprocity instance | Role in QOU |
|---|---|
| $\mathrm{Hom}_G(\mathrm{Ind}_H^G V, W) \cong \mathrm{Hom}_H(V, \mathrm{Res}_H^G W)$ (classical) | basis identity |
| Center inclusion $Z(H_3) \hookrightarrow Z(H_n)$ via knot embedding | depth-$k$ restriction here |
| Wedderburn-block restriction $\chi^\lambda \to \chi^\lambda \cdot e_{K_k^*}$ | the boxed FR weight (FR) |

At high curvature-rank $k \ge 4$, "no specific knot ideal remains in
the centre — what survives is the dualizing-complex residue" (per
[`prop:plancherel-term-7-formulation`](#prop:plancherel-term-7-formulation)).
This is the case where FR is **trivial** (the centre is the whole
algebra; restriction = identity) and the uniform Plancherel weight
$\dim_q^2 / [n]_q!$ is correct.

### Empirical falsifications recorded

[`binding_depth_stratified_knot_weighted.py`](https://github.com/litlfred/qou/blob/main/computations/binding_depth_stratified_knot_weighted.py)
tested two simple empirical forms of "ideal restriction at low $k$" —
*both falsified* on D, T, ${}^{3}$He, ${}^{4}$He:

| Form tested | Hypothesis | max/min variance | Verdict |
|---|---|---:|---|
| Uniform $\tilde w_\lambda$ (baseline) | no restriction | $1.82\times$ | (the current  result) |
| $\tilde w_\lambda \cdot \|\chi^\lambda\|^\beta$ ($\beta > 0$) | concentrate on Markov-significant | $2.30$–$3.00\times$ | **falsified** |
| $\tilde w_\lambda$ on self-conjugate partitions only | Wenzl-bridge stratum | $5.94\times$ | **falsified** |

These rule out two simple Wedderburn-weight refinements, sharpening
the structural form of the FR pullback. **The FR-restricted weight
$\tilde w_\lambda^{(K_k^*)}$ above is precisely what these
empirical forms approximate but miss** — they use either the
braid's own character or self-conjugacy, neither of which is the
distinguished knot ideal $e_{K_k^*}$.

### Connection to the "you cannot hear the shape of a drum" problem

The Markov trace $\mathrm{tr}_M(\beta_\mathcal{K}) =
\sum_\lambda y_\lambda \chi^\lambda(\beta_\mathcal{K})$ is
**isospectral data** — like the Laplacian spectrum of a drum.
**Jones-faithfulness theorem** at crossing $\le 10$
(`rem:jones-faithfulness-crossing-10`)
states that the Jones polynomial distinguishes knots up to 10
crossings. Beyond this, **Conway–KT mutant pairs**
(`rem:conway-kt-mutant-pair`) have the
same Jones polynomial but distinct hyperbolic volumes — they are
"isospectral isobars".

For atomic braids of D, T, ${}^{3}$He, ${}^{4}$He (at crossings $22^+$), the
canonical Jones polynomial may *not* distinguish them from
Kanenobu/mutant twins. The FR refinement (FR) above is precisely the
**enrichment of the Wedderburn sum** that breaks the Jones-only
spectral degeneracy — by weighting partitions through the
distinguished knot-ideal central projector $e_{K_k^*}$, the formula
"hears" not the Jones spectrum but the **knot-ideal-restricted
data**.

This is the categorical content of:

- "one can hear *more than* the Jones polynomial when as known which
 knot ideal each Wedderburn block belongs to";
- the FR pullback $\chi^\lambda \to \chi^\lambda \cdot \chi^\lambda(e_{K_k^*})$
 recovers the missing volume information at low curvature-rank.

### Significance: closing the 1.82$\times$ variance

If true, the FR refinement (FR) closes the variance on  to
$\le 1.05\times$ (universal categorical constant) by enhancing the
low-$k$ contributions through the per-knot ideal restriction:

- $k = 3$ ($K_3^* = 4_1$, empirically resolved per ):
 chirality channel, full FR pullback computable from the $4_1$
 central projector in $H_n$. Empirically reduces variance to
 $1.551\times$ (+14.8% vs the $1.82\times$ uniform-Plancherel
 baseline). The Fricke-trace derivation in
 [`prop:chirality-from-frobenius-self-pairing`](#prop:chirality-from-frobenius-self-pairing)
 independently picks out $4_1$ at $H_3$ via $\chi_{4_1}((2,1)) = 2 - [3]_q$.
- $k = 1, 2$: **open** — the distinguished knots are NOT named in
 the existing paper. Candidates: $K_1^* \in \{4_1, 5_2\}$ (smallest
 hyperbolic), $K_2^* \in \{5_2, 6_1\}$ (chirality precursors).
 These need structural identification *before* the FR conjecture is
 computationally testable at $k = 1, 2$.

### Existence requirements

For the conjecture to be well-defined, three structural ingredients
must exist:

1. **Distinguished knot $K_k^*$ at each $k \in \{1, 2, 3\}$**: at
 $k = 3$ this is $4_1$ (empirically resolved per ,
 consistent with the Fricke-trace derivation in
 [`prop:chirality-from-frobenius-self-pairing`](#prop:chirality-from-frobenius-self-pairing));
 at $k = 1, 2$ this is the open question. Candidates and selection
 criteria are recorded in
 [`docs/audits/-variance-per-depth-diagnosis.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-variance-per-depth-diagnosis.md).

2. **Central projector $e_{K_k^*} \in Z(H_n)$**: the Hecke-ideal
 central projector for $K_k^*$. For $K_k^*$ a knot on $m$ strands,
 this is its image in $H_n$ via the standard inclusion
 $H_m \hookrightarrow H_n$ via Wenzl branching.

3. **Convergence of the FR sum**: at low $k$, the FR-restricted sum
 is over a *strict subset* of partitions (those for which
 $\chi^\lambda(e_{K_k^*}) \ne 0$) — finite by Wedderburn-block
 finiteness.

### Falsification path

The conjecture was **directly falsified for the originally-asserted $K_3^* = 6_1$**
by : with corrected
canonical braid words (verified against KnotInfo via hyperbolic
volume) and proper $S_{\text{uniform},k}$-preserving weight
normalization, Stevedore $6_1$ regresses the variance to $1.878\times$
(worse than the $1.82\times$ baseline). The **corrected resolution**
is $K_3^* = 4_1$ (figure-eight), giving variance $1.551\times$
(+14.8% reduction) — consistent with the Fricke-trace derivation in
[`prop:chirality-from-frobenius-self-pairing`](#prop:chirality-from-frobenius-self-pairing).
The conjecture is therefore **partially supported at $k = 3$**: the
FR mechanism reduces variance, but with $K_3^* = 4_1$, not the
originally-asserted $6_1$.

A concrete computation requires:

1. The braid word for $4_1$ in $H_3$: $4_1 = $ closure of
 $\sigma_1 \sigma_2^{-1} \sigma_1 \sigma_2^{-1}$
 (figure-eight; braid index 3). $4_1$ has hyperbolic volume
 $\approx 2.0299$ (smallest among hyperbolic knots).
2. Wenzl-embedded $4_1 \in H_n$ for $n = 3A$ via the standard
 inclusion at strand-positions $\{i, i+1, i+2\}$ for some $i$
 inside the atomic braid.
3. $\chi^\lambda(4_1^{(n)})$ for each $\lambda \vdash n$ of depth 3 —
 computable via the Rust kernel
 ([`compute_atom_chi_rust.py`](https://github.com/litlfred/qou/blob/main/computations/compute_atom_chi_rust.py))
 or the symbolic Hoefsmit pipeline. The script
 [`fr_pullback_k3_test.py`](https://github.com/litlfred/qou/blob/main/computations/fr_pullback_k3_test.py)
 (from ) carries this end-to-end with KnotInfo cross-validation.

### Lean formalisation

[`qou:QOU.BraidKnot.depth_stratified_frobenius_reciprocity`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/DepthStratifiedFrobeniusReciprocity.lean)
axiomatises the FR refinement as a class hypothesis (per
CLAUDE.md §3b-cond). Downstream theorems depending on the
FR-corrected mass formula consume this class as an explicit
`[Instance]` hypothesis. The classical-limit case ($k = 0, 1, 2, 3$
at $q = 1$) reduces to standard Frobenius reciprocity for $S_n$ —
provable in Mathlib via `Representation.induced` and
`Representation.restricted`.

### Why this is "the final key"

Per the structural narrative on  and
[`docs/audits/-variance-per-depth-diagnosis.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-variance-per-depth-diagnosis.md):

- The unified mass formula is established
 ([`prop:unified-curvature-rank-mass-formula`](#prop:unified-curvature-rank-mass-formula))
- The depth-stratified $\alpha_k \cdot \Phi_k$ schedule is fixed
 ([`prop:plancherel-term-7-formulation`](#prop:plancherel-term-7-formulation),
 $\alpha_{k \ge 4} = m_e \cdot 8G$)
- The convolution structure (Hecke-product with interface knot $\bowtie_K$)
 is fixed
 (`def:ew-interface-knot`)
- The bar-symmetrization Li_2^q / Φ_q split is established
 (`prop:li2q-phiq-bar-symmetrization`)
- The pre-$\tau$ / post-$\tau$ pentagon distinction is established
 ([`prop:q-rogers-pentagon-archimedean`](#prop:q-rogers-pentagon-archimedean))

The **only remaining structural ambiguity** in the binding-energy
chain at low $k$ is which **Wedderburn-weight modification** captures
the per-knot ideal restriction. Two empirical forms have been
falsified. The FR pullback above is the
**categorically-canonical candidate**: it is the unique
Wedderburn-weight modification compatible with the center inclusion
$Z(H_3) \hookrightarrow Z(H_n)$ and the chirality-channel labelling
at $k = 3$.

If true, this conjecture **closes the unified mass formula** to
universal precision — all atomic binding energies follow from
$(m_e, q_0, \mathfrak{Q}_\beta)$ + the three distinguished knots
$\{K_1^*, K_2^*, K_3^* = 4_1\}$ (with $K_3^* = 4_1$ empirically
resolved per ).

### Discussion

**Conjecture, with structural framing solid + two empirical
falsifications recorded.** Open: identification of $K_1^*, K_2^*$;
formal proof of FR pullback for the q-deformed centre inclusion.
The classical-limit ($q = 1$) case is standard Frobenius reciprocity
for $S_n$ (provable in Mathlib).
