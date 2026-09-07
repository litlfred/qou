# The substrate branch $s = \pm\sqrt{q}$, the missing $\varphi^2$ degeneration, and the $q = 1$ interface

**Date:** 2026-09-07
**Branch:** `claude/dark-matter-antimatter-feasibility-9rhx37`
**Beans:** `qou-7r6d` (session), `qou-ndt5`, `qou-v1jg`, `qou-kyi3`, `qou-hjs8`
**Status:** measurement + analysis. No content block is edited by this document; the
content changes it implies are listed in §7 as *proposals*, for the author to accept
or decline.

## 0. Why this exists

The session began from an owner question — could missing dark matter be explained by
$\gamma\gamma$ production yielding antiparticles, with some visible galaxies made
entirely of antimatter and only their photonic emission reaching us? The first pass
returned a negative on all three legs (§6 below, retained for the record). The owner
then made two corrections that changed the problem:

1. **$m(e^+)$ need not equal $m(e^-)$** — the CPT equality is not a QOU theorem.
2. **$q$ varies.** An antimatter region need not sit at $q_0$, nor even inside the
   window our physics occupies.

The second is the load-bearing one, and following it produced the algebra recorded
here. Everything in §§1–4 is exact symbolic computation with no empirical input.

## 1. The second Weierstrass coefficient depends on $s$, not on $q$

[`prop:descartes-elliptic-curve`](../../content/quantum-observable-universe/brings-surface/descartes-elliptic-curve.md)
gives the colour elliptic fibre with $s = \sqrt q$ and states that the Weierstrass
coefficients are *"expressible directly in $q$"*, then writes

$$
  r(q) =
  \frac{20(q-1)^3}{27 q^{3/2}} +
    \frac{5(q-1)^2}{9q} +
    \frac{5(\sqrt q - 1/\sqrt q)}{9} +
    \frac{20}{27}.
$$

**That expression carries $q^{3/2}$ and $\sqrt q$.** It is therefore not a function of
$q$; it is a function of $s$, and a choice of $s = +\sqrt q$ or $s = -\sqrt q$ changes
its value. The quoted sentence is wrong as stated.

**Verified:** the factored form quoted in
[`rem:golden-ratio-degeneration`](../../content/quantum-observable-universe/observations/golden-ratio-degeneration.md),

$$
  s^3 r(q) = \tfrac{5}{27}\,(s^2+s-1)(4s^4-s^3-4s^2+s+4),
$$

expands to $\tfrac{20}{27}s^6 + \tfrac59 s^5 - \tfrac53 s^4 - \tfrac{10}{27}s^3 +
  \tfrac53 s^2 + \tfrac59 s - \tfrac{20}{27}$, **identical** to $s^3$ times the
$r(q)$ above (symbolic difference exactly $0$). The two blocks agree; only the
"directly in $q$" claim is at fault.

A consistency check that makes the point independently: if $r$ were a function of
$q = s^2$ it would be even in $s$, so $s^3 r$ would be **odd**. It is not —

$$
  s^3r(s) + s^3r(-s) = \tfrac{40}{27}s^6 - \tfrac{10}{3}s^4 + \tfrac{10}{3}s^2 - \tfrac{40}{27} \neq 0 .
$$

## 2. The degeneration locus is bar-symmetric, and the corpus lists half of it

$s^2 + s - 1$ vanishes at $s \in \{1/\varphi,\; -\varphi\}$. Squaring,

$$
  q = s^2 \in \Bigl\{\tfrac{3-\sqrt5}{2},\; \tfrac{3+\sqrt5}{2}\Bigr\}
       = \{\varphi^{-2},\; \varphi^{2}\}
       = \{0.381966011250,\; 2.618033988750\},
$$

and these are **exactly bar-conjugate**: $\varphi^{-2}\cdot\varphi^{2} = 1$.

The quartic $4s^4 - s^3 - 4s^2 + s + 4$ has **no real roots** — all four are complex
($-0.8088 \pm 0.4605i$, $0.9338 \pm 0.5317i$) — so it contributes no further real
degeneration. The two values above are the whole real locus.

[`rem:golden-ratio-degeneration`](../../content/quantum-observable-universe/observations/golden-ratio-degeneration.md)
lists only $\varphi^{-2}$ and gives the physical regime as $q > 1$, unbounded above.
Under the reading established in §3 that is incomplete: there is a second degeneration
at $q = \varphi^2 \approx 2.618$.

## 3. Which lift of the bar involution? $s \mapsto -1/s$, uniquely

The bar involution is $q \mapsto q^{-1}$. It has two lifts to $s$, and they are not
interchangeable — only one preserves the degeneration locus:

| lift | $s^2\cdot(s^2{+}s{-}1)|_{\text{sub}}$ | $s^4\cdot\text{quartic}|_{\text{sub}}$ | locus preserved? |
|---|---|---|---|
| $s \mapsto 1/s$ | $-s^2+s+1 = -(s^2-s-1)$ | $4s^4+s^3-4s^2-s+4$ | **no** — different polynomials |
| $s \mapsto -1/s$ | $-s^2-s+1 = -(s^2+s-1)$ | $4s^4-s^3-4s^2+s+4$ | **yes** — anti-invariant / invariant |

So $s \mapsto -1/s$ is the unique lift under which $\mathcal{E}_q$'s degeneration
structure is bar-symmetric. Under it the root set $\{1/\varphi, -\varphi\}$ is
preserved, which is precisely why $\varphi^2$ joins $\varphi^{-2}$ in §2.

**Fixed points.** $s = -1/s \Rightarrow s^2 = -1 \Rightarrow q = -1$. On the $q$-line
$q \mapsto q^{-1}$ fixes $q = \pm 1$. So $q = 1$ is fixed *as a point of the $q$-line*
while its two square roots $s = \pm 1$ are **exchanged** by the lift.

**That is the structural content of the owner's $q=1$ proposal (§4): crossing $q = 1$
is a branch swap $s \leftrightarrow -s$, not a collision.**

## 4. The $q = 1$ interface

Matter sits at $q_0 = 1.1099785827513808$ (Physical regime, $q>1$). A bar-conjugate
region sits at $q_0^{-1} = 0.900918283956$. Any continuous path between them **must**
cross $q = 1$. This is forced by continuity, not assumed.

Three exact facts about that crossing:

**(a) The branch-independent part of $r$ vanishes there, and only there.** Splitting
$s^3r$ into its even and odd parts in $s$:

$$
  \text{even}(s) = \tfrac{5}{27}\,(q-1)(4q^2-5q+4), \qquad
  \text{odd}(s) = s^3 \cdot \tfrac{5}{27}\Bigl(3q - 2 + \tfrac3q\Bigr).
$$

The even part is a genuine function of $q$ and factors with a root at $q = 1$;
$4q^2-5q+4$ has discriminant $-39 < 0$, so **$q = 1$ is its only real zero**. The odd
part's cofactor $\tfrac{5}{27q}(3q^2-2q+3)$ is **bar-even** ($r_{\text{odd}}(1/q) -
r_{\text{odd}}(q) = 0$, verified) and has no real zeros.

**(b) The pair-separation residue vanishes there.**
[`prop:crossing-energy-pair-cancellation`](../../content/quantum-observable-universe/observations/crossing-energy-pair-cancellation.md)
gives $\mathfrak{E}(\mathfrak{H}) + \mathfrak{E}(\mathfrak{H}^\sigma) = 2(p+m)\sinh\lambda$
with $\lambda = \ln q$, and reads the residue as *"the Coulomb energy that separates a
created particle–antiparticle pair."* At $q=1$, $\lambda = 0$ and the residue is
**exactly zero**. It is also **bar-odd**: positive for $q>1$, negative for $q<1$.

**(c) The deformation switches off.** $\hbar_q = (q-1)/q \to 0$, $h = q - q^{-1} \to 0$,
and $H_n(1) = \mathbb{C}[S_n]$ — the group algebra. Crossings become transpositions;
chirality is erased.

### The tension this exposes

[`rem:cosmological-chirality-flip`](../../content/quantum-observable-universe/observations/cosmological-chirality-flip.md)
states that at $q \to 1$ the electron and muon *"survive as indistinguishable
topological excitations with **vanishing masses**."* But the CAL-2 relation
$m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$ is exact and $\hbar_q \to 0$, so the ratio
**diverges**:

| $q$ | $\hbar_q$ | $m_\mu/m_e$ |
|---|---|---|
| $1.1099785827513808$ | $0.099081716$ | $206.7683264$ |
| $1.01$ | $0.0099009901$ | $20706.83865$ |
| $1.001$ | $0.000999001$ | $2033945.009$ |
| $1.0001$ | $9.9990001\times10^{-5}$ | $203028921.0$ |

Two masses whose **ratio diverges** cannot be "indistinguishable". Either the prose is
wrong, or the mass formula does not survive to $q=1$ and the limit needs a separate
treatment. **This must be settled before any $q=1$ interface argument can be trusted**,
because whether the interface is soft or violent depends on which way masses go there.
Tracked as `qou-v1jg`.

### 4a. What is emitted at the interface — nothing, and for a structural reason

Asked directly: at $q=1$ would we see photonic emission, or does it move out of the
observable band? **Neither — at $q=1$ there is nothing left to emit.** From the Hecke
relation $\sigma_i^2 = (q-q^{-1})\sigma_i + 1$:

1. At $q=1$ it becomes $\sigma_i^2 = 1$, so $\sigma_i = \sigma_i^{-1}$. The generators
   are involutions, the braid group surjects onto $S_n$, and $H_n(1) = \mathbb{C}[S_n]$.
   **There is no knotting at $q = 1$.**
2. Every knot invariant trivialises — $V_K(1) = 1$ for every knot — so no distinct
   particle labels survive.
3. $\sigma_i = \sigma_i^{-1}$ means **bar acts trivially**: no chirality, hence no
   matter/antimatter distinction and nothing to annihilate with.

The interface is therefore a **de-particling layer**, not an annihilation zone. Matter
reaching it does not burn to photons; its knot structure dissolves. This is a
qualitatively different boundary from the one Cohen–De Rújula–Glashow compute, which is
why that bound does not transfer without a fresh calculation.

**Direction of the shift, and why it does not decide the question.** Under the formula
reading ($m \propto \hbar_q^{-2}$) transition energies blueshift without bound:

| $q$ | $E/E_0$ | 2 eV (visible) becomes |
|---|---|---|
| $q_0 = 1.10998$ | $1.0$ | 2.0 eV — visible |
| $1.05$ | $4.33$ | 8.66 eV — UV |
| $1.01$ | $100.1$ | 200 eV — soft X-ray |
| $1.001$ | $9837$ | 19.7 keV — hard X-ray |
| $1.0001$ | $981915$ | 1.96 MeV — gamma |

Under the prose reading ("vanishing masses") they redshift to zero instead. **Either way
the emission leaves the observable window**, so on this particular question the §4
contradiction fixes the *direction*, not the *answer*. (This corrects an earlier framing
in which §4 was said to gate everything downstream; it does not gate this.)

**A falsifiable signature.** `rem:cmb-photon-color-content` assigns T/E to jet degree 1
and **B to degree 2** — the Hopf-link dressing carrying linking number $\pm1$. With bar
trivial at $q=1$ the two signs are identified, so the parity-odd component has nothing
to carry: **a $q\to1$ interface emits no B-mode polarisation.** Relatedly, crossing
energy collapses to the writhe exactly ($3.32994 \to 3$ for the trefoil) — topological
rather than metric.

**Where §4 does bite: barrier or door.** Under the formula reading, mass diverges as
$q\to1$, so reaching the layer costs unbounded energy and the surface is
**self-shielding** — matter and antimatter domains never contact, there is no
annihilation, and the CDG98 bound is evaded by an infinite barrier rather than by a
small cross-section. That would be `rem:time-reversal-energy-barrier`'s
$\mathfrak{E}_{\text{flip}} = +\infty$ appearing *spatially* rather than in configuration
space. Under the prose reading there is no barrier and the interface is freely
permeable. **Same contradiction, opposite physics.**

**Not established.** That a $q$-gradient is stable, or that such interfaces exist. The
de-particling is exact only *at* $q=1$, a codimension-1 surface, so the physics lives in
the neighbourhood where $q \approx 1$ but $\neq 1$ and the blueshift is large but finite.
Energy conservation across the layer is unchecked. And this is a **boundary** mechanism,
not a **substance** one: interface area scales differently from volume, so the
dark-matter budget arithmetic differs entirely from §6 and has not been done.

## 5. Scope of the negatives

Per AGENTS.md §"Before declaring refuted":

- §1, §2, §3 are **positive** results (exact symbolic identities), not refutations.
- The $\varphi^2$ omission in §2 is a **scope-(b) structural claim**, justified by the
  proved invariant that $s^2+s-1$ has exactly the root set $\{1/\varphi,-\varphi\}$ —
  a finite algebraic fact, not a numerical probe.
- The §4 divergence is a **scope-(a)** finding: the mass formula and the prose
  disagree in the $q\to1$ limit *as currently written*. It does not exclude a $q=1$
  interface; it says the limit is unspecified.

## 6. Retained from the first pass: why the fixed-$q$ antimatter route fails

Kept so the route is not re-proposed. All figures are recalled literature — **the
library holds no source on antimatter cosmology or dark-matter phenomenology** (checked
across `INDEX.md`, `sections/`, `ocr/`, `uploads/` on 14 spellings), so none of these
can be checked in-corpus.

- **Budget.** $\Omega_c/\Omega_b = 5.364$ (Planck 2018). Making dark matter from
  antibaryons needs a $5.36{:}1$ antimatter *excess*; $\gamma\gamma$ production is
  C-symmetric and delivers $1{:}1$. A symmetric universe gives $2\Omega_b = 0.0986$
  against a required $0.3138$ — short by $3.18\times$.
- **Luminosity.** An antimatter galaxy radiates identically; dark matter is defined by
  not radiating.
- **Collisionality.** Bullet-Cluster lensing mass is offset from the gas; an antimatter
  plasma would sit with the gas.
- **Photon coupling.** Antibaryons couple to photons before recombination and cannot
  grow structure.
- **Domain bound.** Cohen–De Rújula–Glashow (ApJ **495**, 539, 1998): boundary
  annihilation over-produces the MeV background unless domains are $\gtrsim 1$ Gpc.
- **Direct measurement.** SN 1987A delivered **antineutrinos** via inverse beta decay
  in Kamiokande-II/IMB, so the LMC is matter by lepton-number sign, not by light.

**QOU offers no evasion at fixed $q$.** `rem:time-reversal-energy-barrier` gives
$\mathfrak{E}_{\text{flip}} = +\infty$, but that barrier is on *conversion*, not
annihilation; the block itself names pair creation at $2m_e$ as the open channel.

**The $q$-varying route is different and is not covered by any of the above**, because
every one of those bounds is computed at fixed $q$ with standard-model cross-sections.
What happens at a $q$-gradient is uncomputed. That is `qou-v1jg`.

## 7. Proposed content changes — NOT applied

Listed for the author to accept or decline. Nothing in `content/` is touched by this PR.

1. **`descartes-elliptic-curve.md`** — the sentence *"with Weierstrass coefficients
   expressible directly in $q$"* is false of the expression that follows (it carries
   $q^{3/2}$ and $\sqrt q$). Replace with a statement that $r$ is a function of
   $s=\sqrt q$, and fix the branch explicitly.
2. **`golden-ratio-degeneration.md`** — the regime table omits the degeneration at
   $q = \varphi^2 = (3+\sqrt5)/2$. If §3's lift is accepted, the physical window is the
   bar-symmetric interval $(\varphi^{-2},\varphi^{2}) = (0.381966, 2.618034)$ rather
   than $q > 1$ unbounded.
3. **A new remark on the bar lift** — $s \mapsto -1/s$ is the unique lift preserving
   the degeneration locus; $s\mapsto 1/s$ does not. Currently stated nowhere.
4. **`cosmological-chirality-flip.md`** — the "vanishing masses" clause contradicts the
   CAL-2 relation in the same limit (§4). Needs either a correction or an explicit
   statement that the mass formula does not extend to $q=1$.

Item 4 is the one with downstream reach: it is the $q\to1$ boundary of the whole
cosmological layer.

## 8. What was measured here, and what was not

**Measured this session** (exact symbolic, `sympy`; numerics at `mp.dps` 30–50):
the §1 identity and its non-oddness; the §2 root sets and the quartic's complex roots;
the §3 lift table; the §4 even/odd split, its factorisation, and the $m_\mu/m_e$
divergence table.

**Not measured.** Whether $s = -\sqrt q$ is *physically* admissible in the framework —
§3 shows it is the branch the bar involution requires, which is an argument, not a
derivation from the substrate axioms. Whether annihilation is suppressed, enhanced or
undefined at a $q$-gradient. What the Classical band's nucleosynthesis actually
produces beyond the corpus's own "$n=p$" row.

**Caveats on the environment.** `q_parameter` would not import (bare container, no
`numpy`), so $q_0$ was taken from AGENTS.md's documented proton pin. The §1–§3 results
are branch-and-root algebra and do not depend on $q_0$ at all. `corpus_search` — the
one grep path that survives a change of vocabulary — **did not run**; the
`paper-assistant` MCP server failed to connect, so every absence claim in §6 is
grep-shaped: those spellings, on those surfaces.
