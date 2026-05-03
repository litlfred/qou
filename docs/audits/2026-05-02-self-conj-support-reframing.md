# Reframing "supported on self-conjugate λ" — operator vs Plancherel-sum

**Status:** structural reframing for 5 blocks that use the phrase
"supported on self-conjugate λ".

## The two interpretations

The phrase appears in:

1. [`conj:categorical-neutrality-saturated-shells`](../../content/quantum-observable-universe/braids-and-knots/categorical-neutrality-saturated-shells.md):
   *"$\Phi_n$ is supported on self-conjugate partitions"* at saturated $n$.
2. [`rem:single-magic-O18-diagram`](../../content/quantum-observable-universe/observations/single-magic-O18-diagram.md):
   *"Wedderburn support is spread"* (counter-example block).
3. [`conj:diagrammatic-double-magic-lr-fusion`](../../content/quantum-observable-universe/observations/diagrammatic-double-magic-lr-fusion.md):
   *"force self-conjugate support of $\Phi_Z$ and $\Phi_N$"*.
4. [`prop:magic-numbers-bring`](../../content/quantum-observable-universe/algebraic-substrate/magic-numbers-bring.md):
   passing reference.
5. [`conj:homological-shell-condensation`](../../content/quantum-observable-universe/lifting-and-descent/homological-shell-condensation.md):
   *"forces the Wedderburn support of $\Phi_n$ onto self-conjugate
   partitions"*.

The phrase has **two distinct mathematical meanings**:

### Meaning A — operator-level support (the correct reading)

$$
\Phi_n \in \bigoplus_{\lambda = \lambda'} \mathrm{End}(V_\lambda) \subset \bigoplus_{\lambda \vdash n} \mathrm{End}(V_\lambda) = H_n(R, q)
$$

The operator $\Phi_n$ has zero component on every NON-self-conjugate
isotypical block. It's still a **non-trivial operator** on the
self-conjugate isotypical blocks, with arbitrary matrix entries
there.

### Meaning B — Plancherel-weighted character sum (the WRONG reading)

$$
\mathrm{tr}(\Phi_n) = \sum_{\lambda = \lambda'} w_\lambda \cdot \chi^\lambda(\text{some braid permutation})
$$

This is the sum I and earlier probes computed. We empirically
showed (commit `5bf642b20`,
[2026-05-02-w-lambda-level1-bb-result.md](2026-05-02-w-lambda-level1-bb-result.md))
that this sum vanishes at $D, ^4\!\mathrm{He}, ^6\!\mathrm{Li}, ^{16}\!\mathrm{O}$
INDEPENDENTLY of the Plancherel weight choice $w_\lambda$ — a
character-sum vanishing identity:

$$
\sum_{\lambda = \lambda',\, \lambda \vdash 3A} \chi^\lambda(W_\text{atom}) = 0 \;\text{at certain } (Z, N).
$$

## Why this distinction matters

**Meaning A is consistent**: the operator $\Phi_n$ being supported
on self-conjugate isotypical blocks is a well-defined non-trivial
constraint that selects which Wedderburn blocks contribute.

**Meaning B is empirically empty at magic atoms**: weighted
character sums vanish, so any "magic-shell binding contribution"
formulated as such a sum is literally zero — useless for
extracting binding energies.

The empirical Term6/A³ + magic-residual probes
(commit `46bc03fa6`, +0.74 corr with `is_magic_pair`) show that
the actual binding enhancement at magic atoms IS REAL — it's
just NOT a partition-summed quantity. The conjecture's "support"
notion must be operator-level (Meaning A) for binding-energy
predictions to follow from saturation.

## Recommended block updates

Each of the 5 blocks should add a **clarifying note** distinguishing
Meaning A from Meaning B, with a link to this memo.

Suggested wording:

> **Note (operator vs sum interpretation).** "Supported on
> self-conjugate partitions" here means **operator-level**: the
> categorical mass operator $\Phi_n$ has zero matrix entries on
> non-self-conjugate isotypical components. It does **not** mean
> the Plancherel-weighted character sum
> $\sum_{\lambda = \lambda'} w_\lambda \chi^\lambda(\beta)$ — that
> sum vanishes identically at certain atomic-braid cycle types
> (representation-theoretic identity; see
> [self-conj support reframing memo](../../../docs/audits/2026-05-02-self-conj-support-reframing.md)).
> The binding-energy enhancement at magic shells is the
> operator-level non-vanishing of $\Phi_n$ on self-conjugate
> isotypical blocks, NOT the partition sum.

## What's downstream

The conjecture `conj:homological-shell-condensation` already
phrases its content in BB-spectral-sequence terms ($E_\infty^{p, >0}(n) = 0$),
which IS operator-level (page collapse on associated graded).
This block's reading is consistent with Meaning A.

The other four blocks should be tightened so they don't
inadvertently suggest Meaning B.

## Status

This memo is the canonical clarification. The 5 blocks should
reference it where they use the phrase. No proof content
changes; only narrative tightening of an ambiguity.
