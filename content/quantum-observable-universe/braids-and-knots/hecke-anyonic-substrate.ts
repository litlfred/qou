import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:hecke-anyonic-substrate",
  title:
    "Iwahori–Hecke algebra is the anyon algebra: every QOU particle is anyonic before observation",
  uses: [
    "def:hecke-normal-form",
    "def:observation",
  ],
  cites: [
    "kassel1995",
    "kitaev2006",
    "nayak2008",
    "khovanovlauda2009",
  ],
  tags: [
    "anyon",
    "braid-group",
    "hecke-algebra",
    "topological-statistics",
    "observation-frame",
  ],
});
