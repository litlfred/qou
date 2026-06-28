import { ContentBlock } from "../../pipeline/content-block";

export const atomicQReebUniversalRho = new ContentBlock({
  id: "prop:atomic-q-reeb-universal-rho",
  title: "Universal-ρ normalisation on the atomic q-Reeb object (Lever 3)",
  author: "QOU",
  tags: ["mass-theory", "q-reeb", "binding", "lever-3", "cal-4"],
  dependencies: [
    "def:q-reeb-flow",
    "def:markov-trace",
    "rem:cal4-discipline"
  ],
});
