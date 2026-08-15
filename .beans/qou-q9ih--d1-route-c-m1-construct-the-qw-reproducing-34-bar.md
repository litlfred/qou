---
# qou-q9ih
title: 'D1: Route C M1 — construct the (Q,W) reproducing {3,4} + bar split (7,1); fitted quiver = candidate only (parent qou-rtec)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T02:49:30Z
updated_at: 2026-08-15T10:56:28Z
---


## 2026-08-15 first rung — implementation class pruned (Lean-proved)

`QOU/QBeta/QuiverMirrorAutomorphismExcluded.lean` (sorry-free, axioms
[propext, Quot.sound]): any COUNT-INVARIANT mirror implementation — a
quiver automorphism, the op-duality Q ↦ Q^op, or any DT-preserving
equivalence — forces every readable pair amphichiral, so the (4,3)
datum is unreachable (`count_invariant_excludes_five_two`), and
conversely reading (4,3) forces Ω(σd) ≠ Ω(d)
(`five_two_forces_count_breaking`).

CONSEQUENCE for the search: the M1 object is (quiver, potential, TWO
stability rays) with the mirror acting on the RAY, never (quiver +
automorphism). Consistent with M2's distinct-Borel-rays finding
(RouteCM3CategoryIdentification). Extends Driver14's no-scalar theorem
one level up (no count-preserving symmetry implementation either).

REMAINING (the big rung, still open): actually construct a (Q,W) + ray
pair whose DT counts are (4,3) with bar split (7,1), FROM Hecke/Bring
data. A fitted quiver stays a labeled CANDIDATE only (anti-laundering).


## Attack-options ledger — construction rung (2026-08-15, dispatched-agent research)

Target object (post-pruning): **(Q, W, ray+, ray-)** — quiver with potential
plus TWO stability rays, ray-wise DT counts (4,3), bar split (7,1).
Constraints Lean-proved: no count-preserving mirror implementation
(QuiverMirrorAutomorphismExcluded); abelian spectrum at distinct Borel rays
(AomegaM2BPSCohomology / RouteCM3); datum is set-valued (Driver14 no-scalar).
Standing negative respected: driver-14 NOT constructible from scalar drivers.
Any quiver whose only credential is matching the datum = labeled CANDIDATE.

### D1-a — KS/Reineke small-quiver two-ray DT scan (CANDIDATE generator)
Enumerate <=3-4-vertex quivers, DT counts on ray pairs, filter (4,3)+(7,1).
Session-scale. Either outcome is progress: no hit -> bounded negative
(">= N vertices required"); many hits -> datum underdetermines (Q,W),
sharpening why only derivation counts. Expect many hits (2-integer target is
weak — the #4534 two-knot-linear-fit guard); say so in the docstring.
No dependencies; parallel-safe.

### D1-b — Jacobi algebra from certified character-variety / spectral data
Nodes per connection (3 / 4 incl. abelian, certified in
dt_crossknot_connection_count_certified_probe.py), arrows/potential from the
NZ-gluing datum (DGG closed-sector). Multi-session; the NZ->(Q,W) dictionary
must be assembled from KS/DGG lit. CANDIDATE-plus tier: certified GEOMETRIC
imports (allowed — the audit says the missing input IS geometric), not
Hecke-derived. Do NOT resurrect the refuted KRSS open-sector route (det(K)=5).

### D1-c — Hecke/Bring-side extraction (the derivation-tier target = M3)
Vertices from Wedderburn blocks of H3(q) (both knots are 3-braids), bar-graded
per DTChiralityBarInvolutionLink; rays from the bar involution on stability.
First step is a cheap disconfirmable shape test: does ANY natural pairing on
the 5_2 braid blocks give a 2-ray abelian spectrum summing to 7?
Research-programme; heavy prior against (driver-14 negative), but a quiver is
not a scalar so not formally excluded. Only route whose success = derivation.
Open-outcome — sibling overlap encouraged with distinct angle.

### D1-d — Exponential-network import (literature frontier)
BPS counts of the A-polynomial curve at two conjugate phases (BLR style).
Multi-session+; no network infra in corpus. Even reproducing 4_1's count 3
locally would upgrade the DT import tier. Import-tier, clearly labeled.
Lowest priority per unit cost.

### D1-e — Formalize-first: Lean constraints on the (Q,W,ray,ray) shape
Before any scan: prove what abelian + two rays + the datum force —
(i) >=4 / >=3 stable classes per ray (vertex lower bounds); (ii) rays not
exchangeable by arrow-preserving relabeling (import of the landed exclusion);
(iii) the M2 dimBPSplus = sAtOne+1 anchor as a ray-count tie. Session-scale,
sorry-free-achievable. Each theorem must delete a concrete slice of the D1-a
enumeration. DO D1-e BEFORE OR WITH D1-a.

### D1-f — Wait-on-lit watch (named unblockers)
(1) published closed-sector BPS quiver for T[5_2] -> unblocks D1-b;
(2) exponential-network counts for 5_2 -> validates (4,3) independent of GGM;
(3) a 6_1 (or 3_1) DT spectrum -> the third-knot falsification target;
(4) any categorification of the 3d-index from Hecke/Soergel data -> reopens
D1-c. Passive; not a substitute for D1-a/e.

### Sequencing
1. D1-e (formalize-first, prunes downstream) 2. D1-a (candidate generator)
3. D1-b (main multi-session thrust) 4. D1-c (parallel sibling, distinct angle)
5. D1-d/D1-f passive. Nothing derives A_omega; datum stays certified-imported;
q0-derivation untouched (forever-gated).
