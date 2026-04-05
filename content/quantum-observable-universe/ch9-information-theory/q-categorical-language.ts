import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-categorical-language",
  lean: { decl: "QOU.MotivicIntegration.CategoricalLanguage", validation: "not_checked" },
  title: "First-order language of rigid monoidal categories",
  uses: [
    "def:quantum-universe",
  ],
  cites: ["denef2001"],
  tags: ["motivic-integration", "model-theory", "first-order-language"],
});
