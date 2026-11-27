# Bond-selection rule search: what each corpus rule picks for the nuclear γγ bond

**Date** 2026-11-27 · **Brief** C2, front C (compute-accuracy epic `qou-myts`) · **Beans** `qou-brng`, `qou-ales`
**Follows** `docs/audits/2026-11-27-binding-ceiling-at-q0.md` (PR #9526), §6 item 2
**Probe** [`computations/probes/bond_selection_rules/`](../../computations/probes/bond_selection_rules/): 6/6 checks. The classical structure is exact integer arithmetic. Reading 3 at `q₀` uses the corpus seminormal helpers (mpmath 40 dps, convention D, proton pin). A = 3 junction-only population: 1244 words, 690 s.
**Lean** [`QOU/MassTheory/GammaGammaVertexTelescope.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/GammaGammaVertexTelescope.lean): sorry-free, lean-direct exit 0 (`-DautoImplicit=false -s 65536`), `#print axioms` = `[propext, Quot.sound]`, generic group, no numbers.
**Scope** (a) throughout. AME is not read by the probe. No rule was chosen by its binding, and nothing is wired or re-scored.

## 0. The decision, in one paragraph

The question is which corpus rule should pick the nuclear bond word without looking at the binding
it produces. There are six candidates, and they split into two families:

- **Linking-neutral rules (R3, R4).** These pick the vertex power `V(s)³` on every junction at A = 2, 3, 4.
  It merges no components, and the binding is keV (²H −99.7 %).
- **Unrestricted cheapest rules (R1, R6).** These pick telescoped words such as `V2V3 = σ₂σ₄⁻¹` and
  `V2V3V4 = σ₂σ₅⁻¹`. They merge 2, and the binding is MeV (²H +162 %).

The junction-vertex-only rule of owner card 1 (R2) is **not stable**. It gives `V(2)³` at A = 2 only
with the written-crossing cost. With the reduced cost it gives `V1V2V1V2`, which unbinds. At A = 3 it
gives a 69-way tie of five-vertex words that merge 2 or 4. **Recommendation (judgement):** extend
whole-word linking neutrality to the bond (R3). It is the only rule that is robust to the cost
function and uniform in A. It also follows from the independent rationale of an existing ruling. It
needs an owner ruling, because the 2026-11-25 ruling put "the H₂ bond words" outside the scope of
neutrality.

**For the coordinator: a conflation to check.** The brief describes the current stance as "keep the
cheapest γγ bond (V2V3 …, 5.826 MeV)". The 2026-11-27 18:05Z note on `qou-brng` describes the same
card option as "the deuteron −99.7 % stays". Those are two different words, picked by two different
rules:

- `V2V3` is R1, the cheapest bond over all bond words.
- `V(2)³` (−99.7 %) is R2, card 1 option A, junction vertices only.

The "merges" wording in the ceiling audit §6 is not what separates them. R1 already selects `V2V3`
with no merge requirement.

## 1. Candidates found, by corpus path

| # | rule | source (ruling, Lean, block, bean) | status |
|---|---|---|---|
| R1 | reading 3 + cheapest by crossing count over **all** γγ bond words | `FrobeniusSelected` (`QOU/MassTheory/GammaGammaFrobeniusSelection.lean`), the same rule that selects `β_Bor`. Owner ruling 2026-11-22: *"Minimization of energy is okay as a selection rule"* (proton word). | owner-sanctioned input. Applying it to bonds over all words has not been ruled. |
| R2 | R1 restricted to **junction vertices** (`V(3j−2)`, `V(3j−1)`), plus right-hand closure (bond enters the newer nucleon) | owner card 1 of 2026-11-25, option A, accepted with *"go"* (`computations/probes/gg_deuteron_bond/results.md`). Closure: ruling 2026-11-22. | ruled at A = 2 only |
| R3 | **whole-word linking neutrality** (every component self-writhe and every pairwise linking number zero) + reading 3 + cheapest | owner rulings 2026-11-21 / 22 / 25 (`PhotonU1NeutralCut.Neutral`, `PhotonNeutralSelection.lean`). Rationale stated there: charge conservation in each history. | scope excludes "the H₂ bond words" (2026-11-25, clause iv). Extending it to nuclear bonds needs a ruling. |
| R4 | **pure zero-linking** (trivial permutation + R3) + cheapest | `BorromeanWordForcing.lean` (`PureZeroLinking`, `borromean_minimises_energy`). This is the family in which `β_Bor` is the unique energy minimiser. | proved for the nucleon. Not applied to bonds. |
| R5 | R1 restricted to bonds that **merge no strands inside a nucleon** (a bond must not restructure a nucleon's own components) | new here, motivated by nucleon identity: the free reference `V³⊗V³` is the nucleons' own state | proposal, not in the corpus |
| R6 | cheapest bond **that merges** | ceiling audit §6 item 2, option "cheapest bond that merges" | selection against the target (see §3) |

Searched and **not** a bond-selection rule for the γγ word:

- **Isospin projectors** (`qou-kj4v`, `InterfaceScalar`). `μ₊ + μ₋ = 1`, so they cannot both bind
  (`cor:interface-never-realises-isospin-weight`). They are not γγ words. In the γγ-nucleon cell
  `p = n`, so isospin cannot act there.
- **The production template** `pp→σ`, `nn→σ⁻¹`, `pn→σ_avg` and its colour-tube refinement
  (`conj:inter-nucleon-channel-color-tube`, conditional on `conj:s5-so3-fiber-action`). Both are
  single-crossing letters, superseded by the 2026-11-15 ruling (the γγ rule covers bond letters).
- **`rem:pn-bond-cannot-be-extremal`.** It is stated on the superseded letters.
- **The contiguous layout** (`qou-u5qs`, derived). It fixes where the nucleons sit, not the bond.
- **Nucleon order by GB reduction** (ruling 2026-11-21). It fixes the order, not the bond.
- **Literal PSD, reading 1.** It selects only the empty word on `H₃` (`GammaGammaSelectorH3`).
- **Reading 2.** It has no selection theorem.
- **The confinement SDP / LP** (`nucleus_operator_selection_sdp.py`). It sweeps `n_target` from the
  atom word, which makes it circular for selection (`qou-ales`). The LP is degenerate.
- **Molecular LP-dual bond order** (`covalent-bond-order-and-lp-selection`). It concerns electron pairs, not nucleons.
- **`conj:bond-order-eq-jet-degree`.** It is a decomposition, not a selection.
- **The library** (`INDEX.md`, sections, ocr). It holds no braid bond-selection rule. These rules are
  internal to the model, so the result is citation-free by nature, not missing.

Paths run:

- `bun scripts/corpus-search.ts` (bond, interface, deuteron, isospin, confinement SDP, nucleon order);
- `docs/audits`, `docs/coordination/owner-rulings.md`, `folio/`, `computations/`;
- beans on the mount: `qou-ales`, `qou-kj4v`, `qou-99qc`, `qou-brng`, `qou-u5qs`, `qou-g8i1`,
  `qou-nial`, `qou-gr3t`, `qou-edt7`;
- QA sidecars grepped for *cheapest* / *bond selection* (two hits, both molecular or unrelated).

## 2. What each rule selects

Populations:

- A = 2: the 408 passing words of length ≤ 6 (`binding-ceiling-q0.witness.json`, = PR #9426).
- A = 3: the 28 passing words of length ≤ 4, plus every junction-vertex-only word of length 2–5 and
  `V(a)³V(b)³` (73 of 1244 pass, computed here).
- A = 4: two spot words.

Cost is the crossing count, either as written (2 per vertex, the cost PR #9426 used) or after free
reduction. `B = −E₀ ln r` at tower `E₀ = 4.2274834` MeV is a **scorecard only**.

| A | rule | cost | selects | merges (intra-nucleon) | neutral | ratio r | B (MeV) |
|---|---|---|---|---|---|---|---|
| 2 | R1 = R6 | written | `V2V3`, `V3V2` | 2 (1) | no | 0.252058 | 5.826 |
| 2 | R1 = R6 | reduced | `V2V3`, `V1V2V3` | 2 (1–2) | no | 0.2521, 0.2553 | 5.826, 5.773 |
| 2 | R2 | written | `V1³`, `V2³` → `V(2)³` by closure | 0 | yes | 0.998497 | 0.00636 |
| 2 | R2 | reduced | `V1V2V1V2` | 0 | no | 1.035874 | −0.149 |
| 2 | R3 = R4 | both | `V1³`, `V2³` → `V(2)³` | 0 | yes | 0.998497 | 0.00636 |
| 2 | R5 | written | `V1³`, `V2³` | 0 | yes | 0.998497 | 0.00636 |
| 2 | R5 | reduced | five words of four crossings (`V1V2V1V2`, …) | 0 | no | 1.031–1.036 | −0.13 … −0.15 |
| 3 | R1 = R6 | written | `V2V3V4` and its cyclic shifts | 2 (0) | no | 0.247298 | 5.906 |
| 3 | R1 = R6 | reduced | `V2V3V4`, `V1V2V3V4`, `V2V3V4V5` | 2 (0–1) | no | 0.2434–0.2504 | 5.85–5.97 |
| 3 | R2 | written | **69-way tie**, five vertices | 2 or 4 (0–3) | no | 0.098–0.351 | 4.4–9.8 |
| 3 | R2 | reduced | `V4V5V1V2V5`, `V4V5V5V1V2` | 4 (3) | no | 0.097809 | 9.828 |
| 3 | R3 = R4 | both | `V(a)³V(b)³`, a ∈ {1,2}, b ∈ {4,5} → `V2³V5³` by closure | 0 | yes | 0.996997 | 0.0127 |
| 3 | R5 | both | `V2V3V4` (= `σ₂σ₅⁻¹`) | 2 (0) | no | 0.247298 | 5.906 |
| 4 | R3 = R4 (spot) | — | `V2³V5³V8³` passes reading 3 | 0 | yes | 0.995498 | 0.0191 |
| 4 | R1 (partial) | — | `V2V3V4V8` passes (PR #9526 §7). The full A = 4 run is not finished, so the R1 minimum is not established | 4 (1) | no | 0.060201 | 11.88 |

AME, for orientation only, since no rule reads it: ²H 2.2246, ³H 8.4818 MeV.

Facts the table rests on, all measured:

1. **No passing merging word is linking-neutral**, in either population: 0 of 362 merging passers at
   A = 2 and 0 of 97 at A = 3 (`population_stats`). Within these populations, neutrality plus reading 3
   implies merges = 0. This is measured, not proved. A single vertex `V(1)` is neutral and merges 2,
   but it fails reading 3.
2. **R1's words are telescoped single crossings.** `V(s)V(s+1)⋯V(s+n−1) = σₛσₛ₊ₙ⁻¹`
   (`GammaGammaVertexTelescope.run_eq`, any group). So `V2V3 = σ₂σ₄⁻¹` and `V2V3V4 = σ₂σ₅⁻¹`. The
   unrestricted γγ grammar contains every `σₛσₜ⁻¹` with `s < t` (`exists_run_of_lt`), which re-admits
   the single-crossing letters the 2026-11-15 ruling took out of the bond.
3. **At A = 2, R1's word changes a nucleon.** In `V2V3 = σ₂σ₄⁻¹`, the letter `σ₄⁻¹` lies inside
   nucleon 2, so one of its two merges is intra-nucleon (strands 4 and 5). The bound word then
   contains a nucleon that is no longer `V³`, while the free reference keeps `V³`. At A = 3, `V2V3V4`
   has no intra-nucleon merge. The A = 4 word `V2V3V4V8` again has one (`σ₉⁻¹`).
4. **The cost function is an unstated choice, and it changes R2's answer** (`V(2)³` against
   `V1V2V1V2`, binding against unbinding). R3 and R4 pick the same words under both costs.

## 3. Derived or selection against the target

- **R6 is selection against the target as stated.** The merge requirement is there because merges are
  what bind classically (`ClassicalLogBindingCycleCount`). The ceiling audit §6 already says so.
  However, R6 and R1 select the same words in every measured cell. So `V2V3` can be kept **as R1**,
  without the merge clause, and then it is not a fit. It remains a rule whose words change a nucleon
  (fact 3) and re-admit single crossings (fact 2).
- **R1 is target-free.** It is the owner-sanctioned energy principle applied to the widest population.
- **R2 is target-free** (its results file records that the binding words were not used). But it is
  cost-dependent and not uniform in A, so it cannot be the A-general rule as it stands.
- **R3 and R4 are target-free.** They are extensions of rulings whose rationale (charge conservation in
  each history; the pure zero-linking family of `β_Bor`) predates this question. The anti-fit caveat
  from the 2026-11-25 row applies equally here: these rulings were chosen with their nucleon result
  known, not their bond result.
- **R5 is target-free but new.** It is cost-dependent at A = 2.
- **Trap check.** No candidate was chosen because it produces the needed sign pattern (unlike pair
  binds, like pairs don't). The γγ-nucleon cell has `p = n`, so no candidate here can express that
  pattern at all.

## 4. Lean

`QOU.MassTheory.GammaGammaVertexTelescope` (sorry-free, generic `[Group G]`):

- `run_eq`: `V(s)⋯V(s+n−1) = σₛσₛ₊ₙ⁻¹`;
- `vertex_mul_vertex_succ`: `V(s)V(s+1) = σₛσₛ₊₂⁻¹`;
- `exists_run_of_lt`: every `σₛσₜ⁻¹` with `s < t` is a vertex product;
- `run_eq_one_iff`.

This is the structural fact behind R1's selections, not a selection rule. None of R1–R6 is
*derived* in the sense of AGENTS.md. Each one is a ruling or a proposal, so no selection theorem is
stated in Lean. Fact 1 (neutral and passing implies merges 0) is the candidate theorem. Proving it
needs reading 3 on six and nine strands in Lean, which is not feasible in this tranche.

## 5. Options for the owner (put to the owner through the coordinator, not here)

| option | what it means | costs | risks | commits to |
|---|---|---|---|---|
| **A. Extend linking neutrality to bonds (R3)** — recommended, judgement | the bond is the cheapest passing word with the whole atom linking-neutral: `V(s)³` per junction | a ruling row; the scorecard row already uses `V(2)³` | the γγ bond binds at keV at every A measured; the MeV-scale binding must come from elsewhere | the nuclear binding is not a bond-letter effect in this cell |
| **B. R1, all bond words** | `V2V3` (A = 2), `V2V3V4` (A = 3), MeV scale | re-score ²H (+162 %), ³H (−30 %) | the bond word is a telescoped single crossing and, at A = 2 and 4, rewrites a nucleon | non-neutral atoms, against the nucleon-side rulings |
| **C. Keep R2 (card 1) as ruled** | junction vertices only, written cost | none now | breaks at A = 3 (69-way tie, merges up to 4) and under reduced cost | must name the cost function and the A = 3 tie-break |
| **D. Do nothing** | the scorecard keeps `V(2)³`, −99.7 %, Conditional | — | the A ≥ 3 bond stays unselected | — |

Default if nobody chooses: D. The deuteron row stays −99.7 % and A ≥ 3 has no ruled bond.

## 6. Open

- Prove fact 1 (neutral passing bonds merge 0) beyond the measured populations.
- The full A = 4 R1 minimum (PR #9526 §7 run).
- A flavoured cell (`p ≠ n`). Every rule here is applied in a cell that cannot tell `pp` from `pn`.
