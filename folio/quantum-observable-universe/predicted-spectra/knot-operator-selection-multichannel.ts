import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:knot-operator-selection",
  label: "rem:knot-operator-selection-multichannel",
  title: "Multi-channel interpretation of knot operator selection",
  uses: ["prop:knot-operator-selection"],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Electron ruling (owner, 2026-11-21): the T_{2,3} channel is no longer labelled 'electron'. The electron is sigma_0 sigma_1 sigma_0 (Hopf closure) and its pair channel is the sigma_0 sigma_1 sigma_0 coefficient of NF(gamma gamma). The muon word is not ruled, so the T_{2,5} channel is not called a muon pair. The operator T_{2,3} -> sigma_0^3 used by the LP selection producer is unchanged." },
  ],
});
