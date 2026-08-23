# G3 keystone attack via the GGM 3d-index of 4₁ (2026-07-14)

**Status: 3d-index face CERTIFIED (2026-08-15, PR #5071); A_ω=3 already
derived via the W_m/Stokes route; internal derivation of the DT spectrum
remains the tracked open frontier (Route C).** Follow-on to the merged
alien-calculus ↔ surreal integration review (PR #3788); executes the
productive route its modular-resurgence probe identified. See
§"Resolution (2026-08-15)" at the foot of this document for the current
state — the "IN PROGRESS — stub" body below is retained as the historical
2026-07-14 record.

## The target

G3 (phib audit §4c/§4e) is the keystone monodromy datum: compute the
Stokes constant `A_ω` via the alien derivative `Δ_ω`. The corpus has
bottomed out on the *analytic* route (the S-ladder singularity was
unresolvable at k = 21 — a finite-n shadow, PR #3737) and on inverting
κ-rungs (a fit, forbidden). The `qbeta-modular-resurgence-stokes` probe
(PR #3788) confirmed: the even-face action is consistent with Vol(4₁)/π
but `A_ω` is *not* identifiable from the perturbative rungs alone.

## The route

Per phib audit §4e (quantum-modularity / Habiro-ring rigidity): the
Garoufalidis–Gu–Mariño resurgent structure of 4₁ gives the Stokes
constants as **integer counts read from the 3d-index / state integral**,
not fitted numbers. The corpus already has the *analytic* state-integral
saddle (complex volume 𝔙 = Vol + iCS, smooth, anchor-blind) and the
*combinatorial* root-of-unity face (∏(1−xζ^k) = 1−x^N). The one unbuilt
face is the **3d-index q-series** whose coefficients are the GGM integer
Stokes data — the algebraic object quantum modularity identifies with
the transcendental `A_ω`.

## Plan

1. Compute the 3d-index of 4₁ as an explicit q-series (tetrahedron-index
   double sum; two ideal tetrahedra).
2. Extract the GGM Stokes constants as the integer sequence built from
   the index; check the formalize-first question — is
   `A_ω = [3d-index datum]` a derivation or a fit?
3. Cross-check the derived Stokes data against the corpus's even-face
   action and the odd-face requirement.
4. Report honestly (scope-(a)/(b) discipline); no `A_ω` or `c_k` wires to
   production unless genuinely derived.

Deliverable: probe + witness + this audit filled in.

## Progress (2026-07-14)

**Built:** `computations/probes/tetrahedron_index.py` — the DGG tetrahedron
index `I_Δ(m,e)(q)` (canonical sum form) plus a self-validating triality
harness `check_symmetries` that numerically tests candidate conventions
rather than hardcoding one.

**Finding (honest gate):** the naive transcription of `I_Δ` does **not**
satisfy the literature triality `I_Δ(m,e) = (±q^?)^e I_Δ(-e-m, m)` across
all `(m,e)`: the `(-√q)^e` form matches the `m=e=1` case to ~1e-41 but
the negative-`e` cases miss by O(0.3). This means the standard definition
carries a normalization prefactor (an overall `q`-power / `ζ=-q^{1/2}`
convention) that must be pinned from the primary source
(Garoufalidis, arXiv:1208.1663; DGG arXiv:1112.5179) before the 4₁
two-tetrahedron gluing is assembled on top of it. Per the
formalize-first / anti-guessing discipline, the 4₁ index is **not** built
on an unvalidated `I_Δ` — the self-test is the gate, and it is currently
red on the negative-`e` triality.

**Next (gated on the verbatim formula):** pin the `I_Δ` normalization so
`check_symmetries` goes green on all cases; assemble `I_{4₁}(0,e)(q)` as
the standard 2-tetrahedron sum; validate against a published coefficient;
then read the GGM Stokes data and run the formalize-first derivation-vs-fit
check against the corpus even-face action (Vol(4₁)/π) and the geometric
`vol_of_m` solver.

## Resolution (2026-08-15, PR #5071)

The three obstacles the 2026-07-14 stub was gated on are all cleared; the
resolution also corrects two of that stub's own assumptions.

### 1. The `I_Δ` normalization was never the blocker — the total-index assembly was

With the DGG source now in-repo (`library/arxiv-1112.5179v1/1112.5179v1.pdf`), eqs 4.17–4.20
were read glyph-verified. The stub's worry — "the standard `I_Δ` carries a
normalization prefactor that must be pinned before the 4₁ gluing" — was a
**red herring**: the canonical `I_Δ` sum
`Σ_n (−1)ⁿ q^{½n(n+1)−(n+e/2)m}/((q)_n (q)_{n+e})` is correct as-is, and the
figure-eight total index is the **bare** flux sum (DGG eq 4.18)

  `I_{4₁}(m,e) = Σ_{e₂∈ℤ} I_Δ(m−e₂, m+e−e₂)·I_Δ(e−e₂, −e₂)`   — **no prefactor.**

The earlier `q^{−e₂}` "near-miss" came from mistakenly applying eq (4.17)'s
*pre-U(1)-breaking* factor `(−q^{1/2})^{−2e₂} = q^{−e₂}` to (4.18).

### 2. The "divergent flat negative wing" was a truncation artifact

The prior assembly rejected the bare (4.18) as divergent. That was wrong: the
DGG index `I_Δ(m,e)` has min-degree ≥ 0 reached only through deep
cancellations, so rebasing a low-order truncation to its *un-cancelled*
minimum reported a false `q⁰` lead for large-charge factors. Computing `I_Δ`
at **absolute degree** (never rebasing per factor) makes large-|e₂| factors
correctly contribute nothing below the target order and the flux sum
converges — exactly as DGG state. No `U=2log m` charge dictionary and no
appendix-B tables were needed (the stub's suspected next-inputs).

### 3. Certified (`computations/probes/qbeta_g3_fourone_index_assembly.py`, 5/5)

- bare (4.18) reproduces the printed anchor **eq (4.20)**
  `I_41(1,1) = −q−q²+2q³+7q⁴+11q⁵+11q⁶+3q⁷` exactly;
- **eq (4.19)** symmetries `I(m,e)=I(−m,e)=I(m,−e)=I(−m,−e)` exact over 7 charges;
- absolute-degree `I_Δ` cross-checks the tranche-1 exact engine;
- `I_41(0,0) = 1−2q−3q²+2q³+8q⁴+18q⁵+18q⁶+14q⁷−…` converges at the substrate;
- the certified index is annihilated by the DGG **quantum A-polynomial** `L̂_{4₁}`
  (eq C.7) over 9 charges — the *same* q-difference operator whose fundamental
  solution `W_m(q)` yields the GGM Stokes matrix `S⁺`. So the index face and the
  A_ω route are descendants of one operator (the AJ recursion for 4₁).

### 4. A_ω is derived via `W_m`, not via this index — and the stub's plan-step 2 is moot

The formalize-first derivation-vs-fit check the stub planned (read A_ω off the
3d-index) does **not** apply: A_ω is not a coefficient read-off of `I_41`. The
corpus already derives **A_ω(4₁) = 3** — Lean-proved (`QOU.QBeta.StokesQZeroDTCount`,
decidable integer-matrix algebra) via the GGM Stokes matrix `S⁺(0)` from `W₋₁(q)`,
composed through the bridge (`thm:aomega-fourone-dt-count`, conditional on
`conj:stokes-dt-bps-bridge`). `W_m(q)` and `I_41` are *different descendants* of
the same q-holonomic module; the certified index is an independent face, not the
A_ω input.

### 5. The internal derivation stays open (Route C), and the bounded angles are exhausted

Deriving the DT spectrum `{3,4}` from the QOU categorical drivers is open in the
DT-categorification literature itself (a Hecke-algebraic BPS-count formula would
be a new theorem). Per the 2026-08-11 attack-options memo: Route A's slope leg is
refuted on 5₂, Route D (knots-quivers, det=5) is refuted, the scalar avenue is
exhausted, and the "C1 binding carrier = `Â_{4₁}`" idea is refuted (C1 Newton
slopes ±½ ≠ ±4). The surviving R1 handle (DT = A-polynomial L-degree =
#flat-connections) is the decategorified χ-shadow of Route C (CoHA/BPS-cohomology,
a research programme). Separately the downstream A_ω→observable bridge is refuted
(2026-08-14, O2 negative). Tracked: beans `qou-qnnq` / `qou-rtec` / `qou-52sn`.

**Net:** the 3d-index face is certified and operator-tied; A_ω=3 stays a
certified, conditionally-adopted GGM/DT count; the internal derivation is the
tracked open frontier, with no bounded angle currently surviving.

### Incidental finding (recorded, not fixed here)

The precision preflight during this work surfaced a **pre-existing** `raw-float64`
ratchet RED on `main` unrelated to this change: the `qns-crow-efolds`,
`qns-backscatter-sustainment`, `qns-tail-pileup`, `qns-amplitude-step` probe
witnesses are NEW-dirty and `rho-k-co-casimir-extended` REGRESSED (3→4). These
need a producer-side fix (carry `mpmath.mpf`, serialize via `_precision.fmt`) —
not a baseline widen. Flagged for the owning sessions.
