# RESULT: coideal (quantum-symmetric-pair) colour on (ℂ³)^⊗n (bean `qou-ni4b`)

- Pre-registration: `PREREGISTRATION-coideal-colour.md`, commit `096d888f561`, pushed before any code.
- Probe: `qcd_coideal_colour_probe.py`, output `qcd_coideal_colour_probe.out.json`, commit `d97eaeddd46`.
- **35/35 checks pass. Every pre-registered prediction held.** One check is post-hoc and is labelled
  `posthoc` in the JSON.
- Exact sympy over ℚ(q, c₁, c₂). The large linear systems use `DomainMatrix` over the fraction
  field. No float, and q₀ is not used. The run takes about 30 s.
- The coideal parameters c₁ and c₂ are free symbols throughout. No value was chosen.

The setting is the sibling probes' setting: Jimbo U_q(gl₃) on ℂ³, coproduct variant B (Kolb's
convention), and the same Ř. Two Letzter coideals were tested, with X = ∅ and s = 0:

- **AI**, (gl₃, so₃): B_i = F_i − c_i E_i K_i⁻¹.
- **AIII**, (gl₃, gl₂⊕gl₁): B₁ = F₁ − c₁E₂K₁⁻¹, B₂ = F₂ − c₂E₁K₂⁻¹, and H = K₁K₂⁻¹.

## Claim

**A coideal does not give colour.** Both coideals commute with the type-A Hecke action and are
carried with the strand. AIII also gives a genuine cylinder (type-B) structure, with a K-matrix that
solves the reflection equation. But:

1. Neither coideal is su(3). Their q → 1 Lie algebras have dimension 3 (so₃) and 4 (s(gl₂⊕gl₁)).
2. Neither produces convention D. Every B-invariant twist tested gives the level-3 trace,
   z₃ = q³/[3]_q, on the type-A part. No rank-2 D twist is B-invariant for any c, including c = 0.

The q² = 1 obstruction of `qcd_colour_action` K4 is not touched. That obstruction is about colour ⊗
flavour on ℂ⁶. On colour ℂ³ alone there was never an obstruction: the full U_q(gl₃) already meets
(b), (c) and (f). A coideal of U_q(gl₃) is strictly smaller than U_q(gl₃), so it can only lose
colour, not gain transport.

## Per candidate

| | AI (so₃) | AIII (gl₂⊕gl₁) | scope |
|---|---|---|---|
| **Q1a** coideal property on V⊗V | Δ(B_i) = B_i⊗K_i⁻¹ + 1⊗F_i − c_i·1⊗E_iK_i⁻¹ ✓ | same form; the first legs are H^{∓1} ∈ B ✓ | exact matrix identity |
| **Q1b** commutes with σ_i, n = 2, 3 | ✓ | ✓ | (b) structurally: B ⊂ U_q(gl₃), whose Δⁿ commutes with Ř (Jimbo duality). A sanity check, not a finding. |
| **Q1c** transport, Ř → P at q = 1 | ✓ | ✓ | exact |
| **Q2a** commutant of B on ℂ³ | scalars only (dim 1) | dim 2: {1, J₀}, J₀ non-diagonal, mixing e₁ and e₃ | exact |
| **Q2b** K-matrix, reflection equation | no non-trivial commuting K. The AI K-matrix is τ₀-twisted and was not tested. | Ř(J⊗1)Ř(J⊗1) = (J⊗1)Ř(J⊗1)Ř on the pencil α + βJ₀ holds iff β = 0 or J ∝ J₀⁻¹. The K-matrix is K = [[0,0,c₁³c₂²q],[0,−c₁³c₂q²,0],[c₁²c₂q², 0, c₁²c₂q(c₂−c₁q)]], with eigenvalues c₁²c₂²q (once) and −c₁³c₂q² (twice). So it is a quadratic type-B Hecke generator, with eigenvalue ratio −c₂/(c₁q). K⊗1⊗… commutes with Δⁿ(B) for n = 2, 3; 1⊗K does not. | exact. The type-B parameter is set by the free c, not derived. |
| **Q2c** B-invariant twists | on V: the pivotal only (dim 1). On V⊗V: dim 3. | on V: dim 2. On V⊗V: dim 7. T₁⊗g is invariant for every V-invariant T₁, but **T⊗T is invariant only for T = pivotal** (solution β = 0). | exact |
| **Q2d** trace on H₃ | pivotal: a trace, Markov, z = z₃ | T₁⊗g⊗g for any (α, β): a trace, Markov, **z = z₃ identically**. The normalised weight on the (1³) block equals the pivotal's, q⁶/(q⁴+q²+1)³, not 0. | (b) on the type-A part, see "Invariant" below |
| **Q2e** D twists (supports {1,2}, {1,3}, {2,3}) | no solution in (c₁, c₂) | no solution in (c₁, c₂) | exact, n = 1 |
| **Q3(a), Q4** su(3)? | Lie dimension **3** (so₃) | Lie dimension **4** (s(gl₂⊕gl₁)) | (b): a classical fixed-point algebra of a symmetric pair of gl₃ has dimension 3 or 4, not 8. Measured here for these two pairs. |
| commutant of B on V⊗V | 3 (U_q(gl₃) gives 2) | 7 | exact |
| **Q3(c)** Hecke + braid | ✓ | ✓ | exact |
| **Q3(d)** z_D from a B-invariant Markov twist | ✗ (z₃) | ✗ (z₃) | |
| **Q3(e)** B-singlets | V^⊗3: dim 1; V⊗V: **dim 1** (σ = q there) | V^⊗3: **dim 3**; V⊗V: 0 | exact |
| **Q3(f)** transport | ✓ | ✓ | |

**Invariant behind Q2d.** For a cylinder-type product twist G = T₁⊗g^{⊗(n−1)} and x ∈ H_n, the
partial quantum trace of x over strands 2…n is a U_q(gl₃)-endomorphism of the irreducible ℂ³. By
Schur's lemma it is a scalar. So tr(Gx) = tr(T₁)·(the level-3 trace of x), whatever T₁ is. The first-strand
(K-matrix) twist is invisible on type-A H_n. It enters only through the type-B generator.

**Acceptance (a)–(f), from `qcd_colour_action`.** AI: (a) ✗, (b) ✓, (c) ✓, (d) ✗, (e) ✓ in V^⊗3 but
it also has a two-strand singlet, (f) ✓. AIII: (a) ✗, (b) ✓, (c) ✓, (d) ✗, (e) ✗, (f) ✓.
**Q4: FAIL for both.** Calling either one colour would be a FAIL by the pre-registered rule.

## What is established and what is not

Established, exactly over ℚ(q, c):

- The two Letzter coideals act on (ℂ³)^⊗n commuting with Hecke and with transport. That is
  inherited from U_q(gl₃) and is not new.
- They are not colour: dimension 3 and 4.
- AIII carries a genuine cylinder structure:
  - the reflection-equation K-matrix is fixed up to scale (J ∝ J₀⁻¹);
  - it commutes with B on strand 1 only;
  - it gives a quadratic type-B generator.
- The type-A part of every B-invariant product twist is the level-3 trace (z₃). D is not produced.
- No rank-2 D twist is stabilised by either coideal, for any c.

Not established, and not tested (scope (a) outside the searched class):

- The τ₀-twisted AI K-matrix (Balagović–Kolb's 𝒦 for ττ₀ ≠ id).
- s_i ≠ 0, and the other Satake data for gl₃.
- Non-product B-invariant twists on V⊗V (dim 3 for AI, dim 7 for AIII) as Markov twists for all n.
- **The route that could matter: a coideal of U_q(gl₆) on ℂ³⊗ℂ².** This is a post-run observation,
  not computed. The symmetric pair (gl₆, gl₃⊕gl₃) has fixed points containing the diagonal sl₃ acting
  as sl₃⊗1 on ℂ³⊗ℂ², which is colour. The other symmetric subalgebras so₆ and sp₆ cannot contain
  sl₃⊗1, because 3⊕3 carries no sl₃-invariant bilinear form. Whether the AIII coideal B ⊂ U_q(gl₆)
  contains a subalgebra deforming U(sl₃^diag), and whether it escapes the K4 q² = 1 obstruction, is
  untested. That would be the next probe, and it needs its own pre-registration.
- The literature claim that "no paper builds SU(3) colour this way" was not re-searched here.
- No gluon is identified. Nothing was selected.

## Post-hoc findings (labelled)

1. **Post-hoc.** The reflection equation does not hold on the whole commutant pencil. It cuts out
   exactly the line J ∝ J₀⁻¹ (residual gcd β·c₁²c₂(q²−1)·(α + β(c₁³c₂q² − c₁²c₂²q))). This was
   solved, not chosen, and the pre-registration had allowed for "only after a normalisation".
2. **Post-hoc.** The AI three-strand singlet has σ₁ = σ₂ = −q⁻¹. So it lies in the (1³) block, and
   convention D's weight on it is 0, by `ocneanuWeight_conventionD_eq_zero_of_three_rows`. This is the
   same radical statement as for the su(3) baryon in `qcd_colour_full_tower`, now for so₃.
3. **Post-hoc.** The AIII three-strand singlets (dim 3) carry the H₃ representation (2,1) ⊕ (1³):
   trace of σ₁ = q − 2q⁻¹. So D sees their (2,1) part, the same 2+1 pattern as the D residual
   U_q(gl₂)×U(1). This was declared in advance as a coincidence of shape, not evidence.
4. **Post-hoc, a citation correction for `qcd_colour_full_tower/LITERATURE.md` §F.** math/0512581 is
   Kolb, *Quantum symmetric pairs and the reflection equation*, a single author. LITERATURE.md lists it
   as "Kolb–Stokman, *Reflection equation algebras, coideal subalgebras and their centres*". That is a
   different paper. I verified it by fetching the arXiv PDF on 2026-11-22, and did not edit
   LITERATURE.md.
5. **Post-hoc, a correction to my own first run.** Q1a first failed for AIII because my membership
   test looked only for H⁻¹, while the first leg for i = 2 is H. That was a bug in the test; the
   coproduct identity itself was unchanged. Check labels were also restated as prediction checks after
   the first run. The predictions themselves were not changed. Acceptance outcomes are recorded
   separately under `acceptance_a_to_f`.

## Implications

- The coideal route named in LITERATURE.md §F does not produce colour for gl₃. Its fixed algebras are
  too small (scope (b) by dimension), and its K-matrix does not touch the type-A trace (scope (b) by
  Schur's lemma, for product twists).
- Convention D is not recovered as a coideal-invariant functional, so the D question is unchanged.
  D is the rank-2 trace, colour singlets are in its radical, and choosing D versus the level-3 trace
  is the owner's modelling choice (see `qcd_colour_full_tower/RESULT.md`).
- The only coideal candidate left that could plausibly carry colour with the strand is the gl₆ /
  (gl₃⊕gl₃) pair on colour⊗flavour. It is untested.

## Verification

- `python3 -u qcd_coideal_colour_probe.py` → `SUMMARY 35/35`, exit 0, about 30 s.
- `scripts/precision-gates.sh --changed`: the RED lines are the repo-wide ratchets (q0-anchor
  flip/refill, never-raises-dps, reference-literal, witness-value copy, q0-value drift). None names a
  file in this directory. The modified audit witnesses in the worktree predate this work and were not
  staged.
