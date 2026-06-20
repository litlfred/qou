# Dual `tr_M` discrepancy — TWO different Markov traces on `main`

**Date:** 2026-05-17
**Branch:** `claude/post-670-story-b-mp-c5-c6`
**Status:** Infrastructure audit. Discovered while critically reviewing
PR #664's c_3 categorical-derivation claim. The codebase has **two**
distinct functions named `tr_M_*` that compute genuinely different
numerical values, with no clear convention indication of which is
canonical. Approximately 15+ production mass-derivation scripts use
one; the precision-ladder framework (AGENTS.md `thm:jones-markov-trace`)
implicitly cites the other.

## The two implementations

| Function | Module | Formula |
|---|---|---|
| `tr_M_symbolic` | [`hoefsmit_symbolic.py`](../../computations/hoefsmit_symbolic.py) | $\displaystyle \text{tr}_M(\beta) = \sum_\lambda \frac{\dim_q^2(\lambda)}{[n]_q!} \cdot \frac{\chi^\lambda(\beta)}{f^\lambda}$ |
| `tr_M_canonical` | [`markov_weights_symbolic.py`](../../computations/markov/markov_weights_symbolic.py) | $\displaystyle \text{tr}_M(\beta) = \sum_\lambda y_\lambda(q) \cdot \chi^\lambda(\beta)$, with $y_\lambda$ from Wenzl's Schur principal specialisation |

The Wenzl $y_\lambda$ is the literature-standard Jones-Markov weight
(Wenzl 1988); `dim_q^2/[n]_q!` is a different weight that gives the
$q$-Plancherel measure on partitions (the q-deformation of $f^\lambda$).

## Numerical evidence — they disagree

For the Hopf+ braid $\sigma_1^2$ in $H_2(q)$ at $q = q_0 \approx 1.10998$
(the substrate parameter):

On σ_1² in H_2:

| Implementation | Symbolic | Value at $q_0$ |
|---|---|---:|
| `tr_M_symbolic` | $(q^4 + 1)/(q^3 + q)$ | 1.0163158... |
| `tr_M_canonical` | (large rational in $q^{1/2}$) | 1.1043881... |
| **Difference** | — | **0.0881 (~8%)** |

Both give $+1$ at $q = 1$ (coincidence in the limit; their first-order
Taylor expansions about $q = 1$ already differ).

**The discrepancy is much worse on the H_3 braids that production
mass-derivation scripts actually consume** (proton = 3-strand
intra-nucleon Hecke word):

| Braid in H_3 | `tr_M_symbolic` | `tr_M_canonical` | rel $\|\Delta\|$ |
|---|---:|---:|---:|
| $\sigma_1$ | 0.1032 | 0.4993 | **79%** |
| $\sigma_1 \cdot \sigma_2$ | 0.00357 | 0.2493 | **99%** |
| $\sigma_1^3$ (proton intra channel) | 0.3142 | 0.7302 | **57%** |
| $\sigma_1^3 \cdot \sigma_2^3$ (proton-like) | 0.09209 | 0.5332 | **83%** |

These are not coordinate-rounding artifacts. The two implementations
compute **fundamentally different numerical invariants** on the very
braids the mass-derivation chains evaluate. If `tr_M_canonical` is
the canonical Markov trace (per AGENTS.md `thm:jones-markov-trace`),
then every production script using `tr_M_symbolic` is computing the
wrong invariant by 57–99% on the proton-like channel.

Reproducible via [`probe_hopf_markov_trace_genuine.py`](../../computations/probe_hopf_markov_trace_genuine.py)
(σ_1² in H_2) and [`probe_c3_taylor_extraction.py`](../../computations/probe_c3_taylor_extraction.py)
(Taylor coefficients), both on this branch. The H_3 comparison table
is reproduced by an inline script in this audit.

## Is either derived from a categorical action?

| Implementation | Categorical origin |
|---|---|
| `tr_M_canonical` (Wenzl y_λ) | **Yes** — Ocneanu trace on $H_n(q)$ (Ocneanu 1985), expressed via Wenzl's Schur-Weyl decomposition (Wenzl 1988). Standard literature derivation. Computes the Jones polynomial (HOMFLY-Wenzl normalization) of the braid closure. |
| `tr_M_symbolic` (dim_q²·χ/[n]_q!/f^λ) | **No documented derivation as a Markov trace.** The formula computes the q-Plancherel expectation of $\chi^\lambda / f^\lambda$ (the *normalized* character). This is a well-defined invariant (the expected normalized character under the q-Plancherel measure on partitions), but it is **not** the Jones polynomial nor obviously a knot invariant. |

The framework's `thm:jones-markov-trace` (AGENTS.md §7a) implicitly
references the Wenzl/Ocneanu Jones-Markov trace — i.e.
`tr_M_canonical`. So the categorical-action-derived version is the
*canonical one* the framework cites, but **NOT** the one the
production scripts use.

This is the smoking gun: production mass scripts are not computing
the framework's named Markov trace.

## Where each is used on main

Scripts calling **`tr_M_symbolic`** (Hoefsmit, ~15+ production scripts):

- [`d_u_closed_form_proof.py`](../../computations/d_u_closed_form_proof.py)
- [`deuteron_tr_M_symbolic.py`](../../computations/deuteron_tr_M_symbolic.py)
- [`markov_trace_recursive.py`](../../computations/markov/markov_trace_recursive.py)
- [`markov_trace_axiomatic_multi_atom.py`](../../computations/markov/markov_trace_axiomatic_multi_atom.py)
- [`option_b_proton_mass_full_chain.py`](../../computations/option_b_proton_mass_full_chain.py)
- [`probe_neutron_gap_round2.py`](../../computations/probe_neutron_gap_round2.py)
- [`y_lambda_equivalence_proof.py`](../../computations/y_lambda_equivalence_proof.py) (which claims equivalence)

Scripts calling **`tr_M_canonical`** (Wenzl Jones-Markov):

- [`markov_weights_symbolic.py`](../../computations/markov/markov_weights_symbolic.py) (itself, demo only)

AGENTS.md §7a refers to:

> **Markov parameter** $z = 1/(q^{1/2} + q^{-1/2})$ — this is the
> Wenzl convention.
>
> **Jones polynomial:** $J_L(q) = \text{tr}_M(\rho(\beta_L))$ in $H_n(q)$ —
> implicitly the Jones-Markov form, i.e. `tr_M_canonical`.

So the framework documentation cites `tr_M_canonical`, but ~15+
production scripts use `tr_M_symbolic`.

## Is this a coordinate change?

**Partially**, but not exclusively. The two differences are:

1. **Coordinate**: `tr_M_canonical` works internally with
   $\text{SQ} = \sqrt{Q}$ (the Wenzl $q^{1/2}$ convention), giving
   outputs in $(q, q^{1/2})$ coordinates with surviving half-integer
   powers. `tr_M_symbolic` uses pure $q$. AGENTS.md §7a prescribes
   the $q^{1/2}$ Markov parameter, so this is genuinely the canonical
   coordinate.
2. **Formula** (the bigger issue): the weights are *not* the same
   function under any coordinate change. `dim_q^2/[n]_q!` is the
   q-Plancherel measure; `y_λ` is the Jones-Markov weight. These
   coincide at $q = 1$ (both reduce to $(\dim V^\lambda)^2/n!$, the
   classical Plancherel measure) but disagree at $q \neq 1$.

The empirical 8% disagreement at $q_0$ is from Difference (2),
not Difference (1). Difference (1) is a presentation issue; (2)
is a genuine math choice.

## Comparison to AGENTS.md §7a notation register

AGENTS.md explicitly distinguishes three partition-weight families:

> - **Markov / Jones-Markov central coefficient** `$y_\lambda$` — Wenzl hook-content closed form. Sign-indefinite at $n \geq 4$. **Distinct** from Plancherel $w_\lambda$ and q-deformed $\tilde{w}_\lambda$ at $q \neq 1$.
> - **Plancherel measure (classical)** `$w_\lambda := (\dim V_\lambda)^2 / n!$` — classical probability measure on partitions.
> - **Wedderburn-block weight (q-deformed)** `$\tilde{w}_\lambda := \dim_q^2(\lambda) / [n]_q!$` — q-deformed analogue of Plancherel. **Not** a probability measure at $q \neq 1$. **Never** call this "Plancherel weight" without the tilde.

So AGENTS.md *itself* warns that $y_\lambda$, $w_\lambda$, and
$\tilde{w}_\lambda$ are **distinct at $q \neq 1$**.

But the production code's `tr_M_symbolic` uses $\tilde{w}_\lambda / f^\lambda$
(the q-deformed Wedderburn weight divided by SYT count) and **calls it
`tr_M`**. The Wenzl Jones-Markov weight $y_\lambda$ is used only in
`markov_weights_symbolic.py` and `tr_M_canonical`.

**This means:** scripts calling `tr_M_symbolic` are NOT computing the
Markov trace as defined in AGENTS.md §7a / `thm:jones-markov-trace`.
They are computing a different invariant — the q-Plancherel
expectation of the character $\chi^\lambda(\beta) / f^\lambda$.

## Recommendation — put everything on QOU straight-q

Per user direction, standardise on the QOU-canonical convention:

1. **Ratify `tr_M_canonical` as the canonical Markov trace** — it
   matches AGENTS.md §7a's `thm:jones-markov-trace` exactly. The
   $y_\lambda$ weights are the literature standard.
2. **Switch the coordinate**: `tr_M_canonical` outputs in
   $(q, q^{1/2})$. Either (a) implement a `tr_M_canonical_pure_q`
   that substitutes $q^{1/2} \to \sqrt{q}$ and simplifies under
   $q > 0$, or (b) keep $(q, q^{1/2})$ symbolically and document the
   coordinate at every API boundary. Per user's "put all on QOU
   straight-q" direction: do (a).
3. **Rename `tr_M_symbolic` to `tr_q_plancherel`** (or
   `tr_M_dimensional_q`) to reflect what it actually computes — the
   q-Plancherel expectation, not the Markov trace. This makes the
   distinction visible at every consumer site.
4. **Audit downstream consumers**: 15+ scripts. Each one's claim of
   what the value "means" needs to be checked. Specifically:
   - mass-prediction chains use `tr_M_symbolic` — if they're predicting
     m/m_e ratios from Markov-trace-of-atomic-braid, they're predicting
     the wrong invariant per AGENTS.md.
   - shift_NF / q-pole probes likely don't care which weight (the
     q-pole order is a property of $\chi^\lambda$ alone), so they're
     unaffected.
   - The 1ppb dashboard's Layer 1/2 numerical agreement is between
     `markov_peel` and Hoefsmit — both presumably using the same
     `tr_M_symbolic` so cross-consistency proves consistency of the
     non-canonical convention, not consistency with the framework's
     Jones-Markov trace.
5. **Resolve `y_lambda_equivalence_proof.py`** — its claimed
   equivalence does not hold symbolically on H_2. Either the
   equivalence claim needs amendment, or the script's notion of
   equivalence is at a different level (modulo q=1 limit only).

## Implications for PR #664's c_3 claim

PR #664's proposition states "*c_3 = J_Hopf(q=1) = -2 from V_(2,1)
seminormal Markov trace of σ_1²*". Under either interpretation of
"Markov trace":

- `tr_M_symbolic(σ_1^2)` at $q = 1$: +1 (NOT -2)
- `tr_M_canonical(σ_1^2)` at $q = 1$: +1 (NOT -2)

Neither matches PR #664's "from Markov trace" route. The −2 value
arises ONLY from the textbook Jones polynomial $-(q + q^{-1})$
which is the *writhe-corrected* form, not the Markov trace itself.

So even after the dual-trace issue is resolved, PR #664's c_3 = -2
requires a separate writhe-correction step that the PR didn't make.

## Implications for the 1-ppb mass program

Per [`onepb_status_dashboard`](../../computations/onepb_status_dashboard.py):

- Layer 1 (LP-dual / GB-NF): unaffected — uses the per-partition
  $\chi^\lambda$ structure, not the Markov-trace weight.
- Layer 2 (Markov-trace cross-check Hoefsmit ↔ `markov_peel`):
  cross-check is between two *implementations of the same convention*
  (`tr_M_symbolic`), so the 1ppb consistency is internal to that
  convention, **not** a verification against the Jones-Markov trace.
- Layer 3 (structural identities): the AME publication-rounding floor
  argument is independent of tr_M convention. Unaffected.

**The 1ppb program's structural claims are not invalidated**, but
the framing "we compute the Jones polynomial of the atomic braid"
would need to be amended to "we compute the q-Plancherel expectation
of the atomic-braid character." These are different invariants.

## Provenance — where did `tr_M_symbolic` come from?

Traced via `git log -p -S "def tr_M_symbolic"`:

- **Introducing commit:** `58e78090e` (2026-05-05) on branch
  `claude/categorical-mass-divergence-audit`.
- **Commit title:** *"Resolve factor-of-2 mismatch: PR #546 uses
  Plancherel trace, not Markov"*.

The commit message **explicitly documents** the dual-trace issue:

> KEY FINDING: the conventions differ at the per-irrep weight level,
> NOT just by a uniform constant.
>
>   λ ⊢ 3       PR #546 w_λ/f^λ    char_fast y_λ      ratio
>   (3)              0.1634            0.4154         2.54
>   (2,1)            0.3303            0.2809         0.85
>   (1,1,1)          0.1634            0.0227         0.14
>
> Trace ratios across braids: {1.01, 4.84, 1.09, 2.32} — NOT uniform.
>
> CATEGORICAL INTERPRETATION:
>
>   PR #546's tr_M = Σ (dim_q²/[n]_q!) · χ^λ / f^λ
>     → PLANCHEREL/REGULAR TRACE (Hopf-algebra integral)
>     → does NOT satisfy Markov axiom tr_M(1) = 1 except at q=1
>     → PR #546's tr_M(1) = (2 + [2]_q²)/[3]_q! ≈ 0.987 at q_0
>
>   char_fast tr_M = Σ y_λ · χ^λ with y_λ from Markov axioms
>     → CANONICAL HOEFSMIT-WENZL MARKOV TRACE
>     → satisfies tr_M(1)=1, tr_M(σ_1)=z, tr_M(σ_1σ_2)=z²
>
> These are DIFFERENT categorical objects, not different normalizations
> of the same trace.

And further:

> Implication for prop:atomic-mass-gb-nf:
>   prop:categorical-mass-markov requires the Markov trace (the
>   descended Frobenius integral). PR #546's closed-form polynomial
>   is the Plancherel trace. To use it as the dimensional anchor,
>   it needs to be CONVERTED to the Markov trace via re-weighting
>   with the Markov-axiom-determined y_lambda(q).

**The original author already knew.** The function was created
deliberately to compute the Plancherel trace and clearly flagged
that downstream usage as a Markov trace required conversion. But:

1. The function is **named `tr_M_symbolic`** — the `M` for "Markov".
   Naming overload caused subsequent agents (and the production
   chain) to treat it as the Markov trace.
2. The **conversion to Markov via `y_lambda(q)`** that the commit
   message mandates was **never implemented at the consumer sites**.
   ~15 production scripts call `tr_M_symbolic` directly without
   applying the Plancherel-to-Markov conversion.

## Validation — is `tr_M_symbolic` correct?

**As the Plancherel/regular trace: YES.**

The formula $\sum_\lambda \frac{\dim_q^2(\lambda)}{[n]_q!} \cdot \frac{\chi^\lambda(\beta)}{f^\lambda}$
correctly computes:
- The q-Plancherel expectation of the normalized character $\chi^\lambda/f^\lambda$
- Equivalently, the Hopf-algebra integral against the regular representation
- This **is** a well-defined invariant of the Hecke algebra element

At $q = 1$, the q-Plancherel measure reduces to the classical Plancherel
$f^\lambda \cdot f^\lambda / n!$ (since $\dim_q \to f^\lambda$), and the
normalized character $\chi^\lambda/f^\lambda$ is the canonical character
table entry. So at $q=1$ the formula computes the standard classical
trace of the group algebra — correct.

**As "the Markov trace": NO.**

It violates the Markov axiom `tr_M(1) = 1` for $q \neq 1$ (gives
$2 + [2]_q^2)/[3]_q! \approx 0.987$ on $H_3$, computed
in the original commit message). The Markov trace must give 1 on
the identity for all $q$; `tr_M_symbolic` does not.

It also fails the Markov property: $\text{tr}_M(\alpha \cdot \sigma_n) = z \cdot \text{tr}_M(\alpha)$
does not hold with any single constant $z$ depending only on $q$.

**Verdict:** `tr_M_symbolic` is mathematically correct as the
**Plancherel trace**, but it is **NOT a Markov trace** despite the
name. The bug is naming + missing downstream conversion, not the
formula itself.

## The actual fix

1. **Rename `tr_M_symbolic` to `tr_Plancherel_symbolic`** (or
   `tr_q_plancherel_symbolic`) at the source. The misleading name
   is the root cause; the math is fine.
2. **Add `tr_Markov_symbolic`** that applies the canonical
   `y_lambda`-weighted formula (calling `tr_M_canonical` or
   equivalent), with `tr_Markov_symbolic = tr_M_canonical` as the
   one-line definition.
3. **Audit downstream consumers** for which trace they actually want:
   - **mass-prediction chains** that derive m/m_e from "atomic
     Markov trace" want the Markov trace (per AGENTS.md
     `thm:jones-markov-trace`) → switch to `tr_Markov_symbolic`.
   - **q-Plancherel measure probes** (Wedderburn-block weight
     verifications) want the Plancherel trace → already correct,
     just rename their import.
   - The `y_lambda_equivalence_proof.py` claim of equivalence needs
     amendment — the equivalence is the Plancherel↔Markov conversion
     formula, not direct equality.

## Open questions

1. Was the production-script choice of `tr_M_symbolic` deliberate
   (a non-Jones-Markov but equally rigorous invariant) or accidental
   (the "tr_M" naming was overloaded)? The presence of
   `y_lambda_equivalence_proof.py` suggests the original author
   *thought* they were equivalent.
2. If they were never meant to be equivalent, which invariant does
   the framework actually compute when it says "atomic Markov trace"?
   Per AGENTS.md §7a, it should be Jones-Markov, but the production
   path uses q-Plancherel.
3. Do the mass predictions (m_p, m_n, atomic binding) come out the
   same regardless of which convention is used at the input? If yes,
   the bug is purely cosmetic. If no, the per-particle predictions
   on main are predictions of a different invariant than the
   framework intends.

These need owner adjudication before automated fixes.

## Mitigations + numerical/symbolic choice

Per user direction "allow choice of numerical and symbolic depending
on need", the following compute paths are available; each script
should pick based on its output needs:

| Need | Path | Cost | Output form |
|---|---|---|---|
| Symbolic closed-form tr_M (q as variable) | `markov_peel.tr_M_atomic` (atomic) or `markov_trace_canonical.tr_M_word` (generic) | 0.0s atomic, polynomial-in-q for generic | sympy rational in q (or q^{1/2}) |
| Symbolic χ^λ from persistent cache | `chi-{atom}-h{n}.witness.json` | sub-ms | sympy expression string |
| Symbolic χ^λ via Hoefsmit seminormal | `chi_lambda_symbolic` (with `@lru_cache`) | 0.1-22s per partition | sympy rational |
| Numerical tr_M at q_0 (full precision 50 dps) | `atomic_tr_m_mpfr_50dps` | ~1s atomic | mpmath.mpf |
| Numerical χ^λ at q_0 | `chi-lambda-at-q0.witness.json` (when present) | sub-ms | mpmath.mpf |
| LaurentQ ring arithmetic | `hecke_laurent_fast.LaurentQ` | faster than sympy on Laurents | dict[degree, coeff] |
| Pole order at q=0 (crystal-basis limit) | `crystal_pole_order.column_syt_pole_per_cycle` | O(1) per cycle | integer |

**Recommendations per use case:**

- *Mass-prediction at q_0 only* → numerical path. Atomic predictions
  go through `atomic_tr_m_mpfr_50dps` + scalar conversion. No need to
  carry rational functions of q.
- *Closed-form derivation for the precision-ladder* → symbolic
  path via `markov_peel.tr_M_atomic`. Use the q^{1/2} convention
  output and substitute \check{q} = q^{1/2} (spinor rate; this
  audit pre-dates the 2026-06-04 r → \check{q} rename, read
  r as \check{q} where it appears) for pole analysis.
- *q→0 pole order / shift_NF derivation* → crystal-basis. Don't
  build the full Markov trace; use `crystal_pole_order` directly.
- *Per-partition character display* → cache-first read from
  `chi-{atom}-h{n}.witness.json`. Only recompute on cache miss.

## Cross-references

- [PR #664 critical review](2026-05-17-pr-664-c3-c4-critical-review.md)
- [PR #671 coordination ledger](../coordination/story-b-c3-c4-categorical.md)
- AGENTS.md §7a notation register (collision avoidance for the three
  partition-weight families)
- [`probe_hopf_markov_trace_genuine.py`](../../computations/probe_hopf_markov_trace_genuine.py) (reproduces the disagreement)
- [`probe_c3_taylor_extraction.py`](../../computations/probe_c3_taylor_extraction.py) (shows the 8% disagreement extends across Taylor coefficients)

## 2026-05-17 update — Production scope CORRECTED (much smaller than initially claimed)

After deeper investigation prompted by user's question on q-CLT framework
relationship, the audit's earlier claim that "~15 production mass scripts
use the Plancherel trace" was **wrong**.

### Actual production trace flow

`mass_formula_6term_mpfr_50dps.py` (the production 6-term mass chain)
computes T1 = `|tr_M(T_w)|` via:

```python
def term_1_descended_mp(Z: int, N: int) -> mp.mpf:
    from atomic_tr_m_mpfr_50dps import _bridge_tr_M
    tr, _, _, _ = _bridge_tr_M(Z, N, q_str, dps=WORKING_DPS)
    return mp.fabs(tr)
```

`_bridge_tr_M` evaluates `Σ_λ y_λ · χ_λ` via the **Wenzl bridge** — that
IS the canonical Markov trace. Verified by direct cross-check:

```
markov_peel.tr_M_atomic(p) at q_0 = 1.0653062286... (canonical Markov)
markov_weights_symbolic    at q_0 = 1.0653062286... (Wenzl, EXACT match)
hoefsmit_symbolic Plancherel = 0.7022507726... (DIFFERENT by 50%)
```

### What ACTUALLY uses the Plancherel trace

Direct callers of `hoefsmit_symbolic.tr_M_symbolic` (now alias of
`tr_q_plancherel_symbolic`):

1. `deuteron_tr_M_symbolic.py` — diagnostic / analysis script (NOT in
   production mass chain). **MIGRATED** in commit `feb1c1d30` to
   `markov_peel.tr_M_atomic` (canonical Markov), no fallback.
2. `probe_c3_taylor_extraction.py` — PR #671 probe, INTENTIONAL
   comparison between both implementations.
3. `probe_hopf_markov_trace_genuine.py` — PR #671 probe, INTENTIONAL
   comparison.

Plus `probe_neutron_gap_round2.py` has an `eval_tr_M_symbolic` HELPER
that parses witness-file rational functions; NOT a call to
hoefsmit_symbolic.tr_M_symbolic.

### Net implications

- **Production mass predictions ARE correct** (using canonical Wenzl
  Markov trace via `_bridge_tr_M`). No 50-99% drift in shipped m_p /
  m_n / m_He predictions.
- The "dual-tr_M discrepancy" was a NAMING bug in one library function
  (`hoefsmit_symbolic.tr_M_symbolic`) that ONE diagnostic script
  (`deuteron_tr_M_symbolic.py`) consumed under the wrong assumption.
- The q-CLT framework on main (`prop:hecke-satisfies-blitvic-hypothesis`,
  `conj:q-clt-non-commutative`, etc.) uses the canonical Markov trace
  as it should — consistent with the production mass chain.

### Updated decision matrix

Of the original three options (A: production wrong, B: paper wrong,
C: both valid for different observables), **the answer is essentially
(A's complement)**: production is RIGHT (canonical Markov), the paper
is RIGHT (canonical Markov), the ONLY issue was the misnamed function
in `hoefsmit_symbolic.py` which is now fixed by the aliases.

The "rewire all production code" task is therefore ALREADY DONE — the
production chain was canonical from the start; only the diagnostic
`deuteron_tr_M_symbolic.py` script needed migration (now complete).
