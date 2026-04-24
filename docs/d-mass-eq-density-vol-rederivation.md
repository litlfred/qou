# Deuterium: re-derivation of $\mathfrak{m} = \rho \cdot V$ from Frobenius

*Trace every step back to the paper blocks, flag what is derived vs.
asserted, locate where the +1.09% D residual can live.*

## Chain of identities

### Step 1 — Categorical mass from the Frobenius structure (derived)

From `def:mass-identity`:

$$
  \mathfrak{m}(\varrho)
  = \bigl\lVert \mathrm{tr}\bigl( (\textstyle\int_A \otimes \mathrm{id}) \circ \Delta \circ \varrho \bigr) \bigr\rVert
$$

for $\varrho\colon \mathbf{1}\to A$. This is a **direct definition**
from the Frobenius-Hopf structure $(\mathbf{C}, A, \tau)$: $\int_A$ is
the Frobenius form, $\Delta$ the comultiplication, $\mathrm{tr}$ the
categorical trace. Exact (no "$\approx$").

### Step 2 — Kashaev identification (conjecture, paper cites it as conjecture)

From `rem:kashaev-volume-density` + `def:algebraic-quantum-volume-specialization` route 2:

$$
  \mathrm{Vol}(K) \;=\; 2\pi\,\lim_{N\to\infty} \frac{\log|J_N(K; e^{2\pi i/N})|}{N}
$$

**Volume conjecture** (Kashaev–Murakami–Murakami). Proved for hyperbolic
knots with ≤ 7 crossings; conjecture in general. Identifies the hyperbolic
volume of $S^3\setminus K$ with the Kashaev asymptotic of colored Jones
at roots of unity.

### Step 3 — Particle-mass formula (exact algebraic restatement)

From `rem:kashaev-volume-density`:

$$
  \mathfrak{m}(K) \;=\; \mathrm{Vol}(K) \cdot \rho_q,
  \qquad
  \rho_q := \frac{1}{\hbar_q^2} = \frac{q^2}{(q-1)^2}
$$

The remark calls this an **"exact algebraic restatement"** of the
topological mass formula (`prop:topological-mass-formula`). No "$\approx$".

### Step 4 — Substrate-evaluation approximation (approximation introduced)

The "$\approx$" sign appears when the continuous Vol(K) is replaced by the
substrate evaluation of the colored Markov trace at finite $q_0$ (route 3
of `prop:algebraic-volume-specialization`):

$$
  \mathfrak{m}(K) \;\approx\; \rho_{q_0} \cdot \mathrm{Vol}_{q_0}(K)
$$

The error term is explicitly acknowledged as controlled by:
- Kashaev limit convergence rate
- Higher-order corrections to `thm:topological-mass`

### Step 5 — Nuclear-binding specialization (conjecture)

From `conj:mass-volume-factorization` + `rem:frobenius-packing-density`:

$$
  B(\mathcal{K}) \;=\; \rho_F(\mathcal{K}) \cdot V_\text{hyp}(\mathcal{K})
$$

where $\rho_F \in \{m_e, 2m_e\}$ is the **Frobenius packing density**,
set by which Wedderburn blocks of $H_{3A}(q)$ are populated:

- $\rho_F = m_e$ if **alt** ∉ Λ(K) (single-chirality)
- $\rho_F = 2m_e$ if **alt** ∈ Λ(K) (CPT-saturated)

Paper labels this a **conjecture** (see `conj:mass-volume-factorization`
§"Why this is a conjecture"):
1. JSJ decomposition compatible with Hecke grading — computational, not proved.
2. $\rho_F(P_i)$ determined locally by Wedderburn profile — **stated but not derived**.
3. Categorical mass ≡ topological Thurston volume at real $q_0$ — volume
   conjecture at real $q$, **open**.

### Step 6 — Deuterium assignment (claimed, not derived)

Paper's `conj:mass-volume-factorization` supporting-evidence table:

| atom | link | V | ρ | B_pred | B_AME |
|:----|:-----|--:|:-:|-------:|------:|
| D | $6_2$ | 4.400 | $m_e$ | 2.249 | 2.225 |

The assignment **D ↔ $6_2$** with **ρ = $m_e$** is asserted. The
reasoning given (`rem:frobenius-packing-density` §"topological triggers"):

> **Two-body links** (e.g. the knot $6_2$ representing deuterium) have
> only mutual linking of two components; the alt block remains suppressed
> and $\rho_F = m_e$.

So D ↔ 6_2 is stated as a TWO-BODY LINK, implying ρ_F = m_e. Not a derivation.

## What IS derived vs asserted

| element | status |
|---------|--------|
| Frobenius pairing → mass identity `m = ‖tr((∫⊗id)·Δ·ρ)‖` | ✓ derived from def |
| Particle formula `m(K) = Vol(K) · ρ_q` with $\rho_q = q^2/(q-1)^2$ | ✓ exact rewrite of topological-mass |
| Kashaev V = lim log\|J_N\|/N | Volume conjecture (proved ≤ 7 crossings) |
| Nuclear binding `B = ρ_F · V_hyp` | ⚠ conjecture |
| ρ_F ∈ {m_e, 2m_e} dichotomy | ⚠ conjecture, not derived from chirality |
| Alt-block rule (two-body → m_e, Borromean → 2m_e) | ⚠ heuristic, not derived |
| D ↔ $6_2$ specifically | ⚠ asserted (two-body link claim) |

## Computing D's residual cleanly

Under the asserted rules:
$$
  B_\text{pred}(D) = m_e \cdot V_\text{hyp}(6_2) = 0.51099895 \cdot 4.4008325161\ldots = 2.2488208\ldots \text{ MeV}
$$

$$
  B_\text{AME}(D) = 2.22456612 \text{ MeV},\qquad \text{residual} = +0.0242547 \text{ MeV} = +1.0903\%
$$

## Where can the 10.9 Mppb residual live?

Walking the derivation chain:

### (a) Precision of inputs

Already ruled out (see `docs/d-error-budget.md`): m_e to 10⁻¹⁰, V(6_2)
to 50 HP digits, q₀ CODATA-bounded at ~1 ppb. Total ≤ 1000 ppb.

### (b) The "≈" in step 4

The paper labels `m ≈ ρ·V` as a derived **approximation**, with error
controlled by:
- Kashaev limit convergence rate at finite $N$
- Higher-order corrections to topological mass

**For D, the Kashaev is fully convergent** (D is hyperbolic; Vol
conjecture proved for ≤ 7-crossing knots). So the convergence term
should be negligible. The higher-order corrections are the open piece.

### (c) The ρ_F conjecture (step 5)

Claim: D's atomic braid populates sym + std but NOT alt. Verification
requires computing the Wedderburn decomposition of D's Hecke element
and showing the alt partition $(1,1,1)$ (in H_3) or its H_n analogue
has zero coefficient. This has not been done rigorously for D.

If alt IS lightly populated — say, with some small weight — the effective
density would be $\rho_F = m_e \cdot (1 + \delta)$ with $\delta \neq 0$.
That would shift $B_\text{pred}$ multiplicatively.

Numerically: $\delta = -0.0108$ (i.e., −1.08%) exactly fits the
residual. **This is a candidate derivation target**: compute
$w_\text{alt}(D)$ from D's full Hecke NF and see if it equals $0.0108$.

### (d) D ↔ 6_2 might be wrong

If D's true atomic link is not 6_2 but some nearby hyperbolic knot with
$V = 4.35328$ exactly (= $B_\text{AME}/m_e$), that would also close
the gap. **But** the census search in `jsj_verification.py` found 6_2
as the closest catalog knot (1.09% from target); the next options
are 5-7% off. Either (i) D's true link is not in the ≤ 8-crossing
census, or (ii) ρ_F = m_e isn't exact.

### (e) The Hecke NF route is independent

The per-block log formula `binding_per_block_log.py` computes B(D)
via the algebraic volume path without SnapPy — and gives +130% error.
So the Hecke-NF-native formula is not a better baseline; the
SnapPy+Kashaev path is literally the best we have.

## Concrete next actions to nail the 1.09%

1. **Compute D's Wedderburn profile explicitly.** Take the 300-term
   NF (in `deuterium-optimal-nf.py`, 7-strand quark model) or the
   32-term NF (my `atom_nf_symbolic_D.py`, 6-strand particle model),
   and decompose into sym/std/alt components per partition. Read
   off the alt coefficient.
2. **If alt has nonzero weight $w_\text{alt}$:** effective ρ = $m_e + w_\text{alt}·m_e$
   (or similar). Check numerically.
3. **If alt is exactly zero:** then step 5 is intact and the +1.09%
   must live in step 4 (higher-order Kashaev corrections) or the
   knot assignment (step 6).

Step 3 → if alt = 0 at D, the next frontier is the **colored-Jones
correction at finite N** (the Kashaev limit's tail term). This is
Phase 2 pentagon-defect territory.

## Pointers

- Formula chain: `rem:kashaev-volume-density` → `prop:topological-mass-formula` → `conj:mass-volume-factorization` → `rem:frobenius-packing-density`
- Code: `mass_table_ppb.py` (zero-parameter); `binding_per_block_log.py` (Hecke-NF route); `d_wedderburn_mass.py` (naive Wedderburn)
- NFs: `deuterium-optimal-nf.py` (300 terms, 7-strand) and its witness
- Prior error budget: `docs/d-error-budget.md`
- Related propositions (PR #397): `prop:markov-pair-z2`, `prop:pentagon-uv-commutation`, `prop:delta-max-uniform-bound`, `prop:descended-level-zero`
