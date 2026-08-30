# Relevance triage — the nine gerbe / Tannakian uploads

**Beans:** `qou-tzfm` (the gap), `qou-bhfg` (the audit that found it).
**Date:** 2026-08-25. **Skill:** `local/paper-relevance-triage`.

## Why these arrived

Measured earlier this session: across `library/`'s 400 ingested documents,
`INDEX.md` returned **one** Tannakian hit and **zero** on gerbes, non-neutral
Tannakian categories, or inequivalent fibre functors. Meanwhile the entire
eightfold-way live surface has
[collapsed onto one question](2026-08-07-eightfold-live-surface-collapse.md):

> Does QOU's braided category admit inequivalent fibre functors? Equivalently:
> is `H¹(base, Aut^⊗)` non-trivial, and can the resulting gerbe's band be
> `SU(3)`?

An agent attacking that was deriving against an empty shelf. The owner uploaded
nine papers; all nine are on-topic, which is not the usual triage outcome.

## The nine

Stage A + B run on all nine — 334 pages, 117 sections, ~786k characters
greppable via corpus-grep path 5; 457 claim candidates, 318 flagged as
formalization candidates.

| doc-id | class | what it is | relevance |
|---|---|---|---|
| `arxiv-2010.12445v1` | math.AG | Tonini, *Stacks of Fiber Functors and Tannaka's Reconstruction* | **primary** — literally the object §4-A names |
| `arxiv-1409.4073v1` | math.AG | Tonini, *Sheafification Functors and Tannaka's Reconstruction* | **primary** — companion to the above |
| `arxiv-2311.14221v2` | math.QA | Lentner–Mombelli, *Fibre Functors and Reconstruction of Hopf Algebras* | **primary** — the *non-symmetric* reconstruction, which is QOU's actual case |
| `arxiv-2607.10525v1` | math.QA | Galindo–Gallego–Morales, *Fiber Functors of Equivariantizations of Finite Tensor Categories* | **primary** — fibre functors of a category carrying a group action |
| `arxiv-1103.4815v3` | math.DG | Nikolaus–Waldorf, *Four Equivalent Versions of Non-Abelian Gerbes* | **supporting** — the non-abelian gerbe / band vocabulary |
| `arxiv-2508.03145v1` | math.AG | Nuiten–Toën, *Θ-Categories and Tannakian Duality* | **supporting** — modern refinement of the duality statement |
| `arxiv-2601.07042v1` | math.NT | Bertoloni Meli–Dillery, *A Tannakian Description of the Local Kaletha Gerbe* | **supporting** — a worked *non-neutral* example |
| `arxiv-1901.08945v2` | math.AG | Bergh–Schnürer, *Decompositions of Derived Categories of Gerbes* | **background** — banded-gerbe decomposition |
| `arxiv-1211.1812v5` | math-ph | Vasselli, *Presheaves of Superselection Structures in Curved Spacetimes* | **background** — physics-side precedent for a non-trivial band |

## The lead this immediately produced — stated as a lead, not a result

Tonini's introduction states classical non-neutral Tannakian duality in the
form §4-A wants: for a `k`-Tannakian `C`, the fibered category

    Π_C(A) = { k-linear, strong monoidal, exact functors C → Vect(A) }

is an **affine gerbe**, and `C ≃ Vect(Π_C)`. So "inequivalent fibre functors"
is exactly "`Π_C` is non-neutral", and the band is `Aut^⊗` of any fibre functor.

Reading that against the framework's own definitions raises a sharp question:

1. **A QOU ships with a fibre functor.** `def:quantum-observable-universe`
   defines the object as a *triple* `(C, A, τ)` in which "the forgetful functor
   `τ` is faithful". A gerbe with a global section is **neutral**. So the
   neutralising section is not something to be searched for — it is part of the
   defining data.
2. **The band is then pinned, and the framework has already computed it.**
   `thm:su2-emergence` states `G = Aut^⊗(τ)` is *forced* to be `SU(2)` (or its
   split real form). A neutral gerbe is `B(Aut^⊗(τ))`.
3. **Inner forms preserve dimension.** `dim SU(2) = 3`, `dim SU(3) = 8`.

If all three transfer, the band cannot be `SU(3)` and §4-A's live question is
answered negatively — which the collapse audit itself says would be *"equally
valuable"*, since it would settle the corpus position that colour and flavour
`SU(3)` are **imported**.

### Why this is NOT written as an exclusion

Three premises are undischarged, and the first is the crux — it is precisely
why the non-symmetric papers above are the important ones:

- **QOU's category is braided and explicitly NOT symmetric.**
  `qou-definition-intro.md` says so in as many words: *"the non-symmetric
  braiding provides a canonical well-ordering on the Hecke basis"*. Classical
  Tannakian duality in the Deligne–Milne / Tonini form is the **symmetric**
  theory. So the affine-gerbe theorem quoted above is **not** the applicable
  one, and whether the band statement survives into the non-symmetric setting
  is exactly what `arxiv-2311.14221v2` and `arxiv-2607.10525v1` are for. It is
  not established here.
- **"base" is unspecified.** §4-A writes `H¹(base, Aut^⊗)` without fixing the
  base. The neutrality argument applies over the base on which `τ` is defined;
  if a different base is intended, it does not apply as stated.
- **The inner-form step imports the classical form theory** of affine group
  schemes, i.e. the same symmetric assumption again.

Per AGENTS.md §"Before declaring refuted", this is at most a **scope-(a)**
observation today — *"the classical symmetric route, on its own, cannot yield
band `SU(3)` for an object that ships with its own fibre functor"* — and it
becomes scope-(b) only if the non-symmetric reconstruction supports the same
band invariant. **Do not cite it as an exclusion**, and do not add a row to the
§4-A exclusion table on the strength of it.

There is also a coincidence worth naming before someone leans on it: §4-A
already flags that `Out(SU(3)) = ℤ/2` and the framework's bar involution are
*both* `ℤ/2`, and records **"do not wire it"**. Nothing above depends on that
coincidence, and nothing here licenses it.

## Next step, and it is a small one

The question is now well-posed enough to be decided by reading rather than by
searching: **does a fibre functor on a non-symmetric braided rigid category
pin a band invariant that inner twisting preserves?** `arxiv-2311.14221v2`
(Hopf-algebra reconstruction) is the paper that answers it, and
`arxiv-2607.10525v1` §"fiber functors on gaugings" is where a group action
enters. That is a reading task against a shelf that now exists, which is the
whole point of the intake.

## Ledger and references

Per `local/paper-relevance-triage`, metadata is born in
`content/schema/references.ts` and the judgement joins from
`content/bib-qa-verifications.json`. Both are follow-on work for this branch;
the extraction artefacts land first so the corpus-grep path is live
immediately.
