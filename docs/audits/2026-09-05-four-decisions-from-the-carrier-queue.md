# Four decisions the carrier queue surfaced, and what each one costs

**Date:** 2026-09-05
**Beans:** `qou-tsnp`, `qou-hprp`
**Status:** decision brief. **Nothing here is applied.** Each item is a choice for the
author, with the evidence, the options, and a recommendation marked as agent judgement.

---

## Why these four, and why now

Repairing the `holds : Prop` carriers turned up four things that are **not** the agent's
to settle. Three are claims in content blocks that a standing owner ruling has already
overtaken; the fourth is a systemic bit of rot. In each case I encoded what was safe and
left the contested part alone rather than resolving it by choosing what to formalise.

The default for every one of them is **do nothing** — nothing is broken today, no build
fails, and each is stated so you can defer with confidence.

---

# Decision 1 — the D11 ref points at a carrier that asserts nothing

## What is being decided

Block `conj:wigner-su4-from-spin-isospin` (D11, Wigner SU(4)) points its Lean reference at
a **vacuous stub** while a **substantive carrier** for the same conjecture exists
elsewhere in the tree. Which one the block should point at is the decision.

## The evidence

| | fully-qualified name | file | content |
|---|---|---|---|
| **stub** (what the `.ts` refs) | `QOU.BraidsAndKnots.WignerSu4FromSpinIsospin` — lower-case `u` | `nuclear-interactions/wigner-su4-from-spin-isospin.lean:50` | `holds : Prop` — nothing |
| **library** | `QOU.WignerSU4FromSpinIsospin` — upper-case `U` | `lean/QOU/ParticleInteractions/WignerSU4FromSpinIsospin.lean:15` | 2 real fields + 3 labelled markers |

The `.ts` carries `ref: "qou:QOU.BraidsAndKnots.WignerSu4FromSpinIsospin"`. The library
carrier is imported at `QOU.lean:421` and holds
`dynamic_capacity_from_plancherel_weight` (`E_gate = E_0 · log(1/W_λ)`) and
`dynamic_occupancy_c_lambda` (`c_λ = B_AME / E_gate`), plus three `: True` fields that
each carry an `opaque marker` docstring naming why they are unstatable.

**Consumers: zero on both classes**, beyond the library's own file and the `QOU.lean`
import. Nothing depends on either, so nothing breaks whichever way this goes.

## 🛑 A correction to my own earlier framing

PR #6711 said the repoint was hard to do unilaterally because *"that directory has no
single convention"* — `QOU.Atomicity`, `QOU.ParticleInteractions`, `QOU.BraidKnot` and
bare `QOU` all appear under `ParticleInteractions/`. **That was the wrong place to look
for the convention.** The relevant precedent is not the directory's; it is **what the
sibling carrier in this same queue did**.

`TFromTraceCyclicity` is the worked example, and it is unambiguous:

- its content stub is **deleted**;
- its `.ts` refs `qou:QOU.BraidsAndKnots.TFromTraceCyclicity`;
- its library file declares `namespace QOU.BraidsAndKnots` — **matching the ref exactly**.

So the queue already contains a finished instance of this exact disposition, and it put
the library carrier under `QOU.BraidsAndKnots` rather than leaving it under a namespace
that does not match the ref.

## Options

### (a) Follow the `TFromTraceCyclicity` precedent — **recommended**

**What it means.** Move the library class into `namespace QOU.BraidsAndKnots`, align its
capitalisation to the ref (`WignerSu4` vs `WignerSU4` — pick one), delete the vacuous
stub, leaving the `.ts` ref resolving to the real carrier by §0a candidate-2.

**What it costs.** One namespace line, one case fix, one file deletion, one `QOU.lean`
import path unchanged (the import is by module path, not namespace). Under an hour.

**What it risks.** Almost nothing measurable: zero consumers on both classes. The only
real risk is the capitalisation choice propagating — pick the ref's spelling and the
`.ts` needs no edit at all.

**What it commits to.** Treating `QOU.BraidsAndKnots` as the namespace for
conjecture-carrier classes referenced from content blocks, which is what
`TFromTraceCyclicity` already established.

### (b) Repoint the `.ts` to the library's current FQN

**What it means.** Change the ref to `qou:QOU.WignerSU4FromSpinIsospin`, delete the stub,
leave the namespace as `QOU`.

**What it costs.** Two lines. Fastest option.

**What it risks.** Resolution then works only through §0a's **candidate-3 grep fallback**,
not candidate-2. That is supported but is the weaker path, and it diverges from the
precedent in (a) for no gain.

**What it commits to.** Nothing much — but it leaves the corpus with two different
dispositions for the same situation.

### (c) Do nothing — the default

**What it means.** The block keeps pointing at a carrier that asserts nothing.

**What it costs.** Nothing today.

**What it risks.** Any future `[WignerSu4FromSpinIsospin]`-conditional theorem is
conditional on nothing, and a reader who follows the block's Lean reference finds the
empty carrier rather than the real one. The census beans keep listing D11 as needing
content, which is the wrong action for it.

## Blast radius in real terms

Zero consumers, so no proof or compute changes. What changes is which declaration a
*reader* — human or agent — lands on when following the block's Lean reference, and
whether the D11 entry in `qou-tsnp` / `qou-hprp` can be closed truthfully.

## Recommendation *(agent judgement)*

**(a).** It is barely more work than (b), it matches a precedent already in this queue,
and it leaves candidate-2 resolution working. My earlier hesitation was based on looking
at the wrong reference class.

---

# Decision 2 — the Kashaev block's ²H evidence row is retired by your own ruling

## What is being decided

`conj:kashaev-density-equals-sdp-multiplicity` cites the deuteron as its first piece of
evidence. **Owner ruling A of 2026-08-29 retires that assignment.** Whether to remove,
annotate, or keep the row is the decision.

## The evidence

The block's evidence table, `kashaev-density-equals-sdp-multiplicity.md:34`:

```
| ${}^{2}\mathrm{H}$ (D)  | knot $6_2$        | 1 | 1 |
```

Against
[`2026-08-29-deuteron-knot-owner-decision.md`](2026-08-29-deuteron-knot-owner-decision.md):
the deuteron knot is the **canonical braid closure** (trefoil / Hopf, `Vol = 0`), the 6₂
census assignment (`Vol = 4.40`) is **retired**, and the deuteron binding is **not** a
hyperbolic-volume term (Bloch volume leg proved 0, PR #5242).

**Why this is not cosmetic.** The block's formula is
`B_pred(K) = ρ_F · m_e · Vol_hyp(K)`. At `Vol = 0` it gives `B_pred = 0` for **any**
`ρ_F` whatsoever. So the ²H row cannot pin a prefactor — it is not merely using a stale
knot, it is contributing no constraint at all.

The three-point evidence base (²H→1, ³H→2, ³He→2) is therefore really a **two**-point
base, and one of those two is what the conjecture's `1, 2, 2` pattern rests on.

## Options

### (a) Delete the ²H row and say the base is two points — **recommended**

**What it means.** Remove the row; state that the evidence is ³H→2 and ³He→2.

**What it costs.** One table row and a sentence. Minutes.

**What it risks.** It weakens the block's apparent support — from three agreeing points
to two. That is a *disclosure*, not a regression: the third point was contributing
nothing.

**What it commits to.** Accepting that this conjecture's empirical base is thinner than
the block currently reads.

### (b) Keep the row with a retirement note

**What it means.** Leave it, annotated as superseded by the 2026-08-29 ruling.

**What it costs.** A sentence.

**What it risks.** A reader scanning the table still counts three supporting rows. The
note has to be read to undo the impression the table gives, and tables are what get read.

### (c) Rewrite the evidence table against the current deuteron assignment

**What it means.** Re-derive what the canonical-braid-closure deuteron implies here, if
anything.

**What it costs.** Real work — this is a physics question, not an edit.

**What it risks.** May conclude the row simply cannot be rebuilt, landing back at (a).

### (d) Do nothing — the default

**What it risks.** The block keeps citing, as its lead evidence, a row that a standing
ruling retired and that mathematically cannot constrain the quantity it appears to
constrain.

## Blast radius in real terms

`ν_SDP` feeds the mass-table prefactor `ρ_F`, so this touches how strongly the block's
identity reads. It does **not** change any computed number: the Lean carrier merged in
#6734 already excludes the row via `vol_pos`, and `mass_table_ppb.py` is untouched either
way. What changes is the honesty of the evidence presentation.

## Recommendation *(agent judgement)*

**(a).** The row cannot constrain the prefactor at `Vol = 0`, so keeping it — even
annotated — overstates the support. Deleting it and stating the two-point base is the
accurate reading. Worth pairing with the separate finding, established in #6734, that six
operational definitions of `ν_SDP` were computed and **none** reproduces `1, 2, 2`; the
committed values carry methodology `"manual-historical-volume-match"`, i.e. hand-assigned.

---

# Decision 3 — the 3d–3d block asserts an absolute proton mass

## What is being decided

`conj:mirror-3d-3d-correspondence` states the proton mass as the value of a partition
function. Your **ABSOLUTE MASS EXCISED** ruling of 2026-08-11 removed absolute nucleon
mass in MeV as a framework prediction. Whether to remove or restate the claim is the
decision.

## The evidence

`mirror-3d-3d-correspondence.md:9` (prose) and `:15` (table):

```
| $m_p$ | partition function $Z_{T[\mathcal{B}_3]}(q_0)$ on $S^3_b$ |
```

Against AGENTS.md, owner ruling 2026-08-11:

> The framework no longer claims, targets, or scores an **absolute** nucleon or atomic
> mass in MeV (`m_p`, `m_n`, `m_⁴He`) as a prediction.

I declined to encode this row in the Lean carrier (#6737) for exactly this reason, and
flagged it rather than dropping it silently — choosing what to formalise is not the way
to settle whether a claim belongs in the paper.

## Options

### (a) Restate as a dimensionless claim — **recommended**

**What it means.** Replace the `m_p` row with the ratio or dimensionless content the
ruling permits. The block's *other* row — `h⁴ = −3/4` ↔ four-loop coefficient — is
already dimensionless and unaffected, so the block keeps a real claim either way.

**What it costs.** One table row and the sentence at line 9. Small, if a dimensionless
form is available.

**What it risks.** There may be no natural dimensionless restatement of "the partition
function evaluates to the proton mass", in which case this collapses into (b).

**What it commits to.** Nothing new; it applies a ruling you have already made.

### (b) Delete the row

**What it means.** The block claims only the `h⁴` correspondence.

**What it costs.** Minutes.

**What it risks.** Loses the block's most striking-sounding claim. But that claim is one
the ruling has already excised from the framework, so the loss is presentational.

### (c) Keep it, marked as pre-ruling

**What it risks.** Leaves a live content block asserting something a standing ruling
removed. This is the case the ruling exists to prevent.

### (d) Do nothing — the default

**What it risks.** Same as (c), without even the marking.

## Blast radius in real terms

No compute, no Lean, no witness. It is a claim in a content block that reaches the paper.
The exposure is that a referee reading the paper finds an absolute-mass prediction the
project has internally ruled out — which is precisely the kind of inconsistency the
2026-08-11 ruling was made to close.

## Recommendation *(agent judgement)*

**(a) if a dimensionless restatement exists, otherwise (b).** I cannot tell from the
block alone whether `Z_{T[B₃]}(q₀)` has a natural ratio form; that is a physics question.
What is clear is that the row cannot stay as written.

---

# Decision 4 — seven content stubs advertise Lean files that do not exist

## What is being decided

Whether to sweep a systemic bit of rot, or keep fixing it as encountered.

## The evidence

Seven live stubs carry a header of the form *"the class axiomatisation lives at
`../lean/QOU/…/X.lean` (file pending)"* where **the file does not exist**:

```
reverse-limit-q-to-infinity.lean    -> ../lean/QOU/BraidsAndKnots/ReverseLimitQToInfinity.lean
kashaev-density-equals-sdp-…        -> ../lean/QOU/Kashaev/DensityEqualsSDPMultiplicity.lean
dim-master-pentagon.lean            -> ../lean/QOU/BraidsAndKnots/DIMMasterPentagon.lean
quantum-langlands-dual.lean         -> ../lean/QOU/BraidsAndKnots/QuantumLanglandsDual.lean
mirror-3d-3d-correspondence.lean    -> ../lean/QOU/BraidsAndKnots/Mirror3d3dCorrespondence.lean
wigner-su4-from-spin-isospin.lean   -> ../lean/QOU/BraidsAndKnots/WignerSU4FromSpinIsospin.lean
type-b-folding-cpt.lean             -> ../lean/QOU/BraidsAndKnots/TypeBFoldingCPT.lean
```

**Correction to my own earlier report:** I said "three" of these, because three is what I
personally hit while repairing carriers. Measured across the tree it is **seven**. Four of
the seven were fixed in passing during this session's repairs (Kashaev, pentagon, 3d–3d,
D11's header); the count above is what the pattern looks like corpus-wide, before those
landed.

Several also name a class that does not match the declared one (`DIMMasterPentagon` vs
`DimMasterPentagon`; `WignerSU4` vs `WignerSu4`), so the pointer is wrong in two ways.

## Options

### (a) Sweep all seven — **recommended**

**What it means.** One pass replacing the dead "(file pending)" sentence with what is
actually there.

**What it costs.** Docstring-only edits; no Lean semantics change, so `lean`-direct
confirms each file still compiles and nothing else moves. An hour or two.

**What it risks.** Very little. The only hazard is doing it *mechanically* — several of
these headers are wrong in more than one way, and a find-and-replace would fix the path
while leaving the wrong class name.

**What it commits to.** Nothing structural.

### (b) Fix as encountered — the status quo

**What it costs.** Nothing up front.

**What it risks.** These pointers actively mislead: each one tells a reader a real
formalisation exists elsewhere. On D11 that reading was *nearly right* and cost a wrong
turn — I began writing content into a stub before checking, and the file the header named
was not the file that actually holds the substantive class.

### (c) Do nothing — the default

**What it risks.** The rot persists at seven and grows with each new stub minted from the
same template.

## Blast radius in real terms

No build, no proof, no number. This is entirely about what a reader — increasingly, an
agent — believes when it follows a pointer. The measured cost so far is one wrong turn
per encounter.

## Recommendation *(agent judgement)*

**(a), but by hand, not by script.** The population is small and the errors are
heterogeneous. This is also the cheapest of the four decisions and the only one with no
physics content, so it is a good candidate to delegate.

---

## Summary

| # | decision | default if you say nothing | my recommendation |
|---|---|---|---|
| 1 | D11 ref points at a vacuous carrier | block keeps pointing at nothing | **(a)** follow the `TFromTraceCyclicity` precedent |
| 2 | Kashaev ²H evidence row | block cites a row that cannot constrain | **(a)** delete it; state the two-point base |
| 3 | 3d–3d `m_p` row | block asserts an excised claim | **(a)** restate dimensionless, else **(b)** delete |
| 4 | seven dead Lean pointers | rot persists and grows | **(a)** sweep by hand |

None of the four blocks anything. Decisions 2 and 3 are about what the paper claims;
decision 1 is about what a reference resolves to; decision 4 is hygiene.
