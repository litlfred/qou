---
# qou-k4oq
title: Build the Hecke algebra foundation in Lean from scratch — Mathlib has NONE
status: in-progress
type: milestone
priority: normal
created_at: 2026-09-05T07:53:31Z
updated_at: 2026-09-05T08:45:40Z
---

LAYER 1 DONE 2026-09-05, sorry-free, lean-direct exit 0 (4.0 s), zero warnings.
AXIOMS: [propext, Quot.sound] only -- NOT EVEN Classical.choice, a cleaner footprint
than the rest of this arc (the q=1 files all pull Classical.choice).

BUILT FROM SCRATCH BECAUSE MATHLIB HAS NOTHING. Measured: zero files matching
HeckeAlgebra, IwahoriHecke, QuantumGroup, BraidGroup, RMatrix, YangBaxter,
TemperleyLieb. Only GroupTheory.Coxeter. Nothing to import, nothing to build on.

LAYER 1 (this file, QOU/IwahoriHecke/HeckePresentation.lean): H_{n+1}(q) as a
RingQuot of FreeAlgebra R (Fin n), generic CommRing R with q : R-units (no R-reals,
per 7c). sigma_sq, sigma_braid, sigma_far, sigma_eigen ((sigma-q)(sigma+q^-1)=0),
sigmaUnit (explicit inverse sigma - h), skein (sigma - sigma^-1 = q - q^-1),
hParam_one + sigma_sq_of_hParam_eq_zero (q=1 degenerates to sigma^2=1), and the
UNIVERSAL PROPERTY lift / lift_sigma / algHom_ext.

The universal property is not decoration: without it the presentation is INERT. It is
what lets a representation, a trace, or any map OUT of H_{n+1}(q) be defined by naming
generator images and checking three relations. Everything in layers 2-4 goes through it.

🛑 NONTRIVIALITY IS NOT PROVED, and this is a SOUNDNESS caveat not a wishlist item.
Nothing in layer 1 shows H_{n+1}(q) != 0. A presentation whose relations collapsed
would satisfy every theorem above VACUOUSLY -- the same failure mode as a LinearMap.trace
without Module.Free (see qou-mex9). Establishing dim = (n+1)! needs the T_w BASIS
THEOREM (Bourbaki/Matsumoto: a reduced word gives a well-defined T_w independent of the
reduction), which is the deep result of the subject. Until that lands, do NOT read
layer 1 as statements about a nonzero algebra.

REMAINING LAYERS:
  2. T_w basis + length function (Matsumoto). THE hard one; unlocks nontriviality.
  3. Markov trace on H_n(q).
  4. Wedderburn / Hoefsmit partition-indexed decomposition -- what qou-mpq5 scoped as
     multi-week, and what quantum Schur-Weyl's BRAIDING half needs.


## CORRECTION 2026-09-05 — the corpus already had layer 1; I searched Mathlib, not the corpus

This bean was opened as *"build the Hecke algebra foundation in Lean from scratch"* on the
finding that **Mathlib** has no Hecke algebra (true: zero files matching `HeckeAlgebra`,
`IwahoriHecke`, `BraidGroup`, `RMatrix`, `YangBaxter`, `TemperleyLieb`). I did not run the
six-path corpus-grep checklist. **This repository already had all four proposed layers**:

| proposed layer | already on `main` |
|---|---|
| 1 presentation + universal property + nontriviality | `QOU/MathlibExt/IwahoriHeckeAlgebra.lean` — 312 lines, **0 sorries**, general Coxeter matrix, `lift`/`hom_ext`/`exists_unique_lift`, and `nontrivial_of_symm` via the index and sign representations |
| skein calculus in the §7a normalisation | `QOU/MathlibExt/SkeinFromHecke.lean` — 454 lines, `IsHeckeGenerator`, explicit inverse, unit, skein relation, eigenvalue factorisation, a non-scalar witness |
| 2 `T_w` basis | `QOU/IwahoriHecke/Tw.lean` (stub — see below) |
| 3 Markov trace | `QOU/IwahoriHecke/MarkovTrace.lean`, `QOU/MathlibExt/MarkovTrace.lean` |
| 4 Hoefsmit / Wedderburn | `QOU/IwahoriHecke/Hoefsmit.lean`, `QOU/MathlibExt/WenzlSchurElement.lean` |

So my `HeckePresentation.lean` was redundant and strictly less general. **Removed from the
branch.**

I also told the author *"nontriviality is not proved; getting `dim = |W|` needs Matsumoto"*.
The second clause is right, the first is **wrong**: `Nontrivial (HeckeAlgebra)` follows from
the two one-dimensional representations in five lines and was already proved. Matsumoto is
needed for the **rank**, not for non-collapse.

## What was actually missing, and is now landed

**(a) The two `MathlibExt` Hecke files were not connected.** One constructs the algebra in
the Iwahori normalisation `(T_i − Q)(T_i + 1) = 0`; the other develops the skein calculus
for the symmetric §7a normalisation `σ² = (q − qi)σ + 1`. The constructed generators are
**not** `IsHeckeGenerator`s — eigenvalues `Q`, `−1` rather than `q`, `−qi` — so the skein
calculus was floating free of the only algebra the corpus builds. Neither file mentions the
other. `QOU/IwahoriHecke/BalancedGenerators.lean` supplies `σ_i := qi·T_i` over `H(M, q²)`
and proves `isHeckeGenerator_sigma`, transferring the whole API; plus braid relation,
`T_i = q σ_i`, `hom_ext_sigma`, `liftBalanced`, and the `q = 1` degeneration.

**(b) `Tw.lean` claimed a conjecture discharge that was empty.** Detail in the file's own
retraction block and in commit `7adc2c65082`. Summary: a second class named
`HeckeAnyonicSubstrate` asserting only `Tw_gen 1 = 1`, inhabited by
`fun w => if w = 1 then 1 else 0`, with `hecke_anyonic_substrate_structural` presented as
discharging `conj:hecke-anyonic-substrate` — **while the canonical carrier
`QOU/BraidKnot/HeckeAnyonicSubstrate.lean` states in its own docstring that the conjecture
is open and deliberately carries no instance.** Same name, opposite verdicts, one tree.
Removed.

**(c) The Matsumoto deferral is now split into its two halves.**
`QOU/IwahoriHecke/BraidWordInvariance.lean` proves the **algebra** half —
braid-equivalent words have equal Hecke products — and states the **group** half
(Matsumoto proper: reduced expressions are braid-related) as a named hypothesis of
`exists_Tw_of_braidEquiv`, which derives a well-defined `T_w` from it. The group half is in
neither Mathlib (`GroupTheory/Coxeter/` has `IsReduced`, length, descents, inversion
sequences — no exchange property, no Matsumoto) nor this corpus.

## Still open

- Matsumoto's theorem for Coxeter groups (the group half). Mathlib's `rightInvSeq` /
  `leftInvSeq` are the machinery the strong exchange property is normally derived from, so
  the route exists; nobody has walked it.
- The `T_w` **basis** theorem (free of rank `|W|`) — needs the regular representation on
  `W →₀ R`, whose braid-relation check is the deep part.
- The Markov trace is `noncomputable opaque` in `IwahoriHecke/MarkovTrace.lean`; not
  constructed.
- `QOU/IwahoriHecke/Quotient.lean` imposes the quadratic relation only (bean `qou-phir`).
