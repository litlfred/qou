# Promoting the generic `speedOfLight` into the library: three shapes, none free

**Date:** 2026-09-05
**Status:** decision brief. **Nothing applied.** Follow-on to #6834 / #6839 / #6843 / #6846.

---

## The decision

The archimedean `QOU.Information.speedOfLight` in `QOU/MathConstants.lean` and the
generic one in the content-block sibling `information-theory/information-speed-of-light.lean`
are the same quantity twice. #6839 proved the archimedean one is the generic one at
`ℝ`; #6846 fixed the live defect (it returns `0` at classicality, where its own
docstring said it diverges). **What remains is whether to reduce the two to one, and
that turns out to have three shapes with different costs — none of them free.**

I said in three PR bodies that the follow-on was "promote the generic definition into
the Lake tree so the `ℝ` form becomes a theorem over it". Measured, that sentence hides
the actual constraint.

## The constraint, measured

**A `definition` block needs a *resolvable ref*, not a co-located file.** AGENTS.md's
summary says *"`definition` requires a sibling `.lean`"*, but `DefinitionBlock` in
`folio-assistant/schemas/types.ts:727` requires `lean : LeanRef`, and the comment at
`:724` reads *"`.lean` sibling exists **(or `companions.lean` resolves)**"*. §0a's
three-candidate resolution is the mechanism, and `TFromTraceCyclicity` is the worked
precedent — stub deleted, ref resolving to the library. So deleting the sibling is
**allowed**.

**But the library cannot hold both under one name.** Promoting the generic definition
into `QOU/` as `QOU.Information.speedOfLight` collides with the archimedean
`QOU.Information.speedOfLight` already in `MathConstants.lean`. Per
[`scripts/lean-duplicate-fqn-audit.py`](../../scripts/lean-duplicate-fqn-audit.py)'s own
rationale, two modules declaring one FQN **can never both be imported** — Lean rejects
the second with `environment already contains`. So promotion forces a choice about the
archimedean one.

**Blast radius, measured.** Consumers of the archimedean `speedOfLight`: exactly three,
all in `MathConstants.lean` — `gravitationalConstant_planck_units` (line 137),
`speedOfLight_positive` (142), `speedOfLight_junk_at_classicality` (159).
`mass-energy-equivalence.lean` declares its own `speedOfLightSq (q : ℝ)`; it is a
different declaration, **not** a consumer. Outside that file: none.

The one that costs is `gravitationalConstant_planck_units`. Its proof runs through
`planck_identity`, a private lemma discharged by `field_simp; ring_nf; field_simp; ring`
with six non-vanishing side conditions established by `linarith`/`nlinarith`. Rewriting
it against unit arithmetic is not a substitution; it is a re-proof.

---

## The three shapes

### (a) Replace — one definition, the generic one

**What it means.** Move the sibling's content into `MathConstants.lean` (or a new
`QOU/Information/SpeedOfLight.lean`), delete the archimedean declaration, delete the
sibling, repoint the block's ref. Rewrite the three consumers against units.

**What it costs.** A re-proof of `planck_identity` in unit arithmetic. That is the
delicate one; the other two consumers are one line each.

**What it risks.** `planck_identity` is the only thing standing behind
`gravitationalConstant_planck_units`, which is a *physics* claim (G = 1 in Planck
units). Breaking or weakening it to tidy a naming issue is a bad trade, and "I could not
re-prove it" is a live outcome.

**What it commits to.** The generic form as canonical for this quantity, and the
precedent that archimedean forms are applications rather than declarations.

### (b) Promote alongside — a second namespace

**What it means.** Put the generic definition at, say,
`QOU.Information.Algebraic.speedOfLight`, keep the archimedean one where it is, prove
the bridge theorem in the library, repoint the block's ref at the generic one, delete
the sibling.

**What it costs.** One new module, one bridge theorem, one ref edit. Touches no existing
proof.

**What it risks.** It is a **naming decision** — the thing I retracted in #6834 — wearing
a different hat. The retraction's argument was that a suffix convention blesses two
independent definitions; a namespace does the same with a dot instead of a suffix. The
difference is that here the two would be *tied by a proved bridge* rather than merely
coexisting, which is what `GroundRingEval` does and what the retraction endorsed. Whether
that difference is real or a rationalisation is exactly the judgement being asked for.

**What it commits to.** An `Algebraic`/archimedean namespace split, corpus-wide, by
precedent.

### (c) Do nothing — the default

**What it means.** The pair stays as a documented §7c mirror. #6846 already fixed the
live defect and recorded the junk value as a theorem; the mirror-drift baseline already
holds the entry as visible, ratcheted debt.

**What it costs.** Nothing.

**What it risks.** The duplication persists and the baseline does not drain. Note it is
**not** currently misleading anyone: the block's checkers read the sibling, and the
sibling is the correct §7c statement.

---

## Recommendation *(agent judgement)*

**(c) for now, (b) if you want the baseline to drain.** Not (a): re-proving
`planck_identity` to resolve a naming redundancy puts a physics claim at risk for a
tidiness gain, and this arc has already shown four times that the tidy-looking problem
is smaller than it appears.

The honest summary is that **the remaining item is cosmetic and the last substantive
thing here was fixed in #6846.** I would rather say that than manufacture a fifth step.

## Record: how many times this follow-on changed shape

| stage | claim | corrected by |
|---|---|---|
| #6834 | "needs a corpus-wide archimedean-naming convention" | reading `GroundRingEval` — the corpus rejects positing-beside |
| #6839 | "four live defects" | reading the type's axioms — two unreachable |
| #6843 | "two live defects" | reading the consumer's class — one is an unguarded signature |
| #6846 | "promote so the `ℝ` form becomes a theorem" | reading the schema and the FQN-collision rule — promotion has three shapes |

Every correction came from reading something I had not read, and every one made the
remaining work smaller. That is the pattern worth carrying forward, and the reason this
brief stops rather than proposing a fifth step.
