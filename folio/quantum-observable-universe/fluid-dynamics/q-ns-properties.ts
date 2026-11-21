import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-navier-stokes",
  label: "rem:q-ns-properties",
  title: "Properties of the $q$-Navier--Stokes system",
  uses: ["def:q-navier-stokes", "thm:q-ns-wellposedness"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The exponential decay of high-wavenumber modes globally bounds the 3D $q$-Navier--Stokes equation for any $q > 1$ ([thm:q-ns-wellposedness](#thm:q-ns-wellposedness))." },
  ],
});
