---
# qou-z08b
title: 'GAP: ruled-word context trace g is not bar-even; locate the bar-breaking part of nuc11_interleaved structurally'
status: in-progress
type: task
created_at: 2026-11-15T09:59:54Z
updated_at: 2026-11-15T11:30:00Z
parent: qou-qs0e
---

f = tr^{z_D}(n - p) = h*g exactly, g = -(T1+T2)/2 the trace of the two context words left when the two n-p letter differences (each -h/2) are removed. Since tr_{z_D} intertwines bar with q->1/q (derived: iff z(q)-z(1/q)=h; Ocneanu uniqueness), f is bar-odd iff g is bar-even. Measured: g_odd = -h[2]_q(q^2+q^-2)/8, a short closed form. Bar maps U<->D and fixes UD, so the CORE alternation and the gluon pair (both positive letters) are not bar-fixed. Open: derive which part of the word produces g_odd. Do NOT test replacement words to make g bar-even (selection against target; the element is ruled by qou-ales / qou-99qc).

## 2026-11-15 append (word-dependent maps; session_01Qmmkt6YA78a79y4cG3D5Pk, fork)

Owner asks: "Search for word-dependent maps", "try Derive the right isospin involution".
Audit docs/audits/2026-11-15-word-dependent-isospin-maps.md; probe
qbeta_word_dependent_isospin_maps_probe.py (6/6, exact; no witness, no Q_beta value).
- Element-level symmetries (#7862): no composite of {bar, rev, swap, chi} maps n -> +/-p.
  Bar breaks at the core, the gluon and the tail placement independently.
- Flavour-only maps (6 actions on the 3 tail slots, 216 maps): 0 element hits, 0 trace hits.
- Slot-dependent maps over all 11 slots (all 6^11 = 362,797,056, by MITM, exact re-check):
  0 element hits. 1,296 trace hits (256 distinct image words). Every one rewrites 10-11 of
  11 letters, the core included, and none is uniform per generator, so none descends to H_3.
  These are word coincidences, not isospin.
- Inner conjugation can never map n to p: the trace is a class function and
  tr(n) != tr(p) exactly. Scope (b).
- (2,1)-block module map: the forced T = rho(n)rho(p)^-1 commutes with neither rho(core) nor
  rho(gluon). Scope (b) for left multiplication on the block; scope (a) for state vectors.
- Side result: tr^{z_D}(core) IS bar-even, tr(gluon) is not. So at trace level the core is
  not where the bar-breaking lives; the trace is not multiplicative, so this is a lead only.
- Literature (held): Lusztig involutions via Geck (rev, dagger = swap), hdr bar, inner
  automorphisms. All act uniformly on generators. No Aut(H_n) classification is held.
  Furey's isospin (thesis s7.3) is inner conjugation acting on a right ideal, made left-only
  by the idempotent eps. Owner decision D-I1 (state/ideal formulation) is in audit s9.


2026-11-15 localisation done (PR #7860, a45ef59d2, probe R5): quark tail contributes exactly 0 (alone and in all cross terms); g_odd = core term K + gluon term + core x gluon cross term (-2K); tr(core) alone bar-even; context without gluon pair bar-even. Obstruction needs the gluon pair, which is census-derived (not gamma-gamma-ruled). Stays todo: why the gluon pair breaks bar-evenness is not derived; links to qou-99qc element question. No word changed.

## 2026-11-15 append (D-I1 = A result; thread "Test isospin as a module map")

Probe qbeta_isospin_module_map_probe.py, 11/11, exact over Q(q); audit section 11.
- P+ H3 P+ is 2-dim and commutative (g = 0, 1): no corner sl2 at n = 3 (Wedderburn).
- Centraliser of {core, gluon} in H3 = the centre (dim 3), so a core/gluon-commuting isospin acts by scalars on H3.P+.
- 14 fixed candidates x 20 state pairs x 2 idempotents: 0 of 560 map psi_p to psi_n, exactly or up to scalar. No candidate commutes with the core.
- Centraliser solve: 4 of 40 settings hit, all degenerate: psi_n = q^-2 psi_p (sigma0 u/d letters cancel; P+(sigma1) absorbs the last letter's flavour as an eigenvalue). None with the gluon.
- Next: n >= 4 only, gated on Stream 11's corner-multiplicity = flavour check (#7867).

## 2026-11-15 — γγ-built nucleon (PR #7741, `h2_gg_atom/`, `h2_gg_electron/`; owner decision C)

On three strands every γγ word is a power of V = σ₀σ₁⁻¹, so a γγ-built nucleon is V^m. Pre-registered and measured: only V³ and V⁶ pass reading 3 at every level (m = 3…7); proton and neutron are then the same word, so there is no flavour on three strands. With a γγ electron (V³ or V⁶) H₂ passes every level and the only passing bond is V³. Every γγ word has χ_(1³) = 1 (#7896). Scope (a). Bearing on this bean: the γγ nucleon V^m has no census gluon pair, so the bar-breaking part identified here is absent from it (V^m bar-evenness not separately checked).
