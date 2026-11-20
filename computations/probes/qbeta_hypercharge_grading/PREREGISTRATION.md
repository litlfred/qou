# Pre-registration: a hypercharge grading as a quark/lepton separator for n⊗ν → p⊗e⁻

Bean `qou-99qc`. Written 2026-11-20 before any number was computed. Companion Lean:
`folio/quantum-observable-universe/lean/QOU/QuarkState/HyperchargeGradingNoGo.lean`.

## Question (owner, Carl, 2026-11-20 20:50)

Under premise L (lepton = a fourth strand carrying the same u/d doublet; ν in the T³ = +½ slot,
e⁻ in −½; PR #8673), is a neutrino "the same as an up quark" or "at a higher q power"? Today the
only strand grading is K = q^{2T³}, and PR #8661 proved n⊗ν and p⊗e⁻ share the K^{⊗4} weight, so
every K-weighted split is 0. Candidate second grading: hypercharge, q^{cY} with Y_quark = +1/3,
Y_lepton = −1 (from Q = T³ + Y/2, `lepton_hypercharge` in #8673).

## Redirect recorded (coordinator, before anything was built)

Hypercharge is an additive charge CONSERVED by the decay: Y(n⊗ν) = 3·(1/3) − 1 = 0 = Y(p⊗e⁻),
and T³ likewise. So any grading by a function of the conserved total charges gives the same total
weight on both sides, for every c. Instruction: prove this as a general no-go (generic field,
scope (b)), STOP the c-derivation, and report instead what in the corpus is NOT conserved by the
decay vertex: (i) the Higgs vacuum idempotent e_H (`HiggsVacuumResidual.lean`), (ii) colour.

## Pre-registered arms and expected outcomes (stated before computing)

1. **Total-weight (grouplike) grading.** Weight = Π over strands of q^{2T³}·g_type. Expected:
   equal on n⊗ν and p⊗e⁻ for all g_quark, g_lepton. Scope (b), invariant: separability of the
   charge (T³ depends only on flavour, Y only on strand type).
2. **Matrix level.** The charged-current exchange E⊗F on a quark⊗lepton pair commutes with the
   dressed grading (g_q K)⊗(g_ℓ K), and with the primitive charge operator 2Q⊗1 + 1⊗2Q. The
   strand-tracked crossing Ř intertwines the dressed gradings with the strand labels swapped.
3. **Markov-normalised trace with a per-strand scalar dressing.** Expected: the dressing cancels
   exactly (Tr(gKX)/Tr(gK) = Tr(KX)/Tr(K)), so the corpus-ruled convention-D functional is blind
   to c.
4. **Per-strand UNnormalised additive energy** Σ_strands g_type·(K-eigenvalue). This is the one
   functional NOT a function of conserved totals. Expected: split = (g_ℓ − g_q)(q − q⁻¹), zero iff
   g_ℓ = g_q. With g = q^{cY}: zero iff c = 0 (ordered field). This functional is NOT the ruled
   one; it would be a new premise. It will be reported as a symbolic family only.

## What will NOT be done

* No value of c is selected. No c is tuned to Q_β. If no corpus structure forces c, no Q_β number
  is computed (redirect + §NO FITTING). CODATA is not read.
* The candidates (i) Higgs idempotent and (ii) colour are reported with what each would need; no
  Q_β is computed from them unless forced.

## Pass/fail

Every Lean statement compiles lean-direct (`-DautoImplicit=false -s 65536`) with no `sorryAx`.
The probe checks arms 1–4 in exact sympy over Q(q, g_q, g_ℓ); any FAIL is reported as is.
