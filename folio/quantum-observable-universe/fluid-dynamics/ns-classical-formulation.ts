import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:ns-obstruction",
  label: "rem:ns-classical-formulation",
  title: "The classical regularity question for the Navier--Stokes equation",
  uses: ["def:ns-obstruction"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): An anchor of $\\chi(A) = 0$ ([torus example](#ex:torus-ns-regular)) forces global regularity. An anchor of $\\chi_{\\mathrm{eu}}(M_0) = -6$ ([Descartes universe](#thm:ns-singularity-descartes)) forces finite-time singularities." },
  ],
  tags: ["navier-stokes", "regularity", "classical", "formulation"],
});
