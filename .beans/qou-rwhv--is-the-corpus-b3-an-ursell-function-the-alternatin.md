---
# qou-rwhv
title: Is the corpus b3 an Ursell function? The alternating-sign theorem says the sign obstruction is the positivity hypothesis
status: in-progress
type: task
priority: normal
created_at: 2026-08-30T09:39:42Z
updated_at: 2026-09-12T05:04:43Z
---

## Where this came from

The owner uploaded six cluster-expansion PDFs on 2026-08-30 (commit `a12f83c4cd`)
after being asked whether the b3 question needed literature. Ingested by PR #6152.

## The finding

`library/s10955-022-02992-6/` (Jansen & Kolesnikov, *Cluster Expansions:
Necessary and Sufficient Convergence Conditions*, J. Stat. Phys. 189:33, 2022)
carries in §3.1 the classical **alternating-sign property of the Ursell
functions**, `phi^T_n = (-1)^n |phi^T_n|`, valid for a **non-negative (purely
repulsive) pair potential** — two independent proofs of the multi-rooted
generalisation. At n = 3 that is `phi^T_3 <= 0`.

`QOU.MassTheory.MayerThreeBodySign.lt_of_b3_pos` reaches the same conclusion from
a different argument (`b3 <= 3*fpn - 2` from `P3 >= 0`, with the framework's
`fpn = z_D = 0.6126880` against the 2/3 threshold).

## The question — and it is genuinely open

**Is the corpus's b3 an Ursell function in the theorem's sense?** They are NOT
the same theorem: the classical object is the third Ursell function of a
grand-canonical activity expansion of a genuine pair potential, the corpus's is
an inclusion-exclusion cumulant of a binding functional; the hypotheses are
`U >= 0` pointwise on the potential vs `P3 >= 0` on a product of bond factors.

- **If yes** — the obstruction is far broader than the `1 - prod f` assembly. No
  change of assembly escapes it; `PairwiseCumulantVanishing` and
  `MayerThreeBodySign` become two shadows of one classical fact, and only the
  hypothesis is left.
- **If no** — `MayerThreeBodySign`'s Mayer/Ursell vocabulary outruns its content
  and should be scoped.

## Why the hypothesis is the interesting half either way

The escape is named in the same 47 pages: the paper's own result is a convergence
condition for **possibly negative** pair potentials, iff in the non-negative case.
That is the class `b3 > 0` needs.

## What would settle it

Exhibit the polymer / cluster model whose activity expansion has the corpus's b3
as its third Ursell coefficient — name the polymer set, the weight, and the
compatibility relation. Then the classical theorem applies, or provably does not.
`rebenko2022virial` is the relevant setting note: it works the **canonical**
(fixed particle number) ensemble, which is what matches a nucleus, where the
grand-canonical activity expansion does not.

## Flagged, not asserted

Under a Boltzmann reading `f = e^{-beta U}`, `f < 1 <=> repulsive`, and all three
corpus bond factors lie in (0,1); an attractive channel would be a bond factor
> 1, of which there is none. But the corpus's f are Markov factors built from z,
and **nothing in the corpus identifies them with an exponentiated potential**.
That identification is the concrete next measurement.

## Scope

Scope-(a). A literature identification and a question. No derivation, no
refutation, no magnitude — the 6-14x gap on `b3_sym` (qou-9v7t) is untouched.

Audit: `docs/audits/2026-08-30-ursell-alternating-sign-and-the-b3-obstruction.md`
Parent question: `qou-brng` (the linking-vs-self-energy amplitude assignment).



---

# 🛑 RESOLVED, AND THE SIGN ABOVE IS WRONG (same day, 2026-08-30)

**Everything above this line asserted `phi^T_3 <= 0` and is retracted.** The
classical law is `(-1)^(n-1) phi^T_n >= 0`, so **`phi^T_3 >= 0`** — the
opposite sign, and the sign nature has.

**How the exponent was settled.** Not by re-reading the scan. The OCR of Eq.
(3.1) does read `(-1)^n`, but that contradicts the paper's own Corollary 3.3
(sign `(-1)^k` for `psi_{n,n+k}`, with `psi_{1,1+k} = phi^T_{1+k}`, i.e.
`(-1)^(m-1)` for `phi^T_m`). Settled by computing `phi^T_n` from the paper's
definitions in exact rational arithmetic: at n=2, `phi^T_2 = g <= 0`, so the
`(-1)^n` reading fails immediately — measured, 0/200 across n=2..5, against
200/200 for `(-1)^(n-1)`. **A superscript is exactly what OCR loses.**

## The answer to this bean's question

**Yes — at n = 3, and exactly.** Under `f_corpus = e^{-v}` (Mayer `g = f-1`):

    b3_corpus(f12,f13,f23)  ==  - phi^T_3(f12-1, f13-1, f23-1)

400/400 random non-uniform triples, exact `Fraction`, no tolerance. Trivially
true at n=2 as well. **It does NOT extend to n=4** — `b4` matches neither
`+phi^T_4` nor `-phi^T_4` (200/200 mismatches each). Low-order identity, which
happens to cover the whole 3-body question.

## The consequence

The corpus carries a **uniform** minus: `b_n = -phi^T_n` at n=2 AND n=3. At n=2
that is right (binding positive, `phi^T_2` negative). At n=3 the Ursell function
has already flipped on its own, so the uniform minus **inverts** the physical
sign — and produces exactly the negative `b3` that `MayerThreeBodySign` proves
is forced.

**`MayerThreeBodySign`'s `b3 < 0` is a missing `(-1)^(n-1)`, not a physical
obstruction.** Restoring the alternation gives `b3 = +phi^T_3 > 0` for every
`f` in (0,1): no threshold, no `fpn > 2/3`, no attractive component.

## Magnitude, measured, zero free parameters

Proton pin, convention D, uniform bonds, scale pinned at the deuteron:

    typing   f_pn          b3 restored (MeV)   / AME avg 1.4262   / AME triton 1.8081
    chi      0.6126880371        2.2511              1.578              1.245
    probe-2  0.5082297894        2.7439              1.924              1.518

Right sign, within **1.25x-1.92x**. The chirality-weighted-trace family (qou-9v7t)
sits **6-14x short** on the same quantity. This is a **postdiction of a magnitude,
not a derivation**, and the over-shoot is real (25% against the triton anchor at
the chi typing).

## What is still open — the load-bearing next step

**The Boltzmann identification `f_corpus = e^{-v}` is NOT derived anywhere.**
The framework's bond factors are Markov factors built from `z`. The algebraic
identity needs no such reading, and the sign law needs only `f` in (0,1) (which
is measured) — but the *physical* conclusion inherits it. Settle it by exhibiting
the polymer / cluster model whose activity expansion has the corpus's `b3` as
its third Ursell coefficient: name the polymer set, the weight, the compatibility
relation. `rebenko2022virial` is the relevant setting note — it works the
**canonical** (fixed particle number) ensemble, which is what matches a nucleus.

Nothing here refutes `MayerThreeBodySign` or `PairwiseCumulantVanishing`; every
statement in both remains true of the object it is about.

Producer: `computations/probes/ursell_alternation_sign_identity_probe.py`, 6/6.
Audit rewritten: `docs/audits/2026-08-30-ursell-alternating-sign-and-the-b3-obstruction.md`



---
**Takeover 2026-09-12** (session claude/ursell-partition-function-b3-2026-09-12). Attacking §"What would settle it": exhibit (or refute) the trace-side partition function whose Mayer expansion has the corpus b3 as its third Ursell coefficient — polymer set, weight g = mu_bond − 1, compatibility, canonical ensemble. Formalize-first Lean under QOU/MassTheory/, then an exact probe under computations/, then audit doc 2026-09-12-ursell-partition-function-for-b3.md.
