---
# s6jb
title: 'do-not-re-walk: cyclotomic-Galois Li3(zeta5) is period-axis, not an s5-so3 keystone falsifier'
status: todo
type: task
tags:
    - s5-so3
    - do-not-re-walk
created_at: 2026-06-20T11:49:26Z
updated_at: 2026-06-20T11:49:26Z
---

Recorded after PR #2506 (hyperbolic-hurdle pre-archimedean assessment), where a
fresh agent (me) independently re-derived the `conj:joint-galois-braid-action` /
`cl3_zeta5_orbit_sum` cyclotomic reduction (Σ Li_3(ζ5^k) = -24/25 ζ(3); open
content → one generator Cl_3(2π/5)-Cl_3(4π/5) ≈ 0.955) and **mistook it for a
cheaper falsifier of the s5-so3 keystone map**. It is not. Correction, per
`docs/coordination/s5-so3-keystone.md`:

- The cyclotomic-Galois / Li_3(ζ5) reduction lives on the **period / z-Habiro
  axis** (the m_τ Goncharov bi-filtration depth side) — explicitly **orthogonal
  to the keystone coupling** (q-side); forcing the period↔knot bridge is the
  *refused unfalsifiable correspondence-chain* (ledger 2026-06-17 note).
- The keystone's single open object is the **geometric leg of ingredient 4**:
  does a 2I-equivariant contact/Sasakian Reeb realization on the Bring 5-strand
  spin bundle EXIST whose Markov trace = the (forced, rigid) H5(q)
  principal-specialization Ocneanu trace. `W_λ = d_q²/[n]_q!` is the q-Plancherel
  measure, NOT the production weight (#2406); finite-dim Sasakian ruled out.
- `partition_to_rotation` was falsified / de-vacuified (#2480).

DO NOT re-pitch the cyclotomic-Galois orbit test as a keystone falsifier. It is a
real fact about the m_τ period axis only. Belongs in the ledger's "Refutations
not to re-walk" if the owner agrees.

Ref: #2506 §6.2 (corrected);
docs/audits/2026-06-20-hyperbolic-hurdle-pre-archimedean-realization.md
