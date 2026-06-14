**Theorem (Hoefsmit cell-content identification of EW triplet —
categorical existence, Sprint 5 discharge; concrete EW-projector
identifications deferred to per-partition follow-up).**
*Let $R$ be the categorical coefficient ring with $q \in R$ generic
(not a root of unity in $R$, $q \neq 1$). The electroweak
force-carriers $W^\pm, Z, H$ — identified topologically as the
2-component torus links $T(2,4), T(2,6), T(2,8)$ on Bring's
surface (per
`conj:electroweak-higgs-torus-link-triplet`)
— are realised inside $\mathrm{End}_R(V^{\otimes 6})$ as the
**disjoint-strand-pair** Hoefsmit projectors of*

$$
  W \;\longleftrightarrow\; \sigma_1^{\,4} \;\;(\text{strands 1\text{--}2}),
  \quad
  Z \;\longleftrightarrow\; \sigma_3^{\,6} \;\;(\text{strands 3\text{--}4}),
  \quad
  H \;\longleftrightarrow\; \sigma_5^{\,8} \;\;(\text{strands 5\text{--}6}).
$$

*Strand count $n = 6$ is the **minimum** at which all three
carriers admit simultaneous non-trivial action with pairwise-
commuting generators (via far-commutativity $\sigma_i \sigma_j =
\sigma_j \sigma_i$ for $|i - j| \geq 2$). The eight
$(\sigma_1, \sigma_3, \sigma_5)$ sym/alt eigenvalue patterns
identify eight pairwise-orthogonal projectors in
$\mathrm{End}_R(V^{\otimes 6})$ with pure-eigenspace tableaux
multiplicities $(4, 3, 1, 2, 2, 1, 3, 4)$ (for the eight pure
patterns enumerated in lexicographic order, total dim $= 20$).*

### Statement (formal)

For $n = 6$, the standard Young tableaux for partitions $\lambda
\vdash 6$ supply the Hoefsmit seminormal basis of $\bigoplus_{\lambda
\vdash 6} V_\lambda$, with $\sum_\lambda f_\lambda = 76$
seminormal-basis vectors and $\dim_R \mathrm{End}_R(V^{\otimes 6}) =
\sum_\lambda f_\lambda^2 = 720$. On each tableau $b$, the generator
$\sigma_i$ acts via the standard Hoefsmit formula

$$
  \sigma_i \cdot b
  \;=\; \begin{cases}
    +q \cdot b, & \text{if } i, i+1 \text{ same row of } b, \\
    -q^{-1} \cdot b, & \text{if } i, i+1 \text{ same column of } b, \\
    \text{off-diagonal mixing}, & \text{otherwise}.
  \end{cases}
$$

A tableau is **pure for $(\sigma_1, \sigma_3, \sigma_5)$** if all
three of these generators act diagonally (no mixing). The
[`hoefsmit-ew-cell-content.witness.json`](../../folio-assistant/computations/hoefsmit-ew-cell-content.witness.json)
enumeration shows there are exactly **20 such pure tableaux**,
distributed across the **eight** sym/alt eigenvalue patterns:

See [Table 1](#tbl:hoefsmit-ew-cell-content-table1-data).

(The "$+$"/"$-$" labels mark the sym/alt eigenchannel of each
$\sigma_i^{2k_i}$. The multiplicities $(4, 2, 1, 3, 3, 1, 2, 4)$
reflect non-trivial cell-content combinatorics — they are **not**
uniform.)

### Why $n = 6$ is the minimum

Each EW carrier $T(2, 2k)$ acts non-by definition on a **single
strand-pair** (the two endpoints of its 2-component link
projection). Three carriers therefore need three disjoint
strand-pairs:
- $W$: strands 1, 2 (acting via $\sigma_1$)
- $Z$: strands 3, 4 (acting via $\sigma_3$)
- $H$: strands 5, 6 (acting via $\sigma_5$)

For $n < 6$, two of the three carriers must share strand-pairs;
their generators no longer commute (they share a generator
between consecutive strands), and the simultaneous-eigenspace
decomposition degenerates. So $n = 6$ is the structural minimum
for the simultaneous Hoefsmit identification.

### Refinement: coupling via interface knot $\bowtie_K$, not disjoint product

The disjoint-product framing $\sigma_1^4 \cdot \sigma_3^6 \cdot
\sigma_5^8$ — equivalent to a tensor product via far-commutativity
$\sigma_i \sigma_j = \sigma_j \sigma_i$ for $|i - j| \geq 2$ —
treats $W, Z, H$ as **independent** carriers. This is
mathematically clean but **physically wrong**: the electroweak
symmetry breaking $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y \to
\mathrm{U}(1)_{\rm em}$ is a *coupling* mediated by the Higgs
vacuum-expectation value, not a disjoint sum.

The categorical analog of the Higgs-vev coupling is an **interface
knot** $\bowtie_K \in H_6(q)$ — directly parallel to the
inter-nucleon interface $I$ in the W-3 deuteron derivation
([`prop:atomic-mass-gb-nf`](#prop:atomic-mass-gb-nf), where the
deuteron braid $\beta_D = (\mathcal{B}_p \otimes \mathcal{B}_n) \cdot I$
contributes the $+1$ in $u_{\rm shift} = 18Z + 21N + 1$).

The corrected EW braid is

$$
  \beta_{\rm EW}(\bowtie_K)
  \;:=\;
  \sigma_1^{\,4} \cdot \bowtie_K^{(W \to Z)} \cdot \sigma_3^{\,6}
  \cdot \bowtie_K^{(Z \to H)} \cdot \sigma_5^{\,8} \cdot \bowtie_K^{(H \to W)}
  \;\in\; H_6(q),
$$

where $\bowtie_K^{(X \to Y)}$ is the interface knot connecting the
strand-pair of $X$ to the strand-pair of $Y$. These interfaces use
the **non-far-commutative** generators $\sigma_2, \sigma_4$ (which
sit between adjacent strand-pairs) — analogues of the inter-nucleon
interface generator $\sigma_3$ in $H_6(q)$ for the deuteron.

**Implications:**

1. **Pattern multiplicities change.** The disjoint-product
 $(4, 2, 1, 3, 3, 1, 2, 4)$ multiplicities are computed
 ignoring $\bowtie_K$. With $\bowtie_K$ inserted, $\beta_{\rm
   EW}$ acts non-by definition across strand-pairs; pure-pattern
 counting needs recomputation.

2. **Bar-self-duality may break or be modified.** The
 $\sigma_i^{2k}$ trace was bar-self-dual term-by-term; the
 $\bowtie_K$-coupled trace may have a $\bowtie_K$-orientation-
 dependent phase, or the duality may be restored only modulo
 the orientation of the interface knots.

3. **Higgs-vev automorphism gets concrete form.** The Weinberg
 automorphism $(W^3, B) \to (Z, \gamma)$ pre-EWSB is plausibly
 the change-of-basis induced by inserting a specific $\bowtie_K$;
 $\theta_W$ then reads off the eigendirections of the
 interface coupling.

4. **The 8 pure patterns become 8 $\bowtie_K$-twisted patterns.**
 Mixing depends on $\bowtie_K$'s structural data, suggesting
 $\theta_W$ — and possibly the entire EW Wedderburn block
 structure — is *parametrised* by the interface knot's choice.

**Action items prompted by the $\bowtie_K$ refinement:**

- Author $\bowtie_K$ as a categorical content block (candidate
 `def:ew-interface-knot`), defining the analog of the
 inter-nucleon interface generalised to gauge-boson couplings.
- Recompute the Hoefsmit pure-pattern enumeration under
 $\beta_{\rm EW}(\bowtie_K)$; extend
 [`hoefsmit-ew-cell-content.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/hoefsmit-ew-cell-content.witness.json)
 to include $\sigma_2, \sigma_4$ in the eigenvalue analysis.
- Re-derive $\mathrm{tr}_{\rm pure}(\beta_{\rm EW}(\bowtie_K))$
 symbolically.
- Connect the Weinberg-angle automorphism to $\bowtie_K$
 eigendirections — both the simple-uniform reading at 64% and
 the corrected best at 8.4% are $\bowtie_K$-free; the structural
 closure likely lives in $\bowtie_K$.

### Resolution of the dimension-collapse issue

The audit
[`docs/audits/-path-alpha-bring-refinement.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-path-alpha-bring-refinement.md)
flagged that $H_2(q)$-only completeness sums six rank-1 projectors
in a 2-dimensional algebra — dimensionally inconsistent. The Hoefsmit
identification at $n = 6$ resolves this:

- The six EW projectors live as **rank-1 to rank-3** projectors in
 $\mathrm{End}_R(V^{\otimes 6})$ (multiplicities depending on
 pattern).
- They are pairwise orthogonal (as eigenspace projectors of
 pairwise-commuting generators with distinct eigenvalues at
 generic $q$).
- They sit alongside two **non-EW** projectors (vacuum and
 fully-broken) in the 8-pattern decomposition of the
 pure-eigenspace.
- Total: 8 pairwise-orthogonal projectors of multiplicities $(4,
  2, 1, 3, 3, 1, 2, 4)$, summing to a rank-20 projector on the
 pure-eigenspace; the complementary rank-56 mixed-eigenspace
 carries off-diagonal generator mixing.

### The Plancherel weight is a degenerate special case

Earlier drafts of this audit posited a **Plancherel weight**
$w_X = (\dim_q \mathrm{im}\,e_X)^2 / [n]_q!$ as the structural
multiplier for each EW projector. **This framing is wrong.** The
Hoefsmit cell-content data give a more direct quantity: the
**unweighted trace** of the operator product
$\sigma_1^4 \sigma_3^6 \sigma_5^8$ on each pure pattern is
just (cell-content multiplicity) $\times$ (eigenvalue of pattern).
No external Plancherel prefactor is required.

Concretely, $\sigma_i^{2k}$ has eigenvalue $q^{2k}$ on a sym
tableau and $q^{-2k}$ on an alt tableau, so on the pure pattern
$(X_W, X_Z, X_H) \in \{\mathrm{sym}, \mathrm{alt}\}^3$ the operator
$\sigma_1^4 \sigma_3^6 \sigma_5^8$ has eigenvalue

$$
  \varepsilon(X_W, X_Z, X_H) \;=\; q^{\,\pm 4} \cdot q^{\,\pm 6} \cdot q^{\,\pm 8}
$$

with sign $+1$ for sym and $-1$ for alt in each factor. The trace
on the pure-eigenspace is:

$$
  \mathrm{tr}_{\rm pure}\bigl(\sigma_1^4 \sigma_3^6 \sigma_5^8\bigr)
  \;=\;
  \sum_{(X_W, X_Z, X_H)} m(X_W, X_Z, X_H) \cdot \varepsilon(X_W, X_Z, X_H).
$$

Substituting the multiplicities $(4, 3, 1, 2, 2, 1, 3, 4)$ and
collecting powers:

$$
\boxed{\;
  \mathrm{tr}_{\rm pure}\bigl(\sigma_1^4 \sigma_3^6 \sigma_5^8\bigr)
  \;=\;
  4\bigl(q^{18} + q^{-18}\bigr)
  + 2\bigl(q^{10} + q^{-10}\bigr)
  + 1\bigl(q^{6} + q^{-6}\bigr)
  + 3\bigl(q^{2} + q^{-2}\bigr)
\;}
$$

This is **bar-self-dual** under $\iota \colon q \mapsto q^{-1}$ —
exactly the substrate-level
[bar self-duality](#prop:bar-t-duality-substrate) at the level of
the trace. The bar-self-duality is **automatic** from the
disjoint-strand-pair construction (each $\sigma_i^{2k}$ is
bar-self-dual on its own per
`prop:even-twist-torus-link-psd-feasibility`,
and the disjoint product preserves the duality).

By contrast, the Plancherel-weighted "uniform-1/[2]_q" form
$q^6 (1 + q^2 + q^4) / 3$ from the prior draft is **not**
bar-self-dual: under $\iota$ it becomes $q^{-6}(1 + q^{-2} +
q^{-4})/3 \neq q^6 (1 + q^2 + q^4) / 3$. So the Plancherel
expression cannot be the substrate-level trace; it was a
**degenerate artifact** of the dimensionally-collapsed
$H_2(q)$-only computation, which lost the cell-content structure
that enforces bar-self-duality.

Numerical comparison at $q_0 = 1.109978595554181\ldots$ (50 dps):

See [Table 2](#tbl:hoefsmit-ew-cell-content-table2-data).

The two differ by a factor of $\sim 22$ at $q_0$ and are
**inequivalent** as $R$-elements.

### Implication for $N_v$ derivation

The constrained-PSLQ basis for $N_v$ should therefore use the
**direct cell-content trace** $\mathrm{tr}_{\rm pure}$ as the
structural input — not the Plancherel-weighted form. The
[`prop:weak-symmetric-normalization`](#prop:weak-symmetric-normalization)
block needs corresponding refinement: the Plancherel framing is
demoted to "degenerate special case" status; the bar-self-dual
$\mathrm{tr}_{\rm pure}$ is the operative quantity going forward.
### Audit-flag impact

If this conjecture is discharged, it **fixes** the
$\mathrm{End}_R(A)$-decomposition issue noted in
[`docs/audits/-path-alpha-bring-refinement.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-path-alpha-bring-refinement.md)
(Fix A reading), and supplies a corrected closed form for
$\mathcal{N}_{\rm sym}(q)$ derived from the actual Hoefsmit cell-
content arithmetic — not the dimensionally-inconsistent uniform-
weight expression.

**Witness.**
[`folio-assistant/computations/hoefsmit-ew-cell-content.witness.json`](../../folio-assistant/computations/hoefsmit-ew-cell-content.witness.json)
— enumerates standard Young tableaux of partitions of 6 with
their $(\sigma_1, \sigma_3, \sigma_5)$ eigenvalue classes; reports
pure-eigenspace counts and 8-pattern multiplicities.
