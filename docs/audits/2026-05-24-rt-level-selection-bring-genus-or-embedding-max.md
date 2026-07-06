# RT-level selection for the torus-knot chain: Bring genus, embedding maximum, or substrate map?

**Date:** 2026-05-24
**Trigger:** Action item #4 from
[`2026-05-24-sm-particle-categorical-map-rt-route.md`](2026-05-24-sm-particle-categorical-map-rt-route.md)
§9. The RT chain for torus-knot masses (Higgs/W/Z/strong-force) requires
selecting a specific Reshetikhin-Turaev TQFT level $k$. This audit lays
out the three structural candidates and what would settle the question.

## §1. The RT level — what is it?

The Reshetikhin-Turaev (RT) TQFT for $\mathrm{SU}(2)$ at **level $k$**
uses the modular tensor category $\mathrm{Rep}_k(\mathrm{SU}(2))$ with
deformation parameter
$$q = \exp(\pi i / (k+2))$$
— a specific **root of unity**, NOT the framework's real substrate
$q_0 \approx 1.1097$.

At level $k$:
- Number of irreps: $k + 1$ (labelled by spin $j = 0, 1/2, 1, \ldots, k/2$)
- Modular $S$-matrix: $(k+1) \times (k+1)$
- Colored Jones $J_N$: well-defined for $N = 1, 2, \ldots, k+1$
- Beyond $N = k+1$: $J_N$ vanishes (level cuts off the color)

## §2. Three candidate level selections

### Candidate (a) $k = 4$ (Bring's surface genus)

**Argument**: the framework's archimedean substrate is Bring's quintic
surface, genus $g = 4$ ([`prop:brings-surface`](../../content/quantum-observable-universe/lean/QOU/BringsSurface.lean)).
The RT TQFT at level $k = g$ has the dimension matching the surface's
genus, giving a "minimal level that the surface can support."

**Pros**:
- Direct geometric connection (genus = level)
- Minimal level, simplest MTC

**Cons**:
- At $k = 4$: only 5 irreps ($j = 0, \tfrac{1}{2}, 1, \tfrac{3}{2}, 2$); color cutoff at $N = 5$
- The Higgs T(2, 8) requires $N \leq 5$, but Q2 (PR #1116) found the suggestive signal at $N = 8$ which would be cut off at this level

### Candidate (b) $k = 9$ (maximum-embedded-twist count)

**Argument**: the SM-relevant torus knots embed in Bring up to $T(2, 9)$
([`cohomological-embedding.md`](../../content/quantum-observable-universe/archimedean-universe/cohomological-embedding.md)
§(iv)). Setting $k = 9$ ensures the framework can colored-Jones-evaluate
every embedded torus knot up to color $N = 10$.

**Pros**:
- Accommodates the full SM torus inventory (W, Z, H, T(2,9))
- $N = 8$ for Higgs T(2, 8) is comfortably below cutoff
- Matches the "maximum twist count" structural feature

**Cons**:
- Not directly tied to Bring's genus
- $k = 9$ is large enough that the RT MTC has 10 irreps — possibly more structure than needed

### Candidate (c) Substrate-derived level $k(q_0)$

**Argument**: the framework's substrate $q_0 \approx 1.1097$ is real,
not a root of unity. There might be a categorical map
$$q_0 \mapsto k(q_0) \in \mathbb{N}$$
sending the real substrate to a specific RT level. The natural map:
$$k(q_0) := \text{nearest integer to } \left\lfloor \frac{2\pi}{\arg(q_0 - 1)} \right\rfloor$$
or similar — but $q_0$ being purely real makes any "argument" trivial.

**Pros**:
- Could in principle unify the hyperbolic and torus chains
- Substrate-natural, no extra input

**Cons**:
- No obvious natural map from real $q_0$ to an integer level
- May not exist as a categorical statement

## §3. What would settle the question

A clean experimental test:

**Cross-particle ratio test at multiple $k$**: compute
$|J_N(T(2, 4))| : |J_N(T(2, 6))| : |J_N(T(2, 8))|$ at $q = e^{\pi i/(k+2)}$
for $k \in \{4, 9\}$ and various $N$. Compare to the SM ratios
$m_W : m_Z : m_H = 0.882 : 1 : 0.729$. The $k$ that matches best is
the substrate-natural level.

The Q2 + the cross-particle ratio probe ([`rt_route_cross_particle_ratio_quantum_dim.py`](../../computations/rt_route_cross_particle_ratio_quantum_dim.py))
in this PR-batch used real $q_0$, NOT root-of-unity $q$. Re-running
those probes at $q = \exp(\pi i / 6)$ ($k=4$) and $q = \exp(\pi i / 11)$
($k=9$) is the missing experimental piece.

## §4. The structural-foundational question

Beyond which level $k$ is "correct", there's a foundational question
the framework hasn't yet addressed:

**Why does the framework's hyperbolic chain use REAL $q_0 \approx 1.1097$
(specifically chosen for the muon match) while the torus chain needs
ROOT-OF-UNITY $q = \exp(\pi i / (k+2))$ (chosen by RT level)?**

One possibility: $q_0$ IS a real specialization of a root-of-unity in a
limit. The Habiro ring (per
[`docs/audits/2026-05-24-pentagon-identity-broad-context.md`](2026-05-24-pentagon-identity-broad-context.md)
§3) constructs arithmetic structures that glue real and root-of-unity
data; the framework's $q_0$ might be an element of (or limit of) the
Habiro ring of a number field, with both real and root-of-unity
specializations.

This would unify the chain split (§1 of the SM-categorical-map audit):
the **same** substrate $q_0$ gives:
- Real specialization → hyperbolic VolDensity chain (Vol-anchored)
- Root-of-unity specialization → RT chain (level-anchored)

The two-chain framework would then be one chain with two views.

## §5. Recommendation

**Most actionable next step**: re-run the cross-particle ratio probe
([`rt_route_cross_particle_ratio_quantum_dim.py`](../../computations/rt_route_cross_particle_ratio_quantum_dim.py))
at $q = \exp(\pi i/(k+2))$ for $k \in \{4, 9, 12, 16\}$. ~50 lines added
to the existing script; immediate empirical signal on level selection.

**Heavier follow-up**: investigate the Habiro-ring connection between
real $q_0$ and root-of-unity RT levels. This is a research-grade
question (1+ weeks), but if resolved would unify the framework's
two-chain structure into one.

## §6. Cross-references

- [`docs/audits/2026-05-24-sm-particle-categorical-map-rt-route.md`](2026-05-24-sm-particle-categorical-map-rt-route.md) — §9 action item #4 (this audit)
- [`docs/audits/2026-05-24-pentagon-identity-broad-context.md`](2026-05-24-pentagon-identity-broad-context.md) — §3.3 Habiro ring reference
- [`content/quantum-observable-universe/archimedean-universe/cohomological-embedding.md`](../../content/quantum-observable-universe/archimedean-universe/cohomological-embedding.md) — §(iv) genus 4 FORCED by torus embedding
- [`content/quantum-observable-universe/lean/QOU/BringsSurface.lean`](../../content/quantum-observable-universe/lean/QOU/BringsSurface.lean) — `genus = 4` definition
- [`computations/rt_route_cross_particle_ratio_quantum_dim.py`](../../computations/rt_route_cross_particle_ratio_quantum_dim.py) — sibling probe (this PR)
- [`computations/probes/pentagon_rt_torus_knot_higgs_probe.py`](../../computations/probes/pentagon_rt_torus_knot_higgs_probe.py) — Q2 (PR #1116) — used real $q_0$, not root-of-unity
