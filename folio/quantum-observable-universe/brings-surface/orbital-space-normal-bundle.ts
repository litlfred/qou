import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`): `2026-09-04-borromean-quark-carriers-trivial.lean` (`T2`) exhibits a definitional instance of the local `BorromeanQuark` carrier.",
      see: "docs/audits/2026-09-04-borromean-quark-carriers-trivial.lean",
    },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "note",
      date: "2026-11-24",
      body: "Dependency cycle cut (`dcy4`): removed forward cross-chapter `conj:reidemeister-mass-invariance` from `uses[]`; the normal-bundle section space and $q$-Laplacian spectrum here do not invoke the mass-theory Reidemeister-invariance conjecture.",
    },
  ],
  label: "conj:orbital-space-normal-bundle",
  title:
    "The orbital space at shell $n$ is the space of framing-$k$ sections of the normal bundle",
  tags: [
    "orbital",
    "normal-bundle",
    "framing",
    "laplacian",
    "eigenmode",
    "resonance",
    "trefoil",
    "seifert-surface",
  ],
  lean: { ref: "qou:QOU.orbital_space_normal_bundle",
    validation: "not_checked",
  },
  uses: [],
});
