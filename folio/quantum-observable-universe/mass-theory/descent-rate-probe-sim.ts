import { simulator } from "../../schema/builders";

export default simulator({
  label: "sim:descent-rate-probe",
  title: "Empirical descent-rate probe (SYT-cell pairs)",
  html: "simulators/descent_rate_probe.html",
  uses: ["rem:mass-tower-syt-cells"],
  tags: ["syt", "descent-rate", "empirical", "interactive"],
  defaultView: {
    name: "default",
    title: "β(d) across distances",
    params: { atom: "proton", n_max: 12 },
  },
});
