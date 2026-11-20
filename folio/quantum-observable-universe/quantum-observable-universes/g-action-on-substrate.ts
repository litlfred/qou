import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:g-action-on-substrate",
  title:
    "Categorical $G = \\mathrm{SU}(2)_L \\times \\mathrm{U}(1)_Y$ action on the Frobenius–Hopf substrate",
  lean: { ref: "qou:QOU.QuantumObservableUniverses.GActionOnSubstrate", validation: "stub" },
  uses: [
    "def:frobenius-hopf-substrate",
    "rem:hecke-algebra-from-braiding",
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
    {
      kind: "status",
      body: "**Open at the closure level.** The four axioms above are a\n**concrete framework extension** that takes the QOU substrate\nfrom \"$\\mathbf{Rep}(\\mathrm{SU}_q(2))$-equivariant\" to\n\"$G \\times \\mathbf{Rep}(\\mathrm{SU}_q(2))$-equivariant\". With\n$\\mathrm{tr}_F(e_H) = 1$ (see the 2026-11-20 note below) they give\n$\\mathcal{N}_{\\rm sym}(q) = [4]_q^2 \\cdot [6]_q \\approx 107.89$ at $q_0$,\n49.4% below the CODATA-derived target 213.11. No factor has been\nre-tuned to recover a match.\n\n**To promote to `proposition`:**\n1. Account for the gap to the target (the former 1.81% agreement\n   rested on a $[2]_q$ factor that (G-4) does not supply)\n2. Provide the unique-existence argument for the four axioms\n3. Author the Lean formalization",
    },
    {
      kind: "refined-framing",
      date: "2026-11-20",
      body: "**Owner ruling (2026-11-20): (G-4) corrected to $\\mathrm{tr}_F(e_H) = 1$.** (G-4) previously assigned $e_H$ the trace $[2]_q$, which (G-2) gives to all of $A^{(H)}$. A rank-one idempotent $e_H = \\varrho_\\Phi\\varrho_\\Phi^*/t$ factors through $\\mathbf{1}$, so for a unit-normalised cyclic trace $\\mathrm{tr}\\,e_H = \\mathrm{tr}\\,\\mathrm{id}_{\\mathbf{1}} = 1$ (Lean `QOU.QuantumObservableUniverses.VacuumPairing.tr_proj_eq_one`). Consequence: the closed form loses its $[2]_q$ factor, $\\mathcal{N}_{\\rm sym}(q_0) = [4]_q^2[6]_q \\approx 107.89$ against the target 213.11 (was $\\approx 216.96$, within 1.81%). The target, computed by `computations/n_sym_numerical_anchor.py`, is unchanged; that producer does not evaluate this closed form, so no witness moves.",
    },
  ],
});
