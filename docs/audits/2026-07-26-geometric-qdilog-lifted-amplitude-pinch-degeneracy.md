# The full lifted dilogarithm gives `r ≈ −2.1%` and the four-shape octahedron degenerates at the pinch — the sharpened `g₂` frontier

**Date:** 2026-07-26 · **Branch:** `claude/geometric-qdilog-amplitude-r-2026-07-26` ·
**Axis:** Δ_λ binding — μ₀ −9% closure, the exact residual `r = g₂ − 1` · **Owner steer:** *"work on
the geometric quantum-dilog regular part on the 4-shape octahedron"* · **Tier:** one principled
full-amplitude evaluation (exact closed form) + Lean-proved structural degeneracy + sharpened wall
(**scope-(a); no fit; no scan**; nothing wired).

## 0. What was asked, and the epistemic ground first established

The frontier note (#4347) reduced `r = +0.87%` to "the geometric quantum-dilog regular part on the
4-shape octahedron" and evaluated only the **bare** `Li₂` (`Li₂(−h²)/(−h²) = 0.9893`, nonlinearity
`−1.07%`, wrong sign), then stopped. This session did the next principled step **and** first nailed
down the epistemic status the frontier note left implicit:

- **`g₂ = 1.00865` is a *measured* ratio** — `(bar-even deuteron/E_unit binding gap)/h²` — labelled
  *"NEAR-MATCH — underived"* throughout the corpus
  ([`2026-07-24-eunit-magnus-order2.md`](2026-07-24-eunit-magnus-order2.md) L128/L209). It is **not**
  back-solved to close the AME gap and **not** a free parameter. So deriving `r` is a legitimate
  prediction target, and matching a single ~0.9% number is subject to the §2e entropy caution.

## 1. The one principled evaluation — the FULL MSR lifted dilogarithm

MSR (`2509.02354`) eq (A.15) gives the **correct** per-tetrahedron amplitude: the *lifted*
dilogarithm, i.e. the complex Chern–Simons invariant of the **flattened** ideal tetrahedron,

$$L(\zeta^0,\zeta^1) \;=\; \frac{\mathrm{Li}_2(e^{2\pi i\zeta^0})}{2\pi i} \;+\; \pi i\,\zeta^0\zeta^1 \;+\; \zeta^0\log\!\big(1-e^{2\pi i\zeta^0}\big),$$

flattening fixed by (A.8) `e^{2πiζ⁰}=z`, `e^{−2πiζ¹}=1−z` — **not** the bare `Li₂`. The corpus already
established (`g2_leading_exact…`, #4339) that `g₂` is carried by the **real (bar-even) face**, so the
principled scalar is `Re L` — no menu choice.

On the pinned trefoil eigenspace shape `z = −h²` (#4345) the flattening is

$$\zeta^0 = \tfrac12 - \frac{i\ln h}{\pi}, \qquad \zeta^1 = \frac{i\ln(1+h^2)}{2\pi},$$

and `Re ζ⁰ = ½` **exactly** — which reconciles the corpus's two long-standing trefoil frames
(`z = ½`, the Rogers-inflection meridian frame #4309, and `z = −h²`, the boundary-rep cross-ratio
#4345: the latter is `e^{2πiζ⁰}` of the former's real flattening). The real part collapses to an
**exact closed form** (verified to 30 dps and symbolically):

$$\boxed{\;\mathrm{Re}\,L(\zeta^0,\zeta^1) = \tfrac14\ln(1+h^2) = \tfrac14\Big(h^2 - \tfrac{h^4}{2} + \tfrac{h^6}{3} - \cdots\Big)\;}$$

Normalising to the derived leading coefficient `1` (`g₂_leading = 1`):

$$g_2^{\text{cand}} = \frac{\mathrm{Re}\,L}{h^2/4} = \frac{\ln(1+h^2)}{h^2} = 1 - \tfrac{h^2}{2} + \tfrac{h^4}{3} - \cdots \approx 0.9788 \quad\Longrightarrow\quad r \approx -2.12\%.$$

## 2. Refutation (scope-(a)) — and it moved the wrong way

Target `r = +0.87%`. The full lifted dilog gives `r ≈ −2.12%`: **wrong sign** and **~2.4× the
magnitude**. Fixing the prior `Li₂`-only omission moved the answer **further** from target
(`−1.07% → −2.12%`), not closer. So the **eigenspace-shape lifted-dilog route, alone, does not
reproduce `r`.** This is a **scope-(a)** negative — it constrains magnitudes/combinations, not
ingredients; no proved invariant excludes the lifted dilog from a closure, so it is **not** scope-(b).
Per §2e, dilog forms/shapes were **not** scanned to hunt for `+0.87%`.

## 3. Structural finding (Lean-proved) — the four-shape octahedron degenerates at the pinch

The deuteron `σ₁³` is the **trefoil** `T(2,3)`, a **torus knot**, so its crossings are **pinched**
(§5.2 Def 5.3: the incoming over/under eigenspaces coincide). At the *standard* pinched log-coloring
(§5.2 eq 5.7 `β₁=β, β₂=β+μ₁, β₁'=β+μ₂, β₂'=β`) **all four** MSR shape-logs `ζ⁰_{r,t,l,b}` (eq
4.11–4.14) vanish **identically**, hence the octahedral

$$e_2 = \textstyle\sum_{i<j}\zeta^0_i\,\zeta^0_j = 0.$$

Machine-checked sorry-free:
[`PinchedOctahedronDegenerate.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/PinchedOctahedronDegenerate.lean)
(`zeta0_{r,t,l,b}_pinch`, `e1_pinch`, `e2_pinch`, `octahedral_constraint`), pure `CommRing` (§7c).

**Consequence.** The "four-shape octahedron" has **no four-distinct-shape content at the pinched
trefoil** — the four ideal tetrahedra collapse to the single degenerate shape `z=1`. So `g₂` **cannot**
be the naive octahedral `e₂` of the MSR shape-logs (that is `0` in the limit that actually applies),
and the `−h²` from the boundary rep is the **eigenspace cross-ratio**, a *different* invariant from
the four `ζ⁰_j`. This corrects the framing carried since #4315.

## 4. The sharpened wall (honest)

The genuine MSR regular part (Garoufalidis–Kashaev eq A.17) carries the torsion factor
`D(ζ) = ∏_{k=1}^{N−1}(1−ω^{ζ+k})^{k/N}`, which lives at `q = ω` a **root of unity** (`N→∞`) — the
**fibre** regime — whereas `g₂` is evaluated at the **real** substrate `q₀` (the **archimedean**
regime). Closing `r` rigorously therefore needs the **fibre→archimedean (τ-functor) transfer** of the
pinched regular part, **not** a further evaluation at real `q₀`. This is the same fibre-vs-archimedean
distinction AGENTS.md flags for the `c_k` saga.

| statement | status |
|---|---|
| `Re L(ζ⁰,ζ¹) = ¼ ln(1+h²)` on `z=−h²` (full lifted dilog); `Re ζ⁰ = ½` reconciles the `z=½`/`−h²` frames | **exact, verified** (this note) |
| normalised `g₂ = ln(1+h²)/h² ≈ 0.9788`, `r ≈ −2.1%` (eigenspace-shape lifted dilog) | **refuted, scope-(a)** — wrong sign vs measured `+0.87%` |
| four MSR shape-logs `= 0` at the standard pinch ⇒ octahedral `e₂ = 0` | **Lean-proved sorry-free** (`e2_pinch`) |
| the exact `r = +0.87%` | **OPEN** — needs the fibre→archimedean (τ) transfer of the pinched regular part (`D(ζ)` torsion) |

**Net.** This session converts the frontier's *"compute the geometric qdilog on the 4-shape
octahedron"* into a sharper, truer picture: the 4-shape object **degenerates** at the pinch (proved),
one more principled evaluation (the correct full amplitude) **refutes** the eigenspace route (and
moves away from target), and the real remaining object is the pinched regular part in the
**root-of-unity regime**, whose real-`q₀` value requires the `τ` transfer. No fit, no scan; nothing
wired.

Refs: probe
[`geometric_qdilog_lifted_amplitude_probe.py`](../../computations/deltalambda/geometric_qdilog_lifted_amplitude_probe.py);
Lean [`PinchedOctahedronDegenerate.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/PinchedOctahedronDegenerate.lean);
#4347 (frontier, bare `Li₂`); #4345 (shape `−h²` from rep); #4339 (`g₂_leading=1`);
`library/arxiv-2509.02354v2/2509.02354v2.pdf` eq (A.15), (A.17), §5.2.
