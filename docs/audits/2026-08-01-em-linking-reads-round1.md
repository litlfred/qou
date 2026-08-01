# EM-linking invariant — round-1 reads (bean qou-o6ml)

**Date:** 2026-08-01. Reads of the uploaded EM-linking literature batch
(`be8fe53f`) against the κ(A) gate (3.2 → 2.1–2.3, from
`em-linking-invariant-scoping.witness.json`). Two parallel readers;
upload-quality problems found — see the re-upload list at the end.

## The keeper results

**1. The Milnor integral IS a mutual-energy integral** (DGKMSV,
"Pontryagin invariants and integral formulas for Milnor's triple
linking number", read in full). For a Brunnian 3-component link
(pairwise linkings zero — exactly the corpus baryon regime), Milnor's
μ̄₁₂₃ equals **the helicity of the characteristic field** `v_L` on the
parameter 3-torus:

- μ(L) = ½ ∫_{T³×T³} v_L(x) × v_L(y) · ∇φ(x−y) — a two-point
  Biot–Savart mutual-energy double integral (their Thm B(2)); φ = the
  torus Green's function. Also a Fourier form (Thm B(3)) that is
  directly computable — their Borromean model integrates to μ ≈ −0.97
  vs the exact −1 at coarse resolution.
- **Per-pair decomposition exists**: the characteristic map normalizes
  `F = (x,y)₊ + (y,z)₊ + (z,x)₊` — an additive sum of *pair* terms,
  coupled only through the normalization. And their asymmetric map
  `h_L` is literally "a pairwise Gauss map modulated by the third
  curve" — the cleanest structural hook for a *per-pair energy inside
  a triple invariant*, which is what the two-like-charge invariant
  needs (a pp-pair energy that exists only because the third strand
  closes the Brunnian structure).
- Caveat kept honest: the paper's integrals produce the topological
  ±1, nothing A-dependent — **κ(A) must come from QOU-side structure**
  (the per-pair blocks of F under the corpus braid closure, or the
  hyperbolic kernel below), not from these formulas alone.

**2. The hyperbolic per-pair kernel exists and decays exponentially**
(DeTurck–Gluck, partially recovered §48–56): explicit Biot–Savart /
linking kernels on H³ of csch/coth class — `φ(α) ~ csch α ≈ 2e^{−α}` —
replacing 1/r². Three structural bonuses for the QOU fibre:
exponential decay makes the descent to a **compact hyperbolic
quotient** convergent (Poincaré series) and kills the H³ Green-operator
non-uniqueness (discrete spectrum); pair-interaction strength falling
exponentially with hyperbolic separation is a *natural mechanism for
an A-dependent factor* — the right shape for κ(A); and their kernel
φ₃ "involves dilogarithms" — direct contact with the corpus Li₂/Li₂^q
machinery.

## Upload-quality problems (blocking full fidelity)

| file | expected | actually contains |
|---|---|---|
| `0808.1533v3.pdf` | Komendarczyk, third-order helicity | duplicate of DGKMSV 1101.3374 |
| `1101.0956v3.pdf` | DGKMSV, generalized Gauss maps | Arcuş (Lie algebroids, unrelated) ×2 + orphaned tail pages (§48–56) of DeTurck–Gluck |
| `0510388v1.pdf` | DeTurck–Gluck electrodynamics | mixed/corrupted; only tail pages recovered |

**Re-upload list** (verified IDs): DeTurck–Gluck is
**arXiv:math/0406276** (not 0510388); the generalized-Gauss-maps pair
is **arXiv:0901.1612** (announcement) + **arXiv:1207.1793** (Part 2,
Euclidean case); the Komendarczyk third-order-helicity papers (Comm.
Math. Phys. 291 (2009); J. Math. Phys. 51 (2010)) carry the
Freedman–He-style **energy lower bounds for Borromean flux tubes** —
the single most gate-relevant missing item.

## Round 2 — clean re-uploads read in full (CORRECTS round 1)

The owner re-uploaded the correct files (`math/0406276` full 40 pp;
`0901.1612` 23 pp). Reading them in full **retracts two round-1
keepers** — both were artifacts of the corrupted uploads — and
replaces them with two genuine *structural obstructions*. Net effect:
the attack surface is narrower and better defined than round 1
claimed.

### Retractions (round-1 claims that do not survive)

1. **"Per-pair decomposition exists" — RETRACTED.** The additive form
   `F = (x,y)₊ + (y,z)₊ + (z,x)₊` is real, but it does **not** survive
   into the integrand: the characteristic field carries `1/(4π‖F‖³)`
   and cross-partials, so the normalization couples the three pairs.
   The paper gives **no** splitting of the Theorem-B integrand into
   two-component pieces. The only genuinely per-pair objects are the
   three subtorus **degrees** — which are `p = q = r = 0` in the
   Brunnian case, i.e. they carry *zero* information exactly where we
   need it.
2. **"Dilogarithm contact" — RETRACTED.** No dilogarithm, `Li₂`, or
   Lobachevsky function appears anywhere in the real DeTurck–Gluck
   paper (kernel inventory is trig/hyperbolic only: `cot`, `csc`,
   `coth`, `csch`, plus polynomial). The round-1 sighting came from
   the foreign pages bound into the corrupted PDF.

### Two structural obstructions (the round-2 payload)

**O1 — Total antisymmetry blocks reading a pair energy off μ̄₁₂₃.**
Under a permutation of the three components, `g_L` transforms by the
corresponding automorphism of `T³` *times the sign of the
permutation*: μ is **totally antisymmetric** in the three components.
A per-pair repulsion energy is *symmetric* in its pair. So a symmetric
per-pair quantity cannot be read off μ̄₁₂₃ directly — any construction
must break the antisymmetry by additional structure (e.g. a
charge-weighting that is itself antisymmetric under the same
exchange), and that requirement is now explicit rather than hoped-for.
Related caveat: the helicity in Theorem B is that of an **auxiliary
field on the configuration 3-torus**, not of a physical field in the
ambient space where the link sits — round 1 overstated this as a
physical mutual-energy integral.

**O2 — Compact-quotient neutrality forbids "two like charges alone".**
On a closed manifold `∫Δu = 0` forces total charge zero; the paper
makes this explicit for `S³` (charge density must have average value
zero; the fundamental solution carries the offset `Δϕ = δ − 1/2π²`).
The same applies verbatim on a compact hyperbolic quotient — which is
the QOU fibre. **So the invariant as currently specified — two like
charges, alone, on the compact fibre — is not admissible without a
neutralizing background**, and the Green's function acquires a
`−1/vol(M)` offset. This is a genuine constraint on the *statement* of
the open problem, not merely on its solution: the pp-pair energy must
be defined relative to the neutralizing background (equivalently, only
charge-neutral combinations are well-posed), which is physically
sensible (the nucleus is neutral overall) but changes what must be
computed.

### What survives, sharpened

- **The hyperbolic Coulomb kernel is real and is the right object**:
  the `H³` Laplacian Green's function is `ϕ₀(α) = −coth(α)/4π`
  (Thm 1(3), Thm 2(3), p. 19) — the exact hyperbolic analogue of
  `1/r`. Its behaviour matters for the gate: `coth α → 1/α` as
  `α → 0` (Euclidean limit recovered) but `coth α → 1` as `α → ∞`,
  so the *potential saturates* at a nonzero constant while the *field*
  decays like `1/sinh²α`. A repulsion energy built from it therefore
  does **not** vanish at large separation — which bears directly on
  whether a monotone κ(A) falling 3.2 → 2.1–2.3 is attainable.
- **Well-definedness is confirmed exactly in our regime**: when the
  pairwise linkings all vanish (Brunnian — the baryon case), the
  Pontryagin/Hopf invariant is an **absolute integer** (the
  mod-2·gcd ambiguity degenerates), so μ = ν/2 is unambiguous. Good
  news for any construction that does use μ.
- **Gate-relevant negative**: `Lk` itself is an *integer topological*
  invariant, so it cannot supply a smooth κ(A). Any A-dependence must
  come from the **geometry** — the `coth α` kernel evaluated on the
  actual configuration — before it is closed up into a linking number.
  The only volume-dependent quantity in the paper is an upper bound
  `N(R) = sinh R ~ √vol` (Thm 7), not an interaction energy.

### Absent everywhere (do not go looking again)

No interaction-energy / mutual-inductance double integral; no explicit
point-charge formula (only the recipe `E(ρ) = ∇∫ρϕ₀`); no `H³` Green's
*operator* on vector fields (Thm 3 is `S³`-only); no Euclidean `R³`
triple-linking formula (explicitly conceded — the non-compact isometry
group obstructs it); no hyperbolic third-order formula; no
compact-quotient or deck-sum theory; no Freedman–He-style energy bound
(Arnol'd–Khesin is quoted as an *open dream*).

## Next attack step

The route is now: **geometry-first, not topology-first.** Build the
pp-pair energy from the `coth α` kernel evaluated on the configuration
(relative to the neutralizing background per O2), and let κ(A) come
from hyperbolic separation — checking against the saturation behaviour
noted above. The Milnor/triple-linking route is *not* dead but is
blocked at O1: it needs an antisymmetry-breaking charge weighting
before it can yield a symmetric pair energy. The Komendarczyk
third-order-helicity papers (CMP 291 (2009); JMP 51 (2010)) remain the
only cited source that might carry an actual energy bound for
Borromean flux tubes, and remain un-uploaded.
