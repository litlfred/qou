# 1ppb gap closure — analysis of structural ceilings (2026-05-23)

**Context**: post-#942 merge (substrate flavor-split wireup), the
per-observable 100× status shows m_p / m_n at honest +2.89%
(Family A class-uniform residual). User directive: *"lets work on
closing 1ppm gap after review, reanalysis and `/coordinate`"*.

This audit does the reanalysis + records the structural ceilings
for each observable's contribution to the L2 (100×) target.

## Per-observable status (latest origin/main)

| obs | err_ppb | σ_exp_ppb | 100× target | miss factor | beats 100× ? |
|-----|--------:|----------:|------------:|------------:|:---:|
| m_e | 0 | 0.294 | 0.003 ppb | (anchor) | ✅ |
| m_μ | **0.06** | 21.77 | 0.218 ppb | **0.27×** | ✅ NEW |
| m_p | 2.89×10⁷ | 0.309 | 0.003 ppb | 9.35×10⁹ | ❌ |
| m_n | 2.89×10⁷ | 0.575 | 0.006 ppb | 5.03×10⁹ | ❌ |
| Δ_pn | 2.86×10⁷ | 473.9 | 4.74 ppb | 6.03×10⁶ | ❌ |
| Q_β | 11.13 | 779.7 | 7.80 ppb | 1.43× | ❌ |

**2 of 6 beat 100×** (m_e anchor + m_μ).

## Why the numbers shifted from "1ppb m_p" to "2.89% m_p"

The recent CAL-4 work (PRs #888, #895, #942) removed the calibrated
`LAMBDA_PROTON_DOC` literal and replaced it with the genuine
Family A categorical derivation. The prior ~1 ppb m_p / m_n match
was a CAL-4-in-disguise calibration. Post-#942, m_p / m_n show the
structural residual: ~2.89 % — the absolute Bring-Bloch / λ_scale
gap that's been the open research direction all along.

The substrate flavor-split closes **Δm_pn to 0.03 %** (substrate-pure
closed form, framework-proved, no fit). The absolute m_avg scale
carries the open gap.

## Structural ceiling table

| obs | structural ceiling | gap to 100× target | gated on |
|-----|--------------------|--------------------|----------|
| m_e | anchor | 0 | — |
| m_μ | 0.06 ppb (already met) | DONE | — |
| Q_β | **Q_N2 · (1 - b³·ℏ_q^6) ≈ 0.62 ppm** | -1.4× (close, just over) | exact c_3 value; higher-order |
| m_p | **V_7 = `Σ dim_q V_λ / [4]_q` ≈ +0.144 %** | -1.44×10⁵ | substrate-derivation of q_0 |
| m_n | V_7 same | -1.44×10⁵ | substrate-derivation of q_0 |
| Δ_pn | flavor-split: 0.03 % (substrate-pure proved) | -3.04×10⁴ | absolute m_avg scale |

## V_7 deep-dive (m_p / m_n track)

V_7 = `Σ_{λ⊢4} dim_q V_λ / [4]_q` = `5/2 − (13/16)h² + O(h^4)`.

The empirical fit form is `5/2 − G·h²` with `G ≈ 0.91596`
(Catalan's constant; comes from the Volume of B_3 in hyperbolic
geometry). The h²-coefficient gap is **G − 13/16 ≈ 0.1035**.

Tested 7 natural h²-coefficient corrections against the gap:

| candidate | value | gap-residual | rel diff |
|-----------|------:|-------------:|---------:|
| `-π²/96` | -0.10281 | +0.000657 | **0.6%** ★ |
| `-ζ(3)/12` | -0.10017 | +0.00329 | 3.2% |
| `-G/9` | -0.10177 | +0.00169 | 1.6% |
| `-ln(2)/7` | -0.09902 | +0.00444 | 4.3% |
| `-1/(2π)` | -0.15915 | -0.0557 | 54% |
| `-1/(8·ln 2)` | -0.18034 | -0.0769 | 74% |

`-π²/96` is **0.6 % from closing the gap at h² level** — most
interesting empirical match but not a structural identity (would
need motivation from a Bloch-class evaluation; π²/96 is
`ζ(2)/16`).

**Empirical refinement at q_0**:
- V_7 alone: +0.144 % vs target
- V_7 + (-π²/96)·h²: **-0.039 % vs target** (3.7× improvement)
- Required c such that `V_7 + c·h² = target` numerically: **-0.0808**

The difference between the h²-coefficient analysis (-0.103) and
the numerical-at-q_0 analysis (-0.0808) reflects V_7's own h^4
contribution — at h = 0.21 (q_0), h^4 ≈ 0.0019 is the same order
as the target precision (~0.14 %). Pure-h²-coefficient closure is
incomplete.

### Verdict on V_7

V_7 is the **best pure-rational categorical structural form** for
the m_p / m_n closure. Closing the remaining +0.144 % requires:

- (a) **Categorical h^4 corrections** — would need a sub-leading
  character formula. Not obvious from existing infrastructure.
- (b) **Hyperbolic / Bring-Bloch input** — the irrational G in the
  empirical fit comes from B_3 hyperbolic volume. To recover G
  exactly requires Bloch-Wigner / dilogarithm evaluations on the
  brane substrate. This IS the open Bring-Bloch closure problem.
- (c) **Substrate-derivation of q_0** — declined per coord-ledger
  2026-05-08; out-of-scope without owner reversal.

**Pure-categorical work has a ceiling at +0.144 % (V_7).** Below
that requires non-rational input.

## Q_β deep-dive (CAL-3 anchor track)

Q_β has a 14-candidate empirical scan in
[`q-beta-operator-valued-N3.witness.json`]. Salient results:

| candidate | eps_ppm |
|-----------|--------:|
| Q_N2 alone (`Q_A · cos(α_N1) / (1 + b²·ℏ_q^4)`) | 1.247 |
| **Q_N2 · (1 - b³·ℏ_q^6)** | **0.624** |
| Q_N2 · (1 + b³·ℏ_q^6) | 1.860 |
| Q_N2 · (1 + c_3_emp · b³·ℏ_q^6) [fit, c_3 = -2.0097] | 0.0 |

**Structural conjecture**: `c_3 = -2 = J_Hopf(q=1)`. With c_3 = -2
exactly, Q_β lands at ~0.62 ppm (the `Q_N2 · (1 - b³·ℏ_q^6)`
variant).

### Verdict on Q_β

- **The `c_3 = -2` conjecture would beat 1 ppm but not the 100×
  target (7.8 ppb = 0.0078 ppm).**
- To close to 100×, c_3 would need to equal **-2.0097** exactly,
  which is the empirical fit value — not obviously a natural
  categorical quantity.
- The 0.97 % deviation from c_3 = -2 might be a c_4·ℏ_q^8 (or
  higher) categorical correction.

**Pure-categorical work on Q_β has a ceiling around 0.6 ppm
(c_3 = -2 exactly).** Hitting 100× target (7.8 ppb) requires
higher-order categorical corrections beyond N=3.

## Cluster status (sibling PRs as of 2026-05-23)

| PR | scope | state | next step |
|----|-------|-------|-----------|
| #909 | strategy-d λ_scale stage-1 (D1–D6 probes) | open | stage-2 PSLQ on -5.6 ppm ε residual |
| #916 | λ_scale alternatives F/G/H | open, dirty | refine V_7 (this audit) |
| #920 | cheat-sheet tracker (META) | open | recommends V_7 next step |
| #942 | flavor-split wireup → m_p ≠ m_n | **merged** | (closed) |
| #945 | deprecate m_n_difference_formula | open | (followup of #942) |

**Coordination posted on 2026-05-23**: brief intent comments on
#916, #920, #909 noting this V_7 + Q_β audit pass.

## Recommended next moves

1. **m_μ — celebrate; nothing to do** (0.06 ppb, beats 100× by 4×).
2. **Q_β — confirm c_3 = -2 exact** as a separate categorical-
   derivation PR; report whether it lands at 0.62 ppm. If yes,
   the 1.4× miss against the 100× target is the new structural
   ceiling (modulo higher-order c_4 work).
3. **m_p / m_n / Δ_pn — V_7 is the structural ceiling at +0.144 %.**
   Below that, three research directions:
   - **GAP-A-3 / GAP-A-4** (categorical brane-tower level
     selection / ρ general rule) per CLAUDE.md §Δ_λ gate
   - **Option E (Kashiwara crystal)** per CLAUDE.md §Δ_λ gate
   - **Substrate derivation of q_0** (out-of-scope per
     coord-ledger 2026-05-08)

None of these are mechanical migrations; all are research-grade
open problems. The cheat-sheet §5 backlog is closed for the
mechanical items (#1, #3, #5 closed; #2 gated on H_12 A-operator
extract; #4 closed for the one tractable case via #921).

## Cross-references

- [`docs/canonical-derivation-cheat-sheet.md §5`](../canonical-derivation-cheat-sheet.md) — migration backlog
- [`docs/coordination/2026-05-22-cheat-sheet-manager.md`](../coordination/2026-05-22-cheat-sheet-manager.md) — cheat-sheet cluster ledger
- [`docs/coordination/2026-05-23-cheat-sheet-fix-3-default-flip.md`](../coordination/2026-05-23-cheat-sheet-fix-3-default-flip.md) — recent PR #946 work
- [`folio-assistant/computations/probe_family_a_variants.py`](../../folio-assistant/computations/probe_family_a_variants.py) — V_1 .. V_8 catalogue
- [`folio-assistant/computations/q-beta-operator-valued-N3.witness.json`](../../folio-assistant/computations/q-beta-operator-valued-N3.witness.json) — 14-candidate Q_β empirical scan
- PR #916 — λ_scale alternatives F/G/H
- PR #920 — cheat-sheet tracker (recommends V_7 refinement)
