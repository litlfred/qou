---
name: one-voice-style-guide
description: Author voice profile and narrative style guide. Reference when authoring or editing prose. Pairs with `one-voice-audit` (mechanical sweep for status leaks, emoji, and Unicode crashes).
roles: [reader, collaborator]
triggers:
  - "one voice style"
  - "voice profile"
  - "author voice"
  - "narrative style"
  - "before committing narrative"
---

# One-Voice Style Guide — Author Voice Profile

> **See also:** `one-voice-audit` is the mechanical sweep (greps for
> ✅/TODO/first-person work tone). This file is the *style profile*
> agents follow when *writing* prose; the audit is what runs *after*.

Reference this skill when authoring or editing narrative content
(.md files).
It ensures the paper speaks with a single, consistent voice across
all chapters, sections, and the running SU(2) example.

## Author Voice Profile

Frederick Carl Leitner writes with **crystalline precision in the
service of clarity**. The voice is:

- **Authoritative and precise**: No hedging, no editorializing, no
  personal asides. Every sentence carries mathematical weight.
- **Collaborative**: "We" for joint reasoning with the reader, never
  "I". The reader discovers alongside the author.
- **Object-focused**: Prioritizes what structures *do* over what they
  *are*. The paper's thesis — "we ask what its mechanics do" — is
  embedded in the prose itself.
- **Economical**: No filler, no rhetoric. If a result is striking,
  the mathematics shows it; the prose does not comment on it.

### Sentence patterns

- **"Not assumed; derived"**: "The symmetry group is not assumed; it
  emerges via Tannaka–Krein reconstruction." Distinguishes derivation
  from stipulation.
- **"Forced by"**: Structures are "forced by the Frobenius–Hopf
  structure, not by assumption."
- **"Equivalent viewpoints"**: "not competing descriptions but
  equivalent viewpoints, exchanged by..."
- **"Precisely" language**: "makes the observation from paragraph two
  precise" — exactness is paramount.
- **Never begins a sentence with a math symbol**: always "The operator
  $X$", not "$X$ is..."

### Pacing

Layered introduction, repeated at every scale (paragraph, section,
chapter):

1. Accessible observation or motivation
2. Precise mathematical statement
3. Formal definition or theorem
4. Consequence or example (SU(2) running example)

## Paper-Level Voice Rules

| Rule | Standard | Violation example |
|------|----------|-------------------|
| **Person** | First-person plural ("we") | "the author shows", "one can see", "it is shown" |
| **Referent** | "this paper" | "this book", "this work", "the present article" |
| **Tense** | Present ("we define", "the theorem states") | Past ("we defined", "the theorem stated") |
| **Tone** | Direct, declarative, no editorializing | "surprisingly", "remarkably", "it is perhaps the most", "interestingly" |
| **Math voice** | Active ("we construct $X$") for new definitions; passive ("$X$ is called") for established terms | Mixing active/passive for the same concept |
| **Reader address** | Never address the reader directly | "you can verify", "the reader will note" |

## Title Conventions (chapter / section / subsection)

Titles are the table-of-contents face of the paper's story. Three
rules, enforced by `content/pipeline/qa-section-title-audit.ts` (machine
pass) plus an agent coherence pass:

1. **Short and concise.** A title is a noun phrase naming the section's
   *one* governing idea — not a sentence, and not a comma-list of every
   concept in the section. Three-plus comma-joined concepts
   ("A, B, C, and D") and over-long titles are flagged.

2. **Ownership hierarchy.** The **paper** is responsible for its
   **chapter** titles, each **chapter** for its **section** titles,
   each **section** for its **subsection** titles. A title is judged
   coherent *read against its responsible parent*: it must make sense
   in that container without outside context, and distinguish itself
   from its sibling sections.

3. **Title from the story, not the label.** Read the section's content
   blocks (the intro block states the arc) and title it by what the
   section *does* in the chapter — never by mechanically de-slugging
   its `label`. Bad (label-derived): "Confinement operator selection :
   vs". Good (story-derived): "Which confinement constraints survive".

**Never ship an auto-split artifact title** — a trailing ` : <tag>`
(` : vs`, ` : generation`, ` : characterisation`, ` : comparison`)
left by the chapter-restructure migration is meaningless out of context
and is a hard defect. Run
`bun run content/pipeline/qa-section-title-audit.ts` before committing
chapter-manifest changes.

## Chapter Context Snippets

Use these when writing or reviewing content for a specific chapter.
Each snippet captures the chapter's intent, its place in the paper's
arc, and the voice it requires.

### Ch 0 — Introduction

**Paper context**: The introduction frames the entire paper. It begins
with everyday observations (color, rotation, time, volume, free will,
computation) and shows that these determine a specific algebraic
structure. It previews each chapter without proving anything.

**Intent**: Convince the reader — who may know complex numbers and
calculus but not category theory — that the axioms are natural and
their consequences are concrete. Plant the seed: constants need not
be constant.

**Voice**: Accessible, first-person plural, no jargon without
immediate explanation. Short, vivid sentences for observations;
longer, precise sentences for mathematical content. No editorializing
— let the scope of the consequences speak for itself.

**Map to content**: Observations (¶1-2) → "lack of assumption" about
constants (¶3) → categorical language (¶4) → QOU definition (¶5) →
consequences preview (¶6-8) → chapter-by-chapter guide (¶9+).

---

### Ch 1 — Quantum Universes

**Paper context**: Lays the algebraic foundation. Everything in the
paper rests on the triple $(\mathbf{C}, A, \tau)$ defined here.

**Intent**: Introduce the quantum universe axioms (rigid monoidal
category, Frobenius–Hopf object, fibre functor) and derive their
first consequences (Frobenius relation, dagger involution,
Tannaka–Krein). Each definition is immediately grounded by the
SU(2) running example ($A = \mathcal{O}(\mathrm{SU}(2))$,
$V = \mathbb{C}^2$).

**Voice**: Definition–theorem–example rhythm. Formal mathematical
prose. Definitions are boxed; examples follow immediately. The SU(2)
example uses explicit matrix entries ($\alpha, \beta, \bar\alpha,
\bar\beta$) so a reader with linear algebra can follow.

**What a writer should know**: Every new definition needs a
corresponding `ex:*-su2` example block. The reader should be able
to verify each claim by working in $\mathbb{C}^{2 \times 2}$.

---

### Ch 2 — Quantum Observable Universes

**Paper context**: Promotes QU to QOU by adding three axioms
(observability, measurability, volume). This is where SU(2) emerges,
the Dirac operator decomposes, and the substrate parameter $q$
appears.

**Intent**: Show that the three additional axioms — which encode
that the universe is shared, measurable, and has volume — force
the gauge group to be SU(2), produce the categorical action
(gravity + gauge + matter), and introduce the deformation parameter
$q$ that parametrises the departure from the classical limit.

**Voice**: Same definition–theorem–example rhythm as Ch 1, but
building on Ch 1 vocabulary. Can assume the reader knows "rigid
monoidal category" and "Frobenius pairing" without re-explanation.
The SU(2) example continues: emergence of SU(2) as
$\mathrm{Aut}^{\otimes}(\tau)$, the maximal torus, weight
decomposition, spin labels.

**What a writer should know**: This chapter is the most technically
dense. Proofs may be deferred to the Elaboration section (§14) but
the main line must remain accessible. The categorical action formula
is the culmination — it must be motivated before it is displayed.

---

### Ch 3 — Lifting and Descent

**Paper context**: Addresses the global extension problem. Local
categorical data (on $A$) must be lifted to the jet object $J^1(A)$
and iterated into the brane tower. The Yekutieli lifting condition
makes this precise; the Descartes condition $\chi(A) = -6$ emerges
as the unique obstruction-consistent value.

**Intent**: Build the brane tower $\{A_n\}$, show that lifting
fails precisely when the obstruction class $\kappa(x)$ is nonzero,
derive the mass identity, and arrive at $\chi(A) = -6$ as a
forced conclusion.

**Voice**: Technical, proof-heavy, but still first-person for
narrative glue ("We now iterate the prolongation..."). Obstruction
theory language (gerbes, cocycles, descent data). The SU(2) example
continues at each brane-tower level.

**What a writer should know**: The key results are
`thm:qu-to-qou` (main theorem), `def:mass-identity`, and
`def:descartes-condition`. Every block should trace its logical
dependence back to these. The Yekutieli lifting condition is the
engine; cite [yekutieli2010] for the gerbe-theoretic foundation.

---

### Ch 4 — Braids and Knots

**Paper context**: Replaces continuum path integrals with discrete
braid-group computations. Particles are knots; interactions are
Skein relations; mass is hyperbolic volume divided by $\hbar_q^2$.

**Intent**: Develop a purely mathematical model, built entirely from
the categorical data, for objects we call photons, electrons, atoms.
These are associated to knots which, by self-duality, encode not only
what the objects *are* but how they interact. Describe explicitly the
transfer matrices that govern all particle interactions through
computational cost. Derive interaction completeness: exactly 7
transfer matrices on $\Sigma_4$. Show that physical constants (mass,
crossing energy, binding energy) are parametrised solely by $q$.
Electronic shells arise as torus knots in Gröbner bases.

**Voice**: Computational and concrete. Explicit matrices, crossing
diagrams, worked calculations. "We compute the R-matrix...",
"The transfer matrix acts as...". The SU(2) example gives way to
explicit knot calculations (trefoil, figure-eight, Borromean links).

**What a writer should know**: The reader should be able to follow
every knot calculation with pencil and paper. Use the Hecke algebra
generator $\sigma_i$ (never $T$); the same symbol $\sigma_i$ serves
both as braid generator in $B_n$ and its image in $H_n(q)$. Jones
polynomial is $J_K(q)$ (never $V_K(t)$). Hadrons are
$\mathfrak{H}$ (fraktur). The topological mass formula
$\mathfrak{m}(K) = \mathrm{Vol}(K)/\hbar_q^2$ is the chapter's
central equation.

---

### Ch 5 — Models of QOUs

**Paper context**: Concrete realisations. Part A covers general
models (archimedean, $p$-adic, finite-field, Witt-vector, Jones
polynomials, fluid dynamics). Part B is the Descartes universe:
Bring's surface $\Sigma_4$ as the specific QOU with $\chi(A) = -6$.

**Intent (Part A)**: Show that the QOU axioms admit realisations over
different ground fields. The archimedean model (over $\mathbb{C}$)
connects to Calabi–Yau, ALE spaces, instantons. Non-archimedean
models ($p$-adic, finite-field) demonstrate universality.

**Intent (Part B — Descartes)**: Study Bring's surface — the
universal genus-4 curve with automorphism group $S_5$ — as a
concrete model for QOU. Develop coordinate systems for the red,
green, and blue color tubes (the exceptional divisors where all
particle interactions occur). Identify specific torus knots with
specific particles. Derive the Descartes theorem: Bring's surface is
the terminal object in the category of QOUs with $\chi(A) = -6$.

**Voice (Part A)**: Expository, showing how the abstract framework
specialises to familiar geometric objects.

**Voice (Part B)**: The most "hands-on" chapter. Coordinate-heavy,
with explicit equations for Bring's surface ($\sum x_j = \sum x_j^2
= \sum x_j^3 = 0$), color tube coordinates, color elliptic curves,
and particle assignments. The reader should feel they are working
inside the surface.

**What a writer should know**: "Color tubes" are the geometric
objects (twisted, fractal, knotted); "color tube coordinates" are
the coordinate system. Particles are fraktur ($\mathfrak{u}$,
$\mathfrak{d}$, $\mathfrak{e}$). The Descartes theorem is a
categorical statement about terminal objects — prove it categorically,
then interpret geometrically.

---

### Ch 6 — Physical Observations

**Paper context**: Reaps the rewards of the mathematical machinery.
Confronts theory with experiment using CODATA/PDG data.

**Intent**: Estimate $q$ from the muon-to-electron mass ratio. From
this single parameter, compute estimated masses for all hadrons
(agreeing with observed values to good precision), hadron half-lives
via transfer matrices (aligning with observation), and hydrocarbon
energetics. Also: double-slit predictions, nuclear stability, CMB
signatures, and proposed experiments.

**Voice**: Data-driven. Comparison tables, error bounds, plots. "We
estimate", "the predicted value is $X \approx Y$", "which agrees
with the CODATA value to $n$ significant figures". No claims of
precision beyond what the numbers show. Use $\approx$ for all
derived/observed values (never $=$ without an error term).

**What a writer should know**: This is where the paper is most
vulnerable to overclaiming. Every numerical statement must use
$\approx$. The consistency window $q \in [1.109, 1.112]$ is
overdetermined by three independent measurements — state this fact
without commentary on how "remarkable" it is. Numerical $q$ values
are permitted only in this chapter and Ch 0.

---

### Ch 7 — Information-Theoretic Perspectives

**Paper context**: Addresses Wigner's "unreasonable effectiveness"
question. The QOU mechanics are Turing complete; computation is
intrinsic to the algebraic substrate.

**Intent**: Show that the same categorical structure that produces
particles and forces also supports computation (Gröbner basis
confluence), generates an arrow of time (Reeb flow), produces
fractal dynamics (Julia sets at the boundary), and derives
$E = mc^2$ from the information speed of light $c_q = 1/(q-1)$.

**Voice**: Speculative but grounded. "The framework suggests",
not "we prove", for claims that extend beyond the established
formalism. Mark conjectures clearly. The Hausdorff dimension
formula $d_H(q) = (2q-1)^2/q^3$ and the mass-energy equivalence
$E_{\mathfrak{H}} = \mathfrak{m}_{\mathfrak{H}} \cdot c_q^2$ are
derived results; state them as theorems. The Big Bang as an
information-theoretic event and Planck-scale computation are more
speculative — frame accordingly.

**What a writer should know**: This chapter connects to computer
science and information theory. Assume the reader knows basic
computability (Turing machines) but not the categorical encoding.
The Skein Turing machine construction is the key technical result.

---

### Glossary (Ch 8) and Appendices

**Voice**: Reference material. Terse, definitional. Each glossary
entry maps a paper term to a Mathlib declaration. The knot-periodic
table is a data table, not prose. The index of definitions is
machine-generated.

## Running Example Consistency

The SU(2) running example (starting from `ex:rigid-monoidal-vect`
and `ex:quantum-universe-su2`) must maintain consistent notation
and voice across all chapters:

| Element | Notation | First introduced |
|---------|----------|-----------------|
| Category | $\mathbf{Rep}(\mathrm{SU}(2))$ | Ch 1 |
| Frobenius-Hopf object | $A = \mathcal{O}(\mathrm{SU}(2))$ | Ch 1 |
| Fundamental rep | $V = V_{1/2} \cong \mathbb{C}^2$ | Ch 1 |
| Basis | $\{e_1, e_2\}$ for $V$ | Ch 1 |
| Matrix generators | $\alpha, \beta, \bar{\alpha}, \bar{\beta}$ | Ch 1 |
| Fibre functor | $\tau$ (forgetful functor) | Ch 1 |

When extending the example in later chapters, always reference back:
"Continuing the SU(2) example from §1..." or use the `interprets`
field pointing to the earlier example block.

## Terminology Consistency

| Term | Correct | Incorrect |
|------|---------|-----------|
| Geometric tubes on Bring's surface | color tubes | color tubes, chiral tubes |
| Coordinate system for r,g,b | color tube coordinates | color tube coordinates |
| Physical chirality (experiments) | chiral | color |
| Hadron variable | $\mathfrak{H}$ | $H$ (plain italic) |
| Hadron mass | $\mathfrak{m}_{\mathfrak{H}}$ | $\mathfrak{m}_H$, $m_H$ |
| Category | $\mathbf{C}$ (bold) | $\mathcal{C}$ (calligraphic) |
| Fibre functor | $\tau$ | $\omega$, $U$ |
| Energy | $\mathbf{E}$ (bold) | $\mathfrak{E}$ (fraktur) |
| Mass | $\mathfrak{m}$ (fraktur) | $m$ (plain) |
| Substrate parameter | $q$ (symbolic) | $q = 1.1097$ (numerical, except Ch 6) |

## Editorializing Blacklist

The following phrases and patterns must never appear in the paper:

- "surprisingly", "remarkably", "interestingly", "notably"
- "perhaps the most surprising/important/significant"
- "it is worth noting that"
- "the reader will appreciate"
- "it turns out that" (just state the result)
- "one might expect" (state what happens, not what was expected)
- "a beautiful result" / "an elegant proof"
- Any commentary on the importance or surprise value of results

Results speak for themselves.

## Pre-Commit Checklist

Before committing any .md content, verify:

1. [ ] **Person**: All narrative uses "we" (first-person plural)
2. [ ] **Referent**: "this paper" (never "this book/work/article")
3. [ ] **Tense**: Present tense for definitions and theorems
4. [ ] **Tone**: No editorializing phrases (check blacklist above)
5. [ ] **Notation**: All symbols match the notation register (§7aa)
6. [ ] **Color/color**: Geometric tubes = "color"; coordinates = "color"
7. [ ] **Hadron fraktur**: $\mathfrak{H}$ for hadrons, not $H$
8. [ ] **Example thread**: SU(2) examples use consistent notation
9. [ ] **Cross-chapter**: Terms introduced in earlier chapters are
       referenced, not re-defined
10. [ ] **Chapter voice**: Content matches the chapter context snippet

## Procedure

1. **Read** the target .md file(s)
2. **Identify** the chapter and section context (see snippets above)
3. **Check** each rule in the pre-commit checklist
4. **Flag** violations with file path, line number, and fix
5. **If ambiguous** — if you're unsure whether a passage should be
   active or passive, concrete or abstract, or what the author's
   intent is — **ask the author** using AskUserQuestion before
   making changes
6. **Fix** all clear violations
7. **Report** summary of changes made
