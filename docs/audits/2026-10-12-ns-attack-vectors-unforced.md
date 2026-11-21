# Attack vectors on the unforced Navier–Stokes problem: literature handles mapped to QOU

**Date:** 2026-10-12. **Bean:** `qou-0ueg` (owner question: *"can we reformulate any of QOU to help with a topological obstruction? Any open attack vectors? Any hints in the literature?"*).
**Branch:** `ns-attack`, based on `claude/bold-gates-00l1bl` at `cb8195cb9`.
**Scope:** a read-only survey. No content block, `.lean` file or witness was edited.

**Setting.** The problem is unforced incompressible 3D NS, $\partial_tu+(u\cdot\nabla)u=\nu\Delta u-\nabla p$, $\nabla\cdot u=0$, $f\equiv0$, with smooth data. This is Fefferman's alternative (A) on $\mathbb R^3$ (Schwartz-class data) and (B) on $\mathbb T^3$, as now stated in `fluid-dynamics/ns-obstruction.md`.

**Inputs, cited and not re-derived:**
- [`2026-10-12-ns-chain-after-item3-retraction.md`](2026-10-12-ns-chain-after-item3-retraction.md), "chain audit".
- [`2026-10-12-ns-rescue-reformulations.md`](2026-10-12-ns-rescue-reformulations.md), "rescue audit". It shows:
  - there is no honest topological rescue on Bring;
  - the model's Reeb field on $UT(\Sigma_4)$ is Beltrami, so $e^{-\nu t}V$ is an exact global NS solution;
  - NS on a closed 2-surface is globally regular;
  - $\mathcal S$ is used both as a surface and as a contact 3-manifold;
  - the computation and the Levi chain take opposite branches on Levi degeneration.

**Tags.**
- **[D]** derived here.
- **[S]** standard and cited. A citation verified this session against a bibliographic or abstract record is marked ✓.
- **[N]** numerical observation, not a theorem.
- **[H]** heuristic.
- **[A]** asserted in the corpus with no derivation.
- **[O]** open.

**Library check (corpus-grep path 5) [D].** I grepped `library/INDEX.md`, `library/*/sections/` and `library/*/ocr/` (736 directories).
- **Absent:** every NS-regularity source. There are zero hits for Navier–Stokes, Beale–Kato–Majda, Constantin–Fefferman, Beirão da Veiga, Elgindi, Chen–Hou, or Tao's averaged NS.
- **Held, fluid-topology only:**
  - `candetgl` (Cantarella–DeTurck–Gluck, Biot–Savart);
  - `helicity03mmj` (higher helicities);
  - `procrsoclondona92` (Moffatt–Ricca, helicity and the Călugăreanu invariant);
  - `arxiv-0808.1533v3` (third-order helicity);
  - `deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-lin`;
  - `arxiv-physics-0203048v1` (third-order link integral).
- **In `folio/schema/references.ts` but not in the library:** `beale-kato-majda1984`, `moffatt1969`, `moffatt1994`, `necas-ruzicka-sverak1996`, `tsai1998`, `cardona2021`, `tao2019`.
- Corpus paths 1–3 and 6 return nothing for "Constantin", "direction of vorticity", "Enciso", "Elgindi" or "Chen–Hou", apart from this bean. The one hit for "geometric depletion" is `2026-07-25-qns-surreal-bridge-campaign-ledger.md:138`, which names it as a full-NS mechanism that no shell model captures.
- `corpus_search` (MCP) was unavailable because the server connection closed. So this is a grep-only negative, and it does not rule out vocabulary-shifted prior work.

---

## 0. Verdict

1. **No topological obstruction can come from the domain** [D]; scope (b). The invariants are the following.
   - $\mathbb R^3$ is contractible. $T\mathbb T^3$ is trivial, and so is $T\mathbb R^3$.
   - Every characteristic class of the domain's tangent bundle or frame bundle therefore vanishes.
   - A constant field is a nowhere-zero, divergence-free, smooth global solution.

   This is the $\mathbb R^3/\mathbb T^3$ version of the rescue audit's Bring result. Any obstruction must therefore be **dynamical**: a statement about the evolving fields $u$ and $\omega$, not about the space they live on.
2. **Topology change of vortex lines cannot obstruct NS either** [S ✓]. Enciso–Lucà–Peralta-Salas, *Adv. Math.* 309 (2017) 452–486, construct smooth NS solutions in which vortex lines and tubes of arbitrary knot and link type are created and destroyed in arbitrarily short time, with the solution smooth throughout. In smooth **Euler**, topology is frozen (§2, H5), so "reconnection ⇒ singularity" is a true implication **for Euler only**.
3. **The geometric literature points the other way from the corpus's chosen branch.** The sharpest known geometric handle is Constantin–Fefferman together with Beirão da Veiga–Berselli. It says that **regularity** of the vorticity *direction* in high-vorticity regions **prevents** blow-up. So blow-up forces direction geometry to *degenerate*. The corpus's `levi-degeneracy-conjecture` (A) pairs *bounded* Levi geometry with *blow-up*. Under the only identification of "Levi form" with a flow-dependent object that I can make honestly (§3, V1), this pairing is in tension with C–F. It is not a contradiction outright, because the corpus's quantity is a scale-free condition number (§3).
4. **The corpus's chosen scenario is the least favourable one in the literature.** The anti-parallel vortex pair (Kerr 1993) has the following record:
   - it is the scenario C–F's line-field formulation treats as *depleting*: anti-parallel means $\sin\angle=0$;
   - Hou–Li 2006 re-ran Kerr's data and found no blow-up [N];
   - Moffatt–Kimura's reconnection model of blow-up (2019) was not reproduced by the DNS of Yao–Hussain (2020) [N];
   - the corpus's own `crow-approach-amplification` finds the linear 3D amplification bounded.
5. **Two vectors are honest and non-vacuous.** Both need a framework change: the flow-dependent fields must live on $\mathbb R^3/\mathbb T^3$, not on a fixed Boothby–Wang form.
   - **V1** recasts the Levi conjecture as a geometric-depletion statement about the vorticity plane field $\omega^\perp$.
   - **V2** is a vortex-tube knot invariant that is frozen under smooth Euler and discriminates Euler from NS.

   Neither gives an NS obstruction. V1 gives a correctly signed *necessary condition* for blow-up. V2 gives an *Euler*-singularity criterion (the inviscid limit).

---

## 1. Literature survey

| # | Handle | Precise statement | Setting | Status |
|---|---|---|---|---|
| L1 | **Beale–Kato–Majda** (CMP 94, 1984; `beale-kato-majda1984`) | A smooth solution on $[0,T^*)$ extends past $T^*$ iff $\int_0^{T^*}\lVert\omega\rVert_{L^\infty}dt<\infty$. | Euler; the same criterion holds for NS, unforced, $\mathbb R^3$ and $\mathbb T^3$ | theorem [S] |
| L2 | **Leray / Escauriaza–Seregin–Šverák / Seregin** | Blow-up at $T^*$ forces $\lVert u(t)\rVert_{L^p}\ge c_p(T^*-t)^{-(p-3)/2p}$ for $p>3$ (Leray 1934). ESS (Russ. Math. Surveys 2003) show $u\in L^\infty_tL^3_x$ ⇒ regular. Seregin (CMP 2012) shows $\lVert u(t)\rVert_{L^3}\to\infty$ at blow-up. | NS, $\mathbb R^3$ | theorems [S] |
| L3 | **CKN** (CPAM 1982) | Suitable weak solutions have a singular set of 1-dimensional parabolic Hausdorff measure zero. | NS | theorem [S] |
| L4 | **Constantin–Fefferman** (IUMJ 42 (1993) 775–789) ✓ | Let $\xi=\omega/\lvert\omega\rvert$. Suppose there are $\Omega,\rho$ with $\lvert\sin\angle(\xi(x,t),\xi(y,t))\rvert\le\lvert x-y\rvert/\rho$ whenever $\lvert\omega(x,t)\rvert,\lvert\omega(y,t)\rvert>\Omega$. Then the solution is smooth on $[0,T]$. | NS, $\mathbb R^3$, unforced | theorem [S ✓] |
| L5 | **Beirão da Veiga–Berselli** (Diff. Int. Eq. 15 (2002)) ✓ | The same conclusion holds with $\lvert\sin\angle\rvert\le C\lvert x-y\rvert^{1/2}$. The exponent ½ is described as hard to improve; boundary versions also exist. | NS, $\mathbb R^3$ | theorem [S ✓] |
| L6 | **Constantin's stretching formula** (SIAM Rev. 1994) | $\alpha=\xi\cdot S\xi=\tfrac{3}{4\pi}\,\mathrm{P.V.}\!\int D(\hat y,\xi(x+y),\xi(x))\,\lvert\omega(x+y)\rvert\,\lvert y\rvert^{-3}dy$, where $D$ vanishes when $\xi(x+y)\parallel\pm\xi(x)$. This is the mechanism behind L4 and L5. | Euler and NS | identity [S] |
| L7 | **Deng–Hou–Yu** (CPDE 2005) ✓ | Lagrangian geometric conditions along a vortex-line segment (curvature, $\nabla\cdot\xi$, length) exclude Euler blow-up. Uses $\partial_s\lvert\omega\rvert=-(\nabla\cdot\xi)\lvert\omega\rvert$ along lines. Applied to Kerr's data. | Euler | theorem [S ✓] |
| L8 | **Grujić et al., sparseness** (Bradshaw–Farhat–Grujić, arXiv 1704.05546) ✓ | Sparseness of vorticity super-level sets reduces the "scaling gap" algebraically. Albritton–Bradshaw (arXiv 2110.02187) give a simpler proof and argue the gap closes only *inside* the sparseness framework. | NS | theorem plus a disputed interpretation [S ✓] |
| L9 | **KNSS / CSTY** | Type-I blow-up ($\lvert u\rvert\le C(T^*-t)^{-1/2}$) is excluded for **axisymmetric** NS. References: Koch–Nadirashvili–Seregin–Šverák (Acta Math. 203, 2009); Chen–Strain–Tsai–Yau (2008/09). | NS, axisymmetric | theorem [S, not re-verified here] |
| L10 | **Leray self-similar** (`necas-ruzicka-sverak1996`, `tsai1998`) | Backward self-similar $L^3$ or local-energy profiles are trivial. Discretely self-similar blow-up is **not** excluded. | NS | theorem [S] |
| L11 | **Helicity** (`moffatt1969`, `moffatt1994`; Arnold 1974) | $H=\int u\cdot\omega$ is conserved by smooth Euler and equals the linking invariant for thin tubes. For NS, $dH/dt=-2\nu\int\omega\cdot\mathrm{curl}\,\omega$. | Euler (conserved); NS (dissipated, sign-indefinite) | theorem [S] |
| L12 | **Helicity uniqueness** (Enciso–Peralta-Salas–Torres de Lizaur, PNAS 113 (2016) 2035–2040) ✓ | Helicity is the only regular *integral* invariant of volume-preserving diffeomorphisms. | kinematic | theorem [S ✓] |
| L13 | **Kelvin/Helmholtz/Cauchy** | For $C^1$ Euler, $\omega(t)=(D\phi_t\,\omega_0)\circ\phi_t^{-1}$. Vortex lines are transported by the flow diffeomorphism, so the isotopy class of any vortex-line link is invariant. | Euler | theorem [S] |
| L14 | **Viscous reconnection** (Enciso–Lucà–Peralta-Salas 2017) ✓ | Smooth NS solutions change vortex-line and vortex-tube topology arbitrarily, structurally stably and in arbitrarily small time; also for small $\nu$ and large data. | NS, unforced | theorem [S ✓] |
| L15 | **Knotted steady structures** (Enciso–Peralta-Salas, Ann. 175 (2012) 345–367; Acta 214 (2015) 61–134) ✓ | Every locally finite link is realised, up to a $C^r$-small diffeomorphism, by vortex lines of a steady Euler field on $\mathbb R^3$. Thin knotted tubes are realised as vortex tubes of a decaying Beltrami field, carrying KAM tori and so structurally stable. | steady Euler | theorems [S ✓] |
| L16 | **Etnyre–Ghrist** (Nonlinearity 13 (2000) 441–458) ✓ | Rotational Beltrami fields are exactly Reeb fields of contact forms, up to rescaling. | steady Euler | theorem [S ✓] |
| L17 | **CMPP** (`cardona2021`: PNAS 2021; IMRN 2022) | Turing-complete steady Euler flows, i.e. Reeb fields of constructed contact forms and metrics on $S^3$ and $\mathbb R^3$. They give undecidability of orbit questions, not singularity. | steady Euler | theorem [S] |
| L18 | **Tao, averaged NS** (JAMS 29 (2016) 601–674) ✓ | An averaged nonlinearity that keeps the energy identity, the scaling and the standard harmonic-analysis estimates admits smooth finite-time blow-up. *Barrier:* a regularity proof must use finer structure of the true nonlinearity than the energy identity and those estimates. Tao also proposes a program toward true NS: a self-replicating "fluid computer" in Euler/NS, plus `tao2019` universality. | modified NS, $\mathbb R^3$ | theorem (for the model) [S ✓]; program [H] |
| L19 | **Elgindi** (Ann. 194 (2021) 647–727) ✓ | Finite-time singularity for $C^{1,\alpha}$ (not $C^\infty$) axisymmetric-without-swirl Euler on $\mathbb R^3$, with finite energy. | Euler, low regularity | theorem [S ✓] |
| L20 | **Chen–Hou** (arXiv 2210.07191 and 2305.05660; SIAM 2025) ✓ | Computer-assisted proof of stable, nearly self-similar blow-up for 2D Boussinesq and for **3D axisymmetric Euler with smooth data in a domain with boundary** (Luo–Hou scenario). | Euler with boundary | theorem (computer-assisted) [S ✓] |
| L21 | **Hou** (FoCM 2022, arXiv 2107.06509) ✓ | Potential singularity of axisymmetric NS from smooth data: about $10^7$ vorticity growth, nearly self-similar. **No proof.** NS remains open. | NS | [N] |
| L22 | **Kerr anti-parallel** (Phys. Fluids A 5 (1993)) versus Hou–Li (J. Nonlinear Sci. 2006) ✓ | Kerr reported $\lVert\omega\rVert_\infty\sim(T-t)^{-1}$ for perturbed anti-parallel Euler tubes. Hou–Li, from Kerr's data at higher resolution, found at most doubly-exponential growth past Kerr's $T$, with no blow-up. | Euler | [N], contested |
| L23 | **Moffatt–Kimura** (JFM 861, 870, 2019; Part 3 JFM 967, 2023) ✓ | A reduced Biot–Savart model of reconnecting vortex rings, suggesting very large amplification near $Re_\Gamma\approx4000$. The DNS of Yao–Hussain (2020) found much smaller amplification. | NS | [H]/[N] |
| L24 | **Wang–Lai–Gómez-Serrano–Buckmaster et al.** (arXiv 2509.14185) ✓ | Machine-learned unstable self-similar profiles (IPM, Boussinesq, CCF) at near machine precision. Proposed as input to future computer-assisted proofs. | Euler-type, boundary | [N] |
| L25 | **Ladyzhenskaya / Wolibner; small data; 2½-D** | Global regularity holds in 2D (any closed surface), for small data in critical spaces (Fujita–Kato; Koch–Tataru), and for axisymmetric flow without swirl. | NS | theorems [S] |

**Explicit "topological obstruction to global regularity" claims [D, survey].**
- I found none for NS in the theorem-grade literature.
- The true topological statements all point the other way, or they apply to Euler only:
  - L13 is a topological *invariance* for smooth Euler;
  - L14 shows NS violates that invariance *smoothly*;
  - L16 and L17 concern *steady* flows.
- The barrier for spaces is §0 item 1. The barrier for methods is L18: any criterion that uses only energy, scaling and Fourier-side estimates cannot decide the question, and topology enters only through *which* structure of the nonlinearity it encodes.
- Whether Tao's averaged nonlinearity preserves a vorticity transport law, Kelvin circulation or helicity was **not verified this session**. WebFetch was DNS-blocked, and the abstract is silent. This matters for ranking V2 and V3 and is flagged [O].

---

## 2. Mapping to corpus objects

| Handle | Corpus object it would attach to | Does a reformulation give a true, non-vacuous statement? |
|---|---|---|
| L1 BKM | `q-bkm-criterion.md` (the $q>1$ version; trivially finite there) and `vorticity-lower-bound.md` | Already used. The classical L1 is a theorem. The corpus's (b)/(c) assert a **rate** $\lVert\omega^*\rVert_\infty\ge c_1/(T^*-t)$ for a *weak limit* $v^*$ of q-NS. That rate is [A]: no derivation exists, and the existence of $T^*<\infty$ is assumed. Nothing new. |
| L4/L5 C–F direction | `core-levi-form.md` and `levi-degeneracy-conjecture.md` | **Yes, via V1**, but only after replacing the fixed $\ker\varTheta$ by the flow plane field $\eta_\omega=\omega^\perp$. Identity D1 below makes "Levi form of $\eta_\omega$" a function of $\nabla\xi$. |
| L6/L7 stretching geometry | `townsend-biot-savart-strain.md`, `crow-approach-amplification.md` | These blocks model the strain $\alpha=1/(2(T^*-t))$ **as an input** [A]. L6 says $\alpha$ is determined by $\xi$-geometry, so the model's assumed strain is exactly the quantity C–F controls. |
| L11/L12 helicity | `helicity-conservation.md`, `helicity-physical.md` | Partly. Classical helicity conservation for smooth Euler is true (L11). Several items need care: |
| | | – The $q$-helicity "conservation by the quantum Euler equation" and its discrete-lattice quantisation are [A]. |
| | | – The "Jones refinement" formula $J_L=\exp(\sum\frac1n\mathrm{tr}\check R^n(q-q^{-1})^n)$ is [A] and is not an integral invariant of the flow. L12 forbids any *integral* invariant other than helicity, so a Jones-type quantity must be an invariant of a *selected sub-object* (a tube link), which is V2. |
| | | – The block's claim that classical helicity "assigns zero to … the trefoil" is **framing-dependent**, not a property of the knot type: a single tube's helicity is $\Phi^2(\mathrm{Wr}+\mathrm{Tw})$, the framing number times flux squared (Călugăreanu; Moffatt–Ricca, held in `procrsoclondona92`). It is zero only for a zero-framed tube, which is equally available to the unknot and the trefoil. Flagged, not edited. |
| L13/L14 topology frozen vs reconnection | `braid-fluid.md`, `vortex-reconnection.md` (Hecke eigenvalue $-q^{-1}$ = reconnection), `helicity-physical.md` ("smooth evolution cannot alter…") | **Yes for Euler, via V2.** For NS, L14 contradicts any claim that smooth evolution preserves vortex topology. `vortex-reconnection.md`'s "quantum pressure regularises the classical reconnection singularity" presupposes a classical NS reconnection singularity. L14 shows NS reconnection can be smooth, so that premise is [A] and likely misframed. |
| L16 Etnyre–Ghrist | the Reeb field (`mass-theory/reeb-bundle.md`) | Already transferred exactly (rescue audit §5). It gives a **regular** NS solution. |
| L17/L18 universality, Tao program | `q-metric-contact-deformation.md` ("Turing-complete Reeb flow", [A]); the Hecke/braid "gate" picture | V4 only: [H], aimed at **blow-up**, and requires a construction absent from the corpus. |
| L18 barrier | `regularity-breakdown.md`'s three obstructions | **Adversarial [D].** All three are energy-, spectrum- or scaling-level heuristics: loss of spectral gap, $\nu_q\to0$, continuous cascade. Tao's averaged NS shares the energy identity and scaling. So these obstructions cannot distinguish true NS from a model that does blow up, and they cannot prove blow-up of true NS either: Tao's model, not NS, is what they describe. As *evidence* they are therefore uninformative in both directions. |
| L19–L21 Euler/NS blow-up numerics | `leray-profile.md` (discrete self-similarity) | L10 leaves backward discrete self-similarity open [S]. Chen–Hou's profile is *nearly* self-similar with boundary. A corpus DSS profile on $\mathbb R^3$ without boundary would need its own construction [O]. The corpus's period "set by the root-of-unity scaling $\lambda_\kappa$" is [A]. |
| L22/L23 anti-parallel and reconnection | `vorticity-lower-bound.md`, `townsend-biot-savart-strain.md`, `crow-approach-amplification.md`, collision locus $\Sigma$ | §0 item 4: this is the most-studied scenario and has **no** established blow-up. |

**Derived identities used above [D].** Each is checkable in a few lines.

- **D1.** For a smooth vector field $w$ on a Riemannian 3-manifold, write $w^\flat$ for its metric dual. Then $w^\flat\wedge dw^\flat=(w\cdot\mathrm{curl}\,w)\,\mathrm{vol}$. Hence the plane field $\ker w^\flat$ (where $w\ne0$) is contact at $x$ iff $w\cdot\mathrm{curl}\,w(x)\ne0$. (This is the identity underlying Etnyre–Ghrist.)
  - For $w=u$, contactness of $\ker u^\flat$ is non-vanishing helicity *density*. That condition is not Galilean-invariant on $\mathbb R^3$, since $u\mapsto u+c$ shifts $u\cdot\omega$ by $c\cdot\omega$.
  - For $w=\omega$ it is $\omega\cdot\mathrm{curl}\,\omega\ne0$, which is Galilean-invariant.
- **D2.** Write $\omega=f\xi$ with $f=\lvert\omega\rvert$ and $\lvert\xi\rvert=1$. Then $\mathrm{curl}\,\omega=f\,\mathrm{curl}\,\xi+\nabla f\times\xi$, so $\omega\cdot\mathrm{curl}\,\omega=f^2\,(\xi\cdot\mathrm{curl}\,\xi)$.
  - The twisting of the vorticity plane field $\eta_\omega=\omega^\perp$ is therefore governed purely by the **abnormality** $\tau:=\xi\cdot\mathrm{curl}\,\xi$ of the direction field, and $\lvert\tau\rvert\le\sqrt2\,\lvert\nabla\xi\rvert$.
  - So C–F Lipschitz control of $\xi$ in $\{\lvert\omega\rvert>\Omega\}$ bounds $\tau$ there. The converse fails: bending and splay are not seen by $\tau$, and D–H–Y's $\nabla\cdot\xi$ is one of them.
- **D3.** Euler with $u\in C^1([0,T]\times\mathbb T^3)$ preserves, for every time, the isotopy class of each invariant vortex tube (L13). This is a direct corollary of Cauchy's formula. It fails for NS by L14.

---

## 3. Ranked attack vectors

Ranking: (i) soundness, (ii) connection to existing corpus machinery, (iii) feasibility.

| Rank | Vector | (i) | (ii) | (iii) | Framework change needed? |
|---|---|---|---|---|---|
| 1 | **V1** Geometric-depletion recast of the Levi chain (vorticity plane field $\eta_\omega$) | high (rests on L4/L5 theorems) | high (`core-levi-form`, `levi-degeneracy-conjecture`, Townsend/Crow blocks) | high for the reformulation; the underlying question is the open Clay problem | **yes**: the Levi form must be of a flow-dependent plane field on $\mathbb R^3/\mathbb T^3$, not of fixed $\ker\varTheta$ on a Boothby–Wang manifold |
| 2 | **V2** Hecke/Jones invariant of knotted vortex tubes: frozen by smooth Euler, broken smoothly by NS | high (L13, L14, L15) | high (`braid-fluid`, `vortex-reconnection`, Markov trace) | medium; well-posed only on the structurally stable tubes of L15 | **yes**: replace the "categorical helicity" [A] with an invariant of a selected tube link |
| 3 | **V3** Helicity/Beltrami depletion: contactness of $\ker u^\flat$ as a regularity mechanism | low–medium: the Lamb-vector depletion $u\times\omega\to0$ is [H]/[N], and no helicity-only criterion is known | medium (Reeb/Beltrami, helicity blocks) | medium for probes, low for theorems | **yes**: same as V1, and it points toward **regularity** |
| 4 | **V4** Tao/CMPP universality: the braid/Hecke "gate" as a fluid computer that self-replicates | low ([H]) | low–medium | very low | **yes**, and a construction the corpus does not have |
| — | Domain topology, Kummer/Euler classes, 2D readings | — | — | — | **excluded**, scope (b): §0 item 1, the rescue audit, and L25 |

### V1: a geometric-depletion formulation of the Levi conjecture [top]

**Object.** For an NS solution on $\mathbb R^3$ or $\mathbb T^3$:
- $\xi=\omega/\lvert\omega\rvert$ on $\{\omega\ne0\}$, the unoriented line field $\ell=[\xi]$;
- its plane field $\eta_\omega=\omega^\perp$;
- the "Levi data" of $\eta_\omega$: the abnormality $\tau=\xi\cdot\mathrm{curl}\,\xi$ (D2), and the full $\nabla\xi$ restricted to $\eta_\omega$, i.e. the second fundamental form of the plane field.

The model must **define** these as the objects its Levi form refers to. The current `core-levi-form.md` uses $\ker\varTheta$ on $(\mathcal S,\varTheta)$, which is not flow-dependent and lives in a space of the wrong dimension (rescue audit §1a).

**True statement, derived from cited theorems [S]+[D].** If a smooth unforced NS solution on $\mathbb R^3$ blows up at $T^*$, then for every $\Omega>0$ and $C>0$ there exist $t<T^*$ and $x,y$ with $\lvert\omega(x,t)\rvert,\lvert\omega(y,t)\rvert>\Omega$ and $\lvert\sin\angle(\xi(x,t),\xi(y,t))\rvert>C\lvert x-y\rvert^{1/2}$.

This is the contrapositive of L5. In words: **blow-up forces the vorticity line field to lose ½-Hölder control on the high-vorticity set.** It is a *degeneration* of direction geometry, the geometric content of the corpus's branch (B), with the **opposite** regularity verdict to the one (B) records. That is a correctly signed necessary condition, and it is non-vacuous: it fails for every regular solution with Lipschitz $\xi$, for example Burgers vortices and the Beltrami/Reeb solution.

**Proposed conjecture (replacing the A/B/C trichotomy) [O].** Let $\mathcal C(t)=\Omega(t)^{-1/2}\sup\{\lvert\nabla\xi(x,t)\rvert:\lvert\omega(x,t)\rvert>\Omega(t)\}$, a scale-normalised direction gradient with $\Omega(t)=\tfrac12\lVert\omega(t)\rVert_\infty$.
- *Necessary for blow-up* (from L4/L5 and parabolic scaling; to be checked [O]): $\limsup_{t\to T^*}\mathcal C(t)=\infty$.
- *Open question in the corpus's terms*: does the anti-parallel family realise $\mathcal C\to\infty$? Crow bending gives curvature $\sim1/\lambda$. Core twist gives $\tau$.

This replaces the corpus's scale-free condition number with a **scaled** quantity. A condition number, being a ratio of Levi eigenvalues, cannot be compared with C–F at all, because C–F's hypothesis carries a length scale $\rho$.

**What is known.**
- L4 and L5 are theorems, together with their bounded-domain versions.
- The anti-parallel line field is depleted at leading order: anti-parallel gives $\sin\angle=0$.
- Any blow-up in that scenario must come from *bending or twisting* of the tubes on the core scale, not from the anti-parallel geometry itself. This agrees with the corpus's own Crow block, whose verdict is bounded linear amplification.

**What is missing.**
1. A definition in the corpus of $\eta_\omega$ for the classical flow.
2. A reconciliation of `levi-degeneracy-conjecture` (A) "bounded Levi ⇒ blow-up" with L5. Under V1 it must be withdrawn or re-scoped, because bounded direction geometry implies regularity.
3. Resolution of the sign conflict of rescue audit §1b, which V1 resolves in favour of "degeneration is necessary for blow-up".

**First concrete steps.**
- (a) **Probe**, cheap, mpmath. Evaluate $\tau$, $\lvert\nabla\xi\rvert$ and $\mathcal C$ on the exact smooth solutions the corpus already uses: the Burgers vortex, the Lamb–Oseen pair, and the Townsend sheet of `townsend-biot-savart-strain.md`. This calibrates which corpus scenarios are C–F-depleted.
- (b) **Lean.** D1 and D2 are pointwise vector identities. With $\omega=f\xi$ and $\mathrm{curl}\,\omega=f C+g\times\xi$, they reduce to $\langle f\xi,\,fC+g\times\xi\rangle=f^2\langle\xi,C\rangle$ over a generic `CommRing R` using Mathlib `crossProduct`. That is feasible and sorry-free in about 20 lines. Formalising C–F itself is **not** feasible in Mathlib today. If wanted, it can be stated only as a `-- Ref:`-cited hypothesis class, which per AGENTS.md §3b-cond proves the implication and never the premise.
- (c) **Owner decision** (§4) on whether to re-scope the Levi blocks.

### V2: a knotted-tube invariant that discriminates Euler from NS

**Object.**
- A finite family of structurally stable vortex tubes $T_1,\dots,T_k$, each bounded by an invariant KAM torus of $\omega(t)$, as in L15 (Enciso–Peralta-Salas, Acta 2015).
- Their isotopy class $[\sqcup T_i]$.
- Any link invariant $I$ of it. The corpus's Markov trace $J_L(q)=\mathrm{tr}_M(\rho(\beta_L))$ evaluated on a braid presentation is one choice.

**True statement [D from L13; S].** If $u$ is a $C^1$ Euler solution on $[0,T]$ and the tubes persist, then $I([\sqcup T_i(t)])$ is constant.
- *Contrapositive:* a change of $I$ along an Euler evolution forces loss of $C^1$, which is an **Euler singularity**.
- *For NS* the statement is false: L14 changes topology smoothly. The honest corpus content is therefore:
  - an Euler-singularity criterion;
  - an inviscid-limit diagnostic: if $\nu\to0$ NS solutions reconnect in time $O(1)$, then the limit is not a $C^1$ Euler solution on that interval.

This is non-vacuous, falsifiable, and uses the braid/Hecke machinery directly.

**What is known.**
- L13–L15 are established.
- The `vortex-reconnection.md` table, assigning pass-through to $q$ and reconnection to $-q^{-1}$, is [A]. No derivation connects the Hecke eigenvalues to the NS or Euler reconnection dynamics.
- L12 forces $I$ to be a sub-object invariant, not an integral functional of $u$. That rules out the corpus's integral "categorical helicity" as a carrier of anything beyond $H$ [S ✓].

**What is missing.**
1. A rule that selects the tubes for a given flow. KAM tori exist only on open sets of data.
2. A proof that "tube persists until a singularity" holds for Euler. That is open in general, and this is where Euler's own open problem enters.
3. Any NS content. V2 cannot by itself say anything about NS regularity (L14).

**First step.** Rewrite, as a *proposal* (owner approval needed), the `helicity-physical.md` sentence "smooth evolution cannot alter the total helicity" so that it is scoped to Euler, and add L14 as the NS counterpoint. In Lean, D3 is not feasible without flow-map theory. A combinatorial lemma is feasible: "a link invariant is constant along an isotopy", stated for braid closures under Markov moves, already present via `thm:jones-markov-trace`.

### V3: helicity/Beltrami depletion [lower]

By D1, $\ker u^\flat$ is contact exactly where $h=u\cdot\omega\ne0$. Where $u\parallel\omega$ (Beltrami), the Lamb vector $u\times\omega$, and with it the non-gradient part of the nonlinearity, vanishes.
- The model's Reeb field realises this globally (rescue audit §5), giving a regular solution.
- "Beltramization suppresses blow-up" is [H]/[N]. No theorem gives regularity from relative helicity alone. Helicity is sign-indefinite and dissipated in NS (L11).

**Attachment.** The helicity blocks and the Reeb bundle. Any statement here points toward **regularity**, not obstruction.

**Possible conditional theorem [O].** A Serrin-type criterion on the Lamb vector $u\times\omega$. Whether one exists in the literature was **not checked** this session: an absence-of-search, not an absence-of-result.

### V4: universality and replicators [lowest]

Tao's program (L18) and CMPP (L17) suggest building, inside Euler/NS, a self-similar replicating "machine". The corpus's braid-gate picture is suggestive, but:
- no construction exists;
- CMPP's flows are steady and need chosen metrics;
- the Hecke "gate" has no derivation from the NS nonlinearity.

Recorded for completeness. Do not pursue without a concrete Euler-level construction.

---

## 4. Decisions this raises for the owner (framed per AGENTS.md)

**Q1. Re-scope the Levi chain to the vorticity plane field (V1)?**
- **What it means.** `core-levi-form` and `levi-degeneracy-conjecture` would refer to $\eta_\omega=\omega^\perp$ of the classical flow, not to $\ker\varTheta$. Branch (A) ("bounded Levi ⇒ blow-up") would be withdrawn as contradicting Beirão da Veiga–Berselli, and replaced by the necessary condition of §3 V1.
- **Cost.** About 4 blocks (`core-levi-form`, `levi-degeneracy-conjecture`, `townsend-biot-savart-strain`, `crow-approach-amplification`), their `.lean` siblings (`core_levi_form.lean`, `levi_growth_trichotomy.lean`, `levi_pair_channel_branch_b.lean`), and one probe.
- **Risk.** The narrative "QOU argues for blow-up" loses its geometric leg. The comparison point is unaffected, because there is none: NS has no experimental comparison here.
- **What it commits to.** The chapter's geometric claim becomes a literature-consistent necessary condition, not a blow-up argument.
- **Default if nothing is chosen.** Nothing changes. The chain keeps the internal sign conflict of rescue audit §1b, and branch (A) stays in tension with L5.
- **Recommendation (judgement).** Take Q1. It is the only reformulation found that keeps the Levi machinery and makes it say something true.

**Q2. Scope the vortex-topology claims to Euler (V2)?**
- **What it means.** The blocks `helicity-physical` ("smooth evolution cannot alter…"), `vortex-reconnection` ("regularises the classical reconnection singularity") and `helicity-conservation` item 3 (the "trefoil has zero helicity" sentence) would state Euler scope, cite Enciso–Lucà–Peralta-Salas 2017 for NS, and rewrite the trefoil sentence as a framing statement.
- **Cost.** 3 blocks of prose, plus 3 new `references.ts` entries (ELP-S 2017, EPT 2016, Constantin–Fefferman 1993).
- **Risk.** Low. These are corrections to match theorems.
- **Default if nothing is chosen.** Three sentences that are false for NS stay in the chapter.
- **Recommendation (judgement).** Take Q2. It is mechanical once approved, and per §🟥 ASK it waits for approval.

---

## 5. Not established here (absence-of-evidence notes)

- **Tao's averaged nonlinearity.** Whether it preserves Kelvin circulation, helicity or a vorticity transport law is unverified (WebFetch was DNS-blocked). If it preserves them, V2 and V3 sit *inside* Tao's barrier, and only finer structure such as V1's direction geometry escapes it.
- **Lamb-vector regularity criterion.** Whether one exists was not searched.
- **KNSS and CSTY citations (L9).** Recalled, not re-verified this session.
- **Vocabulary-shifted prior work.** `corpus_search` (MCP) was down, so the corpus-grep negative is lexical only.
- **The forced case.** Not addressed. The unverified 2026 "forced blow-up" report surfaced in search results and is **not** relied on.
