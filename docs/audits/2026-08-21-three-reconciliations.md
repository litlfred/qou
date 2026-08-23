# Three reconciliations: the false trefoil matrices, the braid-word tables, the q₀ surface

Worked 2026-08-21 from the `qou-3nva` ledger's "hand the owner first" list.
Every claim below was recomputed here rather than carried from the ledger.

---

## 1. `ex:trefoil-operator-algebra` — the displayed matrices satisfy the wrong relation

### What is wrong

The block takes α and β from
[`def:su2-generators`](../../content/quantum-observable-universe/brings-surface/su2-generators.md)
and asserts the braid relation `αβα = βαβ`, displaying a common value for
both sides. Computed exactly:

| | value |
|---|---|
| `αβα` | `[[0, i], [i, 0]]` = **β** |
| `βαβ` | `diag(e^{2πi/3}, e^{−2πi/3})` |
| what the block says both equal | `[[0, ie^{2πi/3}], [ie^{−2πi/3}, 0]]` — **neither** |

It cannot be repaired by adjusting the displayed product, because the
premise is impossible: **all braid generators are conjugate in `B₃`**, so
they must share a trace, and `tr α = 1` while `tr β = 0`.

### Why it happened

`def:su2-generators` is a **dihedral** presentation — α is the lift of a
3-cycle, β the lift of a transposition, generating `Dic₃`. Its stated
relation is `βαβ⁻¹ = α⁻¹`, and that is correct. The braid/Coxeter relation
is a statement about the **two transpositions**, not about a 3-cycle and a
transposition. The block applied the braid relation to the dihedral pair.

Both identities that *do* hold for α and β were verified:
`αβα = β` and `βαβ⁻¹ = α⁻¹`.

### The correct pair, inside the same group

Take the two transposition-lifts:

```
s₁ = β        = [[0, i], [i, 0]]
s₂ = α²β      = αβα⁻¹ = [[0, −e^{iπ/6}], [−e^{5iπ/6}, 0]]
```

Verified: `tr s₁ = tr s₂ = 0` (conjugate, as required); `s₁² = s₂² = −I`;
the braid relation **holds**, with common value `[[0, e^{5πi/6}], [e^{πi/6}, 0]]`;
and `(s₁s₂)³ = −I`, the binary lift of the `A₂` Coxeter relation.

This also *improves* the block's closing physical claim. Its composite `αβ`
has eigenvalues `±i` — order 4, which is not a colour phase. The correct
composite `s₁s₂` has `(s₁s₂)³ = −I`, hence eigenvalues `e^{±iπ/3}`: the
three-fold phase the sentence about colour exchange is reaching for.

### Options

1. **Minimal repair.** Keep α, β; introduce `s₁, s₂` as the braid
   generators; display the true common value; keep the closing sentence
   with `s₁s₂`. ~6 lines, no other block affected, and the physics reads
   better than before.
2. **Recast in the Hecke rep.** Replace the `SU(2)` matrices with the
   2-dimensional Hoefsmit block at generic `q`, where the braid relation
   holds for all `q` and `q → 1` recovers this picture. Ties the example to
   the `tr_M` machinery the rest of the corpus uses, at the cost of leaving
   the `Dic₃` setting the parent definition establishes.
3. **Retract to what is true.** State `αβα = β` and drop the braid claim.
   Smallest edit; loses the example's purpose.

---

## 2. The braid-word tables — one misconception, two variants

`T(p,q)` closes from a word on **`p` strands**, i.e. `p−1` generators:
`(σ₀ ⋯ σ_{p−2})^q ∈ B_p`. Every wrong row writes it with `p` generators.

Verified by computing the closure permutation of each word as written:

| row | as written | closure | should be | correct word |
|---|---|---|---|---|
| Hopf `L2a1` | `σ₀σ₁ ∈ B₃` | 1 comp (**unknot**) | 2-comp link | `σ₀² ∈ B₂` |
| Trefoil `3₁` | `σ₀σ₁σ₀ ∈ B₃` | 2 comp | knot | `σ₀³ ∈ B₂` |
| Cinquefoil `5₁` | `(σ₀σ₁)²σ₀ ∈ B₃` | 2 comp | knot | `σ₀⁵ ∈ B₂` |
| Septafoil `7₁` | `(σ₀σ₁)³σ₀ ∈ B₃` | 2 comp | knot | `σ₀⁷ ∈ B₂` |
| `T₂,₉` `9₁` | `(σ₀σ₁)⁴σ₀ ∈ B₃` | 2 comp | knot | `σ₀⁹ ∈ B₂` |
| `T₃,₄` `8₁₉` | `(σ₀σ₁σ₂)⁴ ∈ B₄` | 4 comp | knot | `(σ₀σ₁)⁴ ∈ B₃` |
| `T₃,₅` `10₁₂₄` | `(σ₀σ₁σ₂)⁵ ∈ B₄` | **1 comp** | knot | `(σ₀σ₁)⁵ ∈ B₃` |
| Borromean | `σ₀σ₁σ₂σ₀σ₁σ₂ ∈ B₄` | 2 comp | 3 comp | `(σ₀σ₁⁻¹)³ ∈ B₃` |
| Figure-8 `4₁` | `(σ₀σ₁⁻¹)² ∈ B₃` | 1 comp | knot | **correct as written** |

Two variants of the same error:

- **`T(2,n)` rows** keep the right crossing count and only get the strand
  count wrong, so the closure picks up a spurious component (or collapses
  to the unknot).
- **`T(3,n)` rows** get the strand count wrong *and therefore* the crossing
  count: `3n` letters where the knot has `2n` crossings. These name a
  different knot — `T(4,q)`, not `T(3,q)`.

The one row that is right is the only non-torus knot in the table, which is
why it escaped: the misconception is specifically about the torus family.

**A component-count check alone does not catch everything.** `T₃,₅` as
written closes to a *knot* — 1 component — and is caught only by the
crossing count (15 written vs 10 for `10₁₂₄`). Any guard needs both.

The intent is recoverable precisely because the correct word's length is
the knot's own crossing number in every row.

### Scope

`knot-particle-dictionary` Tables 1–2 are upstream;
`binding-knots-visual-inventory` Table 1 cites them as "first appearance"
and repeats the errors. `nucleon-hecke-element-normal-form` carries the
wrong trefoil word inline, while neighbouring proof blocks in the same
chapter use the correct `σⁿ` form — so the chapter already disagrees with
itself.

### Options

1. **Fix upstream and propagate.** Correct the dictionary tables, then the
   derived inventory and the inline occurrence. Mechanical; the table above
   is the patch.
2. **Fix, and add the guard.** Same, plus a checker that parses any `σ`-word
   in content, computes its closure's component count *and* letter count,
   and compares both against the row's declared knot. ~40 lines. This class
   has now recurred across two chapters and three tables, and the guard is
   what makes the recurrence visible.
3. **Flag in prose only.** Note the discrepancy without changing the words.
   Leaves a table that a reader can reproduce and find wrong.

---

## 3. The q₀ surface — four presentations, and the problem is in Lean

Measured across `content/` today:

| form | files | occurrences | note |
|---|---|---|---|
| `1.1097` (mis-rounded) | 58 (55 in q₀ context) | **127** | true q₀ rounds to `1.1100` |
| `1.109978595554181` (old muon) | 33 | 43 | arithmetically correct, off-canon |
| `1.110` / `1.1100` (correct short) | 90 | — | fine |
| `1.1099785827513808` (proton, canonical) | 18 | — | the directive's default |
| `1.1099785955573347` (muon) | 2 | — | ideal CAL-2 pin |
| `1.10977859555` (digit transposition) | 2 | — | in a production-identity block |
| `:val[q_0]` witness macro | **3** | — | the mechanism exists, barely used |

The finding that changes the shape of this item: **the mis-rounded value is
overwhelmingly a Lean problem, not a prose problem.** Of its 127
occurrences, 110 are in `.lean` files, and **79 sit inside statements
rather than comments**:

```lean
q_approx : |q - 1.1097| < 0.001
cfl_gap 1.1097 > 2 ∧ cfl_gap 1.1097 < 2.1 := by
diquark_binding_per_baryon 1.1097 < 4 := by
```

These are not false — `|1.10998 − 1.1097| = 0.00028 < 0.001`, so the slack
absorbs the error — but they are *centred on a value that is not the
substrate*, and the proofs discharge at that point. Re-pointing them is a
change to proof obligations, not a text edit, and the Lean LSP is not
available in this container to verify the re-runs.

The old-muon string is the mirror image: 30 of its 43 occurrences are in
`.md`, and 27 of them carry the label **"(50 dps)"** on a 16-digit string.

### Options

1. **Single-source everything.** One Lean constant plus `:val[q_0]` in
   prose, then mechanical replacement. Ends the ambiguity permanently, and
   is the only option that fixes the Lean centring. Cost: 79 Lean
   statements whose proofs must be re-discharged, which needs a working
   Lean build.
2. **Prose now, Lean as a scoped bean.** Fix the 12 `.md` + 5 `.ts`
   occurrences and the transposed digits; open a bean for the Lean pass
   carrying the 79-statement cost. Removes what a reader sees; leaves the
   formal layer centred wrong.
3. **Make it legible without changing values.** Correct the 27 "(50 dps)"
   mislabels and annotate each literal with which pin it is. Cheapest, and
   it addresses the actual reported harm — that a reader cannot tell which
   of four numbers is authoritative — without touching a single proof.

Options 3 and 2 compose. Option 1 subsumes both and should not be started
in a container that cannot build Lean.
