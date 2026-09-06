---
# qou-pfh7
title: 'coupling normalisation: s² IS [2]_q − 2, so the coupling is a classical-value deviation — and W − W(1) vanishes at the wrong ORDER'
status: completed
type: task
priority: normal
created_at: 2026-09-05T06:17:05Z
updated_at: 2026-09-05T12:17:13Z
---

Owner "merge and coupling renorm" (2026-09-05). The open item qou-ix74 left: what normalisation relates the derived weak-vertex trace W(q) to the single-crossing coupling s² the decay rate actually uses.

Entry measurement (sympy, exact) — the pattern is DERIVED, not assumed:
- s² = (q^{1/2} − q^{−1/2})² = [2]_q − 2 EXACTLY. So the corpus's own single-crossing coupling is the q-dimension MINUS ITS CLASSICAL VALUE, [2]_1 = 2. That is what makes it vanish at q = 1 and stop beta decay classically, and it is the pattern any W-based replacement must follow.
- W(1) = 1/4 and W'(1) = 5, so W − W(1) vanishes to FIRST order in (q−1): W − 1/4 = 5(q−1) + (93/4)(q−1)² + …
- s² vanishes to SECOND order: s² = (q−1)² − (q−1)³ + …

So the two objects have different vanishing orders, which is a structural obstruction no q-independent constant can fix, and it prunes the whole family c·(W − W(1)). An order-matching bridge needs one factor vanishing as (q−1) (h, ℏ_q, s, q−1 are the corpus's candidates).

Plan: Lean the identity and the two vanishing orders (formalize-first pruning); probe the order-matched bridge candidates and report the residual honestly; audit doc. Do NOT fit a coefficient.


## Result (2026-09-05)

Branch `claude/weak-vertex-coupling-normalisation-2026-09-05`. One positive, one proved negative.

**POSITIVE — s² is derived, not conventional.** s² = (q^{1/2} − q^{−1/2})² = [2]_q − [2]_1 EXACTLY: the decay-rate coupling is the SU_q(2) fundamental dimension minus its classical value, which is why the rate vanishes at q = 1. First derivation of the SHAPE of s² in the corpus. Lean `sSq_eq_twoQ_sub_two`. This is what motivates the candidate family c·(W − W(1))·X — motivation derived, not assumed, so it is not the defined-residual failure mode.

**NEGATIVE — that family is excluded, scope-(b).** s² vanishes to 2nd order at q=1 (s²''(1)=2); W − W(1) to 1st (W'(1)=5). A bridge repairs the order, so order does not decide. What decides: the ratio RUNS — R(q) = (q+1)(4q¹²+4q¹⁰+8q⁸+8q⁶+8q⁴+7q²+1)/(4(q²+1)²), R → 5 at q→1, 8.5242 at q₀, 65.269 at 3/2, 695.91 at 2 — so no normalisation CONSTANT can absorb it. Required c is 100/69591 at q=2 vs 86528/5647625 at q=3/2. Lean `no_constant_rescaling`, `candidateRatio_two`, `candidateRatio_three_halves`, decided at two rational points. Every order-matched bridge (h, ℏ_q, s, q−1, h/2) carries leading coefficient W'(1)=5 times its own, never s²'s 1.

Producer `markov/weak_vertex_coupling_normalisation_probe.py` 7/7; both Lean files lean-direct exit 0, axioms clean; §7c split done on the gate's demand; precision gates 0 NEW dirty.

STILL OPEN (the real remainder): a W-based coupling of another SHAPE is untested — a ratio against another trace in the tower (the trefoil is the natural denominator, the corpus already reads the electron off its three crossings), a Jones-normalised object (V_K(1) = 1 for EVERY knot, so V − 1 has its normalisation fixed by topology rather than chosen), or a bar-parity component. What would settle it is deriving the coupling's normalisation from the rate formula's own construction, not another scan.

FOLLOW-UP: the same §7c mixed-content flag is latent in the two files merged earlier in this arc (WeakVertexT35TraceClosedForm, WeakVertexSubstitutionScale); unflagged only because the gate inspects changed files. Mechanical, name-preserving, not done here.


## 🛑 Superseded magnitude — the power was s⁴, not s² (2026-09-05, bean qou-xql6)

Every `1.19e4` / `10⁴` / "four orders of magnitude" figure in this bean is high by
`1/s² = 91.7694991484`. `substitutionRateFactor` was
`(weakVertexTrace q)² / (sSq q)²`, and **`sSq` is already `s²`** — `sSq_eq` even
says `q + q⁻¹ − 2` — so it computed `|W|²/s⁴`. The rate carries `s²` exactly once:
`prf:trace-ratio-observable` gives `|ℳ_q|² = |skein_amp|²·|tr(par)/tr(dau)|²` with
`skein_amp = q^{1/2} − q^{−1/2}`, *"the Skein amplitude at the beta-decay vertex"*,
and nothing else in the rate carries an `s`.

    |W|²/s⁴ = 11875.4418937      as recorded
    |W|²/s² =   129.405107404    the rate's actual power

**The verdict is unchanged.** At 129× the substituted half-lives land at 0.8–0.9 %
of observed — ~110× too short, where a 10–17 % shortening was wanted. So this
stays a scope-(a) negative; only "four orders of magnitude" is withdrawn, in
favour of "two orders, ~129×".

Producer `computations/markov/beta_rate_skein_power_audit.py` (9/9).


## 2026-09-05 — the §7c MIXED flag is REAL but TOOTHLESS here; the actual defect is upstream of it

Measured rather than assumed, before spending a tranche on it.

**The flag is real.** Both `QOU/Braiding/WeakVertexT35TraceClosedForm.lean` and
`QOU/Braiding/WeakVertexSubstitutionScale.lean` are MIXED — generic
`{K : Type*} [Field K]` for the algebra plus inline `ℝ` numeric-bound theorems
(`weakVertexTrace_near_q0`, `substitutionRateFactor_near_one_hundred_thirty`,
`sSq (1 : ℝ) = 0 ∧ …`). AGENTS.md §7c says the archimedean specialisation
"lives in a *separate* file" and "the generic block itself stays … without ever
mentioning `ℝ`".

**But §7c's own rationale is already void for these files.** The rule justifies
itself with: *"What is not cheap is the downstream code that inherits the wrong
specialisation and accretes archimedean assumptions silently."*
`WeakVertexT35TraceClosedForm` does **`import Mathlib.Tactic`**, which
transitively pulls in `Real`, and `WeakVertexSubstitutionScale` inherits that
through it. So no consumer is protected from archimedean deps by moving the
theorems out — the import cone already dominates.

**The fix is cheap and safe WHENEVER someone does it**, which is why there is no
urgency: both ℝ theorems have **zero external consumers** (grepped across
`content/**/*.lean`, excluding the two files themselves), and the companion
pattern already exists in this same arc
(`WeakVertexCouplingNormalisationArchimedean.lean`,
`WeakVertexJonesMarkovArchimedean.lean`). Nothing gets harder by waiting.

**The defect actually worth fixing is the one upstream:** the blanket
`import Mathlib.Tactic` violates AGENTS.md §8 ("Keep imports minimal — only
import what the file actually uses"), and it is *what makes* the §7c violation
harmless. Narrowing it would restore §7c's force and shrink the cone; it is
also the slower job (find which tactics are actually used) and it is NOT done
here.

**Recommendation (my judgement):** do the §7c move only as a rider the next
time either file is touched for a substantive reason, and treat the
`Mathlib.Tactic` narrowing as the real item. Churning two merged, verified Lean
files for a naming convention whose protective effect is nil is not worth a
verification cycle on its own.
