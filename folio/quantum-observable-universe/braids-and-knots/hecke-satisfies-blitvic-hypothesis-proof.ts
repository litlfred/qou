import { proof } from "../../schema/builders";

export default proof({
  label: "prf:hecke-satisfies-blitvic-hypothesis",
  title: "Proof: the third centred moment of a Hecke generator",
  uses: [
    "prop:hecke-satisfies-blitvic-hypothesis",
  ],
});
