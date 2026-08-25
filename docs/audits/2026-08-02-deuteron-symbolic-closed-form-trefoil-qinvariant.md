# Deuteron binding as a closed-form symbolic q-invariant of the σ₁³ trefoil — proof-tier attempt

**Date:** 2026-08-02 · **Branch:** `claude/deuteron-symbolic-closed-form-2026-08-02` ·
**Bean:** (deuteron Δ_λ magnitude, `qou-3q7t` family) · **Axis:** Δ_λ / `C_knot` magnitude ·
**Tier:** PROOF-tier attempt (symbolic/exact → Lean-provable if closed) — complement to the
EMPIRICAL tessellation state-sum on the sibling branch
`claude/sigma1cubed-seifert-tessellation-nastokes-2026-08-02` (PR #4619).

## 0. BLUF — HONEST NEGATIVE (structural, Lean-backed)

**No closed-form 0-parameter scalar q-invariant of the σ₁³ trefoil at q₀ reproduces the deuteron
`C_knot = 5.853`.** This is an independent second confirmation of the sibling empirical route
(#4619: writhe-normalized Jones state-sum = 0.136× ≠ 5.853×; `tr[A,B]=0` annihilates the
surface-ordering correction), reached by a *different* method — an exhaustive scan of the canonical
scalar q-invariant space finds no parameter-free hit (§3), and a Lean proof gives the *structural
reason* (§3a).

The deuteron 5.853× binding deficit collapsed (pincer #4615 `qou-prjo` + #4617 `qou-i4pz`) to
ONE object — the transverse NA-Stokes surface-curvature term on the σ₁³ trefoil Seifert surface =
first-order per-bond amplitude Δ¹g = the fitted `C_knot = 5.853`. A triangulation-invariant
q-deformed surface state-sum (WRT / Turaev–Viro) does have a closed form for the trefoil — the
Chebyshev/Markov trace `tr_M(σ₁ⁿ) = aₙ(s)z + aₙ₋₁(s)` (Lean-proved, §3a Part 1) — but that closed
form is a **single commutative scalar** with no free normalization, and cannot carry the mixed-sign
chirality charge the deuteron needs.

**Missing symbolic ingredient (named):** an *eigenphase-weighted per-block handle-commutator charge*
(naturally mixed-sign / sum-to-zero) living in the **non-abelian H₆ interface braid** — NOT the
2-strand trefoil, whose Hecke algebra H₂(q) is *commutative* so every commutator vanishes identically
(Lean `commutator_zero`, §3a Part 2). This is the same object PROBE-4's KL-positivity prune could not
supply the sign for; it is not in the corpus.

**Framing (per sibling / `g2-frame-artifact`):** the deuteron is separately closed to ~0.036% via
fibre-level tiers, so `C_knot = 5.853` is a **categorical master-formula normalization artifact**,
not an open physical prediction; the honest resolution is the fibre→archimedean τ-transfer, not a
scalar surface term.

## 1. Target (locked BEFORE compute — anti-fit)

| quantity | value | source |
|---|---|---|
| B_D (deuteron binding) | 2.22452 MeV | AME2020 (diagnostic only, never inverted) |
| m_e | 0.51099895 MeV | CODATA |
| `\|S(D)\|` | 0.7438 | committed Wenzl-weighted signed Markov sum (#4543) |
| first-order `m_e·\|S\|` | 0.38008 MeV | DT-count derived (#4601) |
| **target `C_knot`** | **5.8528** | `B_D/(m_e·\|S\|)` — the number the closed form must hit, 0-fit |

q₀ (muon-anchored, `computations/` canonical) = `1.10997859555733471989976...`

The trefoil is the **torus knot T(2,3)** = closure of σ₁³ in B₂; **non-hyperbolic**, so
volume/dilogarithm (Bloch–Wigner) routes give 0 and are excluded a priori (§7b caveat).

## 2. Method

Enumerate the canonical closed-form q-invariants of the σ₁³ trefoil at q₀ and check each against
5.8528 with 0 tuning. A hit is proof-tier ONLY if the object is the one the corpus **independently**
identifies as the NA-Stokes surface term (not a scan-selected coincidence — invariant/normalization
choice is a hidden freedom, cf. F3 of `2026-07-13-na-stokes-ck-recursion-binding-adversarial-review.md`).

Probe: [`computations/deltalambda/deuteron_trefoil_qinvariant_closed_form_probe.py`](../../computations/deltalambda/deuteron_trefoil_qinvariant_closed_form_probe.py)
(sympy exact + mpmath 50 dps).

## 3. Results — scalar q-invariant scan (0-fit)

Probe evaluated the canonical scalar q-invariant battery exactly at q₀ (mpmath 50 dps). Closest
candidates to `C_knot = 5.8528`:

| candidate | value | rel.err | knobs | note |
|---|---|---|---|---|
| **q₀¹⁷** | 5.8932 | 0.69% | 0 | **numerology, already ruled out** (#4556 §4, writhe-framing) |
| Verlinde dim SU(2)₅ = k+1 | 6.0 | 2.5% | 1 (level) | free level ⇒ **fit** |
| `[3]_q!` (√q) | 6.030 | 3.0% | 0 | nearest *structural* single |
| `[6]_q` (√q) | 6.096 | 4.2% | 0 | |
| `[5]_q` | 5.220 | 10.8% | 0 | |

- **Nothing lands within the exactness threshold** (~1e-6 rel.err) an exact closed form demands; at
  50 dps a genuine closed form agrees to ~1e-40.
- **2-factor composite scan** (products/ratios of `{[n]_q, [n]_q!, tr_M(T(2,n)), z, s, q₀ᵏ}`): for
  `C_knot`, **zero** composites within 0.2%. (For the alternate target `B_D/m_e = 4.3533`, the sole
  near-miss `[7]_q·tr_M(T(2,3)) = 4.3575`, 0.097%, is a selection-fit with no surface-term motivation
  and is not exact.)
- The raw trefoil Markov trace `tr_M(σ₁³) = (s²+1)z + s = 0.609`; the Jones values `V_{3_1}(q₀)` are
  all O(1); none is near 5.85.

The nearest 0-knob object is ruled-out numerology; the nearest *structural* object misses by 3%; the
only objects landing within ~2.5% carry a free level/color knob (= fit). **No parameter-free scalar
q-invariant of the trefoil supplies 5.853.**

## 3a. Structural reason — H₂(q) is commutative (Lean-proved, Mathlib-free)

[`computations/deltalambda/TrefoilSurfaceStateSum.lean`](../../computations/deltalambda/TrefoilSurfaceStateSum.lean)
(sorry-free; `lean`-direct exit 0, v4.24.0; axioms `[propext, Quot.sound]` — no `sorryAx`,
no `native_decide`, no `axiom`):

- **Part 1 — the surface state-sum closed form EXISTS.** `σ₁ⁿ = aₙ(s)·σ₁ + aₙ₋₁(s)` in H₂(q) with the
  Chebyshev recursion `aₙ₊₁ = s·aₙ + aₙ₋₁`; `a_three : a 3 s = s*s + 1` proves the trefoil coefficient.
  So "the WRT/Turaev–Viro surface state-sum has a closed form" is **TRUE** — but it is a pure function
  of `(s, z)` with **no free normalization scalar**.
- **Part 2 — the scalar channel is null by abelianness.** Modeling H₂(q) as `Int × Int` with the
  `σ₁² = s·σ₁ + 1` product, `mul_comm` proves H₂(q) is **commutative** for every `s`, and
  `commutator_zero` proves **every commutator `[x,y] = 0` identically**. Hence the surface-ordering /
  handle-commutator correction (a product of commutators — sibling #4619's `tr[A,B]`) vanishes on the
  trefoil *by abelianness*, independent of q₀ — not a numerical accident.

This unifies the two independent negatives (this branch's scan; #4619's `tr[A,B]=0`): the 2-strand
trefoil algebra is abelian, so it **cannot** host a non-zero mixed-sign chirality charge. Such a charge
requires the **non-abelian H₆ interface braid** (H₆ is genuinely non-commutative).

## 4. Verdict

- **scope-(b) structural exclusion** (cited invariant: H₂(q) commutativity, `commutator_zero`): the
  σ₁³ trefoil **scalar / commutator channel is null** — no handle-commutator charge lives on the
  2-strand algebra. This confirms and structurally explains #4619's numerical null.
- **scope-(a):** no 0-parameter scalar q-invariant of the trefoil (Jones / Markov / WRT-scalar /
  quantum-dim / torus-trace-ratio, and 2-factor composites thereof) reproduces `C_knot = 5.853`.
- **NOT proof-tier closure** — this is an honest negative. `C_knot = 5.853` is a categorical
  master-formula **normalization artifact** (deuteron already ~0.036%-closed via fibre tiers,
  `g2-frame-artifact`), and the live proof-tier target is the mixed-sign handle-commutator charge in
  the non-abelian H₆ interface braid, **not** a scalar trefoil invariant. Beaned below.

## 5. Missing symbolic ingredient (bean)

The one object that could carry the deuteron's mixed-sign chirality magnitude — and is provably absent
from the trefoil scalar channel — is:

> an **eigenphase-weighted per-block handle-commutator charge** on the **non-abelian H₆ interface
> braid**, naturally mixed-sign / sum-to-zero (matching the PROBE-4 chirality requirement that
> KL-positivity could not supply). It is NOT the H₂ trefoil (abelian ⇒ handles collapse, Lean-proved),
> and it is not currently in the corpus.

## Anti-fit ledger

| statement | status |
|---|---|
| target `C_knot=5.8528` locked before compute | ✓ |
| B_AME used only as diagnostic ratio, never inverted | ✓ |
| free parameters | 0 |
| nothing wired to production | ✓ |
| nearest 0-knob candidate is ruled-out numerology (q₀¹⁷, 0.69%) | measured |
| H₂(q) commutative ⇒ trefoil commutator charge null | **Lean sorry-free** |
| verdict is honest NEGATIVE (not a manufactured closure) | ✓ |
