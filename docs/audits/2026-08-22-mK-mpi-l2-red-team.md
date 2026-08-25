# Red-team: is `m_K/m_π` a genuine parameter-free L2 win, or a fitted correction on a scan-selected term?

**Date:** 2026-08-22
**Scope:** adversarial audit of the framework's *single* claimed L2
accuracy success — `m_K/m_π`, the only observable that "beats 100×
scoreable" per `computations/per-observable-100x-status.witness.json`
and AGENTS.md §"Precision goals" ("1/5 scoreable"). Read-only. Mirror
of the c_k red-team ([`2026-08-16-ck-ladder-red-team.md`](2026-08-16-ck-ladder-red-team.md)).

**Standing under the Critical-distance license (AGENTS.md).** This is
an assessment of the framework's best result on the merits.

---

## TL;DR verdict

**Tiered:** the accuracy-determining piece is **fitted** (a
truncation-selected EM correction whose scale-setting input `α_em` is
itself conditional on an open Lean `sorry`); the structural backbone
`[3]_q·[4]_q` is a **scan-selected derived-candidate** at ~100–200 ppm
that **does not, by itself, beat 100×**.

**Is "beats 100×" honest?** The arithmetic is real, but the *label*
"genuine parameter-free prediction" is not. Under the framework's own
rules — "Axiomatization is NOT a Proof", "conditional-proved ≠
premise-established", "sorry-free ≠ derived" — a closure that only
clears the target *after* a truncation-fitted correction whose input
carries an open `sorry` cannot be credited as a proved, unconditional
prediction. **The count of genuinely parameter-free, unconditional
sub-100× predictions is 0/5, not 1/5.** The "1/5" is defensible only if
you accept "α_em-conditional-on-an-open-sorry + a data-selected
truncation order" as "derived".

---

## 1. The formula the dashboard actually uses

`per_observable_100x_status.py` (lines 590–636) computes:

```
m_K²/m_π²  =  [3]_q·[4]_q  +  (α_em/π)·(3q² − 1)/(2q²)
              └── strong ──┘   └──────── EM ─────────┘
m_K/m_π    =  √( … )
```

evaluated at the **proton-pinned** q₀ = 1.10997858275138…, with `α_em`
imported from `meson_em_sinh_closed_form.alpha_em_inv_derived(q₀)`.

Reproduced end-to-end in mpmath at 70 dps (matches the witness to all
printed digits): full `m_K/m_π = 3.53711852189`, err **23.45 ppb** vs
PDG 3.53711843895.

Experimental bar (from the witness): σ_exp = **26 360 ppb** (26.4 ppm),
so the 100× target is **263.6 ppb**, miss_factor 0.089 → "beats 100×".

---

## 2. Where the accuracy comes from — term ablation (mpmath, 70 dps)

| Formula evaluated at q₀ | m_K/m_π | err vs PDG | beats 100× (264 ppb)? |
|---|---|---:|:--:|
| **strong only** √([3]_q·[4]_q) | 3.53675923 | **101 553 ppb** (101.6 ppm) | ✗ misses **385×** |
| strong + (α_em/π)·**1** (EM factor = 1) | — | 8 719 ppb | ✗ misses 33× |
| strong + (α_em/π)·**(1+log(1+ℏ_q))** (untruncated) | — | 51.5 ppb | ✓ |
| strong + (α_em/π)·**(3q²−1)/(2q²)** (3-term truncation) — **shipped** | 3.53711852 | **23.45 ppb** | ✓ |
| shipped, but with **CODATA α_em** instead of derived | — | 23.40 ppb | ✓ |

Two facts fall out immediately:

1. **The genuinely-derived-candidate piece (`[3]_q·[4]_q`) does NOT
   beat 100×.** Alone it misses the target by ~385×. The entire
   sub-100× win is manufactured by the EM correction term.
2. **The `α_em` *value* is not the lever; the truncation *order* is.**
   Swapping the framework-derived α_em (137.03593509) for CODATA
   (137.03599918) — a 0.16% change — moves the result by 0.05 ppb
   (23.45 → 23.40). But the shipped 3-term truncation `(3q²−1)/(2q²)`
   beats the *natural untruncated resummation* `1+log(1+ℏ_q)`
   (23.45 ppb vs 51.5 ppb). **The truncation is better than the full
   series** — the tell-tale signature that the stopping point was
   chosen against the data, not derived. `α_em/π` merely sets the EM
   scale to ~0.16%; the correction's *magnitude* is set by the
   truncation choice.

The corpus's own honest audit
([`2026-05-28-meson-mass-ratio-derived-vs-fitted.md`](2026-05-28-meson-mass-ratio-derived-vs-fitted.md))
records the term-by-term hunt that produced this factor: LO `(α/π)m_π²`
→ 9% miss; `×(1+ℏ_q)` → 0.46%; `×(1+ℏ_q−ℏ_q²/2)` → 72 ppm. That is a
ladder truncated at the rung that best matches data — the same pattern
that audit itself flags as "the same fitting pattern as the Habiro
1/30, 1/1260 corrections", and the same class the c_k red-team caught.

---

## 3. DOF-vs-precision accounting

Claimed inputs: q₀ (CAL-2), and the ratio cancels the m_e/m_π scale
(CAL-1/CAL-3). Actual knobs that entered the 23-ppb number:

| # | Ingredient | Status | Trace |
|---|---|---|---|
| — | squaring to m²-ratio (GMOR) | **motivated, 0 free** | χPT GMOR relation; defensible |
| 1 | the pair **(3, 4)** in `[3]_q·[4]_q` | **scan-selected** (≥1 discrete DOF; 2 indices) | 2026-05-28 audit: "candidate found by scanning q-integer products"; "spin assignment post-hoc; first-principles braid derivation open" |
| 2 | **α_em** as a 4th physical input | **NOT one of the 3 CALs**; and conditional | dashboard note: "CLASS-A acknowledged anchor … conditional on Witten-κ class" — open `sorry` in `em-coupling-chern-simons.lean` |
| 2b | crossings **(9, 10)** inside α_em⁻¹ = q·[9]_q·[10]_q, plus the CS-tower κ_gram structure | selected/derived-with-its-own-scan | `meson_em_sinh_closed_form._alpha_em_inv_derived` |
| 3 | **truncation order** of `1+log(1+ℏ_q)` → stop at ℏ_q² | **data-selected** (beats the untruncated series — §2) | 2026-05-28 audit's term-by-term sequence |

**Accounting.** The number is quoted to 23 ppb. To get there from the
101 600-ppb (0.1%) strong-only baseline required: 2 scan-selected
indices + a 4th input (α_em) that is itself conditional on an open
`sorry` and carries its own selected crossings (9,10) + a data-selected
truncation order. That is ≥3 effective discrete knobs plus a conditional
input. **Clearing a 264-ppb target — set loosely because the kaon is
poorly measured (§4) — with that much selected machinery is not a
parameter-free prediction.**

---

## 4. Why it is "the only one" — the target is 85 000× looser than the mass targets

The 100× target scales with the *experimental* uncertainty. m_K is
known only to 26 ppm (m_K± = 493.677 ± 0.013 MeV), so:

| observable | 100× target | vs m_K/m_π target |
|---|---:|---:|
| m_p | 0.003091 ppb | — |
| m_K/m_π | **263.6 ppb** | **~85 000× looser** |

`m_K/m_π` is the "only observable that beats 100×" in large part
because its target bar sits ~5 orders of magnitude *below* the bar the
mass observables must clear. Even so, the *derived* piece (`[3]_q·[4]_q`)
still misses this loose bar by 385×; only the fitted EM term clears it.
Had the kaon been measured to proton-like precision, this "win" would
miss by ~385×.

This is not a pure ratio-cancellation artifact — the strong term
`[3]_q·[4]_q` is a genuine, dynamical q₀-dependent quantity, and the
prediction does move with q₀. So the correct framing is **not** "two
meson masses share a scale so their ratio is trivially close" (that
would be a structural-ratio artifact). It is: **a legitimate ~0.1%
categorical postdiction of the strong ratio, pushed under a
loosely-set target by a data-selected EM correction.**

---

## 5. The "both pieces Lean-proved" claim is true but non-probative

The witness credits `qou:QOU.BraidKnot.meson_qCG_3x4` and
`qou:QOU.BraidKnot.meson_EM_closed_form`. Both were read in full:

- **`meson_qCG_3x4`** proves the q-Clebsch–Gordan *fusion decomposition*
  `[3]_q·[4]_q = [2]_q+[4]_q+[6]_q` (a real, non-trivial `ℤ[q,q⁻¹]`
  identity). It says **nothing** about the kaon — the physical
  identification "m_K²/m_π² *is* this product" is entirely outside the
  Lean.
- **`meson_EM_closed_form`** proves `1+ℏ_q−ℏ_q²/2 = (3q²−1)/(2q²)` — a
  one-line `linear_combination` rewrite of one rational function as
  another. This is a notation identity (`X = X` class): it proves that
  two spellings agree, not that this factor is the meson EM correction.
  Per Strict Lean Discipline §5 ("tautological conclusions … provable
  without using any hypothesis about the mathematical objects"), it is
  non-probative for the physics.

Both are honest algebra; neither closes the physical gap. Classic
**sorry-free ≠ derived**. The genuinely open pieces — "why 3 and 4",
and the first-principles derivation of the `(3q²−1)/(2q²)` truncation —
are both admitted open in the 2026-05-28 audit and remain open.

---

## 6. Prior corpus assessment — what was and wasn't settled

- [`2026-05-28-meson-mass-ratio-derived-vs-fitted.md`](2026-05-28-meson-mass-ratio-derived-vs-fitted.md)
  is honest about the *components* (labels them derived-candidate /
  fitted / open) but predates the dashboard wiring and never connects
  them to the "1/5 scoreable win" framing.
- [`2026-08-18-mass-binding-accuracy-what-is-closeable.md`](2026-08-18-mass-binding-accuracy-what-is-closeable.md)
  establishes the **count** (1/5, m_K/m_π alone; only ratio) and takes
  the "beats 100×" at face value — it does **not** red-team whether the
  one survivor is itself parameter-free.
- A stale, superseded formula still sits on disk:
  `meson-kaon-pion-derivation.witness.json` (2026-07-05) uses
  `(q⁵−q⁻⁵)·(9/5)²` with a `squaring_proof` that selects the exponent
  `power=2` *by minimizing error against data* (444 605 / 290 / 799 479
  ppm for powers 1/2/3) — a naked exponent fit. The dashboard comment
  notes this form was "retracted as a fit (#1420)". That there were
  multiple successive retracted closed forms is itself a fit-hunt
  signature.

**This red-team fills the gap:** the count-establishing audits never
scrutinized whether the single survivor is a genuine prediction. It is
not, in the unconditional sense.

---

## 7. Recommendations (non-blocking; read-only audit)

1. The dashboard row and AGENTS.md §"Precision goals" should footnote
   `m_K/m_π` as **conditional** (α_em open `sorry`) **+ truncation-
   selected**, not present it unqualified as the "1/5 scoreable win".
   The honest count of *unconditional parameter-free* sub-100×
   predictions is **0/5**.
2. If the framing "1 conditional prediction meets L2" is kept, it must
   name both conditions in the same breath: the Witten-κ `sorry` and
   the data-selected truncation order — mirroring how the c_k banner
   now carries its convention/fit caveats inline.
3. Delete or clearly mark-superseded the stale
   `meson-kaon-pion-derivation.witness.json` (the `(9/5)²`/power-scan
   form) so a future reader does not cite the retracted fit.

---

## Bottom line (blunt)

`m_K/m_π` is the framework's best number, and it is **not** a
parameter-free prediction. Its genuinely-derived core — the q-Clebsch–
Gordan fusion `[3]_q·[4]_q` — is a respectable ~0.1% categorical
postdiction of the strong ratio, but by itself it misses even this
observable's unusually loose 264-ppb target (loose only because the
kaon is measured to a mere 26 ppm) by ~385×. The sub-100× "win" is
manufactured entirely by an EM correction term `(α_em/π)·(3q²−1)/(2q²)`
whose magnitude is set by a **truncation order chosen against the data**
(it beats the natural untruncated series) and whose scale input `α_em`
is **conditional on an open Lean `sorry`**. The two cited Lean lemmas
prove only algebra, not the physical identifications. So the "beats
100× → 1/5 scoreable" headline is arithmetically true but
epistemically inflated: the count of unconditional, parameter-free,
sub-100× predictions is **0/5**. This is the mirror image of the c_k
finding — a data-selected ladder truncation dressed as a derived
closed form — except here it was quietly wired into the headline
dashboard rather than quarantined.

---

## 8. RESOLUTION — recommendation 3 actioned; §2/§3-knob-3 removed (2026-08-22, PR #5467)

**One of the three knobs is gone. The 0/5 verdict stands on the other two.**

### What was found after this audit was written

The corpus had **already ruled** on the truncation.
[`docs/precision-goals.md` §L2](../precision-goals.md) records the caveat
as **RESOLVED 2026-08-09, owner directive** — *"the EM factor is now the
**full series** `1 + log(1+ℏ_q)`, not the two-term truncation
`(3q²−1)/(2q²)`"*, with the correct reason (*"a truncation chosen because
it matches is a fit"*) and the correct cost (*"still MEETS L2 … 51.43 ppb
— 5.13× margin"*).

**No producer was ever updated.** The ruling lived in one prose file while
`per_observable_100x_status.py`, `meson_em_sinh_closed_form.py`,
[`observable-sector-tracker.md`](../observable-sector-tracker.md) and the
content block all kept shipping the truncation — and the L2 scorecard kept
crediting 23.45 ppb. This audit, written 13 days later, red-teamed the
*stale* formula in good faith and independently reached the same verdict
the owner had already reached. That convergence is worth recording: it is
the second confirmation, not the discovery.

**The failure mode is worth naming**: a durable ruling recorded in prose
with no code change and no bean is indistinguishable, to every later
reader and every later agent, from no ruling at all.

### Sharpening §2 — the fit test, made reproducible

§2's table showed the truncation beating the untruncated series. The
stronger form is the full stopping-order sweep (70 dps, proton pin), now
emitted as witness data by `meson_em_sinh_closed_form.py` under
`em_truncation_order_sweep_ppb`:

| stop at | m_K/m_π err (ppb) |
|---|---:|
| ℏ¹ | 479.11 |
| **ℏ²** | **23.45** ← was shipped |
| ℏ³ | 53.55 |
| ℏ⁴ | 51.31 |
| ℏ⁵ | 51.49 |
| ℏ⁶ | 51.474 |
| ℏ⁷ | 51.4755 |
| ℏ⁸ | 51.4754 |
| untruncated | **51.4754** ← now shipped |

The series converges to 51.475 ppb, and **order 2 is the only order below
that limit** — a non-monotonic dip with every further term walking *away*
from the data. This is stronger than "the truncation beats the full
series": it shows the chosen order is the unique outlier, which no
convergence argument can produce and only selection-against-data can.

It also disposes of the producer's own defence — that `(3q²−1)/(2q²)` is
*"a rational polynomial in q⁻² with coefficients (3, −1) — not a series
truncation"*. The closed form is exact, but it is exactly *that*
truncation; the "3 = generations" reading was applied after the order had
been picked. Re-spelling a truncation does not derive it (AGENTS.md
§"Defined residual ≠ derived decomposition"). That prose is retained in
the producer, explicitly marked as a record of the retired argument.

### What changed, and what did not

| | before | after |
|---|---|---|
| EM factor | `(3q²−1)/(2q²)` | `1 + log(1+ℏ_q)` |
| m_K/m_π err | 23.45 ppb | **51.48 ppb** |
| L2 margin (target 263.6 ppb) | 11.2× | **5.1×** |
| scorecard | 1/5 scoreable | **1/5 scoreable — unchanged** |

The fit was never load-bearing: removing it costs 2.2× of margin and
changes no verdict.

**§3's knob table, revised:** knob 3 (truncation order) is **removed**.
Knobs 1 (the scan-selected `(3,4)` pair) and 2 (`α_em` as a 4th input,
conditional on the open Witten-κ `sorry`, carrying its own selected
crossings `(9,10)`) are **untouched**.

**§5 stands, with one clarification.** `meson_EM_closed_form` proves
`1+ℏ_q−ℏ_q²/2 = (3q²−1)/(2q²)`. That identity is exact and stays proved —
the producer still verifies it every run. §5's point was never that the
algebra is wrong; it is that proving two spellings agree is non-probative
for the physics. That reading is now the operative one: what was wrong was
the *identification* of that quantity as the physical EM factor.

**The bottom line is unchanged.** `m_K/m_π` remains the framework's best
number and remains **not a parameter-free prediction**. The strong core
still misses the target by 385× alone, and the correction that clears it
is still conditional on an open `sorry`. **0/5 unconditionally
parameter-free stands.** What this resolution buys is narrower and worth
having: the number is no longer *additionally* propped up by a knob
chosen against the data.

### Recommendations status

| # | Recommendation | Status |
|---|---|---|
| 1 | Footnote the dashboard row + tracker as conditional, not "the 1/5 win" | **done** — dashboard row description and `observable-sector-tracker.md` now say CONDITIONAL and name both remaining conditions |
| 2 | If the framing is kept, name both conditions in the same breath | **done** — the truncation condition is now *removed* rather than named; the Witten-κ `sorry` and the scan-selected `(3,4)` are named inline in both artifacts |
| 3 | Remove the truncation-selected EM correction | **done** — PR #5467 |
