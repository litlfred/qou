/-!
# `QOU.BringsSurface.WeierstrassTransitivityNotForced` — transitivity alone narrows nothing

Bean `qou-qhcr`.  Direct sequel to
`QOU.BringsSurface.BranchPointSixNotForced`, which established that Steps 3–4 of
`ex:chi-minus-six-derivation` pin `χ(A)` to the non-positive even integers **and
nothing more**, so that Step 5 alone supplies `−6` out of a countably infinite
set.  That file refuted three candidate sources for the `6`.  This file tests the
**fourth and, until now, the most promising** one.

## The route under test

The one hypothesis found in the corpus sweep that narrows `χ(A)` *without
naming six* is transitivity of the automorphism group on the Weierstrass points:

> **Laing & Singerman**, *Transitivity on Weierstrass points*, Ann. Acad. Sci.
> Fenn. Math. **37** (2012), Theorem 15 — a compact Riemann surface of genus
> `g > 2` with `g³ − g` Weierstrass points on which `Aut` acts **transitively**
> is Bring's curve (`g = 4`), or one of two genus-3 possibilities.

Since `χ = 2 − 2g`, that reads `χ(A) ∈ {−4, −6}` — an infinite set cut to two, by
a **homogeneity** hypothesis of the same register as the QOU observability axiom.
The question this file was opened to answer is whether a QOU axiom supplies it.

## The finding

**It does not, and the reason is structural rather than a failure to find the
right axiom: the hypothesis that does the narrowing is not the transitivity.**

`g³ − g` is the *total Weierstrass weight* at every genus `g ≥ 2` (Hurwitz), and
each Weierstrass point carries weight `≥ 1`.  So "`g³ − g` Weierstrass points" is
not a count appearing alongside transitivity — it is the independent hypothesis
that **every Weierstrass point is simple** (weight exactly 1).  The cited theorem
has two hypotheses, not one, and the held source says so in as many words:

> *"Laing and Singerman in [24] searched for all Riemann surfaces of genus
> `g > 2` admitting a transitive action on the Weierstrass points, **but under
> the additional assumption that such points are simple (namely, of weight
> 1)**."* — Reyes-Carocca & Speziali, §4
> (`library/arxiv-2211.08164v2/sections/sec-003-4-simple-weierstrass-points.md`)

Separating the two hypotheses is what settles the route:

* **(H1) transitivity** — proved below (`weight_constant_of_transitive`) to force
  all Weierstrass weights **equal**, and nothing further.  Its narrowing power on
  the genus is **zero**: the Accola–Maclachlan curve realises it at *every* genus
  `g ≥ 2`, and there are infinitely many non-hyperelliptic examples besides.
  That is the main theorem of the held source, and it is its title.
* **(H2) simplicity** — the constant is `1`.  This is a *genericity* condition, not
  a homogeneity one, and inside the very family the classification is about it is
  **anti-correlated with symmetry**: the two members of Laing & Singerman's
  genus-3 family `K₃` that *fail* simplicity are Fermat's quartic and `C₃`, the
  two most symmetric members (held source, §4).

So an axiom supplying homogeneity pushes *away* from the hypothesis that carries
the narrowing.  This is recorded as a **scope-(b) structural exclusion** of the
transitivity half (§6) — the invariant is an explicit infinite family in a
published, held source — and a **scope-(a)** negative on the simplicity half.

## What is nevertheless derived here

§3 gives a **self-contained narrowing that does not use the classification at
all**: transitivity + simplicity + Hurwitz's `|Aut| ≤ 84(g − 1)` forces `g ≤ 8`.
This is strictly weaker than the cited `g ∈ {3, 4}`, and it is *ours* — it needs
neither Laing & Singerman (not held) nor Reyes-Carocca & Speziali.  It is the
first narrowing of `χ(A)` in this arc obtained from a finite, cited, classical
input rather than read off Bring's curve.

§5 records a correction to the arc's framing: **`χ = −2` survives.**  The
classification is stated for `g > 2`, and genus 2 satisfies (H1) ∧ (H2)
unconditionally — every genus-2 Weierstrass point is simple, because the maximum
weight `g(g−1)/2` is itself `1` there, and the six of them carry a transitive
action.  Nothing in the chain supplies `g > 2`: Step 4 gives `g ≥ 1` and
observability gives `χ ≠ 0`, i.e. `g ≥ 2`.  So the honest conclusion of the route
is `χ(A) ∈ {−2, −4, −6}`, not `{−4, −6}`.

## Discipline

No `sorry`, no `axiom`, no `native_decide`, no `ℝ` (§7c: nothing archimedean
appears; the only types are `ℕ`, `ℤ` and two abstract carriers).  Every classical
input is a **hypothesis of the theorem that consumes it**, never an assumed
`axiom` — `genus_le_eight` takes Hurwitz's bound as an argument, so the file
proves an implication and assumes nothing (§"Axiomatization is NOT a Proof").

**Deliberately import-free.**  Every statement is closed arithmetic on `ℕ`/`ℤ`
plus one elementary group-action lemma, so `decide`, `rfl` and `omega` from core
suffice.  The module therefore verifies in a container with no olean tree at all.

## Sources for the classical inputs

* **Transitive action on the Weierstrass points, and the infinitude of examples**
  — S. Reyes-Carocca & P. Speziali, *Infinitely many Riemann surfaces with a
  transitive action on the Weierstrass points*, arXiv:2211.08164v2. **Held**:
  `library/arxiv-2211.08164v2/`, registered in `folio/schema/references.ts`,
  `library/INDEX.md:364`.  Used for: the Accola–Maclachlan family at every
  `g ≥ 2` (§1, item 1); the main theorem (infinitely many non-hyperelliptic
  transitive examples); the two-hypothesis reading of Laing & Singerman (§4); and
  Theorem 2, which *completes* Laing & Singerman's Theorem 15.
* **Laing & Singerman**, Theorem 15 — quoted as Theorem 3.4 of
  `[braden-disney-hogg-2022]`
  (`library/s40879-023-00706-0/sections/sec-008-31-weierstrass-points.md`).
  **Not separately held**; §3 below is deliberately independent of it.
* **Total Weierstrass weight `g³ − g`; maximum weight `g(g−1)/2`, attained
  exactly at hyperelliptic Weierstrass points** — classical (Hurwitz 1893).
* **`|Aut(X)| ≤ 84(g − 1)` for `g ≥ 2`** — Hurwitz's automorphism theorem,
  classical.
-/

namespace QOU.BringsSurface.WeierstrassTransitivityNotForced

universe u v

/-! ## §1. Transitivity forces equal weights — and only that

The Weierstrass weight function is an invariant of the surface, so `Aut` preserves
it.  If `Aut` acts transitively on the Weierstrass locus, the weight is therefore
**constant** on it.  That is the entire content of (H1); the lemma below is the
proof, stated for an arbitrary action on an arbitrary carrier so that nothing
about Riemann surfaces is assumed.

Note what is *not* concluded: the constant is not shown to be `1`.  §4 exhibits a
datum where it is not. -/

/-- **(H1) ⟹ equal weights.**  If a group acts transitively on `P` and `w : P → ℕ`
    is invariant under the action, then `w` is constant.

    Read on a compact Riemann surface of genus `≥ 2`: `P` is the Weierstrass
    locus, `w` the Weierstrass weight, the action that of `Aut(X)`.  Invariance is
    automatic (the weight is defined from the gap sequence, which an automorphism
    carries along), so transitivity alone gives constancy. -/
theorem weight_constant_of_transitive {P : Type u} {G : Type v}
    (act : G → P → P) (w : P → Nat)
    (hinv : ∀ (γ : G) (p : P), w (act γ p) = w p)
    (htrans : ∀ p q : P, ∃ γ : G, act γ p = q) (p q : P) :
    w p = w q := by
  cases htrans p q with
  | intro γ hγ => rw [← hγ, hinv]

/-! ## §2. The Weierstrass weight arithmetic

`totalWeight g = (g−1)·g·(g+1) = g³ − g` is the total Weierstrass weight of a
compact Riemann surface of genus `g ≥ 2` (Hurwitz).  Written with the factor
`g − 1` in front so that no `ℕ`-subtraction beyond `g − 1` ever appears, and so
that the Hurwitz bound `84(g − 1)` cancels against it in §3.

**Simplicity (H2)** is then exactly `|W| = totalWeight g`: since every weight is
`≥ 1` and the weights sum to `totalWeight g`, the number of Weierstrass points is
`≤ totalWeight g`, with equality iff every weight is `1`. -/

/-- Total Weierstrass weight of a genus-`g` surface, `g³ − g`, written so the
    `(g − 1)` factor is exposed. -/
def totalWeight (g : Nat) : Nat := (g - 1) * g * (g + 1)

/-- Euler characteristic of a closed orientable genus-`g` surface (matching
    `BranchPointSixNotForced.eulerChar`). -/
def eulerChar (g : Nat) : Int := 2 - 2 * (g : Int)

/-- The exposed-factor form really is `g³ − g`, checked across `g = 2 … 12`, the
    range §3 and §5 care about.  A wrong `totalWeight` fails this. -/
theorem totalWeight_eq_cube_sub_table :
    (List.range 11).map (fun i => totalWeight (i + 2))
      = (List.range 11).map (fun i => (i + 2) * (i + 2) * (i + 2) - (i + 2)) := by
  decide

/-! ## §3. The self-contained narrowing: `g ≤ 8`

This is the one positive result in the file, and it uses **no classification**.

Transitivity makes the Weierstrass locus a single `Aut`-orbit, so `|W|` divides
`|Aut(X)|` and in particular `|W| ≤ |Aut(X)|`.  Simplicity makes `|W| = g³ − g`.
Hurwitz bounds `|Aut(X)| ≤ 84(g − 1)`.  Cancelling the common `(g − 1)`:

    (g − 1)·g·(g + 1) ≤ 84·(g − 1)   ⟹   g(g + 1) ≤ 84   ⟹   g ≤ 8.

Every classical input is an explicit hypothesis, so the theorem is an implication
and assumes nothing. -/

/-- **Transitivity + simplicity + Hurwitz ⟹ `g ≤ 8`.**

    `hsimple` is (H2) (`|W| = g³ − g`); `horbit` is (H1) via orbit–stabiliser
    (a single orbit has size dividing, hence at most, the group order);
    `hhurwitz` is Hurwitz's `|Aut(X)| ≤ 84(g − 1)`, valid for `g ≥ 2`.

    Derived here rather than cited: it is strictly weaker than Laing &
    Singerman's `g ∈ {3, 4}`, and unlike that theorem it depends on no source
    this corpus does not hold. -/
theorem genus_le_eight (g npoints autOrder : Nat) (hg : 2 ≤ g)
    (hsimple : npoints = totalWeight g)
    (horbit : npoints ≤ autOrder)
    (hhurwitz : autOrder ≤ 84 * (g - 1)) :
    g ≤ 8 := by
  have h0 : totalWeight g ≤ 84 * (g - 1) := by
    rw [← hsimple]; exact Nat.le_trans horbit hhurwitz
  have hchain : (g - 1) * (g * (g + 1)) ≤ (g - 1) * 84 := by
    have e1 : (g - 1) * (g * (g + 1)) = totalWeight g :=
      (Nat.mul_assoc (g - 1) g (g + 1)).symm
    have e2 : (g - 1) * 84 = 84 * (g - 1) := Nat.mul_comm (g - 1) 84
    rw [e1, e2]
    exact h0
  have hpos : 0 < g - 1 := by omega
  have hle : g * (g + 1) ≤ 84 := Nat.le_of_mul_le_mul_left hchain hpos
  cases Nat.lt_or_ge 8 g with
  | inr h8 => exact h8
  | inl h8 =>
      have h90 : 9 * 10 ≤ g * (g + 1) :=
        Nat.mul_le_mul (by omega) (by omega)
      exact absurd (Nat.le_trans h90 hle) (by decide)

/-- The bound of `genus_le_eight` is **attained by the arithmetic**, i.e. the
    proof is not throwing away a factor: at `g = 8` the inequality
    `g(g + 1) ≤ 84` still holds, and at `g = 9` it fails.  So `8` is the exact
    cut-off of this argument, not an artefact. -/
theorem eight_is_sharp_for_this_argument :
    8 * (8 + 1) ≤ 84 ∧ ¬ (9 * (9 + 1) ≤ 84) := by decide

/-! ## §4. Transitivity alone: zero narrowing power

The Accola–Maclachlan curve of genus `g` is hyperelliptic with `2g + 2`
Weierstrass points, each of the maximal weight `g(g−1)/2`, and its automorphism
group acts **transitively** on them — at *every* genus `g ≥ 2` (held source, §1,
item 1; the infinitude was already noted by Laing & Singerman).

Weights are carried **doubled** below (`2w = g(g−1)`) so that no `ℕ`-division
appears anywhere; simplicity is then the statement `2w = 2`.

The two theorems are: the datum is *arithmetically consistent at every genus*
(so nothing in the Weierstrass arithmetic obstructs transitivity anywhere), and
it *fails simplicity at every genus `≥ 3`* (so it is invisible to the
classification while still being transitive).  Together: **(H1) cuts out no
genus whatsoever.** -/

/-- Weierstrass-point count of a hyperelliptic surface of genus `g`. -/
def hyperellipticPoints (g : Nat) : Nat := 2 * g + 2

/-- **Twice** the Weierstrass weight of a hyperelliptic Weierstrass point at
    genus `g`.  The weight is `g(g−1)/2`, the maximum possible; doubling keeps
    the file free of `ℕ`-division. -/
def twiceHyperellipticWeight (g : Nat) : Nat := g * (g - 1)

/-- **The datum is consistent at every genus `≥ 2`.**  `|W| · (2w) = 2 · (g³ − g)`,
    i.e. the `2g + 2` hyperelliptic Weierstrass points of weight `g(g−1)/2` carry
    exactly the total Weierstrass weight.  Stated at `g = k + 2` so that `g ≥ 2`
    is structural rather than a hypothesis. -/
theorem accola_datum_total (k : Nat) :
    hyperellipticPoints (k + 2) * twiceHyperellipticWeight (k + 2)
      = 2 * totalWeight (k + 2) := by
  show (2 * (k + 2) + 2) * ((k + 2) * (k + 1)) = 2 * ((k + 1) * (k + 2) * (k + 3))
  have h : 2 * (k + 2) + 2 = 2 * (k + 3) := by omega
  rw [h, Nat.mul_assoc]
  congr 1
  rw [Nat.mul_comm (k + 3) ((k + 2) * (k + 1)), Nat.mul_comm (k + 2) (k + 1)]

/-- **The datum fails simplicity at every genus `≥ 3`**: the common weight is
    `g(g−1)/2 ≥ 3`, never `1`.  So the Accola–Maclachlan curves are transitive
    (H1) and non-simple (¬H2) at every genus from 3 up — they are exactly the
    witnesses that transitivity alone classifies nothing. -/
theorem accola_datum_not_simple (k : Nat) :
    twiceHyperellipticWeight (k + 3) ≠ 2 := by
  show (k + 3) * (k + 2) ≠ 2
  have h6 : 3 * 2 ≤ (k + 3) * (k + 2) :=
    Nat.mul_le_mul (by omega) (by omega)
  exact fun h => absurd (h ▸ h6) (by decide)

/-- Consequently the datum's point-count misses `totalWeight` at every genus
    `≥ 3` — i.e. `|W| < g³ − g`, the inequality that makes it invisible to a
    theorem hypothesising `g³ − g` Weierstrass points. -/
theorem accola_points_ne_totalWeight (k : Nat) :
    hyperellipticPoints (k + 3) ≠ totalWeight (k + 3) := by
  show 2 * (k + 3) + 2 ≠ (k + 2) * (k + 3) * (k + 4)
  have h1 : 2 * (k + 3) ≤ (k + 2) * (k + 3) :=
    Nat.mul_le_mul (by omega) (Nat.le_refl _)
  have h2 : 2 * (k + 3) * 4 ≤ (k + 2) * (k + 3) * (k + 4) :=
    Nat.mul_le_mul h1 (by omega)
  have h3 : 2 * (k + 3) + 2 < 2 * (k + 3) * 4 := by omega
  exact Nat.ne_of_lt (Nat.lt_of_lt_of_le h3 h2)

/-! ## §5. Genus 2 survives — the route gives `{−2, −4, −6}`, not `{−4, −6}`

Laing & Singerman's theorem, and its completion by Reyes-Carocca & Speziali
(Theorem 2), are both stated for genus `> 2`.  That restriction is a hypothesis,
not a conclusion, and genus 2 satisfies (H1) ∧ (H2) outright:

* the maximum Weierstrass weight is `g(g−1)/2 = 1` at `g = 2`, so **every**
  genus-2 Weierstrass point is simple — (H2) holds for *every* genus-2 surface;
* there are `2g + 2 = 6` of them, and `totalWeight 2 = 6` agrees;
* the Accola–Maclachlan curve of genus 2 has `Aut` transitive on them (held
  source, §1, item 1, which states the family for `g ≥ 2`).

Nothing in `ex:chi-minus-six-derivation` supplies `g > 2`: Step 4 gives `g ≥ 1`
and observability gives `χ ≠ 0`, i.e. `g ≥ 2`.  So `χ = −2` is admissible and the
route's honest output is a **three**-element set. -/

/-- **Genus 2 satisfies both hypotheses.**  The hyperelliptic point count, the
    total weight and the doubled weight all agree at `g = 2`: six simple
    Weierstrass points.  (At `g = 2` the hyperelliptic datum *is* the general
    datum — every genus-2 surface is hyperelliptic.) -/
theorem genus_two_transitive_and_simple :
    totalWeight 2 = 6
      ∧ hyperellipticPoints 2 = 6
      ∧ twiceHyperellipticWeight 2 = 2
      ∧ hyperellipticPoints 2 = totalWeight 2 := by decide

/-- Genus 2 is the *only* genus at which the hyperelliptic datum is simple: the
    doubled weight equals 2 exactly there.  So §4's witnesses start at `g = 3`,
    and `g = 2` is a genuine member of the admissible set rather than another
    Accola–Maclachlan counterexample. -/
theorem hyperelliptic_simple_iff_genus_two (g : Nat) (hg : 2 ≤ g) :
    twiceHyperellipticWeight g = 2 ↔ g = 2 := by
  constructor
  · intro h
    cases Nat.lt_or_ge g 3 with
    | inl h3 => omega
    | inr h3 =>
        have h6 : 3 * 2 ≤ g * (g - 1) :=
          Nat.mul_le_mul (by omega) (by omega)
        exact absurd ((show g * (g - 1) = 2 from h) ▸ h6) (by decide)
  · intro h; subst h; decide

/-- The admissible Euler characteristics after the **classification** (genus 2,
    plus Laing & Singerman's `g ∈ {3, 4}` as completed by Reyes-Carocca &
    Speziali Theorem 2).  `−6` is in the list, and so are two others. -/
theorem classification_admissible_chi :
    [eulerChar 2, eulerChar 3, eulerChar 4] = [(-2 : Int), -4, -6] := by decide

/-- The admissible Euler characteristics under the **self-contained** §3 bound
    alone (`2 ≤ g ≤ 8`), with no classification input.  Seven values, a genuine
    narrowing from the infinite set that Steps 3–4 leave, and not to `−6`. -/
theorem hurwitz_admissible_chi :
    (List.range 7).map (fun i => eulerChar (i + 2))
      = [(-2 : Int), -4, -6, -8, -10, -12, -14] := by decide

/-- `−6` is admissible under both hypothesis sets and unique under neither.  This
    is the file's bottom line in one statement: the route narrows, and does not
    select. -/
theorem minus_six_admissible_not_unique :
    (-6 : Int) ∈ [eulerChar 2, eulerChar 3, eulerChar 4]
      ∧ (-4 : Int) ∈ [eulerChar 2, eulerChar 3, eulerChar 4]
      ∧ (-2 : Int) ∈ [eulerChar 2, eulerChar 3, eulerChar 4] := by decide

/-! ## §6. Scope of the negative, per AGENTS.md §"Before declaring refuted"

* **Scope (b) — structural exclusion of the transitivity half.**  Transitivity
  alone, *however it is sourced*, cannot narrow `χ(A)`: the Accola–Maclachlan
  curves realise it at every genus `g ≥ 2` (held source, §1 item 1), and the
  held source's main theorem adds infinitely many non-hyperelliptic examples.
  The invariant is an explicit infinite family in a published source, and §4
  carries its arithmetic.  This is not "no axiom was found"; it is "there is
  nothing here for an axiom to supply".
* **Scope (a) — the simplicity half.**  No QOU axiom was found that supplies
  (H2), and none of the surfaces searched carries one.  That is an absence of
  evidence over the surfaces named in bean `qou-qhcr`, not a proof that no
  axiom could.  What *is* argued structurally — and it is an argument, not a
  theorem — is that (H2) is a genericity condition anti-correlated with
  symmetry inside the classification's own family, so a homogeneity axiom is
  the wrong shape to supply it.
* **Not excluded.**  `g = 4` may still be right, and the classification is
  genuine mathematics; §3's `g ≤ 8` is a real narrowing.  What is excluded is
  the reading under which *transitivity* is the hypothesis doing the work. -/

/-! ## §7. What the axioms actually say (recorded, not formalised)

The corpus encodes observability twice, and neither encoding reaches a surface
automorphism group:

* `QOU.FluidDynamics.QOUFluidUniverse.observability` is an **opaque `Prop`
  field** with no content at all.
* `QOU.FluidDynamics.ObservabilityData` gives it its only content in the corpus:
  a single `hom_rank : ℕ` with `observable : hom_rank = 0`, i.e.
  `Hom_𝐂(𝟙, Ad(A)) = 0`.

That is a statement about a Hom-space in the monoidal category — about the
algebra object `A`.  There is no theorem in the corpus relating it to
`Aut(M₀)` acting on anything, let alone on a Weierstrass locus.  Supplying (H1)
from it would require building that bridge; and by §6 the bridge would buy
nothing, because (H1) narrows nothing.  Deliberately left as prose: a
non-existence claim about the corpus is not a Lean proposition, and inventing a
class to carry it would be the self-assuming projection §3b-cond item 5
forbids. -/

end QOU.BringsSurface.WeierstrassTransitivityNotForced
