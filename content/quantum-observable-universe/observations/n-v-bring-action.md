**Conjecture ($S_5$ acts on the EW slice of $H_n(q)$).**
*Let $\mathcal{U} = (\mathbf{C}, \varTheta, G, \mathcal{S})$ be a quantum
observable universe with substrate parameter $q_0$ and Bring's-surface
geometric substrate ([brings is qou](#prop:brings-is-qou)). At the
**electroweak slice** $\Sigma_{\mathrm{EW}}$ of the brane tower---the level
at which the weak scale $v$ emerges as a categorical observable---the
Iwahori--Hecke algebra $H_{n_{\mathrm{EW}}}(R, q)$ carries a faithful action
of $S_5 = \mathrm{Aut}(\mathbf{Bring})$ that fixes the Markov trace $\tau_M$.*

*Furthermore, the Markov-trace-residual rescaling factor at the EW slice
equals $|S_5| = 120$:*

$$
  \tau_M\bigl(C_{\dim_q}^{\mathrm{EW}}\bigr) \cdot
    \mathrm{rescale}_{\Sigma_{\mathrm{EW}}}
  \;=\; 120 \cdot \tau_M\bigl(C_{\dim_q}^{H_{n_{\mathrm{EW}}}(R,q)}\bigr),
$$

*where $\mathrm{rescale}_{\Sigma_{\mathrm{EW}}}$ is the categorical
projector from the universal Frobenius co-Casimir trace
([Frobenius co-Casimir universal](#thm:frobenius-codim-universal))
onto the EW slice.*

## Forcing of $S_5$ over other finite groups

Three structural constraints force the choice of $S_5$:

1. **Bring's-surface symmetry.** The geometric substrate is the genus-4
   quintic Bring curve ([Bring is QOU](#prop:brings-is-qou),
   [hyperelliptic quintic](#def:hyperelliptic-quintic)). Its conformal
   automorphism group is exactly $\mathrm{PSL}_2(\mathbb{F}_5) \cong
   A_5 \rtimes \mathbb{Z}/2 \cong S_5$ of order $|S_5| = 120$.
2. **Quintic intersection.** The symmetric polynomial relation
   $\sum x_i = \sum x_i^2 = \sum x_i^3 = 0$ in $\mathbb{P}^4$ cuts out the
   Bring locus. This relation is manifestly $S_5$-invariant.
3. **TQFT level.** The Reshetikhin--Turaev TQFT at level $k = 5$ has a
   Hilbert-space dimension matching the EW gauge content. The level-$5$
   structure ties the categorical $S_5$ action to the SU$(2)_5$ modular
   tensor category.

## Constructions required

To upgrade this conjecture to a theorem, we require three categorical ingredients:

1. **Definition** of the EW slice $\Sigma_{\mathrm{EW}}$ as a distinguished
   level of the brane tower ([mass endomorphism conjecture](#conj:mass-endomorphism)).
   The GB filtration grade or jet order at which the EW closure occurs
   remains undefined.
2. **Construction** of the $S_5$-action on $H_n(R, q)$ at that slice, proceeding
   from the geometric Bring action on $\mathcal{S}$ via the fibre functor $\tau$.
3. **Proof** that the Markov-trace residual rescales by $|S_5|$ rather than
   another categorical invariant of the $S_5$-action (such as the rank of the
   associated representation).

Without these components, the closure $N_v = 120 \cdot q_0^{90}$ constitutes an
empirical observation with a $-0.58\%$ residual against CODATA, not a derivation.

## Empirical evidence

Per [`docs/audits/n-v-derivation-candidates.md`](../../../docs/audits/n-v-derivation-candidates.md),
the closure $N_v = 120 \cdot q_0^{90}$ matches the experimental target
$N_{v,\mathrm{target}} = 1.4455 \times 10^6$ to within $-0.58\%$. No other
small-prefactor or integer-$L$ pair in a search space of approximately 1000
pairs yields a closer match. The next-best candidate ($5^2 \cdot h \cdot q^{120}$)
exhibits a $-0.93\%$ residual. We retain conjectural status pending the required
categorical proofs.
