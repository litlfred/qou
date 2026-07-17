# The colored Lawrence–Rozansky modulus identification on Σ(2,3,5) — corrected exact identity

**Date:** 2026-07-17 · **Axis:** s5-so3 keystone geometric `W_λ` (1ppQ front 2, unowned per
[`2026-07-17-1ppq-path-reassessment.md`](2026-07-17-1ppq-path-reassessment.md) §4; attack spec
[`2026-07-17-three-front-attack-specs.md`](2026-07-17-three-front-attack-specs.md) §2) ·
**Branch:** `claude/lr-modulus-identification-2026-07-17` (PR #3822) ·
**No fit; no constant wired; the `loc_matches` gate is NOT closed.**

## Target

The keystone's last open piece (#3703 honest refocus): identify or refute

$$
|S_{0\lambda}^{\Sigma(2,3,5)}(\zeta)| \;=\; d_\zeta(\lambda)/D(\zeta),
\qquad d_q(\lambda) = [\mathrm{mark}(\lambda)]_q
$$

with the value map on the affine-$\widehat{E}_8$ McKay **marks** (= dims of the $2I$ irreps,
$1,2,3,4,5,6,4,2,3$; $\sum \mathrm{mark}^2 = 120 = |2I|$), exact per the merged #3685 route.

## Verdict — corrected exact identity (rubric outcome 2, a full win)

For every McKay node $\lambda$ and **both** flat connections $m = 1, 2$ of $\Sigma(2,3,5)$:

$$
\bigl|S_{0\lambda}^{(m)}\bigr| \;=\; \frac{2\,\bigl|[\mathrm{mark}\,\lambda]_{\zeta^m}\bigr|}{D_{\widehat{E}_8}(\zeta^m)}
\;=\; \frac{\sqrt{2}\; \bigl|d_{\zeta^m}(\lambda)\bigr|}{D_{\mathrm{MTC}}(\zeta^m)},
\qquad \zeta = e^{i\pi/5},
$$

exact in $\mathbb{Q}(\sqrt 5)$, with $D_{\widehat{E}_8}(\zeta^m)^2 = 10 \pm 2\sqrt 5$ and the core
identity $(10-2\sqrt5)(10+2\sqrt5) = 80$. The conjectured shape holds with three derived
corrections:

1. **$\zeta$ is the fibre root $e^{m\pi i/5}$** (order $2p_3 = 10$, the order-5-fibre holonomy
   scale), **Galois-indexed by the flat connection $m$** — NOT the level root $\zeta_N$ (the
   flat-connection amplitudes are $N$-independent constants, so an identity varying with
   $\zeta_N$ is impossible) and NOT $e^{2\pi i/30}$. The two flat connections are the two Galois
   embeddings $\zeta \mapsto \zeta^m$ — the standard CS/Galois pairing, here landed exactly.
2. **A global factor $2$** against the $\widehat{E}_8$-node normalizer (equivalently $\sqrt 2$
   against the folded-MTC normalizer): the 9-node affine-$\widehat{E}_8$ set folds **2:1** onto
   the $r=5$ alcove $\{1,2,3,4\}$ with node 5 → 0, so
   $D_{\widehat{E}_8}^2 = 2\,D_{\mathrm{MTC}}^2$ exactly ($10+2\sqrt5 = 2(5+\sqrt5)$).
3. **The identity lives at the folded $D=2$ level.** The color map
   $\alpha \mapsto \chi^{(1,1,\alpha)}$ (Hikami eq. 3.1) factors through the $r=5$ affine-Weyl
   fold with the **same kernel and signs** as $\alpha \mapsto [\alpha]_\zeta$ — computed exactly
   (integer tables, zero floats):

   | color α | character | quantum integer at $\zeta = e^{i\pi/5}$ |
   |---|---|---|
   | 4 | $\chi^{(1,1,4)} = +\chi^{(1,1,1)}$ | $[4]_\zeta = +[1]_\zeta = 1$ |
   | 3 | $\chi^{(1,1,3)} = +\chi^{(1,1,2)}$ | $[3]_\zeta = +[2]_\zeta = \varphi$ |
   | 5 | $\chi^{(1,1,5)} \equiv 0$ | $[5]_\zeta = 0$ |
   | 6 | $\chi^{(1,1,6)} = -\chi^{(1,1,1)}$ | $[6]_\zeta = -[1]_\zeta = -1$ |

## The pre-registered kill criteria, answered

- **The D=2 collapse** (the decisive structural trap named in the spec): the McKay-labelled
  coloring does **not** escape it — it factors through it, identically on both sides of the
  identity. The collapse is the fold. A "9 independent moduli at a single $\zeta$" reading is
  **(b)-excluded**: the invariant is $D(2,3,5) = (p_1{-}1)(p_2{-}1)(p_3{-}1)/4 = 2$ — exactly two
  irreducible flat SU(2) connections on $\Sigma(2,3,5)$ ([fintushelstern1990]; Hikami's
  $D$-formula machine-validated in-repo by `keystone_valuemap_genuine_smatrix_s013`). Any
  per-flat-connection amplitude family has at most 2 independent components.
- **α=1 anchor:** the colored Gauss sum at $\alpha = 1$ reproduces the bare $\tau_N$ and the
  exact Hikami Theorem-10 identity to ~1e-38.
- **Split node:** the electron block $(3,1,1)$ has $d_\zeta = [5]_\zeta + 1 = 1 = |[6]_\zeta|$ —
  the $S_5$-level value map ($[5]_q+1$, #3685) and the $2I$-node mark map ($[6]_q$) **agree in
  modulus** at the fibre root (sign differs: $[6]_\zeta = -1$; recorded, not interpreted). The
  muon class $(3,2)$ folds to $[5]_\zeta = 0$.
- **Conjugation-modulus:** $\lambda$ and $\lambda'$ share a mark ⇒ equal moduli, trivially
  satisfied; consistent with the #3703 framing-is-phase result.

## Validation chain (tiered, per the refute-honestly discipline)

| leg | tier | result |
|---|---|---|
| character fold tables; fold = $[\alpha]_\zeta$ fold (kernel + signs) | **exact** (integers + $\mathbb{Q}(\sqrt5)$) | pass |
| $D^2$ values, fold multiplicity $D_{\widehat{E}_8}^2 = 2 D_{\mathrm{MTC}}^2$, core $(10{-}2\sqrt5)(10{+}2\sqrt5)=80$, per-node modulus identity (9 nodes × 2 connections) | **exact** ($\mathbb{Q}(\sqrt5)$, `Fraction` arithmetic; 50-dps numeric cross-check) | pass |
| bare Theorem-10 anchor; $\tau_N(4)-\tau_N(1) = 1+2\cos(2\pi/N)$; $\tau_N(3)-\tau_N(2) = e^{-6\pi i/(5N)}$ (discovered, then verified at fresh $N$: 7, 11, 13, 25) | **machine-zero** (~1e-38) | pass |
| flat amplitudes $A_m(\alpha) = \pm(2/\sqrt5)\sin(\alpha m\pi/5)$, $\alpha \in \{1,2,3,4,6\}$, parameter-free 2×2 inversion + fresh-pair cross-check | numeric **evidence** (~1%) | pass |
| $\alpha=5$ flat-free; $\tau_N(6)+\tau_N(1)$ bounded after Cor-12 normalization | numeric evidence | pass |

The two elementary difference identities are a by-product finding: **the colored Gauss sum
depends on α beyond its fold class only through elementary trivial-connection-type terms** —
the flat-connection amplitudes (the only input to the modulus identification) depend on the
fold class alone.

Probe + witness: [`computations/lr_modulus_identification_sigma235.py`](../../computations/lr_modulus_identification_sigma235.py),
[`computations/lr-modulus-identification-sigma235.witness.json`](../../computations/lr-modulus-identification-sigma235.witness.json)
(1 assertion, all passed). Lean carrier (exact fold algebra, sorry-free):
[`KeystoneLRModulusFold.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/KeystoneLRModulusFold.lean).

## Per-node table

$|A_m| = (2/\sqrt5)|\sin(\mathrm{mark}\cdot m\pi/5)|$ (LR side, flat connection $m$);
RHS $= |[\mathrm{mark}]_{\zeta^m}|/D_{\widehat{E}_8}(\zeta^m)$; ratio $= 2$ exactly at every
nonzero entry (and $0 = 2\cdot 0$ at node 5):

| node (2I irrep) | mark | $\|A_1\|$ | $d/D(\zeta)$ | $\|A_2\|$ | $d/D(\zeta^2)$ |
|---|--:|--:|--:|--:|--:|
| triv | 1 | 0.5257 | 0.2629 | 0.8507 | 0.4253 |
| 2s | 2 | 0.8507 | 0.4253 | 0.5257 | 0.2629 |
| 3 | 3 | 0.8507 | 0.4253 | 0.5257 | 0.2629 |
| 4s | 4 | 0.5257 | 0.2629 | 0.8507 | 0.4253 |
| 5 | 5 | 0 | 0 | 0 | 0 |
| 6 | 6 | 0.5257 | 0.2629 | 0.8507 | 0.4253 |
| 4 | 4 | 0.5257 | 0.2629 | 0.8507 | 0.4253 |
| 2s′ | 2 | 0.8507 | 0.4253 | 0.5257 | 0.2629 |
| 3′ | 3 | 0.8507 | 0.4253 | 0.5257 | 0.2629 |

$S_5$-class view at $\zeta$: $\{(5),(1^5)\} \to 1$; $\{(4,1),\dots\} \to 1$;
$\{(3,2),\dots\} \to 0$; $\{(3,1,1)\} \to 1$ (split node; modulus $= |[6]_\zeta|$).

## What this does and does not close (anti-laundering)

- **Closed:** the modulus identification at the fibre roots — the deferred colored-LR compute
  named open by #3703/#3685 and the reassessment. The identity is exact, parameter-free, and
  Galois-equivariant; the previously refuted "bwS0 = vacuum row" reading (s013) is recovered as
  the correct statement *after* the fold with the factor-2 normalization.
- **Not closed:** the Lean `loc_matches` gate and the archimedean `q₀`-continuation. At the
  fibre root the 4 generic-$q$ Hecke classes collapse to the $D=2$ folded space (values
  $\{0, 1, \varphi\}$); the generic-$q$ separation of the 4 classes — the information the mass
  observable needs — lives in the continuation across roots (#3652/#3681), unchanged and open.
  The analytic input $A_m(\alpha) = \pm(2/\sqrt5)\sin(\alpha m \pi/5)$ is machine-validated
  evidence (~1% extraction + exact difference identities), not a Lean theorem; the Lean file
  carries only the exact fold algebra.
- **Scope of the (b) exclusion:** only the narrow reading "9 independent per-node moduli at a
  single root" — via the $D(2,3,5)=2$ invariant. Everything else negative here is (a)-scoped.

## Coordination

Sibling #3719 (cyclotomic-boundary mechanism fix) — no file overlap; this doc follows its
"marks = dims; coincidence of orders; product-of-cyclotomics ≠ boundary mechanism" framing and
makes no causal McKay-mechanism claim. Intent posted on #3719.
