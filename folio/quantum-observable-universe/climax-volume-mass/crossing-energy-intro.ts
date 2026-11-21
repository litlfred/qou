import { prose } from "../../schema/builders";

export default prose({ label: "sec:crossing-energy-intro",
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): Because the Hecke generator $T = P \\circ R$ has eigenvalues $(q, -q^{-1})$, the ratio of the per-crossing Coulomb shift $q - q^{-1}$ to the strong baseline $q + q^{-1}$ is the rational function $\\tanh(\\ln q) = (q^2-1)/(q^2+1)$ ([Proposition](#prop:coulomb-strong-ratio-q-rational)), and the skein difference $L_+ - L_- = (q - q^{-1})L_0$ is bar-antisymmetric under $q \\mapsto q^{-1}$ ([Proposition](#prop:skein-bar-antisymmetry))." },
  ],
});
