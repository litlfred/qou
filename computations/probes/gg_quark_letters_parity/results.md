# Does the γγ construction fix each quark letter's through-strand parity? Results

Recipe: `preregistration.md` (`74045a7695d`), committed before computing. Producer: `gg_quark_letters_parity_probe.py`. Witness: `gg-quark-letters-parity.witness.json` (records the proton pin q₀). Exact over ℚ(q); signs on (1, ∞) by exact Sturm counts and rational root isolation; mpmath 60 dps for display. Wall time ≈ 10 s. Issue #7777, beans `qou-ales`, `qou-99qc`. Nothing adopted, ranked, or compared with data.

One code fix after the first run, before any interpretation: the sign sampler cut at both ends of each root-isolating interval, which reported a spurious third sign segment. It now samples only in the root-free gaps. The root counts and all values were unchanged.

## Checks: 4/4 pass

| check | what it confirms | result |
|---|---|---|
| P0 | TL coefficients of V and V³ equal step 2's witness exactly | pass |
| P1 | all 8 templates at the builder placement reproduce #7718's χ_(3), χ_(2,1) exactly; S+AVG reading-3 verdicts at q₀ for all 8 placements match #7718 (4/8 each nucleon) | pass |
| P2 | V·e₁ = −q·σ₀·e₁ and e₀·V = −q⁻¹·e₀·σ₁⁻¹, the identities fixed by hand in advance | pass |
| P3 | the one-sided ideal structure the survivor rule relies on | pass |

## The rules' outputs

| rule | generator 0 | generator 1 | placement | flavour sign map |
|---|---|---|---|---|
| R1 vertex inheritance | σ₀ (q) | σ₁⁻¹ (q⁻¹) | not fixed | not fixed |
| R2 h-leading residue of V³ | σ₀⁻¹ (q⁻¹) | σ₁ (q) | not fixed | not fixed |
| R3a Jones-pair closure on V | **ambiguous**: q or −q(q²−1) | **ambiguous**: q⁻¹ or (q²−1)/q³ | not fixed | not fixed |
| R3b Jones-pair closure on V³ | no letter parity (4 closures, none q^{±1}) | no letter parity | not fixed | not fixed |
| R4 pair-production balance | [2]/2 (bar-fixed) | [2]/2 (bar-fixed) | not fixed | not fixed |
| R5 flavour dictionary | — | — | — | **cannot** |

**R3 in detail** (survivor through coefficient c = −[2]a/b after annihilating one pair with the Jones projection):

| word | closure | survivor on | c |
|---|---|---|---|
| V | e₁ on the right | g0 | **q** (σ₀), with scalar −q |
| V | e₁ on the left | g0 | −q(q²−1) |
| V | e₀ on the left | g1 | **q⁻¹** (σ₁⁻¹), with scalar −q⁻¹ |
| V | e₀ on the right | g1 | (q²−1)/q³ |
| V³ | e₁ right | g0 | q³(q³−q−1)(q³−q+1)/((q²−1)²(q⁴+1)) |
| V³ | e₁ left | g0 | −q(q⁵−q⁴−q³+q²−1)(q⁵+q⁴−q³−q²+1)/((q²−1)²(q⁴+1)) |
| V³ | e₀ right | g1 | (q⁵−q³−q²+q+1)(q⁵−q³+q²+q−1)/(q³(q²−1)²(q⁴+1)) |
| V³ | e₀ left | g1 | −(q³−q²+1)(q³+q²−1)/(q(q²−1)²(q⁴+1)) |

- On a single vertex, the closure **adjacent** to the annihilated crossing returns that vertex's other crossing with its own parity, exactly R1. The non-adjacent closure returns a through coefficient that is not a crossing at all. By the pre-registered criterion (all four closures must agree) R3a is ambiguous.
- On the confined core V³, **no** closure returns q, q⁻¹ or [2]/2. Every survivor coefficient has (q²−1)² in its denominator: V³ = 1 at q = 1, so the cap–cup part b vanishes to second order there, and the survivor is not a letter. **The Jones-pair closure of the core does not fix a through parity.** This is the case the owner asked for, and it is an honest gap.

## Reading 3 on each rule's family (level m = 3, the only level at n = 3)

All rule elements are identical for proton and neutron (no rule reads quark content), so each row covers both. Letters in pair order (0,1), (0,2), (1,2). χ_(3) > 0 on all of (1, ∞) in every row. ✓ = χ_(2,1) ≥ 0.

| placement | R1 χ_(2,1)(q₀) | R1 at q₀ / on (1,∞) | R2 χ_(2,1)(q₀) | R2 at q₀ / on (1,∞) | R4 χ_(2,1)(q₀) | R4 at q₀ / on (1,∞) |
|---|---|---|---|---|---|---|
| 000 | +0.60481 | ✓ / ✗ (root 1.37230) | −0.66413 | ✗ / ✗ | −0.02873 | ✗ / ✗ |
| 001 (builder) | −0.42477 | ✗ / ✗ (root 1.42916) | +0.48410 | ✓ / ✓ | +0.02873 | ✓ / ✓ |
| 010 | −0.42477 | ✗ / ✗ (root 1.42916) | +0.42726 | ✓ / ✓ | +0.00031 | ✓ / ✓ |
| 011 | +0.42477 | ✓ / ✗ (root 1.42916) | −0.48410 | ✗ / ✗ | −0.02873 | ✗ / ✗ |
| 100 | −0.36794 | ✗ / ✗ (root 1.27890) | +0.42726 | ✓ / ✓ | +0.02873 | ✓ / ✓ |
| 101 | +0.42477 | ✓ / ✗ (root 1.42916) | −0.42726 | ✗ / ✗ | −0.00031 | ✗ / ✗ |
| 110 | +0.36794 | ✓ / ✗ (root 1.27890) | −0.42726 | ✗ / ✗ | −0.02873 | ✗ / ✗ |
| 111 | −0.60481 | ✗ / ✗ (root 1.37230) | +0.66413 | ✓ / ✓ | +0.02873 | ✓ / ✓ |

Template-expressible rows (same letters as a #7718 template for both nucleons): R1·000 = S0·000, R1·111 = S1·111, R2·000 = S1·000, R2·111 = S0·111. Every other row is outside the template family, because a template gives the two ud letters of the proton the same letter, while these rules can put them on different generators with different parities.

These verdicts are reported, not used. No rule or placement is preferred because it passes.

## Outcome

- **Flavour sign map: outcome (iv).** No rule fixes it. R1–R4 depend only on the generator, never on the quark content, so the proton and neutron elements are identical under each of them. The only γγ datum that distinguishes two produced lines is their parity, and the two dictionaries u ↔ q and u ↔ q⁻¹ are exchanged by the bar involution. Nothing in V, V³ or its closures names a flavour (R5).
- **Generator parity: outcome (iii).** The rules that fix one disagree: R1 gives (g0, g1) = (q, q⁻¹), R2 the opposite, R4 the bar-fixed average on both. The Jones-pair closure agrees with R1 on a single vertex only for adjacent closures (ambiguous by the pre-registered criterion), and fixes nothing on the core.
- **Placement:** no rule fixes it.

## What this leaves open

- **The gap is a flavour-to-line dictionary.** Fixing the sign map needs a rule that maps quark flavours to produced lines. The γγ construction does not supply one at n = 3, and neither does the Jones-pair closure. Any choice between u ↔ q and u ↔ q⁻¹ made without such a rule would be a hand pick, which option 4 forbids.
- **The placement is also open.** None of R1–R4 constrains it.
- **Not tested:** constructions above three strands, where produced lines could sit on their own strands and the pair closure would act between them; the gluon pair; two nucleons. A rule living there would need its own pre-registration.
- Scope (a): this concerns these five rules at n = 3. It does not exclude a flavour-reading rule from a larger construction.
