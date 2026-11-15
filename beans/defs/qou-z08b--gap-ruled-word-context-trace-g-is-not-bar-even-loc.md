---
# qou-z08b
title: 'GAP: ruled-word context trace g is not bar-even; locate the bar-breaking part of nuc11_interleaved structurally'
status: todo
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
