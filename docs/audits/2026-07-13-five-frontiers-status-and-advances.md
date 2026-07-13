# Five frontiers — status, advances, and honest gates (one pass)

**Date:** 2026-07-13 · **Branch:** `claude/five-frontiers-2026-07-13` ·
**Owner directive:** work the five open frontier items. Each gets: checkcorpus
state, any in-sandbox advance made here, and the honest gate. Scope-(a); no
fits; nothing wired.

## 1. α_EM EmFermionLoop 2-loop (the 1 ppQ flagship)

**Sharper state than "uncomputed":** the phase-2 script
(`alpha_em_rt_phase2_emfermionloop.py`) *defined* the candidate categorical
primitive (EmFermionLoop = closed strand in the fundamental SU_q(2) rep) and it
was **empirically refuted** (best −445 %). So the open item is not "compute the
diagram" but "**find the right primitive**" — the first candidate is dead, c₂ is
entropy-blocked from any numerical identification (two-loop-structure probe),
and the honest route remains a genuinely new categorical 2-loop construction.
**Gate:** research-frontier; no in-sandbox advance possible beyond this scoping.

## 2. SDP canonical knot-ID at H₁₂ (the true ⁴He link)

**Checkcorpus:** a sibling already ran the obvious route —
`he4_link_volume_braid_closure.py`: **naive Markov closure of the canonical
atomic word does NOT reproduce the SDP binding links at any A** (wrong component
counts, non-hyperbolic closures). The 3-body links (8₁₁, L6a4) are
SDP/canonical-knot-ID outputs, not closures. Combined with this session's
#3758 negative (no pre-named 4-component link at the back-out 8.048), the
single-volume n=4 reading is now **doubly disfavored**, and the recorded A=4
tension stands: provisional doubly-magic `2·Vol(Bor) = 14.655` vs the `8.046`
back-out (~1.8×). **Gate:** extend the knot-ID SDP solver scope A≤3 → A=4 —
needs B₅ Hoefsmit + the Clarabel (Rust) backend, unavailable in this sandbox.
Concrete, named, environment-blocked.

## 3. Volume conjecture / scale derivation — NARROWED (advance)

The binding-scale ledger marks `Vol = scale` conditional on
`conj:kashaev-volume-conjecture`. **The framework does not need the full KMM
conjecture — only the instances for its specific SDP links:**

| link | isotope | volume-conjecture status |
|---|---|---|
| **L6a4 = Borromean rings** | ³He | **PROVEN** — the Borromean rings are a Whitehead chain, and the volume conjecture is proved for Whitehead chains (R. van der Veen, *Proof of the volume conjecture for Whitehead chains*, arXiv:math/0611181). ⚠ citation recalled from the literature; the sandbox arXiv search returned empty — **verify before wiring into the ledger's Lean table.** |
| 8₁₁ | ³H | open (no proof known for this knot) |
| 4₁ (figure-8, muon anchor) | — | proven (Ekholm / Andersen–Hansen) |

If the van der Veen citation verifies, the ³He (and 4₁-anchored) scale
identifications upgrade from "conditional on an *open* conjecture" to
"conditional on a **proven instance**" — leaving only ³H (8₁₁) on an open
instance. That is a real reduction of the conditionality footprint of the
binding program. **Action queued:** verify citation, then update the
[binding-scale ledger](../coordination/binding-scale-is-hyperbolic-volume.md)
Lean-status table per-link.

## 4. Substrate q₀ (s5-so3 keystone)

Sibling-active thread with landings inside this window (fibre residue sorry-free
#3677; categorical fibre→observable explication #3681; Watson uniqueness bricks
landing daily on `el8w`). **Coordination decision: no duplicate work from this
session** — the active thread owns it; nothing added here beyond this note.

## 5. Geometric/Milnor Coulomb object — NEW GEOMETRIC DATA (advance)

The #3738 redirect established the pairwise EM-linking route is structurally
empty (Borromean pairwise linking = 0) and left "geometric or Milnor-triple" as
the object class. **New SnapPy data (this branch):** the L6a4 complement has
symmetry group **Z/2 × octahedral (order 48)** with all three cusps geometrically
identical (max-cusp volume 0.324760 each, reach 1.255482 — exact 3-fold
equivalence).

This **substantiates the pre-named 1/3 candidate structurally**: the measured
effective Coulomb/strong ratio the full ³H–³He split needs is
`split/B_pp = 0.3341` — within **0.2 %** of `1/3` — and the Borromean geometry
now says the pp pair is *one of three geometrically equivalent pair-channels*.
Upgraded from a numerology-guarded datum (#3738) to a **structural conjecture
candidate**:

> **Candidate (conjecture-tier, NOT wired):** the ³He Coulomb reduction is the
> strong pair-bond through exactly one of the three equivalent Borromean
> pair-channels, `E_split = B_pp/3` — predicting the split to 0.2 % with zero
> parameters *if* the one-channel selection is derived. The missing derivation
> is *why the two-like-charge (pp) pair occupies exactly one channel* — the
> Milnor triple `μ̄(123) = ±1` (the defining Borromean invariant, nonzero where
> all pairwise invariants vanish) is the natural candidate selector.

Numerology guard: `1/3` is reported with its structural justification (S₃
channel equivalence, now SnapPy-verified) and stays unwired pending the
selection derivation.

> **⚠ SAME-DAY CALIBRATION (the selection-derivation attempt REFUTES the fixed
> 1/3 as a universal rule).** Checkcorpus for the derivation surfaced the 8-pair
> [mirror-Coulomb systematics](2026-07-11-mirror-nuclei-coulomb-systematics.md)
> (merged 2026-07-11): the mirror split is proportional to the **continuum
> Coulomb displacement** `ΔE_C ∝ Z(Z−1)/(r₀A^{1/3})` across ALL eight pairs
> (`split/ΔE_C = 0.838 ± 0.059`). At A=3 the two parameterizations are
> indistinguishable (`0.765·ΔE_C = 0.764` vs `B_pp/3 = 0.762`), but the fixed
> `B_pp/3` **fails ⁷Li/⁷Be** (predicts 0.76 vs measured 1.644 MeV, 2.2×) while
> `0.84·ΔE_C` covers the whole chain at 7 % scatter. Eight points beat one: the
> 1/3-channel reading is a **single-point coincidence**, downgraded same-day
> (scope-(a)). The honest target for the geometric/Milnor object is therefore
> to *derive the continuum-Coulomb scaling* `~0.84·α·Z(Z−1)/R(A)` from the
> categorical EM (α_EM + a derived radius law) — not a fixed channel fraction.

## Net

Advances made here: item 3 narrowed (per-link conjecture status; ³He likely on a
*proven* instance — verify citation), item 5 upgraded (SnapPy symmetry data backs
the 1/3 channel candidate), items 1–2 sharpened to named, environment- or
research-gated steps, item 4 explicitly deferred to its active sibling. No fits;
no wiring; no tier changes.
