# G3 keystone attack via the GGM 3d-index of 4₁ (2026-07-14)

**Status: IN PROGRESS — stub.** Follow-on to the merged alien-calculus ↔
surreal integration review (PR #3788); executes the productive route its
modular-resurgence probe identified.

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
