# Q_β f-map — the root-of-unity (Faddeev) saddle (why F(q) is never real-q)

**Date:** 2026-07-06
**Status:** FORMALIZE-FIRST SCOPE (structural argument + search narrowing).
Conditional on [`conj:binding-qbeta-complex-volume`](../../folio/quantum-observable-universe/mass-endomorphism/binding-qbeta-complex-volume.md) (#3437)
and the Askey two-saddle structure of
[`self-dual-higgs-real-volume`](../../folio/quantum-observable-universe/braids-and-knots/self-dual-higgs-real-volume.md).
No c_k value, no wiring — flip-flop guard (registry §8) respected.
Complements [`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`](../audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md)
(this is the *forward-pruning* geometric reason for its Invariant 1).

> **Correction note (self-review).** An earlier draft of this doc attributed
> Q_β's root-of-unity structure to the trefoil being a *torus* knot
> (`Vol = 0`, rational CS). That is **backwards** and is retracted. Per the
> Askey two-saddle table below, **torus knots are the real-q / bar-even /
> *mass* saddle**; Q_β is bar-**odd** (the *decay* face) and lives on the
> **hyperbolic / root-of-unity / Faddeev saddle**. And Q_β is a *many-body
> chiral defect* (`Im 𝔙`), **not** any single knot's Chern–Simons invariant
> (the self-dual-Higgs block states this explicitly). The corrected argument
> lands on the same conclusion — F(q) is root-of-unity — for the right reason.

---

## 1. Q_β is the bar-odd decay face of a many-body defect, not a single-knot CS

Per `conj:binding-qbeta-complex-volume` (#3437), Q_β is the imaginary part
of the many-body **binding defect**
`𝔙 = E₀·tr_M((Π_free − 1)∘𝓜)` — the QOU Neumann–Zagier
`Vol + i·CS` analogue, with `Re 𝔙` = binding (bar-even, cosh, hyperbolic
volume) and `Im 𝔙` = **Q_β** (bar-odd, sinh, Chern–Simons/decay). The
lone Higgs knot `4₁` is amphichiral ⇒ self-dual ⇒ `CS(4₁) = 0`: it carries
**only** the real (mass) face, so Q_β is explicitly **not** a property of
any single knot. The decay face is recovered **only from a chiral
(amphichirality-broken) many-body configuration**.

## 2. The Askey two-saddle structure fixes which saddle Q_β lives on

From the self-dual-Higgs block, the two archimedean saddles of the one
quantum A-polynomial `Â_K` (AJ machinery; strong AJ proved for `4₁`,
Nguyen–Tran 2021):

| | torus knots (leptons) | hyperbolic knots |
|---|---|---|
| archimedean saddle | **real `q ∈ (0,1)`** | **root of unity `q = e^{2πi/N}`** |
| dilog regulator | Rogers `Li₂^q` | Faddeev `Φ_q` |
| bar-parity | **bar-even (cosh)** = mass | **bar-odd (sinh)** = decay (chiral only) |

Q_β is **bar-odd (sinh)** ⇒ it sits on the **hyperbolic / root-of-unity /
Faddeev-`Φ_q`** saddle, recovered only when chiral. The bar-even/bar-odd
split IS the two-saddle (real-q Rogers ↔ root-of-unity Faddeev) split.

## 3. Consequence: F(q) is a root-of-unity object — derived, not observed

Because Q_β's archimedean saddle is at **`q = e^{2πi/N}`** (the Faddeev
saddle), the fibre element `F(q)` carrying its ladder is a
**root-of-unity / fibre-level object**, never a real-analytic function of
the substrate `q₀ ∈ (1, ·)`. This **derives Invariant 1** of the
refuted-class map (*"F(q) is fibre-level / root-of-unity, never a real-q
formula"*) from the saddle structure. Until now that invariant was only
*empirical* — the residue of 14 refuted real-q classes and the c_3
rigidity `dc_3/dq ≈ 4.6×10⁶`.

**This also explains *why* the 14 real-q classes failed** (C1–C4, C13,
C14): a real-q formula lives on the **torus/lepton/mass** saddle
(real `q`, Rogers dilog, bar-even) — the **wrong face**. Q_β's decay face
is on the transverse (root-of-unity, Faddeev, bar-odd) saddle, so no
real-q ansatz can ever carry it. The refutations were sampling the wrong
saddle.

## 4. The singularity: a Faddeev-`Φ_q` pole lattice ⇒ the observed simple pole

The Faddeev quantum dilogarithm `Φ_b` has its zeros/poles on a **lattice
of simple poles** at `c_b + ibℕ + ib^{−1}ℕ` (the modular-double lattice).

> **Accuracy caveat (2026-07-06).** The corpus `_phi_q_util.py` "Φ_q" is the
> *compact* single product `∏(1−q^{−k}z)^{−1}`, **missing the `b^{−1}`
> modular-dual factor** that carries the bar-odd/CS structure. The true
> object for the decay face is the modular-double `Φ_b` with the
> `sinh(zb)sinh(zb^{−1})` kernel. Prior compact-`Φ_q` probes are therefore
> unreliable on the Q_β (bar-odd) face — see
> [`2026-07-06-qbeta-faddeev-phi-b-modular-double-accuracy.md`](../audits/2026-07-06-qbeta-faddeev-phi-b-modular-double-accuracy.md). So the ladder generating
function `g(u) = Σ c_k u^k` inherits **simple** poles, and its dominant
one is the nearest Faddeev pole. This matches the measured structure:
PR #1727 found `g(u)` has a **simple pole at `u_substrate`**, fibre-level,
same location at both anchors (210 ppb), residue `A ≈ 1.804×10⁻¹⁵`.

(Note — corrected from the earlier draft: the point is **not** "no dilog
because `Vol = 0`". The Q_β saddle *does* carry a dilog — the **Faddeev**
`Φ_q` — but its singularities are simple poles on a root-of-unity lattice,
so a *simple* pole is the prediction. What is genuinely forbidden is a
**Rogers**-`Li₂^q` structure on the Q_β face — that is the *other* (torus,
bar-even) saddle. The AGENTS.md §7b caution against Bloch–Wigner/dilog
arguments *on the trefoil* still stands: the trefoil is on the bar-even
saddle; the relevant dilog for Q_β is Faddeev on the hyperbolic many-body
defect, not Rogers on the trefoil.)

## 5. How this narrows the f-map search (the deliverable)

- **Seek `F(q)` among Faddeev-`Φ_q` / root-of-unity objects of the
  *hyperbolic, chiral* many-body defect** (Borromean-type links are
  hyperbolic and enter `𝓜`), *not* among torus-knot / real-q / Rogers
  objects.
- **Prune** any ansatz built on the real-q (Rogers, bar-even) saddle — it
  is the mass face, transverse to Q_β. (This retro-classifies the 14
  refuted real-q classes as *wrong-saddle*, not merely *unlucky*.)
- **The chirality requirement is a hard filter:** any candidate must break
  amphichirality (an amphichiral input gives `CS = 0`, no decay face).
- The phase reframe `Q_β/Q_A = cos Φ(u)`, `Φ₁ = √2` (anchor-exact), is the
  Faddeev-saddle holonomy; `Φ` should come from the `Φ_q` regulator of the
  chiral defect, evaluated at the root-of-unity saddle.
- **Next concrete probe (pre-registered, non-fishing):** verify the
  structural claims, not a numeric coincidence — (i) confirm the Borromean
  / many-body `𝓜` inputs are hyperbolic (Faddeev saddle) while the trefoil
  base is torus (Rogers saddle); (ii) confirm `Φ_q`'s pole lattice yields a
  *simple* dominant pole and locate it relative to `u_substrate`. **Do not
  fit `Φ₁ = √2` or `A` to a hand-picked root-of-unity value** — a scan for
  a match would itself be a fit (the C14 anti-fitting lesson).

## 6. Coordination

- **#3429** (Q_β f-map power-class pincer) prunes by **ζ₄ / bar-even
  parity**; this scope prunes by **saddle identity (real-q Rogers vs
  root-of-unity Faddeev)** and singularity type — orthogonal axes. Intent
  posted on #3429.
- **#3437** carries `conj:binding-qbeta-complex-volume`; **#3445 / #3444**
  carry the toroidal/parabolic-cylinder channel work. This scope is a
  *consequence* of #3437 + the self-dual-Higgs Askey table, not
  independent of them.
- **c_3 status:** `a_1 = −c_3` is anchor-dependent (swings 2.375%,
  [c_3 cross-anchor verdict](../audits/2026-07-06-c3-not-exact-cross-anchor-verdict.md)) —
  consistent with §3 (only a root-of-unity `F(q)` on the Faddeev saddle
  can carry the anchor structure; a real-q c_3 cannot be exact).
