This remark develops the canonical projections, the classification of
QOU quantities by bar-type, the key algebraic identities, and the
bar-grading proofs for the [bar-involution](#def:bar-involution).

## The two canonical projections

The bar-involution is an involution: $\overline{\overline x} = x$.
Every Hecke-algebra element $x \in H_n(q)$ over a field of
characteristic $\ne$ 2 decomposes uniquely as

$$x \;=\; P_{\mathrm{avg}}(x) + P_{\mathrm{skew}}(x),$$

where

See [Table 1](#tbl:bar-involution-table1-data).

The framework's empirical content is that **$P_{\mathrm{avg}}$ is
the canonical projection** — the bar-symmetric part of every
Hecke-algebra computation is the physical/observable content; the
bar-anti-symmetric part is projected away.

> **Antiskew-vs-symmetric clarification.** $P_{\mathrm{avg}}(x)$
> is the bar-**even** (= bar-**symmetric**) projection. The
> framework retains $P_{\mathrm{avg}}$ ($\cos, \cosh, \mathrm{Li}_2^q$)
> and discards $P_{\mathrm{skew}}$ ($\sin, \sinh, \Phi_q$ alone).
> "Anti-skew" is only accurate in the discarding sense — the
> kept residual is symmetric/even.

## Classification of QOU quantities by bar-type

The canonical reference. Every quantity in the paper that has a
well-defined bar-action falls in one of these rows:

### Bar-symmetric (bar-even, $P_{\mathrm{avg}}$ image, retained)

See [Table 2](#tbl:bar-involution-table2-data).

### Bar-anti-symmetric (bar-odd, $P_{\mathrm{skew}}$ image, discarded)

See [Table 3](#tbl:bar-involution-table3-data).

### Trivial under bar (rational scalars)

See [Table 4](#tbl:bar-involution-table4-data).

## Key algebraic identities

### Half-step factorization of $h$

$$h \;=\; q - q^{-1} \;=\; \underbrace{(q^{1/2} - q^{-1/2})}_{h_{1/2},\;\text{bar-ANTI-sym}} \;\cdot\; \underbrace{(q^{1/2} + q^{-1/2})}_{1/z,\;\text{bar-SYM (Markov param)}}$$

The bar-anti-symmetry of $h$ comes *entirely* from $h_{1/2}$; the
bar-symmetric Markov parameter $z = 1/(q^{1/2}+q^{-1/2})$ factor
is bar-invariant. This is the same $z$ that the cross-PR Phase 5c.1 cross-check
identified as the interface-knot value $\bowtie_K = z$ exactly.

### Hoefsmit-Quantum-2 identity

$$\boxed{\;\; b^2(q) \;=\; 1 \,-\, \frac{1}{[2]_q^2} \;\;}$$

Proved as a pure algebraic identity over a field of char $\ne 2$;
no `sorry`. See [`prop:c5-involution-leibniz-decomposition`](#prop:c5-involution-leibniz-decomposition)
in the Lean sibling `hoefsmit_b_squared_eq_one_minus_inv_quantum_two_squared`.

### $c_5$ via quantum-2

$$c_5(q) \;=\; -b^2 - \tfrac{1}{2} \;=\; -\tfrac{3}{2} + \frac{1}{[2]_q^2}.$$

Proved as a corollary of the Hoefsmit-Quantum-2 identity; see
`c5_decomposition_via_quantum_two`.

### $c_5$ classical limit (commutative QOU)

$c_5(q=1) = -5/4$. Proved as `c5_classical_limit_eq_neg_five_quarters`.

### Commutative-QOU categorical identification of $-3/2$

The q-independent $-3/2$ in $c_5(q) = -3/2 + 1/[2]_q^2$ is identified
categorically as **half the dimension of the non-sign Wedderburn
blocks of $\mathbb{C}[S_3] = H_3(q=1)$**:

$$
-3/2 \;=\; -\frac{\dim V_{(3)} + \dim V_{(2,1)}}{2} \;=\; -\frac{1 + 2}{2}.
$$

The sign rep $V_{(1,1,1)}$ (dim 1) is excluded — it carries the
bar-anti-symmetric part of the Hopf-link Markov trace, projected
away by $P_{\mathrm{avg}}$. Proved as
`c5_classical_eq_wedderburn_nonsign_dim_half`.

This identifies the "−1/2 fingerprint" of the empirical
$c_5 = -b^2 - 1/2$ decomposition as the **bar-symmetric
Wedderburn-block contribution from the non-sign sector** in the
commutative limit — categorical content, not a quantum artifact.

### $c_5$ as a rational function of the bar-anti-symmetric Hecke skein

The closed form $c_5(q) = -3/2 + 1/[2]_q^2$ rewrites as a
function of the bar-anti-symmetric Hecke skein $h = q - q^{-1}$
alone, using the algebraic identity (PROVED in Lean as
`quantum_two_squared_eq_skein_squared_plus_four`):

$$
[2]_q^2 \;=\; (q + q^{-1})^2 \;=\; h^2 + 4
\quad\text{(from } q^2 + 2 + q^{-2} = (q^2 - 2 + q^{-2}) + 4\text{)}.
$$

Substituting:

$$
\boxed{\;\; c_5(q) \;=\; -\frac{3}{2} \,+\, \frac{1}{h^2 + 4}, \quad h = q - q^{-1}. \;\;}
$$

Both terms are **even functions of $h$** (the constant $-3/2$
by definition; $1/(h^2 + 4)$ because $h^2$ is bar-symmetric by
`IsBarAntiSymmetric.pow_two_mul`).

**Categorical reading**: this expresses $c_5$ purely as a function
of the universal bar-anti-symmetric kernel $h$ — the
`BarHeckeFunctor` $K \mapsto -3/2 + 1/(K^2 + 4)$ applied to
$K = h$. The Markov-trace-functor shape is now **explicit** for
$c_5$: it is the image of the bar-anti-symmetric skein under a
specific even rational function, which is exactly the
$P_{\mathrm{avg}}$-projection of the kernel through the
series-layer functor.

Proved in Lean as `c5_as_function_of_skein` (no `sorry`).

### Bar-grading algebraic structure (all PROVED in Lean, no `sorry`)

The bar-involution induces a $\mathbb{Z}/2\mathbb{Z}$-grading on
the underlying ring. The bar-symmetric subspace is a **subring**;
the bar-anti-symmetric subspace is an $R^+$-module that satisfies
the natural sign rules:

See [Table 5](#tbl:bar-involution-table5-data).

These are **fully proved** from the four ring-involution axioms
alone — no `sorry`, no auxiliary `Field` instance needed (only
`CommRing`). They formalize previously narrative-only claims:

- *"$h^2$ is bar-symmetric because $h$ is bar-anti-symmetric"* —
 now `IsBarSymmetric.of_mul_antisym hx hx` for any
 `hx : IsBarAntiSymmetric h`.
- *"$\cosh(h) = (e^h + e^{-h})/2$ is even, hence bar-symmetric"* —
 the formal-series structure that makes $\cosh$, $\cos$,
 $\mathrm{Li}_2^q$ bar-symmetric reduces to repeated applications
 of `pow_two_mul` and `add`.
- *"The framework retains only the even part"* — the
 bar-symmetric subspace is closed under the ring operations, so
 applying $P_{\mathrm{avg}}$ to any sequence of operations
 on bar-symmetric inputs lands in the bar-symmetric subspace
 again.

### Falsifiability: silver vs golden $c_5$ outlier

`computations/probes/qbeta_golden_ratio_fibonacci_probe.py`
computes $c_k(q)$ for $k = 3..10$ at golden ratio $q = \varphi$
($b^2 = 4/5$ exact) and tests Fibonacci-Lucas-cleanness vs the
silver-ratio Pell-Lucas test. Result (witness confirmed):

See [Table 6](#tbl:bar-involution-table6-data).

**Silver outliers: $\{5\}$. Golden outliers: $\emptyset$.**

This **confirms the hypothesis** that the $c_5$ outlier is
silver-specific — the inert-prime fingerprint of the β-decay null
($h=2$ at silver, no analog at golden $h=1$). The outlier IS the
forced collapse into the bar-invariant fixed-point sector at the
unique null point in the proton/neutron kinematic window.

## Geometric reading

The bar-involution corresponds at three different geometric levels:

See [Table 7](#tbl:bar-involution-table7-data).

The bar-symmetric projection at each level is the **orientation-
averaged** quantity: averaged crossings (knot), unsigned winding
(color tubes), symmetrized Wilson loop (ED), $\alpha \wedge d\alpha$
(contact volume).

## Kac–Sunada meta-justification

Kac (1966) / Sunada (1985): distinct manifolds can be isospectral
(share Laplace-Dirichlet spectrum). The Hecke analog: distinct
braids share $\tau_M(\beta)$ at fixed $q$ (Hecke-trace isospectral
pairs). But demanding agreement at BOTH $q$ AND $q^{-1}$ —
bar-symmetric matching — **is much tighter**.

The Faddeev $\Phi_q$ channel hears only one orientation;
symmetric Li_2^q hears the bar-symmetrized spectrum. So
**bar-symmetric is FORCED** — the projection isn't a stylistic
choice but the isospectral lift demanded by Kac–Sunada non-
uniqueness applied to Hecke-trace-determined braids.

## Cross-references

This definition is the canonical reference for bar-symmetry. Other
blocks that consume it (with their primary bar-classification):

- `thm:averaging-resonance-rule` — $\sigma_{\mathrm{avg}}$ bar-symmetric; level-selection rule at half-fill rung.
- [`prop:c5-involution-leibniz-decomposition`](#prop:c5-involution-leibniz-decomposition) — $c_5$ bar-symmetric closed form; Hoefsmit-Quantum-2 identity proved here.
- [`prop:silver-ratio-beta-decay-null`](#prop:silver-ratio-beta-decay-null) — $\Delta(\text{net}) = h(h-2)/2$ bar-anti-symmetric in $h$; $h = 2$ root at silver.
- `prop:bar-symmetric-three-layer-synthesis` — series / phase / gain layers, all bar-symmetric projections (conjecturally of one universal kernel).
- [`def:categorical-q-reeb-flow`](#def:categorical-q-reeb-flow) — Reeb field $R$ bar-anti-symmetric.
- [`prop:chirality-residue-mass-term`](#prop:chirality-residue-mass-term) — chirality residue bar-anti-symmetric.

## Notation summary

See [Table 8](#tbl:bar-involution-table8-data).

## Proofs (Lean $\leftrightarrow$ paper bridge)

Every Lean theorem in [`bar-involution.lean`](bar-involution.lean) has both a narrative proof here and a `sorry`-free formal proof. Theorems split into three sections by structural prerequisite (`CommRing` / `Field`).

### Bar-grading over `CommRing R`

**Proposition (Lean: `decompose x`).** $x = P_{\mathrm{avg}}(x) + P_{\mathrm{skew}}(x)$.
*Proof.* $\frac{x + \overline x}{2} + \frac{x - \overline x}{2} = \frac{2x}{2} = x$. $\square$

**Proposition (Lean: `isBarSymmetric_zero`, `isBarSymmetric_one`).** $0$ and $1$ are bar-symmetric.
*Proof.* Direct from `BarInvolution.bar_zero` and `bar_one`. $\square$

**Proposition (Lean: `IsBarSymmetric.add`).** Sum of bar-symmetric is bar-symmetric.
*Proof.* $\overline{x+y} = \overline x + \overline y = x + y$. $\square$

**Proposition (Lean: `IsBarSymmetric.mul`).** Product of bar-symmetric is bar-symmetric.
*Proof.* $\overline{x \cdot y} = \overline x \cdot \overline y = x \cdot y$. $\square$

**Proposition (Lean: `IsBarAntiSymmetric.add`).** Sum of bar-anti-symmetric is bar-anti-symmetric.
*Proof.* $\overline{x+y} = \overline x + \overline y = -x + (-y) = -(x+y)$. $\square$

**Theorem (Lean: `IsBarSymmetric.of_mul_antisym`).** $x, y$ bar-anti-symmetric $\Rightarrow$ $x \cdot y$ bar-symmetric.
*Proof.* $\overline{x \cdot y} = \overline x \cdot \overline y = (-x)(-y) = x \cdot y$. **This is the "anti $\times$ anti = sym" identity that generates the bar-symmetric content from bar-anti-symmetric kernels** (e.g., $h^2$ bar-sym from $h$ bar-anti-sym). $\square$

**Theorem (Lean: `IsBarAntiSymmetric.of_sym_mul`).** $x$ bar-symmetric, $y$ bar-anti-symmetric $\Rightarrow$ $x \cdot y$ bar-anti-symmetric.
*Proof.* $\overline{x \cdot y} = \overline x \cdot \overline y = x \cdot (-y) = -(x \cdot y)$. $\square$

**Proposition (Lean: `bar_neg x`).** $\overline{-x} = -\overline x$ — bar commutes with negation.
*Proof.* From $x + (-x) = 0$ and bar additive: $\overline x + \overline{-x} = \overline 0 = 0$, hence $\overline{-x} = -\overline x$. $\square$

**Proposition (Lean: `IsBarSymmetric.neg`, `IsBarAntiSymmetric.neg`).** Negation preserves both grading sectors.
*Proof.* For sym: $\overline{-x} = -\overline x = -x$. For anti-sym: $\overline{-x} = -\overline x = -(-x) = x = -(-x)$. $\square$

**Theorem (Lean: `IsBarAntiSymmetric.pow_two_mul`).** $x$ bar-anti-sym $\Rightarrow$ $x^{2n}$ bar-symmetric.
*Proof.* Induction on $n$. Base ($n=0$): $x^0 = 1$ bar-symmetric. Step: $x^{2(k+1)} = x^{2k} \cdot (x \cdot x)$; $x^{2k}$ bar-sym by IH, $x \cdot x$ bar-sym by `of_mul_antisym`; product bar-sym by `IsBarSymmetric.mul`. $\square$

**Theorem (Lean: `IsBarAntiSymmetric.pow_two_mul_add_one`).** $x$ bar-anti-sym $\Rightarrow$ $x^{2n+1}$ bar-anti-symmetric.
*Proof.* $x^{2n+1} = x^{2n} \cdot x$; $x^{2n}$ bar-sym (above), $x$ bar-anti-sym (hypothesis); product bar-anti-sym by `of_sym_mul`. $\square$

### Bar on integer scalars

**Proposition (Lean: `bar_two`).** $\overline 2 = 2$.
*Proof.* $\overline 2 = \overline{1 + 1} = \overline 1 + \overline 1 = 1 + 1 = 2$. $\square$

**Proposition (Lean: `bar_natCast n`).** $\overline n = n$ for every $n \in \mathbb{N}$.
*Proof.* Induction on $n$. Base: $\overline 0 = 0$. Step: $\overline{k+1} = \overline k + \overline 1 = k + 1$. $\square$

**Proposition (Lean: `isBarSymmetric_natCast n`).** Every natural-number scalar is bar-symmetric.
*Proof.* Restatement of `bar_natCast n` in the `IsBarSymmetric` predicate. $\square$

### Projection theorems (require `Field R`)

**Proposition (Lean: `bar_inv x`).** $\overline{x^{-1}} = (\overline x)^{-1}$ over a field.
*Proof.* If $x = 0$: both sides are $0$ (from $\overline 0 = 0$ + $0^{-1} = 0$ convention). If $x \neq 0$: $\overline x \neq 0$ (bar is injective by involutivity), and $\overline x \cdot \overline{x^{-1}} = \overline{x \cdot x^{-1}} = \overline 1 = 1$, hence $\overline{x^{-1}} = (\overline x)^{-1}$. $\square$

**Proposition (Lean: `bar_half`).** $\overline{1/2} = 1/2$ over a field.
*Proof.* $\overline{1/2} = \overline{1 \cdot 2^{-1}} = \overline 1 \cdot (\overline 2)^{-1} = 1 \cdot 2^{-1} = 1/2$ via `bar_inv` and `bar_two`. $\square$

**Proposition (Lean: `isBarSymmetric_intCast n`).** Every integer scalar is bar-symmetric.
*Proof.* For $n = \mathrm{ofNat}\, k$: use `bar_natCast`. For $n = \mathrm{negSucc}\, k = -(k+1)$: $\overline{-(k+1)} = -\overline{k+1} = -(k+1)$ via `bar_neg` + `bar_natCast`. $\square$

**Proposition (Lean: `barSymmetricProjection_of_sym x`).** If $x$ is bar-symmetric, $P_{\mathrm{avg}}(x) = x$.
*Proof.* $P_{\mathrm{avg}}(x) = (x + \overline x)/2 = (x + x)/2 = x$. $\square$

**Proposition (Lean: `barSymmetricProjection_of_antisym x`).** If $x$ is bar-anti-symmetric, $P_{\mathrm{avg}}(x) = 0$.
*Proof.* $P_{\mathrm{avg}}(x) = (x + \overline x)/2 = (x - x)/2 = 0$. $\square$

**Proposition (Lean: `barSkewProjection_of_antisym x`).** If $x$ is bar-anti-symmetric, $P_{\mathrm{skew}}(x) = x$.
*Proof.* $P_{\mathrm{skew}}(x) = (x - \overline x)/2 = (x - (-x))/2 = x$. $\square$

**Proposition (Lean: `barSkewProjection_of_sym x`).** If $x$ is bar-symmetric, $P_{\mathrm{skew}}(x) = 0$.
*Proof.* $P_{\mathrm{skew}}(x) = (x - \overline x)/2 = (x - x)/2 = 0$. $\square$

**Theorem (Lean: `barSymmetricProjection_pow_even_of_antisym x n`).** For bar-anti-sym $x$: $P_{\mathrm{avg}}(x^{2n}) = x^{2n}$.
*Proof.* $x^{2n}$ is bar-symmetric by `pow_two_mul`; apply `of_sym`. $\square$

**Theorem (Lean: `barSymmetricProjection_pow_odd_of_antisym x n`).** For bar-anti-sym $x$: $P_{\mathrm{avg}}(x^{2n+1}) = 0$.
*Proof.* $x^{2n+1}$ is bar-anti-sym by `pow_two_mul_add_one`; apply `of_antisym`. **This is "the framework projects away odd-power components" at the formal level.** $\square$

**Theorem (Lean: `barSymmetricProjection_isBarSymmetric x`).** $P_{\mathrm{avg}}(x)$ is bar-symmetric for every $x$.
*Proof.* $\overline{P_{\mathrm{avg}}(x)} = \overline{(x + \overline x)/2} = \overline{x + \overline x} \cdot \overline{1/2} = (\overline x + x) \cdot (1/2) = P_{\mathrm{avg}}(x)$ via `bar_half`. $\square$

**Theorem (Lean: `barSymmetricProjection_idempotent x`).** $P_{\mathrm{avg}}^2 = P_{\mathrm{avg}}$.
*Proof.* $P_{\mathrm{avg}}(x)$ is bar-symmetric by the previous theorem; applying $P_{\mathrm{avg}}$ to a bar-symmetric input gives the input back by `of_sym`. $\square$

**Theorem (Lean: `barSkewProjection_isBarAntiSymmetric x`).** $P_{\mathrm{skew}}(x)$ is bar-anti-symmetric.
*Proof.* $\overline{P_{\mathrm{skew}}(x)} = \overline{(x - \overline x)/2} = (\overline x - x) \cdot (1/2) = -P_{\mathrm{skew}}(x)$. $\square$

**Theorem (Lean: `barSkewProjection_idempotent x`).** $P_{\mathrm{skew}}^2 = P_{\mathrm{skew}}$.
*Proof.* Analogous to $P_{\mathrm{avg}}$ idempotency via `barSkewProjection_of_antisym`. $\square$

All 33 theorems / definitions in [`bar-involution.lean`](bar-involution.lean) have narrative proofs here and `sorry`-free Lean proofs.
