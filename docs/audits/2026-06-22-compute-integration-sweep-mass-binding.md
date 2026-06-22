# Compute-integration sweep — are the week's findings wired to mass & binding?

**Date:** 2026-06-22
**Window:** 2026-06-15 → 2026-06-22
**Method:** `local/compute-integration-watcher` (I1–I13). A finding is **WIRED**
only if a *production consumer* (`paper_six_term_isotope_sweep.py`,
`derive_m_p_hecke_full_tower_50dps.py`, `canonical_plus_multibrane.py`,
`m_p_borromean_verification_50dps.py`, `mass_formula_6term_mpfr_50dps.py`, the
L1/L2 dashboards) imports its producer, references its witness, or consumes its
derived constant — not a docstring mention, not a probe witness alone.

## Bottom line

**Zero of the week's compute findings are newly wired into production mass or
binding.** That is **by design, not a regression**: the week was a *refutation*
(z-Habiro Φ_q), *frontier probes* (A=3 ³He combiner, Pauli→Δ_λ, keystone), and
*hygiene* (CODATA→registry). The production mass/binding path is **stable and
unchanged in formula** — the canonical 6-term sweep + Hecke towers run on the
same upstream witnesses as before; the only consumer-script edits this week were
a CODATA-literal→registry routing (`5859630d`, ~9.4e-8 diagnostic shift) and
incidental plumbing. No upstream mass/binding witness was regenerated, and the
L1/L2 dashboards did not move.

The one production-adjacent gap is a **proof**, not a wire: the production tower
already uses the bounded Rogers `li2q`, but the lemma justifying it as the
correct real-q archimedean face of the merged `eulerCoeff` limit is still open
(see [the bounded-Rogers direction doc](2026-06-22-zhabiro-bounded-rogers-continuation-direction.md) §4).

## Per-thread verdicts

| Thread | Finding | Lean | Probe witness | Production consumer | Verdict |
|---|---|---|---|---|---|
| **z-Habiro Φ_q** (#2447/#2460/#2475/#2609, #2481) | Faddeev Φ_q per-generator brane-tower term | §3b-cond merged (`ZHabiroCauchy`) | ✓ `zhabiro-phiq-production-crosscheck`, `zhabiro-physical-z-pin` | ✗ none — production uses `li2q`; Φ_q regresses (−737 MeV) | **REFUTED-DIAGNOSTIC** |
| **z-Habiro Rogers** (#2609) | real-q saddle = `li2q` (the open justification lemma) | ✗ open (formalize-first) | ✗ (direction doc only) | `li2q` term *is* in production (predates this week) | **OPEN PROOF** — code correct, lemma unproven |
| **A=3 ³He combiner** (#2371, merged: `5890366e`/`8cf8015c`) | operator-form `A^λ` combiner reconstructs ³He χ^λ @50dps | §3b-cond stub | ✓ `binding-a3plus-joint-ji-combiner` | ✗ canonical sweep reads `atomic-tr-m-mpfr-50dps` (T1), not the A=3 result | **PROBE-ONLY** (merged ≠ wired) |
| **Pauli → Δ_λ** (#2461) | weighted-channel / Δ_λ binding decomposition | §3b-cond candidate | ✓ `probe-pauli-young-delta-lambda-*` (diagnostic) | ✗ sweep uses baseline form | **PROBE-ONLY** |
| **Keystone S5-SO3 / Habiro-WRT** (#2488/#2503/#2521/#2524, `ed4b0450`) | Lawrence–Zagier false-theta on Σ(2,3,5) vs W_λ | research-boundary | ✓ `keystone-habiro-wrt-s3-2i` (states *"no fit; nothing wired"*) | ✗ none (frontier-sharpening) | **PROBE-ONLY / FRONTIER** |
| **CODATA registry + over-count** (`46ke`, `j1hg`) | route 46 hardcoded literals → `codata_constants.py`; triage 34 over-count FPs | n/a | ✓ `canonical-script-input-audit` | touched consumers (`…:1325` 938.272→`M_P_MEV_VALIDATION`) — *constant source only* | **AUDIT/HYGIENE** (I9 cleanup, no formula change) |
| **A=5 ⁵He** (#2492); **qbeta c_k/c4** (#2474/#2414/#2106) | tower / Q_β probes | — | — | — | **not confirmed in window** — almost certainly PROBE-ONLY (qbeta c_k is a long-running probe saga; not re-verified here) |

## Production-stability evidence

- `paper_six_term_isotope_sweep.py:139` reads `atomic-tr-m-mpfr-50dps.witness.json`
  (T1) and `term6-habiro-residue-mpfr-50dps.witness.json` (T6) — neither
  regenerated this week.
- `git log --since=2026-06-15` on the consumer scripts shows only `5859630d`
  (CODATA→registry routing) + `d6ac02a3` (keystone-scaffold incidental touch);
  no formula edit, no witness regen.
- grep for `a3plus` / `operator-form` / `joint-ji-combiner` in the canonical
  mass/binding consumers → **no match** (confirms A=3 PROBE-ONLY).
- A large batch of exploratory witnesses (`atom-mass-*`, `brane-tower-*`,
  `alpha-em-*`, `binding-*`) was moved to `computations/_deprecated/` this week
  — actively pulled *out* of the tree.

## Wiring the two production-adjacent leads

### 1. z-Habiro Rogers saddle lemma — SCAFFOLDED (Lean conjecture-class)

Production already runs the bounded Rogers `li2q`; the missing deliverable is
the *proof* that it is the correct real-`q` archimedean saddle of the merged
`eulerCoeff` (Faddeev) limit. Now scaffolded as a formalize-first conjecture
class `QOU.BraidKnot.ZHabiroRogersSaddle` in `QuantumDilogarithm.lean`, reusing
the file's existing `phi_q` (Faddeev face) and `towerTerm = -li2_q(-|·|)`
(Rogers production face), with two **non-vacuous** conditional corollaries
(`realQSaddle_phi_q_at_zero`, `realQSaddle_phi_q_ne_phi_q_at_zero`) that compose
the conjecture with the proven `towerTerm_at_zero` / `phi_q_at_zero`. The
`saddle_phi_q_eq_towerTerm` field is the open conjectural input (the AJ-saddle
identification, open for `𝓑₃`). A full proof is research-grade
(saddle-point / Stokes); this turns the prose conjecture into a typed Lean
object that downstream can depend on conditionally. *(Local Lean verify
unavailable — olean restore failed and a from-source build would storm Mathlib;
the additions mirror verified idioms in the same file, but CI / lean-direct must
confirm elaboration.)*

### 2. A=3 ³He operator-form combiner → binding: BLOCKED at the Δ_λ gate

The A=3 combiner (`binding_a3plus_joint_ji_combiner.py`) is a Path-D-style
binding combiner — `S_joint(K) = |Σ_λ y_λ dim_λ (z_atom_λ − z_free_λ)|` (joint
J⊕I rotation⊕growth eigenvalues, *no fits*; ³He +17.4% vs the `Σ|Δθ|`
baseline). It produces the χ^λ / per-block eigenvalue ingredients, but
production binding is `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ`, and the gate is **Δ_λ**, not
the combiner.

Per the **2026-06-20 binding-gate stocktake**, *no binding path is closed*, and
the Δ_λ family (Path D) is open with every probed closure refuted:
- 6 Δ_λ ansätze failed; the 2026-05-26 "deuteron closure" was **retracted**
  (−82.9% on Path D).
- This week, independently: the **qbk2** q-Bessel quadratic-action correction
  collapsed to **20–80× too small** under the *forced* `y_λ` measure; the
  **ν_SDP** reading (Path C) has no computable definition.
- The operator route reduces to the LP **𝓑₃-selection**, and (2026-06-17)
  **both** remaining directions — close the 𝓑₃-selection gate, and the
  α-cluster recursion sidestep — are **negative**: no continuous variational
  principle selects the Borromean signature (the SDP returns the trivial
  `tr_M=0` / mesonic channel).

**Verdict:** the A=3 combiner is *ready as an ingredient* but **cannot be wired
to production binding** — the blocker is the Δ_λ / 𝓑₃-selection gate, which is
open and whose every probed shortcut (including this week's two) is refuted.
Per AGENTS.md, **do not propose a 7th fit-based Δ_λ ansatz**; the productive
directions are GAP-A-3 / GAP-A-4 (categorical brane-tower level selection / ρ
general rule) and Option E (Kashiwara crystal). Wiring the combiner is therefore
*not* the actionable step — closing the gate is, and that is research-grade.

## Caveats

- **Validate could not run** in this checkout (`folio-assistant/schemas/` absent)
  — the content edits on #2609 await CI confirmation.
- The A=5 and qbeta-c_k threads were not fully resolved within the 7-day window
  by the sweep; classified provisionally as probe-only.

## Cross-references

- `.claude/skills/local/compute-integration-watcher.md` (I1–I13 method)
- [`2026-06-22-zhabiro-bounded-rogers-continuation-direction.md`](2026-06-22-zhabiro-bounded-rogers-continuation-direction.md)
- [`2026-06-18-zhabiro-physical-z-pin-and-wiring-verdict.md`](2026-06-18-zhabiro-physical-z-pin-and-wiring-verdict.md)
- consumers: `computations/sweeps/paper_six_term_isotope_sweep.py`,
  `computations/derive_m_p_hecke_full_tower_50dps.py`,
  `computations/canonical_plus_multibrane.py`
- dashboards: `computations/onepb-status-dashboard.witness.json`,
  `computations/per-observable-100x-status.witness.json`
