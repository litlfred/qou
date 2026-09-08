# L2 / 1 ppQ — the research program, its gaps, and where each is being closed (2026-09-08)

**Tier:** coordination + audit (no new mathematics). Written on
`claude/l2-1-ppq-gaps-c9zuwt` (PR #7159) at the owner's request: *"what do we need to
do to get to L2 1 ppQ? Walk through the canonical derivation of mass and binding. List
exactly what the gaps are and where we are trying to close them … what is the status of
Q_β, c₃ or the f-map? What are the open conjectures? … articulate the research program
cohesively and see what are the priority gaps to close."*

**Provenance key used throughout.** `[W]` carried from a committed witness on
`origin/main` (with `computedAt`); `[M]` measured this session (git / grep / exact
arithmetic on witness fields); `[D]` carried from a cited audit doc or Lean file;
`[PR]` an open sibling PR not yet on `main`. No producer was re-run: `mpmath` is absent
from this container, so every number is the committed witness, not a fresh run.

---

## 0. The headline, and what "L2 1 ppQ" actually means

**"L2 1 ppQ" conflates two targets, and the distinction changes what has to be done.**

| leg | target | live status |
|---|---|---|
| **L1 — compute precision** | cross-method agreement ≤ 1 ppQ (10⁻¹⁵) at the substrate q₀ | **met**: 6 atoms, peel-vs-χ agreement 6e-50 … 1.2e-49 `[W]` (`onepb-status-dashboard`, 2026-08-30; `cross-check-trM-1ppb`, 2026-09-07). Two caveats in §5. |
| **L2 — per-observable accuracy** | for each predicted observable O, σ_theory(O) ≤ σ_exp(O)/100 | **1 of 6 scoreable (m_K/m_π), 0 of 6 unconditional** `[W]` 2026-09-07. |
| **σ_theory at 1 ppQ** (the owner's underlying goal, precision-goals.md §"reframe") | every residual becomes calibration-limited | residuals are 10⁴–10⁹ above 1 ppQ, and **every one traces to an un-derived object, not to compute** (§1.2). |

So L2 is never "1 ppQ": the tightest per-observable target is 1.5 ppt (α_em⁻¹) and the
loosest 264 ppb (m_K/m_π). What the owner is really asking is *which un-derived objects
stand between the chain and calibration-limited residuals*. That is the list in §6.

**The count moved on 2026-09-07 and the docs have not caught up.** Commit `d626761a34`
(bean `qou-37j2`) added `alpha_em_inv` to the L2 dashboard; `scoreable_total` went 5 → 6.
`docs/precision-goals.md` (lines 38, 240, 256, 265–267, 588) and `AGENTS.md` (lines
2373, 2421, 3112) still say 1/5. The unconditional count stays **0/6** under the
2026-08-22 red-team (`m_K/m_π` clears only through an α_em term resting on an open
`sorry`).

---

## 1. Live L2 status and where each residual comes from

### 1.1 The dashboard `[W]` — `per-observable-100x-status.witness.json`

`computedAt 2026-09-07T12:39:23Z`, `scriptHash 66f1e9466de8`, proton pin
`q₀ = 1.10997858275138080759…`, 70/60 dps. Q_β rows are stamped `INHERITED_C`
(canonical convention is D) and `INADMISSIBLE_FUNCTIONAL` (`z = 1`).

| obs | pred | CODATA/PDG | err (ppb) | σ_exp (ppb) | target σ/100 (ppb) | miss | scored? |
|---|---|---|---:|---:|---:|---:|---|
| m_p | 938.272089427 | 938.272089430 | 0.0029 | 0.309 | 0.0031 | N/A | no — anchor round-trip |
| m_e | 0.510998950690 | same | 0 (defined) | 0.313 | 0.0031 | N/A | no — CAL-1 input |
| m_μ | 105.658397811 | 105.658375496 | **211.2** | 21.77 | 0.2177 | **970.2×** | yes |
| Q_β | 0.782334410278 | 0.782333410 | **1279** | 779.7 | 7.797 | **164.0×** | yes |
| m_n | 939.565422788 | 939.565421940 | **0.903** | 0.511 | 0.0051 | **176.7×** | yes |
| Δ_pn | 1.29333336097 | 1.29333251 | **658.0** | 433.6 | 4.336 | **151.7×** | yes |
| α_em⁻¹ | 137.035999127 | 137.035999177 | **0.365** | 0.153 | 0.0015 | **238.3×** | yes (added 2026-09-07) |
| m_K/m_π | 3.53711862102 | 3.53711843895 | 51.5 | 26 364 | 263.6 | 0.195× (meets, 5.1× margin) | yes |

Quote `beats_100x_scoreable = 1 / scoreable_total = 6`. `beats_100x_count = 2` counts the
two inputs and must not be quoted (AGENTS.md STRICT). There are **no binding-energy rows**:
the per-isotope 100× targets (D 4.5, T 1.2, ³He 1.3, ⁴He 0.35 ppb) are unscored because
the extensive magnitude term is open (§3).

### 1.2 Residual → un-derived object → chain step

This is the table that answers "what do we need to do". Each residual is a framework
quantity; calibration noise is negligible against all of them (q₀'s own σ contributes
0.045 ppb to Q_β and 0.317 ppb to m_μ `[M]`).

| obs | residual | the un-derived object it traces to | chain step | owner bean |
|---|---:|---|---|---|
| m_μ | 211.2 ppb | **The μ–p substrate tension, exactly.** The CODATA-2022 muon pin and the proton pin differ by 11.614 ppb in q₀ `[M]`; m_μ = m_e·Vol(4₁)/ℏ_q² has lever `d ln m_μ / d ln q = −2/(q−1) = −18.185`, and 11.614 × 18.185 = **211.21 ppb** `[M]`, reproducing the witness to four digits. Every *ratio* observable has ℏ-exponent 0 and is blind to it (`PinRobustnessOfRatios.lean`). Re-pinning moves it, never shrinks it; deriving q₀ is forever gated. So this residual is **structural** — it can only close if the framework produces two pins that agree, i.e. if the archimedean evaluation of ℏ_q⁻² is refined, not if any anchor is chosen better. | 9 (archimedean functor at q₀) | none open — recorded as the two-way tension |
| Q_β | 1279 ppb | **Two stacked defects, one number.** (a) The scored value is the `Q_N2` rung of the c_k ladder in **convention C**; `qbeta_ck_cache.py` refuses under D, so no D-frame value exists (`qou-cds1`). (b) The closed form it sits on solves to Markov parameter `z = 1`, inadmissible under D (`ConventionDAdmissibleRoots.lean`, sorry-free); admissible alternatives give +12.47 % (`z = q`) and −43.16 % (`z_D`), and choosing by residual is forbidden (`qou-99qc`). | 11 (β-decay functional) — via 6 (Markov trace) | `qou-99qc`, `qou-cds1` |
| m_n | 0.903 ppb | **Pure Q_β propagation** via Path C `m_n = m_p + Q_β + m_e`: absolute offsets are Q_β +1.000 µeV, m_n +0.848 µeV, Δ_pn +0.851 µeV `[M]` — one number. Path C bypasses the flavour split, so the p/n colour-weighting convention (R3, `bring_color_weighted`) does **not** enter this row. | same as Q_β | same |
| Δ_pn | 658.0 ppb | same 0.85 µeV over a 1.29 MeV denominator | same | same |
| α_em⁻¹ | 0.365 ppb | Schwinger-ladder cubic form conditional on three unproved classes (`ArchimedeanLimit`, `BlochSuslinUniqueness`, `BringZeroModeBlochClass`) `[W]`; the residual's sign flips with the CODATA edition. | separate α_em chain | see §4 |
| m_K/m_π | 51.5 ppb (meets) | `√([3]_q[4]_q)` core is scan-selected (two discrete indices) and misses 385× on its own; clears only via the EM term `(α_em/π)(1+log(1+ℏ_q))` whose α_em rests on the Witten-κ `sorry`. Truncation knob removed 2026-08-22 (PR #5467); two selection knobs remain. | meson leg | `2026-08-22-mK-mpi-l2-red-team.md` |
| B(K), all A ≥ 2 | unscored | the **extensive (many-body) binding term** — a separate additive object, not a per-block weight (§3) | 9b | `qou-brng`, `qou-edt7` |

**Consequence for priorities.** Four of the six scoreable misses (Q_β, m_n, Δ_pn, and
the binding rows behind ⁴He) are downstream of **two** un-derived objects: the Q_β
functional under convention D, and the extensive binding term. m_μ is a third, structural
one. α_em and m_K/m_π share a fourth (the α_em conditional classes). That is the whole
L2 frontier: four objects.

### 1.3 The CAL-2 floor, restated

The "780 ppb CAL-2 floor" quoted in precision-goals.md is σ_exp(Q_β)/Q_β = 779.7 ppb
`[M]` (PDG 2024), the precision of the *ideal* CAL-2 datum. Under the proton
precision-substitution it is **not** the operative floor: q₀ is pinned from m_p/m_e at
0.0174 ppb, which propagates to 0.045 ppb in Q_β and **0.317 ppb in m_μ**. Every 100×
target in the table sits below 780 ppb, so "Subgoal-1 = targets ≥ 780 ppb" is satisfied by
nothing except the two anchors. And one target is unreachable at the proton pin by
*any* theory: **m_μ's target (0.2177 ppb) is below its calibration-propagated floor
(0.317 ppb)**. Only a tighter m_p/m_e measurement, or re-pinning to the muon (which makes
m_μ the tautological anchor and moves the 211 ppb onto m_p), changes that.

