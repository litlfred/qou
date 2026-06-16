import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:gs-reduce-to-hecke-nf",
  title: "Gröbner–Shirshov reduction to Hecke normal form",
  uses: [
    "def:hecke-normal-form",
    "def:categorical-action",
  ],
  computation: {
    engine: "rust",
    script: "tools/hecke-engine/src/gb_nf_reducer.rs",
    witness: "computations/hecke-core-symbolic-migration.witness.json",
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
