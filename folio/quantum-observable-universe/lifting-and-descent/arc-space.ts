import { definition } from "../../schema/builders";

export default definition({
  label: "def:arc-space",
  title: "Arc space $\\mathcal{L}(X)$ of the brane tower",
  tags: ["arc-space", "jet-scheme", "brane-tower", "motivic"],
  uses: [],
  cites: ["denef-loeser2001"],
  lean: {
    ref: "qou:QOU.LiftingDescent.LiftingDescentRoot.ArcSpace",
    validation: "not_checked",
  },
});
