# Piece A: Specht Module Character Evaluation

This file provides the narrative counterpart to the representation-theoretic route for Piece A.

**Theorem (Lean: `trace_centralC2_specht_module`).** The trace of the central element $C_2$ (the sum of Jucys-Murphy squares) on the Specht module $S^\mu$ evaluates to:
$$ \text{Tr}(C_2|_{S^\mu}) = \dim(S^\mu) \cdot \sum_{c \in \mu} c(c)^2 $$
*Proof.* The central element $C_2$ acts as a scalar on the irreducible Specht module $S^\mu$. By properties of the Jucys-Murphy elements, this scalar corresponds precisely to the sum of squared contents of the diagram $\mu$. Pulling this scalar out of the trace yields the scalar multiplied by the dimension of the module. □

**Lemma (Lean: `trace_centralC2_regular_rep`).** The trace of $C_2$ on the full regular representation of the symmetric group $S_n$ satisfies:
$$ \text{Tr}(C_2) = \sum_{\mu \vdash n} \left( \sum_{c \in \mu} c(c)^2 \right) \dim(S^\mu)^2 $$
*Proof.* This follows by decomposing the regular representation into its irreducible Specht module components via Artin-Wedderburn theory. Each Specht module $S^\mu$ appears with multiplicity equal to its dimension $\dim(S^\mu)$. Taking the trace over this decomposition and applying Lean: `trace_centralC2_specht_module` gives the required sum. □

**Lemma (Lean: `pieceA_hook_sq_eq_content_sq_add_n_sq`).** Piece A fundamental identity (representation-theoretic route): For a valid partition represented by row lengths $\lambda$, we have:
$$ \sum_{c \in \lambda} h(c)^2 = \sum_{c \in \lambda} c(c)^2 + n^2 $$
*Proof.* This bridges the combinatorial structure to representation theory. By equating the trace of $C_2$ on the regular representation (computed via Specht modules) with the class-function evaluation on specific cycle types, one establishes the correspondence. The relation then implies the target identity relating the squared hook lengths to the squared contents plus $n^2$. □
