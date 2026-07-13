# c_3^even is substrate-solved; c_3^odd's S is pruned to the quantum complex volume 𝔙_q

**Date:** 2026-07-07 · **Axis:** z→c_k f-map keystone (c_3 parity channels)
· **Tier:** proved-lean (prune) + structural-exact (even channel) + exploratory (𝔙 identification)
· **Discipline:** no fit, no c_k value, no wiring, no tier change. "Sorry-free ≠ derived";
scope-(a)/(b) classified throughout.

Answers three questions raised this session: **(1) c_3^even?** **(2) is c_3^even
interpretable in 𝔇_β?** **(3) can the 𝔙 Geom(K) / q-hyperbolic framing close it?**

## 1. c_3^even is already solved — exactly, substrate-derived, no calibration leak

The bar-even channel of `log R` is a strongly over-determined **exact ℚ(√3)
ũ-ladder** (ũ = q·u the genuinely bar-even variable; bean `ai81`/`08ds`,
[9fnm audit](2026-07-03-9fnm-c3even-exact-rational-measurement.md)):
`e₁ = 3√3/4, e₂ ≈ −15.035, …, e₈ ≈ −356734`, persisting through s¹⁷ with
**over-determination margin 9, every residual order exactly zero**. The
mixed-projection rung `c₃^even = 841/144 + 604739√3/12960 ≈ +86.66` is a
projection artifact; the honest rungs are the `e_k`.

**So c_3^even carries NO archimedean leak.** The `√3` is the substrate's own
hexagonal / ζ₃ (three-strand `[3]_q`, Eisenstein) constant — categorical, not an
experimental input. c_3^even is **substrate-derived**, full stop.

### Is c_3^even interpretable in 𝔇_β? — No; by parity it's 𝔇_π, but really it's neither

The bar involution splits everything into sinh/cosh partners, and the canonical
cheat-sheet pins the CAL sides:

| parity | trig | observable | datum |
|---|---|---|---|
| **bar-ODD** | sinh | Q_β | **𝔇_β (CAL-2)** |
| **bar-EVEN** | cosh | m_π | **𝔇_π (CAL-3)** |

`c_3^even` is bar-EVEN, so its parity-matched datum is **𝔇_π (CAL-3)**, not the
bar-odd `𝔇_β`. And since it is in fact substrate-exact (ℚ(√3)), it needs no CAL
datum at all — it is categorical. `𝔇_β` interprets the **odd** channel (below).

## 2. c_3^odd's scalar S — parity re-label + the rigidity prune

The odd channel factors `c_3^odd = κ_(2,1)(q)·S` with the derived pure-q bar-odd
carrier `κ_(2,1) = (q−1)³(q+1)/q²` and the single archimedean scalar
**`S = Q_β/E₀`** — "the single archimedean leak" (heat-fmap §2, PR #1752).
`S_proton ≈ 908.4`, `S_muon ≈ 886.8` (`S_p/S_μ ≈ 1.024`).

**Parity re-label (refines PR #3466).** S inherits bar-odd from `Q_β = ℏ/𝔇_β`;
`E₀` (block energy) is the bar-even CAL-3 unit. So S's calibration *content* is
**𝔇_β (CAL-2)**, not 𝔇_π — the #3466 docstring's "S = g(𝔇_π)" was parity-imprecise.
Lean: [`SRigidityPrune.S_bar_odd_of_ratio`](../../content/quantum-observable-universe/lean/QOU/QBeta/SRigidityPrune.lean).

**The rigidity prune (scope-(b), proved invariant).** S swings 2.44% across the
proton/muon anchors while q₀ moves only ~1.15×10⁻⁸ (relative) — a **~2.1×10⁶
logarithmic sensitivity** (the registry `dc_3/dq ≈ 4.6×10⁶` obstruction; probe
[`qbeta_s_complex_volume_rigidity_probe.py`](scripts/qbeta_s_complex_volume_rigidity_probe.py),
5/5). Any pure function of an **anchor-invariant** datum is constant across
anchors, so it cannot realize S:

> [`no_anchor_invariant_realizes_swing`](../../content/quantum-observable-universe/lean/QOU/QBeta/SRigidityPrune.lean)
> (sorry-free): `datum a = datum a'` ∧ `S a ≠ S a'` ⇒ `¬ ∀ x, S x = g (datum x)`.

Every fixed CAL constant (𝔇_β, 𝔇_π, m_π) and every classical topological invariant
is anchor-invariant, so **S is not a pure function of any of them.**

## 3. 𝔙 Geom(K) + q-hyperbolic — the classical reading is pruned, the quantum one survives

The **classical complex volume** `𝔙(K) = Vol(K) + i·CS(K)` is a topological
invariant of a *fixed* knot ⇒ anchor-invariant. By the prune above, **S ≠ f(𝔙(K))
for any f** (scope-(b)). The numerical search confirms no clean identification of
`S_muon` to any framework volume (Vol(4₁), Vol(Borromean), Vol(5₂), Vol(6₁)) under
linear / `2π` / log / volume-conjecture-shaped f.

**The survivor is the QUANTUM complex volume `𝔙_q(K)`** — the Faddeev quantum
dilogarithm `Φ_b(z)` with `b ↔ q₀`. `𝔙_q` depends on q₀ (its ℏ→0 limit is the
classical 𝔙), so it is anchor-dependent by construction and survives the prune.
This is exactly the fibre-object-evaluated-at-q₀ reading (Im(q) fibre-vs-observable)
and the heat-fmap §2-quater localization: *prove the fibre kernel R from its
root-of-unity residues + bar-parity + pole; leave S to CAL-3.*

**The c_k ladder is structurally the Ohtsuki asymptotic series around 𝔙:**
`J_N(K) ~ N^{3/2} e^{N𝔙/2πi}(1 + Σ_k κ_k (2πi/N)^k)`, the `κ_k` a q-correction
ladder in the shape of our `c_k`. Literature (q-hyperbolic functions):

| source | object | relevance |
|---|---|---|
| Faddeev 1995; Faddeev–Kashaev | quantum dilog Φ_b, modular double | THE q-hyperbolic function; `FaddeevModularDouble.lean` in-repo |
| Kashaev 1997; Murakami–Murakami | volume conjecture (+ complex) | J_N → 𝔙 = Vol+iCS |
| Ohtsuki | asymptotic series of J_N | κ_k ladder = c_k analog |
| Zagier 2010; Garoufalidis–Zagier | quantum modularity, state integrals | S-transform → bar-involution |
| Andersen–Kashaev | Teichmüller TQFT | partition fn = Φ_b state integral; limit = 𝔙 |
| Garoufalidis–Gu–Mariño | resurgence / Stokes constants of J_N | quantum-modular corrections as resurgent data |
| Garoufalidis 2004 (`garoufalidis2004`, cited) | AJ / Â-polynomial | q-holonomic parent of the c_k recursion |

### 3a. Ohtsuki pursued — the 4₁ computation (concrete)

Probe [`qbeta_ohtsuki_figure_eight_ladder.py`](scripts/qbeta_ohtsuki_figure_eight_ladder.py)
(4/4, 60 dps) computes the figure-eight Kashaev invariant
`J_N(4₁) = Σ_{k<N} ∏_{j≤k}(2 sin(πj/N))²` and fits its asymptotics:

- **Volume conjecture recovered to rel err `2.4×10⁻¹²`**: `2π·(slope) = 2.0298832128`
  vs `Vol(4₁) = 2Λ(π/3) = 2.0298832128`. The quantum object `J_N` (the 𝔙_q side)
  has exponential rate = the **classical** `𝔙(4₁)` — the 𝔙_q↔𝔙 bridge, concrete.
- **Leading constant `b = −¼ log 3`** exactly (measured `−0.274653`), i.e. the
  `3^(−1/4)` prefactor — the **same √3/hexagonal ζ₃ constant** that appears in the
  c_3^even ℚ(√3) rungs. Structural consistency (not a fit): the even channel and
  the figure-eight quantum volume share the ζ₃ hexagonal datum.
- **κ-ladder** (Ohtsuki corrections): `κ₁ ≈ 0.554, κ₂ ≈ 0.730, κ₃ ≈ 2.814`.

**These κ_k are fixed-knot, anchor-invariant.** They pin the c_k ladder
*structure* (the derived even channel); they do **not** — and must not —
reproduce S's 2×10⁶ swing, which is a circular-extraction artifact, not fibre
physics. **Bridging the Ohtsuki κ_k (in the `2π/N` basis) to our `u = b·ℏ_q²`
ladder normalization is exactly the open f-map** — the next concrete step.

### 3b. The κ→u re-basing test — the f-map is resurgence, not a coefficient map

Probe [`qbeta_fmap_ohtsuki_rebasing_test.py`](scripts/qbeta_fmap_ohtsuki_rebasing_test.py)
(5/5, 80 dps) tests whether the f-map is "read the c_k off the Ohtsuki ladder":

- **One-scale re-basing fails (parameter-free).** Fixing the single scale
  `ũ = λ·(2π/N)` from rung 1 (`λ = e₁/κ₁ = 2.344`) and *predicting* the even
  rungs: `e₂^pred = +4.02` vs actual `−15.04` (wrong **sign and magnitude**);
  `e₃, e₄` likewise. No single scale maps the 4₁ Ohtsuki ladder to the QOU even
  channel. (A *free per-order* change of variables could fit anything — the
  Weber-ODE overfitting trap; the one-scale test is the honest version.)
- **Structural reason (scope-(b)).** The colored Jones has an **essential
  singularity** at q=1 (Kashaev `~ e^{N·Vol/2π}`); its Ohtsuki series is
  **divergent asymptotic** — measured growth `|κ_{k+1}/κ_k| = 1.32 → 3.62 → 5.50`
  (increasing). The Q_β ratio `∏(1+c_k u^k)` is **regular** at q=1 (→1). A regular
  function and an essential-singularity function are **not** related by an
  analytic change of variables — so the f-map **cannot** be a coefficient
  re-basing. It is the **resurgence connection**: the c_k are the perturbative
  series around the *trivial* flat connection; the Ohtsuki κ_k are around the
  *geometric* (volume) connection; the bridge is the Stokes data
  (Garoufalidis–Gu–Mariño), not a variable substitution.
- **Knot-identification caveat.** 4₁ is the *lepton* knot (Vol enters m_μ). The
  even channel's knot may differ (meson/pion sector); identifying the correct
  knot is prerequisite to any sharper f-map test. The one-scale failure is
  therefore scope-(a) w.r.t. the knot choice and scope-(b) w.r.t. the
  analytic-type obstruction (which holds for *every* hyperbolic knot).

**Nucleon-side volumes (Task 2).** Classical volumes: 4₁ = 2.02988 (lepton),
5₂ = 2.82812, 6₁ = 3.16396, **Borromean 6³₂ = 7.32772 = 2·Vol(ideal octahedron)**
exactly (nucleon). The Borromean *quantum* volume needs the 3-component link
colored Jones — the next concrete compute (the single-sum Kashaev form is
knot-only).

## 4. Does this get us closer? — honest assessment

- **Closer to a sharp statement + runnable experiment: yes.** The keystone is now
  precise: *S ≈ leading Ohtsuki term of `𝔙_q(K)` for the CAL-2 β-decay knot K,
  evaluated at the substrate q₀.* Concrete next experiment: compute `𝔙_q(K)` via
  `Φ_b` at q₀ and test whether it reproduces `S_muon ≈ 886.8` and its ~2e6
  q₀-sensitivity.
- **Closer to a *derivation*: no — and the prune says why.** `S = Q_β/E₀` carries
  `Q_β = ℏ/𝔇_β = CAL-2`, a calibration *input*. Deriving S from the substrate ⟺
  substrate-deriving CAL-2 (q₀) = **Subgoal-2, owner-declined 2026-05-08**. So
  `𝔙_q` can *identify* S with a known invariant and could *predict* it if computed
  independently to precision — but it does not *derive* it around the calibration.
  Heat-fmap caveat stands: finitely many root-of-unity residues **constrain** R,
  they do not **determine** it.

## Bottom line

The even channel of c_3 is **done** (substrate-exact ℚ(√3), no leak). The odd
channel's scalar S is **provably not** a pure function of any calibration datum or
classical volume (Lean-proved invariant), which **forces** the quantum complex
volume `𝔙_q(K)` (Faddeev Φ_b) — the Ohtsuki-series route,
`conj:binding-qbeta-complex-volume`. That is a sharper keystone and a concrete
experiment, not a closure: S is anchored on CAL-2, so its derivation is the
declined Subgoal-2.

## Cross-references

- Lean: [`SRigidityPrune.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/SRigidityPrune.lean)
- Probe: [`qbeta_s_complex_volume_rigidity_probe.py`](scripts/qbeta_s_complex_volume_rigidity_probe.py)
- c_3^even measurement: [9fnm](2026-07-03-9fnm-c3even-exact-rational-measurement.md)
- S origin: [heat-fmap §2](2026-06-13-qbeta-heat-fmap-symbolic-and-literature.md)
- Cross-anchor verdict: [c_3 not exact](2026-07-06-c3-not-exact-cross-anchor-verdict.md)
- CAL-3 anchor structure (prior): [2026-07-07 CAL-3 anchor](2026-07-07-cal3-anchor-structure-and-table-impact.md)
