# Deriving the q-Laplacian eigenvalue Σ[c][c+1] — pre-registration and result

Owner request, 2026-11-15: "try derive [the eigenvalue] Σ[c][c+1]".
Context: PR #8043 recorded that in `q-heat-kernel-peter-weyl` the factor ħ_q² is derived
(rem:q-laplacian-expansion) but the eigenvalue of Δ_ξ on a Wedderburn block is only asserted.

## Pre-registration (written before any Lean or computation)

The claim "Δ_ξ acts on V_λ by Σ_{□∈λ} [c(□)][c(□)+1]" splits into two steps. Each is judged
separately.

**Step 1 (algebra).** There is a central element C_n of H_n(q) that acts on every
Jucys–Murphy weight vector of shape λ (L_k acting by q^{2c_k}) by Σ_k [c_k][c_k+1].

- Success: a sorry-free Lean proof, over a generic commutative ring, of (a) centrality of C_n
  and (b) its action on a JM weight vector, from the existing `qJM` / `qJMInv` API.
- Honest limit fixed in advance: that every V_λ *has* a JM weight basis with eigenvalues
  q^{2c} is the seminormal form (Ram 1997 Thm 4.1). The corpus proves it only for the trivial,
  sign and (2,1) representations. Step 1 inherits that hypothesis; it does not remove it.
- Prediction: the symmetric-integer form passes; the Jackson-integer form as printed in the
  statement cannot be the eigenvalue of any element of the Laurent algebra in the L_k^{±1},
  because it needs q^{c}, not q^{2c}.

**Step 2 (geometry).** Δ_ξ, defined in rem:q-laplacian-expansion as
(Θ∧L_ξ)(L_ξ* ι_ξ) + (L_ξ* ι_ξ)(Θ∧L_ξ), acts on V_λ through C_n.

- Success: a corpus artifact that defines an H_n(q)-action on the space Δ_ξ acts on, shows Δ_ξ
  commutes with it, and identifies Δ_ξ with C_n (or any element with the same eigenvalues).
- Failure modes named in advance: no such action in the corpus (then the step stays open), or a
  consistency check that fails.
- Pre-registered check: compute Δ_ξ on 0-forms from its own definition and compare with
  Σ c(c+1) at q = 1.

**What would change compute.** Only if both steps close does the "A anyway" code change
(μ_λ = ħ_q² Σ[c][c+1], symmetric integers) become derived. If only Step 1 closes, the code stays
as it is and the gap moves from "the eigenvalue" to "Δ_ξ = C_n".

## Result

(filled in below after the work)
