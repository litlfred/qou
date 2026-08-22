# `prop:confinement-frobenius-reciprocity` asserts a premise convention D makes false

**Branch** `claude/frobenius-reciprocity-premise-audit-2026-08-22` · surfaced while
closing bean `qou-cnbm` (PR #5417)

> **Two probes cited below are on #5417 and not yet on `main`.** They are linked
> at that branch rather than relatively, so the links resolve today; re-point
> them to `main` once #5417 merges.

## The conflict, in two lines

The proposition's proof opens:

> *The Markov trace $\mathrm{tr}_M$ is a **non-degenerate** Frobenius form on $H_n(q)$.*
> — [`confinement-frobenius-reciprocity.md`](../../content/quantum-observable-universe/nuclear-interactions/confinement-frobenius-reciprocity.md) line 37

Under **convention D**, canonical since the owner ruling of 2026-08-15, the
Markov–Gram form on the $H_3$ NF basis is **singular**: rank 5 of 6, radical =
the sign representation. Established by `qou-m7py` (`be59f01376`) and
independently re-validated in
[`2026-08-16-s2-gram-radical-independent-revalidation.md`](2026-08-16-s2-gram-radical-independent-revalidation.md),
whose headline is that *"every relayed number is correct"* and the degeneracy is
**"exact and structural"**.

Non-degeneracy is not decoration in that proof — it is what licenses the step
$T^\vee = \sum_{i,j} x_i^* (G^{-1})_{ij}\, b_j$, i.e. the existence of $G^{-1}$,
which is the master formula's whole content.

## Why this is not merely a stale sentence

Per AGENTS.md §*"Conditional-proved ≠ premise-established"*, a result whose
antecedent is false is not thereby false — but it is **not established either**,
and it cannot be cited as though it were. The master formula is currently cited
by four compute consumers and three sibling content blocks.

**Two of the four compute consumers cannot run at all** (measured 2026-08-22):

| consumer | status |
|---|---|
| `borromean-axial-coupling.py` | `KeyError: 'gram_inverse'` |
| `probes/delta_lambda_master_formula_h3_probe.py` | `KeyError: 'gram_inverse'` |
| `bound_state_observable_validator.py` | exit 0 |
| `audit_frobenius_pairing.py` | exit 0 |

The key is absent because `be59f01376` removed it deliberately and renamed it
`gram_quotient_inverse`, on the reasoning that *"a consumer keyed on the old
name should fail loudly rather than silently receive a different matrix"*. So
these two failures are the corpus working as designed. They are listed here as
**evidence of reach**, not as bugs to patch.

## A second disagreement: the two readings of $(G^{-1})|_{A^*}$

The block and its compute do not describe the same object.

- The block calls $(G^{-1})_{ij}$ *"the Frobenius dual-basis matrix on the
  $|A^*(T)|$-dimensional **active subspace**"* — which reads as
  $(G|_{A\times A})^{-1}$, the dual basis **of that subspace**.
- `borromean-axial-coupling.py` says *"restricting $G^{-1}$ to its principal
  submatrix on $A^*$"* — which is $(G^{-1})|_{A\times A}$.

These differ by a Schur complement whenever $A^*$ is proper. Measured at 50 dps:
$G|_{A\times A}$ is **nonsingular on all 62 proper subsets**, singular only on
the full set, worst proper $|\lambda_{\min}| = 0.0564$ — so the subspace reading
is well-posed even though the ambient one is not
([`gram_restricted_nonsingularity_probe.py`](https://github.com/litlfred/qou/blob/claude/muon-fallback-drain-2026-08-21/computations/probes/gram_restricted_nonsingularity_probe.py) — lands with #5417).

## And the case that decides it is not a computability question at all

For the observable this producer exists to compute, neither reading helps.
`be59f01376` states the constraint: *"Dualising against a degenerate form is
well-defined only for vectors orthogonal to the radical, because generalized
inverses differ precisely by radical terms."* Measured at 50 dps
([`axial_observable_is_the_gram_radical_probe.py`](https://github.com/litlfred/qou/blob/claude/muon-fallback-drain-2026-08-21/computations/probes/axial_observable_is_the_gram_radical_probe.py) — lands with #5417):

| observable | $|\cos|$ to radical |
|---|---|
| trivial $O_V$ | $2.95\times10^{-51}$ — orthogonal to the arithmetic floor |
| sign $O_A$ | $\mathbf{1.0}$ — **is** the radical, exactly |

The radical **is** the sign representation, and $O_A$ **is** the sign character,
so they coincide by construction. The **axial** pairing therefore has no value:
every generalized inverse answers differently, by exactly a radical term. The
trivial channel is fine.

## What this audit does and does not claim

**Claims, measured:** the proposition's stated premise is false at $n = 3$ under
the canonical convention; the block and its compute describe different objects;
the axial channel has no dual pairing in this construction.

**Does not claim:** that the proposition is *wrong*. Its conclusion may well hold
on the quotient by the radical — the S2 revalidation adjudicates
quotient-by-radical as *"the standard construction rather than a repair hack"*,
which is the obvious re-scoping. That is a mathematical judgement for whoever
owns `qou-m7py`, not something to assert from a compute branch.

**Scope-(a)** per AGENTS.md: this measures $H_3$ in the NF basis under
convention D. Other $n$, bases, or conventions are untested here.

**Not established:** `bound_state_observable_validator.py` requires
`gram_inverse` among its `REQUIRED_FIELDS` and still exits 0, checking 3 of 1427
witnesses. That *looks* like a gate whose subjects are stale enough to still
carry the removed key — but I could not reproduce its flagging predicate, so
whether it is latently broken is **unmeasured**, and is recorded as a question
rather than a finding.

## Suggested disposition

1. Re-scope the proposition's premise to the quotient (or state non-degeneracy
   as a hypothesis it is conditional on), per §*"Conditional-proved ≠
   premise-established"*.
2. Reconcile the block's *"dual-basis matrix on the active subspace"* with the
   compute's *"principal submatrix of $G^{-1}$"* — they are different objects
   and only one can be meant.
3. Decide whether the axial channel is meaningful under the quotient. Measured,
   in this construction, it is not.
