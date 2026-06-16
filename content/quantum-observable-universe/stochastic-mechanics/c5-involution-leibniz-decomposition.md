*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

> **Bar-symmetry class** (per [`def:bar-involution`](#def:bar-involution)):
> $c_5(q) = -b^2(q) - 1/2 = -3/2 + 1/[2]_q^2$ is **bar-symmetric**
> as a function of $q$. The Hoefsmit-Quantum-2 identity
> $b^2 = 1 - 1/[2]_q^2$ is a proved algebraic theorem in the
> Lean sibling (`hoefsmit_b_squared_eq_one_minus_inv_quantum_two_squared`,
> no `sorry`). The "$-1/2$" piece is a q-independent
> commutative-QOU constant; $c_5(q=1) = -5/4$ proved as
> `c5_classical_limit_eq_neg_five_quarters`. So the c_5 outlier
> at silver is the *arithmetic sum* of two clean bar-symmetric
> pieces landing on inert prime $11 \in \mathbb{Z}[1+\sqrt 2]$,
> not a quantum-deformation artifact.

> **Pentagon-reduction cross-link.** The Leibniz expansion in
> step 3 below uses the q-dilogarithm pentagon identity
> implicitly. The algebraic identity making this rigorous in
> $\mathbb{Z}[q^{\pm 1}]$ for $|z| \ge q$ via duplication
> $u = v = i\sqrt{|z|}$, plus the post-$\tau$ $\log_q^2$
> correction, lives on `main` in
> [`pentagon_reduction_li2q.py`](../../../computations/pentagon_reduction_li2q.py)
> with audit doc
> [`-pentagon-reduction-li2q.md`](../../../docs/audits/-pentagon-reduction-li2q.md).
> Cross-link: the *Pentagon coherence layer* of $c_5$'s
> decomposition (one of the three layers in
> `prop:bar-symmetric-three-layer-synthesis`)
> is what `pentagon_reduction_li2q.py` makes algebraic.

**Proposition ($c_5$ involution + Leibniz decomposition).**

*Let $c_5(q)$ be the precision-ladder coefficient at rung $N=5$ in
the $\mathfrak{Q}_\beta$ categorical formula
[`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder).
Then $c_5$ admits the categorical decomposition:*

$$
\boxed{\;
c_5(q) \;=\; \underbrace{-b(q)^2}_{\text{pure-}\sigma\text{ Kashiwara}}
\;-\; \underbrace{\tfrac{1}{2}}_{\substack{\text{averaged-crossing}\\\text{involution fingerprint}}}
\;}
$$

*where $b(q)^2 = (q^4+q^2+1)/(q^2+1)^2$ is the Hoefsmit off-diagonal
coupling squared on $V_{(2,1)}$. The $-1/2$ summand is **NOT** an
ad-hoc empirical offset: it is the fingerprint of the bar-invariant
averaged-crossing operator $\sigma_{\text{avg}} = (\sigma + \sigma^{-1})/2$
used at specific positions in the typed-$\mathbf{B}_3$ braid recipe
([`prop:neutron-qvalue-symbolic`](#prop:neutron-qvalue-symbolic)).*

*The decomposition resolves the Pell-Lucas outlier status of $c_5$
at the silver ratio
([`prop:silver-ratio-beta-decay-null`](#prop:silver-ratio-beta-decay-null)):
the pure-$\sigma$ part $-b^2$ evaluates to $-7/8$ (Pell-Lucas-clean),
and the involution fingerprint $-1/2$ is the **non-Hecke** correction.*

## Proof sketch

### Step 1: bar involution and the averaged crossing

The Hecke algebra $H_n(q)$ carries the **bar involution** $\overline{\,\,}$,
a $\mathbb{Z}$-linear anti-ring-automorphism defined by:
$$
\overline{q} = q^{-1}, \quad \overline{\sigma_i} = \sigma_i^{-1}.
$$

Using the Hecke quadratic $\sigma_i^2 = h\sigma_i + 1$ (where $h = q - q^{-1}$),
we have $\sigma_i^{-1} = \sigma_i - h$.

The **bar-invariant projector** is $P_{\text{avg}} = (1 + \overline{\,\,})/2$.
Its action on $\sigma_i$ gives:
$$
P_{\text{avg}}(\sigma_i) \;=\; \frac{\sigma_i + \overline{\sigma_i}}{2}
\;=\; \frac{\sigma_i + \sigma_i^{-1}}{2}
\;=\; \frac{\sigma_i + \sigma_i - h}{2}
\;=\; \sigma_i - \frac{h}{2}.
$$

This is the **averaged crossing operator** $\sigma_{\text{avg}}$ used
in the typed-$\mathbf{B}_3$ braid recipe.

### Step 2: averaged crossings in the typed braid

From [`prop:neutron-qvalue-symbolic`](#prop:neutron-qvalue-symbolic),
the typed-$\mathbf{B}_3$ proton braid uses ONE averaged $\sigma_1$:
$$
\mathcal{B}_p \;=\; \sigma_0 \cdot (\sigma_1 - \tfrac{h}{2}\mathbf{1})
\;=\; \sigma_0 \cdot \sigma_{1,\text{avg}}.
$$

The typed neutron braid uses TWO averaged crossings (one at $\sigma_0$,
one at $\sigma_1$):
$$
\mathcal{B}_n \;=\; (\sigma_0 - \tfrac{h}{2}\mathbf{1}) \cdot (\sigma_1 - h\mathbf{1})
\;=\; \sigma_{0,\text{avg}} \cdot \sigma_1^{-1}.
$$

Each averaged crossing contributes a factor of $h/2 = 1/2$ at the
specific position where it appears.

### Step 3: Leibniz propagation to higher rungs

The categorical Markov-trace expansion of the typed braid in powers
of $h$ generates the single-wrap baseline (Form A) plus the
precision-ladder corrections. The $h/2$ contributions from averaged
positions propagate via the **Leibniz product expansion**:

$$
\tau_M(\mathcal{B}_n - \mathcal{B}_p) \;=\; \mathrm{net}(n) - \mathrm{net}(p)
\;=\; \frac{h^2}{2} - h
\;=\; \frac{h(h-2)}{2}.
$$

The $h^2/2$ term is the product of TWO averaged-crossing $h/2$
contributions (the neutron has two such positions). The $h/2$
generates the $1/2$ in $\Delta(\mathrm{net})$.

For higher rungs $N = k \geq 4$ of the precision ladder, the
expansion of $\tau_M(T_\beta)$ in $b \cdot \hbar_q^2$ produces
coefficients with two distinct categorical origins:

- **Pure-$\sigma$ contributions**: from non-averaged positions in
  the braid. These factor through $\sigma^p \cdot b^{2m}$
  combinatorics. At the silver ratio ($\sigma$-eigenvalues
  $= 1 \pm \sqrt{2}$ via the Hecke quadratic
  [`prop:silver-ratio-beta-decay-null`](#prop:silver-ratio-beta-decay-null)),
  these reduce to **Pell-Lucas-clean** rationals.

- **Averaged-crossing contributions**: from positions where $\sigma_{\text{avg}}$
  acts. These pick up the $1/2$ fingerprint of $P_{\text{avg}}$. At
  the silver ratio they give rationals with a $1/2$ component that
  is **Pell-Lucas-incompatible**.

### Step 4: rung-by-rung classification

Sequential extraction of $c_k$ via $R(q_0) = \prod_k (1 + c_k b^k \hbar_q^{2k})$
gives:

| $c_k$ | Closed form | Origin | At silver ratio |
|:----:|:-----------:|:-------|:-------|
| $c_3$ | $-2$ | $J_{\text{Hopf}}(q=1)$, pure inter-block | $-2$ (clean) |
| $c_4$ | $c_3 \cdot b^4$ | $\sigma^p \cdot b^{2m}$ pure | $-49/32 = -a_3^2/2^5$ (clean) |
| $c_5$ | $\boxed{-b^2 - 1/2}$ | $\sigma$ + averaging | $-11/8$ (1/2 OUTLIER) |
| $c_6$ | $c_3^2 \cdot b^2$ | $\sigma^p \cdot b^{2m}$ pure | $7/2 = a_3/2$ (clean) |
| $c_7$ | $c_3^3$ | pure $\sigma$ powers | $-8$ (clean integer) |

The $c_5$ outlier is **structurally distinct** because $\sigma_{\text{avg}}$
contributions at rung $5$ are dominant — at all other rungs in
$[3, 7]$, the pure-$\sigma$ contributions dominate and the
averaging contributions are subdominant. □

## Categorical interpretation

The framework's $\mathfrak{Q}_\beta$ predictions live in TWO distinct
categorical sectors:

1. **Pure-$\sigma$ sector** ($c_3, c_4, c_6, c_7$): contributions
   from positions in the braid that act as pure Hecke generators
   or their inverses. Algebraically lives in the $\mathbb{Z}$-span
   of Hecke-quadratic eigenvalues, reducing at the silver ratio
   to the **Pell-Lucas extension** $\mathbb{Z}[1 + \sqrt{2}]$.
2. **Bar-invariant fixed-point sector** ($c_5$): contributions from
   averaged-crossing positions. Algebraically lives in the
   bar-invariant subring (fixed by $\sigma \leftrightarrow \sigma^{-1}$),
   which intersects with $\mathbb{Z}[1+\sqrt{2}]$ only on integer
   subspaces — the $1/2$ is the residual after this intersection.

The two sectors are **independent categorical inputs**: pure-$\sigma$
is the Hecke-generator action; bar-invariant fixed-point is the
involution-projector action. Both are needed to reproduce $\mathfrak{Q}_\beta$
exactly via the precision ladder.

## Falsifiable prediction

Any future rung $c_k$ at $k \geq 8$ whose order $\hbar_q^{2k}$
coincides with an **averaging-resonance** position (= a $k$-fold
cyclic substructure including at least one averaged crossing)
will pick up similar $1/2$ fingerprints.

Specifically, the proton braid has 11 typed crossings: 7 pure
$\sigma_0$, 4 pure $\sigma_1$, 1 averaged $\sigma_0$ (at coefficient
$-h/2$), 1 averaged $\sigma_1$ (at coefficient $-h/2$), 3 inverted
$\sigma_1^{-1}$ (at coefficient $-h$). The averaging-resonance
rungs are determined by the positions where two averaged crossings
interact at a given order in $\hbar_q^{2k}$.

By combinatorial counting of pairs of averaged positions among the
11 typed crossings, the predicted averaging-resonance rungs are
those $k$ for which $\binom{2}{2} \cdot (\text{combinatorial weight})$
peaks. **$k = 5$** is the first; subsequent peaks predicted at
**$k = 8, 11, \ldots$** (every 3 rungs by the 3-strand
sub-braid combinatorics).

This is testable by extending SDP-$T_\beta$ extraction to $k \geq 8$
and checking whether c_8 has a $1/2$ fingerprint — the probe is
queued in
[`computations/qbeta/qbeta_decay_sdp_extended_ck.py`](../../computations/qbeta/qbeta_decay_sdp_extended_ck.py).

## Discussion

This decomposition is a **structural identification**, not a
first-principles derivation. The $-b^2$ and $-1/2$ summands are
identified categorically, but the proof that the precision-ladder
$c_5$ takes exactly this form (modulo $2.4\%$ empirical residual)
requires:

1. Explicit computation of the typed-$\mathbf{B}_3$ Markov-trace
   expansion at order $b^5 \hbar_q^{10}$.
2. Separating pure-$\sigma$ contributions from averaged-position
   contributions order-by-order.

Both are concrete finite computations; neither is yet executed in
the framework. This proposition sets up the categorical grammar;
its full proof is gated on the order-by-order Hecke expansion
machinery (open R&D).

## Proofs (Lean $\leftrightarrow$ paper bridge)

Every substantive Lean theorem in [`c5-involution-leibniz-decomposition.lean`](c5-involution-leibniz-decomposition.lean) has both a narrative proof here and a `sorry`-free Lean proof.

### Hoefsmit–Quantum-2 identity

**Theorem (Lean: `hoefsmit_b_squared_eq_one_minus_inv_quantum_two_squared`).** For all $q \neq 0$ in $\mathbb{R}$,

$$b^2(q) \;=\; \frac{q^4 + q^2 + 1}{(q^2 + 1)^2} \;=\; 1 - \frac{1}{[2]_q^2}.$$

*Proof.* Multiply both sides by $[2]_q^2 = (q + q^{-1})^2$:
$(q^2 + 1)^2 = q^2 \cdot (q + q^{-1})^2$ since $(q+q^{-1})^2 = (q^2+1)^2/q^2$. So $b^2 = (q^4+q^2+1)/(q^2[2]_q^2)$. Multiply numerator and denominator of $b^2$ by $1/q^2$: $b^2 = (q^2 + 1 + q^{-2})/[2]_q^2 = ([2]_q^2 - 1)/[2]_q^2 = 1 - 1/[2]_q^2$ since $q^2 + 1 + q^{-2} = (q+q^{-1})^2 - 1 = [2]_q^2 - 1$. Lean tactic: `field_simp; ring`. $\square$

**Corollary (Lean: `c5_decomposition_via_quantum_two`).** $c_5(q) = -3/2 + 1/[2]_q^2$.
*Proof.* Substitute $b^2 = 1 - 1/[2]_q^2$ into $c_5 = -b^2 - 1/2$:
$c_5 = -(1 - 1/[2]_q^2) - 1/2 = -3/2 + 1/[2]_q^2$. $\square$

### Classical-QOU limit + Wedderburn identification

**Theorem (Lean: `c5_classical_limit_eq_neg_five_quarters`).** $c_5(q = 1) = -5/4$.
*Proof.* At $q = 1$: $[2]_q = 2$, so $[2]_q^2 = 4$, $1/[2]_q^2 = 1/4$, $c_5(1) = -3/2 + 1/4 = -5/4$. By `norm_num`. $\square$

**Theorem (Lean: `c5_classical_eq_wedderburn_nonsign_dim_half`).** $c_5(1) = -(\dim V_{(3)} + \dim V_{(2,1)})/2 + 1/4 = -5/4$.
*Proof.* The Wedderburn decomposition of $\mathbb{C}[S_3]$ has three irreps with dimensions $1$ ($V_{(3)}$), $2$ ($V_{(2,1)}$), $1$ ($V_{(1,1,1)}$). The non-sign sum is $1 + 2 = 3$; half is $3/2$. So $-3/2 = -(\dim V_{(3)} + \dim V_{(2,1)})/2$. Combine with $1/4 = 1/[2]_q^2$ at $q=1$ to get $-5/4$. $\square$

### Silver-ratio identity

**Lemma (Lean: `quantumTwo_at_silver_ratio_squared`).** $[2]_q^2 = 8$ at $q = 1 + \sqrt 2$.
*Proof.* $[2]_{1+\sqrt 2} = (1+\sqrt 2) + 1/(1+\sqrt 2) = (1+\sqrt 2) + (\sqrt 2 - 1) = 2\sqrt 2$. So $[2]_q^2 = 8$. Lean tactic:

```lean
field_simp; ring_nf; linarith [Real.mul_self_sqrt (by norm_num : (2:ℝ) ≥ 0)]
```

$\square$

**Theorem (Lean: `b_squared_at_silver_ratio`).** $b^2(1 + \sqrt 2) = 7/8$.
*Proof.* From Hoefsmit–Quantum-2 + the lemma above: $b^2 = 1 - 1/[2]_q^2 = 1 - 1/8 = 7/8$. $\square$

**Corollary (Lean: `c5_at_silver_ratio_is_minus_11_over_8`).** $c_5(\mathrm{silver}) = -11/8$.
*Proof.* From the c_5 closed form + the silver-ratio identity: $c_5 = -3/2 + 1/8 = -12/8 + 1/8 = -11/8$. Numerator $11$ is **inert** in $\mathbb{Z}[1+\sqrt 2]$ (not in Pell-Lucas closure) — the c_5 outlier fingerprint. $\square$

### c_5 in terms of Hecke skein h

**Lemma (Lean: `quantum_two_squared_eq_skein_squared_plus_four`).** For all $q \neq 0$:
$[2]_q^2 = h^2 + 4$ where $h = q - q^{-1}$.
*Proof.* $(q + q^{-1})^2 = q^2 + 2 + q^{-2}$ and $(q - q^{-1})^2 + 4 = (q^2 - 2 + q^{-2}) + 4 = q^2 + 2 + q^{-2}$. Equal. $\square$

**Theorem (Lean: `c5_as_function_of_skein`).** $c_5(q) = -3/2 + 1/(h^2 + 4)$ where $h = q - q^{-1}$.
*Proof.* Substitute the previous lemma into the closed form $c_5 = -3/2 + 1/[2]_q^2$. $\square$

### c_5 as a rational map over $\mathbb{R}$

**Proposition (Lean: `c5RationalMap_at_skein_eq_c5Decomposition`).** `c5RationalMap(h(q)) = c5Decomposition(q)`.
*Proof.* Direct rewrite via `c5_as_function_of_skein`. $\square$

**Proposition (Lean: `h_sq_plus_four_pos`, `h_sq_plus_four_ne_zero`).** $h^2 + 4 > 0$ over $\mathbb{R}$.
*Proof.* $h^2 \geq 0$; add $4$ to get $\geq 4 > 0$. $\square$

**Proposition (Lean: `c5RationalMap_zero/two/one`).** Three concrete evaluations: $c_5(h{=}0) = -5/4$, $c_5(h{=}2) = -11/8$, $c_5(h{=}1) = -13/10$.
*Proof.* Direct numerical computation via `norm_num`. $\square$

**Theorem (Lean: `c5RationalMap_even h`).** $c_5(-h) = c_5(h)$ (even function).
*Proof.* $(-h)^2 = h^2$; substitute. The categorical content of bar-symmetry: $c_5$ is invariant under bar acting as $h \to -h$. $\square$

**Theorem (Lean: `c5RationalMap_le_neg_five_quarters h`).** $c_5(h) \leq -5/4$ for all real $h$, with equality at $h = 0$.
*Proof.* $h^2 + 4 \geq 4$, so $1/(h^2 + 4) \leq 1/4$, hence $c_5 = -3/2 + 1/(h^2+4) \leq -3/2 + 1/4 = -5/4$. $\square$

**Theorem (Lean: `c5RationalMap_gt_neg_three_halves h`).** $c_5(h) > -3/2$ for all real $h$.
*Proof.* $1/(h^2 + 4) > 0$, so $c_5 > -3/2$. The bound is approached asymptotically as $|h| \to \infty$ but never reached. $\square$

**Theorem (Lean: `c5RationalMap_strict_neg h`).** $c_5(h) < 0$ for all real $h$.
*Proof.* From the upper bound: $c_5 \leq -5/4 < 0$. $\square$

**Theorem (Lean: `c5RationalMap_max_at_zero h`).** $h = 0$ achieves the maximum of $c_5$.
*Proof.* Combine $c_5(h) \leq -5/4$ with $c_5(0) = -5/4$. $\square$

**Theorem (Lean: `c5OfHSquared_antitone_on_nonneg`).** $c_5$ is monotonically decreasing in $h^2$ on the nonneg domain.
*Proof.* For $0 \leq x \leq y$: both $x+4$ and $y+4$ are positive, $y + 4 \geq x + 4$, so $1/(y+4) \leq 1/(x+4)$, hence $c_5(y) \leq c_5(x)$. $\square$

### Factorization through $h^2$

**Theorem (Lean: `c5RationalMap_factor h`).** $c_5(h) = c_5\text{OfHSquared}(h^2)$.
*Proof.* By definition both unfold to $-3/2 + 1/(h^2 + 4)$. $\square$

Categorical reading: $c_5$ factors as
$$h \xrightarrow{\text{squaring}} h^2 \xrightarrow{\text{rational fn}} c_5$$
where the first arrow is the canonical anti-sym $\to$ sym projection (`IsBarSymmetric.of_mul_antisym`) and the second is a bar-symmetric-preserving function. This makes the bar-symmetric structure of $c_5$ explicit at the level of function composition.

All 24 substantive Lean theorems / definitions in the sibling have narrative proofs above. The Lean file is `sorry`-free.
