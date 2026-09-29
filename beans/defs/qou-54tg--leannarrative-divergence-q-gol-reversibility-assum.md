---
# qou-54tg
title: 'LEAN/NARRATIVE DIVERGENCE: q-GoL reversibility assumes involutivity its own proof denies'
status: completed
type: task
priority: normal
created_at: 2026-08-29T16:24:54Z
updated_at: 2026-08-29T17:58:32Z
---

**Found 2026-08-29** reviewing what landed on `main`, from the SM arc (PR #5744).
In my lane because my arc proved the σ-level fact the two sides disagree about.

**The divergence.** `content/quantum-observable-universe/information-theory/`,
one content object, two contradictory statements:

`q-game-of-life.lean:55-60` — `qGameOfLife_reversible` takes
`hT : Function.Involutive T`, justified in its docstring as

> *"Each q-Toffoli gate is its own inverse (an involution in `H₃(q)` under the
> Markov-trace dagger involution)"*

`q-game-of-life-proof.md` — the block's **own proof** says the opposite:

> *"The generators are **not** involutions at generic $q$: $\sigma_i^{-1} =
> \sigma_i$ holds precisely when $q = q^{-1}$, i.e. in the classical limit
> $q \to 1$"*

**Which is right, at the σ level: the .md.** Proved sorry-free on the SM arc,
`QOU.Eightfold.HeckeBraidingNonSymmetric.double_braiding_eq_one_iff`:
$\sigma^2 = 1 \iff q^2 = 1$, from the Hecke relation alone; and
`QOU.Archimedean.HeckeBraidingSubstrateNonSymmetric.q_gt_one_double_braiding_ne_one`
places the substrate off that locus. The .md's inverse formula
$\sigma^{-1} = \sigma - (q - q^{-1})$ is likewise
`QOU.MassTheory.TraceSignFlipRegime.inv_eq_sub`.

**SCOPE — what I have NOT shown, and it matters.** $\mathrm{Toff}_q$ is a
**word of three crossings** (the .md: *"three elementary crossings, taking three
Planck steps"*), not a single generator. A word can square to 1 where its
letters do not, so **I have not shown $\mathrm{Toff}_q^2 \neq 1$** and this is
**not** a claim that the theorem is false.

**What IS established:**

1. The involutivity hypothesis is **unsupported by the block's own proof**. That
   proof establishes *unitarity* ($\mathrm{Toff}_q^\dagger \mathrm{Toff}_q =
   \mathbb{I}$) and *invertibility* — never $T^2 = \mathrm{id}$. Unitary is
   not involutive.
2. The docstring's **stated reason** for the hypothesis contradicts the proof:
   it asserts involutivity *in $H_3(q)$*, at generator level, which is exactly
   what the proof denies at generic $q$.
3. The sibling theorem `qGameOfLife_unitary`, keyed on
   `Function.Bijective`, **is** supported — bijectivity is what the prose
   proves. It is the sound one of the pair.

Per AGENTS.md §"Conditional-proved ≠ premise-established": `_reversible` is a
true implication whose premise is unestablished, so it must not be read as
establishing that the q-GoL tick is reversible.

**Cheapest honest fixes, for whoever owns the block** (I have not applied any —
this is not my content object):

- **(a)** Drop `_reversible` and keep `_unitary`; bijectivity already gives
  reversibility in the sense the automaton needs (an invertible tick), and it is
  what the proof supports.
- **(b)** Keep the theorem, and correct the docstring to say the hypothesis is
  about the *composite gate*, not about $H_3(q)$ generators — then establish or
  cite $\mathrm{Toff}_q^2 = \mathrm{id}$, which is a real open question.
- **(c)** If $\mathrm{Toff}_q^2 = \mathrm{id}$ turns out **false** at generic
  $q$, `_reversible` is vacuous at the substrate and (a) is forced.

Deciding between them needs the $\mathrm{Toff}_q$ word, which the .md does not
pin down explicitly. That is the measurement to make first.



---

**SETTLED 2026-08-29 — disposition (c): the involutivity hypothesis is
unsatisfiable by the gate it names.**

The bean said the measurement to make first was the $\mathrm{Toff}_q$ word.
**It turned out not to be needed.** `prop:toffoli-transfer-matrix` supplies two
properties that settle it without knowing the word or its row support:

- **unitarity** — $\mathrm{Toff}_q^\dagger \mathrm{Toff}_q = \mathbb{I}$
  (`q-game-of-life.md` property 4); entries are real for $q > 0$, so this is
  orthogonality;
- **antisymmetry** — $P_{67} = -P_{76}$ (`prop:toffoli-transfer-matrix` item 4).

A real orthogonal involution equals its own transpose. Symmetric **and**
antisymmetric forces the entry to zero. So $\mathrm{Toff}_q^2 = \mathrm{id}$
requires $\Phi(q) = 0$.

Lean, sorry-free, axiom-clean:
`QOU/Information/AntisymmetricInvolutionForcesZero.lean` —
`involutive_orthogonal_transpose_eq`,
`entry_eq_zero_of_antisymm_of_involutive_orthogonal`,
`not_involutive_of_antisymm_entry_ne_zero`. Non-vacuity: the 90° rotation is
orthogonal with a **nonzero** antisymmetric entry, and the theorem correctly
concludes it is no involution.

**An over-claim of mine, caught by my own probe.** I first wrote that $\Phi$
vanishes *"exactly in the classical limit"* on the strength of its $(q-1)$
factor. **False** — $\Phi$ also vanishes at $q = u^2 \approx 0.4656$, $u$ the
real root of $u^3 + u - 1$. Both zeros lie **at or below $q = 1$**, and the
block's own stability condition is $q > 1$, so the conclusion survives on the
regime the block declares; the phrasing did not. Corrected before commit.

**Corroboration by an independent route** (`toffoli_involutivity_probe.py`,
sympy exact throughout, no float64). Assuming row 7 is supported on $\{6,7\}$ as
the classical Toffoli's is, $M^2 = I$ forces $P_{77}^2 - \Phi^2 = 1$;
substituting $q = u^2$ gives a degree-16 polynomial with **zero real roots** by
exact Sturm count. At the substrate $P_{77}^2 - \Phi^2 = 0.3016$, a shortfall of
$0.698$ — not marginal. Same verdict, and it needs an assumption the theorem
above does not.

**Disposition for the block owner: (a) or (c) from the list above, not (b).**
`qGameOfLife_reversible`'s hypothesis cannot be discharged for the gate at any
$q > 1$. `qGameOfLife_unitary`, keyed on `Function.Bijective`, is sound and is
what the block's proof supports.

**Scope, and it matters.** This says the q-Toffoli is not an **involution**. It
does **not** say the q-GoL tick is irreversible — a unitary gate is invertible,
which is the property the automaton actually needs. The defect is that
`_reversible` asks for the wrong one.
