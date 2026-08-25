# Coordination ledger — SM 26-parameter chip-away (2026-08-02)

**Goal.** Chip at the 26 Standard-Model parameters from the QOU categorical
model: identify which are fundamental observables vs. derived renderings, and
attack the tractable open fronts under strict derive-then-check / anti-fit
discipline. Owner-driven session; feeds the QOU→SM derivation queue (#4600,
bean `qou-jsx5`).

**Governing insight (the reframing, PR #4602).** The 26 are a *downstream
rendering* of the categorical action under archimedean evaluation
(cat action → q-CLT → archimedean → observables → rendered SM params). All
torus-knot *carriers* are Vol=0 (#4589), and confined-quark "masses" are not
direct observables — they are scheme-dependent Lagrangian parameters extracted
from color-singlet bound states. So ~14 of the "21 open" (6 quark masses + 8
mixings) are **derived quantities of the observable spectrum**, not independent
open knots.

## PR cluster (this session)

| PR | Front | Result | Copilot |
|----|-------|--------|---------|
| #4602 | reframing | observable-vs-rendering reclassification of the 26 | — |
| #4589 | m_ν + map | carrier≠mass-knot (all torus carriers Vol=0); neutrino volume-density scope-(b) excluded (~10¹⁰ gap) | — |
| #4584 | m_c scaffold | complex-mass constituent functional (primary conjecture, open); 3 charm negatives (tower scope-a, carrier scope-b, composite volume) | — |
| #4594 | m_c projection | Frobenius charm-block ratio O(1) vs O(100) hierarchy — scope-(a) negative | ✅ resolved |
| #4591 | m_τ | complex-volume (Vol+i·CS) search — sharpened negative (entropy 14.5 bits forbids census ID; torus carrier; CS-blind muon anchor) | ✅ resolved |
| #4597 | sin²θ_W / Y | **advance:** Milnor triple linking μ̄₁₂₃ = the writhe-independent 2nd invariant; separates the two U(1)s; Y=B on non-strange; Lean sorry-free | ✅ resolved |
| #4596 | θ_QCD | bar-symmetry ⟹ θ∈{0,π} proved sorry-free (modest anchor); CP-evenness → open SU(3); smallness open | ✅ resolved |
| #4582 | charm knot | charm/bottom column-swap fix + gg→cc̄ colour-threading reconciliation (T(3,5)=production vertex, not weak mediator; W=T(2,4)) | — |
| #4562 | EW even-tower | boson tower uniformly harmonic (continuant divisibility) | ✅ resolved |
| #4579 | reverse divisibility | b_a∣b_n ⟺ a∣n sorry-free (generation windings = odd primes, whole tower) | (DRY note: morganVoyceB now on main) |
| #4565 | generation bridge | general Fibonacci-poly harmonic law + honest quark-H₃ negative | — |
| #4564 | SU(3) | Hecke-centralizer obstruction on regular H₃ (dim 6<8 exclusion), sorry-free | — |

| #4608 | J/ψ observable | **mechanism-applicable + sharpened negative:** the J/ψ scale IS in-range (Vol≈24 hyperbolic braids → ≈3097 MeV) — distinguishes J/ψ (applicable) from ν (scope-(b) excluded). But NO derived braid: the canonical meson flux-tube operation is undefined (bean `qou-qpj9`); J/ψ vs η_c want different-topology braids (per-state-fit signature); dense spectrum (entropy). | — |

## Scorecard (honest)

- **Parameter tiers moved: 0.** Canonical L2 count stays 2/7; the 26-param split
  stays 1 input / 1 proxy / 1 partial / 2 conjectural / 21 open **by the SM's
  accounting** — but the reframing re-scopes ~14 of the 21 as *derived*.
- **One genuine structural advance:** μ̄₁₂₃ separating the two U(1)s (#4597) — the
  most tractable lever toward sin²θ_W.
- **One conceptual correction:** observable-vs-rendering (#4602) — explains why
  the four charm-mass attacks were category errors (targeting a non-observable).
- **A stack of honest negatives** pruning dead routes (charm tower/carrier/
  composite/projection; m_τ census; neutrino volume; θ_QCD ceiling at {0,π}).
- **Zero fabricated numbers.**


## Session log

| Date | Agent / branch | Intent | Results |
|---|---|---|---|
| 2026-08-04 | Copilot / `copilot/eight-fold` | INTENT: external electron.pdf triage + drain nearby electron arc beans in SM/eight-fold scope | RESULTS: network fetch to physicsdetective blocked; corrected electron-arc prose to keep knot identification but remove standalone trefoil-mass overclaim, and aligned the example with CAL-1 framing. |

## Open fronts (beans / follow-ups)

1. **Canonical meson flux-tube operation** (bean `qou-qpj9`, #4608) — the J/ψ
   attack confirmed the observable is *in mechanism range* but is blocked on a
   *derived* c̄c-binding braid. **Resolved to an honest negative + the precise
   missing datum (#4614, bean `qou-mesont3`):** the Y-junction 3→2 reduction
   gives B₂ (abelian) → torus link → Vol=0 (scope-(b), SnapPy-verified) — strand
   *removal* can't build hyperbolic structure (the framework already puts the
   meson at H₃(q), Hopf-binding = 3rd strand). And the operator-selection input
   is under-determined because **`windingContent` is non-injective** (Lean-proved):
   charm (n=5) and strange (n=5) share the generation-2 block — the D-meson
   `{5,3}` collides with the kaon `{3,5}` (same multiset). The missing object is a
   **weak-isospin T₃ grading orthogonal to the winding n** (up-type charm vs
   down-type strange). Bonus: a live corpus inconsistency — charm assigned both
   T(2,5) and T(2,7) across tables (canonical-watcher).

**★ CONVERGENCE (the headline).** The charm-mass gate (`qou-mesont3`: a
weak-isospin T₃ distinguishing up/down-type at fixed generation) is **the same
missing object** as the electroweak-mixing gate. #4597 gave the writhe-independent
2nd invariant μ̄₁₂₃ = Y; the writhe→I₃ map (G2 #4561) is the T₃; and the
up/down-type distinction the D-meson needs IS weak isospin. So the charmed-hadron
observable spectrum, sin²θ_W, and hypercharge Y all block on **one** object: a
weak-isospin T₃ grading orthogonal to the generation winding. That is now the
single highest-leverage target — it unlocks three fronts at once.

**★★ UPDATE — T₃ DERIVED (partial), #4618 (`qou-tdrd`).** The signed writhe factors
canonically: `κ = sign(κ)·|κ| = T₃ × generation-winding`, so **T₃ = sign(κ)/2 ∈
{±½}** is the *sign-half of the very integer whose magnitude the framework already
reads as the generation* — orthogonal by construction, derived from the oriented
crossing already in the corpus (not a second postulate). Sorry-free Lean (exit 0,
axioms clean): **charm ≠ strange** (both n=5, opposite T₃) resolves the meson
degeneracy, and **GMN `Q = T₃ + Y/2` closes** — a real derive-then-check (a wrong sign or a
wrong ½ breaks it). **State its width, though:** quantified over six quarks it
collapses to **two** distinct rows, since `Y` is constant and `Q`, `T₃` both
depend only on the up/down-type bit. One sign correlation plus one
normalisation, checked twice — now machine-checked as such
(`gmn_check_has_two_distinct_rows`, `genWinding_finer_than_gmn_data`), so the
"all six quarks" phrasing cannot be read as six confirmations. Honest remainder
(conjecture class, no instance): up=positive is *inherited* from the ⋈_K strong-
isospin datum (consistent, not *forced*), and the SU(2)_L gauge/CKM lift is open —
both reduce to the open SU(3)-flavour sector. So: a real orthogonal ℤ/2 passing GMN,
NOT yet *the* gauged weak isospin. Chiral-EFT lit for the binding-side template in
`library/` (owner: 1011.1343, 1906.12122, s00601-2022).

**★★★ UPDATE — the two follow-on tests (both landed, both honest negatives that sharpen):**
- **`qou-buxs` (T₃ vs Δ_λ sign), #4623 — DERIVED negative.** The literal T₃ = sign(net
  writhe) is the WRONG sign *statistic*: matches 3/3 at n=3 but 8/11 at n=6 (fails the
  height-4/5 columns). The chiral-EFT template (HKvK p.12: isospin sign = exchange
  symmetry of the isospin wavefunction) *derives* the correct statistic = crossing-**count**
  parity `(−1)^C(c,2)`, which **is** `sgn(w₀^{S_λ'})` restated (not new info from T₃). So T₃
  locates *where* the sign lives (the antisymmetrizer crossings — what PROBE-4 demanded) but
  is too coarse. Scope-(a): surviving route = a **count-parity** closure, not net-writhe.
- **`qou-2udt` (T₃ into meson op-selection), #4625 — degeneracy RESOLVED, mass still open.**
  Signed-writhe `(n,2T₃)` separates all 6 quarks (sorry-free); charm block distinctly
  selectable from strange on `{π,K,η,D}`. But proved `mass_from_graded_content_cannot_separate`:
  the mass is NOT a function of `(n,T₃)`.

**⇒ The D-meson mass now gates on exactly TWO objects:**
1. **Third flavour grade — SU(3)/SU(4)-flavour Cartan** (`qou-dnm1`): `(n,T₃)` still collides
   D̄⁰{c̄,u} with K⁰{d̄,s} (same multiset); needs strangeness S / charm C. This is the
   **flavour** SU(3) eightfold-way (global) — DISTINCT from the excluded **colour** SU(3)
   (#4564, gauge). Owned partly by #4600 (`qou-d7h1`).
2. **Flux-tube braid word** (`qou-qpj9`): the hyperbolic braid giving the mass; `(n,T₃,flavour)`
   only pins the Vol=0 carrier.

2. **Generation physical bridge** — the *counting* (3 = odd primes in the
   Bring-genus window N(χ=−6)=9, {3,5,7}; 9 harmonic) is clean given the
   identifications; the *physical bridge* (why prime-winding = a fermion
   generation; why harmonic knots add none) stays open (G1: no rigorous
   argument). Blocks the 8 mixings.
3. **SU(3) colour sector** — only a negative (#4564); blocks α_s, θ_QCD-smallness,
   Y=B+S strangeness extension of #4597.
4. **sin²θ_W normalization** — #4597 separated the U(1)s but the relative U(1)
   coupling normalization inherits open SU(3)-flavour.

## Anti-fit discipline (held throughout)
Every "closest hit" was gated against search-space entropy; every scaffold is a
content-bearing conjecture with **no instance** (open); no anchor-inversion was
wired as canonical; negatives are scope-tagged (a)/(b) with cited invariants.
