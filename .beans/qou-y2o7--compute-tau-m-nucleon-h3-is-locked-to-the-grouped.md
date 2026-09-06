---
# qou-y2o7
title: compute_tau_M_nucleon_H3 is locked to the grouped ordering by its monotone-only chi kernel; 18 consumers inherit it
status: in-progress
type: bug
priority: normal
created_at: 2026-09-06T11:12:06Z
updated_at: 2026-09-06T11:31:45Z
---

## The mechanism

`closed_form_tau_M.compute_tau_M_nucleon_H3` does not call
`atom_braid_word_3A`. It builds its own word from the `hecke_core` chains:

```python
# The chain is (c, d, gen) and MONOTONE (all gen 0, then all gen 1),
# which is what `chi_all_lambda` requires.
word = [(mpf(c), mpf(d), 0) for c, d in g0] + \
       [(mpf(c), mpf(d), 1) for c, d in g1]
```

The comment states the cause outright. `chi_monotone_transfer.chi_all_lambda`
is the **monotone-only** transfer kernel, so the word has to be monotone, so
the generators are emitted grouped. The 2026-09-05 owner ruling (`qou-hu1f`)
says the canonical intra-nucleon core is **borromean**, `(σ₀σ₁⁻¹)³`, which is
non-monotone by construction:

    grouped   (as built here)   gen sequence [0,0,0,0,0,0,0,1,1,1,1]
    canonical (atom_braid_3A)   gen sequence [0,1,0,1,0,1,0,0,1,0,0]

This is not a stale constant that a re-run fixes. The function **cannot
express the canonical word** while it uses that kernel.

## Measured

At the proton pin, 50 dps, via `chi_general_word.chi_all_lambda_any` (the
dispatcher, which accepts both):

| | grouped (shipped) | canonical (ruling) | ratio |
|---|---:|---:|---:|
| τ_p | 1.145759692457300869689 | 0.629328402202921918165 | 1.8206 |
| τ_n | 0.987743688115809571634 | 0.475133517155682212506 | 2.0789 |

Cost is not the obstacle: at H₃ the general kernel is `d_λ ≤ 2`, sub-second.
Swapping `chi_all_lambda` → `chi_all_lambda_any` and the hand-built word →
`atom_braid_word_3A(1,0)` / `(0,1)` reproduces the canonical column exactly.
I verified this; I have **not** applied it (see scope below).

## Blast radius — 18 consumers

`legacy_marshalled_frame`, `nucleus_sdp_assembly`,
`per_knot_mass_table_demonstration`, `binding_channel_taxonomy_probe`,
`deuteron_from_scratch_ledger`, `probes/gap_a4_He3_residual_probe`,
`probes/nucleon_h3_marshalling_divergence_probe`, `probes/gap_a4_S_K_additive_probe`,
`probes/gap_a4_T2_per_knot_vol_probe`, `probes/gap_a4_L1_light_series_probe`
(+ `_perknot_rerun`), `probes/binding_triangle_3body_cluster_probe`,
`mass_table_comprehensive`, `binding_color_vs_charge_tn3he`,
`atomic_tr_m_helium4_canonical`, `qbeta/qbeta_delta_vs_deltaTbeta_settled_probe`,
`binding_channel_saturation_probe`, `closed_form_tau_M` itself.

Several feed published mass/binding tables. The reference witness the
docstring validates against — `habiro-coefficients-atomic.witness.json`,
τ_p = 1.14575969245730087 — is itself grouped-era, so the whole cluster is
*internally consistent* in the superseded ordering. That is why no
cross-check caught it.

## Why the qou-hu1f sweep missed all of it

Same selector gap as `binding_canonical`: the sweep selected witnesses whose
producers reference `atom_braid_word_3A` by name. This subsystem reaches the
nucleon braid through `hecke_core._PROTON_G0/_G1` instead, so it was invisible.
Two independent subsystems have now been found this way; the selector, not the
individual producers, is the thing to fix.

It is also a `word-provenance-gate` defect in spirit — a word built by hand
rather than obtained from its producer — but the gate looks for literal integer
lists and this is assembled from named constants, so it does not fire.

## Independent confirmation that borromean is the right target

Three structurally independent routes to canonical |tr_M(⁴He)| agree exactly
once borromean nucleon inputs are used (`qou-hft3`):

    Wenzl bridge on atom_braid_word_3A(2,2)   0.0112374176597674215641995493744
    markov_trace_canonical (binding_canonical) 0.011237417659767421564199549374…
    closed_form_tau_M, bring_color_weighted    0.0112374176597674215641995493744

The third is `closed_form_tau_M` **fed borromean τ_p, τ_n by hand**. Fed the
grouped values this function supplies, it returns 0.16097414544240738 — off by
14.325, which is exactly (1.8206)²·(2.0789)². So the closed form is correct and
its inputs are not.

That comparison also discriminates the pn convention independently:
`bring_color_weighted` matches to 30 digits while `chi_lambda_braid` /
`uniform` give 0.013547 (20 % off), confirming the owner's 2026-08-15 R3
ruling from a direction that did not assume it.

## Scope — deliberately not fixed here

Changing this moves numbers in 18 producers and contradicts a reference witness.
That is a subsystem-wide ruling application and an owner call, not a side effect
of a helium-4 fix. What I did instead: `atomic_tr_m_helium4_canonical.py` alone
is corrected at its call site, because its published value is *labelled
canonical* and is 14.3x wrong.

**Decision needed:** apply the ruling across this cluster (swap the kernel,
take the word from its producer, regenerate the 18 + the habiro reference), or
record a documented reason the nucleon H₃ blocks stay grouped.


---

# Options (2026-09-06) — what the decision actually is

**One question:** does the 2026-09-05 intra-ordering ruling apply at **A = 1**,
to the single-nucleon H₃ block?

Everything else follows. The ruling changed `atom_braid_word_3A`'s `intra_order`
default to `borromean` on the stated ground that *σ₀ and σ₁ do not commute and
only the alternating word is β_Bor*. At A = 1 that argument is not weaker — the
nucleon word's core **is** `(σ₀σ₁⁻¹)³`. I can find no reading on which the
ruling holds for the assembly but not for the block it is assembled from.

## What has changed since this bean was opened

Three things that make the options cheaper and clearer than first recorded.

**1. Both canonical entry points already honour the ruling.**
`atom_braid_word_3A` and `canonical_braid_crossings.atom_canonical_crossings`
both default to `intra_order="borromean"`. Nothing is structurally locked to
grouped except `compute_tau_M_nucleon_H3`, which bypasses both and builds its
own word.

**2. The habiro reference is stale, not load-bearing-by-construction.**
`habiro-coefficients-atomic.witness.json` carries the whole grouped chain
(p 1.14575969, n 0.98774369, D 0.57517224, T 0.22931010, ³He 0.40376704) as
**symbolic `tr_M_in_q` polynomials**, which looked like a hand re-derivation.
It is not: its producer `habiro/habiro_coefficients_atomic.py` goes through
`atom_canonical_crossings`, which defaults to borromean. The witness is dated
**2026-08-26**, ten days before the ruling. It is a re-run, not a rewrite.

**3. The published-content exposure is one file, and it quotes nothing.**
Of 17 consumers, 13 emit witnesses and exactly **one** is cited from a content
block — `mass_table_comprehensive.py` from
`brings-surface/inter-nucleon-channel-color-tube.md`, and that citation is a
link in a source list. The block quotes no τ or mass figure that would move.
The blast radius on the paper is, as far as this measurement goes, **nil**.

## The one thing that will break, and it is not a bug

`probes/nucleon_h3_marshalling_divergence_probe.py` asserts that
`compute_tau_M_nucleon_H3` agrees with the habiro witness. That agreement is
the 2026-08-26 fix (`qou-qu2w`) and it is an agreement between **two grouped
sources**. Repoint one without the other and this probe goes red — correctly,
but for the wrong reason, and it is the regression guard for a real earlier
defect. Whichever option is chosen must move both together or give this probe a
way to keep asking its historical question.

---

## Option A — repoint the helper, regenerate the cluster

Change `compute_tau_M_nucleon_H3` to take its word from `atom_braid_word_3A`
and its characters from `chi_general_word.chi_all_lambda_any`. Re-run habiro,
then the 13 witness-emitting consumers.

- **Effort:** small edit; the cost is the regeneration sweep and reading 13 diffs.
- **Speed:** the fix is *faster* — 0.669 s → 0.0023 s per nucleus, measured, because
  the general dispatcher at H₃ is `d_λ ≤ 2` and needs no transfer setup.
- **Ends with:** one ordering everywhere; the ruling actually applied.
- **Risk:** the divergence probe must be re-pointed in the same change or it
  reads as a regression. Any consumer with a transcribed grouped constant will
  surface as a diff — that is the sweep's job, but it is 13 diffs to read.

## Option B — add `intra_order` to the helper, default `borromean` — **recommended**

Same edit, plus a keyword. Production moves; a caller that genuinely wants the
historical grouped value asks for it.

- **Everything A gets**, plus: `nucleon_h3_marshalling_divergence_probe` passes
  `intra_order="grouped"` and keeps documenting the `qou-qu2w` agreement as a
  live, green, *explicitly historical* check instead of becoming a false alarm.
- **Migration is reviewable per caller** rather than all-at-once, and a caller
  that must not move can say so at its own call site with a reason.
- **Cost over A:** one keyword and the discipline to not let `grouped` spread.
  The parameter is a documented historical escape hatch, not a choice — the
  default is the ruling.
- **Why I recommend it:** the only thing that would stall Option A is the
  divergence probe going red for a reason that is not a regression. B removes
  that without weakening the outcome.

## Option C — new function, deprecate the old, migrate one at a time

`compute_tau_M_nucleon_H3_canonical` alongside; move consumers individually.

- **Slowest, most individually revertible.**
- **Risk I would weigh heavily:** two near-identical trace helpers coexisting is
  *exactly* the configuration that produced this bean's predecessor. `qou-qu2w`
  was a silent 15.3 % / 27.3 % divergence between two paths to the same nucleon
  trace that nobody compared for months. C recreates that shape deliberately.

## Option D — document that the nucleon H₃ block stays grouped

Requires a stated reason the ruling's argument fails at A = 1.

- I could not construct one. The nucleon word's core is `(σ₀σ₁⁻¹)³`; the
  non-commutation argument applies verbatim.
- Leaves production contradicting the ruling, and leaves the ⁴He result
  (`qou-hft3`) — where three independent routes agree only on borromean inputs —
  contradicting the nucleon blocks feeding the rest of the mass table.
- Listed for completeness; I do not think it is defensible on the evidence.

## Evidence bearing on the decision

Independent of the ruling itself, borromean nucleon inputs are what make the
⁴He value close. Three structurally different routes agree to 51 digits on
`0.011237417659767421564199549374410607269662696081261`, and the closed form —
the one making a *different* structural claim (multiplicativity along the
chain) — reproduces it only when fed borromean τ_p, τ_n. Fed the grouped values
this helper supplies it returns 0.16097414544240738, off by 14.325, which is
exactly `(1.8206)² · (2.0789)²`. That is not evidence about the ruling's
motivation, but it is evidence that the rest of the pipeline is already
borromean and this helper is the odd one out.

---

## Tested the habiro re-run — two things the options must account for

I ran `habiro/habiro_coefficients_atomic.py` to find out whether habiro is a
re-run or a re-derivation, then reverted the output. It is a re-run, and it
works — but not cleanly.

**Good: the ordering change does not break the cyclotomic structure.** Proton
and neutron recompute to borromean (`tr_M @ q₀ = 0.475134` for the neutron, the
ruling's value, not the grouped 0.987744), the Habiro coefficients stay
**integral** — 9 each, `all integral: True` — and the reconstruction identity
`Σ a_m·(q;q)_m = p(q)` still closes. Integrality is not automatic; had the
borromean trace broken it, that would have been real evidence against applying
the ruling here. It does not.

**Hazard 1 — a plain re-run produces a MIXED-ORDERING witness.** The producer
merge-preserves entries it did not recompute:

    [merge-preserve] kept prior witness entry: D (deuteron, A=2) (not recomputed)
    [merge-preserve] kept prior witness entry: T (tritium, A=3) (not recomputed)
    [merge-preserve] kept prior witness entry: 3He (helium-3, A=3) (not recomputed)

so the file it writes holds

| entry | value | ordering |
|---|---|---|
| p (A=1) | 0.6293284022029219 | **borromean** |
| n (A=1) | 0.4751335171556822 | **borromean** |
| D (A=2) | 0.5751722439177718 | *grouped, stale* |
| T (A=3) | 0.2293101021045565 | *grouped, stale* |
| ³He (A=3) | 0.4037670368514281 | *grouped, stale* |

unmarked, in one file. That is strictly worse than either pure state and it is
what anyone executing option A or B naively will produce. **Reverted, not
committed.** Whatever option is taken must force the A ≥ 2 entries to
recompute, or the witness has to declare per-entry ordering.

**Hazard 2 — there are two copies of this witness.**

    computations/habiro/habiro-coefficients-atomic.witness.json
    qou-mass/src/qou_mass/habiro-coefficients-atomic.witness.json

Byte-identical today (both `computedAt` 2026-08-26T14:43:07), and the producer
writes only to the first. So a re-run silently forks them. Both must move
together, or the second must be repointed at the first.

**Net effect on the options:** A and B are still re-runs, not re-derivations —
that part holds and is the main cost question. But the sweep is not "run 13
producers"; it is "force full recompute of habiro across all five entries,
reconcile two copies, then run 13 producers". Option C's staged migration looks
worse under this finding, not better: a per-caller migration would hold the
corpus in exactly this mixed state for the duration.
