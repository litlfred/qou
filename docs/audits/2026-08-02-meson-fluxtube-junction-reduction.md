# Meson flux-tube braid — Y-junction reduction / D-meson operator-selection: honest negative (2026-08-02)

**Branch:** `claude/meson-fluxtube-operation-2026-08-02` · **PR:** #4614
**Lean:** [`MesonFluxTubeReduction.lean`](../../content/quantum-observable-universe/lean/QOU/ParticleInteractions/MesonFluxTubeReduction.lean) (sorry-free, `lean`-direct exit 0)
**Witness:** [`meson-fluxtube-topology.witness.json`](../../computations/meson-fluxtube-topology.witness.json)
**Serves:** bean `qou-qpj9` (meson-binding braid gate); the J/ψ attack [`2026-08-02-jpsi-boundstate-mass.md`](2026-08-02-jpsi-boundstate-mass.md) (PR #4608); owner bean `qou-jsx5` (lattice-QCD-from-QOU, PR #4600).

## The task

Derive the **canonical meson flux-tube braiding operation** — the operation that turns a `q̄q` colour singlet into a definite braid/tangle whose mass the framework can then predict. The J/ψ attack showed the charmonium mass is *in-range* for the hyperbolic mechanism (Vol ≈ 24 → 3097 MeV) but **no canonical c̄c braid exists** — J/ψ and η_c wanted different-topology braids (per-state-fit signature), so any braid choice was a fit.

Two routes were attempted:
1. **Topological (Y-junction → single-tube reduction).** Reduce the baryon's 3-tube Borromean vertex to the meson's single tube.
2. **Owner-redirected (symbolic gg→c̄c operator-selection on the D meson).** Target the D meson `c̄u` (1864.84 MeV) — the minimal dressing of a *stable* isolated `c̄` (no annihilating `c` partner, unlike charmonium) — and fix the asymmetric `c̄`(n=5) | light(n=3) tube via the Frobenius–Gram operator-selection rather than a numerical braid-volume search.

**Both routes fail to canonically fix a braid a priori.** The joint mass check was therefore **not** run (running it would be the per-state fit the discipline forbids). The negatives are sharp and name the precise missing structural data.

## Route 1 — the naive Y-junction → single-tube reduction is `Vol = 0` (scope (b))

The proton mass-knot is the Borromean link `6₂³ = (σ₁σ₂⁻¹)³`, a **3-strand** braid whose exterior is hyperbolic:

| object | strands | word | Vol (SnapPy) |
|---|---|---|---|
| Borromean (proton) | 3 | `(σ₁σ₂⁻¹)³` | **7.32772475342** = 2·V_oct ✓ |
| `(σ₁σ₂⁻¹)⁶` | 3 | — | 21.6315986792 |
| `(σ₁σ₂⁻¹)⁷` | 3 | — | 26.054401507 |
| `T(2,k)`, k=2..10 | 2 | `σ₁^k` | **0** (incl. gluon `T(2,9)`) |
| drop-σ₂ reduction | 2 | `σ₁³` (trefoil) | **0** |

QCD reading: three quarks, three colour flux tubes meeting at a string (Y-)junction. A meson `q̄q` has two endpoints and a single tube — no junction. The *literal* junction reduction (collapse the Y, drop one tube) takes the strand count **3 → 2**.

**The obstruction.** A 2-strand braid has no braiding freedom beyond one winding number: `B₂ ≅ ℤ` is abelian — the braid relation `σ₁σ₂σ₁ = σ₂σ₁σ₂` needs a *third* strand. Hence every 2-strand braid is a torus braid `σ₁^k`, closure `T(2,k)`, hyperbolic volume `0` (Thurston; SnapPy-verified above). The reduction yields only a `Vol = 0` **carrier** (quantum numbers), never a hyperbolic mass-knot — strand *removal* cannot build the Brunnian (≥ 3-component) structure hyperbolicity requires.

This is a scope-**(b)** structural exclusion of *this specific operation*, cited invariant: `B₂` abelian (Lean-proved: `twoStrand_comm`, `twoStrand_commutator_trivial`, `twoStrand_winding_bijective`) + the torus-link `Vol = 0` theorem (SnapPy-witnessed). Every one of those Lean facts is **false** for `B₃` — whose nonabelian commutator structure *is* where the hyperbolic Borromean `(σ₁σ₂⁻¹)³` lives.

**The framework already knows this.** `lepton-meson-parallel.md` places the meson at **`H₃(q)` (3-strand)**, braid `(σ₀σ₁)²·σ₁σ₀` (Hopf-bound `q̄q` pair) — the Hopf-binding *supplies* the third strand. So the naive single-tube reduction is not the framework's meson; the "3rd strand" is the binding, not a quark. This route rules out the literal picture and points at the actual `H₃(q)` construction.

## Route 2 — the D-meson operator-selection is charm-degenerate (the load-bearing negative)

On the `H₃(q)` meson, the owner-redirected route fixes the braid via the symbolic **gg→c̄c operator-selection** (`operator-selection-lp.md`, `knot-operator-selection-proof.md`): the Frobenius–Gram LP selects the minimum-crossing-energy operator `Φ*` for a given `(n_strands, n_target)` and produces a dual certificate. The mechanism *is* canonical — a well-posed LP with a unique optimiser. **Its inputs for the D meson are not.**

### The generation-winding dictionary indexes generation, not up/down-type

`lepton-meson-torus-knot-dictionary.lean` fixes the meson crossing count as the **sum of the two quark generation windings** `n ∈ {3,5,7}` (`meson_crossing_is_sum`, Lean-proved):

| meson | quarks | windings | crossings |
|---|---|---|---|
| π | ū d | {3,3} | 6 |
| K | ū s | {3,5} | 8 |
| η/φ | s̄ s | {5,5} | 10 |

The dictionary is a **symmetric function of the unordered winding pair.** For the D meson `c̄u = {n_charm, 3}` this immediately collides:

- **charm = 5** ⇒ D `{5,3}` = kaon `{3,5}` — *identical multiset*, 8 crossings, same operator-selection target;
- **charm = 7** ⇒ D `{7,3}` shares its 10-crossing count with `η/φ` `{5,5}`.

But `m_D ≈ 1865 ≈ 3.8·m_K`. The winding dictionary **cannot separate D from K** (Lean-proved: `windingContent` is non-injective, `winding_content_not_injective`). The gg→c̄c operator-selection selects the *generation-2* (`n=5`) block — which is exactly the strange-selection; nothing in the `{γ,σ₀,σ₁,L₊,L₋,e⁻}` `H₃(q)` basis produces a charm-*specific* operator distinct from the strange operator.

### Corpus inconsistency (flag for canonical-watcher)

> **🛑 RETRACTED 2026-08-24 — this inconsistency does not exist and never did.**
> The paragraph below claimed the corpus assigns charm two incompatible windings.
> It does not. Both tables say **T(2,5)**:
>
> - `knot-formula-table-table2-data.md` line 11: `| Charm quark | 𝔠 | $T_{2,5}$ | 2 | 5 |`
> - `knot-notation-convention-table1-data.md` line 9: `| 𝔎_c | $(2,5)$-torus knot | $5_1$ | charm c | c^σ |`
>
> The reported `(2,7)`/`7₁` is the value on the **preceding line** — line 8,
> `| 𝔎_τ | septafoil | $7_1$ | τ⁻ | τ⁺ |`, the **tau lepton**. The audit read
> line 9's label with line 8's knot: an off-by-one across two adjacent rows.
>
> Verified, not assumed: `git log -L 9,9` on that file shows the line was
> **created** as `(2,5)` (commit `e54ffbca0a`); `git log -S` finds **no** commit
> that ever wrote a charm `7₁` row there; and a corpus-wide grep finds charm
> mapped to 7 **nowhere**.
>
> **Consequence — the "two independent ❌s" below are ONE.** Charm's own winding
> is unambiguous at n = 5. What survives is the D-vs-K degeneracy, and it is
> *sharper* for this correction, not weaker: with charm fixed at 5 there is no
> n = 7 escape hatch, so `D {5,3}` is an **exact** multiset collision with
> `K {3,5}` and no winding assignment separates them.
>
> ~~Original paragraph, retained:~~

~~The prerequisite input — *which* torus knot is the charm quark — is itself ambiguous in the corpus:~~

- ~~`knot-formula-table-table2-data.md` row 11: **charm `𝔠` → T(2,5)** (m=2, n=5).~~
- ~~`knot-notation-convention-table1-data.md` row 9: **charm `c` → (2,7)-torus knot `7₁`** (n=7).~~

~~These are incompatible (n=5 vs n=7).~~

## The grading the audit calls missing is IN the corpus — as `σ` (added 2026-08-24)

The section below concludes that a canonical D braid needs "an invariant the
`T(2,n)` winding number does **not** carry: a weak-isospin / up-down-type grading
`T₃` orthogonal to the generation winding `n`". Reading table 2 whole, the corpus
already carries a grading that separates the two, and it is one the audit's own
next-step names as a candidate ("a bar/mirror asymmetry on the `c̄` end"):

| gen | up-type | down-type |
|---|---|---|
| 1 | `u = T(2,3)` | `d = T(2,3)^σ` |
| 2 | **`c = T(2,5)`** | **`s = T(2,5)^σ`** |
| 3 | *(top deprecated → `T(3,4)`)* | `b = T(2,7)^σ` |

**`σ` is present iff the quark is down-type — in all five quark rows, three
generations for three.** So `c` and `s` are *not* the same object in the corpus:
they are `T(2,5)` and its mirror. `knot-notation-convention.md` defines
`T_{m,n}^σ = T_{m,-n}`.

**So the degeneracy is a LOSSY PROJECTION, not an absent structure.** `D {c̄, u}`
and `K {ū, s}` collide only after `windingContent` maps each knot to a bare `ℕ`
and discards `σ`. The discriminator survives one level up.

### ⚠️ WEAKENING MY OWN FINDING — `σ` is DOCUMENTED as charge conjugation (2026-08-24, second pass)

The section above says `σ` is "overloaded" and treats which meaning applies as
merely undecided. Reading `knot-notation-convention.md` in full makes the tension
sharper than that, and **against** the T₃ reading. Two consecutive sentences of
that block:

> "Particles in this framework are identified with their knots. We write
> `𝔎_x^±` … **The superscript distinguishes a particle from its antiparticle via
> mirror reflection (charge conjugation).**"
>
> "We denote torus knots by `T_{m,n}`, with **mirror image** `T_{m,n}^σ =
> T_{m,-n}`."

So on a knot, the corpus *states* `σ` = mirror = **charge conjugation**, and
instantiates it on leptons: electron `T_{2,3}` / positron `T_{2,3}^σ`.

`knot-formula-table.md` then applies the same superscript to quarks:
`𝔲 = T_{2,3}`, `𝔡 = T_{2,3}^σ`; `𝔠 = T_{2,5}`, `𝔰 = T_{2,5}^σ`;
`𝔟 = T_{2,7}^σ`. Read with the stated meaning, that asserts

    d = ū,    s = c̄,    b = t̄

— identifying charge `−1/3` quarks with charge `−2/3` antiquarks. **That cannot
be intended.**

**Consequence for the T₃ question, stated against my own earlier framing.** If
`σ` is charge conjugation as documented, it **cannot** be the `T₃` grading: it
would make every down-type quark the antiparticle of its up-type partner. So the
σ observation is *not* "the missing grading is already here" — it is "the corpus
uses one superscript for two relations, has documented only the one that does not
work for this purpose, and the discriminating assignment is therefore
**undefined**, not merely unprojected." The 5/5 down-type alignment is real and
still suggestive; what it is *not* is a licensed grading.

This is a genuine corpus defect, not a reading difficulty: the same operation is
defined as charge conjugation and used as the weak-isospin partner map. Which one
the quark rows mean is an authorial call, and it is the prerequisite for
`qou-mesont3` — not a detail downstream of it.

### A second, independent defect in the same block: `𝔡` is given two incompatible knots

`knot-formula-table.md` writes `𝔡 = T_{2,3}^σ` and then, one sentence later:
"Here `𝔡` denotes the three-twist knot `5₂`, which is a Skein descendant of the
trefoil."

These are different knots. `T_{2,3}^σ = T_{2,-3}` is the **mirror trefoil** `3₁`
— 3 crossings, a torus knot. `5₂` is a **twist knot** with 5 crossings and is
**not a torus knot at all**. The block's own table 2 lists `| Down quark | 𝔡 |
T_{2,3}^σ | 1 | 3 |` — **Crossings = 3**, agreeing with the formula and
contradicting the prose.

Corpus-grepped: unrecorded. Every other `5₂` in the corpus is Kashaev-invariant /
Borel-summability literature (`references.ts`, the `5₂` saddle sum rule), none of
it about the down quark. **Not resolved here** — whether `𝔡` is the mirror
trefoil or `5₂` is an authorial call, and picking one to make the table
self-consistent would be exactly the kind of silent resolution the corpus
disciplines forbid. Flagged with the evidence.

### The `𝔡` defect is a ONE-OFF finding, not a QA criterion — measured and declined

The obvious next move is to mechanise the `𝔡` check as a sidecar criterion:
`T(2,n)` has crossing number `n`, `5₂` is not a torus knot, so a block asserting
both should be decidable by arithmetic. **Measured, it is not mechanisable at
that level, and the criterion is declined.** Recorded here so it is not
re-proposed.

The arithmetic claim is correct; the *detector* built on it is not. Two scopes
were prototyped against the whole `content/` tree:

| scope | flagged | real |
|---|---|---|
| file-level co-occurrence of `T(2,n)` and an AB symbol | 11 | **1** |
| single table row carrying both | worse | — |

**File scope** over-flags ~10:1: 8 of the 11 hits are one auto-generated
`definition-index.md` counted once per occurrence; one is `3_2`, which is not a
knot at all (regex noise); and the `brings-surface` hits are the corpus's
legitimate Kashaev / Borel-summability work on `5₂` merely *co-occurring* with a
`T(2,n)` in the same file. Co-occurrence in a file is not a claim about the same
object.

**Row scope is worse, not better.** A table row routinely holds several distinct
objects and several unrelated integer columns, so the check reads genus and index
cells as crossing counts (`crossings=1` against `T(2,7)`) and flags
`4₁` beside `T(2,3)` in an *embeddability comparison* table — where naming two
different knots in one row is the point.

Doing it properly needs per-table column semantics — knowing which cell names the
object and which is its crossing number. That is table-specific schema, not a
generic criterion, and the corpus has ~215 `.md` files carrying a `T(2,n)`.

**So: `𝔡` stays a one-off finding, flagged above with its evidence.** The general
lesson is the one this session has now hit twice: a criterion that sounds
deterministic is worth nothing until you measure what it flags. (The other
instance: `qou-omiu`'s suffix exclusion, declined at 26.6 % of scan surface for
zero measured benefit.)

**Two cautions, so this is not over-read.** (1) `σ` is **overloaded**: the same
superscript marks particle/antiparticle elsewhere (`knot-notation-convention.md`:
electron `T_{2,3}` vs positron `T_{2,3}^σ`; `antineutrino-knot.md`). Whether
table 2's `σ` *is* the `T₃` grading or is notation reuse that happens to align is
exactly the open question — the alignment is 5-for-5, which is not nothing, but a
pattern is not a derivation. (2) Nothing here fixes a D braid or predicts `m_D`;
the joint mass check stays un-run for the same anti-fit reason. What changes is
**where to look**: at the dictionary's projection, not at importing a new `T₃`
from the weak sector.

### The precise missing datum

A canonical D-meson braid needs an invariant the `T(2,n)` winding number does **not** carry: a **weak-isospin / up-down-type grading `T₃`** orthogonal to the generation winding `n`. Charm (up-type gen-2) and strange (down-type gen-2) share `n`; what distinguishes them is weak isospin. Consistently, the framework itself places the up/down distinction in the *weak* sector — the cross-family generator `T(3,5)` (`force-knot-identification.md`), which transmutes up↔down — **not** in the `T(2,n)` winding dictionary. Until the meson-binding operation is refined to consume a `T₃` grading (so the c̄ block is selected distinctly from the s̄ block), the D-meson braid is not canonically fixed and its mass can only be fitted.

## What is canonical vs not (summary)

| ingredient | canonical? |
|---|---|
| operator-selection LP mechanism (unique `Φ*` per `(n, n_target)`) | ✅ yes (well-posed, dual-certified) |
| meson = `H₃(q)` Hopf-bound `q̄q` (3-strand) | ✅ yes (framework) |
| `m_K/m_π` mass *ratio* (down-type mesons) | ✅ yes (L2-MET observable) |
| charm's own winding `n` | ✅ **yes — n = 5** (the claimed T(2,5)-vs-T(2,7) ambiguity was a misread; retraction above, 2026-08-24) |
| D-vs-K separation from winding number | ❌ **degenerate** (same multiset at n=5) |
| up/down-type grading `T₃` on the meson tube | ❌ **undefined** — a `σ` superscript does mark down-type in 5/5 quark rows, but `knot-notation-convention.md` *documents* `σ` on a knot as **charge conjugation**, under which those rows assert `d = ū`, `s = c̄`, `b = t̄` (charge −1/3 = −2/3). One superscript, two relations, only the wrong one defined. Second pass 2026-08-24 — this row briefly read "present as `σ`"; that was too generous. |

**ONE `❌` blocks a canonical D-meson braid, not two** (corrected 2026-08-24): the D-vs-K winding degeneracy. Charm's winding is unambiguous at n = 5, and that makes the surviving obstruction *sharper* — with no n = 7 alternative, `D {5,3}` is an exact multiset collision with `K {3,5}`. The reduction is still **not** canonical and the honest step is still not a mass check. The structural refinement to aim at is now specific — but it is **upstream** of where this audit was looking: before `windingContent` can be lifted to carry `σ`, the corpus has to *define* which relation `σ` denotes on a quark knot, because the only meaning it currently documents (charge conjugation) is the one that cannot serve. That is a prerequisite for `qou-mesont3`, not a step within it.

## Anti-fit statement

No braid was hand-picked to reproduce 1864.84 / 1869.66 MeV. The joint `m_D` check was deliberately **not** run: with the braid under-determined at two independent points, a "closest hit" would be exactly the per-state fit the J/ψ attack already recorded as worthless. A negative that names the missing datum (`T₃` grading ⟂ `n`) is the valuable output.

## Next honest step (refines `qou-qpj9`)

Derive (or refute) a **weak-isospin `T₃` grading of the `H₃(q)` meson tube** that selects the charm (up-type) block distinctly from the strange (down-type) block — e.g. from the `T(3,5)` weak-generator's up↔down action, or a bar/mirror asymmetry on the `c̄` end. If such a grading is derived and canonically fixes the asymmetric `c̄`(5̄)|light(3) braid, *then* check once against `m_D`. ~~Separately: resolve the charm T(2,5)-vs-T(2,7) corpus inconsistency (canonical-watcher).~~ **Withdrawn 2026-08-24 — there is no such inconsistency** (retraction at the top of Route 2). The live successor is narrower and better posed, and has **two** parts: (1) decide which relation `σ` denotes on a quark knot — the corpus documents charge conjugation, which would make `d = ū`, so the down-type usage is currently undefined rather than merely unprojected; then (2) lift `windingContent` to carry it. Separately and independently: `𝔡` is assigned two incompatible knots in one block (`T_{2,3}^σ` = mirror trefoil, 3 crossings, vs prose "the three-twist knot `5₂`", 5 crossings, not a torus knot; the table's own Crossings column says 3).
