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

## 4. Measured

(Filled in after the run. See below.)
