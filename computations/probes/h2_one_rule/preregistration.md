# H₂ under the one rule: pre-registration

Committed before the probe is written or run. Bean `qou-a1hh`; PR #7741.

## Why this run

Owner ruling 2026-11-15, in the thread "Map SM and eightfold way, probe option C": *"molecular bonds should be same... all one rule."* So the γγ + confinement-SDP rule of `qou-ales` (owner 2026-09-08) selects bond words too. The bond exemption was an agent recommendation (2026-10-13), never a ruling.

The re-audit (Claude Doc "Re-audit: γγ, gluon, bonds and the ILP after the one-rule ruling") found that the earlier statement "γγ gives H₂ no bond" was over-stated:

- in the committed witness `knot-convoluted-tensor-h2.witness.json`, the cell with no p–e letter and the junction letter ON rejects every γγ word only on the trace-drop clause of `prop:ilp-covalent-bond`, and that cell's junction letter is a single crossing, so it is not γγ itself;
- in the cell with no p–e letter and no junction letter, V = σ_sσ_{s+1}⁻¹ passes reading 3 and lowers the trace;
- reading 3 was applied at n = 12 only, while the every-level ruling (2026-10-11/12, `gg_ntower`) requires it at every strand count.

## The cell (fixed, not chosen by result)

- x = A₁ ⊗ A₂ on 12 strands, each atom = production proton block (`mjw.tokens(1, 0)`, unchanged from the committed probe) + electron on its own 3 strands.
- **No p–e letter, no junction letter.** Both are single crossings, so neither is a γγ word. This is the only cell in which every letter added beyond the atoms is γγ.
- The atoms themselves are NOT re-derived here. The proton block is the production word; its odd 3-letter quark block is open (decision C of the re-audit). This run therefore tests the bond rule, not the atom.

## Run over (all values reported, none selected)

- electron word: `Tw0_s0s1s0` and `trefoil_s0s0s0s1` (as in the committed probe);
- atom2 orientation: `pe` (junction p|e... e|p) and `ep` (junction e|e);
- bond K ∈ {none, V, V², V³}, V = σ_sσ_{s+1}⁻¹, at sites s = 4 and 5 (the two 3-strand sites straddling the cut). **The knot (one-component closure) requirement is dropped**: it is not part of `qou-ales`, and V³ (Borromean) is included.

## What is measured

1. **Reading 3 at every level.** For each level m = 3..12, χ_μ(E_{12→m}(x·K)) for every two-row μ ⊢ m, where E closes strands from the top by the convention-D Markov trace. Formula (as in `gg_ntower`, check C3 there): χ_μ(E(W)) = Σ_λ (y_λ / y_μ) Σ_{T : T restricted to 1..m has shape μ} W_TT, seminormal (Gelfand–Tsetlin) basis, y_λ = [λ₁−λ₂+1]_q / [2]_qⁿ. A word passes iff every such character is ≥ −TOL at every level.
2. **Trace drop** tr(x·K) < tr(x), reported as a column, not used to select (owner decision B pending).

## Checks before any result is read

- K1: y_λ from the formula equals `y-lambda-at-q0.witness.json` at n = 3 and 12.
- K2: level m = n reproduces χ_λ directly.
- K3: trace is preserved by every closing: Σ_μ y_μ χ_μ(E_{n→m} W) = tr(W) for every m.
- K4: E(a σ_{m−1} b) = z_D·ab on characters, for a, b on strands below m, at n = 6.

## Outcomes and what each would mean

- (i) Some γγ K passes reading 3 at every level in some cell: γγ supplies an H₂ bond candidate under the one rule. Not a selection of a word: the minimisation rule (min crossings vs min trace) is not part of `qou-ales` and stays open.
- (ii) Every K fails at some level, **and so does the bare x**: the rejection comes from the atom (production proton block), not from the bond. Then this run says nothing about bonds until the atom is γγ-derived (decision C).
- (iii) The bare x passes at every level but every K fails: γγ gives no H₂ bond in this construction. A scope-(a) negative about this construction only.

Nothing is fitted, ranked against data, or wired. No comparison with any measured binding energy.
