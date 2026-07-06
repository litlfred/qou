import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:classical-limit-functor",
  label: "rem:classical-limit-topology-free",
  title:
    "Topology-free surreal reformulation of the $q\\to1$ limit",
  uses: [
    "def:classical-limit-functor",
    "def:classical-limit-obstruction",
  ],
  tags: [
    "classical-limit",
    "surreal",
    "standard-part",
    "q-to-1",
    "topology-free",
  ],
});
