---
# qou-arvu
title: "Corpus sweep: does 'non-holonomic hence resurgent' appear elsewhere?"
status: in-progress
type: task
created_at: 2026-08-14T20:02:00Z
updated_at: 2026-08-14T21:58:00Z
---

Spun out of `qou-tdp0` step 1 (owner-directed, 2026-08-14).

## SWEEP DONE 2026-08-14 — docs fixed; three producers REMAIN (blocked on sympy)

Full findings: [`2026-08-14-non-holonomic-implies-resurgent-corpus-sweep.md`](../docs/audits/2026-08-14-non-holonomic-implies-resurgent-corpus-sweep.md).

**5 class-(a) sites** found across 22 candidate files. Two were prose and are
fixed on this branch; **three are producers and are NOT fixed** — they are the
remaining work on this bean.

### Fixed (prose, no producer hash touched)

- `docs/audits/2026-07-12-dladder-divergence-correction.md` — SUPERSEDED banner.
  Its **title** asserted the refuted conclusion. The banner names the specific
  defect: its central "no singularity at ρ" argument ran a search that **omitted
  the `Q_b` zero** `q*_ρ ≈ 1.48989` whose image *is* `ρ = 0.1428`.
- `docs/audits/2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md`
  — banner + two clauses struck. Its exact linear algebra is untouched and
  correct; only the "tightens the resurgent reading" interpretation is withdrawn.

### REMAINING — three producers, and two committed witnesses that assert a refuted verdict

| file | offending content |
|---|---|
| `computations/qbeta/qbeta_dladder_generating_function_structure_probe.py` | computes `divergent = bool(root_rising and C > 0 and ssr_ratio < 0.3)`; docstring §3 "super-exponentially DIVERGENT (radius → 0)", "spurious finite ρ≈0.143", "SAME divergent family as the κ-tower" |
| `computations/qbeta/qbeta_odd_channel_stokes_borel_probe.py` | whole premise — "characterize the **divergence class** of the bar-ODD Q_β D-ladder"; witness description asserts a drifting Gevrey order |
| `computations/qbeta/qbeta_dladder_coupled_qsqrt3_recurrence_probe.py` | docstring: NEGATIVE "⇒ … (corroborates the q-Gevrey/**resurgent** reading)" — the invalid step verbatim |

`qbeta-dladder-generating-function-structure.witness.json` currently records
`data.super_exponentially_divergent = true` and a `verdict` string asserting the
κ-tower family membership and the "finite-n shadow" reading. **This is a
committed witness carrying a refuted conclusion.**

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
