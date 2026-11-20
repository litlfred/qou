---
# qou-wkcd
title: 'Derive weak chirality (doublet L vs singlet R): |q|>1, quaternion sides, literature'
status: in-progress
type: task
priority: normal
tags:
    - quark-state
    - chirality
    - weak
parent: qou-qs0e
blocking:
    - qou-hlx7
created_at: 2026-11-15T13:00:00Z
updated_at: 2026-11-15T21:00:00Z
---

Owner question (relayed by coordinator session_01M5GA1LmsEf8tSMxFjMkmnn, tracker #7735):
"L vs R on singlet vs doublets should be derivable somehow / related? anything in the lit?"
and "does it depend on |q| > 1 vs |q| < 1, or is it derivable from that? Is that the same as
the convention of which crossing carries q in the skein weighting?"

Session: https://claude.ai/code/session_01Qmmkt6RTXyN5gg3AQBGRy7
Branch: claude/weak-chirality-doublet-singlet-2026-11-15

Three routes, each to a derivation or a scoped negative:
1. |q|>1: does the observable regime |q0|>1 select the L line? Is q0>1 forced?
2. Quaternions: left vs right multiplication (Sp(1)_L x Sp(1)_R) as the one-sided source.
3. Literature: Connes-Chamseddine, LR-symmetric / Pati-Salam, SO(10), Furey,
   Bilson-Thompson / Gresnigt, Finkelstein, the Ozma problem.

Starts from #7844 (OneSidedWeakVertex.lean), #7836 (HelicityCommonSource.lean),
#7825 (PolarizationActionHecke / ChiralityPolarizationHopf / PolarizationRealStructure).

## 2026-11-15 result (PR #7855, draft; Lean verified at 6e1e536a9, lean-direct exit 0, sorry-free)

- Route 1: a letter fixes only h; the root relabel q ↦ −q⁻¹ swaps lines and W_L ↔ W_R
  (WeakChiralityRootLabel.lean). "Which crossing carries q" = "which root is q" = L/R.
  Per-letter modulus labelling flips under flavour (scope b, conditional on #7836).
  q0 > 1 is declared, not derived (q-zero-complex-extension.md:11; solvers seed it).
- Owner ruling 2026-11-15: leftLine := eigenline where the positive generator σ has
  |eigenvalue| > 1 (LeftLineDefinition.lean). Derived: label-independent, flavour-blind,
  universal; weakVertex flips flavour on the left line only; = P+ iff |q| > 1; mirror
  swaps; −σ⁻¹ is no braid image (given an index character, cited).
- Route 2: right complex structure ⇒ Sp(1)_left × U(1)_right; conjugation swaps sides;
  left Sp(1) moves Γ_u (QuaternionSidedSymmetry.lean). Weak-isospin identification: scope (a).
- Route 3: no held source derives which side; one-sidedness derived (Connes, Furey,
  SO(10)), label conventional; LR models take v_R > v_L as input.
Open: D-W2 (long-braid limit as mechanism), D-W3 (second singlet space). Audit §4.

## 2026-11-15 owner decisions D1/D2/D3 (coordinator relay) — results, audit §6

- D1 flavour su(2) on leftLine: NEGATIVE inside one letter (scope b; invariant: commutative
  corner, left line 1-dim). u_L, d_L proportional; span{u,d} = L ⊕ R so a flavour sl2 mixes
  lines (same failure as quaternion Sp(1)_left). H3 same (cited Wedderburn). n >= 4 open lead.
  FlavourDoubletOnLeftLine.lean.
- D2 long-braid limit: real (tendsto_normalised_pow) but no current observable in regime
  (scope a). T(3,5) 17.2 % from limit; 1e-3 needs N = 31. Probe
  long_braid_limit_dominant_line_probe.py ALL PASS; matches corpus W(q) (qou-egvf).
  Finding: convention D kills the all-R (sign) block and z_D is not relabel-invariant, so
  the D ruling already chose the side (agrees with leftLine = P+ at q > 1). Scope (a).
- D3 index character built from corpus indexRep + §7a rescaling; neg_flip no-braid-image
  now uncited (wordImage_ne_neg_negCrossing). BalancedIndexCharacter.lean.
Lean verified at 4139a76ee (lean-direct exit 0, no sorryAx). Precision gates: the RED
ratchets are tree-wide and do not name this branch's probe (no witness added).


## 2026-11-15 owner ruling (thread 'Map SM and eightfold way', decision card): D-H2 restated at the pair level
D-H2 = no stays for single letters (flip_ne_swap). Added: on γγ pairs the swap ι: σ ↦ −σ⁻¹ sends V = σᵢσᵢ₊₁⁻¹ to V̄ = σᵢ⁻¹σᵢ₊₁ (signs cancel on even words), so the pair orientation bit V/V̄ IS the chirality mirror. Flavour must come from elsewhere (n ≥ 4 lead, qou-wkcd). Lean lemma ι(V)=V̄ not yet written. Evidence: PR #7741 gg_two_orientations (03b13f15561), gg_decay (6ff2aaaa8bf).

## 2026-11-15 n >= 4 lead — four-strand left flavour doublet (PR #7957 draft, issue #7956)

Thread "Derive flavour from the n ≥ 4 doublet". Branch claude/n4-left-flavour-doublet-2026-11-15 (9f1f05c7c).
FlavourDoubletFourStrands.lean (lean-direct exit 0, std axioms only): explicit (3,1) rep of H4(q);
sigma1 left line 2-dim (doublet), right 1-dim (singlet).
- A. sigma3 eigenline (pre-registered): nonzero left-only sl2, c = 2(q^4+1)/(q^2+1)^2; gg vertex
  s1 s2^-1 carries it; 3-strand words mix u<->d.
- B. J4 = s3 s2 s1^2 s2 s3 eigenline (owner: both side by side): no 3-strand word mixes it; only
  strand-4 vertices (s2 s3^-1, mirror) flip it; nonzero sl2, c = 2(q^2+1)^2(q^4+1)/(q^4+q^2+1)^2.
- Probe computations/probes/n4_left_doublet_flavour_probe.py on SM-thread reading-3 passing words
  (m=3,4): ALL PASS. On Ja ((3) sector) every gg vertex acts as 1.
Open: 3-strand words mix L and R; which of Ja/Jb is n is unassigned (owner call); physical
reading is scope (a).

## 2026-11-15 19:2xZ — weak vertex on the n=4 J₄ doublet (PR #7957, commit 7d0faf867)
- Lean (sorry-free): W(σ) = σ − h·P_L(σ). W on strands 1–2 commutes with J₄, so it never changes the J₄ flavour (weak_site1_comm, weak_site2_comm). On strand 4 the insertion between flavours is −h/[2]·eJ, and −h/[2]·fJ back (weak_site3_flips, weak_site3_flips_back). So a one-vertex n↔p step exists, and only on the 4th strand.
- Probe computations/probes/n4_weak_vertex_decay_probe.py (pre-registered, symbolic q, ALL PASS): in the reading-3 passing words, 31/48 have a positive-σ₃ slot; all 44 slots change Ja→Jb; but in most of these words the free word already flips flavour, and 40/44 slots also leak to σ₁'s right line. Only 8 slots flip ONLY through the vertex; 2 of them are leak-free (V0.V1.Vb0.Vb1 and Vb0.Vb1.V0.V1, slots 7 and 3).
- Still open: which of Ja/Jb is n (owner call); the right-line leak; vertex on inverse letters (not ruled).

## 2026-11-15 correction and open items (PR #7975, issue #7974)
- CORRECTION: the earlier note here said the strand-4 weak vertex is a one-vertex n<->p step. That is wrong. The J4 label is the H3 isotypic sector: Ja = (3) (sigma1 = sigma2 = q), Jb = (2,1). Under Schur-Weyl that is the three-strand isospin 3/2 vs 1/2, NOT T3. Hecke elements commute with the U_q action (qou-0whz C2), so no braid word and no weak vertex changes n<->p. Neither J4 state is n or p. Also corrected in a #7957 comment.
- Inverse letters: weakVertex q^-1 sigma^-1 = weakVertex q sigma; the insertion is h*rightLine (WeakVertexInverseLetter.lean).
- Leak: the vertex on sigma1/sigma3 keeps the lines of sigma1; sigma2 is the leak (s2_leaks).

## 2026-11-20 — W2 cross-workstream briefing (owner: "make sure they know")
Full briefing: PR #8526 comment 7047864732 and docs/coordination/2026-11-20-w2-qbeta-ud-briefing.md. Record: docs/audits/2026-11-20-qbeta-epsilon-is-ruled-not-derived.md sections 1-11.
Key points: Q_beta = (h[2]/2)*y3*E0 and sees only the isospin-3/2 block. The ruled epsilon (z_D, -43%) = label-A round trip = whole-space quantum trace. Label B (J4, strand-4 gamma-gamma) gives +0.33% and is NOT adopted (it labels isospin multiplicity, not n<->p). Label C gives 1/3, 0 and 0.202, none close. The owner made no label ruling ("3 2"). u/d are separate lines of the (3,1) rep of H4, not orientation-only (def:up/down-quark are stale). Convention-D volumes lie past the Phi_q pole. The six-term -2.43e15 was a truncated divergent series (fixed). The +0.17% / ~1 ppm Q_beta values and the April BW run are superseded or circular.
