import { proof } from "../../schema/builders";

export default proof({
  label: "prf:ns-singularity-descartes",
  title: "Proof of ns singularity descartes",
  uses: ["thm:ns-singularity-descartes"],
  authorNotes: [
    { kind: "note", date: "2026-11-24", body: "Relocated from the block prose by the voice-leak / commentary drain (qou-d4kh): Earlier versions of this theorem asserted that the Descartes universe is NS-singular, $\\mathrm{NS}(A) = e(\\xi)|_\\Sigma \\neq 0$, via (1) Kummer survival of $\\kappa_0 \\bmod 2\\kappa$, (2) complementary-subgroup non-cancellation with $\\delta_n|_\\Sigma$, (3) [core-Levi equivalence](#prop:core-levi-form), and (4) the [vorticity lower bound](#conj:vorticity-lower-bound) and [BKM divergence](#thm:q-bkm)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The arithmetic is checked in Lean as `QOU.FluidDynamics.descartes_kummer_root_levels`. The full analysis is in the audit `docs/audits/2026-10-12-ns-chain-after-item3-retraction.md`." },
  ],
});
