import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:skein-shell-correction",
  title:
    "Shell corrections from Skein polynomial factorization of the multi-nucleon link",
  tags: [
    "shell-correction",
    "skein-polynomial",
    "factorization",
    "stability-pairs",
    "closed-sublink",
    "binding-energy",
  ],
  uses: [
    "def:skein-binding-lagrangian",
    "def:stable-nucleus",
    "def:hadron",
    "prop:beta-stability",
    "prop:integer-stability",
    "rem:skein-crossing-asymmetry",
    "def:crossing-energy",
    "conj:elliptic-stability-locus",
  ],
});
