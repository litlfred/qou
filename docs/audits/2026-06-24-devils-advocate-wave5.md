# Devil's-advocate audit — Wave 5 (numerology-prone hot zones)

**Watcher:** [`local/devils-advocate-watcher`](../../.claude/skills/local/devils-advocate-watcher.md)
**Date:** 2026-06-24 · **Branch:** `claude/lucid-gates-92e98s` · **Model:** claude-opus-4-8 · L1–L4 + adjudicator.

Wave 5 deliberately targeted the numerology-prone zones: the dressed-quark "numerology" block, the term-6 binding density (a hot area — recent main commits flag a term-6 `c_4` keystone as "a rounded fit"), the open Δ_λ per-isotope binding gate, the α-shift torus-knot binding, and the neutron β-decay Q-value.

## Results (5 blocks)

| Block | Verdict | Strongest objection |
|-------|---------|---------------------|
| [`alpha-shift-torus-knot`](../../content/quantum-observable-universe/mass-theory/alpha-shift-torus-knot.md) | **🔴 open-objection** | The Lean **defines** `alphaShift p k := k(p−1)` then "proves" `alphaShift = k(p−1)` by `rfl` (both the sibling stub the `lean.ref` resolves to *and* the library class) — a §3b-cond **rule-5 violation** (class axiomatizes its own conclusion); the real claim (pole-order maximality over partitions) is absent from Lean. |
| [`dressed-quark-numerology-at-q0`](../../content/quantum-observable-universe/observations/dressed-quark-numerology-at-q0.md) | 🟡 survivable | Honest "numerology" remark, but recasts a fit-selected ansatz residual as a "prediction"; its production sibling `HadronicMass.lean` hardcodes the 311.10/312.39 literals and a `norm_num`-on-constants "theorem" under a "Derived from …" docstring. |
| [`neutron-qvalue-symbolic`](../../content/quantum-observable-universe/particle-interactions/neutron-qvalue-symbolic.md) | 🟡 survivable | Honest about the "POSTULATED, NOT DERIVED" ansatz, but wires a **CODATA-masses** witness (not a Q_β witness) and prose/`.ts` name different scripts — a reproducibility-wiring defect. |
| [`term6-binding-density`](../../content/quantum-observable-universe/mass-theory/term6-binding-density.md) | 🟢 clean | Two broken witness links (date prefix dropped) — **auto-discharged this PR**. The "rounded fit" suspicion from main is a *different object* (m_p absolute-mass `c_4` Habiro residue, not this B(Z,N) α/β block). |
| [`mba-step09b-per-isotope-binding`](../../content/quantum-observable-universe/appendix-mass-binding-algorithms/mba-step09b-per-isotope-binding.md) | 🟢 clean | The status-label checker's `no-fit`/`sorry-free` flag is **rebutted by the lens**: those labels are scoped to E₀ and the τ-recurrence, not to the honestly-open Δ_λ gate. |

## Highlights

- **`alpha-shift-torus-knot` (open).** The cleanest example yet of the §3b-cond **rule-5** degenerate pattern: the class field *is* the conclusion (`alphaShift := k(p−1)`, then `alpha_shift_eq : alphaShift = k(p−1) := rfl`). The combinatorial content (maximality at `V_{(1^p)}`) is real and reproducible in the sympy witness, but the Lean adds nothing beyond `n = n`. Fix: restate the class to carry per-irrep pole bounds (genuine hypotheses), or demote the maximality direction to honest `sorry` + `-- Ref:`.

- **`mba-step09b` — the two-layer design validated.** The class-2 mechanical checker flagged this block (`no-fit`/`sorry-free` over a `sorry`), but the adversarial lens **rebutted** it: the labels are correctly scoped to E₀ and `prop:sl2-prolongation-recurrence`, and the block honestly flags Δ_λ as "the Track A blocker". This is exactly the intended division of labor — the cheap checker is high-recall, the lens is the precision filter. (Recorded as a `partial` label-proximity-hygiene note, not a surviving objection.)

- **`term6-binding-density` — corpus-grep prevented a false positive.** The wave deliberately fed the agent the main-branch "rounded fit" suspicion; it correctly disambiguated that the f2ff63c `{46,4,29}` fit is the *m_p absolute-mass* term-6 Habiro residue, a distinct object from this binding-density block — which already discloses its calibrated status. Clean, modulo the link fix.

- **Recurring class-1 again:** `dressed-quark` and `alpha-shift` both show the durable Lean encoding less than (or contradicting) the prose — the most consistent finding across all five waves.

## Auto-discharged this wave
- `term6-binding-density.md` — restored the `2026-05-02-` prefix on two witness links (separate `fix(link)` commit).

## Running tally (waves 1–5, 24 blocks)

**4 open-objection · 13 survivable-objection · 7 clean.** The four open-objections — `borromean-baryon-mass-formula` (λ_scale revival), `knot-factor-frobenius-pairing` (retracted ratio form + non-compiling Lean), `operator-selection-lp` (null-dual witness, now corpus-swept to 11), `alpha-shift-torus-knot` (defines-then-`rfl` Lean) — are all **durable-artifact defects** (Lean/witness/`.ts` encoding something the math or the corpus contradicts), not disputes about the underlying mathematics. That is the single most actionable pattern the adversary has surfaced.
