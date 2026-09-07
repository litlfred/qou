---
# qou-9yt9
title: 'A+C: land the ConfinementLevel refactor and the DressedParticle shadowing fix'
status: in-progress
type: task
priority: high
created_at: 2026-09-06T09:08:06Z
updated_at: 2026-09-07T09:02:41Z
---

## Landed (A + C)

**A — ConfinementLevel refactor.** `level_canonical` deleted; `valid` is now a
parameter indexed by `BraidDatum` with `level_valid`/`level_min` as proof
fields. `unique` is a one-line theorem, `nonempty` a real `Nat.find`
construction, `level_eq_find` new. **No axioms at all** on all three — not even
`propext`. Registered in the axiom guard, exit 0.

Also repaired `prop:confinement-level-exists`, unplanned: its Lean backing was
the junk record `⟨0,1,0,0⟩`, proving the *type* inhabited rather than that any
braid has a level.

`.md` rewritten: its three stated reasons over-attributed — uniqueness needs
only antisymmetry, and neither monotonicity nor upward-closure does any work in
it. Both kept, correctly scoped.

**C — DressedParticle unshadowed.** The library had already done the refactor
its sibling called "pending" (`shell_on_bare`, `level_preserved` as proof
fields; `dressing_composes` proved from them). Sibling replaced by a witness
extract, matching the pattern `confinement-level-exists.lean` already used.

Axioms 136 → 134, flagged 21 → 19. All touched files lean-direct exit 0;
`check-sidecars` exit 0.

## Two traps recorded

1. **The root `.lake` olean tree precedes the paper's in `LEAN_PATH`**, so a
   `lean-direct-cone.sh` rebuild into the paper tree is INVISIBLE — the stale
   root copy shadows it. Three files reported spurious unknown-identifier errors
   until the paper tree was put first. Root olean 09:08:28 vs source 09:09:25 vs
   paper-tree olean 09:11:28.
2. **`check-sidecars.sh` prints `→ refresh` UNCONDITIONALLY** for every changed
   content-block `.lean` (line 107). It is an advisory reminder, not a staleness
   verdict, and it does not set the failure flag. I misread it as a failure for
   several turns; the discriminator is the `⚠` lines and the exit code.


## NINTH false axiom — `KnotOperatorEnergy.shadowPrice_canonical` (same class, refactored)

`climax-volume-mass/knot-operator-energy-unique.lean`. Plain structure with
`shadowPrice : R` free; the axiom asserted two records agreeing on
`partition` and `q` share it. Refuted by `⟨[],0,0,none⟩` vs `⟨[],0,1,none⟩`.
**Third docstring in this family to name its own defect** — *"requires ... a
structure refactor carrying the LP-canonicity as a proof field."*

Same three-way pattern as #7: false uniqueness axiom **plus** a junk-record
existence witness (`{partition := [1], q := 0, shadowPrice := 0}`), so
`prop:knot-operator-energy-exists` was vacuously backed too.

**Applied the owner's A ruling by analogy** — same defect class, and no library
counterpart exists (unlike #8), so the refactor was the only option that keeps
the claims. One design choice worth naming: the determining data is carried as
a **function** `dualValue : List ℕ → R → R` with `shadowPrice_eq`, NOT as a
relation with a uniqueness field. A structure carrying its own conclusion would
be the self-assuming projection AGENTS.md §3b-cond item 5 forbids; here
uniqueness follows from functionality.

The real content — that the LP dual exists and is unique (Schrijver §7.4) — now
sits explicitly in the `dualValue` parameter a caller supplies, instead of
being smuggled in by a witness that ignored its own indices.

Axioms 134 → 133, flagged 19 → 18. All three blocks lean-direct exit 0,
zero axioms; check-sidecars exit 0.

## The docstring sweep — a useful NEGATIVE

Grepping `"proof field" | "not free data" | "does not enforce"` across
`content/` returns 11 files; excluding Mathlib and the already-fixed ones, only
**one** new instance (this ninth). So this family is **three** — #7, #8, #9 —
not an open-ended class. That is a cheaper and far more specific detector than
the over-quantification rules, because it keys on the author having ALREADY
noticed the defect and written it down.


## The class surface (2026-09-07, PR #6987)

Two measurements, opposite directions, both new.

**Vacuity — clean negative.** `scripts/lean-class-hypothesis-vacuity-probe.py`
deletes the instance binder and asks Lean for the conclusion unaided:
**0 of 27 scored provable** (FAIL=27, SKIP=14, NOBASE=0). The same question on
the axiom surface found 8 of 112 (#6933). So the conditional-class surface is
not vacuous — its problem is visibility.

`NOBASE=0` is what makes that usable: every probe compiles the file UNCHANGED
first, since a red baseline fails in the direction that reads as "the class is
load-bearing". The 14 SKIPs are the explicit-structure-argument idiom, which
has no instance binder and is also the idiom that does not hide.

**Reach — 8 paper claims.** `scripts/lean-self-assuming-content-join.py` joins
the 41 self-assuming declarations against every `lean.ref` in `content/`:
8 blocks of provable kind (1 theorem, 6 propositions, 1 corollary, **zero
conjectures**); 7 carry no §3b-cond item-3 banner signal.

**Two of my own errors caught before shipping.** The join first said 9 — it
matched last name segments and paired `prop:quantum-universe-exists` with
`QuantumObservableUniverse.exists_instance`, two real distinct declarations.
And "14 single-field classes are item-5 violations" was too strong: reading
three shows honest §3b-cond carriers. Field count does not decide it.

**Nothing repaired**, deliberately. The banner column measures phrasing, not
honesty — `sw-period-residue-sum` scores NO BANNER over the most scrupulous
narrative in the set, and `prop:quantum-observable-universe-exists` turned out
to carry a worked narrative proof over four cited axiom lemmas.

Audit: `docs/audits/2026-09-07-self-assuming-projection-reaches-the-paper.md`

**Still open:** the opaque-operator disposition (now five, spanning
`IwahoriHeckeAPI.lean` and the vertex-algebra file) needs an author decision.
Follow-up tranche: read the seven no-banner blocks one at a time and add
§3b-cond item-3 banners where genuinely absent — a `.md` repair, not Lean.


## The banner tranche (2026-09-07, PR #7011)

Read the eight projection-backed paper claims one at a time. **Five repaired,
three deliberately left.**

**The discriminator the corpus already had, and I should have used first.**
`qou-z9ws` / `2026-08-30-sizing-the-self-assuming-projection-drain.md`: a
projection is the legitimate Mathlib accessor idiom ONLY when something BUILDS
the bundle. Measured on all eight carriers: **0 builders, every one**. So none
is the accessor idiom — each is a paper claim of provable kind resting on a
hypothesis nothing in the corpus has ever witnessed.

**41 vs 112 reconciled**, neither correcting the other: 112 = `genuine`
verdicts in the vacuity review ledger (of 191) on 2026-08-30; 41 = raw scanner
candidates today, post-`e674c94003`. Different populations, different dates.

**Repaired:** `thm:strong-multiplicativity` (the `.md` asserted, verbatim, the
claim its own Lean docstring says the accessor does not establish — seven
weeks side by side); `prop:categorical-self-duality` (and its Lean docstring's
`variational_einstein` pointer, which goes to the Einstein equation, not the
self-duality step — the Bogomolny derivation is narrative-only);
`prop:flavor-dressed-mass-from-substrate-split` (banner into the prose, since
`authorNotes` are render-skipped; plus the missing `uses[]` edge to
`lem:pair-skein-mass-formula`); `prop:electron-period-base` (`lean.ref`
retargeted to `second_period_contains_me`, which DERIVES the identity the
prose states); `cor:jet-prolongation-C`.

**Left alone, read in full:** `sw-period-residue-sum` (730 words, scrupulous),
`quantum-observable-universe-exists` (worked narrative proof in its `proofs:`
sibling), `categorical-jet-prolongation` (already bannered).

**My own detector was wrong first, in the flattering direction.** A
line-anchored inhabitation grep returns 0 for EVERY carrier including the
known-inhabited controls — this corpus writes instance headers across four
lines with the result type last — and a 0 reads as "uninhabited", the
interesting answer. Caught by a control on `SkeinMultisetInvariant`, read by
hand an hour earlier. `scripts/lean-carrier-inhabited-check.py` scans
declarations, and refuses to report if its control goes missing.
