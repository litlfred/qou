# S₅↓S₃ branching backbone of the s5-so3 keystone — VERIFIED; functor status tiered

**Date:** 2026-06-16
**Branch:** `claude/brave-hopper-ghhp9a`
**Status:** combinatorial backbone verified; geometric fibre map + physics still open
**Discipline:** formalize-first (verify the structural backbone before any physics claim) +
corpus-grep + critical-distance license.

## TL;DR

The 2026-06-13 "functor resolution" doc
([`2026-06-13-s5-so3-fiber-action-functor-resolution.md`](2026-06-13-s5-so3-fiber-action-functor-resolution.md))
proposes that the open fibre functor of `conj:s5-so3-fiber-action` is the restriction
functor $\mathrm{Res}^{S_5}_{S_3}$, and rests on three combinatorial claims (two branchings
+ a sign-rep difference). **All three are now verified** by a self-contained computation
([`scripts/s5so3_branching_backbone_verify.py`](scripts/s5so3_branching_backbone_verify.py)).
**But** the doc's header status *"Functor Identified"* over-reads what the verification
buys: the **combinatorial** side of the functor is a verified candidate; the **geometric
fibre map** (partition of 5 → A₅ rotation on Bring's surface), the **Markov-trace shift
evaluation**, and the **210 ppb muon resolution** remain open — by the functor-resolution
doc's *own* §4. The just-merged synthesis
([`2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md`](2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md))
omitted this doc entirely; a one-line cross-reference + verified-combinatorics note is added
there.

## 1. What was verified (Tier: VERIFIED — pure combinatorics, exact, no fit)

The branching rule for symmetric-group irreps ($\mathrm{Res}^{S_n}_{S_{n-1}}\lambda = \bigoplus_\mu \mu$
over single removable corner boxes) applied twice gives $S_5\downarrow S_3$. Dimensions by the
hook-length formula. Verified output:

```
=== S5 irrep dims (hook-length) ===
  dim (3, 2) = 5
  dim (2, 2, 1) = 5
  dim (3, 1, 1) = 6

=== Branching S5 -> S3 (two box removals) ===
  (3,2)   downto S3 = (3) + 2*(2,1)
  (3,1,1) downto S3 = (3) + 2*(2,1) + (1,1,1)

=== electron(3,1,1) - muon(3,2) restriction difference ===
  difference = (1,1,1)            (== exactly the sign rep)

=== dim conservation (sum dim_{S3} mu == dim_{S5} lambda) ===
  (3,2):   sum = 5, dim_S5 = 5, match = True
  (3,1,1): sum = 6, dim_S5 = 6, match = True
ALL BACKBONE CLAIMS VERIFIED: True
```

This confirms, exactly, the three load-bearing claims of the functor-resolution doc:

| Claim (functor-resolution doc) | Where | Verified |
|---|---|---|
| $(3,2)\downarrow S_3 = (3)\oplus 2\cdot(2,1)$ | §2 ℓ=2 step 3 | ✅ |
| $(3,1,1)\downarrow S_3 = (1,1,1)\oplus 2\cdot(2,1)\oplus(3)$ | §2 ℓ=1 step 3 | ✅ |
| electron(ℓ=1) − muon(ℓ=2) restriction difference $=$ sign rep $(1,1,1)$ | §3 + cross-ref to the operator-branching §5 | ✅ |
| $(3,2),(2,2,1)$ are the dim-5 $S_5$ irreps ($H\subset A_5$); $(3,1,1)$ is dim-6 ($T_1\subset A_5$) | §2 | ✅ (dims 5,5,6) |

The $(2,1)$-with-multiplicity-2 in *both* branchings also reproduces the 2026-06-01 audit's
correction of the "$S_3$ trace only sees $\ell\le 1$" false premise: the standard block $(2,1)$
— the carrier of the Borromean $h^4=-3/4$ coefficient — appears at both ℓ=1 and ℓ=2.

### 1a. The geometry→combinatorics bridge (also VERIFIED — two further branchings)

The functor-resolution doc routes *spherical-harmonic level ℓ* (the SO(3)/icosahedral
generation grading) to the $S_5$ Wedderburn blocks via two more branchings, both now verified by
the same checker:

| Branching | Result | Verified |
|---|---|---|
| $\mathrm{SO}(3)\downarrow A_5$ (icosahedral), via $\chi_\ell(\theta)=\frac{\sin((2\ell+1)\theta/2)}{\sin(\theta/2)}$ | $V_1\!\to\!T_1$, $V_2\!\to\!H$, $V_3\!\to\!T_2\oplus G$ | ✅ |
| $S_5\downarrow A_5$ (self-conjugate splits; James–Kerber) | $(3,1,1)$ self-conj $\to T_1\oplus T_2$; $(3,2),(2,2,1)\to H$; $(4,1),(2,1,1,1)\to G$; $(5),(1^5)\to A$ | ✅ |

Composing gives the full chain the doc asserts:

- **electron** ℓ=1 → $T_1$ → block $(3,1,1)$ → $(1,1,1)\oplus2(2,1)\oplus(3)$
- **muon** ℓ=2 → $H$ → block $(3,2)$ → $(3)\oplus2(2,1)$
- **difference** $=(1,1,1)$ sign rep $=$ the **alt channel** $W_{\mathrm{alt}}(-q^{-1})^{2m+1}$ of the
  existing $H_3$ lepton mass formula ([`lepton-bring-surface-h3-3channel.md`](../../content/quantum-observable-universe/mass-theory/lepton-bring-surface-h3-3channel.md)).

Two structural facts worth flagging (verified, but unremarked in the source docs):

- **$(3,1,1)$ hosts BOTH $T_1$ and $T_2$.** So tau's $T_2$ part (ℓ=3) shares the *same* $S_5$ block
  as the electron's $T_1$; tau's $G$ part sits in $(4,1)$. The electron and tau are not in disjoint
  blocks.
- **Embedding independence (your frame correction).** $\mathrm{Res}^{S_5}_{S_3}$ is a priori
  embedding-dependent. The naive $123\!\to\!123$ vs. the spacetime-frame-fixing $123\!\to\!345$ give
  **identical multiplicities** — the two $S_3$'s are conjugate in $S_5$, so every $g\in S_3$ has the
  same $S_5$ cycle type under both embeddings (verified: both give the multiset
  $\{1^5,(2,1^3)^{\times3},(3,1^2)^{\times2}\}$). **The multiplicities are embedding-invariant; the
  geometric realization is NOT** — it must fix the spacetime strands, i.e. use $123\!\to\!345$
  (S₃ on $\{3,4,5\}$, frame $\{1,2\}$ held fixed). This pins which strands close in the Markov trace
  (obligation §2.2) and is recorded here so the geometric step does not silently default to the
  conjugation-equivalent-but-physically-wrong $\{1,2,3\}$ embedding.

## 2. What is NOT closed by the above (Tier: OPEN — by the functor-resolution doc's own §4)

The verified combinatorics is a **necessary** consistency check on a *candidate* functor. It is
**not** a derivation of the conjecture. Three obligations remain — these are the
functor-resolution doc's own "Next Steps" §4, restated as open:

1. **Geometric fibre map is still open.** That the *combinatorial* restriction $\mathrm{Res}^{S_5}_{S_3}$
   coincides with the *geometric* map `partition_to_rotation` (partition of 5 ↦ a specific A₅
   rotation on Bring's quintic surface) — the actual content of `conj:s5-so3-fiber-action` — is
   asserted, not shown. The branching being consistent does not single out the restriction
   functor as *the* geometric map; many functors $H_5\to H_3$ produce compatible block data.
2. **Markov-trace shift not evaluated.** The physics needs the algebraic shift in the $H_3(q)$
   Markov trace induced by routing the knot through the $E_{(3,2)}$ (ℓ=2) projector vs. the
   $E_{(3,1,1)}$ (ℓ=1) projector — i.e. the correction factor $F(E_{(3,2)},q_0)$. The exact trace
   value $\chi^{(1,1,1)}(\beta_{\mathrm{Bor}})=1$ is one necessary number, not the factor.
3. **210 ppb muon tension not resolved.** Whether the shift closes the GAP-A-4 muon gap is the
   open empirical question; the verified branching says nothing about its magnitude.

### 2a. Candidate geometric realization — Reeb flow on the exceptional divisor

The corpus already carries a *geometric* construction that realizes the $S_3$ side: the q-Reeb flow
on the exceptional divisor $\mathcal{S}_p\cong\mathbb{CP}^1=S^2$ (Reeb/Hopf bundle $S^3\to S^2$),
threading the six $S_3$ braid words into six knot operators with boundary monodromy $=$ the $S_3$
Galois action ([`exceptional-divisor-reeb-intro.md`](../../content/quantum-observable-universe/mass-theory/exceptional-divisor-reeb-intro.md),
[`q-reeb-flow-on-color-coords`](../../content/quantum-observable-universe/mass-theory/q-reeb-flow-on-color-coords.md)). Since
$S^2$ is exactly where $\mathrm{SO}(3)\supset A_5\cong I$ acts, this is the right arena for the
*geometric* fibre map — but **as built it realizes only the cyclic $C_5$ (Lagrange-resolvent
diagonalization) and is a 3-strand construction**, i.e. the $S_3$ *target*, not the $S_5$ *source*.
Promoting it to the full icosahedral $A_5$ action threading the Reeb flow is a five-ingredient
construction program, scoped separately:
[`docs/scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md`](../scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md).
The cheap formalize-first link (the two bridging branchings §1a) is now discharged. **Follow-up
(2026-06-16): ingredient 1 fully settled** (the $2I$ spin lift exists via the SU(2) structure group +
the $S_3\!\to\!\mathrm{Dic}_3$ precedent; the geometric $A_5$ is forced to the icosahedral $T_1$),
**ingredient 4's algebraic leg is concrete** (Hecke-tower restriction = the verified branching, projector
traces computable in `pyhecke`), and **ingredient 5 (the 210 ppb muon mechanism) is REFUTED** — every
named Wedderburn-projector correction overshoots the gap by 6–8 orders of magnitude. Full close-out +
compute: [`docs/scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md` §"Ingredient 4+5 close-out"](../scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md)
+ [`scripts/s5so3_ingredient_4_5_markov_shift.py`](scripts/s5so3_ingredient_4_5_markov_shift.py). The sole
remaining structural unknown is the **geometric Reeb = functor identification** (ingredient 4 geometric leg).

## 3. Critical-distance flag — two status over-reads to correct

- **"Functor Identified" (functor-resolution doc header) is an over-read.** Accurate status:
  *"combinatorial branching candidate ($\mathrm{Res}^{S_5}_{S_3}$) verified; geometric realization +
  Markov-shift + physics open."* The verification in §1 strengthens the candidate but does not
  identify the functor in the sense the conjecture requires (a *geometric* map). This is the same
  §4-vs-§5 internal tension already flagged for the operator-branching doc in the synthesis §4
  ("§4 says open, §5 says closed") — the functor-resolution doc inherits it in its header.
- **The synthesis doc (2026-06-16) omitted this evidence.** Its §7 cross-references list neither the
  functor-resolution doc nor the verified combinatorial backbone. Its "awaiting the functor" framing
  is **correct for the geometric map** but **incomplete**: it should record that the *combinatorial*
  side has an identified, now-verified candidate. A cross-reference + one-line note is added to the
  synthesis §3 and §7 in the same commit.

Net: nothing here wires to production; this is a verified structural lemma + a status correction.
The keystone (`conj:s5-so3-fiber-action`) remains the single open object for m_τ, Δ_λ binding, and
λ(K) mass, exactly as the synthesis concludes.

## 4. Canonical-home note for the verification script

[`scripts/s5so3_branching_backbone_verify.py`](scripts/s5so3_branching_backbone_verify.py) is a
dependency-free audit checker (stdlib only — branching rule by box removal + hook-length formula),
sited under `docs/audits/scripts/` per the existing precedent
(`docs/audits/scripts/build-conjecture-cones.py`). It deliberately does **not** import the
`pyhecke` / `hecke-engine` compute stack: the claim it checks is pure $S_n$ representation
combinatorics, so a self-contained checker is the appropriate (and auditable) form. If a
Markov-trace–level follow-up is opened (obligation §2.2), that compute belongs in
`computations/` and should consume `pyhecke`.

## 5. Cross-references

- [`2026-06-13-s5-so3-fiber-action-functor-resolution.md`](2026-06-13-s5-so3-fiber-action-functor-resolution.md) — the candidate functor + the three claims verified here
- [`2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md`](2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md) — the synthesis (cross-ref added)
- [`2026-06-13-gap-a4-operator-valued-muon-branching.md`](2026-06-13-gap-a4-operator-valued-muon-branching.md) — the (1,1,1) sign-block subtraction §5 (the difference verified here)
- [`2026-06-01-s5-so3-su2-u1-fiber-action.md`](2026-06-01-s5-so3-su2-u1-fiber-action.md) — the "(2,1) appears at both ℓ=1 and ℓ=2" correction, corroborated here
- [`2026-06-05-gap-a4-final-retrospective.md`](2026-06-05-gap-a4-final-retrospective.md) — 22 closures → one conjecture
- `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean` — the keystone scaffold (open geometric map)
