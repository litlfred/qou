import QOU.MathlibExt.YoungDiagramCells
import QOU.BraidKnot.IdentityAArmLeg
import QOU.BraidKnot.TableauContent
import QOU.BraidKnot.JucysMurphy
import QOU.BraidKnot.PieceAGeneral
import QOU.MathlibExt.QPartitionCombinatorics
import QOU.MathlibExt.WenzlSchurElement
import QOU.BraidKnot.TwoFiltrationBridge
import QOU.SchurWeyl.HoefsmitRep
import QOU.QBeta.WenzlWeightVanishing
import QOU.Hecke.Hoefsmit
import QOU.HeckeAlgebra.JonesMarkovWenzl

/-!
# Bridges from the scattered cell statistics onto the single home

Bean `qou-cdup`. `QOU.MathlibExt.YoungDiagramCells` is the one home for
`content` / `arm` / `leg` / `hook`; this file connects the pre-existing copies
to it, so a lemma proved against one is usable against any other.

## Why bridges rather than a migration

Deleting each local definition and rewriting its call sites would touch proofs
in six modules at once. These lemmas are **purely additive** — no existing file
changes — and they are what a later migration would rewrite along. They also
*test* a claim I had so far only asserted, in a bean and two commit messages,
namely that every copy is definitionally equal so every bridge is `rfl`.

## What the test found

**Thirteen bridges land: twelve by `rfl`, one conditional. Two copies cannot be
bridged at all.** Broken down, because a single number here would hide the two
different things being counted — *content* copies, and *arm/leg/hook* copies:

| | reachable | `rfl` |
|---|---|---|
| `content` copies (8 in the tree) | **6** | 6 |
| `arm` / `leg` / `hook` copies (2 sets) | 2 | 6 lemmas |
| `hookLength` (ℕ-valued) | 1 | **no** — needs `c ∈ μ` |

The blanket claim I had been repeating — *"eight copies, each a `rfl` bridge"* —
was wrong in both directions:

* **Two copies are unreachable.** `QOU.BraidsAndKnots.cellContent`
  (`mass-theory/y-lambda-recipe-from-partition.lean`) and
  `QOU.BraidKnot.cellContent`
  (`mass-theory/jucys-murphy-central-elements-qou.lean`) live in **standalone
  content-block siblings**, not library modules, so nothing can import them.
  The second is additionally the clash partner from the `cdup` record — it
  shares a fully-qualified name with a library declaration — so it is
  *unbridgeable by construction*: importing both is the very error the bridge
  would have to survive.
* **`hookLength` is not `rfl`.** `TwoFiltrationBridge.hookLength` is valued in
  `ℕ` with truncated subtraction, so it agrees with the `ℤ`-valued `hook` only
  **on cells of the diagram** — off-diagram the ℕ version saturates at `0`
  while the ℤ version goes negative. It is a real lemma with a hypothesis, and
  recording it as "a `rfl` bridge" would have been wrong.

So the honest count for the migration is: six free, one conditional, two
requiring the sibling to be promoted to a library module first.

**Superseded — read the 2026-08-24 section below before trusting the table
above.** Re-measured from the tree rather than from this record, there are
**ten** reachable `content` copies, not eight; four were never listed anywhere,
including one this record explicitly claimed does not exist. `axialDistance` is
duplicated three times, and that is where the duplication stops being cosmetic.
-/

namespace QOU.MathlibExt.YoungDiagramCells

/-! ### The six free bridges

Each is `rfl`: the definitions are syntactically identical up to binder name. -/

theorem content_eq_identityAArmLeg (c : ℕ × ℕ) :
    content c = QOU.BraidKnot.IdentityAArmLeg.content c := rfl

theorem content_eq_tableauContent (c : ℕ × ℕ) :
    content c = QOU.BraidKnot.TableauContent.content c := rfl

theorem content_eq_jucysMurphy (c : ℕ × ℕ) :
    content c = QOU.BraidKnot.JucysMurphy.cellContent c := rfl

theorem content_eq_pieceA (c : ℕ × ℕ) :
    content c = QOU.BraidKnot.PieceA.contentZ c := rfl

/-- The curried copies take `(i j : ℕ)` rather than a pair, so the bridge is
stated at the uncurried point. Still `rfl`. -/
theorem content_eq_qPartitionCombinatorics (i j : ℕ) :
    content (i, j) = QOU.MathlibExt.QPartitionCombinatorics.cellContent i j := rfl

theorem content_eq_wenzlSchurElement (i j : ℕ) :
    content (i, j) = QOU.MathlibExt.WenzlSchurElement.cellContent i j := rfl

/-! ### Arm, leg and hook -/

theorem arm_eq_identityAArmLeg (μ : YoungDiagram) (c : ℕ × ℕ) :
    arm μ c = QOU.BraidKnot.IdentityAArmLeg.arm μ c := rfl

theorem leg_eq_identityAArmLeg (μ : YoungDiagram) (c : ℕ × ℕ) :
    leg μ c = QOU.BraidKnot.IdentityAArmLeg.leg μ c := rfl

theorem hook_eq_identityAArmLeg (μ : YoungDiagram) (c : ℕ × ℕ) :
    hook μ c = QOU.BraidKnot.IdentityAArmLeg.hook μ c := rfl

theorem arm_eq_pieceA (μ : YoungDiagram) (c : ℕ × ℕ) :
    arm μ c = QOU.BraidKnot.PieceA.armZ μ c := rfl

theorem leg_eq_pieceA (μ : YoungDiagram) (c : ℕ × ℕ) :
    leg μ c = QOU.BraidKnot.PieceA.legZ μ c := rfl

theorem hook_eq_pieceA (μ : YoungDiagram) (c : ℕ × ℕ) :
    hook μ c = QOU.BraidKnot.PieceA.hookZ μ c := rfl

/-! ### The one conditional bridge

`hookLength` is `ℕ`-valued with truncated subtraction, so it agrees with `hook`
only where the cell is actually in the diagram. This is the lemma my earlier
"every bridge is `rfl`" claim mis-described. -/

theorem hook_eq_hookLength {μ : YoungDiagram} {c : ℕ × ℕ} (hc : c ∈ μ) :
    hook μ c = (QOU.BraidKnot.TwoFiltrationBridge.hookLength μ c : ℤ) := by
  have hj : c.2 < μ.rowLen c.1 := (YoungDiagram.mem_iff_lt_rowLen).mp hc
  have hi : c.1 < μ.colLen c.2 := (YoungDiagram.mem_iff_lt_colLen).mp hc
  simp only [hook, arm, leg, QOU.BraidKnot.TwoFiltrationBridge.hookLength]
  omega

/-! ## 2026-08-24 — four more `content` copies, and the `axialDistance` pair

Re-measured from scratch rather than from the record above, and the record was
wrong again — in the direction that matters, *under*-counting.

**There are ten `content` copies in the library tree, not six.** Four were never
listed anywhere:

| declaration | file | why it was missed |
|---|---|---|
| `QOU.SchurWeyl.cellContent` | `SchurWeyl/HoefsmitRep.lean:115` | a `cdup` note claimed this one "does not exist" |
| `QOU.QBeta.WenzlWeight.content` | `QBeta/WenzlWeightVanishing.lean:91` | never listed |
| `QOU.Hecke.content` | `Hecke/Hoefsmit.lean:80` | never listed |
| `QOU.HeckeAlgebra.JonesMarkovWenzl.cellContent` | `HeckeAlgebra/JonesMarkovWenzl.lean:195` | never listed; carries an unused `Partition` argument, so a signature-shaped search misses it |

All four are `rfl`. The last takes a partition it ignores (`_lam`), which is why
it looks like a different function and is not.

**Importing all of them together is safe.** These six modules had never been
co-imported; doing so here is itself the test that no two of the ten share a
fully-qualified name. They do not — this file compiles.

### The `axialDistance` pair — the reason this stopped being cosmetic

`content` being duplicated costs duplicated effort. `axialDistance` being
duplicated costs a **silent `rw` failure**, which is a different kind of bug:

`QOU.SchurWeyl.axialDistance` and `QOU.BraidKnot.TableauContent.axialDistance`
are `rfl`-equal but are *different constants*. Inside `namespace QOU.SchurWeyl`
a bare `axialDistance` resolves to the first **even under `open
QOU.BraidKnot.TableauContent`** — the enclosing namespace wins over the `open`.
So a `rw` with a lemma stated in the other does not fire, and the error prints
the two sides *identically* (`axialDistance c (a, ν.rowLen a)` both times),
differing only in a fully-qualified name buried in the pattern line.

Live instances already on opposite sides of that line:
`MarkovAssembly.markov_of_corner_identity` uses the first,
`SeminormalNodeForm.axialDistance_corner_addable` the second;
`QOU.SchurWeyl.axialDistance_eq_tableauContent` in `SchurWeyl/WenzlMarkovCorner.lean`
is the ad-hoc bridge written to compose them. That lemma stays where it is —
callers depend on it — but it is now an instance of a general pattern rather
than a one-off.

### The third `axialDistance` is in scope after all

`QOU.Hecke.axialDistance` was set aside as "tableau-indexed, a different
signature, probably not part of this drain". Checked rather than assumed, and
that is **wrong on the part that matters**: it is a different signature, but it
is *built on a fourth undocumented copy of `content`* (`QOU.Hecke.content`,
above), and it bridges — conditionally, one lemma per branch of its `dite`.
Being differently-shaped kept it out of the duplication count while leaving it
squarely inside the duplication. -/

/-! ### The four `content` copies the record missed — all `rfl` -/

theorem content_eq_schurWeyl (c : ℕ × ℕ) :
    content c = QOU.SchurWeyl.cellContent c := rfl

theorem content_eq_qBetaWenzlWeight (c : ℕ × ℕ) :
    content c = QOU.QBeta.WenzlWeight.content c := rfl

theorem content_eq_hecke (i j : ℕ) :
    content (i, j) = QOU.Hecke.content i j := rfl

/-- `JonesMarkovWenzl.cellContent` takes a partition it never uses (`_lam`,
kept for call-site symmetry with `cellHookLength`). The bridge holds for every
partition, which is the precise sense in which the argument is inert. -/
theorem content_eq_jonesMarkovWenzl {n : ℕ} (lam : Nat.Partition n) (i j : ℕ) :
    content (i, j) = QOU.HeckeAlgebra.JonesMarkovWenzl.cellContent lam i j := rfl

/-! ### `axialDistance` -/

theorem axialDistance_eq_schurWeyl (c d : ℕ × ℕ) :
    axialDistance c d = QOU.SchurWeyl.axialDistance c d := rfl

theorem axialDistance_eq_tableauContent (c d : ℕ × ℕ) :
    axialDistance c d = QOU.BraidKnot.TableauContent.axialDistance c d := rfl

/-- The two duplicates are therefore equal to each other. This is the composite
that `QOU.SchurWeyl.axialDistance_eq_tableauContent` states directly; deriving it
here shows it is not special — it is what any two copies give. -/
theorem schurWeyl_axialDistance_eq_tableauContent (c d : ℕ × ℕ) :
    QOU.SchurWeyl.axialDistance c d = QOU.BraidKnot.TableauContent.axialDistance c d :=
  (axialDistance_eq_schurWeyl c d).symm.trans (axialDistance_eq_tableauContent c d)

/-! ### The tableau-indexed third copy

`QOU.Hecke.axialDistance` reads two cells out of a standard tableau and takes
their content difference, with a `dite` guarding `k+1 < n` and a `+1` index
shift (its tableau coordinates are 0-based, its contents 1-based). It is not
pointwise-equal to anything, so it gets one lemma per branch. -/

theorem hecke_axialDistance_eq_of_lt {n : ℕ} {lam : QOU.Hecke.Partition n}
    (T : QOU.Hecke.StandardYoungTableau lam) (k : Fin n) (h : k.val + 1 < n) :
    QOU.Hecke.axialDistance T k
      = axialDistance ((T.cells k).1 + 1, (T.cells k).2 + 1)
          ((T.cells ⟨k.val + 1, h⟩).1 + 1, (T.cells ⟨k.val + 1, h⟩).2 + 1) := by
  simp only [QOU.Hecke.axialDistance, dif_pos h, axialDistance, content, QOU.Hecke.content]

theorem hecke_axialDistance_eq_zero {n : ℕ} {lam : QOU.Hecke.Partition n}
    (T : QOU.Hecke.StandardYoungTableau lam) (k : Fin n) (h : ¬ (k.val + 1 < n)) :
    QOU.Hecke.axialDistance T k = 0 := by
  simp only [QOU.Hecke.axialDistance, dif_neg h]

/-- The `+1` shift is a translation of both cells, so it cancels: the Hecke
axial distance is the canonical one on the *unshifted* tableau coordinates.
This is what makes the shift a bookkeeping convention rather than a difference
in the quantity being computed. -/
theorem hecke_axialDistance_eq_unshifted {n : ℕ} {lam : QOU.Hecke.Partition n}
    (T : QOU.Hecke.StandardYoungTableau lam) (k : Fin n) (h : k.val + 1 < n) :
    QOU.Hecke.axialDistance T k
      = axialDistance (T.cells k) (T.cells ⟨k.val + 1, h⟩) := by
  rw [hecke_axialDistance_eq_of_lt T k h]
  simp only [axialDistance, content]
  push_cast
  ring

end QOU.MathlibExt.YoungDiagramCells
