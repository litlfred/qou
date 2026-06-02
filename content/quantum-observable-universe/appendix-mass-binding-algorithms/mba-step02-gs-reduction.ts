import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:gs-reduce-to-hecke-nf",
  title: "Gröbner–Shirshov reduction to Hecke normal form",
  uses: [
    "def:hecke-normal-form",
    "def:categorical-action",
  ],
  computation: {
    engine: "python",
    script: "tools/hecke-engine/src/gs_reduce.rs",
    witness: "folio-assistant/computations/hecke-core-symbolic-migration.witness.json",
    status: "verified",
  },
  tags: [
    "mba",
    "step-2",
    "gs-reducer",
    "hecke-normal-form",
    "stokes",
    "canonical-chain",
  ],
});
