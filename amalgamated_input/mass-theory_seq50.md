<!-- FILE_START: block-multiplicativity-v-free.md -->
**Conjecture (Block-Multiplicativity of $\hat V^{\text{free}}$ on the
Disjoint Hecke Product).**

*Let $\mathcal{B}_K^{\mathrm{vac}} = \mathcal{B}_p^{(1)} \cdots \mathcal{B}_n^{(N)} \in
H_{3A}(q)$ denote the **constituent vacuum** — the disjoint Hecke
product of $Z$ proton braids and $N$ neutron braids on disjoint
3-strand blocks, with no interface crossings
(`def:ew-interface-knot`). For each
generator $\sigma_g$ acting non-by definition only inside the $k$-th
nucleon block, the Wedderburn-weighted per-generator character ratio*

$$
  \hat V^{(3A)}_g(\mathcal{B}_K^{\mathrm{vac}})
   :=
  \sum_{\lambda \vdash 3A}
    \frac{\dim_q^2(\lambda)}{[3A]_q!} \cdot
    \frac{\chi^\lambda(W_g)}{\dim(\lambda)}
$$

*is **independent of $A$**: it depends only on the flavor of the
$k$-th nucleon (proton vs neutron) and on the local position
$g \bmod 3 \in \{0, 1\}$ within the block, not on the total strand
count $3A$ or the flavor content of the other blocks.*

### Empirical verification

Computed via the canonical formalism
on D, T, ${}^{3}$He at $H_6, H_9, H_9$ respectively (50 dps), as recorded in
[`binding-via-interface-knot.witness.json`](https://github.com/litlfred/qou/blob/claude/log-delta-categorical-derivation/computations/binding-via-interface-knot.witness.json):

| atom | proton block (gens 0, 1) | neutron block | matches D? |
|---|---|---|:-:|
| D (A=2) | $V_0 = 0.6714$, $V_1 = 1.0551$ | $V_0 = 0.5517$, $V_1 = 1.0884$ | — |
| T (A=3) | same | same | yes |
| ${}^{3}$He (A=3) | same | same | yes |

Block-multiplicativity holds **exactly** to 4 digits, the resolution
of the recorded witness. The block factors evaluate to

$$
  v_p := \hat V^{p}_0 \cdot \hat V^{p}_1 = 0.7084, \qquad
  v_n := \hat V^{n}_0 \cdot \hat V^{n}_1 = 0.6005.
$$

### Classical-limit proof sketch ($q \to 1$)

When $\sigma_g$ acts inside the first 3-strand block (positions $1, 2, 3$),
the symmetric-group character factors via the Littlewood–Richardson
restriction rule:

$$
  \chi_\lambda(\sigma_g)
   =
  \sum_{\mu \vdash 3, \nu \vdash 3A-3}
    c_{\mu, \nu}^{\lambda} \cdot
    \chi_\mu(\sigma_g) \cdot \dim(\nu).
$$

At $q = 1$ the Wedderburn weight $w_\lambda = \dim^2(\lambda) / (3A)!$ is
the classical Plancherel measure. Plugging in:

$$
  \hat V^{(3A)}_g
   =
  \frac{1}{(3A)!} \sum_{\mu, \nu}
    \chi_\mu(\sigma_g) \dim(\nu)
    \sum_\lambda c_{\mu, \nu}^\lambda \dim(\lambda).
$$

By the classical **Plancherel duality identity**
$\sum_\lambda c_{\mu,\nu}^\lambda \dim(\lambda)
 = \binom{3A}{3} \dim(\mu) \dim(\nu)$, this simplifies to

$$
  \hat V^{(3A)}_g
   =
  \binom{3A}{3} \frac{(3A-3)!}{(3A)!}
  \cdot
  \sum_{\mu \vdash 3} \chi_\mu(\sigma_g) \dim(\mu)
   =
  \frac{1}{6}
  \sum_{\mu \vdash 3} \chi_\mu(\sigma_g) \dim(\mu),
$$

using $\binom{3A}{3} \frac{(3A-3)!}{(3A)!} = \frac{1}{6} = \frac{1}{3!}$.
The right-hand side **depends only on the H_3 character data** of
$\sigma_g$, hence is $A$-independent. This proves the classical
limit ($q = 1$) of the conjecture.

### $q$-deformation: the open structural step

For $q \ne 1$, the q-deformed weight is $\tilde w_\lambda = \dim_q^2(\lambda)/[3A]_q!$
and the LR identity generalises to a **q-Schur duality**

$$
  \sum_\lambda c_{\mu, \nu}^\lambda \dim_q^2(\lambda) / \dim(\lambda)
   \stackrel{?}{=}
  \binom{3A}{3}_q \cdot (\text{factor depending only on } \mu, \nu),
$$

where $\binom{3A}{3}_q$ is the q-binomial. The conjecture is that this
identity yields an $A$-independent residual after factoring out
$[3A]_q! / [3A-3]_q!$. Empirically it holds to 4 digits at $q_0 \approx
1.11$ across $A \in \{2, 3\}$; structural proof via the q-Schur–Weyl
duality for $H_n(q)$ acting on tensor products of $\mathrm{U}_q(\mathfrak{sl}_n)$-
modules is pending.

### Significance

Block-multiplicativity reduces the $T_1^{\text{free}}$ term of the
mass-endomorphism tower
([`prop:mass-endomorphism-tower`](#prop:mass-endomorphism-tower)) from
an $O(p(3A) \cdot 3A^3)$ character-sum compute to an $O(1)$
exponentiation:

$$
  T_1^{\text{free}}(K) = v_p^Z \cdot v_n^N.
$$

Together with the structural identities
$T_1^{\text{atom}}(K) = 0$ (interface generator zeros the product)
and

$$
  T_2^{\text{diff}}(K) = (Z-1) \delta_{pp} + (N-1) \delta_{nn} + \delta_{pn},
   \quad
  \delta_{XY} = \mathrm{Li}_2^q(1) - \mathrm{Li}_2^q(|\hat V^{XY}_{\text{inter}}|),
$$

this gives a **closed-form $B^{(1)}_{\text{dim}}(Z, N)$** computable
in microseconds for any $(Z, N)$ — bypassing the $H_{3A}$ character
sum entirely beyond the one-time $H_6$ calibration of
$\{v_p, v_n, |\hat V^{pp}_{\text{inter}}|, |\hat V^{nn}_{\text{inter}}|\}$.

the canonical formalism
applies this to 16 atoms (D $\to$ ${}^{56}$Fe) in $< 1$ s total, all signs correct;
finer agreement awaits the $T_3$ pair-term closure (see
[`prop:mass-endomorphism-tower`](#prop:mass-endomorphism-tower)
§T_3 deferral).
<!-- FILE_END: block-multiplicativity-v-free.md -->

<!-- FILE_START: wenzl-A-operator.md -->
**Definition (Wenzl A-operator).**
*Let $\lambda \vdash n$ with $n = n_1 + n_2$, and let
$I = \sigma_{n_1} \in \mathbf{H}_n(q)$ be the inter-block interface
generator joining $\mathbf{H}_{n_1}(q)$ and $\mathbf{H}_{n_2}(q)$. In the
Wenzl 1988 Littlewood–Richardson decomposition of the restriction*

$$
  V_\lambda \;\downarrow_{\mathbf{H}_{n_1}(q) \otimes \mathbf{H}_{n_2}(q)}
  \;=\; \bigoplus_{\mu \vdash n_1,\; \nu \vdash n_2}
        c^\lambda_{\mu\nu}\,(V_\mu \boxtimes V_\nu),
$$

*the **Wenzl A-operator** $A^\lambda_{\mu\nu}(I)$ is the $(\mu, \nu)$-block
of $I$ acting on the corresponding isotypic summand:*

$$
  A^\lambda_{\mu\nu}(I) \;\in\; \mathrm{End}(V_\mu \otimes V_\nu)^{\oplus c^\lambda_{\mu\nu}},
$$

*where $c^\lambda_{\mu\nu}$ is the
[Littlewood–Richardson coefficient](lr-coefficient-hecke.md).*

## Role

The A-operator is the operator-valued payload of Wenzl 1988 Sub-lemma 2.1:
for $\beta_1 \in \mathbf{H}_{n_1}(q)$, $\beta_2 \in \mathbf{H}_{n_2}(q)$,

$$
  \chi^\lambda(\beta_1 \cdot I \cdot \beta_2)
    = \sum_{\mu \vdash n_1,\; \nu \vdash n_2}
      c^\lambda_{\mu\nu}\,
      \mathrm{Tr}\!\bigl(A^\lambda_{\mu\nu}(I)\,
                         (\rho_\mu(\beta_1) \otimes \rho_\nu(\beta_2))\bigr).
$$

Two downstream blocks consume it:

- [`prop:crystal-r-matrix-sub-lemma`](crystal-r-matrix-sub-lemma.md)
  reads its matrix-entry **pole order** at $q \to 0$
  ($\mathbf{1}[\rho_T(i) \le -1]$, conditional on
  [`conj:crystal-graph-realization`](crystal-graph-realization.md)).
- [`prop:operator-valued-combiner-convergence`](operator-valued-combiner-convergence.md)
  accumulates its **per-peel contributions** into the per-isotope binding
  tower.

## Computational realisation

The matrix entries of $A^\lambda_{\mu\nu}(I)$ at the substrate $q_0$ are
extracted by the bilinear-system solver
the canonical formalism,
with per-level witnesses
`A-operator-extract-h{n}-{iface}.witness.json`. The $\mathbf{H}_6$
(deuteron) extract is full-rank; the $\mathbf{H}_{9+}$ extracts are
least-squares fits over the inner-test family, so a *universal*
A-operator — the input required for a concrete
[`prop:operator-valued-combiner-convergence`](operator-valued-combiner-convergence.md)
instance — remains the research-grade open item.

## Lean

[`wenzl-A-operator.lean`](wenzl-A-operator.lean) names the operator data as a
class `WenzlAOperator` carrying the per-`(λ, μ, ν, I)` block slot and its LR
multiplicity. This is a naming/structure block (no semantic claim beyond the
existence of the operator data), so it carries no `sorry`.
<!-- FILE_END: wenzl-A-operator.md -->

<!-- FILE_START: crystal-r-matrix-sub-lemma.md -->
<!-- Theorem (conditional on:
       conj:crystal-graph-realization,
       prop:hecke-branching-trace-decomposition). -->

**Proposition (Crystal R-matrix Sub-lemma 2.1, operator-valued
form, conditional on
[`conj:crystal-graph-realization`](crystal-graph-realization.md)).**
*Let $\mathbf{H}_n(q)$ be the Iwahori–Hecke algebra over $R$ with
$q$ generic, $\lambda \vdash n$, and $\beta_1 \in \mathbf{H}_{n_1}(q)$,
$\beta_2 \in \mathbf{H}_{n_2}(q)$ with $n = n_1 + n_2$. Let
$\sigma_i \in \mathbf{H}_n(q)$ be a boundary generator and let
$A^\lambda_{\mu, \nu}(\sigma_i) \in \mathrm{End}(V_\mu \otimes V_\nu)^{\oplus c^\lambda_{\mu, \nu}}$
be its $(\mu, \nu)$-block in the
Wenzl 1988 LR decomposition
of $V_\lambda \downarrow_{\mathbf{H}_{n_1} \otimes \mathbf{H}_{n_2}}$.*

*Under
[`conj:crystal-graph-realization`](crystal-graph-realization.md)
(Brundan–Kleshchev iso $\mathbf{H}_n(R, q) \xrightarrow{\sim} R_\Lambda^{\mathrm{cyc}}(\mathfrak{sl}_n)$
plus the Kashiwara crystal limit at $q \to 0$), the matrix-entry
pole order of $A^\lambda_{\mu, \nu}(\sigma_i)$ at $q = 0$ on any
standard Young tableau $T \in \mathrm{SYT}(\lambda)$ in the
$(\mu, \nu)$-block is*

$$
  \boxed{\;\;
    \mathrm{pole}\bigl(A^\lambda_{\mu, \nu}(\sigma_i),\, T\bigr)
    \;=\;
    \mathbf{1}\bigl[\rho_T(i) \le -1\bigr]
  \;\;}
$$

*where*

$$
  \rho_T(i) \;:=\; c(\text{cell of }i{+}1\text{ in }T) - c(\text{cell of }i\text{ in }T),
  \qquad c(\square) \;:=\; \mathrm{col}(\square) - \mathrm{row}(\square)
$$

*is the **axial distance** between the cells of $i$ and $i + 1$ in $T$.*

## Closure of the W-3 residual

The
[scalar form of Sub-lemma 2.1](../../../docs/audits/-sub-lemma-2-1-categorical-proof.md)
suffices for the W-3 D(u) closure at the column maximizer
$\lambda^* = (1^p)$ (1-dim irrep). The
[refined / operator-valued form](../../../docs/audits/-sublemma-2-1-refined.md)
was open for general multidim $\lambda$ (verified canonical 11/11
on the deuteron, but lacked a categorical proof).

This block closes the operator-valued form **categorically modulo**
[`conj:crystal-graph-realization`](crystal-graph-realization.md):

- **Step 1** of the audit: $q \to 0$ limit of $\sigma_i$ on the
  seminormal basis is the combinatorial $R$-matrix on
  $B_\mu \otimes B_\nu \subset B_\lambda$.
- **Step 2**: pole order is the indicator $\mathbf{1}[\rho_T(i) \le -1]$
  (this proposition).
- **Step 3**: the LR-supported $(\mu^*, \nu^*)$ achieving the maximum is
  column-rich (the $p$ boundary cells of $\lambda$ form a single column).
- **Step 4** ([cycle composition](#prop:alpha-shift-torus-knot)):
  $\alpha_{\mathrm{shift}}(T_{(p, k)}) = k \cdot (p - 1)$ — recovered
  in $\sim$10 lines of combinatorics (no Hoefsmit matrix entries).

## Conditional-class hypothesis (AGENTS.md §3b-cond)

The Lean file at
[`crystal-r-matrix-sub-lemma.lean`](crystal-r-matrix-sub-lemma.lean)
declares

```lean
class CrystalRMatrixSubLemma (R : Type u) [CommRing R] (q : R)
    [C : CrystalGraphRealization R q] where
  poleIndicator : ℤ → Bool
  pole_indicator_correct : ∀ rho : ℤ,
    poleIndicator rho = decide (rho ≤ -1)
```

with the upstream `[CrystalGraphRealization R q]` as an explicit
`[Instance]` hypothesis, satisfying the §3b-cond conditional-class
exception. A trivial model
(`CrystalRMatrixSubLemma.trivialModel`) proves the class
axiomatisation is **consistent** (no `sorry` introduced). The
unconditional structural lemmas
`poleIndicator_minus_one_eq_true`, `poleIndicator_plus_one_eq_false`,
`column_syt_pole_per_cycle`, and the AXKIA sanity checks
`axkia_pole_T_2_9`, `axkia_pole_T_3_5` are all proved by `rfl` /
`decide` from the class field, requiring no further hypothesis.

## canonical structural verification (witness)

the canonical formalism
computes the column-SYT pole-per-cycle for seven torus-knot
interfaces $\{T_{(2, 1)}, T_{(2, 3)}, T_{(2, 5)}, T_{(2, 9)}, T_{(3, 4)}, T_{(3, 5)}, T_{(3, 7)}\}$
plus six non-column $\lambda$ shapes for $n \in \{2, 3, 4\}$.
[`crystal-pole-order.witness.json`](../../../computations/crystal-pole-order.witness.json)
records 21 / 21 passing assertions, including the
[AXKIA chain](alpha-em-categorical-trace.md) values
$\alpha_{\mathrm{shift}}(T_{(2, 9)}) = 9$ and
$\alpha_{\mathrm{shift}}(T_{(3, 5)}) = 10$, giving
$\alpha_{\mathrm{EM}}^{-1} = q \cdot [9]_q \cdot [10]_q$
combinatorially.

## Bridge to `prop:confinement-nf-partial-proof`

The class instance produced by this block can be used to populate
`HasBranchingBlockLemma` in
[`confinement-nf-partial-proof.lean`](confinement-nf-partial-proof.lean)
via the Step 4 cycle composition. With both instances in scope,
the operator-valued form of `theorem_2_shift_decomposition` becomes
a categorical theorem (no `sorry` at the math level — only the two
routine LP-theory `sorry`s remain in the partial-proof file, which
are out of scope for this proposition).
<!-- FILE_END: crystal-r-matrix-sub-lemma.md -->

<!-- FILE_START: operator-valued-combiner-convergence.md -->
<!-- Proposition (conditional on:
       conj:crystal-graph-realization (via the Wenzl A-operator class),
       prop:crystal-r-matrix-sub-lemma,
       prop:lr-coefficient-hecke). -->

**Proposition (operator-valued combiner convergence, conditional on
[`conj:crystal-graph-realization`](crystal-graph-realization.md) via the
Wenzl A-operator class).**
*Let $\beta_{\mathrm{atom}}$ be the canonical $A$-nucleon atomic braid in
$\mathbf{H}_{3A}(q)$, with inter-nucleon interfaces at the peel levels
$n_k = 3(A - k + 1)$. Write $\chi^\lambda_A := \chi^\lambda(\beta_{\mathrm{atom}})$
for the level-$A$ character. Then the iterated application of the
operator-valued [Sub-lemma 2.1](crystal-r-matrix-sub-lemma.md) — each peel
weighted by the [Littlewood–Richardson coefficient](lr-coefficient-hecke.md)
$c^\lambda_{\mu\nu}$ — assembles into a single convergent representation:
the value at level $A + 1$ is the LR-weighted value at level $A$,*

$$
  \boxed{\;\;
    \mathrm{cv}(A + 1) \;=\; w(A)\,\cdot\,\mathrm{cv}(A),
    \qquad A \ge 2,
  \;\;}
$$

*so that the character of an arbitrarily large atom is the deuteron
($A = 2$) base case accumulated through the LR-weight tower:*

$$
  \mathrm{cv}(2 + m) \;=\; \Bigl(\textstyle\prod_{j = 0}^{m - 1} w(2 + j)\Bigr)\,\cdot\,\mathrm{cv}(2),
  \qquad m \ge 0,
$$

*where $\mathrm{cv}(A)$ is the combiner value at peel level $A$ and $w(A)$
is the LR weight entering the peel $A \to A + 1$.*

## Categorical interpretation

The proposition is the **convergence content** of the operator-valued
Wenzl branching combiner: the atomic Markov trace
$\mathrm{tr}_M(\beta_{\mathrm{atom}}) = \sum_\lambda y_\lambda\,\chi^\lambda_A$
need not be recomputed at full strand count $3A$ for each isotope.
Instead it is *peeled* one nucleon at a time — each peel is a single
application of Sub-lemma 2.1, multiplying the running value by the
LR-weighted A-operator contribution of the newly attached nucleon block.
The recursion bottoms out at the deuteron, the smallest two-nucleon
interface, which is computed directly at $\mathbf{H}_6$. The "tower" of
weights $w(2), w(3), \dots$ is exactly the per-interface
[`def:wenzl-A-operator`](wenzl-A-operator.md) data, and the product form
exhibits the per-isotope binding tower as a telescoping accumulation
rather than an independent high-strand computation.

## Conditional-class hypothesis (AGENTS.md §3b-cond)

The compiled Lean home is
[`QOU.BraidKnot.OperatorValuedCombiner`](../../../content/quantum-observable-universe/lean/QOU/BraidKnot/OperatorValuedCombiner.lean),
which axiomatises the combiner as a `class WenzlAOperator` carrying
`combinerValue`, `lrWeight`, and the `branching_recursion` field
(the one-step recursion above). The convergence theorem

```lean
theorem operator_valued_combiner_convergence
    [W : WenzlAOperator R q] :
    ∀ n : ℕ, W.combinerValue (n + 2) = iteratedCombinerValue W n
```

is proved by `Nat.rec` from that field, so it is **fully Lean-verified
modulo the `[WenzlAOperator R q]` instance hypothesis**. No instance is
provided: the missing instance — universal $A^\lambda_{\mu\nu}(I)$
extracts at $\mathbf{H}_{9+}$ — *is* the research-grade conjecture, and
the dependency cone reaches
[`conj:crystal-graph-realization`](crystal-graph-realization.md) through
[`prop:crystal-r-matrix-sub-lemma`](crystal-r-matrix-sub-lemma.md).

## Production wiring and verification

The recursion is realised in
the canonical formalism
(`compute_tr_m_via_branching`), wired into the canonical mass table via
`--method branching` in
the canonical formalism:

- **$A = 2$ (deuteron)** runs the operator-valued branching end-to-end,
  agreeing with `markov_peel.tr_M_atomic` at $0.72$ ppb (Phase A
  baseline).
- **$A \ge 3$** delegates to the production native Hoefsmit kernel
  $\mathrm{tr}_M = \sum_\lambda y_\lambda\,\chi^\lambda$, which handles
  every $A$ — including the color-weighted $p$–$n$ interface that the
  symbolic `markov_peel` path cannot represent.

## Lean formalization

**Conditional theorem (Lean-verified modulo the
[`def:wenzl-A-operator`](wenzl-A-operator.md) class instance).** The
convergence recursion and its product unwinding hold for every commutative
ring $R$; the only unproved input is the existence of a concrete combiner
instance, which is the universal-extract conjecture documented in the audit
trail (`docs/audits/2026-06-02-subgoal-1-phase-a-baseline.md`).
<!-- FILE_END: operator-valued-combiner-convergence.md -->

<!-- FILE_START: depth-stratified-frobenius-reciprocity.md -->
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

### Categorical content of the FR refinement

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

the canonical formalism
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
 (the canonical formalism)
 or the symbolic Hoefsmit pipeline. the formalism
 the canonical formalism
 (from ) carries this end-to-end with KnotInfo cross-validation.

### Lean formalisation

[`qou:QOU.BraidKnot.depth_stratified_frobenius_reciprocity`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/DepthStratifiedFrobeniusReciprocity.lean)
axiomatises the FR refinement as a class hypothesis (per
AGENTS.md §3b-cond). Downstream theorems depending on the
FR-corrected mass formula consume this class as an explicit
`[Instance]` hypothesis. The classical-limit case ($k = 0, 1, 2, 3$
at $q = 1$) reduces to standard Frobenius reciprocity for $S_n$ —
provable in Mathlib via `Representation.induced` and
`Representation.restricted`.

### Role as the final structural ingredient

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
<!-- FILE_END: depth-stratified-frobenius-reciprocity.md -->

<!-- FILE_START: eigenvalue-product-expansion.md -->
**Proposition.**
*For a nucleus with $Z$ protons and $N$ neutrons ($A = Z + N$),
the symmetric channel eigenvalue product of the nuclear braid in the
$[2{,}1]$ representation of $H_3(R, q)$ is:*

$$
  \Lambda_{\mathrm{sym}}
  = q^{(Z-N)(A-1)/2} \cdot \Bigl(\frac{[2]_q}{2}\Bigr)^{\!ZN}
$$

*Its logarithm expands in the isospin variable $T = |Z - N|/2$ as:*

$$
  \ln|\Lambda_{\mathrm{sym}}|
  = \underbrace{\ell_2 \cdot \frac{A^2}{4}}_{\mathrm{(I)}}
  \;+\; \underbrace{\ell \cdot T \cdot A}_{\mathrm{(II)}}
  \;-\; \underbrace{\ell \cdot T}_{\mathrm{(III)}}
  \;-\; \underbrace{\ell_2 \cdot T^2}_{\mathrm{(IV)}}
$$

*where $\ell = \ln q$ and $\ell_2 = \ln([2]_q/2)$.*

*The four terms are:*

| *Term* | *Scaling* | *Origin* |
|:---:|:---:|:---:|
| *(I)* | *$A^2$* | *pn crossing count $ZN = A^2/4 - T^2$* |
| *(II)* | *$T \cdot A$* | *pp vs nn crossing excess $(Z-N)(A-1)/2$* |
| *(III)* | *$T$* | *linear isospin correction* |
| *(IV)* | *$T^2$* | *quadratic isospin (Casimir)* |

*The Coulomb correction arises separately from the standard channel,
where pp crossings contribute eigenvalue $q$ (not $[2]/2$), and the
excess*

$$
  \ln\Bigl(\frac{2q}{[2]_q}\Bigr)
  = \ln\Bigl(\frac{2q}{q + q^{-1}}\Bigr)
  \approx \frac{h^2}{2}
$$

*generates a term proportional to $Z(Z-1)$.*

*The $q$-integer $[c+1]$ in each Bethe--Weizsäcker coefficient counts
the geometric sum of eigenvalue powers over $c$ crossings:*

$$
  [c+1]_q = \sum_{j=0}^{c} q^{c - 2j}
$$

*For the Borromean braid ($c = 6$), this gives $[7]_q$.
For the figure-eight braid ($c = 4$), this gives $[5]_q$.*
<!-- FILE_END: eigenvalue-product-expansion.md -->

<!-- FILE_START: knot-operator-lp-selection.md -->
**Proposition (knot-operator LP/SDP selection via Gram-inverse dual basis; conditional on [`conj:weak-spectral-completeness`](#conj:weak-spectral-completeness)).**

*Let $R$ be the categorical coefficient ring with $q \in R$ generic
(not a root of unity in $R$ — note $q = 1$ IS excluded), and let
$H_n(q)$ be the Iwahori-Hecke algebra over $R$ in the standard
generators ([Hecke-Skein convention](https://github.com/litlfred/qou/blob/main/AGENTS.md) §7a).
Let $\{b_i\}$ be a Frobenius-non-degenerate basis (e.g. the
Gröbner-Shirshov NF basis $\{\gamma, \sigma_0, \sigma_1, L_+, L_-,
e^-\}$ for $H_3(q)$ on three strands). Then for any confinement
target $T \in H_n(q)$ — a bound-state defined by a vector of
required NF-channel multiplicities $n_T = (n_T^i)_{i=1}^{|\text{basis}|}
\in R^{|\text{basis}|}$ — the selection of a knot operator
$\beta(T_{m,m'}) \in H_n(q)$ producing $T$ is determined by the
Frobenius-Gram-inverse LP/SDP dual basis:*

$$
  \min_{\substack{x \geq 0 \\ G^{-1} S x \;\geq\; n_T}}
  \;\;\sum_{m'} t_{(m, m')} \, x_{(m, m')},
$$

*where $S = (s_{i,(m, m')})$ is the supply matrix encoding which
NF channel each torus knot $T_{m,m'}$ produces (computed by
[`knot-operator-table.witness.json`](https://github.com/litlfred/qou/blob/main/computations/knot-operator-table.witness.json)
for $H_3(q)$ matter operators and
[`knot-operator-table-h2.witness.json`](https://github.com/litlfred/qou/blob/main/computations/knot-operator-table-h2.witness.json)
for $H_2(q)$ EW even-twist links), $t_{(m, m')}$ is the crossing
energy ($q$-rational expression in $R$), and $G^{-1}$ is the
Frobenius co-Casimir Gram-inverse.*

*By Schrijver §7.4 strong duality + complementary slackness, the
LP dual variables $(y_0^*, y^*)$ supply:*

- *the **shadow price** $y_0^*$ of the net-multiplicity
  constraint;*
- *per-NF-channel **Frobenius positivity shadow prices** $y_i^* \geq
  0$ for each demand channel;*
- *the **active set** $A^*(T) := \{(m, m') : x_{(m, m')}^* > 0\}$
  identifying which knot operators actually contribute to the
  bound state $T$.*

*The selected operator is the unique $T_{m,m'}$ with $x_{(m,
m')}^* > 0$ when $A^*(T)$ is a singleton; otherwise the bound
state is a Wedderburn superposition with weights given by
$x^*$.*

### Statement (formal)

Define the **demand profile** of a confinement $T$ as the negative
NF coefficients (knot-operator basis table)
of the formal product $T = \prod_i b_i^{n_T^i}$. Define the
**supply profile** of a candidate knot operator $\beta(T_{m,m'})$
as the vector of positive NF coefficients in $b_i \cdot
\beta(T_{m,m'}) \cdot b_j$ ranging over basis pairs $(b_i, b_j)$.

The LP

$$
  \begin{aligned}
    \min_{x \geq 0} \quad & \sum_{(m, m')} t_{(m, m')} \, x_{(m, m')} \\
    \text{s.t.} \quad     & \sum_{(m, m')} S_{i, (m, m')} \, x_{(m, m')}
                            \;\geq\; n_T^i, \qquad i = 1, \ldots, \dim H_n(q),
  \end{aligned}
$$

is feasible iff the bound state $T$ is **realisable** —
i.e. iff the demand profile lies in the positive cone spanned by
the supply profiles. The Frobenius pairing
$\langle \cdot, \cdot \rangle_F$ on $H_n(q)$ provides the natural
inner product underlying the SDP relaxation.

**The Gram-inverse $G^{-1}$ is the canonical dual basis** for the
constraint matrix: rewriting the LP in the dual basis transforms
the constraint $S x \geq n_T$ into $\widetilde{S} x \geq G^{-1}
n_T$ where $\widetilde{S}$ is sparse (each torus knot couples to
at most a small fixed number of dual-basis directions). This is
the LP-rewriting that makes operator selection efficient.

### Existence + uniqueness of the selection

*By LP duality (Schrijver §7.2 strong duality), if the LP is
feasible, the optimal active set $A^*(T)$ is determined by the
complementary slackness condition*

$$
  y_i^* > 0 \;\;\Longleftrightarrow\;\;
  \text{constraint } i \text{ is tight at } x^*.
$$

*The active set is generically unique (Schrijver §7.4); ties
correspond to degenerate confinements with a continuous family of
operator-selection equivalents.*

### Existing instances (from witness data)

Per [`confinement-operator-selection.witness.json`](https://github.com/litlfred/qou/blob/main/computations/confinement-operator-selection.witness.json):

| Confinement | Active operator (LP-optimal) | NF demand | Crossing energy $t_{(m,m')}$ |
|-------------|------------------------------|-----------|-----------------------------:|
| Proton | $L_+ = \sigma_0\sigma_1$ | 0 | $\approx 0.152$ at $q_0$ |
| Neutron | $L_+ = \sigma_0\sigma_1$ | 0 | $\approx 0.106$ at $q_0$ |

Per [`knot-operator-table-h2.witness.json`](https://github.com/litlfred/qou/blob/main/computations/knot-operator-table-h2.witness.json):

- **EW carriers** $T(2,4), T(2,6), T(2,8)$ in $H_2(q)$ select the
  Wedderburn-(sym, alt) projector pair as the LP-active set,
  superseded — see Hoefsmit n=6 lift below.

### EW-sector LP/SDP-dual input via Wedderburn-pair volumes

The EW-sector instance of this proposition draws its supply
matrix from the Wedderburn-block-decomposed pair amplitude
$|V_i V_j|_{\rm Wedderburn}$ defined in
the canonical formalism
(integrated from  commit `06305f30c`):

$$
  |V_i V_j|_{\rm Wedd}
  \;=\;
  w_{\rm sym} \cdot \lambda_i^{\rm sym} \lambda_j^{\rm sym}
  \;+\; w_{\rm std} \cdot \mathrm{tr}_{\rm Markov}(M_i M_j)\big|_{\rm std\ block}
  \;+\; w_{\rm alt} \cdot \lambda_i^{\rm alt} \lambda_j^{\rm alt},
$$

where $M_i$ are the full $2 \times 2$ transfer matrices (not just
the $(m_{21}, m_{22})$ bottom row used by the basic
`hecke_core.atom_per_generator_volumes`).

**LP/SDP-dual pair amplitudes for the EW sector:**

| Pair | Categorical interpretation |
|------|----------------------------|
| $\|V_W V_Z\|_{\rm Wedd}$ | LP-active edge: $W^\pm \leftrightarrow Z$ coupling via shared sym/alt block on $V^{\otimes 6}$ |
| $\|V_Z V_H\|_{\rm Wedd}$ | LP-active edge: $Z \leftrightarrow H$ Higgs vacuum-induced linkage |
| $\|V_W V_H\|_{\rm Wedd}$ | LP-active edge: $W^\pm \leftrightarrow H$ Yukawa-like coupling |
| $\|V_W V_W\|_{\rm Wedd}$ | self-pair amplitude for $W^\pm$ (charge-2 channel) |

These amplitudes feed the supply matrix $S$ in the LP for the EW
operator-selection instance. Combined with the Hoefsmit
cell-content multiplicities $(4, 2, 1, 3, 3, 1, 2, 4)$ of
[`thm:hoefsmit-ew-cell-content`](#thm:hoefsmit-ew-cell-content),
they determine the active set $A^*(T)$ for each EW confinement
target.

The LP dual variables (shadow prices) $y^* \geq 0$ then identify
the saturated demand channels — the EW-sector analog of the
existing $\{e^-, L_+, L_-, \gamma\}$ active-set extraction for
matter operators.
### Audit-flag impact

*Closing this proposition would close the methodological
discontinuity in the **FROB-FILTER** flag (the
Frobenius-positivity activation threshold between $A = 3$ and
$A = 6$ in
[`docs/audits/-nv-frob-filter-conjectures.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-nv-frob-filter-conjectures.md)):
the activation rule becomes a **derived consequence** of
LP/SDP duality, not an empirical fit per atomic mass.*

**Witness inputs.**
[`gram-matrix-dual.witness.json`](https://github.com/litlfred/qou/blob/main/computations/gram-matrix-dual.witness.json),
[`knot-operator-table.witness.json`](https://github.com/litlfred/qou/blob/main/computations/knot-operator-table.witness.json),
[`knot-operator-table-h2.witness.json`](https://github.com/litlfred/qou/blob/main/computations/knot-operator-table-h2.witness.json),
[`confinement-operator-selection.witness.json`](https://github.com/litlfred/qou/blob/main/computations/confinement-operator-selection.witness.json).

**Audit doc.** [`docs/audits/-path-alpha-bring-refinement.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-path-alpha-bring-refinement.md).
<!-- FILE_END: knot-operator-lp-selection.md -->

