# Results: the H₂ bond with the ruled electron σ₀σ₁σ₀ and photon-term bond letters

Pre-registration: [`PREREGISTRATION.md`](PREREGISTRATION.md), commit `8c6466a88`, pushed before
computing. Producer `h2_ruled_electron_probe.py`, witness `h2-ruled-electron.witness.json`, 3/3
checks. mpmath 40 dps, convention D, proton pin `q₀`, reading 3 at every level 1…12. Run time 104 s
(4 processes), 620 bonded rows plus 4 bare rows. Issue #8821.

## Outcome: (ii). V³ is not unique.

| | nucleon V³, atom 2 `pe` | V³, `ep` | V⁶, `pe` | V⁶, `ep` |
|---|---|---|---|---|
| electron alone, levels 1–3 | pass | pass | pass | pass |
| bare H₂ word | pass | pass | pass | pass |
| bonds passing every level (of 155) | 37 | 32 | 37 | 32 |
| … of which cross the 5\|6 cut | 30 | 25 | 30 | 25 |
| `V_4³`, `V_5³` | pass | pass | pass | pass |
| `V_s`, `V_s²` | fail | fail | fail | fail |
| least crossings of a passing cut-crossing bond | 2 (`σ₅²`) | 2 (`σ₅²`) | 2 (`σ₅²`) | 2 (`σ₅²`) |

V⁶ gives the same pass/fail as V³ in every cell. Only some trace ratios differ.

### Calibration (pre-registered checks)

- **E0.** The 12 rows `K = V_s^k` with nucleon V³ reproduce the committed `h2-gg-atom` Tw0 rows
  exactly (max diff 0 at 20 printed digits). So the old γγ-power family gives the old answer with the
  ruled electron as well: only `V³` passes, at either site.
- **E1.** `χ_(3)(σ₀σ₁σ₀) = q₀³ = 1.36755…`.
- **E2.** The derived lepton insertion of #8743 is constant on every weight space `W_m`, for both
  layouts. Exact `Fraction` evaluation on all 4096 basis states. The pairs-only insertion is not
  constant (up to 7 distinct values on `W_0`), so the check can fail.

## What passes

**The electron alone passes only with equality.** Its characters are `χ_(1) = 0.6912`,
`χ_(2) = 0.7549`, `χ_(1,1) = 0.4973`, `χ_(3) = q₀³`, and `χ_(2,1) = 0`. The zero is exact for every
`q` (Lean `trace_electron_std`). In the Hecke algebra
`χ(T₁T₂T₁) = (q − q⁻¹)χ(T₁T₂) + χ(T₂) = −(q − q⁻¹) + (q − q⁻¹) = 0`.

**Single photons never bond.** Of the three one-photon letters that cross the cut (`σ₅`, `V₄`,
`V₅`), none passes. `σ₆` passes, but it lies inside atom 2 (strands 6–7), and `σ₄` (inside atom 1)
fails at level 6.

**The cheapest passing bond is `σ₅²`.**
- It is two photons, two crossings, and a pure braid: a Hopf clasp between strand 5 (atom 1's
  electron) and strand 6 (atom 2's first strand).
- It passes in all four cells.
- Its trace ratio is `1.12809` in all four cells, so the trace **increases**.
- `V³` (three photons, six crossings) also passes. Its ratio is `0.9974`–`1.0`.

The passing cut-crossing bonds with the fewest crossings (present in every cell unless marked):

| bond | photons `j` | crossings | pure | trace ratio |
|---|---|---|---|---|
| `σ₅σ₅` | 2 | 2 | yes | 1.12809 |
| `σ₅V₄` | 2 | 3 | no | 0.61269 |
| `σ₅V₅` | 2 | 3 | no | 0.44821 / 0.44274 (`pe`, V³ / V⁶), 0.61269 (`ep`) |
| `σ₄σ₅σ₄`, `σ₅σ₄σ₅` | 3 | 3 | no | 0.70903 |

**Purity.** Every pure word in the set passes, and many non-pure words pass too. So the
"pass if and only if pure" pattern of `gg_twist_reading3` stage 1 holds here in only one direction.

## Two-term trace

The two-term trace equals the one-term trace on every row. The derived insertion (all pairs plus
`(2/3)Σ_ℓ Q_ℓ²`, #8743) depends only on the total weight and the species counts (Lean
`derived_insertion_closed_form`). So it is a scalar on every weight space, and its connected part is
0 against every word. The prediction P4 holds, with scope (b): the invariant is the cancellation of
the `T³`-linear terms. Reading 3 and every trace ratio above are therefore the same under the
two-term trace. This rests on the C-lep strand charges (an assumption) and on #8743's insertion,
which is not yet merged.

## Priors against outcome

| prior | stated | result |
|---|---|---|
| P1: electron and bare word pass | 95 % | yes. The electron passes with `χ_(2,1) = 0` exactly. |
| P2: only `V³` in the `V_s^k` subfamily | 95 % | yes |
| P3: outcome (ii) | 70 % | yes. The cheapest is `σ₅²`, which was the example named. |
| P4: two-term connected term is 0 | 99 % | yes, proved in Lean |

## Reading

- **Under the ruled photon, reading 3 does not select a unique H₂ bond.** The present proposition's
  uniqueness ("passes exactly for `K = V_s³`") is a property of the γγ-power alphabet `{V_s^k}`. It
  does not survive the change to the ruled photon's term alphabet `{σ_s, σ_{s+1}, σ_sσ_{s+1}⁻¹}`.
  Scope (a): this alphabet, up to three photons, at `q₀`, in the option-1 cell.
- **The selection gap is reported, not filled.** A crossing-count minimum would pick `σ₅²`, and a
  "trace must drop" rule would exclude it (ratio 1.128). Neither rule was pre-registered, and both are
  owner questions. The two candidates disagree: `σ₅²` (one complete entangled pair absorbed on the
  cut, linking number 1 between the atoms) and `V³` (three chiral-vertex photons).
- **The constituent rule now leans on an equality.** The electron's `(2,1)` character is
  identically 0. "Passes alone" therefore depends on reading 3 being `≥ 0` rather than `> 0`.
- **The exchange model is not resolved.** As pre-registered, the word records only the absorbed
  terms. A prior entangled pair and an unseen emitter give the same word.

## Lean

`QOU/Molecular/H2RuledElectronBond.lean`, generic field, no `sorry`. lean-direct (`-DautoImplicit=false`) exits 0, and `#print axioms` gives `propext, Classical.choice, Quot.sound` for all six theorems: `std_quadratic_one`, `std_quadratic_two`, `std_braid`, `trace_electron_std`, `derived_insertion_closed_form`, `derived_insertion_eq_of_total_eq`.

## Not done

The trefoil backup electron; the pairs-only H_N comparison of #8707; other values of `q`; bonds with
more than three photons; the p–e and junction letters.
