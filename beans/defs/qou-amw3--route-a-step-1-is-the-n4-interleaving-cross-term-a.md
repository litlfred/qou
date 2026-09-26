---
# qou-amw3
title: 'Route A step 1: is the n=4 interleaving cross term an Euler characteristic — HOMFLY-PT / Soergel-bimodule Hochschild homology of the two words'
status: completed
type: task
priority: normal
created_at: 2026-09-06T03:31:24Z
updated_at: 2026-09-06T04:13:26Z
parent: qou-2akx
---

## 2026-09-06 — MEASURED (step 1 done; step 2 is the honest gap)

Lean QOU/MathlibExt/InterleavedWordClosures.lean (sorry-free, lean-direct exit 0, axioms standard): from the Ocneanu axioms alone, tr(s0 s1 s0 s2 s1) = z²·tr(σ³) and tr(s0² s1² s2) = z·tr(σ²)², so Δ = z²·tr(σ³) − z·tr(σ²)² (crossTerm_eq_closures). The interleaved word is a doubly-stabilised σ³ — closure the TREFOIL; the sequential word is a stabilised Hopf-chain — three components. Identities hold with z, h FREE (two-variable HOMFLY-PT level), confirmed in the 16-dim rep (probe interleaving_cross_term_closures_probe.py, 13/13).

VERDICT on "is Δ an Euler characteristic": TRUE only in the content-free sense (each side is χ of a Khovanov–Rozansky homology, of two DIFFERENT links, so Δ = χ of a shifted direct sum). The interesting sense — a natural chain map HHH(chain) → HHH(trefoil) whose cone carries Δ — is NOT supplied by anything in the corpus: the closures have different component counts and no braid move relates the words. Step 2 = construct such a map (a cobordism map: two saddles join the three components into one) and compute its cone; this is genuine new work, bean-level, not attempted here.

2026-09-06: step 2 done in qou-s82c — canonical virtual Soergel object; see doc §7f.
