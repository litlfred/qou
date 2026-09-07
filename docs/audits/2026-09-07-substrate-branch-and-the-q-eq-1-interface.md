# The substrate branch $s = \pm\sqrt{q}$, the missing $\varphi^2$ degeneration, and the $q = 1$ interface


> ## Read this first — live state, 2026-09-07
>
> This document accreted across one session and **§9 retracts or reframes five of its
> own earlier claims**. Rather than renumber (which would break every cross-reference in
> the PR and commit history), each superseded section carries a 🛑 banner pointing at its
> retraction. The corrected state is:
>
> | | claim | status |
> |---|---|---|
> | **Live** | The modulus is `z = s − 1/s`; `r(z) = (5/27)(z+1)(4z²−z+4)`, matching `t-duality-elliptic.md` exactly | §9.4, Lean-verified |
> | **Live** | `r(z) − r(−z) = (10/27)z(4z²+3)` — matter and antimatter colour fibres are **different curves**, 7.878 % at `q₀` | §10.1, Lean-verified |
> | **Live** | They coincide **iff `q = 1`** — the interface has a derived meaning | §10.2, Lean-verified |
> | **Live** | One degeneration, at `z = −1`; `4z²−z+4 > 0` | §9.5, Lean-verified |
> | **Live** | Interfaces **cannot** be dark matter — codimension forces `ρ ∝ a⁻¹` | §11, scope-(b) |
> | **Live** | `Σ_λ y_λ(H₃) → 3/4` exactly, so `ρ` does not vanish at `q = 1` | §4b (the measurement half) |
> | Conditional | The `q = 1` **barrier** — needs `conj:mass-endomorphism` | §9.3 |
> | Open | Is `s = −√q` physically reachable? Owner: *"don't exclude but maybe not observable"* | §13 |
> | Reframed | §1 and §2 — true observations, wrong frame | §9.4, §9.5 |
> | **Retracted** | "Nothing to emit at `q = 1`" — false for baryons | §9.2 |
> | **Retracted** | "Five reasons antimatter can't be dark matter" — 2 of 5 | §9.1 |
>
> **Nothing under `content/` is modified by this document.** The four content changes it
> implies are §7 proposals, awaiting the author.

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

> **🛑 BADLY FRAMED — read §9.4 first.** The observation is true and the point is
> elsewhere: the modulus is $z = s - s^{-1}$ and $r$ is a clean **polynomial in $z$**,
> already written as $q_W(z)$ in `t-duality-elliptic.md`. Two blocks agree; one
> sentence of presentation in a third is wrong. Formalised in
> `QOU/BringsSurface/ColourCurveModulus.lean`.


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

> **🛑 BADLY FRAMED — read §9.5 first.** There is **one** degeneration, at $z = -1$.
> The two $q$-values are its two preimages under $q = s^2$, so the regime table lists
> one preimage of one point, not half of a two-point set. Whether the second preimage
> is physically reachable is open — owner ruling, §13.


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

> **🛑 FALSE FOR BARYONS — read §9.2 first.** $V_L(1) = (-2)^{c-1}$ trivialises
> **knots**, not **links**: Hopf $\to -2$, Borromean $\to 4$. The proton is a link.
> The de-particling claim holds for leptons only, and §10.4 draws the (more
> interesting) corrected consequence.


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

### 4b. Settled: the mass ratio diverges, so the interface is a BARRIER

> **🛑 CONDITIONAL ON AN OPEN CONJECTURE — read §9.3 first.** The measured divergence
> of $\mathrm{Vol}(K)\rho(K)/\hbar_q^2$ stands. The **barrier** does not: it is an
> absolute-energy claim in a framework that excises absolute mass, and it needs
> $m_e$'s own $q$-scaling, which comes from `conj:mass-endomorphism` because the
> electron is a torus knot with $\mathrm{Vol} = 0$.


§4 left "barrier or door" open, because `rem:cosmological-chirality-flip`'s
"vanishing masses" contradicts $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$. The escape
route for the prose was that the density $\rho$ might itself vanish at $q=1$, cancelling
the $\hbar_q^{-2}$ divergence. **It does not.**

Measured via `wedderburn_jones_markov.y_lambda_at(3, q)`:

| $q$ | $\hbar_q$ | $\sum_\lambda y_\lambda(H_3)$ | $\mathrm{Vol}(4_1)/\hbar_q^2$ |
|---|---|---|---|
| 1.1099785827513808 | 0.099081716 | 0.752702113252 | 206.7683264 |
| 1.05 | 0.047619048 | 0.750594176855 | 895.1784969 |
| 1.01 | 0.0099009901 | 0.750024750637 | 20706.83865 |
| 1.001 | 0.000999001 | 0.75000024975 | 2033945.009 |
| 1.0001 | $9.9990001\times10^{-5}$ | 0.7500000025 | 203028921.0 |

The weight sum converges cleanly to **exactly $3/4$**. With $\hbar_q \to 0$ and
$\mathrm{Vol}(K)$ $q$-independent, $m(K)/m_e = \mathrm{Vol}(K)\rho(K)/\hbar_q^2$
**diverges**. Since the framework's mass content is entirely in the ratios — absolute
mass is $m_e \times$ (dimensionless ratio) with $m_e$ fixed by fiat — the prose claim
has no support from the machinery.

**Consequence.** Reaching the $q=1$ layer costs unbounded energy: the surface is
**self-shielding**, matter and antimatter domains never come into contact, and the
CDG98 $\gamma$-ray bound is evaded by an infinite barrier rather than by a suppressed
cross-section. This is `rem:time-reversal-energy-barrier`'s
$\mathfrak{E}_{\text{flip}} = +\infty$ appearing *spatially* rather than in
configuration space.

**Scope: (a), not (b).** What was measured is $\sum_\lambda y_\lambda$, not
$\rho_{\text{pb}}(K) = \sum_\lambda y_\lambda \chi^\lambda(\beta_K)$ for a specific
knot. At $q=1$ the algebra is $\mathbb{C}[S_n]$ and the $\chi^\lambda$ are integer
symmetric-group characters, so $\rho$ could still vanish for a knot whose image
permutation makes the sum cancel. **Generic** knots give finite nonzero $\rho$ and hence
a divergent ratio; a per-knot character computation would be needed to upgrade this to a
structural exclusion.

**Flagged, not claimed.** AGENTS.md's notation register states the three partition-weight
families coincide at $q=1$ and that $\sum_\lambda w_\lambda(1) = 1$ exactly. The measured
$y_\lambda$ sum converges to $3/4$, not $1$. That is most likely a normalisation
convention inside `y_lambda_at` rather than a defect, but it has not been checked and
should not be quoted as agreement.

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

> **🛑 2 OF 5 SURVIVE — read §9.1 first.** The budget, CMB-vs-BBN and photon-coupling
> arguments all presuppose fixed fundamental constants, which is what a varying-$q$
> proposal denies. Only the Bullet-Cluster offset and the fixed-$q$ luminosity
> objection are clean.


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

---

# 9. Adversarial pass on this document's own claims (2026-09-07)

Run under the standing critical-distance licence. Eight assertions made in this
session, attacked. Three fail, two are badly framed and are restated, three survive.

## 9.1 FAILS — "antimatter cannot be dark matter, five independent reasons" (§6)

Three of the five **presuppose fixed fundamental constants**, which is precisely what
the varying-$q$ proposal denies. The budget argument ($\Omega_c/\Omega_b = 5.364$), the
CMB-vs-BBN 3 % agreement, and the pre-recombination photon-coupling argument are all
inferences made *within* $\Lambda$CDM's assumption that $\alpha$, $m_e$ and $m_p/m_e$ are
constant in space and time. Using them against a proposal that varies $q$ is circular,
and I did not flag it.

**Survive cleanly:** the Bullet-Cluster offset (a kinematic fact about collisionality,
independent of constants) and the luminosity objection *at fixed $q$*. So the honest
count is **2 of 5**, not 5 of 5.

## 9.2 FAILS — "at $q=1$ there are no particles, so nothing to emit" (§4a)

**False for baryons.** The Jones polynomial at $q=1$ obeys $V_L(1) = (-2)^{c-1}$ for a
link of $c$ components. Only **knots** trivialise:

| object | components | $V_L(1)$ |
|---|---|---|
| trefoil $T_{2,3}$ — electron | 1 | $1$ |
| Hopf link $\mathcal{L}_H$ | 2 | $-2$ |
| Borromean $\mathcal{B}_3$ — proton core | 3 | $4$ |

The proton is $\mathcal{B}_3 \oplus \mathcal{L}_H$, a **link**. So §4a's claim holds for
leptons and fails for baryons. See §10.4 — the corrected statement is more interesting
than the wrong one.

## 9.3 FAILS AS STATED — "barrier, not door" (§4b)

I made an **absolute-energy** argument in a framework that excises absolute mass
(AGENTS.md, owner ruling 2026-08-11). What §4b measures is that
$\mathrm{Vol}(K)\rho(K)/\hbar_q^2$ diverges — a **ratio to $m_e$**. Whether *reaching*
the layer costs unbounded energy needs $m_e$'s own $q$-scaling, and that is unknown:
the electron is the trefoil, a **torus** knot with $\mathrm{Vol}(T_{2,3}) = 0$, so its
mass does **not** come from the volume–density formula at all. Per
`q-energy-terms-and-limits.md` it arises from quantum-dilogarithm contributions across
the brane tower — `conj:mass-endomorphism`, **a conjecture**.

So the barrier claim is **conditional on an open conjecture**, not established. The
divergence of the *ratio* stands; the *barrier* does not.

## 9.4 BADLY FRAMED — "$r$ depends on $s$, not $q$" (§1)

True, and it misses the point. The right statement is that the modulus is
$z = s - s^{-1}$ — the corpus's own "spacetime ratio" — and $r$ is a clean **polynomial
in $z$**. Setting $s^2+s-1 = s(z+1)$ and $4s^4-s^3-4s^2+s+4 = s^2(4z^2-z+4)$,

$$
  s^3 r = \tfrac{5}{27}\,s^3 (z+1)(4z^2-z+4)
  \quad\Longrightarrow\quad
  r(z) = \tfrac{5}{27}(z+1)(4z^2-z+4) = \tfrac{5}{27}(4z^3+3z^2+3z+4),
$$

which is **exactly** the $q_W(z)$ already written in `t-duality-elliptic.md` (verified,
symbolic difference $0$). I reported a defect where two blocks in fact agree; what is
actually wrong is one sentence of presentation in a third.

## 9.5 BADLY FRAMED — "the corpus lists half the degeneration locus" (§2)

There is **one** degeneration, at $z = -1$, since $z+1 = 0 \iff s^2+s-1 = 0$. The golden
ratio appears only on pulling that single condition back along $z = s - s^{-1}$ and
$q = s^2$, where it acquires two preimages $q \in \{\varphi^{-2}, \varphi^2\}$. So the
regime table lists **one preimage of one point**, not half of a two-point set. Same
actionable content, correct frame.

## 9.6 OVERSTATED — the $\theta_{\rm res}^2$ comparison

Corrected in three ways already (normalisation $\times2$; coefficient $3.9162481$, not
$O(1)$; and the bridge from *crossing energy* to *mass* is asserted, not derived).
Deeper: `sec:cp-violation-evidence` prefixes the ansatz with **"If"**. I called a hedged
guess in a remark "the framework's own scale".

## 9.7 UNVERIFIED — the CDG98 bound

Quoted from memory, with a specific number ($\gtrsim 1$ Gpc). The library holds no
source on antimatter cosmology, so it cannot be checked in-corpus, and §10.2 may make it
inapplicable anyway.

## 9.8 WEAK — "no B-mode at the interface" (§4a)

Rests on a **remark**'s T/E/B $\leftrightarrow$ jet-degree mapping, which is not derived,
and holds exactly at $z = 0$, a measure-zero locus.

## Survives the pass

The $z$-modulus reframing (§9.4, new and verified); the bar defect and its vanishing
locus (§10.1–10.2); the degeneration being $z=-1$ with $4z^2-z+4 > 0$; the measured
$\sum_\lambda y_\lambda(H_3) \to 3/4$; SN 1987A; the Bullet Cluster.

# 10. Conclusions and implications for QOU

Stated granting that the binding-energy accuracy problems are resolvable, so that they
are not the objection.

## 10.1 QOU carries a DERIVED matter/antimatter asymmetry at the substrate level

The bar involution $q \mapsto q^{-1}$ is $s \mapsto s^{-1}$, which sends $z \mapsto -z$.
The Weierstrass coefficient is **not even in $z$**, and the defect is exact:

$$
  r(z) - r(-z) = \tfrac{10}{27}\,z\,(4z^2+3).
$$

At $q_0$: $z_0 = 0.104388058259$, $r(z_0) = 0.805630515912$,
$r(-z_0) = 0.687958595244$, fractional asymmetry
$\bigl(r(z_0)-r(-z_0)\bigr)/\bigl(r(z_0)+r(-z_0)\bigr) = \mathbf{0.07878466694}$.

**Implication.** The matter and antimatter colour fibres are *different elliptic curves*.
QOU does not need a Sakharov mechanism to *distinguish* matter from antimatter — the
distinction is already in the geometry of the colour fibration, derived and unfitted.
This redirects `sec:cp-violation-evidence`'s stated expectation that "cosmological
regimes must provide the required enhancement": the asymmetry is not cosmological, it is
in $\mathcal{E}_z$.

**Do not over-read.** $7.9\%$ is eight orders of magnitude from $\eta \sim 6\times10^{-10}$.
This is a **curve** asymmetry, not a **number-density** asymmetry, and nothing here
connects them. It is a relocation of the open problem, not a solution to it.

## 10.2 $q = 1$ is the unique locus where matter and antimatter coincide

$r(z) = r(-z) \iff z = 0 \iff s = s^{-1} \iff q = 1$, since $4z^2+3 > 0$.

**Implication.** The interface is at $q=1$ for a *derived* reason — it is exactly where
the framework's own asymmetry vanishes — rather than by the continuity argument of §4,
which only said a path must cross it.

## 10.3 The substrate window is bounded and bar-symmetric

One degeneration at $z=-1$, two $q$-preimages $\varphi^{-2}$ and $\varphi^{2}$. The
physical window is $(\varphi^{-2}, \varphi^{2}) = (0.381966, 2.618034)$, **bounded above**,
against the regime table's unbounded $q>1$. A structural constraint the corpus does not
currently use.

## 10.4 The interface is SELECTIVE: leptons de-particle, baryons do not

From §9.2: at $q=1$ knots trivialise ($V=1$) but links do not ($\mathcal{L}_H \to -2$,
$\mathcal{B}_3 \to 4$). Leptons lose their invariant at the interface; baryons keep a
nonzero one.

**Implication, and it is the most striking thing in this document:** a $q=1$ surface
would treat leptons and baryons differently. **Marked speculative** — "retains a nonzero
Jones value" is not the same as "is reflected", and no transport calculation has been
done. But a charge-separating boundary is a strong, unusual prediction and is worth a
real calculation.

## 10.5 What this does NOT do for dark matter

> **🛑 SUPERSEDED BY §11, which computes it.** The hedge below was a punt. Interfaces
> **cannot** be dark matter: codimension alone forces $\rho \propto a^{-1}$ against
> dark matter's $a^{-3}$.


The budget objection is untouched: nothing here produces $\Omega_c/\Omega_b = 5.364$.
And this is a **boundary** mechanism, so its energy content scales with interface *area*
while a halo's scales with *volume* — the arithmetic is entirely different from §6 and
**has not been computed**. Do not claim it helps; do not claim it cannot.

## 10.6 Bottom line

Granting resolvable binding errors, the session's net gain for QOU is: a derived
substrate-level matter/antimatter asymmetry, a derived meaning for $q=1$, and a bounded
bar-symmetric substrate window. Its net loss is three of my own claims, one of which
(§9.3) was an absolute-mass argument in a framework that forbids them.

**Not gained:** dark matter, the baryon-asymmetry magnitude, absolute masses.

---

# 11. The area-vs-volume arithmetic — §10.5 computed, and §10.5 roasted

§10.5 said "do not claim it helps; do not claim it cannot." **That was a punt dressed as
caution.** The answer takes five lines of geometry, is decisive, and needed no QOU
microphysics. Deferring it transferred the work to a reader who types with difficulty.

## 11.1 The scaling argument — geometric, and it alone is decisive

A codimension-1 surface stretched by the expansion has area $\propto a^2$ inside a
volume $\propto a^3$, so

$$
  \rho_{\text{interface}} \propto a^{-1}, \qquad \rho_{\rm DM} \propto a^{-3},
$$

and the ratio evolves as $a^{2}$. **This follows from the codimension alone** — no
surface tension, no substrate dynamics, nothing QOU-specific.

| matched at | consequence |
|---|---|
| today | at recombination ($z = 1100$) the interface supplies $8.24946\times10^{-7}$ of the dark matter the CMB third peak requires |
| recombination | today the interface exceeds $\rho_{\rm DM}$ by $1.2122\times10^{6}$ |

The CMB acoustic-peak heights measure $\Omega_c$ *at* $z \approx 1100$. A component six
orders of magnitude short there cannot be dark matter, whatever it does today.

## 11.2 Surface tension, independently

Matching $\Omega_{\rm DM}$ today at Hubble-scale separation ($\rho = \sigma/L$,
$L = c/H_0 = 1.37332\times10^{26}$ m, $\rho_{\rm DM} = 2.25852\times10^{-27}$ kg m$^{-3}$)
requires

$$
  \sigma = 0.310168\ \mathrm{kg\,m^{-2}} = 2.78765\times10^{16}\ \mathrm{J\,m^{-2}}
        = 6.77486\times10^{21}\ \mathrm{eV}^3,
  \qquad \sigma^{1/3} = 18.922\ \mathrm{MeV}.
$$

The Zel'dovich–Kobzarev–Okun domain-wall bound is $\sigma^{1/3} \lesssim 1$ MeV.
**Violated by $18.9\times$ in the scale, $6775\times$ in $\sigma$** — the classic
domain-wall problem, arrived at from the other end.

## 11.3 Clustering, independently again

Flat rotation curves need $\rho(r) \sim r^{-2}$ in halos. A wall network is
$\rho \sim \sigma/L$, roughly uniform on scales below $L$. Even at the right budget it
produces the wrong profile.

## 11.4 Verdict, and what it does NOT kill

**Interfaces cannot be dark matter.** Scope-(b): the excluding invariant is the
**codimension**, which fixes the $a^{-1}$ scaling independently of any microphysics.

It does **not** touch the *bulk* proposal — matter at $q \neq q_0$ filling a volume
still scales $a^{-3}$ and is subject only to the §6/§9.1 objections. Interfaces as dark
matter was a possibility **I** raised in §10.5, not the original proposal; this closes my
own suggestion, not the owner's.

# 12. `qou-kyi3` — what a Classical-band domain is made of

`rem:golden-ratio-degeneration`'s regime table gives $1/\varphi^2 < q < 1$ as
"symmetric nuclei ($n = p$)". Taking that literally:

| nuclide | $Z$ | $N$ | status |
|---|---|---|---|
| $^{1}$H | 1 | 0 | **excluded** — a bare proton has $N \neq Z$ |
| $^{2}$H | 1 | 1 | stable |
| $^{4}$He | 2 | 2 | stable, doubly magic |
| $^{6}$Li | 3 | 3 | stable |
| $^{8}$Be | 4 | 4 | **unstable** — $\to 2\alpha$ in $\sim 8\times10^{-17}$ s |
| $^{12}$C … $^{40}$Ca | | | the $\alpha$ ladder, all stable |
| $^{44}$Ti, $^{48}$Cr, $^{52}$Fe, $^{56}$Ni | | | **unstable** ($N=Z$ but $\beta^+$/EC) |
| $^{56}$Fe | 26 | 30 | **excluded** — the iron peak has $N \neq Z$ |

**Three signatures, in decreasing confidence.**

1. **The ladder terminates at $^{40}$Ca**, the heaviest stable $N=Z$ nuclide. No iron
   peak, no $s$- or $r$-process, nothing with $Z > 20$. A Classical-band domain has no
   heavy elements at all.
2. **The $^{8}$Be gap persists**, so the triple-$\alpha$ bottleneck is still there and
   whether a Hoyle-like resonance exists at $q<1$ is unknown.
3. **No hydrogen.** $^{1}$H has $N=0 \neq Z=1$. This is the sharpest and least secure
   of the three — see the caveat — and if it holds it is remarkable: **we survey the
   universe through hydrogen** (21 cm, Ly-$\alpha$ forest, H$\alpha$, the Balmer series).
   A hydrogen-free domain is nearly invisible to every standard survey, for a reason
   entirely separate from the §4a band-shift.

**This distinguishes the proposal from generic mirror dark matter**, which duplicates our
periodic table wholesale and predicts no compositional signature at all.

## 12.1 Roast of §12

The whole section rests on **one unexplained cell of one table in one remark**.
`rem:golden-ratio-degeneration` asserts "symmetric nuclei ($n=p$)" for the Classical band
with no derivation and no citation, and the corpus's binding machinery is not run at
$q<1$ anywhere. The "no hydrogen" reading in particular turns on whether the rule is
about *nuclei* (so $N=0$ fails) or about *isospin balance in bound states* (where a lone
proton might be exempt). **Nothing here is a QOU derivation; it is the consequence of
taking a table cell literally**, and it should be labelled that way wherever it is used.
The honest next step is to run the binding calculation at $q < 1$ rather than to reason
from the cell.

# 13. Owner ruling on `qou-ndt5`, and what depends on it

Recorded 2026-09-07, verbatim: *"not sure. don't exclude but maybe not observable."*

So the negative branch $s = -\sqrt q$ stays **open, not excluded**, with the live
possibility that the two sheets are physically identified and the branch carries no
observable. The bean stays open (AGENTS.md §13a).

**What this gates.** §10.3's bounded window $(\varphi^{-2}, \varphi^{2})$ **depends on
this ruling.** If the negative branch is not physically reachable, $q = \varphi^2$ is not
a reachable degeneration and the window is *not* bounded above — §10.3 weakens to a
statement about the modulus $z$ rather than about $q$. §10.1, §10.2 and the Lean are
unaffected: they are statements about $z$, and $z = -1$ is a single point regardless of
how many $q$-preimages are physical.

---

# 14. `qou-kyi3` measured — and it undercuts §12's premise

§12 read the regime table's "symmetric nuclei ($n = p$)" cell literally, and §12.1 flagged
that the cell has no derivation. Running the machinery at $q<1$ now gives **positive
evidence against the cell**, not merely an absence of support for it.

## 14.1 The Wedderburn weight sum is exactly bar-even

$\sum_\lambda y_\lambda(H_3)$, computed at `mp.dps` 40 via
`wedderburn_jones_markov.y_lambda_at`:

| $q$ | $S(q)$ | $S(1/q)$ | $\lvert\text{diff}\rvert$ |
|---|---|---|---|
| 1.1099785827513808 | 0.752702113251965401 | 0.752702113251965401 | $0$ |
| 1.5 | 0.786982248520710059 | 0.786982248520710059 | $0$ |
| 2.0 | 0.84 | 0.84 | $0$ |
| 2.618033988749895 | 0.888888888888888898 | 0.888888888888888898 | $1.069\times10^{-50}$ |

**Exactly bar-even**, to the full working precision, at four independent points.

Two exact values fall out. At **both** golden thresholds $q = \varphi^{-2}$ and
$q = \varphi^{2}$, $S = 8/9$ — consistent with bar-evenness, since they are reciprocal.
And the interface limit is $S \to 3/4$ (measured $0.75000000000025$ at $q = 1+10^{-6}$,
$0.75$ at $1+10^{-9}$), confirming §4b independently.

## 14.2 Therefore the $n \neq p$ asymmetry cannot come from the weights

If the weight structure is identical at $q$ and $1/q$, it cannot distinguish the
Classical band from its bar-image. The regime table's contrast between "symmetric nuclei
($n=p$)" and "full nuclear chart" must therefore be carried by the **writhe-odd character
sector**, where $\chi^\lambda(\beta)$ carries $q^{w}$ and bar sends $w \mapsto -w$.

The corpus supplies exactly that object.
`mba-sidecar-isovector-chiral-residue` states the bar-odd writhe
$\sigma - \sigma^{-1} = 4Z = 2A + 2(Z-N)$, splitting into an isoscalar part $2A$ and an
**isovector part $2(Z-N)$**.

## 14.3 The consequent prediction contradicts the table

> **🛑 RETRACTED — see §15. The corpus refuted this mechanism on 2026-06-15,
> three months before I proposed it.** The mirror isospin split is **Coulomb**, not
> categorical chirality, established symbolically and validated against AME2020. A
> Coulomb term is charge-magnitude and does not flip sign under bar, so there is no
> isovector sign flip to predict proton excess from.


Under bar, the isovector term $2(Z-N)$ **flips sign**. If in our regime it drives the
neutron excess ($N > Z$) that the observed chart shows at high $A$, then in the
bar-image regime it drives the opposite: **proton excess, $Z > N$** — not $n = p$.

**Scope.** The bar-evenness in §14.1 is measured and solid. The inference in §14.2 is
sound. §14.3 is **conjectural**: it needs the sign convention on the isovector term
checked against the producer, which has not been done. But it is a *positive* prediction
that disagrees with the table cell, where §12.1 could only report the cell as
underived — so §12's three signatures ($^{40}$Ca termination, the $^{8}$Be gap, and
especially "no hydrogen") should now be treated as **resting on a cell that the
framework's own isovector mechanism appears to contradict.**

## 14.4 A defect found in passing: the interface point is not computable

`y_lambda_su_n.q_int` evaluates $[m]_q = (q^m - q^{-m})/(q - q^{-1})$, which divides by
zero at $q = 1$ — a `ZeroDivisionError`, not a guard. The singularity is **removable**
($[m]_q \to m$), and the limit is approached cleanly from above ($0.75$ by $q = 1+10^{-9}$),
but it is unimplemented.

So **no producer in the corpus can be evaluated at the interface point itself.** Every
$q=1$ statement in this document, §4a and §4b included, is a limit taken from one side,
never an evaluation at the point. That is a fair way to compute the limit and it is not
the same thing; §4b's "barrier" in particular is a statement about a limit whose
endpoint the machinery cannot reach.


---

# 15. §14.3 retracted, and how I came to make it

## 15.1 The claim and the refutation

§14.3 argued that the bar-odd isovector writhe $2(Z-N)$ flips sign under
$q \mapsto q^{-1}$, so the bar-image regime should show proton excess rather than
$n = p$.

**The corpus had already refuted the premise.**
[`mirror_isospin_coulomb_split.py`](../../computations/mirror_isospin_coulomb_split.py)
and its audit
[`2026-06-15-bqclt-isospin-split-coulomb-not-categorical.md`](2026-06-15-bqclt-isospin-split-coulomb-not-categorical.md)
prove symbolically (sympy) that the categorical chirality split and the Coulomb split
share the isospin factor $(Z-N)(A-1)$ but scale as $A^{-1}$ and $A^{-1/3}$ — so the
over-split goes as $A^{-2/3}$ and **no constant damping $\kappa$ maps the categorical
split onto the physical one.** Validated numerically: one Coulomb length
$r_0 \approx 1.6$ fm fits both $^{3}$H/$^{3}$He and $^{7}$Li/$^{7}$Be, where $\kappa$ is
inconsistent between them (0.50 vs 0.85).

**The mirror isospin split is Coulomb.** A Coulomb term is charge-*magnitude*
($\propto Z^2$) and does not change sign under bar. There is no isovector sign flip,
so §14.3's prediction has no mechanism.

## 15.2 What replaces it — and it is a better argument against the same cell

> **🛑 ALSO WRONG — see §16.** I wrote "our chart with a rescaled Coulomb-to-nuclear
> ratio, not $n=p$". In the deep Classical band the rescaling is **four to five orders
> of magnitude**, which is not a rescale but a switch-off — and with Coulomb off,
> $n = p$ is exactly right. The regime table's cell is **derived**, not contradicted.


§14.2 still stands: the weight sum is bar-even (§14.1, measured), so the Wedderburn
weights cannot carry an $n \neq p$ distinction. The corpus's answer to *what does* carry
it is Coulomb — and Coulomb is bar-even in **sign**.

So under bar the neutron-excess *structure* is unchanged. What changes is the Coulomb
term's **magnitude**, through the $q$-dependence of $\alpha_{\rm EM}$ and $\hbar_q$,
which moves the valley of stability without reflecting it. **A Classical-band domain
should therefore have our chart with a rescaled Coulomb-to-nuclear ratio — not $n = p$.**

That is a cleaner argument against the regime-table cell than §14.3 was, and it rests on
a corpus result rather than on my conjecture. **How far the valley moves is not computed
here** — it needs $\alpha_{\rm EM}(q)$ below $q = 1$, and the corpus's $\alpha_{\rm EM}$
route is itself conditional on an open Lean `sorry` (the Witten-$\kappa$ Gram
determinant).

## 15.3 The process failure, stated plainly

I proposed a mechanism the corpus had refuted in a dedicated audit document three months
earlier. AGENTS.md's corpus-grep checklist exists precisely to prevent this, and **I did
run it — at session start, on antimatter and dark matter.** I did not re-run it when the
session moved onto the isovector/isospin split, which is a different topic with different
vocabulary.

**The rule this yields: a new claim needs a new grep, not the session's opening one.**
The checklist is per-claim, not per-session. Both producers that settle this
(`mirror_isospin_coulomb_split.py`, `em_linking_fh_mirror_split_charge_blindness.py`)
sit in `computations/` under the obvious spellings — path 3 would have returned them on
the first try.

Aggravating: `corpus_search`, the one path that survives a change of vocabulary, has
been down all session (the `paper-assistant` MCP server fails to connect). That is a
reason to grep *more*, not less, and I did the opposite.


---

# 16. $\alpha_{\rm EM}$ is symbolic in $q$ — and it derives the regime-table cell

Owner correction: $\alpha_{\rm EM}$ is symbolic in $q$, so the $\alpha_{\rm EM}(q<1)$
question does not need the `sorry`-conditional route I assumed in §15.2.
[`bring-residue-resolvent-context.md`](../../content/quantum-observable-universe/mass-theory/bring-residue-resolvent-context.md)
gives the closed form

$$
  1/\alpha_{\rm EM} = q\,[9]_q\,[10]_q + \tfrac{2}{3\pi}.
$$

**Provenance.** The orders 9 and 10 are labelled the **genus-4 pair** and tied to
`BringResidueAtOrder`, i.e. to Bring's surface, *not* selected to hit 137 — so this is
not the "selection against the target" failure the NO-FITTING directive names. But it is
**conditional**: `BringResidueAtOrder` is an open class, so the form is
conditional-proved, and everything below inherits that.

At $q_0$ it gives $1/\alpha = 137.035415444$ against CODATA $137.035999084$ —
**4.259 × 10⁻⁶ relative**.

## 16.1 The whole bar-asymmetry is the prefactor

$[n]_q = (q^n - q^{-n})/(q - q^{-1})$ is **exactly bar-even** (numerator and denominator
both negate; measured difference $7.35\times10^{-40}$ at `mp.dps` 40). So
$1/\alpha = q\,P(q)$ with $P$ bar-even, and the entire $q \mapsto q^{-1}$ asymmetry sits
in the prefactor:

$$
  \tfrac{1}{\alpha(1/q)} - \tfrac{2}{3\pi}
  = \frac{1}{q^{2}}\Bigl(\tfrac{1}{\alpha(q)} - \tfrac{2}{3\pi}\Bigr)
  \qquad\text{(verified to } 5\times10^{-29}\text{)}.
$$

**And unlike `y_lambda_su_n.q_int` (§14.4), this expression is evaluable at $q = 1$**:
the $q$-integers become the integers, so
$1/\alpha(1) = 9\cdot 10 + 2/(3\pi) = 90.2122065908$, i.e.
$\alpha(1) = 0.01108497439$ — **1.519× ours**. The maximum is just below the interface,
at $q = 0.983351259$ with $\alpha = 0.01117811536$, **1.5318× ours**.

## 16.2 The Classical band splits in two, and only the deep half gives $n = p$

| $q$ | $1/\alpha$ | $\alpha/\alpha(q_0)$ | Coulomb |
|---|---|---|---|
| 1.1099786 (ours) | 137.0354154 | 1.0 | — |
| 1.0 (interface) | 90.21220659 | 1.5190341 | **stronger** |
| 0.95 | 92.63566229 | 1.4792944 | **stronger** |
| 0.90091828 (bar of $q_0$) | 111.2652777 | 1.2316099 | **stronger** |
| 0.85 | 159.3072664 | 0.86019564 | ~ours |
| 0.8 | 266.2995174 | 0.5145913 | ~ours |
| 0.75 | 516.9008173 | 0.26510969 | weaker |
| 0.7 | 1154.29389 | 0.11871796 | weaker |
| 0.6 | 8653.079795 | 0.015836606 | weaker |
| 0.5 | 116508.1011 | 0.0011761879 | **off** |
| 0.38196601 ($\varphi^{-2}$) | 6677056.383 | $2.05\times10^{-5}$ | **off** |

**Deep band, $q \lesssim 0.75$:** $\alpha_{\rm EM}$ collapses by four to five orders of
magnitude. Coulomb switches off, and with it the only force pushing $N$ above $Z$. What
remains is the symmetry term, which favours $N = Z$. **The regime table's "symmetric
nuclei ($n=p$)" is derived here, not asserted.**

**Upper band, $\approx 0.87 < q < 1$:** $\alpha_{\rm EM}$ is *stronger* than ours, up to
1.53×. Coulomb repulsion is **stronger**, so the chart should carry **more** neutron
excess than ours — not $n = p$. The crossing where $\alpha$ returns to our value lies
between $q = 0.85$ and $q = 0.90$ (the root-finder converged back to $q_0$ rather than
the sub-unity root, so this is bracketed from the table, not solved).

So the cell is **right for the deep band and wrong for the upper band**, and the table
states it for the whole of $1/\varphi^2 < q < 1$.

## 16.3 What this says about the owner's scenario specifically

**The bar-image of our substrate, $q = 1/q_0 = 0.900918$, sits in the *upper* band**,
where $\alpha_{\rm EM}$ is **1.2316× ours**. A bar-conjugate domain therefore has
*stronger* Coulomb and a **more neutron-rich** chart than ours — not a symmetric one, and
not our chart either. That is a compositional signature, and it is the one that would
actually apply to the antimatter-domain proposal, rather than the $n=p$ signature of
§12 which belongs to the deep band.

## 16.4 Two of my own claims retracted, in opposite directions

§14.3 said the bar-image regime has **proton excess** (mechanism: isovector sign flip).
Retracted in §15 — the split is Coulomb, which does not flip sign.

§15.2 said it has **our chart with a rescaled Coulomb ratio, not $n=p$**. Also wrong:
in the deep band the "rescale" is $10^{-5}$, which is a switch-off, and $n=p$ is correct
there.

The third answer came from **evaluating the closed form** rather than reasoning about
which mechanism ought to dominate. Both wrong answers were mechanism arguments; the right
one is four lines of arithmetic on a formula that was in the corpus the whole time.

---

# 17. `qou-fi93` — the curve asymmetry cannot reach a number density

§10.1 found a derived 7.878 % matter/antimatter asymmetry in the colour fibre. The
question this bean asks is whether it can become the baryon asymmetry
$\eta \sim 6\times10^{-10}$, or whether the gap can be stated precisely. **It can be
stated precisely, and the answer is no by an exact invariant.**

## 17.1 Every counting object in the framework is bar-even

A number density is a *count*. The framework's counting objects are the Wedderburn
dimensions and the measures built on them, and all of them are bar-even. Measured at
`mp.dps` 40:

| object | bar-parity | worst $\lvert f(q_0) - f(1/q_0)\rvert$ |
|---|---|---|
| integer dimension $\dim V_\lambda$ | $q$-independent | $0$ (trivially) |
| $q$-dimension $d_q(\lambda)$, $n = 3,4$ | **bar-even** | $1.378\times10^{-40}$ |
| Plancherel measure $\mu(\lambda) = d_q^2/D^2$ | **bar-even** | $3.444\times10^{-41}$ |
| Markov weight sum $\sum_\lambda y_\lambda(H_3)$ (§14.1) | **bar-even** | $0$ to 40 digits |

And the parity is exact, not numerical. $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ negates
both numerator and denominator under $q \mapsto q^{-1}$, so $[n]_q$ is **exactly**
bar-even; $d_q(\lambda)$ is a ratio of products of $[n]_q$ (the $q$-hook-length formula),
hence bar-even; $\mu$ and $D^2$ inherit it. The residuals above are round-off at 40 digits,
not structure.

## 17.2 The two sectors do not couple

The 7.878 % asymmetry lives in the **colour geometry** — a difference between the
Weierstrass coefficients of $\mathcal{E}_z$ and $\mathcal{E}_{-z}$. Every **counting**
object is bar-even. So matter and antimatter carry *identical statistical weight* in
every measure the framework defines, and the geometric asymmetry has nothing to multiply
against.

**Scope (b) — a structural exclusion, with the invariant named:** no quantity built from
$q$-integers can be bar-odd, and every counting measure in the Hecke tower is built from
$q$-integers. This is exact algebra, not a numerical probe.

## 17.3 What that buys, which is more than a negative

The exclusion is **constructive about where a solution would have to live**. Baryogenesis
in QOU would require a counting measure **not built from $q$-integers** — a genuinely new
structural object, not a tuning of an existing one. That is a sharper statement of the
corpus's open problem than `sec:cp-violation-evidence`'s "cosmological regimes must
provide the required enhancement", and it rules out an entire class of attempts:
re-weighting $y_\lambda$, re-normalising $\mu$, or choosing a different partition measure
cannot work, because all of them are bar-even by construction.

**It also closes the loop on §10.1's caveat.** That section warned against reading the
7.878 % as baryogenesis on the grounds that it is eight orders of magnitude off. The
better reason is this one: it is not eight orders from $\eta$, it is **disconnected** from
$\eta$ — a magnitude gap invites a search for a suppression factor, and there is no
channel to suppress.

## 17.4 What is not established

That no *other* route exists. §17.2 excludes the counting measures the framework
currently defines; it does not exclude a coupling somebody constructs between the colour
geometry and a density. The bean stays open on that residual — the underlying question
(can QOU produce $\eta$?) is an open conjecture, and AGENTS.md §13a forbids closing a
bean whose subject is one, however cleanly the present route is excluded.

---

# 18. §16 checked against `main`'s better $\alpha_{\rm EM}$ route, and the observational test

`main` moved 44 commits under this branch. Two of them
(`aa546b4ba`, `d626761a3`, bean `qou-37j2`) touch $\alpha_{\rm EM}$ directly, and one
announces that a CODATA edition freeze *"flipped its sign"* — so §16 needed checking
against them rather than assuming.

## 18.1 The route I used is the ladder's leading term

`alpha_em_schwinger_ladder_probe.py` on `main` defines

$$
  T(q) = q\,[9]_q\,[10]_q + \tfrac{8}{12\pi}, \qquad H(q) = \tfrac{[2]_q}{8\pi},
$$

and solves the cubic $-H h^2 \alpha^3 + H\alpha^2 + T\alpha - 1 = 0$ (form B, with the
derived Schwinger factor). **$8/12 = 2/3$, so $T$ is exactly the closed form §16 used**,
and §16's $1/\alpha = T$ is the ladder with $H \to 0$.

Reconstructed here, form B at $q_0$ gives $1/\alpha = 137.03599912695$, a residual of
**−0.36523 ppb** against CODATA 2022 — matching `main`'s stated −0.3652 ppb, so the
reconstruction is right.

## 18.2 The band structure is unaffected

| $q$ | $1/\alpha$ leading (§16) | $1/\alpha$ form B (full) | rel. diff |
|---|---|---|---|
| 1.1099786 | 137.035415444 | 137.035999127 | $4.259\times10^{-6}$ |
| 1.0 | 90.2122065908 | 90.2130886964 | $9.778\times10^{-6}$ |
| 0.90091828 | 111.265277741 | 111.265996556 | $6.46\times10^{-6}$ |
| 0.8 | 266.299517437 | 266.299823501 | $1.149\times10^{-6}$ |
| 0.7 | 1154.29389007 | 1154.2939634 | $6.354\times10^{-8}$ |
| 0.5 | 116508.101096 | 116508.101097 | $7.328\times10^{-12}$ |
| 0.38196601 | 6677056.38306 | 6677056.38306 | $2.677\times10^{-15}$ |

The Schwinger correction is at most $\sim10^{-5}$ and **shrinks to $10^{-15}$ in the deep
band**, against a band effect of four to five orders of magnitude. §16 stands, and its
structural claim strengthens: $H = [2]_q/(8\pi)$ is **bar-even**, so in the full ladder
too the entire bar-asymmetry is the $q$ prefactor of $T$.

**A third instance of the $q=1$ singularity.** At $q = 1$, $h^2 = 0$ kills the cubic's
leading coefficient and `mp.polyroots` raises `ZeroDivisionError` — the same removable
degeneration as §14.4, in a different producer. The cubic collapses to form A there; that
is the correct limit, and it is unguarded.

## 18.3 Do we see neutron-rich patches? Yes — and they are not this.

**Observed, and real:**

- **r-process-enhanced metal-poor stars** (r-II, $[\mathrm{Eu/Fe}] > +1$): CS 22892-052,
  CS 31082-001.
- **Reticulum II** — an ultra-faint dwarf where roughly 70 % of member stars are
  r-process enhanced (Ji, Frebel, Chiti & Simon, *Nature* **531**, 610, 2016). This is a
  **galaxy-scale** neutron-rich patch, attributed to a single neutron-star merger
  enriching the dwarf's entire gas reservoir.
- **GW170817 / AT2017gfo** — direct kilonova observation of r-process ejecta.

**None of these is what a shifted-$\alpha$ domain looks like, and the difference is
sharp.** r-process enrichment is *more neutron-capture products* on the **same nuclear
chart** — normal stability, anomalous abundances, because a neutron-rich event happened
nearby. A bar-conjugate domain would have a **different chart**: different *stable*
isotopes at higher $N/Z$, with nuclides stable here unstable there.

**So the discriminator is isotopic, not elemental** — isotope ratios inconsistent with
any known nucleosynthesis, or isotope shifts in absorption lines. That is exactly what
varying-constants spectroscopy tests.

**And it excludes the prediction along every measured sightline.** §16 gives
$\alpha(1/q_0)/\alpha(q_0) = 1.23160717$, i.e.

$$
  \Delta\alpha/\alpha = 0.23160717 = 23.16\,\%,
$$

against quasar-absorption bounds $\lvert\Delta\alpha/\alpha\rvert \lesssim 10^{-6}$ —
**exceeded by $2.3\times10^{5}$** — and the Oklo natural-reactor bound $\lesssim10^{-8}$,
exceeded by $2.3\times10^{7}$. Even the contested Webb *et al.* spatial dipole at
$\sim10^{-5}$ is four orders too small to accommodate it.

**The standing caveat applies unchanged:** those sightlines are luminous gas. A domain
that is dark is not probed by any of this, which is the one place the proposal still
lives.

*Literature here is recalled; the library holds no source on r-process observations or
varying-constants spectroscopy, so none of it is checkable in-corpus.*

---

# 19. The $q=1$ singularity measured — and my "three sites" was wrong twice over

I ended the previous turn saying three unguarded $q=1$ singularities "are now a class,
not incidents", and that "one guard fixes all three". **Both halves are wrong, and
measuring it gives a better finding than the one I claimed.**

## 19.1 The count

I had measured **two** — `y_lambda_su_n.q_int` (§14.4) and the Schwinger cubic's
`mp.polyroots` (§18.2). The third I gestured at does not exist; I wrote "three" from
memory of a pattern rather than from a count.

The real surface, measured over `computations/` and `tools/` excluding `_deprecated`:

| | count |
|---|---|
| files implementing $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ | **197** |
| of those, carrying a $q = 1$ guard | **6** |
| without a guard | **191** |

## 19.2 But 191 is not 191 defects

An unguarded division is a defect only if something can reach $q = 1$. Every producer in
the corpus pins $q_0 \approx 1.11$ or sweeps away from unity, so nothing reaches it —
**the corpus has no $q=1$ evaluation path because no prior work has needed one.** This
session's §4a, §4b and §16 limits are the first thing to want the interface, which is why
it surfaced twice here and nowhere before.

So the honest characterisation is not "a class of defects" but **a convention that holds
because the interface has never been studied**. That is a weaker claim about the code and
a more interesting one about the corpus.

## 19.3 The finding that is real, and larger than the guard

A canonical implementation **exists** —
`tools/qou-substrate/python/qou_substrate/constants.py:176 def q_int(n)`. It is used by
**21** files. **192 define their own.**

So roughly **90 % of the corpus reimplements the $q$-integer locally**, and "one guard
fixes all three" is wrong for a reason that has nothing to do with the count: there is no
single place to put a guard. Any correction to $[n]_q$ — a $q=1$ limit, a precision
change, a convention fix — needs ~192 edits, and a fix applied to the canonical one
reaches 10 % of callers.

This is the same shape as the detector-blindness taxonomy AGENTS.md maintains: a
correction that lands in one spelling and not the others. Here it is a *definition* rather
than a detector, which makes it worse — a detector that misses a case reports a low
number, while a definition that is reimplemented 192 times can silently disagree with
itself.

**Not established:** that the 192 local definitions agree with each other or with the
canonical one. Some may differ deliberately (a different bracket convention, a symbolic
rather than numeric form). Checking that is a separate audit and is not done here; what is
measured is only the count and the absence of a shared import.

---

# 20. Observational programme: which of these actually discriminates

Owner supplied the three standing observational handles on neutron-rich environments.
§18.3 said they are r-process enrichment rather than a shifted chart; this section asks
which of them could nonetheless *test* §16's prediction, and quantifies the one that can.

## 20.1 The three handles, and what each can and cannot do

| handle | what it observes | discriminates a shifted chart? |
|---|---|---|
| **GW170817 kilonova** — Sr II absorption in the AT2017gfo spectrum (VLT/X-shooter) | r-process nucleosynthesis *in real time* | **Indirectly.** The r-process path depends on masses and $\beta$-rates far from stability, which a shifted $\alpha$ would move. But the event is local — it constrains our own neighbourhood, not a distant domain. |
| **Reticulum II** — ~70 % of bright members r-process enhanced, extreme $[\mathrm{Eu/Fe}]$ at very low metallicity | one polluting event's yield, preserved | **Only if isotopic.** Elemental overabundance is normal chemistry with anomalous abundances. The test needs *isotope ratios*, which are hard to resolve in metal-poor giants. |
| **r-II halo stars** — $[\mathrm{Eu/Fe}] > +1$; **actinides detected** in CS 31082-001 (U II 3859.57 Å) | the yield *and* a radioactive clock | **Yes — this is the one.** See §20.2. |

## 20.2 Actinide cosmochronometry is the real probe, and it works differently than I expected

$\alpha$-decay rates are **exponentially** sensitive to $\alpha_{\rm EM}$ through the
Gamow barrier penetrability, $\ln t_{1/2} \approx 2G + \text{const}$ with $2G \propto
\alpha$. Calibrating $2G$ against observed half-lives and applying §16's shift factor
1.23160717:

| nuclide | $t_{1/2}$ (yr) | $2G$ | $2G$ shifted | $t_{1/2}$ ratio |
|---|---|---|---|---|
| $^{238}$U | $4.468\times10^{9}$ | 87.8419 | 108.187 | $6.85\times10^{8}$ |
| $^{232}$Th | $1.405\times10^{10}$ | 88.9876 | 109.598 | $8.93\times10^{8}$ |
| $^{235}$U | $7.04\times10^{8}$ | 85.994 | 105.911 | $4.46\times10^{8}$ |

**The chronometer does not give a wrong age — it gives no age.** Th/U dating reads
$(\mathrm{Th/U})(t) = (\mathrm{Th/U})_0 e^{-(\lambda_{\rm U}-\lambda_{\rm Th})t}$, and the
rate difference collapses from $1.058\times10^{-10}\,\mathrm{yr}^{-1}$ to
$1.713\times10^{-19}$. Over 13 Gyr the ratio drifts to 0.2527 in our regime and to
**1.0000** in the shifted one. So a shifted-$\alpha$ region produces a *null drift*, and
**the fact that r-II stars yield finite, mutually consistent ages is itself evidence that
$\alpha$ was unshifted where their actinides formed.**

## 20.3 The correction: I expected tighter, and it is looser

I said in the previous turn that Gamow amplification would make this "a far tighter probe
than the $10^{-6}$ spectroscopic bound". **Wrong.** The amplification is real, but the
*measurement precision* on stellar ages is only $\sim\pm20\,\%$, so the bound it yields is

$$
  \lvert\Delta\alpha/\alpha\rvert \lesssim 2.08\times10^{-3},
$$

which is **~2000× looser** than quasar absorption spectroscopy. §16's 0.2316 exceeds it by
112×, so it is still an exclusion — just not the tight one I advertised.

**Its value is independence of *location*, not tightness.** Spectroscopic bounds constrain
$\alpha$ in the intervening gas along a sightline; the actinide clock constrains $\alpha$
in the *r-process site where the nuclei were forged*. Those are different places, and for
a proposal whose whole surviving territory is "regions we cannot see spectroscopically",
the second is the more relevant one.

*Literature recalled — Watson et al. on the AT2017gfo strontium, Ji et al. on Reticulum II,
Cayrel et al. on the CS 31082-001 uranium line. The library holds none of these, so none
is checkable in-corpus.*
