# §4-A asks a symmetric-theory question of a non-symmetric category

**Bean:** `qou-tzfm`. **Date:** 2026-08-25. **Status:** finding, two tiers —
read the tier split in §3 before citing this.

## The claim

The eightfold surface's one surviving question is
[recorded](2026-08-07-eightfold-live-surface-collapse.md) as:

> Does QOU's braided category admit inequivalent fibre functors? Equivalently:
> is `H¹(base, Aut^⊗)` non-trivial, and can the resulting gerbe's band be
> `SU(3)`?

**The second sentence is not equivalent to the first for QOU's category, and the
machinery it names is the symmetric theory.** QOU's category is non-symmetric by
its own definition. So the question as posed is not open-or-closed — it is
mis-posed, and re-posing it changes what an agent should go and read.

This does **not** re-open any excluded route, and it is **not** an exclusion.
See §4.

## 1. QOU is non-symmetric, by its own definition

Not an inference — the corpus says it in as many words:

- [`qou-definition-intro.md`](../content/quantum-observable-universe/quantum-observable-universes/qou-definition-intro.md):
  *"the **non-symmetric braiding** provides a canonical well-ordering on the
  Hecke basis, identifying the categorical arrow of time."*
- [`quantum-observable-universe.md`](../content/quantum-observable-universe/quantum-observable-universes/quantum-observable-universe.md):
  *"A quantum universe is thus braided; a quantum observable universe is braided
  and rigid."*

The non-symmetry is not incidental. It is load-bearing: it is what the arrow of
time is derived from.

## 2. The band machinery is the symmetric theory

Newly ingested this session (`qou-tzfm`), and all three agree:

| source | the hypothesis it works under |
|---|---|
| Tonini, *Stacks of Fiber Functors* (`arxiv-2010.12445v1` §1) | defines the relevant monoidal structure as *"**symmetric or commutative** if for all `V, W ∈ C` the following diagram is commutative"* |
| Tonini, *Sheafification Functors* (`arxiv-1409.4073v1` §2) | the same definition, verbatim |
| Nuiten–Toën, *Θ-Categories and Tannakian Duality* (`arxiv-2508.03145v1`) | *"a notion of Tannakian ∞-category solely based on **symmetric** monoidal ∞-categories"* |

Tonini's statement of classical non-neutral duality is what §4-A is reaching
for: for a `k`-Tannakian `C`, the fibered category
`Π_C(A) = {k-linear, strong monoidal, exact functors C → Vect(A)}` is an
**affine gerbe**, and `C ≃ Vect(Π_C)`. That is the theorem that makes "band"
and "`H¹`" mean what §4-A wants them to mean — and it is stated for Tannakian,
i.e. symmetric, `C`.

The general non-symmetric case is the fourth paper, and its output is a
different kind of object: Lentner–Mombelli (`arxiv-2311.14221v2`) reconstruct a
**Hopf algebra `H ∈ C`** — a Hopf algebra *in a braided category*, via a
relative coend `C(F) = ∮^{B∈B} F(B) ⊗ *F(B)` — not a group scheme with a band.

## 3. The two tiers — cite them differently

**Tier 1, established from the shelf and citable now.** The affine-gerbe/band
formulation is developed under an explicit symmetric hypothesis in all three
sources above; QOU is explicitly non-symmetric; the general reconstruction
target in the non-symmetric case is a Hopf algebra in `C`. Each of these is a
quotation, given above.

**Tier 2, standard but NOT yet discharged against a source in this corpus.** The
step that would turn Tier 1 into a conclusion about `Aut^⊗`:

> An affine group scheme is `Spec` of a **commutative** Hopf algebra. The coend
> Hopf algebra of a fibre functor is commutative iff the category is symmetric.
> Hence for non-symmetric `C` there is no classical band, and `Aut^⊗(τ)` — which
> is still a perfectly good affine group scheme — classifies only a symmetric
> shadow of `C`, not `C`.

I believe this is standard (Deligne–Milne; Ulbrich; Schauenburg), but **I have
not cited a line for it from the ingested sections**, and it is doing real work,
so it is flagged rather than asserted. Discharging it is the next task
(`arxiv-2311.14221v2` §6.3–6.4 is the place, and Schauenburg92 is in its
reference list).

## 4. What follows, and what does not

**If Tier 2 holds**, then `thm:su2-emergence`'s `Aut^⊗(τ) = SU(2)` is not a
constraint that `SU(3)` must contradict — the two live in different places.
Colour `SU(3)`, if the framework has it at all, would have to appear in the
**reconstructed Hopf algebra**, which `Aut^⊗` does not see. The search has been
aimed at an invariant that cannot carry the answer either way.

**What this does not do:**

- **Not an exclusion.** Nothing here says `SU(3)` cannot be found. It says
  `H¹(base, Aut^⊗)` is the wrong place to look for it. Per AGENTS.md
  §"Before declaring refuted", a re-posing is neither scope-(a) nor scope-(b);
  it is a statement about the question.
- **Not a re-opening.** The seven §4-A exclusions are
  [separately provenance-audited](2026-08-25-n3-exclusion-provenance-audit.md)
  and hold. In particular the `Sym²`-gate argument is about summands of tensor
  powers of the 2-dimensional fibre and is untouched by anything here.
- **Does not license the `ℤ/2` coincidence.** §4-A flags that `Out(SU(3))` and
  the framework's bar involution are both `ℤ/2` and says **do not wire it**.
  Nothing above depends on it.

## 5. Next

1. **Discharge Tier 2** against `arxiv-2311.14221v2` §6.3–6.4. Cheap, and it
   decides whether §1–2 amount to a re-posing or merely a caution.
2. If it holds, **re-pose §4-A in the cheat sheet** as: *what is the
   reconstructed Hopf algebra `H = End^⊗(τ)` of a QOU, and does it contain an
   `SU(3)`-like sub-object?* — and record that `H¹(base, Aut^⊗)` was the wrong
   invariant, with this file as the reason.
3. `arxiv-2607.10525v1` §"fiber functors on gaugings" is where a group action
   enters a finite tensor category, which is the nearest thing on the shelf to
   "impose a symmetry and see what fibre functors survive".
