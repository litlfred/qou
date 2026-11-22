# H₂ under the one rule: results

Recipe: [`preregistration.md`](preregistration.md), committed `4ff6d8d594d` before the probe was written. Producer `h2_one_rule_probe.py`, witness `h2-one-rule.witness.json` (proton pin). mpmath 40 dps, no float. Wall time 94 s. Bean `qou-a1hh`, PR #7741. Nothing fitted, ranked against data, or wired.

## Checks: 4/4 pass

| check | confirms |
|---|---|
| K1 | y_λ = [λ₁−λ₂+1]_q/[2]_qⁿ equals `y-lambda-at-q0.witness.json` at n = 3 and 12 |
| K2 | closing to level m = n reproduces χ_λ directly |
| K3 | every closing preserves the trace: Σ_μ y_μ χ_μ(E_{n→m}W) = tr W, m = 3..6 |
| K4 | E(aσ₄b) = z_D·ab on characters at n = 6 (Markov property, top closing) |

## Outcome (ii): the atom fails, so this run cannot decide the bond

**The bare two-atom word x fails reading 3 in all four cells, with no bond at all.** It fails at level 3 (and level 4, by the same block), where the (2,1) character is negative:

| electron | atom2 | bare x: failing levels | χ_(2,1) at level 3 |
|---|---|---|---|
| T_w0 = σ₀σ₁σ₀ | pe | 3, 4 | −0.084356789 |
| T_w0 | ep | 3, 4 | −0.084356789 |
| trefoil σ₀³σ₁ | pe | 3, 4 | −0.047727033 |
| trefoil | ep | 3, 4, 8, 9, 10 | −0.047727033 |

Closing down to three strands leaves the first atom's proton block times a scalar from the closed strands. So the level-3 failure is the production proton block's own (2,1) failure, the one already on record for `nuc11_interleaved` (bean `qou-99qc`). That block is not γγ-derived: its 3-letter quark block is odd, and its origin is decision C of the re-audit.

By the pre-registered reading, outcome (ii) means **this run says nothing about whether γγ supplies an H₂ bond** until the atom itself is γγ-derived. So the earlier "γγ gives H₂ no bond" (bean `qou-a1hh`, PR #7741) stays withdrawn. It is not replaced by "γγ gives a bond" either.

## What the bonds add on top of the atom (observation, not pre-registered as a criterion)

For each bond K, these are the levels where x·K fails beyond those where bare x already fails.

| electron, atom2 | V@4 | V@5 | V²@4 | V²@5 | V³@4 | V³@5 |
|---|---|---|---|---|---|---|
| T_w0, pe | 7–11 | 9–11 | 9, 10 | 7–11 | none | none |
| T_w0, ep | 7–12 | 9–11 | 9, 10 | 7–12 | none | none |
| trefoil, pe | 8, 12 | 8–12 | none | 7–12 | none | none |
| trefoil, ep | 12 | none | none | 7, 11, 12 | none | none |

- **V³ (Borromean closure) never adds a failing level**, in any cell or at either site. V and V² add failures at levels 7 to 12, apart from two cells.
- Trace ratios tr(xK)/tr(x): V³@4 gives 0.9974 (T_w0) and 0.9883 (trefoil); V³@5 gives 1.0011, 1.0000 or 1.0081. V and V² lower the trace much more (0.30 to 0.81), but they are also the bonds that add failures. Trace drop is reported here, not used to select (owner decision B).
- The committed n = 12-only witness (`knot-convoluted-tensor-h2.witness.json`, cell pe_letter = 0, cmol = 0) had V@4 and V@5 passing. That was the top level only. Checked at every level, both fail, for reasons that go beyond the atom.

## What would decide it

Re-run with a γγ-derived atom. That needs decision C (where a 3-letter quark block comes from under the one rule), or the atom built entirely from V-products, which has not been pre-registered. If the atom then passed every level, this table predicts that V³ would be the only one of the four bonds tested that survives. That is a statement about this table, not a result.

Scope (a): this concerns this construction (production proton block, these two electrons, these two sites, top closing). It does not exclude a γγ bond in any other construction.
