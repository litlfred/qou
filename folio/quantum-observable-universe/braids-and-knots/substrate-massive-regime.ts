import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:substrate-massive-regime",
  lean: { ref: "qou:QOU.OneDim.TLIsXXZChain.one_lt_anisotropy", validation: "leanok" },
  title:
    "The Temperley--Lieb anisotropy $\\Delta = \\tfrac{1}{2}(q + q^{-1})$ exceeds unity for every real $q \\neq 1$",
  uses: ["def:two-row-stratum", "prop:convention-d-kills-antisymmetriser"],
  cites: ["jones1985", "jimbo1986"],
  tags: [
    "temperley-lieb",
    "anisotropy",
    "convention-d",
    "one-dimensional",
    "spectral-regime",
  ],
});
