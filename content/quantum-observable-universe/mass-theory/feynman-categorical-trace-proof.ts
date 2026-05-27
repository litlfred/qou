import { proof } from "../../schema/builders";

export default proof({
  label: "prf:feynman-categorical-trace",
  lean: { ref: "qou:QOU.FeynmanPathIntegrals.mass_eq_abs_amplitude",
    validation: "not_checked",
  },
  title: "Proof of Feynman transition amplitude as categorical trace",
  uses: [
    "prop:feynman-categorical-trace",
    "lem:feynman-trace-collapse",
    "lem:feynman-markov-identification",
  ],
});
