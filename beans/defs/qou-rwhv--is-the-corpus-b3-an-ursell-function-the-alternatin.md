---
# qou-rwhv
title: Is the corpus b3 an Ursell function? The alternating-sign theorem says the sign obstruction is the positivity hypothesis
status: in-progress
pr: 8265
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T09:39:42Z
updated_at: 2026-11-15T17:10:00Z
parent: qou-v2om
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



---
# 🛑 RESOLVED AGAIN 2026-09-12 — the partition function exists, and it REVERSES the sign reading above (PR #7198)

**The answer to §"What would settle it".** Polymer set = the nucleons of one fixed nucleus; hard-core activity `z_i` per site; pair weight `mu_e = z_D + d_e` = the interface-letter trace (0.61269 pp / 0.50823 pn / 0.40363 nn, proton pin, convention D); Mayer variable `g = mu − 1`; compatibility = the Mayer graph expansion on the word's bond set; ensemble = **grand canonical over the sub-clusters** of the fixed nucleus:
`Xi_S(z) = SUM_{T ⊆ S} z^T PROD_{e ⊆ T} mu_e`, with `PROD mu = tr_M(atom)/tr_M(free)` re-measured on the LIVE alternating-core word to 2.5e-60 at A = 2,3,4. `ln Xi = SUM z^T phi^T_T` verified symbolically through n = 4. The corpus cumulants are Boolean-lattice inversions of `1 − Z` (= minus the no-isolated-vertex graph sum); the Ursell functions are partition-lattice inversions of `Z` (connected graphs); they coincide iff n ≤ 3, and at n = 4 differ by exactly the three perfect matchings (`b4corpus_eq`). That is the closed form of the 400/400 + 200/200 above.

**The sign.** `B = −alpha ln(Xi/Xi_free)` has Mayer coefficients `−phi^T_T` at EVERY order, so the corpus's `b2 = −phi2 > 0`, `b3 = −phi3 < 0` **is the Mayer expansion**. `phi^T_3 > 0` on (0,1)³ strictly (`phi3_pos`), hence `b3 < 0` for every triple — **no 2/3 threshold** (`b3(f,f,f) = −(1−f)²(f+2)`). The "restore (−1)^(n−1)" prescription in the section above is EXACTLY the same expansion at negative activity `z → −z` (`restored_eq_neg_activity`) and names no ensemble; it chose one sign per order against the data. **§"The consequence" above is withdrawn.** The fixed-A (canonical) partition function is the top coefficient `Z_S`, whose log is exactly pairwise (ln-cumulant 1e-60) — `PairwiseCumulantVanishing` and `MayerThreeBodySign` are the canonical / grand-canonical faces of one lattice gas, neither with a sign error.

**Magnitudes, no fit, sign WRONG at both:** Mayer 3rd coefficient at the live chain bonds, alpha-scaled: **−1.2277 MeV (3H)** vs AME +1.8081; **−0.7973 MeV (3He)** vs AME +1.0443 (68–83 % in magnitude). The 2.2511 / 2.7439 MeV above reproduce exactly and are negative-activity coefficients.

**Scope (b), invariant = Ursell alternation on (0,1).** Not excluded (scope a): an attractive Mayer channel (a letter with trace > 1 — none in the production word, measured), or a non-Mayer assembly. Per-block `chi_lambda` ratios are NOT the bond factor (worst dev 1.45 on 2H): the identification is tr_M-only.

Lean `QOU/MassTheory/UrsellPartitionFunctionB3.lean` — lean-direct exit 0, 13 decls, no sorryAx. Probe `computations/probes/ursell_partition_function_for_b3_probe.py` 11/11. Audit `docs/audits/2026-09-12-ursell-partition-function-for-b3.md`. `MayerThreeBodySign.lean` docstring re-scoped on the same branch; AGENTS.md bullet 4 wording proposed in the PR body.

**Still open:** the extensive term itself (`qou-brng`) — this closes the vocabulary question, not the magnitude.


## 2026-09-13 — cluster-expansion primary literature is now HELD; state what it is precisely

This bean's scope-(b) exclusion rests on *"invariant = Ursell alternation on
(0,1)"*, sourced to a 2022 survey. The `library/` ingestion of merge
`3cb26d4b9f8` adds primary sources in that lineage, now reachable by
corpus-grep path 5. **Measured per document (files containing the name, not hit
counts):**

| doc | sections | Groeneveld | Ursell | Penrose |
|---|---|---|---|---|
| `library/arxiv-1303.6444v3/` (*Virial Expansion Bounds*) | 14 | 2 | **0** | 14 |
| `library/arxiv-math-ph-0605041v2/` (Fernández–Procacci) | 3 | 2 | 1 | 2 |

**Do NOT read this as "the alternation theorem is now held."** What is held is
the **Groeneveld / Penrose** cluster-expansion *bounds* lineage — the ancestry of
the alternation and the right place to look for it — and the word *Ursell*
appears in exactly **one** file across both. The alternation itself was not
located here and this note does not claim it was. A triage pass characterised
these as carrying "Groeneveld and Ursell"; on measurement that is true of one
document, not both.

Separately, `library/arxiv-nucl-th-0507033v2/` (*Cluster Formation and the
Virial EOS of Low-Density Nuclear Matter*, 19 sections) was flagged as on-point
for the canonical-ensemble setting. It is topically adjacent and carries
**none** of Groeneveld / Ursell / Penrose — useful for the nuclear-matter
framing, not for the invariant.

**Also correcting a claim of mine from earlier in this session**, which the
scheduled check-in for #7255 still carried in its standing prompt: I said
Groeneveld *"is not in `library/`"* and made that the precondition for attacking
`qou-q8vl`'s remaining item. It was wrong then (I had run only the `INDEX.md`
tier, which is one line per **document** — a body-text term can never appear
there, so that tier structurally cannot answer the question), and there are now
two more holdings besides. `UrsellPartitionFunctionB3.lean:73` already cited
Jansen–Kolesnikov by DOI the whole time.

Holding a source is a **citation, not a derivation.** §13a: stays open; the
residual this bean names is still `qou-brng`, the extensive term.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.
