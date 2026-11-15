# The Navier–Stokes singularity chain after the retraction of `thm:qu-to-qou` item 3

**Date:** 2026-10-12. **Bean:** `qou-507c` (owner-directed; parent epic `qou-vo9t`).
**Branch:** `ns-followup`, based on `claude/bold-gates-00l1bl` at `de9179ac2`.

**Inputs.** These are cited, not re-derived:
- The restatement of `thm:qu-to-qou` in `bc60f24b9`, in `lifting-and-descent/qu-to-qou.md:8-9`.
  - Item 2: $\kappa_0 = c_1(\xi) = e(\xi) \in H^2(\mathcal S,\mathbb Z)$, equal to $\chi(\mathcal S)$ for the unit tangent bundle.
  - Item 3: $\xi$ has an $n$-th root iff $n \mid \chi$. The obstruction is $\chi \bmod n \in H^2(\mathcal S,\mu_n)\cong\mathbb Z/n$.
- `docs/audits/2026-10-12-jet-tower-band-construction.md`.
- `docs/audits/2026-10-12-atiyah-jet-classes-bring.md`.

Paths below are relative to `folio/quantum-observable-universe/` unless absolute.

**Tags.** Every claim carries one tag:
- **[D]** derived here;
- **[S]** standard, cited;
- **[A]** asserted in the corpus with no derivation;
- **[O]** open.

---

## 0. Overall verdict

**The end conclusion does not survive in any form the chain supports.** Three forms are claimed:
- "the Descartes universe is NS-singular";
- $\mathrm{Obs}_\partial(A)=0$;
- $\kappa_n|_\Sigma\neq0$ for all $n$.

None of the three is established, and two of the three are **false as literally written**. The scope-(b) invariant for those two is that a 1-dimensional space has cohomological dimension at most 1.

What survives consists of true topological facts about the Reeb bundle of a genus-4 surface. None of them says anything about the collision locus $\Sigma$, and none says anything about Navier–Stokes regularity:

1. $c_1(\xi) = -6$, so $\xi$ has no nowhere-vanishing section. [S] (Poincaré–Hopf.)
2. **Kummer persistence**, item 3 as restated. $\xi$ has an $n$-th root iff $n\mid 6$. The class $c_1(\xi)\bmod n\in H^2(\mathcal S,\mu_n)\cong\mathbb Z/n$ is non-zero for every $n\notin\{1,2,3,6\}$. [S]/[D], see §2.
3. **Local cohomology at a point.** $H^2_{\{p\}}(\mathcal S,\mathbb Z)\cong H^2(D^2,S^1;\mathbb Z)\cong\mathbb Z$ for every $p$. The map $H^2_{\{p\}}\to H^2(\mathcal S)$ is an isomorphism, so $e(\xi)$ localises at any point. [S]/[D], see §3.3.

The step that carried the chain from these facts to "NS-singular" had three parts:
- the complementary-subgroup non-cancellation of item 3;
- a restriction of a degree-2 class to the 1-dimensional $\Sigma$;
- the identification of a pointwise jet divergence with a cohomology class.

The first is retracted. The second is identically zero. The third is a category error: the class it names is zero.

**Recommendation (my judgement, not a finding).** The owner should decide whether to demote `thm:ns-singularity-descartes` from `theorem` to `conjecture`, or to restate it as the topological facts 1–3 with no NS verdict. Both moves change a block's kind, so they wait on the owner. I have added scope notes and nothing else. **Default if the owner does nothing:** every block keeps its current kind and carries scope notes saying the verdict is not established.

---

## 1. Verdict table

**(i)** survives as stated. **(ii)** survives via the Kummer form. **(iii)** cannot be supported: (a) = not established; (b) = excluded by a cited invariant.

| # | Block : line | Step / claim | Verdict | Why (tag) |
|---|---|---|---|---|
| 1 | `fluid-dynamics/ns-obstruction-tower.md:32` | (a) $\kappa_0=e(\xi)$, $\mathrm{tr}\,\kappa_0=\chi$ | **(i)** | This is item 2 as restated. [S] |
| 2 | `ns-obstruction-tower.md:34-47` | (a) $\kappa_n=\kappa_0+\delta_n$ with $\delta_n\in\mathrm{im}\,H^2(\mathcal S,\mathcal O)$; complementary subgroups; $\kappa_n\ne0$ for all $n$ | **(iii-b)** for $\delta_n\ne0$, **(iii-a)** for the rest | $H^2(\mathcal S,\mathcal O_{\mathcal S})=0$ on a compact Riemann surface (dimension) [S], so $\delta_n=0$ by the block's own definition. $\kappa_n=\kappa_0$, which is non-zero in $H^2(\mathbb Z)$. For the bands $\mathcal O^\times$ and $\mathbb G_m$ the group $H^2$ is 0, so $\kappa_n=0$ there. The non-vanishing therefore depends on which band is meant, and the chain never fixes it. The existing Scope note (`:49`) is correct. |
| 3 | `ns-obstruction-tower.md:12-26` | Statement: $\mathrm{Obs}_\partial=\ker(\oplus H^2(\mathcal S)\to\oplus H^2(\Sigma))$; NS-singular iff $\mathrm{res}_\Sigma\kappa_n\ne0$ for some $n$ | **(iii-b), degenerate** | $\Sigma$ is a line segment (`:53`), so $H^2(\Sigma,\mathcal F)=0$ for every sheaf $\mathcal F$: a paracompact space of covering dimension 1 has cohomological dimension $\le 1$ (Godement, *Topologie algébrique et théorie des faisceaux*, II.5.12) [S]. Hence $\mathrm{res}_\Sigma\equiv0$ and $\mathrm{Obs}_\partial$ is the whole sum. Read literally, the criterion returns **NS-regular for every QOU** and cannot discriminate. [D] |
| 4 | `ns-obstruction-tower.md:53-67` | (b) LES of $(\mathcal S,\mathcal S\setminus\Sigma)$; "$\kappa_n\vert_\Sigma\ne0$ iff local-cohomology support at $\Sigma$" | **(iii-b)** | The displayed sequence restricts to $\mathcal S\setminus\Sigma$, not to $\Sigma$. Two different maps are identified. The left side of the "iff" is identically false (row 3). [D] |
| 5 | `ns-obstruction-tower.md:69-87` | (c) $H^1_{\mathfrak m_p}(A)=V_{1/2}\oplus V_{1/2}$ | **(iii-a)** | No derivation is given. The degree is $H^1$, while the obstruction lives in degree 2. Not used by the Kummer form. [A] |
| 6 | `ns-obstruction-tower.md:89-103` | (d) local cohomology $\ne0$ iff Levi non-degenerate | **(iii-a)** | Conditional on `prop:core-levi-form`. Independent of item 3, but it feeds a class that row 3 shows is 0. [A] |
| 7 | `ns-obstruction-tower.md:107-119` | (e) $\kappa_n\vert_\Sigma=\mathrm{lk}\cdot e(\xi)\vert_\Sigma+\delta_n\vert_\Sigma$; "$e(\xi)\vert_\Sigma\ne0$ when $\Sigma$ is homologically non-trivial" | **(iii-b)** | Both sides lie in $H^2(\Sigma)=0$. A 1-cycle's homology class does not make a degree-2 class restrict non-trivially. [D] |
| 8 | `fluid-dynamics/ns-obstruction-computation.md:16` | (a) $e(\xi)=-6\in H^2(\Sigma_4,\mathbb Z)\cong\mathbb Z$ | **(i)** | [S] |
| 9 | `ns-obstruction-computation.md:18` | $e(\xi)\vert_\Sigma=0$ | **(i)** | Correct, and it concedes row 3. [S] |
| 10 | `ns-obstruction-computation.md:20-30` | $H^2_{\{p\}}(\Sigma_4,\mathbb Z)\cong H^2(D^2,S^1)\cong\mathbb Z$ | **(i)** | Excision. [S] |
| 11 | `ns-obstruction-computation.md:32-36` | $e(\xi)\vert_p=-6\cdot\deg_p(\xi)$; a Reeb zero is forced at a collision point | **(iii)**: formula **(b)**, forcing **(a)** | See §3.3. The localisation is $\mathrm{ind}_p(s)$ for a chosen section $s$, and $\sum_p\mathrm{ind}_p(s)=-6$. The factor $-6\cdot\deg_p$ is wrong. Topology forces zeros of $s$ to exist but not to lie on $\Sigma$, because any finite zero set can be isotoped off $\Sigma$ [S]. Whether the model's Reeb field vanishes on $\Sigma$ is a dynamical question. [O] |
| 12 | `ns-obstruction-computation.md:38-52` | (b) $\delta_n\vert_\Sigma\ne0$ because $\vert j^nv\vert\to\infty$ | **(iii-b)** for the class, **(iii-a)** for the divergence | $\delta_n$ lies in the image of $H^2(\mathcal S,\mathcal O)=0$ (`ns-obstruction-tower.md:41-44`), so $\delta_n=0$ whatever the jets do. A pointwise norm of a velocity jet is not a cohomology class. The rate $(T^*-t)^{-(n+1)/2}$ assumes the self-similar collapse $d\sim(T^*-t)^{1/2}$, i.e. it assumes the blow-up it is used to prove. [A] |
| 13 | `ns-obstruction-computation.md:54-78` | (c), (d): complementary subgroups; $\kappa_n\vert_\Sigma\ne0$ for all $n$; $\mathrm{Obs}_\partial=0$; NS-singular | **(iii-b)** | This cites retracted item 3 (`:61`), and both summands are 0 (rows 9 and 12). The block had **no** scope note before this audit; one is added. |
| 14 | `ns-obstruction-computation-interpretation.md:1` | "Novelty … complementary subgroups … persists across all jet levels" | **(iii-b)** | Rests on rows 12–13. Left for owner decision (an interpretive remark). |
| 15 | `ns-obstruction-computation-asymptotic.md:1` | $\mathrm{ord}_\omega$ of the jet divergence | **(i)** as bookkeeping | Restates row 12's asymptotic, which is conditional on the collapse ansatz. |
| 16 | `fluid-dynamics/ns-kummer-specialisation.md:1,13-26` | Statement: $\kappa_0\in H^2(\mathcal S,\mathbb G_m)$; class in $H^2(\mathbb G_m)/n$ | **(ii)**, group corrected | $H^2(\mathcal S,\mathcal O^\times)=0$ on a closed surface: $H^2(\mathcal O)=0\to H^2(\mathcal O^\times)\to H^3(\mathbb Z)=0$ [S]. As written, the block asserts a non-zero class in the zero group. The Kummer sequence must be read one degree lower; see §2. **Edited.** |
| 17 | `ns-kummer-specialisation.md:45-55` | (a) $\kappa_0\bmod n=0$ iff $n\mid\chi$; vanishing exactly for $n\in\{1,2,3,6\}$ | **(ii)** | True in $H^2(\mathcal S,\mu_n)\cong\mathbb Z/n$, which is the group the proof actually computes in. [S]/[D] |
| 18 | `ns-kummer-specialisation.md:57-67` | (b) the root of unity $q=e^{i\pi/\kappa}$ "is" Kummer level $n=2\kappa$ | **(iii-a)** for the identification, **(i)** for the arithmetic | The identification of the substrate's root-of-unity order with the root-extraction level of $\xi$ is asserted, not derived [A]. The arithmetic $2\kappa\nmid6\iff\kappa\notin\{1,3\}$ is correct. $\kappa=2$ also persists, so "$\kappa\ge4$" understates the set. Note also that $\kappa$ here collides with the aspect ratio $\kappa(p)$ and with $\kappa_n$. |
| 19 | `ns-kummer-specialisation.md:69-78` | (c) persistence as $\kappa\to\infty$ | **(ii)** | True arithmetic, conditional on row 18 for its $q\to1$ reading. |
| 20 | `ns-kummer-specialisation.md:35-41` | Genericity caveat | **(i)** | Correct and pre-existing. It already says persistence is cheap and is not evidence of a regularity criterion. |
| 21 | `ns-kummer-specialisation-consequence.md:1-3` | "$\chi=-6$ ⇒ NS-singular, $\mathrm{Obs}_\partial=0$, classical NS permits finite-time blowup", via complementary summands of $H^2(\mathcal S,\mathbb G_m)$ | **(iii-b)** | Cites retracted item 3. The group is 0 (row 16) and $e(\xi)\vert_\Sigma=0$ (row 9). The classical claim contradicts the explicit disclaimer in `ns-singularity-descartes.md:12`. **Re-scoped.** |
| 22 | `fluid-dynamics/ns-singularity-descartes.md:5-12` | $\mathrm{NS}(A)=e(\xi)\vert_\Sigma\ne0$, "unconditional" | **(iii-b)** | The middle term is 0 (rows 3 and 9). There is also a degree mismatch with `def:ns-obstruction` (`ns-obstruction.md:5`), which places $\mathrm{NS}(A)$ in $H^3_{\mathrm{loc}}$. **Scope note added; kind change left to the owner.** |
| 23 | `ns-singularity-descartes-proof.md:6-12` | Step 1: $\kappa_0\bmod2\kappa\ne0$ for $\kappa\ge4$ | **(ii)** | True in $H^2(\mathcal S,\mu_{2\kappa})\cong\mathbb Z/2\kappa$, as the global class. It is not a statement about $\Sigma$. Corrected wording. |
| 24 | `ns-singularity-descartes-proof.md:14-23` | Step 2: complementary subgroups | **(iii-b)** | Retracted. Moreover $\kappa_0\vert_\Sigma=0$, so there is no non-zero term to protect. Scope note extended. |
| 25 | `ns-singularity-descartes-proof.md:25-29` | Step 3: $\mathrm{NS}(A)\ne0$ ⇒ Levi non-degenerate | **(iii-a)** | Its premise is not established (row 22). Conditional on `prop:core-levi-form`. |
| 26 | `ns-singularity-descartes-proof.md:31-36` | Step 4: Levi ⇒ vorticity bound ⇒ BKM | **(iii-a)** | Conditional implications whose premise is unestablished. The links themselves were not re-audited here. |
| 27 | `ns-singularity-descartes-interpretation.md:1` | "four conditional inputs … dictates finite-time blowup" | **(iii-a)** | Two of the four inputs fail (rows 22, 24). Left for owner decision. |
| 28 | `fluid-dynamics/substrate-gm-torsion.md:53-71` | $\kappa_n\in H^2(\mathcal S,\mathbb G_m)$; the motivic theorem makes it "categorically" non-collapsing | **(ii)** after a group correction | Same group error as row 16. **Scope note added.** |
| 29 | `appendix-surreals/q-bsd-classical-limit.md:26-35` | $\kappa_0\in H^2(\mathcal S,\mathbb G_m)$ not $n$-divisible | **(ii)** after a group correction | Same as row 16. **Scope note added.** |
| 30 | `fluid-dynamics/torus-ns-regular.md:8-14` | $\chi=0$ ⇒ $\kappa_0\bmod n=0$ for all $n$; $\mathrm{NS}(A)=\kappa_0\vert_\Sigma=0$ | **(i)**, but vacuous | Both claims are true. The second holds for **every** genus because $H^2(\Sigma)=0$, so the torus/Bring contrast it is meant to draw does not come from the $\Sigma$-restriction. Not edited. |
| 31 | `fluid-dynamics/observability-independent-motivation.md:1` | "strictly deduces classical Navier–Stokes blowup" | **(iii-a)**, pre-existing overclaim | Contradicts `ns-singularity-descartes.md:12`, independently of item 3. Not edited (outside this bean's citation-correction scope); listed for the owner. |
| 32 | `lifting-and-descent/motivic-perpetual-obstruction.md:11` | non-vanishing "in $H^2(\mathcal S,\mathbb G_m)$" via HKR | **(iii-b)** for that clause | Zero group (row 16). Upstream of the chain, cited at `ns-obstruction-tower.md:47`. Not edited here (owned by the qu-to-qou arc); flagged. |
| 33 | `climax-volume-mass/vertex-algebra-relations.md:475-477` | C-5 "complementary subgroups" | **(iii)** | Already carries a correct scope note (`:477`). No change. |

---

## 2. The corrected Kummer argument (verdict ii), in full

**Setting.** $\mathcal S=\Sigma_4$, Bring's surface, is a compact Riemann surface of genus 4. $\xi$ is the Reeb bundle, which the restated item 2 identifies with the unit tangent bundle, so $\deg\xi=c_1(\xi)=\chi=-6$.

**What $\kappa_0$ denotes.** Either of two equivalent classes:
- the isomorphism class $[\xi]\in H^1(\mathcal S,\mathcal O^\times)=\mathrm{Pic}(\mathcal S)$, holomorphically, or $[\xi]\in H^1(\mathcal S,\underline{\mathrm U(1)})$, smoothly;
- its image $c_1(\xi)\in H^2(\mathcal S,\mathbb Z)\cong\mathbb Z$.

It is **not** a class in $H^2(\mathcal S,\mathbb G_m)$, which is zero. [S]

**The sequence.** The Kummer sequence $1\to\mu_n\to\mathcal O^\times\xrightarrow{(\cdot)^n}\mathcal O^\times\to1$ is exact as a sequence of analytic sheaves, because $n$-th roots exist locally. Its cohomology sequence reads

$$
H^1(\mathcal S,\mathcal O^\times)\xrightarrow{\ \cdot n\ }H^1(\mathcal S,\mathcal O^\times)\xrightarrow{\ \partial_n\ }H^2(\mathcal S,\mu_n)\to H^2(\mathcal S,\mathcal O^\times)=0 .
$$

**Computation.**
- $\mathrm{Pic}(\mathcal S)\cong\mathrm{Pic}^0\times\mathbb Z$.
- $\mathrm{Pic}^0$ is a complex torus and hence divisible.
- Therefore $\mathrm{coker}(\cdot n)\cong\mathbb Z/n$, the map being $\deg\bmod n$.
- Exactness and $H^2(\mathcal O^\times)=0$ make $\partial_n$ surjective with kernel $n\,\mathrm{Pic}$, so $H^2(\mathcal S,\mu_n)\cong\mathbb Z/n$.

This matches $H^2(\Sigma_g;\mathbb Z/n)\cong\mathbb Z/n$. [S]

The same holds for smooth $\mathrm U(1)$-bundles, with $\mathrm{Pic}$ replaced by $H^2(\mathcal S,\mathbb Z)$. Here $\partial_n$ is reduction mod $n$, which is item 3 exactly.

**Conclusion.** $\xi$ admits an $n$-th root iff $\partial_n[\xi]=0$ iff $n\mid c_1(\xi)=-6$ iff $n\in\{1,2,3,6\}$. For all other $n$, $\partial_n[\xi]=(-6\bmod n)\ne0$. [D]

**What this does not give.** It is a statement about the **global** class on $\mathcal S$. Its restriction to $\Sigma$ lies in $H^2(\Sigma,\mu_n)=0$. Kummer persistence therefore cannot by itself produce a non-zero class "at the collision locus". It also carries no Navier–Stokes content: the genericity caveat already in the block (row 20) says so.

**Selection-against-target check.** The original statement moved $\kappa_0$ into $H^2(\mathcal S,\mathbb G_m)$ so that it could be "not $n$-divisible". The corrected group $H^2(\mathcal S,\mu_n)$ is the target of the connecting map that the chain's own Kummer sequence induces from the object the chain actually uses (the class of $\xi$). No new group is chosen to make the claim true. The corrected claim is weaker than the original: global, not on $\Sigma$.

---

## 3. The three structural facts that decide the chain

### 3.1 $H^2(\mathcal S,\mathcal O_{\mathcal S})=0$ ⇒ $\delta_n=0$
$\mathcal S$ is a complex curve, so the Dolbeault complex stops at degree 1. [S] The tower block defines $\delta_n$ as lying in the image of this group (`ns-obstruction-tower.md:41-44`). Hence $\delta_n=0$ for every $n$, whatever the jets of $v$ do.

The `atiyah-jet-classes-bring` audit shows that the jet-extension classes which **do** depend on $n$ live in degree 1 ($\propto 3n(n-3)$, vanishing at $n=3$). They are not candidates for $\delta_n$ either.

### 3.2 $\dim\Sigma=1$ ⇒ $H^2(\Sigma,\cdot)=0$
A segment, and indeed any paracompact space of covering dimension 1, has sheaf-cohomological dimension $\le1$. [S] Every restriction $H^2(\mathcal S,\mathcal F)\to H^2(\Sigma,\mathcal F|_\Sigma)$ is therefore zero. This holds for $\mathbb Z$, $\mu_n$, $\mathcal O^\times$ and any other sheaf. It kills:
- the tower block's criterion (rows 3, 4, 7);
- the descartes statement (row 22);
- any Kummer-form substitute "on $\Sigma$".

### 3.3 The local-cohomology substitute: $H^2_{\{p\}}=\mathbb Z$, but the local class is not determined by $\xi$
**The local group.** Excision gives $H^2_{\{p\}}(\mathcal S,\mathbb Z)\cong H^2(D^2,S^1)\cong\mathbb Z$. [S]

**The map to $H^2(\mathcal S)$.** In the sequence
$H^1(\mathcal S)\to H^1(\mathcal S\setminus p)\to H^2_{\{p\}}(\mathcal S)\to H^2(\mathcal S)\to H^2(\mathcal S\setminus p)=0$,
the first map is an isomorphism ($\mathbb Z^{8}$ on both sides for $g=4$). So $H^2_{\{p\}}\to H^2(\mathcal S)$ is an isomorphism. [D]

**Consequence.** The Euler class localises at **every** point. A section $s$ of $\xi$ with isolated zeros gives the refinement $e(\xi)=\sum_{p\in Z(s)}\mathrm{ind}_p(s)$ with $\sum\mathrm{ind}_p(s)=-6$ (Poincaré–Hopf). [S]

The local class at a given $p$ is therefore a property of the **section**, not of $\xi$. The formula $e(\xi)|_p=-6\cdot\deg_p(\xi)$ (`ns-obstruction-computation.md:33`) is incorrect: it multiplies the global degree by a local index.

**No forced zero on Σ.** Topology forces $Z(s)\ne\varnothing$, but a diffeomorphism isotopic to the identity moves any finite set off $\Sigma$. [S] So "$\chi=-6$ forces a Reeb zero on $\Sigma$" is **excluded as a topological consequence** (scope b). Whether the model's actual Reeb field vanishes on $\Sigma$ is open (scope a).

---

## 4. Edits made on this branch (citation corrections and re-scopes only)

| File | Change |
|---|---|
| `fluid-dynamics/ns-kummer-specialisation.md` | The statement's group is corrected from $H^2(\mathcal S,\mathbb G_m)/n$ (which is 0) to the connecting map $H^1(\mathcal S,\mathbb G_m)\to H^2(\mathcal S,\mu_n)\cong\mathbb Z/n$, derived from item 3 as restated. A sentence marks the root-of-unity/level identification in (b) as asserted. |
| `fluid-dynamics/ns-kummer-specialisation-consequence.md` | Scope note: retracted citation, zero group, $e(\xi)\vert_\Sigma=0$; the verdict is not established. |
| `fluid-dynamics/ns-obstruction-tower.md` | Scope note after (b): $H^2(\Sigma,\cdot)=0$, so the criterion is degenerate; (e) is $0=0+0$. |
| `fluid-dynamics/ns-obstruction-computation.md` | Scope note after (c), covering $\delta_n=0$, the incorrect local formula, and the retracted item 3. |
| `fluid-dynamics/ns-singularity-descartes.md` | Scope note: the displayed non-vanishing is not established; restriction to $\Sigma$ is zero. |
| `fluid-dynamics/ns-singularity-descartes-proof.md` | Step 1 is stated in $H^2(\mathcal S,\mu_{2\kappa})$ as a global class. The Step 2 scope note is extended. A scope sentence says Steps 3–4 are conditional on an unestablished premise. |
| `fluid-dynamics/substrate-gm-torsion.md` | Scope note on the $H^2(\mathcal S,\mathbb G_m)$ placement. |
| `appendix-surreals/q-bsd-classical-limit.md` | Scope note on the $H^2(\mathcal S,\mathbb G_m)$ placement. |

No block kind, `uses[]`, Lean file, numerical finding or witness was changed. No statement was deleted.

## 5. Decisions left to the owner

Not raised as questions; framed here for the owner's schedule.

1. **The kind of `thm:ns-singularity-descartes`.**
   - **(A) Demote to `conjecture`.** One `.ts` kind field and the banner change. Its consumers become conjecture-downstream: `torus-ns-regular`, `leray-profile`, `observability-independent-motivation`, the interpretation remark, and `ns-kummer-specialisation` (which lists it in `uses[]`). Under §3b they would need conditional-class treatment or demotion.
   - **(B) Restate it as the true topological facts of §0.** This drops the NS verdict entirely.
   - **(C) No-op.** The theorem kind stays, carrying a scope note saying its displayed claim is not established.
   - *Recommendation (judgement):* **(B)**. Row 22 is false as literally written, not merely unproved, so a conjecture banner over it would also be wrong.
2. **The two interpretive remarks** (rows 14, 27) and `observability-independent-motivation` (row 31) still advertise the retracted mechanism or a classical blow-up. Rewriting interpretive prose is not a citation correction, so it is left.
3. **The `thm:motivic-perpetual-obstruction` sketch** (row 32) places a non-vanishing class in the zero group. That is upstream of this chain and belongs to the qu-to-qou arc.
