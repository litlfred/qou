# Kontsevich–Soibelman 0811.2435 vs QOU — dictionary, what to borrow, what to avoid

**Date:** 2026-06-04
**Source paper:** Maxim Kontsevich, Yan Soibelman, *Stability structures, motivic
Donaldson–Thomas invariants and cluster transformations*, arXiv:0811.2435v1
(148 pp, 16 Nov 2008). PDF now in the corpus at
[`uploads/0811.2435v1.pdf`](../../uploads/0811.2435v1.pdf) (added by the owner in
commit `1372394e`).
**Supporting cast** (all in [`uploads/`](../../uploads/), uploaded alongside): the
Kashaev/quantum-modularity refinement (Garoufalidis–Zagier `2111.06645`), the
microlocal-Lagrangian / constructible-sheaf Euler-characteristic paper
(Franecki–Kapranov `9909088`), the geometry of Markov traces (Webster–Williamson
`0911.4494`; Geck–Lambropoulou `0405508`; Orellana `9806163`), Yekutieli
multiplicative integration (`1007.1250` = `[yekutieli2015]`), Lusztig-cone /
canonical-basis combinatorics (Marsh `0008040`), surreal exp-log classes
(Kuhlmann–Matusinski `1203.4538`), and the unital-Gröbner-basis / simpler-PBW
paper (`0409565`).
**Prior QOU mention:** [`docs/audits/2026-05-18-d2a-categorical-thimble-resolution.md`](2026-05-18-d2a-categorical-thimble-resolution.md)
§Tier 4 flagged KS as a wall-crossing literature tier but developed no comparison.
This doc is that comparison.

---

## 0. Verdict table (answers to every question, scannable)

| # | Owner question | Short verdict |
|---|---|---|
| Q1 | Special Lagrangian ≈ QOU observables? Do we show it? | **Right pattern, not yet shown explicitly.** SLags are the *stable objects* of the Fukaya category; QOU observables are the *central/trace elements*. The shared abstraction is "category + numerical realization + trace invariant." A dictionary block is worth adding; it buys **exposition + reuse**, not a free theorem. |
| Q2 | Translate "real volume form" into algebraic + archimedean QOU terms? SLag = commutative QOU = trace/central? | **Yes, cleanly — and your translation is structurally correct.** *Lagrangian* ↔ maximal-commutative subalgebra (center / character ring, where the skew Euler form vanishes); *special* ("restriction of holomorphic volume form is **real**") ↔ the archimedean functor τ landing in **ℝ** at the real substrate q₀ (the `lusztig_q_0_imaginary_part_zero` reality condition). So: SLag ↔ {real-valued simultaneously-observable central elements} ↔ image of the Markov trace. |
| Q3 | Crystal-bases flow = twisting observables in the quantum space? | **Partly.** Crystal/canonical bases *organize* the partition labels (λ ⊢ n) the observables live on; the actual *twist* of a QOU observable is the **bar-involution** q ↦ q⁻¹ (Lusztig) + chirality/q-Reeb phase. The crystal *limit* is q→0; QOU evaluates at q₀≈1.11, the opposite end. KS's "flow" is the cluster/WCF mutation — which QOU declines (Q8). |
| Q4 | Do we need the ind-constructible A∞ assumption? Were they lazy? | **Not lazy — it's the minimal tameness hypothesis that makes motivic integration well-defined** on the moduli stack of objects of a *general* 3CY A∞-category. QOU does **not** need to assume it: the **GB normal form gives finite slices per Coxeter length** (constructible by theorem), and the **jet order + surreal exp-log grading** controls the tower. QOU pays a smaller price because its category is the specific Hecke/braid category, not an arbitrary 3CY. |
| Q5 | Is the paper a special case of a QOU? | **Neither is literally a special case of the other.** Both instantiate (linear/monoidal category **C** + numerical realization to ℂ/ℝ + trace-type invariant). KS is far more general on geometry (any 3CY, *varying* stability); QOU is far more rigorous (Lean) and pinned (Hecke, *fixed* q₀, physical observables). Cousins under one abstraction, not subset/superset. |
| Q6 | Is their Theorem 1 part of QOU axioms (paper = example)? | **No.** KS Theorem 1 = "the central-charge map Stab(C) → Hom(Γ,ℂ) is a local homeomorphism" (Bridgeland deformation, generalized). It is a statement about the **moduli space of stability conditions** — exactly the apparatus QOU *declines* by sitting at one calibrated point. QOU's analog axiom is "τ at fixed q₀ is well-defined/unique" (`archimedean-functor-uniqueness`), which is the *rigid* opposite of a deformation theorem. |
| Q7 | Can we use their (mostly algebraic) infrastructure? Euler form? Easier proofs or pretty story? | **Mostly pretty story + exposition; two concrete reusables.** (a) The **Euler form** χ(E,F)=Σ(−1)ⁿdim Extⁿ on K₀^num is the Grothendieck-shadow of QOU's **Frobenius/Markov pairing** — a clean exposition upgrade and a naming bridge (we already have `euler-char-stability`). (b) The **motivic Thom–Sebastiani factorization** (KS Thm 6, a *cited, rigorous* Denef–Loeser-type result) is the categorical parent of Wenzl **disjoint multiplicativity** tr_M(K⊔K′)=tr_M(K)·tr_M(K′), already in production. The rest is heuristic (see §1). |
| Q8 | Is the multiplicative WCF the archimedean wall we avoid? Kashaev a sub-part (trivial knot)? | **Yes on both.** The WCF's walls live in the space of central charges Z:Γ→**ℂ** — an archimedean/real-analytic locus (arg Z(γ₁)=arg Z(γ₂)). KS build the formal WCF over a **non-archimedean** field and only *speculate* (String Theory) an archimedean manifold M (§1.5). QOU avoids the wall by **fixing q₀ and staying in ℚ(q)/generic-R until the final τ** (the CLAUDE.md §7c base-ring wall = the same wall). Kashaev **is** a sub-part: `QOU.Kashaev.VolumeConjecture` (tr_M ~ exp Vol); the unknot/trivial rep σ₀ is literally a column index in Garoufalidis–Zagier's refined matrix invariant. |
| Q9 | Why don't the exp()-algebra people go straight to Wedderburn/partitions? | **Because their algebra isn't semisimple/finite-dimensional.** KS's exp() lives in an *infinite-dimensional, non-semisimple* world (the quantum torus, the pro-nilpotent group GV of dilogarithm Hamiltonian flows, the motivic Hall algebra) where Wedderburn ⊕ M_{d_λ} simply does not apply. **QOU's central structural bet is to engineer the problem into the generically-semisimple Hecke algebra H_n(q)**, where Wedderburn/partition decomposition *is* available — so QOU *can* "go straight to partitions," and does. This is arguably QOU's single biggest methodological win over the KS/exp school. |
| Q10 | Relation to KLR? | **One step removed, and QOU already lives on the KLR side.** KS-WCF → (their follow-up) Cohomological Hall Algebra → KLR / quiver-Hecke (Schiffmann–Vasserot, Varagnolo–Vasserot) → canonical/crystal basis. QOU uses KLR-adjacent tools directly (CLAUDE.md §7b type-B folding, KL-basis classical limit, Demazure resonances; `klr_canonical_basis_filter.py`, `crystal_basis.py`; Marsh `0008040`). QOU sits on the categorified-basis side and *omits* the WCF dynamics on top. |

---

## 1. The rigor caveat (read first — the owner's warning)

> *"Kontsevich never quite proves anything… some of his 'trivial' assertions are
> far from it. Careful."* — repo owner, 2026-06-04.

This is correct and load-bearing for everything below. Direct textual evidence
from the paper itself:

- **Theorem 3** (existence/uniqueness of the lifted stability section):
  *"We are going to sketch the proof leaving the details for the reader."*
- **Theorem 4** (the monodromy = wall-crossing formula): *"Here we also present a
  sketch of the proof."*
- The **whole edifice** rests on foundational objects asserted to exist:
  the **motivic Hall algebra** and the homomorphism to the **motivic quantum
  torus** (depends on **orientation data** / a square root of the canonical
  bundle that is only later, partially, constructed), the **ind-constructibility**
  of the stack of objects, and the **Support Property**. Several of these were
  tightened only in *later* papers (and some remain folklore).

**Consequence for QOU.** Importing a KS "theorem" does **not** confer rigor.
The QOU discipline is the opposite: Lean-verified, `sorry`-tracked, three-
calibration, formalize-first. So the correct posture is:

1. **Borrow the *dictionary and the story*** (the §3 table) — for exposition,
   motivation, and to know *where to look*.
2. **Borrow only the *cited, externally-rigorous* lemmas** — e.g. the motivic
   Thom–Sebastiani factorization KS attribute to others (Denef–Loeser-type),
   or Bridgeland's actual deformation theorem behind their Theorem 1.
3. **Never** restate a KS sketch as a QOU proposition/Lean statement. If a KS
   assertion is genuinely wanted as QOU content, it must be **re-proved from
   scratch** under the §3b conjectural-propagation rules (axiomatize as a `class`,
   carry it as an explicit hypothesis), not cited as established.

This mirrors the existing `2026-05-30-klr-dialog-assessment.md` verdict (external
re-pitches of fashionable categorical machinery rarely *shorten* a QOU proof) and
the `production-vs-exploratory-discipline` skill.

---

## 2. What the paper actually is (one paragraph)

KS define a **non-commutative compact 3d Calabi–Yau variety** as an Ext-finite,
**ind-constructible**, k-linear triangulated **A∞-category C**. A **stability
structure** is (Css, Z) — a class Css of *semistable* objects plus a **central
charge** Z : Γ → ℂ on the numerical Grothendieck lattice Γ = K₀^num(C) (= K₀ mod
the radical of the **Euler form** χ(E,F)=Σ(−1)ⁿdim Extⁿ(E,F), which is
skew-symmetric in odd CY dimension). The **generalized Donaldson–Thomas
invariant** Ω(γ) is the virtual "number" of stable objects of class γ. As you
vary Z and cross a **wall of marginal stability** (where two charges become
phase-aligned), the Ω(γ) jump; the **multiplicative wall-crossing formula** says a
certain product of automorphisms of a **quantum torus** — with factors built from
the **quantum dilogarithm** — stays invariant (monodromy = identity around a wall
intersection, their Theorem 4). The invariants are realized **motivically** (in a
quantum torus over a ring of motivic functions), with **q-analogs** via Serre
polynomials and a quasi-classical limit q^{1/2} → −1.

The geometric anchor (their **footnote 1**, the line you quoted):

> *"Recall that a Lagrangian submanifold L ⊂ X is called **special** iff the
> restriction to L of a holomorphic volume form on X is a **real** volume form on
> L."*

In the Fukaya/A-brane category these special Lagrangians **are the stable
objects**, with central charge Z(L) = ∫_L Ω (a period of the holomorphic volume
form) and **|Z(L)| = vol(L)** (their Remark 1, large-volume limit). "Special" =
the phase arg(Ω|_L) is constant = **calibration**.

---

## 3. The dictionary (KS ↔ QOU)

Status legend: 🟢 rigorous/structural on both sides · 🟡 analogy good but only
heuristic so far · 🔴 KS side is sketch/speculation — do not import.

| KS 0811.2435 object | QOU object | Match | Notes |
|---|---|---|---|
| A∞ / triangulated category **C** (objects = sheaves / A-branes) | rigid monoidal **C**; Hecke category H_n(q)-mod / braid words | 🟡 | Both are the "ambient category." QOU's is far smaller and concrete. |
| **Stable object** = special Lagrangian L | **Observable** = central/trace element (χ^λ, image of tr_M) | 🟡 | The §0/Q1–Q2 identification. SLag stable ↔ "saturates" a calibration; QOU observable ↔ a Wedderburn-block character. |
| **Central charge** Z : Γ → ℂ, Z(L)=∫_L Ω | **Archimedean functor** τ : C → Vec_ℝ at q₀ (period/eval → MeV) | 🟢 | Both are *the* numerical realization. KS varies Z (moduli); QOU **pins** τ by 3 calibrations. `archimedean-realization-functor.md`. |
| `|Z(L)|` = vol(L) (calibration) | `|tr_M(𝓑_K)|` = mass; tr_M ~ exp(Vol) (Kashaev) | 🟢 | The modulus-of-period = volume statement is *literally* QOU's mass=`m_e·Geom_full` / `QOU.Kashaev.VolumeConjecture`. |
| **"special"** = Ω\|_L is a **real** volume form | τ lands in **ℝ** at real q₀; Im(q₀)=0 (`lusztig_q_0_imaginary_part_zero`) | 🟢 | The reality/calibration condition = the archimedean reality condition. This is the cleanest single translation. |
| **Lagrangian** (⟨•,•⟩ vanishes on L) | **maximal-commutative** subalgebra (center / character ring; q-torus commutes when ⟨γ₁,γ₂⟩=0) | 🟢 | "Lagrangian = isotropic-maximal = commutative observables." Your "commutative QOU = observables = trace/central" is exactly this. |
| **Euler form** χ(E,F) on Γ=K₀^num | **Frobenius / Markov pairing** ⟨a,b⟩_F; self-duality Ψ=S²=id | 🟢 | χ is the Grothendieck-group shadow of the Frobenius pairing. QOU already has `euler-char-stability`, `crossed-module-euler-characteristic`. |
| Γ = K₀^num (lattice of charges) | partitions λ ⊢ n (Wedderburn block labels) | 🟡 | Both index the "irreducible content." QOU's is the partition lattice; KS's is a charge lattice with skew form. |
| **Quantum torus** + **quantum dilogarithm** factors | **Habiro ring** / Φ_q (Faddeev, `[faddeev1994]`) / Li₂^q (Rogers) | 🟢 | Same special function. QOU's Φ_q vs Li₂^q bar-symmetry split (cheat-sheet §4) is finer than KS's single E(x). |
| **Wall of marginal stability** / cluster transformation / WCF | **the wall QOU avoids** (CLAUDE.md §7c generic-R ↔ ℝ; fixed q₀) | 🟢 | See §4. KS *crosses* walls; QOU *never approaches* one. |
| **ind-constructible** stack of objects | **GB normal form** (finite per ℓ(w)-slice) + **jet order** + **surreal** grading | 🟢 | The finiteness KS *assumes*, QOU *derives*. See §5. |
| Motivic **Thom–Sebastiani** (KS Thm 6, cited) | Wenzl **disjoint multiplicativity** tr_M(K⊔K′)=tr_M(K)·tr_M(K′) | 🟢 | A *rigorous* reusable: the categorical parent of an identity already in QOU production (Phase 5l). |
| Stab(C) is a complex manifold (Theorem 1) | — (QOU has **no** stability moduli; it pins one point) | 🔴 | Not a QOU axiom; the apparatus QOU declines (Q6). |
| §1.5 hyperkähler M, "quaternionic Fukaya", 4d black holes | — | 🔴 | KS's own speculations; do not import. |

---

## 4. The multiplicative WCF **is** the archimedean wall (Q8)

The owner's instinct is exactly right, and KS themselves make it explicit:

1. **The walls are archimedean.** A wall of marginal stability is the locus where
   two charges become **phase-aligned**: arg Z(γ₁) = arg Z(γ₂) in ℂ. That is a
   real-analytic condition on the **archimedean** target ℂ of the central charge.
   Crossing it is where Ω(γ) jumps and all the analytic difficulty lives.

2. **KS build the formula on the *non-archimedean* side.** In §1.5 point 1 they
   realize the symplectomorphism collection AV as a **rigid analytic space X^an
   over a non-archimedean field**, with the actual **complex (archimedean)
   symplectic manifold M only conjectured** ("String Theory suggests there exists
   an actual complex symplectic manifold M…"). The hard archimedean object (later
   the Gaiotto–Moore–Neitzke hyperkähler metric) is *speculation* in this paper.

3. **QOU's avoidance strategy is the §7c discipline.** Everything categorical
   stays over a generic commutative ring `{R : Type*}` / ℚ(q); the **single**
   archimedean step is the functor τ at the **fixed, calibrated** q₀. Because q₀
   never moves, **no wall is ever crossed** — there is no Ω(γ) to jump. The
   "archimedean wall" the codebase already names (generic-R vs ℝ, the
   `Real.sqrt`/`0<q` boundary) is *the same wall* as KS's marginal-stability
   locus: the cut between the algebraic/formal/non-archimedean world and the
   analytic/archimedean one.

**Net:** the WCF is a tool for *transporting* invariants *across* the wall. QOU's
design goal is to *never need* such transport, by pinning the realization. So the
WCF is not something QOU should adopt — it is precisely the thing QOU's
architecture is built to make unnecessary. (Where a *bounded* deformation of q₀
is wanted — e.g. the complex-q₀ lift, cheat-sheet §5 / `2026-05-24-q-zero-reality-audit`
— the relevant control is the bar/Hermitian involution split, **not** a WCF.)

### Kashaev sub-part (trivial knot)

`QOU.Kashaev.VolumeConjecture` already encodes `tr_M ~ exp(Vol)` and the
"Vol=0 ⇒ sub-exponential ⇒ torus knots need a different chain" logic
(cheat-sheet §5, electroweak T(2,k) route). The **refined** home of this is now in
the corpus: **Garoufalidis–Zagier `2111.06645`** introduce a matrix invariant
Φ_α(h) whose **(σ₀, σ₁) entry is the Kashaev invariant in the Habiro ring**, with
**σ₀ = trivial representation** (the unknot/trivial-knot column you mention) and
σ₁ = geometric representation. This is the rigorous, all-orders, quantum-modular
upgrade of Kashaev's volume conjecture and it lands directly on QOU's Habiro-ring
machinery (Φ_q / Li₂^q). **Recommended:** when QOU next touches the volume-
conjecture bridge, cite GZ `2111.06645` for the Habiro-ring / trivial-rep column
structure rather than the bare 1995 Kashaev conjecture.

---

## 5. ind-constructible vs GB-filtration + jet + surreal (Q4)

KS: *"All A∞-categories in this paper will be ind-constructible. This roughly
means that their spaces of objects are countable inductive limits of constructible
sets."* This is **not laziness** — it is the **minimal tameness hypothesis** that
lets them put a **motivic measure** on the moduli stack of objects (constructible
sets → motivic integration → motivic Hall algebra → Serre-polynomial q-analog). For
an *arbitrary* 3CY A∞-category there is no other way to make "the number of
objects of class γ" well-defined.

QOU does **not** need the hypothesis, for the reason the owner names:

- The QOU "objects" are **braid words / Hecke elements**. The **Gröbner–Shirshov
  normal form** (the very `0409565` unital-GB / simpler-PBW paper in `uploads/`)
  gives a **canonical, finite** set of normal forms **per Coxeter-length slice
  ℓ(w)** — so each slice is a *finite scheme*, **constructible by theorem**, not by
  assumption. (Chain steps 7–8: "E_∞ = ⊕_λ M_{d_λ}; collapse at E_2 ⇒
  finite-slice.")
- The **jet order** organizes the slices into the tower, and the **surreal
  exponential-logarithmic hierarchy** (Kuhlmann–Matusinski `1203.4538`, in
  `uploads/`) gives the jet grading a rigorous value-group home — so the q→1
  classical limit is a controlled Hahn/surreal expansion, **not** an ad-hoc
  analytic limit.

So QOU replaces "assume ind-constructibility to get a measure on a wild moduli
stack" with "the GB-NF makes every slice finite, and the jet/surreal grading
controls the tower." This is a **genuine structural advantage**, available only
because QOU committed to the specific Hecke/braid category. It is not that KS were
lazy; it is that QOU bought finiteness with specificity.

---

## 6. Why not go straight to Wedderburn? (Q9 — the methodological crux)

This is the sharpest question and it has a clean answer.

The "exp()-and-algebra" crowd (KS, the Hall-algebra / cluster / DT school) works
with objects like:

- the **quantum torus** automorphism `exp(Ham-vector-field of the dilogarithm)`,
- the **pro-nilpotent group GV** of such symplectomorphisms,
- the **motivic Hall algebra** (a bialgebra over a stack).

**None of these is a finite-dimensional semisimple algebra.** Wedderburn's
theorem (A ≅ ⊕_λ M_{d_λ}) applies to finite-dimensional semisimple algebras only.
For an arbitrary 3CY category there is **no semisimple finite-dimensional algebra
in sight**, so there is nothing to Wedderburn-decompose; the pro-nilpotent /
exp() world is the *only* structure available, and that is why they stay there.

**QOU's bet is to manufacture semisimplicity.** By routing the physics through the
**Iwahori–Hecke algebra H_n(q)**, which is **split semisimple whenever q is not a
root of unity** (q₀ ≈ 1.1097 is generic, real, > 1 ⇒ semisimple), QOU *earns* the
Wedderburn decomposition ⊕_{λ⊢n} M_{d_λ}(ℚ(q)). Then the exp() objects — the
volume-conjecture `tr_M ~ exp(Vol)`, the Habiro element, the q-dilogarithm —
get evaluated **block-by-block over partitions λ**, which is the entire QOU
compute engine (`y_lambda_wenzl_bridge`, `chi_lambda_braid`, the per-λ q-Reeb
phase). So the answer to *"why don't they just go to partitions"* is: **they
can't (no semisimple algebra); QOU can (it engineered one), and that is QOU's
defining methodological move.**

Caveat (heeding "careful"): this advantage is **conditional on genericity of q**.
At a root of unity H_n(q) is *not* semisimple and the partition picture degenerates
(Wenzl/Gyoja–Uno) — exactly the regime where KS-style non-semisimple machinery
would re-assert itself. QOU stays generic precisely to keep Wedderburn.

---

## 7. KLR (Q10)

Chain of relations:

```
KS wall-crossing / motivic DT  →  Cohomological Hall Algebra (KS follow-up)
   →  KLR / quiver-Hecke algebra  (Schiffmann–Vasserot, Varagnolo–Vasserot)
   →  canonical / crystal basis  (Lusztig, Kashiwara)
```

The COHA of a (symmetric) quiver with potential is a shuffle-algebra incarnation
of the same data the KLR algebra categorifies (the negative half U_q(n⁻)). So
KS-DT and KLR are two faces of "categorify the (quantum) Hall/Grothendieck
structure."

**QOU already lives on the KLR/crystal side** and uses it as *authoring
shortcuts* (CLAUDE.md §7b): type-B folding for CPT/chirality, KL-basis
decategorification for the classical (Pauli/Bose) limit, Demazure sub-crystals for
resonances. Compute infra exists (`klr_canonical_basis_filter.py`,
`crystal_basis.py`, the `qbeta_chain4_kashiwara_crystal_scaffold` family), and the
combinatorial substrate is the Lusztig-cone / canonical-basis material of Marsh
`0008040` (in `uploads/`). What QOU **omits** is the WCF dynamics sitting on top of
the KLR layer — consistent with §4 (avoid the wall) and with the
`2026-05-30-klr-dialog-assessment.md` verdict that a KLR layer does not, by itself,
shorten QOU's existing Diamond-Lemma / Wenzl proofs.

---

## 8. Recommendations (small, concrete)

1. **Add the four references** to `content/schema/references.ts`:
   `kontsevich-soibelman-2008` (the paper; arXiv-only, no journal DOI),
   `garoufalidis-zagier-2024` (SIGMA, DOI `10.3842/SIGMA.2024.055`),
   `franecki-kapranov` (microlocal Euler/constructible), `webster-williamson-2010`
   (geometry of Markov traces). They are now in the corpus and future blocks will
   cite them. *(Done in the accompanying commit; verify `validate-refs` is green.)*
2. **Optional content block (exposition only):** a `remark` with
   `interprets: "prop:pre-archimedean-derivation-chain"` (or the archimedean-
   functor block) recording the §3 dictionary — **as interpretation, never as a
   theorem**. This is the "pretty story" the owner asks about; it is worth having
   for readers coming from the DT/wall-crossing world, and it costs no rigor.
3. **One genuinely reusable lemma:** when the Wenzl disjoint-multiplicativity
   identity (Phase 5l, `tr_M(K⊔K′)=tr_M(K)tr_M(K′)`) is next written up, cite the
   motivic **Thom–Sebastiani** factorization as its categorical parent — a
   *rigorous, externally-proved* result, unlike the KS sketches.
4. **Do not** open any work to "import the WCF" or "prove Stab(C) structure" —
   that is the wall QOU is architected to avoid (§4) and the deformation apparatus
   QOU declines (§6). 
5. **Citation hygiene (the owner's warning):** anywhere a KS statement is
   referenced in QOU content, mark it as *conjectural/sketch-level on the source
   side* unless it is one of the externally-rigorous cited lemmas. Treat KS
   "trivial" assertions as open until independently checked.

---

## 9. One-line summary

KS 0811.2435 and QOU are **cousins under "category + numerical realization +
trace invariant"**: KS varies the realization across **archimedean walls** and
pays with non-rigorous sketches over a wild moduli stack; QOU **pins** the
realization at a single calibrated q₀, engineers a **semisimple Hecke algebra** so
it can go **straight to Wedderburn/partitions**, and earns finiteness from the
**GB normal form** instead of assuming **ind-constructibility**. Borrow KS's
**dictionary** (special-Lagrangian ↔ real-valued central/trace observable; Euler
form ↔ Frobenius pairing) and the one **cited** Thom–Sebastiani lemma; **avoid**
its wall-crossing machinery and its sketch-level theorems.
