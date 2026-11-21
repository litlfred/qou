import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:hyperbolic-volume-transcendence",
  title: "Algebraic independence of QOU hyperbolic volumes",
  tags: [
    "tier:famous",
    "hyperbolic-volume",
    "transcendence",
    "algebraic-independence",
    "bloch-wigner",
    "open-problem",
  ],
  uses: [],
  lean: { ref: "qou:QOU.Archimedean.HyperbolicVolumeIndependence",
    validation: "not_checked",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean\nformalisation proves the structural half: the tower\ndecomposition, Chern--Simons faithfulness, and the downstream\nimplications (algebraic independence $\\Rightarrow$ Borel--Zagier\n$\\Rightarrow$ irrationality). The transcendence core is\naxiomatised as the Lean class `HyperbolicVolumeIndependence`. Following\nthe conditional-class convention, the downstream results remain conditionally rigorous." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): These include [single-volume irrationality](#conj:single-volume-irrationality)\n(no hyperbolic 3-manifold volume is known to be irrational), [Borel--Zagier](#conj:borel-zagier-qou-volumes), and the Kontsevich--Zagier and Grothendieck period conjectures." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The framework approaches the conjecture via two complementary, partial reductions. The deeper statement remains open. The sharper reduction is the\n[jet-order reduction](#conj:three-knot-jet-order-independence). It\nreplaces Grothendieck-period machinery with a finite\nper-order Gröbner--Shirshov independence computation. The skein engine\nexecutes this computation natively. This pairs with a single QOU-native surreal bridge lemma. This reduction converts an external problem into an incremental\nresearch target natively structured on the framework's jet-order filtration. The second reduction is the [transcendence shadow](#rem:yekutieli-transcendence-shadow). It\nreduces algebraic independence to the non-collapse of the brane tower\nand Nesterenko-type arithmetic control of the quantum dilogarithm.\nBoth paths relocate the difficulty. The structural half is\nproved: the tower\ndecomposition, Chern--Simons faithfulness, and the downstream\nimplications (algebraic independence $\\Rightarrow$ Borel--Zagier\n$\\Rightarrow$ irrationality). The transcendence core is\ntaken as an explicit hypothesis, and the downstream results are rigorous conditional on it." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): As the [formal-chain\nremark](#rem:formal-chain-transcendence) records," },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The framework operates strictly on the proved numerical\n[distinctness](#prf:knot-volumes-verification) of the three volumes. This distinctness suffices for all mass predictions." },
  ],
});
