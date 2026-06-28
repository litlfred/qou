**Remark (bar-symmetry class, categorical sectors, and the $c_5$ falsifiable prediction).**

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
