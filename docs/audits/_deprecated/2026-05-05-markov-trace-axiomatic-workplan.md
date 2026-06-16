> **DEPRECATED on 2026-05-24.** Point-in-time status, intermediate workplan iteration, dead-end exploration, or earlier sublemma version superseded by a later "refined" iteration. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T2 for the deprecation rationale.

# Workplan — Axiomatic Markov-trace closed form for atomic braids

**Date:** 2026-05-05
**Branch:** `claude/categorical-mass-divergence-audit` (PR #534)
**Sibling PRs:** #545 (`gb-filtration-jet-tracker`), #546 (`hoefsmit-2x2-fix`)

## TL;DR

We now have a fully axiomatic, representation-theory-free derivation of
$\operatorname{tr}_M(\sigma_1^7\sigma_2^4)$ in $H_3(q)$ that:

- gives a closed-form rational function in $q$,
- evaluates to $1.63315$ at $q_0$ (matches `char_fast` Markov to $<0.1\%$),
- yields $\rho_p^{\mathrm{CODATA}} \approx 1124.3$,
- bypasses PR #546's seminormal `IndexError` on $\sigma_2$ acting on $(3)$.

This is the **categorical-mass anchor for the proton** required by
[`prop:atomic-mass-gb-nf`](../../content/quantum-observable-universe/braids-and-knots/atomic-mass-gb-nf.md).

## Current state (PR #534)

### Done

| item                                                     | location |
|----------------------------------------------------------|----------|
| Factor-of-2 audit: traces are *different*, not normalised | [`docs/audits/2026-05-05-factor-2-resolved-different-traces.md`](2026-05-05-factor-2-resolved-different-traces.md) |
| Hecke-quadratic + Markov axiom reduction (H_3 basis)     | `computations/markov/markov_trace_axiomatic_proton.py` |
| Hecke-power recurrence (a_k, b_k for k=0..7)             | `computations/markov/markov_trace_atomic_proton_full.py` |
| Closed form $\operatorname{tr}_M(\sigma_1^7\sigma_2^4) = (\dots)/q^{10}(q+1)^3$ | same script, witness JSON |
| `prop:markov-trace-antipode-polynomial-symmetry` (.ts/.md/.lean) | content/quantum-observable-universe/braids-and-knots/ |
| `prop:markov-trace-axiomatic-closed-form` (.ts/.md/.lean)  | content/quantum-observable-universe/braids-and-knots/ |
| Plancherel-vs-Markov per-irrep ratio table {2.54, 0.85, 0.14} | `factor_2_normalization_trace_probe.py` witness |

### Numerical anchor at $q_0$

| word                          | $\operatorname{tr}_M$ value | source             |
|-------------------------------|----------------------------|--------------------|
| $\sigma_1$                    | $0.4993$                   | axiom              |
| $\sigma_1\sigma_2$            | $0.2493 = z^2$             | axiom (Markov 2×)   |
| $\sigma_1\sigma_2\sigma_1$    | $0.5514 = z + h z^2$       | axiom + braid + Hecke |
| $\sigma_1^7\sigma_2^4$ (proton) | $1.63315$                  | Hecke-power recurrence |
| `char_fast` reference         | $1.6334$                   | seminormal ascent  |

Match to $4$ significant digits validates both the axiomatic and
seminormal routes.

### Open

| item                                                       | priority | notes |
|------------------------------------------------------------|---------|-------|
| Recursive symbolic Markov-trace reducer for general $H_n$  | P1      | bug in `tr_m_basis_element`: H_3 truncation infinite-recurses |
| Lean infrastructure: `Hecke n q` typeclass + `MarkovTrace` axioms | P2 | gates the formal proof of `markovTraceAxiomaticClosedForm` |
| Apply axiomatic reducer to neutron $\sigma_1^6\sigma_2^4\sigma_1^{-1}$ | P1 | uses $\sigma^{-1} = \sigma - h$ from quadratic |
| Apply to deuteron in $H_6$ ($\sigma_1\sigma_2\sigma_4\sigma_5$ disjoint) | P2 | tests methodology on disjoint clusters |
| Formal antipode-symmetry test on Markov trace (cf. PR #546's polynomial) | P3 | empirically NOT anti-self-reciprocal for Markov (only for Plancherel) |

## Methodology summary

1. **Hecke-power recurrence** — for any single-generator power
   $\sigma_i^k$, decompose as $a_k(h)\sigma_i + b_k(h)$ via the
   quadratic relation; $a_k, b_k$ are integer polynomials in
   $h = q - q^{-1}$ given by the linear recurrence
   $a_{k+1} = h a_k + b_k$, $b_{k+1} = a_k$, $a_0=0$, $b_0=1$.
2. **Word expansion** — for words $\sigma_{i_1}^{k_1}\cdots\sigma_{i_m}^{k_m}$
   factor each generator power as $a_k\sigma_i + b_k$ and distribute.
   Result: a $\mathbb{Z}[h]$-linear combination of basis elements
   $\sigma_{i_1}^{\epsilon_1}\cdots\sigma_{i_m}^{\epsilon_m}$ with
   $\epsilon_j \in \{0, 1\}$.
3. **Basis-element trace values** — for $H_3$, six basis elements
   $\{1, \sigma_1, \sigma_2, \sigma_1\sigma_2, \sigma_2\sigma_1, \sigma_1\sigma_2\sigma_1\}$
   have axiom-determined trace values (cf. content block table).
4. **Substitution + simplification** — substitute $h = q - q^{-1}$,
   $z = 1/(q^{1/2}+q^{-1/2})$, run `sp.cancel`. Output is a
   rational function in $\sqrt{q}$ over $\mathbb{Z}$.

## Sibling-PR coordination

### PR #545 — `gb-filtration-jet-tracker`

**Status:** complementary. PR #545 provides the GB-filtration
infrastructure (`gb_filtration_jet_tracker.HeckeElement` symbolic
class) used by the axiomatic computation as a backing for general
braid-word reduction. No conflict; this PR's `markov_trace_recursive.py`
imports `HeckeElement` directly.

**Ask of PR #545:** confirm `HeckeElement.right_mul_T(i)` correctly
implements the Hecke quadratic in symbolic $q$ (it appears to from
inspection; recursive reducer's bug is in *our* truncation logic,
not in HeckeElement).

### PR #546 — `hoefsmit-2x2-fix` / Plancherel closed form

**Status:** different categorical object. PR #546's "tr_M" is the
**Plancherel trace** $\operatorname{tr}^{\mathrm{Plan}} = \sum_\lambda w_\lambda \chi^\lambda$
with $w_\lambda = \dim_q^2(\lambda)/[n]_q!$, NOT the Markov trace.
The Markov trace uses Jones-Markov weights $y_\lambda$ from the
Markov-axiom system; per-irrep ratios in $H_3$ are
$y_\lambda / w_\lambda \in \{2.54, 0.85, 0.14\}$ (non-uniform, so
not a normalisation factor).

**Ask of PR #546:**

1. The IndexError bug in `q_character_on_braid_word` (gen_idx 2
   out of range for shape $(3)$) — should this be fixed in PR #546,
   or do we accept the axiomatic route as the primary categorical
   anchor and treat #546's seminormal route as cross-check only?
2. The polynomial closed form $p(q)/(12 q^{10})$ derived in #546 is
   the *Plancherel* trace; the axiomatic Markov-trace closed form
   has denominator $q^{10}(q+1)^3$ instead. Confirm the title /
   description in #546 should be updated to "Plancherel trace
   closed form" to avoid confusion with prop:categorical-mass-markov.

## Decision points for the user

The axiomatic route is now self-sufficient for the proton anchor.
Two choices for next step:

1. **Generalise**: fix the recursive reducer bug, run on neutron +
   deuteron, get a unified table of axiomatic Markov traces for
   $A \in \{1, 2, 3, 4\}$.
2. **Formalise**: build the `Hecke n q` Lean typeclass + `MarkovTrace`
   axioms to upgrade `markovTraceAxiomaticClosedForm` from a
   `trivial` placeholder to a fully verified Lean proof.

Recommend **(1) first** (broader coverage matters more for the paper
than premature Lean formalisation). Lean infrastructure can land in
a follow-up.

## Cross-post template

Below is a short summary suitable for posting to PR #545 and #546.

> **From PR #534 (categorical-mass-divergence-audit), 2026-05-05:**
>
> We have a representation-theory-free axiomatic closed form for
> $\operatorname{tr}_M(\sigma_1^7\sigma_2^4)$ giving the proton mass
> anchor $\rho_p^{\mathrm{CODATA}} \approx 1124.3$. Methodology and
> implications for sibling PRs are documented in
> [`docs/audits/2026-05-05-markov-trace-axiomatic-workplan.md`](https://github.com/litlfred/qou/blob/claude/categorical-mass-divergence-audit/docs/audits/2026-05-05-markov-trace-axiomatic-workplan.md).
> See the **Sibling-PR coordination** section for asks/notes specific
> to this PR.
