import { definition } from "../../schema/builders";

export default definition({
  label: "def:ns-regular-qou",
  title: "NS-regular quantum observable universe",
  uses: [
    "def:quantum-universe",
    "def:q-navier-stokes",
    "def:recursive-brane-tower",
    "def:quantum-characteristic-classes",
  ],
  tags: [
    "definition",
    "navier-stokes",
    "obstruction",
    "euler-characteristic",
    "categorical",
  ],
});
