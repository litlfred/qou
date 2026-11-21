import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:torus-knot-shell-binding",
  label: "rem:torus-knot-shell-binding-interpretation",
  title: "Torus-knot mediation of inter-shell crossings",
  uses: ["prop:torus-knot-shell-binding", "prop:shell-closure-normal-form"],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Owner ruling 2026-11-21 (docs/coordination/owner-rulings.md): the nuclear Regime-I shell-size rule T(2,n_s) is withdrawn; its basis was a mislabel ((sigma_0 sigma_1)^2 sigma_0 closes to T(2,4), not T(2,5)). The block is withdrawn in place, not deleted, because observations/double-magic-delta-i-bound and hopf-link-non-magic cite it. Sidecar retriage 2026-11-21 also found the Lean sibling is rfl/decide over a hard-coded table." },
  ],
});
