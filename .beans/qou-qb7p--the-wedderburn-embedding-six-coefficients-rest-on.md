---
# qou-qb7p
title: The Wedderburn embedding six coefficients rest on is opaque, axiom-bearing, and the wrong shape
status: completed
type: task
priority: normal
created_at: 2026-09-05T16:11:46Z
updated_at: 2026-09-05T16:17:29Z
---


Branch `claude/q407-self-assuming-projections-2026-08-21`. `qou-orjl` left this
as the single load-bearing unknown: six of the seven mass coefficients depend on
a bridge the corpus names only as *"their image under the Wedderburn
embedding"*. Setting out to specify it, the answer is that it **cannot be
specified from what is there** — and the reason is mechanical, not a matter of
taste.

## 1. It exists and is deliberately unconstructed

`QOU/HeckeAlgebra/Wedderburn.lean` declares `opaque wedderburnEmbed`, with the
file's own explanation, quoted verbatim:

> "Using `axiom` keeps the embedding opaque pending concrete construction."

No body. The file is admirably honest about this; the mass-theory block that
leans on it is not.

## 2. It registers as a FOURTH axiom

Measured with `lean`-direct on a theorem that merely *mentions* it:

    'uses_embed' depends on axioms: [propext, Classical.choice, Quot.sound,
                                     QOU.HeckeAlgebra.Wedderburn.wedderburnEmbed]

**Every Lean file this arc has landed reports exactly the first three.** So
anything routed through the bridge is *not* axiom-clean by the corpus's own
standard — and that is checkable rather than rhetorical.

## 3. Its shape is wrong for the job

    wedderburnEmbed : {n : Nat} -> WedderburnDecomposition n
                      -> Matrix (Fin (heckeDim n)) (Fin (heckeDim n)) Real

Blocks **in**, one matrix **out** — an assembly map. The clause needs the
opposite: one block's scalar `C_{(2,1)}` split into three coefficients. Wrong
direction *and* wrong arity.

## 4. And there is no alternative

Searched: the sibling `wedderburn*` objects are weights (`wedderburnWeight`,
`wedderburnStd`, `wedderburnSym`) and dimensions (`wedderburnNonSignDimS3`, the
`wedderburn_nK_via_witness` family). None is a map of algebras.

**So the bridge is unavailable on BOTH readings.** If the block means
`wedderburnEmbed`, it is opaque, axiom-bearing and mis-shaped. If it means
something else, that something is not defined anywhere in the corpus.

## What was done

`unified-iterative-correction-proof.md`'s `(2,1)` clause is **annotated as an
open obligation, not deleted** — the claim may well be true, it is simply
unsupported, and a reader should not take it as derived. The annotation names
the opaque object, its axiom footprint and its arity mismatch.

## 🛑 Why NO Lean theorem accompanies this

The tempting one — "three independent coefficients cannot come from one scalar"
— is **false as stated**: set-theoretically a single real can encode three.
Making it true needs a continuity or naturality hypothesis the corpus does not
supply, and manufacturing one would be the same overreach this bean documents.
The real Lean content is the `#print axioms` measurement in §2, recorded in the
probe. Scoping this out is part of the result.

## Artifacts

`computations/qbeta/qbeta_wedderburn_bridge_probe.py` (6/6). One assertion
initially failed because the Lean source wraps mid-phrase and a raw substring
check missed it — fixed by normalising whitespace, and the reason is in a
comment so it is not re-introduced.

Gates: `bun run scripts/run-validate.ts` **✓ Valid**, 4 issues, all pre-existing
and in other blocks. float64 guard clean.

## Successor

Construct `wedderburnEmbed`, or state the `(2,1)` clause's decomposition as its
own posit with its own coefficients. Until one of those happens, six of the
seven mass coefficients have **no derivation at all** and the fit-shape QA note
on `mass-formula-regime-switching-table1-data` stands unanswered for every one
of them.
