# Nuclear Regime-I shell rule: formalize, then measure (the rule stays withdrawn)

Date: 2026-11-21. Block: [`prop:nuclear-operator-regimes`](../../folio/quantum-observable-universe/nuclear-interactions/nuclear-operator-regimes.md).
Owner instruction (2026-11-21): keep the rule withdrawn, and try to derive a shell rule properly.

## 1. Where the rule came from

The block's Regime I used to say that the operator selected at a shell-filling
step is the torus knot `T(2, n_s)`, where `n_s` is the shell size. The one
example given was `Φ = (σ₀σ₁)²σ₀`, labelled `T(2,5)`. PR #8739 withdrew the
rule, because that word closes to `T(2,4)`. The evidence the block cites is
`nuclear-binding-lp.witness.json`, and no file of that name exists on `main`.

**Provenance, measured this session.** This clone is shallow, so the history
came from the GitHub commits API on the path:

- The producer `computations/nuclear-binding-lp.py` (439 lines) moved to
  `computations/_deprecated/` in `d27b002745` (2026-06-15). It left `main`
  together with its witness in `6333715860` (2026-10-10, "fsh-guts: cut over to
  the cat/cat-harness/fsh-guts branch"). Both files were retrieved from
  `6333715860^`.
- **The witness never held the transition table.** It contains `parameters`
  (q₀ = 1.1099785955541805, i.e. the muon pin; z = 0.4993203340, i.e.
  convention C) and an `sdp_lift` block for three pair channels (pp, nn, pn).
  The step-by-step operator selection behind Regimes I/II/III went to **stdout
  only**. So "verified computationally in nuclear-binding-lp.witness.json",
  as `QOU/Interactions/NuclearOperatorRegimes.lean` §5 says, has never pointed
  at a record of the regime claims.
- **What the producer did.** It builds the nucleus one nucleon at a time inside
  `H₃(q)`. At each step it computes `N_k · o · n_{k+1}` for every operator `o`
  in a hand-picked list of 10, and keeps the one with the least "demand" (the
  sum of the absolute values of the negative coefficients in the GS normal
  form), breaking ties by Markov trace. The arithmetic was float64 throughout.
  The trace weight of `σ₀σ₁σ₀` was written `z³`; the Markov trace gives
  `h·z² + z` (`pyhecke.gram.TR_M`). The docstring lists `T_{2,7}` and
  `T_{2,9}` as candidates, but the code never defined them.
- **The candidate set could not express the rule.** Its only torus-labelled
  words were `σ₀²`, `σ₀σ₁σ₀` and `(σ₀σ₁)²σ₀`, and the largest index any of them
  carried was 5. By `not_shellRuleT2_of_bounded_index` (§3), no selection from
  such a set can satisfy a `T(2, n_s)` rule at a shell with `n_s > 5`. That
  includes the `p`-shell (6) and the `sd`-shell (12). The general rule therefore
  rested on a single step, and could not have been tested beyond the first
  shell even in principle.

Corpus checks run before this note was written:

- `bun scripts/corpus-search.ts "nuclear operator regimes shell"` returned 0 seeds.
- Grepping `docs/audits`, `folio/` and `computations/` for
  `nuclear-binding-lp`, `shell filling`, `T_{2,n_s}` and `demand-minimi` found
  the block and its Lean, `predicted-spectra/torus-knot-shell-binding.md` (a
  separate, explicitly **proposed** shell-capacity construction `r × s`, whose
  closure the block itself calls "the key open problem"), and
  `computations/magic-ladder-pattern-investigation.md` (which shows no
  partition statistic singles out the magic numbers).
- No audit or bean records the transition table being re-measured.

## 2. Pre-registered criteria (fixed before the probe was run)

The probe is
[`computations/nuclear_regime_shell_rule_probe.py`](../../computations/nuclear_regime_shell_rule_probe.py).
This section and the probe were committed **before** the first run, and the
commit order on the PR is the record of that.

- **Model.** The 2026-04 model, re-implemented: the legacy nucleon elements
  `(σ₀σ₁⁻¹)³ · Π(typed quark crossings)` in `H₃(q)`, and the step
  `N_k · o · n_{k+1}`. **The model is not canonical.** Under the owner's γγ
  ruling, nucleon words are selected by γγ construction, and this element
  predates that ruling. The aim here is to find out what the original
  computation actually gives, and whether a shell rule can come out of it.
- **Arithmetic.** mpmath at 80 dps, repeated at 120 dps; convention D,
  `z = q³/(q²+1)`; proton q₀.
- **Cost K1** (the original): demand, with ties broken by `tr_M`.
  **Cost K2** (reported only): demand divided by the ℓ¹ norm of the product.
  K1 is not scale-free, and K2 shows how much of the K1 selection is just
  operator size.
- **Candidate sets.** C0 is the original 10. C1 is C0 plus `σ₀ⁿσ₁` for
  n = 2..12. By Markov stabilisation the closure of `σ₀ⁿσ₁` is exactly
  `T(2,n)`, so C1 contains a genuine `T(2,n)` for every shell size up to 12.
- **Torus index.** `σ₀ⁿσ₁ ↦ n`; `L₊ ↦ 1` (unknot); `e⁻ = σ₀σ₁σ₀ ↦ 2` (Hopf
  link, owner ruling 2026-11-21); `(σ₀σ₁)²σ₀ ↦ 4`; every other operator gets
  no index.
- **Shell size.** The size of the same-type shell the added nucleon enters.
  Capacities are 2, 6, 12, 8, 22, 32, 44.
- **Rule test.** A step passes iff every selected operator has torus index
  `n_s`. Every step is tested; no step is reclassified afterwards as "not
  Regime I".
- **Sequences.** `ppnn` and `ppnnpn` (the original orders), `p²⁰`, `n²⁰`,
  `(pn)¹⁰`.
- **No rule is adopted from the output.** If a regularity shows up, it is
  written down as a conjecture with its evidence and a falsifier, and any
  restated rule goes to the owner.

## 3. Lean

[`QOU/Interactions/NuclearRegimeShellRule.lean`](../../folio/quantum-observable-universe/lean/QOU/Interactions/NuclearRegimeShellRule.lean)
is new. It is sorry-free, generic over a linear order, and its axioms are only
`propext`, `Classical.choice` and `Quot.sound`.

| declaration | content |
|---|---|
| `wordPerm_phiWord` | the strand permutation of `(σ₀σ₁)²σ₀` is `(1 2)` |
| `phiWord_closure_not_connected` | no power of it sends strand 0 to strand 1, so the closure is not a knot, and in particular not `T(2,5)` |
| `StepSelection`, `IsSelected` | one step of argmin selection over a finite candidate set |
| `ShellRuleT2` | the withdrawn rule, stated as a class with content and **no instance** |
| `exists_isSelected` | a nonempty candidate set always has a selection |
| `not_shellRuleT2_of_counterStep` | a single counter-step refutes the rule |
| `not_shellRuleT2_of_bounded_index` | torus indices bounded by `M`, plus a Regime-I shell larger than `M`, refutes the rule |
| `isSelected_smul_iff` | positive rescaling of the costs leaves the selection unchanged |

## 4. Measured (run 2026-11-21, after §2 was committed)

Command: `python3 -u computations/nuclear_regime_shell_rule_probe.py 2>&1 | tee /tmp/nrsr.log`.
Wall time is about 4 s. Witness: `computations/nuclear-regime-shell-rule.witness.json`
(`q0Anchor: proton`). The runs at 80 and 120 dps select the same operator at
every step of every run. The smallest nonzero gap between the selected cost
and the runner-up cost is `5.07e-4`, so precision decides nothing here.

### 4.1 Rule test (`T(2, n_s)` with `n_s` the shell size)

| candidate set / cost | steps passing | of |
|---|---|---|
| C0 / K1 (the original) | 3 | 65 |
| C0 / K2 | 3 | 65 |
| C1 / K1 | 3 | 65 |
| C1 / K2 | 1 | 65 |

Every pass is the same case: `e⁻ = σ₀σ₁σ₀` (Hopf link, index 2) selected
while the first `s`-shell (`n_s = 2`) is filling, at the first or second
neutron of `n²⁰` / `(pn)¹⁰`. The rule never passes past the first shell. In
C1, with a genuine `T(2,n)` available for every `n ≤ 12`, the selection does
not move to the index the rule predicts at any `n_s = 6` or `n_s = 12` step.
In `p²⁰` only two steps pick a torus word at all.

### 4.2 Per-step selection, cost K1

`*` means the step was decided by the `tr_M` tie-break among several
candidates whose demand is exactly 0, not by the demand.

| sequence | C0 (original 10) | C1 (C0 + `σ₀ⁿσ₁`, n = 2..12) |
|---|---|---|
| `ppnn` | Φ, L₊\*, L₊\* | σ₀³σ₁\*, L₊\*, L₋\* |
| `ppnnpn` | Φ, L₊\*, L₊\*, L₋\*, C_pn\* | σ₀³σ₁\*, L₊\*, L₋\*, C_pn\*, B₃\* |
| `p²⁰` | Φ, L₋\*, C_nn\*, B₃\*×7, C_nn\*×4, 1\*, C_nn\*, B₃\*, C_nn\*×2 | σ₀³σ₁\*, σ₀²σ₁\*, B₃\*×5, C_nn\*×7, 1\*, C_nn\*×4 |
| `n²⁰` | e⁻, L₋, Φ, e⁻\*, 1\*, C_pn\*, L₊\*, e⁻\*, 1\*, C_nn\*, L₊\*, L₋\*×8 | e⁻, L₋, Φ, σ₀²σ₁\*×2, L₋\*, 1\*×2, C_pn\*, L₊\*, σ₀²σ₁\*×2, L₋\*, C_nn\*, L₊\*, L₋\*, C_nn\*, L₋\*, C_nn\* |
| `(pn)¹⁰` | e⁻, L₊, e⁻\*, B₃\*×6, L₋\*, 1\*, C_pn\*, 1\*, L₊\*, C_pp\*, 1\*, C_nn\*, 1\*, C_nn\* | same as C0, except step 2 becomes a tie-break |

Here Φ = `(σ₀σ₁)²σ₀`. The full per-step record is in the witness under
`data.selection`. For every step it holds the selected operator(s), the runner-up
and its cost gap, the number of candidates at the minimum cost, the selection
under a convention-C tie-break, and the exact LP duals `y0_star`, `y_star`,
`active_set`, `primal_obj`, `dual_obj` and `duality_gap`.

### 4.3 What the numbers say

1. **The recorded transition table does reproduce, and it rests mostly on a
   tie-break.** On the original orders with the original candidates (C0), the
   sequence is Φ → L₊ → L₊ → L₋ → C_pn, which is exactly the block's Regime
   I → II → III sequence. Only the first step, `p → pp` (Φ), is decided by the
   demand. Steps 2–5 are `tr_M` tie-breaks among 4, 6, 9 and 9 candidates of
   demand exactly 0. So Regimes II and III, as recorded, are artifacts of the
   trace tie-break, not of the demand.
2. **The single Regime-I datum is an artifact of the candidate set.** At
   `p → pp`, Φ has demand `0.0046181`, which is **not zero**. It wins in C0
   only because none of the ten C0 operators reaches zero. Once C1 adds the
   `σ₀ⁿσ₁` words, ten candidates reach zero demand and the tie-break picks
   `σ₀³σ₁` (`T(2,3)`, against `n_s = 2`). In the C1 LP, Φ's reduced cost is
   `y*_Φ = 0.0046181 > 0`, which puts it in the active set (excluded).
3. **The primary criterion is degenerate.** Across all runs, **57 of 65**
   (C0) and **61 of 65** (C1) steps are tie-breaks among zero-demand
   candidates, with up to 21 of 21 candidates tied. From about step 3 on,
   "minimise demand" selects nothing. What selects is "minimise `tr_M`", and
   that is not scale-free, so it favours operators by size. K2 does not
   remove the degeneracy, because a demand of zero normalises to zero.
4. **The tie-break depends on the trace convention.** Re-breaking the same
   ties with the convention-C trace changes the selection at 4 of 65 steps
   (C0) and 14 of 65 (C1). The 2026-04 run used convention C. Its table
   happens to agree on the original orders, but in general the regime
   assignments are not convention-stable.
5. **B₃ is selected at the nuclear level in this model.** In `p²⁰` (C0) it is
   picked at 8 steps, the first at step 4 (A = 5), and in `(pn)¹⁰` at 6 steps
   (A = 5…10). Every one is a tie-break. `NuclearOperatorRegimes.lean` §5
   (`borromean3_not_nuclear_level`) says *"For A ≤ 8 … B₃ is NOT selected …
   Verified computationally in nuclear-binding-lp.witness.json"*. The witness
   never held that check, and this model contradicts the statement on the
   pure-proton and alternating orders. It holds on the original `ppnn` /
   `ppnnpn` orders. This is a scope-(a) statement about this model only. The
   Lean theorem itself proves only `hopfPlus ≠ hopfMinus` and is untouched.

## 5. Conjectures and scope

- **No shell rule is supported by this data.** On the pre-registered test,
  `T(2, n_s)` fails at 62 of 65 steps in C0/K1 and C1/K1, and never passes
  past the first shell. This is **scope (a)**. It is a negative for this
  construction: the legacy nucleons, the greedy `N·o·n` step in `H₃(q)`,
  demand with a `tr_M` tie-break, and these candidate sets. It is not a
  structural exclusion of shell rules.
- **The structural limit is a Lean statement, scope (b).**
  `not_shellRuleT2_of_bounded_index` proves that any candidate set with
  torus indices `≤ M` cannot satisfy the rule at a shell larger than `M`.
  That rules out the 2026-04 set (`M = 5`) for the `n_s = 6, 12` shells,
  whatever the costs are.
- **The model has no room for shell structure, and this is an observation,
  not a theorem.** The nucleus never leaves the six-dimensional `H₃(q)`, so
  nothing in the construction grows with nucleon number apart from
  coefficient magnitudes. A shell rule indexed by shell size would need an
  object whose size tracks occupancy, for example `H_{3A}(q)` with γγ-selected
  nucleon words, as the atom words already do.
- **One observed regularity, stated as a conjecture only.** At the very first
  step, the demand criterion has a unique minimiser with a positive gap. The
  minimiser is `e⁻` (Hopf link) for `n + n` (first step of `n²⁰`) and for
  `p + n` (first step of `(pn)¹⁰`), and Φ (`T(2,4)`) for `p + p`. That is one
  step per pair type, three data points in all, which cannot support a rule. **Falsifier:** any candidate with lower demand at that
  step. C1 already falsifies it for `p → pp` (zero-demand `σ₀ⁿσ₁`), so it
  survives only as "e⁻ minimises demand at the first step for `nn` / `pn`
  within C0 ∪ C1".

## 6. What was not changed

- The block's claim is unchanged. The `.ts` gets an `authorNotes` caveat
  pointing here and naming the reproduced table and its tie-break character.
  Any restated rule needs the owner.
- `QOU/Interactions/NuclearOperatorRegimes.lean` is not edited: a sibling
  branch, `claude/hopf-electron-relabel-2026-11-21`, is relabelling it. Its §5
  docstring cites a witness that never held the check (§4.3 item 5), and that
  should be fixed after the relabel lands.
- Nothing here was resource-limited, so there is no Antigravity bean. The
  natural next measurement is the same selection on γγ-selected nucleon words
  in `H_{3A}(q)`. That is a new model, not a re-run, and it needs owner scoping.
