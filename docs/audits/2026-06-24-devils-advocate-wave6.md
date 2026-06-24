# Devil's-advocate audit — Wave 6 (formal backing of the core claims)

**Watcher:** [`local/devils-advocate-watcher`](../../.claude/skills/local/devils-advocate-watcher.md)
**Date:** 2026-06-24 · **Branch:** `claude/lucid-gates-92e98s` · **Model:** claude-opus-4-8 · L1–L4 + adjudicator.

Wave 6 targeted the **formal backing of the core claims** — the central calibration-cohomology identity, the canonical Wedderburn weight, the unified knot-mass theorem — plus two blocks the mechanical class-2 checker had flagged (a Bucket-B `: True` and a Bucket-C1 `sorry-free`-contradiction), so the lens could adjudicate the checker. (Three of the five agents hit transient API-529 overloads on first dispatch and were re-run.)

## Results (5 blocks)

| Block | Verdict | Strongest objection |
|-------|---------|---------------------|
| [`calibration-cohomology-alignment`](../../content/quantum-observable-universe/mass-theory/calibration-cohomology-alignment.md) | **🔴 open-objection** | The central `theorem calibrations_eq_cohomology` is a self-assuming projection (`:= by rw [A.align1,A.align2,A.align3]`, the alignments being axiomatic struct fields) — it proves **nothing** about Bring cohomology — yet `.ts` declares `validation: "validated"`, kind `proposition`. |
| [`knot-mass-formula-unified`](../../content/quantum-observable-universe/mass-theory/knot-mass-formula-unified.md) | **🔴 open-objection** | `lean.ref` resolves to a `degenerate(field)` projection (`:= ctx.claim_boxed_six_term_expansion`, audit-confirmed); the "closed-form" banner is contradicted by the body ("ρ_K spectral closure remains open", "Markov-invariance-broken at q₀"); **4 of 5 cited witnesses missing**. |
| [`wedderburn-weight-canonical`](../../content/quantum-observable-universe/mass-theory/wedderburn-weight-canonical.md) | 🟡 survivable | The self-conjugate `y_λ = ỹ_λ` identity is **circular**: at n=3 the only self-conjugate λ is (2,1), where the cited probe gives `y/ỹ ≈ 0.43 ≠ 1`. The identity holds only under a tautological definition of `y_λ`; witnesses are deprecated/relocated under `status:"verified"`. |
| [`b1-figure-8-row-theorem`](../../content/quantum-observable-universe/appendix-surreals/b1-figure-8-row-theorem.md) | 🟡 survivable | A §0a shadow-stub (`theorem b1_figure_8_row : True := by trivial`) that should be deleted (a real library decl exists), and that library decl is itself a §3b-cond rule-5 projection; `.md` says "Theorem-level (no conditional)" but the Lean is conditional. |
| [`wenzl-positivity-implies-substrate-positivity`](../../content/quantum-observable-universe/appendix-surreals-archimedean/wenzl-positivity-implies-substrate-positivity.md) | 🟢 clean | **Bucket-C1 false positive** — the checker matched `sorry` in a *doc comment* and `sorry-free` in prose; the block is an honest `conjecture`/`open-problem`. |

## Highlights

- **Two opens, both on the formal backing of central claims.** `calibration-cohomology-alignment` and `knot-mass-formula-unified` both have a Lean "theorem" that *assumes its own conclusion* (`rw` by axiomatic fields / `:= ctx.claim`). The underlying mathematics is sound in each case (genus-4 ⇒ `dim H¹ = 2g = 8`; the Frobenius co-Casimir values at n≤5 are real `rfl` theorems), but the headline formal artifact verifies nothing — and `calibration-cohomology` compounds it with `validation: "validated"` in the manifest. This is the same self-assuming-projection class as the α-shift (wave 5) and three-calibration-discipline (wave 1) Lean, now hitting the **most load-bearing** claims.

- **`wedderburn-weight-canonical` closes the loop on the §7aa conflation.** Wave 3 found `mba-step05` conflated `ỹ_λ` with the Markov `y_λ`; wave 6 shows the *canonical-definition* block does not cleanly resolve it either — the self-conjugate identity is circular under the cited witnesses. This is a corpus-level normalization ambiguity, not a single-block slip.

- **The checker adjudicated, and self-corrected.** `wenzl-positivity` was a Bucket-C1 false positive (the checker matched `sorry` in a Lean comment). I fixed `status_label_overclaim_audit.py` to strip Lean comments before matching; the **SHARP count corrected 95 → 42**. `b1-figure-8` refined the other way — a *real* problem, but mis-located by the checker's stale verbatim quote (the `: True` is the sibling shadow-stub; the resolved decl is a separate projection). Both show the intended division of labor: cheap checker flags, lens adjudicates and tunes the checker.

## Checker correction (this PR)

`status_label_overclaim_audit.py` now strips `/- … -/` and `--` Lean comments before testing the `sorry`/`:True`/`trivial` signals. Corrected counts: **214 candidates, 42 sharp** (was 227 / 95). The [overclaim triage](2026-06-24-status-label-overclaim-triage.md) Bucket-B/C1 lists should be regenerated against the 42-sharp set; the wenzl-class comment false positives are gone.

## Running tally (waves 1–6, 29 blocks)

**6 open-objection · 15 survivable-objection · 8 clean.** The two newest opens make the dominant pattern unambiguous: **every open-objection is a durable-artifact defect** — a Lean theorem / witness / `.ts` that encodes less than, or contradicts, the mathematics or the corpus. None disputes the underlying math. The single highest-value remediation remains: **finish or honestly demote the self-assuming-projection Lean on the central claims** (`calibration-cohomology-alignment`, `knot-mass-formula-unified`, `alpha-shift-torus-knot`, `three-calibration-discipline`).
