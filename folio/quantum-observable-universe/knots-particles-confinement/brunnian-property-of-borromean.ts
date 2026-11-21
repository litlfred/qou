import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:brunnian-property-of-borromean",
  title:
    "Brunnian property of $\\mathcal{B}_3$: every two-component sub-link is the unlink",
  lean: {
    ref: "qou:QOU.KnotTheory.Brunnian.borromean_brunnian",
    validation: "stub",
  },
  uses: [
    "def:borromean-baryon",
    "rem:borromean-topological-confinement",
  ],
  cites: ["kawauchi1996", "dgkmsv2009"],
  tags: [
    "tier:S",
    "borromean",
    "brunnian",
    "link-theory",
    "knot-complement",
    "color-confinement",
    "topology",
    "conditional-on-class",
    "open-problem",
  ],
});
