import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:topological-mass-cat-transient",
  lean: { ref: "qou:QOU.TopologicalMass.cat_transient_localises_blowup",
    validation: "not_checked",
  },
  title: "Transient terms localise to blow-up centres (categorical)",
  tags: ["transient", "blow-up", "brane-boundary", "mass-defect"],
  uses: [
    "def:brane-boundary",
    "lem:topological-mass-cat-eigenspace",
  ],
  proofs: ["prf:topological-mass-cat-transient"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-10-10",
      body:
        "**Lean scope (bean `tmvac`).** The Lean module " +
        "`lean/QOU/TopologicalMass/cat_transient_localises_blowup.lean` is stated over a " +
        "generic commutative ring `R` and an arbitrary `R`-module (§7c: the statement is " +
        "linear algebra). The support clause — the transient component lies in the span " +
        "of the local kernels `ker 𝔡_{n+1}|_{p_i}` — is an explicit hypothesis, not derived; " +
        "the trace decomposition is derived from it by linearity, and the local " +
        "contributions are shown unique when the kernels are independent. The earlier " +
        "module defined its inputs as opaque reals and projected the decomposition back " +
        "out of a class field.",
    },
  ],

});
