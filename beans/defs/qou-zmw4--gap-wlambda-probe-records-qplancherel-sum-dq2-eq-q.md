---
# qou-zmw4
title: 'GAP: wlambda probe records qplancherel_sum_dq2_eq_qfact=False and has reported allPassed=true over it since 2026-07-02'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T14:34:13Z
updated_at: 2026-10-11T07:45:50Z
parent: qou-cdx1
---

Surfaced while draining `qou-srvu` slice E (subdirectory witnesses).

## The measurement

`computations/substrate/wlambda-identity-i-structure-probe.witness.json` on
`main`, computed **2026-07-02**, carries in its own `results`:

    qplancherel_sum_dq2_eq_qfact: false
    allPassed: true
    assertions: []

A recorded FAILED identity check, inside a witness reporting green, for two
months. Nothing noticed because `all([]) is True` and no consumer reads the
flag. Draining the witness (PR branch `claude/srvu-drain-e-2026-08-30`) made it
visible: the probe now emits 5 assertions, 4 pass, this one fails, and
`allPassed` is honestly `false`.

The check is `sum_lambda d_q(lambda)^2 = [n]_q!` — the identity that makes
`sum_lambda W_lambda = 1`, i.e. that `W_lambda` is a probability measure at
all. The probe is `auditOnly: docs/coordination/s5-so3-keystone.md`.

## What is MEASURED, and what is NOT

**Measured.** The flag is false; it has been false on `main` since 2026-07-02;
and from the witness's OWN recorded `W_lambda` at n = 3, exact sympy gives

    sum_lambda W_lambda = q(q^4 + 4q^2 + 1)/((q^2+1)(q^2-q+1)(q^2+q+1))

which is exactly **1 at q = 1** but **22/35 at q = 2** — not identically 1.

**NOT established.** Whether this refutes the q-Plancherel identity, or whether
this probe's `dim_q`/`qfact` normalisation is off by a power of `q`. The second
is a common slip and is *consistent with* the value being exactly 1 at q = 1,
but it is **not confirmed**. This is a scope-(a) observation about ONE probe,
not a claim about the mathematics, and it is deliberately not written into any
durable verdict.

## The actionable pointer (corpus-grep path 6)

Bean `z3a2` records that on 2026-06-28 this probe was migrated to take
`qint`/`qfact`/`dim_q` from the shared `young_qdim` module, keeping the
classical SYT/hook combinatorics local, and states the witness came out
**BYTE-IDENTICAL**. This witness's `computedAt` is 2026-07-02, i.e. AFTER that
migration — so the false flag is **not** a regression introduced by it; it
predates and survives it.

So the first place to look is `young_qdim.dim_q`'s normalisation convention
against the `[n]_q!` that `qfact` returns, and against the classical `f_lambda`
this probe kept local. The n = 3 arithmetic above is a two-line reproduction.

## Next honest step

Decide which of the two it is, then either fix the normalisation (and the flag
goes true) or record a scoped negative naming the invariant that fails. Do NOT
close it by deleting the check.


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

A probe recording `qplancherel_sum_dq2_eq_qfact=False` while reporting
`allPassed=true`. A probe that passes while its own field records a failure is
a reporting defect independent of convention. Live.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.

## 2026-10-11: the (a)/(b) fork is SETTLED — the corpus PROVES the check is false

This bean's "next honest step" is *"decide which of the two it is"* — (a) the
identity genuinely fails, or (b) this probe's `dim_q`/`qfact` normalisation is
off by a power of `q`. **It is (a), and it is proved in Lean, not merely
measured.**

[`QOU/MathlibExt/MolienFakeDegree.lean`](../../folio/quantum-observable-universe/lean/QOU/MathlibExt/MolienFakeDegree.lean)
carries **`sum_qDim_sq_ne_qFactorial_n3_at_two`** — sorry-free (the only
`sorry` in the file is the word inside a docstring) — stating exactly
`Σ_λ qDim q λ² ≠ qFactorial q n`, **at `n = 3`, `q = 2`**: the very datapoint
this bean recorded. Its module docstring names the contrast deliberately:
*"The contrast is proved too … which is the whole of the `Z(n)` defect
measured."*

**So the flag is CORRECT and must stay**, exactly as this bean says (*"Do NOT
close it by deleting the check"*). The probe is reporting a proved
non-identity. What was wrong was only the *reporting* — `all([]) is True` — and
that is already fixed: the witness was regenerated **2026-09-05** and now
carries 5 assertions, 4 passing, `qplancherel_sum_dq2_eq_qfact` failing, and
`allPassed: false` honestly.

**Option (b) is excluded**, and not by argument: a normalisation slip in *this
probe* cannot make a Lean theorem about `qDim` false.

### Reproduced, with the harness calibrated against this bean's own number

Using `computations/substrate/young_qdim.py` (whose `qint` is the **symmetric**
`(q^k − q^-k)/(q − 1/q)`, which is the convention that matters here):

    sum_lambda dq^2 / [3]_q!  at q=2  =  22/35      <- exactly this bean's recorded value

My first attempt used the **classical** `[m]_q = 1+q+…+q^{m-1}` and got `11/21`,
which matches nothing here. Switching to the corpus module reproduced `22/35`
and only then was anything trusted.

### 🛑 And it turned up TWO errors in AGENTS.md §7aa, both now fixed

§7aa pointed at *"the Molien `f^λ dim_q(λ)`, which sums to `[n]_q!` exactly
(Lean, sorry-free, all `n`, all `q>1`)"* — the sentence it uses to justify
sending **cross-atom consumers** to `d_q²/D²`. Measured against the Lean:

1. **It omits a per-partition `q^{−κ_λ}` factor.** The theorem is
   `Σ_λ f^λ · q^{−κ_λ} · dim_q(λ) = [n]_q!`, and at `n=3` it writes the weights
   out as `q^{-3}, 1, q^{3}` on `[3], [2,1], [1³]`. Verified symbolically:
   **with** the factor `LHS − RHS` simplifies to **0**; **without** it — as
   §7aa stated — the ratio is **8/15 at `q = 2`**. So the identity as written
   in AGENTS.md was simply false, which is why my own first check of it failed.
2. **It is not proved for all `n`.** The file has three separate explicit
   theorems `molien_qanalogue_n2` / `_n3` / `_n4`, each a written-out finite sum
   rather than a `Finset.sum`. The general-`n` case is **open** and the file
   says what is missing — *"the graded decomposition of the coinvariant algebra
   (Chevalley/Steinberg) plus an induction over `Finset`-many partitions"* —
   tracked as bean `qou-3quc`, *"rather than faked with a `sorry`"*.

Both corrected in AGENTS.md §7aa in the same commit. `qou-oots`'s open question
(is `dim_q²` the right numerator?) is **unaffected** — if anything it is now
better posed, since its comparator is a three-`n` result with a `q^{−κ}` weight
rather than an all-`n` identity.

**Status: `todo` → `completed`.** The fork is settled, the flag is correct and
staying, and the reporting defect was fixed a month ago. Nothing here is an
open conjecture: `qou-oots` and `qou-3quc` own what remains open.
