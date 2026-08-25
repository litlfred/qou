# Three different filtrations are called "the GB filtration", and two of them provably cannot do the job

Follow-on to [`2026-08-16-word-depth-vs-partition-depth-bridge-is-unstated`](2026-08-16-word-depth-vs-partition-depth-bridge-is-unstated.md)
(bean `wpdb`). That audit said the word-depth ↔ partition-depth identification is
*unstated*. Reading the proof block rather than only the statement changes the
finding: the identification is not merely unstated, it is stated **three
inequivalent ways** under one symbol `J^\bullet`, and two of the three are
excluded by proved invariants.

This document also **retracts one of my own claims and upgrades another**. Both
corrections are recorded in full below; the upgrade matters more than the
retraction.

## The three objects

| # | definition | where | status |
|---|---|---|---|
| **1** | *"$J^\ell(q)$ collects elements requiring at least $\ell$ applications of $R_H, R_{YB}$ to reach normal form"* | [`prf:curvature-rank-gb-stratification`](../../content/quantum-observable-universe/mass-theory/curvature-rank-gb-stratification-proof.md) Step 2, first sentence | not obviously well defined — see §3 |
| **2** | *"Equivalently, $J^\ell$ is the image of $I^\ell$ (the $\ell$-th power of the rewrite ideal) under the quotient map"* | same sentence, `curvature-rank-gb-stratification-proof.md` Step 2 | **provably `⊥` for every `ℓ ≥ 1`** |
| **3** | *"$F_\ell$ is the span of basis elements $T_w$ with $\ell(w) \leq \ell$"* | [`alg:mba-step07-gb-filtration`](../../content/quantum-observable-universe/appendix-mass-binding-algorithms/mba-step07-gb-filtration.md) | well defined; **fails the dimension count at `n ≤ 3`** |

Step 2 asserts 1 and 2 are equivalent. They are not. And 3 is a third object
again — a filtration by Coxeter length, which is neither a rewrite count nor an
ideal power.

## 1. Object 2 is zero — and this is the claim my own Lean already refutes

`H_n(R, q) = R\langle\sigma\rangle / I`. For the quotient map `π`,

$$\pi(I) = 0 \quad\Longrightarrow\quad \bigl(\pi(I)\bigr)^{\ell} = 0 \ \ (\ell \geq 1),$$

and `Ideal.map π (I^ℓ) = (Ideal.map π I)^ℓ`, so **`J^ℓ = ⊥` for every `ℓ ≥ 1`**.
The filtration has two strata: everything in degree `0`, nothing above.

Formalised sorry-free and axiom-clean in
[`QOU/BraidKnot/WordFiltrationObstruction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WordFiltrationObstruction.lean)
— `map_defining_ideal_eq_bot`, `map_pow_eq_bot`, `graded_piece_trivial` — with
the incompatibility against the partition side supplied by `gbDepth_ne_on_H4`
(`gbDepth [4] = 4 ≠ 3 = gbDepth [2,2]`, so no one-stratum grading can be
`gbDepth`).

> ### 🔺 Correction — I under-claimed this yesterday
>
> That file was written and merged describing object 2 as *"the tempting
> reading"* and *"the one reading that would make them relate for free"* — i.e.
> a hypothetical nobody had written down. **That framing is wrong, and too
> generous.** Step 2 of the proof of the very proposition asserts object 2
> outright, as an "equivalently". I had read the statement block and not the
> proof block.
>
> So the Lean does not rule out a reading I invented as a strawman. It refutes a
> clause the corpus actually asserts. Correcting an under-claim upward is the
> same duty as correcting an over-claim downward, and this is the more
> consequential direction: a reader of that file would have concluded the
> obstruction was hypothetical.

**Scope-(b), proved.** A named invariant (`π(I) = 0`) forbids the construction,
so this is a structural exclusion, not a failed probe.

**What is *not* excluded.** Object 1 — the rewrite-depth reading, Step 2's first
sentence — is untouched. Step 2's *conclusion* may well be recoverable from it
alone. What is dead is the equivalence, and therefore Step 3 **as written**,
since Step 3 chains through both ("*Combined with Step 2, $F^{r}(T_w) \in J^r$*").
Nothing here bears on the proposition's statement, on `prop:gb-spectral-sequence`,
or on any mass result.

## 2. Object 3 is well defined — and fails a dimension count at `n ≤ 3`

> ### 🔻 Retraction — my "probably not well defined" was wrong for this object
>
> In [PR #5205](https://github.com/litlfred/qou/pull/5205) and in bean `wpdb` I
> wrote that the sharper open question was whether `r(T_w)` is well defined on
> the quotient at all — *"a word is not an element of `H_n(q)`… on the face of
> it, it is not."*
>
> For object 3 that is simply wrong. `T_w` is the standard Hecke basis, indexed
> by `w ∈ S_n`, and `ℓ(w)` is the **Coxeter length** — a function on the group,
> independent of the choice of reduced word by Matsumoto's theorem. The
> filtration is perfectly well defined. Retracted.
>
> (The objection *does* still apply to object 1: "elements requiring at least
> `ℓ` applications" is a statement about a *word*, and the minimum over
> representing words is `0` for every element, since every element has a
> normal-form representative. So object 1 is either not defined on the quotient
> or is identically zero. That needs a chosen normal form as part of the data,
> not just a rank function.)

With `r = ℓ` pinned, the two sides become **countable**, and the comparison
needs no Hecke machinery at all.

Four blocks read `Z^{(k)}(A) = \mathrm{span}\{e_\lambda : \mathrm{gbDepth}(\lambda) = k\}`
off the stratification, whose stratum is `gr_r` of the filtration. On the
charitable reading — `Z^{(k)}` is the degree-`k` piece of the filtration
*induced on the centre*, `(Z \cap F_k)/(Z \cap F_{k-1})`, which injects into
`gr_k` — a necessary condition falls out:

$$\#\{\lambda \vdash n : \mathrm{gbDepth}(\lambda) = k\} \;\leq\; \#\{w \in S_n : \ell(w) = k\} \quad \text{for every } k.$$

The left side is a dimension because the `e_\lambda` are orthogonal idempotents,
hence independent; the right because the `T_w` are a basis. Both are integers.
`gbDepth(\lambda) = \lambda_1 + \lambda'_1 - 1` is proved sorry-free
(`QOU.BraidKnot.gbDepth_eq_corner`), so neither side rests on an assumption.

Measured by
[`curvature_rank_vs_gbdepth_dimension_count.py`](scripts/curvature_rank_vs_gbdepth_dimension_count.py):

| `n` | gbDepth distribution | length distribution | verdict |
|---|---|---|---|
| 2 | `{2: 2}` | `{0:1, 1:1}` | **fails** — needs `dim gr_2 ≥ 2`, `gr_2` is empty |
| 3 | `{3: 3}` | `{0:1, 1:2, 2:2, 3:1}` | **fails** — needs `dim gr_3 ≥ 3`, `dim gr_3 = 1` |
| 4 | `{3:1, 4:4}` | `{…, 3:6, 4:5, …}` | holds |
| 5–7 | — | — | holds |

**The failure is exactly at `n ≤ 3`, and `n = 3` is the single-nucleon case** —
`H_3` is where `m_p` and `m_n` live. `gbDepth` is constant (`= 3`) on all three
partitions of `3`, so the reading needs a `3`-dimensional `gr_3`; but only the
longest element of `S_3` has length `3`, so `gr_3` is a line.

**Scope-(b) where it fails.** A subspace cannot exceed the dimension of its
ambient space, so this is a proved exclusion of the charitable reading — not a
failed probe. It holds from `n = 4` up, so it is not an exclusion of the
identification in general.

## 2b. `T_w` is also used two ways, and object 1 needs the second

Observation, **not** a proved defect — flagged because it decides whether the
one surviving object is viable, and it is cheap for the author to settle.

The symbol `T_w` carries two incompatible jobs in the same proof:

- **(a) a basis element indexed by `w ∈ S_n`.** This is what `mba-step07`'s
  `span\{T_w : \ell(w) \leq \ell\}` requires — `\ell(w)` is a function of a group
  element, so `w` must range over `S_n`.
- **(b) an arbitrary free-algebra word.** This is what Step 2 requires:
  *"Writing any `T_w` as a free-algebra word, the GB rewriting algorithm reduces
  `T_w` to normal form."* Something already in normal form is not reduced *to*
  normal form.

Object 1 — rewrite depth — is non-trivial only under reading (b). Under (a) it
is **identically zero**, because Step 2's own first sentence says the Bergman
normal-form theorem *gives the basis*: a basis element is a normal-form word, so
it needs `0` rewrites, so `r(T_w) = 0` for every `w` and
`\{T_w : r(T_w) = r\}` is the whole basis at `r = 0` and empty above.

So the survivor survives only on reading (b) — under which `w` is not a group
element and `\ell(w)` is not defined, which is object 3's requirement. **The two
readings needed to make objects 1 and 3 each non-degenerate are mutually
exclusive.**

I have not proved this, because "the `T_w` are the normal-form basis" is read off
prose rather than a definition — `def:hecke-normal-form` would have to be checked
against both uses to settle it. It is stated here as the question a repair has to
answer, not as a result.

## 3. The dilemma the four blocks are in

Either

- **(i)** the identification is meant as compatibility with the length
  filtration — and it is excluded at `n ≤ 3` by §2, precisely where the
  single-nucleon results are; or
- **(ii)** `Z^{(k)}` is merely a *labelling* of the centre by `gbDepth`, with no
  claim of compatibility — in which case the citation to
  `prop:curvature-rank-gb-stratification` is doing no work at all, which is the
  original `wpdb` finding.

There is no third branch on which the citation both means something and
survives. That is a stronger statement than "the bridge is unstated", and it is
what changes between the previous audit and this one.

## What is NOT claimed

- **Not** that the mass results are wrong. Every count here is about which
  *filtration* can carry a labelling; none of it evaluates a mass.
- **Not** that `prop:curvature-rank-gb-stratification` is false. Its statement is
  untouched; what is refuted is one clause of its proof (object 2) and one
  reading of its downstream use (object 3 at `n ≤ 3`).
- **Not** that `prop:gb-spectral-sequence` or the `E_2`-collapse claim is
  affected. Neither was examined.
- **Not** that object 1 is refuted. It is the one survivor, and its own
  well-definedness is the open question.

## The repair, and why it is not cosmetic

Give `J^\bullet` **one** definition and say which. If it is object 1, the chosen
normal form has to become part of the data and `r` has to be shown constant on
fibres. If it is object 3, the `n ≤ 3` failure has to be confronted — and that
is the case the physics uses. Deleting the "equivalently" clause in Step 2 is
necessary either way, since it is false, but on its own it repairs nothing: the
three-way ambiguity is what let a provably-zero object sit unnoticed inside a
load-bearing proof.

## Search performed

Corpus-grep checklist, all four paths, plus a Lean pass:

1. **`docs/audits/`** — the predecessor audit; nothing defining `J^\bullet`.
2. **`content/`** — the three definitions tabulated above; no fourth, and no
   block reconciling them.
3. **`computations/`** — `gb_depth_period_bring_fig8.py` attributes the
   partition depth to the word proposition while *itself* flagging the
   relationship as open; `gb_filtration_jet_tracker.py` is the object-3 producer.
4. **`docs/coordination/`** — no ledger entry.
5. **Lean** — no declaration mentions both a partition-indexed depth and a
   curvature-rank / `J^r` object.
