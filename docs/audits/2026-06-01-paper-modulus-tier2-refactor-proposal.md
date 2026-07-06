# Tier-2 paper `|...|` refactor — proposal (for per-site author review)

**Date:** 2026-06-01
**PR:** TBD (claude/phi-q-modulus-audit-and-reframe-2026-06-01)
**Status:** PROPOSAL — author per-site review required.
**Triggered by:** user 2026-06-01: "we want to minimize use of `|...|`, if
needed use `tr_M · \bar{tr_M}`. Per-site author review for each of 15
flagships."

## Discipline rules (per user 2026-06-01)

1. **Minimize `|...|`** in categorical / pre-archimedean statements.
2. When modulus is needed, use **`tr_M · \bar{tr_M}`** (explicit Hecke
   bar-involution) — NOT `|tr_M|²`.
3. Archimedean specialization may reintroduce `|...|` if the observable
   is positive AND the modulus is the post-τ evaluation step.

## Already executed (this PR's commits)

| Site | Action |
|---|---|
| `atom-knot-mass-derivation.md:66,76` | `\|tr_M(T_w)\|` → `tr_M(T_w)`; `\|V̂_i\|` → `V̂_i` in categorical `M(𝔥)` definition + tower (PR #1643 prior commit) |
| `markov-disambiguation.md:17-18` | `\|tr_M\|² / Σ\|tr_M\|²` → `tr_M·\bar{tr_M} / Σ tr_M·\bar{tr_M}` (Tier-3 rewrite, executed) |
| 13 production scripts (`mass_formula_6term`, `mass_endomorphism`, `multi_level_jet_sum`, `binding_via_interface_knot`, `hydrogen_qshuffle_compound`, `atom_level_wedderburn_tower`, `brane_tower_isospin_diagnosis`, `mass_formula_6term_mpfr_50dps`, `paper_six_term_isotope_sweep`, `_li_2_q_util`) | `Phi_q(abs(v))` / `Li_2^q(-abs(v))` → signed `Phi_q(v)` / `Li_2^q(-v)`. Production aligned with corrected paper categorical statements. |

## Proposal: remaining 32 Tier-2 sites — per-site author review

For each entry: **B**efore (current) → **A**fter (proposed). Author confirms / amends. Tier-1 was a false positive (audit imprecision); each site below should be confirmed before editing.

### Group I — Categorical mass DEFINITIONS

#### `calibration-inputs.md:147`

```
B: 𝔪(ϱ) = |tr_M(ρ(β))|
A: 𝔪(ϱ) = tr_M(ρ(β))
   (archimedean specialization at q_0: physical mass = |𝔪(ϱ)|_{q=q_0})
```

#### `descended-level-zero.md:194`

```
B: The single-level mass is |tr_M(ρ(β))|.
A: The single-level mass is tr_M(ρ(β)); its archimedean image at q_0 is the positive observable |tr_M(ρ(β))|_{q=q_0}.
```

#### `feynman-categorical-trace.md:41`

```
B: |tr_M(ρ(β))|
A: tr_M(ρ(β))    [drop |...| — Feynman categorical content is signed; archimedean realization is the post-τ step]
```

#### `feynman-qou-dictionary-table-data.md:5`

```
B: 𝔈_q(ϱ) = |tr_M(ρ(β))|
A: 𝔈_q(ϱ) = tr_M(ρ(β))    [q-energy is the categorical scalar; archimedean realization may take absolute value]
```

### Group II — Flagship binding/mass formulas with `|tr_M(T_w)|`

#### `brane-tower-z-habiro.md:122,172,217`

```
B: B(𝔥) = m_e · ρ · (|tr_M(T_w)| + tower^(k) + σ_3A)
A: B(𝔥) = m_e · ρ · (tr_M(T_w) + tower^(k) + σ_3A)
   (archimedean specialization at q_0: physical binding = |...|_{q=q_0})
```

#### `conj-canonical-knot-id-sdp.md:20,99`

```
B: B = m_e · ρ · |tr_M(T_w)|     (flagship single-term)
A: B = m_e · ρ · tr_M(T_w)
   archimedean: physical_B = m_e · ρ · |tr_M(T_w)|_{q=q_0}
```

#### `e-infinity-page-identifications.md:60`

```
B: |tr_M(T_w)|
A: tr_M(T_w)    [E∞ page categorical content is signed]
```

#### `e-infinity-page-identifications-table-data.md:3`

```
B: descended ‖tr_M(T_w)‖ (Term 1) DERIVED
A: descended tr_M(T_w) (Term 1) DERIVED    [drop double-pipe; remains a categorical Term 1]
```

#### `atom-knot-mass-derivation.md:400` (single-term shorthand discussion — may already be archimedean)

**ESCALATE** — line 400 mentions a single-term shorthand. Need author confirmation whether it's the SAME categorical form (`B = m_e · ν_SDP · tr_M(T_w)`) or an archimedean step.

### Group III — Mass DIFFERENCE formulas where `|...|` is on both sides

#### `deuterium-derived-binding.md:131-132`

```
B: Δtr = |tr_M(free)| − |tr_M(atom)|
A: Δtr = tr_M(free) − tr_M(atom)    [both terms positive at q_0; |...| redundant; keep one outer archimedean modulus if author confirms]
```

#### `np-discrepancy-resolution.md:70-71`

```
B: Term 1 (descended |tr_M|): |tr_M(𝓑_p)| ≈ 1.065 > |tr_M(𝓑_n)| ≈ 0.923
A: Term 1 (descended tr_M): tr_M(𝓑_p) ≈ 1.065 > tr_M(𝓑_n) ≈ 0.923
   (both positive at q_0; statement is sign-preserving; archimedean reformulation works either way)
```

### Group IV — Borromean / Frobenius factor

#### `borromean-markov-trace-closed-form.md:175,177`

```
B: F_Bor = |tr_M| · [3]_q! / q³
A: F_Bor = tr_M(β_Bor) · [3]_q! / q³
   archimedean: physical_F_Bor = |...|_{q=q_0}
   (closed form: F_Bor(q) = (4+h²-3h⁴-h⁶)/(h²+4) per PR #1615 — signed throughout the q-rational)
```

#### `proton-mass-substrate-identity.md:14`

```
B: |tr_M(β_Bor, q)|
A: tr_M(β_Bor, q)    [substrate identity at q-level is signed; |...| at archimedean]
```

### Group V — Remarks / table data

#### `rem-im-q-vs-p-skew.md:33`

```
B: 𝔪_{q,𝓚} = |tr_M(ρ(β_𝓚))|
A: 𝔪_{q,𝓚} = tr_M(ρ(β_𝓚))
   (this remark interprets the Im(q) vs P_skew distinction; signed tr_M at categorical level is the correct framing — the |...| was inherited from older convention)
```

#### `atom-mass-full-hecke.md:44`

```
B: 𝔪_vert = |tr_M^full(Φ_mass)|
A: 𝔪_vert = tr_M^full(Φ_mass)
   archimedean: physical_𝔪_vert = |...|_{q=q_0}
```

### Group VI — Delta uniform bound (special — may genuinely need |...|)

#### `delta-max-uniform-bound.md:50`

```
B: |tr_M(x)|
A: ESCALATE
   This appears in a BOUND statement (|tr_M(x)| ≤ ...). Bounds genuinely need
   modulus — the bound is on the magnitude. Possibly OK as-is. Author confirms.
```

## Sites NOT in proposal (already classified as audit false positive)

#### `conj-im-q-physical-role.md:5,23`

The `|tr_M|` in this conjecture is **CORRECTLY discussing the current
archimedean modulus projection** that hides Im(q). The conjecture's
point is THAT projection — refactoring it would erase the conjecture's
subject. **NO CHANGE.**

## Total scope summary

| Group | Sites | Action |
|---|---|---|
| Already executed | 16 (1 paper + 1 paper Tier-3 + 13 production + 1 audit-doc) | this PR |
| I — Categorical defs | 4 | proposal — drop `|...|` |
| II — Flagship binding | 7 (across 4 files) | proposal — drop `|...|`; 1 escalates |
| III — Differences | 2 (across 2 files) | proposal — drop both `|...|` |
| IV — Borromean | 2 | proposal — drop, with closed-form reference |
| V — Remarks/table | 2 | proposal — drop |
| VI — Bounds | 1 | ESCALATE — bound may need modulus |
| **False positive** | 2 | NO CHANGE (`conj-im-q-physical-role`) |
| **Total in scope** | **33** | **per-site author review** |

## Author confirmation needed

Please tick / strike through each Group / site. Once confirmed I batch-edit on the next session (or as follow-up commits to this PR). The most semantically heavy entries are **Group II** (flagship binding formulas) — those define how the framework expresses binding/mass, so any change has paper-wide ripple.

For **Group VI** (`delta-max-uniform-bound.md:50`), author guidance is needed: should bounds use `|...|` (categorical magnitude bound) or signed `tr_M` (with the bound rephrased in terms of `tr_M · \bar{tr_M}`)?

## Cross-refs

- This PR's audit: 34 NON-ARCH-MISUSE sites
- This PR's executed edits (16 sites)
- PR #1641 — Φ_q signed-vs-|...| sensitivity (92% per-term)
- PR #1626 — complex-c_3 fibre diagnostic
- PR #1616 — Im(q) fibre/observable framing in AGENTS.md
- `prop:li2q-phiq-bar-symmetrization`
- AGENTS.md §7c — base ring convention (analogous discipline)
