import { definition } from "../../schema/builders";

export default definition({
  label: "def:qns-unit-layers",
  lean: { ref: "qou:QOU.FluidDynamics.qns_unit_layers" },
  title:
    "Unit layers of the $q$-NS classical limit: substrate (vanishing $\\nu_q$) and physical ($c_q$-rescaled, $\\nu_{\\mathrm{phys}} = 1/(2q)$)",
  uses: [
    "thm:q-ns-wellposedness",
  ],
  tags: [
    "navier-stokes",
    "classical-limit",
    "unit-convention",
    "fluid-dynamics",
    "millennium-problem",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The substrate/physical-layer pile-up answers are, per the witness `qns-tail-pileup-probe.witness.json`." },
    {
      kind: "status",
      date: "2026-08-14",
      body:
        "**Option C, owner-selected 2026-08-14** (rescaling decision brief: " +
        "`docs/audits/2026-08-14-qns-model-to-pde-uniformity-decomposition.md` " +
        "§5). Two explicit unit layers with the derived $c_q$ tie, mirroring " +
        "the q₀ ideal/experimental two-pin discipline, including its strict " +
        "never-straddle rule. Motivating measurement: the SF5 pile-up probe " +
        "(`qns-tail-pileup-probe.witness.json`) — the uniformity question's " +
        "answer is layer-dependent (substrate: pile-up real, exponent " +
        "≈ 0.83; physical: converted tail vanishes ≈ ε^1.17). Lean sibling " +
        "proves ν_phys = 1/(2q) exactly and the conversion identities; " +
        "lean-direct exit 0, sorry-free.",
    },
  ],
});
