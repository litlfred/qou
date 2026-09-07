---
# qou-d8de
title: 'GAP W1: construct the q-difference prolongation D_q from the color spectral curve Σ'
status: todo
type: task
priority: normal
created_at: 2026-08-01T01:43:06Z
updated_at: 2026-09-05T08:12:57Z
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
