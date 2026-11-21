import { definition } from "../../schema/builders";

export default definition({
  label: "def:mass-energy",
  title: "Energy of a braid class ($\\mathfrak{E} = \\mathfrak{m} \\cdot c_q^2$)",
  tags: [
    "mass-energy",
    "speed-of-light",
    "information-theory",
  ],
  lean: { ref: "qou:QOU.Information.energy",
    validation: "not_checked",
  },
  uses: ["def:information-speed-of-light", "def:mass-identity"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Until 2026-11-15 this block was `thm:mass-energy-equivalence`, claiming that the " +
        "crossing energy equals mass times $c_q^2$. Its Lean proof held only because mass " +
        "was defined there as $E\\,(q-1)^2$, and with the mass of `def:mass-identity` the " +
        "claim is false (trivial braid: crossing energy $0$, mass nonzero). Owner ruling: " +
        "energy is now defined as $\\mathfrak{m}\\,c_q^2$; crossing energy keeps its " +
        "subscript. Open question on a crossing-additive energy: bean `qou-078y`.",
    },
  ],
});
