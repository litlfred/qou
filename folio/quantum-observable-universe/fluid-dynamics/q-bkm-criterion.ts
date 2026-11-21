import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:q-bkm",
  lean: { ref: "qou:QOU.FluidDynamics.q_bkm_criterion", validation: "not_checked" },
  title: "$q$-deformed Beale--Kato--Majda criterion",
  uses: ["prop:q-ns-nonlinear-uniqueness"],
  tags: ["BKM", "blowup-criterion", "vorticity", "regularity"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): All three are one shared object, `QOU.Information.SkeinObservationSystem` (regularity is `Regular` / `regular_of_len_nonincreasing`, the abstract shadow of this criterion)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): **Shared substrate.** Boundedness of $\\int_0^T \\lVert \\omega_q \\rVert_{L^\\infty}\\,dt$ is the *regularity* leg of the shared length-filtration trichotomy on the Skein substrate $\\mathcal{S}(q)$ ([one length filtration, three problems](#rem:skein-filtration-trichotomy)): $q$-Navier--Stokes asks the crossing-number filtration $\\ell$ (the vortex-knot complexity) to stay **bounded** — no finite-time blow-up — the same $\\ell$ that $q$-Collatz asks to **descend** and $\\mathrm{P}$ vs $\\mathrm{NP}$ asks to be **polynomially** reachable. All three are one shared object, the Skein observation system, in which regularity follows from non-increase of the length filtration — the abstract shadow of this criterion." },
  ],
});
