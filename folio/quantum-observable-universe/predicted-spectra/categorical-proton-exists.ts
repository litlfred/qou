import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
    {
      kind: "caveat",
      date: "2026-08-08",
      body:
        "**Lean sibling proves a degenerate witness.** " +
        "`QOU.CategoricalProton.exists` is `Nonempty CategoricalProton`, " +
        "discharged by `skein_uu = skein_ud = 0` — a zero-mass proton. The " +
        "statement above asserts membership in $H_3(q)$ and Frobenius " +
        "stability $G x[\\gamma] \\ge 0$; `CategoricalProton` carries two " +
        "reals and two defaulted fields and no properties, so neither claim " +
        "is *statable* against the type. A sharper witness is therefore not " +
        "the repair — the structure must carry its defining properties first, " +
        "which is blocked on the Hecke NF reduction infrastructure. Class A + " +
        "narrative audit: " +
        "`docs/audits/2026-08-08-narrative-lean-equivalence-nonempty-kernels.md`.",
      see: "docs/audits/2026-08-08-narrative-lean-equivalence-nonempty-kernels.md",
    },
  ],
  label: "prop:categorical-proton-exists",
  title: "Existence of the categorical proton",
  lean: { ref: "qou:QOU.CategoricalProton.exists",
    validation: "not_checked",
  },
  uses: ["def:categorical-proton"],
  proofs: ["prf:categorical-proton-exists"],
  tags: ["existence", "proton", "baryon"],
});
