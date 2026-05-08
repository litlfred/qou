import { proof } from "../../schema/builders";

export default proof({
  label: "prf:fiber-adjoint-involution",
  title: "Proof of Fiber--adjoint-fiber involution",
  uses: [
    "prop:fiber-adjoint-involution",
    "lem:fai-projector-coadjoint-orbit",
  ],
});
