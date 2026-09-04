# The canonical binding path IS full-tower in n; the NF path is not — and the ruling has been applied to neither

**Date:** 2026-09-04
**Bean:** `qou-hu1f`
**Status:** observation + measurement. No claim is closed here.

**🛑 This file's first revision, pushed and then corrected the same day, claimed
the canonical binding path is H₃ as well. That is false — measured, it sums over
all `p(3A)` partitions. The correction and the trap that produced it are in
§"CORRECTION" below, kept rather than quietly edited away.**

## The two things

**1. The owner ruled, 2026-09-03 (verbatim, from chat):**

> *"The QOU should be on the full tower in the derivations to the standard model —
> should make use of the full tower even though what is observable is only order
> zero."*

Confirmed the same day to mean **both** senses: all `n` of the Hecke tower, and
all orders in `q`. Recorded in
[`2026-09-03-sm-26-term-status.md` §10](2026-09-03-sm-26-term-status.md).

**2. Bean `qou-tower` measured that the mass/binding surface has no tower in it.**
`build_atom_nf_mp` applies the H₃ Gröbner–Shirshov reduction after every crossing,
so the state is a 6-vector at every step of every nucleus.

## What is unconnected

§10 applies the ruling to the **standard-model** surface — §§2–7 of that audit,
the `Q`/`T₃`/eightfold/`α_EM` attacks — and concludes every one of them is
order-zero-only bar two. It does not mention mass, binding, or the nuclear chain.

And the collapse finding has **no durable home at all**: `build_atom_nf_mp`
appears in **zero** files under `docs/` or `content/`. It lives in one bean and
five probes. So the ruling has never been put to the surface where a hard
measurement already says the tower is gone.

## Re-measured here, independently of the bean

A bean is not a primary source (AGENTS.md says so explicitly, and says it about
beans written by other agents that look authoritative because they are specific
and recent). Re-run directly against `compound_shift_nf.build_atom_nf_mp`:

| nucleus | nominal strands `n = 3A` | NF state components |
|---|---|---|
| hydrogen, A=1 | 3 | **6** |
| ⁴He, A=4 | 12 | **6** |
| ¹⁶O, A=16 | **48** | **6** |

¹⁶O is a case the bean did not test and is the sharpest: a nominal `H₄₈` object
carried as six numbers. The claim reproduces.

## 🛑 CORRECTION, same day, to the central claim of this audit

**An earlier revision of this file said the canonical path is H₃ too — "the
tower is never built". That is FALSE, and it was the more important half of what
this audit claimed.**

`binding_canonical`'s **default** path (`use_transfer=True`) is the fine-Bratteli
transfer matrix, and it sums the Frobenius pairing over **every partition of
`3A`**. Measured, not read:

| nucleus | `n = 3A` | `n_partitions` reported | `p(3A)` |
|---|---|---|---|
| ²H | 6 | **11** | 11 |
| ³He | 9 | **30** | 30 |
| ⁴He | 12 | **77** | 77 |

Exact agreement at every level. **The canonical binding path is a full-tower
object in the `n` sense**, and satisfies that half of the ruling already.

**How the error was made, since it is a reusable trap.** I cited
`binding_canonical.py:37` (`tower_binding_full (H_3 tower)`), `:324` ("the H₃
building blocks `tr_M³(p)`, `tr_M³(n)`") and `:341` (the Wenzl bridge at H₃).
Those lines are real — but **:324 and :341 sit inside the `use_closed_form=True`
branch**, a non-default alternative retained for a specific caller family. I read
three grep hits naming H₃ and inferred the default from them without checking
which branch they were in. A grep hit inside a non-taken branch is not evidence
about the path that runs.

## What is actually true, restated

There are **two different objects**, and the interesting fact is that they
disagree in structure:

- **Canonical route** (`binding_canonical`, transfer path) — sums `Σ_{λ ⊢ 3A}
  y_λ χ^λ` over all `p(3A)` partitions. **Full tower in `n`.**
- **NF route** (`build_atom_nf_mp`) — reduces to a 6-vector after every
  crossing, at every `A`. **No tower at all.**

The NF route has seven consumers: five probes, plus
`all_nuclides_sdp_admissibility_mp.py` (a producer with a committed witness) and
`qbeta_level_k_binding_operator_probe`. The canonical mass path is not among
them.

So the live question is **not** "does the mass surface honour the ruling" — in
the `n` sense the canonical one does. It is narrower and sharper:

**do the two routes agree?** `qou-tower` measured that a genuine full-tower walk
shows no shell structure, and concluded the degree of freedom is absent from the
construction. That conclusion was drawn from the NF route's collapse. But the
canonical route never had that collapse, so the argument does not transfer to it,
and any probe reasoning from `build_atom_nf_mp` to a statement about *the
framework's* binding is reasoning about the wrong object.

## What this does NOT establish

- **Not a defect.** Neither route is wrong; both are what the corpus says they
  are. This is a statement about what the ruling asks for versus what exists.
- **Not "the ruling is unsatisfiable here".** `qou-tower` ran a genuine
  full-tower walk (no per-step reduction, generators at true strand positions)
  at A = 2, 3, 4 exhaustively. It is *reachable* to A=4; it showed no shell
  structure; A=5 needs `max_λ d_λ²` = 686 GB and is out. So the honest statement
  is that the full tower is computable exactly up to ⁴He and returns a negative
  there — not that it cannot be done.
- **Not a claim about the SM surface.** §10 already covers that and its verdict
  stands.

## The question this leaves

Under the 2026-09-03 ruling, an order-zero-only construction's residual is not
evidence about the tower. Both mass/binding routes are order-zero in the `n`
sense — H₃ throughout. Whether that means the mass/binding results need the same
**tower status** line the SM per-term beans now carry (`qou-bsu0`) is a judgement
for the author, not something to assert here.

What is measurable, and is not yet measured: whether the A ≤ 4 full-tower walk
reproduces the canonical H₃ binding numbers. If it does, H₃ is a faithful
order-zero rendering and the ruling is satisfied in substance. If it does not,
the two routes disagree and that gap is the real finding. `qou-tower`'s walk
measured *distributional* quantities (top-block share, participation,
argmax partition) against magic numbers — it never compared a binding energy.
