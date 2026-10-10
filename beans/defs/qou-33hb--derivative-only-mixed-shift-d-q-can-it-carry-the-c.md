---
# qou-33hb
title: 'Derivative-only mixed-shift D_q: can it carry the C1 kernel L_K as its symbol? (W2 dictionary test)'
status: completed
type: task
priority: normal
created_at: 2026-09-04T03:31:01Z
updated_at: 2026-09-04T10:42:56Z
---


PLAN (2026-09-04). Owner: "the derivative-only mixed-shift D_q". Route: read the
C1 kernel L_K = (q^2 x - 1) sigma^2 - (q-1) sigma - (q-1) in the ramified shift
calculus, in the two natural dictionaries (sigma = unit t-shift; sigma = t-shift 2
on the double cover), and test the derivative-only class against it via the
constant-seed invariant. Formalize first (QOU.Mass.C1KernelAsShiftSum), then
exact probe, then audit doc + a scope sentence on the conjecture block.


## RESULT (2026-09-04, PR #6582, commits c830ce8a40 + 59cdfad6b6)

**No derivative-only mixed-shift D_q can have the C1 kernel as its symbol** — scope-(b), invariant named: a derivative-only sum kills the constant seed t⁰ (`sumOp_derivativeOnly_const`, generic CommRing), the kernel's zeroth-order term evaluates it to −(q−1) (dictionary (a): σ = unit t-shift, x = q^e) / −(u²−1) (dictionary (b): double cover, σ = t-shift 2). `derivativeOnly_ne_c1KernelOp` / `derivativeOnly_ne_c1KernelOpCover` in `QOU.Mass.C1KernelAsShiftSum`, sorry-free, axioms propext/choice/Quot.sound. If the conjecture holds, D_q has a non-derivative component — #6474's clause by a third route (kernel shape), independent of residue (#6498) and residual (#6523).

Where the kernel sits: under (a) it is literally the corpus recurrence `[m+2]_q b_{m+2} = b_{m+1} + b_m` in the geometric qint × (q−1) (`c1KernelOp_eq_recurrence`), in the #6474 admissible class (odd shift, constant weight −(q−1)); residue dead at level 1, alive at level 2 = (q−1)²(a₀−a₁) — reads the branch value, which the derivative-only candidate (level-2 residue −a₁) cannot. Under (b) all shifts even, commutes with covering monodromy, residue −(u²−1)a₀ at level 1. The two dictionaries disagree on parity = W2 in its sharpest form; not settled here.

Honest scope: D_q NOT constructed; conditional on kernel = symbol; dictionary not derived. Probe over-claim corrected before commit (L(t⁰) supported on {−1,0}, not {0}).

Artifacts: `content/quantum-observable-universe/lean/QOU/Mass/C1KernelAsShiftSum.lean`, `computations/probes/derivative_only_dq_vs_c1_kernel_probe.py`, `docs/audits/2026-09-04-derivative-only-dq-vs-c1-kernel.md`, scope paragraph on `mass-theory/qdifference-kernel-prolongation-symbol.md` (sidecar re-swept).

Waiting on: owner merge permission for #6582.



Merged as PR #6582 (rebase-merge, main b16d5da1db, 2026-09-04). Follow-on: the dictionary/parity question (which t-shift σ is) opened as its own bean.



## CORRECTION (2026-09-04, level-reading bean): #6582 read σ as a t-shift; the conjecture's x = q^m is the body order = jet level. The theorems stand; the sentence 'if the conjecture holds D_q has a non-derivative component' is re-derived on the correct axis in the level-reading tranche (derivative-like shift-2 ⇒ level-1 residue vanishes).
