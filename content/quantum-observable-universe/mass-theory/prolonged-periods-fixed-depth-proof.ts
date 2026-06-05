import { proof } from "../../schema/builders";

export default proof({
  label: "prf:prolonged-periods-fixed-depth",
  title: "Proof that a fixed-depth recurrence for the prolonged periods exists",
  uses: [
    "prop:prolonged-periods-fixed-depth",
  ],
});
