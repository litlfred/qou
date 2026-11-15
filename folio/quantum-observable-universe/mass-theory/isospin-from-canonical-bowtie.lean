import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum

/-!
# QOU.BraidsAndKnots.IsospinFromCanonicalBowtie — the D9 conjecture carrier

**Sibling-resolution carrier** for content block
[`conj:isospin-from-canonical-bowtie`](isospin-from-canonical-bowtie.md): *D9 isospin SU(2)_I*.

Per AGENTS.md §3b, the class instance is the **conjectural witness** (sorry = conjecture),
not a missing proof; downstream theorems take `[IsospinFromCanonicalBowtie]` as an explicit
`[Instance]` hypothesis. **No instance is provided** — that is the honest open state.

## 2026-09-04 — this carrier used to assert nothing

It read, in full:

```lean
class IsospinFromCanonicalBowtie where
  holds : Prop
```

A field typed `: Prop` is a field whose *type* is the universe of propositions, so an
instance supplies **a proposition, not a proof of one**: `instance := ⟨True⟩` type-checks
and discharges the class. Every `[IsospinFromCanonicalBowtie]`-conditional theorem was
therefore conditional on nothing. This is the shape AGENTS.md §3b-tax forbids
(*"class fields must carry the conjecture's content … never a bare `True` or an empty
body"*), and it is now detected as `proof-claims-unencoded` / `prop-universe-field`.

**Why this mattered beyond hygiene.** D9 is one side of the identification that the
two-nucleon channel-asymmetry closure rests on (`InterfaceScalar.separable_interface_degenerate`
assumes the spin and isospin `SU(2)`s carry the same projector scalars). "D9 has no witness"
was the recorded blocker — but the real blocker was that a witness would have been *trivial
and would have proved nothing*. See
`docs/audits/2026-09-04-pauli-lock-rests-on-an-unexamined-su2-identification.md`.

## Prior work — the defect CLASS was known; this fixes one carrier in it

**The `holds : Prop` class is not a new finding, and it would be wrong to read this
file as reporting one.** Bean `qou-tsnp` states it in the same words —
*"GAP: 12 conjecture carriers axiomatised as `holds : Prop` assert nothing"* — and
[`docs/audits/2026-08-23-free-prop-field-census.md`](../../../docs/audits/2026-08-23-free-prop-field-census.md)
(PR #5562, beans `qou-tsnp` / `qou-lo1t`) is its corpus-wide census, with a
re-runnable detector at
[`scripts/free-prop-field-audit.py`](../../../scripts/free-prop-field-audit.py)
measuring **156 free `: Prop` fields across 105 carriers**. It was named earlier
still in `2026-06-07-klr-gs-order-formalization-plan.md` and
`2026-06-24-devils-advocate-wave10.md`.

That census also draws a distinction worth carrying: a free `P : Prop` is **not
automatically a defect** — it is harmless when another field *pins* it
(`regular_iff : regular ↔ 0 < x`), and its three buckets are `UNPINNED-EMPTY` /
`UNPINNED-FAKE-IF` / `PINNED`. D9's old carrier was `UNPINNED-EMPTY`: it had no
other field, so there was nothing that could pin it.

**What is new here is the repair, not the diagnosis.** `qou-tsnp` records the gap;
this file closes it for D9, which is the carrier on the two-nucleon channel-asymmetry
critical path. The rewrite removes the free field entirely rather than pinning it, so
it does not land in the `PINNED` bucket either — it leaves the census's population.

## What is encoded below, and what is not

**Encoded — the falsifiable numeric content**, taken from the block's own statement:

    Δm / M_N  =  ℏ_q² · h · [2]_q · (1 + ℏ_q³) / 3

The three factor conventions are **read from the producer**
[`computations/verify_isospin_bar_anomaly.py`](../../../computations/verify_isospin_bar_anomaly.py),
not inferred from the glyphs:

| symbol | producer | note |
|---|---|---|
| `ℏ_q` | `(x - 1) / x` | `= 1 - q⁻¹`, matching `hbarQ` elsewhere in the tree |
| `h` | `x - 1/x` | `= q - q⁻¹` |
| `[2]_q` | `x + 1/x` | the **symmetric** bracket — deliberately **not** `QGenericBase.qBracket`, which is the unbalanced `1 + q` |

The parameters `q` and `ratio` are supplied **by the caller**, following the design rule
recorded in `QOU/AlgebraicSubstrate/ConditionalClasses.lean`: *"an `∃` over a quantity you
get to pick cannot be false, while a `∀` about a quantity the caller supplies can."* So this
class **is refutable** — `q = 2, ratio = 0` falsifies it — which the previous `holds : Prop`
was not.

**NOT encoded — the categorical half.** The block also asserts that *the regularised crystal
functional leaves the canonical isospin swap invariant up to a single isospin-`ℤ/2`-antisymmetric
residue*, and that the residue below **is** that swap-defect. Formalising that needs a crystal
functional and a swap map the corpus does not currently carry as Lean objects; inventing them
here would encode a different claim than the one the block makes. The residue is therefore a
class *parameter* rather than a construction, and this file does not claim the identification.
That gap is the conjecture's remaining unformalised part and is stated rather than papered over.

**NOT claimed:** that the formula is derived. It is an empirical closed form matching CODATA to
~305 ppm; the block says so, and axiomatising it here is the §3b conjecture pattern, not a
derivation (AGENTS.md §"Axiomatization is NOT a Proof").

**Archimedean.** Stated over `ℝ`. The block's own text places it on the archimedean side of the
substrate wall, and the CODATA comparison is a real-number comparison, so §7c's generic-`R`
default does not apply here.

-- Ref: [leitner2026] quantum-observable-universe/mass-theory/isospin-from-canonical-bowtie.ts
-/

namespace QOU.BraidsAndKnots

/-- **CONJECTURE (D9).** Canonical `SU(2)_I` isospin from the operator-valued `⋈_K`
interface: the isospin-`ℤ/2`-antisymmetric residue of the regularised crystal functional
resolves to the substrate flavour split.

`q` is the substrate modulus and `ratio` the nucleon mass split `Δm / M_N`, both supplied
by the caller — so the class is false at values that do not satisfy `residue_eq`, which is
the point (see the header). Factor conventions are the producer's, not the glyphs'.

**No instance is provided.** Downstream results consume this as `[IsospinFromCanonicalBowtie q ratio]`
and are genuinely conditional on it.

-- Ref: [leitner2026] conj:isospin-from-canonical-bowtie -/
class IsospinFromCanonicalBowtie (q ratio : ℝ) : Prop where
  /-- The substrate modulus is a genuine deformation parameter: positive and not the
  classical point. Both are needed for `q⁻¹` to behave and for `h = q - q⁻¹` to be nonzero. -/
  q_pos : 0 < q
  /-- Away from the classical point `q = 1`, where the whole split degenerates. -/
  q_ne_one : q ≠ 1
  /-- **The content.** `Δm / M_N = ℏ_q² · h · [2]_q · (1 + ℏ_q³) / 3`, with
  `ℏ_q = 1 - q⁻¹`, `h = q - q⁻¹`, `[2]_q = q + q⁻¹` (symmetric). -/
  residue_eq :
    ratio =
      (1 - q⁻¹) ^ 2 * (q - q⁻¹) * (q + q⁻¹) * (1 + (1 - q⁻¹) ^ 3) / 3

/-- The class is **refutable**, which the previous `holds : Prop` carrier was not: at
`q = 2` the right-hand side is `(1/2)²·(3/2)·(5/2)·(1 + 1/8)/3 = 0.3515625`, so the
instance `⟨q := 2, ratio := 0⟩` cannot exist.

This is stated as a `theorem` rather than left implicit because "the carrier asserts
something" is exactly the property that was missing, and a reader should be able to see it
discharged rather than take it on the docstring's word. -/
theorem isospinFromCanonicalBowtie_refutable :
    ¬ IsospinFromCanonicalBowtie 2 0 := by
  intro hc
  have h := hc.residue_eq
  norm_num at h

end QOU.BraidsAndKnots
