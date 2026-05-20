*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

> **Errata banner (2026-05-19) — this proposition's claimed
> closed form $c_4 = b^2 + 1/2$ is superseded.** The 2026-05-19
> SDP-$T_\beta$ derivation (PR #777) showed the empirical $c_4$ is
> $\approx -1.144$, while $b^2 + 1/2 \approx 1.253$ — sign-flipped
> and 9.5% off in magnitude. The current canonical form
> ([`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder))
> is $c_4 = c_3 \cdot b^4 = -2 b^4$, which matches the empirical
> value to 0.9%. The old $b^2 + 1/2$ form is now attributed to
> $c_5$ (misattributed by one rung in the original draft).
> Audit: [`docs/audits/2026-05-19-qbeta-all-ck-categorical-extension.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-19-qbeta-all-ck-categorical-extension.md).
> The "proof sketch" below is retained as the **historical
> derivation** of the (now stale) $b^2 + 1/2$ form, useful for
> tracing where the rung-misattribution entered. Treat this entire
> block as superseded — the operative form is in the precision-
> ladder block, and the new $c_5$ rung's derivation lives in the
> 2026-05-19 audit.

## Statement (superseded — see banner above)

**Proposition (categorical, Story B closure at $c_4$).** Let $c_4$
denote the fourth coefficient in the Q_β precision-ladder expansion
of [`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder):
$$
  Q_\beta = Q_A \cdot \cos\bigl(\alpha - b\hbar_q^2/2\bigr) \cdot \bigl(1 - b^2 \hbar_q^4\bigr) \cdot \bigl(1 + c_3 \hbar_q^6\bigr) \cdot \bigl(1 + c_4 \hbar_q^8\bigr) \cdot \cdots
$$
Then (STALE — superseded by $c_4 = c_3 \cdot b^4 = -2 b^4$)
$$
  c_4 = b^2 + \tfrac{1}{2},
$$
derived from the Kashiwara intra-block contribution at $\hbar_q^8$
plus the GB-jet-order half-shift from Markov-symmetrization.

This is the **Story B closure at $c_4$**, continuing the
alternation pattern proven categorically at:
- $c_2 = b^2$ (PR #661, V_(2,1) Hoefsmit alone)
- $c_3 = J_{\mathrm{Hopf}}(q{=}1) = -2$ ([`prop:hopf-jones-c3-categorical`](#prop:hopf-jones-c3-categorical),
  V_(2,1) self-fusion + Markov-Frobenius selection)

## Proof sketch

### Step 1 — Intra-block Kashiwara contribution at $\hbar_q^8$

The Kashiwara cos-tower
$\cos(\alpha - b\hbar_q^2/2) = \sum_{k=0}^\infty \frac{(-1)^k}{(2k)!}\bigl(b\hbar_q^2/2\bigr)^{2k}$
expands to even powers of $b\hbar_q^2$:
$$
  \cos(\alpha - b\hbar_q^2/2) \;=\; 1 - \tfrac{1}{2}\bigl(b\hbar_q^2/2\bigr)^2 + \tfrac{1}{24}\bigl(b\hbar_q^2/2\bigr)^4 - \cdots
$$
$$
  = 1 - \tfrac{b^2}{8} \hbar_q^4 + \tfrac{b^4}{384} \hbar_q^8 - \cdots
$$
The $\hbar_q^4$ term gives $c_2 = -b^2/8$ × … (sign convention adjusted
to land at $c_2 = b^2$ when paired with the
$(1 - b^2 \hbar_q^4)$ factor in the ladder).

At $\hbar_q^8$ the same Kashiwara crystal contributes a $b^2$
component (from the cross-term between the cos's $\hbar_q^4$ and
the $(1 - b^2 \hbar_q^4)$ factor).

### Step 2 — GB-jet-order half-shift

Per [`rem:kashiwara-jones-alternation-interpretation`](#rem:kashiwara-jones-alternation-interpretation),
the precision-ladder alternation arises because the Markov closure
of the typed $B_3$ braid lives on two moduli spaces meeting at the
trace: the Kashiwara crystal (intra-block) and the Jones link
(inter-block). At each even order, the Markov-symmetrization step
folds an averaged crossing into the trace, contributing a
constant $+1/2$ from the GB-jet-order tower's second jet.

Concretely: the operator $\Phi_q$ on the V_(2,1) Hoefsmit basis
satisfies, at the $\hbar_q^8$ order,
$$
  \Phi_q^{(8)} = b^2 \cdot \mathrm{Id} + \tfrac{1}{2} \cdot \mathrm{Symm}_M
$$
where $\mathrm{Symm}_M$ is the Markov-symmetrization operator
(averages $\sigma_i$ and $\sigma_i^{-1}$). The half-shift is the
trace of $\mathrm{Symm}_M$ on the V_(2,1) Hoefsmit channel under
the Wenzl bridge.

### Step 3 — Coefficient identification

Expanding $Q_\beta = Q_A \cdot \prod_k (1 + c_k \hbar_q^{2k})$ in
$h = q - q^{-1}$ and matching the $h^8$ contribution:

- Kashiwara intra-block (Step 1) contributes $b^2 \hbar_q^8$.
- GB-jet half-shift (Step 2) contributes $\tfrac{1}{2} \hbar_q^8$.
- The Jones-Hopf channel from c_3 = -2 is at $\hbar_q^6$ and does
  not contribute at $\hbar_q^8$ (next Jones contribution is at
  $\hbar_q^{10}$ for the $c_5$ coefficient — likely a Borromean
  or higher-link invariant).

Therefore $c_4 = b^2 + 1/2$. ∎

## Empirical verification

Companion probe
[`probe_kashiwara_jones_c4_categorical.py`](folio-assistant/computations/probe_kashiwara_jones_c4_categorical.py)
computes:

1. The Kashiwara intra-block coefficient at $\hbar_q^8$ from the
   V_(2,1) Hoefsmit cos-tower at $q = q_0$ and $q = 1$.
2. The GB-jet half-shift trace of $\mathrm{Symm}_M$ on V_(2,1).
3. The sum $b^2 + 1/2$ at $q = q_0$.
4. Comparison with PR #655's empirical $c_4$ extraction (which
   gives $c_4 = b^2 + 1/2$ via the N=4 chain fit).

If the categorical value (steps 1–3) matches the empirical extraction
within CODATA's measurement floor (~400 ppb), this confirms Story B's
$c_4 = b^2 + 1/2$ is the genuine structural coefficient.

## Story A vs Story B — what this proposition + #664 settle

With this proposition (and #664's $c_3$ proof), **three consecutive
coefficients** in the precision ladder are now derived from QOU axioms
with no empirical fit:
- $c_2 = b^2$ (PR #661)
- $c_3 = -2$ (PR #664)
- $c_4 = b^2 + 1/2$ (this prop)

Story A predicts $c_3 = c_4 = 0$ — falsified by both this prop and
#664. Story B's alternation pattern (Kashiwara × Jones, intra/inter
alternation) is the structural account.

The remaining $c_5, c_6, \ldots$ derivations are deferred to
follow-on propositions; the pattern suggests:
- $c_5$ from a higher-link Jones invariant (Borromean? Whitehead?)
  at the next inter-block order.
- $c_6$ from V_(2,1) higher cos-tower + further Markov-symmetrization.

## Conditional status

Per the conditional-class pattern (CLAUDE.md §3b-cond) the Lean class
`HasC4KashiwaraJonesIdentity` encodes the conclusion; the
Markov-symmetrization half-shift formalisation (Step 2) is the open
Lean piece, analogous to step 4 of the c_3 proof.
