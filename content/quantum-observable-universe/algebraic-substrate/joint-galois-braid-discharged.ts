import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:joint-galois-braid-discharged",
  title:
    "Joint motivic-Galois $\\times$ braid action commutes on every bi-filtration cell — discharged",
  uses: [
    "conj:joint-galois-braid-action",
    "def:hq-bi-filtration",
    "prop:explicit-central-idempotent",
    "prop:hecke-baer-star-generic",
    "prop:joint-galois-braid-figure-8-verified",
    "conj:two-filtration-bridge",
    "prop:two-filtration-bridge-small-cases",
  ],
  cites: [],
  tags: [
    "joint-action",
    "discharged",
    "general-case",
    "centrality",
    "bar-transposition",
    "graded-mikusinski",
    "theorem-level",
  ],
});
