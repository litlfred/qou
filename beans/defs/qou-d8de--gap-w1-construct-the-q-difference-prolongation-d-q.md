---
# qou-d8de
title: 'GAP W1: construct the q-difference prolongation D_q from the color spectral curve Σ'
status: todo
pr: 8200
type: task
priority: normal
tags:
    - 8f-lean
    - 8f-open
    - reorg-2026-10-04
created_at: 2026-08-01T01:43:06Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
---


## The wall (W1 / G1 of the C1↔SW leg)

Parent: `qou-3cgi` (C1↔SW geometric leg). Keystone conjecture
`conj:qdifference-kernel-prolongation-symbol`: the proved binding q-difference
carrier **C1** (`[m+2]_q b_{m+2} = b_{m+1} + b_m`, Lean `qlift_normalized_kernel_exists`)
IS the principal symbol of the jet-prolongation operator `J^n E → J^{n+1} E` of the
Seiberg–Witten connection on the color spectral curve

  `Σ:  P(X,z) = X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1) = 0`,   `λ_SW = X dz`.

**W1 = build the prolongation operator itself.** A genuine derivation needs an
operator `D_q : J^n E → J^{n+1} E` lifting the SW connection to the jet tower over
Σ. This bean is *only* W1 (construct `D_q`); the downstream symbol extraction (W2)
and the anti-fit symbol=C1 check (W3/G3) are separate.

## Why the obvious candidate is DEAD (proved, load-bearing)

The classical lift `D = d/dz` is **proved wrong** — do not retry it:
- `prop:sw-classical-jet-exactness` (Lean `classical_jet_period_zero`,
  `classical_jet_period_ne_lw`, `fresidue_fderiv`, generic `CommRing`, sorry-free):
  classical jets `λ_SW^(n) = d(X^{(n-1)})` are **exact** ⇒ all periods/residues `= 0`
  ⇒ can never equal the binding period `I(m)/m > 0`.
- Ramification-parity (Lean `QOU/Brings/RamificationParityMonodromy.lean`, sorry-free):
  at a simple branch `z = z_c + t²` the covering monodromy `t ↦ −t` acts by `(−1)^k`
  on `a_k t^k`; classical `d/dz = (1/2t) d/dt` shifts the `t`-exponent by exactly −2,
  hence **preserves t-parity** — so the classical jet cannot generate the Door-v
  `(−1)^n` twist that `C1⊗C1` vs GGM differ by.
- `ColorCubicPowerSums.color_power_sums`: the power sums `pₙ = −(zⁿ+1)` are **q-free**,
  so any operator reproducing the q-deformed C1 must be **non-classical (q-difference)**,
  not built from the classical differential of Σ.

So the "which prolongation" question is closed down to **q-difference**; W1 is to
actually construct that q-difference `D_q` from Σ.

## What is missing (the real gap)

Neither Mathlib nor the corpus has a **q-jet bundle / q-D-module prolongation of a
connection on an algebraic curve**. There is no object `J^n_q E` and no q-difference
connection lift.

> 🛑 **Correction (2026-09-06, `qou-p6m1`).** This sentence also said “no q-symbol calculus at a ramified pole”. That half is **false since 2026-09-03**: `QOU.Mathlib.RamifiedShiftCalculus` builds exactly that, sorry-free. `J^n_q E` and the connection lift remain absent, so **this gap stands** — narrowed, not closed. This is genuine
mathematical-infrastructure construction, not a probe.

## Existing infra to build on

- `QOU/Mass/ColorSpectralCubicGeometry.lean` — `color_cubic_discriminant`
  (disc = −branchSextic), `branchSextic_palindromic` (`z ↦ 1/z`), the branch locus.
- `QOU/Mass/sw-classical-jet-exactness.lean` — the proved `fresidue`/jet model
  (`fresidue_fderiv`, `classical_jet_period_zero`) — the model to *extend* with a
  q-difference (rather than classical `d/dz`) prolongation.
- `QOU/Brings/RamificationParityMonodromy.lean` — the `t ↦ −t` parity involution at
  the branch point (the local coordinate where `D_q`'s symbol would be read).
- `computations/probes/zgeometric_ramification_parity_probe.py` — numerical branch
  point `z_c` (|P_X(X0,z_c)| ≈ 6e−21), local `t`-expansion machinery.

## Honest candidate routes (none attempted — this is the open work)

1. **q-shift on the base.** Define `D_q` from the base q-shift `z ↦ q² z` (or the
   multiplicative structure the fibre root-of-unity singularity induces on Σ), and a
   q-connection lift on the jet tower; test whether the induced symbol is depth-2.
2. **Root-of-unity fibre monodromy.** The fibre singularity is a root of unity; a
   q-difference connection may arise naturally from its local monodromy. Construct the
   q-D-module from that datum.
3. **Literature.** q-difference D-modules / q-jets: Sauloy; Di Vizio; van der Put–
   Singer *Galois Theory of Difference Equations*; Ramis–Sauloy–Zhang local
   classification of q-difference modules (needed for W2 anyway). Import the
   right definitional framework before hand-rolling.

## Anti-laundering (STRICT — carries to W3/G3)

C1 is *already* fixed by the binding recurrence. A symbol match is meaningful ONLY
if `D_q` and its symbol are computed from Σ **independently** — never fitted to
reproduce `[m+2]_q(·)=(·)+(·)`. Constructing `D_q` "so that" its symbol is C1 is a
fit, not a derivation, and must not be wired to production (owner directive; §Axioms
are NOT a Proof; Subgoal-2 open-for-all grants permission to *derive*, not to fit).

## Verdict / scope

Multi-month geometric-analysis construction (per
`docs/audits/2026-07-20-zgeometric-prolongation-symbol-scoping.md` §3–4:
"cannot be closed by a probe or a short Lean lemma"). Not a session brick. Honest
next step: pick route 3 (import the q-difference D-module framework from the
literature) before attempting routes 1–2, so `D_q` is built on a real definitional
foundation rather than an ad-hoc operator.

## Progress (2026-08-01, PR #4449) — two concrete ingredients landed

Both sorry-free, non-circular (computed from Σ / the operator, independent of C1),
no fit, no conjecture-class asserting the identification:

1. **Candidate base operator** (`QOU/Mass/QDiffProlongationBaseOperator.lean`): the
   q-shift / Jackson q-derivative names the quantum integer —
   `(q·z)^n − z^n = [n]_q·(q−1)·z^n`, i.e. `D_q(z^n) = [n]_q·z^{n−1}` (vs classical
   `n·z^{n−1}`, q-free per `ColorCubicPowerSums`); `[n]_1 = n` (classical limit).
2. **Σ is a q-integer curve** (`QOU/Mass/ColorCurveQIntegerForm.lean`):
   `C_z(X) = [1]_z X³ + [2]_z X² + [3]_z X + [4]_z` — the coefficients ARE quantum
   integers; `[k+1]_z = [k]_z + z^k` (q-integer ladder). So the base q-shift acts
   naturally on Σ through the coefficient functional equations.

## Precise remaining obstruction (the genuine multi-month core)

The **jet-tower lift** `D_q : Jⁿ E → Jⁿ⁺¹ E` over Σ compatible with the SW connection
is still open, blocked on TWO things:

- **(i) Missing infra.** No q-jet bundle prolongation of a connection on
  an algebraic curve exists in Mathlib or the corpus (the ingredients above are
  the *base* operator + the *curve* structure, not the bundle lift). The
  *symbol calculus* half of this item's original wording is **PRESENT** since
  2026-09-03 — `QOU.Mathlib.RamifiedShiftCalculus`, sorry-free; see `qou-p6m1`.
- **(ii) q-chain-rule obstruction.** The classical jet uses implicit differentiation
  `X' = −(∂_z C)/(∂_X C)` of `C_z(X(z))=0`. The Jackson q-derivative has **no clean
  chain rule** for `D_q(C_z(X(z)))`, so the classical implicit-jet route does not
  q-deform directly. A single-valued `D_q` on the jet bundle requires choosing a
  branch of the z↦qz correspondence on Σ (the fibre root-of-unity datum) — this is
  the geometric heart, not yet constructed.

Honest next step (if resumed): either (a) the q-partial-derivatives `D_q^{(z)} C`,
`D_q^{(X)} C` as an intermediate (well-defined, no chain rule) then attack the
branch-selected assembly; or (b) import a q-difference D-module / q-jet framework from
the literature (Sauloy; van der Put–Singer) before hand-rolling the bundle. Still a
multi-month construction; not a session brick.

## Update (2026-08-01, PR #4449) — 5 ingredients; wall localized to single monodromy

Added beyond the two above:
3. q-difference operator infra (`QOU/MathlibExt/QDifferenceOperator.lean`): q-Leibniz
   (clean), monomial q-chain rule (q→q^m), and the PROVED no-naive-chain-rule
   counterexample — why a non-monomial branch X(z) admits no implicit-jet q-recurrence.
4. q-partials + branch-selection defect (`QOU/Mass/ColorCurveQPartials.lean`):
   on Σ, `Δ_q^z C(X,z) = C_{qz}(X)` — the defect measuring X leaving Σ under z↦qz.
5. sheet structure (`QOU/Mass/ColorCurveSheets.lean`): Vieta reconstruction (sheets ↔
   q-integer symmetric functions) + `defect = (X−Y₁)(X−Y₂)(X−Y₃)` (gaps to the shifted
   sheets); branch coherent ⟺ X is a shifted sheet.

**The wall is now ONE thing:** which shifted sheet Yᵢ continues X **single-valuedly** —
the monodromy of the 3-sheeted cover around the branchSextic zeros (fibre root-of-unity
datum; (−1)ⁿ parity proved on main, `Brings.RamificationParityMonodromy`). Everything
algebraic around it is now formalized; the global single-valued algebraic `D_q` is the
transcendental core. **Honest terminus for the calculus/algebra approach** — closing it
needs the q-difference D-module / monodromy-representation framework from the literature
(the branch is a section of the cover, not a rational function). Not faked; not a session
brick.



## Route 1 PRUNED (2026-09-04, bean qou-1z28, PR #6695) — scope (b), invariant cited

A rational q-connection on the base z-line (z -> lambda z, lambda not a root of unity) with the three colour sheets as flat sections does NOT exist. Shape: the colour cubic is irreducible over K(z) for every char-0 field K (Lean QOU.Mass.ColorCubicIrreducible.colorCubicAt_ne_zero + colorCubic_no_ratFunc_root, sorry-free) so no sheet is rational in z; each sheet is algebraic hence D-finite (explicit order-3 ODE in the probe, leading coefficient vanishing on the branch sextic); a rational rank-3 q-difference system with the sheets as solutions would make a sheet q-holonomic; D-finite AND q-holonomic => rational (Bezivin 1992 / Ramis 1992 / Schaefke-Singer JEMS 2019). Contradiction.

NOT pruned: non-rational coefficients, operators on Sigma rather than the base, and the LOCAL q-dilation t -> qt at a branch point (the theorem does not apply there — every power series is trivially first-order q-holonomic with a power-series coefficient). Routes 2 and 3 untouched; 3 (RSZ / Sauloy local framework) is the natural next step since the surviving object is local. Audit: docs/audits/2026-09-04-w1-route1-base-qshift-rationality-prune.md.



## Route 1 prune STRENGTHENED 2026-09-05 (bean qou-7fnr, PR #6738) — it covers the local chart too

The route-1 entry above ends by saying the LOCAL q-dilation t -> mu t at a branch point is not pruned because the theorem does not apply there. That is wrong: the reason given concerned power-series coefficients, the theorem concerns rational ones. In the local coordinate the sheets are still algebraic over K(t) hence D-finite, and still not rational (t^2 = z - z_c makes K(t)/K(z) quadratic, and an irreducible cubic has no root of degree <= 2 — QOU.Mass.IrreducibleCubicNoQuadraticRoot, sorry-free). So a rational q-dilation is excluded in the local chart as well.

Route 1 is now excluded in BOTH coordinates. Routes 2 (root-of-unity fibre monodromy) and 3 (RSZ / Sauloy local framework) remain, and route 3 now has to supply an operator whose coefficients are NOT rational in a coordinate — a sharper requirement than the earlier entry implied. Audit: docs/audits/2026-09-05-w1-local-qdilation-also-excluded-correction.md.

## Route 1 closed on Sigma too (2026-09-05, bean qou-lmnq, PR #6769)

The 2026-09-04 entry above closed route 1 in the base and local COORDINATES, by the coefficient field. It left an operator on Sigma itself untouched. That is now closed for the dilation: no nontrivial z -> lambda z lifts to an automorphism of Sigma at all, because such a lift would permute the six finite branch points and hence satisfy D(lambda z) = c D(z), whose constant and linear coefficients force c = 1 then lambda = 1 (Lean QOU.Mass.DilationBranchLocusRigidity, sorry-free). Holds for every lambda including roots of unity, so it is complementary to Bezivin-Ramis rather than dependent on it.

Route 1 is therefore closed in all three charts. ROUTE 2 (root-of-unity FIBRE monodromy) is untouched — it acts on the fibre, not the z-line — and is now the live route; route 3 (RSZ/Sauloy framework import) likewise.


## Route 2's EIGENVALUE reading is closed (2026-09-07, bean qou-hmrm, PR #7114)

Route 2 above proposes building D_q from the "root-of-unity fibre monodromy". Which
root of unity that datum supplies is now settled, and it is `-1`.

The branch sextic is squarefree, and the colour cubic has **no triple root for any
z** (Lean `QOU.Mass.FibreMonodromyOrderTwo.colorCubic_no_triple_root`, sorry-free:
matching against `(X-r)^3` and eliminating r forces both `2z^2+z+2 = 0` and
`26z^3+24z^2+24z+26 = 0`, which give `15z = 30` and then `12 = 0`). So no THREE
sheets ever collide: every branch point is simple, its local monodromy is a
transposition, order exactly 2, eigenvalue `-1`.

And `q = -1` is exactly where C1 cannot live: `[2]_{-1} = 0` FALSIFIES the standing
hypothesis `forall k >= 1, [k]_q != 0` of `qlift_normalized_kernel_exists`, so that
carrier does not apply there rather than merely degenerating
(`c1_hypothesis_fails_at_neg_one`).

Scope (b) over ONE identification: q = the eigenvalue of the local fibre monodromy.
Still open at scope (a) at most, and NOT pruned: a structure using the monodromy
*representation* without setting q to an eigenvalue; a construction at `z = infinity`;
one from the global S_3 rather than a local generator.

**NEW STRUCTURAL FACT, and route 3 wants it: SIGMA IS AN ELLIPTIC CURVE, g = 1.**
The fibre at infinity is `(Y+1)(Y^2+1)`, disc = -16 — three distinct sheets, so the
cover is unramified there; Riemann-Hurwitz gives `2g-2 = 3*(-2) + 6 = 0`. The corpus
had not computed the genus of Sigma before. Route 3 (Ramis-Sauloy-Zhang / Sauloy) is
stated against a curve of known genus, so it now has its input.

**And a symmetry none of the route-1 work covers.** The fibre at infinity coinciding
with the fibre at `z = 0` is the palindromic `z -> 1/z` symmetry of the branch sextic
appearing geometrically. #6769 closed dilations `z -> lambda z`; `z -> 1/z` is not of
that form, so the dilation rigidity says nothing about it. That involution is the
natural next automorphism to test.

Audit: docs/audits/2026-09-07-w1-route2-fibre-monodromy-is-order-two.md.


## Route 2, second reading (2026-09-08, bean `qou-ei4q`) — the involution lifts, and the base route is now closed ENTIRELY

The `z -> 1/z` opening this bean recorded after #7114 is resolved, and it went
both ways at once.

**It lifts.** `z^3 * P(X/z, 1/z) = P(X, z)`, so `iota~ : (X,z) |-> (X/z, 1/z)` is
an automorphism of Sigma. Unlike every dilation, `iota` passes the branch-locus
test #6769 uses -- because `D` is palindromic -- and unlike the eigenvalue reading
of #7114 it produces a real object. Sigma's **first recorded nontrivial
automorphism**.

**It is the elliptic involution.** 4 fixed points, genus-1 Sigma, quotient `P^1`.
Independently: the `w = z + 1/z` reciprocal cubic `16w^3+24w^2-13w+2` that the
corpus has used since 2026-05-19 to index the three Galois orbits IS the base
quotient coordinate for exactly this involution. That connection was not recorded.

**But the base-automorphism route is now closed entirely, not narrowed.** This is
the part that supersedes rather than extends #6769: a Moebius map is determined by
three points, so `Stab(B)` embeds in `Sym(B) = S_6` and EVERY base automorphism
preserving the branch locus has order at most 6 -- for any squarefree sextic
branch locus, not just this `D`. The substrate shift has infinite order
(`q_0 = 1.10997858... > 1`). So no automorphism of the base supplies the W1
q-shift, dilation or not, root of unity or not.

Explicitly, `Stab(B) = {id, iota} = Z/2` (120 dps, labelled numerical).

**What that leaves for W1.** Route 3 (Ramis-Sauloy-Zhang / Sauloy) is the live
one, and it is now better supplied than it has ever been: Sigma has a genus (1), a
distinguished involution, and an identified quotient (`P^1`). The three
alternatives still open at scope (a) are unchanged from #7114 -- a structure not
arising from a base automorphism at all, one built from the monodromy
REPRESENTATION rather than an automorphism, and one built at `z = infinity`.

`D_q` is still NOT constructed. The verdict of this bean -- import the framework
before hand-rolling an operator -- is unchanged and is now better founded: four
tranches have each closed a way of hand-rolling one.

Audit: `docs/audits/2026-09-08-w1-palindromic-involution-lifts-and-is-elliptic.md`.


## Route 3's spectral-curve reading is closed (2026-09-12, `qou-ar4v`, PR #7208)

The "honest next step" of this bean was: *import the q-difference D-module framework
from the literature before attempting routes 1–2.* Done, from the sources this corpus
holds (RSZ Astérisque 355 §2.1.1; DVRSZ §2.4–2.5).

**The framework's input is a difference field `(K, σ)`, and a system is read modulo a
TWISTED gauge** — DVRSZ eq. (2.4.1), `B = (σ_q F)⁻¹ A F`, **not** conjugation. That
single fact decides the obvious instantiation:

- `F = z^k·1` gives `A ↦ q^{-k}A`, and a scalar multiple **moves** the characteristic
  cubic (`X^{3−k}` coefficient picks up `t^k`).
- Stability of ANY monic cubic under `X ↦ tX` forces
  `a₀(1−t³) = a₁t(1−t²) = a₂t²(1−t) = 0`; at any non-root-of-unity `t` — every real
  `t > 1`, so every `q₀^{-k}` — all three non-leading coefficients **vanish**.
- So **the only gauge-stable monic cubic is `X³ = 0`**, and Σ is not it: its `z = 0`
  fibre is `X³+X²+X+1`.

**Consequence for obstruction (ii) of this bean.** The bean states the geometric heart
as *"a single-valued `D_q` on the jet bundle requires CHOOSING A BRANCH of the `z↦qz`
correspondence on Σ."* Taken with #6769 and #7185 (no base automorphism preserving the
branch locus has infinite order) and with this tranche (no fibre motion preserves the
cubic), the honest restatement is stronger: **there is no branch to choose.** The
difficulty is not selection, it is non-existence — for the reading in which Σ carries
the structure.

**What is still open, and it is now a sharper question than before.** Route 3 is NOT
dead. A q-difference module over `(ℂ(z), σ_q)` is a perfectly good object, and this
corpus already uses RSZ that way for scalar kernels
(`docs/audits/2026-07-20-qlift-routeA-rsz-invariants.md`). What has been removed is
the reading everything upstream was pointing at. So the question this bean now carries
is:

> **If Σ is not the spectral curve of the q-difference module, what is it?**

Candidates the framework itself offers, none tested: Newton polygon / slope data, the
Birkhoff connection matrix, the bundle on the Tate curve `E_q = ℂ*/q^ℤ` (RSZ §6.3) —
noting that Σ is itself genus 1 (#7114) with its elliptic involution identified
(#7185), so a comparison of the two elliptic structures is available and has not been
made. Treat any numerical coincidence between them as suspect until derived.

**The bridge remains an assumption.** *"The sought `D_q` would have Σ as its spectral
curve"* is what `λ_SW = X dz` sets up, but it is a hypothesis, carried as one in the
Lean and the probe. A tranche that gives Σ a different role in the module is not
obstructed by any of this. `D_q` is still NOT constructed.


## The prose chain is now ONE link long (2026-09-12, `qou-6pib`, PR #7208)

Every W1 tranche to date ended by naming a step it did not formalise. Three such steps
are now proved; **one** remains, and it is the only genuinely geometric one.

| step | was | now |
|---|---|---|
| a scaling preserving a finite nonzero set has finite order | prose (#6769, #7185) | `BranchLocusFiniteOrder.exists_pow_eq_one_of_stabilizes` — pigeonhole |
| a Möbius map is determined by three points (`Stab(B) ↪ S₆`) | prose; #7185 said it "would need Möbius machinery Mathlib does not carry" | `MoebiusThreePointRigidity` — it needed none; cleared, it is a quadratic |
| the gauge / spectral-curve dictionary (DVRSZ 2.4.1) | cited, not proved (#7208) | `QDifferenceGaugeMatrix` — `scalar_gauge_eq`, `det_charMatrix_smul`, `det_charMatrix_conj` |
| **an automorphism of `Σ` permutes the branch locus** | **prose** | **still prose — the one remaining link** |

Two of the three were blocked by their **formulation**, not their content. Clearing
denominators turned the Möbius fixed-point condition into a quadratic (no chart at `∞`);
clearing the inverse turned DVRSZ (2.4.1) into a hypothesis with no invertibility
side-condition. Worth remembering the next time a Lean gap here is blamed on missing
Mathlib machinery.

## And the two existing W1 bricks have been joined (same PR)

`QDiffProlongationBaseOperator` proves `D_q(zⁿ) = [n]_q·z^{n−1}`.
`ColorCurveQIntegerForm` proves the colour cubic **is** a q-integer curve,
`C_z(X) = [1]_z X³ + [2]_z X² + [3]_z X + [4]_z`, and asserts *in prose* that the q-shift
"acts on each coefficient through the q-integer functional equations". Neither computed
the composite. `QOU/Mass/QShiftColorCoefficientLadder.lean` does:

  `[n+1]_{q·z} − [n+1]_z = (q−1)·z·∑_{k<n} [k+1]_q·z^k`

so `D_q [n+1]_z = gradedZInt q z n`, against the classical `d/dz [n+1]_z = ∑ (k+1)z^k`:
**the Jackson operator puts `[k+1]_q` exactly where the classical derivative puts `k+1`**,
and they agree at `q = 1`. This is the mechanism by which `q` enters data that is itself
q-free — the gap the 2026-06-25 z2bn audit named when it excluded the classical
prolongation for precisely that reason.

Consequence for the curve: `D_q C = g₁X² + g₂X + g₃` with `gᵢ = gradedZInt q z i` —
the same shape as `C_z`, ladder index dropped by one, `[k]_z ↦ gradedZInt q z (k−1)`.
**The operator preserves the q-integer-curve class.** A computation, not an assertion.

**Branch-free by construction, which is the point.** Obstruction (ii) of this bean —
*"requires choosing a branch of the `z↦qz` correspondence on Σ"* — does not arise,
because the coefficients are symmetric functions of the sheets and hence single-valued in
`z`. The prolongation is taken where the obstruction does not live.

**Still not done, and not fudged:** this is not the jet-tower lift `Jⁿ E → Jⁿ⁺¹ E`,
`λ_SW^{(n)}` is not constructed, no period `∮` is computed, and there is deliberately
**no** comparison with the anchors `a_D^{(n)}` — those are functions of `q` alone while
`D_q [n]_z` is a function of `z` and `q`, so matching them would be numerology, not a
result. `D_q` is not constructed.


## Triaged 2026-10-10 — tagged `8f-open`; this is the arc's live research wall, not a scaffold

Read as part of finishing the `8f-lean` front's triage. No re-classification of
content needed — this bean is actively maintained, correctly scoped, and it ends
on the sentence a reader needs: **"`D_q` is not constructed."** Tagged `8f-open`
only so the front's queue separates research from repairs.

Two things worth surfacing for anyone scoping from the front list:

- **It is the downstream home of `qou-an6y`**, closed today. `an6y` established
  (scope-(a), PR #6652 merged) that the Jackson + q-`d/dz` residue tower fails C1
  from level 2 on the actual Σ seed, and that with free weights the level-axis
  constraint is underdetermined — 6/10/14/18 weight values at `m = 0..3`, of
  which 6/4/4/4 new, all linear, against one constraint per level. Its prune
  lands here: **do not fit the weights to the recurrence, a fit always exists.**
  The content is in where `D_q`'s weights come from, which is this bean.
- **Its own best reusable finding is a Lean one and is not about this wall.** Two
  of three gaps closed in it were blocked by their *formulation*, not by missing
  Mathlib: clearing denominators turned the Möbius fixed-point condition into a
  quadratic (no chart at `∞` needed), and clearing the inverse turned DVRSZ
  (2.4.1) into a hypothesis with no invertibility side-condition. A prior pass
  had recorded one of them as needing "Möbius machinery Mathlib does not carry".
  Worth remembering the next time a gap on this arc is blamed on Mathlib.

## Progress (2026-11-16, PR #8200)
- [x] Formalized `spectralCubicE1`, `spectralCubicE2`, `spectralCubicE3`, `spectralCubicP1`, `spectralCubicP2`, `spectralCubicP3`, `spectral_cubic_p1_p2_closed_form`, and `spectral_cubic_power_sums_and_ramified_parity` in `folio/quantum-observable-universe/lean/QOU/Eightfold/TauAnchoredRatioChiralBraidWritheAndSpectralCubicPowerSums.lean` + 50-dps mpmath witness (`qou_d8de_spectral_cubic_power_sums_and_ramified_parity`) in PR #8200 (`ec7070e7f1b47f4548cd7f98fc2a7948b28854b0`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8200, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-09-13: "lean(qou-d8de): close the prose-only finite-order step -- it was pigeonhole, not Moebius"). The work may be partly or fully done. Read the bean before you close it.
