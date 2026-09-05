# Roast: the six attack routes, and a rank count that hits the two I ranked first

**2026-09-04.** Adversarial pass over epic `qou-2q85` (routes A–F for the
depth-0 → depth-2 gap). The headline is not that a route is expensive. It is
that **routes A and B share a premise the corpus's own dictionary appears to
refute on a rank count**, and I did not check it before recommending them.

---

## R1 — Route B has the arrow backwards

I recommended: *"build `ℋ_q^(1,K)`, then the shuffle squares it into
`ℋ_q^(2,K)` = volume."* That reads depth 2 as **a product of depth-1 things**.

The K-theory side of the corpus's own dictionary says the opposite. The
Bloch–Suslin complex is

```
    B(F)  --δ-->  Λ²F^×          δ[z] = z ∧ (1 − z)
```

and `K_3^ind` is captured by the **kernel** of `δ`, not by the image of a
product. So under `rem:k-theory-period-rosetta`'s matching — depth 1 ↔ `K_1(F) =
F^×`, depth 2 ↔ `K_3^ind(F) ⊗ ℚ` — the depth-2 object sits **over** `Λ²`(depth-1)
as a kernel. It is not manufactured by multiplying two depth-1 elements; the
multiplication is the map it is the kernel *of*, and it points the other way.

**Two further problems with "square it", both structural:**

* **`Λ²` is antisymmetric, so `x ∧ x = 0`.** Squaring a *single* depth-1 element
  gives zero on that side. What lands is `z ∧ (1−z)` — two **distinct** units.
  "Square a depth-1 object" is not merely hard, it is the one case that vanishes.
* **The ranks do not match, and not marginally.** For a number field `F` with
  `r₁` real and `r₂` complex places, Borel gives `rank(K_3^ind(F) ⊗ ℚ) = r₂` —
  **finite, and equal to 1 for an imaginary quadratic field** such as the
  `ℚ(z_K)` of a hyperbolic knot shape. Meanwhile `F^×` is infinite rank and so
  is `Λ²F^×`. A graded object whose degree-2 piece is the square of its degree-1
  piece cannot have a rank-1 degree-2 piece over an infinite-rank degree-1 piece.

**What this does and does not establish.** It does **not** prove route B fails:
the `ℋ_q` shuffle filtration and the K-theory weight tower are *different
structures*, and the rosetta matching them is explicitly *"an analogy that
becomes a theorem at low depth and a conjecture at high depth, not a fully-
established equivalence"*. What it establishes is that **the two cannot be
matched as graded algebras** — the shuffle's `n₁+n₂` additivity on `ℋ_q` and the
weight grading on `K_{2n−1}^ind` disagree at the first place one can check them.

So route B's real content is not "build the object and square it". It is:
**which of the two structures is the depth axis actually indexed by?** That is
now the first question, and it is cheaper than any construction.

## R2 — Route A inherits the same premise, more weakly

Route A uses the coproduct's `2 = 2+0` split rather than the product, so it does
not need depth 1 and does not square anything. **It survives R1.** But it still
assumes `Δ_q`'s depth-splitting is the same grading the volume lives in — the
same identification R1 finds unsupported. The difference is that A can be tested
without committing to it: the compatibility check *"does a `bowtie_K` action on
`ℋ_q^(2,K)` commute with `tr_M`?"* is a statement about objects that exist,
whatever the grading turns out to mean.

**A is now the correctly-ranked first move**, and for a reason I did not give
when I ranked it second: it is the only route that is *agnostic* about the
question R1 opens.

## R3 — Route E is the only route targeting the actual goal

Routes A, B and D all target **volume**. The epic sits under `qou-8lxd`,
*"eightfold way / SM derived from QOU"*, whose goal is **flavour**. Bean
`qou-52fu` already established that the volume route cannot get there: the
complement's hyperbolic holonomy is `ρ : π₁ → PSL(2,ℂ)`, **rank 1**, more SL(2)
rather than SU(3).

So four of six routes are working a sub-goal, and only **E** (PGL(3) /
Fock–Goncharov) attacks what the epic is named for. That is a defensible
division of labour — volume feeds mass and binding, which are real targets — but
it should be stated, and the epic's framing did not state it. **Corrected in
`qou-2q85`.**

## R4 — What I got right, stated so the roast is not uniformly negative

* **Route C is genuinely dead** and the kill is solid: three inequivalent
  readings of `J^•`, one provably zero, one excluded for every `n ≥ 2` with no
  re-indexing repairing it (`qou-wjbd`). That verdict is not mine and predates
  this session by three weeks.
* **Route D's exclusion is proved**, sorry-free, and its surviving form
  (creative telescoping) is correctly labelled a template rather than an answer.
* **Route F is cheap and correct** and has now absorbed the harder finding that
  filtration 3 has no well-defined object behind it, not merely an ambiguous
  name.

## R5 — Two collisions avoided this hour, and the rate is the finding

Checking for prior beans before filing, two near-misses:

* **`qou-ec5z`** is titled *"EPIC: (TAIL) depth-1 — ν_{n−1} carrier"*. Different
  depth-1 entirely — the ν tail carrier, not the bi-filtration stratum. Its body
  is empty, so only the title would have been read.
* **`Hadamard` matches 24 beans**, and **none** is the Hadamard product of
  sequences. All 24 are `HadamardFactorization`, the entire-function
  factorization theorem.

Both are the same failure class as the seven corrections already on PR #6584.
Recorded in the route beans so the next agent does not read either as prior work.

---

## Revised ranking

| | route | verdict after the roast |
|---|---|---|
| **A** | `2 = 2+0` coproduct split | **first** — the only route agnostic about R1 |
| **B** | build `ℋ_q^(1,K)` and square | **demoted** — settle R1 first; "square it" is the vanishing case |
| **C** | curvature-rank | dead |
| **D** | Hadamard / telescoping | template only, does not cross depth |
| **E** | PGL(3) / Fock–Goncharov | **the only route aimed at flavour** |
| **F** | notation drain | cheap, do it regardless |

**Recommendation, revised (my judgement):** settle **R1** — is the depth axis the
shuffle filtration on `ℋ_q`, or the K-theory weight tower? — before building
anything. It is a reading question over objects that already exist, it is
cheaper than any construction on the list, and both A and B change shape
depending on the answer.
