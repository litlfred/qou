import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-observable-universe",
  label: "rem:brings-qou-axiom-map",
  title: "QOU axioms instantiated on Bring's surface",
  uses: [
    "prop:positive-definite-dagger",
    "rem:brings-qou-4tuple",
    "rem:lagrange-resolvents",
    "rem:archimedean-realisations",
    "lem:volume-from-rigidity",
  ],
});
