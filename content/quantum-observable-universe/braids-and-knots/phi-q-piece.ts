import { definition } from "../../schema/builders";

export default definition({
  label: "def:phi-q-piece",
  title: "Φ$_q$-piece sub-link $K_S$ of a braid closure",
  lean: {
    ref: "qou:QOU.PhiQPiece.subLink",
    validation: "not_checked",
  },
  uses: [
    "thm:jones-markov-trace",
    "def:algebraic-quantum-volume",
  ],
  cites: ["kauffman1991"],
  tags: [
    "phi-q",
    "kashaev",
    "smoothing",
    "skein",
    "sub-link",
    "archimedean",
  ],
});
