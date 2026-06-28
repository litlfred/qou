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

## Formalization

The bar-grading algebra is formalised in [`prop:bar-grading-algebra`](bar-grading-algebra.md) (sorry-free in Lean).
