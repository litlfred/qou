# 210× scale-gap — third pass: it's a symptom of two acknowledged discipline gaps

> **Status (2026-05-18, third pass).** PR #772 was closed without merging.
> An interim v2 (this file) initially reframed the gap as "Borromean
> derives m_p to 1 ppm without using |tr_M|" — that framing is **also
> wrong**, because `λ_scale` in the Borromean form is currently a
> hardcoded literal solved against CODATA m_p (cheat-sheet §5 Migration
> Backlog #1; §8 pitfalls #1). This third pass corrects both #772 and
> the interim v2.

## TL;DR

The 210× ratio `(m_p / |tr_M(p)|) / E_0 ≈ 881 / 4.186 ≈ 210` is a
**symptom of two acknowledged discipline gaps** in the production
m_p chain:

1. **CAL-4 violation via hardcoded `λ_scale`** — the Borromean rest-
   mass form `m(B) = m_e · [Vol(𝓑₃)/ℏ_q² · λ_scale + S(B)]` uses
   `LAMBDA_PROTON_DOC = 2.4599527869` and `LAMBDA_NEUTRON_DOC =
   2.4633436333`, both literally solved against CODATA m_p and m_n.
   This is **Migration Backlog #1** in
   [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
   and is explicitly flagged as a **3-calibration discipline
   violation**. The proposed first-principles replacement
   (`conj:lambda-scale-bring-bloch-identity`) has been **empirically
   refuted in the hyperbolic-knot basis** — Bring-Bloch tier 0–5
   PSLQ searches at 100 dps over 52 prime hyperbolic knots through
   11 crossings, coefficient ≤ 10³⁰, returned NO integer relation
   (per tier 5 conclusion: "genuinely transcendental" in the tested
   basis; PR #904 demoted the block to `conj:`). The remaining
   research direction is the **q-dilog tower** route.

2. **20 production scripts still import SUPERSEDED `mass_endomorphism.py`** —
   Migration Backlog #2 in the same cheat sheet. The new
   `prop:mass-tower-operator-valued` block has 2-factor verification
   only; the (Z+N) extension blocks migration of `build_proton_mass_50dps_chain.py`,
   `mass_formula_6term.py`, `mass_at_3A_proper.py`, and ~17 more.

The 210× factor itself, computed as `m_p / (|tr_M(p)| · E_0^lept)`,
has a structural interpretation (§"What 210× actually measures"
below), but **the existing cheat sheet already documents the
underlying issues**. This audit's value-add is calling out that
*both* PR #772 *and* the interim v2 misframed the symptom.

## What the cheat sheet already says (and why we should not re-litigate it)

[`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
§5 — Compute-pipeline migration backlog:

| # | Action | Where | Risk |
|---|---|---|---|
| 1 | Replace `LAMBDA_PROTON_DOC / LAMBDA_NEUTRON_DOC` literals with `conj:lambda-scale-bring-bloch-identity` derivation | `m_p_borromean_verification_50dps.py` | **3-calibration discipline violation; production m_p chain uses calibrated literal** |
| 2 | Migrate 20 importers of SUPERSEDED `mass_endomorphism.py` to the new `mass_tower_operator_valued` API | 20 scripts | SUPERSEDED dependency in production |

§8 — Common pitfalls:

> "Hardcoded literal values where a categorical derivation exists →
> **discipline violation**. Example: `LAMBDA_PROTON_DOC = 2.4599527869`
> should derive from `conj:lambda-scale-bring-bloch-identity`."

> "Calibration parameters not in the 3-input set →
> **4th-calibration violation**."

The 210× scale gap is a **downstream symptom** of these two known
issues. Closing the backlog items closes the symptom.

## What 210× actually measures (structural reading)

Defining `E_0^lept ≜ m_e / (q_0·(q_0-1))` ≈ 4.186 MeV (leptonic
energy quantum, cheat-sheet step 9 first branch) and treating it as
the would-be multiplier on `|tr_M(p)|`:

```
naive: m_p_pred = |tr_M(p)| · E_0^lept ≈ 1.065 · 4.186 ≈ 4.46 MeV
actual: m_p_CODATA ≈ 938.27 MeV
ratio: 938.27 / 4.46 ≈ 210.5
```

The 210× gap is the answer to "by how much would a naive
`|tr_M| · E_0^lept` pairing under-predict m_p?". Two
structurally-distinct frameworks both reproduce m_p, neither
through this naive pairing:

- **Cheat-sheet step 9 (binding/decomp framework)**:
  `B(K) = m_e · ρ · [|tr_M(T_w)| + tower(T_w) + tr_M(C_{dim_q})]`.
  This is **binding energy**, not absolute rest mass. The `ρ`
  factor (categorical density) absorbs the magnitude scale; the
  bracket sum is `O(1)`. `|tr_M|` enters but multiplied by
  `m_e · ρ`, not by `E_0^lept`.

- **Borromean rest-mass formula**:
  `m(B) = m_e · [Vol(𝓑₃)/ℏ_q² · λ_scale + S(B)]`.
  Here `Vol(𝓑₃)/ℏ_q² ≈ 746` already supplies the bulk of the
  1836 ratio; `λ_scale ≈ 2.46` is a small multiplicative
  correction that **currently absorbs the residual** to hit
  CODATA. `|tr_M|` does not appear.

Neither framework predicts m_p via `|tr_M| · E_0^lept`. The 210× is
not the gap between two competing formulas — it's the gap between a
**naive ansatz** that nobody in the production chain actually uses
and **either** of the two production frameworks.

## What is independent of the CAL-4 issue (and what isn't)

| quantity | currently derived without fitting? |
|---|---|
| `m_p` absolute value | **No** — uses `λ_scale` literal (Migration Backlog #1) |
| `m_n` absolute value | **No** — uses `λ_scale` literal (Migration Backlog #1) |
| `m_n − m_p` difference | **Conditionally yes** — under the common-scale conjecture (one `λ_scale` for both p and n), Borromean form predicts ΔS = (m_n − m_p)/m_e from CAL-1 + CAL-2 + Vol(𝓑₃) alone (per [`rem:delta-skein-substrate-identity`](../../content/quantum-observable-universe/braids-and-knots/delta-skein-substrate-identity.md)). The 1015 ppm agreement with CODATA is **not** independent evidence for the conjecture — it is consistent with the existing substrate Q_β ansatz's own ~760 ppm residual at the current q_0 pinning. |
| `m_μ / m_e` (CAL-2) | **Yes** — `Vol(4_1)/ℏ_q²` (figure-8 sector, no calibration) |
| `Q_β` | calibration input (CAL-3) |
| `B(K)` binding energies | uses `|tr_M|` chain; `B(K)/B(reference)` ratios are CAL-4-free; absolute scale relies on the same fitted normalisation chain |

So: the **first-principles content** of the Borromean form is the
**common-scale hypothesis** that one `λ_scale` covers both p and n
(producing ΔS = m_n − m_p as a substrate-derived prediction). The
**individual values** m_p and m_n are still CAL-4-anchored.

## Why PR #772 was right about the symptom but wrong about the diagnosis

PR #772 framed the 210× as "missing `ρ_K` structural factor" and
"between three distinct E_0 notions." The correct diagnosis:

| #772 claim | Corrected |
|---|---|
| "Production formula: `M_pred = ρ_K · m_e · |tr_M|`" | `ρ_K · m_e · |tr_M|` is a leading-order *atomic* aggregator in `atomic_mass_via_rho_k.py` and is tautological. Production rest mass is Borromean; production binding is `m_e · ρ · [|tr_M| + tower + tr_M(C)]` (cheat-sheet step 9). |
| "Cited `mass-endomorphism-tower` + `e_0_full_mev`" | That block IS SUPERSEDED (`fd54c89b2` → `mass-tower-operator-valued`). But the SUPERSEDED structure was also a `|tr_M|`-based binding-decomposition; it didn't predict absolute m_p either. The supersession is about correctness of the binding decomposition (Li_2^q vs operator-valued), not about which framework predicts m_p. |
| "210× gap is between three E_0 notions" | The 210× factor is the ratio between a **naive `|tr_M| · E_0^lept` pairing** (which nobody actually uses) and CODATA m_p. The two production frameworks each work, neither uses the naive pairing. |
| "Add ρ_K structural factor to fix" | No — `ρ_K` is downstream (atomic aggregation); it doesn't fix anything at the baryon level. The real fix is **resolve the CAL-4 in `λ_scale`** (Backlog #1). |

## Why the interim v2 of this file was also wrong

The interim v2 claimed:

> "Vol(𝓑₃)/ℏ_q² · λ_scale = 1836.1527 vs CODATA m_p/m_e = 1836.15267,
> diff −1.79e-6 — so the Borromean form delivers m_p/m_e to ~1 ppm."

This is **circular**. `λ_scale = 2.4599527869` is `LAMBDA_PROTON_DOC`
in [`m_p_borromean_verification_50dps.py:100`](../../computations/m_p_borromean_verification_50dps.py),
and the script's own header (line 31) states:

> "With λ_scale fixed at the CODATA closure target 2.4599527869"

So `Vol(𝓑₃)/ℏ_q² · λ_scale = m_p/m_e` is a tautology by construction
of `λ_scale`. The "1 ppm" agreement is round-trip, not derivation.

What's NOT circular in the Borromean framework: under the
**common-scale hypothesis** (same `λ_scale` for p and n), the
identity `ΔS = (m_n − m_p)/m_e` is substrate-derivable from
{m_e, q_0, Vol(𝓑₃)} alone, with no fit to m_p or m_n
individually. The 1015 ppm agreement with CODATA, however, is
**not independent evidence** for the common-scale conjecture —
per [`rem:delta-skein-substrate-identity`](../../content/quantum-observable-universe/braids-and-knots/delta-skein-substrate-identity.md)
it is consistent with the existing substrate Q_β ansatz's own
~760 ppm residual at the current q_0 pinning. The first-
principles content of the Borromean form is the *structure* of
the orientation-difference identity, not yet a falsified
prediction.

## Migration status (answers to "are all refs migrated?")

**Block references** — `prop:mass-endomorphism-tower` appears in
**15 `.ts` files** (excluding the SUPERSEDED block's own
`mass-endomorphism-tower.ts` and the replacement
`mass-tower-operator-valued.ts` which mentions the old block
only in its supersession note):

- All 15 list it in `uses[]` arrays:
  `alpha-cosh-h-z-step-correction.ts`, `alpha-k-categorical-closure.ts`,
  `block-multiplicativity-v-free.ts`, `interface-knot-markov-z.ts`,
  `mass-endomorphism-jet-tower.ts`, `per-braid-mass-tower.ts`,
  `phi-q-resums-trace-series.ts`, `phi-q-tower-algebraic-stratification.ts`,
  `phi-q-tower-jsj-bridge.ts`, `quantum-dilogarithm-disambiguation.ts`,
  `six-term-per-derivation-weights.ts`, `stable-atom.ts`,
  `bw-empirical-misses.ts`, `three-calibration-discipline.ts`,
  `tower-binding-energy.ts`.
- 2 of those 15 also list it in `interprets:`
  (`mass-endomorphism-jet-tower.ts`, `phi-q-resums-trace-series.ts`).
- ~60 in-prose `[…](#prop:mass-endomorphism-tower)` links across `.md` files.
- ~12 `Ref: [manuscript] prop:mass-endomorphism-tower` lines across
  `.lean` files (under `lean/QOU/...`).

Most in-prose links can be either updated to `mass-tower-operator-valued`
or left in place (the SUPERSEDED block still exists with a pointer
banner). **`uses[]`/`interprets:` references should be migrated** to
keep the dep graph honest.

**Compute** — 20 scripts still import the SUPERSEDED
`mass_endomorphism.py` API. From Migration Backlog #2: blocked on
extending the new `mass_tower_operator_valued` verification from
2-factor to (Z+N).

**Cheat sheet** (this file's parent doc) — references both old and
new block in different sections; the §5 backlog item explicitly tracks
the migration debt.

## Recommended Bucket D rewire (revised)

For probe scripts that pair `|tr_M|` with an `E_0`:

- **Don't** wire `|tr_M| · E_0^lept` as a mass predictor — the 210×
  gap will manifest at every nucleon.
- **For rest mass**: use the Borromean form (per `derived_masses.py`)
  with the understanding that `λ_scale` is currently a calibrated
  literal (Backlog #1).
- **For binding-energy decomposition**: `|tr_M|` enters the
  cheat-sheet step 9 binding formula
  `B(K) = m_e · ρ · [|tr_M(T_w)| + tower(T_w) + tr_M(C_{dim_q})]`,
  not as a multiplier on `E_0^lept`.

## Action items downstream of this audit

1. **Track Migration Backlog #1** (resolve CAL-4 via a derivation
   of `λ_scale`). The `bring_bloch_tier{0..5}_search_m_p.py`
   scripts (hyperbolic-knot-basis PSLQ) **returned consistent
   negatives**; `conj:lambda-scale-bring-bloch-identity` was
   correspondingly demoted to a conjecture in PR #904. The
   remaining first-principles direction is the **q-dilog tower**
   route; closing it would resolve the 210× symptom.
2. **Track Migration Backlog #2** (migrate 20 scripts off SUPERSEDED
   `mass_endomorphism.py`). Blocked on (Z+N) extension of the new API.
3. **Block-graph hygiene**: update `uses[]` and `interprets:` arrays in
   the 15 `.ts` files that still reference `prop:mass-endomorphism-tower`,
   so the dep graph reflects the canonical block (`mass-tower-operator-valued`).
4. **Don't** wire any new "fix" for the 210× symptom — it dissolves
   automatically once #1 and #2 close.

## Cross-references

- [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
  — Migration Backlog §5; common-pitfalls §8 (already documents both
  issues).
- [`conj:borromean-baryon-mass-formula`](../../content/quantum-observable-universe/braids-and-knots/borromean-baryon-mass-formula.md)
  — formula with `λ_scale` as conjectural common-scale; "why this is a
  conjecture, not a fit" section discusses the ΔS independence.
- [`conj:lambda-scale-bring-bloch-identity`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-bring-bloch-identity.md)
  — proposed first-principles derivation of `λ_scale`.
- [`prop:mass-tower-operator-valued`](../../content/quantum-observable-universe/braids-and-knots/mass-tower-operator-valued.md)
  — Stage-1 unblock of SUPERSEDED `mass-endomorphism-tower`.
- [`prop:atom-knot-mass-derivation`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)
  — cheat-sheet step 9 source.
- [`computations/m_p_borromean_verification_50dps.py`](../../computations/m_p_borromean_verification_50dps.py)
  — production verification using hardcoded `LAMBDA_PROTON_DOC` (line 100).
- [`computations/probe_neutron_gap_round2.py`](../../computations/probe_neutron_gap_round2.py)
  — probe whose `E_0 = m_p / |tr_M(p)|` setup surfaces the 210×
  artifact.

## Provenance

| pass | framing | error |
|---|---|---|
| PR #772 (closed) | "ρ_K is the missing structural factor" | wrong production path; cited SUPERSEDED block |
| Interim v2 (this file's first draft) | "Borromean derives m_p to 1 ppm" | circular — `λ_scale` was fitted to m_p |
| **This pass** | 210× is a symptom of Migration Backlog #1+#2 (CAL-4 in `λ_scale` + SUPERSEDED `mass_endomorphism.py` deps) | — already documented in cheat sheet; audit just amplifies |
