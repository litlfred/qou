import { proof } from "../../schema/builders";

export default proof({
  label: "proof:jackson-q-bessel-contiguity",
  of: "rem:brings-q-hyperbolic-geometry",
  lean: {
    ref: "qou:QOU.QBeta.qbessel_first_kind_coeff_closed_form",
    validation: "not_checked",
  }
});
