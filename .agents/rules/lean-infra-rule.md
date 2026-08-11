# Lean proof infrastructure rule

When a Lean theorem needs Mathlib infrastructure to prove:

1. **BUILD the infrastructure locally.** Write helper lemmas, Tendsto proofs, continuity results, derivative bounds, etc. directly in the file or in a nearby `MathlibExt/` module.

2. **Do NOT** just add the conclusion as a class field ("context enrichment") unless the theorem is genuinely parameterized over abstract data where the conclusion is a hypothesis of the theorem's universe.

3. **Do NOT** just create a bean saying "needs Mathlib infra" and skip. Write the actual math.

4. **Bean only** genuinely open conjectures or proofs requiring 500+ lines of entirely new Mathlib theory (e.g., argument principle, Hadamard factorization theorem from scratch).

5. For everything else — Taylor bounds, limits, continuity of polynomials, geometric series sums, basic filter calculus — **prove it properly** using existing Mathlib lemmas.
