import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-08",
      body:
        "**Lean sibling proves a degenerate witness.** `QOU.Hadron.exists` is " +
        "`Nonempty Hadron`, discharged by two `unknot` constituents at " +
        "`θ = φ = 0`. The statement above asserts the stability condition " +
        "$\\mathfrak{E}_{\\mathrm{cross}}(\\mathfrak{H}_p) < 0$; the `Hadron` " +
        "structure carries no crossing-energy field, so that condition is " +
        "*unstatable* against the type rather than merely unproved. The repair " +
        "is to give `Hadron` the field first, then discharge existence with the " +
        "intended Borromean-plus-Hopf-gluon witness — both steps blocked on the " +
        "Hecke NF reduction infrastructure. Class A + narrative audit: " +
        "`docs/audits/2026-08-08-narrative-lean-equivalence-nonempty-kernels.md`.",
      see: "docs/audits/2026-08-08-narrative-lean-equivalence-nonempty-kernels.md",
    },
  ],
  label: "prop:hadron-exists",
  title: "Existence of hadrons",
  lean: { ref: "qou:QOU.Hadron.exists",
    validation: "not_checked",
  },
  proofs: ["prf:hadron-exists"],
  tags: ["existence", "hadron"],
});
