import { table } from "../../schema/builders";
export default table({
  label: "tbl:lepton-tower-witness-table-data",
  title: "Data table from rem:lepton-tower-witness",
  uses: ["rem:lepton-tower-witness"],
  tags: ["extracted-table"],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Owner rulings: the photon is 1 + phi_0 sigma_0 + phi_1 sigma_1 + phi_01 sigma_0 sigma_1^{-1}, so the n = 0 row (the identity) is no longer called the photon, and the n = 1 row no longer says 'virtual' (no virtual photons). The electron is sigma_0 sigma_1 sigma_0, so the n = 3 trefoil row is the backup electron; the muon and tau words are not ruled." },
  ],
});
