---
# qou-88nf
title: 'Conjecture carrier: BlowupYekutieli — fabricated trivial-zero instance, asserts nothing'
status: todo
type: task
priority: normal
created_at: 2026-08-29T19:46:36Z
updated_at: 2026-08-30T07:35:59Z
parent: qou-rq9n
---

Carrier at ConditionalClasses.lean:79; instance `blowup_yekutieli_canonical` at :113.
Field: `exists_blowup_rate : forall (T : R), 0 <= T -> exists r : R, 0 <= r /\ r <= 1 + T`.
Discharged `<0, le_refl 0, by linarith>`.

Docstring promises "the blow-up exponent is bounded above by an explicit
constant determined by the substrate scale"; the encoded bound is `1 + T`,
which involves no substrate scale, and is satisfied by r = 0 -- i.e. by NO
blow-up, the negation of the claim the class is named for.

Bound as `[BlowupYekutieli]` in **4** files (the only one of the five not at 5).
Ledger entries: 0. Parent: qou-rq9n.



## STILL OPEN 2026-08-30 — and now the ONLY vacuous carrier in the file (PR #6122)

Its three siblings were re-encoded and left the vacuous population; `CriticalExponent`
had already. This one could not be, and the reason is specific rather than effort:

**The docstring names a bound it never gives.** "An explicit constant determined by
the substrate scale" says a constant exists and not which. The encoded bound
`1 + T` involves no substrate scale at all and is satisfied by `r = 0` — by NO
blow-up, the negation of the claim the carrier is named for.

The other three were fixed by transcribing a claim their docstrings already made.
Writing a bound here would mean **choosing the constant myself**, which is the step
separating transcription from invention: `r <= f(q0)` for an `f` I picked would
look exactly like the other three fixes and be a fitted value wearing their clothes.

**What closing it needs**, so this is not re-derived: the Yekutieli blow-up rate as
an explicit function of the substrate modulus, from the source `conj:blowup-yekutieli`
points at. With that in hand the encoding is the same shape as its siblings — the
exponent as a class parameter, the field bounding it by that function, and the gate
a refutation probe showing some rate is excluded.

Stated at the declaration in ConditionalClasses.lean so a reader hits it there.



## MEASURED 2026-08-30 — the rate is NOT IN THE CORPUS, and the name is borrowed

Full write-up: `docs/audits/2026-08-30-blowup-yekutieli-has-no-source.md`.

I went looking for "the Yekutieli rate as an explicit function of the substrate
modulus", which is what I said this bean needed. **It is not there, and the
reason is structural rather than a gap in my search.**

**The corpus's Yekutieli is Amnon Yekutieli, *Central Extensions of Gerbes*
(Adv. Math. 2010) — pure algebra.** Counted over live content: "Yekutieli
lifting" 92, `YekutieliTriple` 86, "Yekutieli obstruction" 45, "Yekutieli
Stokes" 29, "Yekutieli tower" 6, "Yekutieli volume" 2. **Yekutieli blow-up
rate or exponent: 0.** Every use is the gerbe-lifting/obstruction framework or
the non-abelian Stokes theorem in the derivation chain.

**Six-path corpus-grep, all negative:** docs/audits (only this carrier's own
trail); content (`blow-up exponent` appears ONCE, in the carrier's own
docstring); computations (a volume witness, rest `_deprecated/`);
docs/coordination (one hit and it says *"Not the q-NS PDE solve (blowup
exponent) — survey research target"*, i.e. recorded as NOT DONE); library —
3 ingested docs mention Yekutieli, **none** pairs him with blow-up; beans.

**The sharper finding: its conjecture block does not exist.** The four siblings
each have one — q-aubin-lions.ts, p5-counterexample.ts, p2-critical-exponent.ts,
regularity-breakdown.ts. **Zero `.ts` blocks declare `conj:blowup-yekutieli`**,
yet the Lean cites it. That is exactly why transcription was impossible here and
worked for the other four: there was no upstream statement.

A `p3-blowup-yekutieli` block DID once exist (ch10-fluid-dynamics/,
ch6-descartes-universe/, plus a .lean) and is gone. Recovering its last
committed .md does not help — its content is the REGULARITY-BREAKDOWN argument
(smoothness as lifting, `v` smooth iff `kappa_n(v) = 0`), with no blow-up
exponent in it.

**This is the borrowed-name class** that sibling bean `qou-0avp` targets: named
after an external theory whose statement is entirely local. Scope (a), not (b) —
this says the rate is not HERE, not that none exists.

**AUTHORIAL, three options, none mine:**
1. Write the missing conjecture block stating the rate; then transcribe as with
   the other four.
2. **Rename** — if the intended content is the lifting obstruction (which is
   what the corpus's Yekutieli material IS, and what the deleted p3 block
   contained), the encoding should be against `kappa_n`, not a blow-up bound.
3. **Retire it** — one live consumer leg remains, the fourth conjunct of
   `qNS_cone_full_composition`, which is the one conjunct still satisfied by zero.

**Recommendation (my judgement, not a finding): option 2.** The corpus has
substantial Yekutieli *lifting* material and none about blow-up, so the name most
likely drifted from the obstruction framework onto a blow-up claim it never
described. But renaming a conjecture carrier is an authoring decision.
