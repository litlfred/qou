# Does Bring's S₅ single out the chirality unit `u`? — PREREGISTRATION

**Status:** preregistration, written and committed BEFORE any computation or Lean is run.
**Date:** 2026-11-15 · **Branch:** `claude/bring-s5-unit-2026-11-15` · **Beans:** `qou-wqto`, `qou-rydq`.
**Owner ruling (2026-11-15, chat, option 2):** look for a point that Bring's own `S₅`
symmetry singles out, to fix the unit `u` of the chirality grading `Γ_u = L_u ∘ M_i`.

## 0. What is being decided, and what may not be used to decide it

`QOU/BringCone.lean` (PR #7784, merged) shows that the chirality grading
`Γ_u := L_u ∘ M_i` on the model cone `BringCone R = Quaternion R` needs `u` to be a
pure unit quaternion — a point of `S²` — that the Reeb triad `M_i, M_j, M_k` cannot
distinguish choices, and that only a base point `p` fixes `u` (`u = p·i·p̄`, the Hopf
image). The question here is whether a **group action** coming from Bring's
automorphism group singles out such a point.

**Fixed in advance:** nothing below may be chosen, preferred, or re-ranked by what it does
to chirality labels, the `Gen1Quark` assignment, `Q_β`, any mass, any binding energy, or
any other data. The selection rules in §2 are stated purely in terms of the group action,
before the action has been computed. If two rules disagree, both results are reported and
neither is promoted.

## 1. (a) The action — what the corpus fixes and what it does not

Corpus-grep performed before writing (surfaces: `brings-surface/*.{md,lean}`,
`lean/QOU/BringCone*.lean`, `lean/QOU/Brings/*.lean`, `docs/audits`, `docs/coordination`,
`computations/`, `beans/defs`, `library/INDEX.md`, `library/*/sections`, `library/*/ocr`;
terms: `binary icosahedral`, `2I`, `icosahedral`, `BringCone`, `Bring cone`, `ℙ(V)`).

**What the corpus fixes.**

1. *Triad-commuting maps are left multiplications.* `commutes_reeb_triad_iff_leftMul`
   (`BringCone.lean`): an `R`-linear map commuting with `M_i, M_j, M_k` is `L_{f(1)}`.
   So any symmetry of the cone that respects the Reeb triad and is linear is a left
   multiplication `L_g`; for unit `g` it is invertible with inverse `L_{ḡ}`.
2. *Two A₅'s exist in the corpus, on other spaces.*
   - Klein's icosahedral `A₅` acting on the categorical base `ℙ(V) ≅ ℙ¹`
     (`brings-surface/klein-bring-icosahedral-bridge.{md,lean}`; arithmetic sorry-free,
     the orbifold identification still a content-bearing conjecture class with no
     instance). Its exceptional orbits are recorded as sizes 12 / 20 / 30 with cyclic
     stabilisers of orders 5 / 3 / 2 (`cone_orders`).
   - `S₅ = Aut(Σ₄)` acting on Bring's genus-4 curve (`def:brings-surface`, library
     `arxiv-2208.13692v1`, `s40879-023-00706-0`, `sigma12-065`).
3. *The model cone is not Bring's cone.* `QOU/Brings/BringConeLinkEulerNumber.lean` and
   `docs/audits/2026-09-03-bring-cone-link-is-the-unit-tangent-bundle.md`: the real link
   is `UT(Σ₄)` (Euler number −6, `SL̃₂` geometry); `BringCone R = Quaternion R` is the cone
   over the Hopf fibration `S³ → S² = ℙ¹` (Euler number −1). The `S²` on which `u` lives is
   the **Hopf base of the model**, not Bring's curve.

**What the corpus does NOT fix (found on none of the surfaces above).**

- No homomorphism `S₅ → (unit quaternions)` or `A₅ → (unit quaternions)` acting on
  `BringCone`, and no statement that Bring's automorphisms act on the model cone at all.
- No identification of the model's Hopf base `S²` with Klein's `ℙ(V)`, and no
  `A₅`-equivariant map `Σ₄ → ℙ¹` to Klein's icosahedral `ℙ¹`.

So the link "Bring's `S₅` acts on the admissible `u`" is **not established**; it is the
gap. To get any answer at all, the following is introduced as a labelled ASSUMPTION, not a
corpus fact:

> **(H-ico)** `A₅` acts on the model cone by triad-commuting unit automorphisms `L_g`,
> `g` ranging over the binary icosahedral group `2I ⊂ ℍ^×` (order 120). By fact 1 this is
> the only shape a triad-respecting linear action can have.

Two structural constraints, which bind before any computation (standard representation
theory; to be checked, not assumed, where feasible):

- The induced action on `u` is conjugation, `u ↦ g u ḡ` (to be proved:
  `L_g ∘ Γ_u ∘ L_{ḡ} = Γ_{g u ḡ}`), i.e. through `SO(3)`. `S₅` has no faithful
  real 3-dimensional representation (irreducible degrees 1,1,4,4,5,5,6), so **only the
  orientation-preserving `A₅` can act on `S²` this way**; the odd coset cannot.
- `A₅` has two inequivalent 3-dimensional irreducibles, interchanged by the outer
  automorphism that `S₅`'s odd coset induces (Galois `√5 ↦ −√5`). So even under (H-ico)
  the embedding `A₅ → SO(3)` is one of two, and `S₅` itself does not choose between them.

## 2. (b) Candidate selection rules — fixed now, group-theoretic only

Under (H-ico), with `A₅` acting on `S² = {pure u : normSq u = 1}` by conjugation:

| rule | statement | expected (standard icosahedral facts, to be verified) |
|---|---|---|
| **R0** global fixed point | `u` with `g·u = u` for all `g ∈ A₅` | none (no fixed axis) |
| **R1** maximal stabiliser | the points whose stabiliser has maximal order | the 12 vertex directions (stabiliser `C₅`), = 6 axes |
| **R2** exceptional orbits | the points with nontrivial stabiliser | three orbits, sizes 12 / 20 / 30 (`C₅` / `C₃` / `C₂`) |
| **R3** minimal orbit | the smallest orbit | = R1 by orbit–stabiliser |

**Reported property (not a selection rule):** for each selected orbit, whether it is
closed under the global L↔R flip `u ↦ −u` (`Γ_{−u} = −Γ_u`, `chiralGammaU_neg`), and
whether `−u` lies in the **same `A₅`-orbit** as `u`. This is a property of the group action
alone and is computed regardless of outcome. It decides whether a selected orbit can carry a
handedness at all: if `−u = g·u` for some `g ∈ A₅`, the symmetry conjugates `Γ_u` to
`−Γ_u` and identifies L with R rather than fixing one.

## 3. (c) What counts as "singles out"

- **(i) unique point** — R0 non-empty, or a rule returning exactly one point. Would fix `u`.
- **(ii) distinguished orbit, not a point** — a rule returning exactly one orbit with more
  than one point. Report: orbit size, number of `±` pairs, whether `±` pairs are related
  inside the orbit (then the orbit relabels L↔R and cannot fix handedness).
- **(iii) nothing distinguished, or action not established** — R0 empty and no rule returns
  a unique orbit, OR the action itself is not supported by the corpus. (iii) on the
  "action not established" leg holds already from §1, independently of any computation:
  any (ii) obtained is conditional on (H-ico).

## 4. Method, fixed in advance

1. Lean (new file `QOU/BringConeIcosahedral.lean`, generic `CommRing` where possible):
   the conjugation law for `Γ_u`; no nonzero pure quaternion fixed by conjugation by both
   `i` and `j` (these lie in `2I` in the standard embedding — so R0 is empty under any
   action containing them); the flip `L_j Γ_i L_{j̄} = −Γ_i` (a 2-fold rotation
   perpendicular to `u` sends `u ↦ −u`). No `sorry`, no `: True`, no `native_decide`.
2. Exact compute (sympy over `ℚ(√5)`, no float): generate `2I` from explicit generators,
   form the 60 rotations, find all points of `S²` with nontrivial stabiliser (the rotation
   axes), compute orbits, stabiliser orders, and the antipode test of §2.
3. Report against §3 without changing any rule.

---

## 5. RESULTS (added after measurement; §§0–4 above are as committed in `5b76d41e08`, unchanged)

No rule in §2 was altered after measuring. Both legs were measured as fixed.

### 5.1 The action leg — outcome (iii), independent of any computation

Re-stated from §1, now as the headline: **the corpus does not establish that Bring's `S₅`,
or its `A₅`, acts on the model cone `BringCone` or on its admissible units `u`.** The
`A₅` actions it holds are on Klein's `ℙ(V)` and on `Σ₄`; the `S²` of admissible `u` is
the Hopf base of the quaternionic model, which `BringConeLinkEulerNumber.lean` already
records is not Bring's link (`UT(Σ₄)`, Euler number −6, vs Hopf, −1). Searched surfaces
are listed in §1; this is a statement about them, not a proof no such action exists.

Two structural facts constrain what any such action could be:

- `S₅` has no faithful real 3-dimensional representation (irreducible degrees
  1,1,4,4,5,5,6 — standard character table), so only `A₅` can act on `S²` linearly.
- `A₅` has two inequivalent 3-dimensional representations. **Measured:** the
  Galois-conjugate embedding `√5 ↦ −√5` of `2I` has a different character on
  corresponding order-5 elements (values `(1 ± √5)/2` swap). That the odd coset of `S₅`
  realises this swap is the standard outer-automorphism fact, cited, not computed. So
  `S₅` does not choose between the two embeddings.

### 5.2 Conditional on (H-ico) — what the group action gives

Lean, `QOU/BringConeIcosahedral.lean` (generic `CommRing`; `lean -DautoImplicit=false
-s 65536` exit 0; axioms ⊆ `propext, Classical.choice, Quot.sound`):

| decl | content |
|---|---|
| `leftMul_conj_chiralGammaU` | `L_g ∘ Γ_u ∘ L_{ḡ} = Γ_{g u ḡ}` — a left-multiplication symmetry acts on `u` by conjugation |
| `re_conjBy`, `normSq_conjBy` | conjugation by a unit preserves pure + norm |
| `conjBy_unitI_unitJ_fixed_eq_zero` | a pure `u` fixed by conjugation by `i` and `j` is `0` (2 cancellable) |
| `conjBy_neg_of_anticomm` | a unit `w` anticommuting with `u` sends `u ↦ −u` |
| `leftMul_flips_chiralGammaU` | …so `L_w` carries `Γ_u` to `−Γ_u` (L↔R) |
| `leftMul_unitJ_flips_chiralGamma_i` | the instance `w = j`, `u = i` |

Exact compute, `computations/probes/bring_cone_icosahedral_unit_orbits_probe.py`
(pairs of `Fraction` over `ℚ(√5)`, no float; 12/12 checks pass): `|2I| = 120`,
image in `SO(3)` = 60, `i, j ∈ 2I`, and

| rule | result |
|---|---|
| **R0** global fixed point | **none** (0 directions; also Lean, via `i, j ∈ 2I`) |
| **R1 / R3** maximal stabiliser = minimal orbit | **unique orbit: the 12 vertex directions**, stabiliser `C₅`, = 6 axes |
| **R2** exceptional orbits | three orbits, 12 / 20 / 30, stabilisers 5 / 3 / 2 — not unique |
| antipode test | **every exceptional orbit contains `−u` for each of its `u`**, moved there by 5 / 3 / 2 rotations of `A₅` (the half-turns perpendicular to `u`) |

### 5.3 Reading against §3

- **(i) unique point — NO.** R0 is empty.
- **(ii) distinguished orbit — YES under R1/R3, conditionally:** the 12 vertex directions
  (6 `±` pairs). But three things make this no better than the base-point choice it was
  meant to replace:
  1. **It cannot fix a handedness.** Each vertex `u` and its antipode `−u` are in the
     same orbit, related by an `A₅` half-turn `w` perpendicular to `u`, and
     `leftMul_flips_chiralGammaU` then gives `L_w Γ_u L_{w̄} = −Γ_u`. So the symmetry the
     rule is built from **identifies L with R**; an `A₅`-invariant prescription cannot
     carry a chirality at all. Fixing one requires breaking `A₅` to the stabiliser `C₅` of
     a chosen vertex: one of 12 points (6 axes, then an orientation).
  2. **The orbit is only defined once `2I ⊂ ℍ^×` is placed.** Any conjugate `h·2I·h⁻¹`
     moves the 12 points by `h`, and the Reeb triad does not constrain `h` (left
     multiplications commute with it). The probe's standard icosians, with `i, j, k ∈ 2I`,
     are a coordinate choice aligned with the triad's axes, not a derived one. The freedom
     in placing `2I` is the same `SO(3)`-worth of freedom as the freedom in `u`.
  3. **Two embeddings.** Under (H-ico) there is in addition the Galois choice of §5.1,
     which `S₅` does not resolve.
- **(iii) — YES on the action leg.** Nothing in the corpus puts Bring's symmetry on the
  cone.

**Outcome: (iii), with a conditional (ii) that fails to fix handedness.** The ruling's
question has a negative answer on the corpus as it stands: Bring's `S₅` does not single out
`u`. Granting the action, it singles out the 12-vertex orbit — and then itself swaps L and
R inside it.

### 5.4 Gap

The missing link is a homomorphism from Bring's automorphisms to the triad-commuting
symmetries of the model cone (necessarily through `2I`, by
`commutes_reeb_triad_iff_leftMul` and the representation constraint above), with the
placement of `2I` fixed. Any such link sits on the same model-vs-`UT(Σ₄)` question as
`qou-rydq`: on Bring's real link the `S₅` acts on `Σ₄`, not on a Hopf base `S²`.
