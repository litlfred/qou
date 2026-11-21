import { proof } from "../../schema/builders";

export default proof({
  label: "prf:c-equals-bar-iff-all-1dim",
  title: "Proof of c equals bar iff all 1dim",
  uses: ["prop:c-equals-bar-iff-all-1dim"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-21",
      body: "Under the owner ruling of 2026-11-21 the electron is $\\sigma_0\\sigma_1\\sigma_0 \\in H_3(q)$, not an element of $H_2(q)$, so the \"leptons\" label on the $H_2$ row was removed. The proof is unaffected (it is a statement about $H_n(q)$). Three sentences after the Corollary still read the $H_2$ level as the lepton sector: \"The lepton sector is algebraically distinguished ...\", item 1 (Leptonic simplicity) and item 2 (\"inaccessible from the bar-symmetric lepton sector\"). They are left for an owner decision; see `docs/audits/2026-11-21-electron-word-options-downstream.md` §3 item 2.",
    },
  ],
});
