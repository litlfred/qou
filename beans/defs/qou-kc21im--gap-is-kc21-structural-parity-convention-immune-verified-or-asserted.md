---
# qou-kc21im
title: 'GAP: is KC21''s "structural parity is convention-immune" VERIFIED or asserted? c_3(q) is DEFINED BY the C-frame extractor'
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T15:05:00Z
updated_at: 2026-10-04T15:10:58Z
parent: qou-avtq
---

## The question

PR #5107 (merged 2026-08-15) audited the c_3 refutation chain against the
C→D trace-convention change and correctly split the findings:

- **value layer → C-conditional** (c_3 ≈ −2.07 under C, ≈ −974 under D;
  (H1), `[3]_q/25`, `J−ℏ²`, `S_leak`, `q*_S`, the D-ladder constants, and
  even the "canonical" c_2 = −1 are all C-frame statements);
- **structural layer → claimed convention-IMMUNE.** The registry note added
  to KC21 (§9g) says: *"the structural parity statement (`S(−ε) = −S(ε)`)
  and the `1/u³` result are convention-immune"*.

**This bean asks whether that second claim was verified or asserted.**

## Why it is not obvious

The bar-parity argument is a statement about the **function** `c_3(q)` (and
its odd part `S`): with `q = q₀ + iε`, `S(−ε) = −S(ε)`. But `c_3(q)` is not a
convention-free object — it is *defined by* the extractor, whose N=1 rung
consumes the convention-C Markov parameter (`α = (z−1)h/2`,
`qbeta_utils.py:124-125`). Under D the extractor returns a numerically and
structurally different function (c_3 ≈ −974; rung convergence 58× → 1.12×).
The parity of function `f_C` does not transfer to function `f_D` merely
because both are called "c_3".

Compare the neighbouring, *checked* immunity claims from the same audit —
the anchor-swing mechanism and the entropy bound were shown immune **because
their inputs (`u`, `Q_A`, σ) are z-free**. The parity claim has no analogous
z-free-input demonstration on record; `S = h·D(ũ)` runs through the ladder
that #5107 itself marks C-conditional in the same registry sentence.

## What would settle it

1. **Re-derive the parity under D.** Extract `c_3^D(q)` with the D parameter
   and test `S^D(−ε) = −S^D(ε)` symbolically (sympy exact / mpmath 60 dps,
   proton pin) — the same shape of test #5107 ran for the swing ratio.
2. **Or exhibit the z-free reduction.** If the parity follows from
   `fig8Trace_im_odd` + `fig8Trace_im_real_zero` (both proved-lean) with no
   z-bearing input in between, write that dependency chain out explicitly;
   that *is* the immunity proof and the claim stands as stated.
3. Update KC21's §9g note to the tiered outcome (`verified-immune` /
   `C-conditional`) in the `.md` **and** the JSON twin; run
   `kernel_constraints_registry_validate.py` (R6 now guards twin drift).

## Interaction with the new `disputed` registration

Bean `qou-b3nk` (PR #5111) proves the decay ladder's `z_C` fails the
**full-bar condition** `bar(z) = z − h` away from `q² = 1` (`z_C` is
bar-EVEN; `z_D` satisfies it). So the C-frame trace does **not** commute with
the full bar involution. That does not by itself invalidate fibre-variable
parity bookkeeping (`ZBarParity`'s z-alone exclusion is pure algebra in `q`
and survives), **but it removes the obvious reason to expect trace-derived
quantities to carry clean bar parity** — which is precisely what `S`'s
odd-part claim asserts. The two questions should be answered together.

## Discipline

Not a refutation — scope-(a) at most until tested. Per §"Defined residual ≠
derived decomposition": `S` is a residual of a C-frame extraction, so its
parity is a property of that extraction until shown otherwise. Do not flip
any registry tier on assertion in either direction; the honest interim label
is "immunity claimed, not yet audited".

Raised by the session that ran the #5107 redirect, on reading the audit's own
logic back against the sentence it added to KC21.

## Findings — 2026-08-15 (PR #5123, branch `claude/kc21-parity-immunity-audit-2026-08-15`)

**Answer to the bean's question: it was ASSERTED. It is now VERIFIED.** Both
of the listed routes closed, and they agree.

### Route 1 — re-derived under D (probe A3/A4/A5/A6)

`Im c₃^D(q₀−iε) = −Im c₃^D(q₀+iε)` and `Re` even, to `1e-45` relative over
`ε ∈ [10⁻³⁰, 10⁻²]`, non-vacuously (`Im c₃^D(q₀+10⁻⁸i) = 0.0385845 ≠ 0`) —
while the C→D reframing moves the value by 972, i.e. **470× |c₃^C|**.

*Trap for anyone re-running this:* `qbeta_utils` writes `Q_A` with
`mpfabs(q²−2q−1)`. `abs` is not holomorphic, so a complex-ε probe that keeps it
tests a different function. At `q₀` the argument is negative, so the analytic
branch is the signed `(2q+1−q²)` — what the exact-series ladder already uses.

### Route 2 — the reduction, and it is stronger than the bean anticipated

The bean asked for a chain with "no z-bearing input in between". The truthful
chain is different and better: **`z` does intervene — it just cannot matter.**

The parity is **Schwarz reflection**. Its only hypothesis on the Markov
parameter is that `z` be *real-valued on the real q-axis* near `q₀`; it never
reads `z`'s formula. Every ingredient (`h`, `ℏ_q`, `b`, `u`, `Q_A`, `z_C`,
`z_D`, `cos`) is reflective, and the class is closed under the field operations
and composition. Decisive check (A10): a control convention `z_X = q/(1+q²)`,
present in **no** channel, has the parity too. So immunity is a property of the
class, not of C-vs-D — it extends to conventions nobody has written down.

Formalized sorry-free (`lean`-direct exit 0, no `sorryAx`) in
`QOU/QBeta/LadderParityReflection.lean`, quantified over conventions:
`alphaPhase_im_odd_of_reflective_markov`, with `zD_reflective` the concrete D
instance. The C instance needs the principal `√` branch (outside that file's
algebraic scope) and is measured at 60 dps instead — said so in the docstring.

### Two corrections the verification forced

**1. The literal statement is FALSE.** `S(−ε) = −S(ε)` read of the full complex
value requires `Re S` to equal its own negation. Measured: `Re S = −0.0394593`
at the proton pin (the corpus's own `S(proton)`), `|S(−ε) − (−S(ε))| = 0.0789`.
The true statement is about **`Im S`** / the decay projection. Registry
corrected; `reflective_re_even` makes the failure a theorem rather than a note.

**2. The parity is NOT evidence for bar-oddness — this is the finding with
downstream consequences.** KC21 and the 2026-07-12 capstone both derive it as
*"bar-odd ⇒ odd in ε"*. That is not the implication the Lean proves:
`ImQDecayLinearResponse`'s chain is `fig8TraceC_conj` — **real integer
coefficients** ⇒ conjugation commutes ⇒ `Im` odd in `ε`. `σ: q↦q⁻¹` never
appears. Measured consequence (A11): the manifestly bar-**even** `Q_A` has the
identical `ε`-parity. Every real-analytic ingredient of the ladder has it, so
observing it in `S` does not discriminate the bar-odd channel.

*"The sign-flip is structural, not a fit, because `S` is bar-odd"* should read
*"…because `S` is real-analytic in `q`"* — a far weaker premise, satisfied by
essentially everything in the ladder.

### Interaction with `qou-b3nk` / PR #5111 — sharper, not resolved

The bean flagged that #5111's `z_C` full-bar-condition failure "removes the
obvious reason to expect trace-derived quantities to carry clean bar parity",
and asked that the two questions be answered together. They are **not** the
same question, and this audit only answers one:

- **complex conjugation** (`q₀+iε ↦ q₀−iε`) — settled, immune, above;
- **the bar involution** (`σ: q ↦ q⁻¹`) — **untouched**. `bar(z_D) = q⁻⁴·z_D`
  and the `z_C` full-bar-condition failure stand exactly as stated, and **the
  `h·D(ũ)` bar-split inherits none of the ε-parity's immunity.**

Correction 2 makes the bar question **more** pressing: the ε-parity had been
doing evidential duty for the bar-odd reading, and it turns out not to bear on
it at all. So the bar-parity half of KC21 now rests on the `S = h·D(ũ)` split
alone — which §9g already marks C-conditional at the value level, and which per
§"Defined residual ≠ derived decomposition" is a residual of a C-frame
extraction to begin with.

### Left open (candidate follow-up, not opened as a bean here)

Whether `S` is bar-odd **at all** under D — i.e. whether the `h·D(ũ)`
factorization with `h` bar-odd and `D` bar-even survives the C→D flip, given
that `z_D` is not bar-even. That is a separate symbolic test from anything run
here, and it belongs with `qou-b3nk`'s channel-convention question rather than
with this bean.

### Artifacts

| kind | path |
|---|---|
| probe | `computations/qbeta/qbeta_kc21_parity_convention_immunity_probe.py` (12/12, exit 0) |
| witness | `computations/qbeta/qbeta-kc21-parity-convention-immunity.witness.json` |
| Lean | `content/quantum-observable-universe/lean/QOU/QBeta/LadderParityReflection.lean` |
| registry | `docs/coordination/ck-dk-canonical-registry.md` §9h + KC21 row; JSON twin |
| audit | `docs/audits/2026-08-15-kc21-parity-convention-immunity-audit.md` |
| ledger | `docs/coordination/1ppq-qbeta.md` |

Adjacent, drained on the way: the NO-FLOAT64 ratchet's NEW-dirty count went
**2 → 0** (a `round()` raw float64 in this probe and one left by the #5107
probe, both fixed at the producer). Left standing and not from this branch:
`rho-k-co-casimir-extended.witness.json` REGRESSED 3 → 4.

**Not closed** — closing is human-only. Awaiting owner review of the two
corrections, particularly correction 2, which weakens an evidential claim the
corpus has been relying on.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-15 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
