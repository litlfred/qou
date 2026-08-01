---
# qou-su6h
title: Scaffold Jucys-Murphy
status: todo
type: task
created_at: 2026-07-08T14:00:13Z
updated_at: 2026-07-08T14:00:13Z
---


## Scoping note 2026-08-01 — blocked on missing Mathlib infra (NOT a session task)

Piece B = `(1/n!) Σ_{λ⊢n} dim(λ)² Σ_c content(c)² = C(n,2)` (the JM content-square
mean, the `n(n-1)` half of Identity I). Unlike Piece A (now proven sorry-free,
`QOU.BraidKnot.PieceA.pieceA` — pure Young-diagram combinatorics), Piece B is
intrinsically a **sum over all partitions weighted by dim²**, which needs one of:
Jucys–Murphy elements in `ℂ[S_n]` + the regular-character coefficient formula, OR
RSK + `Σ_λ (f^λ)² = n!`. **Mathlib provides NONE of these** (grep 2026-08-01:
no RSK, no Jucys–Murphy, no Specht modules, no hook-length formula, no S_n
character theory — only `YoungDiagram` + `SemistandardTableau`). So a clean
sorry-free general proof is a **major multi-week Mathlib contribution**, not a
session task. The math itself is settled (JM argument, brute-verified n=2..6 in
the corpus; and Identity I is decide-verified n≤8 in `WLambdaDefectClosedForm`).
Honest status: OPEN, blocked on infra; do NOT axiomatize JM and pass it off as a
proof (anti-laundering). A conditional reduction "Piece A + (Σf^λ²=n!) ⟹ Piece B"
is possible but still rests on the RSK gap.
