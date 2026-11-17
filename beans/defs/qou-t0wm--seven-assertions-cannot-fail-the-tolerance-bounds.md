---
# qou-t0wm
title: 'Seven assertions cannot fail: the tolerance bounds its own residual, in six producers'
status: in-progress
pr: 8290
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T06:21:10Z
updated_at: 2026-11-17T08:47:00Z
parent: qou-5vkl
---

Found 2026-09-05 while closing out the `qou-tol0` root cause. That bean's own
instance (`atom_mass_derived`, ten assertions under `tolerance=max(abs(r.delta_MeV)*2, 50)`)
was fixed in `7f95ad5962`; the SHAPE was never made detectable, so nothing had
looked for it elsewhere.

Detector: [`computations/audits/tolerance_from_residual_audit.py`](../computations/audits/tolerance_from_residual_audit.py).
Full analysis: [`docs/audits/2026-09-05-tolerance-that-bounds-its-own-residual.md`](../docs/audits/2026-09-05-tolerance-that-bounds-its-own-residual.md).

## The seven, each verified by hand

| producer:line | assertion | why it cannot fail |
|---|---|---|
| `mass-from-q-symbolic.py:568` | `𝔪(𝔅₃) Borromean topological mass` | `borromean_mass_ratio` IS `VOL_BORROMEAN / HBAR_Q_SQ0` (line 246); `expected` restates it |
| `mass-from-q-symbolic.py:577` | `𝔪(𝔅₃) in MeV` | both sides expand identically; the witness records residual **0.0 exactly** |
| `confined_knot_binding.py:289` | `W_sym equals W_alt` | `W_SYM` and `W_ALT` are the same expression, character for character (lines 42, 44) |
| `confined_knot_binding.py:308` | `V_pn = W_std*(z+d_pn)` | `expected` restates `V_pn_exact`'s definition (line 251) |
| `yekutieli_borromean_h2_extraction.py:216` | `kappa_computed` | tolerance `2*max(\|c\|,\|e\|)`; unfalsifiable by the triangle inequality |
| `compute_atom_chi_rust.py:164` | `rust_kernel_loaded` | `float(x)` vs `x`, same subscript |
| `channel_asymmetry_crossing_budget_bound_probe.py:204` | `budget_is_s_squared` | `c_inter = s * s` (line 134); `expected` is `s * s` |

## The two worth reading twice

**`W_sym equals W_alt`** carries `source="Wedderburn-Artin: dim_q((3))=dim_q((1,1,1))=1"`,
advertising a check of a representation-theoretic fact. It checks nothing — the
two constants are one expression written twice. **If the Wedderburn–Artin fact
were false, the assertion would still pass.** The `source` field is doing all
the epistemic work and none of it is tested.

**`kappa_computed`** is the one with a live wrong number. Recorded:
computed `0.1875`, expected `-0.915965594177219…`, tolerance `1.8319…`,
`passed: true`. Opposite signs; residual **1.1035**, a 121 % miss.

## What would close this, per assertion

Fix at the producer, and expect one to go RED — that is the honest outcome:

1. `mass-from-q-symbolic` ×2, `confined_knot_binding` ×2 — need an INDEPENDENT
   expected (a literal from the source each `source` field already names), or
   the assertion deleted. Restating a definition is not a check. Witness
   regeneration required; attribute any value movement against an unmodified
   run first.
2. `yekutieli_borromean_h2_extraction:216` — needs a real tolerance, and will
   then **fail** at 121 %. AGENTS.md asks for the honest negative explicitly.
   Whether κ = 0.1875 or the expected `-Vol/…` is the wrong side is a separate
   question this bean does not settle.
3. `compute_atom_chi_rust:164`, `channel_asymmetry…:204` — self-reports, the
   benign class `always_vacuous_assertion_scan` documents. Renaming suffices.

## Not to be confused with three neighbouring beans

- `qou-tol0` — the same root cause, its own instance already fixed. This is the
  corpus-wide sweep of the shape.
- `qou-26f2` — 266 assertions where `computed` and `expected` are the same AST.
  This audit deliberately **excludes** raw-identical arguments; only the case
  needing an indirection to see is new here.
- `qou-ploj` — `add_assertion(name, X, X)`, same exclusion.

## Do NOT widen anything

The audit exits 1 on any blocking hit. The fix is always at the assertion.


---

## 2026-09-05: one fixed, and a measured NEGATIVE on the next one

**`yekutieli_borromean_h2_extraction:216` — FIXED** (`cc28f268fb`). Two
falsifiable assertions replace the unfalsifiable one:

- `kappa_is_three_sixteenths` **passes** — κ = 3/16, verified exact
  (`κ − 3/16 = 0.0` at dps 30, 50 **and** 80, so not a PSLQ guess). The
  producer was already *printing* `mpmath.identify(κ) = (3/16)` to stdout and
  asserting nothing about it.
- `yekutieli_kappa_equals_minus_G` **fails**, at 121 %. `allPassed` is now
  false, which is the correct state.

Bonus: `max(abs(float(κ)), abs(float(G))) * 2` computes in float64, so that one
expression was **both** the tautology and this witness's only raw-float64
field. Draining it took the witness 1 → 0.

### `confined_knot_binding:289` — do NOT wire `y_λ` in. Measured.

The obvious repair for `W_sym equals W_alt` is to derive the two weights
independently from the corpus's canonical Markov weights. **That is a category
error and the numbers say so.** At the proton q₀:

    y_lambda_at(3, q0) = {(3,): 0.5054042265, (2,1): 0.2472978867, (1,1,1): 0.0}

`y_λ[(1,1,1)] = 0` — the alternating block is killed by the SU(2) truncation at
N = 2 — whereas `W_ALT = q²/(q⁴+4q²+1)` is nonzero. **`W_λ` and `y_λ` are
different objects sharing a subscript**, exactly the "shared type is not shared
instance" trap. Anyone repairing this assertion must first establish what
`W_SYM`/`W_ALT` are *meant* to be derived from; it is not `y_λ`.

So this one is left open deliberately rather than closed by guess. The two
constants are `q2 / denom_w` **on both lines** (42 and 44), so any repair is
research, not a mechanical substitution.

### Remaining, with dispositions

| producer:line | disposition |
|---|---|
| `confined_knot_binding:289` | **open** — needs the intended independent source for `W_ALT`; `y_λ` ruled out above |
| `confined_knot_binding:308` | same shape; `expected` restates `V_pn_exact`'s definition |
| `mass-from-q-symbolic:568,577` | candidate: turn each into an explicitly-labelled **regression pin** against a recorded literal. That catches drift in `VOL_BORROMEAN` / `HBAR_Q_SQ0`, which is real value — but it must be NAMED a regression pin, never "verifies the mass formula", or it launders a definition into a derivation |
| `compute_atom_chi_rust:164`, `channel_asymmetry…:204` | self-reports; renaming suffices. The first needs the rust kernel to re-run |

Detector count: **7 → 6 blocking**.


---

## Final state of this tranche (PR #6732)

**Detector: 7 → 4 blocking.** Three fixed, two left open with a measurement,
and one was never a defect.

| producer:line | outcome |
|---|---|
| `yekutieli_borromean_h2_extraction:216` | **fixed** — 2 falsifiable assertions; one FAILS at 121 %; raw-float64 1 → 0 |
| `mass-from-q-symbolic:568` | **fixed** — independent route via `Vol/(1−1/q)²` recomputed from `q` |
| `mass-from-q-symbolic:577` | **fixed** — same; and it exposed the false positive below |
| `confined_knot_binding:289` | **open** — `y_λ` ruled out by measurement; needs the intended source for `W_ALT` |
| `confined_knot_binding:308` | **open** — same shape |
| `compute_atom_chi_rust:164` | **open** — self-report; needs the rust kernel to re-run |
| `channel_asymmetry…:204` | **open** — self-report; renaming suffices |

## A false positive in my own dataflow tier, found by using the audit on a fix made with it

After `mass-from-q-symbolic:599` got an independent `expected`, it was **still**
blocking: `borromean_mass_MeV_err` is residual-named and reaches both sides. It
is a 1σ **propagated uncertainty**,
`sqrt((ratio_err·m_e)² + (ratio·m_e_err)²)`, and correct. An error-propagation
formula mentions the measured quantities for the same reason the residual does.

Discriminator: **a residual is a difference**. `_reaches_subtraction` requires a
`Sub` in the provenance — keeps the `qou-tol0` positive, drops this class.

**The general lesson outranks the instance.** The audit doc had claimed the
provable tiers were 7-for-7 and the name tier 0-for-4. Both true as counts on
`main`; but the dataflow half had fired on **nothing** there, and I read that
zero as soundness. **A tier that has never fired has been measured for recall
and not at all for precision.** Recorded as taxonomy row 34.

## Also fixed: the self-test was self-defeating

It pinned the two provable shapes to the live files that motivated them, and
went red the moment the first was **fixed**. A calibration that a successful
drain breaks is measuring the corpus, not the detector. Both are synthetic
fixtures now; only the git-history one stays live, durable because it is a
fixed sha.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress 2026-11-17 (PR #8290)

Cleared the remaining 2 `blocking` tautological assertions in `computations/confined_knot_binding.py` (`tolerance_from_residual_audit.py` `blocking: 2 -> 0`, exit 0) by comparing `W_SYM` (`q^2/(q^4+4q^2+1)`) against the bar-conjugate symmetric form `1/(q^2+4+q^-2)` and comparing the 3-channel sum `crossing_channels(1, -h/2)[3]` against `W_STD * (z - h/2)`, while lifting `confined_knot_binding.py` to `mpmath.mpf` (`54 -> 0` raw `float64`) on PR #8290 (`1c907342f24ac048c99eb24f30832b0b87b024b0`).
