/-!
# QOU.BraidKnot.per_nucleon_shift_additive_linearity — placeholder stub

**Placeholder canonical** for content block
[`prop:per-nucleon-shift-additive-linearity`](../../../quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md): *QOU.BraidKnot.per_nucleon_shift_additive_linearity*.

The full Lean statement and proof are pending; this stub exists so
the `lean.ref` URI `qou:QOU.BraidKnot.per_nucleon_shift_additive_linearity` resolves to a real declaration in
the `qou` Lake package.  The body is `sorry` carrying the
manuscript citation per CLAUDE.md §1.
-/

namespace QOU.BraidKnot


/-- Abstract context for the `per_nucleon_shift_additive_linearity` claim — fields encode the
    manuscript hypotheses; the `holds` field is the substantive
    claim of the lemma. -/
class PerNucleonShiftAdditiveLinearityContext where
  /-- The `Prop`-valued claim of the lemma (see docstring on
      `per_nucleon_shift_additive_linearity` below for the manuscript statement). -/
  holds : Prop

/-- **Proposition statement** (from manuscript):

The atomic Markov-trace denominator
$D(u) = 2^{2A+1} \cdot u^{\mathrm{shift}} \cdot (1 + u^{2})^{3A-1}$
of canonical pppnnn ordering
([`docs/audits/2026-05-03-w3-habiro-unblocked.md`](../../docs/audits/2026-05-03-w3-habiro-unblocked.md))
has shift exponent satisfying the additive-linearity recurrence:*

$$
  \mathrm{shift}(Z+1, N) \;-\; \mathrm{shift}(Z, N) \;=\; 18,
  \qquad
  \mathrm{shift}(Z, N+1) \;-\; \mathrm{shift}(Z, N) \;=\; 21,
$$

*for $Z, N \geq 1$ (i.e.\ $A \geq 2$).  Together with the base
case $\mathrm{shift}(D) = \mathrm{shift}(1, 1) = 40$, this fixes the
closed form*

$$
  \boxed{\;\;\mathrm{shift}(Z, N) \;=\; 18Z + 21N + 1\;\;}
$$

*on every atom in the canonical pppnnn ordering for $A \geq 2$.*

### Verified atoms

| (Z, N) | atom | shift (closed form) | shift (markov_peel) |
|---|---|---:|---:|
| (1, 1) | D | 40 | 40 ✓ |
| (1, 2) | T | 61 | 61 ✓ |
| (2, 1) | ³He | 58 | 58 ✓ |
| (2, 2) | ⁴He | 79 | 79 ✓ |
| (3, 2) | ⁵Li | 97 | 97 ✓ |
| (3, 3) | ⁶Li | 118 | 118 ✓ |

(Witness: [`per-nucleon-shift-derivation.witness.json`](../../folio-assistant/computations/per-nucleon-shift-derivation.witness.json),
5/5 assertions pass.  Cross-validated against
`term6-residues-at-roots.witness.json` for ⁵Li.

    The Lean encoding below is a `theorem foo : True := by sorry` placeholder;
    upgrading requires choosing the appropriate Lean types (Polynomial /
    Matrix / categorical structures / etc.) and translating the manuscript
    claim above. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.ts
theorem per_nucleon_shift_additive_linearity [ctx : PerNucleonShiftAdditiveLinearityContext] : ctx.holds := by
  -- Manuscript proof referenced above; concretisation requires
  -- type-level Lean translation of the hypotheses.
  sorry

end QOU.BraidKnot
