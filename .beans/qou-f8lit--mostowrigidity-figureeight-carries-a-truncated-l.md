
## Verified 2026-09-04 — the headline defect IS fixed; a sibling instance was not

**`Encounter/MostowRigidity.lean` no longer carries the truncated literal.** Line
243 now reads

    volume := QOU.Knot.FigureEightVolume.VOL_4_1

i.e. the exact carrier, with lines 236–237 recording the old
`2.02988321281930` and why it was wrong. `Encounter/FigureEightVolumeBridge.lean`
exists as the "Done" section describes. So this bean's stated defect is closed
and it is only the status that is stale.

### The sibling: `BraidKnot/QBetaKeystoneInteraction.lean:17`

Found by sweeping the Lean tree for `2\.0298832[0-9]*` rather than re-reading the
named file. A **second** declaration named `Vol_4_1`:

    /-- The exact continuum volume of the figure-eight knot 4_1.
        Defined via the Bloch-Wigner dilogarithm. -/
    noncomputable def Vol_4_1 : ℝ := 2.029883212819307

Both docstring clauses are false — it is a hardcoded 16-significant-digit
decimal, and nothing in the file evaluates a dilogarithm.

    this def   2.029883212819307
    exact      2.0298832128193072500424051085490…
    difference 2.500424051085490e-16   (1.232e-16 relative)

**Fixed by correcting the docstring, NOT by pointing at the exact carrier**, and
the reason is the measurement rather than caution: the declaration has **zero
consumers**. `c_3_keystone_structure` takes `V_4_1` as a *parameter* and never
reads it, and `QOU.BraidKnot.QBetaCategoricalAction` — the only module importing
this file — does not reference it. Making it exact would add a dependency to a
file whose own CORRECTIVE NOTE states its entire content is hardcoded literals
with no mathematical content, and would move no number anywhere.

### What the sweep did NOT find

The other `2.0298832…` literals in the Lean tree are **honest** and were left
alone, which is worth recording so the next agent does not sweep them:

| site | literal | verdict |
|---|---|---|
| `MassDerivation.lean:110` | 25 digits | approximation carrier, digits discussed in the adjacent comment |
| `KnotTheory.lean:136` | 25 digits | docstring says "24 dps verified" and records the bump from the old 15-dps literal |
| `Knot/ClausenValueBounds.lean:218` | 31 digits | exact-value bound |
| `KnotRegistry.lean:110,116` | `2.02988321281931` | prose, written `≈` and with a `± 1×10⁻¹⁴` bar |
| `HadronicMass.lean:585` | `2.02988321281931` | docstring table, names `2·Cl₂(π/3) = 6·Λ(π/3)` alongside |

**Generalises the bean's own lesson.** It already says checking a carrier for
degenerate models is not finished when the relation is fixed, because the
constants can carry the same defect. One more turn of the same screw: fixing the
constant at the named site is not finished either, because the same constant is
redeclared elsewhere under the same name. `Vol_4_1` / `VOL_4_1` is a two-value
overload of one name, exactly the `markovZ` pattern AGENTS.md tracks.

### Verification status

**NOT machine-checked.** The toolchain is present (v4.24.0) but this container
has 0 mathlib oleans and 1.9 G free against a 2.4 G cache restore, so
`lean`-direct cannot run. Established instead: the diff is comment-only, the
comment delimiters balance (8 `/-` / 8 `-/`), and the value is byte-identical.
