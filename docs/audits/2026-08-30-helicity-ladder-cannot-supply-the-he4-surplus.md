# The helicity ladder cannot supply the ⁴He ≥3-body surplus — both rungs are already closed

**Date:** 2026-08-30 · **Beans:** `qou-brng` (the self-vs-mutual route), coordinates with
`qou-vibo` / `qou-klgu` (GAP-2) · **Tier:** scope-**(b)** structural exclusion, two cited
invariants + one cited literature equivalence · **Compute:** none — this is a formalize-first
prune, deliberately run *before* a tranche rather than after. No fit, no wiring, no number
changed.

## Why this was written

The 2026-08-30 corpus-grep of the `qou-brng` "linking vs self-energy" route left **one** live
angle: a **helicity** assembly — Moffatt & Ricca's self/mutual split for the pairwise part, plus
**third-order helicity** for the ≥3-body part that both corpus assemblies provably lack. It looked
attractive because it is *citation-backed rather than re-derived*: the framework already holds
Moffatt & Ricca 1992 and the third-order-helicity literature.

**It does not survive.** Both rungs of the helicity ladder are closed, by two *different*
already-established obstructions. Recording it here so the next agent does not spend the tranche.

## Rung 2 — second-order helicity is bilinear, so it is intrinsically ≤ 2-body

Helicity is the quadratic functional `H = ∫ A·B`. Decomposing the field into flux tubes
`B = Σᵢ Bᵢ` gives, by bilinearity and nothing else,

```
H  =  Σᵢ Lkᵢ Φᵢ²          (self / Călugăreanu, Lk = Wr + Tw)
   +  2 Σ_{i<j} lk_ij Φᵢ Φⱼ   (mutual)
```

with **no term coupling three or more tubes** — not as a modelling choice but because a bilinear
form on `Σ Bᵢ` expands into exactly the diagonal and the pairs. That is the whole content of the
"self vs mutual" split `qou-brng` asks about, and it is the reason the split cannot answer the
question it was recruited for.

Binding is measured relative to free nucleons, so the 1-body self terms drop out of `B(K)`, and the
mutual part is exactly a per-pair function — the shape

```lean
ofBondFunctional (f : R → R) (μ : Fin 4 → Fin 4 → R)
```

of [`QOU/Mass/PairwiseCumulantVanishing.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/PairwiseCumulantVanishing.lean).
`b3_eq_zero_ofBondFunctional` (sorry-free) forces `b₃ = 0` for **every** `f` — the theorem
quantifies over `f` with **no hypothesis** (not continuity, not positivity) and indexes `μ` by the
**pair**, so bond-*dependent* amplitudes are covered too, not merely a uniform `ε`. With
`b3 i j k := triple i j k − (pair i j + pair i k + pair j k)` and AME2020 giving
**`b₃ = +1.426222 MeV ≠ 0`**, `not_isPairwise_of_b3_ne_zero` closes it.

**⇒ Second-order helicity cannot be the complete binding, for the same reason no bond-sum can.**

## Rung 3 — third-order helicity IS the Milnor μ̄ route, in different notation

The natural repair is to climb to third-order helicity, which is genuinely 3-body. But it is not an
independent object. Komendarczyk, *On the third order helicity of magnetic fields on invariant
domains in S³* (arXiv:0808.1533v3, held at `library/arxiv-0808.1533v3/`), §"Comparison to the known
approaches via Massey products", verbatim:

> "In several prior works […] helicities were developed via th e Massey product formula for ¯µ123.
> These approaches are **equivalent** to the one presented here in th e sense that invariants
> obtained this way **measure the same topological informat ion**."

and Berger's standard third-order formula is stated there **"in the case of Borromean flux tubes"** —
i.e. on the vanishing-pairwise-linking locus, which is exactly where a Massey triple product is
defined.

That is fatal here, because the ⁴He configuration is the opposite case. From
[`2026-08-29-gap2-he4-milnor-indeterminacy-exclusion.md`](2026-08-29-gap2-he4-milnor-indeterminacy-exclusion.md)
(bean `qou-klgu`, scope-(b)): ⁴He is the **max-contact tetrahedron `K₄`**, every one of the
`C(4,2) = 6` pairs bonded with `lk = 1`; Milnor's `μ̄` is defined only modulo the gcd of the lower
invariants, so the modulus is `gcd(lk) = 1` and every higher `μ̄` lives in `ℤ/1 = 0` — **no
invariant content beyond the pairwise bonds.**

Since third-order helicity measures *the same topological information* as `μ̄₁₂₃`, it inherits that
indeterminacy exactly. **⇒ Third-order helicity is `ℤ/1 = 0` on ⁴He too.**

## Verdict

**The helicity ladder is not a second route to the ⁴He surplus.** At rung 2 it is the
pairwise-excluded route; at rung 3 it is the μ̄ route wearing different notation. The two rungs fail
for *different* proved reasons, which is what makes the exclusion structural rather than a magnitude
miss:

| rung | object | why it cannot supply the ⁴He ≥3-body surplus |
|---|---|---|
| 2nd order | `H = ∫A·B`, self + mutual | **bilinear ⇒ intrinsically ≤ 2-body**; `b3_eq_zero_ofBondFunctional` forces `b₃ = 0` vs AME `+1.426222` |
| 3rd order | Massey / Berger `M₁₂₃` | **= μ̄₁₂₃'s information** (Komendarczyk §8); on `K₄` all `lk = 1` ⇒ `gcd = 1` ⇒ `ℤ/1 = 0` (`qou-klgu`) |

## Scope — what this does NOT exclude

Stated explicitly, per the "(a) vs (b)" discipline. This is scope-**(b)** *for the max-contact,
all-`lk = 1` configuration* (tightly-bound ⁴He), on two cited invariants plus a cited equivalence.
It does **not** exclude:

- **Helicity on loosely-bound, low-`lk` configurations.** The triton's single triple is genuinely
  Borromean (`lk = 0`, `μ̄₁₂₃ = +1`), so third-order helicity is well-defined there — it simply
  returns what `μ̄` already returns, adding no new content rather than being wrong.
- **`Lk = Wr + Tw` as geometry.** The Călugăreanu decomposition carries real information at fixed
  `Lk` (Moffatt & Ricca 1992, `library/procrsoclondona92/`). But it is **self**-linking — 1-body
  data — so it cannot contribute to `b₃` whatever its geometric content.
- **The surplus itself.** `qou-klgu` already localizes it in a **non-link-invariant** object (the
  SU(4) `[1⁴]` shell), and nothing here touches that. The present result strengthens that
  localization: it is now excluded from the *entire* helicity/Massey/μ̄ family, not just from `μ̄`.

## Method note

This is a formalize-first prune in the sense of AGENTS.md §"Formalize-first probe discipline": the
hypothesis class was stated, the invariant that the whole class must satisfy was found, and the
class was excluded — **before** running the scan, not after. The cost was two greps and two reads;
the probe it replaces would have been a tranche.

It also depended on a library path that did not exist until today: Moffatt & Ricca is invisible to
the documented `library/*/sections/` grep (1,916 B of JSTOR banner vs 46,511 B in `ocr/`), which is
why the `ocr/` tier was added to the corpus-grep checklist in the same session (PR #6123).
