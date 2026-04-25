import { example } from "../../schema/builders";

export default example({
  label: "ex:hadron-half-life-verification",
  title: "Half-life predictions for selected beta emitters",
  tags: [
    "half-life",
    "beta-decay",
    "verification",
    "numerical",
    "tritium",
    "cobalt-60",
    "carbon-14",
  ],
  lean: { ref: "qou:QOU.Descartes.HalfLifeVerification.all_six_agree",
    validation: "not_checked",
  },
  uses: ["rem:hadron-half-life-regimes"],
});
