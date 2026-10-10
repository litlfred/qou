---
# bwsd
title: 'bwS0-closure: bwS0 is bounded-degree (Habiro rigidity) (OPEN)'
status: completed
type: task
priority: high
created_at: 2026-07-27T00:30:00Z
updated_at: 2026-09-03T04:45:09Z
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


---

## Title and parent listing are stale (noted 2026-09-03)

This bean is `completed` — dissolved 2026-08-01 by `KeystoneHabiroInfiniteRigidity.eq_of_habiro_root_agreement`. Two places still read as though it were open:

1. **This bean's own title** still ends "(OPEN)".
2. **Parent `bws0`'s decomposition** still lists *"bwS0 bounded-degree (Habiro rigidity) — OPEN (bwsd)"*. Its residual is `bwsc` + `bwse` only, which the body of this bean already says.

### And the dissolution had never been wired to anything (fixed, PR #6459)

Measured on `origin/main`: `eq_of_habiro_root_agreement` has **no consumers anywhere in the corpus**. Meanwhile the concrete `n = 5` theorems (`muon_block_pinned_level7`, `electron_block_pinned_level7`) still carry `hbw : bwPoly.natDegree < 6` — the very hypothesis the dissolution removes. So the degree obligation was dissolved in the abstract and left standing on every concrete block.

`muon_block_pinned_all_roots` / `electron_block_pinned_all_roots` are that wiring: the physical muon and electron blocks pinned with **no degree hypothesis at all**.

Worth recording that the two forms are a **trade, not a strict improvement**, and neither dominates: the level-6 form asks for agreement at five roots of one level; the all-roots form asks for one root of every level and pays no degree. Which is cheaper depends on what WRT actually supplies — that is `bwsc`, and it is open.
