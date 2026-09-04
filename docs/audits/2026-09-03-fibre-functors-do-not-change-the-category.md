# A fibre functor changes dimensions, not fusion rules — the T3g question is answered, and it was the wrong question

**Date:** 2026-09-03
**Branch:** `claude/8-fold-way-qou-derivation-qj9uzv` (PR #6458), front 2
**Beans:** `qou-yjwg` (this front); bears on `qou-y7vg` (T3g), `qou-8pl3` (Route A), `qou-d7h1`
**Lean:** [`QOU/Eightfold/FibreFunctorDimensionNotCategorical.lean`](../../content/quantum-observable-universe/lean/QOU/Eightfold/FibreFunctorDimensionNotCategorical.lean) — 12 declarations, `lean`-direct exit 0, `#print axioms` on every one gives only `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`
**Probe:** [`computations/probes/fibre_functor_dimension_not_categorical_probe.py`](../../computations/probes/fibre_functor_dimension_not_categorical_probe.py) — exact over `ℚ(q)[b]` and `ℤ`; witness carries no JSON float
**Supersedes in part:** the re-posing in [`2026-08-25-4a-question-imports-symmetric-theory.md`](2026-08-25-4a-question-imports-symmetric-theory.md) §4–§5 (see §1 below)

---

## 0. The claim, flatly

The eightfold programme's recorded live surface
([`2026-08-07-eightfold-live-surface-collapse.md`](2026-08-07-eightfold-live-surface-collapse.md) §3,
cheat-sheet §4-A) is one question:

> Does QOU's braided category admit inequivalent fibre functors?

**Yes — and it does not help.** On the single-fibre category, which the corpus
identifies with `Rep(SL_q(2))` at generic `q`
([`def:quantum-gauge-group`](../../content/quantum-observable-universe/quantum-observable-universes/quantum-gauge-group.md),
[`ex:tannaka-krein-su2`](../../content/quantum-observable-universe/q-geometric-langlands/tannaka-krein-su2.md)),
the fibre functors are **classified** (Bichon 2003 \[`bichon2003`\];
Etingof–Ostrik 2004 \[`etingof-ostrik2004`\]), and they exist at **every**
dimension `n ≥ 2`, including `n = 3`, and are real at the substrate `q₀`. But a
fibre functor is monoidal, so it carries the category's fusion rules with it: it
changes `dim τ'(V)` and nothing else. Under a three-dimensional fibre functor,

```
V^{⊗3}  ≅  V_{3/2} ⊕ V_{1/2} ⊕ V_{1/2}     with dimensions  21 + 3 + 3 = 27,
```

never `10 + 8 + 8 + 1`. The eightfold decomposition needs a **one-dimensional
summand** of `V^{⊗3}` (the totally antisymmetric channel, `Λ³`), and no fibre
functor of any dimension supplies one, because the spin-`0` object is absent
from `V^{⊗3}` by Clebsch–Gordan parity — a property of the **category**.

Scope-**(b)** structural exclusion of the *fibre-functor route*; the invariant is
the Clebsch–Gordan parity of `Rep(SL_q(2))`, preserved by every monoidal
functor. It is **not** an exclusion of the eightfold way from QOU. It relocates
the missing object from `τ` to `C`.

## 1. Why the 2026-08-25 re-posing pointed at the wrong reconstruction

That audit correctly retracted the band/`H¹` formulation (symmetric-Tannakian
machinery applied to a proved-non-symmetric category) and proposed instead:

> what is the reconstructed Hopf algebra `H = End^⊗(τ)` of a QOU, and does it
> contain an `SU(3)`-like sub-object? — citing Lentner–Mombelli's Hopf algebra
> *internal to* `C`.

Two things about that. First, Lentner–Mombelli's Theorem 6.11
(`library/arxiv-2311.14221v2` §6.4) is the reconstruction for a monoidal
functor `F : B → C` whose *target* is a braided category — the situation *"in
the absence of fibre functors"* (their own words). QOU's `τ` lands in `R-Mod`
by definition
([`def:quantum-universe`](../../content/quantum-observable-universe/quantum-universes/quantum-universe.md):
*"an `R`-linear faithful fibre functor `τ : 𝐂 → R-Mod`"*), which is symmetric.
So the applicable reconstruction is the classical one for a braided **source**
with a fibre functor to vector spaces — Ulbrich/Majid, the coend
`∫^X τ(X)^∨ ⊗ τ(X)` — and it produces an ordinary coquasitriangular Hopf
algebra over `R`, not a Hopf algebra internal to `C`. The corpus **already
does this computation**: `ex:tannaka-krein-su2` runs the coend and obtains
`H ≅ 𝒪_q(SU(2))`, and `def:quantum-gauge-group` names it. So the "what is `H`?"
question was answered before it was asked, and the answer (`𝒪_q(SL_2)`) has no
`SU(3)`-like sub-object for the same reason `Rep(SL_q(2))` has no
three-dimensional fundamental.

Second, and this is the substantive point: **which reconstruction one uses does
not matter for the eightfold question**, because `C ≃ Comod(H)` for *any* fibre
functor `τ'` and its `H' = End^⊗(τ')`. The categories are equivalent; the
multiplet structure lives in the category. Changing `τ` changes the Hopf
algebra (from `𝒪_q(SL_2)` to Bichon's `B(E)`) and the dimension of the
fundamental comodule (from `2` to `n`), and leaves every fusion rule intact.

## 2. F1 — the fibre functors exist, at every dimension, real at `q₀`

Bichon's theorem: for `E ∈ GL_n(k)`, `n ≥ 2`, with

```
tr(E⁻¹ Eᵗ) = −q − q⁻¹ ,
```

the comodule category of the bilinear-form quantum group `B(E)` is monoidally
equivalent to that of `𝒪_q(SL_2)`, with the fundamental of `𝒪_q(SL_2)` going to
the `n`-dimensional fundamental of `B(E)`. Composing the equivalence with the
forgetful functor of `B(E)` gives a fibre functor `τ'` on `Rep(SL_q(2))` with
`dim τ'(V) = n`.

The probe exhibits such `E` exactly. Sanity case `n = 2`: the standard
`E_q = [[0, 1], [−q⁻¹, 0]]` gives `tr(E⁻¹Eᵗ) = −q − q⁻¹` and recovers
`𝒪_q(SL_2)` itself. For `n ≥ 3`, the block form
`E = I_{n−2} ⊕ [[0, 1], [b, 0]]` has `tr(E⁻¹Eᵗ) = (n − 2) + b + 1/b`, so the
condition is the quadratic

```
b + 1/b = −(q + q⁻¹) − (n − 2) ,
```

whose discriminant `(q + q⁻¹ + n − 2)² − 4` is at least `n² − 4 > 0` for every
real `q > 0` (since `q + q⁻¹ ≥ 2`). Both roots are real and nonzero (product
`1` by Vieta). At the proton pin, `n = 3`:

| root | value (30 dps, sign is all that is claimed) |
|---|---|
| `b₋` | `−2.6307817108703560132…` |
| `b₊` | `−0.3801151558367662851…` |

So **a real three-dimensional fibre functor exists on the single-fibre category
at the substrate `q₀`**. That is the affirmative answer to T3g's question, and
it is a literature fact, not a QOU result.

## 3. F2/F3 — and it changes nothing that matters

`τ'` is monoidal and exact, so `τ'(V ⊗ V_j) ≅ τ'(V) ⊗ τ'(V_j)` and the
Clebsch–Gordan rule `V ⊗ V_j ≅ V_{j+½} ⊕ V_{j−½}` gives the dimension recursion
`d_{k+2} = n·d_{k+1} − d_k` with `d_0 = 1`, `d_1 = n`. Proved in Lean
(`dimSeq_three : dimSeq n 3 = n³ − 2n`, `cube_total`, `dims_cube_at_three`):

| `n = dim τ'(V)` | dims of `V^{⊗3} = V_{3/2} ⊕ 2V_{1/2}` | total |
|---|---|---|
| 2 (standard `τ`) | 4, 2, 2 | 8 |
| **3** | **21, 3, 3** | **27** |
| 4 | 56, 4, 4 | 64 |
| 8 | 496, 8, 8 | 512 |
| 10 | 980, 10, 10 | 1000 |

The eightfold `𝟑^{⊗3} = 𝟏𝟎 ⊕ 𝟖 ⊕ 𝟖 ⊕ 𝟏` has the same total as the `n = 3` row
and a different split. The decisive difference is the `𝟏`:

- `cgSpins_parity` (Lean): every summand of `V^{⊗k}` has `2j ≡ k (mod 2)`, so
  `zero_not_mem_cgSpins_three`: **the spin-`0` object does not occur in
  `V^{⊗3}`** — this is `Λ³V = 0` stated categorically.
- `no_one_dimensional_summand_of_cube` (Lean): for every `n ≥ 2`, every summand
  of `V^{⊗3}` has dimension `≥ n ≥ 2`. **No fibre functor produces the singlet.**
- `dimSeq_three_ne_ten`, `dimSeq_three_ne_eight` (Lean): `n³ − 2n ∉ {8, 10}`
  for every `n`, so the top summand is never a decuplet or an octet; a
  `10`-dimensional summand occurs only at `n = 10`, and it is `V` itself.

Probe cross-checks: no `n ∈ [2, 10⁴]` gives a one-dimensional summand or the
multiset `{10, 8, 8, 1}`; `n³ − 2n = 10` and `= 8` have no integer root (exact,
sympy).

**The `8` that does appear is not the octet (F4).** At `n = 3`,
`V ⊗ V ≅ V_0 ⊕ V_1` has dimensions `1 + 8`, and it is tempting to read the `8` as
`SU(3)`'s adjoint. Its square says otherwise: `V_1 ⊗ V_1 ≅ V_0 ⊕ V_1 ⊕ V_2` has
dimensions `{1, 8, 55}`, against the octet's
`𝟖 ⊗ 𝟖 = 𝟏 ⊕ 𝟖 ⊕ 𝟖 ⊕ 𝟏𝟎 ⊕ 𝟏𝟎̄ ⊕ 𝟐𝟕`. Same total `64`, different multiset.
Recorded so that a coincidence of one dimension is not read as a coincidence of
representation theory — the exact trap the anti-laundering discipline names.

## 4. What this settles, and what it does not

| | status |
|---|---|
| T3g / `qou-y7vg`: "does the category admit inequivalent fibre functors?" | **answered: yes** (Bichon), at every `n ≥ 2`, real at `q₀` — literature, cited |
| "…and can one of them be the three-dimensional flavour object?" | **excluded, scope-(b)**: no fibre functor changes the fusion rules; the singlet `V^{⊗3}` needs is absent categorically |
| the 2026-08-25 "what is the reconstructed Hopf algebra?" | **already answered** by `ex:tannaka-krein-su2` (`𝒪_q(SU(2))`); and irrelevant to the eightfold question, since every reconstruction gives an equivalent category |
| Route A of `qou-8pl3` (a 3-dim `W` with `Sym²W` irreducible, at the groupoid level) | **untouched** — this note is about fibre functors on the *single-fibre* category; a genuinely different category is a different question |
| the eightfold way from QOU | **not excluded**; relocated |

**Where the missing object now lives.** The eightfold decomposition is a
property of a category in which `Λ³` of the fundamental is non-zero. QOU axiom 5
([`def:quantum-observable-universe`](../../content/quantum-observable-universe/quantum-observable-universes/quantum-observable-universe.md))
imposes `Λ²V ≅ 𝟙` on the fundamental, which forces `dim V = 2`
(`VolumeConstraintForcesFibreTwo.exteriorSquareDim_eq_one_iff`) and hence
`Λ³V = 0`. So the honest statement is:

> **The eightfold way is unreachable from the fundamental `V` of a QOU by any
> change of fibre functor, because axiom 5 fixes the fusion rules of the
> single-fibre category to those of `Rep(SL_q(2))`. A flavour `SU(3)` needs
> either a different fundamental object (not a summand of `V^{⊗n}` — the Sym²
> parity exclusions already cover those) or a category not generated by one
> object satisfying axiom 5.**

That is the same conclusion `qou-dwsh` reached as a *specification*
("the representation must not be a tensor power of one `V`"), now with the
fibre-functor escape closed by a proved invariant rather than assumed away.

## 5. Relation to the tower (PR #6415) — one clarification

PR #6415 measures the Wedderburn blocks of `H_n(q)` with `ℓ(λ) > 2` as
**trace-blind** under convention D and asks whether an `SU(3)` action might live
there. This note adds one categorical fact to that framing: those blocks are not
merely invisible to the trace on `V^{⊗n}`; **they do not occur in `V^{⊗n}` at
all** (the `(1³)` isotypic component of `V^{⊗3}` is `Λ³V = 0`; in general
`V^{⊗n}` carries only `ℓ(λ) ≤ 2`, which is the row cap as a statement about
objects rather than weights). The abstract algebra `H_n(q)` has them; the tensor
powers of the fundamental do not. This is consistent with #6415's own caution
(*"the blind blocks are `H_n`-side structure"*) and sharpens it: realising them
on anything requires an object `W` with `Λ³W ≠ 0`, i.e. the same missing object
as §4. Convention D's Markov trace is the categorical trace of `V^{⊗n}`, so its
blindness to those blocks is their absence, not their concealment.

## 6. Verification

- **Lean**: `lean`-direct against the restored olean cache
  (`.lake/RESTORED-NO-TRACES` present; no `lake build`), specific Mathlib imports
  only. Exit 0, no diagnostics. `#print axioms` on all 12 declarations:
  `[propext, Classical.choice, Quot.sound]` at most; `dimSeq_three`, `cube_total`
  need only `[propext, Quot.sound]`. Zero `sorryAx`.
- **Probe**: runs from its own directory with `PYTHONPATH` unset (the
  `_path_bridge` bootstrap defect class). Every stated fact is an `assert`.
  The witness contains no JSON float (recursive scan). The only numerical step
  is the 30-dps evaluation of `b` and the discriminant at the proton pin, and
  only their **signs** are claimed.
- **Bibliography**: `bichon2003`, `etingof-ostrik2004` added to
  `content/schema/references.ts` **without DOI and unverified**: `doi.org` and
  `arxiv.org` are blocked by the sandbox egress proxy this session. Both notes
  say so. Verify before print.
- **Not run**: CI (dispatch-only repo-wide). No content block edited in this
  slice; the chapter's open-problems ledger is updated in the next commit with
  its own render-QA.

## 7. Corpus-grep record

Paths 1–6 for *Bichon*, *bilinear form quantum group*, *Etingof–Ostrik*,
*Mrozinski*, *Hopf–Galois*: `content/` hits only the unrelated
`quantum-dilogarithm-stratified-proof.md`; `docs/` only the library
title-override ledger; `computations/` none; `.beans/` only this session's
`qou-yjwg`; `library/INDEX.md` has Etingof–Ostrik on semisimplification and
fusion categories but **not** the 2004 module-category paper, and no Bichon;
`library/*/sections/` and `library/*/ocr/` no hit for Bichon or `B(E)`. So the
classification is **not held** in the library and is cited from the literature
with the verification caveat above. The *question* it answers is held in five
audit docs and the cheat sheet (list in `qou-yjwg`).
