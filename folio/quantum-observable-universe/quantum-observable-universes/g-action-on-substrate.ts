import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:g-action-on-substrate",
  title:
    "Categorical $G = \\mathrm{SU}(2)_L \\times \\mathrm{U}(1)_Y$ action on the Frobenius–Hopf substrate",
  lean: { ref: "qou:QOU.QuantumObservableUniverses.GActionOnSubstrate", validation: "stub" },
  uses: [
    "def:frobenius-hopf-substrate",
    "rem:hecke-algebra-from-braiding",
    "prop:higgs-vacuum-residual-idempotent",
    "conj:electroweak-higgs-torus-link-triplet",
    "thm:hoefsmit-ew-cell-content",
  ],
  tags: [
    "tier:S",
    "g-action",
    "electroweak",
    "frobenius-hopf-substrate",
    "g-equivariance",
    "categorical-higgs",
    "n-sym",
    "open-problem",
  ],
  // The witness below provides the q_0 numerical anchor cited via
  // :val[q_0] in the body — it does NOT verify this conjecture
  // (which is tagged `open-problem`). Status reflects the
  // conjecture's open status, not the witness script's correctness.
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "not_run",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): , Lean `VacuumPairing.tr_proj_eq_one`) | that `computations/n_sym_numerical_anchor.py` obtains by dividing" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3):  for a unit-normalised cyclic trace (Lean: `VacuumPairing.tr_proj_eq_one`)." },
    {
      kind: "note",
      date: "2026-11-20",
      body: "**Owner ruling (2026-11-20): the host of $\\mathcal{N}_{\\rm sym}$ is left open.** Both readings stay recorded: (a) tensor product, $[4]_q^2[6]_q \\approx 107.89$; (b) direct sum as (G-1) states, $2[4]_q + [6]_q \\approx 14.61$, under which the composite trace of idempotents on orthogonal summands is $0$. Neither is to be selected by closeness to the back-solved target $213.11$ (no-fitting rule). Choosing (a) needs a structural reason for the tensor reading.",
    },
    {
      kind: "status",
      body: "**Open at the closure level.** The four axioms are a\n**concrete framework extension** that takes the QOU substrate\nfrom \"$\\mathbf{Rep}(\\mathrm{SU}_q(2))$-equivariant\" to\n\"$G \\times \\mathbf{Rep}(\\mathrm{SU}_q(2))$-equivariant\". The closed form of\n$\\mathcal{N}_{\\rm sym}$ is an open identification (2026-11-20 QA): reading (a), a tensor\nproduct of hosts, gives $[4]_q^2[6]_q \\approx 107.89$ at $q_0$ ($-49.4\\%$ against the\nCODATA-derived anchor 213.11); reading (b), the direct sum that (G-1) states, gives\n$2[4]_q + [6]_q \\approx 14.607$ ($-93.1\\%$). Neither is selected, and no factor has been\nre-tuned to recover a match.\n\n**To promote to `proposition`:**\n1. Fix the composition rule for $\\mathrm{tr}_F(e_{\\rm sym}^{\\rm EW}\\cdot e_H)$ across the hosts (tensor vs direct sum), from structure, not from the anchor value\n2. Account for the gap to the anchor under that rule\n3. Provide the unique-existence argument for the four axioms\n4. Author the Lean formalization",
    },
    {
      kind: "refined-framing",
      date: "2026-11-20",
      body: "**Owner ruling (2026-11-20): (G-4) corrected to $\\mathrm{tr}_F(e_H) = 1$.** (G-4) previously assigned $e_H$ the trace $[2]_q$, which (G-2) gives to all of $A^{(H)}$. A rank-one idempotent $e_H = \\varrho_\\Phi\\varrho_\\Phi^*/t$ factors through $\\mathbf{1}$, so for a unit-normalised cyclic trace $\\mathrm{tr}\\,e_H = \\mathrm{tr}\\,\\mathrm{id}_{\\mathbf{1}} = 1$ (Lean `QOU.QuantumObservableUniverses.VacuumPairing.tr_proj_eq_one`). Consequence: the closed form loses its $[2]_q$ factor, $\\mathcal{N}_{\\rm sym}(q_0) = [4]_q^2[6]_q \\approx 107.89$ against the target 213.11 (was $\\approx 216.96$, within 1.81%). The target, computed by `computations/n_sym_numerical_anchor.py`, is unchanged; that producer does not evaluate this closed form, so no witness moves.",
    },
    {
      kind: "caveat",
      date: "2026-11-20",
      body: "**Product of per-host $q$-dimensions withdrawn as a derivation (QA finding, 2026-11-20).** The derivation section wrote $\\mathrm{tr}_F(e_{\\rm sym}^{\\rm EW}\\cdot e_H)$ as $\\dim_q$ of $e_{\\rm sym}^{\\rm EW}[A^{(W^+)}\\oplus A^{(W^-)}\\oplus A^{(Z)}]$ and then multiplied $[4]_q[4]_q[6]_q$. $\\dim_q$ is additive over $\\oplus$ and multiplicative over $\\otimes$; and idempotents supported on orthogonal summands of (G-1) compose to $0$. The corpus does not fix which object is meant: (G-1) states a direct sum, while the product needs a tensor structure that only the disjoint-strand-pair realisation of `thm:hoefsmit-ew-cell-content` resembles (one $W$ slot, $H = T(2,8)$, so it does not match (G-2)). Both readings are now recorded with their values; neither is chosen. The phrase \"grounds Anchor II\" is removed, and 'unique' vortex morphism is scoped to 'unique up to a non-zero scalar (phase after the norm condition)'. Values: symmetric $[n]_q$, $q_0 = 1.10997859564273904668$, mpmath at 50 dps.",
    },
  ],
});