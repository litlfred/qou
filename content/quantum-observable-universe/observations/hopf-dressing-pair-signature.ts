import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hopf-dressing-pair-signature",
  title: "Photon Hopf dressing $\\varphi_{01}$ is the monotone driver of pair creation",
  interprets: "prop:four-term-pair-nucleon",
  uses: [
    "prop:four-term-pair-nucleon",
    "rem:breit-wheeler-observation",
    "rem:photon-nucleon-hecke-action",
  ],
  tags: [
    "hopf-dressing", "pair-creation", "phi-01", "breit-wheeler",
    "testable", "monotone", "photon-polarisation",
  ],
});
