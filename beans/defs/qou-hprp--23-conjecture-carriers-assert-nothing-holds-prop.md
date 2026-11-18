---
# qou-hprp
title: '23 conjecture carriers assert nothing — the `holds : Prop` shape'
status: in-progress
type: task
priority: medium
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T18:10:00Z
updated_at: 2026-10-04T15:14:32Z
parent: qou-5p7n
---

Found sweeping the q-geometric-langlands Lean siblings after the four
`False`-proving axioms (`qou-hwax`, `qou-qexf`).

```lean
class QuantumLanglandsDual where
  holds : Prop
```

`⟨True⟩` inhabits this. So a downstream `[QuantumLanglandsDual]`-conditional
theorem proves nothing modulo the conjecture, and the carrier records only that
*someone intends a proposition to go here*. It is the `true-class-field` variant
of `proof-claims-unencoded` — one step less obvious than an empty carrier, and it
passes every existing check.

## Measured, and the first number was wrong

| measure | files |
|---|---|
| naive grep `holds : Prop` | 38 |
| **live, comments stripped** | **23** |
| prose-only false positives | 15 |

A 39 % false-positive rate for the naive grep. The false positives are
docstrings describing a stub that was *already replaced* — including
`modular-s-transform-q-q-tilde.lean`, whose docstring records that it
"replac[ed] the former `holds : Prop` stub". A grep that reads comments as code
would have sent an agent to fix the one file in the chapter that is already
correct.

By chapter: mass-theory 7, `lean/` 6, nuclear-interactions 4,
stochastic-mechanics 2, q-geometric-langlands 2, appendix-surreals 1,
appendix-surreals-archimedean 1.

Detector: [`scripts/lean-overclaim-audit.py`](../scripts/lean-overclaim-audit.py)
reports 39 such *declarations* under `contentless-carrier`, plus 9
`empty-carrier`. That is the trustworthy family in that script; read its
docstring for what is not.

## The model to copy is in the same chapter

`ModularSTransformQQTilde` shows the right shape — a conjectural continuation
`F : ℂ → ℂ`, a `nondegenerate` field so the duality is not vacuous, and the
`s_automorphy` law carrying the actual claim. Three carriers in one chapter, two
dispositions, and the good one already documents its own migration.

## Why this is NOT a mechanical drain

**Do not sweep these.** Filling in a carrier means deciding what the conjecture
claims, which is a mathematical judgment about the author's intent, not a
repair. The specific trap, worked through on `QuantumLanglandsDual`: its `.md`
claims `H_n(q) ↔ H_n(q^{-1})` via Cartan folding. An encoding restricted to the
*parameter* — an involution `q ↦ q⁻¹` on `ℝ`, nontrivial for `q > 1` — is
content-bearing, satisfiable, and **provable**, so supplying it with an instance
would report an open conjecture as closed. That is strictly worse than the stub
it replaced.

A faithful encoding has to reach the algebra. `QOU.Hecke.HeckeAlgebra R n q A`
exists (`QOU/StaircaseCornerHook.lean` uses it as an instance binder), so the
statement is expressible — an algebra equivalence `A ≃+* B` between `H_n(q)` and
`H_n(q⁻¹)` compatible with folding — but that is a per-conjecture piece of work
needing the author's reading of each claim, and it carries a build cost the
content-block siblings do not currently pay.

---

## TRIAGE 2026-08-29 — and the ordering above is WRONG

That closing line said *"take the ones whose `.md` states a single crisp identity
or inequality first."* Having read all 23 `.md` claims, **that is backwards.** The
crisp ones are crisp *because* they are classical or numerical, and those are
precisely the two categories that need a different disposition rather than a
content-bearing conjecture class. Filling one in would be wrong work, not easy
work.

The 23 are **not one population.** Four kinds:

**(a) The claim is a CLASSICAL theorem, mislabelled as a framework conjecture.**
`conj:poincare-lefschetz-borromean` states `H^k(M, ∂) ≅ H_{3−k}(M)` — Poincaré–
Lefschetz duality, a theorem of algebraic topology — and `H₁ ≅ ℤ³` for the
3-cusped Borromean complement, which is standard. Nothing here is conjectural.
The right disposition is a **cited hypothesis class** in the `IsWeilZeta` pattern
(`qou-hwax`), carrying the classical result as a named, referenced hypothesis —
not a conjecture stub, and not an axiom. `conj:borromean-bloch-group-element` is
partly this too: Bloch-group/regulator theory is classical, the `h⁴` shadow is
the framework's.

**(b) The `.md` declares conditionality that the type does not carry.**
`conj:spin-from-so3-fiber` ("conditional on the S₅ ↔ SO(3) fibre action"),
`conj:wigner-su4-from-spin-isospin` ("conditional on spin and isospin"),
`conj:lusztig-canonical-basis-q-eq-1` ("conditional on
[`conj:kazhdan-lusztig-classical-limit`]"), `conj:kashaev-density-equals-sdp-multiplicity`
("under the Kashaev volume conjecture"). This is the named criterion
`proof-dependent-conjecture-not-conditional` — which could not see any of them;
see `qou-vgat`.

**(c) An IDENTIFICATION of a framework notion with a mathematical object,
blocked on the framework notion having no formal carrier.**
`conj:p-from-braid-mirror` (parity *is* the braid mirror),
`conj:quantum-langlands-dual`, `conj:mirror-3d-3d-correspondence`,
`conj:hecke-anyonic-substrate`, `conj:type-b-folding-cpt`. Same blocker shape as
`qou-qspc`: the mathematical half is often provable, the identification is the
claim, and there is nothing to identify *with*. `p-from-braid-mirror` is the
sharpest illustration — "P is an involution negating writhe" is a provable fact
about braid words; that P *is parity* is not statable without a formalised
parity operation.

**(d) A NUMERICAL near-match.** `conj:isospin-from-canonical-bowtie` gives
`Δm/M_N = ℏ_q²·h·[2]_q·(1+ℏ_q³)/3` at **305 ppm** against CODATA. Encoding it as
an equation would be **false**; encoding it with a tolerance is a modelling
decision under the anti-fit discipline, not a transcription.

**Separately, one is not a conjecture at all.**
`prop:crystal-basis-resolves-mass-tower-open-problems` is a **`proposition`**
whose carrier is `holds : Prop`. A provable-kind block asserting nothing is worse
than a conjecture doing so — the label claims it is established. Worth handling
before any of the conjectures.

**Revised order.** (1) the `prop:` above, since its kind over-claims; (2) the
category-(a) classical ones, which need a citation rather than a derivation and
are the only genuinely cheap group; (3) category (b), where the fix is adding a
binder the prose already asserts; (4) leave (c) and (d) — they need the author.


--------

## 2026-09-03 — item (1) of the revised order was ALREADY DONE, and the count moved

**Correcting this bean against the tree.** The revised order above puts
`prop:crystal-basis-resolves-mass-tower-open-problems` first, "since its kind
over-claims". That was written 2026-08-29. It was fixed on **2026-08-31** — the
file now carries `ReducesTo`, a seven-parameter `CrystalBasisCorrespondence` with
three reduction fields, and a derived `crystal_basis_reduction`, plus a
"What is NOT claimed here" section. It does not appear in the detector's
`contentless-carrier` list. The bean's own top-priority item was stale by two
days; re-run the detector before working from this list.

**Live detector figures, `scripts/lean-overclaim-audit.py` on main + this branch:**

| | at triage | now |
|---|---:|---:|
| candidates | — | 128 |
| `overclaim-structure` | — | 78 |
| `contentless-carrier` | 39 | **37** |
| `empty-carrier` | 9 | 9 |
| `overclaim-independent-binders` | — | 3 |

Both steps measured separately: 39 → **38** after the Poincaré–Lefschetz fix,
38 → **37** after the Bloch-group one. (This entry briefly carried a 37 that was
a *prediction* — the Bloch file was still being `lean`-checked when it was
written. Corrected to a measurement, then re-measured to the same value.)

**Two category-(a) carriers done — the classical ones, as the triage predicted.**

1. **`conj:poincare-lefschetz-borromean`.** Poincaré–Lefschetz duality and
   `H₁(S³∖𝓑₃) ≅ ℤ³` enter as **cited hypotheses** (the `IsWeilZeta` pattern), not
   as conjectures — encoding settled topology as "conjectural" would misreport it.
   The framework's own claim is the third field, that the top-degree pairing is
   `Vol(𝓑₃)`. Derived: `rankHrel_two_eq_three` (the block's own "in particular
   `H²(∂𝓑₃) ≅ H₁ ≅ ℤ³`" — none of the fields, and it needs two of them),
   `plPairing_eq_eight_catalan`, `plPairing_pos`.

2. **`conj:borromean-bloch-group-element`.** Stronger: the block's headline
   `r₂[𝓑₃] = 8G` is **derived, not assumed**. One classical field
   (`r₂([i]) = Cl₂(π/2) = G`); Thurston's two-octahedron decomposition lives in the
   *definition* `borromeanClass := 8 • [i]`; then `regulator_borromean` gets `8G`
   out of **additivity of the regulator**, so the `8` comes from the group
   structure rather than from a hypothesis. Also derived: the class is non-zero in
   `B` (the block's "non-trivial element of `K₃(ℂ)`"), and the `h⁴` shadow
   `r₂[𝓑₃]·(−3/4) = −6G`.

**Both show non-vacuity from BOTH sides**, which the triage did not ask for and
which is what actually distinguishes a content-bearing field from a decorative
one: a witness satisfying the fields, *and* a theorem that a specific datum does
**not** satisfy them (`b₁ = 2` fails one; a vanishing regulator fails the other).
Both witnesses are `theorem`s, never `instance`s — as instances the next reader is
invited to add one to a datum not constructed to satisfy the fields
(`trivialSkeinGenerationContext`, `qou-skgn`).

**What each file does NOT formalise is written in the file**, not left implied:
no manifold-with-cusps machinery (the PL block's own "still open" item 3), no
Bloch group / five-term relation / `K₃` construction, `blochI` not forced to be
`[i]` so the ζ₄-vs-ζ₆ care in the block is carried only by the *value*, and the
`h⁴ = −3/4` coefficient taken as a hypothesis rather than re-derived.

Verification: `lean`-direct exit 0 on both; `#print axioms` clean on all ten new
declarations. Sidecars refreshed.

**Remaining category (a) is now empty.** Next is category (b) — four carriers
whose `.md` declares a conditionality the type does not carry — and note the fix
there is **not** just adding a binder: adding `[KazhdanLusztigClassicalLimit]` to a
`holds : Prop` carrier leaves the field just as contentless. Both halves are
needed.


### 2026-09-03 (cont.) — first category-(b) carrier, and a verification trap worth more than it

**`conj:lusztig-canonical-basis-q-eq-1`** done. Category (b)'s named defect is that
the `.md` declares a conditionality the type does not carry — the block's own title
says *"conditional on `conj:kazhdan-lusztig-classical-limit`"* while the type said
no such thing, so the derived primary/dependent graph classified it as a **root**.
The `[KazhdanLusztigClassicalLimit R q]` binder now *is* that edge.

**But the binder alone is not the fix, as this bean already warned.** The field
needed content, and the upstream class supplied the objects to state it over —
`NormalForm`, `KLBasisElt`, `klMap`. Upstream axiomatises the *statistics* half of
the `q → 1` limit; this block is the *decategorification* half. Assumed:
`klMap` is a **bijection** at `q = 1` (the block says the crystal decategorifies
*to* the canonical basis — a map missing part of it would not be onto, one
collapsing two normal forms would lose the count), plus KL positivity and
`P_{w,w}(1) = 1`.

**The payoff is a result neither class has alone.**
`canonicalBasis_statSign_pm_one`: upstream gives `statSign = ±1` on the *image* of
`klMap`; surjectivity here extends it to **every** canonical basis element. That is
what a §3b-cond conditional result should look like, and it is why the binder earns
its place rather than decorating the signature.

Detector: contentless-carrier **37 → 36**. Running total this tranche 39 → 36.

**🛑 The verification trap this turned up is the more valuable finding.**
`lean`-direct against the restored `lake-cache` oleans checks your file against
**the cone as it was when the cache was seeded**, not against your checkout.
Measured: `KazhdanLusztigClassicalLimit.olean` dated **2026-07-02**, source last
changed **2026-08-25** — in the commit that *added* the load-bearing `q = 1 →`
hypothesis. Correct code failed with an error pointing at my call site, and **I
first blamed dot notation and wrote that wrong diagnosis into a source comment**
before checking the signature with `#check`. Fix: build the cone from current
source into a scratch dir and prepend it to `LEAN_PATH` (four modules, under a
minute); never `lake build`, which evicts the restore. Recorded as a TRAP in
`.claude/agent-memory/lean-verifier/MEMORY.md` with the worked case in
`verification-harness.md`.

**Scope, so this is not read as wider than it is:** a stale cone does not
invalidate every restore-based green. The two carriers earlier in this tranche
import `BorromeanVolumeCatalan` (source 2026-08-30, olean 2026-07-02); one commit
touched it in that window and `git diff` shows **zero** changes to any `vol_B3` /
`catalan_G` line, so those greens stand. Measure the declarations you used.

**Note for whoever prunes:** `lean-verifier/MEMORY.md` is **383 lines** against the
~200 the injection budget allows, so roughly half of it is not reaching the agent.
It was 362 before this entry. Pruning someone else's TRAPs is not mine to do
unilaterally.


### 2026-09-03 — category (b) is 1 doable of 4, and the triage above mis-sorts one of them

Measured after doing `conj:lusztig-canonical-basis-q-eq-1`. **Category (b)'s stated
fix — "adding a binder the prose already asserts" — is structurally impossible for
three of its four members**, for two distinct reasons. Where each upstream class
lives decides it:

| downstream (category b) | its upstream | upstream class lives in | content-bearing? | doable? |
|---|---|---|---|---|
| `lusztig-canonical-basis-q-eq-1` | `KazhdanLusztigClassicalLimit` | **library** `lean/QOU/BraidKnot/` | yes | ✅ **done** |
| `kashaev-density-equals-sdp-multiplicity` | `VolumeConjecture` | **content-block sibling** `mass-theory/` | yes | ❌ unimportable |
| `spin-from-so3-fiber` | `isospin`/`color-tube` | sibling / **absent entirely** | **`holds : Prop`** | ❌ |
| `wigner-su4-from-spin-isospin` | `spin-from-so3-fiber`, `isospin-from-canonical-bowtie` | siblings | **both `holds : Prop`** | ❌ |

**Reason 1 — siblings cannot import siblings, so a sibling-resident upstream class
cannot be bound.** Confirmed structurally, not from a docstring:
`folio/quantum-observable-universe/lean/lakefile.toml` declares
`globs = ["QOU", "QOU.+"]` with `srcDir = "."` (the `lean/` dir), so a file at
`mass-theory/foo.lean` has no module name at all. Corroborated by measurement:
**every** `^import QOU.` line in a sibling resolves to a library module
(`QOU.Basic`, `QOU.MathlibExt.*`, `QOU.BraidKnot.*`) — not one sibling imports
another. `conj:kashaev-density-equals-sdp-multiplicity` is otherwise the most
tractable item in the whole bean (a crisp integer identity `ρ_F = ν_SDP` with three
confirmed atoms), and it is blocked purely on `VolumeConjecture` sitting in
`mass-theory/kashaev-volume-conjecture.lean:51` instead of the library. Promoting
it is a refactor with its own blast radius, **not** a carrier fix — it is the
`IsWeilZeta` move (that class was promoted to a library module for exactly this
reason, and its docstring says so).

**Reason 2 — binding to a `holds : Prop` upstream buys nothing.** You would get a
theorem conditional on `True`. Both of `wigner-su4`'s upstreams are contentless
carriers, so it is transitively blocked; and one of them,
`conj:isospin-from-canonical-bowtie`, is this bean's own **category (d)** (the
305 ppm near-match needing the owner). So `wigner-su4` is owner-blocked through
its dependency, which the triage does not say.

**🛑 `conj:spin-from-so3-fiber` is mis-sorted — it is not category (b).** Its own
`authorNotes` (2026-06-01, audit `2026-06-01-s5-so3-su2-u1-fiber-action.md`)
records that the stated mechanism is **falsified**: the premise that `S₃` "sees
only ℓ ≤ 1" is false (the (2,1) irrep appears at ℓ=1 mult 1 *and* ℓ=2 mult 2), and
the icosahedral story lives on `A₅ ⊂ S₅` (5 strands) while `h⁴ = −3/4` lives on the
`H₃` trace (3 strands) — *"different representation rings with no canonical map,
so the ℓ=2 ⟹ h⁴ link is not derivable as written"*. That is the same
do-not-launder situation as `conj:magic-numbers-from-q`, not a missing binder.

What survives there is sharp and worth someone's time: **spin-ℤ₂ ≠ sign-ℤ₂**,
because the binary icosahedral group `2I` is perfect while `|2I| = 120 = |S₅|` and
`2I ≇ S₅`. That is provable in the abstract form *"a perfect group is not
isomorphic to a non-perfect one"* — but note this Mathlib has **no `IsPerfect`**
(grepped: zero hits), so it would be spelled `commutator G = ⊤` by hand.

**Revised order, replacing the one above.** (1) `kashaev-density` **if** the owner
wants `VolumeConjecture` promoted to the library — one small refactor unblocks the
bean's best remaining item. (2) `spin-from-so3-fiber`'s surviving positive as a
standalone proved lemma, leaving the falsified mechanism unencoded. (3) everything
else waits on the owner.

**Also dead here:** `wigner-su4`'s classical core (`Λ⁴` of a 4-dim space is
1-dimensional, i.e. four nucleons fill the singlet) is **not cheap** — this
Mathlib has no `Mathlib/LinearAlgebra/ExteriorPower/` and
`exteriorPower.finrank_eq` is an unknown identifier. Probed, not assumed.


## 2026-09-05 — progress, and one entry whose prescribed action is WRONG

Three of this list worked in order (D9 → D10 → D11), reading each block first per
*"not mechanical … do not batch-rewrite"*. Two repaired; the third is mis-scoped.

**Repaired, in the prescribed shape** — content encoded as caller-supplied
parameters so the class is refutable, refutability discharged as a theorem, **no
instance** provided:

- `IsospinFromCanonicalBowtie` (D9) — PR #6671. Content is the block's
  `Δm/M_N = ℏ_q²·h·[2]_q·(1+ℏ_q³)/3`; conventions **read from the producer**
  `verify_isospin_bar_anomaly.py`, and one would have been wrong if guessed —
  `[2]_q` there is the **symmetric** `q + q⁻¹`, not `QGenericBase.qBracket`'s
  unbalanced `1 + q`.
- `SpinFromSo3Fiber` (D10) — PR #6683. Content is the block's own named missing
  object, the level → Wedderburn-coefficient map, constrained at `h² = 0` and
  `h⁴ = −3/4`. The block's Family-A identity is **derived as a theorem**, not
  axiomatised. Guard case applied: the functor's *construction* is left unstated
  and what must grow first is named (a level type indexed against `H₃`'s blocks).

**🛑 `WignerSu4FromSpinIsospin` (D11) — the same repair would be WRONG.** A
substantive D11 carrier already exists: `QOU.WignerSU4FromSpinIsospin` at
`lean/QOU/ParticleInteractions/WignerSU4FromSpinIsospin.lean` (imported at
`QOU.lean:421`), with two real parameter-quantified fields
(`E_gate = E_0·log(1/W_λ)`, `c_λ = B_AME/E_gate`) plus three `: True` fields that
each carry an `opaque marker` docstring naming why they are unstatable. The `.ts`
refs the **stub** instead — the names differ by **capitalisation and namespace**
(`WignerSu4` in `QOU.BraidsAndKnots` vs `WignerSU4` in `QOU`), and the stub's own
header named a third path that does not exist.

So this is **this bean's own shadow case**, a fifth one its 18 → 16 → 12 correction
could not catch: that pass keyed on *"the ref's leaf name in a differently-named
file"*, and here the file name matches while the case and namespace do not.
Writing content into the stub would create a second D11 competing with the real
carrier. **The defect is the ref, not the encoding.**

Blast radius measured: **zero consumers** of either class. The ref repoint is left
as an author decision (§0a prefers candidate-2 resolution, which would need a
namespace alignment in a directory that has no single convention). Finding:
`docs/audits/2026-09-05-d11-is-a-mis-ref-not-a-vacuous-carrier.md`.

**Net for this queue:** two closed, one re-classified. The syntax count is right;
for D11 the implied action is not.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 89 Formalization (`litlfred/qou#8474`)
- Formalized in `QOU.Foundations.AxiomDischargedScopeUnencodedCarrierFilterDownstreamInstanceBindingDeLaunderedEnrichmentSiblingPreservationRebuild` (`folio/quantum-observable-universe/lean/QOU/Foundations/AxiomDischargedScopeUnencodedCarrierFilterDownstreamInstanceBindingDeLaunderedEnrichmentSiblingPreservationRebuild.lean`).
- 80-dps `mpmath` probe & 2-commit witness (`849ef0b15f72606c848eb897a5fda003d289f504` -> `2fff5cb2db76633d952c403baec2a6519c2cf61d`, `scriptHash = scriptSha256 = 2a824ebc8929957fb1b4acfb6fc295d57631c4e806a1217ab45cd79c79b1902b`).
- PR: https://github.com/litlfred/qou/pull/8474
