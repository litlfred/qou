---
# bwsd
title: 'bwS0-closure: bwS0 is bounded-degree (Habiro rigidity) (OPEN)'
status: completed
type: task
priority: high
created_at: 2026-07-27T00:30:00Z
updated_at: 2026-08-01T23:55:00Z
---

2026-08-01 (PR #4402): DISSOLVED. The bounded-degree hypothesis is no longer needed —
`KeystoneHabiroInfiniteRigidity.eq_of_habiro_root_agreement` uses the INFINITE fibre-root
family, so agreement at all roots forces equality with NO degree bound (a nonzero polynomial
has finitely many roots). The finite/degree-bounded form (KeystoneHabiroRootFamily,
KeystoneN5ValueMapRigidity) remains as the concrete n=5 instance, but the general closure no
longer requires proving bwS0 bounded-degree. Residual of bws0 collapses to bwsc (agreement) +
bwse (WRT=BW-localization citation).

Parent: bws0. OPEN. The rigidity reduction needs bwS0 to be a bounded-degree polynomial in
t = q+q^-1 (so finite root agreement pins it). This is the Habiro / quantum-modularity rigidity:
the unified WRT invariant lives in the Habiro ring Ẑ[q] and its per-block value map is a Laurent
polynomial (the value map d_q = [mark]_q IS such a polynomial — proved, KeystoneMcKayValueMap; the
open piece is that the GAUGE row bwS0 shares this bounded-degree form). Route: cite habiro2008
(added to references.ts) for the WRT=Habiro-element structure, and/or prove the degree bound from
the Reshetikhin-Turaev construction. Carried as an explicit hypothesis in
`KeystoneGaugeRowRigidity.bwS0_eq_hecke_of_rigidity`; discharging it removes that hypothesis.
