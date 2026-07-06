# Muon knot-ID conflict — updated with S₅-theorem + Φ_q-probe evidence (2026-06-30)

**Branch**: `claude/formula-for-q-bzym14` · **PR**: [#3183](https://github.com/litlfred/qou/pull/3183)
**Supersedes the verdict of**: [`2026-05-24-muon-knot-id-conflict.md`](2026-05-24-muon-knot-id-conflict.md)
**Status**: **resolved on the identity question** (four-layer trace below) —
**muon = T(2,5); 4₁ = Higgs**, never the muon. The earlier "likely a typo,
muon = 4₁" conclusion is overturned. Two owner-gated *corpus fixes* and one
*open physics question* remain (see Determination + Recommendation).

## Determination (four-layer trace, 2026-06-30)

A layer-by-layer trace through the canonical chain
(categorical → algebraic → geometric → archimedean) resolves the
**identity** question. Every layer except one low-authority script agrees:

| Layer | Muon identity | 4₁'s role | Source (authority) |
|---|---|---|---|
| Categorical | **T(2,5)** ($\mathbb{Z}_5\!\hookrightarrow\!S_5$) | — | `prop:s5-equivariant-torus-knots` (theorem) |
| Algebraic | **T(2,5)** $=\sigma_1^5\in H_2$ | — | `lepton-meson-torus-knot-dictionary` (.lean + proof) |
| Geometric | T(2,5), $\mathrm{Vol}_{\mathrm{hyp}}=0$ | **Higgs**, $\mathrm{Vol}=2.03$ | `KnotRegistry.lean` (Lean primary source) |
| Archimedean | — | **Higgs**; $\mathrm{Vol}(4_1)$ = mass *scale* | `skein-mass-relation-proof` (says "$4_1$ = Higgs") |

**The verdict.** The muon's *identity* knot is **T(2,5)** at every layer that
assigns one. The figure-eight **$4_1$ is the Higgs** (mass mechanism) —
asserted by the Lean `KnotRegistry`, the `knot-particle-dictionary`, and the
Skein *proof* itself ("The Higgs field is identified with the figure-eight
knot $4_1$"). The "muon = $4_1$" reading was a **category error**: it confused
the muon's *identity* knot (T(2,5)) with the *Higgs* knot ($4_1$) whose volume
**gives** the muon its mass. The lone dissenter is
`computations/knot-volumes.py`, which labels $4_1$ `particle:"muon"` (while
self-noting "also Higgs") and $T(2,5)$ `particle:"w_boson"` — a low-authority
script, and the source of the whole conflict.

**Reinterpreting the Skein formula.** $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$
is therefore the **Higgs-coupling mass scale**, *not* the muon's own knot
volume. This is forced: the muon is a torus knot, so its algebraic quantum
volume $\mathrm{Vol}_q(T(2,5)) = 0$ (like the electron $3_1$); a torus-knot
lepton has **no intrinsic volume-mass** and acquires mass only by coupling to
the Higgs ($4_1$), the simplest hyperbolic knot.

**Consequence for the ξ_ℓ probes (Phase 4/5).** Those probes computed the
*leptons' own* per-braid towers and correctly found $O(1)$ — but that $O(1)$
is the lepton's **intrinsic** (non-Higgs) contribution, not its mass. The
$\sim10^2$ mass scale lives in the **Higgs ($4_1$) coupling**, a different
object. The Phase-4 two-constraint obstruction was predicated on the muon
mass being the muon's own $\mathrm{Vol}_q^{\mathrm{tower}}$; under this
resolution that premise is wrong, which **dissolves the obstruction** (it was
measuring the wrong quantity, not a real barrier).

**Still open (physics, not identity).** *Why* coupling to the Higgs ($4_1$)
yields exactly $\mathrm{Vol}(4_1)/\hbar_q^2$ for the muon, and how the
generation index $T(2,3)/T(2,5)/T(2,7)$ modulates that common coupling so that
$m_\tau \neq m_\mu$ (CODATA $m_\tau/m_e = 3477$, not $206.77$), is **not
derived**. The lepton-tower framing factor $q^{n}$ (writhe $n = 3,5,7$,
monotone in generation; `2026-06-02-lepton-t2n-torus-tower.md` §4) is the
natural candidate modulator but is unproven. This is the genuine forward
target, distinct from the now-resolved identity question.

## The standing conflict (recap)

Three corpus sources disagree on the muon's underlying knot:

| Source | Muon knot | Vol_hyp | Authority |
|---|---|---|---|
| `prop:skein-mass-relation` (+ proof) | $4_1$ figure-eight | $2.0299$ (**hyperbolic**) | published proposition |
| `computations/knot-volumes.py` | $5_1 = T(2,5)$ cinquefoil | $0$ (torus) | numerical script |
| S₅-equivariance / lepton T(2,n) tower | $T(2,5)$ | $0$ (torus) | **group-theoretic theorem** |

The 2026-05-24 audit concluded "most likely a labeling error in
`knot-volumes.py`; muon = $4_1$", on the authority of the published Skein
proposition and the fact that $\mathrm{Vol}(4_1)/\hbar_q^2 \approx 206.77$
matches CODATA.

## Why that verdict no longer holds — two pieces of newer evidence

### 1. The S₅-equivariance theorem (2026-06-02, post-dates the verdict)

[`2026-06-02-lepton-t2n-torus-tower.md`](2026-06-02-lepton-t2n-torus-tower.md)
(PR #1682) establishes — as a **group-theoretic theorem, not a numerical
match** — that the charged leptons are the odd-$n$ torus tower
$T(2,n)$ with $\mathbb{Z}_n \hookrightarrow S_5 = \mathrm{Aut}(\Sigma_4)$.
$S_5$ has element orders $\{1,2,3,4,5,6\}$, so the admissible odd $n \ge 3$
are exactly $\{3,5\}$ = (electron, muon). This **derives** muon $= T(2,5)$
from the Bring-surface symmetry, and is reproduced by
`prop:s5-equivariant-torus-knots`. It is the cleanest derived result in
the lepton sector. It favours $T(2,5)$, and it did not exist when the
2026-05-24 "typo" verdict was written.

### 2. The Φ_q probe (2026-06-30, this PR)

[`xi_ell_phi_q_probe.py`](../../computations/xi_ell_phi_q_probe.py)
(`xi-ell-faddeev-phi-q-probe.witness.json`) evaluates the per-braid mass
tower with the proper Plancherel-weighted Wedderburn $\hat V_i$ under five
dilog normalizations. The two muon candidates behave **qualitatively
oppositely** under *every* one:

| muon candidate | $\hat V$ | (a) Li₂^q | (b) Φ_q | (d) Φ_q($\hat V/q_0$) |
|---|---:|---:|---:|---:|
| $4_1$ | $1.009$ | $6.34$ | $116{,}611$ | $13{,}042$ |
| $T(2,5)$ | $0.543$ | $1.64$ | $13.99$ | $9.98$ |

(CODATA $m_\mu/m_e = 206.77$.) The figure-eight's $\hat V \approx 1.009$
sits essentially **on** the $\Phi_q$ convergence radius $q_0 = 1.110$, so
$4_1$ **overshoots** under any $\Phi_q$ form; $T(2,5)$ stays well inside
and **undershoots**. Neither closes — but the spread between them is
$\sim 8000\times$, so the muon knot choice is now **numerically
decisive**, not a cosmetic label.

## The conflict is structural, not a typo — two internally-coherent pictures

- **(A) $4_1$, archimedean / Kashaev face.** The hyperbolic
  $\mathrm{Vol}(4_1)$ makes the Skein LO match CODATA exactly, and the
  Skein relation is a *published proposition*. **But**: it breaks the
  uniform torus tower (why is only the muon hyperbolic while
  $e = T(2,3)$ and $\tau = T(2,7)$ are torus, $\mathrm{Vol}_{\mathrm{hyp}} = 0$?),
  and `knot-volumes.py` independently labels $4_1$ the **Higgs**.

- **(B) $T(2,5)$, categorical / S₅ face.** A uniform $T(2,2k+1)$ tower,
  group-theoretically selected, with fermion statistics via
  $\gcd(2,n) = 1$. **But**: $\mathrm{Vol}_{\mathrm{hyp}}(T(2,5)) = 0$, so
  the Skein formula's $\mathrm{Vol}(4_1)$ is "borrowed" from a different
  knot, making the CODATA match look like a coincidence under this
  picture.

These are not reconcilable by relabeling: (A) needs a hyperbolic muon,
(B) needs a torus muon.

## Candidate resolution (hypothesis — owner call)

The original audit's **option (iii)** (both, at different levels) is the
only candidate consistent with all evidence, and it parallels the
**fibre-vs-observable two-level convention** in AGENTS.md (Im(q) at the
fibre vs the observable):

- muon $= T(2,5)$ at the **categorical / pre-τ** level (the S₅ braid,
  quantum numbers, generation index $\mathbb{Z}_5$);
- the mass *magnitude* enters at the **archimedean / Kashaev** level,
  where the $\mathrm{Vol}(4_1)$ in the Skein LO is the hyperbolic-limit
  scale.

This is a **hypothesis**, not a closure: it requires a knot-theoretic
reason the $T(2,5)$ categorical object's archimedean shadow carries the
$4_1$ volume (no elementary $T(2,5) \leftrightarrow 4_1$ relation is
known), which is unproven. The Φ_q probe does **not** select between (A)
and (B) — both fail to close, oppositely.

## Recommendation (no unilateral edits)

This conflict touches a **published proposition** (`prop:skein-mass-relation`)
and the **particle dictionary** (`knot-volumes.py`) — both owner-gated. No
files are changed by this audit. Requested owner ruling:

1. Is the canonical muon knot $4_1$ (Skein/archimedean) or $T(2,5)$
   (S₅/categorical), or the two-level split above?
2. If two-level: the Skein proposition and the S₅ tower need an explicit
   bridge note so neither reads as the sole identification.
3. If $T(2,5)$ supersedes: `prop:skein-mass-relation` needs a framing
   note that $\mathrm{Vol}(4_1)$ is the archimedean *scale*, not the muon
   knot's own volume.

Until then, the lepton ξ_ℓ work
([`lepton-mass-tower-canonical.md`](../../content/quantum-observable-universe/mass-theory/lepton-mass-tower-canonical.md)
§"compact q-dilog Φ_q probe") treats the muon knot as **unresolved and gating**.

## Cross-references

- Prior audit: [`2026-05-24-muon-knot-id-conflict.md`](2026-05-24-muon-knot-id-conflict.md)
- S₅ theorem: [`2026-06-02-lepton-t2n-torus-tower.md`](2026-06-02-lepton-t2n-torus-tower.md)
- Φ_q probe: [`xi_ell_phi_q_probe.py`](../../computations/xi_ell_phi_q_probe.py)
- Conjecture doc: [`lepton-mass-tower-canonical.md`](../../content/quantum-observable-universe/mass-theory/lepton-mass-tower-canonical.md)
