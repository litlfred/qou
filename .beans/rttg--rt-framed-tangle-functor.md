---
# rttg
title: 'RT-2: framed-tangle category + Reshetikhin-Turaev ribbon functor'
status: todo
type: task
priority: normal
created_at: 2026-08-02T09:20:00Z
updated_at: 2026-08-02T09:20:00Z
---

Parent: rtep. TIER: LARGE (major Mathlib project, multi-month; not session-scale). The RT functor
F : Rib(𝒞) → 𝒞 from the category of framed oriented tangles/ribbon graphs colored by 𝒞 to 𝒞.
Needs: (a) the category of framed tangles (Turaev's Rib) — NOT in Mathlib; must be built (generators
= cup/cap/braid/twist, relations); (b) the monoidal functor from ribbon structure; (c) the resulting
link invariant (colored Jones as F of a closed braid). This is the honest bulk of "the ribbon
functor." Realistic: incremental — start with the tangle category presentation. Flag to owner: this
is an open Lean-formalization research target, not a session deliverable.
