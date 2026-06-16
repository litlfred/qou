# D's 1.09% residual — session summary

*Systematic check of the D binding prediction via the
formula chain from Frobenius → $\mathfrak{m} = \rho \cdot V$.
Everything tried, everything that matters, honestly.*

## Starting point

$$
  B_\text{pred}(D) = m_e \cdot V_\text{hyp}(6_2) = :val[m_e_MeV]{precision=6} \cdot 4.4008325161\ldots = 2.2488208 \text{ MeV}
$$

$$
  B_\text{AME}(D) = 2.22456612 \text{ MeV},\qquad \text{residual} = +1.0903\%
$$

## Hypotheses tested

### (1) Precision of inputs

Ruled out. m_e CODATA ±1.5e-10; Vol(6_2) at 50 HP digits; q₀ at
~1.22e-9 (CODATA-bounded). All sub-ppb.

### (2) Wrong knot assignment

**Tested: extended census up to 14 crossings** + Dehn surgeries on
s776 (magic manifold) + q in [1,9] × p in [-10,10].

- **No hyperbolic manifold in the ≤ 14-crossing census has
  Vol = 4.35328** within 1.5% tolerance.
- Closest after 6_2: 9²_50 and 10²_126 at Vol = 4.41533 (+1.42%)
- Dehn surgeries on s776: zero matches within 1%.

Conclusion: either D's atom-link is at ≥15 crossings (unlikely
for a 2-nucleon system) OR D is not a single knot (user direction).

### (3) Full Wedderburn decomposition

Re-derived from `def:mass-identity` → `rem:kashaev-volume-density`
→ `prop:wedderburn-mass-formula` → `prop:tower-binding-energy`.

**Computed D's per-partition Wedderburn profile** ($n = 3A = 6$):

| partition | role | dim | dim_q | w_λ | χ_λ(β_D) | contribution |
|-----------|------|----:|------:|----:|---------:|-------------:|
| (6) | **sym** | 1 | 1.00 | 0.0012 | **+1.5598** | +1.86e-3 |
| (5,1) | mixed | 5 | 5.22 | 0.0325 | +3.2159 | +2.09e-2 |
| (4,2) | mixed | 9 | 9.67 | 0.1115 | +1.6737 | +2.07e-2 |
| (4,1,1) | mixed | 10 | 10.67 | 0.1357 | -0.4702 | -6.38e-3 |
| (3,3) | mixed | 5 | 5.45 | 0.0354 | +4.2491 | +3.01e-2 |
| (3,2,1) | mixed | 16 | 17.34 | 0.3586 | -1.9728 | -4.42e-2 |
| (3,1,1,1) | mixed | 10 | 10.67 | 0.1357 | -0.4900 | -6.65e-3 |
| (2,2,2) | mixed | 5 | 5.45 | 0.0354 | -3.4976 | -2.48e-2 |
| (2,2,1,1) | mixed | 9 | 9.67 | 0.1115 | -0.8197 | -1.02e-2 |
| (2,1,1,1,1) | mixed | 5 | 5.22 | 0.0325 | +2.1554 | +1.40e-2 |
| (1^6) | **alt** | 1 | 1.00 | 0.0012 | **-0.6769** | -8.07e-4 |

Key: **χ_alt(β_D) = -0.6769 ≠ 0**. The alt partition is populated.
This disproves the naive reading of `rem:frobenius-packing-density`
two-body → unpopulated → ρ_F = m_e. What's small is the
Plancherel weight, not the character.

### (4) Per-block log formula

Restored from the deprecated `binding_per_block_log.py` (commit
30d7a33c). Direct formula from `prop:tower-binding-energy`:

$$B = \sum_\lambda w_\lambda \cdot m_e \cdot \sum_i \log|\Phi_q(\hat V_i^\lambda)|$$

**D prediction: +5.11 MeV** (vs AME 2.22), i.e. **+130% on binding**.

Note: the paper's own numerical table in `prop:tower-binding-energy`
shows $B_\text{pred}(D) = 4.92$ MeV, $B_\text{obs} = 2.22$. It reports
"mass error -0.144%" — correct, but on TOTAL MASS (~1876 MeV),
not on binding. On BINDING, the paper's own formula is +122% off.

The "0.15% baseline floor" in the docstring is a mass metric, not
a binding metric. Misleading at ppb scale.

### (5) Naive Wedderburn (d_wedderburn_mass)

My implementation: $\alpha \log|w_\text{sym}\lambda^\text{sym} +
w_\text{std} V^\text{std} + w_\text{alt}\lambda^\text{alt}|$ summed
over generators.

**D prediction: +0.11 MeV** (vs AME 2.22), i.e. **-95% on binding**.

### (6) binding_full_pipeline (canonical + Kähler tower)

Runs. **D prediction: +28817 MeV**. Diverges.

### (7) Jet brane tower

From commit 30d7a33c: jet-tower augmentation
$B = B_\text{level-0} + \sum_n \hbar_q^{2n} \Delta^{(n)}$.

- N=1: tail ≤ 1.9e-4 MeV
- N=2: tail ≤ 1.8e-6 MeV
- N=3: tail ≤ 1.8e-8 MeV (sub-ppb)

**The jet-tower tail is bounded far below the 24 MeV residual.**
The accumulation across levels doesn't close the +1.09% gap.
However, the tail bound is $\Delta_\text{max}$ from
`prop:delta-max-uniform-bound`; the explicit summed contribution
could be larger than the bound suggests (bound is uniform, not tight).

## Honest current state

| approach | B_pred(D) | err on binding |
|----------|----------:|---------------:|
| m_e · Vol(6_2) | 2.249 MeV | +1.09% |
| Wedderburn naive | 0.11 MeV | -95% |
| Per-block log (paper) | 5.11 MeV | +130% |
| binding_full_pipeline | 28817 MeV | diverges |
| AME2020 | 2.2246 MeV | — |

Kashaev + census-match with 6_2 is the CLOSEST at 1.09%. Every
more "principled" path gives a worse number.

## Where the 1.09% most likely lives

Given the exhaustive checks:

- NOT in input precision (ruled out).
- NOT in wrong-knot-within-14-crossings (ruled out).
- NOT in Wedderburn chirality blocks (computed; alt IS populated,
  but net contribution is dominated by middle-partition terms).
- NOT in jet-tower tail (bounded sub-ppb).
- Possibly in: the Kashaev IDENTIFICATION itself (volume
  conjecture at finite q₀ has subleading corrections).
- Possibly in: the ρ_F = m_e dichotomy rule being exact instead
  of fractional. Paper acknowledges this is "stated, not derived."
- Possibly in: D being "not a single knot" — sum over multiple
  JSJ pieces, where `V_hyp(6_2)` captures the dominant piece but
  not all of them.

## What needs to happen for 1 ppb on D

One of:
1. A derivation showing χ_alt(β_D) contribution is exactly zero
   (contradicts numerical finding: χ_alt = -0.6769).
2. A working accumulation-over-tower formula that doesn't diverge
   (binding_full_pipeline's 28817 MeV suggests a coefficient bug
   or missing regularization).
3. An explicit derivation of ρ_F beyond the "m_e or 2m_e" dichotomy,
   allowing fractional density tied to the alt-block character.
4. A non-single-knot JSJ decomposition for D's atomic complement
   with sub-6_2 pieces whose contributions sum to the residual.

None of these are reachable in this session without fresh
theoretical input.

## Pointers

- `docs/d-error-budget.md` — initial precision audit
- `docs/d-mass-eq-density-vol-rederivation.md` — formal chain audit
- `docs/d-nf-knot-operators.md` — D's NF operators
- `computations/d_wedderburn_mass.py`
- `computations/d_wedderburn_profile.py` — per-partition
- `computations/d_knot_extended_search.py` — census ≤ 14
- `computations/binding_per_block_log.py` — paper-exact
- `computations/mass_table_ppb.py` — zero-param table
