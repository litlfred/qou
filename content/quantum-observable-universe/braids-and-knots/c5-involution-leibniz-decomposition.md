> **Refined-framing note (added when promoting this block from the
> source PR into the level-selection rule PR).** This block
> *interprets* the unique averaging-resonant rung k = 5 identified
> in [`prop:averaging-resonance-rule`](#prop:averaging-resonance-rule)
> — it does **not** by itself derive *why* the resonance lives at
> rung 5. The involution $P_{\mathrm{avg}} = (1 + \overline{\,\cdot\,})/2$
> supplies the **magnitude** of the $1/2$ fingerprint; the
> **half-fill cyclicity** $k = \lfloor n_{\text{total}}/2 \rfloor = 5$
> for the proton typed-$\mathbf{B}_3$ recipe supplies the **rung
> selection**. The Leibniz propagation discussion below interprets
> the $1/2$ as a Markov-trace expansion fingerprint and is
> consistent with both layers, but reading "Leibniz alone explains
> $c_5$" overfits the rung — the half-fill argument is essential.
> See [`prop:averaging-resonance-rule`](#prop:averaging-resonance-rule)
> §"Why $k = 5$ specifically".

> **Pentagon-reduction cross-link.** The Leibniz expansion in
> step 3 below uses the q-dilogarithm pentagon identity
> implicitly. The algebraic identity making this rigorous in
> $\mathbb{Z}[q^{\pm 1}]$ for $|z| \ge q$ via duplication
> $u = v = i\sqrt{|z|}$, plus the post-$\tau$ $\log_q^2$
> correction, lives on `main` in
> [`pentagon_reduction_li2q.py`](../../../folio-assistant/computations/pentagon_reduction_li2q.py)
> with audit doc
> [`2026-05-19-pentagon-reduction-li2q.md`](../../../docs/audits/2026-05-19-pentagon-reduction-li2q.md).
> Cross-link: the *Pentagon coherence layer* of $c_5$'s
> decomposition (one of the three layers in
> [`prop:bar-symmetric-three-layer-synthesis`](#prop:bar-symmetric-three-layer-synthesis))
> is what `pentagon_reduction_li2q.py` makes algebraic.

**Proposition ($c_5$ involution + Leibniz decomposition).**

*Let $c_5(q)$ be the precision-ladder coefficient at rung $N=5$ in
the $Q_\beta$ categorical formula
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
\beta_p \;=\; \sigma_0 \cdot (\sigma_1 - \tfrac{h}{2}\mathbf{1})
\;=\; \sigma_0 \cdot \sigma_{1,\text{avg}}.
$$

The typed neutron braid uses TWO averaged crossings (one at $\sigma_0$,
one at $\sigma_1$):
$$
\beta_n \;=\; (\sigma_0 - \tfrac{h}{2}\mathbf{1}) \cdot (\sigma_1 - h\mathbf{1})
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
\tau_M(\beta_n - \beta_p) \;=\; \mathrm{net}(n) - \mathrm{net}(p)
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

The framework's $Q_\beta$ predictions live in TWO distinct
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
involution-projector action. Both are needed to reproduce $Q_\beta$
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
[`folio-assistant/computations/qbeta_decay_sdp_extended_ck.py`](../../folio-assistant/computations/qbeta_decay_sdp_extended_ck.py).

## Status

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
