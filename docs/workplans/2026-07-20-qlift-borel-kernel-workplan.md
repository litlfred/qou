# q-lift of the normalized binding kernel + prolongation-symbol identification — workplan

**Branch:** `claude/qlift-borel-kernel-derivation-2026-07-20`
**Basis (merged):** raw-OGF kernel excluded + classical fibre proved
(`QOU.Mass.QDifferenceConfluentObstruction.normalized_classical_kernel_exists`,
`(n+2)·b_{n+2} = b_{n+1} + b_n`, depth 2 exact); audit
`2026-07-20-qdifference-kernel-confluent-narrowing.md`.

## Open targets (in order)

1. **Literature check** (owner ask): q-Borel / q-Laplace kernels for
   q-difference equations of Gevrey-type series (Ramis–Zhang q-summability;
   Ohtsuki-series q-holonomy; GGM descendant q-difference eq 49) — what is
   known about depth-2 q-liftings of `f' = (1+x)f`-type confluent shadows.
   Tools: paper-search MCP (arXiv/Crossref), corpus references.ts.
2. **The q-lift**: state and test the candidate `[n+2]_q·b_{n+2} =
   b_{n+1} + c(q)·b_n` on the q-Borel transform of the q-deformed binding
   terms (Habiro/GGM side supplies the q-data); probe first at low rungs,
   formalize-first the bar-symmetry/parity constraints on `c(q)` before any
   scan.
3. **Identification**: derive the kernel from the prolonged SW connection's
   local monodromy at a branch point (`z = z_c + t²` chart per
   `prop:sw-classical-jet-exactness`), comparing against the SL₂ Stokes
   matrix route (GGM `[[1,0],[−3,1]]`) — the honest home of the reverted
   #4129 τ-instinct.
4. **Appendix sync** (owner ask): mirror the keystone status + any new
   result into `appendix-mass-binding-algorithms` per the STRICT sync rule,
   and keep `docs/canonical-derivation-cheat-sheet.md` current.

Discipline: anti-fit (no AME anchors as inputs); scope-(a)/(b) vocabulary;
conjecture stays a conjecture until an actual derivation lands.
