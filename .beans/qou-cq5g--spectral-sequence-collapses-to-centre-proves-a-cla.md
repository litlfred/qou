---
# qou-cq5g
title: spectral_sequence_collapses_to_centre proves a class-field projection, not the collapse
status: in-progress
type: task
priority: normal
created_at: 2026-08-25T21:16:54Z
updated_at: 2026-08-26T03:07:38Z
---

`QOU.WedderburnMass.spectral_sequence_collapses_to_centre`
(`content/quantum-observable-universe/mass-theory/spectral-sequence-collapse.lean`)
has conclusion

    forall i : I.central_idempotents, I.e i * I.e i = I.e i

and body `fun i => I.e_idem i`. It re-exports a class field. It does not mention
E_infinity, does not mention a filtration, and **never uses its own
`[WhiteheadHH R A]` instance** — the hypothesis the whole result is supposed to
turn on. The docstring immediately above states the E_infinity result, so the
gap is docstring-vs-type, the §3b-cond item-5 self-assuming shape.

The block's `.ts` carries `validation: "not_checked"`.

**It is not in `docs/audits/lean-vacuity-review-ledger.json`** — grepped
2026-08-25, no entry — so no agent verdict has ever been recorded against it.
That is the actionable part: it is a library-adjacent declaration whose shape is
exactly what the ledger exists to catch, and it has never been seeded.

**Honest dispositions** (per the AGENTS.md rubric), in preference order:

1. Rename to what it proves (`centralIdempotent_idem` or similar) and let the
   collapse be stated separately — cheapest, and removes the mis-citation
   without asserting anything new.
2. State the real proposition with `sorry` + `-- Ref:` and mark `has_sorry`.
3. Demote the collapse to a `conjecture` carrier alongside `WhiteheadHH`.

**Do not "fix" it by proving the collapse.** Mathlib has no Hochschild-cohomology
framework (the file says so), and — separately and more fundamentally — the
filtration whose collapse is asserted is not defined: all three corpus readings
of `J^bullet` are excluded (`2026-08-16-three-gb-filtrations-one-name.md`). There
is no spectral sequence here yet to collapse.

Analysis: `docs/audits/2026-08-25-spectral-sequence-is-a-no-go-not-a-tool.md` §2.


## THIS WAS FOUND IN JUNE AND CLOSED ON A MISREADING (2026-08-25)

My original entry said this was a new finding, "not in the vacuity review
ledger", with "no agent verdict ever recorded". **That framing was too narrow and
the real story is worse.**

**1. It was found on 2026-06-07.** `docs/audits/2026-06-12-qa-drain-r5r6-findings.md`
§2.3 carries the row verbatim: *"Lean only proves `e*e=e` idempotency"*.

**2. It was closed as stale, and the section is headed "Superseded by `main`
(do NOT re-file)".** So the record actively instructed future agents not to look
again. Two and a half months.

**3. The dismissal's evidence is all TRUE and all IRRELEVANT.** It reads:
*"Developed: now `class SemisimpleAlgebra`, `class WhiteheadHH`, real
`innerDerivation`, `theorem spectral_sequence_collapses_to_centre`,
`wedderburnWeight`/`plancherelWeight`. Finding is stale."* Every one of those
additions happened. **None changes what the theorem proves** — conclusion still
`e*e = e`, body still `I.e_idem i`, `[WhiteheadHH R A]` still never used.

**The failure mode, named:** scaffolding was added AROUND a vacuous theorem and
the theorem was given an impressive name; the drain then read the presence of a
well-named theorem as answering the complaint that the theorem is trivial. A
declaration's NAME AND NEIGHBOURS ARE NOT ITS CONTENT — only its type and body
are. This is the repo's own "Axiomatization is NOT a Proof" / "sorry-free !=
derived" rule, failing from the inside of a QA drain.

**4. A machine signal agreed with the finding the whole time.**
`docs/audits/lean-triviality.json` carries the declaration with
`"closed": false`, last checked `2026-08-07`. The audit never accepted the
staleness verdict. So the correct statement is not "no verdict was ever
recorded" — it is that a HUMAN-READABLE verdict said stale while the MACHINE
verdict said open, and the human-readable one carried a do-not-re-file marker.

**Correction landed** in the June audit doc: the row is struck through with the
live Lean quoted beneath it, and marked "Do re-file." The other §2.3 rows are
explicitly left alone — each was assessed on its own evidence.

**Consequence for the disposition options above:** unchanged in substance, but
this is no longer routine hygiene. A rename touching `spectral-sequence-collapse.ts`
(`lean.ref`), `definition-index.md`, and a docstring cross-reference in
`phi-q-categorical-truncation.lean` is a 3-source-file change with a 2.5-month
history behind it, so it is worth the owner's eye rather than a silent drain.


## DONE (2026-08-26) — disposition 1 taken, with the block-level question left open

Owner picked options 1+2+3. This is 3.

**Renamed** `QOU.WedderburnMass.spectral_sequence_collapses_to_centre` ->
`centralIdempotent_idem`, the honest name for `forall i, e i * e i = e i`. The
`[WhiteheadHH R A]` instance is KEPT in the signature — unused, deliberately, so
the rename is behaviour-preserving for any call site that supplies it, and so
the docstring can point at the fact that it is unused as the evidence.

**Docstring rewritten** to say plainly what the theorem does not establish, and
to carry the twice-found history so a third agent does not have to rediscover it.

**A `-- GAP:` block added** stating why the collapse cannot honestly be written
in Lean *yet*, with both reasons: (1) there is no defined filtration to collapse
— all three `J^bullet` readings are excluded; (2) Mathlib has no
Hochschild-cohomology framework, so `E_infinity` has no type. Ends with "Do not
close this by renaming a different theorem back", which is precisely how it was
closed the first time. Carries `-- Ref: [cartan1956]`.

**Three consumers updated:** the `.ts` `lean.ref`, the docstring cross-reference
in `phi-q-categorical-truncation.lean`, and the row in `definition-index.md`. The
only surviving occurrence of the old name is inside the new history note, which
quotes it deliberately.

**`authorNotes` added to the `.ts`** (schema-checked: `AuthorNote` at
`folio-assistant/schemas/types.ts:487`, `BlockBase.authorNotes` at :686) stating
that the Lean does not prove the block's `.md` statement.

**STILL OPEN, and deliberately not decided here:** whether
`prop:spectral-sequence-collapse` should remain a `proposition` at all. Its `.md`
asserts a collapse its Lean does not prove. Demoting to `conjecture` would be
honest and would propagate under §3b to every consumer — a much larger change
than a rename, and an author call rather than an agent one. Recorded in the
authorNote so the block carries its own question.

Note the underlying mathematics is NOT in doubt for the finite Hecke algebra —
semisimple at generic q, so Whitehead gives HH^k = 0 for k >= 1. Only the Lean
statement is missing, and (1) and (2) above block writing one.
