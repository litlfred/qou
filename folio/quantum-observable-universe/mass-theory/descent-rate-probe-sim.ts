import { simulator } from "../../schema/builders";

// Stub simulator block: empirical probe of descent-rate β(d) on
// SYT-cell pairs. Used by mass-tower-syt-cells.md to point at the
// numerical evidence that β(d) = 1 uniformly across distances.
// HTML implementation deferred — wire to a future probe page or
// existing witness JSON.
export default simulator({
  label: "sim:descent-rate-probe",
  title: "Empirical descent-rate probe (SYT-cell pairs)",
  html: "fsh-guts/deprecated/simulators/descent_rate_probe.html",
  uses: ["rem:mass-tower-syt-cells"],
  tags: ["syt", "descent-rate", "empirical", "todo-html", "interactive"],
  defaultView: {
    name: "default",
    title: "β(d) across distances",
    params: { atom: "proton", n_max: 12 },
  },
});
