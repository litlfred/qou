# τ-assignment coherence program: orbit invariants, 1ppq relevance, and the Habiro bridge

**Date**: 2026-07-26 · **Branch**: `claude/5two-habiro-tail-bar-odd-l0k3ol` ·
**PRs**: #4340, #4362, #4366, #4373 (all merged or in flight)

## 1. What was proved (the program record)

| Result | Where | Status |
|---|---|---|
| `(fᵢfⱼ)^m = 1` at every bond order; `simple_injective` for EVERY Coxeter system, zero hypotheses | `CoxeterGeometricRepresentationFull.lean` (#4340) | sorry-free |
| Strict pair-independence of the τ-assignment REFUTED at A₃ (explicit witness) | `HeckeTauAssignmentCanonicity.lean` (#4340) | sorry-free, scope-(a) |
| Diagram-symmetry edges coherent (pullback) | `HeckeTauAssignmentCoherence.lean` (#4340) | sorry-free |
| W-conjugation edges coherent; pair-swap obstructed **target-side** (no function `T` with `τ' = T∘τ`) | `HeckeTauAssignmentSwapConjugation.lean` (#4362) | sorry-free |
| THE ASSEMBLED FUNCTOR: marked-pair category; `tauAssignment_hom_coherent` engine; natural transformation; `Core` groupoid restriction | `HeckeTauAssignmentGroupoidFunctor.lean` (#4366) | sorry-free |
| Pasted square (tower × groupoid); `PairCoherent` gauge discipline; cell Markov trace = ORBIT INVARIANT | `HeckeTauAssignmentOrbitInvariants.lean` (#4373) | sorry-free |
| Diagram symmetries preserve length; `q = i` monodromy DIAGRAM-equivariant | `HeckeTauAssignmentMonodromyEquivariance.lean` (#4373) | sorry-free |

Canonicity resolution: **not** a pair-independent map (refuted) but a
coherently indexed family — a natural transformation on the marked-pair
groupoid.

## 2. Relevance to the categorical-action → mass-binding 1ppq path

**No numeric delta.** Nothing here changes any MeV value; L1/L2
dashboards untouched (L2 stays 2/7). The machinery lives at the fibre
monodromy point `q = i`, not at the archimedean `q₀`.

**Three structural contributions to the canonical chain:**

1. **The "canonical" in `tr_M` is now machine-checked at the gauge
   level.** The chain step "categorical action → Hecke → Markov trace"
   involves gauge choices (which pair, which parabolic, which cell).
   `cellMarkovTrace_pairCoherent` proves the trace — the object the
   mass formula consumes (`F_Bor = |tr_M(β_Bor)|·[3]_q!/q³`) — is
   marked-pair-gauge independent; `trM4_iota34_stabilizes` (merged
   earlier) covers the rank-tower direction. Both coherence directions
   of `tr_M` are proved.
2. **What is NOT canonical is identified.** Isotypic-slot *coordinates*
   are pair-dependent (swap obstruction). Wiring a slot coordinate into
   a "derived" number would be a hidden gauge choice = hidden degree of
   freedom; this failure mode is provably closed.
3. **A formalize-first prune for the Δ_λ gate.** Any candidate derived
   Δ_λ (Track A binding `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ`) must pass
   orbit-invariance (`PairCoherent`) + pasted-square compatibility
   BEFORE numerics. A pair-gauge-dependent candidate is dead on
   arrival. This is the §compute-author formalize-first discipline with
   the pruning invariant already formalized.

## 3. Literature check: orbit structures and Habiro-ring actions

**External (verified 2026-07-26):**

- **Garoufalidis–Scholze–Wheeler–Zagier, *The Habiro ring of a number
  field*** ([arXiv:2412.04241](https://arxiv.org/abs/2412.04241)):
  the Habiro ring of `K` and **modules over it graded by `K₃(K)`**;
  elements are collections of power series **at each root of unity**
  glued by a **Frobenius endomorphism**, with corrections governed by
  Bloch-group elements and the p-adic dilogarithm. I.e., exactly a
  local system over evaluation points with arithmetic transition maps.
- **Wagner, *q-Hodge complexes over the Habiro ring***
  ([arXiv:2510.04782](https://arxiv.org/abs/2510.04782)): module /
  cohomology theory (q-de Rham with q-Hodge filtration) over the Habiro
  ring — representations *over* the Habiro ring exist and are active.
- Habiro's original unified WRT invariant lives in the Habiro ring with
  evaluations at all roots of unity ([arXiv:math/0605314](https://arxiv.org/abs/math/0605314)).

**In-corpus anchors (corpus-grep, same date):**

- `alpha-em-habiro-bar-involution` block: the α_EM Habiro element
  `H(q) = [2]_q(1 − h²α)` is bar-involution-fixed with **exact modular
  zero `H(ζ₄) = 0`** — evaluated at the SAME 4th root of unity as the
  monodromy point `q = i` of the τ-assignment tower.
- `docs/audits/2026-06-01-qbeta-habiro-zeta8-categorical-witness.md`:
  ζ₈ evaluations already in play.
- `docs/coordination/2026-06-02-qbeta-habiro-element-scope.md` Phase B:
  **Galois descent on the Habiro ring** is an already-sanctioned route.

**The bridge this suggests (research framing, nothing claimed):** the
τ-assignment/monodromy apparatus at `q = i` is the **ζ₄ fibre** of what
the Habiro-ring viewpoint would organize as a root-of-unity-indexed
family. The marked-pair groupoid supplies the *horizontal* edges
(change of pair at fixed evaluation point); GSWZ Frobenius/Galois
structure supplies candidate *vertical* edges (change of evaluation
point). Two concrete observations:

1. **The bar involution at ζ₄ is complex conjugation** (`|i| = 1` so
   `q ↦ q⁻¹` is `z ↦ z̄`), and the `TauAssignmentData.rho_compat` law
   (star-compatibility of `toFun`/`toFunBar`) is exactly the statement
   that the assignment is equivariant for this ℤ/2 action. The first
   vertical edge is therefore ALREADY PROVED in the merged corpus —
   it just wasn't stated in this language.
2. A genuine `q₀`-bridge (where the 1ppq battle is) would require the
   family over all roots of unity plus the Habiro/Frobenius gluing —
   the same object #1713 Phase B targets for the c_k. The groupoid
   coherence proved here is a *precondition*: without pair-gauge
   independence, a root-of-unity family would not even be well-defined.

## 4. Open items (beaned)

1. Conjugation-edge monodromy equivariance — inner automorphisms do
   not preserve length; diagram half proved
   (`monodromyN_diagram_equivariant`), conj half OPEN (decide or
   refute with the length-rule obstruction made explicit).
2. `PairCoherent` prune interface for Δ_λ candidates — wire the
   orbit-invariance gate into the Δ_λ candidate checklist
   (documentation + a Lean predicate any candidate must instantiate).
3. Habiro ζ₄ bridge — state `rho_compat` as ℤ/2 (bar) equivariance at
   ζ₄ in Lean; scope the root-of-unity family (GSWZ-style) for the
   assignment tower. Research-grade; coordinate with the 1ppq-qbeta
   ledger (#1713 Phase B).

## 5. Scope discipline

All results scope-(a) or proved exclusions with explicit invariants;
no fits; nothing wired to production compute; L2 count unchanged (2/7).
The Habiro-bridge section is research framing with citations, not a
claim.

## Addendum (same date) — the three beans worked

**qou-yvel — DECIDED as a criterion**
(`HeckeTauAssignmentGaugeGate.lean` §1).
`monodromyN_equivariant_iff_descent_transport`: monodromy equivariance
along a marking homomorphism holds for all states **iff** the
homomorphism transports the descent condition pointwise. Sufficient
condition in clean general form: any **length-preserving** marking
homomorphism is equivariant (`monodromyN_equivariant_of_length_preserving`
— subsumes the diagram-edge theorem; covers `w₀`-conjugation in finite
systems). Analysis of a generic conjugation edge (scope-(a), prose
only): in A₃ the 4-cycle `c = (1234)` carries pair `(0,1)` to `(1,2)`;
the descent criterion at `l = 0` reads `c(x(1)) > c(x(2)) ↔ x(1) > x(2)`
in the value-comparison form, and `c` is order-preserving except
`4 ↦ 1` — so any permutation `x` with `x(1) = 4` (e.g. the
transposition `(14)`, length 5) violates transport. Generic conj edges
are therefore expected to FAIL equivariance; a machine-checked
refutation needs `ℓ((14)) = 5`-grade length certificates and is left
open — the criterion reduces it to finite combinatorics per edge.

**qou-fc35 — the master gate LANDED**
(`HeckeTauAssignmentGaugeGate.lean` §2).
`pairCoherent_of_cell`: every functional factoring through the
six-element cell restriction is pair-coherent, in one stroke;
`pairCoherent_comp` closes the class under post-composition. This is
the Δ_λ prune gate in executable form: a candidate routed through
marked-pair cell data passes automatically; anything else must supply
its own coherence proof or is dead on arrival.

**qou-vegn — first vertical edge NAMED; family scoping recorded**
(`HeckeTauAssignmentGaugeGate.lean` §3).
`zeta4_inv_eq_star` (`i⁻¹ = conj i`) +
`tauAssignment_zeta4_bar_equivariance`: the `rho_compat` law of every
`TauAssignmentData` **is** ℤ/2 bar-equivariance at the ζ₄ fibre. The
GSWZ and Wagner papers are now in-repo
(`uploads/2412.04241v2.pdf`, `uploads/2510.04782v2.pdf`, commit
4c05849); sandbox PDF extraction is currently broken (system
`cryptography`/pypdf conflict), so the deep-read of the Frobenius
gluing definitions (needed to state candidate vertical edges beyond
bar) remains queued on the bean. Bean stays in-progress.

## Addendum 2 (same date) — GSWZ deep-read: the 4₁ knot IS their running example; concrete downstream uses

PDF extraction unblocked (`pip install cffi` repaired the system
`cryptography`/pypdf conflict; poppler unavailable, apt fetch blocked).
Read: §1.2–1.5 (definitions), §4.5–4.6 (examples) of
`uploads/2412.04241v2.pdf`.

### What GSWZ actually provides (verified against the text)

1. **Definition 1.1 (the gluing)**: an element of the Habiro ring of
   `R = O_K[1/∆]` is a collection `f_m(x) ∈ R[ζ_m][[x]]`, one per root
   of unity, with `f_m(x + ζ_pm − ζ_m) = (φ_p f_pm)(x)` in
   `R_p^∧[ζ_pm][[x]]` — Frobenius-twisted p-adic re-expansion gluing.
   These are the **vertical edges** in executable form: ζ_m ↔ ζ_pm per
   prime p.
2. **§1.5 (the K₃-graded modules)**: `H_{R,ξ}` for `ξ ∈ K₃(K)`;
   leading terms at ζ_m carry the unit root `ε_m(ξ)^{1/m}` from the
   étale Chern class, with **χ⁻¹-Galois-equivariance** — explicit
   Galois action data on leading coefficients.
3. **The motivating example is the figure-eight knot 4₁** — the QOU
   muon-anchor knot. Its Kashaev asymptotic series `Φ(h)` (their
   eqn (1)) lives in `H_{R,ξ}` for `K = Q(√−3)` with
   `ξ ∈ K₃(Q(√−3))` whose **regulator is Vol(4₁) = 2 Im Li₂(e^{iπ/3})
   = 2.0299…** — the exact constant of CAL-2's proxy
   `m_μ/m_e = Vol(4₁)/ℏ_q²`. The completion `exp(iVol/h)Φ(h)` becomes
   p-adic via the **p-adic dilogarithm**.
4. **Symmetrization integrality (their eqns (1)–(2))**: `Φ(h)` alone
   has wild denominators; the bar-symmetric `Φ(h)Φ(−h)` is **integral
   away from 3** in `(q−1)`. Arithmetic integrality prefers the
   bar-even sector.
5. **§4.5 eqn (278)**: an exact global generator of the 4₁ module via
   the infinite Pochhammer symbol at ζ₆ — cheap high-precision
   representation (they computed 600 terms).
6. **§4.6**: the scissors-congruent pair 5₂ / (−2,3,7)-pretzel gives
   two elements of the SAME module (equal Bloch class mod 6-torsion).

### Downstream-use map (how to use)

- **U1 — the muon anchor as an arithmetic object.** CAL-2's
  `Vol(4₁)` is the Borel regulator of the GSWZ class ξ; the anchor
  acquires p-adic shadows `D_p(ξ)` and Galois data `ε_m(ξ)` for free.
  Any future substrate-derivation attempt on q₀ (Subgoal-2) can now be
  tested against arithmetic constraints, not just the one real number.
- **U2 — cross-anchor rigidity for the Q_β Habiro element (#1713).**
  The sought fibre-level element `F(q)` reproducing c_k at every
  anchor should live in a GSWZ module. Membership imposes: coefficient
  integrality away from ∆, Frobenius gluing across ζ_m, and the
  ε_m-unit leading-term structure. These are refutation-grade tests a
  c₃ candidate can FAIL without any anchor inversion — the missing
  constraint class behind the historical c_k flip-flop
  (under-determination).
- **U3 — arithmetic justification of the bar-parity discipline.** GSWZ
  integrality holds for the symmetrized (bar-even) combination. The
  corpus's bar-even/bar-odd split (m_π cosh vs Q_β sinh;
  `CuspShapeBarParity`) matches: falsifiable check — corpus 4₁-derived
  series (e.g. the lever1 Habiro-tail closed form) should show the
  3-integrality pattern in their bar-even symmetrization. A cheap
  probe target.
- **U4 — vertical edges for the τ-tower.** The ζ₄ fibre
  (`rho_compat` = bar edge, proved) sits inside the gluing lattice
  ζ_m ↔ ζ_pm. First concrete check: the corpus already holds ζ₄
  (α_EM zero) and ζ₈ (Q_β witness) evaluations — the p = 2 edge
  ζ₄ → ζ₈ is a Frobenius-gluing test on EXISTING corpus data.
- **U5 — module-mates organize the knot table.** Scissors-congruent
  knots share a module. Borromean/Whitehead (Vol(𝓑₃) = 2·Vol(Wh) = 8G)
  and other corpus volume identities should be re-read as Bloch-class
  relations ⇒ module relations — an organizing principle for the
  knot-particle spectrum with proof leverage (their 5₂/pretzel
  precedent).

Beans: U2 and U3+U4 spun off as new probes; U1/U5 recorded as framing
for existing epics. `qou-vegn` deep-read portion complete; family
formalization continues there.

## Addendum 3 (2026-07-27) — beans 1hlh / c0aw / vegn worked: probes green, gate executable, ζ₄ facts formalized

**qou-c0aw (U3+U4) — COMPLETED, both probes 100% green.**

- `computations/probes/gswz_symmetrization_integrality_probe.py`
  (7/7): from the printed GSWZ 4₁ data (their eqns (1)–(2)), the
  bar-even symmetrization's odd coefficients cancel EXACTLY, the h²
  coefficient collapses to the sqrt-free, 3-integral `−1/27`
  (the nontrivial `(2·697/1152·27⁻¹) − (11/72)²·(−3)⁻¹`-type
  cancellation verified in exact arithmetic), and the x = q−1
  conversion reproduces GSWZ eqn (2) at x², x³. The corpus bar-parity
  discipline now has a machine-verified arithmetic instance.
- `computations/probes/zeta4_zeta8_habiro_gluing_probe.py` (5/5): the
  p = 2 edge ζ₄ → ζ₈ is 2-adically genuine (Norm(ζ₈−ζ₄) = 2), both
  fibre expansions of the categorical `[2]_q` are integral, the
  re-expansion gluing holds exactly to order 5, and the fibre constant
  at ζ₄ is the corpus modular zero. Honest scope: classical Habiro
  ring (K = Q, trivial Frobenius) — the harness, smallness, and zero;
  the number-field twist test needs multi-fibre Φ-series data.

**qou-1hlh (U2) — gate v1 LANDED, bean stays in-progress.** The
symmetrization probe doubles as the first executable module-membership
gate: check 7 shows a generic rational perturbation of one coefficient
(the shape of a fitted c_k) breaks 3-integrality of the symmetrization
— refutation without any anchor comparison. Remaining on the bean: the
Frobenius-gluing membership test over Q(√−3) (needs the Φ-series at
several roots of unity; GSWZ eqn (276)/(278) give exact generators to
compute them).

**qou-vegn — ζ₄ facts formalized, family half still open.**
`HabiroZeta4Bracket.lean` (sorry-free): `two_bracket_zeta4_eq_zero`
(`[2]_{ζ₄} = 0` — the α_EM modular zero at the monodromy point, pinned
at the categorical-factor level) and `two_bracket_bar_fixed`
(`[2]_{q⁻¹} = [2]_q`, unconditional). The root-of-unity family for the
τ-tower remains the bean's open half.

## Addendum 5 (2026-08-01) — T1 mod-p dilog layer green; Copilot hardening

**qou-dugz (T1) — mod-p dilog layer LANDED, 4/4.**
`gswz_padic_dilog_modp_probe.py`: Kontsevich's finite polylogarithm
`li_{2,5}` + GSWZ Prop 3.2 (`p⁻²D_p(ζ^p) ≡ li_{2,p}(ζ)/(ζ−1)^p mod p`)
in exact `Z/5⁶` arithmetic. Since `25 ≡ 1 mod 24`, every `ζ₂₄^k` is a
5th power, so ALL three printed `D₅` values of GSWZ eqn (273) are
reachable — and all three match (at `ζ₂₄`, `ζ₂₄²`, `ζ₂₄⁶`), plus the
`li_{2,5}(1) ≡ 0` sanity. Transcription note: the middle row of (273)
is `D₅(ζ₂₄²)` — pypdf mangles the superscript; the exponent-5 reading
was Frobenius-INCONSISTENT (the Prop-3.2 predictions at ζ and ζ⁵ are
Frobenius conjugates), which is how the error was caught and the
exponent-2 reading confirmed. The full Coleman `Li₂` (higher precision,
non-root arguments for the printed (271)) stays queued.

**Copilot review (first in 7 PRs) — correct, accepted, fixed.** The
Teichmüller stabilization check was vacuously true on loop exhaustion
and `any()` accepted orders 8/12. Fixed (break-only flag; `all()` over
maximal proper divisors); witnesses regenerated, still 9/9 — the
math stood, the checks are now falsifiable. Lesson recorded: witness
checks must be constructed to be able to fail.

Gate stack status: symmetrization integrality ✓, Frobenius lift ✓,
Teichmüller ✓, mod-p dilog ✓; remaining for the full membership
harness (bean qou-9p9y): Coleman Li₂ precision layer + ε_m units.

## Addendum 6 (2026-08-01) — T2: gate run on the corpus binding Habiro tails, 6/6

First in-corpus gate run (`habiro_tail_membership_gate_probe.py`, bean
qou-1ddd): the binding Habiro tails `D(n)`, n = 4..9, recomputed from
the q-hook-length na-Stokes period with the corpus's BALANCED
q-integer convention (anchored against the printed n ≤ 4 table rows —
the anchor caught an initial unbalanced-convention transcription,
exactly as designed). All gates pass: integer Laurent coefficients
(classical-Habiro membership), bar-evenness, the universal `(q−1)²`
double root, and fibre-level reality at ζ₄.

**New fibre data (observations only, no interpretation claimed):**
`D(n)(ζ₄)` = −2, 8, −16, 16, −36, **0** and `D(n)(ζ₈)` = −√2, −4, 4,
8, −20, 24 for n = 4..9. Notable: `D(9)` has an exact modular zero at
the monodromy point ζ₄ (the α_EM-element zero class), and
`D(4)(ζ₈) = −√2 = −[2]_{ζ₈}` (the bracket-family fibre value with a
sign). Both recorded in the witness for the ζ-indexed picture; whether
either is structural or coincidental is OPEN and not claimed.

## Addendum 7 (2026-08-01) — T3 harness v1: the Bloch-group decomposition verified mod 5³

**qou-9p9y — harness v1 LANDED (6/6); bean stays in-progress for the
Coleman layer.** `gswz_membership_harness_v1_probe.py` assembles every
layer built this program (Frobenius lift, Teichmüller, mod-p finite-
polylog dilog, archimedean integrality/bar gate) into one harness with
a candidate interface (pass/fail demo included), and adds the genuinely
new module-side check: **GSWZ eqn (274) — the decomposition of the 5₂
knot's Bloch/K₃ class over root-of-unity symbols — verified mod 5³**
by combining the printed coefficients (mod 5) with the Prop-3.2 dilog
values (mod 5³), matching the printed `D₅(ξ)` of eqn (271) exactly.
Normalization, stated explicitly: every `D₅` value is divisible by 25,
so the mod-5³ statement is checked in the form `D₅(·)/25 (mod 5)` —
the displayed congruence
`1·[2,4,4] + 3·[1,3,2] + 1·[2,3,3] ≡ [2,1,3] (mod 5)` in
(const, α, α²) coordinates is that normalized form, i.e. a genuine
mod-5³ identity on the unnormalized `D₅` values (the coefficients
enter only mod 5 precisely because of the 25-divisibility).
This is Theorem 9 exercised on printed
data — the ε_m-class module-side layer of the membership test, live.

**Single named missing ingredient**: the Besser–de Jeu overconvergent
`Li₂` expansion (GSWZ reference [8]) is not among the uploaded sources;
until it lands, the dilog layer is mod-5³-exact and the full-precision
membership test (and ε_m units beyond mod-p) stays queued on qou-9p9y.
Uploading Besser–de Jeu (arXiv/journal: "The syntomic regulator for
K-theory of fields" / Besser's Coleman-integration papers) would
unblock the final layer.

## Addendum 8 (2026-08-01) — the Besser–de Jeu papers land; full-precision Coleman Li₂ COMPLETE (8/8)

**The single named missing ingredient arrived.** The owner uploaded
Besser–de Jeu, *"Li(p)-service? An algorithm for computing p-adic
polylogarithms"*, Math. Comp. 77 (2008) 1105–1134
(`uploads/S0025-5718-07-02027-3.pdf`), plus Besser's *"Finite and
p-adic polylogarithms"* (`uploads/0006051v1.pdf`) and Besser–de Jeu
arXiv:0707.3682 (`uploads/0707.3682v2.pdf`). Habiro's paper was
already present (`uploads/0605314v1.pdf`).

**qou-9p9y dilog layer COMPLETE.**
`gswz_coleman_li2_full_precision_probe.py` (8/8) implements the
Besser–de Jeu algorithm end-to-end:

- **Prop 4.3**: the `g₂`-series of `Li₂^{(p)}(z) = g₂(1/(1−z))`
  computed to 120 terms in exact rationals; all coefficients verified
  5-integral, and the Prop 6.1 valuation bound
  `v₅(a₂,k) ≥ k/4 − log₅k − c(2,5)` gives tail valuation ≫ the 5⁸
  working precision.
- **Prop 4.2** (telescoped Frobenius, f = 2 since 25 ≡ 1 mod 24):
  `Li₂(ζ) = (5⁴−1)⁻¹(5⁴·g₂(1/(1−ζ)) + 5²·g₂(1/(1−ζ⁵)))` at every
  Teichmüller point of the 5₂ trace field, exact in
  `(Z/5⁸)[x]/(x³−x²+1)`.
- **`D₅ = Li₂` at Teichmüller points**: the Iwasawa log kills roots of
  unity (`24·log ζ = 0`), so the full-precision `D₅` needs no separate
  log term there.

**Results against printed GSWZ data:**

1. **(273) rows 1 and 3 reproduced at every printed digit** (to 5⁴):
   `D₅(ζ₂₄)` and `D₅(ζ₂₄⁶)`.
2. **Row-2 superscript ADJUDICATED**: the cleaner re-extraction shows
   the pdf's row 2 reads `D₅(ζ₂₄⁵)`, while (274)/(275) decompose over
   `[ζ₂₄²]`. At full precision the printed digits match `Li₂(ζ₂₄²)` on
   all 9 compared digits and do **not** match `Li₂(ζ₂₄⁵)` — the
   printed superscript is a typo in the source; the earlier mod-5³
   inference (3 digits) is confirmed at 9.
3. **Internal Frobenius equivariance** `Li₂(ζ⁵) = φ₅(Li₂(ζ))` holds at
   the full 5⁸ working precision (Galois equivariance of Coleman Li₂
   exercised through the merged Hensel lift).
4. **Merged mod-p layer consistency**: `Li₂(ζ)/25 mod 5` equals the
   Prop-3.2 finite-polylog values for all three targets.
5. **(274) Bloch-group decomposition upgraded mod 5³ → mod 5⁴**:
   `c₁·D₅(ζ₂₄) + c₂·D₅(ζ₂₄²) + c₃·D₅(ζ₂₄⁶) = D₅(ξ)` with the printed
   coefficients, capped only by the two printed digits of `c₂`.

**Remaining on qou-9p9y**: the ε_m units at full precision (the
étale-Chern-class layer beyond mod p). The dilog bottleneck is gone;
the harness's number-field membership test can now run at any 5-adic
precision the printed/derived data supports. Scope-(a); nothing wired.
PR: #4490.

## Addendum 9 (2026-08-01) — 5₂ symmetrization + gluing digit verified; the 23-power denominator reading

`gswz_52_symmetrization_probe.py` (4/4) verifies GSWZ §4.6 printed
data for the 5₂ knot exactly, in `Q[α]/(α³−α²+1)`:

- **(283) x² coefficient**: `2φ₂ − φ₁²` from the printed (282) series
  equals the printed `(465α² − 465α + 54)/23³` exactly. The pdf's
  mangled "1/233" denominator is **adjudicated as 23³ = 12167** by the
  exact numerator match — structurally right, since
  `N(δ) = N(3α−2) = 23` is the 5₂ trace field's discriminant prime,
  so the symmetrized coefficients are integral away from Δ ∋ 23:
  GSWZ's integrality-away-from-Δ in miniature (and 5-integral, checked).
- **(283) x³ coefficient**: transcribed as the negative of x², and the
  math forces exactly that (only h² contributes below x⁴;
  `log(1+x)² = x² − x³ + (11/12)x⁴ − …`).
- **(286) Habiro gluing digit**: `(α²+4α)⁵ ≡ α²+3α+2 (mod 5)` — the
  p-power gluing between the ζ₅ fibre (284) and the m=5 constant term
  (285), checked in the exact ring.
- **Derived observation** (witness, not a claim): the printed x⁴
  digit-group determines the unprinted `φ₄` of (282); recorded for the
  (287) capstone.

Discipline note: the h-odd cancellation in `Φ̃(h)Φ̃(−h)` is an
identity for any coefficients, so it is deliberately NOT posed as a
check (constructed-to-fail rule from the Copilot #4397 lesson).

**Remaining on qou-9p9y**: the (287) Ψ-section division test — the
module-membership capstone consuming the full-precision Li₂ layer
(m=1 fibre needs no ε_m; Pochhammer expansion machinery required) —
and ε_m units at m > 1 (no printed GSWZ targets; needs the CGZ [10]
data).

## Addendum 10 (2026-08-01) — Ψ-section capstone: the mod-5 membership shadow PROVED-BY-COMPUTE; printed-(287) reproduction honestly OPEN

`gswz_psi_section_division_probe.py` (3/3 gating) implements the
m = 1 fibre of the GSWZ module generator Ψ_ξ (Definition 3.9) and runs
the (287) division experiment on the 5₂ series:

- **Construction**: ε₁ is trivial; the half-shifted Bernoulli/polylog
  expansion gives `log Ψ_[ζ],1 = −(1/24)Li₀(ζ)h + (7/5760)Li₋₂(ζ)h³ +
  O(h⁵)` with only EXACT rational polylog values (`B₁(1/2) = B₃(1/2)
  = 0` kill the Li₁ and h² terms; the Def-3.9 prefactor cancels the
  Coleman-Li₂ pole).
- **The 5-pole cancellation (PASSES, and is construction-specific)**:
  both `φ₃` of the printed (282) series (denominator `414720 =
  2¹⁰·3⁴·5`) and the Ψ h³ coefficient (`7/5760`) carry genuine
  5-poles; 5-integrality of the quotient's x³ coefficient — the mod-5
  shadow of module membership — holds for the principled construction
  and **fails** for Frobenius-twisted fibres, permuted assignments,
  and the wrong sign (1 surviving class of 14 in a 28-point grid; the
  other formal survivors are exact mathematical equivalents: Li₋₂ is
  odd under ζ → ζ⁻¹, and the two Bernoulli offsets coincide mod 5 via
  7 ≡ −8). This nontrivially links the 5₂ perturbative series' h³
  coefficient to the printed Bloch-decomposition coefficients c₁, c₂,
  c₃ through the Ψ-module structure.
- **OPEN (honest negative, recorded in the witness)**: digit-by-digit
  reproduction of the printed (287) x¹..x³ coefficients fails under
  every grid variant and under any scalar `(1+x)^λ` prefactor (the
  mismatch has α-components). Candidates: the pdf's displayed `f₅`
  subscript is genuine (m = 5 fibre unprinted → inputs unavailable);
  an unprinted α-dependent normalization factor in (281) (footnote 5
  warns of factor differences vs [26]); or digit-group transcription
  mangling. Computed quotient digits are recorded for future
  adjudication.

**Bean qou-9p9y state after this tranche**: dilog layer COMPLETE
(full-precision Coleman Li₂, Addendum 8); m = 1 Ψ-section built and
mod-5-validated; remaining: the (287) input-series identification
(above), ε_m at m > 1 (needs CGZ [10] printed data or an independent
ε construction), and m > 1 fibres generally.

## Addendum 11 (2026-08-02) — CGZ lands: the ε_m machinery implemented and verified vs printed Theorem 7.4 (γ = 2)

The owner uploaded CGZ (Calegari–Garoufalidis–Zagier,
arXiv:1712.04887v3, `uploads/1712.04887v3.pdf`) — GSWZ's [10], the
source of the ε_m units. `cgz_cyclic_qdilog_unit_probe.py` (4/4)
implements the computable realization:

- **Cyclic quantum dilogarithm** `D_ζ(x) = Π_{k=1}^{n−1}(1−ζ^k x)^k`
  (CGZ (8)), `P_ζ(X) = D_ζ(x)/D_ζ(1)` (CGZ (20)), in CGZ's own
  finite-field realization (§4.4: for `q ≡ −1 mod p` every element of
  `F_q` is an n-th power, `H = F_{q²}`, and `R_ζ = P_ζ` literally).
- **Lemma 2.4(a) engine identity (21)** `(1−X)^m D_ζ(ζ^m x)/D_ζ(x) =
  Π_{k<m}(1−ζ^k x)^n` verified exactly (the pdf flattens the `(1−X)^m`
  exponent; the exact check adjudicated it — first run with `(1−X)¹`
  failed, the corrected transcription passes on a 12-point (m,x)
  sweep per case).
- **Printed target, Theorem 7.4**: `R_ζ(η_ζ) = ζ²` for the n-torsion
  element `η_ζ` of CGZ (34), verified over SIX finite-field cases
  (n = 5: q = 19, 29, 79; n = 7: q = 13, 41, 83) with the γ-exponent
  **pinned to exactly 2** in each (specificity: j ≠ 2 classes all
  fail; ζ-class primitivity checked so the test has full resolution).

Also this addendum: Copilot review of #4490 addressed (witness `note`
now carries file pointers; the canonical-5-adic digit convention of
`matches_printed` documented — omitted digits below the highest
printed power are genuinely 0 by positional convention, so
zero-filling is exact, not an assumption; the `xx9f` GAP bean body
filled with context + next steps), and the Ψ-expansion coefficients
are now archimedean-validated inside the capstone probe (h³/h⁵ error
scaling — the `archimedean_expansion_validation` check).

**Path to ε_m 5-adic**: run the same `P_ζ` construction in
`(Z/5^W)[α]`-coefficient rings at fibre order m on the GSWZ 5₂
symbols `[ζ₂₄^k]` — the machinery is now validated end-to-end on CGZ's
printed data. Queued on `qou-9p9y`.

## Addendum 12 (2026-08-02) — 5-adic cyclic quantum dilog at the Q₂₅ place; PR #4490 MERGED

**PR #4490 merged** (rebase, `ce82d8d`): full-precision Coleman Li₂
(8/8), 5₂ symmetrization (4/4), Ψ-capstone (4/4 gating + open (287)
item, bean `xx9f`), CGZ finite-field ε-machinery (4/4, γ = 2). Copilot
review addressed (2 comments + suppressed bean-body note; the
zero-fill digit-convention suggestion answered with the canonical
5-adic-expansion argument rather than weakened).

**New (this branch): `gswz_epsm_5adic_cyclic_qdilog_probe.py` (4/4)** —
the cyclic quantum dilogarithm run 5-adically at the **Q₂₅ place** of
the 5₂ trace field (Hensel-split quadratic component ring; the first
full-product-ring attempt honestly failed — the Q₅ component has
μ = μ₄ only, so P_{ζ_m} does not live there for m ∤ 4):

- identity (21) exact 5-adically (multiplication-only form; the sweep
  first hit exact-zero factors at ω-power points, and non-unit
  inversions — both structural, both fixed by construction not fudge);
- Teichmüller class extraction total (unit classes mod m-th powers are
  pure Teichmüller data since 1+5Z₂₅ is m-divisible);
- **root-difference law verified**: class(P(ζ^r x)) − class(P(x)) =
  −r·class(1−X) mod gcd(m,24) across all root pairs — per-symbol
  ε-classes are root-dependent by exactly this law, which is the
  honest reason only the full Bloch combination is canonical;
- **structural finding**: within μ₂₄ an m-th root of ζ₂₄^j exists iff
  gcd(m,24) | j — so the j=1 symbol (hence the c-weighted ξ-class)
  needs the next unramified Kummer level μ_{24m}; computable base-place
  pairs (j=2, m=2; j=6, m ∈ {2,3,6}) have their class data recorded in
  the witness.

Next increments on `qou-9p9y`: the μ_{24m} Kummer level for the j=1
symbol; bean `qou-xx9f` for the (287) input identification.

## Addendum 13 (2026-08-02) — Kummer level: the 5₂ root-of-unity symbol ε-classes are ALL TRIVIAL (canonical, root-independent)

`gswz_epsm_kummer_level_probe.py` (6/6) lifts the gcd obstruction by
working in the unramified extensions `F = Q₅(μ_{24m})` (degree
`d = ord₅(24m)`, up to d = 48 at m = 24; seeded-deterministic
irreducible-polynomial construction, exact `(Z/5⁸)[x]/(h)` arithmetic):

- identity (21), root-difference law, base-place consistency, and
  **non-vacuity controls** (χ_m(ζ_M) = (5^d−1)/m ≠ 0; χ₂(1−ζ₄₈³) = 24)
  all verified;
- **RESULT (corrected in review — Copilot caught an overclaim in the
  first framing)**: cls(1−X) = 0 everywhere, so all per-symbol classes
  are root-independent (canonical). They are **zero for every m | 12
  and for [ζ₂₄²], [ζ₂₄⁶] at m = 24 — but the [ζ₂₄] symbol at m = 24
  carries an exact order-2 obstruction, χ₂₄(P([ζ₂₄])) = −1** (all 24
  root choices). The ξ-combination is canonically zero for
  m ∈ {2,3,4,6,8,12}; at m = 24 it equals (−1)^{c₁}, and the parity
  of the 5-adic c₁ is NOT determined by its printed digits — the
  m = 24 ξ-class is honestly OPEN. Witnesses now carry the
  provenance triple (engine/scriptFile/commitSha) since the Kummer
  probe reads the base-place witness.
- xx9f narrowing recorded in the bean (transcription ruled out; q^λ
  passes x² mod 25 but fails x³; [26] = uploads/2111.06645v3.pdf
  located).

**Remaining honest route to a nontrivial ε_m(ξ)**: the GLOBAL
integer-coefficient Bloch symbols `[z₁]+[z₂]+[z₃]` of GSWZ (270)
(non-root-of-unity arguments; genuinely ramified Kummer data) — the
final 9p9y layer.

## Addendum 14 (2026-08-02) — new uploads gap-map: where 1-loop = torsion and the spherical partition algebra bear on 1ppq / SM derivation gaps

Two uploads (`uploads/2411.03801v2.pdf` Garoufalidis–Yoon "1-loop
equals torsion for two-bridge knots"; `uploads/2402.01890v4.pdf`
Bastías–Martin–Ryom-Hansen "On the spherical partition algebra")
assessed against the open derivation gaps. Corpus-grep run first; the
existing 1-loop/torsion thread lives in
`borromean_jones_1loop_torsion.py` / `borromean_nz_adjoint_torsion.py`
and the α_EM / 1ppq ledgers.

**A. GY Theorem 1.1 (PROVED: 1-loop = adjoint torsion for hyperbolic
2-bridge knots) + their cited [PW] (Pandey–Wong: proved for
fundamental shadow links):**

1. **m_p chain, Steps 9–10 (SM leg).** The corpus validated
   `exp(2c₀) = 1/|det J_NZ|` on 4₁ (= √3) and computed
   `|det J_NZ(𝓑₃)| = 64` — under the then-CONJECTURAL DG13 bridge.
   4₁ is 2-bridge (GY Thm 1.1) and the Borromean rings are the
   classic fundamental shadow link ([PW]), so **both instances are
   now theorem-backed**: the subleading 1-loop constant in the
   Borromean Kashaev asymptotics equals an exact algebraic
   determinant by theorem, not conjecture. The ρ(𝓑₃)-density
   correction layer below Vol in `m(K) = m_e·Vol(K)·ρ(K)/ℏ_q²` gains
   a derived ingredient. Follow-up beaned: re-scope the two witness
   producers' conjecture-conditional wording to theorem-backed and
   register the GY + PW refs.
2. **Q_β c₃ / A_ω (1ppq leg).** The A_ω = 3 result on main is
   conditional on `conj:stokes-dt-bps-bridge`; separately, the
   τ^{1/2} (1-loop) normalization inside the 4₁/5₂ resurgent Stokes
   prefactor is now exact for 2-bridge — one conditional layer
   removed from the prefactor normalization side (NOT from the
   DT/BPS identification itself; scope-(a) framing).
3. **Bean `xx9f`.** δ₅₂ = 3α−2 in GSWZ (281)/(282) IS the 1-loop
   invariant = τ_adj by GY/OT15 — the δ-prefactor of every 2-bridge
   Φ-series is a derived quantity with an exact closed form. This
   pins the provenance of the normalization but does not by itself
   resolve the x³ mismatch (the unprinted series factor).

**B. Spherical partition algebra (assessment — suggested tool, no gap
closed today).** The Sₙ rep-theory infra epic on main has the
Burnside `Σ(f^λ)² = n!` brick "dimension side proved, HLF-gated".
The spherical partition algebra's idempotent truncation realizes the
invariant-theory side of Sₙ Schur–Weyl — candidate machinery for the
multiplicity bookkeeping in that brick and for partition-algebra
dualities on the `tr_M` binding-combiner side. Noted for the epic
owner; no wiring.

## Addendum 15 (2026-08-02) — pvuw done; [26] read cracks the xx9f SHAPE (E-factor); 5₂ Galois norm verified

**Bean `pvuw` COMPLETE**: `pandey-wong-2023` registered in
`references.ts` (validate exit 0); both Borromean 1-loop/torsion
producers re-scoped with the theorem-backing note (GY Thm 1.1 for 4₁,
2-bridge; PW for 𝓑₃, fundamental shadow link) and their witnesses
regenerated with a `theorem_backing` field. `garoufalidis-yoon-2024`
was already registered by a sibling (its note recorded the pdf as
403-unreachable — it now lives at `uploads/2411.03801v2.pdf`).

**xx9f SHAPE IDENTIFICATION (the [26] payoff)**: GZ §9 defines the
single-series correction factor
`E(h) = exp(−Σ_{r≥1} |B_{r+1}|/(r+1)!·C_r·h^r)` — explicitly "the
h-deformed versions of the units constructed in [10]" (the CGZ
ε-units this program computes) — which makes one Φ integral without
its bar partner, with `E(h)E(−h) = 1`. Its signature: h¹ term
(B₂/2!), **no h² term** (B₃ = 0), h³ term (B₄/4!). This is EXACTLY
the (287) mismatch pattern found on this branch (λ-solve passes x²
with the h¹ term alone; x³ residual remains). Candidate (b) is
upgraded from "some unprinted series factor" to "a GZ E-type unit
deformation"; implied `C₁ = −12λ₁`, `C₃`-relation recorded in the
witness. GZ print C_r data for 4₁ only (their §8.1) — extracting and
cross-verifying the 5₂ values stays open on `xx9f`.

**New probe `gswz_52_galois_norm_probe.py` (4/4)**: the GZ Galois
triple-product claim for 5₂ verified EXACTLY to h³ from printed (282)
— `N(h) = det(I + M(φ₁)h + M(φ₂)h² + M(φ₃)h³)` has rational
coefficients `1, −615/184, 8709543/1557376, −1793137595/286557184`
with denominator support exactly **{2, 23}**: 5-integral (the harness
core), the 3s cancel entirely (stronger than the 4₁ `Z[1/3]`
statement), and the 23-powers are the per-order δ³ᵏ normalization
(integrality away from Δ, disc = −23). `N(3α−2) = −23` (odd-degree
sign) checked exactly.

## Addendum 16 (2026-08-02) — global symbols: machinery to degree 96, and the Kummer-field-collapse finding; xx9f E-hypotheses refuted on digits

**xx9f second narrowing (scope-(a) negatives)**: GZ §8.1 identifies
the C_r as Taylor data of `log(1 − e(1/6 + w))` (shifted Li₋ᵣ values).
Two zero-free-parameter hypotheses for the (287) mismatch λ were
tested against its known digits and **both refuted**: the
uniform-Bernoulli-shift form `Δ(s)·Σc_j Li₀(ζ_j)` (full s-grid, both
signs) and the weaker parallel form (any 5-unit rational multiple).
Conclusion: the E-factor's tail arguments are not the (275) roots of
unity — most plausibly the Nahm z-data of the ψ³ bracket in (281).

**y3xv increment (`gswz_epsm_global_symbols_probe.py`, 5/5)**: the
global integer-coefficient symbols (ξ = 2[z₁]+[z₂], z₁ = 1−α²,
1−z₁ = α² exactly) run through the cyclic-quantum-dilog machinery in
unramified fields containing μ_{624m} up to **degree 96** (≈60 s
total): field integrity, α Hensel-lift, and the root-difference law
all green. **The honest structural finding (vacuity vigilance, the
#4533 lesson applied proactively)**: a diagnostic showed
`χ(ζ_N) = 624 ≠ 0` (the character resolves F) but `χ` kills ALL of
μ₆₂₄ — since `624m | 5^d−1` by construction, every base-Teichmüller
unit is an m-th power in F. The all-zero classes are **Kummer-field
collapse, not ε-triviality**; the α²-identity and Bloch-shadow checks
hold vacuously at these field sizes (disclosed in probe + witness).
**The ε-invariant lives in the base field**: CGZ's descent
`P(ξ) = a·b^m, a ∈ F_n^×` — extracting the base-field class of `a`
via the Galois norm/transfer from F down to `Q₂₅(ζ_m)` is the
precisely-defined next increment (bean `y3xv` stays in-progress).

## Addendum 17 (2026-08-11) — the descent EXECUTED at m = 2: ν = +1, canonical ε₂(ξ) = +1 (PR #4968)

The increment-2 spec (Addendum 16 / PR #4946) is now implemented and
run: `gswz_epsm_descent_m2_probe.py`, **20/20 checks**, the first
genuinely **descended and well-defined** ε_m value of the program.

**Setup.** F = Q₅(μ₁₂₄₈) (degree 8 unramified), base B = Q₂₅,
Γ = ⟨σ⟩ = ⟨φ₅²⟩ of order 4. σ is the Hensel-lifted Frobenius
(checked: h(σx) = 0 and σ⁴ = id). P(ξ) = D(x₁)²·D(x₂)·D(1)⁻³ from
the Addendum-16 machinery.

**Layer 1 — the obstruction (abstract Tonelli root).**
c = √(σ(P)/P) exists (Tonelli–Shanks on the 2-Sylow + Newton);
**ν = N_{F/B}(c) = +1** ∈ μ₂, root-choice invariant — unobstructed.
**Honest finding, self-caught the same day in two stages before any
review:** (i) the first pushed version used χ_B = teich(·)³¹², which
is *identically* +1 on the σ-fixed base (312 ≡ 0 mod 24) — fixed to
the genuine quadratic character teich(·)¹² = teich(·)^{(25−1)/2} with
a base-level non-vacuity control (χ_B(ζ₆₂₄²⁶) = −1); (ii) with the
genuine character, the abstract-layer value **flips with the root
choice** (χ_B(a) = +1 for c, −1 for −c — asserted as a check): the
flip c → −c moves a by v² with σ(v) = −v, forcing teich(v)²⁴ = −1.
So the abstract layer pins **only ν**; χ_B(a) from an arbitrary
Tonelli branch is not an invariant.

**Layer 2 — the canonical equivariant cocycle (the value).** σ fixes
z₁, z₂, α, and acts on the chosen roots by x₁ → −x₁ (r₁ = 1),
x₂ → x₂ (r₂ = 0) — measured, not assumed. The Lean-proved shift law
(21) (`QOU.Machinery.CyclicQuantumDilog`, PR #4964) then gives σP/P
as an **explicit product**, D(−x₁)/D(x₁) = (1−x₁)²/(1−z₁), whose
square root is *forced* (every exponent even before rooting, gated by
`canonical_root_integral`):

$$c_{\mathrm{canon}} = \frac{(1-x_1)^2}{1-z_1}, \qquad
c_{\mathrm{canon}}^2 = \frac{\sigma P}{P} \;\text{(exact)}.$$

No Tonelli choice anywhere. The c_canon-splice satisfies
c·σ(b) = b exactly, the descended a = P·b⁻² is σ-fixed (the
falsifiable certificate), and

**ε₂(ξ) = χ_B(a_canon) = +1**, **invariant under x₁ → −x₁** (the
whole canonical chain re-run on flipped data; both give +1).

**Why this is new information.** Addendum 16's collapse finding showed
every F-level Kummer class is structurally vacuous. ε₂(ξ) = +1 is the
base-level class of the canonically-descended element — the object
CGZ's ε actually is. No printed target exists; the value is
falsifiable against any independent computation.

**Next.** m = 3: d = 12 (ord₅ mod 1872), Γ of order 6, ν ∈ μ₃
(root-ambiguity ζ₃⁶ = 1 auto-invariant), χ_B = teich(·)⁸; the
canonical-cocycle integrality pattern must again be read off the
measured r_i. Then remaining m | 24; m = 24 is where the #4533 −1
obstruction on [ζ₂₄] and the open (−1)^{c₁} parity live.

## Addendum 18 (2026-08-11) — m = 3 descent: ν = 1, but the shift-law layer cannot pin ε₃; the cocycle lives on the α-line (PR #4968)

`gswz_epsm_descent_m3_probe.py`, **18/18 checks**, F = Q₅(μ₁₈₇₂)
(d = 12), Γ = ⟨φ₅²⟩ of order 6, χ_B = teich(·)⁸ into the base
μ₃ = ⟨g₂₄⁸⟩.

**Measured structure (none of it assumed):**

- Shift exponents **r = (r₁, r₂) = (0, 1)**: z₁ *has* a σ-fixed (base)
  cube root; z₂ does **not** — its Frobenius shifts every cube root by
  ζ₃. (r_i is intrinsic to z_i: σ fixes ζ₃, so the shift is the same
  for all three roots.)
- **ν = N_{F/B}(c) = 1** (Tonelli cube root via the 3-Sylow, order 9 =
  3^{v₃(5¹²−1)}; c³ = σP/P exact; ν root-choice invariant since
  ζ₃⁶ = 1). The descent **exists**.
- **The canonical layer is integrally obstructed**: with n = (2, 1),
  the shift law gives σP/P = (1−x₂)³·(1−z₂)⁻¹, and the (1−z₂)-factor's
  cube root is fractional — unlike m = 2, where every exponent was
  even before rooting. Any residual cube-root choice sweeps the class
  through **all of μ₃** (the m = 2 flip generalizes: a root twist
  c → ζ₃c moves the descended a by v³ with σ(v) = ζ₃v, forcing
  teich(v)²⁴ = ζ₃, i.e. Δχ_B = ζ₃ per twist). So the shift-law layer
  pins **ν only** at m = 3 — reported as such, not forced.
- **The α-line identity (exact, new):** 1−z₁ = α² *and* **1−z₂ = α**
  (α⁴−α²+1 = −α from α³ = α²−1). The entire cocycle obstruction of
  ξ = 2[z₁]+[z₂] is a power of α: σP/P = (1−x₂)³/α. A canonical ε₃
  therefore reduces to one question — a canonical cube root of α —
  which the CGZ square-argument η-elements (their Thm 7.4 arguments
  are squares, sidestepping root choices) are the natural candidate
  mechanism for. Queued on `qou-y3xv`.

**Contrast table so far:**

| m | r (measured) | canonical root | ν | ε_m(ξ) |
|---|---|---|---|---|
| 2 | (1, 0) | integral — no choice | +1 | **+1, well-defined** (x₁-flip invariant) |
| 3 | (0, 1) | fractional in (1−z₂) = α | 1 | pinning-dependent; only ν invariant at this layer |

## Addendum 19 (2026-08-11) — the c_k payoff run: named corpus candidates through the gate stack, twisted p = 5 leg executed (PR #4968)

`ck_membership_payoff_run_probe.py`, **7/7**, exact sympy/cyclotomic
arithmetic. This executes the "twisted test" queued on `qou-9p9y` by
the classical gate run (`habiro_tail_membership_gate_probe.py`) and
the U2 payoff promised on `qou-1hlh`.

> **⚠ SCOPE ADDED by Addendum 26 (2026-08-18).** The gate verdicts below
> are **VALID-immune** — exact Laurent/cyclotomic arithmetic, measured to
> contain no trace parameter and no anchor. But the *identification* of
> these elements as "the corpus's named c_k / α_EM candidates" is
> **C-CONDITIONAL**: that provenance comes from the convention-C-frame
> ladder, which the 2026-08-15 ruling leaves un-re-derived (`qou-cds1`).

**Candidates (the corpus's actual named fibre-level objects):**
J_Hopf(q) = −(q+1/q) (the c₃ fibre candidate); [2]_q (the α_EM
element's q-factor); D(4) (binding Habiro tail control). Exact anchor:
the corpus's two c₃ q-forms, −2 − ℏ_q²q and J_Hopf(q), are **the same
Laurent element** (verified exactly).

**Gates:** G1 integer-Laurent (global); G2 bar-even symmetrization
3-integral (GSWZ pattern); G3 the p = 2 Frobenius edge
F(ζ₈)² ≡ F(ζ₄) mod 2 in Z[ζ₈]; **G4 the twisted p = 5 leg
F(ζ₅)⁵ ≡ F(1) mod 5 in Z[ζ₅]** — the Frobenius-endomorphism
congruence at the prime where the whole 5₂/GSWZ program lives.

**Result table (all signatures predicted in advance and asserted):**

| candidate | G1 | G2 | G3 (p=2) | G4 (p=5) |
|---|---|---|---|---|
| J_Hopf (c₃) | ✓ | ✓ | ✓ | ✓ |
| [2]_q (α_EM) | ✓ | ✓ | ✓ | ✓ |
| D(4) (binding tail) | ✓ | ✓ | ✓ | ✓ |
| swing-fit (×(1+149/5000)) | ✗ | ✓ | ✗ | ✗ |
| denom-7 | ✗ | ✓ | ✓ | ✓ |

The two controls fail **per-prime, exactly where their denominators
live**: the 2.98%-swing-sized fitted shape (denominator 2³·5⁴) breaks
the global, p = 2 and p = 5 gates while passing the 3-gate; the
denominator-7 shape breaks only the global gate — every local gate at
p ∉ {7} passes. This is "coefficient integrality away from Δ" made
operational: a fitted c₃-shape is refuted by arithmetic alone, no
anchor inversion anywhere. VALUE-level c₃ verdicts (near-match,
2.98% swing — SETTLED 2026-05-31) are untouched; this is
element-level arithmetic.

## Addendum 20 (2026-08-11) — xx9f third narrowing: the Nahm-argument E-factor is also excluded on digits; the Nahm saddle IS z₁; the (1+x)^a structure exact (PR #4968)

`gswz_287_nahm_efactor_probe.py`, **6/6**, exact (Z/5⁸)[α] arithmetic.
This executes the surviving route from the second narrowing ("the
E-factor's tail arguments are most plausibly the Nahm z-data of the
ψ_{0,z,1}³ bracket in (281)").

**New exact positives:**

- **The 5₂ Nahm saddle is the shape z₁.** The cube-potential saddle
  equation (1−z)³ = z² (disc −23, the same cubic field) has K-rational
  root exactly **z = z₁ = 1−α²** — verified in the ring. So the (281)
  ψ_{0,z,1} parameter is the tetrahedron shape itself, mirroring 4₁'s
  ψ_{0,ζ₆,1} (ζ₆ = the 4₁ shape).
- **The mismatch has the exact (1+x)^a structure at h².** With
  a = e₁ from the reconstruction printed = (1+e₁x+e₂x²+e₃x³)·computed,
  the identity e₂ = a(a−1)/2 holds on **all** available digits — an
  independent re-derivation of the Addendum-16 x²-confirmation, i.e.
  the B₃ = 0 E-factor signature.
- **The h³ residual pinned:** μ₃ = e₃ − a(a−1)(a−2)/6 has digits
  (4, 0, 3)·(const, α, α²) mod 5 — nonzero, so the normalization is a
  genuine series (not a single (1+x)^a power).

**The test and its outcome (scope-(a)):** 84 zero-free-parameter
candidates C₁ = ±(n₁Li₀(ζ₆ᵗz₁) + n₂Li₀(ζ₆ᵗz₂)) (t ∈ 0..5, structural
weights, both signs; ζ₆ = the GZ Z-shift e(−5/6) at c = 1), each
implying a = −C₁/12 — **none matches the e₁ digits**. A planted-
candidate sensitivity control (synthetic mismatch from weights (2,1))
is found *exactly* by the same scanner, so the empty result is a
genuine exclusion, not a scanner artifact. Had any candidate survived
h¹, it would have faced −C₃ = 720μ₃ (same weights, Li₋₂) at h³.

**Where xx9f stands (three argument-classes now excluded on digits):**
(275) roots of unity under uniform Bernoulli shift; parallel 5-unit
scalars; Nahm z-arguments under structural Li₀ weights. Remaining:
(a) the f₅ fibre reading of the printed subscript (owner's pdf
eyeball pending: p. 57 (287) f-subscript; p. 56 (281)→(282) factor);
(b) Bernoulli-polynomial-weighted mixed arguments (GZ (8.7) at c > 1)
— which needs unprinted higher-fibre data to constrain without
fitting. Bean `qou-xx9f` reopened accordingly.

## Addendum 21 (2026-08-11) — the m | 24 sweep: ν = 1 at every level; m = 2 is the unique shift-law-canonical case; everything else is "a canonical m-th root of α"

`gswz_epsm_descent_m4to24_probe.py`, **6/6** (77 s; fields to degree
96). With the m = 2 / m = 3 layers from earlier on this program, the
descent table over the full divisor lattice is now complete:

| m | d | n_gal | canonical root (shift law) | ν | ε_m(ξ) |
|---|---|---|---|---|---|
| 2 | 8 | 4 | **integral** (no choice) | +1 | **+1 well-defined** |
| 3 | 12 | 6 | fractional in (1−z₂) = α | 1 | ν only |
| 4 | 16 | 8 | fractional | 1 | ν only |
| 6 | 24 | 12 | fractional (2r₁ ok, r₂ not) | 1 | ν only |
| 8 | 32 | 16 | fractional | 1 | ν only |
| 12 | 48 | 24 | fractional | 1 | ν only |
| 24 | 96 | 48 | fractional | 1 | ν only |

**Findings:**

- **ν = 1 for every m | 24** — the Galois descent of P(ξ) exists at
  every level; there is no descent obstruction anywhere in the lattice.
  (Not in tension with the #4533 result: the exact −1 there is the
  *Kummer-layer symbol class* of [ζ₂₄] at m = 24 — a different object
  from the descent obstruction of P(ξ).)
- **m = 2 is structurally special**: it is the only level where the
  multiplicities n = (2, 1) and the measured shifts make every
  exponent even before rooting. At every other m the fractional part
  sits on the α-line — 1−z₁ = α², 1−z₂ = α, z₁ = −α³ (all re-verified
  exactly in each of the five fields) — so **the entire remaining
  ε_m(ξ) program is one question: a canonical m-th root of α.**
- **Convention note (honest):** the raw shift exponents r_i are
  relative to each field's ζ_m choice (different primitive-root seeds
  per field), so they are not comparable across fields; the
  integrality verdicts m | 2r₁ / m | r₂ ARE intrinsic (unit rescaling
  of r preserves divisibility by m).
- The abstract layer's class is deliberately not extracted at any
  fractional m (PR #4968 established it sweeps μ_m with the root
  choice — the abstract layer pins ν only).

**Next (bean `qou-y3xv`):** the canonical m-th root of α. Candidate
mechanisms: CGZ's square-argument η-elements (their Thm 7.4 arguments
are chosen to kill root ambiguities); or a norm-compatible pinning via
α = (1−x₂)(1−ζ_m x₂)···-factorizations (α is the full σ-orbit product
of (1−x₂) at m = 3). Until then, ε₂(ξ) = +1 plus ν ≡ 1 on the whole
lattice is the complete extractable dataset.

## Addendum 22 (2026-08-11) — the α-obstruction is MAXIMAL: α generates μ₂₄, so no root choice can ever repair the canonical cocycle (PR #4983)

`gswz_epsm_alpha_teichmuller_order_probe.py`, **14/14**. This sharpens
Addendum 21 in two directions — one that could have overturned its
table, and one that explains it.

> **⚠ CORRECTED by Addendum 24 (same day).** The paragraph below calls
> the combined condition m | Q "the sharp criterion". That is the wrong
> label: m | Q controls **existence** of an m-th root, not
> **canonicity**. The canonicity criterion is the per-factor
> m | n_j·r_j that Addendum 21 used. The two **agree on ξ**, so every
> verdict in this addendum stands unchanged — only the label was wrong.

**The published criterion was not sharp.** Addendum 21 scored each
level with the *per-factor* condition m | n_i·r_i (n = (2,1)). But the
α-line identities make **both** base elements powers of the *same*
element (1−z₁ = α², 1−z₂ = α), so the cocycle's whole fractional part
is a single α-power and the sharp condition is the **combined**
m | (4r₁ + r₂) — strictly weaker, and intrinsic (rescaling ζ_m
multiplies both r_i by one unit). Re-scored:

| m | 2 | 3 | 4 | 6 | 8 | 12 | 24 |
|---|---|---|---|---|---|---|---|
| (4r₁+r₂) mod m | **0** | 1 | 2 | 4 | 2 | 10 | 22 |

Only m = 2 vanishes. **The Addendum-21 verdicts stand under the more
permissive test** — the obstruction survives being tested harder, which
strengthens the table rather than correcting it (m = 8 improves 6 → 2,
m = 24 improves 18/10 → 22, neither reaching 0).

**Why no root choice can help — a proved invariant.** α is σ-fixed, so
it lies in the base B = Q₂₅ with Teichmüller group μ₂₄. Measured:

$$e_\alpha := \mathrm{dlog}_{g_{24}}\ \mathrm{teich}(\alpha) = 13,
\qquad \gcd(13, 24) = 1.$$

**α is a primitive generator of μ₂₄** (exact order 24, computed
independently of the gcd). Three consequences, each checked:

1. **α is an m-th power in B for no m > 1** — the m-th powers are
   ⟨g₂₄^m⟩ and m ∤ 13 for every m > 1. There is no base m-th root of α
   *to choose*: the canonical construction cannot be repaired by a
   better choice.
2. **α contributes no divisibility of its own** — e_α being a unit mod
   24 makes m | e_α(4r₁+r₂) equivalent to m | (4r₁+r₂). The lattice is
   governed entirely by the shift exponents.
3. **m = 2 is canonical for a different reason than one might guess** —
   not because α is a square (13 is odd; it is not), but because
   4r₁+r₂ = 4 is *even*, so the exponent is an integer and no root of α
   is needed at all. Addendum 21's "m = 2 is uniquely canonical" is now
   explained, not merely observed.

**Scope (strict).** The exclusion is **scope-(b)** with its invariant
named — *the order of α in the cyclic group μ₂₄* forbids any m-th root
in the base, permanently, for m > 1. But the ε_m consequence stays
**scope-(a)**: ε_m is a function of the **Bloch class**, and a different
representative of the same class (five-term-related, or CGZ's
square-argument η-form, their Thm 7.4) has different 1−w_i and may avoid
α entirely. What is excluded is **one route on one representative** — not
ε_m at m ≥ 3. That change of representative is the next increment on
`qou-y3xv`.

## Addendum 23 (2026-08-11) — the obstruction is a quadratic form, and the α-block is CLEARABLE by a representative change (Lean-proved backbone)

`gswz_epsm_representative_obstruction_probe.py` (**27/27**, exact 𝔽₂₅
arithmetic) + `QOU/Machinery/EpsMObstruction.lean` (**sorry-free**,
axioms `[propext, Classical.choice, Quot.sound]` only). This settles the
question Addendum 22 deliberately left open.

**The closed form.** σ = φ₅² acts on μ₂₄ₘ by ζ ↦ ζ²⁵, so an m-th root
written ζ^e is moved by (ζ²⁴)^e — i.e. **r(w) = e(w) mod m**, the
Teichmüller discrete logarithm. Lean: `frobenius_shift` (generic
`CommGroup`) with `orderOf_shift_factor` proving the shift factor has
order exactly m. **Validated, not assumed**: every measured shift pair in
the merged p-adic sweep (all seven m | 24, fields to degree 96) is
reproduced from two residue-field logarithms.

**The obstruction form.** The canonical cocycle is integral at level m iff

$$m \mid Q\Big(\textstyle\sum_j n_j[w_j]\Big) := \sum_j n_j\,e(w_j)\,e(1-w_j) \bmod 24 .$$

Q is computable entirely in **𝔽₂₅** — the whole degree-96 lattice
recomputed by hand-sized arithmetic — and is independent of the
logarithm generator, because every unit of Z/24 squares to 1 (Lean:
`unit_sq_eq_one`, `qSymbol_rescale`). **Q(ξ) = 10, gcd(10,24) = 2**:
only m = 2 divides it, reproducing the merged lattice verdicts row by
row.

**The decisive sweep.** Over all 506 admissible five-term instances in
𝔽₂₅, Q takes **every even residue mod 24 and never an odd one**. So
**Q mod 24 is not a class invariant** — a representative change shifts it
by an arbitrary even amount.

> **⚠ CORRECTED by Addendum 24 (same day).** The consequence below
> infers a *canonical* cocycle from Q(ξ′) = 0. It does not follow:
> m | Q only makes U an m-th power, leaving m roots whose choice moves
> the class. **The conclusion survives, for a stronger reason** — a
> representative meeting the genuine (per-factor) criterion exists at
> every m | 24, with an explicit m = 24 witness. See Addendum 24.

**Consequence — the α-block is clearable.** Q(ξ) = 10 is even, so a
representative ξ′ of the *same* Bloch class has Q(ξ′) ≡ 0, giving an
integral canonical cocycle **simultaneously at every m | 24**. Explicit
witness: a five-term instance with Q = 14 seeded at x = y = 1 + 2α
(K-rational; α's residue generates 𝔽₂₅ over 𝔽₅, so every target residue
lifts), giving a 7-symbol representative with Q = 0. Lean:
`clearable_of_even`.

**This confirms Addendum 22 was correctly scoped.** The α-order exclusion
was deliberately called scope-(b) *for the root choice* and scope-(a)
*for ε_m*; the α-block is now shown to be genuinely representative-
specific and **not** a barrier to ε_m.

**A parity claim of mine, refuted by its own check.** An earlier draft
here asserted that Q mod 2 is a Bloch-class invariant. The probe's
inversion check **failed**, and the closed form (Lean:
`inversion_closed_form`, `inversion_even_iff`) says why:

$$Q([x]+[1/x]) = e(x)^2 - 12\,e(x), \quad\text{odd exactly when } e(x)
\text{ is odd (12 of 23 cases).}$$

Inversion holds in the Bloch group only **modulo torsion**, and Z/24 sees
exactly that torsion. The honest statement is therefore: Q mod 2 is
invariant under the *defining* five-term relation (exhaustively swept)
and under reflection — **not** claimed for B(K) modulo torsion. The
clearing argument above uses only five-term shifts and does not depend on
parity.

**Next.** Extracting the ε_m **values** at m ≥ 3 needs the p-adic descent
re-run on the 7-symbol representative — the route is now open, the values
are not yet computed.

## Addendum 24 (2026-08-11) — CORRECTION: m | Q is existence, not canonicity; and a genuinely canonical representative exists at every m | 24

`gswz_epsm_canonicity_criterion_correction_probe.py`, **14/14**.
Corrects two statements of my own in already-merged work (Addendum 22 /
PR #4983, Addendum 23 / PR #4999), both amended in place above.

**What was wrong.** Running the Lean-proved shift law through
P(ξ) = ∏_j D(x_j)^{n_j}/D(1)^{Σn_j} gives

$$\frac{\sigma P}{P} \;=\; \frac{\big[\prod_j \prod_{k<r_j}(1-\zeta^k x_j)^{n_j}\big]^m}{U},
\qquad U := \prod_j (1-w_j)^{n_j r_j},$$

so a cocycle needs an **m-th root of U**. The two conditions do
different jobs:

| condition | what it gives |
|---|---|
| **per-factor** m \| n_j·r_j (each j) | U is an m-th power with *explicit integer exponents* — the root is **written down**, so the cocycle is **canonical** |
| **combined** m \| Q | only that U's Teichmüller dlog is divisible by m — U is *some* m-th power, with **m roots** whose choice **moves the class** |

Per-factor ⟹ combined, never conversely. The choice-moves-the-class
failure is not hypothetical: it is exactly the flip already measured at
m = 2 (abstract Tonelli layer, PR #4968) and the μ₃ sweep at m = 3. So
Addendum 22's "sharp criterion" label was wrong, and Addendum 23's
inference of a *canonical* cocycle from Q(ξ′) = 0 does not follow.

**What survives, checked rather than asserted.** On ξ the two criteria
**agree at every m | 24** (both give m = 2 only), so every merged
lattice verdict stands; the Lean file `EpsMObstruction.lean` is
unaffected (it proves the shift law and the algebra of Q, all true and
used here); the α-order result is unaffected.

> **⚠ THE EXISTENCE ANSWER BELOW IS RETRACTED by Addendum 25 (same
> day).** The lattice computation merges symbols by **residue**, but the
> product U is indexed by distinct **field elements** — and 58 % of
> built symbols are distinct elements sharing a residue, so the model is
> not a harmless approximation. The **criterion correction above stands**
> (it is a derivation); what falls is "a canonical representative exists
> at every m | 24", which that computation does not establish.

**The corrected question, and its answer.** Per-factor demands
μ_w | n_w with μ_w := m/gcd(m, e(w)) — a **lattice membership**
question: is ξ ∈ L_m + R, with R the five-term relation subgroup of
ℤ^{23}?

- **Non-vacuity first**, since the result would be empty if the
  relations generated everything: R has full rank but index
  **[ℤ²³ : R] = 3120** — the pre-Bloch group of 𝔽₂₅ is ℤ/2 × ℤ/1560 —
  and ξ ∉ R, nor is any single symbol. The membership tester is
  controlled in both directions.
- **Answer: yes at every m | 24.** A per-factor — hence genuinely
  canonical — representative exists at every level.
- **Explicit witness at the hardest level m = 24**, found by BFS over
  the 3120-element quotient (464 cosets explored): symbols with
  Teichmüller dlogs 18, 16, 4 at coefficients 4, 3, 6. Verified
  directly: 4·18 = 72, 3·16 = 48, 6·4 = 24 are all divisible by 24, and
  the witness differs from ξ by an element of R.

**Net effect.** Addendum 23's headline — the α-block is clearable —
**stands**, but on the correct criterion and with a stronger witness.
The value-extraction increment is now *well-posed*: the cocycle it will
build is canonical, which the Addendum-23 criterion did not guarantee.
Still open, unchanged: the ε_m **values** at m ≥ 3.

## Addendum 25 (2026-08-11) — RETRACTION: the residue-level model does not establish a canonical representative; the per-element question is open

`gswz_epsm_residue_model_insufficient_probe.py`, **6/6**. A negative
about my own claim of one turn earlier, found while starting the
value-extraction increment. Addendum 24 amended in place.

**What does not follow.** Addendum 24 answered "does a per-factor
representative exist?" with a lattice-membership computation in ℤ^{S},
S = the 23 admissible symbols of the **residue field** 𝔽₂₅. That model
merges every symbol sharing a residue into one coordinate. The product

$$U = \prod_j (1-w_j)^{n_j r_j}$$

does not merge them: its factors are indexed by the distinct **field
elements** w_j, and two Bloch symbols can be congruent mod 5 while being
different elements of the base — then (1−w_j) and (1−w_k) are separate
factors, each needing its own exponent divisible by m for the root to be
explicit. So the residue-level condition is **necessary but not
sufficient** (the implication direction is checked), and the existence
claim is not established by that computation.

**The measurement.** Building five-term relations in the p-adic base
from α-basis lifts — so the relations hold *exactly* — over a sample of
seeds:

| symbols built | distinct residues | distinct elements sharing a residue |
|---|---|---|
| 310 | 23 | **180 (58 %)** |

With only 23 residues and arbitrarily many admissible field elements,
collisions are the generic case.

**A bug this probe's own control caught.** The first run reported
150/300 collisions but **failed** its exactness control. The cause: the
residue field was modelled in a t² = 2 basis while lifts were built as
a + bα, whose residue is (a+2b, b) — so symbols were paired with the
wrong residues, and some 1−XY became non-units, making `R.inv` return
garbage. Rebuilt in the α-basis (ᾱ² = 4ᾱ + 3, from the quadratic factor
of x³−x²+1 over 𝔽₅) the control passes and the count is 180/310. The
control exists precisely so that a broken lift cannot produce a
publishable number, and it did its job.

**What survives, checked rather than asserted.** The **criterion
correction** of Addendum 24 — per-factor is canonicity, m | Q is only
existence of a root — is a derivation from the shift law and is
unaffected. Every merged per-m verdict on ξ is unaffected: those were
computed on ξ's own two symbols, whose residues are distinct
((3,1) and (1,4), checked). `EpsMObstruction.lean` and the α-order
result are unaffected.

**Open, restated honestly (bean `qou-y3xv`).** Whether a representative
of ξ exists whose **per-element** multiplicities satisfy m | n_j r_j at
any m ≥ 3. The residue-level answer was yes; the per-element question is
strictly harder, and a per-element solution would imply the
residue-level one — so the residue "yes" is *consistent with*, but no
evidence for, a per-element solution. The ε_m values at m ≥ 3 remain
uncomputed.

## Addendum 26 (2026-08-18) — convention-immunity of this programme, measured; and the one C-conditional label in my merged wording

`gswz_program_convention_immunity_probe.py`, **7/7** (both controls
fire). Written after the week's rulings — convention **D** canonical and
**C excised** (2026-08-15), proton pin reaffirmed, and the standing
AGENTS.md warning that the Q_β `c_k` ladder is C-frame throughout and
**not re-derived** (`qou-cds1`), so every `c_k` conclusion is
C-conditional until it is.

The question for this programme is whether *its* results inherit that
conditionality. Answered by **measurement**, following the template of
[`2026-08-15-c3-refutation-chain-convention-validity-audit.md`](2026-08-15-c3-refutation-chain-convention-validity-audit.md):

| measured over the 20 programme probes | result |
|---|---|
| imports of `pyhecke` / a Gram module / Markov-trace machinery | **none** |
| references to `z_C`, `z_D`, `√q/(q+1)`, `q³/(q²+1)` | **none** |
| references to `q_parameter`, `q0`, the 50-digit pin, `qou_substrate` | **none** |

Convention C vs D is a statement about the **Markov parameter z** and
the Gram form built from it; a chain that never touches that layer
cannot be C- or D-framed. Likewise, a chain that never evaluates at a
substrate modulus is untouched by the proton-pin directive. The `q` that
*does* appear in five probes is the **quantum variable, not z** — under
C ↔ D it is z that changes *as a function of* q, while q is unchanged,
so a Laurent element in q is the same element in both conventions
(verified: the candidates are integer Laurent elements of ℤ[q,1/q], a
ring in which no convention choice is even expressible).

**Classification:**

| result | verdict |
|---|---|
| ε_m descent chain, all layers (Addenda 17, 18, 21–25) | **VALID-immune** — no q, no z, no anchor |
| the c_k membership **gates** (Addendum 19) | **VALID-immune** — exact Laurent/cyclotomic arithmetic |
| the c_k candidate **provenance** (Addendum 19) | **C-CONDITIONAL** — the identification of J_Hopf(q) and [2]_q as *the corpus's named c_k / α_EM candidates* comes from the C-frame ladder; the gate verdicts are unaffected |

Addendum 19 now carries that scope banner in place. This audit does
**not** claim the c_k ladder survives convention D — that is
`qou-cds1`'s question and is untouched here.

**Kept as a standing gate**, not a one-off: the probe fires the moment a
z-dependent or anchor-dependent input is wired into this chain, which is
the drift it exists to catch.

**Also this pass — a real defect a sibling found in my code.** `qou-kx04`
(commit `0f50c3d2`) fixed `gswz_epsm_descent_m4to24_probe.py`, whose
witness path was the repo-root-relative literal
`computations/probes/…`: run from its own directory — which is how the
regeneration harness invokes every producer — it died with
`FileNotFoundError` **after** completing a 69-second compute. **Eleven
more of my probes carried the same defect**; all are now anchored to
`pathlib.Path(__file__).resolve().parent`, verified by running from
`computations/probes/` (the failing cwd): 5/5, 7/7, 7/7, 18/18 green.
Same cwd-assumption class as the `parents[2]` bug fixed in 12 scripts.

## Addendum 27 (2026-08-18) — a per-element representative EXISTS at m = 3 and 6, the canonical cocycle closes there — and the value is still not an invariant

> **⚠ SCOPE NARROWED by Addendum 30 (2026-08-19).** The ambiguity this
> addendum measures is real, but it belongs to **my** descent-to-B +
> χ_B composite, **not** to CGZ's P_ζ — which is root-independent by
> their Lemma 2.4(a). Read every "obstruction" below as a condition
> for the *B-level composite* to be well defined.

`gswz_epsm_per_element_representative_probe.py`, **16/16**. Answers the
question Addendum 25 reopened (bean `qou-w4gn`), and then finds the next
obstruction rather than a value.

**Why the earlier search found nothing.** The single-relation negative
(bean note, 2026-08-11) placed z₂ only in the **seed** slot, used
coefficient **1**, and assumed z₂ appears **once**. Widening all three:

- **Position** — z₂ can occupy any of the five slots, each reachable by
  construction (slot 3 via y = α/x, since 1−xy = 1−α = z₂ exactly;
  slots 2 and 4 by solving for the partner seed).
- **Coefficient** — with general c the demand is m | (1−ck)·e(z₂) plus
  m | c·e(w), strictly weaker than the c = 1 case.
- **Multiplicity** — z₂ can appear **twice** in one relation, and that
  is exactly what the survivors do.

**Result.** Of 550 relations built containing the actual z₂, exactly
**2** contain it twice. For both, **c = 2** makes ξ′ = ξ − 2R
per-element divisible at **m = 3 and m = 6**:

| element | mult | e(w) | mult·e |
|---|---|---|---|
| z₁ | +2 | 3 | +6 |
| z₂ | −3 | 22 | −66 |
| w_a | −2 | 12 | −24 |
| w_b | −4 | 15 | −60 |

Four distinct field elements, every product divisible by 3 and by 6.
**m = 4, 8, 12, 24 have no candidate** at this level — they also need z₁
fixed (2·e(z₁) = 6 divides by none of them), which a relation touching
only z₂ cannot do.

**A trap avoided, having been caught by it once.** A residue-level
search with seeds lifted afterwards produced five apparent m = 3
candidates that **evaporated**: in the field their z₂ multiplicity was
**0**, not 2 — lifting a residue yields *some* element of that class,
not the specific z₂. Every candidate here is built so the slot **is**
the actual z₂, and the representative is verified element-by-element in
the p-adic ring.

**The descent then closes — a first at m ≥ 3.** With every canonical
exponent integral *by* the per-element property, the cocycle needs no
root choice, and the gate **c_canon³ = σ(P)/P holds exactly**. The
Hilbert-90 resolvent, the splice law, the σ-fixed certificate and χ_B
all follow, giving **ε₃ = ω¹**.

**But that value is not an invariant.** The m-th roots x_j remain
choices, and re-running the *whole* canonical chain under
x_j → ζ₃^t·x_j moves the class through **all of μ₃** (measured: twists
on the e = 3 and e = 15 symbols give 0 and 2; twists on e = 22 and
e = 12 leave it at 1). So **ε₃ = ω¹ is CONVENTIONAL** under the
teich-dlog pinning — the same lesson as the m = 2 abstract layer, one
construction deeper. Recorded as an asserted check, so a future
construction that genuinely pins the x_j would break it and be noticed.

**Net.** The per-element criterion was necessary but **not sufficient**
for a well-defined value. What the canonical cocycle removed was the
*U-root* choice; what remains is the *x_j* choice. That is now the
precise remaining obstruction, and it is a different object from
everything excluded so far — CGZ's square-argument η-elements (their
Thm 7.4, whose arguments are squares precisely to sidestep root
choices) are the natural candidate mechanism. The ε_m **values** at
m ≥ 3 remain uncomputed as invariants.

## Addendum 28 (2026-08-18) — the root ambiguity has a closed form: a second condition, an obstruction at m ≥ 4, and a door still open at m = 3

> **⚠ SCOPE NARROWED by Addendum 30 (2026-08-19).** The ambiguity this
> addendum measures is real, but it belongs to **my** descent-to-B +
> χ_B composite, **not** to CGZ's P_ζ — which is root-independent by
> their Lemma 2.4(a). Read every "obstruction" below as a condition
> for the *B-level composite* to be well defined.

`gswz_epsm_root_ambiguity_criterion_probe.py`, **9/9**. Explains
Addendum 27's non-invariance exactly, and turns it into a criterion.

**The closed form.** Twisting one root x_j → ζ_m·x_j changes D(x_j) by
the Lean-proved shift law at r = 1, D(ζx)/D(x) = (1−x)^m/(1−w). So P
changes by [(1−x_j)^m/(1−w_j)]^{n_j}, and χ_B kills the m-th power
(χ_B(u^m) = teich(u)²⁴ = 1), leaving

$$\Delta_j \;=\; -\,n_j\, e(1-w_j) \pmod m .$$

**Verified against all four measured twists** of the Addendum-27
representative — including the two that left the value fixed.

**The criterion.** A well-defined ε_m needs **both**:

| | condition | what it buys |
|---|---|---|
| **C1** | m \| n_j·e(w_j) | canonical cocycle integral (Addendum 27) |
| **C2** | m \| n_j·e(1−w_j) | value root-choice invariant (**new**) |

equivalently μ*_w \| n_w with μ*_w = m/gcd(m, gcd(e(w), e(1−w))).

**This is the shape of CGZ's own construction.** Their Bloch elements
are **D·[ζ_D]** (§7 circular units, p. 33) — a root-of-unity symbol
carrying a *multiplicity*, whose R_ζ images are literally
∏(1−ζᵏζ_D)ᵏ. The multiplier is not decoration: C2 is what it is for.

**The obstruction, and why a residue-level negative is valid here.** The
conditions depend only on residues, and an element-level representative
**merges into** a residue-level one satisfying the same conditions
(m | n_j·a for each j gives m | (Σ n_j)·a over a fixed residue). So
*residue-infeasible ⟹ element-infeasible* — the sound direction. (The
converse is unsound and is precisely the Addendum-25 error; it is not
used.) Measured over 23 symbols and 506 relations:

| m | 3 | 4 | 6 | 8 | 12 | 24 |
|---|---|---|---|---|---|---|
| ξ ∈ L*_m + R | **TRUE** | false | false | false | false | false |
| special symbols (μ* = 1) | 3/23 | 2/23 | 3/23 | 0 | 0 | 0 |

A control confirms the *weaker* C1-only condition still succeeds at
m = 3 and 24, so the infeasibility is C2 biting rather than a broken
test.

**Scope (strict).** The m ≥ 4 result excludes **this construction** —
the D_ζ descent with χ_B and freely chosen m-th roots — **not** the
existence of ε_m as a map; a route that *pins* the roots rather than
choosing them is untouched. And m = 3 having the necessary condition
satisfied is **not a value**: an element-level representative meeting
both conditions still has to be exhibited, and the single-relation
family (550 relations containing the actual z₂, every coefficient)
contains none.

**A convention trap, caught by this probe's own check.** The first run
compared measured twists (whose dlogs use the p-adic g₂₄ = ζ₆₂₄²⁶) with
e(1−w) computed from a *different* 𝔽₂₅ generator — the two differ by a
unit rescale, and the check went red. Fixed by doing that comparison in
one convention. The lattice test is unaffected: μ* is invariant under
the rescale, since gcd(m, u·g) = gcd(m, g) for a unit u mod 24.

## Addendum 29 (2026-08-18) — m = 3 closed for one and two relations: no element-level representative meets both conditions

> **⚠ SCOPE NARROWED by Addendum 30 (2026-08-19).** The ambiguity this
> addendum measures is real, but it belongs to **my** descent-to-B +
> χ_B composite, **not** to CGZ's P_ζ — which is root-independent by
> their Lemma 2.4(a). Read every "obstruction" below as a condition
> for the *B-level composite* to be well defined.

`gswz_epsm_m3_one_two_relation_closure_probe.py`, **8/8**. Addendum 28
left m = 3 as the only level where the two-condition criterion was
*residue-level* feasible; residue feasibility is only **necessary**
(Addendum 25), so the question was whether an element-level
representative actually exists. It does not, for one or two relations.

**The mechanism, measured:**

- μ*(z₁) = μ*(z₂) = **3**, and ξ carries them at multiplicities 2 and 1
  — so both need moving.
- The maximum in-relation repetition of any argument is **2, never 3**
  (over 1097 distinct relations containing the actual z₁ or z₂). For a
  non-special argument u, μ*_u | c·k_u with k_u ∈ {1,2} therefore forces
  **3 | c**.
- Hence a relation usable with c ∦ 3 needs *every distinct* non-target
  argument special — and **0 of 1097 qualify** (only 3 of 23 residues
  are special at m = 3).

**Result:**

| search | coverage | solutions |
|---|---|---|
| one relation | exhaustive, 1097 | **0** |
| two relations sharing a non-special argument | exhaustive: 307 590 pairs, 2 460 720 coefficient combos, 13 s | **0** |
| two relations with disjoint non-special arguments | excluded structurally (each c_i ≡ 0 mod 3, so z₂ stays 1 mod 3) | — |

The pair search finished in 13 s against a 300 s budget, so no cutoff
hid anything — asserted as a check.

**Open, and explicitly not searched:** three or more relations forming a
**chain** of shared non-special arguments. The mechanism does not
exclude those, and the pair result is not evidence about triples beyond
showing no two-relation chain closes.

**Scope.** Combined with Addendum 28 this says: the D_ζ descent with χ_B
and *freely chosen* m-th roots yields no well-defined ε_m at any m ≥ 3
within one or two relations. It says nothing about ε_m as a map, and
nothing about a construction that **pins** the roots (CGZ's η-elements)
rather than choosing them — which is now the only route left standing.

**A check that failed for a coding reason, not a mathematical one.** The
"no relation has all others special" gate first went red. The claim was
*true* (the measured count is 0); the predicate was miscoded —
accumulating `max(0, specials − len)` from a sentinel of 0 and then
requiring `< 0`, which cannot hold when nothing qualifies. Recorded
because at a glance that is indistinguishable from a mathematical
failure, and I briefly wrote it up as one.

## Addendum 30 (2026-08-19) — RE-SCOPE: CGZ's P_ζ *is* root-independent; the m ≥ 3 ambiguity belongs to my descent step, not to the invariant

`gswz_epsm_cgz_lemma24a_rescope_probe.py`, **9/9**. Reading CGZ's own
definition instead of continuing to build on mine shows that Addenda
27–29 characterise **my composite**, not their invariant. Scope banners
added to all three in place.

**What CGZ actually define** (eqn (20), p. 10):

$$P_\zeta(X) := D_\zeta(x)/D_\zeta(1) \ \in\ H^\times/(H^\times)^n,
\qquad x^n = X,$$

with the parenthetical *"only its image modulo nth powers was ever used,
and it is more canonical to define it in the manner above."* Then
**Lemma 2.4(a): P_ζ(X) is independent of the choice of nth root x of
X**, proved via their eqn (21) — which is exactly the shift law this
programme proved in Lean (#4964) — plus the observation that the shift
factor **lies in H^×ⁿ**.

**Measured here**, in the degree-12 field F = Q₅(μ₁₈₇₂) where the m = 3
work was done:

| | shift ratio D(ζx)/D(x) is an m-th power |
|---|---|
| in **F** | **4 of 4** — Lemma 2.4(a) confirmed |
| in the base **B = Q₂₅** | **1 of 4** |

The ratio equals (1−x)^m/(1−w) exactly (the Lean law, re-verified). Its
(1−x)^m part is an m-th power anywhere; the (1−w)⁻¹ part lives in the
**base**, and — structurally — **B^× ⊆ (F^×)^m** here, since μ₂₄ sits in
F^× as ⟨g^{(5¹²−1)/24}⟩ with (5¹²−1)/24 = 10 172 526 divisible by 3, and
the 1+5R part is uniquely 3-divisible. So in F the ratio is *always* an
m-th power, and P_ζ is root-independent for free.

**The ambiguity enters only when I descend to B and apply
χ_B = teich(·)^{24/m}**, which does not kill those ratios.

**Consequence.** Addenda 27–29 are not retracted — their computations
stand — but their scope narrows:

| addendum | was framed as | actually is |
|---|---|---|
| 27 | ε₃ value not invariant | the **B-level composite** is not invariant |
| 28 | obstruction at m = 4, 6, 8, 12, 24 | when the **B-level composite** is well defined |
| 29 | m = 3 closed for 1–2 relations | ditto, for the **B-level composite** |

**None of them obstructs ε_m.** The right target is CGZ's own: the class
in F^×/(F^×)ⁿ, where root-independence is Lemma 2.4(a) and no
representative search is needed at all. That is the next increment, and
it is **not** done here — no ε_m value is claimed.

**Two controls that went red for non-mathematical reasons**, both
recorded because they look identical to real failures at a glance:
sweeping 𝔽₅ scalars for a non-cube finds none (order divides 4, and
(5¹²−1)/4 is divisible by 3), and neither does sweeping a+bα+cα² — every
element of B^× is a cube in F, which is the structural fact above. The
control had to leave B entirely, using the ring generator.

## Addendum 31 (2026-08-19) — computing CGZ's class where they put it: the invariant is bracketed, not obtained

`gswz_epsm_field_bracketing_probe.py`, **9/9**. Addendum 30's stated
next increment was to compute the class in F^×/(F^×)ⁿ instead of
descending to the base. Done — and the answer is a bracketing, not a
value.

**The computation.** For a unit of F the class is carried entirely by
the Teichmüller part (1+5R is uniquely m-divisible), so it reads off as
teich(u)^{(5^d−1)/m} in μ_m. *Applying the exponent to u itself does not
work* — the 1+5R factor survives, and an earlier version of this probe
did exactly that and returned no class at all.

**Result 1 — Lemma 2.4(a), measured rather than quoted.** For
P_ζ(ξ) = D(x₁)²D(x₂)/D(1)³ the class is **0**, and it is 0 for **all
nine** choices of the two cube roots. Root-independence is confirmed
empirically in this setting.

**Result 2 — and this is why it is a bracket.** The class map is *not*
globally trivial: it returns class 1 on an element built from the ring
generator. But on the objects that matter it is identically zero — the
class of P_ζ(w) is **0 for every one of the 23 admissible base
arguments**. So in F the invariant carries no information about ξ, and
the 0 above is **vacuous**. (P itself is not σ-fixed, so this is not the
trivial "it landed in B, and B^× ⊆ (F^×)^m" explanation from
Addendum 30.)

| field | root-independence | class |
|---|---|---|
| base B = Q₂₅ | **fails** (Addenda 27–29) | distinguishes |
| F = Q₅(μ₁₈₇₂) | **holds** (Lemma 2.4(a)) | **identically 0 on base arguments** |

**Neither field supports the invariant.** The useful field is
intermediate — or, reading CGZ more carefully, the invariant is not this
bare class at all: their Lemma 2.4(d),(e) record that P_ζ is
Φ-invariant and transforms under Gal by the cyclotomic character, and
their R_ζ lands in K₂ / Galois cohomology rather than in a quotient of
units. A bare class in F^×/(F^×)ⁿ discards exactly that structure, which
is consistent with its collapsing.

**Scope.** A negative that localises the difficulty rather than
resolving it. No ε_m value is claimed at m ≥ 3; the m = 2 result
(PR #4968) is untouched. The non-vacuity control is what makes the
collapse a finding rather than a broken class function.
