import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:root-of-unity-mtc-truncation",
  title:
    "At $q = e^{2\\pi i / k}$, the KLR algebra truncates to a Modular Tensor Category of non-abelian anyons",
  uses: [
    "conj:hecke-anyonic-substrate",
    "conj:crystal-graph-realization",
  ],
  cites: [
    "kitaev2006",
    "nayak2008",
    "bakalovkirillov2001",
    "khovanovlauda2009",
    "kashiwara1991",
  ],
  tags: [
    "anyon",
    "modular-tensor-category",
    "non-abelian-anyon",
    "root-of-unity",
    "klr",
    "crystal-truncation",
  ],
});
