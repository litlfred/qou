import { block } from "../../../scripts/lib/html_nodes.ts";
import { parseMarkdown } from "../../../scripts/lib/markdown.ts";

export const toroidalHarmonicsDeltaLambda = block(
  "toroidal-harmonics-delta-lambda",
  {
    title: "Toroidal Harmonics and the Δ_λ Mass Gap",
    authors: ["Claude"],
    is_mathematics: true,
    dependencies: [
      "he4-two-row-dominance",
      "interface-knot-markov-z"
    ],
    witnesses: [
      "computations/qbeta/toroidal_harmonics.py"
    ]
  },
  parseMarkdown(__dirname, "toroidal-harmonics-delta-lambda.md")
);
