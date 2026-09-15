import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:brings-euler-characteristic",
  lean: { ref: "qou:QOU.ArchimedeanUniverse.brings_euler_characteristic",
    validation: "not_checked",
  },
  title: "Categorical Euler characteristic of $\\mathcal{O}_q(\\mathrm{SU}(2))$ on Bring's surface",
  tags: ["euler-characteristic", "brings-surface", "categorical-trace", "descartes-substrate"],
  uses: ["prop:euler-char-stability"],
  proofs: ["prf:brings-euler-characteristic"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-15",
      body:
        "**Scope: which `tr(id_A)` this is.** Three live sites read `tr(id_A)` three ways and two corpus claims about it conflict; the register entry in `notation/notation-collisions.md` separates them. This block applies the `prop:euler-char-stability` bridge with the generic fibre of `S` taken to be Bring's `Sigma_4`, giving -6. `ex:quantum-characteristic-classes-su2` applies the SAME bridge with `S = SU(2)/U(1) = CP^1` and gets 2, so the two disagree about the fibre (genus 4 against genus 0) and at most one describes the Descartes universe's state bundle. Separately, this block's own proof recovers -6 as *\"the quantum dimension specialised at the Descartes substrate parameter q_0\"*, while `rem:substrate-line-bundle-base-not-fibre` states that `chi(A) = tr(id_A)` is *strictly independent of q* -- a quantity independent of q does not need specialising at q_0. Not resolved here. Bean `qou-2uf0`.",
    },
  ],
});
