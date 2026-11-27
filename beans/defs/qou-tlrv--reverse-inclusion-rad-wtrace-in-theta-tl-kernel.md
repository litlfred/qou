---
# qou-tlrv
title: 'Reverse inclusion: rad(wtrace) ⊆ θ(tlKernelPulled) — the remaining half of the Hecke radical = TL ideal equality'
status: completed
type: task
priority: normal
created_at: 2026-11-27T15:20:00Z
updated_at: 2026-11-27T15:45:00Z
parent: qou-0cyu
---

Open conjecture (rule 13a: do not close on partial progress).

**Settled (PR #9482, `BraidKnotOctonion/TLKernelConvention.lean`):** θ(tlKernelPulled) ⊆ rad(wtrace) at every n (`theta_mem_rad`), and the untwisted inclusion fails at n = 2 (`tlKernelPulled_not_le_rad`). See `qou-jb7k`.

**Target:** rad(wtrace) ⊆ θ(tlKernelPulled), i.e. every x killed by all ≤2-row seminormal blocks has θ⁻¹x in the TL kernel. With the ⊆ half this gives the ideal equality asked for by `rem:hecke-radical-is-temperley-lieb`.

**Candidate routes (none chosen yet):**
1. Dimension: H/rad has dimension Σ_{≤2 rows} (f^λ)² = Catalan (`dimHLF_two_row_sq_sum`, on main), so the ideal equality follows from dim TL_n(δ) ≤ Catalan(n) at general n. Earlier ruled out as circular only if dim TL = Catalan is itself derived from this arc; an independent spanning-set bound (Jones normal form / reduced words) is not circular.
2. Representation: show the TL quotient map's kernel is cut out by the ≤2-column blocks directly (each such block factors through TL, Wedderburn on the semisimple quotient).

## 2026-11-27 — PROVED (PR #9488)

`BraidKnotOctonion/TLKernelEquality.lean`, `mem_tlKernelPulled_iff`: y ∈ tlKernelPulled ↔ θ y ∈ rad(wtrace), over any CharZero field, q ≠ 0 not a root of unity. Neither candidate route was needed: `JimboKernelGeneric.traceQuotTLEquiv` (H/rad ≅ TL, eᵢ ↦ q − σᵢ) already existed, and the θ-twisted skein map equals its composite `heckeToTLGeneric` on generators. 188-module cone green. The conjecture is now a theorem, so this bean is completed.

