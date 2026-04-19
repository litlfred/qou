import { remark } from "../../schema/builders";

export const massTowerSYTCells = remark({
  label: "rem:mass-tower-syt-cells",
  title: "SYT / Jucys\u2013Murphy reindexing of the mass tower pair set",
  interprets: "rem:mass-endomorphism-jet-tower",
  uses: [
    "rem:mass-endomorphism-jet-tower",
    "prop:mass-endomorphism-tower",
    "thm:markov-trace-factorization",
    "def:recursive-brane-tower",
    "def:descent-involution",
  ],
  tags: ["mass-tower", "jucys-murphy", "syt", "audit"],
});
