---
# qou-d7h1
title: 'GAP: Eightfold Way flavor SU(3) from QOU components — distinguish from colour SU(3), then derive octet/decuplet organization'
status: in-progress
type: task
priority: normal
created_at: 2026-08-02T17:29:24Z
updated_at: 2026-08-02T17:30:46Z
parent: qou-a0gr
---

Near term: inventory the existing I3/Q/Y, strange-quark, and three-strand colour ingredients; prove the corpus already has the right state labels for u,d,s-level organization.

Medium term: build a flavor-SU(3) candidate action on the hadron state space and test baryon-octet / meson-octet / decuplet decomposition without conflating it with the colour module.

Long term: connect the flavor action, if it exists, to the Bring/icosahedral side (A5 / S5 / W-plane geometry) as a derivation route rather than a one-number analogy.
2026-08-02 concrete inventory.

- `sm-gauge-truncation.md` already separates the three roles cleanly: `Q` is derived, `I_3` is matched by the writhe ladder on the nucleon doublet, and `Y` remains open because proton and neutron share `Y=+1` while their writhes differ.
- `strand-twist-datum.md` gives the best current candidate for the missing second invariant: twist is independent of writhe, and the candidate hypercharge is `Y_t = 2(Q_twist - I_3)`, but only as a battery candidate.
- `strangelet-crossing-energy-proof.md` and `strangelet-intro.md` already carry usable flavor labels: `d = T_{2,3}^σ`, `s = T_{2,5}^σ`, and baryonic `(u,d,s)` units use the `{+,-,-}` charge partition.
- Colour SU(3) is partially closed elsewhere: `sm-colour-stabilizer-action` plus `OctonionColourActionBaseModule.lean` already realize the abstract colour-action class on `O = C ⊕ C^3`; the open piece there is the action on QOU's own Hecke three-strand state space.

- There is already a q=1 SU(3) symmetry anchor in the corpus: completed bean `1ict` resolved that Elliott SU(3) sits at the q=1 corner of the existing Schur-Weyl / Wedderburn shell picture, via mutual centralizers on `(ℂ^3)^{⊗ n}`. So the flavor route is not starting from zero representation theory.
- There is also already a baryon-label precursor table: `predicted-spectra/linking-relations-table-table3-data.md` lists `p,n,\Lambda,\Sigma^\pm,\Xi^0,\Xi^-,\Omega^-` as Borromean `(u,d,s)` triples. But this is NOT yet an Eightfold-Way derivation: it mixes octet and decuplet content (`\Omega^-` is decuplet) and omits the full weight-multiplet organization (e.g. `\Sigma^0`, meson octet, decuplet structure).

- Gap list after corpus grep: no relevant `meson octet`, `baryon octet`, `decuplet`, or `weight diagram` layer is present in the content tree, and the existing baryon-label table does not yet include a `\Sigma^0` row. So the corpus currently has state labels and one q=1 SU(3) anchor, but not the Eightfold-Way multiplet geometry itself.

## Owner re-ask (2026-08-02): "missing 8-fold way. categorical?"

Yes — the tracked route IS categorical, and it is this bean. The
Eightfold Way should fall out of the **q=1 corner of the existing
Schur–Weyl / Wedderburn shell picture** (Elliott SU(3), bean `1ict`):
mutual centralizers on $(\mathbb{C}^3)^{\otimes n}$ give the flavor
SU(3) multiplets categorically, with the octet/decuplet split being the
Wedderburn block decomposition of $(u,d,s)$ Borromean triples. The one
missing categorical piece is the **weight-multiplet geometry** (octet vs
decuplet organisation, the $\Sigma^0$ row, meson octet) — NOT the SU(3)
representation theory, which is already anchored at q=1. Owner's
"icosahedral embedding on Bring's surface" hint is the geometric handle:
the $A_5\cong$ icosahedral / Bring-Jacobian $E^4$ structure is where the
flavor weight lattice should sit. Session: `qou-ywj9`.

## Colour-level measurement + the code-vs-Lean question (PR #5241, 2026-08-16)

Commissioned to re-open what PR #5234 closed on one measurement. Full writeup:
docs/audits/2026-08-16-colour-level-and-tln-compute.md (TASK 1).

**#5234's measurement CONFIRMED, independently.** Symbolically over Q(q),
z_2 = q^3/(q^2+1) exactly, so convention D IS level r=2. All 11 production
colour/strong paths resolve to that one z (closed_form_tau_M.markov_z,
hecke_symbolic.z_markov, pyhecke/gram.py:175 + :437, hecke-engine gram.rs:125,
color_weight.rs; the rest inherit). The color_tube_*.py family (8 files) uses
no z at all -- they build the 9-element colour-pair weight tensor W.
z_C solves z_r = z_C at r = 2.5995 (no integer). **z_3 appears NOWHERE outside
one probe** (ocneanu_param_from_fibre_dimension.py, nothing imports it) and one
audit comparison table.
Grep warning: the literal 0.44930482320583087 in many witnesses is h_q, NOT
z_3 (0.449304809090...) -- they differ at the 8th decimal.

**bring_color_weighted implies NO level.** It is a per-bond scalar over the
A-1 nearest-neighbour bonds: p-p -> z, n-n -> z-h, p-n -> z-h(1/2-delta/4).
It CONSUMES z and never defines, derives or constrains it; no representation,
no fibre object, no row cap anywhere in it. So its canonicity under owner
ruling R3 says nothing about the level.

**The code-vs-Lean tension: THERE IS NONE — they are about different
objects.** Two things the cited line does not show on its own:
  1. FibreDimensionForcesTL.lean:69-71 is a PROSE REMARK inside a module
     docstring, under a heading literally titled "What this does NOT
     establish". Nothing below it formalizes the claim. The formalized content
     is entirely about the mass channel (ocneanu_param_eq_of_fibre_qdim,
     twoDimFibre_pins_h3_weights). So it is not "the Lean says colour needs
     three rows" — a comment says it.
  2. Production has no colour fibre at all (see bring_color_weighted above).
So the Lean remark correctly describes a not-yet-constructed object, and the
code correctly implements a different, weaker thing. Neither "code is wrong"
nor "Lean is aspirational" is right.

**Eightfold line: the numerological inference is DEAD; a structural test is
not.** "Level 3 is SU(3) and colour is SU(3)" stays unsound — the Wenzl tower
contains every SU(r). z_3's absence from production removes even the weak
circumstantial version.
BUT: ocneanu_param_eq_of_fibre_qdim is proved GENERAL IN N, not just N=2:
dim_q V = [N]_q  =>  z.[N]_q = q^N. So a genuine 3-dimensional colour fibre
would FORCE z = q^3/[3]_q = z_3, with no freedom and no fitting. The live test
is therefore:
  [ ] Construct a functor with a 3-dim fibre that actually realizes colour
      antisymmetry (the three-row block). This is the whole difficulty and
      nothing in the corpus does it.
  [ ] Its Markov parameter is then z_3 BY THE ALREADY-PROVED THEOREM.
  [ ] Check whether that functor reproduces colour phenomenology.
NUMEROLOGY FLAG ON THIS ENTRY: the above is a statement of what evidence WOULD
look like, not evidence. If it is later cited as support for the eightfold
line without step 1 being done, that citation is the error.
Scope (a): unsupported as stated, usual argument invalid; NOT structurally
excluded, and I have no invariant that would exclude it.
