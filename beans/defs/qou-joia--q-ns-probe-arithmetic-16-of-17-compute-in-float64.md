---
# qou-joia
title: 'q-NS probe arithmetic: 16 of 17 compute in float64 — wider than the two witness-tier beans, and the directive that scopes it postdates them'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T08:11:29Z
updated_at: 2026-10-04T15:22:53Z
parent: qou-a3n3
---

Measured 2026-09-14 on `main`-equivalent tree, while answering a
"where does the q-NS arc stand" question. **Not acted on** — filed rather than
swept, per AGENTS.md §"ASK THE OWNER BEFORE CHANGING THINGS".

## The measurement

    computations/qns_*.py                          17 probes
      import mpmath                                 1
      import math (float64), no mpmath             16

The one exception is `qns_levi_lock_beta_exact_probe.py`.

## Why this is not already covered by `qou-xwjs` / `qou-o227`

Both existing beans are about **witnesses**: `qou-o227` (completed) is
"three new q-NS probes carry raw float64 without declaring `precision_tier`";
`qou-xwjs` (todo) is "the 5 (now 6) qns exploratory probe witnesses carry
float64 — mpf-carry the summary fields at the producer or record a probe-tier
disposition; NEW-dirty on the ratchet". Five `qns-*` witnesses are in
`computations/raw-float64-baseline.json` accordingly.

That is the **serialization** surface. This bean is the **arithmetic** surface:
whether the probe *computes* in float64, which AGENTS.md §"PROBES ARE NOT
EXEMPT" rule 1 forbids independently of what the witness writes. 6 tracked vs
16 measured.

**Both beans predate the directive that scopes them.** `qou-o227` and
`qou-xwjs` are dated **2026-08-15**; the owner directive making probes
non-exempt is **2026-08-18**. So they are not stale so much as written under the
earlier rule — which is exactly why the wider surface has no tracker.

## What this does NOT establish, and the distinction is load-bearing

**I have NOT shown that float64 rounding corrupted any `qou-a3n3` SF
conclusion.** Do not read it that way and do not write it that way.

What the corpus *does* already carry is one instance where the exact route
overturned a recorded conclusion in this exact family — and the mechanism was
**not** rounding. `qns_levi_lock_scaling_probe.py` recorded
`beta_fit = 0.99628` for the anti-parallel-pair Levi channel;
`qns_levi_lock_beta_exact_probe.py` shows the closed form is exact algebra —
`C_L = (2Γ/π)(1+ε)/ε`, so `β = 1` on the nose — and that `0.99628` is a
**finite-window least-squares artifact dominated by its coarse end** (secant
exponent `0.96293` over `[10⁻¹,10⁻²]`, `0.99999996` over `[10⁻⁷,10⁻⁸]`,
`1.0` over `[10⁻¹⁹,10⁻²⁰]`).

That matters for `conj:levi-degeneracy` specifically: `0.99628` sits inside
**window C**, where the trichotomy's regularity verdict is explicitly
*undetermined*; `β = 1` is **branch B (regular)**. So the recorded fit read the
channel as undetermined when the corpus's own formula says regular — still
scope (a) and still conditional on the lock formula `C_L = Γ/(πν_q)`, which is
a model input, not derived.

The probe's own header states why it used mpmath: *"the whole point here is a
discrepancy in the 3rd decimal place, which float64 slope fitting is exactly the
wrong instrument for."* The lesson is about **fit-vs-closed-form posture**, and
exact arithmetic is what made the posture visible — not that the digits were
wrong.

## Blast radius, in what-a-reader-sees terms

The float64 probes are the evidence base for the SF-series entries of
`.beans/qou-a3n3` (EPIC, in-progress, reopened) — SF2/SF3 (no finite unforced
structure blows up in-model), SF5 (pile-up is unit-dependent; the two
normalisations give **opposite** answers, and the epic blocks on that owner
call), SF6 (amplitude-form step refuted for small ε), SF10 ("phases weaken the
tail" refuted). Each is recorded **scope (a)**, which is correct and is not
what is in question here. What is in question is that several of them turn on
small differences at small ε — the same regime where the β fit misled.

## Options

1. **Nothing.** The default. The 16 stay, the ratchet keeps flagging the 5-6
   witnesses, and the SF conclusions stand as scope-(a) records. Costs nothing;
   leaves the arithmetic surface untracked once this bean is read.
2. **Re-run the ε-sensitive SF probes under mpmath and compare.** Bounded — the
   probes are small and fast — and it either confirms the conclusions (which is
   worth having, since they are load-bearing negatives) or finds another fit
   artifact. Does not require changing any recorded verdict up front.
3. **Migrate all 16 to mpmath.** Largest, and mostly mechanical; but a shell
   model is a caricature whose *own* fidelity is the dominant uncertainty, so
   exact arithmetic on a caricature buys less than option 2's targeted check.

**Recommendation (judgement, not a finding): option 2, and only for the probes
whose conclusion turns on behaviour as ε → 0** — SF5 and SF6 are the two the
β artifact most resembles. Option 3 is the kind of blanket sweep the
ask-the-owner rule exists to stop.
