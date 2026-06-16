# D's Hecke NF — what knot operators appear

*Per-user direction: "in NF calculations you can see knot operators."
Dictionary-model deuterium, symbolic in q.*

## Existing pipeline

`computations/deuterium-optimal-nf.py` already
computes D's atom Hecke NF in the dictionary model (trefoil quarks
per Remark 4.25.4 Table 4):

- 7 strands: `types = [u, u, d, u, d, d, e]` (proton uud + neutron
  udd + atomic electron)
- Quark crossings: uu → σ₀σ₁σ₀ (trefoil), dd → σ₀⁻¹σ₁⁻¹σ₀⁻¹ (mirror
  trefoil), ud → ½(σ₀σ₁σ₀ + σ₀⁻¹σ₁⁻¹σ₀⁻¹) (average)
- Protium (u,u,d,e) = 5-term NF, registered as ℵ₁ quotient
- Deuterium = reduction to NF in H₇(q)

## Existing stored witness

`computations/deuterium-optimal-nf.witness.json`
carries the layered decomposition by ℵ₁-count (protium
completeness):

| layer | terms | net @ q₀ | |abs|.weight @ q₀ |
|-------|------:|---------:|-----------------:|
| **ℵ₁⁴ (optimal)** | **7** | **+2.863033** | 4.441992 |
| ℵ₁³ | 23 | −1.209367 | 1.551340 |
| ℵ₁² | 32 | −0.262980 | 0.424394 |
| ℵ₁¹ | 32 | +0.087859 | 0.121066 |
| ℵ₁⁰ | 8 | −0.000542 | 0.000654 |

The aleph_1^4 layer is the one whose terms contain ℵ₁ (= protium)
with full completeness 4. Its word-length histogram
(sigma-generators only, stripping ℵ₁):

| sigma-word length | count |
|------------------:|------:|
| 3 | 1 |
| 4 | 3 |
| 5 | 2 |
| 7 | 1 |

Total: 7 terms = 7 strands. The script's docstring calls this the
"optimal Gröbner–Shirshov basis for deuterium."

## Knot-operator identification (from NF_BASIS)

`knot-operator-table.py` and `basis_knot_tables.py` fix the
H₃(q) basis dictionary:

| word | name | knot |
|------|------|------|
| `()` | γ | unknot (0₁) |
| `(0,)`, `(1,)` | σ₀, σ₁ | virtual (ℓ=1) |
| `(0,1)`, `(1,0)` | L₊, L₋ | Hopf link |
| `(0,1,0)` | e⁻ | trefoil (3₁) |

For the 7-strand H₇(q) NF of deuterium, named sub-patterns from
the script:

| sub-word | name |
|----------|------|
| `(3, 4, 3, 5)` | n₁ (neutron tail) |
| `(2, 3, 2)` | I₇ (electron bridge) |
| `(0, 1)` | I₁_ext (σ₀ extension) |
| `(0, 2, 3, 2)` | I₁·I₇ (extended bridge) |

## Symbolic Markov trace of the aleph_1^4 layer

From the stored witness:

$$
  \mathrm{tr}_M(\mathrm{optimal\ layer})(q_0) = -0.005440624\ldots
$$

and a symbolic expression that is a ratio of polynomials in $q$ of
degree $\leq 32$ in numerator, degree $\leq 26$ in denominator.

## What this means for Phase 3

1. **D's NF IS known and explicit at the Hecke level.** 300 terms
   in H₇(q) (34.8s build time); 7 of them in the aleph_1^4 layer
   that contains the actual deuterium content.
2. **The "knot operators" the user referenced are visible** as
   named sub-patterns — trefoil (length-3), Hopf link (length-2),
   etc. — embedded in the length-3/4/5/7 NF basis words.
3. **The Markov trace = Jones polynomial is a computed symbolic
   function in q** (not a catalog knot's Jones). So D's atom does
   NOT have a low-crossing-catalog-knot Jones polynomial — its
   Jones is the specific rational function from the 7-term layer.
4. **SnapPy's Vol(6_2) = 4.40083 was a census MATCH not a
   derivation.** 6_2's Jones is $q^{-5} - 2q^{-4} + 2q^{-3} - 2q^{-2}
   + 2q^{-1} - 1 + q$; D's Jones is a high-degree rational (above).
   They are different polynomials.

## The formal route to B(D)

Per `def:algebraic-quantum-volume-specialization`:

$$
  B(D) = -\alpha \cdot \Phi_1(D) \cdot (\text{Wedderburn weights})
$$

where $\Phi_1(D) = \ln|\mathrm{Vol}_{q_0}(D\text{-NF})|$ from the
transfer-matrix chain. This does NOT go through SnapPy. The
Wedderburn weights involve Vol², Vol³ via the sym/alt/mixed
decomposition of the H₇(q) regular representation.

Current mass_table_ppb.py uses $\alpha = m_e \cdot 8G$ and
$\Phi_1$-only, which gives D at −94.8% (very wrong). Either the
full Wedderburn-weighted product OR a different α formula is
needed to get D to ppb-precision from the symbolic NF.

## Suggested next step

Implement the full Wedderburn formula directly from D's 7-term
optimal layer:
1. Take the symbolic Markov trace polynomial (we have it).
2. Decompose into chirality blocks (sym/alt).
3. Construct $\mathrm{Vol}^{(1)} \cdot \mathrm{Vol}^{(2)^{-2[3]_q}} \cdot
   \mathrm{Vol}^{(3)^{H_A^2}}$.
4. Evaluate at $q_0$, take log.
5. Compare to $B_\text{AME}(D)$ at ppb.

All symbolic, no SnapPy, no knot-matching needed. This is the
"knot operators in NF → mass formula" path the framework intends.

## Pointers

- `computations/deuterium-optimal-nf.py`
- `computations/deuterium-optimal-nf.witness.json`
- `computations/trefoil-quark-nucleon-nf.py`
  (dictionary-model quark + nucleon NFs)
- `computations/knot-operator-table.py`
  (H₃ NF basis = named knot operators)
- `computations/basis_knot_tables.py`
  (H₃ 6-basis multiplication tables)
- `content/quantum-observable-universe/braids-and-knots/algebraic-quantum-volume.md`
- `content/quantum-observable-universe/braids-and-knots/algebraic-quantum-volume-specialization.md`
- `content/quantum-observable-universe/particle-interactions/wedderburn-mass-formula.md`
