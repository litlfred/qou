**Definition (bar-involution).**

*The* **bar-involution** *$\overline{(\cdot)} \colon H_n(q) \to H_n(q)$
is the ring anti-involution on the Iwahori–Hecke algebra defined
on generators by*

$$
\overline{\sigma_i} \;=\; \sigma_i^{-1}, \qquad \overline{q} \;=\; q^{-1}.
$$

*Equivalently, on the parameter alone: $q \mapsto q^{-1}$, and on
crossings: positive $L_+ \leftrightarrow$ negative $L_-$ (mirror
reflection of the braid diagram).*

## The two canonical projections

The bar-involution is an involution: $\overline{\overline x} = x$.
Every Hecke-algebra element $x \in H_n(q)$ over a field of
characteristic ≠ 2 decomposes uniquely as

$$x \;=\; P_{\mathrm{avg}}(x) + P_{\mathrm{skew}}(x),$$

where

| Projection | Formula | Image | Idempotent? |
|---|---|---|---|
| $P_{\mathrm{avg}}$ | $\frac{1}{2}(1 + \overline{(\cdot)})$ | **bar-symmetric** ($\overline x = x$) | yes ($P_{\mathrm{avg}}^2 = P_{\mathrm{avg}}$) |
| $P_{\mathrm{skew}}$ | $\frac{1}{2}(1 - \overline{(\cdot)})$ | **bar-anti-symmetric** ($\overline x = -x$) | yes ($P_{\mathrm{skew}}^2 = P_{\mathrm{skew}}$) |

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

| Symbol | Reads | Where it appears |
|---|---|---|
| $q + q^{-1} = [2]_q$ | quantum-2 | Hecke skein / Markov parameter |
| $[n]_q$ (any $n$) | q-integer | Hecke characters everywhere |
| $b^2 = 1 - 1/[2]_q^2$ | Hoefsmit coupling squared | $V_{(2,1)}$ off-diagonal |
| $\sigma_{\mathrm{avg}} = (\sigma + \sigma^{-1})/2 = \sigma - h/2$ | averaged crossing | typed-$\mathbf{B}_n$ recipe |
| $\sigma + \sigma^{-1}$ | symmetric crossing pair | self-conjugate Wedderburn |
| $\mathrm{Li}_2^q(z) = \frac{1}{2}(\log\Phi_q + \log\Phi_{q^{-1}})$ | symmetric q-dilog | T2, T3 binding tower |
| $\cos(\alpha - b\hbar_q^2/2)$ | phase factor at $N{=}1$ | master $Q_\beta$ formula |
| $\cosh(h)$ | hyperbolic-cosine of skein | per-Z gain $\alpha_Z \approx [3]_q^2 \cdot \cosh(h)$ |
| Volume forms $\alpha \wedge d\alpha$ | contact volume | Reeb dynamics |
| Unsigned linking $|\mathrm{lk}|$ | absolute linking | knot multiplicity |
| Markov parameter $z = 1/(q^{1/2}+q^{-1/2})$ | Markov-axiom factor | interface knot $\Delta_I^K = z$ |
| All $c_k(q)$ in the precision ladder | classical rationals in $q$ | $\tau_M$ expansion about $q=1$ |

### Bar-anti-symmetric (bar-odd, $P_{\mathrm{skew}}$ image, discarded)

| Symbol | Reads | Where it appears |
|---|---|---|
| $h = q - q^{-1} = h_{1/2}/z$ | Hecke skein parameter | every Hecke skein relation |
| $h_{1/2} = q^{1/2} - q^{-1/2}$ | half-step Hecke skein | quantum group $\mathrm{SU}_q(2)$ |
| $\sigma - \sigma^{-1}$ | anti-symmetric crossing pair | skein difference |
| $q^n - q^{-n}$ | anti-symmetric q-monomial | $[n]_q$'s anti-sym numerator |
| $\Phi_q(z)$ alone (Faddeev) | Faddeev q-dilog | $-737$ MeV mirror-nucleus pathology if used alone |
| $\sin(\alpha)$ alone | phase odd-component | discarded at $N{=}1$ |
| $\sinh(h)$ | hyperbolic-sine of skein | discarded at per-Z gain |
| Writhe $w(K) = \sum_c \mathrm{sign}(c)$ | signed crossing sum | chirality / orientation |
| Signed linking $\mathrm{lk}(K_1, K_2)$ | signed Hopf-link invariant | knot factor |
| Self-linking $\mathrm{SL}(K)$ | framed self-linking | ribbon structure |
| Reeb field $R$ (vector) | contact flow direction | `def:categorical-q-reeb-flow` |
| Reeb 1-form $\alpha$ | contact 1-form | (orientation 1-form) |
| Curvature 2-form $d\alpha$ | contact curvature | Reeb-bundle |
| Chern–Simons 3-form $\mathrm{CS}(A)$ (mod $\mathbb{Z}$) | CS Lagrangian | topological mass |
| Instanton number $n = \tfrac{1}{8\pi^2}\int \mathrm{tr}(F\wedge F)$ | second Pontryagin | topological charge |
| Hopf invariant | $S^3 \to S^2$ winding | bundle classification |
| Helicity (right- vs left-handed) | chirality direction | parity-violating amplitudes |
| Chirality residue | residue at chirality pole | `prop:chirality-residue-mass-term` |

### Trivial under bar (rational scalars)

| Symbol | Reads | Where it appears |
|---|---|---|
| Any $r \in \mathbb{Q}$ (constant) | rational constant | structure constants like $-1/2$, $-3/2$ |
| Any $r \in \mathbb{Q}(\sqrt 2)$ at silver (computed) | rational at silver | $-11/8$, $-49/32$, $7/2$, ... |

## Key algebraic identities

### Half-step factorization of $h$

$$h \;=\; q - q^{-1} \;=\; \underbrace{(q^{1/2} - q^{-1/2})}_{h_{1/2},\;\text{bar-ANTI-sym}} \;\cdot\; \underbrace{(q^{1/2} + q^{-1/2})}_{1/z,\;\text{bar-SYM (Markov param)}}$$

The bar-anti-symmetry of $h$ comes *entirely* from $h_{1/2}$; the
bar-symmetric Markov parameter $z = 1/(q^{1/2}+q^{-1/2})$ factor
is bar-invariant. This is the same $z$ that the cross-PR Phase 5c.1 cross-check
identified as the interface-knot value $\Delta_I^K = z$ exactly.

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

### Falsifiability: silver vs golden $c_5$ outlier

`folio-assistant/computations/qbeta_golden_ratio_fibonacci_probe.py`
computes $c_k(q)$ for $k = 3..10$ at golden ratio $q = \varphi$
($b^2 = 4/5$ exact) and tests Fibonacci-Lucas-cleanness vs the
silver-ratio Pell-Lucas test. Result (witness confirmed):

| $k$ | Silver | Golden |
|:---:|:---:|:---:|
| 5 | $-11/8$, **inert** (11) | $-13/10$, **clean** ($13 = F_7$) |
| all other $k \in \{3,4,6,7,8,9,10\}$ | clean | clean |

**Silver outliers: $\{5\}$. Golden outliers: $\emptyset$.**

This **confirms the hypothesis** that the $c_5$ outlier is
silver-specific — the inert-prime fingerprint of the β-decay null
($h=2$ at silver, no analog at golden $h=1$). The outlier IS the
forced collapse into the bar-invariant fixed-point sector at the
unique null point in the proton/neutron kinematic window.

## Geometric reading

The bar-involution corresponds at three different geometric levels:

| Level | Bar action |
|---|---|
| **Knot diagram** | Mirror reflection (over- ↔ under-crossing swap) |
| **Color tube** | Orientation reversal of winding around the chromaticity axis |
| **Exceptional divisor (Bring blowup)** | Orientation reversal of ED components |
| **Contact 3-manifold** | $\alpha \to -\alpha$, $R \to -R$ (Reeb flow reversal) |
| **Wilson loop** | $W(\gamma) \to W(\bar\gamma)$ (path reversal) |

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

- [`prop:averaging-resonance-rule`](#prop:averaging-resonance-rule) — $\sigma_{\mathrm{avg}}$ bar-symmetric; level-selection rule at half-fill rung.
- [`prop:c5-involution-leibniz-decomposition`](#prop:c5-involution-leibniz-decomposition) — $c_5$ bar-symmetric closed form; Hoefsmit-Quantum-2 identity proved here.
- [`prop:silver-ratio-beta-decay-null`](#prop:silver-ratio-beta-decay-null) — $\Delta(\text{net}) = h(h-2)/2$ bar-anti-symmetric in $h$; $h = 2$ root at silver.
- [`prop:bar-symmetric-three-layer-synthesis`](#prop:bar-symmetric-three-layer-synthesis) — series / phase / gain layers, all bar-symmetric projections (conjecturally of one universal kernel).
- [`def:categorical-q-reeb-flow`](#def:categorical-q-reeb-flow) — Reeb field $R$ bar-anti-symmetric.
- [`prop:chirality-residue-mass-term`](#prop:chirality-residue-mass-term) — chirality residue bar-anti-symmetric.

## Notation summary

| Notation | Meaning |
|---|---|
| $\overline{x}$ | bar-involution of $x$ |
| $P_{\mathrm{avg}}(x) = (x + \overline x)/2$ | bar-symmetric projection of $x$ |
| $P_{\mathrm{skew}}(x) = (x - \overline x)/2$ | bar-anti-symmetric projection of $x$ |
| $\sigma_{\mathrm{avg}} = P_{\mathrm{avg}}(\sigma) = \sigma - h/2$ | averaged crossing operator |
| `IsBarSymmetric x` | Lean predicate $\overline x = x$ |
| `IsBarAntiSymmetric x` | Lean predicate $\overline x = -x$ |
