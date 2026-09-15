import { example } from "../../schema/builders";

export default example({
  interprets: "def:quantum-characteristic-classes",
  label: "ex:quantum-characteristic-classes-su2",
  title: "Quantum characteristic classes for $\\mathrm{SU}(2)$",
  tags: ["su2", "obstruction", "cohomology", "chern-class"],
  uses: ["def:quantum-characteristic-classes", "ex:recursive-brane-tower-su2"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-15",
      body:
        "**Scope: this block's `tr(id_A) = chi(CP^1) = 2` and `lem:brings-euler-characteristic`'s `-6` are the SAME bridge applied to DIFFERENT `S`.** Both invoke `prop:euler-char-stability` (`tr(id_{A_n}) = chi_top(S_n)`); this one takes `S = SU(2)/U(1) = CP^1` (genus 0), that one takes the generic fibre to be Bring's `Sigma_4` (genus 4). At most one of the two describes the state bundle of the Descartes universe, and the corpus does not yet say which. Register entry in `notation/notation-collisions.md`; bean `qou-2uf0`.",
    },
  ],
});
