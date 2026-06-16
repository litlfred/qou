# PR #1122 retraction + adapting existing canonical-derivation classes

**Date:** 2026-05-24
**Trigger:** User challenge: *"Is this proved formally? Are you sure you
have a hold of the factors? you check the complete GB filtration and
jet order"* + follow-up: *"can you investigate if any of the existing
canonical derivation proofs can be adapted to be utilized here?"*

## §1. Retraction of PR #1122's "STRONG result" claim

PR [#1122](https://github.com/litlfred/qou/pull/1122) titled "W = √[2]_q
closes ratios to 7% (STRONG)" claimed:
- At substrate q_0, N=2: applying √[2]_q to W gives total |dev| = 7.11% across SM ratios
- The √[2]_q is "the quantum spinor norm — categorically derived"

**These claims are overstated.** The jet-order validation probe
[`rt_w_sqrt2_jet_order_validation.py`](../../computations/rt_w_sqrt2_jet_order_validation.py)
(this session, post-challenge) shows:

### What the jet-order check reveals

At every jet order h^{2j} (j = 0, 1, 2, 3), the **uncorrected** colored
Jones ratios are EXACTLY the twist-count ratios:

| ratio | jet 0 | jet 2 | jet 4 | jet 6 | SM | structural |
|---|---:|---:|---:|---:|---:|---|
| W/Z | 0.667 | 0.663 | 0.667 | 0.667 | 0.882 | = 4/6 (twist) |
| Z/H | 0.750 | 0.745 | 0.750 | 0.750 | 0.729 | = 6/8 (twist) |
| W/H | 0.500 | 0.494 | 0.500 | 0.500 | 0.643 | = 4/8 (twist) |

**The colored Jones at small h is proportional to n (twist count)**,
so the bare RT chain gives WZH ratios = 4:6:8.

### With √[2]_q correction on W (PR #1122's claim)

At every jet:
- W/Z ≈ 0.94 (vs SM 0.882) → **+7% dev** (consistent jet-to-jet)
- Z/H ≈ 0.75 (vs SM 0.729) → +3% dev (consistent)
- W/H ≈ 0.71 (vs SM 0.643) → +10% dev (consistent)

**Total ~20% per jet, consistent across jets.** The √[2]_q correction
is JET-STABLE (good — not a numerical accident) but SYSTEMATICALLY
OVERSHOOTS (W needs more boost; H needs less).

### Why PR #1122's 7.11% number was misleading

PR #1122 measured `|J_N(T(2,k), q_0)|` at the **substrate point** —
which mixes all jet orders weighted by $h_0^{2j} \approx 0.044^j$. The
jet-mixing happens to land near SM ratios with √[2]_q correction by
coincidence; the underlying h-expansion shows the W needs +32% boost
while H needs -29% reduction.

**A SINGLE multiplicative W-only correction CANNOT close both W/Z and
H/Z simultaneously** because they require boosts in opposite directions.

### What IS structurally real (kept)

- **Z/H ratio match** within ~3% at every jet order — this IS genuine
  because Z and H share the twist-count ratio 6/8 = 0.75, very close to
  SM 0.729. The framework's twist-count structure matches the Z/H SM
  ratio AT THE GB-FILTRATION LEVEL.
- **The RT-chain SM identification** W=T(2,4), Z=T(2,6), H=T(2,8)
  remains the framework's cohomological assignment (from existing
  `electroweak-higgs-torus-link-triplet.md`).

### What was NOT real (retracted)

- The √[2]_q correction is NOT a categorical structural fact at the
  jet-order level
- The "7.11% match" was a substrate-point coincidence; jet-order
  validation shows 20% per jet
- The categorical origin attribution to "quantum spinor norm" was
  speculation

## §2. Existing canonical-derivation classes — what's adaptable

The repo has substantial existing Lean infrastructure. Two classes are
DIRECTLY applicable to the torus-knot RT chain:

### 2.1 `QOU.Kashaev.VolumeConjecture` (existing, `lean/QOU/Kashaev.lean`)

Encodes the Kashaev volume conjecture:
$$\mathrm{Vol}(S^3 \setminus K) = 2\pi \lim_{N \to \infty} \frac{\log |J_N(K, q)|}{N}$$

For torus knots, Vol = 0 (Seifert-fibered, not hyperbolic), so the
class IMPLIES:
$$\lim_{N \to \infty} \frac{\log |J_N(T(2, n))|}{N} = 0$$

i.e., $|J_N(T(2, n))|$ grows **sub-exponentially** in N. This is
ALREADY ENCODED in the existing class. My Q3 finding ("torus knots
have Vol = 0; canonical VolDensity gives zero mass") is structurally
captured by this typeclass.

**Adaptation candidate**: extend with a `TorusKnotKashaevLimit` subclass
that supplies the polynomial-growth rate of $|J_N(T(2, n))|$ for the
SM torus-link masses.

### 2.2 `QOU.QuantumObservableUniverses.CategoricalHiggsIdempotent` (existing, placeholder)

Per [`CategoricalHiggsIdempotent.lean`](../../content/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/CategoricalHiggsIdempotent.lean):
the conjecture states there is a Frobenius–Hopf idempotent
$e_H : A \to A$ projecting onto unbroken $\mathrm{U}(1)_{em}$, with:

- $G = \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ group action
- Higgs doublet $\Phi \in V_{1/2, 1/2}$ (spin-$\tfrac{1}{2}$ of
  $\mathrm{SU}(2)_L$, hypercharge $Y = \tfrac{1}{2}$)
- VEV $\langle \Phi \rangle = (0, v/\sqrt{2})^\top$

**The $\sqrt{2}$ factor in the SM Higgs VEV decomposition** is in this
existing class. The W boson mass $m_W = gv/2$ is derived FROM the
lower-component VEV $v/\sqrt{2}$, with an implicit $\sqrt{2}$ in the
W coupling.

**This is the categorical origin of any $\sqrt{2}$ that appears in the
framework's W mass formula** — but it's the SM Higgs-VEV convention,
NOT a deeper structural fact about the RT chain.

### 2.3 What PR #1122's √[2]_q actually means in this context

The framework's RT-chain `|J_N(T(2,k))|·N·m_e` formula, when fit to
SM W:Z:H ratios via a W-only √[2]_q correction at q_0, is implicitly
**recovering the SM Higgs-VEV doublet-normalization convention**. It's
NOT deriving the W mass from substrate; it's matching a known SM
normalization that lives in the (pre-existing, placeholder)
`CategoricalHiggsIdempotent` class.

## §3. What a RIGOROUS derivation would look like

Three structural pieces would together constitute a real categorical
W mass derivation:

### A. Refined `CategoricalHiggsIdempotent` class

Currently a placeholder with a single `residual = 0` field. Refine to:

```lean
class CategoricalHiggsIdempotent extends FrobeniusHopfSubstrate where
  /-- The Higgs doublet as element of the spin-1/2, Y=1/2 irrep. -/
  Phi : SpinIrrep (1/2) × HyperchargeIrrep (1/2)
  /-- The vacuum expectation value v in MeV (CAL-1 anchor + g coupling
      derive from this). -/
  vev_v : ℝ
  /-- The VEV's doublet decomposition: lower component carries v/√2. -/
  vev_decomposition : ⟨Phi⟩ = (0, vev_v / Real.sqrt 2)
  /-- The categorical Higgs idempotent e_H projecting onto U(1)_em. -/
  e_H : A → A
  /-- e_H is idempotent. -/
  e_H_idempotent : e_H ∘ e_H = e_H
  /-- e_H projects onto unbroken U(1)_em. -/
  e_H_projects_to_em : ker(e_H) = SU(2)_L_broken_directions
```

This makes the $\sqrt{2}$ factor EXPLICIT in the class structure.

### B. `TorusKnotMass` class extending KashaevConjecture

```lean
class TorusKnotMass (q_0 : ℝ) extends QOU.Kashaev.VolumeConjecture q_0 where
  /-- For T(2, k), polynomial growth rate of |J_N| in N. -/
  growth_rate_T2k : ℕ → ℕ → ℝ
  /-- Vol = 0 implies kashaevLimit = 0; growth_rate captures sub-exp. -/
  is_polynomial : ∀ k, kashaevLimit (T2_braid k) = 0
  /-- Categorical mass formula for torus knots T(2, k): combines
      polynomial growth rate with Higgs VEV when k corresponds to
      a charged particle (W±). -/
  mass_formula : ∀ k, ℝ
```

The `mass_formula` field encodes:
- For W (k=4, charged): `mass = m_e · growth_rate · g · v / (2)` where
  `v / √2` comes from `CategoricalHiggsIdempotent.vev_decomposition`
- For Z (k=6, neutral): `mass = m_e · growth_rate · √(g²+g'²) · v / 2`
- For H (k=8, scalar): `mass = m_e · growth_rate · (Higgs self-coupling structure)`

This would be a STRUCTURAL derivation of why W has a $\sqrt{2}$ factor
relative to the bare $|J_N|$ — it's the Higgs VEV's lower-component
normalization, encoded in the existing (placeholder) class.

### C. Proof obligations

A real proof would need:
1. Show `mass_formula T(2,4) / mass_formula T(2,6) = cos θ_W` (W/Z ratio)
2. Show `mass_formula T(2,6) / mass_formula T(2,8) = m_Z/m_H` (Z/H ratio)
3. Both proofs use the explicit `vev_decomposition` field

These are not free; they require:
- A categorical derivation of $g, g'$ couplings from substrate (not
  currently in framework)
- A derivation of `growth_rate_T2k` from RT-TQFT first principles
- A formal Lean proof tying them together

Effort: **research-grade, multi-week**.

## §4. Honest summary

| claim | status | evidence |
|---|---|---|
| Z/H ratio match within ~3% | **STRUCTURAL** ✓ | jet-order check; Z & H share twist-count ratio 6/8 ≈ SM 0.729 |
| W ratios off by ~30% (no correction) | **CONFIRMED** ✓ | jet-order check; W has twist-count 4 vs Z/H's 6/8 |
| W = √[2]_q correction closes ratios to 7% (PR #1122) | **OVERCLAIMED** ✗ | substrate-point coincidence; jet-order check shows 20% per jet |
| √[2]_q is "quantum spinor norm" (PR #1122) | **SPECULATION** ✗ | the √2 is the SM Higgs-VEV doublet normalization (existing `CategoricalHiggsIdempotent` class) |
| RT-chain SM particle map W=T(2,4), Z=T(2,6), H=T(2,8) | **EXISTING** ✓ | `electroweak-higgs-torus-link-triplet.md` (not from this session) |
| Categorical W mass derivation | **OPEN** | research-grade; requires refining 2 existing classes (§3) |

## §5. Adaptable next steps (queued)

1. **Refine `CategoricalHiggsIdempotent`** to encode the doublet
   structure + VEV decomposition with explicit √2. ~50 lines Lean,
   1 day. Promotes the placeholder class to structural content.

2. **Define `TorusKnotMass` extension class** of `VolumeConjecture` for
   the RT chain. ~100 lines Lean, 2-3 days. Encodes the polynomial-
   growth + mass-formula structure.

3. **Derive W/Z = cos θ_W from class hypotheses** as a conditional
   theorem. Heavy: 1-2 weeks if the categorical coupling-constants
   chain is filled in.

These adaptations would convert PR #1122's empirical W = √[2]_q
finding into a structurally-grounded conditional theorem (modulo
class instances). NONE are implemented in this session — listed as
the next concrete Lean work.

## §6. Cross-references

- [PR #1122](https://github.com/litlfred/qou/pull/1122) — overclaimed "STRONG" finding being retracted here
- [`computations/rt_w_sqrt2_jet_order_validation.py`](../../computations/rt_w_sqrt2_jet_order_validation.py) — jet-order check (this session)
- [`content/quantum-observable-universe/lean/QOU/Kashaev.lean`](../../content/quantum-observable-universe/lean/QOU/Kashaev.lean) — existing VolumeConjecture class
- [`content/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/CategoricalHiggsIdempotent.lean`](../../content/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/CategoricalHiggsIdempotent.lean) — existing Higgs-VEV class (placeholder)
- [`docs/audits/2026-05-24-sm-particle-categorical-map-rt-route.md`](2026-05-24-sm-particle-categorical-map-rt-route.md) — RT-chain framing (still valid; PR #1116)
- [`docs/audits/2026-05-24-rt-route-research-frontiers-w-correction-habiro-heegaard.md`](2026-05-24-rt-route-research-frontiers-w-correction-habiro-heegaard.md) — three frontiers audit (this PR's predecessor)
