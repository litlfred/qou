# qou-ales: reading-3 feasibility up the tower, H_3 → H_6 → H_9 (pre-registration)

**Status: written and committed BEFORE any H_9 number was computed.** Issue #7701,
bean `qou-ales`. Nothing here is fitted, and nothing is selected against a measured
value: no AME2020, CODATA, `Q_β` or census number is read at any point.

## The question

The owner-selected confinement criterion is **reading 3** (Frobenius positivity):
`χ_λ(w) ≥ 0` on every Wedderburn block `λ` with Markov weight `y_λ > 0`, applied to
the whole element. It has so far been evaluated per nucleon at `H_3` and for the
two-nucleon interface at `H_6`. The question here is whether the verdict a
candidate receives at `H_3` survives when the nucleon is embedded in the larger
algebra `H_6` (two nucleons) and `H_9` (three nucleons, `A = 3`), or whether going
up the tower **rejects** candidates `H_3` admitted, or **admits** candidates `H_3`
rejected.

## Fixed conventions

- Hecke algebra `H_n(q)`, `(σ − q)(σ + q⁻¹) = 0`, `σ⁻¹ = σ − h`, `h = q − 1/q`.
- A **letter** is `(g, d)` denoting `σ_g + d·h`, `d ∈ {0, −1/2, −1}`
  (`σ_g`, colour-blind average `(σ_g + σ_g⁻¹)/2`, `σ_g⁻¹`).
- Markov parameter **convention D**, `z = q³/(q²+1)`. Weights `y_λ` from
  `markov_weights_symbolic.y_lambda_symbolic(n)` (Wenzl principal specialisation),
  evaluated exactly at the rational `q₀` and then in mpmath.
- `q₀` = proton pin, `qou_substrate.constants.Q_50_DIGIT_STR`.
- Characters `χ_λ` from Hoefsmit seminormal matrices,
  `computations/hecke/hoefsmit_mpfr.build_hoefsmit_mpfr`, generator `g` (0-indexed)
  ↦ `ρ_λ(T_{g+1})`.
- Precision: `mp.dps = 60` throughout. No float64 in any computation.

## Levels and blocks

| level | strands | nucleon slots (local generators 0,1 shifted) | interfaces |
|---|---|---|---|
| H_3 | 0–2 | (0,1) | — |
| H_6 | 0–5 | (0,1), (3,4) | generator 2 |
| H_9 | 0–8 | (0,1), (3,4), (6,7) | generators 2, 5 |

**Blocks tested at each level** = every partition `λ ⊢ n` with `y_λ > 0`. Expected
(and asserted, not assumed): exactly the two-row partitions —
H_3 `(3),(2,1)`; H_6 `(6),(5,1),(4,2),(3,3)`; H_9 `(9),(8,1),(7,2),(6,3),(5,4)` —
with `y_λ = 0` on every partition of three or more rows.

**Feasible at level H_n** ⇔ `χ_λ(element) ≥ 0` on every block above. A value with
`|χ_λ| < 10⁻⁴⁰` is recorded as a structural zero (counted feasible) and listed
separately, so a tie is never silently decided.

## Bond columns (two, reported separately)

1. **none** — the free product of the slot words.
2. **G³ on every interface** — the step-6 γγ bond shape, `G_i³ = (σ_i σ_{i+1}⁻¹)³`,
   on interface `i = 2` at H_6 and `i = 2, 5` at H_9. Element = (slot words) · (bonds).

(One-interface-bonded H_9 elements are NOT in this registration.)

## Candidate set

Nucleon words on local generators (0,1):

- **CORE** — `β_Bor = (σ_0 σ_1⁻¹)³` alone.
- **K0p[a]**, `a ∈ {0,1}³` — `CORE · (a_1, 0)(a_2, −½)(a_3, −½)`: the proton k = 0
  family of `qbeta_cost_minimal_budget_under_reading3_probe.py` (8 words; that
  probe records 4/8 reading-3-feasible).
- **K0n[a]** — `CORE · (a_1, −½)(a_2, −½)(a_3, −1)`: the neutron k = 0 family
  (8 words, 4/8 feasible there).
- **LIVE_p / LIVE_n** — the live production elements of
  `pyhecke.atom.build_nucleon_nf_mp`: proton `CORE·(0,0)(0,−½)(1,−½)·(0,0)(0,0)`,
  neutron `CORE·(0,−½)(0,−½)(1,−1)·(0,0)(0,0)` (recorded infeasible at H_3,
  `χ_(2,1) = −0.2806 / −0.3720`).

Two families of embedded elements:

- **F1, homogeneous.** Each of the 19 nucleon words `w` placed in every slot:
  `w|w` at H_6, `w|w|w` at H_9. This is the direct "is w's verdict stable" test.
- **F2, physical composition.** Per nucleon type, the 8 k = 0 words plus the live
  word (9 options). Protons first, as in `atom_braid_word_3A`:
  H_6 `pp`, `pn`, `nn` (81 ordered assignments each); H_9 `³He = p|p|n` and
  `³H = p|n|n` (729 each).

## What is reported

Per F1 candidate: `χ_λ` on every tested block at H_3, H_6, H_9 for both bond
columns, the `y_λ`, and the verdict per level. For F1 and F2, the 2×2 table per
(level, bond column): H_3-verdict (all slot words feasible at H_3) against
H_n-verdict, with the off-diagonal cells named:
**REJECTED-by-tower** (H_3 yes, H_n no) and **ADMITTED-by-tower** (H_3 no, H_n yes).

## Prediction stated in advance (a hypothesis, not a proved claim)

**H1 (bond = none).** Restriction of a two-row `V_λ` of `H_{3m}` to
`H_3^{⊗m}` decomposes with non-negative multiplicities (Littlewood–Richardson,
generic-`q` Hecke = symmetric-group branching) into `V_μ⊗…` with every `μ ⊂ λ`,
hence two-row. So `χ_λ(w_1|…|w_m) = Σ c·∏ χ_μ(w_i)` over two-row `μ` only, and
**H_3-feasible slots ⇒ H_n-feasible free product (zero REJECTED-by-tower in the
`none` column)**. ADMITTED-by-tower is not excluded by H1: an even number of
negative `χ_(2,1)` factors can be positive. No prediction for the bonded column.

## Cross-checks that must pass BEFORE any H_9 number is trusted

1. H_3: on all 16 k = 0 words, `χ_(2,1)` here equals the H_3 probe's
   `(tr_M − y_(3)χ_(3))/y_(2,1)` to `< 10⁻⁴⁰`, and the 4/8 + 4/8 counts reproduce.
2. H_6: `tr_M(LIVE_p|LIVE_p · G³) / tr_M(LIVE_p|LIVE_p)` reproduces the merged
   `diproton-response-closed-form-probe.witness.json` `ratio_atom_over_free` to
   `< 10⁻⁴⁵`.
3. `Σ_λ y_λ f^λ = 1` at n = 3, 6, 9, and `y_λ = 0` exactly on ≥3-row `λ`.
