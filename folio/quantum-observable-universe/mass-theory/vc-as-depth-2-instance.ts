import { remark } from "../../schema/builders";

export default remark({
  label: "rem:vc-as-depth-2-instance",
  title:
    "Volume Conjecture as the depth-2 instance of GS $\\leftrightarrow$ period correspondence",
  interprets: "conj:kashaev-volume-conjecture",
  uses: ["conj:gb-depth-period-correspondence"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([The algebraic core of QOU lifts to any real-closed field](#rem:algebraic-core-survives))" },
  ],
  cites: [
    "kashaev1997",
    "murakami-murakami2001",
    "bloch2000",
    "zagier1986",
  ],
  tags: [
    "volume-conjecture",
    "depth-2",
    "bloch-wigner",
    "regulator",
    "graded-mikusinski",
    "interpretation",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/hyperbolic_volumes.py",
    witness: "computations/hyperbolic-volumes.witness.json",
    status: "verified",
  },
});
