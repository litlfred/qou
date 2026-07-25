---
# qou-4hq0
title: 'A1 (deep bet): exact/semi-exact evaluation of T3=Sum(f)^2 chi(3-cyc) via content-sum formulas'
status: todo
type: task
priority: normal
created_at: 2026-07-25T03:30:08Z
updated_at: 2026-07-25T03:31:40Z
parent: qou-v8t7
---

## A1 — deep bet: exact/semi-exact evaluation of T₃ = Σ_λ (f^λ)² χ^λ(3-cyc)
IDEA. If T₃ (or cov(k)) has a closed form manifestly ≤0, everything closes. χ^λ(3-cyc)=content
polynomial (JM), so T₃=Σ_λ(f^λ)²·[content poly of λ]. Shifted-symmetric / content-sum evaluation
machinery (Okounkov-Olshanski shifted Jack; Stanley content formula) sometimes closes such sums.
CAVEAT. Already known: |T₃|,|cov| OEIS-absent AND non-P-recursive (no linear recurrence, k≤28), so a
SIMPLE closed form is unlikely — but a shifted-symmetric / signed-sum form may still exist.
FIRST STEP. Read uploads/9608020v2.pdf (Okounkov-Olshanski, shifted Jack + binomial formula) and
Stanley content-evaluation; look for Σ_λ (f^λ)^a p_μ(contents) formulas; test candidates against the
exact sequence T₃(k)= −2,−2,−16,−260,−2336,−28792,… (k=3..).
SUCCESS. Closed form manifestly ≤0.
KILL. Provably no shifted-symmetric closed form. Lower-probability but highest-payoff.
