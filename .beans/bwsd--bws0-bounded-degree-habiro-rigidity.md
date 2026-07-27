---
# bwsd
title: 'bwS0-closure: bwS0 is bounded-degree (Habiro rigidity) (OPEN)'
status: todo
type: task
priority: high
created_at: 2026-07-27T00:30:00Z
updated_at: 2026-07-27T00:30:00Z
---

Parent: bws0. OPEN. The rigidity reduction needs bwS0 to be a bounded-degree polynomial in
t = q+q^-1 (so finite root agreement pins it). This is the Habiro / quantum-modularity rigidity:
the unified WRT invariant lives in the Habiro ring Ẑ[q] and its per-block value map is a Laurent
polynomial (the value map d_q = [mark]_q IS such a polynomial — proved, KeystoneMcKayValueMap; the
open piece is that the GAUGE row bwS0 shares this bounded-degree form). Route: cite habiro2008
(added to references.ts) for the WRT=Habiro-element structure, and/or prove the degree bound from
the Reshetikhin-Turaev construction. Carried as an explicit hypothesis in
`KeystoneGaugeRowRigidity.bwS0_eq_hecke_of_rigidity`; discharging it removes that hypothesis.
