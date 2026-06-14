**Conjecture (S_5 acts on the EW slice of $H_n(q)$).**
*Let $\mathcal{U} = (\mathbf{C}, \varTheta, G, \mathcal{S})$ be a quantum
observable universe with substrate parameter $q_0$ and
Bring's-surface geometric substrate
([brings is qou](#prop:brings-is-qou)).
At the **electroweak slice** $\Sigma_{\mathrm{EW}}$ of the brane
tower — the level at which the weak scale $v$ emerges as a
categorical observable — the Iwahori--Hecke algebra
$H_{n_{\mathrm{EW}}}(R, q)$ carries a faithful action of
$S_5 = \mathrm{Aut}(\mathbf{Bring})$ that fixes the Markov trace
$\tau_M$.*

*Furthermore, the Markov-trace-residual rescaling factor at the
EW slice equals $|S_5| = 120$:*

$$
  \tau_M\bigl(C_{\dim_q}^{\mathrm{EW}}\bigr) \cdot
    \mathrm{rescale}_{\Sigma_{\mathrm{EW}}}
  \;=\; 120 \cdot \tau_M\bigl(C_{\dim_q}^{H_{n_{\mathrm{EW}}}(R,q)}\bigr),
$$

*where $\mathrm{rescale}_{\Sigma_{\mathrm{EW}}}$ is the categorical
projector from the universal Frobenius co-Casimir trace
([Frobenius co-Casimir universal](#thm:frobenius-codim-universal))
onto the EW slice.*
## Why $S_5$, not another finite group

The choice of $S_5$ is forced by **three independent structural
constraints**:

1. **Bring's-surface symmetry.**  The QOU geometric substrate is
   the genus-4 quintic Bring curve
   ([Bring is QOU](#prop:brings-is-qou),
   [hyperelliptic quintic](#def:hyperelliptic-quintic)),
   whose conformal automorphism group is exactly
   $\mathrm{PSL}_2(\mathbb{F}_5) \cong A_5 \rtimes \mathbb{Z}/2 \cong S_5$
   of order $|S_5| = 120$.
2. **Quintic intersection.**  The Bring locus is cut out by
   the symmetric polynomial relation
   $\sum x_i = \sum x_i^2 = \sum x_i^3 = 0$ in $\mathbb{P}^4$ —
   manifestly $S_5$-invariant.
3. **TQFT level.**  The Reshetikhin--Turaev TQFT at level $k = 5$
   has Hilbert-space dimension matching the EW gauge content.
   The level-$5$ structure ties the categorical $S_5$ action to
   the SU$(2)_5$ modular tensor category (the formal
   identification of this MTC as a QOU content block is open).

## What needs to be constructed

To upgrade this conjecture to a theorem, the missing categorical
ingredients are:

(a) **Definition** of the EW slice $\Sigma_{\mathrm{EW}}$ as a
distinguished level of the brane tower
([mass endomorphism conjecture](#conj:mass-endomorphism)).  The
GB filtration grade or jet order at which the EW closure occurs
is currently undefined.

(b) **Construction** of the $S_5$-action on $H_n(R, q)$ at that
slice — from the geometric Bring action on $\mathcal{S}$ via the
fibre functor $\tau$.

(c) **Proof** that the Markov-trace residual is rescaled by
$|S_5|$ rather than some other categorical invariant of the
$S_5$-action (e.g. the rank of the associated representation).

Without (a)--(c), the closure $N_v = 120 \cdot q_0^{90}$ remains a
**numerical observation** with $-0.58\%$ residual against CODATA,
not a derivation.

## Empirical evidence

Per [`docs/audits/n-v-derivation-candidates.md`](../../../docs/audits/n-v-derivation-candidates.md),
the closure $N_v = 120 \cdot q_0^{90}$ matches the experimental
$N_{v,\mathrm{target}} = 1.4455 \times 10^6$ to within $-0.58\%$.
No other small-prefactor / integer-$L$ pair in a search space of
$\sim 1000$ pairs gives a closer match; the next-best ($5^2 \cdot h \cdot
q^{120}$) is at $-0.93\%$.

The Bonferroni-corrected significance is non-trivial; the match
is suggestive but not by itself conclusive — hence the
conjectural rather than theorem-level status.
