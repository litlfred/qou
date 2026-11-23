import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:borromean-two-photon-factorisation",
  title: "The Borromean braid is a product of two commuting photons in $H_3(q)$",
  lean: {
    ref: "qou:QOU.Mass.BorromeanPhotonFactorisation.borromean_eq_photon_product",
  },
  uses: ["def:photon", "prop:borromean-markov-trace-closed-form"],
  cites: ["iwahori1964", "kassel2008"],
  tags: ["borromean", "hecke-algebra", "photon", "gamma-gamma", "nucleon-element"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean statement holds in every algebra that satisfies the relations," },
  ],
});
