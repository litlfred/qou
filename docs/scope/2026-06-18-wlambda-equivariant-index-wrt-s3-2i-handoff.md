# Scope handoff — the `W_λ` equivariant-index problem on `WRT(S³/2I)` (the sole open keystone object)

**Date:** 2026-06-18
**Branch:** `claude/s5so3-keystone-continuation-2026-06-18`
**Status:** scope / sharp handoff — **owner-gated differential geometry, NOT a probe to run blind, NOT Lean-closable** without the geometric construction.
**Discipline:** formalize-first (everything cheap is already discharged — see below) + critical-distance (a geometric construction would establish the *origin* of the weights; it does **not** by itself close any mass/binding observable).

> **One-line statement of the open object.** Does the Witten–Reshetikhin–Turaev / full-Hecke
> arena attached to `S³/2I` (the Poincaré homology sphere) admit a geometric realization whose
> S¹-equivariant index reproduces the canonical Ocneanu / q-Plancherel Markov weights
> $W_\lambda \;=\; \frac{d_q(\lambda)^2}{[n]_q!}$?
> A **finite-dimensional Sasakian arena is RULED OUT** (see §1, correction C). This is the single
> remaining structural unknown for `conj:s5-so3-fiber-action`.

---

## 0. What is already done — do NOT re-walk these (formalize-first ledger)

The keystone has been reduced, by formalize-first pruning, to *one* differential-geometry problem.
Everything combinatorial, representation-theoretic, and algebraic is **done or refuted**; **no fit was
introduced anywhere**. The authoritative state is the ledger
[`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md); summarised here so the
handoff is self-contained.

| Layer | Status | Where |
|---|---|---|
| Combinatorial backbone `Res^{S₅}_{S₃}` + `SO(3)↓A₅↪S₅` bridge | ✅ verified | `S5SO3FiberAction.lean` (`s5_to_s3_restriction_dim_consistent`, `so3_to_a5_irrep_content`), #2352/#2431 |
| Geometry: 2I spin lift exists; geometric A₅ forced to icosahedral T₁; chirality = T₁/T₂ split | ✅ verified | construction-program doc §"Residual-2 RESOLVED" |
| Algebraic functor target (Bratteli = box removal; Ocneanu trace) | ✅ forced (rigid, no free parameter) | construction-program doc §"Ingredient 4 geometric leg" |
| Static coupling `V_ℓ → E_λ` (Schur: dim Hom = 1) | ✅ forced | #2364 |
| **Generation selection ℓ → λ = the Hopf moment map μ** (spatial SO(3)-equivariance) | ✅ **realized** | #2370 |
| Δ_λ = chirality sign × Wedderburn magnitude | ✅ Lean (sorry-free) | `S5SO3FiberAction.lean` (`binding_magnitude_eq_dim`, `deltaSign_mixed`), #2416 |
| McKay 2I ↔ affine E₈ arithmetic anchors | ✅ Lean (sorry-free) | `S5SO3FiberAction.lean` (`binaryIcosahedral_order_eq_120`, `affineE8_marks_sum_eq_coxeter_30`), #2424 |
| 210 ppb muon mechanism (Wedderburn-projector correction) | ❌ **refuted** (6–8 orders too coarse) | construction-program doc §"Ingredient 4+5 close-out" |
| colour ⊗ spin = (3,1,1) dim-6 shortcut | ❌ refuted (spin-parity mismatch) | ledger refutation #2 |
| Reeb-eigenvalue resonance | ❌ refuted (no parameter-free ≥3-anchor match) | #2368 |

**Refutations not to re-walk** (canonical no-negative-result discipline): the 210 ppb projector
mechanism, the colour⊗spin tensor shortcut, and the Reeb-eigenvalue resonance are all closed
*negatively* — re-deriving any of them is wasted effort. See ledger §"Refutations not to re-walk".

---

## 1. The corrected open object (supersedes the older "Sasakian" framings)

The open object has been re-stated **three times** as the corpus understanding sharpened; the
current (2026-06-16) statement supersedes all earlier ones. Read the corrections in order so the
handoff target is unambiguous:

1. **First framing (superseded).** "Markov-trace weighting `W_λ` via a finite SU(3)/SO(3)
   (Wu-manifold) Sasakian equivariant index." — the arena was taken to be a *finite-dimensional*
   Sasakian 5-manifold.

2. **Correction A — the arena is full-Hecke, not finite SU_q(3)** (#2406, reconciling sibling #2389).
   The production trace is **not** a finite colour-ℂ^N: the colour-ℂ³ row is only a *lower* bound
   (spinor ℂ² cannot host the electron block; ℂ³ is forced as a minimum), and the full production
   trace needs **>3-row** Wedderburn blocks too (SU_q(3)/colour-ℂ³ misses 3.4 % at ⁴He). The trace is
   the **full Hecke / Wenzl principal specialization** $s_\lambda(1,q,q^2,\dots)$ — intrinsically
   $p(3A)$-dimensional, infinite-variable. **There is therefore no finite colour-SU(3) arena.**

3. **Correction B — `W_λ` is the q-Plancherel measure, not the production weight** (sibling
   `e269ca12ea`). The Markov weights $W_\lambda = d_q(\lambda)^2/[n]_q!$ are the **q-Plancherel /
   Ocneanu** measure on the Hecke tower; the *production* trace weight is the Wenzl principal
   specialization. The open object is the geometric origin of **`W_λ` (the q-Plancherel measure)**;
   it is distinct from, but the canonical companion of, the production specialization. Do not conflate
   the two when matching an index (see §4 item 2).

4. **Correction C — the finite SU(3)/SO(3) Wu-manifold arena is RULED OUT** (#2398). The spacetime
   SO(3) is the *isotropy* subgroup and has no continuous centralizer in SU(3) (Schur's lemma), so no
   spacetime-fixing Reeb field exists on `SU(3)/SO(3)`. ⇒ **spacetime ⊥ colour** (= the corpus
   factorization `S₅ = S₂ × S₃`), confirmed. The finite Sasakian route on `SU(3)/SO(3)` is closed.

**Current corrected open object (the handoff target).**

> Does the **full-Hecke principal-specialization arena** attached to `S³/2I` — equivalently the
> **WRT(S³/2I)** invariant / Lawrence–Zagier object — admit *any* geometric realization whose
> S¹-equivariant index reproduces the canonical Ocneanu / q-Plancherel Markov weights
> $W_\lambda = d_q(\lambda)^2/[n]_q!$?

A finite-dimensional Sasakian arena is ruled out (correction C). The arena, if it exists, is an
infinite-dimensional (full-Hecke / WRT) object; the question is whether its equivariant index has
the q-Plancherel weights as residues/multiplicities.

---

## 2. Why `S³/2I` and `WRT(S³/2I)` is the right arena

The geometric anchors are all in the corpus and machine-checked (see the McKay block of
`S5SO3FiberAction.lean`):

- **`S³/2I` is the Poincaré homology sphere** = the link of the E₈ surface singularity
  $\mathbb{C}^2/2I$. Here `2I` is the binary icosahedral group, the SU(2)-preimage of $I \cong A_5$,
  $|2I| = 120 = |S_5|$ (but $2I \not\cong S_5$ — `2I` is perfect, $S_5$ has $\mathbb{Z}_2$
  abelianisation; Lean `spin_Z2_ne_sign_Z2`).
- **McKay 2I ↔ affine E₈** (Lean, sorry-free): the 9 irreps of `2I` have dims equal to the affine E₈
  Coxeter marks $[1,2,3,4,5,6,4,2,3]$, $\sum d^2 = 120$, $\sum \text{marks} = h(E_8) = 30$,
  $|2I| = 4h$, $\dim E_8 = 8\cdot 31$ (`binaryIcosahedral_*`, `affineE8_*`,
  `order_2I_eq_four_times_coxeter`, `e8_dim_eq_rank_times_h_plus_one`).
- **WRT / Lawrence–Zagier.** The full-Hecke Markov trace on the icosahedral tower is the
  WRT(S³/2I) invariant (Lawrence–Zagier), a *q-series* object — this is the natural infinite-variable
  home for the q-Plancherel measure, consistent with corrections A/B that the arena is full-Hecke
  rather than a finite ℂ^N.

The arena is therefore an **honest, named object** with rigid arithmetic — not a free construction.
What is open is purely the **geometric/index realization** of `W_λ` on it.

---

## 3. Necessary conditions — what they do and do NOT decide

For the (now ruled-out) *finite* Sasakian framing, the Boothby–Wang necessary conditions were checked
and met (dim 5 odd ✓; χ(Wu) = 0 ✓). These do **not** transfer to the full-Hecke arena and are
recorded only so a future agent does not re-run that finite check expecting it to decide anything: the
finite arena is ruled out by correction C *regardless* of Boothby–Wang.

The live necessary-condition question for the corrected (full-Hecke / WRT) arena is open and is the
content of this handoff — see §4.

---

## 4. The handoff — what a future (owner-authorised) session must build

This is **differential geometry / index theory on an infinite-dimensional arena**, owner-gated and
multi-session. It is **not** a numerical probe (ingredient 5 / the 210 ppb mechanism closed that
route) and **not** Lean-closable without the construction. Concretely:

1. **Identify the equivariant-index object.** On the WRT(S³/2I) / full-Hecke arena, identify the
   S¹-action (Reeb-flow analogue) and the index whose multiplicities/residues are the candidate for
   `W_λ`. The finite Reeb field is ruled out (§1 correction C); the analogue here is the q-series /
   modular structure of the Lawrence–Zagier invariant, not a contact Reeb field on a 5-manifold.

2. **Match to `W_λ = d_q(λ)²/[n]_q!`.** Show (or refute) that the index reproduces the **q-Plancherel
   measure** — *not* the Wenzl principal specialization (correction B). The two are companions; do not
   conflate the weight you are matching.

3. **Respect spacetime ⊥ colour.** Any construction must be compatible with the verified
   factorization `S₅ = S₂ × S₃` (correction C): the spacetime SO(3) is isotropy with no continuous
   colour-centralizer. A construction that re-couples them contradicts a proved Schur obstruction and
   is wrong.

4. **Critical-distance gate.** A successful index match establishes the **geometric origin** of the
   Markov weights — it is a structural result, not a physics closure. It does **not** by itself
   resolve m_τ, GAP-A-3 (Δ_λ binding), or GAP-A-4 (mass λ(K)); those consume `W_λ` but have their own
   open pieces (e.g. the deuteron undershoot, ledger §"Δ_λ chirality decomposition" caveat). State this
   explicitly in any closure claim.

### What is forced (rigid) vs. open

- **Forced (no free parameter):** the algebraic target. By Ocneanu consistency on the Hecke tower
  ($\mathrm{tr}_{n+1}|_{H_n} = \mathrm{tr}_n$, $\mathrm{tr}_{n+1}(x\sigma_n) = z\,\mathrm{tr}_n(x)$),
  the trace restricted to the 3-tube is *forced* to the existing $H_3$ construction; the q-Plancherel
  measure $W_\lambda$ is a determined function of $\lambda, q$. **Do not run an algebraic search over
  candidate functors / weights** — the target is rigid.
- **Open (geometric existence only):** whether *any* geometric realization on the WRT(S³/2I) /
  full-Hecke arena has this rigid target as its equivariant index.

---

## 5. The Lean boundary — why this is NOT Lean-closable now

`S5SO3FiberAction.lean` carries the keystone as a **§3b-cond conditional class**
`BringFiberAction` with the substantive field
`five_distinct_classes : Function.Injective (fun r : A5Irrep => (irrepToRotation r).asSO3.angle)`.
No global instance is provided, so downstream results are genuinely conditional on the open geometric
map (`conj:s5-so3-fiber-action`). The new combinatorial facts this branch adds (Hopf generation
selection, A₅-class duality — in the same file) are **sorry-free** and unconditional; they sharpen the
scaffold but do **not** supply the `BringFiberAction` instance.

The instance can only be supplied by the §4 differential-geometry construction. Until then, the class
correctly encodes "rigorous modulo one named, owner-gated geometric input" — the honest formalization
of an open keystone. **Do not** discharge `BringFiberAction` with a `: True`-style or fitted instance;
the prior such instance was falsified and removed (#2480, per
`docs/audits/2026-06-13-bring-fiber-action-falsification.md`).

---

## 6. Cross-references

- Ledger: [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md)
- Construction program (five ingredients, geometry settled): [`2026-06-16-icosahedral-reeb-fiber-map-construction.md`](2026-06-16-icosahedral-reeb-fiber-map-construction.md)
- Arena corrections: [`docs/audits/2026-06-16-keystone-arena-is-full-hecke-not-su3.md`](../audits/2026-06-16-keystone-arena-is-full-hecke-not-su3.md), [`docs/audits/2026-06-16-keystone-wu-manifold-reeb-obstruction.md`](../audits/2026-06-16-keystone-wu-manifold-reeb-obstruction.md)
- Falsification (why the old 7-partition map / vacuous instance was removed): [`docs/audits/2026-06-13-bring-fiber-action-falsification.md`](../audits/2026-06-13-bring-fiber-action-falsification.md)
- Synthesis (single open object): [`docs/audits/2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md`](../audits/2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md)
- Lean scaffold: [`content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean)
- Sibling arena work (the three faces of the full-Hecke realization + the Habiro-ring unification with Q_β): PR #2409 — sharpens the §1-corrected arena into the colour (type-A subfactor) / spacetime (affine-E₈ basic rep) / arithmetic (Habiro ring at q₀) faces. The §4 equivariant-index match is the open coupling that #2409 also leaves open.
