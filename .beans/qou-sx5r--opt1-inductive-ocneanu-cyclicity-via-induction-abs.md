---
# qou-sx5r
title: 'opt1-inductive: Ocneanu cyclicity via induction — abstract bricks (gen-trace-commute, one-g coset); two-g core residual'
status: todo
type: task
priority: normal
created_at: 2026-07-19T18:09:26Z
updated_at: 2026-08-26T06:47:15Z
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
