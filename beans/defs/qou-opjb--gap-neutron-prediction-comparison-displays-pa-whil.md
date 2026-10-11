---
# qou-opjb
title: 'GAP: neutron-prediction-comparison displays p*(A) while naming n_pred(p), and its c = 0.01497 traces to an SEMF ratio, not to a definition in the corpus'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
    - split-from-6766
    - 8f-decide
created_at: 2026-10-10T08:12:47Z
updated_at: 2026-10-10T12:00:00Z
parent: qou-8lxd
---

Split out of `qou-6766` on 2026-10-10, which packed seven findings into its
title and therefore could not be claimed, worked or closed by anyone. Three were
enacted there; this is residual item (1) of four.

## The display mismatch, measured

`folio/quantum-observable-universe/observations/neutron-prediction-comparison.md`
is a **`proposition`** block. Its opening sentence promises one quantity and its
display defines another:

> "the beta-stability formula predicts a stable neutron number $n_{\mathrm{pred}}(p)$:"

then displays

```
p*(A) = A / (2 + c · A^{2/3}),    c = a_C / (2 a_A) = 0.01497
```

Different symbol (`n` vs `p*`), different argument (`p` vs `A`). The residual it
then reports is `|Δn|` (mean 1.7, max 8 at `p = 102, 103`).

**The parent proposition gives a different route, and the block skips it.**
`prop:beta-stability`
(`folio/quantum-observable-universe/nuclear-interactions/beta-stability.md`)
defines `p*(A) = A/(2 + a_C A^{2/3}/(2 a_A))` and then says: for a given `p`, the
stable mass number is the **fixed point** of `A*(p) = p(2 + (a_C/2a_A)·A*^{2/3})`,
with `n*(p) = A*(p) − p`. So `n_pred(p)` requires solving that fixed point. The
comparison block displays neither the quantity it names nor the route its own
parent specifies — it displays the parent's *first* formula, which is the inverse
map.

## The second defect, which is the one that needs the owner

**`c = 0.01497` is not derivable from the definitions the corpus states.**
`prop:beta-stability` gives `a_C = (q − q⁻¹)·λ_C` with **`λ_C` nowhere defined**,
and calls `a_A` "the Pauli asymmetry coefficient" with **no definition at all**.
So the numeral has to come from outside.

Arithmetic (circumstantial, not proof): the SEMF Coulomb and asymmetry
coefficients give `a_C/(2a_A) = 0.714/(2·23.7) = 0.015063`, 0.6 % from 0.01497;
at `a_A = 23.85` it is `0.014969`, matching to four digits. AGENTS.md's own
extensive-term section quotes `a_A` as "the SEMF asymmetry coefficient (23.7)",
so 23.7 is the value this corpus uses elsewhere.

If that is what it is, then under **§NO FITTING** this is the named case —
*"importing an empirical term … citing a phenomenological formula from the
literature (an empirical Wigner energy, an SEMF coefficient) imports somebody
else's fit"* — sitting inside a `proposition`, whose content is then a mean
discrepancy against observed isotopes across 103 elements.

## Options

1. **Trace `λ_C` and `a_A` and show `0.01497` is derived.** If it is, the
   objection dissolves and only the display mismatch remains. Cost: a corpus
   trace; this bean's author did not find a definition for either symbol.
2. **Keep the comparison, demote the block** `proposition` -> `remark` or
   `example`, state the SEMF import explicitly as an input. Cost: one `.ts` kind
   change plus label-reference updates; risk: the `prop:` label has consumers.
3. **Keep the kind, scope the claim** in prose as a comparison against an
   imported phenomenological ratio, not a prediction.
4. **Nothing.** The block keeps a proposition whose numeral's provenance is
   untraced and whose display defines the inverse of the quantity it names.

**Recommendation (agent judgement, not a finding):** do (1) first — it is cheap
and it decides between the others. If `λ_C`/`a_A` are genuinely undefined, (2).

**Default if unanswered: (4), nothing changes.**

**Blast radius:** `prop:neutron-prediction-comparison` +
`tbl:neutron-prediction-comparison-table-data` + its `-interpretation` sibling,
and whatever cites `prop:beta-stability`. Nothing in the mass / binding / Q_β
chain reads any of them.


## Option 1 EXECUTED 2026-10-10 — and it CORRECTS this bean's own central claim

Option 1 above was *"trace `λ_C` and `a_A` and show `0.01497` is derived"* —
measuring, not changing, so it needed no permission. Done. **The claim I wrote
above, that `λ_C` is "nowhere defined", is WRONG. Both coefficients are defined
and derived in the corpus**, and I did not find them because I searched only
`prop:beta-stability`'s own chapter.

`folio/quantum-observable-universe/lean/QOU/Interactions/QIntegerMassFormula.lean`
(mirrored at `mass-theory/q-integer-mass-formula.lean`, tabulated at
`mass-theory/mass-formula-regime-switching-table1-data.md`) defines all seven
mass-formula coefficients as products of quantum integers times `m_e`, with

```lean
q_int q n = (q^n - q^(-n)) / (q - q⁻¹)        -- line 27, BALANCED convention
lambda_C  = (q - q⁻¹) * q_int q 6 * m_e       -- line 42
a_asym    = 3 * q_int q 2 * q_int q 7 * m_e   -- line 46
```

So `a_A`, called "the Pauli asymmetry coefficient" with no definition in
`prop:beta-stability`, has a derived counterpart `a_asym` two chapters over. The
gap is **local to that block**, not corpus-wide.

### Measured, and the provenance question is NOT settled by it

Arithmetic in `decimal` at 50 digits (arbitrary precision, no float64), proton
pin `q₀ = 1.1099785827513808`, `m_e = 0.510998950690` MeV from the corpus's own
CODATA table (`qou_substrate/data/allascii.txt:109`):

| candidate provenance of `c` | value | vs the published `0.01497` |
|---|---|---|
| **published in the block** | `0.01497000` | — |
| **SEMF** `a_C/(2a_A) = 0.714/(2·23.69)` | `0.01506965` | **+0.67 %** |
| **corpus-derived** `λ_C/(2·a_asym)` | `0.01451583` | **−3.03 %** |
| the block's **own literal chain**, `a_C = (q−q⁻¹)·λ_C` | `0.00303468` | **−79.73 %** |

**Neither candidate reproduces `0.01497` exactly**, so the provenance is
undetermined; the SEMF reading is 4.5× closer. **Do not upgrade "4.5× closer"
to "it is the SEMF ratio"** — the two candidate inputs are themselves close
(below), so this margin does not cleanly discriminate.

### The hard finding, which does NOT depend on provenance

**The block's own stated formula, followed literally, misses its own published
numeral by 80 %.** `prop:beta-stability` writes `a_C = (q − q⁻¹)·λ_C`, while the
Lean `λ_C` **already contains** `(q − q⁻¹)`. Composing them double-counts `h`
and gives `c = 0.00303`. Reading `a_C ≡ λ_C` instead gives `0.01452`, 3 % away.
So one of the two is a transcription error, and that is an internal
inconsistency inside the corpus, independent of where the numeral came from.

### A separate and more interesting fact — and it is a POSTDICTION, stated as one

| | derived | SEMF | gap |
|---|---|---|---|
| Coulomb | `λ_C = 0.682437` MeV | `a_C = 0.714` MeV | **−4.42 %** |
| asymmetry | `a_asym = 23.50663` MeV | `a_A = 23.69` MeV | **−0.77 %** |

The framework's *derived* asymmetry coefficient `3[2]_q[7]_q·m_e` lands within
**0.77 %** of the empirical SEMF `a_A`. That is a postdiction of a textbook
phenomenological constant from `q₀` and two quantum integers, and it is the
reason the provenance question is not cheap: **the derived and empirical inputs
agree too well for a 3 %-vs-0.67 % comparison to settle which one was used.**

Register discipline, since this is exactly where it matters: this is a
comparison of a model quantity against a fitted literature constant, not
evidence that the framework derives nuclear masses. The corpus itself names
`a_A` as empirical — `computations/_deprecated/per_braid_tower_wigner.py:81`,
*"SEMF `a_A` is empirically 23.69 MeV"* — in a file whose own docstring reports
that its *categorical* asymmetry scale (hook product of `(3,1)`) gives
`~m_e·[4]_q·[2]_q ≈ 4.5` MeV, **an order of magnitude too small**. So the corpus
holds two different categorical candidates for this one coefficient, 5× apart,
and `a_asym` is the one that works.

### Revised options

1. **~~Trace `λ_C` and `a_A`~~ — DONE, above.** It did not dissolve the
   objection; it relocated it.
2. **Fix the formula, which is now the narrowest real defect.** Make
   `prop:beta-stability` state `a_C` consistently with the Lean `λ_C` (drop the
   duplicated `(q − q⁻¹)`, or rename), and cite `a_asym` where it says "the
   Pauli asymmetry coefficient". Then **recompute `c` and publish what the
   derived chain actually gives** (`0.01452`), with the residual `|Δn|` that
   follows. Cost: two prose edits plus a re-run of the comparison table. Risk:
   the mean `|Δn| = 1.7` will move; that is the point.
   **Recommended (agent judgement)** — it replaces an untraced numeral with a
   derived one and makes the postdiction above visible instead of hidden.
3. **Keep `0.01497`, declare the SEMF import explicitly**, and demote the block
   from `proposition` (per §NO FITTING, an imported phenomenological constant is
   somebody else's fit and does not belong in a provable kind).
4. **Nothing.** The block keeps a numeral that neither candidate chain
   reproduces and a formula that misses it by 80 %.

**Default if unanswered: (4).** Nothing numerical moves elsewhere — no witness,
no Lean, no compute reads this block.

### And the display mismatch is unchanged

Everything in the first section still stands: the block names `n_pred(p)` and
displays `p*(A)`, the inverse map, while its parent reaches `n*` through the
fixed point `A*(p) = p(2 + (a_C/2a_A)·A*^{2/3})`, `n* = A* − p`.


## 2026-10-10 — the owner asked "but lean proved?". ANSWER: NO. Half enacted, numeral HELD.

Owner leaned to option 1 and asked whether the derived chain is Lean-proved.
Measured, and it is not — this is the sorry-free-≠-derived distinction one step
further back, because there is no theorem to be sorry-free *about*.

| object | what it is |
|---|---|
| `lambda_C = (q - q⁻¹) * q_int q 6 * m_e` | **`noncomputable def`**, `QIntegerMassFormula.lean:42`, `-- Ref: [manuscript] Ch 11 §8` |
| `a_asym = 3 * q_int q 2 * q_int q 7 * m_e` | **`noncomputable def`**, line 46, same Ref |
| `asym_volume_relation` | theorem, `a_asym = (3/2)·lambda_V`, discharged by `unfold; ring` |
| `exchange_coulomb_relation` | theorem, discharged by `unfold; field_simp` |

Both theorems are **true by definition** — `3[2][7]` against `2[2][7]`, and an
identity after clearing denominators. AGENTS.md Strict Lean Discipline item 8
names exactly this: *"if it's true by definition / by unfolding / by `rfl`, then
it is not a theorem — it is notation."* **Nothing derives the assignments
`[6]_q` or `3[2]_q[7]_q`.** They are asserted in Ch 11 §8.

**And the file's conjecture class is laundered, which is worth knowing before
building on any of it.** Its own 2026-08-24 correction note (bean `qou-hjf4`)
records that `IsAMEValue` carries a third field `fits_bound` — docstring
*"Trivialized bound hypothesis to close sorry"* — asserting the 1 % agreement
outright, so `fits_AME_conditional` reduces to `∀ …, [claim] → [claim]`.
`canonical` was demoted `instance` → `def` to stop it reading as established,
and its `f_magic := fun _ => 0` means that model zeroes every magic correction.

### What landed (both change ZERO numbers, both corpus-derived)

1. **`prop:beta-stability` no longer double-counts $(q-q^{-1})$.** It wrote
   `a_C = (q - q^{-1})·λ_C` while the Lean `λ_C` already contains that factor;
   following the block's own chain literally gives `c = 0.00303468`, **80 % off
   its own published 0.01497**. It now states
   `a_C = λ_C = (q-q⁻¹)[6]_q m_e` and `a_A = a_asym = 3[2]_q[7]_q m_e`, with a
   line saying the factor appears once. This is the §7aa exemption-2 case — the
   convention is declared one file over and violated here.
2. **The comparison block's prose no longer promises what it does not show.** It
   now says the display is the beta-stability *line* `p*(A)` and that
   `n_pred(p) = A*(p) − p` comes from inverting it through the fixed point
   `A* = p(2 + c·A*^{2/3})`.

### What is HELD, and what unblocks it

Republishing `c = 0.01451583` and re-running the `|Δn|` table. That swaps an
untraced numeral for a **definitionally-asserted** one — better, not a
derivation — and it moves a reported figure (`mean |Δn| = 1.7`). One word
enacts it. The full measurement is now an `authorNotes` caveat on
`prop:neutron-prediction-comparison` so it is readable without this bean.

**The honest framing for whoever enacts it:** label `c` as fixed by the
q-integer coefficient *assignments* of Ch 11 §8, not as derived. And do not
quote the `a_asym = 23.50663` MeV vs SEMF `a_A = 23.69` MeV agreement (0.77 %)
as evidence for the framework — `a_asym` is a chosen monomial in q-integers, so
that is a postdiction of an empirical constant by an assignment, which is
exactly the comparison §NO FITTING says to rank below a derivation.
- 2026-10-11 (after #7652 merged): measured the source of `tbl:stability-cubic-plot-table-data`. Tried p = A/(2 + k·c·A^{2/3}) for k ∈ {1/2, 1, 2, 4} at both c (mpmath, 30 dps). Best is k = 1 (the probe's inversion), total |ΔN| over the 14 rows = 24 (old c) / 26 (new c). No variant gives N = 20 for Ca (all give 22–38), while the table's N_pred column equals its N_obs column in 10 of 14 rows. So N_pred is not produced by this c under any of these normalisations, and the block's "ΔN is zero up to iron, at most 2 everywhere" is not reproducible. Owner decision pending.


## 2026-10-10 — owner decision 1b ENACTED: `c = λ_C/(2·a_asym) ≈ 0.01452` published, labelled "assigned, not derived"

Ruling (ofri): option (b). Done on branch `claude/opjb-neutron-constant-2026-10-10`.

- **Constant.** `c = (q₀−q₀⁻¹)[6]_{q₀} / (6[2]_{q₀}[7]_{q₀}) = 0.0145158337165852716…` at the proton pin
  (`qou_substrate.constants.q_at`), balanced q-integers, `m_e` cancels. Prose says it is
  "fixed by the q-integer coefficient assignments of Ch 11 §8, not derived".
- **New producer** (the table never had one):
  `computations/observations/neutron_prediction_comparison_probe.py` + witness
  (`q0Anchor: proton`), mpmath 60 dps. It also states the observation rule for the
  first time: `n_obs(p)` = N of the most abundant isotope (NUBASE2020 `IS=`, parsed from
  `library/kondev-2021-…/sections/`), else the longest-lived ground state.
- **Result, reported as it came out:** mean `|Δn|` **1.7 → 1.8155 (worse)**, max **8 → 7**
  (now at p = 52, Te; ¹³⁰Te is far on the neutron-rich side). Bins 0/1/2/3/4/5–7 =
  16/34/25/16/8/4 (sum 103). Under the same observation rule the OLD c gives 1.7961, max 8
  at p = 102, so the published 1.7 also depended on an unstated observation table, not
  only on the constant. (That old table was inconsistent anyway: its `5–8` row listed 7
  elements against a count of 4.)
- **Still carry 0.01497, outside this ruling's scope:** `observations/stability-cubic-plot.md`,
  `predicted-spectra/elliptic-stability-locus.md` (its erbium `p ≈ 67.8` estimate), and the
  Lean sibling `neutron-prediction-comparison.lean` (`asymmetry_coeff`; its
  `predicted_mass_number` uses yet another inversion). Leaving them is an owner call.
- Display mismatch (first section): already resolved in the prior entry.

## 2026-10-10 follow-up (owner picks "1 2")

- New c ≈ 0.0145158337 now in `observations/stability-cubic-plot.md` and the Lean sibling `observations/neutron-prediction-comparison.lean` (`asymmetry_coeff`; docstrings now quote the probe witness: mean 1.8155, max 7 at p = 52). lean-direct `-DautoImplicit=false -s 65536` exit 0.
- NOT changed: `predicted-spectra/elliptic-stability-locus.md`. Its claim "p ≈ 67.8 (erbium)" does not follow from its own equation p² = (1−c)/(4c³) at either c: 270.93 (c = 0.01497), 283.81 (new c). The elimination step itself is also off: with z = −(2cp+1), z²+1 = 4c²p²+4cp+2, not 4c²p²+1; the corrected condition 4c³p² + 4c²p + 2c − 1 = 0 gives p ≈ 237.5 at the old c. No reading gives 67.8. Owner decision pending.
- Also measured: the stated cubic t³ = 2p(1+ct²) does not reproduce `tbl:stability-cubic-plot-table-data` at either c (U: 218 vs 144 in the table). The inversion A = 2p + c·p·A^{2/3} comes closer but still misses (U: 145 old c, 143 new c, vs 144). The table's source is untraced. Not fixed.
- 2026-10-10 19:16Z owner picked "Correct it" for `elliptic-stability-locus.md`: elimination step corrected to 4c³p² + 4c²p + 2c = 1; the block now states p ≈ 249.4 at the new c (237.5 at 0.01497) and that this matches no observed nucleus; erbium sentence removed; `uses` gains prop:neutron-prediction-comparison. The conjecture itself is unchanged and still open. Still unfixed: item 2 of the conjecture writes z(p) = −1/(2cp), while the coefficient match gives z = −(2cp+1); and the stability-cubic table's source is untraced.
- 2026-10-11 owner picked 1: `tbl:stability-cubic-plot-table-data` regenerated from the probe witness by `computations/observations/stability_cubic_table_from_probe.py` (no new compute; reads the witness rows). The block now shows the prop:beta-stability cubic t³ = p(2 + ct²) at the new c and states the measured spread (14 rows: max 5 at Ba, mean 31/14; all p ≤ 103: mean 1.8155, max 7 at Te). NEW, not fixed: rem:diophantine-valley writes t³ = 2p(1 + ct²), twice the ct² term of prop:beta-stability, and the elliptic-stability-locus derivation uses that doubled form.
- 2026-10-11 owner picked 1+2 on the factor-of-2: resolved by deriving from the energy. Minimising a_C p²/A^{1/3} + a_A(A−2p)²/A gives p* = A/(2 + cA^{2/3}), c = a_C/(2a_A) = prop:beta-stability. integer-stability had a_A for 4a_A (and a_C = (q−q⁻¹)λ_C, double factor); diophantine-valley had 2c for c; elliptic-stability-locus inherited 2c. All three now follow beta-stability, with caveat authorNotes. Elliptic coefficient match now c³p² + 2c²p + 2c = 2, p ≈ 736.8. Provenance of 0.01497 found: computations/elliptic-stability.json carries a_C = 0.697, a_A = 23.29 (SEMF-type values), and 0.697/(2·23.29) = 0.01496. Still open in the elliptic block: z(p) = −1/(cp) vs match z = −(cp+1); pairing coefficient 2λ_P/a_A untraced.
- 2026-10-11: (D) in elliptic-stability-locus derived from integer-stability energy + pairing ∓λ_P/A^{1/2} (equal energy of ee (p,A) and oo (p+1,A)); result t³ − c p̄ t² − 2p̄ = (λ_P/(2a_A)) t^{3/2}, p̄ = p + 1/2 (sympy). Old coefficient 2λ_P/a_A was 4× too large. Open: z(p) = −1/(cp) vs match z = −(cp+1), owner decision.

## 2026-10-11 — conjecture restated at z(p) = -(cp+1) (owner pick 1, PR #7675)

Under X = t only the X^2 coefficient agrees; the X^1 coefficient c^2p^2+cp+1 never agrees for real cp; X^0 agrees only at p ~ 736.8 (checked with sympy). Upstream: item 2 now cites the color elliptic cubic (C), not the color-tube cubic; the Descartes discriminant -18.95 became -303.17 (standard -16(4a^3+27b^2), recomputed at the proton q0; j = 129.86 unchanged; see qou-3nva); the "shares algebraic origin (exact)" bullet was replaced. Downstream: the modular-s-transform-q-q-tilde link for prop:descartes-elliptic-curve now points at the right file; two Lean docstrings cited a conj: label and now cite rem:. The conjecture itself stays open.
