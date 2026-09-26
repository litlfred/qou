---
# qou-7r6d
title: 'Session: dark-matter / antimatter-domain feasibility (gamma-gamma C-symmetry, QOU cosmology)'
status: todo
type: milestone
priority: normal
created_at: 2026-09-07T11:50:19Z
updated_at: 2026-09-07T12:03:24Z
---

## Session findings (2026-09-07) — chat-only delivery, no paper content written

Owner asked: can missing dark matter be explained via QOU gamma-gamma production
yielding antiparticles, with some visible galaxies being antimatter entirely
(we see only photonic emission), in a local neighbourhood that minimally
intersects matter?

### Verdict per leg

- **"Only photonic emission" — correct premise, not the weak link.** Photon is
  self-conjugate; ALPHA measured antihydrogen 1S-2S agreeing with hydrogen to
  2e-12. Spectroscopy genuinely cannot distinguish. But this is the standard
  MOTIVATION of the antimatter-domain literature, not a gap in it, and a
  *visible* galaxy is already in the luminous budget.
- **Antimatter as dark matter — category error.** Five independent fatal
  reasons: (1) it is luminous, which is the premise; (2) budget — Planck 2018
  gives Omega_c/Omega_b = 5.364, so DM-from-antibaryons needs a 5.36:1
  antimatter EXCESS, while gamma-gamma is C-symmetric and can only deliver
  1:1; a symmetric universe gives 2*Omega_b = 0.0986 vs required 0.3138,
  short by 3.18x; (3) Bullet Cluster — DM is offset from the collisional gas,
  antimatter plasma is not; (4) antibaryons are photon-coupled pre-recombination
  so cannot grow structure; (5) CMB counts total (b + bbar), BBN counts net,
  and they agree to ~3% where a 50/50 domain universe needs ratio 2.0.
- **Local antimatter neighbourhood — directly excluded.** Cohen-De Rujula-Glashow
  ApJ 495, 539 (1998): domain-boundary annihilation over-produces the MeV
  diffuse background unless domains are >~ 1 Gpc. Independently, SN 1987A gave
  ANTINEUTRINOS via inverse beta decay in Kamiokande-II/IMB, so the LMC is
  matter by direct lepton-number measurement, not by light.

### QOU offers no evasion

CDG98 is escaped only if boundary annihilation is suppressed.
`rem:time-reversal-energy-barrier` gives E_flip = +inf, but that barrier is on
CONVERSION (knot -> mirror), not annihilation; the block itself says the open
channel is pair creation at 2m_e. `prop:crossing-energy-pair-cancellation`
(Lean `QOU.Braiding.pair_cancellation`) gives a positive residue read as the
Coulomb attraction separating a created pair — that PROMOTES annihilation.

### CPT check (the substantive measurement)

`prop:antiparticle-crossing-reversal` has a sorry-free, axiom-free Lean sibling
whose claim 4 `bare_mass_invariance` proves
`mirror.pos + mirror.neg = pos + neg` by `omega` — a CROSSING-COUNT identity,
not the mass. Its docstring bridges to mass via "hence the knot type and its
hyperbolic volume", and that implication is FALSE in general: 5_1 (torus,
Vol 0) and 5_2 (hyperbolic, Vol ~ 2.8281) share crossing number 5.

The conclusion holds for a better, unstated reason: Vol(K^sigma) = Vol(K)
because the mirror is an orientation-reversing isometry of the complement and
hyperbolic volume is unsigned (Mostow).

Density leg measured at 50 dps, proton pin q0 = 1.1099785827513808:
  h = q - 1/q = 0.20906029879563930168        (BAR-ODD)
  chi^(2,1)(pi+) = -(h^2+1) = -1.04370620853  at q0
                            = -1.04370620853  at 1/q0   -> exactly equal
So rho is mirror-invariant HERE because the character is built from h^2, an
even power. That is a measured fact about this character, not a theorem about
densities. Contrast the crossing-energy channel for the trefoil:
E(K) = 3.32993574825, E(K^sigma) = -2.70275485187, difference 6.03269060012.

VERDICT: CPT is not broken and not proved. Two cheap repairs — (a) replace the
crossing-count proxy with a real Vol(mirror) = Vol lemma citing the
orientation-reversing isometry; (b) state that mass-invariance rides on the
bar-parity of the density and check it is structural not accidental.

### The finding that outranks the original question

`prop:c-equals-bar-iff-all-1dim` (sorry-free) proves C = bar iff every irrep is
1-dimensional: true at H_2 (leptons), FALSE at H_3+ (mesons, baryons). Corpus
witness: chi^(2,1)(pi+) = -1.044, bar-image -1.044 (invariant), C-image +1.892
— ratio -1.813.

`def:breit-wheeler-pair-production` builds gamma_1 * gamma_2 = NF(e-) + NF(e+)
with e- = s0 s1 s0 and e+ = s0^-1 s1^-1 s0^-1, i.e. a word plus its bar-image.
So QOU pair production is BAR-equivariant by construction. But baryon number
cares about C, and C != bar exactly where baryons live. Therefore
bar-symmetric production does NOT imply C-symmetric production in the baryon
sector, and a baryon asymmetry could enter at H_3 without any cosmological
regime — contradicting `sec:cp-violation-evidence`'s stated expectation that
"cosmological regimes must provide the required enhancement".

AGENT JUDGEMENT, NOT A FINDING: not checked whether the C-vs-bar gap has the
right size or sign. The chi ratio -1.813 is O(1); baryogenesis needs 6e-10, so
the naive magnitude is wildly wrong and the real question is what suppresses it.

Second, related tension: `prop:antiparticle-crossing-reversal` claim 1 says the
MIRROR defines the antiparticle; `prop:c-equals-bar-iff-all-1dim` proves mirror
!= C for baryons. Both sorry-free. The antiproton is one or the other.

### Corpus-state facts established this session

- Library holds ZERO sources on antimatter cosmology or dark-matter
  phenomenology (no CDG98, Steigman, Alfven-Klein, AMS-02) — checked across
  INDEX.md, sections/, ocr/ and uploads/ on 14 spellings.
- ZERO cosmological witnesses in computations/. The categorical cosmology layer
  (CCC, aeons, CMB functor) is prose + Lean scaffold with no compute.
- The QOU photon is NOT the unknot: it is the trivial HECKE representation
  1 = T_e; the unknot 0_1 = T_{1,0} is the NEUTRINO.
- Two Lean decls share the name `QOU.Torsion.antiparticle_crossing_reversal` —
  one real and unconditional, one a self-assuming class projection. Cite the
  file path, not the decl name.
- `prop:qou-is-ccc` is stronger in its .md than in its Lean: CCC-2 (CMB
  inheritance across the aeon boundary) is explicitly unformalised.

### Caveats on this session's own evidence

- corpus_search (grep-path 0, the vocabulary-independent one) DID NOT RUN —
  the paper-assistant MCP server failed to connect (ENOENT). All negatives above
  are grep-shaped: "these spellings, on these surfaces", not graph negatives.
- q_parameter would not import (bare container, no numpy), so the proton pin was
  hardcoded from AGENTS.md. The bar-parity result does not depend on the value:
  h is bar-odd algebraically, so h^2 is bar-even for any q.
- Cosmological figures (CDG98 1 Gpc, Steigman <~1e-6, FIRAS mu/y, cosmic
  birefringence 0.34 +/- 0.09 deg) are RECALLED literature, not measured here,
  and the library holds none of those papers to check against.

### Open follow-ups (none claimed)

1. Settle whether the antiparticle is mirror or C in the baryon sector.
2. Replace `bare_mass_invariance`'s crossing-count proxy with a Vol(mirror) lemma.
3. Check whether density bar-parity is structural or accidental.
4. Is the gamma-gamma production functor C-equivariant (not merely bar-equivariant)?
