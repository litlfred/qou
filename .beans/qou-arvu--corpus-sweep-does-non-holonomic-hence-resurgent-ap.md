---
# qou-arvu
title: "Corpus sweep: does 'non-holonomic hence resurgent' appear elsewhere?"
status: completed
type: task
priority: normal
created_at: 2026-08-14T20:02:00Z
updated_at: 2026-08-15T00:29:43Z
---

Spun out of `qou-tdp0` step 1 (owner-directed, 2026-08-14).

## COMPLETE 2026-08-14 — all 5 class-(a) sites fixed (2 prose #5039, 3 producers #5050)

Full findings: [`2026-08-14-non-holonomic-implies-resurgent-corpus-sweep.md`](../docs/audits/2026-08-14-non-holonomic-implies-resurgent-corpus-sweep.md).

**5 class-(a) sites** found across 22 candidate files: 2 prose, 3 producers. All
five are now fixed. The sections below are kept in the order the work happened,
so the handoff that was written mid-way — and the call it got wrong — stay
visible rather than being tidied away.

### Fixed (prose, no producer hash touched)

- `docs/audits/2026-07-12-dladder-divergence-correction.md` — SUPERSEDED banner.
  Its **title** asserted the refuted conclusion. The banner names the specific
  defect: its central "no singularity at ρ" argument ran a search that **omitted
  the `Q_b` zero** `q*_ρ ≈ 1.48989` whose image *is* `ρ = 0.1428`.
- `docs/audits/2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md`
  — banner + two clauses struck. Its exact linear algebra is untouched and
  correct; only the "tightens the resurgent reading" interpretation is withdrawn.

### ✅ PRODUCERS DONE 2026-08-14 (PR #5050) — the sympy block was removable

**`sympy` installed cleanly here.** It pins `mpmath<1.4`, which is what **107**
of the qbeta witnesses already record, so the stack *matches* the one that
produced these witnesses (`sympy 1.14.0`) — no provenance regression. The
"blocked on tooling" call in the section below was right that it was blocked,
and wrong that it had to stay that way; the first move should have been to try
installing it.

**Control run first.** The generating-function probe, run unmodified, reproduced
`divergent=True`, `C=0.0617`, root test `4.3721→5.9104` and a byte-identical
verdict in 96.1 s — confirming this bean's claim that re-running is not the fix.

**All three re-scoped, every measurement kept:**

1. **`generating_function_structure`** — §5's search omitted the `Q_b` zero. It
   now tests `q*_ρ = 1.4898947996883652482` and finds
   `|ũ(q*_ρ)| = 0.142799996644689688905721`, reproducing the published ρ to
   **2.24e-30** *using the probe's own ũ map*. §3's boolean renamed
   `divergent` → `root_test_rising_in_window`, with the reason it is consistent
   with a finite radius (`|d_k|^{1/k} → 1/ρ = 7.0028` from below; at k=21 it is
   5.9104, still short). Witness: `super_exponentially_divergent` **removed**,
   `singularity_at_qb_zero` added, 7 assertions pass.
2. **`odd_channel_stokes_borel`** — "divergence class" → "growth class"; the
   Gevrey drift-down and the `s→0` Borel–Leroy pole at 0.147 now recorded as
   *corroboration* (scope-(a): consistency, **not** a derivation of ρ). Its
   method negative — plain-Borel does not transfer, G3 needs the q-Borel chain —
   is unaffected.
3. **`coupled_qsqrt3_recurrence`** — verdict untouched and correct; only the
   "corroborates the q-Gevrey/resurgent reading" gloss removed, replaced by the
   explicit statement that an algebraic negative carries no growth-class
   information.

**Precision:** raw-float64 counts byte-identical before/after (43/43, 6/6, 0/0);
none of the three is in the NEW-dirty list; the two with raw floats were already
on `raw-float64-baseline.json`. The ratchet RED is inherited.

### Original REMAINING section (superseded by the above)

| file | offending content |
|---|---|
| `computations/qbeta/qbeta_dladder_generating_function_structure_probe.py` | computes `divergent = bool(root_rising and C > 0 and ssr_ratio < 0.3)`; docstring §3 "super-exponentially DIVERGENT (radius → 0)", "spurious finite ρ≈0.143", "SAME divergent family as the κ-tower" |
| `computations/qbeta/qbeta_odd_channel_stokes_borel_probe.py` | whole premise — "characterize the **divergence class** of the bar-ODD Q_β D-ladder"; witness description asserts a drifting Gevrey order |
| `computations/qbeta/qbeta_dladder_coupled_qsqrt3_recurrence_probe.py` | docstring: NEGATIVE "⇒ … (corroborates the q-Gevrey/**resurgent** reading)" — the invalid step verbatim |

**All three have committed witnesses** (verified via `scriptFile` match +
`git ls-files`), in **three different states** — do not treat them alike:

| witness | state | work needed |
|---|---|---|
| `qbeta-dladder-generating-function-structure.witness.json` | **refuted verdict** — `data.super_exponentially_divergent = true`, `verdict` asserts κ-tower family + "finite-n shadow" | re-scope the boolean's meaning + verdict text, re-run |
| `qbeta-odd-channel-stokes-borel.witness.json` | **refuted framing, corroborating data** — see below | mostly relabelling |
| `qbeta-dladder-coupled-qsqrt3-recurrence.witness.json` | **verdict CORRECT** (`NO coupled ℚ(√3) P-recurrence up to (r≤4, D≤4)`); only the `description` gloss carries the invalid step | drop one clause, re-run |

**The middle one is the interesting case.** Its heading calls it the odd-channel
*"divergence class"*, but its own numbers point the other way:
`data.gevrey_order_drifts_down = true` (C falls `~0.08 → 0.05` as the tail
lengthens — the apparent divergence *weakens* with more terms); the description
already says *"NOT q-Gevrey-1 in any base > 1"*; and the Borel–Leroy pole runs
`0.147 → 0.165 → 0.249` for `s = 0.02 → 0.10 → 0.30`, so the small-`s` end is
**0.147**, within ≈ 3 % of `ρ = 0.142799996644689…` and trending toward it.

Scope-(a): that is *consistency with* the 2026-08-09 radius, **not** a
derivation of `ρ` from Borel–Leroy. But it means the data was pointing at the
true radius while the framing called the channel divergent — so re-scoping turns
those numbers from contradicted into supporting, and no measurement is lost.

> **Count correction.** An earlier revision of this bean said *"two committed
> witnesses"* and named one file. Wrong on both: three, in three states. Caught
> in review on PR #5039.

### The fix is re-scoping at the producer, NOT a re-run

The arithmetic is not wrong. At `k ≤ 21–27` the root test really does rise
without plateau and `C > 0` really does fit — so a re-run reproduces
`divergent = True` byte-for-byte and changes nothing. The **diagnostic**
misfired: with the true `d_k = −(1/(2h*_ρ))ρ^{−k}/k(1+O(1/k))`, the `1/k` factor
makes `|d_k|^{1/k}` approach `1/ρ` far too slowly to plateau in the available
window, and the `log` branch point makes a Domb–Sykes `1/k` fit noisy.

So the work is: **re-scope the verdict text and the boolean's meaning at the
producer** (e.g. rename to `root_test_rising_in_window` and state that this is
*consistent with* a `ρ^{−k}/k` law, not evidence against it), then re-run so the
witness regenerates honestly.

**Blocked here:** `sympy` is absent in this sandbox (`numpy` too), so none of the
three can be executed. Editing a docstring without the ability to re-run would
drift `scriptHash` and leave a stale witness — the failure mode AGENTS.md
§idle-backlog names explicitly. Needs an environment with `sympy`.

### Scope discipline for whoever picks this up

Scope-(a). Do **not** convert this into "the D-ladder has no interesting growth
structure" or into any exclusion of q-Borel methods. And do not touch the
**κ-tower** work: that ladder *is* genuinely divergent (Gevrey-1, Borel
singularity `A ≈ 0.7`) and its resurgence programme is unaffected. Same for
`qou-vkg5` (C1 at `∞`, irregular, slope `½`).

## Original brief (retained)

## The inference, and why it is invalid

Found in `docs/coordination/1ppq-qbeta.md` (framing bullet, corrected in place
2026-08-14):

> the odd channel … has no quantum-A-polynomial recurrence, **hence the
> resurgent/Écalle route**

**Non-holonomic does not imply divergent, and only a divergent series can be
resurgent.** The counterexample is the object under discussion: KC22's own
closed form

    D(w) = φ(w)·log(1 − w/ρ) + ψ(w),   φ, ψ algebraic over a degree-12 field

is **convergent** (`ρ = 0.1428`, `κ = 0`) *and* provably not low-order P-finite.
KC22 even says so in as many words — "a convergent series need not be
holonomic … exactly the sort of element that is not low-order P-finite" — so
the corpus already carries the refutation next to the bad inference.

This is a **separate defect** from the 2026-08-09 convergence correction. That
correction withdrew a conclusion drawn *from a divergence that turned out to be
absent*. This is a step that would have been invalid **even if the ladder had
diverged**: the premise (no holonomic recurrence) simply does not deliver the
conclusion (resurgent).

## Work

1. Grep the corpus — `docs/`, `content/`, `computations/`, `.beans/`, Lean
   docstrings — for the *step*, not the words. Patterns: "not holonomic" /
   "no P-finite" / "no A-polynomial recurrence" / "non-holonomic" appearing
   within a sentence or two of "hence"/"so"/"therefore" + "resurgent" /
   "transseries" / "Borel" / "Écalle" / "divergent".
2. For each hit, classify:
   - **(a) the invalid step** — asserts resurgence/divergence *from*
     non-holonomicity ⇒ correct it, citing the `φ·log + ψ` counterexample;
   - **(b) independently grounded** — the object is *separately* known to
     diverge (e.g. the Ohtsuki κ-tower: Gevrey-1, ratios 1.32→3.63→4.93, Borel
     singularity `A ≈ 0.7`) ⇒ leave; the conclusion is right even though this
     particular route to it would not be;
   - **(c) technique** — Écalle median / M-dictionary as a normalization
     scheme ⇒ leave.
3. Check the **converse** while in there: any claim that convergence implies
   holonomicity, or that holonomicity implies convergence. Both are also false
   and the same `φ·log + ψ` object refutes the first.

## Scope discipline

Scope-(a): this is "an inference step does not license its conclusion", **not**
"these objects are not resurgent". Several corpus objects *are* genuinely
divergent and resurgent — the κ-tower above, and C1 at `∞` (irregular, slope
`½`, the live `qou-vkg5`). Correcting the *route* must not be read as
withdrawing those. Do not convert any hit into a scope-(b) exclusion without a
proved invariant.

## Why it is worth a sweep

The corpus's recurring failure mode is a correct finding restated one step too
strongly, then relied on downstream. This one is cheap to check and, unlike the
convergence correction, does not depend on any numerical result — it is a
logical step that can be audited by reading.

---
## Sweep result (2026-08-15, session qou-gylf, PR #5037 branch)

> Merged with the concurrent #5050 session's work during rebase: its banners on
> the 07-12 divergence-correction + 07-13 coupled-recurrence files are kept
> (more detailed than this pass's, which are dropped); this pass's banners on
> the OTHER three files (rung-followup, 07-17 qgevrey-drift, moire) are novel
> and kept. The doc-sweep portion is DONE; the bean stays in-progress for the
> producer/witness re-scope above (blocked on sympy in both sandboxes).

Proximity sweep (premise terms within ±2 lines of conclusion terms) over
docs/ content/ computations/ .beans/: **32 candidates, classified**:

- **(a) the invalid inference step itself: 0 live sites.** Every occurrence of
  the step is inside the already-corrected ledger/registry text or this bean's
  own quotation of it (1ppq-qbeta.md 1846-1850, 3450-3451 = the correction).
- **STALE DIVERGENCE CONCLUSION (the 2026-08-09 withdrawal never propagated
  to the July audit files): 5 sites, now banner-marked at the claim site:**
  1. 2026-07-12-dladder-divergence-correction.md — whole conclusion reversed
     (its estimators missed the Q_b zero); top banner.
  2. 2026-07-12-bar-odd-s-deformed-rung-followup.md — Route-2 correction
     blockquote reversed a second time; inline banner.
  3. 2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md —
     result stands, "resurgent reading" framing stale; scope-note banner.
  4. 2026-07-17-dladder-extension-qgevrey-drift-confirmed.md — headline
     ("genuinely resurgent") withdrawn; k≤31 ladder + non-holonomicity stand.
  5. 2026-07-13-moire-resonance-framing-critical-assessment.md — surgical
     strikethrough of the D-ladder divergence attribution only; the GZ
     asymptotic series named there is a different object, genuinely
     divergent (class (b), untouched).
- **(b) independently grounded (κ-tower Gevrey-1, C1 at ∞): untouched.**
- **(c) technique usages (Écalle median / M-dictionary): untouched.**
- **Converse check (convergent⇒holonomic / holonomic⇒convergent): 0 hits**
  (only the registry's correct "convergent need not be holonomic").

Scope-(a) throughout: banners mark the withdrawn divergence claims; the exact
d_k ladders, non-holonomicity negatives, and genuinely-divergent objects all
stand as recorded.
