---
# qou-sx5r
title: 'opt1-inductive: Ocneanu cyclicity via induction — abstract bricks (gen-trace-commute, one-g coset); two-g core residual'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-19T18:09:26Z
updated_at: 2026-11-18T07:46:25Z
parent: qou-59vq
---


## Progress: two-g reduction sub-bricks (2026-07-19)
Added gwg_of_lower (g·a·g = a + a·hh·g, far-commute+Hecke) and gwg_of_mid
(g·(b·f·c)·g = b·f·g·f·c, far-commute+braid) — the g·w·g reduction pieces for the
two-g case, sorry-free. Remaining crux: the ASSEMBLY — decompose w∈Hn over its
H_{n-1} cosets (w=a+bfc), apply these term-by-term, then trace-reduce both sides
of tr((ugv)(pgq)) via Markov+IH. Documented, not sorry'd.

STALE, re-measured 2026-08-26 (bean qou-k5jt).

This bean says the 'Remaining crux' is the ASSEMBLY of the two-g case, 'Documented, not sorry'd'. It has since been BUILT. QOU/Machinery/MarkovInductiveCyclicity.lean carries cyclic_one_g, cyclic_two_g and the gwg_* bricks -- 0 sorry, 0 axiom, 0 native_decide -- and cyclic_two_g's docstring states the conclusion is DERIVED, with hgwg/hCE each applied at two distinct argument tuples and no hypothesis restating two-g cyclicity.

What is genuinely still open is NOT the assembly:
  * the module is an ORPHAN -- 0 importers corpus-wide, and 0 consumers of
    cyclic_one_g / cyclic_two_g;
  * its hypotheses (hIH, hgwg, hCE) are discharged nowhere, so this is
    conditional-proved, not premise-established.

Also relevant: there are THREE disconnected formalizations of Markov-trace cyclicity in the corpus.
  1. QOU.HeckeAlgebra.MarkovTrace.MarkovTrace_cyclic -- was an axiom over an opaque heckeMul, ZERO consumers. REMOVED 2026-08-26; surface 22 -> 21 library / 198 -> 197 corpus.
  2. QOU.MathlibExt.MarkovTrace.character_append_comm -- PROVED, concrete: tr_rho(v ++ w) = tr_rho(w ++ v) via rho.eval_append + Matrix.trace_mul_comm.
  3. this module -- proved conditionally, orphan.

None is wired to another. Re-scope this bean to the wiring, not the assembly.

LIFT DELIVERED 2026-08-26 (qou-k5jt): QOU/Machinery/MarkovCosetLift.lean.

The step MarkovInductiveCyclicity's header names as 'the only step not mechanised in Lean' -- the linear lift of the single-coset grounding lemmas to a general w = a + sum b_i f c_i -- is now proved, sorry-free:

  tr_finset_sum             tr additive over a Finset sum
  gwg_trace_lower_shape     lower coset in E-shape (hh = hbar . 1)
  gwg_trace_mid_shape       mid coset in E-shape, via f^2 = 1 + hbar.f
  gwg_trace_cosetSum        THE LIFT -- supplies hgwg for w in coset form
  ce_trace_cosetSum         supplies hCE the same way

#print axioms: all five clean; two need only propext.

Needed [Algebra R A], which MarkovInductiveCyclicity deliberately lacks. That absence is WHY E had to stay an interface there: E(b.f.c) = z.b.c is not expressible without a scalar action, so the traced identity could only be assumed. The added instance weakens nothing -- every intended instance has it.

STILL OPEN, unchanged: cyclic_two_g remains conditional. Instantiating needs a concrete tower (algebra, memB, a trace with the Markov property, and a coset decomposition of each w). Conditional-proved is not premise-established.

CORRECTION to my own framing in PR #5820: I called MarkovInductiveCyclicity 'an ORPHAN -- 0 importers corpus-wide' as if notable. True, but the base rate guts it: 86 modules on disk under QOU/Machinery/, only 23 registered in QOU.lean. Being unregistered is the local norm, not evidence of abandonment. The new module is left unregistered for consistency.

- Round 72 (`lane-e667`): Formalized `qou-sx5r`, `qou-slck`, `qou-dgsw`, `qou-jfr8`, `qou-zoyv` in `QOU.Foundations.SandwichTraceCyclicityVectorBraidingReducedWordSeparationRibbonMonodromy` with 80-dps `mpmath` 2-commit witness stamp (`c95261a9c444144dd0cc07d50ddaabb0b496a13f` -> `c3e4ad1f706f5fd2e70cbb90c8c9bd7753ec1e10`, `scriptHash=e347a9e84468088888c8978781442fc5eb1e2e281357cbff708b7491a3fcbcb8`) in PR `litlfred/qou#8390` (`status: in-progress`).
