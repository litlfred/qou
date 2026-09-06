# Corpus sweep: "non-holonomic ⇒ resurgent" — 5 sites, and three committed witnesses in three different states

> **⚠ CONVENTION-C CONDITIONAL — scope note added 2026-09-06 (bean `qou-h6o3`).**
> This document's conclusions depend on the `c_k` precision ladder / `Q_β`, which
> AGENTS.md records as **convention-C-frame throughout and NOT re-derived** under
> the owner ruling of 2026-08-15 making convention D (`z = q³/(q²+1)`) canonical.
> Treat every `c_k`-dependent statement below as **C-conditional** until the
> ladder is re-derived (bean `qou-cds1`). The numbers here are correct *for C*
> and are kept as recorded — they need **scoping, not correction**. This note was
> applied mechanically to the 45 documents in this arc that reference the ladder;
> it asserts dependence on the ladder, not that any particular conclusion changes
> under D.


**Date:** 2026-08-14 · **Bean:** `qou-arvu` (spun out of `qou-tdp0`, PR #5032) ·
**Tier:** documentation audit · **Scope:** (a) throughout — an inference step
does not license its conclusion; **no** ingredient is excluded, no producer
re-run, no witness written, no `c_k` wired, no tier change.

## The step being swept for

> `D(ũ)` has no (q-)holonomic recurrence, **hence** it is transcendental /
> resurgent (Écalle class).

**Non-holonomic does not imply divergent, and only a divergent series can be
resurgent.** A non-holonomicity result constrains the *algebraic* class; it says
nothing about the *growth* class. The counterexample is the object under
discussion: KC22's own closed form

    D(w) = φ(w)·log(1 − w/ρ) + ψ(w),   φ, ψ algebraic over a degree-12 field

is **convergent** (`ρ = 0.142799996644689…`, `κ = 0`) *and* provably not
low-order P-finite. KC22 states this in as many words, one row from where the
bad inference sat.

This is **distinct from** the 2026-08-09 convergence correction. That withdrew a
conclusion drawn from a divergence that turned out to be absent. This step would
have been invalid **even if the ladder had diverged**.

## Method

Candidate files = mention a non-holonomicity term (`non-holonomic`, `not …
holonomic`, `P-finite`, `A-polynomial recurrence`) **and** a growth-class term
(`resurgent`, `transseries`, `Écalle`, `Borel`, `divergent`, `Gevrey`) — 22
files across `docs/`, `content/`, `computations/`, `.beans/`. Then a
whitespace-flattened proximity pass (±260 chars) requiring an inference
connective (`hence`, `so`, `therefore`, `thus`, `⇒`, `implies`, `consequence`).

## Findings — 5 sites, in two classes

### Class (a) — the invalid step, or a conclusion it produced

| # | site | what it says | disposition |
|---|---|---|---|
| 1 | [`2026-07-12-dladder-divergence-correction.md`](2026-07-12-dladder-divergence-correction.md) | **title asserts** "super-exponentially DIVERGENT (radius → 0), not convergent"; `ρ≈0.143` called "a finite-n shadow" | **SUPERSEDED banner added** |
| 2 | [`2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md`](2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md) | negatives "tighten the resurgent reading"; closed form "is transcendental / resurgent" | **banner + 2 clauses struck** |
| 3 | `qbeta_dladder_generating_function_structure_probe.py` | computes `divergent = …`; docstring: "SAME divergent family as the κ-tower" | **BEANED** — see below |
| 4 | `qbeta_odd_channel_stokes_borel_probe.py` | premise: "characterize the divergence class of the bar-ODD D-ladder" | **BEANED** |
| 5 | `qbeta_dladder_coupled_qsqrt3_recurrence_probe.py` | docstring: NEGATIVE "corroborates the q-Gevrey/resurgent reading" | **BEANED** |

### Class (b)/(c) — correct as written, left alone

- [`2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md`](2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md)
  — **the authority.** Already says "a convergent analytic function need not be
  holonomic" and "what falls is only KC22's *inference*".
- `docs/coordination/1ppq-qbeta.md` — fixed in PR #5032.
- `.beans/qou-qb8e` — *quotes* the old KC22 text as a record of what was
  superseded; it is reporting, not asserting.
- The **Ohtsuki κ-tower** resurgence work throughout — that ladder **is**
  genuinely divergent (Gevrey-1; ratios 1.32→3.63→4.93; Borel singularity
  `A ≈ 0.7`). Correcting the route must not be read as withdrawing it. The
  ledger already carries this as a proved scope-(b) result: a divergent and a
  convergent series cannot be equated term-by-term.

## The escalation: three committed witnesses, in three different states

Sites 3–5 are **producers**, not prose, and **all three have committed
witnesses** (verified by `scriptFile` match + `git ls-files`). They are not
equally affected, and the difference matters for whoever fixes them:

### 1. Refuted verdict — `qbeta-dladder-generating-function-structure.witness.json`

- `data.super_exponentially_divergent = **true**`
- `data.verdict`: *"super-exponentially DIVERGENT (radius → 0) … the SAME
  resurgent family as the κ-tower … the earlier 'convergent ρ≈0.143' was a
  finite-n shadow"*

Every clause of that was reversed on 2026-08-09. This is the one that genuinely
asserts something refuted.

### 2. Refuted framing, **corroborating data** — `qbeta-odd-channel-stokes-borel.witness.json`

Its heading calls it the odd-channel *"divergence class"*, but its own
measurements point the other way:

- `data.gevrey_order_drifts_down = **true**` — the effective Gevrey order `C`
  falls `~0.08 → 0.05` as the tail lengthens, i.e. the apparent divergence
  **weakens** with more terms, which is what a *non*-divergent series does to
  this diagnostic;
- the description already records *"NOT q-Gevrey-1 in any base > 1"*;
- the fixed-order Borel–Leroy pole runs `0.147 → 0.165 → 0.249` for
  `s = 0.02 → 0.10 → 0.30`, so the small-`s` end sits at **0.147** — within
  ≈ 3 % of `ρ = 0.142799996644689…`, and trending toward it as `s → 0`.

**Scope-(a), stated carefully:** this is an observation that the recorded
numbers are *consistent with* the 2026-08-09 radius, not a derivation of `ρ`
from them. But it means this witness's data was pointing at the true radius
while its framing called the channel divergent. Re-scoping it is mostly a
relabelling job, and the numbers become supporting evidence rather than
contradicted ones.

### 3. Verdict correct, only the description carries the bad step — `qbeta-dladder-coupled-qsqrt3-recurrence.witness.json`

- `data.verdict = "NO coupled ℚ(√3) P-recurrence up to (r≤4, D≤4) at this ORD"`
  — a pure non-holonomicity result, **correct and unaffected**.

Only the surrounding `description` carries the invalid step, *"NEGATIVE ⇒ …
(corroborates the q-Gevrey/**resurgent** reading)"*. The measurement stands; the
gloss on it does not. This is the cheapest of the three to fix and the one least
at risk of being over-corrected.

> **Count correction (2026-08-14).** An earlier revision of this document and of
> `qou-arvu` said *"two committed witnesses"* and named only one file. Both were
> wrong: there are **three**, and they are in three different states. Caught in
> review on PR #5039. Noted here because an unverified count in an audit about
> unverified claims is the same defect one level up.

**Re-running does not fix it, and that is the important part.** The probe's
arithmetic is not in question: at `k ≤ 21–27` the root test really does rise
without plateau and `C > 0` really does fit. The *diagnostic* misfired. With the
true behaviour `d_k = −(1/(2h*_ρ))ρ^{−k}/k(1+O(1/k))`, the `1/k` factor makes
`|d_k|^{1/k}` approach `1/ρ` far too slowly to plateau in the available window,
and the `log` branch point makes a Domb–Sykes `1/k` fit noisy. So the verdict
needs **re-scoping at the producer**, not recomputation — and that is a code
change requiring a re-run to propagate into the witness.

**Why it was not done here.** `sympy` is absent in this sandbox, so these
producers cannot be run and their witnesses cannot be regenerated. Editing a
producer's docstring would drift `scriptHash` and leave a stale witness with no
way to refresh it — the exact failure mode AGENTS.md §idle-backlog warns about.
Recorded precisely instead: **bean `qou-arvu`**, which carries the file list, the
offending strings, and the reason re-running is not the fix.

## What is NOT claimed

Scope-(a). Nothing here excludes q-Borel or Écalle methods from any object. The
κ-tower's resurgence stands; `qou-vkg5` (C1 at `∞` — irregular, slope `½`)
stands. Two things share the word "Écalle" and have opposite regularity, and the
recurring failure in this arc is treating them as one.

Nor is the 2026-07-13 audit's *content* withdrawn: its exact linear algebra —
no coupled `ℚ(√3)` P-recurrence, no q-holonomic recurrence in base `3`/`1/3`/`k`,
the 2-adic parity grading — is untouched and correct. Only the interpretation
layered on it is.

## Pattern note

This is the **fourth** instance today of one shape: a correction applied to one
site and not propagated to the summaries and consumers that restate it.

1. §3 of the registry out-ran KC22 (PR #5022)
2. the 1ppQ ledger never received the correction at all (PR #5032)
3. my own blockquote header out-ran its own body (PR #5032, caught in review)
4. the 07-12/07-13 audits and three producers still carry the pre-correction
   reading (this sweep)

The corpus-grep discipline in AGENTS.md exists because agents trust status
lines. The cheap structural defence is the one the 2026-08-09 document already
practises: name, in the correcting document, every downstream site that must
move — and check them off.
