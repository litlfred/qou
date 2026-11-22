# The per-quark flavor split is not derived: the pivot gives a simple zero, the ansatz a triple one

Date 2026-11-21. Issue #8922. Asked by the owner as a sibling of the nuclear-interactions migration thread.

Target: Step 2 of `prf:flavor-split-substrate`
([`flavor-split-substrate-proof.md`](../../folio/quantum-observable-universe/mass-theory/flavor-split-substrate-proof.md)),
which sets

    (μ_d − μ_u)/μ_avg  ≈  f(q) := h² · ħ_q / √q,     h = q − q⁻¹,  ħ_q = (q − 1)/q.

The proof already marks this as a fitted ansatz (condition (c) is agreement with CODATA). The task was to derive it
from the axioms and corpus with no CODATA input, or to record an honest negative.

**Result: a negative.** Inside every class of object the corpus derives, the per-quark split vanishes to **first**
order at q = 1. The ansatz vanishes to **third** order. So no derived object gives it. Scope (b) for the class
stated below; it is proved in Lean.

Model register: "proton", "neutron", "u", "d", "mass" are names of constructions. Physics enters only in §5.

## 1. What the corpus derives about p versus n

- Proton and neutron are the T³ = ±½ weight spaces of (ℂ²)^⊗3, with u = e₁ (orientation forced, PR #7971).
- `NucleonIsospinExclusions.restrictedTrace_ratio` (Lean, on main): for every braid word w, the quantum trace
  restricted to the two weight spaces satisfies T_p(w) = q² · T_n(w). `commutant_restrictedTrace_ratio` extends this
  to every operator in the U_q(sl₂) commutant.
- Bridge B audit (2026-11-16, issue #8101): braids, Hecke elements and the KZ connection all commute with U_q(sl₂),
  so inside the chain the only p/n differentiator is the pivot power q^{±2}. Anything else is imported by hand.
- The T³ weight split of the z_D trace on V³ (2026-11-20 audit), ε_flavour(V³) = (q² − 1)P(q)/(q⁴(q² + 1)³).

## 2. Lean (`QOU/FlavorDressing/PivotSplitOrder.lean`)

| declaration | statement |
|---|---|
| `perQuark_split_of_nucleon_ratio` | additive strands (m_p = 2μ_u + μ_d, m_n = μ_u + 2μ_d) and m_p = ρ·m_n give (μ_d − μ_u)/μ_avg = 6(1 − ρ)/(1 + ρ) exactly |
| `perQuark_split_pivot` | the case ρ = q²: the split is `pivotSplit q = 6(1 − q²)/(1 + q²)` |
| `pivotSplit_bar_odd` | pivotSplit(q⁻¹) = −pivotSplit(q): exactly bar-odd |
| `ansatz_bar` | in t = √q, f(t⁻¹) = −t⁴ f(t): the ansatz is bar-odd only up to q². Condition (a) of Step 2 fails (now in Lean, not only sympy) |
| `ansatz_numerator_factor` | (t⁴ − 1)²(t² − 1) = (t − 1)³ · (t³ + t² + t + 1)²(t + 1) |
| `ansatz_ne_pivotSplit` | for every c ≠ 0 and m ≥ 1, c(t^m − 1)/(t^m + 1) ≠ f(t) as rational functions (cleared of denominators) |

`ansatz_ne_pivotSplit` covers, in one statement: ρ = q^{±k} for every k ≥ 1 (m = 2k, c = ∓6), the per-strand
K-weight reading μ ∝ q^{±1} (c = ∓2), and any power-law mass map m ∝ T^s with s a nonzero integer (ρ = q^{2s}).
The proof is the derivative at t = 1: the ansatz side has a double (indeed triple) root there, the pivot side has
derivative c·m ≠ 0.

## 3. Exact probe (`computations/flavour_split_derivation/order_at_classical_limit_probe.py`)

Exact over ℚ(√q), no float, no q₀. Order of vanishing at q = 1, leading coefficient in (q − 1), and the bar image:

| object | order | leading coeff | f(q⁻¹)/f(q) |
|---|---|---|---|
| Step-2 ansatz h² ħ_q/√q | **3** | 4 | −q² |
| per-strand pivot, μ ∝ K | 1 | −2 | −1 |
| per-strand pivot, μ ∝ K⁻¹ | 1 | 2 | −1 |
| restricted trace, m ∝ T, additive strands | 1 | −6 | −1 |
| restricted trace, m ∝ 1/T, additive strands | 1 | 6 | −1 |
| ε_flavour(V³) (2026-11-20 audit) | 1 | −3/4 | −1 |

Every derived differentiator is exactly bar-odd (so it meets condition (a), which the ansatz does not) and has a
simple zero (so it fails condition (b), which the ansatz meets). The two conditions of Step 2 are not met together
by anything on record.

The I₃-weighted Murphy sum (2026-11-21 octet audit) was also run: its n − p difference is order 0 (−3 at q = 1)
because it is an isospin-weighted operator with T_n(1) < 0, not a mass. It is not a candidate for μ_d − μ_u.

## 4. Scope and what it does not exclude

- (b) for the class: additive strand masses, and a nucleon mass ratio that is a nonzero integer power of q. The
  invariant cited is the order of vanishing at q = 1 (a derivative at t = 1), proved in Lean.
- It does not exclude an object that breaks U_q(sl₂) symmetry (a boundary datum, a sea strand, a non-additive
  strand rule). Bridge B records that the corpus contains no such derived object. A derivation of Step 2 needs one.
- It does not exclude a non-power-law mass map. Any smooth map m = φ(T) with φ'(T(1)) ≠ 0 gives a first-order
  split by the same argument; a map tuned to have φ'(T(1)) = 0 would be a choice, not a derivation.
- Step 1 of the same proof uses z_mkv = √q/(q + 1), the excised convention-C weight. Under convention D the
  pair-Skein relation is not re-derived, so Step 1 is not established either. Not changed here.

## 5. Comparison boundary (physics enters only here)

At q₀ ≈ 1.10998 (muon pin) the ansatz is ≈ 4.1 × 10⁻³. The pivot splits are ≈ ∓0.624 (nucleon trace, additive
strands) and ≈ ∓0.208 (per strand): 50 to 150 times larger, and with the sign set by which map is chosen.
These numbers are not used in any argument above.

## 6. Options for the corpus (owner's decision)

1. Keep Step 2 as a labelled ansatz and cite this negative from the proof's Scope paragraph. Cheapest; no number moves.
2. Same as 1, and demote `prf:flavor-split-substrate` / `prop:flavor-split-substrate` to a conjecture (its
   statement already says "≈"). Touches the `.ts`/`.md` pair and the downstream readers of the 1.287 MeV figure.
3. Look for a U_q-breaking object with a triple zero (for example a boundary datum on the Bring colour tube). Open
   research; nothing on record suggests one.
