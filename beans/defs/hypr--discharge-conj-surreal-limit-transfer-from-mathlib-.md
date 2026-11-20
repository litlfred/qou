---
# hypr
title: Discharge conj:surreal-limit-transfer from Mathlib Hyperreal (ℝ* is a SurrealField)
status: todo
type: task
priority: high
tags:
    - lean
    - surreals
    - nonstandard
    - conjecture-discharge
    - reorg-2026-10-04
created_at: 2026-08-09T19:15:46Z
updated_at: 2026-11-20T08:32:31Z
parent: qou-3kkl
---

`QOU/AppendixSurreals/SurrealLimitTransfer.lean` carries `conj:surreal-limit-transfer`
as a content-bearing class with **no instance**, on the stated grounds that an
ω-evaluation "exists model-theoretically (Robinson ultrapower; Berarducci–Mantova germ
evaluation at ω), but is not constructible from the abstract `SurrealField` interface
alone".

That is right about the *abstract* interface — and it is the reason no instance was
fabricated, correctly. But the Robinson ultrapower it names **is already in Mathlib**,
and every class field appears to be exactly a Mathlib lemma. Checked 2026-08-09 against
the vendored Mathlib:

| `SurrealLimitTransfer` field | Mathlib |
|---|---|
| `evalOmega : (ℕ → ℝ) → K` | `Hyperreal.ofSeq` (`ℝ* = Germ (hyperfilter ℕ) ℝ`) |
| `evalOmega_const` | `Germ.const` / `Hyperreal.ofReal = const` |
| `evalOmega_add`, `evalOmega_mul` | `Germ` ring structure |
| `evalOmega_le_of_eventuallyLE` | `Germ` order + `Nat.hyperfilter_le_atTop` |
| `evalOmega_isClose_of_tendstoReal` | `Hyperreal.isSt_of_tendsto` |

And `SurrealField` extends `Field K, LinearOrder K, IsStrictOrderedRing K` — `ℝ*` has
all three as instances in `Mathlib/Analysis/Real/Hyperreal.lean` (lines 30/33/36), plus
`ofReal := const`. So `SurrealField ℝ*` looks close to free, and
`SurrealLimitTransfer ℝ*` follows.

> ⚠ **THE SENTENCE IMMEDIATELY ABOVE IS WRONG AS ARGUED.** It was written from the
> `extends` clause alone and never read the rest of the class. See
> **§ CORRECTION (2026-08-09)** at the foot of this bean. It happens to land on a true
> conclusion, but only for a reason that is a *defect report* on `Basic.lean`, not the
> reason given here.

**Payoff.** Discharges a standing no-instance primary conjecture, and makes the two
derived theorems (`standardPart_evalOmega_of_tendstoReal`,
`tendstoReal_le_of_eventuallyLE`) unconditional. Everything downstream that takes
`[SurrealLimitTransfer]` as a hypothesis becomes unconditional at `K = ℝ*`.

**⚠ The one thing that will bite, and the reason to scope this carefully.**
`Hyperreal.isSt_ofSeq_iff_tendsto : IsSt (ofSeq f) r ↔ Tendsto f (hyperfilter ℕ) (𝓝 r)`,
and `Nat.hyperfilter_le_atTop` means hyperfilter convergence is **strictly weaker** than
`atTop` convergence. The arrow `Tendsto atTop → IsSt` is available
(`isSt_of_tendsto`); the **converse is false**. So this instance lets you *push* real
limits into the surreal/hyperreal world, but does **not** let you discharge a
`Tendsto … atTop` goal by a standard-part computation. `IsSt (ofSeq f) r` is `f(ω) ≈ r`
for one specific `ω`, not "for all infinite hypernaturals", which is what a genuine NSA
limit argument needs and which Mathlib does not package.

Consequence: this bean is worth doing on its own merits, but it does **not** on its own
let surreal/standard-part machinery replace an ε–δ argument whose *goal* is
`Tendsto … atTop` — see the "what this cannot do" note in bean `thmb`.

Related: `QOU/AppendixSurreals/ClassicalLimitStpart.lean` currently defines
`abbrev StandardPart := ℝ → ℝ` — an explicit **surrogate**, "represented as a real
function for the formal Lean shell", carrying no surreal content. If `ℝ*` lands, that
surrogate should be revisited too.

---

## § CORRECTION (2026-08-09) — the argument above was wrong; the conclusion lands for a worse reason

Worked in `QOU/AppendixSurreals/HyperrealLimitTransfer.lean`. Every status below is
`lake build`-verified by module name with the `.olean` deleted first, and
`#print axioms`-clean on `[propext, Classical.choice, Quot.sound]`.

### 1. What this bean got wrong

The sentence *"`SurrealField ℝ*` looks close to free"* was written from the `extends`
clause **and nothing else**. `SurrealField` (`Basic.lean:54`) also demands Conway's

    birthday : K → Ordinal

with six axioms — `birthday_zero`, `birthday_one`, `birthday_neg`, `birthday_add_le`,
`birthday_avg_le`, `birthday_ofReal_le_omega` — plus `omegaSurreal` and
`omegaSurreal_gt_natCast`. Verified: Mathlib's `Hyperreal` has no birthday, Mathlib's
`Surreal` has no birthday, and **no `SurrealField` instance existed anywhere in the
corpus** before this work. "Close to free" was not a reading of the class; it was a
reading of one line of the class.

### 2. The conclusion survives — via a defect in `Basic.lean`, not via Mathlib

`flatBirthday x := if x = 0 then 0 else 1` — **two-valued** — satisfies **all six
birthday axioms**. `surrealFieldHyperreal : SurrealField ℝ*` is now a proved (sorry-free)
term. So:

> **The birthday axioms do not characterise Conway's birthday.** They admit a model in
> which every nonzero element is born on day 1. Any theorem proved from those axioms
> alone is true in that model too, and so says nothing specific about birthdays.

Proved, not asserted: `flatBirthday_two : flatBirthday 2 = 1` (Conway: `2`),
`flatBirthday_omega : flatBirthday ω = 1` (Conway: `ω`), and
`flatBirthday_omega_lt_omega0 : flatBirthday ω < ω₀` — an element above every natural
number gets a birthday below `ω`.

Sharpest instance: **`birthday_avg_le`** — the axiom carrying the longest design
commentary in `Basic.lean` ("exactly Conway's `{L | R}` recipe", "genuinely independent
of `birthday_add_le`", with a "narrow kernel rationale") — is satisfied here *vacuously*.
Its RHS is `≥ 0 + 1 = 1` and its LHS is `≤ 1`. Under any bounded birthday it constrains
nothing.

`omegaSurreal_gt_natCast` **does** do real work: it is false in any archimedean field,
so `ℝ` is not a counter-model and `ℝ*` is needed.

### 3. What is actually delivered, and it is birthday-free

The mathematics this bean wanted needs no surreal structure at all. §1 of the new module
proves it unconditionally at `ℝ*` — no class, no instance, no `birthday`:

| result | content |
|---|---|
| `st_ofSeq_of_tendstoReal` | limits are computed by `st ∘ ofSeq` |
| `ofSeq_le_ofSeq_of_eventuallyLE` | eventual domination transfers to `ℝ*` |
| `tendstoReal_le_of_eventuallyLE'` | limit comparison via one inequality at `ω` |

`isClose_iff_isSt` is the bridge that makes §3 cheap: QOU's `IsClose x (ofReal r)`
unfolds to Mathlib's `isSt_iff_abs_sub_lt_delta` **by `rfl`**. That is the whole finding
in one lemma — the conjecture's content was always Mathlib's `IsSt`, wearing a carrier
it does not need.

### 4. Status of `conj:surreal-limit-transfer`

`surrealLimitTransferHyperreal : SurrealLimitTransfer ℝ*` is constructed (every field a
real theorem; **none mentions `birthday`**). But it sits on `surrealFieldHyperreal`, so
the discharge is only as meaningful as that carrier.

⚠ **Both are `def`, never global `instance`**, used only under
`attribute [local instance]`. Promoting either would make every `SurrealField`-generic
theorem silently apply to `ℝ*` under a two-valued birthday. **Do not promote them.**

So: **do not mark this conjecture discharged.** The honest reading is that it was
*stated at the wrong strength* — see the follow-on below.

### 5. Follow-on (not done here)

Split `SurrealField` into a birthday-free base — `Field` + `LinearOrder` +
`IsStrictOrderedRing` + `ofReal` + `ofReal_strictMono` — with the birthday axioms as a
separate mixin. Checked: **nothing in `StandardPart.lean` uses `birthday`**, and
`isFinite_decomposition` (`Basic.lean:382`) is birthday-free, so the entire standard-part
theory would move down to the base unchanged, `SurrealLimitTransfer` would be statable
there, and `ℝ*` would be a genuine instance with no degeneracy. `BlowupCalculus.lean`
already demonstrates this exact pattern: `BlowupField` is declared over the three plain
ordered-field classes and carries a real `instBlowupFieldHyperreal`.

Cost: `SurrealField` is used across ~38 modules, and 6 of them (`Basic`, `SignSequence`,
`BirthdayGrading`, `DiophantineBirthday`, `HoefsmitBridge`, `Conjectures`) genuinely
touch `birthday` — those would need the mixin. Not attempted blind.

Separately: the birthday axioms should be **strengthened** so a two-valued function no
longer satisfies them, or the modules that reason from them should be re-read to see what
they actually establish. That is the more important half of this correction.

### 6. Unchanged

The ⚠ limitation above stands exactly as written. `Nat.hyperfilter_le_atTop` gives only
`Tendsto atTop → IsSt`; the converse is false. Everything here **pushes** real limits into
`ℝ*` and nothing here discharges a `Tendsto … atTop` goal by a standard-part computation.
Surreal/standard-part machinery does not replace this corpus's ε–δ arguments.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-09 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


**2026-11-20T08:32:31Z — owner-approved status change (coordinator session_01VQDpPdnjTBLBcPi6D5gj61, PR #8542 batch C):** in-progress → todo. Open conjecture: stale claim released; never to be completed while the conjecture is open (AGENTS rule 13a).
