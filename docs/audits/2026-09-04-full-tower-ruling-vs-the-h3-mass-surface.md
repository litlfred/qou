# The full-tower ruling has not been applied to the mass/binding surface — where the tower is already collapsed

**Date:** 2026-09-04
**Bean:** `qou-hu1f`
**Status:** observation + measurement. No claim is closed here; the point is that
a ruling and a measurement have not been put in the same room.

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

## Correcting the bean's scope while confirming its substance

`qou-tower` calls this "the production chain". Measured, `build_atom_nf_mp` has
**seven consumers**: five probes, plus `all_nuclides_sdp_admissibility_mp.py`
(a producer with a committed witness) and `qbeta_level_k_binding_operator_probe`.
It is **not** the canonical mass path — that is `canonical_mass.py`, per the
mass-formula guardrail.

**But the correction does not rescue the tower, because the canonical path is
H₃-based too, by a different mechanism.** `binding_canonical.py` describes its
own current path as `tower_binding_full (H_3 tower)` (:37), builds from "the H₃
building blocks `tr_M³(p)`, `tr_M³(n)`" (:324), and bridges "`tau_p`, `tau_n` via
the Wenzl bridge at H₃" (:341) — while carrying `n = 3 * (Z + N)` (:528) as the
nominal strand count.

So there are **two distinct routes to H₃**, and they should not be conflated:

- **NF route** (`build_atom_nf_mp`): a growing word is *reduced* to 6 dimensions
  after every crossing. The tower is built and destroyed.
- **Canonical route** (`binding_canonical`): per-nucleon H₃ traces are
  *composed*. The tower is never built.

The bean measures the first. The second is not a reduction at all and is
untouched by its argument — but it is equally not a full-tower derivation.

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
