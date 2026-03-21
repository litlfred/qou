import { remark } from "../../schema/builders";

export default remark({
  label: "rem:brings-qou-axiom-map",
  title: "QOU axioms instantiated on Bring's surface",
  uses: [
    "def:quantum-observable-universe",
    "def:positive-definite-dagger",
    "rem:brings-qou-4tuple",
    "rem:lagrange-resolvents",
    "rem:archimedean-realisations",
    "lem:volume-from-rigidity",
  ],
});
