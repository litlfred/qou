**Conjecture (categorical linking operation $\mathrm{Lk}_R$).**
*Let $\mathbf{C}$ be a rigid monoidal $R$-linear category with
braiding $c_{X, Y} \colon X \otimes Y \to Y \otimes X$
([rigid monoidal](#def:rigid-monoidal-category)), and let $A$ be
the substrate algebra
([Frobenius-Hopf substrate](#def:frobenius-hopf-substrate)). The
**categorical linking operation** is the family of $R$-linear maps,
indexed by integer linking number $k \in \mathbb{Z}$,*

$$
  \mathrm{Lk}_R^{(k)}
  \;\colon\;
  \mathrm{Hom}_R(\mathbf{1}, A) \otimes_R \mathrm{Hom}_R(\mathbf{1}, A)
  \;\longrightarrow\;
  \mathrm{End}_R(A),
$$

*defined by**

$$
  \mathrm{Lk}_R^{(k)}(a, b)
  \;:=\;
  (\mathrm{id}_A \otimes \tau_R) \,\circ\,
  \bigl( c_{A, A}^{\,k} \circ (a \otimes b) \otimes \mathrm{id}_A \bigr)
  \,\circ\, \mathrm{id}_A,
$$

*where $\tau_R \colon A \to \mathbf{1}$ is the Frobenius trace and
$c_{A, A}^{\,k}$ is the $k$-fold braiding of $A$ with itself
($k$ counted with sign — positive crossings vs negative crossings
algebraically).*

*Equivalently, $\mathrm{Lk}_R^{(k)}(a, b)$ is the categorical
**trace-cut** of the 2-component link $\hat\beta(a) \cup \hat\beta(b)$
with linking number $k$: closing one component via $\tau_R$ leaves
the other as an endomorphism of $A$.*

### Statement (formal)

The categorical linking operation $\mathrm{Lk}_R^{(k)}$ has the
following properties (each is conjectural; status open):

1. **Linearity.** $\mathrm{Lk}_R^{(k)}$ is $R$-linear in each
   factor separately.
2. **Reduction at $k = 0$.** $\mathrm{Lk}_R^{(0)}(a, b) = (\tau_R(b))
   \cdot a^*$ where $a^*$ is the dual morphism of $a$ in
   $\mathrm{End}_R(A)$ (no linking ⟹ disjoint trace closure ⟹
   scalar multiplication).
3. **Multiplicativity in $k$.** $\mathrm{Lk}_R^{(k_1 + k_2)}(a, b)
   = c_{A, A}^{\,k_2} \cdot \mathrm{Lk}_R^{(k_1)}(a, b)$ (linking
   composes additively in the integer index).
4. **Trace-cut symmetry.** Cutting via $\tau_R \otimes \mathrm{id}_A$
   instead of $\mathrm{id}_A \otimes \tau_R$ produces the
   $\iota$-conjugate $\mathrm{Lk}_R^{(-k)}(b, a)$, where $\iota$
   is the bar involution on $R$.
5. **Compatibility with bar involution.**
   $\iota(\mathrm{Lk}_R^{(k)}(a, b)) = \mathrm{Lk}_R^{(-k)}(\iota(a),
   \iota(b))$. Equivalently: bar self-duality holds for $k = 0$ pairs;
   non-zero linking breaks bar self-duality by exactly the linking
   sign.

The first four are direct from the ribbon-category axioms once
the trace-cut definition is fixed; the fifth is the categorical
content needed for path-α-Bring's even-twist parity rule
([prop:even-twist-torus-link-psd-feasibility](#conj:electroweak-higgs-torus-link-triplet)).

### Why this is the right operation for the Higgs mechanism

Per [`conj:categorical-higgs-mechanism`](#conj:categorical-higgs-mechanism)
Step C, the Higgs mechanism's "Goldstone-eating" lifts a gauge
boson from $\mathrm{Hom}_R(\mathbf{1}, A)$ (1-component knot,
unbroken-symmetry mediator) to $\mathrm{End}_R(A)$ (2-component
link, broken-symmetry mediator). The categorical linking
operation $\mathrm{Lk}_R^{(1)}$ realises this lift exactly:

$$
  \begin{aligned}
    & \text{pre-EWSB:}
    && (\text{boson, Goldstone}) \in \mathrm{Hom}_R(\mathbf{1}, A)
       \otimes_R \mathrm{Hom}_R(\mathbf{1}, A) \\
    & \text{Higgs vacuum induces } \mathrm{Lk}_R^{(1)}: \\
    & \text{post-EWSB:}
    && \mathrm{Lk}_R^{(1)}(\text{boson}, \text{Goldstone})
       \in \mathrm{End}_R(A).
  \end{aligned}
$$

The mass of the post-EWSB boson is the Markov trace of this
endomorphism, weighted by the appropriate Hoefsmit projector
([`conj:hoefsmit-ew-cell-content`](#conj:hoefsmit-ew-cell-content)).

### Reduction to $\sigma_i^{2k}$ on disjoint strand-pairs

When $a, b$ are images of disjoint-strand-pair generators
$\sigma_{i}, \sigma_{j} \in B_n$ (with $|i - j| \geq 2$ to
guarantee far-commutativity), the operation $\mathrm{Lk}_R^{(k)}(a,
b)$ reduces to multiplication of the corresponding
$\sigma_i^{2 k_a} \cdot \sigma_j^{2 k_b}$ in $H_n(q)$ — exactly
the form used in
[`conj:hoefsmit-ew-cell-content`](#conj:hoefsmit-ew-cell-content)
for the EW carriers $W \leftrightarrow \sigma_1^4, Z
\leftrightarrow \sigma_3^6, H \leftrightarrow \sigma_5^8$ in
$B_6$.

### Status

**Open.** The categorical content above is internally
consistent with the ribbon-category framework, but each of the
five properties (linearity, reduction at $k=0$, multiplicativity,
trace-cut symmetry, bar-involution compatibility) requires a
formal proof in the QOU substrate-category. To promote to a
`proposition`:

1. **Construct $\mathrm{Lk}_R^{(k)}$** as a concrete morphism in
   $\mathbf{C}$ using the trace-cut formula above.
2. **Prove the five properties** above from the rigid-monoidal-
   category axioms + the Frobenius-trace structure on $A$.
3. **Verify the disjoint-strand-pair reduction** matches the
   Hoefsmit identification at $n = 6$.
4. **Discharge the bar-involution compatibility** by direct
   computation in $H_n(q)$ (path-α-Bring eigenvalue analysis).

### Audit-flag impact

If discharged, this conjecture supplies the categorical
**linking** operation needed by:

- [`conj:categorical-higgs-mechanism`](#conj:categorical-higgs-mechanism)
  Step C (Higgs mechanism as $\mathrm{Lk}_R^{(1)}$);
- [`conj:force-carrier-knot-vs-link-dichotomy`](#conj:force-carrier-knot-vs-link-dichotomy)
  Step 6 (broken-symmetry mediators are 2-component links);
- the Weinberg angle categorical block
  ([`conj:weinberg-angle-categorical`](#conj:weinberg-angle-categorical))
  — $\theta_W$ is realised via the relative ratio of
  $\mathrm{Lk}_R^{(1)}$ outputs on the W- and B-channels;
- the $N_v$ derivation pipeline (Tier C of
  [`docs/audits/2026-05-06-refocused-1ppb-workplan-v2.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-06-refocused-1ppb-workplan-v2.md)).
