import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:on-p-modular-hecke",
  title:
    "Modular Hecke at $q = \\zeta_p$ corresponds to nimber surreals $\\mathbf{On}_p$",
  lean: { ref: "qou:QOU.AppendixSurreals.OnPModularHecke", validation: "stub" },
  tags: [
    "tier:P",
    "surreal-numbers",
    "characteristic-p",
    "nimbers",
    "modular-hecke",
    "kazhdan-lusztig",
    "root-of-unity",
    "p-ary-fusion",
    "open-problem",
  ],
  uses: [
    "prop:hoefsmit-is-surreal-construction",
    "rem:algebraic-core-survives",
  ],
  cites: ["conway1976", "gonshor1986", "ehrlich2012"],
  authorNotes: [
    {
      kind: "status",
      body: "**Open**. The conjecture is harder than its char-0 counterpart\nbecause:\n\n1. Mathlib's nimber-arithmetic library is even less developed\n than its surreal library.\n2. Modular Hecke combinatorics requires Kazhdan--Lusztig cell\n theory, also under-developed in formalisation.\n3. The $p$-ary sign-sequence-to-nimber map is not as \n recursive as Conway's binary case.\n\nA first goal would be to verify the conjecture for $H_3(\\zeta_2)$\n(the simplest non-trivial case) by hand: KL cells of $H_3$ at $q\n= -1$ should match the first few elements of $\\mathbf{On}_2$.",
    },
  ],
});
