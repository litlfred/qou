import { proof } from "../../schema/builders";

export default proof({
  label: "prf:unified-iterative-correction",
  title: "Proof of unified iterative correction",
  uses: ["prop:unified-iterative-correction"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The obstruction is one of shape.  The formalised Wedderburn embedding\n`QOU.HeckeAlgebra.Wedderburn.blockDiagonal` is a concrete construction\n(axiom footprint `propext`, `Classical.choice`, `Quot.sound`), but it has\ntype\n\nthe RSK identity $\\sum_\\lambda (f^\\lambda)^2 = n!$, carried as the named\nhypothesis `RSKDimIdentity` and discharged by nothing here.\n\n— itself now a theorem (`trace_does_not_separate`,\n`exists_indistinguishable_by_every_traceFunctional`): whenever a block\n\nthat at $(2,1)$ needs $f^{(2,1)} = 2$; that value is now formalised\n(`SeminormalDimSmall.seminormalDim_p21`, via the Frame–Robinson–Thrall\nhook-length formula), so `trace_does_not_separate_p21` holds\nunconditionally.\n\nrather than merely permitted: `three_blockEntry_independent_p21`\nexhibits three linearly independent\n\n**Witness:** `mass-qvalue-by-level.witness.json` — every isotope" },
    {
      kind: "note",
      date: "2026-08-25",
      body: "**Provenance and scope (2026-08-25).** The witness named here is absent\nfrom the tree — added 2026-04-15 in commit `e2814e577f` under\n`folio-assistant/computations/`, lost in the miga migration. Recovered\n([analysis](https://github.com/litlfred/qou/blob/main/docs/audits/2026-08-25-atom-mass-complete-wedderburn-witness-recovered.md)), its `data.mass_by_level` does carry 19 rows\nfrom H to $^{208}$Pb, so the coverage claim below is fair, and its\n$\\mathrm{BW}(k{=}5)$ column is accurate ($^3\\mathrm{H} \\to {}^3\\mathrm{He}$:\n$0.018228$ against $0.01861$ measured).\n\nIts **assertions** are another matter. Seven of them test the inaccurate\nNF-trace column against experiment with a tolerance set just above each\ndiscrepancy — $Q({}^3\\mathrm{H} \\to {}^3\\mathrm{He})$ is recorded as\n*passing* at $13\\,017\\%$ error under a tolerance $14\\,319\\%$ of the\nexpected value. A bound sized to its own miss is a fit, and the owner\ndirective of 2026-08-25 is **no fitting**. The contrast is inside the same\nfile: $B(\\mathrm{T})$ and $B({}^3\\mathrm{He})$ carry tolerances of $0.0004$\nand $0.0001$ and are recorded as *failing* at $0.0\\%$ error.\n\nCite the $\\mathrm{BW}(k{=}5)$ figures if any; do not cite the NF-trace\nQ-values as confirmed.",
    },
    {
      kind: "note",
      date: "2026-09-05",
      body: "Bean qou-qb7p gave three reasons the corpus could not supply the Wedderburn-image step. Two were removed (bean qou-kp2z): wedderburnEmbed was opaque and registered a fourth axiom; it is now the concrete blockDiagonal and the opaque is deleted. The shape objection remains.",
    },
  ],
});
