# Colour: bringing the viewpoints together (2026-11-22)

Synthesis of the session's colour probes (issue #9096; PRs #9059, #9095, #9097).
Every result below is exact, pre-registered, and selects nothing. The gluon is
still open. No ruling is changed by this document.

Rulings in force: photon `γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹`; electron `σ₀σ₁σ₀`
with Hopf closure (trefoil backup); up quark an unknot strand; convention D
(`z_D = q³/(q²+1)`) canonical.

## 1. Where the viewpoints agree

| Viewpoint | Point of contact with our framework | Probe |
|---|---|---|
| Gresnigt (Clifford braids, ℂ and ℍ) | His braid rep is **H_n(q) at q = ζ₈** after σ ↦ iσ; its trace is **convention D at ζ₈** (z = i/√2 = z_D(ζ₈)); weights (0,1,0) on H₃ | `qcd_gresnigt_hecke` |
| Bilson-Thompson helons | The helon fermion braid is **σ₀σ₁⁻¹, the photon's fourth term**; tr_D(σ₀σ₁⁻¹) = q²/(q²+1)² is the φ₀₁ coefficient (flagged coincidence) | `qcd_helon_battery` |
| Chester–Arsiwalla–Kauffman | σ₀σ₁⁻¹ is one of their four CPT-invariant two-crossing helon words; their twist lattice **is the gl₃ weight map**, Q = centre/3 | `qcd_chirality_psl2z`, `qcd_weight_lattice_map` |
| Turaev / Wenzl twisted traces | The rank-2 colour twist gives z_D and, at n = 2, 3, **exactly D's weights** (y₍₁³₎ = 0) | `ColourTwistMarkov.lean` (sorry-free) |

So all three helon/octonion programmes meet ours at the same two objects: the
chiral vertex σ₀σ₁⁻¹ and the convention-D trace. They differ in where q sits:
Gresnigt at one root of unity, CAK at the group level (no q), ours at formal q.

## 2. Where they conflict

1. **Electron.** Helon/CAK electron: one closed component, writhe 0 (σ₀σ₁⁻¹ or
   σ₀⁻¹σ₁ with twists). Ours: σ₀σ₁σ₀, Hopf link, writhe 3. Different braids.
2. **Charge.** Twist charge T/3 ≠ crossing charge for every charged helon
   (all helon braids have writhe 0).
3. **The up-quark / colour / charge triple** (`qcd_weight_lattice_map`). These
   three cannot all hold with colour-singlet hadrons:
   (i) up quark = one strand, (ii) colour = position label, (iii) Q = T/3 per strand.
   One-strand u needs twist 2, which lands in the colour **6**; uud on three
   positioned strands has Q = 1 but is not a singlet.
4. **Position colour is end-dependent.** The helon 3-cycle permutes positions,
   so a quark's colour differs between top and bottom (scope b).
5. **Bring's handles ≠ 1, i, j, k.** H¹(Bring) = 2 × (4-dim A₅ irrep): no
   trivial and no 3-dim summand (scope b). Only H¹ ≅ ℂ⊗ℍ as a module survives.

## 3. Colour carried by the strand: the map of routes

| Route | Colour moves with strand at generic q? | Price |
|---|---|---|
| K0 position colour | No (position label) | End-dependent under the helon 3-cycle |
| K4 / colour+spin on ℂ³⊗flavour (Hopf action on colour alone) | Forces q² = 1 | Excluded in tested classes (scope a) |
| Letzter coideals AI, AIII on ℂ³ | — | Not colour: so₃ / gl₂⊕gl₁ (scope b, dimension) |
| **(gl₆, gl₃⊕gl₃) coideal on ℂ³⊗ℂ²** | **Yes**; U_q(sl₃) relations hold n ≤ 3; gl₃⊗1 at q = 1 | Colour action depends on flavour at q ≠ 1; singlets carry the fermionic trace, not z_D |
| Oriented strand (walled Brauer, 3̄ = reversed ℂ³) | Yes | A second strand type; octonions not needed |
| G₂ strand (Im 𝕆) | Classically yes, but trivially (the braid is O(7)-invariant); at q ≠ 1 no colour su(3) Hopf subalgebra of U_q(g₂) exists | Second Hecke parameter q′, q′ + 1/q′ = dim_q V₇; see `2026-11-22-g2-colour-strand-map.md` |
| Furey ideal ℂ⁸ with gl₈ braiding | No (single su(3) needs q = 1) | — |

In every route the gluon is a **channel** (e.g. the octet projector on V⊗V*),
not a word in σ.

## 4. The one structural fact the routes share

For any sl₃ ⊗ 1 colour transported with the strand, at q = 1 the braid is
P_c ⊗ P_f. The only colour singlet in V^⊗3 is ε, on which P_c = −1, so on the
singlet sector σ ↦ −P_f: **colour singlets are flavour-antisymmetric in the braid
sense, carrying z = z_D(−q⁻¹) = −1/(q(q²+1))**. This is the S₃ sign
(scope b, argument written, not in Lean). Physically this is the usual statement
that the colour wavefunction of a baryon is antisymmetric. It is also why
convention D, which kills the (1³) block, cannot see colour singlets.

## 5. Decisions for the owner

### D1. Must colour singlets carry the convention-D trace (acceptance test (d))?

- **Keep (d).** Meaning: hadron traces are D traces. Cost: none now. Risk:
  every colour that travels with the strand is excluded by §4, so colour stays a
  position label (K0) and the end-dependence of §2.4 must be lived with.
  Commits to: colour is never dynamical on the strand.
- **Replace (d) by "singlets carry the transported trace z_D(−q⁻¹)".** Meaning:
  accept that baryons see the fermionic (sign) channel. Cost: re-score the
  colour probes (cheap, all exact). Risk: two Markov parameters in the hadron
  sector; D's statement "three-row blocks vanish" must be scoped to the
  colour-blind flavour sector. Commits to: the gl₆ coideal (or the oriented
  strand) as the colour carrier.
- **Drop (d) as a colour test.** Meaning: D governs the flavour/decay channel
  only (as its 2026-09-08 scope already says). Cost and risk as above, lighter.

**Recommendation (judgement):** the third. D was ruled for the decay channel; §4
shows asking it of colour singlets contradicts any transported colour.
**Default:** nothing changes; (d) stays in the acceptance list and the gl₆
coideal is recorded as failing it.

### D2. Which colour-carrier strand to develop next (only if D1 is not "keep")?

- **gl₆ coideal on colour ⊗ flavour.** Only route at the substrate q with no new
  strand type. Next step: relations for n ≥ 4, Lean for the §4 sign argument.
- **Oriented strand.** Cleanest algebra (walled Brauer); needs 3̄ as reversed
  strand, which the corpus does not yet have.
- **G₂ at q′.** The octonions enter through the trivalent vertex (3-form), not through the braid (see `2026-11-22-g2-colour-strand-map.md`); needs a second algebra
  H(q′) and an account of how it couples to the photon's H₃(q).

**Recommendation (judgement):** gl₆ coideal first, oriented strand as its
cross-check. **Default:** no new work.

### D3. The up-quark / colour / charge triple (§2.3)

One of (i)–(iii) must give. Options: up quark as a multi-strand object (the
helon reading); charge as a tube/flavour label rather than per-strand twist;
colour carried on the tube. **No recommendation yet**: this touches the
up-quark ruling and needs the D1 answer first. **Default:** the conflict stays
recorded in `qcd_weight_lattice_map/RESULT.md`.

## Not established

General-n weights (Lean stops at n = 3; Ocneanu uniqueness cited); gl₆ coideal
relations for n ≥ 4; the §4 sign argument in Lean; any gluon.
