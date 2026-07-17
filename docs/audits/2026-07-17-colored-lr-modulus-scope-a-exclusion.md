
# Colored Lawrence–Rozansky modulus — scope-(a) excluded at the Σ(2,3,5) fibre root

**Date:** 2026-07-17 · **Axis:** W_λ keystone (m_p·m_μ root cause) ·
**Tier:** exact structural probe — no fit, nothing wired, no tier change, Lean
`loc_matches` gate stays open. Executes **Front 2** of
[`2026-07-17-three-front-attack-specs.md §2`](2026-07-17-three-front-attack-specs.md),
the one attack front with no owning sibling PR.

**Probe:** [`keystone_colored_lr_modulus_s013.py`](../../computations/probes/keystone_colored_lr_modulus_s013.py)
→ [`keystone-colored-lr-modulus-s013.witness.json`](../../computations/probes/keystone-colored-lr-modulus-s013.witness.json)
(exact fifth-root / golden-ratio sympy; reuses the machine-validated s013
τ_N / Thm-10 anchor by citation).

## The open target

Framing-is-phase (#3703) left one open object in the keystone chain:
$$|S_{0\lambda}^{\Sigma(2,3,5)}(\zeta)| = d_\zeta(\lambda)/D(\zeta)$$
at fibre roots of unity, colours mapped by McKay$(2I\leftrightarrow\hat E_8)\circ(A_5\subset S_5)$
onto the **marks** $\{1,4,5,6\}$. The value map at real $q_0$ is $d_{q_0}(\lambda)=[\text{mark}]_{q_0}$,
with the split electron node $(3,1,1)$ equal to $[5]_{q_0}+1$ (**not** $[6]_{q_0}$).
Target ratio-vector $(1,\,4.110,\,5.220,\,6.220)$.

## The construction and the four kill criteria (all exact)

A Wilson line of colour $\alpha$ on the order-$p_3=5$ fibre multiplies each of the
two flat connections $k\in\{1,2\}$ (CS $=-1/120,-49/120$) by the SU(2) quantum
dimension $[\alpha]_k = \sin(\alpha k\pi/5)/\sin(k\pi/5)$, $\alpha=1..4$.

| # | criterion | result |
|---|---|---|
| **K1** | $\alpha=1$ anchor: $[1]_k=1$ both flats (bare vacuum row) | **holds** |
| **K2** | reflection $[5-\alpha]_k=\pm[\alpha]_k$ ⇒ colours collapse $\alpha{=}4\equiv1,\ \alpha{=}3\equiv2$; **2** independent moduli per flat | **D=2 collapse confirmed** — colouring $p_3{=}5$ does *not* escape the D=2 vacuum row |
| **K3** | $|[\alpha]_k|\le 1/\sin(\pi/5)=1.7013$, but max target ratio $=6.220$ | **target exceeds the root bound** — the value map is a real-$q_0$ *growing* object |
| **K4** | mark $6>$ fibre order $5$ ⇒ not a single $p_3{=}5$ colour; $3\oplus3'$ two-block $2[3]_k=3.236\ (\text{flat }1)\ne[5]_{q_0}+1=6.220$ | **split node not reproduced** ("$[6]_\zeta$ vs $[5]_\zeta+1$" criterion, decided) |

Exact closed forms: flat 1 gives $([1],[2],[3],[4]) = (1,\varphi,\varphi,1)$, flat 2
gives $(1,\varphi^{-1},-\varphi^{-1},-1)$ ($\varphi$ the golden ratio) — bounded and
reflection-symmetric, the algebraic signature of a fifth-root modular object.

## Reading (scope discipline)

**Scope-(a).** What is excluded: the colored-LR construction *at the Σ(2,3,5)
fibre roots of unity* as the carrier of the value map. It re-derives the D=2
collapse (K2), is bounded below the growing target ratios (K3), and the split
mark-6 node lies outside the single-fibre colour range with no two-block rescue
(K4). This **refines, does not contradict**, the standing ledger note
("colored Lawrence–Rozansky modulus + $q_0$-continuation deferred/open"): the
genuine open object is precisely the **$q_0$-continuation**. The value map
$[\text{mark}]_{q_0}$ is a *real-$q_0$, Habiro-continued, growing* quantum
integer; the root-level modular object is D=2 and bounded, so it cannot *be* the
value map — only continue to it. A carrier, if any, is a $q_0$-continued or
larger-$D$ geometric family (more exceptional fibres, or genuinely colored
knot-complement blocks), exactly as s013 concluded.

**What this sharpens vs s013.** s013 refuted "bwS0 = the *bare* vacuum row"
(2 vs 4 classes). This probe adds the *colored* insertion the spec asked for and
shows the coloring reflection-collapses back to D=2 (K2) — so the "add a color to
escape D=2" route is closed — and gives the precise reason the root cannot carry
it (bounded fifth-root vs growing real-$q_0$, K3) plus the mark-6/fibre-order-5
structural obstruction (K4). The keystone frontier stays on the $q_0$-continuation
of $[\text{mark}]_{q_0}$, not the root-level modular S-matrix.

**Method note.** Exact sympy fifth-root arithmetic; the s013 τ_N/Thm-10 machinery
is machine-validated and cited, not re-run. Math grep battery run by hand;
pipeline render unavailable in this sandbox — **not machine-validated**.

---

## Addendum (2026-07-17, same day) — cross-reference + K3 framing correction

A sibling probe landed on `main` in the same wave:
[`lr_modulus_identification_sigma235.py`](../../computations/lr_modulus_identification_sigma235.py)
(PR #3822, audit
[`2026-07-17-lr-modulus-identification.md`](2026-07-17-lr-modulus-identification.md))
+ [`habiro_interpolation_wlambda.py`](../../computations/habiro_interpolation_wlambda.py).
It executes the **fuller** Front 2: all three exceptional fibres ($p=2,3,5$),
not only the order-5 fibre this probe treated, and derives the **corrected exact
identity**
$$|S_{0\lambda}^{(m)}| = 2\,d_{\zeta^m}(\lambda)/D_{\hat E_8}(\zeta^m)\quad(\text{exact }\mathbb{Q}(\sqrt5)),$$
with $\zeta = e^{m\pi i/5}$ (the order-$2p_3=10$ fibre holonomy, Galois-indexed by
the flat connection $m$), a global fold factor $2$ (resp. $\sqrt2$), and the whole
identity living at the folded $D=2$ level. That is the more complete and more
precise treatment; **read #3822 as the reference result** for Front 2. This
probe's contribution is the single-order-5 restriction of the same picture.

**Consistency and one framing correction.**

- **K2 (D=2 collapse) agrees** with #3822's fold verdict exactly — the McKay
  colouring factors *through* the collapse ($\alpha{=}4\equiv1$, $\alpha{=}3\equiv2$),
  it does not escape it. #3822's `(F)` is this probe's K2.
- **K3 should be read narrowly.** This probe phrased K3 as "the root modulus
  *cannot reach* the growing target ratios." #3822 shows the sharper truth: the
  modulus **identity holds *exactly* at the folded root level** ($|S_{0\lambda}|\,D = 2|[\text{mark}]_\zeta|$,
  $\mathbb{Q}(\sqrt5)$-exact). So the correct statement is not that the root
  "fails" to reach the target, but that the root realizes the identity *at the
  folded $D=2$ level*, and the **generic-$q$ / archimedean-$q_0$ separation of the
  four classes is the standing open continuation problem** (#3652 / #3681),
  unchanged. The bounded-fifth-root-vs-growing-$q_0$ observation (K3) is a
  *symptom* of that continuation gap, not an independent obstruction. K4 (the
  mark-6 / fibre-order-5 split-node point) likewise refines to #3822's exact
  reading: at the fibre root $[5]_\zeta + 1 = 1 = |[6]_\zeta|$, moduli consistent
  across the $S_5$-block and $2I$-node dictionaries.

**Net.** The scope-(a) headline stands — the colored-LR object at the Σ(2,3,5)
fibre root is folded ($D=2$) and the value map's four-class separation is a
*real-$q_0$ continuation* problem, not a root-level one — but the precise carrier
of that statement is #3822's corrected exact identity, to which this probe should
defer. No fit; nothing wired; the continuation gap (#3652/#3681) is the live open
object.
