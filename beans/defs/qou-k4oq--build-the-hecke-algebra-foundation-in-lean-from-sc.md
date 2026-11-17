---
# qou-k4oq
title: Build the Hecke algebra foundation in Lean from scratch — Mathlib has NONE
status: in-progress
type: epic
priority: normal
created_at: 2026-09-05T07:53:31Z
updated_at: 2026-11-17T08:12:13Z
parent: qou-rtxm
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


## 2026-09-05 — cyclicity + the Markov peel (PR #6845), and both moves are now proved

Branch `claude/hecke-cyclicity-markov-2026-09-05`. Two files, both lean-direct
exit 0 with `-DautoImplicit=false -s 65536`, `#print axioms` = [propext,
Classical.choice, Quot.sound] on every headline result — no `sorryAx`.

**`QOU/IwahoriHecke/QTraceCyclic.lean` — Markov move I.** `QuantumTrace` had
cyclicity only against a generator. The image of `heckeActionN` now provably
lies in `Subalgebra.centralizer R {siteWeight w}` for every `x`
(`heckeActionN_mem_weightCentralizer`), obtained by corestricting the action
along `liftBalanced` and composing back with `Subalgebra.val` — subalgebra
closure in place of an induction over the algebra. Hence `qTrace_mul_comm`
(`tr_w(xy) = tr_w(yx)`, arbitrary x, y, every w) and `qTrace_conj`.

**`QOU/IwahoriHecke/MarkovPeel.lean` — Markov move II.** The tower
`tower : H_{m+1}(q) →ₐ H_{m+2}(q)` (input: `coxA_castSucc`) and its matrix
counterpart `extendSiteHom` (= `idTensorHom` reindexed along `Fin.snocEquiv`),
squared up by `heckeActionN_tower`. Then `trace_peel` /`qTrace_peel`:
`tr_w(ι(x)·σ_last) = z·tr_w(x)`.

**The result worth carrying forward.** `peel_forces_physical_weight`: if the
peel holds at all then `w 1 = q²·w 0`; with `w 0 = 1` that is `w = (1, q²)` and
`z = q³` (`peel_weight_eq`). So `K = diag(1, q²)` — the weight
`WeightedPermutationCharacter` and the rest of the corpus use — is **not a
convention adopted to make the arithmetic work**; it is the unique weight up to
scale admitting a Markov peel at all, and `q³` is `w 1 · q`, forced by the same
two equations rather than fitted. The mechanism: the weighted partial trace of
`Ř` over the new site is diagonal (the swap entry would need `u = t` and
`t = v` at once), with entries `w0·q + w1(q − qi)` and `w1·q`; equating them is
`w0·q = w1·qi`.

**Still NOT done, and named in the files rather than scaffolded:**

* normalisation `tr(1) = 1` — `qTrace_one` is `(∑ₖ w k)^{m+1}` = `(1+q²)^{m+1}`
  at the physical weight, so the normalised functional and its `z` carry that
  factor;
* the link invariant — `QOU.IwahoriHecke.MarkovTrace.markovTrace` is still
  `noncomputable opaque`, constructed nowhere;
* Matsumoto (the group half) — bean `qou-06h7`, updated today with the measured
  Mathlib status (its own TODO list says it is unproved);
* surjectivity onto the commutant — bean `qou-us0a`, updated today;
  `centralizer_centralizer` is still absent from Mathlib v4.24.0.


## 2026-09-05 (same PR #6845) — normalisation, and convention D's z is DERIVED

`QOU/IwahoriHecke/MarkovNormalized.lean`. The third Markov axiom, and the
finding that makes this arc touch the compute layer.

`R` is a bare `CommRing`, so the inverse of the total weight is carried as a
scalar with a witnessing equation, the idiom `q * qi = 1` already uses:
`(∑ₖ w k) * wi = 1`, `markovTr x := wi^(m+1) * qTrace w x`. Three axioms:
`markovTr_one`, `markovTr_mul_comm`, `markovTr_peel` (scalar `z · wi`).

**The peel already forced `w = (1, q²)` and `z = q³`. The total weight is then
`1 + q²`, so the normalised peel scalar is `q³/(q² + 1)` — convention D's
Markov parameter verbatim** (`pyhecke/gram.py::z_mp`, *"z = q³/(q² + 1) —
convention D"*), and not convention C's `√q/(q+1)`. Division-free as
`markovParam_eq_conventionD`; `markovParam_unique` shows the equation
`ẑ·(q²+1) = q³` pins `ẑ` once `1+q²` is invertible, so it is a determination
rather than a choice of representative. `markovTr_physical` collects all four.

Nothing chose it. The weight was forced by the peel existing at all, the
unnormalised scalar by the same two equations, the normalisation is division
by `tr_w(1)`.

**Two limits, in the file rather than glossed.** (1) It is a match of
algebraic FORM in the §7a balanced parameter — which IS the parameter
`gram.py`'s `z` is written in, since §7a fixes `(σ − q)(σ + q⁻¹) = 0` — but
proving the compute layer's *numerical* `z` at the substrate pin is this same
object needs the two trace conventions identified, and that is not attempted.
(2) Still not a link invariant: that needs `B_n → H_n(q)`, Markov's theorem
and closure-invariance. `MarkovTrace.markovTrace` stays `noncomputable opaque`.

**Relevance to the 2026-08-15 owner ruling (R1, convention D canonical).**
That ruling settles which convention is canonical and notes the `c_k` ladder
must be *re-derived* under D. This is an independent derivation of D's `z`
from the R-matrix — it does not re-derive the ladder, but it says the
convention the ladder must be re-derived in is not arbitrary.


## 2026-09-05 — the braid group (PR #6860), and both Markov moves on braids

Branch `claude/braid-group-hecke-rep-2026-09-05`, immediately after #6845.

**Mathlib has no braid group.** Measured on the pinned v4.24.0:
`Mathlib/GroupTheory/` has `PresentedGroup.lean` and **no `Braid*` file at all**.
So it is built here from the presentation, as the Hecke algebra was.

`QOU/IwahoriHecke/BraidGroup.lean` — `artinRels M` written with the SAME
`altProd` as `T_braid` / `Balanced.sigma_braid`, so the group relation and the
algebra relation are one alternating word in two monoids and `map_altProd`
moves between them. `ArtinGroup M := PresentedGroup (artinRels M)`;
`BraidGroupN m := ArtinGroup (coxA m)`. `heckeRep : Art(M) →* H(M,q²)ˣ` from
the universal property, once the braid relation is checked in the UNIT group
(`sigmaUnit_braid`). `braidTrace` + `braidTrace_conj` = **Markov move I**.

This closes a gap the corpus's own docstrings had been pointing at:
`isUnit_sigma` says invertibility is *"what makes H(M,q²) a quotient of the
braid group algebra rather than merely of the free algebra"* — there was no
braid group for that sentence to be about.

`QOU/IwahoriHecke/BraidTower.lean` — `braidGen_braid` (the relation read back
out of the quotient), `braidTower : B_{m+1} →* B_{m+2}` (single input:
`coxA_castSucc`), `heckeRep_braidTower` closing the square against the algebra
tower, and `braidTrace_peel` = **Markov move II**. All three layers now have a
tower map and all three squares commute; each is two homs agreeing on
generators, never an induction.

**STILL NOT A LINK INVARIANT, and the two gaps are NAMED rather than written
as hypotheses** — a hypothesis would hide how much either is doing:

1. **The writhe normalisation.** II⁺ and II⁻ carry *different* scalars (`σ` and
   `σ⁻¹` do not peel to the same thing), so the raw functional is an invariant
   of a **framed** closure. Fixing it needs a well-defined writhe (exponent
   sum) on `ArtinGroup`. This is the cheaper of the two and is the natural next
   piece of work.
2. **Markov's theorem** — closure-equivalence is generated by exactly these two
   moves. Low-dimensional topology, absent from Mathlib, not proved here.

`MarkovTrace.markovTrace` therefore still stays `noncomputable opaque`.


## 2026-09-05 — the framing correction is CLOSED; only Markov's theorem is left (PR #6860)

Same branch, two more files. This closes the FIRST of the two gaps the previous
entry named, so the honest gap list is now one item long.

`QOU/IwahoriHecke/NegativePeel.lean` — move II comes in two flavours and they do
NOT share a scalar. No new sum manipulation: the skein relation gives
`σ⁻¹ = σ − (q − qi)` on the nose, so the negative peel is the positive one minus
`(q−qi)` times the peel of `1`. The one new ingredient is that last piece,
`trace_extendSite`: `tr_w(X ⊗ 1) = (∑ₖ w k)·tr_w(X)` — an inert site multiplies
the trace by the total weight, which is `qTrace_one` one factor at a time.
Hence `z⁻ = z − (q−qi)(∑ w)`, and at the forced weight
`q³ − (q−qi)(1+q²) = q³ − (q³ − qi) = qi`. **So `z⁻ = q⁻¹` against `z⁺ = q³`,
and their product is `q²`, NOT 1** (`peel_scalars_physical`) — which is exactly
why a writhe-only correction cannot work.

`QOU/IwahoriHecke/JonesNormalisation.lean` — Mathlib has no braid group hence no
writhe. `writhe : Art(M) →* Multiplicative ℤ` sends every generator to 1 and is
well defined on the presented group **precisely because `M` is symmetric**: an
Artin relation equates alternating words of lengths `M i j` and `M j i`, which a
constant assignment turns into the same power. Same hypothesis `heckeRep` and
`liftBalanced` already take. `braidWritheZ_braidTower`: an inert strand does not
change it.

Then `J(β) := A^n · B^{writhe β} · tr(β)`. The two moves give two equations —
`A·B·z⁺ = 1` and `A·B⁻¹·z⁻ = 1` — whose product and quotient give
`A² = q⁻²(1+q²)²` and `B² = q⁻⁴`. So `A = (1+q²)q⁻¹`, `B = q⁻²`, written
division-free as UNITS over `q·qi = 1` and `(1+q²)·wi = 1`, so `R` stays a bare
`CommRing`. `jonesFn_peel` / `jonesFn_peel_neg` verify both moves;
`jonesFn_conj` is move I, untouched (writhe and strand count are both
conjugation-invariant).

**`framing_constants_unique` states what the equations pin AND NO MORE**: for any
`a,b,c` with `a·b·z⁺ = 1`, `a·c·z⁻ = 1`, `b·c = 1`, they force
`a²·(q³·qi·wi²) = 1` and `b²·q³ = qi`. That is a determination of the SQUARES —
the sign is genuinely free, which is why the standard Jones normalisation carries
a `(−1)`-type factor, and the file does **not** claim uniqueness of `A` and `B`.

**ONE gap left, and it is the topological one.** `jonesFn` is invariant under
both Markov moves and under conjugation. It is still not a link invariant because
**Markov's theorem** — closure-equivalence of braids is generated by exactly
these moves — is low-dimensional topology, absent from Mathlib, and not proved
here. It is NOT hypothesised anywhere: with it `jonesFn` descends to links;
without it `jonesFn` is a function on braids constant on the orbits of both
moves. `MarkovTrace.markovTrace` accordingly stays `noncomputable opaque`.



## Reorganisation 2026-10-04

Now the epic for P3.HECKE under Lean / Mathlib foundations.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.


## Round 57 Progress (lane-e667)
- **PR:** https://github.com/litlfred/qou/pull/8254 (`e9795825b5e02ba1c5315e9cbd5d10db4bc08957`)
- **Module:** `QOU.Foundations.OcneanuTowerConventionDRibbonClebschGordan` (`folio/quantum-observable-universe/lean/QOU/Foundations/OcneanuTowerConventionDRibbonClebschGordan.lean`), wired into `QOU.lean`.
- **Theorem:** `partial_trace_peel_forces_weight_and_convention_d` — proves that `2 × 2` R-matrix partial-trace diagonal balance `w0 · q + w1 · (q - q⁻¹) = w1 · q` forces `w0 · q = w1 · q⁻¹` and `w1 = q² · w0`, pinning `w = (1, q²)`, `z = q³`, and the cleared Convention D normalization identity `zNorm · (1 + q²) = q³`, verified in `ocneanu-tower-convention-d-ribbon-clebsch-gordan.witness.json`.
- **Status:** Kept at `in-progress` pending Merge Manager merge and full dependency verification.
