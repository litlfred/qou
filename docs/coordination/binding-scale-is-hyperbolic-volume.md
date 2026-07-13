# The binding scale is the hyperbolic volume — coordination ledger

**Date:** 2026-07-13 · **Owner question:** "what is driving the scale?" (of
per-isotope binding). This ledger records the answer and, per the "make sure
Lean proved" directive, the **exact** proof status of each part — separating what
is Lean-proved, what is conditional on an open conjecture, and what is empirical.

## The answer

The per-isotope binding scale is `m_e · Vol(K)` — the **hyperbolic volume** of the
nuclear sub-link — carried by the bond-count law

`B(K) = m_e · Σ_n M_n(A) · Vol_n(K)`,  `M_n(A) = (n−1)` (linear-chain bonds).

This is the one construction that does **not** undershoot: ³H = m_e·2·Vol(8₁₁) =
8.47 MeV (−0.16%), ³He = m_e·2·Vol(L6a4) = 7.49 MeV (−3%), zero fit. Every
parameter-free object that undershot this session (the `sgn·dim` Δ_λ base 70–89%,
the Reeb phase θ_λ ~270×, the deuteron resummation ~37×) undershot precisely
because it **lacked the volume** — the missing magnitude is not a q₀ power (checked
and excluded) but the **volume**, a distinct hyperbolic invariant.

**Physical driver (volume conjecture).** `Vol(K)` is the exponential growth rate
of the colored Jones polynomial, `Vol(K) = lim_N (2π/N)·log|J_N(K; e^{2πi/N})|`
— the braid's categorical entropy / na-Stokes "computational time." So *binding
energy = m_e × (hyperbolic complexity of the nuclear braid)*: more linking → more
volume → more binding.

## Lean / proof status (STRICT — the "make sure Lean proved" table)

| claim | status |
|---|---|
| **bond-count multiplicity `M_n(A) = (n−1)`** and the cluster-measure identity `6·Σ_k (A−k)k = (A−1)A(A+1)` | ✅ **Lean-proved, sorry-free** — [`QOU/Mass/LinearChainBondCount.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/LinearChainBondCount.lean) (`chainBonds`, `linear_chain_cluster_measure`, proved by induction; 0 sorries; source-confirmed — not `lean_verify`'d in this sandbox) |
| **deuteron `Vol = 0`** (2-body Hopf sub-link) | geometric fact — the Hopf link is **non-hyperbolic**, so the RHS of the volume conjecture vanishes ([`degree-one-braid-trivial-volume-proof.md`](../../content/quantum-observable-universe/mass-theory/degree-one-braid-trivial-volume-proof.md), KMM convention) |
| **`Vol(K)` IS the binding scale** (the load-bearing claim) | ⚠️ **CONDITIONAL on an OPEN conjecture** — the identification of `Vol` with the colored-Jones/categorical-density growth is [`conj:kashaev-volume-conjecture`](../../content/quantum-observable-universe/mass-theory/kashaev-volume-conjecture.md), a **conjecture** (axiomatised as a Lean class, not proved; the KMM volume conjecture is open in the literature). Per "conditional-proved ≠ premise-established," the scale claim is *conditional*, **not** established. |
| **the 3% accuracy** of `m_e·2·Vol` vs AME | empirical (measured; the −3% ³He residual is the Coulomb/EM piece, 31% derived) |

**Bottom line for Lean:** the *combinatorics* of the scale (the bond count) is
proved; the *identity* that makes `Vol` the scale is the open volume conjecture.
So "binding = m_e·Vol" is a **rigorous conditional result** modulo one named,
class-axiomatised conjecture — not an unconditional theorem. Claiming it as
"derived/proved" without that qualifier would be laundering.

## What this narrows the open gate to

The magnitude is **not** a universal missing scale — it is `m_e·Vol` wherever the
sub-link is hyperbolic (derived modulo the volume conjecture). The genuine open
items are narrow and specific:

1. **⁴He 4-body `Vol₄`** — the bond-count route predicts `Vol₄ = 8.05` for the
   ⁴He 4-component link (from `B_AME − (n=2,3 terms) = m_e·3·Vol₄`). **Falsifiable
   prediction:** compute the hyperbolic volume of the canonical ⁴He link with
   SnapPy and compare to 8.05 (in-family with 8₁₁=8.29, L6a4=7.33). *Not run here
   — SnapPy unavailable in this sandbox.*
2. **deuteron** — Hopf `Vol=0` is a regime boundary (non-hyperbolic), not a gap;
   the 2-body scale is the derived q-rotational `μ₀·ℏ_q·J_q²` (−9%), a genuinely
   different mechanism. Refining −9% → tighter is the open A=2 item.
3. **mirror Coulomb residual** — 31% derived (`tanh(ln q₀)·B_pp`); the rest is the
   geometric/Milnor EM object (the pairwise route is provably empty — Borromean
   L6a4 has pairwise linking 0). The Reeb phase θ_λ is the right geometric
   candidate but bare-undershoots ~270× (needs the `Vol`-type magnitude).

## Session cross-refs

Deuteron trans-series negative (#3736); Δ_λ gate + CKRecursion review (#3723);
Borromean redirect + Reeb test + "magnitude not a q₀ power" (#3738);
θ_λ magnitude gate ([`2026-07-03-theta-lambda-via-reeb-nastokes-jet-filtration.md`](../audits/2026-07-03-theta-lambda-via-reeb-nastokes-jet-filtration.md)).
