import { proof } from "../../schema/builders";

export default proof({
  label: "prf:hydrogen-capacity",
  title: "Hydrogen capacity verified across IUPAC organic taxonomy",
  tags: [
    "hydrogen-capacity",
    "verification",
    "computation",
    "iupac",
  ],
  uses: ["prop:hydrogen-capacity"],
  computation: {
    engine: "python",
    script: "computations/hydrogen_capacity.py",
    witness: "computations/hydrogen-capacity.witness.json",
    status: "verified",
  },
});
