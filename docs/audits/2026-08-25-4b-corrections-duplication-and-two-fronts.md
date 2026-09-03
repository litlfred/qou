# Two corrections to this session's 4-B work

**Bean:** `qou-bhfg`. **Date:** 2026-08-25. Both are corrections; one is to my
own output, one is to the cheat sheet. Neither is a new result.

---

## Correction 1 — my `μ̄₁₂₃` Lean duplicates existing corpus Python

**`QOU/BraidsAndKnots/MilnorTripleLinkingMagnus.lean` re-derives what
[`computations/binding_mn_milnor_linking.py`](../computations/binding_mn_milnor_linking.py)
already had**, and I should have found it before writing a line.

That file, already on `main`, states the method I implemented, in the same words:

> *"Milnor `μ̄` is computed by the standard Magnus expansion of the longitudes in
> the free group: `μ̄(i₁…i_k)` = coeff of `X_{i₁}…X_{i_{k−1}}` in the Magnus image
> of the longitude `ℓ_{i_k}`, with `x_i ↦ 1+X_i` (truncated at total degree D)."*

and carries the same objects and the same validation set:

| its content | my Lean |
|---|---|
| `BORROMEAN = {1: comm(2,3), 2: comm(3,1), 3: comm(1,2)}` | `borromeanLongitude = [x₁,x₂]` |
| `Hopf: lk = 1` | `hopf_crossSum_ne_zero` |
| `Borromean: lk_ij = 0` | `borromean_crossSum_zero` |
| `Borromean: μ̄₁₂₃ = +1` | `mubar_borromean_eq_one` |
| `3-chain: lk = 1,1,0, μ̄₁₂₃ = 0` | **absent from mine** |

It also draws the conclusion I presented as a prune — *"Milnor DISTINGUISHES the
genuine 3-body (Borromean) from a chain of pairwise bonds"* — and
`mirror_split_s3_em_functional_probe.py` §(A3) already reasons from it:
*"For L6a4 every pairwise `lk_ij = 0` … so the pairwise-mediated part of `w_ij`
vanishes and any nonzero `w_ij` is mediated by the first"* non-vanishing
invariant.

### The claim I withdraw

`MilnorTripleLinkingMagnus.lean` and the audit both call
`mubar_borromean_eq_one` **"the corpus's first nonzero triple linking value"**.
**That is false and is withdrawn.** `binding_mn_milnor_linking.py` computes
`μ̄₁₂₃ = +1` on the Borromean link and validates it. The corpus had it.

### Why I missed it, which is the part worth keeping

I *did* run a corpus-grep for "Milnor" — over `content/` and the Lean tree. I
did **not** run it over `computations/`. That is **path 3 of the AGENTS.md
checklist**, and its stated purpose is exactly this failure:

> *"`grep -rln <topic> computations/` — implemented Python may already realise
> the categorical content the source file says is open."*

Third grep-discipline miss this session, and the most expensive: it produced
~200 lines of Lean that re-derive committed work. The earlier two were an arity
check skipped (the `evenTwistTripleLinking` retraction) and a topic-grep taken
for an availability check.

### What survives as genuinely new

Stated narrowly, because the temptation after a correction is to over-rescue:

* **The Lean formalisation itself.** The corpus's version is Python; mine is
  Lean, sorry-free, and axiom-free. Under formalize-first that is worth having —
  but it is a *port*, not a discovery, and the file now says so.
* **`odd_symmetric_functional_vanishes`** — that `E_EM` must be **even** in
  `μ̄₁₂₃`. The probe observes the sign flip (*"the mirror of L6a4 has `μ̄ = −1`,
  same E"*) and uses it for mirror-insensitivity; the statement that *component
  exchange* forces evenness, and so kills the linear ansatz, is not there.
  Related, not identical — do not cite it as untouched ground.
* **`deleted_word_not_two_components`** — the strand-deletion component-count
  trap. Not found elsewhere.

---

## Correction 2 — "one invariant, two fronts" is wrong, and the 69 % is unsourced

[`sm-eightfold-derivation-cheat-sheet.md`](../sm-eightfold-derivation-cheat-sheet.md)
says of 4-B, in three places:

> *Gates `m_d − m_u` **and** the remaining 69 % of the ³He mirror split. One
> invariant, two fronts.*

**Both halves have problems, and this session's audit repeated the first
uncritically.**

### The two fronts are two different objects

The phrase "two-like-charge EM-linking invariant" is doing double duty:

| front | the two like charges | level |
|---|---|---|
| `m_d − m_u` | the two **up quarks** inside one nucleon | **intra**-nucleon |
| ³He mirror split | the two **protons** of ³He | **inter**-nucleon |

Both are "two like charges, linked", which is presumably how they were merged.
They are not the same object — and `mirror_split_s3_em_functional_probe.py`
§(A1) **derives** that they cannot be:

> *per-component self-terms `a·Σqᵢ²` **cancel identically** in binding energy
> `B = Z·m_p + N·m_n − M`, because single-component EM self-energy lives in the
> free-nucleon masses `m_p, m_n`. So `a = 0` is DERIVED from the definition of
> `B`, not assumed.*

And `split_AME` is a **binding** difference — `mirror_nuclei_coulomb_systematics.py`
defines it as `B(lo) − B(hi)`. So the intra-nucleon self-energy contributes
**exactly zero** to the mirror split. The mirror front needs the inter-nucleon
pair term `w_ij·q_i·q_j`; the quark-mass front needs the intra-nucleon
self-energy. Deriving one does not deliver the other.

This is the overloaded-symbol failure AGENTS.md flags in the `c_k` registry:
*distinct objects sharing a glyph is a recurring root cause*.

### The 69 % has no source

Fixed-string grep over `docs/`: the figure occurs **three times, all inside the
cheat sheet itself**, and nowhere in `docs/audits/`, `docs/coordination/`, or
any witness. It is unsourced. (For scale: the `A=3` mirror ratio is `0.765`, so
the residual against the canonical Coulomb is ≈ 23.5 %, not 69 % — the number
does not obviously correspond to that quantity either.)

### Consequence for priority

Cheat-sheet §8 ranks 4-B **first**, and its stated rationale is that it *"closes
`m_d − m_u` **and** 69 % of the ³He mirror residual **together**"*. If the two
fronts are separate objects and the 69 % is unsourced, that rationale does not
hold as written. 4-B may still deserve rank 1 on its other grounds — smallest
scope, needs no `SU(3)`, stage-1 scoping done — but **not** on the two-for-one
argument.

**Not edited in the cheat sheet here.** That file is what agents read as the
prune; changing its §4-B framing and its §8 ranking is an author call, and it is
now the third item on this branch waiting for one.
