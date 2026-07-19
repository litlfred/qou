---
# qou-g6vb
title: 'F4 research: prove trM_cyclic on H4 via bilinearity ⇒ 24² basis identities'
status: in-progress
type: task
priority: normal
created_at: 2026-07-19T01:52:06Z
updated_at: 2026-07-19T02:17:07Z
---


## Finding (2026-07-19)
The bilinearity reduction (isolate 24 per-word functionals trM(W_j u), then
Gram symmetry A_{j,i}=A_{i,j}) is mathematically correct but does NOT rescue
the Lean proof: a SINGLE depth-6 word already whnf-explodes. 6 tactic
strategies infeasible (brute simp; per-word simp; per-word rfl; incremental
have-chain rfl; incremental fin_cases; 200k–4M heartbeats). Root cause:
top-down Matrix.cons indexing re-derives inner-word entries per outer index
(exponential, non-memoized). Single-layer rfl works (opaque u); depth-2+ fails.
Tractable path: Matrix.Reflection re-encode (needs Matrix.Notation olean,
absent from sandbox cache) OR abstract regular-rep trace tr(AB)=tr(BA).
Audit: docs/audits/2026-07-19-h4-cyclicity-whnf-explosion.md. Sorry kept honest.
