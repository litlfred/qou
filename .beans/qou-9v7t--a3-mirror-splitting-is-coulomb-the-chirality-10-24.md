---
# qou-9v7t
title: 'A=3 mirror splitting is Coulomb: the chirality 10-24x range was that leaking in'
status: completed
type: task
priority: normal
created_at: 2026-08-29T09:03:12Z
updated_at: 2026-08-29T09:03:44Z
---

## PR #5990, branch `claude/b3-cross-isotope-tracking-2026-08-29`

### The finding

The 2026-06-23 audit records the chirality-weighted trace as the sign carrier for
the 3-body force, magnitude **"10-24x" short**. That is a RANGE because it was
measured per atom: ~24x at 3H, ~8.7x at 3He.

**It is not candidate spread.** 3H and 3He are MIRROR nuclei, so
`b3(3H) - b3(3He) = B(3H) - B(3He) = 0.763755 MeV` **exactly** (the pair-additive
`3*B(2H)` cancels), and that is the **Coulomb displacement energy**, up to the
Nolen-Schiffer residual. The range was Coulomb splitting leaking into a
strong-channel comparison.

Split into charge-symmetric / charge-antisymmetric:
- `b3_sym  = 1.4262225 MeV` — the strong channel's obligation
- `b3_asym = 0.3818775 MeV` — the EM channel's

### Four results

1. **The gap is ONE number per variant**: 2-bond chiral **14.5x**, triangle-closed
   **8.4x**, with long-range 1-3 bond **6.1x** — all on `b3_sym`.
2. **Every** chiral variant has a **wrong-signed** antisymmetric part, including
   triangle-closed and long-range. So the inversion is **not** the 2-adjacent-bond
   truncation artifact the audit flags, and closing the triangle does not fix it.
3. **9 of 10** candidates get the mirror asymmetry backwards. Only the product
   3-bond term is right-signed, at **21.8%** of the displacement. The wrong-signed
   ones reach up to 65% magnitude — worse, not better.
4. **Mechanism**: two competing NON-EM sources. `tau_p/tau_n = 1.1600` favours 3He;
   the bond product ratio `0.6494` favours 3H. The 1-bond term is dominated by the
   first, the 3-bond term by the second. **The sign of the mirror splitting is an
   accident of which term dominates, not a prediction.**

### Consequence

A cross-atom ordering test over the mirror pair **cannot discriminate 3-body
candidates** — it grades them on a channel none of them has. Candidates belong on
`b3_sym`; the splitting is a separate **EM-channel** obligation.

Directly relevant to the arc's three-channel framing: **the A=3 mirror pair is
where the EM channel shows up in binding, and the framework has no EM term in any
per-bond factor** (`f_pp = z`, `f_nn = z - h`, `f_pn = z - h(1/2 - delta/4)`).

### Withdrawn

I first ran this as a candidate *ordering* ranking, concluding the chirality route
anti-correlates with b3. The facts are right and are kept; the framing was wrong
and is withdrawn in the docstring — ordering over a mirror pair is a Coulomb test.

### Scope

Scope-limited **(a)**: n=2 atoms, a decomposition not a closure. Exploratory, no
production wiring, no fit. Pure mpmath algebra over three committed proton-pinned
witnesses sharing E0; no layer straddle.

### Verification

`precision-gates.sh --changed`: NEW-dirty counts **0**. Was `Q0_ANCHOR_MISSING` on
first run — **fixed at the producer** (stamped `q0Anchor`/`q0Value`), now `Q0_OK`.
The five remaining REDs are **pre-existing on main**, measured by stashing and
running the gate on a clean tree. No baseline widened.

### Live successor

What supplies `b3_sym` (6-14x still missing) is one question; what supplies the
**EM channel** at A=3 is a second, and nothing in the corpus currently addresses it.
