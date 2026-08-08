---
# qou-985x
title: 'Extended Bloch group route: flattening supplies the canonical log-branch A1 lacked'
status: todo
type: task
priority: normal
created_at: 2026-08-07T08:53:01Z
updated_at: 2026-08-07T08:53:03Z
parent: qou-kemt
---

Owner steers 2026-08-07: 'should depend on knot' + 'sibling is using extended Bloch group'. Both land on the same object. A1 was killed by the ROAST because 'take the log / do not normalize' is a one-parameter family (branch-of-log ambiguity) => picking a member is a fit. Neumann's extended Bloch group resolves EXACTLY that: flattened shapes [z;p,q] with p,q in Z recording log z + p*pi*i and -log(1-z) + q*pi*i, FIXED by the gluing/parity equations, not chosen. R-hat descends to Vol + i*CS exactly (ordinary Bloch only gives CS mod pi^2/6). Converts A1 from unfalsifiable to derivable. Satisfies all three constraints: additive (sum over ideal tetrahedra BY CONSTRUCTION), super-pairwise (a tetrahedron has 4 vertices; the proved rho_A <= C(A,2) cap bounds PAIR counting, not tetrahedron counting), knot-dependent (Vol+iCS vs the bare normalization N^(n-1) which depends only on strand count). Bridge already in corpus: volume conjecture lim (2pi/N) log|<K>_N| = Vol. Corpus: Kashaev 760 files, volume conjecture 199, complex volume 148, Neumann 230, flattening 36, but 'extended Bloch' in ONE file. OWNER RULING: hyperbolicity of the light-nucleus closures is ASSUMED GRANTED ('assume it is there and work from there') -- caveat 1 stands down, work proceeds from there.

## Re-scoping note (2026-08-08, PR #4824)

Investigated to set a non-trap entry point (audit:
`docs/audits/2026-08-08-extended-bloch-tetrahedron-scoping-trefoil-trap.md`).
The owner's "assume hyperbolicity granted" ruling stands and is respected.
Three facts sharpen this bean:

1. **The literal deuteron carrier is the trefoil T(2,3), Vol=0** (torus,
   Seifert-fibred). The volume/Bloch leg contributes nothing there; the honest
   deuteron probe (`deuteron_octahedral_gluing_probe.py`) uses `Re Φ_q` + the
   bar-even `s(z₀)`, not `Vol`. Granting hyperbolicity relocates this to a
   choice-of-representative question (= the germ/handle freedom below), it does
   not make a genuine deuteron volume appear.
2. **The A=3 parameter-free volume ratio is ALREADY computed**
   (`binding_link_volumes.py`): Vol(8₁₁)/Vol(L6a4) = 1.1308 vs
   B(³H)/B(³He) = 1.0990 (+2.9%); absolute single-link endomorphism −60%.
   Do not re-derive it.
3. **The route's NEW content over that compute is the iCS leg**, and PR #4591
   shows it is **muon-uncalibrated** (CS(4₁)=0, amphichiral ⇒ any F(Vol,CS)
   reducing to Vol at CS=0 is equally muon-consistent). A CS-dependent closure
   cannot be wired to production until an independent CS anchor exists.

**Surviving open item (the real successor to #4798):** on the A≥3 **hyperbolic**
carriers (8₁₁, L6a4/Borromean), does the flattening `β̂=Σ[zᵢ;pᵢ,qᵢ]` (integers
fixed by gluing/parity) pin PR #4798's transverse surface-curvature coefficient
`c₂` **parameter-free** (killing its 0…897 germ/handle range)? Falsifiable; no
free parameter if it works; never touches the trefoil. Carry the §3
CS-calibration caveat alongside.

## Update 2 (2026-08-08, PR #4824, audit §6) — surviving item changed

Pursued §4. An already-landed proved result redirects it:
`one_loop_ambiguity_group_probe.py` (qou-fl4t, PR #4691) shows the DG 1-loop
flattening ambiguity is a **DISCRETE shape-unit group** (⟨√2⟩ for L6a4, trivial
for 4₁, ⟨√ρ⟩ plastic for 5₂). But #4798's transverse c₂ ranges CONTINUOUSLY
0…897. A discrete-group canonicalisation cannot pin a continuous range ⇒ the
"flatten #4798's c₂" framing is **unsupported** (scope-a); c₂ and the
flattenable τ_DG are different constructions with no established reduction.

REDIRECT: the object the flattening actually canonicalises is the DG 1-loop
torsion τ_DG (discrete ambiguity + geometric selection ⇒ canonical value).
Corpus |τ_DG|: 4₁=√3/2, L5a1=√2, L6a4=8.

NEW surviving item (replaces the c₂ item): compute the parameter-free
τ_DG(8₁₁)/τ_DG(L6a4) and compare to B(³H)/B(³He)=1.0990 — the τ_DG analogue of
the §2 volume ratio, on the canonically-flattened object. τ_DG(8₁₁) needs a
SnapPy run (unavailable in the current sandbox — BLOCKED here). Carry the §3
CS-calibration caveat.

## Update 3 (2026-08-08, PR #4824, audit §7) — canonical τ_DG ratio RUN: no improvement

Installed SnapPy in-session and ran the redirected probe
(`computations/probes/dg_torsion_binding_ratio_a3_probe.py`). Calibration
passes (τ_DG(4₁)=√3 classical adjoint torsion; τ_DG(L6a4)=64 corpus).

  τ_DG(8₁₁)/τ_DG(L6a4) = 1.13466  (+3.25% vs B(³H)/B(³He)=1.09895)
  Vol(8₁₁)/Vol(L6a4)   = 1.13082  (+2.90%)

Honest NEGATIVE (scope-a): the canonical DG-torsion ratio is essentially
identical to the volume ratio — canonicalising the object does NOT improve the
A=3 binding mirror-pair. The ~3% miss is shared by both hyperbolic invariants.
Caveat: |det J| is triangulation-representative (full flattening-monomial
repair = qou-fl4t).

STATUS of qou-985x: the hyperbolic-invariant leg (Vol and canonical torsion
alike) tops out at ~3% on the A=3 ratio and carries no A-dependence. Remaining
live angles are NOT more hyperbolic-invariant ratios: (i) the iCS leg — but it
is muon-uncalibrated (#4591, audit §3); (ii) a genuinely additive ≥3-body
extensive term (qou-0c19), which is a different object class from any per-link
invariant. No fit; nothing wired.
