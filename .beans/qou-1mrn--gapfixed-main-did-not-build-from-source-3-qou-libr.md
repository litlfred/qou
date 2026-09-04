---
# qou-1mrn
title: 'GAP/FIXED: main did not build from source — 3 QOU library modules (JHopf, JetHorizon, Summary)'
status: completed
type: task
priority: normal
created_at: 2026-08-29T11:02:05Z
updated_at: 2026-08-29T17:23:57Z
---

Surfaced by the qou-snh8 lake-cache reseed (full from-source lake build QOU). CI is billing-disabled and standalone library .lean files have no QA sidecar, so nothing caught these. THREE modules broke main's from-source build; all fixed + verified lean-direct (exit 0, sorry-free) + pushed on claude/lean-qa-backlog-2h3f8d (PR #5985):
1. QOU.BraidKnot.JHopfQOneProvenance (27f0308e21) — dead rw [Real.sqrt_one] after markovZ/heckeH went sqrt-free (convention-D migration casualty); norm_num.
2. QOU.JetHorizon (27f0308e21) — opaque aeon_recycling needs Nonempty PlanckStepResult (unwitnessable); revert fa0aa1c5c8's over-eager axiom->opaque to axiom (Penrose CCC conjecture).
3. QOU.Mathlib.Summary (3d89d983e4) — inventory_check asserted Nonempty (IwahoriHeckeAlgebra R 2 q) via inferInstance, but that instance was deliberately purged 2026-08-23 (anti-laundering); de-vacuify 3e4934338d made it unprovable. §3b-cond fix: add [IwahoriHeckeAlgebra R 2 q] binder (NOT re-add the purged instance).
SYSTEMIC: with CI down, the from-source lake build is the ONLY gate for un-sidecar'd library files, and it is not being run pre-merge. Consider a periodic manual from-source build gate. The reseed (qou-snh8) is the vehicle that found these and completes once the tree builds clean.
