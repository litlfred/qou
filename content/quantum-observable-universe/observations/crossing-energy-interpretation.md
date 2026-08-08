The [decomposition](#prop:crossing-energy-decomposition) separates crossing energy into two channels.

**Channel identification.**

| Channel | Weight per crossing | Under crossing reversal | Channel total |
|---------|-------------------|-----------------|----------------|
| Symmetric | $\pm\cosh(\ln q)$, signed by the crossing | negates | $(p - m)\cosh(\ln q)$ |
| Antisymmetric | $+\sinh(\ln q)$, independent of the crossing sign | fixed | $(p + m)\sinh(\ln q)$ |

The two channels are told apart by how each responds to reversing a crossing, and that is what fixes their multiplicities ([decomposition](#prop:crossing-energy-decomposition)): the $\cosh$ weight carries the crossing sign, so its total is the *net* count $p - m$, which is $2Q(\mathfrak{H})$ for the [Coulomb charge](#def:coulomb-charge) $Q$; the $\sinh$ weight is blind to the sign, so its total is the *gross* count $p + m$. The sign-blindness is also what leaves a residue when a composite is paired with its mirror.

Which physical force each channel realises is **not** settled by the decomposition, and this block makes no such assignment. In particular the antisymmetric channel cannot be the charge-sensitive one: its coefficient $p + m$ is a crossing count, hence non-negative, so the channel cannot change sign with the chirality of the composite. It is the *symmetric* channel that $Q$ scales. Supplying a route from $Q$ to either channel, or relabelling them, is open.

**Pair creation.**

When creating an $e^- e^+$ pair, cancellation yields:

$$
  \mathfrak{E}_{\mathrm{cross}}(e^-) + \mathfrak{E}_{\mathrm{cross}}(e^+)
  = 6\sinh(\ln q)
  \approx 0.630 \quad (\text{Skein units}).
$$

Symmetric contributions cancel, leaving a purely antisymmetric residual. It is strictly positive, $6\sinh\lambda > 0$, because the surviving coefficient is a crossing count; the pair therefore cannot annihilate to zero crossing energy. Reading that residual as the repulsion which separates the pair requires the channel identification left open above.

**Channel ratio.**

At $q = q_0$, for a positive braid closure ([ratio identity](#prop:crossing-energy-decomposition)):

$$
  \frac{E_{\mathrm{asym}}}{E_{\mathrm{sym}}} = \tanh(\ln q_0) \approx 0.104.
$$

The antisymmetric channel carries roughly $10\%$ of the symmetric channel's magnitude. This is a ratio of the two channel weights at the substrate anchor, not a running coupling ratio: no renormalisation scale is attached to it, and it should not be read as a value of $\alpha / \alpha_s$, which varies over the accessible energy range. The electromagnetic coupling proper is obtained from the antisymmetric *eigenvalue* $-q^{-1}$ of the Hecke generator by the [EM coupling projection](#prop:em-coupling-projection) — a distinct object from the antisymmetric *channel* of this decomposition, which the shared adjective invites confusing with it.

**Crossing energy table** for a particle with $n_c$ positive crossings:

| Quantity | Formula | $T_{2,3}$ ($n_c = 3$) | Value |
|----------|---------|----------------------|-------|
| Total energy | $n_cq$ | $3q$ | $3.330$ |
| Symmetric component | $n_c\cosh(\ln q)$ | $3\cosh(\ln q)$ | $3.015$ |
| Antisymmetric component | $n_c\sinh(\ln q)$ | $3\sinh(\ln q)$ | $0.315$ |
| Pair net energy | $n_c(q - q^{-1})$ | $3(q - q^{-1})$ | $0.630$ |
| Channel ratio | $\tanh(\ln q)$ | $\tanh(\ln q)$ | $0.104$ |

Because $m = 0$ here, the symmetric and antisymmetric totals coincide with the per-crossing weights times $n_c$, and the channel ratio takes its unqualified value; for a composite with $m \neq 0$ both columns acquire the multiplicity factors of the [decomposition](#prop:crossing-energy-decomposition).

By [Hopf stability](#prop:torus-hopf-stability), $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{p}) < 0$. The symmetric channel dominates the antisymmetric one in magnitude, which is what the stability argument uses; it does not require either channel to be identified with a named force.
