import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** The Lean class `RhoPrefactorStructural`'s " +
        "content field is " +
        "`rho_eq_qdim : |(rho : ℝ) - q_int d_lambda_star| ≤ (1 : ℝ) / 2` — " +
        "i.e. `ρ(𝔥) = round[dim_q λ*]`. **Rounding is an ordering notion**: " +
        "\"within one half\" is an absolute-value inequality, and there is no " +
        "`round` on a generic commutative ring. The three concrete instances " +
        "(deuterium, tritium, helium-3) discharge that inequality " +
        "numerically. `ℝ` is required by the shape of the claim itself.",
    },
  ],
  label: "conj:rho-prefactor-structural",
  lean: { ref: "qou:QOU.BraidKnot.RhoPrefactorStructural" },
  title:
    "Structural prefactor rule: $\\rho(\\mathfrak{H}) = \\dim_q(\\lambda^*(T_w))$",
  uses: ["conj:atom-knot-mass-derivation"],
  tags: [
    "tier:E",
    "sdp-multiplicity",
    "wedderburn",
    "prefactor",
    "structural-rule",
    "gap-a",
    "audit",
  ],
});
