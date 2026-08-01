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
values (mod 5³), matching the printed `D₅(ξ)` of eqn (271) exactly:
`1·[2,4,4] + 3·[1,3,2] + 1·[2,3,3] ≡ [2,1,3] (mod 5)` in
(const, α, α²) coordinates. This is Theorem 9 exercised on printed
data — the ε_m-class module-side layer of the membership test, live.

**Single named missing ingredient**: the Besser–de Jeu overconvergent
`Li₂` expansion (GSWZ reference [8]) is not among the uploaded sources;
until it lands, the dilog layer is mod-5³-exact and the full-precision
membership test (and ε_m units beyond mod-p) stays queued on qou-9p9y.
Uploading Besser–de Jeu (arXiv/journal: "The syntomic regulator for
K-theory of fields" / Besser's Coleman-integration papers) would
unblock the final layer.
