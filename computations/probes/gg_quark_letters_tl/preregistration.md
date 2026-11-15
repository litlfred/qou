# Quark letters and γγ words in the Jones (Temperley–Lieb) basis: pre-registration

Written and committed **before any number in this directory was computed**. Issue #7777. Bean `qou-ales`. Owner ruling 2026-10-12 (#7718, option 4): the quark sign map and the placement must be **derived** from γγ plus reading 3 at every strand count. Step 1 (#7760) found that the γγ core V³ has no h¹ term. Nothing here is adopted, ranked, or compared with data.

## 0. The basis, and why (stated before computing)

Under convention D the Markov weight of the (1³) block is zero, so the trace factors through the Temperley–Lieb quotient TL₃ = H₃ / (1³-block). This is the corpus's own statement (`ocneanuWeight_conventionD_eq_zero_of_three_rows`, and #7702's SU(2) reading). TL₃ has dimension 5, with basis

    1, e₀, e₁, e₀e₁, e₁e₀,

where e_i = (q − σ_i)/[2]_q is the Jones projection, the cap–cup, idempotent (`HeckeTowerBasicConstruction.lean:65`, `:113`). Inverting:

    σ_i = q·1 − [2]_q·e_i,        σ_i⁻¹ = q⁻¹·1 − [2]_q·e_i.

So in this basis **a single crossing's cap–cup coefficient does not depend on its sign; only the through-strand coefficient (q versus q⁻¹) does.** The step-2 question: when the quark letters and the γγ words are written in this basis, where exactly does flavour sit, and what does the γγ vertex already carry?

## 1. Computed (fixed)

TL₃ over ℚ(q), with relations e_i² = e_i, e₀e₁e₀ = [2]⁻²·e₀, e₁e₀e₁ = [2]⁻²·e₁, and σ_i ↦ q − [2]e_i. Elements:

- **Letters:** every template letter, meaning sign maps S+ (u=+, d=−), S− (u=−, d=+), S0 (all +), S1 (all −), and pair rules AVG, LO, HI, on generator 0 and on generator 1.
- **γγ words:** V^k (V = σ₀σ₁⁻¹) and U^k (U = σ₀σ₁), k = 1..6.
- **Nucleons (k = 0, no gluon), builder placement** (`pyhecke.atom.build_nucleon_nf_mp`):
  P = V³·L(u,u)₀·L(u,d)₀·L(u,d)₁ and N = V³·L(u,d)₀·L(u,d)₀·L(d,d)₁, for each of the 8 templates.

For each element, report all five TL coefficients exactly, and their values at q = 1.

## 2. Checks (pass/fail fixed in advance)

- **T1.** The image of σ_i satisfies the Hecke relation σ² = hσ + 1 and the braid relation in TL₃, exactly.
- **T2.** The bar involution (q ↦ q⁻¹, σ ↦ σ⁻¹) fixes each e_i. Equivalently, q⁻¹ − σ_i⁻¹ = [2]e_i.
- **T3.** The characters χ_(3) and χ_(2,1) of each nucleon element, computed from its TL coefficients in the two-row representations, reproduce #7718's committed exact values for S+ AVG (proton −0.09198, neutron −0.18200 at q₀; exact rational functions in `computations/probes/quark_template/results.json`). This is a consistency check of the map H₃ → TL₃, not a target.

## 3. Reported, with no expected answer

1. For each letter: its through coefficient and its e-coefficient. Is the e-coefficient the same across all flavours and pair rules?
2. For V and V³: the TL coefficients. In particular, how the vertex weights the cap–cup on its positive-crossing generator versus its negative-crossing generator.
3. For P and N under S+ versus S−: which TL coefficients differ, and at what order in t = q − 1.

## 4. Outcomes (stated before computing)

- **(i)** Flavour is confined to through coefficients, with letter e-coefficients identical across flavours. Then flavour is a bar-parity datum (q versus q⁻¹) on through-strands, and the cap–cup (pair) content is flavour-blind.
- **(ii)** Some letter's e-coefficient depends on flavour. Then flavour also enters the pair content.
- Either way, nothing is adopted. The sign map and placement stay open; this step only locates where a derivation would have to act.

## 5. Not done

No strand counts above 3, no gluon dressing, no comparison with data. Exact sympy arithmetic over ℚ(q); mpmath at 60 dps for display only.
