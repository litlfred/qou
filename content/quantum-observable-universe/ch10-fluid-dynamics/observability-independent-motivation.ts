import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-observable-universe",
  label: "rem:observability-independent-motivation",
  title:
    "Independent motivation for observability: why $\\mathrm{Hom}(\\mathbf{1}, \\mathrm{Ad}(A)) = 0$ is not an NS assumption",
  uses: [
    "def:quantum-observable-universe",
    "def:quantum-universe",
    "thm:ns-singularity-descartes",
    "thm:observability-q-independent",
  ],
  tags: [
    "observability",
    "motivation",
    "independence",
    "gauge-theory",
    "contact",
    "measurement",
  ],
});
