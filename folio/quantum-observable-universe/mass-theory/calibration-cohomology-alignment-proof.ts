import { proof } from "../../schema/builders";

export default proof({
  label: "prf:calibration-cohomology-alignment",
  title: "Proof of the calibration–cohomology alignment",
  uses: ["prop:calibration-cohomology-alignment", "prop:meson-scale-independence"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ([`QOU.Mass.calibrations_eq_cohomology`](#prop:calibration-cohomology-alignment))." },
  ],
});
