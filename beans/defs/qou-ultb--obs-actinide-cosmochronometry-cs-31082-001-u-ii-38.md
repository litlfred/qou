---
# qou-ultb
title: 'OBS: actinide cosmochronometry (CS 31082-001 U II 3859.57A) — Gamow-amplified alpha_EM probe; bounds |da/a| <~ 2.08e-3, LOOSER than quasars but at the FORMATION site'
status: in-progress
pr: 8196
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-obs
created_at: 2026-09-07T13:44:35Z
updated_at: 2026-10-10T07:16:28Z
parent: qou-8lxd
---

---

## 2026-09-13 — the conversion is done, and the answer is a robust NO

This bean was a **title with an empty body**. Giving it one.

### The one number that was computable

    S = |d ln(alpha_em) / d ln q| = 6.86193302278   at the proton q0

from `meson_em_sinh_closed_form.alpha_em_inv_derived` — the same entry point
the L2 dashboard scores, not a re-derivation. Stable to **3.55e-61** between
60 and 90 dps, so it is the derivative and not an artifact of the step.

So any bound `B` on `|d(alpha)/alpha|` is a bound `B/6.86193` on `|dq/q|`.

### The verdict: this cannot constrain q0, by ~2.5e5x

| | |
|---|---|
| bean's asserted B | 2.08e-3 (UNVERIFIED — see below) |
| implied `|dq/q|` | 3.03122e-4 |
| sigma(q0), proton pin | 1.22335 ppb = 1.22335e-9 |
| **ratio bound / sigma** | **2.478e+5** |

**The bean's own framing is what this overturns.** "LOOSER than quasars but at
the FORMATION site" treats formation-site locality as the payoff that offsets
the weaker bound. For THIS framework that trade does not pay: q0 is already
pinned from CODATA mass ratios at 1.2 ppb, so a formation-site measurement
2.5e5x weaker constrains nothing. To matter, B would have to reach **8.4e-9** —
which is far beyond quasar bounds too, so the whole alpha-variation programme
is the wrong instrument for pinning q0, formation site or not.

### Why the verdict survives the unverified input

**Corpus-grep path 5, run today: `library/` holds NO source on CS 31082-001,
actinide cosmochronometry, or the U II 3859.57 A line** — one INDEX.md hit and
one unrelated nucl-th summary, zero section text. So 2.08e-3 has no provenance
in this corpus and is used as an INPUT, not as an established figure.

That does not weaken the conclusion, because **the conclusion is insensitive
to it**: the bound would have to improve by ~2.5e5x to matter. No plausible
correction to 2.08e-3 — nor to the "Gamow amplification" that produces it —
changes the answer.

### Why this bean stays OPEN (AGENTS.md §13a)

The conversion rides on `alpha_em(q)`, and AGENTS.md records that derivation
as **conditional on an open Lean `sorry`** (the Witten-kappa Gram determinant).
A bean whose result depends on an open conjecture does not get closed, even
when the numeric margin (2.5e5x) makes the dependence practically harmless.

### What this does NOT touch

**`qou-ihtw` and `qou-fu7d` are unaffected.** They propose constraining the
framework through **nuclear masses and beta-rates far from stability**, and
through **isotope-vs-element discrimination** — different quantities, not
alpha. Nothing here bears on them, and this negative must not be read across
to them. Scope (a): the alpha-variation ROUTE cannot test q0 at achievable
precision; no ingredient is ruled out.

Probe: `computations/obs/alpha_bound_to_q0_sensitivity_probe.py` (mpmath mpf
at 60 dps, cross-checked at 90; no float64).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress (2026-11-16, PR #8196)
- [x] Formalized `hasSensitivitySlack`, `sensitivity_slack_implies_looser_than_anchor`, and `actinide_u2_cosmochronometry_slack_witness` in `folio/quantum-observable-universe/lean/QOU/Eightfold/LeptonReadoutHiggsScaleMesonSyllableAndIcosahedralOrbit.lean` + 50-dps mpmath witness (`qou_ultb_actinide_cosmochronometry_slack`) in PR #8196 (`38b68fa660bb34e2ffb7a2e1a09e5c4f5308e2cf`).
