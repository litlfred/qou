# A scalar per step: why the γγ strand-tower route cannot derive a magnitude

Producer: `gg_scalar_per_step_probe.py` · witness: `gg-scalar-per-step.witness.json` ·
**8/8 checks** · exact over ℚ(q), q₀ values at 70 dps · beans `qou-cds1`, `qou-99qc`, `qou-ales`.

**This is a re-derivation record, not a pre-registered search.** The invariants
were first surfaced by an adversarial review of two candidate constructions
(PR #7817); they are re-derived here against the corpus's own
`gg_ntower_probe.Rep` / `tr` / `y_lambda` so the result rests on corpus
machinery rather than on a reviewer's reimplementation. **Nothing is searched,
selected, adopted or re-scored.**

## What was asked, and what was missing

Owner, 2026-10-10: *"Find what element or functional supplies a factor above 1 on
the ruled base."* Owner, 2026-10-11: *"go through γγ production step by step to get
to one and two nucleons; each collision/interaction shifts things up the tower."*

`gg_ntower` answered the **braid-vertex** half with outcome (ii): with
`V_i = σ_iσ_{i+1}⁻¹` and a rigid shift, no placement but `s = 0` — which does not
climb — is admissible up to `n = 9`. Its results doc lists what it did not test,
including **pair creation by Jones projections (two strands per collision)**. That
is the physically natural γγ vertex: γγ → e⁺e⁻ creates two particles rather than
braiding existing ones.

The vertex is **forced, not chosen**. σ has eigenvalues `q` and `−q⁻¹`
(§7a Hecke-Skein), so `e_p = (q·1 − σ_p)/(q + q⁻¹)` projects on the antisymmetric
channel and is the unique `U_q(sl₂)`-invariant cup. Check **S** confirms it is
idempotent and that `σ_p e_p = −q⁻¹e_p`, `σ_p⁻¹e_p = −q e_p`, exactly, on every
two-row block at `n = 3,4,5`.

## The three invariants

| | statement | scope verified |
|---|---|---|
| **I1** | `e₀e₂ · Σ₁ = q² · e₀e₂`, `Σ₁ = σ₁σ₀σ₂σ₁`, **both sides** | all 7 two-row blocks, `n = 4,5,6` |
| **I2** | `tr_M(y · e_m) = tr_M(y) / [2]_q²` for `y ∈ H_m` | 7 words, `n = 3,4,5` |
| **I3** | `tr_M(V₀³ V_j³) = tr_M(V₀³)²` | `j = 2` (chain) **and** `j = 3` (disjoint) |

Each residual is **exactly 0** over ℚ(q), not small.

**I1 is the new one.** The cabled crossing on a double singlet is the scalar `q²` —
the two-strand analogue of the already-sorry-free `mul_jonesIdempotent`
(`σ_p e_p = −q⁻¹e_p`).

**I3 is stronger than the corpus's own `explanation.md`**, which claims
multiplicativity only for the disjoint `s = +3` case. It holds for
one-strand-sharing too, on a *published* element (#7733's `s = +2, k = 2` row):
`tr_M(V₀³) = 0.99856216383678726595`, and both products give
`0.99712639504640677422`.

## The closure

I1 gives `e₀e₂ · Σ₁^c = q^{2c} · e₀e₂` immediately, so

> **`tr_M(e₀e₂ Σ₁^c) = q^{2c}/[2]_q⁴ = q^{4+2c}/(q²+1)⁴`**

— verified against the closed form at every `c = 1…8`, with the step ratio
**exactly** `q² = 1.2320524541667639313`:

| c | `tr_M` at q₀ | closed form | F vs `\|tr_M(Δ_S)\|` |
|---:|---|---|---|
| 1 | 0.075347701481 | match | 0.709 |
| 2 | 0.092832320526 | match | 0.874 |
| 3 | 0.114374288330 | match | 1.077 |
| 4 | 0.140915122630 | match | 1.326 |
| 5 | 0.173614822666 | match | 1.634 |
| **6** | 0.213902568345 | match | **2.013** |
| 7 | 0.263539184282 | match | 2.481 |
| 8 | 0.324694098764 | match | 3.056 |

`F_required = 1.75923699418` on the order-zero `E₀` base, so the family passes
**through** the requirement between `c = 5` and `c = 6`.

## 🛑 The consequence: reading 3 is magnitude-blind

**Reading 3 admits every `c`.** Frobenius positivity on every block with
`y_λ > 0` — the criterion ruled canonical 2026-09-12, scoped to the whole word
2026-09-13 and to every strand count 2026-10-12 — imposes **no bound** on a knob
along which `tr_M` grows without limit.

Measured three independent ways, two of them here:

1. **this family** — admissible at every `c = 1…8` while `tr_M` grows as `q^{4+2c}`;
2. **the sibling pair-creation construction** — 10 of 12 configurations admissible
   across a 7.6× magnitude range, all far short, with `χ_(3)(R_3) = 0` *exactly*
   for all 12 so the trace collapses to a single scalar anyway;
3. **the composed tower** — already on record as *"rejects nothing and admits
   everything H₃ rejected"*, with non-monotone thresholds.

So **choosing the `c` that clears 1 is selection against the target** — which
§NO FITTING names outright: *"sweeping a discrete parameter for accuracy is a
fitted parameter."* No `c` is adopted here.

## Scope, stated per §"Before declaring refuted"

**Scope (b) — a structural exclusion with a named invariant**, for the stated
class only:

> Every "fresh strands per collision" γγ construction whose collisions are joined
> by a chain (I3) or by a cabled double singlet (I1) contributes **a scalar per
> step**. The family is geometric, its step index is a free unbounded knob, and a
> magnitude-blind criterion cannot fix it.

This upgrades the route from *"insufficient magnitude"* (scope a) to a closure
with a citable invariant — the reusable-negative form §"a gap is information"
asks for.

**What it does NOT close.** It delivers **no nucleon** — no quark letters, no
flavour, no two-nucleon level — so it answers the *mechanism* half of the
2026-10-11 ask and **not** the deliverable half. It says nothing about the base,
`ε`, `z`, or the ladder, which are closed elsewhere. It is silent on placements
that are neither a chain nor a cabled double singlet, and on creation at the
bottom.

## Verification

- `gg_scalar_per_step_probe.py` → **exit 0, 8/8**
- `precision-gates.sh` (full) → `exit 1`, RED line sha256 `7c24bef867293db6…`
  **byte-identical with and without this probe**, so the red is inherited from
  `main` and this change adds none. A `--changed` A/B was run first and was
  **void** — it skipped ("0 relevant of 9 changed"), examining nothing; only the
  full-mode pair is evidence. The 13 sibling audit witnesses the run dirties were
  restored by name, per `qou-v0t8`.
- `markovWeights_eq_jones_of_threeRow_eq_zero` is **not** cited for `y_(1³) = 0`;
  it proves the converse (TL ⟹ D), per `qou-6moa`. The producer cites
  `ocneanuWeight_conventionD_eq_zero_of_three_rows` (sorry-free, general `n`).
