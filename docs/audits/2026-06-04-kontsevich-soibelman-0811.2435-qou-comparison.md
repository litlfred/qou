# Kontsevich–Soibelman 0811.2435 vs QOU — dictionary, what to borrow, what to avoid

**Date:** 2026-06-04
**Source paper:** Maxim Kontsevich, Yan Soibelman, *Stability structures, motivic
Donaldson–Thomas invariants and cluster transformations*, arXiv:0811.2435v1
(148 pp, 16 Nov 2008). PDF now in the corpus at
[`uploads/0811.2435v1.pdf`](../../uploads/0811.2435v1.pdf) (added by the owner in
[commit `1372394e`](https://github.com/litlfred/qou/commit/1372394e843b23e18fa2cc15d88f2a8fadfde75c)).
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

1. **References (status, this PR).** `franecki-kapranov-1999` and
   `webster-williamson-2014-markov` **already exist** (added 2026-05-19 from a prior
   uploads gap audit), so this PR adds only the two genuinely-missing keys:
   **`kontsevich-soibelman-2008`** (arXiv-only, no journal DOI) and
   **`garoufalidis-zagier-2024`** (SIGMA, DOI `10.3842/SIGMA.2024.055`).
   `validate-refs` reports both as benign "not yet cited" INFO (the 4 pre-existing
   `[prNNNN]` errors are an unrelated Q_β-Lean key bug, out of scope).
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
6. **Flagged for separate triage (not fixed here):** `halverson-1998-markov-weights`
   points at arXiv `math/9806163`, whose PDF is authored **R.C. Orellana** — but the
   entry names *Halverson* and carries a *different* DOI (`10.1006/jabr.1998.7437`)
   used by 3 `.lean` files. Likely a two-works conflation (Halverson J. Algebra vs
   Orellana arXiv); resolve via a `wenzl1988`-style wrong-work-split triage, **not** a
   drive-by author edit (the blast radius touches Lean `-- Ref:` lines).

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

---

## 10. Full result-by-result survey (all 47 numbered results)

The paper has **47 numbered results** (10 Theorems, 17 Propositions, 3 Lemmas,
4 Corollaries, 12+ Conjectures). Surveyed one-by-one below, grouped by theme.

**Columns.** *Side* = PRE (pre-archimedean: formal / motivic / Γ-graded, no ℂ- or
ℝ-valued realization) vs ARCH (lives on the central charge Z : Γ → ℂ, i.e. the
wall side). *Lean* = can it realistically be Lean-backed **in QOU/Mathlib today**:
✓ plain algebra (feasible), △ hard / needs missing Mathlib (Bridgeland defm,
formal NC symplectic, t-structures), ✗ infeasible (motivic integration / Hall
algebra over a stack, or a KS *sketch/conjecture*). *Verdict* under the owner's
**Lean-gate** ("KS allowed only if backed by Lean"):
🟩 **Admit** (relevant + Lean-backable) · 🟦 **Story-only** (dictionary/exposition,
not Lean content) · 🟥 **Exclude** (archimedean wall, motivic-infeasible, or
KS-sketch/conjecture).

### A. Stability moduli & the wall-crossing formula — the archimedean apparatus QOU declines

| KS (p) | Statement | Side | QOU relevance | Lean | V |
|---|---|---|---|---|---|
| **Thm 1** (9) | `Stab(C) → Hom(Γ,ℂ)` is a local homeo (Bridgeland defm) | ARCH | – moduli QOU pins to one point | △ | 🟥 |
| **Thm 2** (23) | bijection `StabQ(g) ≅ Stab^Q(g)` | ARCH | – | △ | 🟥 |
| **Prop 1** (26) | the stability topology is Hausdorff | ARCH | – | ✓ | 🟥 |
| **Prop 2** (26) | `{Q≥0} ∩ Z⁻¹(l)` is a convex cone (Support Property) | ARCH | ○ discreteness QOU gets free at fixed q₀ | ✓ | 🟦 |
| **Thm 3** (29) | unique continuous section φ — *"sketch … details to reader"* | ARCH | – | ✗ | 🟥 |
| **Prop 3** (30) | countable wall set on a generic path | ARCH | – | △ | 🟥 |
| **Thm 4** (31) | monodromy around a short loop = id — **this is the WCF**; *"sketch"* | ARCH | – **the wall QOU avoids** | ✗ | 🟥 |
| **Prop 4** (31) | sections ↔ functions with trivial wall monodromy | ARCH | – | △ | 🟥 |
| **Prop 8** (59) | `C(k')` carries a locally finite (Bridgeland) stability structure | ARCH | – | △ | 🟥 |

### B. Graded Lie algebra & finiteness (pre-arch, but in service of the WCF)

| KS (p) | Statement | Side | QOU relevance | Lean | V |
|---|---|---|---|---|---|
| **Lemma 1** (28) | the order ideal `(γ',t') ≤ (γ,t)` is a finite union | PRE | ○ finiteness | ✓ | 🟦 |
| **Cor 1** (28) | `a_t(γ)` is a **finite Lie expression** of the atoms `a_0(γ_α)` | PRE | ○ finite-generation ↔ **GB-NF (step 7)** | ✓ | 🟦 |
| **Lemma 2** (34) | `G_C` preserves the completion of `N` (torus action) | PRE | ○ quantum-torus action ↔ Habiro | △ | 🟦 |

### C. Dilogarithm & quantum-dilog factorization

| KS (p) | Statement | Side | QOU relevance | Lean | V |
|---|---|---|---|---|---|
| **Conj 1** (13) | pentagon reordering of `T_{1,0}·T_{0,k}` | PRE | ○ pentagon ↔ QOU pentagon/Habiro (`q-dilogarithm.md`) | ✓ | 🟦 |
| **Conj 3** (41) | `K_n = Σ Ω…` dilog expansion | ARCH | – conjecture | ✗ | 🟥 |
| **Prop 5** (42) | `K_n = I_n` for phase-ordered args (dilog integral) | ARCH | ○ archimedean form of Φ_q / Li₂^q | △ | 🟦 |
| **Prop 16** (138) | `E_Q = E_{Q1} E_{Q2}` (quantum-dilog factorization for quivers) | PRE | ⭐ **Habiro-element factorization** spirit (Q_β Habiro) | ✓ | 🟩 |
| **Conj 11** (127) | `χ_Φ(F_l) = ∏(1−t^n)^{nΩ(n)}` (DT product formula) | PRE | ○ product-form ↔ torus-knot patterns | △ | 🟥 |

### D. Minimal model / normal form (pre-arch — a *parallel* QOU already has rigorously)

| KS (p) | Statement | Side | QOU relevance | Lean | V |
|---|---|---|---|---|---|
| **Prop 7** (54) | potential splits `W_E = W^min_E ⊕ (quadratic)` | PRE | ○ minimal model ↔ **GB-NF** | △ | 🟦 |
| **Thm 5** (55) | odd-symplectic formal manifold ≅ minimal × trivial (Darboux) | PRE | ○ normal-form ↔ **GB-NF (steps 7–8)** | △ | 🟦 |
| **Cor 2** (55) | `W^min_E` is independent of the minimal-model choice | PRE | ○ canonicity ↔ **GB-NF uniqueness** | △ | 🟦 |

### E. ind-constructible / motivic foundations (the layer QOU *replaces*)

| KS (p) | Statement | Side | QOU relevance | Lean | V |
|---|---|---|---|---|---|
| **Prop 6** (50) | `C(k)` is an A∞-category; ind-constructible equivalences lift | PRE | ○ the setup QOU replaces with GB-NF | ✗ | 🟦 |
| **Thm 6** (68) | **motivic Thom–Sebastiani** `(1−MF(f⊕g)) = (1−MF f)·(1−MF g)` (*cited* [15]) | PRE | ⭐ categorical **parent of Wenzl disjoint-multiplicativity** | ✗ motivic / ✓ via Wenzl | 🟩 |
| **Conj 4** (69) | integral identity for the motivic Milnor fiber | PRE | – conjecture | ✗ | 🟥 |
| **Prop 9** (70) | `RΓc` isomorphism for the Milnor fiber | PRE | – | ✗ | 🟥 |

### F. Motivic Hall algebra → quantum torus (the structural core)

| KS (p) | Statement | Side | QOU relevance | Lean | V |
|---|---|---|---|---|---|
| **Prop 10** (85) | `H(C)` is an associative algebra | PRE | ○ Hall = categorified (QOU: the Hecke algebra itself) | ✗ | 🟦 |
| **Prop 11** (88) | `A^Hall_V` satisfy the **Factorization Property** | PRE | ⭐ **multiplicativity** spirit | △ | 🟩 |
| **Cor 3** (89) | `(A^Hall_V)` = symmetric stability data on `H(C)` | PRE | ○ | △ | 🟦 |
| **Prop 12** (89) | ring map `H(C) → H_Toën(C)` (derived Hall algebra) | PRE | ○ homomorphism spirit | ✗ | 🟦 |
| **Thm 7** (95) | (cond.) `A^mot_V` satisfy the Factorization Property | PRE | ⭐ multiplicativity (conditional/motivic) | ✗ | 🟦 |
| **Thm 8** (96) | **Φ : H(C) → R_Γ is a homomorphism of Γ-graded ℚ-algebras** | PRE | ⭐⭐ **TOP**: "the invariant is an *algebra map*" ↔ tr_M ⊗-multiplicativity | ✓ `AlgHom` | 🟩 |
| **Prop 13** (118) | the generating series `A(t)` | PRE | ○ | △ | 🟦 |
| **Prop 14** (120) | `A(k) ≅ B-mod` (reconstruction as reps of a topological algebra) | PRE | ○ **Tannakian** `(C,A,τ)` flavor | ✗ | 🟦 |
| **Prop 15** (121) | `A(t)` for the heart of a t-structure | PRE | – | △ | 🟥 |
| **Lemma 3** (123) | `M` is cyclic iff `M_ss` is cyclic | PRE | – | ✓ | 🟥 |

### G. Integrality / deformation-invariance (BPS counting — all conjectural)

| KS (p) | Statement | Side | QOU relevance | Lean | V |
|---|---|---|---|---|---|
| **Conj 2** (41) | `M(f_α)=N(f_α)` ⟹ WCF | PRE | – conjecture | ✗ | 🟥 |
| **Conj 5** (110) | `A_{V,q}`-conjugation preserves a subring | PRE | – conjecture | △ | 🟥 |
| **Conj** (111) | explicit quasi-classical-limit formula | PRE | – conjecture | ✗ | 🟥 |
| **Conj 6** (111) | `Ω(γ) ∈ ℤ` (integrality of BPS counts) | — | ○ integrality (QOU gets it structurally via ℚ(q)) | △ | 🟥 |
| **Conj 7** (112) | `Ω(γ)` is deformation-invariant | — | – conjecture | ✗ | 🟥 |
| **Conj 8** (115) | `A^mot`-conjugation = automorphism of the motivic q-torus | PRE | – conjecture | ✗ | 🟥 |
| **Conj 9** (117) | `F_l(t)` lies in the completion | PRE | – conjecture | △ | 🟥 |
| **Conj 10** (125) | no orientation data ⟹ stability data on Poisson `g_Γ` | PRE | – conjecture | ✗ | 🟥 |

### H. Cluster collections & mutations (the WCF rendered as algebra)

| KS (p) | Statement | Side | QOU relevance | Lean | V |
|---|---|---|---|---|---|
| **Thm 9** (129) | 3CY generated by `{E_i}` with `Ext⁰(E_i,E_i)=k·id`, `Ext⁰(E_i,E_j)=0` | PRE | ○ finite generators ↔ **Bring χ=−6 / 6 GS-NF operators (step 4)** | △ | 🟦 |
| **Thm 10** (134) | mutations can proceed indefinitely off a countable hypersurface set | PRE | – mutation = WCF dynamics | ✗ | 🟥 |
| **Conj 12** (136) | two bifunctors define isomorphic orientation data | PRE | – conjecture | ✗ | 🟥 |
| **Prop 17** (141) | `Ad⁻¹ ∘ Φ_E ∘ Ad = Φ_{E'}` (mutation = conjugation) | PRE | – mutation dynamics | △ | 🟥 |
| **Cor 4** (141) | the cluster-transformation map `C_{Q,0}` | PRE | – | △ | 🟥 |

### Tally

| Verdict | Count | What it is |
|---|---:|---|
| 🟩 **Admit** (Lean-backable + relevant) | **4** | Thm 8 (algebra-homomorphism), Thm 6 (Thom–Sebastiani, *via* Wenzl), Prop 11 (Factorization), Prop 16 (q-dilog factorization) |
| 🟦 **Story-only** | ~16 | dictionary / parallels QOU already has (minimal-model ↔ GB-NF; reconstruction ↔ Tannakian; generators ↔ Bring; dilog) |
| 🟥 **Exclude** | ~27 | the WCF/stability-moduli archimedean apparatus + ~12 conjectures + motivic-infeasible computations |

**Headline:** the **entire wall-crossing / stability-moduli half of the paper is
🟥** (it is the archimedean wall, and it is the half that is sketch-proved), and
**~12 conjectures are 🟥 by the Lean-gate alone**. The Lean-backable, genuinely-
relevant residue is **four results, all expressing one idea**: *the invariant is a
**multiplicative / algebra-homomorphism** object* (Thm 8, Thm 6/7, Prop 11, Prop 16).

---

## 11. The spirit of KS *before the archimedean wall* — can it simplify? (the owner's real question)

### 11.1 The pre-archimedean KS spirit, distilled

Strip away the central charge `Z` (the wall) and the four 🟩 results say one thing,
in four costumes:

> **Package the invariant as a homomorphism from a charge-graded categorified
> algebra into a (quantum) torus, so that disjoint union ↦ product
> (Factorization) — *before* any numerical realization.**

Supporting pre-arch spirit: **finite generation** by atoms (Cor 1), a **canonical
minimal/normal form** (Thm 5, Prop 7, Cor 2), and **reconstruction** of the
category from a fiber-functor-like datum (Prop 14).

### 11.2 QOU already embodies this spirit (convergent design)

| KS pre-arch principle | QOU step that already realizes it | Status in QOU |
|---|---|---|
| charge-graded categorified algebra | Wedderburn `H_n(q) ≅ ⊕_{λ⊢n} M_{d_λ}` graded by partitions (step 5) | 🟢 derived (Wenzl) |
| invariant = homomorphism / character | `tr_M` Markov trace; `tr_M(K⊔K')=tr_M(K)·tr_M(K')` Wenzl disjoint-mult (step 6, Phase 5l) | 🟢 derived |
| Factorization (disjoint ↦ product) | Phase 5l `ρ_Z^constit = tr_M³(𝓑_p)`; Phase 5c.1 interface factorization | 🟢 / ✅ sorry-free |
| finite generation by atoms | GB normal form, finite per `ℓ(w)`-slice (step 7) | 🟢 derived |
| canonical minimal/normal form | GB-NF / canonical `T_w` (steps 7, 10) | 🟢 derived |
| reconstruction from a fiber functor | Tannakian tuple `(𝐂, A, τ)`; `archimedean-functor-uniqueness` | 🟢 derived |

The map is essentially **onto**: every load-bearing pre-archimedean KS principle is
already a step of QOU's chain — but realized over the *tame*, *semisimple* Hecke
category instead of a wild 3CY one, and **Lean-tracked**.

### 11.3 Verdict: net simplification ≈ **no** — with one marginal exception

Honest answer (heeding "careful"):

1. **The spirit is already present**, so there is little to import — QOU and KS
   *converged* on "graded + factorization + homomorphism." KS does not hand QOU a
   shorter chain; it hands QOU a more general (and looser) version of the chain it
   already has.
2. **KS's concrete tools are heavier and fail the Lean-gate.** The motivic Hall
   algebra, ind-constructibility, motivic Milnor fiber, and the quantum/Poisson
   torus over a stack have **no Mathlib support** and would *add* un-Lean-backable
   weight. Adopting them **complicates**, not simplifies.
3. **The one transferable principle QOU already proves**, and proves *more cheaply*
   (Wenzl §1.7 is a one-page computation, already partly sorry-free), so even the
   🟩 results are not a simplification — at most a **re-framing**.

### 11.4 The single marginal Lean candidate (clearly labeled marginal)

The KS Factorization Property (Prop 11 / Thm 7) and the Hall→torus homomorphism
(Thm 8) suggest stating QOU's disjoint-multiplicativity **structurally** rather
than per-λ:

> **Candidate lemma (optional cleanup, not a derivation change).** Define `tr_M` as
> a **character of the disjoint-union (⊗) monoid of links** — i.e. a monoid
> homomorphism `(Links, ⊔) → (ℚ(q), ·)` — and derive `tr_M(K⊔K')=tr_M(K)·tr_M(K')`
> once, instead of re-deriving it per partition. Lean home: a `MonoidHom`
> (or `AlgHom` on the disjoint-union algebra) over `ℚ(q)`; feasible today.

**Precision (do not over-claim — this is exactly the kind of "trivial" assertion to
be careful with):** a trace is **not** an algebra homomorphism for the *internal*
product (`tr(ab) ≠ tr(a)tr(b)`; only `tr(ab)=tr(ba)`). The KS-style multiplicativity
is for the **monoidal / disjoint-union** structure `⊔ = ⊗`, where `tr_M` *is*
multiplicative. KS Theorem 8's "homomorphism" is the **counting/integration map**
`H(C) → R_Γ`, not a trace — the QOU avatar of *that* is the assignment
`braid ↦ tr_M(braid) ê_{class}` landing in the q-character ring, and its
multiplicativity is Wenzl disjoint-mult. Conflating the two would be a real error.

This candidate buys **≈ nothing in derivation length** (Wenzl is already short); its
only value is making the "factorization is structural, not computational" fact
explicit in Lean and giving DT-literate readers a familiar handle. **Low priority.**

### 11.5 Where the spirit *does* point — the one open frontier (step 9b binding / Δ_λ)

§11.3 is about the *solved* steps 1–8. There is exactly one place where the KS
pre-archimedean spirit is genuinely useful, and it is the **only open step**: the
per-isotope binding density **Δ_λ** (step 9b, the Track-A blocker).

**The KS method, in one line, is: *keep the per-charge graded structure; realize it
numerically only at the very end.*** That is *literally* the QOU binding lever the
cheat-sheet already identifies (§9.2):

> the per-λ q-Reeb phase `θ_λ = arccos(χ^λ/d_λ)` is **derived at step 2** (Yekutieli
> boundary holonomy) but **collapsed by the scalar trace** `tr_M = Σ_λ y_λ χ^λ`.
> *Retaining* `θ_λ` per-block instead of collapsing it is the binding lever.

So the KS spirit is a **conceptual reinforcement** of the productive direction
(GAP-A-3 / GAP-A-4, "retain per-λ") over the collapse-to-scalar dead ends — the same
verdict QOU reached empirically (the A=3 mirror pair closes to 2 % with no fit once
`θ_λ` is kept; volume-difference/Lobachevsky observables were refuted).

It also **names the structural object to chase.** KS's graded Lie algebra `g_Γ`
carries a bracket `[•,•]`; QOU's analog is the Frobenius/Hecke commutator, and the
cheat-sheet flags **`[F,F] = Hecke-quadratic` as "identified-but-unused"** — the
heaviest unused lever in the A≥3 campaign. The KS spirit suggests binding may be a
**bracket in the graded structure**, not a per-block scalar.

**This is a research *direction*, not a result — and it is hard-gated:**

| | Allowed (KS spirit, in bounds) | Forbidden (Δ_λ gate) |
|---|---|---|
| form | a **zero-parameter structural derivation**: `[F,F]` (or `θ_λ`) *forces* Δ_λ with no free knob — the GAP-A-3/4 categorical class | a **7th fitted ansatz**: tune a constant so the bracket matches AME |
| Lean | **required** before it enters QOU content (the owner's "Lean only" gate) | n/a — never enters |

The gate already retired six fits; KS gives the *spirit* (where to look), **not** a
shortcut around it. If `[F,F]` yields Δ_λ with zero free parameters and a Lean proof,
that would be a real simplification of the open step — but it must be *derived*, not
*fitted*, and *formalized*, not asserted.

### 11.6 What the spirit explicitly does *not* license (guardrails)

- **Do not** import the WCF / cluster mutation (Thm 4, 10; Prop 17; Cor 4) — that
  *is* the archimedean wall (§4), and it is sketch-proved.
- **Do not** turn §11.5 into a *fitted* `Δ_λ` closure. The `[F,F]` lever is admissible
  **only** as a zero-parameter, Lean-backed derivation; a tuned constant is the 7th
  ansatz the **Δ_λ gate** forbids.
- **Do not** state any KS result as a QOU proposition/Lean theorem on KS's
  authority — ~12 are conjectures and Thms 3/4 are sketches. Re-prove under §3b or
  cite only the externally-rigorous parents (Thm 6's Denef–Loeser source;
  Bridgeland behind Thm 1).

### 11.7 Bottom line on "can it simplify"

- **Solved steps 1–8: no net simplification.** QOU's chain already *is* the
  Lean-tracked, semisimple, tame realization of the KS pre-archimedean spirit (§11.2);
  KS's concrete tools are heavier and fail the Lean-gate (§11.3).
- **Open step 9b: the spirit is useful** — it reinforces the "retain per-λ `θ_λ`"
  binding lever and names the `[F,F]` graded bracket as the structural object to
  chase, strictly as a zero-parameter, Lean-backed derivation (§11.5).
- **Concrete deliverables:** (i) the **dictionary** (exposition, §3); (ii) the
  **citations** (`kontsevich-soibelman-2008`, `garoufalidis-zagier-2024` added here;
  Franecki–Kapranov / Webster–Williamson already present); (iii) **one optional**
  `MonoidHom` cleanup of Wenzl disjoint-multiplicativity (§11.4). The wall-crossing
  payload — the famous, beautiful half of KS — stays **outside** QOU by design.

---

## 12. "What would Lean-formalizing *all* of KS give QOU?" (owner follow-up)

Layered answer.

### 12.1 For QOU's predictions — nothing

The substrate→observable chain (steps 1–11) is self-contained and never invokes KS.
No KS theorem feeds `m_p`, `m_n`, `B(K)`, `Q_β`, or any L1/L2 dashboard number;
formalizing KS would not move a single digit. (By contrast, discharging QOU's *own*
`sorry`s — Markov-trace uniqueness, the SkewSYT jet `sorry`s — *would* harden the
chain. Those are QOU gaps, not KS's.)

### 12.2 For QOU's status — remark → proved embedding

Under the Lean-gate, KS is today a **remark** (§3b: no logical claim without Lean). If
the KS *specialization to QOU's setting* were Lean-backed, the §3 dictionary becomes a
**theorem**:

> a functor/instance exhibiting QOU's `(𝐂, τ, tr_M)` at fixed q₀ as the rigid
> q₀-evaluation of a KS stability structure `(𝐂, Z, Ω)` — with `Z` the τ-period and
> `Ω` the Wedderburn multiplicities.

Payoff: (a) **structural legitimacy** — QOU becomes *an instance* of a recognized
framework, not a parallel invention; (b) a **rigorous bridge** to BPS / Gaiotto–Moore–
Neitzke / cluster-algebra results; (c) **license to cite** KS-proved lemmas as QOU
lemmas. This is "the pretty story becomes a theorem."

### 12.3 But "all their proofs" is the wrong, infeasible target

- **No Mathlib foundation.** Motivic integration (Grothendieck ring of varieties +
  measures), the motivic Milnor fiber, ind-constructible stacks, A∞-categories,
  Bridgeland stability — none are in Mathlib. Each is a multi-year formalization on its
  own; together they are among the hardest unformalized areas of mathematics.
- **You cannot formalize a sketch.** Thm 3/4 are explicitly "details to the reader";
  ~12 of the 47 results are conjectures (§10). To "do their proofs in Lean" you must
  first *complete the mathematics* — open research, not formalization. Parts of the KS
  program were tightened only in later papers / remain folklore.
- **The usable half collapses to one QOU lemma.** The Lean-admissible, QOU-relevant
  residue (§10: 4 results) all say *"the invariant is multiplicative."* In QOU's
  specific Hecke setting that **is** Wenzl disjoint-multiplicativity (Phase 5l) —
  already nearly sorry-free. So "KS in Lean," scoped to what QOU can use, = finishing
  **one small QOU lemma** (§11.4). KS is not needed for it.

### 12.4 Net

Enormous cost; ~zero prediction benefit; the single structural payoff (remark →
embedding) needs only the **specialization**, not the 148-page program. Disciplined
plan: **keep KS as remark + dictionary; Lean-back only the QOU-side specialization.**
The Lean-gate already implies this — it is *why* KS is, correctly, a remark today.
