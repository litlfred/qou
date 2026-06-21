## Two fingerprints, one structure

The pair of propositions
[`prop:he4-two-row-dominance`](#prop:he4-two-row-dominance) and
[`prop:he4-channel-active-set`](#prop:he4-channel-active-set)
analyse the $^4\mathrm{He}$ doubly-magic binding through two
independent compute paths:

| level | machinery | dominant structure | binding source |
|---|---|---|---|
| **Channel** (LP) | operator-selection LP on $\Delta_\mathrm{cat}$ anchors | primal $\mathrm{T} \oplus p$; dual $y^\star_{\mathrm{D} \oplus \mathrm{D}} = 3.778$ | deuteron-pairing receptivity |
| **Wedderburn block** (braid) | $\Sigma_\lambda y_\lambda \cdot \chi^\lambda_q(\beta_{{}^4\mathrm{He}})$ at $n = 12$ | two-row stratum $\Lambda^2(12)$ at $86.6\,\%$; $\lambda^\star = (9, 3)$ at $29.0\,\%$ | $q$-symmetric spin-pairing |

These are not two ways of saying the same thing by definition:

- The channel decomposition operates at the
 categorical atom level — it consumes
 the empirical $\Delta_\mathrm{cat}$ values of $D, T, {}^3\mathrm{He}, {}^4\mathrm{He}$
 and solves a 3-dimensional LP on coupling residuals.

- The Wedderburn decomposition operates at the per-irrep matrix
 trace level on the Hecke algebra $H_{12}(q)$ — it consumes
 the canonical 47-crossing braid word
 $\beta_{{}^4\mathrm{He}} = \mathrm{atom\_braid\_word\_3A}(2, 2)$ and
 evaluates the Wedderburn sum over all $77$ partitions of $12$.

The compute infrastructure for the two is independent: the LP uses
`scipy.linprog`; the Wedderburn sum uses Hoefsmit per-irrep
characters at $q_0$ via the
`global_wedderburn_sum_q_hecke_seminormal` machinery. There is no
shared cache and no shared algebraic identity that would force
agreement.

## Why they agree

The two-row stratum $\Lambda^2(12)$
*is* the algebraic image of $\mathrm{SU}(2)$-symmetric pairing on
12 strands: under the Schur–Weyl functor restricting
$\mathrm{H}_{12}(q) \to \mathrm{End}_{\mathrm{SU}(2)}(V^{\otimes 12})$
with $V = \mathbb{C}^2$, partitions $\ell(\lambda) > 2$ map to
zero. The Wedderburn fingerprint at $86.6\,\%$ in $\Lambda^2(12)$
therefore says: *$^4\mathrm{He}$ is, at the trace level, almost a
$q$-symmetric spin-pairing object*.

The channel fingerprint says the same at the energetic level:
the highest dual shadow price — i.e. the channel into which the
binding "would flow first" under a coupling perturbation — is
$\mathrm{D} \oplus \mathrm{D}$. Deuteron pairing is the
energetically dominant route into the magic shell.

The agreement that **both routes point at deuteron-pairing as
the load-bearing geometry** is the substrate-derived account of
the empirical "doubly-magic" identity of $^4\mathrm{He}$:

> $^4\mathrm{He}$ is doubly-magic *because* its canonical braid
> word lives in the two-row Wedderburn stratum, *and* its
> energetic LP places the highest shadow price on the deuteron-
> pairing channel. These are independent statements of the same
> $q$-symmetric pairing geometry.

## Connection to PR #645 / PR #656

[PR #645](https://github.com/litlfred/qou/pull/645) pinned the
$(2, 2)$ anchor empirically — $\Delta_\mathrm{coupling}(2, 2) \approx
[A-2]_q \cdot E_0 \cdot \log(1/h)$ closes to $0.169\,\%$ — but the
prefactor's universality across $A = 3$ was refuted by the F2
H7a-cross-anchor probe on this branch. PR #656 (the sibling
substrate-derivation session) found that the doubly-magic match
is genuinely special and proposed the D-2
$\mathrm{Cat}_q(A-1, 1) = [A-1]_q\,[A-2]_q / ([2]_q\,[A]_q)$
candidate with Z/N-dependent SYT-shape corrections.

The structural fingerprint here is **complementary**: while #656
proposes a *combinatorial* mechanism (q-Catalan multiplicity with
SYT correction), the Wedderburn–channel agreement above gives an
*algebraic* mechanism (two-row $\Lambda^2$ dominance +
$\mathrm{D} \oplus \mathrm{D}$ shadow-price dominance). The two
descriptions are not in tension — Cat_q multiplicities are
themselves expressible as sums over $\Lambda^2$ partitions — but
they live at different abstraction layers. Future work
([`conj:magic-shell-stabilization`](#conj:magic-shell-stabilization))
should make the bridge between them explicit.

## No new logical claim

This remark interprets the two propositions in physical and
structural terms. It does not introduce a new theorem; per the
remark-authoring convention (AGENTS.md §3a) it sets
`interprets: "prop:he4-two-row-dominance"` and cites the channel
proposition by name in the body.
