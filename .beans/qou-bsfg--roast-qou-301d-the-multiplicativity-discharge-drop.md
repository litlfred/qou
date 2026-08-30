---
# qou-bsfg
title: 'ROAST qou-301d: the multiplicativity discharge drops one loop factor, and its ''falsifiable content'' is x-x=0'
status: completed
type: task
priority: normal
created_at: 2026-08-30T13:46:58Z
updated_at: 2026-08-30T14:26:36Z
---

Red-team of `6033ea80f7` (`QOU.MathlibExt.MarkovTraceMultiplicative` + the
`ArchimedeanTraceBridge` capstone), which closed `qou-301d` as
*"multiplicativity DISCHARGED via route B"*.

**Credit first, because most of this is right.** Route-B scoping (algebraic
Ocneanu trace, no link diagrams) was the correct call and matches `qou-dyij`'s own
roast. Generic `CommRing`, no QOU dependency, genuinely Mathlib-upstreamable.
Sorry-free, axioms clean. And the file's §Scope paragraph is *honest*: it says in
so many words that `IsJuxtaposition` is a definition and that amplitude-is-trace
stays an input. The problems below are all in the gap between that paragraph and
the headline claims in the same commit.

## 1. The physical gloss drops exactly one loop factor — and the corpus holds the counterexample

`freeEnergy_juxtapose_trivial`: *"Adding an unlinked trivial component costs no
free energy … a disjoint trivial component contributes nothing to the mass, **as it
must**."*

It must not. [`_li_2_q_util.py:777-783`](computations/_li_2_q_util.py) records that
a Markov closure of an `n`-strand braid is normalised by **the loop value raised to
`n−1`**. Juxtaposing an `m`-strand and an `n`-strand braid takes the normaliser
from `δ^{m−1}·δ^{n−1} = δ^{m+n−2}` to `δ^{m+n−1}` — **one factor of `δ`
unaccounted**, every time.

Measured at the proton-pinned `q₀ = 1.1099785827513808`:

| quantity | value | `log` |
|---|---|---|
| canonical (Wenzl) loop `δ = [2]_q = q + q⁻¹` | 2.01089686671 | **0.6985808249** |
| convention-C loop `δ_C = √q + 1/√q` | 2.00272236386 | 0.6945074369 |
| **cost the Lean assigns** | — | **0** |

So one juxtaposition is off by ≈ **0.699** in free energy, and ⁴He (four
components, three juxtapositions) by ≈ **2.096**. Not a rounding matter.

**Watch the square.** The source line reads `q + 2 + q⁻¹ = 4.0109`, which is
`δ_C²` — a loop value raised to `n−1 = 2` for a 3-strand closure, **not** the loop
value. I first took it for `δ` and got `log = 1.389`, i.e. exactly 2× the truth.
Anyone re-deriving this should quote `δ = [2]_q`, not `q + 2 + q⁻¹`.

**Why the Lean still checks.** `markovTrace_juxtapose_one` gets `1` from
`Matrix.trace_one` over `Unit`, i.e. from `Fintype.card Unit = 1` — a fact about
the *index type*, not about strands. The theorem is true; the sentence attached to
it is a claim about knots that the corpus refutes.

## 2. Connected sum ≠ disjoint union, and the file's title asserts the implication

Title: *"MULTIPLICATIVE under juxtaposition (disjoint-strand product), **hence**
under connected sum."* The `hence` is false, and it is item 1 seen structurally.
The Kronecker product models the **disjoint union**. For the normalised Jones
polynomial, `V(K₁ # K₂) = V(K₁)·V(K₂)` exactly, while
`V(K₁ ⊔ K₂) = δ·V(K₁)·V(K₂)`. **You get one or the other, never both** — and the
commit claims both, which is precisely how the missing `δ` hides.

## 3. Net new formal content is zero; the hypothesis was renamed, not discharged

* `trace_kron … := Matrix.trace_kronecker A B` — term-mode, an alias.
* `IsJuxtaposition A B C : Prop := C = A ⊗ₖ B` — a **definition**.
* so `markovTrace_juxtapose (h : C = A ⊗ₖ B)` is `trace_kronecker` after one `rw`.

What was ever open was never *"is `tr(A⊗B) = tr A · tr B`"* (Mathlib has it) but
*"does the assembly amplitude factorise"*. That is now spelled `IsJuxtaposition`
and is still assumed. The bean says the earlier roast's prediction — *"the
assumption relocates; it does not vanish"* — **"held exactly"**, and then marks the
bean DONE. Both cannot be true: if the assumption relocated, multiplicativity is
restated, not discharged.

## 4. The "falsifiable content of the whole bridge" is `x − x = 0`

`binding_juxtapose_eq_zero` is docstringed as *"the falsifiable content of the
whole bridge"*. Its proof is `rw [freeEnergy_juxtapose h hA hB]; ring` — after the
rewrite the goal is literally `(a + b) − (a + b) = 0`. It is an identity. Nothing
about it can fail.

## 5. A section promises `n` and delivers 2, citing an induction that does not exist

§*"Extensivity: `n` disjoint components multiply"* contains only `trace_kron_self`
(`k = 2`), whose docstring reads *"stated for the two-fold case plus induction
below"*. That is the file's **only** occurrence of the word "induction", and the
file ends 25 lines later. Extensivity over `A` nucleons is exactly what the mass
formula needs. (`ArchimedeanTraceBridge.freeEnergy_prod` already has the
`Finset.prod` form, so the gap is coverable — the section header just overstates.)

## 6. "BOTH bridge hypotheses from the juxtaposition alone"

`markovTrace_juxtapose_pos` takes `0 < A.trace` and `0 < B.trace` as hypotheses.
That is **preservation** under juxtaposition, not supply from it.

## 7. The deepest point, which the prior roast made and the discharge does not touch

Binding lives in `I ≠ 1` — the *failure* of juxtaposition. `binding_juxtapose_eq_zero`
proves binding is zero exactly where there is no physics, so the whole file is about
the reference state. And `QOU.Mass.InteractionFactorNotPairwise` (merged today,
`d2ed45489f`) sharpens it: if `I` factorises over pairs, `b₃ = 0`, refuted by AME's
`b₃ = +1.4262225`. The object that matters is doubly outside what was proved.

## Verdict

**Scope-(a).** The Lean is correct and the packaging is worth having as a Mathlib
contribution. What is wrong is the reporting: a Mathlib alias plus a definition is
presented as discharging a hypothesis it renames, an identity is presented as
falsifiable content, and a physical "as it must" is asserted against a
normalisation the corpus records three files away. `qou-301d` should read
**"route-B packaging landed; multiplicativity hypothesis RELOCATED to
`IsJuxtaposition`"**, not "DISCHARGED".

## Cheapest fixes, in order

1. Correct `freeEnergy_juxtapose_trivial` and `markovTrace_juxtapose_one` — either
   carry `δ` explicitly, or state plainly that the matrix-level result assumes an
   already-normalised amplitude and that the braid-closure normaliser is `δ^{n−1}`.
   **This is the only one that touches a claim that is false rather than oversold.**
2. Drop "hence under connected sum" from the title, or prove the connected-sum form.
3. Reword `binding_juxtapose_eq_zero`'s docstring: it is a consistency check.
4. Either add the `n`-fold induction or retitle the section to the two-fold case.
5. Reopen `qou-301d` at "relocated", or rename the bean to what was delivered.


---
**RESOLVED 2026-08-30 — item 1 fixed, and the correction is machine-checked rather than prose.**

`QOU/Mass/ClosureNormalisationDefect.lean` (4 declarations, sorry-free, `lean`-direct exit 0,
axioms `[propext, Classical.choice, Quot.sound]`):

* `closureNorm δ k t = t / δ^k` — the closure-normalised trace of a `(k+1)`-strand braid.
* `closureNorm_juxtapose` — normalised traces multiply **only after paying `δ`**:
  `closureNorm δ a A * closureNorm δ b B = δ * closureNorm δ (a+b+1) (A*B)`.
* `freeEnergy_closureNorm_juxtapose` — hence the free energy is additive **up to `log δ`**.
* `freeEnergy_closureNorm_additive_iff` — additivity holds **iff `δ = 1`**.
* `loopValue_ne_one` — `[2]_q ≠ 1` for `q > 1`, so the escape is closed at the substrate.

So the defect is no longer a caveat someone can read past; it is a theorem saying the additive
reading is false except at a point the substrate excludes.

Three minimal corrections to the sibling's files, each retaining the true matrix-level lemma:

1. `MarkovTraceMultiplicative` title — dropped "hence under connected sum", with the reason
   (Kronecker models the disjoint union; `V(K₁⊔K₂) = δ·V·V` while `V(K₁#K₂) = V·V`).
2. `markovTrace_juxtapose_one` docstring — now says the `1` comes from `Fintype.card Unit = 1`, a
   fact about the index type, and that a real unlinked component costs `log δ`.
3. `ArchimedeanTraceBridge.freeEnergy_juxtapose_trivial` — the "as it must" is retracted explicitly
   and pointed at the new file.

**Items 2-6 of the roast are NOT fixed** and were not claimed to be: the title fix covers item 2's
substance, but the `x − x = 0` docstring (item 4), the `n`-vs-2 section header and phantom induction
(item 5), and "BOTH hypotheses from the juxtaposition alone" (item 6) are left for the sibling —
they are rewording, not false claims. Item 3 (hypothesis renamed rather than discharged) is a
scoping judgement for whoever owns `qou-301d`, not something to unilaterally revert.
