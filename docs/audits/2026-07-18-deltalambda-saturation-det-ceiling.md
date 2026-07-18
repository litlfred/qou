# Δ_λ magnitude wall — the nuclear-saturation angle: the det-ceiling cumulant DOES saturate, but saturation PROVABLY caps ρ below the strong target

**Date:** 2026-07-18 · **Branch:** `claude/deltalambda-saturation-ceiling-2026-07-18` ·
**Axis:** per-isotope binding `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ` — the many-body
magnitude wall · **Tier:** structural derive + prune (scope-(a) qualitative
result + scope-(b) proved exclusion; **no fit, no AME inversion, nothing wired**).

Attacks the magnitude wall from the **nuclear-saturation** angle named in the
2026-07-18 attack-vector map, and deliberately in parallel with the sibling
bar-even-symmetrization attack (a distinct context — parallel overlap is
endorsed, 2026-07-17 owner directive).

Probe: [`computations/deltalambda/deltalambda_saturation_det_ceiling_probe.py`](../../computations/deltalambda/deltalambda_saturation_det_ceiling_probe.py)
· witness `deltalambda-saturation-det-ceiling.witness.json` (exit 0, 8/8
assertions pass, mpmath at the production floor).

## 0. The hypothesis under test

**Overshoot IS the failure to saturate.** #3952
([`deltalambda_k4_complete_graph_collective_magnitude_probe.py`](../../computations/deltalambda/deltalambda_k4_complete_graph_collective_magnitude_probe.py))
found that the *bare* graph collective invariants — spanning trees `A^{A−2}`,
Laplacian pseudo-det `A^{A−1}` — **OVERSHOOT ⁴He by 2.6–10.6×**. Real nuclear
binding does the opposite: it **saturates** (`B/A → ~const`). The claim tested
here: the #3924 exchange determinant, taken as the **cumulant**
`b_A = −ln det(I + m·G_A)`, is the object that saturates — the log turns the
super-additive determinant into an **extensive** free energy — and a
parameter-free `m` might land the light-nucleus `ρ = B/B_D` ratios on that
saturation curve.

**Why this is a distinct object, not a re-run.** The 2026-06-02
[intensive-vs-extensive derivation](2026-06-02-binding-intensive-vs-extensive-derivation.md)
proved the canonical trace binding `B = E₀·Δtr_M` is **intensive** (saturates at
~3–4 MeV; 1.65× A-growth vs 12.72× required) and that *"no per-block weight Δ_λ
can convert an intensive quantity into an extensive one"* — the missing object is
an **additive extensive term**. The 2026-07-13
[carrier-saturation audit](2026-07-13-carrier-saturation-crossover-mechanism.md)
sharpened this: *"extensivity must live … in a non-normalized weighting … never
in the normalized linear carrier."* The log-det cumulant `b_A` is precisely such
a non-normalized, extensive object — so this probe tests the candidate those two
audits pointed at, not the intensive carrier they already excluded.

## 1. The isospin-even construction (why unsigned K_A)

Strong is isospin-blind: `IsospinMirrorInvariance.lean` (merged) machine-verifies
the strong ³H/³He split is **exactly 0**. So the strong magnitude must be built
from the **unsigned** (isospin-even) complete graph `K_A` — every bond `+1·m` —
**not** the #3924 isospin-**signed** matrix (pp=+1, nn=−1, pn=±1), whose
`{±√5,±1}` spectrum produces a spurious 2.75× mirror split (the #3943/#3924
finding). For `K_A` the exchange matrix is `m·(J − I)`, whose spectrum is exact:

```
eig(I + m(J−I)) = { 1+(A−1)m  (×1),   1−m  (×(A−1)) }
det(I + m(J−I)) = (1 + (A−1)m)·(1−m)^{A−1}        [PART 0: matches mp.det, A=2..12, <1e-30]
b_A = −ln(1+(A−1)m) − (A−1)·ln(1−m).
```

This automatically gives ³H = ³He (both `K₃`), consistent with the proved
isospin-blindness. The algebraic preflight (closed form vs `mp.det`) passes to
< 10⁻³⁰ for A = 2..12.

## 2. Result 1 (scope-(a) DERIVED) — the cumulant SATURATES

`b_A/A = −ln(1−m)·(A−1)/A − ln(1+(A−1)m)/A → −ln(1−m)` as `A→∞`: the per-nucleon
cumulant **plateaus**. At the parameter-free `m = g_reeb = 0.44673`
(plateau `−ln(1−m) = 0.5919`):

| A | 2 | 3 | 4 | 6 | 12 | 20 |
|---|---|---|---|---|---|---|
| b_A/A | 0.111 | 0.182 | 0.231 | 0.298 | 0.394 | 0.450 |
| % of plateau | 18.8 | 30.7 | 39.1 | 50.3 | 66.6 | 76.0 |

`b_A/A` rises monotonically and flattens — **qualitatively the right
rise-then-flatten shape**. So the determinant ceiling **does** produce
saturation: the log-det cumulant is extensive (`b_A ∝ A` to leading order) and
**does not overshoot**. The #3952 super-additive overshoot was an artifact of
using the **bare** determinant / pseudo-det; the **cumulant** (connected free
energy = log det) tames it. This confirms the log-det cumulant is the extensive
object the 2026-06-02 audit said the intensive trace binding is missing.

Caveat on the shape: the plateau is approached **too slowly** — at A=4 the
cumulant is only ~39 % of its plateau, whereas empirical `B/A` already **peaks**
at ⁴He (the α-particle doubly-magic peak). The model rises to its plateau over
A→∞ (full rise ~5.3×) while empirical reaches ~7.9× of the deuteron per-nucleon
by ⁴He. Right shape, wrong A-profile.

## 3. Result 2 (scope-(b) PROVED) — saturation CAPS ρ at the edge count

The dimensionless magnitude ratio `ρ_A(m) := b_A/b_2` (the E₀ / MeV dressing
cancels) obeys a **proved cap**:

> **`ρ_A(m) ≤ C(A,2) = A(A−1)/2` for all `m ∈ (0,1)`, with the supremum attained
> only as `m→0`, and `ρ_A` strictly decreasing in `m` for `A > 2`.**
>
> *Proof (exact, one line).* Let `g(m) := C(A,2)·b_2(m) − b_A(m)`, so `g(0)=0`
> and
> `g'(m) = A(A−1)·m/(1−m) · [ 1/(1+m) − 1/(1+(A−1)m) ] ≥ 0` on `(0,1)`
> (since `(A−1) ≥ 1 ⇒ 1+(A−1)m ≥ 1+m ⇒` the bracket `≥ 0`). Hence `g ≥ 0`, i.e.
> `ρ_A ≤ C(A,2)`; strict for `A>2, m>0`. ∎

The invariant cited is the **exact spectrum** `{1+(A−1)m, (1−m)^{×(A−1)}}` —
a proved structural fact, not a numerical near-miss. Numerically confirmed across
a dense `m ∈ (0,1)` sweep (199 points): `ρ_3 ∈ [2.06, 2.99]`, `ρ_4 ∈ [3.15, 5.96]`,
both strictly decreasing, both approaching `C(A,2)` (3 and 6) only as `m→0`.

*Lean status.* The cap is proved by the hand derivative argument above (rigorous,
does not depend on any numerics). A machine-checked formalization is
clean but **deferred** — the A=4 case reduces to the polynomial inequality
`(1+3m)(1−m)³ ≥ (1−m²)⁶` on `[0,1)` (equivalent to `b_4 ≤ 6·b_2` via `exp`
monotonicity), an `nlinarith`-ready target — not run here because the sandbox
disk was near-full (Mathlib olean restore would ENOSPC). It is stated as a
follow-up, not claimed as machine-verified.

**The m→0 supremum `C(A,2)` is exactly the #3952 additive edge count.** So the
det cumulant's saturation drives ρ **below** the edge count — turning up `m` only
flattens ρ further. The saturation that tames the overshoot is the *same*
mechanism that caps ρ.

## 4. The exclusion — strong targets exceed the cap

Isospin-corrected **strong** targets (AME + the parameter-free `E_C` from #3990,
`E_C(⁴He) = E_C(³He)·(3/4)^{1/3}`; ³H is Coulomb-free so `ρ_strong(3)=B(³H)/B_D`):

| ratio | value | proved cap `C(A,2)` | exceeds cap? |
|---|---|---|---|
| ρ_strong(3) | **3.813** | 3 | **yes** |
| ρ_strong(4) | **13.037** (mean of sphere/pair E_C) | 6 | **yes** |
| ρ_raw(4) (uncorrected AME) | **12.720** | 6 | **yes (robust)** |

Both strong targets exceed the proved cap; even the **raw** ρ_4 = 12.7 > 6, so
the exclusion is **robust to the E_C model factor** entirely. The isospin-even
determinant cumulant **cannot reach the strong ρ magnitudes for any m** —
a **scope-(b) structural exclusion** (cited invariant: the exact `K_A` spectrum).

Forward test at the corpus parameter-free magnitudes confirms the undershoot
(never solving `m` from the ratios — no seventh fit):

| m | ρ_pred(3) | ρ_pred(4) | ρ_pred(4)/ρ_strong(4) |
|---|---|---|---|
| g_reeb = 0.44673 | 2.450 | 4.158 | 0.319 |
| ceiling 1/√5 = 0.44721 | 2.450 | 4.157 | 0.319 |
| z_naive = 0.49932 | 2.410 | 4.045 | 0.310 |

Every parameter-free `m` lands ρ_4 at ~4.1 — well below both the cap (6) and the
target (13).

## 5. The structural diagnosis (the value of this negative)

The large ⁴He magnitude the wall needs **is** reachable by a determinant — but
only the **isospin-signed** one. The #3924 `{±√5,±1}` spectrum has the tight
ceiling `1/√5`; as `m→1/√5` the factor `(1−5m²)→0`, so `det→0⁺` and `b_4→∞`,
supplying an arbitrarily large ⁴He magnitude (#3943: at g_reeb the signed b_4
lands ~1.06× the ⁴He deficit). But that ceiling lives **entirely in the signed
graph**, whose strong ³H/³He split is proved **0** — so the signed determinant is
excluded from the strong (isospin-even) magnitude by the Lean invariant. The
**isospin-even** ceiling is only `m<1` (mild, no `√5` blow-up), and its ρ is
capped at the edge count.

> **Saturation and the large ρ are in tension.** The det ceiling that produces
> nuclear saturation (isospin-even, `m<1`, `b_A/A → const`) **caps ρ at C(A,2)**,
> below the strong target; the det ceiling that produces the large magnitude
> (isospin-signed, `1/√5`, `b_4→∞`) produces the **wrong mirror split** and is
> Lean-excluded from the strong sector. No single determinant does both.

This unifies the two prior negatives: #3952's additive edge count (ρ_4 = 6,
undershoots 13) is the **m→0 limit** of the det cumulant, and #3943's collective
residual is the gap between that cap and the target — a gap the cumulant's
saturation **cannot** close, because saturation only lowers ρ.

## 6. Verdict (anti-fit / anti-laundering, STRICT)

**Honest negative with a proved structural core.**

- **scope-(a) DERIVED:** the isospin-even complete-graph exchange cumulant
  **saturates** (`b_A/A → −ln(1−m)`) — it is the extensive object the intensive
  trace binding lacks, and it **tames** the #3952 super-additive overshoot. Right
  rise-then-flatten shape (wrong A-profile: plateau approached too slowly).
- **scope-(b) PROVED (cited invariant = exact `K_A` spectrum):** the saturation
  **caps** `ρ_A ≤ C(A,2)`, strictly decreasing in m; the strong targets
  ρ_strong(3) ≈ 3.8 > 3 and ρ_strong(4) ≈ 13 > 6 exceed the cap (robust — even raw
  ρ_4 = 12.7 > 6), so the isospin-even cumulant **cannot** supply the strong ρ
  magnitudes for any m.
- **the magnitude-generating ceiling is isospin-odd** (`1/√5`, `b_4→∞`) and
  Lean-excluded from the strong sector — saturation and large ρ are in tension.

**Not a wall-crack.** `m` is fixed parameter-free before comparison and **never**
solved from the ρ ratios (no seventh fit). The cap `ρ_A ≤ C(A,2)` is **proved**
from the spectrum, not fitted. Nothing wired: no production change, no tier
change, no content-block edit; nothing canonical.

**What would move it (for the next agent).** The strong ρ needs a determinant
whose ceiling blows up (large ρ) **and** is mirror-symmetric (isospin-even). The
isospin-even `K_A` has no such ceiling. Candidates that keep mirror symmetry
while re-introducing a blow-up: a **weighted** (non-uniform-bond) isospin-even
graph whose Perron eigenvalue → 1 at a derived `m` (breaking the `A(A−1)/2` sup),
or the sibling **bar-even symmetrization** of the signed b_4 (Vector 3), which
isolates the bar-even part of the `1/√5`-ceilinged determinant without importing
its bar-odd mirror split. Both are open; neither is closed here.

## Cross-references

- Attack-vector map (saturation angle): [`2026-07-18-deltalambda-attack-vector-map.md`](2026-07-18-deltalambda-attack-vector-map.md)
- #3952 overshoot (bare graph invariants): [`2026-07-18-deltalambda-k4-collective-magnitude.md`](2026-07-18-deltalambda-k4-collective-magnitude.md)
- #3924 signed spectrum + 1/√5 ceiling: [`b4_slater_antisymmetrizer_exchange_sign.py`](../../computations/deltalambda/b4_slater_antisymmetrizer_exchange_sign.py)
- #3943 additive per-pair negative + B_dim/B_AME: [`deltalambda_perpair_bond_magnitude_derive_probe.py`](../../computations/deltalambda/deltalambda_perpair_bond_magnitude_derive_probe.py)
- #3990 E_C isospin correction: [`2026-07-18-deltalambda-coulomb-mirror-split.md`](2026-07-18-deltalambda-coulomb-mirror-split.md)
- Intensive-vs-extensive (missing extensive term): [`2026-06-02-binding-intensive-vs-extensive-derivation.md`](2026-06-02-binding-intensive-vs-extensive-derivation.md)
- Carrier-saturation (extensivity lives in non-normalized object): [`2026-07-13-carrier-saturation-crossover-mechanism.md`](2026-07-13-carrier-saturation-crossover-mechanism.md)
- Strong split = 0 (isospin invariant): [`QOU/MassTheory/IsospinMirrorInvariance.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/IsospinMirrorInvariance.lean)
- Gate reversal (open for all): [`2026-07-13-delta-lambda-gate-open-for-all.md`](2026-07-13-delta-lambda-gate-open-for-all.md)
