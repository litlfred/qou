import { example } from "../../schema/builders";

export default example({
  interprets: "def:rigid-dualizing-complex",
  label: "ex:rigid-dualizing-brings",
  title:
    "Constructive rigid dualizing complex for Bring's coordinate ring",
  tags: [
    "brings-surface",
    "dualizing-complex",
    "constructive",
    "hochschild",
  ],
  uses: [
    "def:rigid-dualizing-complex",
    "def:brings-coordinate-ring",
  ],
  cites: [
    "woronowicz1988",
  ],
});
