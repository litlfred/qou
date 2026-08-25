import { remark } from "../../schema/builders";

export default remark({
  label: "rem:alpha-wigner-supermultiplet-context",
  title:
    "The $A=4$ closure in the nuclear-physics literature: the Wigner $\\mathrm{SU}(4)$ supermultiplet",
  interprets: "conj:wigner-su4-from-spin-isospin",
  uses: ["prop:wigner-np-pairing"],
  cites: ["wigner1937", "satula1997"],
  tags: ["wigner-su4", "magic-shell", "phys-lit-context", "l3-binding"],
});
