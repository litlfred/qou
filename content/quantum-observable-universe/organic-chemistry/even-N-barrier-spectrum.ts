import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:even-N-barrier-spectrum",
  title:
    "Linear-in-$N$ trend of even-$N$ ring-closure barriers",
  tags: [
    "even-N",
    "ring-closure",
    "barrier",
    "linear-trend",
    "half-weight",
    "spectrum",
  ],
  lean: { ref: "qou:QOU.Organic.evenNBarrierSpectrum",
    validation: "not_checked",
  },
  uses: [
    "prop:ring-closure-barrier-quantitative",
    "prop:threading-half-weight",
  ],
  cites: [],
});
