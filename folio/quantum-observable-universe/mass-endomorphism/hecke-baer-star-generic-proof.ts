import { proof } from "../../schema/builders";

export default proof({
  label: "prf:hecke-baer-star-generic",
  title: "Proof of hecke baer star generic",
  uses: ["prop:hecke-baer-star-generic"],
  authorNotes: [
    { kind: "note", date: "2026-11-24", body: "Relocated from the block prose by the reading-order drain (qou-d4kh): [Frobenius Gram matrix and dual construction in $H_3(q)$](#prop:frobenius-gram-matrix)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Canonical q-deformed Wedderburn-block weight $\\tilde w_\\lambda$ and named scalings (BW, LP for all $\\lambda$)](#prop:wedderburn-weight-canonical), [Hoefsmit seminormal matrices as $R$-matrix evaluations in $H_n(q)$](#prop:hoefsmit-seminormal-form))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): (Hoefsmit seminormal form [Hoefsmit seminormal matrices as $R$-matrix evaluations in $H_n(q)$](#prop:hoefsmit-seminormal-form))" },
  ],
});
