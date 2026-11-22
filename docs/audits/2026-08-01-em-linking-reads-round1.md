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

## Round 3 — Komendarczyk + Cantarella–DeTurck–Gluck: the decisive distinction

Two further reads settle *why* every topological route fails, and
confirm which object the invariant actually is.

### The distinction that organises everything

There are **two different bilinear pairings** of two current
distributions, and conflating them is the trap:

| pairing | kernel | character | value for two unlinked, separated tubes |
|---|---|---|---|
| `⟨V₁, BS(V₂)⟩ = ∫J₁·B₂` | `(y−x)/|y−x|³` | **topological** — mutual helicity / linking number, sign-changing | **zero** |
| `⟨A₁, J₂⟩ = ∫A₁·J₂` | `1/|y−x|` (in H³: `−coth α/4π`) | **metric** — Coulomb-like, monotone in separation | **nonzero, positive** |

A like-charge repulsion energy is the **second**. The Brunnian
condition sets every *first*-type pairing to zero by hypothesis — which
is precisely why no topological construction can supply the invariant.
Cantarella–DeTurck–Gluck define the vector potential `A(V)` (eq. 3.1)
but **never form** `⟨A₁, J₂⟩`; DeTurck–Gluck give the H³ kernels but no
energy formula. **The object we need is in neither paper and must be
derived** — but the correct kernel for it is exactly the scalar
Green's function `φ₀ = −coth(α)/4π`, which is what the geometry-first
probe uses.

### What Komendarczyk settles (arXiv:0808.1533, `[komendarczyk2008]`, read in full)

- **An energy bound does exist** — Theorem 6.1: `|H₁₂₃(X;𝒯)| ≤ C_𝒯 ·
  E₂(X)^{3/2}`, i.e. `E₂ ≥ (|H₁₂₃|/C_𝒯)^{2/3}`, for volume-preserving
  fields on invariant unlinked handlebodies (the Borromean flux-tube
  configuration is treated explicitly, Fig. 5).
- **But it is not the Arnol'd–Khesin bound and not usable here.** The
  author states plainly that `C_𝒯` is *geometric, not topological*, and
  that the estimate "is meaningless when the handlebodies get close"
  — it degrades exactly in the regime of interest, and both of its
  geometric factors move the wrong way (the `ω` factor blows up with
  *proximity*; the Neumann eigenvalue weakens the bound as the domain
  grows).
- **O1 is not overcome — it is proved.** Remark 2.6 derives the total
  antisymmetry outright; every constructed quantity is a triple
  integral over `T₁×T₂×T₃`. The *only* pair-indexed object in the paper
  (Cor. 2.5, `deg(F^{kl}) = lk(L_k,L_l)`) is forced to **zero** by the
  unlinked hypothesis (Lemma 4.2).
- **A third, independent scaling obstruction**: `H₁₂₃ ~ Flux³`, so any
  per-component energy derived from it scales as flux-cubed, whereas a
  Coulomb-like pair repulsion requires **flux-squared**. The
  dimensional shape is wrong regardless of the other two problems.
- **O2 reappears** as the non-existence of a global potential `α_ω` on
  `Conf(S³,3)` (Rems. 4.1, 4.4) — the reason the theory lives on
  sub-domains and cannot be globalised.

### What Cantarella–DeTurck–Gluck contributes (usable)

- **`BS` is self-adjoint** (Theorem D): `⟨V₁, BS(V₂)⟩ = ⟨BS(V₁), V₂⟩`,
  with minimal hypotheses (merely smooth fields on a compact domain;
  two tubes are handled as a two-component domain). The proof is *pure
  kernel antisymmetry*, so it should port to H³ given the
  DeTurck–Gluck kernels. **A symmetric pairing is exactly what a
  per-pair quantity needs** — the antisymmetry problem is specific to
  the *third-order* invariant, not to second-order pairings.
- **Consequent per-pair decomposition** (one line from `H = ⟨V,BS(V)⟩`
  plus self-adjointness; *not* stated in the paper): `H(ΣVᵢ) = Σᵢ
  H(Vᵢ) + 2 Σ_{i<j} ⟨Vᵢ, BS(Vⱼ)⟩`. So helicity *does* split into
  self-terms plus symmetric pair terms — but those pair terms are the
  topological ones, hence zero in the Brunnian case. Consistent with
  everything above.
- **The one geometric size functional**: `‖BS‖ ≤ OS(V)/4π` with
  "optical size" `OS(V) = max_y ∫_V |y−x|^{-2}` — a domain functional
  with dimensions of length, and the only place in this literature
  where an A-dependence could enter an operator norm.
- R³-only throughout; the self-adjointness mechanism is the portable
  part.

### Net verdict on the attack

All three topological routes are now closed with reasons on record —
antisymmetry (proved), flux-cubed scaling (dimensional), and
Brunnian-vanishing of every pairwise topological term (by hypothesis).
The surviving route is the **metric Coulomb pairing** `⟨A₁, J₂⟩` built
on the hyperbolic scalar Green's function, which no paper supplies and
which must therefore be derived. The first quantitative test of that
route is `em-linking-coth-separation.witness.json` (bean `qou-zp6a`):
consistent, monotone as required, but **not yet distinguished** from a
generic reciprocal law — the discriminating measurement is heavier
mirror pairs (bean `qou-i6rg`).

## Round 4 — Khesin + Hornig–Mayer: the route around O1, and a convergence

### O1 is now *explained*, not merely observed

Khesin Rmk 4.8 (p. 1003) gives the structural reason: a linking-type
form is **symmetric or antisymmetric according to the parity of the
product of the codimensions**. In 3D the potentials are **1-forms**, so
`α₁∧α₂∧α₃` anticommutes and the triple invariant is forced
antisymmetric; the analogous invariant built from **2-forms** on
`M^{2k−1}` *is* symmetric (p. 1003). So O1 is a form-degree-parity
fact, not an accident of one construction — and Hornig–Mayer
(`[hornig-mayer2002]`) confirm it
independently from the physics side, naming it outright (p. 11):
*"the antisymmetry of `H⁽³⁾` seems to be one of the key problems."*

### The route around O1: use an UNSIGNED quantity

Khesin Rmk 3.4 (p. 995) diagnoses exactly why signed invariants fail
here — helicity bounds **cancel** between oppositely-linked pairs, so
what is needed is an estimate *"where the contribution of any
nontrivially linked tube could not be canceled out."* That points at a
**norm**, and Rmk 3.5 names it: the **Freedman–He asymptotic crossing
number** — the Gauss integral with the **absolute value** of the
numerator, minimised over homotopies.

This is the first object surfaced in the whole literature sweep that
clears every obstruction at once:

| requirement | asymptotic crossing number |
|---|---|
| symmetric in the pair | **yes** — it is a norm, `C(1,2) = C(2,1) ≥ 0`, and cannot be antisymmetrised (routes around O1) |
| nonzero when `lk = 0` | **yes** — unsigned, so Brunnian vanishing does not apply |
| Flux² scaling (Coulomb-like) | **yes** — vs the fatal Flux³ of third-order helicity |
| geometric, A-dependent factor | **yes** — see the convergence below |

Khesin Thm 3.6 (Freedman–He) gives the associated energy bound with an
explicit geometric factor:

`∫_T |ξ|² ≥ (16 / (π·Vol(T)))^{1/3} · |Flux_ξ|² · (2·genus(K) − 1)`

**Caveat, stated plainly:** as literally written this is attached to a
*single* knotted tube and its topological factor `2·genus−1` **vanishes
for an unknot** — and the components of a Borromean configuration *are*
unknots, so the inequality itself is vacuous for our tubes. What is
usable is the **`Flux² × Vol^{−1/3}` template** and the crossing-number
machinery behind it, not the stated bound.

### The convergence — and a correction to how I read my own probe

The Freedman–He template says the per-pair energy carries a factor
`Vol^{−1/3}`. Since `Vol ∝ A`, that is `κ ∝ A^{−1/3}` — which is
**exactly the "null: 1/κ" hypothesis** scored in
`em-linking-coth-separation.witness.json` (`1/κ ∝ A^{1/3}`, 6.12%
scatter, statistically tied with H_coth's 5.80%).

**So that "null control" was mis-labelled: it is not a generic
reciprocal law at all — it is the Freedman–He energy template, arrived
at independently.** Two unconnected routes — an empirical scaling test
on the corpus's own κ(A) data, and a 1991 theorem about the energy of
knotted flux tubes — point at the same `Vol^{−1/3}` dependence. That
raises it from "unexplained fit" to "candidate with an independent
structural reason", which is precisely the bar the anti-fit discipline
sets.

It also **sharpens the discriminating test** (bean `qou-i6rg`): the
contest is no longer "hyperbolic kernel vs. arbitrary power law" but
**coth-saturation (κ → 1) vs. Freedman–He `Vol^{−1/3}` (κ → 0)** — two
physically-motivated hypotheses making opposite predictions in heavy
nuclei. The same mirror-pair extension settles it.

### Two references now clearly worth acquiring

1. **Freedman & He**, *Divergence-free fields: energy and asymptotic
   crossing number*, Ann. of Math. **134** (1991) 189–229 — the source
   of the crossing-number energy bound and the `Vol^{−1/3}` template.
2. **Laurence & Stredulinsky**, *Asymptotic Massey products, induced
   currents and Borromean torus links*, J. Math. Phys. **41** (2000)
   3170–3191 — flagged by Khesin (p. 995) as showing the Borromean
   energy **is bounded away from zero**, the one Borromean-specific
   energy result in the literature. Cited by both Khesin and
   Komendarczyk; still un-acquired.

*(Housekeeping: `1992EvansBerger.pdf` is an image-only scan with no
text layer on any page — it needs OCR before it can be read. Its
Berger cross-term content is available second-hand via Hornig–Mayer
Appendix C, where it appears **antisymmetric**, `A¹×F¹ − A³×F³`, so it
does not solve O1 either.)*

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

---

## Round 5 — reading the primary sources properly, and retracting round 4

Round 4 above rested on a reading of the Freedman–He energy bound that
does not survive contact with the primary sources. Two corrections
follow, both cutting against work committed on this branch.

### Correction 1 — `ac` is per-component, so the pair question was malformed

The Freedman–He asymptotic crossing number that appears in the **link**
energy bound is `ac(L_k, L)`: **one component against the whole link.**
Komendarczyk (arXiv:0808.1533v1, eq. 43, p. 26) states it as

`E_{3/2}(X) ≥ (π/16)^{1/4} ( Σ_{k=1}^{n} ac(L_k, L)|Flux(X_k)| ) · min_k |Flux(X_k)|`

The sum runs over the `n` **components**, not the `n(n−1)/2` pairs, and
no pair-indexed `ac(L_i, L_j)` appears anywhere in Khesin or
Komendarczyk. Khesin never writes `ac(·,·)` at all; his Rmk 3.5
"minimising over all homotopies of two given space curves" is a survey
gloss on the **two-curve warm-up**, not a statement of the invariant
used in (43).

So the question `em_linking_borromean_acn_probe.py` was built to settle
— *is the pair minimisation constrained by the third component, or is
the pair an unlink with infimum 0?* — is **malformed**. There is no pair
minimisation. That probe's `ACN_pair = 1.6426` and its "total link"
reading `3 × that = 4.928` are both the wrong object with the wrong sum.

The underlying (a)-vs-(b) question does resolve, and **against (a)**:
Komendarczyk's lower bound is a smallest Seifert genus **in
`ℝ³ ∖ (other components)`**, so Brunnian-ness genuinely holds the value
up — but via a complement constraint on a *single-component* genus, not
via a constrained pair homotopy. Correctly indexed
(`em-linking-fh-link-bound-correction.witness.json`):

`1 ≤ ac(L_k, L) ≤ 3.285` per component;  `3 ≤ Σ_k ac(L_k, L) ≤ 9.856`

with the upper end realisation-dependent at 7.8%. The `genus ≥ 1` step
(from `μ̄₁₂₃ = 1 ≠ 0` obstructing a genus-0 spanning disk in the
complement) is **my inference** — neither source computes it.

### Correction 2 — there is no volume factor, and round 4's "convergence" was a misattribution

Equation (43) carries `(π/16)^{1/4}`, **a pure constant, and no volume
factor.** The `Vol^{−1/3}` this document has been calling "the
Freedman–He template" is from **Khesin Thm 3.6**, which is the bound for
a *single knotted torus* — not the link bound, and not applicable to a
multi-component Borromean configuration.

**Round 4's central claim is therefore retracted.** It said an empirical
`κ ∝ A^{−1/3}` scaling had *converged* with an independent structural
reason from Freedman–He, and that this raised it "from *unexplained fit*
to *candidate with an independent structural reason*, which is precisely
the bar the anti-fit discipline sets." The two routes were never
independent: the second one was a misattribution of a single-torus bound
to a link.

Consequence, in the direction that hurts: **`H_FH_A` and `H_FH_Z` revert
to bare power laws with no literature backing** — exactly the bar they
must clear and now do not. This does **not** make coth-saturation
correct. It removes its rival's warrant, and it happens to point the
same way the residual-drift test already did independently
(`em-linking-residual-structure.witness.json`: `H_coth` residuals
structureless at `r = −0.33`, `H_FH_Z` carrying `r = +0.71`).

### What eq. (43) actually predicts

With a fixed local Borromean configuration the topological factor is
**A-independent** and there is no volume factor, so all A-dependence of
`κ` must be carried by the flux (`E ~ ac · Flux²`). `κ` falls by 2.099
across `A = 3…41`, which would require the per-component flux to fall by
**1.449** over the same range. That is a specific, independently
derivable quantity. It is **not** derived here and nothing is wired —
it is reported so the size of the remaining obligation is visible. The
FH link bound does not explain `κ(A)`; it *relocates* the explanation
into the flux.

### Residual gap

Freedman–He, *Ann. of Math.* **134** (1991) 189–229 is **not** in the
corpus or in `library/` (201 PDFs scanned by title metadata, no match),
so FH's own definition of the minimisation domain for `ac(L_k, L)` is
not directly verified. Both corrections rest on Komendarczyk's statement
of it — unambiguous on both the per-component indexing and the
complement constraint — cross-checked against Khesin Rmk 3.5 and Thm
3.6. Acquiring FH 1991 §*Definition of ac* would close it.

---

## Round 6 — O2 is applied at last, and it excludes the contest's winner

Full record:
[`2026-08-25-em-linking-o2-neutrality-applied-to-kappa-contest.md`](2026-08-25-em-linking-o2-neutrality-applied-to-kappa-contest.md)
(bean `qou-17mq`, opened here on 2026-08-01 and untouched until now).

**O2 had never been applied to anything.** `neutralis*` / `neutraliz*` appears
at four sites corpus-wide, all inside this file, and at zero sites in
`computations/`. O1 shaped every subsequent route; O2 was recorded and left.

Applying it: on a finite-volume quotient the admissible pair kernel is the
*zero-mean* Green's function, and a zero-mean function that is not identically
zero must take both signs. `coth(α)` is strictly positive and monotone, so **no
admissible kernel is a positive saturating function of the separation** — and
saturation (`κ → +1`) is precisely the qualitative feature that separated
`H_coth` from its rivals in the round-5 contest. The unsubtracted kernel is
outside the admissible family.

Re-scoring the same 29-pair series under the admissible family
`coth(α) − c₀`, `c₀ = ⟨coth⟩_M > 1`: scatter rises **monotonically** with
neutralisation (3.505 % at the inadmissible `c₀ = 0`; 11.15 % at the `c₀ = 1`
infinite-volume boundary; 22.32 % at `c₀ = 7.5`), the best admissible member
carries residual structure `r = −0.904` — *more* than the `r = +0.799` that
counted against `H_FH_Z` in `em-linking-residual-structure.witness.json` — and
48 of 140 scanned members predict a `κ` zero-crossing inside the measured
`A ∈ [3, 63]`, where every measured `κ` exceeds 1.

**Net effect on this thread.** Round 5 withdrew the warrant from the two
`H_FH` hypotheses; round 6 removes the remaining one from the admissible
family. No member of that contest carried a live structural warrant when it
was scored, so its ranking is not support for hyperbolic-saturation. The
metric Coulomb pairing `⟨A₁, J₂⟩` survives as the route exactly as round 3
left it — what fails is this parameterisation of it, and the sharpened next
question is the zero-mean Green's function of the actual fibre rather than a
one-term stand-in for it.

**Addendum, same day — the test could not have discriminated either.** A
reachability check computed from the contest's own fitted constants: the series
spans `α ∈ [0.317, 0.873]`, while `coth` comes within 10 % of its limit only at
`α = 1.522`, i.e. **`A = 334`** — past the heaviest known nuclide (`A = 294`).
Saturation is therefore unreachable in any nucleus, so `qou-i6rg`'s *"needs NO
new theory, only more AME data"* is not the situation: more data cannot help.
Over the measured range `coth` agrees with its two-term expansion
`1/α + α/3` to 0.97 % against the 3.505 % scatter, so `H_coth`'s advantage
tracks the curvature term, not saturation; and the two hypotheses' predictions
differ by at most 6.285 % = 1.79 × that scatter. Details, plus an
O2-independent derivation of the same subtraction from the `H³` boundary
condition (`G = −(coth r − 1)/4π` is the decaying Green's function; the
saturating form is the non-decaying choice of the additive constant), in the
addendum to the round-6 record.
