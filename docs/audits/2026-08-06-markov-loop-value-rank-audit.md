# T3h / `qou-mcwm`: is the Markov loop value $z$ pinned without assuming $N$?

**Date:** 2026-08-06
**Branch:** `claude/eightfold-way-a2-lattice-ijoegv`
**Bean:** `qou-mcwm`, epic `qou-8lxd`
**Predecessors:** [`2026-08-04-chi-A-rank-presupposition-av2.md`](2026-08-04-chi-A-rank-presupposition-av2.md)
(my AV-2 complement) and
[`2026-08-04-ocneanu-trace-parameter-audit.md`](2026-08-04-ocneanu-trace-parameter-audit.md)
(the sibling's T3f), which jointly concluded the rank $N$ is *not derived*
from the Descartes condition and left open whether anything else pins it.

**Answer: no — and that is not the interesting part.** $z$ is nowhere pinned
independently; it is *defined* as the $N=2$ loop value, so no witness can
settle the rank. But the audit shows the rank is nonetheless **empirically
constrained to $N=2$ in the mass sector**, which defuses the
per-observable-$N$ hazard exactly where it mattered.

## 1. $z$ is a definition, not a measurement

The Markov parameter is fixed in the **notation register** — the corpus's
authoritative symbol table
([`notation-register-table3-data.md`](../../content/quantum-observable-universe/notation/notation-register-table3-data.md)):

> $z = 1/(\check q + \check q^{-1})$ — equivalently $1/(q^{1/2}+q^{-1/2})$.

and repeated as a *recall* line in
[`tm-notation.md`](../../content/quantum-observable-universe/appendix-transfer-matrices/tm-notation.md),
`tm-notation-table1-data.md`, `tm-worked-examples.md`,
`tm-heavy-atom-examples.md`, and
[`shell-structure-eigenvalues.md`](../../content/quantum-observable-universe/predicted-spectra/shell-structure-eigenvalues.md).

Writing $\check q = q^{1/2}$, this is

$$
  z \;=\; \frac{1}{\check q + \check q^{-1}} \;=\; \frac{1}{[2]_{\check q}} ,
$$

i.e. **the reciprocal of the $N=2$ quantum dimension, by construction.** For
the $\mathfrak{gl}_N$ specialisation the loop value is $[N]_{\check q}$ and
the parameter is $1/[N]_{\check q}$. The corpus writes the $N=2$ member of
that family and never the family.

**The numerical value is derived, not measured — and it is *wrong*.**
[`q-beta-spectral-bridge-table-data.md`](../../content/quantum-observable-universe/nuclear-interactions/q-beta-spectral-bridge-table-data.md)
records $z = 0.499320334033598$. Recomputing $1/(q_0^{1/2}+q_0^{-1/2})$ at
**65 dps** (repo default) from the canonical 50-digit muon-pinned
$q_0 = 1.10997859555733471989976322048322502665620840878015368660798114614493$
gives

$$
  z_{\text{exact}} = 0.4993203340335612717689664\ldots
$$

against the committed $0.4993203340335\,\mathbf{98}$ — a relative
discrepancy of $7.36\times10^{-14}$, i.e. **73.6 ppQ, exceeding the L1
internal-agreement goal of $\le 1$ ppQ by $\approx74\times$.**

Three candidate explanations, all tested at 65 dps:

| hypothesis | result |
|---|---|
| computed at the **proton** pin instead of the muon pin | **rejected** — an 11.5 ppb shift in $q_0$ moves $z$ by $3\times10^{-10}$ relative, ~4000× larger than observed |
| **float64** evaluation of the same formula | **rejected** — float64 gives $0.49932033403356124$, matching the exact value to $6.4\times10^{-17}$; float64 is *fine* here and does **not** reproduce the committed digits either |
| computed from a **stale / lower-precision $q_0$** | **consistent** — the $q_0$ that reproduces the committed $z$ exactly is $1.10997859555420\ldots$, differing from canonical at the 12th digit ($2.8\times10^{-12}$ relative) |

So the committed value most likely descends from a superseded or
under-converged $q_0$ — the q₀-repin staleness class. Filed as a bean; **it
does not affect this audit's conclusions**, which concern the *form* of $z$,
not its 14th digit.

**It does, however, sharpen §1's conclusion.** A 74-ppQ error sitting
uncaught in a committed table is itself evidence that **nothing independently
constrains $z$**: had any measurement or cross-method check bound it, the
discrepancy would have surfaced. A quantity that can be wrong at the 14th
digit without consequence is a quantity nothing is checking.

**Verdict on the bean as posed:** no witness, no normalisation, and no
computed value in the corpus pins $z$ independently of $N$. Every occurrence
presupposes $N=2$. The rank question **cannot** be settled by auditing
existing $z$ values.

## 2. The rank *is* empirically constrained — just not derived

Rewriting the same definition at other ranks, at the **same** $q_0$:

| $N$ | $[N]_{\check q}$ | $z = 1/[N]_{\check q}$ | shift vs $N=2$ |
|---|---|---|---|
| **2** (corpus) | 2.002722364 | **0.499320334** | — |
| 3 | 3.010896869 | 0.332126952 | **−33.5 %** |
| 4 | 4.027268132 | 0.248307281 | −50.3 % |
| 6 | 6.095698514 | 0.164050108 | −67.2 % |

$z$ is **observable-facing**: it enters the transfer matrices
(`tm-interactions`), the nuclear Skein polynomial (`tm-notation`), the shell
eigenvalues (`shell-structure-eigenvalues`), and the $Q_\beta$ spectral
bridge (`q-beta-spectral-bridge`) — quantities checked against CODATA/AME at
the ppb-to-sub-percent level. A **33.5 %** shift in $z$ would not perturb
those predictions, it would destroy them.

So the honest status of the rank in the mass sector is a third thing,
distinct from both "derived" and "chosen":

> **$N=2$ is not derived, and it is not free. It is *empirically pinned* in
> the mass sector, because $z$ feeds checked predictions and $z$ moves 33 %
> between $N=2$ and $N=3$.**

A clean way to see the rank inside the number: as $q\to1$, $[N]_q \to N$, so
$z \to 1/N$. The corpus value $z \approx 0.4993 \approx \tfrac12$ displays
$N=2$ directly, with the $0.14\%$ excess over $\tfrac12$ being the
$q_0$-deformation.

## 3. This defuses the §5 hazard — in one sector only

My AV-2 complement §5 warned that permitting each observable its own $N$
would hand the framework **one free integer per observable**, making it less
falsifiable, and demanded a *selection rule* fixed independently of the
observable being predicted.

§2 supplies exactly such a rule for the mass sector — and it is the right
kind, because it is a **consistency constraint across many observables at
once**, not a per-observable tuning: one $z$ feeds transfer matrices, shell
structure, and $Q_\beta$ simultaneously. Picking $N$ per observable there is
not merely disallowed by policy; it is arithmetically impossible without
breaking the others.

**The hazard is not retired globally.** It is retired **only** where $z$
feeds a checked prediction. A sector that does not consume $z$ — a purely
topological knot invariant, a flavour multiplet structure — remains free, and
the §5 gate still applies there unimpaired.

## 4. Consequence for flavour / colour $\mathrm{SU}(3)$

This sharpens, rather than reopens, the earlier conclusion:

- **Not in the mass pipeline.** That evaluation is locked at $N=2$ by §2. A
  $\mathfrak{gl}_3$ reading of the *same* trace would move $z$ by a third and
  break the mass chain. This is now a quantitative statement, not a
  structural intuition.
- **Possibly in a different evaluation.** HOMFLY-PT is one object with $N$ an
  evaluation index (the corpus's own
  $\{P(K;q_0^{N-1},h_q)\}_{N\ge2}$ framing). An $N=3$ reading that does
  **not** feed the mass chain is untouched by §2 — but it then owes the §5
  gate an independent selection rule of its own, and none exists.

So the live question is unchanged in substance and sharper in form: **what
selects $N=3$ for a flavour sector, given that $N=2$ is pinned for the mass
sector by consistency across checked observables?** Nothing in the corpus
answers it, and inventing a per-sector $N$ without such a rule remains an
anti-fit violation.

## 5. Scope

Scope-(a) throughout. Nothing here derives a rank, refutes $N=3$ in any
sector, or is wired to production. The §2 constraint is an **empirical**
consistency observation about existing checked predictions — evidence tier,
strictly below a derivation, per the framework's own tiering. The claim that
$z$ is a definition (§1) is a documentary fact about the notation register,
verifiable by reading it.

Arithmetic: all values computed with `mpmath` at **65 dps** (repo default
compute precision) from the canonical 50-digit muon-pinned $q_0$ — no
float64 anywhere. The $N$-family table is exact at that precision; the
committed-value discrepancy of §1 is a genuine 73.6 ppQ disagreement, not a
rounding artefact, with the three candidate causes tested and two rejected.
