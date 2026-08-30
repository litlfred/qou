# §4-A asks a symmetric-theory question of a non-symmetric category

**Bean:** `qou-tzfm`. **Date:** 2026-08-25. **Status:** finding. The tier split in §3 was
sharpened after a better citation turned up; read §3 before citing this.

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

## 1. QOU is non-symmetric — now proved, not just asserted

The corpus already said so in prose:

- [`qou-definition-intro.md`](../content/quantum-observable-universe/quantum-observable-universes/qou-definition-intro.md):
  *"the **non-symmetric braiding** provides a canonical well-ordering on the
  Hecke basis, identifying the categorical arrow of time."*
- [`quantum-observable-universe.md`](../content/quantum-observable-universe/quantum-observable-universes/quantum-observable-universe.md):
  *"A quantum universe is thus braided; a quantum observable universe is braided
  and rigid."*

The non-symmetry is not incidental. It is load-bearing: it is what the arrow of
time is derived from.

**As of this branch it is also a theorem**, which matters because the whole
argument below turns on it. Prose can be revised; a proof cannot be revised by
inattention.

| declaration | statement |
|---|---|
| `QOU.Eightfold.HeckeBraidingNonSymmetric.hecke_rel_iff_factored` | the AGENTS.md §7a convention `(σ − q)(σ + q⁻¹) = 0` and the quadratic `σ² = (q − q⁻¹)σ + 1` are the same relation (needs `q ≠ 0`) |
| `QOU.Eightfold.HeckeBraidingNonSymmetric.double_braiding_eq_one_iff` | **the gate** — an element satisfying the Hecke relation has `σ² = 1` **iff** `q² = 1`. Both directions, so it is not a one-sided bound |
| `QOU.Archimedean.HeckeBraidingSubstrateNonSymmetric.q_gt_one_double_braiding_ne_one` | at any real `q > 1` the double braiding is not the identity |

Symmetry of a braiding is triviality of the double braiding. So the substrate's
non-symmetry is **forced** by the Hecke relation together with `q₀ ≈ 1.10998 > 1`
— it is a consequence, not a stipulation, and it would fail only at `q² = 1`.

Verified `lean`-direct against the real Mathlib import cone, exit 0 on both
files, zero `sorry`, and `#print axioms` on all three declarations gives only
`propext`, `Classical.choice`, `Quot.sound`. Split across two files per §7c —
the gate is wall-side over a generic field and mentions no ordering; `ℝ` enters
only in the archimedean file.

**Scope, stated plainly.** These theorems are about an element `σ` of an algebra
satisfying the Hecke relation. That the QOU braiding *is* such a `σ` is the
corpus's Hecke–Skein convention (AGENTS.md §7a), consumed as a hypothesis and
**not** established here. And nothing in them excludes `SU(3)` from the
framework — they establish the hypothesis under which the symmetric machinery
does not apply, and stop there.

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

**Tier 2, now largely discharged — and the argument no longer needs the step I
originally flagged.** The first draft of this file leaned on *"an affine group
scheme is `Spec` of a commutative Hopf algebra, and the coend Hopf algebra is
commutative iff the category is symmetric"*, marked as standard-but-uncited.
A better citation is on the shelf, and it makes that detour unnecessary.

Tonini (`arxiv-1409.4073v1`, Introduction) states the chain §4-A relies on, and
attributes both halves:

> *"If `G` is an affine group scheme over a field `k` ... if `F : Rep G_k →
> Vect_k` is the forgetful functor then **`G` is canonically isomorphic to the
> sheaf of automorphisms of `F`** (opportunely defined, see [DM82, Proposition
> 2.8]). More generally one can recover **the stack `BG` of `G`-torsors by
> looking at fiber functors** ... is an equivalence of categories (see [DM82,
> Theorem 3.2])."*

Both are theorems **about `Rep G_k`** — Deligne–Milne 2.8 and 3.2 — and
`Rep G_k` is symmetric. That is the whole of what is needed:

- *"`Aut^⊗` of the fibre functor is the band"* is the **conclusion** of a
  theorem whose **hypothesis** is that the category is `Rep G`.
- So reading `thm:su2-emergence`'s `Aut^⊗(τ) = SU(2)` as "the band is `SU(2)`,
  therefore not `SU(3)`" **assumes what §4-A is asking**. It is circular, not
  merely unlicensed.

What remains genuinely open, and is now a smaller question: what the
non-symmetric analogue of the band *is*, if anything. Lentner–Mombelli's answer
is the reconstructed Hopf algebra in `C` (their Theorem 4.3 and §6.4), which is
not a group scheme and carries no `H¹` classification of the classical shape.

## 4. What follows, and what does not

`thm:su2-emergence`'s `Aut^⊗(τ) = SU(2)` is not a
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

1. ~~Discharge Tier 2~~ — **done**, via Tonini's attribution to [DM82, 2.8/3.2]
   (§3). The re-posing stands without the commutativity detour.
2. **Re-pose §4-A in the cheat sheet** as: *what is the
   reconstructed Hopf algebra `H = End^⊗(τ)` of a QOU, and does it contain an
   `SU(3)`-like sub-object?* — and record that `H¹(base, Aut^⊗)` was the wrong
   invariant, with this file as the reason.
3. `arxiv-2607.10525v1` §"fiber functors on gaugings" is where a group action
   enters a finite tensor category, which is the nearest thing on the shelf to
   "impose a symmetry and see what fibre functors survive".
