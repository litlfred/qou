import { definition } from "../../schema/builders";

export default definition({
  label: "def:phi-q-piece",
  title: "Φ$_q$-piece sub-link $K_S$ of a braid closure",
  lean: {
    ref: "qou:QOU.PhiQPiece.subLink",
    validation: "not_checked",
  },
  uses: ["def:quantum-bloch-group"],
  cites: ["kauffman1991", "faddeev1994"],
  tags: [
    "phi-q",
    "kashaev",
    "smoothing",
    "skein",
    "sub-link",
    "archimedean",
  ],
});
