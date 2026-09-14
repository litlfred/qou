import { remark } from "../../schema/builders";

export default remark({
  label: "rem:tl-is-the-xxz-chain",
  title:
    "The production trace computes in the algebra of a one-dimensional spin chain",
  interprets: "prop:substrate-massive-regime",
  uses: ["prop:substrate-massive-regime", "def:two-row-stratum"],
  cites: ["jones1985", "jimbo1986"],
  computation: {
    script: "computations/onedim/tl_is_the_xxz_chain_probe.py",
  },
  tags: [
    "temperley-lieb",
    "one-dimensional",
    "spin-chain",
    "convention-d",
    "bethe-string",
  ],
});
