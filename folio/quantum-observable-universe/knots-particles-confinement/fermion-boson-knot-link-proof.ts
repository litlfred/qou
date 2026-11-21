import { proof } from "../../schema/builders";

export default proof({
  label: "prf:fermion-boson-knot-link",
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): **Quarks in this framework.** Quarks are **not** knots or links in the $T(2,n)$ family. They are unknots Borromean-linked in the exceptional divisor ([Borromean quark](#conj:borromean-quark)). The Borromean link $\\mathcal{B}_3$ has **three** components. It is neither a knot (1) nor a standard link (2). Its statistics are determined by the overall baryon. The proton $\\mathcal{B}_3(u,u,d) \\oplus \\mathcal{L}_H$ is a composite fermion. When resolved via the Skein relation, its Borromean structure reduces to an odd number of knot components." },
  ],
  title: "Proof of fermion boson knot link",
  uses: ["prop:fermion-boson-knot-link"],
});
