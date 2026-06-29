The proof occupies §3--5 of Jones (1987); we take the result as axiomatic
and encode it as a Lean structure whose fields are the three properties above.
The formal goal is to verify that downstream theorems — the unity of the Markov trace and the detection of all irreducible representations — follow from these axiomatized structure fields. The trace's required properties are isolated as axiomatic structure fields, separating the external existence proof from the internal verification of its consequences in the observable mass spectrum.

**Mathematical Novelty:** The theorem itself is a standard result due to Jones, with no new mathematical argument. The novel contribution of this work lies in the formalization: the faithful structure-encoding of the three trace properties alongside the $R_q = \mathbb{Z}[q, q^{-1}]$ ground-ring framing, which constitutes careful engineering to support downstream machine-checked proofs.
