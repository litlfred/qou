import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:brunnian-property-of-borromean",
  renamedFrom: ["conj:brunnian-property-of-borromean"],
  title:
    "Brunnian property of $\\mathcal{B}_3$: every two-component sub-link is the unlink",
  lean: {
    ref: "qou:QOU.BraidKnot.BorromeanBrunnianStrandDeletion.borromean_is_brunnian",
    sorryFree: true,
    validation: "leanok",
  },
  uses: [
    "def:borromean-baryon",
    "rem:borromean-topological-confinement",
  ],
  cites: ["kawauchi1996", "birman1974"],
  tags: [
    "tier:S",
    "borromean",
    "brunnian",
    "link-theory",
    "knot-complement",
    "color-confinement",
    "topology",
  ],
});
