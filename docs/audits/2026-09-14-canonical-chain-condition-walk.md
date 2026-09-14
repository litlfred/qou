# Walking the canonical chain: where do conditions emerge? (2026-09-14)

**Bean** `qou-u96j` · **Probe**
[`computations/audits/canonical_chain_condition_walk_probe.py`](../../computations/audits/canonical_chain_condition_walk_probe.py)
(5/5, exit 0)

## What this asks

[`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
states the chain as eleven steps from the substrate `q₀` to MeV observables, each
written as though its output follows from its input. This walk asks a different
question at each step: **what condition enters that the previous step does not
force?**

A condition being unstated is not the same as its being wrong. Everything below
is scope (a) — measured observations about what the corpus contains, with no
invariant excluding any reading. The reason to surface them anyway is that the
cheat sheet is, in its own words, "the PRIMARY coordination document for the
canonical chain": it is what agents reason from.

## 🛑 This is a PARTIAL walk

Measured here: **steps 5, 6 (partially) and 10**. Step 2's condition is already
documented in the cheat sheet itself and is cited, not re-derived.

**Not yet walked: steps 1, 3, 4, 7, 8, 9, 11.** Named so the gap is visible
rather than implied. Step 3 in particular is expected to carry one (the Markov
trace's "unique" is unique *given* a parameter `z`, which is the fork
`qou-99qc` / `qou-qqm4` have been carrying) but this walk did not establish it
from the corpus and so does not assert it.

---

## Step 2 — the geometry→algebra bridge (already documented)

The cheat sheet's own §2a records it, downgraded from "✅ proved" on 2026-08-25:
the curvature 2-form is **stipulated** to be the Hecke quadratic, so setting it
to zero recovers it tautologically, and `prop:hecke-spectral-sequence` has **0
`label:` declarations** in `content/`. Cited here for completeness of the walk;
nothing in this audit adds to it.

---

## Step 5 — Wedderburn + partitions

The step is stated as

> `H_n(q) ≅ ⊕_{λ ⊢ n} M_{d_λ}(ℚ(q))`;  `tr_M = Σ_λ y_λ χ^λ`

— a sum over **all** partitions of `n`.

> ### 🛑 Read §"Step 3" below before C5a — it corrects C5a's framing
>
> C5a as first written called the two-row cap *"a condition the chain's step
> statement does not carry"*, which reads as though it were a truncation bolted
> on at step 5. **It is not.** The cap is derived in the corpus from the step-1
> choice of the fibre `V`, and it is what *forces* the Markov parameter. What
> step 5's statement omits is the **hypothesis**, not the truncation. The
> measurement in C5a is correct; its emphasis was wrong.

### C5a — the sum runs over TWO-ROW partitions only

Measured against the committed `computations/y-lambda-at-q0.witness.json`
(anchor `proton`, `q₀ = 1.1099785827513808…`): at **every `n` from 2 to 12**,
every `y_λ` whose partition has **three or more rows is exactly 0**, and every
nonzero one has **at most two rows**. At `n = 12` that is 7 nonzero against 70
zero.

The production family is `y_lambda_su_n(n, q, 2)` — the trailing `2` is a row
cap. AGENTS.md does say "convention D = the two-row truncation", so the fact is
known; what is missing is that **the chain's own step statement does not carry
it**. An agent reading step 5 would expect a sum over all `p(n)` partitions.

### C5b — `α` is not an ad-hoc ratio; it is a Wenzl weight

`y_(3)` at `n = 3` equals `(q⁴+1)/(q²+1)²` **exactly** (agreement to 45 dps;
`|diff| = 5.0e-47`, at the witness's serialization floor).

That is the same `α` the 2026-09-08 `Q_β` ruling names as the
augmentation-to-`z_D` factor, and the same `α` that
`QOU/Hecke/MarkovCrossingReversal.lean` (#7334) found relating the two admissible
cells of the flavour split. It was the **trivial block's Wenzl weight** all
along. Two arcs that reached `α` independently were both reaching this.

### C5c — the normalisation is dimension-weighted

`Σ_λ d_λ · y_λ = 1` exactly at every `n` from 2 to 12. This is just `tr_M(1) = 1`
expanded, since `χ^λ(1) = d_λ`.

The **unweighted** `Σ_λ y_λ` is 1 only at `n = 2`, where every `d_λ` is 1, and
then falls away: 0.7527, 0.5666, 0.3804, … , 0.0133 at `n = 12`.

**Recorded because the author got it wrong first.** My initial reading of the
witness was the unweighted sum, from which I drew a false "the `y_λ` are not a
probability measure" conclusion. They are one, under the correct weighting. This
is also distinct from the `w_λ(q)` non-normalisation AGENTS.md's notation
register describes (0.987 / 0.982 / … at `n = 3/4/…`) — that is the **quantum
Plancherel** family, a different object with different numbers, and the register's
"never conflate the three weight families" rule is exactly what keeps them apart.

---

## Step 10 — the confinement SDP

### C10a — `n_target` carries three inequivalent production meanings

The spec block
[`mba-step10-confinement-sdp.md`](../../content/quantum-observable-universe/appendix-mass-binding-algorithms/mba-step10-confinement-sdp.md)
declares *"Target net constraint `n_target ∈ ℤ≥0`"* — an **integer**. Measured at
source, the three production callers pass three different kinds of thing, each
citing a different authority:

| caller | value | kind | cites |
|---|---|---|---|
| `aK_via_lp_dual_hecke_basis.py:175` | `n_target = tr_M_atom` | **real** — a Markov trace | `prop:mass-coefficient-shadow-price` |
| `pn_alpha_lp_dual.py:375` | `target_net = float(pn_vec.sum())` | **real**, and α-dependent | its own `net(pn_α)` |
| `option_b_proton_mass_full_chain.py:588` | `n_target = float(n_gg)` | **integer** — γγ insertions | "AGENTS.md §LP/SDP duals" |

Only the third matches the declared type. `n_target` is the constraint that
*selects* `T_w`, so this is the condition that emerges at step 10 — and the
corpus does not have one definition of it.

*In fairness:* `option_b_proton_mass_full_chain.py` says in its own comment that
its `t = [1,1,1]` and `G = identity` are a "minimal end-to-end demo — replace
with full Gram for real chain", so it should not be read as the production chain.

### C10b — the cheat sheet states an objective the code does not have

The cheat sheet's §1 diagram and §2 table both render step 10 as

> `min ‖tr_M(T_w) 𝔈₀ − B_tgt‖` over GB-NF

The authoritative algorithm block has **no `B_tgt`**:

```
minimize   Σ_i t_i x_i
subject to net(x) = n_target,  G x ≥ 0,  x ≥ 0
```

and the canonical entry point is
`pyhecke.lp_dual_solver.solve_operator_selection_lp(t, G, n_target)` — no
target-binding argument exists in the signature.

**This defect points the safe way** — the document makes the chain look *more*
fitted than the code is — but it is in the primary coordination document, and an
agent reading it would conclude step 10 minimises distance to a measured binding
energy, i.e. that the chain fits AME at its selection step. It does not.

---

---

## Step 3 — the "unique trace", and where the fork actually roots

This was the next item; walking it **closed the question, in the direction
opposite to what I expected**, and corrects C5a above.

`rem:markov-axioms-primitive` states it correctly: axioms 1–2 (normalisation +
cyclicity) with an unspecified stabilisation parameter admit a **one-parameter
family**. So the cheat sheet's step 3 — *"Unique trace `tr_M`"* — is the
compressed form, and `z` is where the condition would enter.

**But the parameter is then forced, and the forcing is sorry-free:**

```
V = fundamental of SU_q(2)      ← the HYPOTHESIS, and the only one
  ⟹ ℓ(λ) ≤ 2                     lem:feynman-eigenbasis-decomposition
  ⟹ y_(1³) = 0
  ⟹ [+ faithfulness y_(2,1) ≠ 0]  markovWeights_eq_jones_of_threeRow_eq_zero
  ⟹ y_(2,1) = 1/[2]_q², y_(3) = (q⁴+1)/(q²+1)² = α, z = q³/(q²+1) = z_D
```

Verified symbolically and against the committed witness: `y_(3)` and `y_(2,1)`
both reproduce to 30 dps. So **`α` is not merely observed to equal `y_(3)` — it
follows**, as `y_(3) = 1 − 2/[2]_q²`.

**The competing root `z = q` is `markovWeights_degenerate_root`**: `y = (1,0,0)`,
so `y_(2,1) = 0` and the trace is **not faithful** on `TL₃` (`z·[2]_q = q²+1 ≠ q²`).

### What that does to the fork

This is a **derivation-first discriminator** on the fork `qou-99qc` / `qou-qqm4`
have been carrying, and it uses **no residual at all** — exactly the ranking
AGENTS.md's anti-fit rule demands. And it points **away** from the augmentation,
which is the cell that reproduced the flavour-split baseline *exactly* in #7334.

**Recorded, not acted on.** Which cell to adopt remains the owner's call; what
changes is that the call is no longer between two equally-derived options.

### And a measurement note

`grep -c sorry` on `MarkovTraceTLUniqueness.lean` returns **1**, and that hit is
the word inside a **comment** (*"sorry-free, `lean`-direct exit 0"*). The file has
no `sorry` tactic. Counting the word is not counting the tactic — I raised a false
alarm on it before checking.

---

## What the walk has produced so far

- **Step 3 + step 5 reduce to ONE condition**, and it sits at **step 1**: the
  choice `V = fundamental of SU_q(2)`. Everything else — the row cap, `y_(1³) = 0`,
  `z_D`, `α` — is derived from it, sorry-free.
- **`α` is derived**, not coincidental: it is `y_(3) = 1 − 2/[2]_q²`.
- **The augmentation is proved degenerate**, which informs the open fork without
  using accuracy.
- **Step 10 carries a genuinely open condition** (`n_target`, three meanings) and
  **the cheat sheet misstates step 10's objective**.
- Two self-corrections: the dimension-weighted normalisation, and C5a's framing.

---

## Steps 1 and 4 — where `V` comes from, and the cycle at the root

Step 3 left everything hanging on `V = fundamental of SU_q(2)`, so this walks it.

**Step 1 does not choose `V`.** `prop:braid-action-tensor` reads *"For each object
`V` in `𝐂`"* — the construction is for an **arbitrary** object.

**Step 4 does.** `why-b3.md`:

> *"The Descartes condition `χ(A) = −6` **forces** the gauge group to be a quantum
> form of `SU(2)`, which has rank 1. Consequently, the fundamental representation
> `V` is 2-dimensional."*

So the dependency runs **step 4 → step 1**, against the direction the chain is
drawn. That alone is worth recording: the chain is a line and the dependency is not.

### The cycle, and only half of it is declared

`chi-minus-six-chain.md` is the block that fixes `χ(A) = −6`. Its **Step 1** reads:

> ***"Step 1: Start with the QOU triple.** We have `(𝐂, A, τ)` with gauge group
> `G = SU(2)`."*

and Step 2 uses `G = SU(2)` to get the rank-2 bundle that Riemann–Roch then turns
into `χ = 2 − 2g`.

So:

```
why-b3            :  χ = −6   FORCES   SU(2)  ⟹  dim V = 2
chi-minus-six-chain: STARTS FROM  G = SU(2),  uses it at step 2
```

**Read as derivations, those form a cycle.**

The block *does* declare a different circularity, in its own words:

> *"Step 5, which fixes the branch-point count at six, reads that count off the
> Weierstrass points of Bring's surface — the surface the chain then identifies at
> Step 7 — so **the chain locates the value rather than deriving it from the axioms
> alone**."*

That candour is to its credit. **The step-1 assumption is the one it does not
declare**, and it is the larger of the two, because `dim V = 2` is what everything
downstream — the row cap, `y_(1³) = 0`, `z_D`, `α`, the flavour split — rests on.

### 🛑 What this is and is not

**This is not a claim that the mathematics is wrong.** Each block is sound read as
a *consistency* statement: "given the QOU triple with `G = SU(2)`, `χ = −6`
follows", and "given `χ = −6`, `SU(2)` follows" are both fine. The measured fact is
that neither derives `SU(2)` from anything prior, and that the condition the whole
chain rests on is **assumed at step 1 of the chain presented as deriving it**.
Scope (a): an observation about the corpus's dependency structure.

**There is a candidate independent route.** `cohomological-embedding.md` §(iv):

> *"Genus 4 is forced. The QOU axioms require `T_{2,3}` and `T_{2,9}` to embed, but
> `T_{2,11}` must not. This uniquely forces `g = 4` and `χ = −6`."*

This does not visibly assume `SU(2)` — but it takes a **knot-embedding pattern** as
input, which relocates the condition rather than removing it. Whether that route is
genuinely independent is **not settled here**.

### A rank contradiction, in passing

- `why-b3.md`: `SU(2)` *"has **rank 1**"* — correct.
- `descartes-knot-eigenbasis-derivation.md`: `χ = −6` *"sets the genus `g = 4` and
  gauge group `SU_q(2)` to **rank 2**"*.

`SU(2)` has rank 1; **2 is `dim V`**, not the rank. One of the two states a wrong
rank as a derived consequence of `χ = −6`.

---

## Where the walk stands

The chain's conditions do not accumulate step by step — they **converge on one**:

```
χ = −6  ⇄  G = SU(2)  ⟹  dim V = 2  ⟹  ℓ(λ) ≤ 2  ⟹  y_(1³)=0  ⟹  z_D  ⟹  α
   ↑ cycle, half-declared        └──────── all of this is sorry-free ────────┘
```

Everything to the right of `dim V = 2` is **derived and sorry-free**. Everything to
the left is a cycle with one leg undeclared. Step 10's `n_target` is the one
*separate* open condition found.

**Next**, in priority order: (1) whether `cohomological-embedding`'s route is
genuinely independent of `SU(2)` — that is the question that would break the cycle;
(2) the rank contradiction, which is a one-line fix someone should own; (3) steps
7, 8, 9, 11, still unwalked.
