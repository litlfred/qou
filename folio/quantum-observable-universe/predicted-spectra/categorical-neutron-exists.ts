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
        "`QOU.CategoricalNeutron.exists` is `Nonempty CategoricalNeutron`, " +
        "discharged by `skein_ud = skein_dd = 0` — a zero-mass neutron. As " +
        "for the proton, the statement above asserts an LP-stable element of " +
        "$H_3(q)$ while `CategoricalNeutron` carries no properties, so the " +
        "claim is *unstatable* against the type rather than merely unproved. " +
        "Blocked on the Hecke NF reduction infrastructure. Class A + " +
        "narrative audit: " +
        "`docs/audits/2026-08-08-narrative-lean-equivalence-nonempty-kernels.md`.",
      see: "docs/audits/2026-08-08-narrative-lean-equivalence-nonempty-kernels.md",
    },
  ],
  label: "prop:categorical-neutron-exists",
  title: "Existence of the categorical neutron",
  lean: { ref: "qou:QOU.CategoricalNeutron.exists",
    validation: "not_checked",
  },
  uses: ["def:categorical-neutron", "prop:categorical-proton-exists"],
  proofs: ["prf:categorical-neutron-exists"],
  tags: ["existence", "neutron", "baryon"],
});
