---
# qou-wfvl
title: 'MIGRATION NOT DONE: the Q_beta element is census-derived while the owner''s gamma-gamma ruling forbids census selection'
status: completed
type: task
priority: high
created_at: 2026-09-12T19:04:20Z
updated_at: 2026-09-12T19:40:13Z
---

**What is wrong.** The Q_β prediction's *functional* was migrated to the ruled
`z_D`, but the *element* it acts on was not. The dashboard scores `Δ_S`, the
**short-NF element**, whose provenance is the census / normal-form construction.

**Why that violates a ruling made the same day.** On 2026-09-08, alongside the
`ε := tr at z_D` ruling, the owner also ruled (`qou-ales`): *"All selection of
great words should be done through gamma gamma production and the semi-definite
product solutions at q₀. Shouldn't use census."* `Δ_S` is census-derived, so it
is not an admissible element under that ruling.

**The candidates, all at level 2 = `z_D`** (from `qbeta-option-e-required-level`):

| candidate Δ | residual | provenance |
|---|---|---|
| `delta_S` short NF | −43.157 % | NF/census — **what the dashboard scores** |
| nuc9 `build_nucleon_nf` | −30.936 % | census |
| **nuc11 interleaved** | **−17.496 %** | **γγ-selected** (PR #7212 Part 4) |
| nuc11 gen-grouped | −15.451 % | census; γγ-**excluded** (positive 2nd letter) |

So the γγ-selected element is **2.5× closer** to CODATA than what is published —
and, more importantly, *derived rather than selected*. Both properties point the
same way, which is unusual here and worth noting.

**Blocked on:** PR #7212, which establishes the γγ ordering result. Open at the
time of writing, so it is a claim, not corpus.

**This is an OWNER DECISION, not agent work.** Changing the scored element is
neither a precision increase nor corpus-derived (exemptions 1 and 2 of the
2026-09-07 ask-before-change directive), so it waits. The row already records
`element_scored`, `element_is_ruled: false` and all four candidates, so nobody
reading the witness mistakes `Δ_S` for the canonical element.

**Do NOT pick the element by residual.** `qbeta_zd_gap_anatomy_probe` shows
`z*`, the parameter reproducing CODATA with `Δ_S`, is 0.99850 — 0.15 % from the
inadmissible `z = 1` — and neither admissible root is within 11 %. Ranking by
residual is the selection-against-the-target the anti-fit directive forbails;
the element must be chosen by the γγ + confinement-SDP construction and its
residual reported afterwards, whatever it is.

**Highest-value item in this arc: it subsumes the Q_β accuracy question.**
Full analysis: `docs/audits/2026-09-12-zd-gap-anatomy-and-three-undone-migrations.md` §5(a).


## 2026-09-12 — MIGRATED, on owner instruction ("work qou-wfvl", "work γγ").

The dashboard now scores **`nuc11_interleaved`**, the γγ-selected nucleon word.

**The chain, every link on main or committed — NOT depending on the open #7212:**

1. `QOU.Mass.GammaGammaWordSelection.vertex i = [(i, +), (i+1, −)]` **on main**,
   so every γγ word has a **negative second letter**. The gen-grouped core begins
   `σ₀σ₀` (positive second letter) and is therefore **excluded**; the interleaved
   core `(σ₀σ₁⁻¹)³` is three vertices and is **admitted**.
2. `qbeta-option-e-required-level.witness.json` (**on main**, `q0_anchor: proton`,
   *both* admissible parameters evaluated) carries `tr_conv_D` for all four
   candidates.

PR #7212 proves (1) as an explicit Lean lemma. It is **open**, so it is cited as
**corroboration, not authority** — the authority is the owner's γγ ruling plus
`vertex`'s definition on main.

**Calibrated, two ways.** `err_pct_at_order_zero_E0 = −17.4959286063` against the
census witness's own `pct_D = −17.495929`; and independently that witness's
`delta_S` `tr_conv_D = −0.106235639848` reproduces my own `−0.1062356398` exactly.

| row | `Δ_S` (was) | γγ-selected (now) |
|---|---|---|
| `Q_β` | 4.259e+8 ppb | **1.668e+8 ppb** — 2.55× better |
| `m_n` | 3.547e+5 ppb | **1.389e+5 ppb** |
| `Δ_pn` | 2.576e+8 ppb | **1.009e+8 ppb** |

**🛑 NOT CHOSEN BY RESIDUAL, and the producer records that.** The γγ element is
2.5× closer to CODATA, but it is selected because it is **derived**. Were it
*further* away it would still be the right element. A later agent revisiting this
must not reverse it on accuracy grounds. The superseded `Δ_S` value stays on the
row (`Q_beta_MeV_on_superseded_delta_S`) so the delta remains measurable.

**A defect in my own earlier work, fixed here.** `_qbeta_ruled_base()` computes
the element, the `E₀` form, the calibration verdict, the four candidates and the
superseded cell — and **none of it reached the witness**. The dict was consumed
for `pred` and for the row's `note` string, then dropped. PR #7221 claimed *"the
row now carries `element_scored` / `element_is_ruled: false`"* **as structured
fields**; it did not — they were prose only. Now emitted as
`data.qbeta_ruled_base`. **A field a consumer cannot read is not a record.**

**Still scoped:** zero `c_k` rungs on the ruled base (`qou-cds1`, blocked on
`qou-pdix`; second re-score `qou-iagg`). The element question is closed; the
ladder is not.

PR #7235, commit `a13b938f451`.
