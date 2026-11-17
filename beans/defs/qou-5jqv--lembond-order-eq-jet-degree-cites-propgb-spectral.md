---
# qou-5jqv
title: lem:bond-order-eq-jet-degree cites prop:gb-spectral-sequence for a filtration that block does not name
status: in-progress
type: task
priority: normal
created_at: 2026-09-14T20:06:19Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-v2om
---


## 2026-09-14 — measured. One hop downstream of `qou-sw8n`; probe 31/31

`qou-sw8n` (today) established that `prop:gb-spectral-sequence` names a
**fourth** reading of `J^•` — the energy-indexed confinement filtration of
`def:confinement-level`, alongside the three tabulated in
`2026-08-16-three-gb-filtrations-one-name.md`. This identifies that block's
first **consumer**, and measures that the consumer reads `J^•` the other way.

**The measurement.** `lem:bond-order-eq-jet-degree` opens by equipping
`H_{3A}(q)` with *"the Gröbner--Shirshov filtration by Coxeter length
$\ell(w)$"* and attributes it to `prop:gb-spectral-sequence` — in the same
sentence, so it reads as the source. That proposition says the filtration is
*"the confinement filtration $J^\bullet(q)$"*, points at `def:confinement-level`,
indexes its strata by **partition energies** `E_ℓ(q₀)`, and **the string
"Coxeter" does not occur in it at all**. The edge is in the `.ts` `uses[]` too,
so the dependency graph routes through it as well.

The shared glyph `ℓ` is a Coxeter length in the citer and a partition index in
the cited block — which is why the mismatch is invisible to a reader skimming
either one alone.

Probe: [`computations/audits/bond_order_jbullet_citation_probe.py`](../computations/audits/bond_order_jbullet_citation_probe.py),
**31/31**. Pure string/AST measurement over committed files — no arithmetic, no
witness, nothing recomputed.

### 🛑 This is NOT a one-line doc fix, and the reason is the Lean

The formalisation sides with the **citing** block. `QOU.Knot.BodyOrderExpansion`
(sorry-free) says in its own words that applying its factorisation to the atomic
braid *"needs the index set of `H_{3A}`'s normal forms to BE such a product —
i.e. that Coxeter length is additive over the Young subgroup `S_3 × ⋯ × S_3`"*,
and discharges exactly that via `QOU.Knot.BlockLengthAdditive` (also sorry-free,
the parabolic length formula). So the Coxeter reading is not a stray link in one
sentence of prose — **it is the reading the whole Lean cone is built on.**

Retargeting the citation would put the prose in agreement with the cited
proposition and in **disagreement with the Lean**. The block's own `.lean` cannot
adjudicate: `gradedTerm : ℕ → ℝ` is abstract — no Hecke algebra, no `J^•`, no
`ℓ(w)` — a §3b-cond structure whose `body_eq_graded` is a hypothesis field.

### 🛑 The prior record asserts the OPPOSITE

`docs/audits/2026-08-25-spectral-sequence-is-a-no-go-not-a-tool.md` §4 draws this
exact dependency edge and concludes the identification *"is stated in terms of
**the same** $J^\bullet$ that has three excluded readings."* "Same" is what §1+§2
measure to be false. This is not a gap in the record — it is a claim in the
record pointing the wrong way, which is why a topic-grep for prior art comes back
reassuring. `beans/defs/qou-ix0x…:50` propagates the same reading (path as of the
2026-10-04 `.beans/` → `beans/defs/` move; the bean is unchanged).

### Why every existing detector missed it — three reasons, none "nobody looked"

1. **`da-citation-misuse` — the criterion built for exactly this — RAN on this
   block and returned `pass` with ZERO findings.** Stamped
   `[EXPIRED-NO-FIELD-HASH]`, dated 2026-07-08, reviewer `gemini-3.1-pro`, and
   its note is content-free filler: *"Reviewed interactively. Sound conceptual
   formulation correctly verifying specific complex categorical configurations
   meticulously within distinct formal boundaries."* Same shape already on record
   for `curvature-rank-gb-stratification-proof`, where four `da-*` criteria
   returned zero findings on a proof its own Step 1 refutes.
2. **The whole `wpdb` / 08-16 / 08-26 arc is keyed on
   `prop:curvature-rank-gb-stratification`**, which this block's `uses[]` does
   not contain — so the arc reaches it only transitively and never names it. The
   08-26 audit does not mention the block at all.
3. **The 08-16 audit's own "Search performed" asserts there is no fourth
   reading.** It walked `mass-theory/`; the fourth lives in
   `knots-particles-confinement/`.

### 🛑 The corpus already knows the distinction — in exactly one place

§6 classifies blocks carrying the word-length rule for a named filtration:
**2 conflate** (`bond-order-eq-jet-degree.md`, and
`alg:mba-step07-gb-filtration` — the appendix AGENTS.md declares a *maintenance
contract* for step-7 prose-vs-compute sync), **1 distinguishes**.
`phi-q-categorical-truncation-interpretation.md` line 1: *"The parameter
$k_{\max}$ recorded in witness data represents the Coxeter-length filtration.
**This strictly differs from the structural GB-depth $k_\star(T_w)$.**"*

So the distinction is stated in the content tree (`folio/` since the
2026-10-04 reorg; `content/` when this was measured) and simply not
propagated. **That
makes this a consistency defect, not an unknown** — the repair is a decision
about which reading to keep, not a discovery to be made.

Two coordination ledgers still propagate the Coxeter reading uncorrected:
`2026-05-30-alpha-em-canonical-chain-walkthrough.md:153` and
`2026-05-23-algebraic-geometric-observable-consistency.md:20`. The cheat-sheet
row was corrected today and points at `qou-sw8n`; the ledgers are behind it, and
the correction was made at the row, never at the blocks downstream of it.

### Two errors of mine, both caught by the probe I was writing

- The first `docs/audits/2026-08-25` matcher was a single-line literal; the
  phrase is **wrapped across a line break** in the source, so it returned False
  on text plainly there. Same detector-blindness class as the subject.
- §6 first reported **"3 carriers"** by matching the rule without classifying —
  counting `phi-q-categorical-truncation-interpretation.md`, which *contradicts*
  the conflation, as evidence *for* it. **Classify before counting.**
- Separately: `grep -c bond` on the cheat sheet is **not** 0 (it matches
  "bond-count", "bonded pairs", "bond-word" in the step-9b row). The probe tests
  the block **label**, not the substring.

### What is NOT claimed

Not that the lemma is false — its Lean carrier is a legitimate §3b-cond
conditional. Not that the Lean is wrong — `BlockLengthAdditive` is a real proof.
Not that either filtration is canonical — that is `qou-sw8n`, which stays **open**,
and whose own exclusion of the confinement reading is **scope-(a)** (a generic-`q`
strata mismatch; ties permitted at a single `q₀`, decisive test needs the step-10
confinement LP, not run). Not that retargeting the citation is the fix.

No (a)/(b) scoping is owed: this is a citation-integrity measurement, not a
refutation.

### 🟡 OPEN — this is an owner decision and is deliberately NOT taken

There are at least three repairs with different blast radii. **Stays open per
§13a** — `qou-sw8n`'s question is an open conjecture and this is one hop from it.

## Parented 2026-11-15 (owner-approved bean triage)

Parent `(none)` → `qou-v2om`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## Round 75 Progress (2026-11-17T11:49:05Z)
- Advanced in PR `litlfred/qou#8329` (branch `feat/round75-blocklen-equilateral-bondletter-descent-framing-43c1`, head `d2c6d3d8e433b1ecf3e00634b44d230b097bc7d3`).
